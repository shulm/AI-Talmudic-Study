"""Evaluator-only reporting; histories averaged as losses, never probabilities."""
from contracts import *

def loss(p,o):return -(o*np.log(np.maximum(p,1e-12))).sum(-1)
def contrast(p):
    l=np.log(np.maximum(p,1e-12));a=np.stack([l[:,:,0]-l[:,:,1],l[:,:,0]-l[:,:,2],l[:,:,1]-l[:,:,2]],-1)
    d=a[::2]-a[1::2];return d-d[:,:1]
def measures(p,y,o):
    return dict(expected_nll=float(loss(p,o).mean()),nll=float(-np.log(np.maximum(np.take_along_axis(p,y[...,None],-1)[...,0],1e-12)).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))

def score(pred,ev):
    rows=[]
    for h in HIST:
        for a in ('active','inactive'):
            ix=ev['active'] if a=='active' else ~ev['active'];o=ev['oracle'][ix];y=ev['y'][ix];truth=contrast(o)
            for m in OWN:
                p=pred[f'{h}_{m}'][ix];con=contrast(p);base=pred[f'{h}_B3'][ix]
                row=dict(id=f'{h}_{a}_{m}',history=h,stratum=a,method=m,metrics=measures(p,y,o),oracle_loss=float(loss(o,o).mean()),gain=float((loss(base,o)-loss(p,o)).mean()),gap=float((loss(base,o)-loss(o,o)).mean()),contrast_mse=float(((con-truth)**2).mean()),contrast_den=float((truth**2).mean()),contrast_square=float((con**2).mean()),per_person_excess=(loss(p,o)-loss(base,o)).mean(1).tolist(),positive_part_excess=float(np.maximum((loss(p,o)-loss(base,o)).mean(1),0).mean()))
                if m in METHODS:
                    row['donor']={k:float(v-row['metrics'][k]) for k,v in measures(pred[f'{h}_{m}_donor'][ix],y,o).items()}
                rows.append(row)
    def gate(rs,m):
        active=[x for x in rs if x['method']==m and x['stratum']=='active'];inactive=[x for x in rs if x['method']==m and x['stratum']=='inactive']
        mean=lambda xx,k:float(np.mean([x[k] for x in xx]))
        gap=mean(active,'gap');den=mean(active,'contrast_den')
        if gap<=0 or den<=0:raise ValueError('Nonpositive oracle denominator')
        values=dict(gain=mean(active,'gain'),recovery=mean(active,'gain')/gap,contrast=float(np.sqrt(mean(active,'contrast_mse')/den)),inactive=-mean(inactive,'gain'))
        margins=dict(gain=values['gain']-.05,recovery=values['recovery']-.5,contrast=.5-values['contrast'],inactive=.01-values['inactive'])
        if not np.isfinite(list(values.values())).all():raise ValueError('Nonfinite gate')
        return dict(values=values,margins=margins,passed={k:bool(v>=0) for k,v in margins.items()})
    gates={}
    for m in OWN:
        g=gate(rows,m);g['histories']={str(h):gate([x for x in rows if x['history']==h],m) for h in HIST}
        g['worst_history_margins']={k:min(x['margins'][k] for x in g['histories'].values()) for k in g['margins']};gates[m]=g
    aggregates=[]
    for a in ('active','inactive'):
        for m in OWN:
            rr=[r for r in rows if r['stratum']==a and r['method']==m]
            avg=lambda k:float(np.mean([r[k] for r in rr]))
            ag=dict(id=f'{a}_{m}',metrics={k:float(np.mean([r['metrics'][k] for r in rr])) for k in rr[0]['metrics']},inactive_contrast_rms=float(np.sqrt(avg('contrast_square'))),positive_part_excess=float(np.maximum(np.mean([r['per_person_excess'] for r in rr],axis=0),0).mean()),per_person_excess=np.mean([r['per_person_excess'] for r in rr],axis=0).tolist())
            if m in METHODS:ag['donor']={k:float(np.mean([r['donor'][k] for r in rr])) for k in rr[0]['donor']}
            aggregates.append(ag)
    return dict(rows=rows,aggregates=aggregates,gates=gates)

