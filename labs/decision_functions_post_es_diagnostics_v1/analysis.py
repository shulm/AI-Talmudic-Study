"""Exactly one exposed cap-removal arm and analytic optimization-error enclosures."""
from common import *
from scipy.special import logsumexp
def uncapped(p,e):
    le=e;h=np.zeros_like(le);positive=le>0;h[positive]=.009*np.expm1(le[positive])
    if not np.isfinite(h).all():raise FloatingPointError('Unrepresentable uncapped h')
    logb=-h;logw=np.full_like(h,-np.inf);logw[positive]=np.log(-np.expm1(-h[positive]));w=-np.expm1(-h)
    lp=np.logaddexp(logb[:,None,None]+np.log(p['B3']),logw[:,None,None]+np.log(p['M1']));new=np.exp(lp);new[h==0]=p['B3'][h==0]
    cap=h>np.log(10);delta=float(np.max(abs(new[~cap]-p['ES'][~cap]),initial=0))
    if delta>1e-12:raise ValueError('Cap-inactive mismatch')
    new[~cap]=p['ES'][~cap]
    if np.max(abs(new.sum(-1)-1))>1e-12 or not np.isfinite(new).all():raise ValueError('Invalid ablation probability')
    return new,dict(h=h,log_beta=logb,log_weight=logw,weight=w,baseline_underflow=np.exp(logb)==0,cap_changed=cap),delta
def loss(p,o):return -np.einsum('pqc,pqc->pq',o,np.log(np.maximum(p,1e-12)))
def contrast(p):
    logs=np.log(np.maximum(p,1e-12));odds=logs[:,:,[0,0,1]]-logs[:,:,[1,2,2]];paired=odds[::2]-odds[1::2];return paired-paired[:,:1]
def measures(p,y,o):
    return dict(expected_nll=float(loss(p,o).mean()),sampled_nll=float(-np.log(np.maximum(p[np.arange(len(p))[:,None],np.arange(p.shape[1])[None],y],1e-12)).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))
def mixture_error(arm,old,coef,eps):
    b=old['B3'];seeds=[old[f'M1_{s}'] for s in SEEDS];loge=[np.log(b)]+[np.log(p) for p in seeds];ee=[eps['B3']]+[eps[f'M1_{s}'] for s in SEEDS]
    n=len(b)
    if arm=='B3':weights=np.column_stack([np.zeros(n),np.full((n,3),-np.inf)])
    elif arm=='M1':weights=np.column_stack([np.full(n,-np.inf),np.full((n,3),-np.log(3))])
    elif arm=='FIXED_MIX':weights=np.tile([np.log(.1)]+[np.log(.3)]*3,(n,1))
    else:
        h=coef['h'] if arm=='ES_UNCAPPED' else np.minimum(coef['h'],np.log(10));lw=np.full(n,-np.inf);ix=h>0;lw[ix]=np.log(-np.expm1(-h[ix]));weights=np.column_stack([-h,lw[:,None]-np.log(3)+np.zeros((n,3))])
    logs=np.stack(loge);error=np.stack(ee)[:,:,:,None];w=weights.T[:,:,None,None]
    center=logsumexp(logs+w,axis=0);lower=logsumexp(logs+w-error,axis=0);upper=logsumexp(logs+w+error,axis=0)
    floor=np.log(1e-12);return np.maximum(abs(np.maximum(center,floor)-np.maximum(lower,floor)),abs(np.maximum(upper,floor)-np.maximum(center,floor)))
def contrast_error_bound(eps):
    # Sum eight signed log terms: two classes x two people x query/reference.
    odds=eps[:,:,[0,0,1]]+eps[:,:,[1,2,2]];pair=odds[::2]+odds[1::2];return pair+pair[:,:1]
