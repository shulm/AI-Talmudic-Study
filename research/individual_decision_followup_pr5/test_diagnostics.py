"""Focused algebra, leakage and observed-development boundary tests; no test outcomes."""
import time
import numpy as np
import diagnostics as d

def main():
    t=time.process_time();old=d.verify_original();real_rows=d.rows
    forbidden={'evaluator_labels_test.jsonl','canonical_observations.jsonl','evaluator_labels.jsonl'}
    def guarded_rows(path):
        assert path.name not in forbidden, 'forbidden label file '+path.name
        yield from real_rows(path)
    d.rows=guarded_rows
    train=d.load(old,'train');validation=d.load(old,'validation');test=d.load(old,'test')
    assert len(train['people'])==304 and len(validation['people'])==len(test['people'])==102
    assert not set(train['people'])&set(validation['people']) and not set(test['people'])&set(validation['people'])
    d.labels(old,train,'train');d.labels(old,validation,'validation')
    try:d.labels(old,test,'test')
    except RuntimeError:pass
    else:raise AssertionError('test label boundary failed')
    folds=d.folds(validation['people'])
    for ind in folds:
        bank=sorted(set(range(102))-set(ind));assert len(ind)==len(bank)==51
        assigned=d.donors([validation['people'][i] for i in ind],[validation['people'][i] for i in bank])
        assert assigned.shape==(51,5) and all(len(set(r))==5 for r in assigned)
        for shift in [1,5,11,17,23]:assert all(a!=b for a,b in zip(ind,np.roll(ind,shift)))
    # Deliberately disparate donor probabilities: wrong averaging order is detectable.
    y=np.array([[1.,0.],[0.,1.]])
    donors=np.array([[[.99,.01],[.9,.1]],[[.01,.99],[.1,.9]]])
    replacement=np.mean([d.nll(y,p) for p in donors],axis=0);mixture=d.nll(y,donors.mean(0))
    assert np.all(replacement>mixture)
    assert np.isclose(d.nll(y,donors[0]).mean(),-np.log([.99,.99,.1,.1]).mean())
    assert np.allclose(d.nll(1-y,1-donors[0]),d.nll(y,donors[0]))
    assert d.ci(replacement-mixture)['participants']==2 # not donors x trials
    # Source-blind reference has no recipient source argument and is identical across recipients.
    blind=d.fixed_reference(donors[:,0,:],7)
    assert blind.shape==(7,2) and np.allclose(blind,blind[0])
    models=d.bundle(old)['profile'];small=d.subset(validation,list(range(4)))
    prior=d.prior_predict(models,small['tx'])
    assert np.allclose(d.prior_predict(models,-small['tx']),1-prior,atol=1e-9)
    for b in d.BUDGETS:
        p=d.posterior_predict(models,small,b)
        flipped={**small,'sx':-small['sx'],'sy':1-small['sy'],'tx':-small['tx']}
        assert np.allclose(d.posterior_predict(models,flipped,b),1-p,atol=1e-7)
        assert np.all((p>0)&(p<1)) and np.allclose(np.stack([1-p,p],-1).sum(-1),1)
        if b==0:assert np.allclose(p,prior)
    # Only the prefix is charged; altering unrevealed answers must not affect predictions.
    hidden={**small,'sy':small['sy'].copy()};hidden['sy'][:,2:]=1-hidden['sy'][:,2:]
    assert np.allclose(d.posterior_predict(models,small,2),d.posterior_predict(models,hidden,2))
    d.dump(d.ROOT/'boundary_checks.json',dict(passed=True,forbidden_files_blocked=sorted(forbidden),
        tests=['person isolation','disjoint per-fold banks','unique donor assignments','actual whole-history derangements','Jensen order','participant not donor/trial clustering','source-blind recipient independence','same-profile prior zero','source and target option-order invariance','probability normalization','uncharged answer invariance'],
        test_outcomes_read=False,process_cpu_seconds=time.process_time()-t))
    d.event('boundary_tests',time.process_time()-t,shared_fits=0,test_outcomes_read=False)
    print('Focused diagnostic checks PASS; no old-test outcomes read.')
if __name__=='__main__':main()