def evidence_summary(e,ev):
    def summary(x):return dict(min=float(x.min()),median=float(np.median(x)),mean=float(x.mean()),max=float(x.max()),q10=float(np.quantile(x,.1)),q90=float(np.quantile(x,.9)))
    rows=[];summaries={}
    for h in HIST:
        for p in range(48):rows.append(dict(id=f'{h}_{p+144}',history=h,person=p+144,active=bool(ev['active'][p]),log_e=float(e[f'{h}_log_e'][p]),evidence=float(np.exp(e[f'{h}_log_e'][p])),h=float(e[f'{h}_h'][p]),w=float(e[f'{h}_w'][p]),seed_log_e={str(s):float(e[f'{h}_{s}_log_e'][p]) for s in SEEDS},counts=e[f'{h}_{SEEDS[0]}_counts'][p].tolist()))
        for a in ('active','inactive'):
            ix=ev['active'] if a=='active' else ~ev['active'];w=e[f'{h}_w'][ix]
            summaries[f'{h}_{a}']=dict(evidence=summary(np.exp(e[f'{h}_log_e'][ix])),weight=summary(w),fraction_zero=float((w==0).mean()),fraction_cap=float((e[f'{h}_h'][ix]==np.log(10)).mean()))
    disagreement={}
    for a in ('active','inactive'):
        ix=ev['active'] if a=='active' else ~ev['active'];u=e['101_w'][ix];v=e['211_w'][ix]
        disagreement[a]=dict(absolute_weight_difference=summary(abs(u-v)),zero_disagreement=float(((u==0)!=(v==0)).mean()),all_weight_differences=(u-v).tolist())
    return dict(rows=rows,summaries=summaries,history_disagreement=disagreement)

def bootstrap_cells(p,ev):
    o=ev['oracle'];cells={}
    for name,a,m1,m2 in [('active_gain',True,'B3','ES'),('inactive_degradation',False,'ES','B3'),('active_donor',True,'ES_donor','ES'),('active_ES_fixed',True,'ES','FIXED_MIX'),('inactive_ES_fixed',False,'ES','FIXED_MIX')]:
        ix=ev['active']==a
        cells[name]=np.mean([loss(p[f'{h}_{m1}'][ix],o[ix])-loss(p[f'{h}_{m2}'][ix],o[ix]) for h in HIST],axis=0)
    return cells

def bootstrap(p,ev):
    rng=np.random.Generator(np.random.PCG64(1702));out={k:rng.integers(0,12,(2000,12)) for k in ('active_pairs','inactive_pairs','query_groups')};summaries={}
    for k,c in bootstrap_cells(p,ev).items():
        block=c.reshape(12,2,12,3).mean((1,3));pp=out['active_pairs' if k.startswith('active_') else 'inactive_pairs'];qq=out['query_groups']
        val=block[pp[:,:,None],qq[:,None,:]].mean((1,2));out[k]=val
        summaries[k]=dict(point=float(c.mean()),interval95=np.quantile(val,[.025,.975],method='linear').tolist())
    return out,summaries

def numerical_summary(pred,num,ev):
    comparisons={}
    for n in (1,7):
        for m in HEADS+('M1','FIXED_MIX','ES'):
            p=num[f'{n}_{m}'];ref=pred[f'101_{m}'][:1]
            comparisons[f'{n}_{m}']=dict(probability_max=float(abs(p-ref).max()),expected_nll_difference=float(abs(loss(p,ev['oracle'][:1]).mean()-loss(ref,ev['oracle'][:1]).mean())))
    return dict(comparisons=comparisons,passed=all(x['probability_max']<=1e-6 and x['expected_nll_difference']<=1e-5 for x in comparisons.values()))