def calculate(datasets,residual):
    rr={x['id']:x for x in residual['rows']};arrays={};coefficients={};rows=[];changed_active=0;unchanged_inactive=0;underflow=0
    for r in REAL:
        data=datasets[r];ev=data['evaluator'];o=ev['oracle'];y=ev['y']
        for h in HIST:
            old={m:data['predictions'][f'{h}_{m}'] for m in ('B3','M1','FIXED_MIX','ES')+tuple(f'M1_{s}' for s in SEEDS)}
            new,co,delta=uncapped(old,data['evidence'][f'{h}_log_e']);arrays[f'{r}_{h}']=new
            coefficients.update({f'{r}_{h}_{k}':v for k,v in co.items()})
            changed_active+=int(co['cap_changed'][ev['active']].sum());unchanged_inactive+=int(np.all(new[~ev['active']]==old['ES'][~ev['active']],axis=(1,2)).sum());underflow+=int(co['baseline_underflow'].sum())
            if co['cap_changed'][~ev['active']].any():raise ValueError('Unexpected inactive cap activation')
            eps={m:np.array([rr[f'{r}_support_{h}_{m}_48/p{p}']['log_probability_bound'] for p in range(48)]) for m in HEADS}
            for a in ('active','inactive'):
                ix=ev['active'] if a=='active' else ~ev['active'];truth=contrast(o[ix]);den=float(np.mean(truth**2));models={}
                for m in ARMS:
                    p=new if m=='ES_UNCAPPED' else old[m];error=mixture_error(m,old,co,eps);cb=contrast_error_bound(error[ix]);con=contrast(p[ix]);err=con-truth;mse=float(np.mean(err**2));low=float(np.mean(np.maximum(abs(err)-cb,0)**2));high=float(np.mean((abs(err)+cb)**2));met=measures(p[ix],y[ix],o[ix]);nllbound=float((o[ix]*error[ix]).sum(-1).mean());ex=(loss(p[ix],o[ix])-loss(old['B3'][ix],o[ix])).mean(1)
                    models[m]=dict(**met,gain=float(-ex.mean()),oracle_loss=float(loss(o[ix],o[ix]).mean()),contrast_mse=mse,contrast_numerator=float(np.sum(err**2)),contrast_denominator=den,contrast_cells=int(err.size),contrast_nrmse=float(np.sqrt(mse/den)) if a=='active' else None,contrast_mse_lower=low,contrast_mse_upper=high,contrast_nrmse_lower=float(np.sqrt(low/den)) if a=='active' else None,contrast_nrmse_upper=float(np.sqrt(high/den)) if a=='active' else None,expected_nll_error_bound=nllbound,expected_nll_enclosure=[met['expected_nll']-nllbound,met['expected_nll']+nllbound],inactive_contrast_rms=float(np.sqrt(np.mean(con**2))),positive_part_excess=float(np.maximum(ex,0).mean()),per_person_excess=ex.tolist(),per_person_change_vs_ES=(loss(p[ix],o[ix])-loss(old['ES'][ix],o[ix])).mean(1).tolist())
                rows.append(dict(id=f'{r}_{h}_{a}',designation=LABEL,real=r,history=h,stratum=a,methods=models,uncapped_mean_weight=float(co['weight'][ix].mean()),changed_weights=int(co['cap_changed'][ix].sum()),baseline_underflow=int(co['baseline_underflow'][ix].sum()),inactive_cap_recalculation_max=delta))
    if changed_active!=153 or unchanged_inactive!=192:raise ValueError('Cap count invariant failed')
    aggregates=[];reference={}
    for r in REAL:
        for a in ('active','inactive'):
            pair=[x for x in rows if x['real']==r and x['stratum']==a];methods={}
            for m in ARMS:
                mm=[x['methods'][m] for x in pair];avg=lambda key:float(np.mean([x[key] for x in mm]));den=avg('contrast_denominator');mse=avg('contrast_mse');gain=avg('gain');gap=float(np.mean([x['methods']['B3']['expected_nll']-x['methods']['B3']['oracle_loss'] for x in pair]));ex=np.mean([x['per_person_excess'] for x in mm],axis=0)
                methods[m]={key:avg(key) for key in ('expected_nll','sampled_nll','accuracy','brier','contrast_mse','contrast_denominator','gain','expected_nll_error_bound')}
                methods[m].update(recovery=gain/gap if a=='active' else None,contrast_nrmse=float(np.sqrt(mse/den)) if a=='active' else None,contrast_nrmse_lower=float(np.sqrt(avg('contrast_mse_lower')/den)) if a=='active' else None,contrast_nrmse_upper=float(np.sqrt(avg('contrast_mse_upper')/den)) if a=='active' else None,positive_part_excess=float(np.maximum(ex,0).mean()),per_person_excess=ex.tolist())
            changes={f'{u}_to_{v}':dict(mse_change=methods[v]['contrast_mse']-methods[u]['contrast_mse'],nrmse_change=methods[v]['contrast_nrmse']-methods[u]['contrast_nrmse'] if a=='active' else None) for u,v in zip(ARMS[1:],ARMS[2:])}
            aggregates.append(dict(id=f'{r}_{a}',designation=LABEL,real=r,stratum=a,methods=methods,ordered_contrast_changes=changes,history_aggregation='Mean losses and squared errors; never mean predictions'))
        pos=next(x for x in aggregates if x['id']==r+'_active')['methods']['ES_UNCAPPED'];neg=next(x for x in aggregates if x['id']==r+'_inactive')['methods']['ES_UNCAPPED']
        reference[r]=dict(gain=pos['gain']>=.05,recovery=pos['recovery']>=.5,contrast=pos['contrast_nrmse']<=.5,inactive=-neg['gain']<=.01,numerical_enclosure_informative=pos['contrast_nrmse_upper']<.5 or pos['contrast_nrmse_lower']>.5)
    return arrays,coefficients,dict(designation=LABEL,qualification=False,rows=rows,aggregates=aggregates,reference_only=reference,active_weight_changes=changed_active,inactive_rows_bitwise_unchanged=unchanged_inactive,baseline_coefficient_underflow_rows=underflow,uncertainty='Analytic optimization bounds evaluated in float64, not directed-rounding certificates or sampling confidence intervals')
