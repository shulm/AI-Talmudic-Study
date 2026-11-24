"""Synthetic fixture and substantive boundary/invariance checks; no test labels."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np
from common import *
from models import *

def main():
    checks=[]
    splits=read(PRIVATE/'splits.json'); support=read(PRIVATE/'supports.json')
    for name in ['people','groups','items']:
        parts=list(splits[name].values())
        assert sum(map(len,parts))==len(set(sum(parts,[])))
    checks.append('Independent person/item-group partitions disjoint')
    for ids in support.values():
        assert len(ids)==len(set(ids))==64 and set(ids)<=set(splits['items']['train'])
        for k in [0,4,16,64]: assert ids[:k]==ids[:64][:k]
    checks.append('Nested identical-question supports; no query overlap')
    for r in read(PRIVATE/'learner.json'): learner_record(r)
    try: learner_record(dict(item_id='1',text='x',Q_overall='Yes'))
    except ValueError: pass
    else: raise AssertionError('Contamination accepted')
    assert CLASSES['Unsure']==1 and '' not in CLASSES
    checks.append('Strict learner allowlist rejects evaluator contamination; missing != Unsure')
    # Neutral engineering fixture: two phrasings of each binary-factor case.
    x=np.array([[int(c)&(1<<j)>0 for j in range(6)] for c in range(64)],dtype=float)
    rng=np.random.default_rng(43); weights=rng.normal(size=(32,6))
    scores=weights@x.T
    shared=np.digitize(scores,[-.5,.5]); exception=shared.copy()
    exception[:,(x[:,0]==1)&(x[:,1]==1)&(x[:,2]==0)]=2
    records=[]
    for c in range(64):
        for variant in range(2):
            facts=', '.join(f'condition {j+1} is '+('present' if v else 'absent') for j,v in enumerate(x[c]))
            records.append(dict(item_id=f'{c}-{variant}',text=('Consider a case: ' if variant==0 else 'The described situation has these facts: ')+facts))
    write(PRIVATE/'synthetic_learner.json',records)
    write(PRIVATE/'synthetic_evaluator.json',dict(latent=x.tolist(),weights=weights.tolist(),shared=shared.tolist(),exceptions=exception.tolist(),groups={r['item_id']:r['item_id'].split('-')[0] for r in records}))
    group_split=partition(range(64),'synthetic_groups_v1')
    for c in range(64): assert sum(str(c) in p for p in group_split.values())==1
    # Insufficient support cannot identify an arbitrary rule: functions coincide at x0=0.
    f0=np.zeros(64,dtype=int); f1=2*x[:,0].astype(int)
    ambiguous=np.where(x[:,0]==0)[0][:16]; query=np.where(x[:,0]==1)[0][0]
    assert np.array_equal(f0[ambiguous],f1[ambiguous]) and f0[query]!=f1[query]
    checks.append('32-person/64-case shared and exception fixtures, grouped phrasings, ambiguous 16-support case')
    # Exercise all heads, shuffled histories, k=0 and ID renaming (row permutation).
    z=rng.normal(size=(24,8)); z/=np.linalg.norm(z,axis=1,keepdims=True)
    y=shared[:8,:24]; w,b=fit_b2(z,y,.1); base=z@w+b; pop=(np.bincount(y.ravel(),minlength=3)+1)/(y.size+3)
    v=fit_m1(z-z.mean(0),y,base,2,.1,11)
    perm=np.array([4,2,7,0,6,1,5,3]); inverse=np.argsort(perm)
    for name,config,vs in [('B0',None,None),('B1',4,None),('B2',None,None),('B3',.1,None),('B4',(4,1),None),('M1',dict(l2=.1),[v])]:
        for k in [0,4,16]:
            zz=z-z.mean(0) if name=='M1' else z
            args=(name,config,zz[:k],zz[16:],y[:,:k],base[:k],base[16:],pop,vs)
            p=predict(*args); losses(p,y[:,16:])
            renamed=predict(name,config,zz[:k],zz[16:],y[perm,:k],base[:k],base[16:],pop,vs)[inverse]
            assert np.allclose(p,renamed,atol=1e-7)
            if k==0 and name in ['B3','B4','M1']: assert np.allclose(p,softmax(base[16:],axis=-1))
    checks.append('All six heads: finite normalized probabilities, person-renaming invariance, zero-support limits')
    # Independent numerical finite differences audit every objective, without fitting.
    import models
    from scipy.optimize import check_grad
    original=models.solve; gradient_errors=[]
    def inspect(fun,initial,kind):
        flat=initial.ravel(); probe=flat+np.linspace(-.03,.03,len(flat))
        error=check_grad(lambda a:fun(a)[0],lambda a:fun(a)[1],probe)
        gradient_errors.append(float(error)); assert error<1e-5,error
        return flat
    models.solve=inspect
    small=z[:5,:2]; labels=y[:2,:5]
    models.fit_b2(small,labels,.1)
    models.fit_m1(small,labels,np.zeros((5,3)),2,.1,11)
    # adapt's log bookkeeping expects a record from solve.
    models.OPT_LOG.append(dict(kind='gradient_only'))
    models.adapt(np.zeros((5,3)),np.zeros((2,3)),small,small[:2],labels,.1,np.ones((3,2,2))*.1)
    models.solve=original
    checks.append('Finite-difference gradients for B2, shared M1, and support adaptation pass <1e-5')
    from evaluate import bootstrap,derangements
    assert all((p!=np.arange(20)).all() for p in derangements(20))
    constant=np.full((5,7),.123)
    interval=bootstrap(constant,['a','a','b','b','c','d','d'])
    assert np.allclose(interval['interval95'],[.123,.123])
    checks.append('Derangements preserve query ownership; grouped paired bootstrap constant contrast exact')
    write(OUT/'validation_results.json',dict(status='PASS',checks=checks,gradient_errors=gradient_errors,synthetic_is_human_evidence=False,synthetic_shared_fits=2,synthetic_adaptation_person_solves=sum(o.get('person_solves',0) for o in OPT_LOG)))
    print(json.dumps(checks))

if __name__=='__main__': main()
