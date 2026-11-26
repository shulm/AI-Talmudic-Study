"""Historical read-only diagnosis. No optimizer or scientific generator invocation."""
from common import *
from objective import design,penalty,error_bounds,probability
def old_forward(private):
    sys.path.insert(0,str(ROOT/'labs/decision_functions_evidence_shrinkage_v1'))
    import verify as old_verify
    checks={}
    for r in REAL:
        aa={role:load(private/r/(role+'.npz')) for role in ('learner','support','models','predictions','numerical','evidence')}
        replay=old_verify.forward(r,aa,private/r)
        for role,a in replay.items():
            exact(list(a),list(aa[role]))
            for key,val in a.items():checks[f'{r}/{role}/{key}']=close(val,aa[role][key],1e-10 if role=='evidence' and key.endswith(('normalizers','log_e')) else 1e-12)
    return dict(method='Reuse original independent forward/DP replay as comparison; new per-person forward/gradient implementation independently expressed in objective.py',checks=checks,count=len(checks),maximum=max(checks.values()))
def calculate(private):
    datasets={r:{role:load(private/r/(role+'.npz')) for role in ('learner','support','models','predictions','numerical','evidence','evaluator')} for r in REAL};rows=[];store={};alignment={}
    for r in REAL:
        for seed in SEEDS:
            x=np.load(private/r/'parameters'/f'{r}_shared_{seed}.npy',allow_pickle=False);m=datasets[r]['models']
            alignment[f'{r}_{seed}']=max(close(m[f'{seed}_V'],x[:12].reshape(3,2,2)),close(m[f'{seed}_U'],x[12:204].reshape(96,2)),close(m[f'{seed}_b'],x[204:].reshape(96,3)))
    for key,spec in personal_specs().items():
        r,h,m,n=spec['real'],spec['history'],spec['model'],spec['n'];data=datasets[r];support=data['support'];l=data['learner'];v=None if m=='B3' else data['models'][m.split('_')[1]+'_V']
        a=design(support[f'{h}_z'],v);q=design(l['query_z'],v);d=penalty(a.shape[-1]);x=np.load(private/r/'parameters'/(key+'.npy'),allow_pickle=False).reshape(n,len(d))
        for p in range(n):
            eb=error_bounds(x[p],a,support[f'{h}_base'],support[f'{h}_y'][p],d,q);prob=probability(x[p],q,l['query_base'])
            discrepancy=None
            if n==48:discrepancy=close(prob,data['predictions'][f'{h}_{m}'][p])
            elif p==0:discrepancy=close(prob,data['numerical'][f'{n}_{m}'][0])
            row=dict(id=f'{key}/p{p}',parameter_file=f'{r}/parameters/{key}.npy',person_global=144+p,**spec,**{k:val.tolist() if isinstance(val,np.ndarray) else val for k,val in eb.items()},saved_probability_difference=discrepancy)
            rows.append(row);store[(r,h,m,n,p)]=(prob,eb)
    pairs=[]
    for r in REAL:
        for m in HEADS:
            for n in (1,7):
                for p in range(n):
                    pa,ba=store[(r,101,m,n,p)];pb,bb=store[(r,101,m,48,p)];bounds=ba['probability_bound']+bb['probability_bound'];delta=np.max(abs(pa-pb),axis=1)
                    covered=bool(np.all(delta<=bounds+1e-12))
                    if not covered:raise ValueError('Historical solution discrepancy outside residual bounds')
                    pairs.append(dict(id=f'{r}_{m}_{n}_p{p}',real=r,model=m,batch=n,person=144+p,probability_difference_max=float(delta.max()),summed_probability_bound_max=float(bounds.max()),per_query_difference=delta.tolist(),per_query_bound=bounds.tolist(),covered=covered,reference='batch48 is not exact'))
    return dict(rows=rows,alignment=alignment,batch_comparisons=pairs,evaluation_allowance='gradient agreement<=1e-12*max(1,maxabs gradients); add allowance*sqrt(sum(1/D)) to R; prediction comparisons +1e-12; no directed rounding',scope='Fixed shared V, priors, evidence, and histories; only personal optimization error'),datasets
