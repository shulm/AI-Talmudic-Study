"""Evaluator-only metrics, conditional numerical margins and exact world inference."""
from common import *
from scipy.stats import binomtest,beta

def loss(p,o):return -(o*np.log(np.maximum(p,1e-12))).sum(-1)
def contrast_logs(l):
    x=np.stack([l[:,:,0]-l[:,:,1],l[:,:,0]-l[:,:,2],l[:,:,1]-l[:,:,2]],-1);x=x[::2]-x[1::2]
    return x-x[:,:1]
def contrast(p):return contrast_logs(np.log(np.maximum(p,1e-12)))
def measures(p,y,o):
    return dict(expected_nll=float(loss(p,o).mean()),sampled_nll=float(-np.log(np.maximum(np.take_along_axis(p,y[...,None],-1)[...,0],1e-12)).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))
def summary(x,world=False):
    x=np.asarray(x);q=[0,.5,.1,.9,1] if world else [0,.5,.9,.95,.99,1]
    names=['min','median','q10','q90','max'] if world else ['min','median','q90','q95','q99','max']
    out=dict(zip(names,np.quantile(x,q,method='linear').tolist()));out['mean']=float(x.mean())
    if world:out.update(sample_std=float(x.std(ddof=1)) if len(x)>1 else None,values=x.tolist())
    return out
def classify(margins,positive_gap):
    status={k:('PASS' if v[0]>=0 else ('FAIL' if v[1]<0 else 'UNRESOLVED')) for k,v in margins.items()}
    if not positive_gap:status['recovery']='UNRESOLVED'
    joint='FAIL' if 'FAIL' in status.values() else ('PASS' if all(s=='PASS' for s in status.values()) else 'NUMERICALLY_UNRESOLVED')
    return dict(gates=status,joint=joint)
def gate(cell):
    B,U,O,D,M= [cell[k] for k in ('B','U','O','D','M')]
    require(D>0 and np.isfinite(list(cell.values())).all(),'Invalid reference or nonfinite endpoint')
    margins=dict(gain=[cell['Blo']-cell['Uhi']-.05,cell['Bhi']-cell['Ulo']-.05],recovery=[.5*cell['Blo']-cell['Uhi']+.5*O,.5*cell['Bhi']-cell['Ulo']+.5*O],contrast=[.25*D-cell['Mhi'],.25*D-cell['Mlo']],inactive=[.01+cell['IBlo']-cell['IUhi'],.01+cell['IBhi']-cell['IUlo']])
    values=dict(gain=B-U,recovery=(B-U)/(B-O) if B-O>0 else None,contrast=float(np.sqrt(M/D)),inactive=cell['IU']-cell['IB'])
    return dict(values=values,margins=margins,positive_gap=cell['Blo']-O>0,**classify(margins,cell['Blo']-O>0))
def score(pred,ev,enclosures,evidence):
    rows=[];cells={};weight_rows={}
    for h in HIST:
        cell={}
        for active in (True,False):
            ix=ev['active']==active;o=ev['oracle'][ix];y=ev['y'][ix];truth=contrast(o);b=pred[h+'_B3'][ix]
            for m in METHODS:
                p=pred[h+'_'+m][ix];met=measures(p,y,o);ex=(loss(p,o)-loss(b,o)).mean(1);con=contrast(p)
                row=dict(history=h,stratum='active' if active else 'inactive',method=m,metrics=met,oracle_loss=float(loss(o,o).mean()),contrast_mse=float(((con-truth)**2).mean()),contrast_den=float((truth**2).mean()),contrast_rms=float(np.sqrt((con**2).mean())),per_person_excess=ex.tolist(),positive_part_excess=float(np.maximum(ex,0).mean()),excess_tails=summary(ex),donor_metrics=measures(pred[h+'_'+m+'_donor'][ix],y,o))
                row['own_minus_donor']={k:met[k]-row['donor_metrics'][k] for k in met}
                row['minus_uncapped']={k:met[k]-measures(pred[h+'_ES_UNCAPPED'][ix],y,o)[k] for k in met};rows.append(row)
            for name,short in [('B3','B'),('ES_UNCAPPED','U')]:
                lo=enclosures[h+'_'+name+'_lower'][ix];hi=enclosures[h+'_'+name+'_upper'][ix]
                prefix='' if active else 'I';cell[prefix+short]=float(loss(pred[h+'_'+name][ix],o).mean());cell[prefix+short+'lo']=float(-(o*hi).sum(-1).mean());cell[prefix+short+'hi']=float(-(o*lo).sum(-1).mean())
            if active:
                p=pred[h+'_ES_UNCAPPED'][ix];logp=np.log(np.maximum(p,1e-12));err=contrast(p)-truth
                eps=np.maximum(abs(enclosures[h+'_ES_UNCAPPED_lower'][ix]-logp),abs(enclosures[h+'_ES_UNCAPPED_upper'][ix]-logp))
                ce=np.stack([eps[:,:,0]+eps[:,:,1],eps[:,:,0]+eps[:,:,2],eps[:,:,1]+eps[:,:,2]],-1);ce=ce[::2]+ce[1::2];ce=ce+ce[:,:1]
                cell.update(O=float(loss(o,o).mean()),D=float((truth**2).mean()),M=float((err**2).mean()),Mlo=float((np.maximum(abs(err)-ce,0)**2).mean()),Mhi=float(((abs(err)+ce)**2).mean()))
            w=evidence[h+'_w'][ix];lb=evidence[h+'_log_beta'][ix];le=evidence[h+'_log_e'][ix]
            weight_rows[h+('_active' if active else '_inactive')]=dict(log_e=summary(le),evidence=summary(np.exp(le)),weight=summary(w),fraction_zero=float((w==0).mean()),fraction_above_point9=float((w>.9).mean()),beta_underflows=int((np.exp(lb)==0).sum()),finite_log_beta_range=[float(lb.min()),float(lb.max())])
        cells[h]=cell
    cells['aggregate']={k:float(np.mean([cells[h][k] for h in HIST])) for k in cells['H1']}
    gates={h:gate(c) for h,c in cells.items()}
    return dict(rows=rows,cells=cells,gates=gates,weights=weight_rows,both_histories_pass=all(gates[h]['joint']=='PASS' for h in HIST),aggregate_hides_failure=gates['aggregate']['joint']=='PASS' and any(gates[h]['joint']=='FAIL' for h in HIST),history_disagreement=gates['H1']['joint']!=gates['H2']['joint'])
def inference(statuses):
    require(len(statuses)==82,'All82 required; no partial inference')
    require(set(statuses)<={'PASS','FAIL','NUMERICALLY_UNRESOLVED'},'Unknown joint outcome')
    s=statuses.count('PASS');un=statuses.count('NUMERICALLY_UNRESOLVED')
    p=float(binomtest(s,82,.8,alternative='greater').pvalue);lower=0. if s==0 else float(beta.ppf(.05,s,83-s))
    return dict(n=82,successes=s,failures=statuses.count('FAIL'),unresolved=un,p_exact=p,one_sided_95_lower=lower,count_pass=s>=72,all_H1_resolved=un==0,statistical_and_resolution_pass=s>=72 and un==0)
