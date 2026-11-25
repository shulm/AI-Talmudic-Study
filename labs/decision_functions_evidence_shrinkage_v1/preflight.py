"""Deterministic zero-fit tests. No E/F/G/H scientific fixtures are generated."""
from contracts import *
import itertools
import importlib.util
import evidence,replay,head,verify
from scipy.special import softmax,logsumexp

def checks():
    results={}
    def check(name,fn,tol=1e-10):
        value=float(fn());results[name]=dict(max_abs=value,tolerance=tol,passed=bool(value<=tol))
        if value>tol:raise AssertionError(name+': '+str(value))
    def rejects(name,fn):
        try:fn()
        except (ValueError,FileNotFoundError,FileExistsError,KeyError):results[name]=dict(rejected=True);return
        raise AssertionError(name+' did not fail')
    rng=np.random.default_rng(903);v=rng.normal(size=(3,2,2))*.4;u=rng.normal(size=(4,2))*.3
    for k in (0,1,3,6):
        z=np.array([[np.cos(i*.7),np.sin(i*.7)] for i in range(k)]).reshape(k,2);g=np.arange(k*3).reshape(k,3)*.031
        assignments=np.array(list(itertools.product(range(3),repeat=k)),dtype=int).reshape(3**k,k)
        atoms=np.vstack((u,-u,np.zeros((1,2))));logits=g[None]+np.einsum('ar,crd,nd->anc',atoms,v,z)
        counts,tab=evidence.partitions(logits);cc,tab2=replay.dp(logits)
        check(f'dp_dense_k{k}',lambda:abs(tab-tab2).max());maxpart=0;maxmean=0;offseterr=0
        e=evidence.seed_evidence(z,g,assignments,v,u);e2=replay.evidence(z,g,assignments,v,u)
        check(f'evidence_scalar_k{k}',lambda:abs(e['log_e']-e2['log_e']).max())
        for j,n in enumerate(counts):
            ix=np.array([np.array_equal(np.bincount(y,minlength=3),n) for y in assignments]);ys=assignments[ix]
            vals=logits[:,np.arange(k)[None,:],ys].sum(-1);part=logsumexp(vals,axis=1)
            maxpart=max(maxpart,float(abs(part-tab[:,j]).max()));q=np.exp(vals[-1]-part[-1])
            maxmean=max(maxmean,abs(float(q@np.exp(e['log_e'][ix]))-1),abs(float(q.sum())-1))
            b=np.array([2.3,-1.4,.2]);pu=softmax(g+b,-1);un=np.prod(pu[np.arange(k)[None,:],ys],axis=1);offseterr=max(offseterr,float(abs(un/un.sum()-q).max()))
        check(f'exhaustive_all_counts_k{k}',lambda:maxpart);check(f'null_mean_normalization_k{k}',lambda:maxmean);check(f'offset_cancellation_k{k}',lambda:offseterr)
        for label in range(3):check(f'one_class_k{k}_{label}',lambda:abs(evidence.seed_evidence(z,g,np.full((1,k),label),v,u)['log_e']).max())
        check(f'zero_feature_k{k}',lambda:abs(evidence.seed_evidence(np.zeros_like(z),g,assignments,v,u)['log_e']).max())
        check(f'zero_prior_k{k}',lambda:abs(evidence.seed_evidence(z,g,assignments,v,np.zeros_like(u))['log_e']).max())
    # Fixed deterministic toy dimensions, no research fixture or optimizer invocation.
    z=rng.normal(size=(6,2));g=rng.normal(size=(6,3))*.2;y=rng.integers(0,3,(4,6));x=rng.normal(size=32)*.1
    spec=importlib.util.spec_from_file_location('frozen_short_head',ROOT/'labs/decision_functions_short_history_v1/head.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
    fun,unpack,sizes=head.shared_objective(z,y,g,2,.01,.1);oldfun,_,_=old.shared_objective(z,y,g,2,.01,.1)
    check('frozen_objective_gradient',lambda:max(abs(fun(x)[0]-oldfun(x)[0]),abs(fun(x)[1]-oldfun(x)[1]).max()),1e-12)
    check('vector_extraction',lambda:abs(np.concatenate([a.ravel() for a in unpack(x)])-x).max(),1e-12)
    fd=np.array([(fun(x+np.eye(len(x))[i]*1e-5)[0]-fun(x-np.eye(len(x))[i]*1e-5)[0])/2e-5 for i in range(len(x))])
    check('shared_gradient_finite_difference',lambda:abs(fd-fun(x)[1]).max(),1e-8)
    pf,shape=head.personal_objective(z,y,g,.06,.6,v);xx=rng.normal(size=20)*.1;of,_=old.personal_objective(z,y,g,.06,.6,v)
    check('personal_objective_equivalence',lambda:max(abs(pf(xx)[0]-of(xx)[0]),abs(pf(xx)[1]-of(xx)[1]).max()),1e-12)
    fd=np.array([(pf(xx+np.eye(20)[i]*1e-5)[0]-pf(xx-np.eye(20)[i]*1e-5)[0])/2e-5 for i in range(20)])
    check('personal_gradient_finite_difference',lambda:abs(fd-pf(xx)[1]).max(),1e-8)
    e=evidence.seed_evidence(z,g,y,v,u);transform=np.array([[1.3,.2],[-.1,.8]]);vv=np.einsum('ab,cbd->cad',np.linalg.inv(transform),v)
    check('latent_invariance',lambda:abs(evidence.seed_evidence(z,g,y,vv,u@transform)['log_e']-e['log_e']).max())
    perm=np.array([2,0,1]);inverse=np.argsort(perm);question=np.array([5,1,0,2,4,3])
    check('class_question_permutation',lambda:abs(evidence.seed_evidence(z[question],g[question][:,perm],inverse[y[:,question]],v[perm],u)['log_e']-e['log_e']).max())
    check('prior_normalization',lambda:abs(e['weights'].sum()-1),1e-12)
    logs=np.array([[-100,0,1,10,1000],[-99,0,2,9,999],[-98,0,3,8,998.]])
    le,h,w=evidence.mixture_weights(logs);le2,h2,w2=replay.weights(logs)
    check('arithmetic_seed_average',lambda:abs(le-le2).max());check('weight_replay',lambda:max(abs(h-h2).max(),abs(w-w2).max()),1e-12)
    check('not_max_seed',lambda:0 if le[2]<logs[:,2].max() else 1,1e-12)
    b=softmax(rng.normal(size=(5,7,3)),-1);m=softmax(rng.normal(size=(5,7,3)),-1);fixed,es=evidence.mixtures(b,m,w)
    check('mixture_normalization',lambda:abs(es.sum(-1)-1).max(),1e-12)
    check('weight_range_fallback',lambda:max(0,float(-w.min()),float(w.max()-.9),float(abs(w[le<=0]).max())),1e-12)
    check('pointwise_clipped_bound',lambda:max(0,float((np.log(np.maximum(b,1e-12))-np.log(np.maximum(es,1e-12))-h[:,None,None]).max())),1e-12)
    check('objective_repeat',lambda:max(abs(fun(x)[0]-fun(x)[0]),abs(fun(x)[1]-fun(x)[1]).max()),1e-12)
    with tempfile.TemporaryDirectory() as td:
        root=Path(td);atomic(root/'once.json',dict(a=1));rejects('output_collision',lambda:atomic(root/'once.json',{}))
        rejects('empty_run',lambda:verify.verify(root,root));rejects('empty_logs',lambda:validate_records(root,{}))
        rejects('missing_config',lambda:validate_records(root,{'x':{}}));rejects('missing_arrays',lambda:ids_equal([],['a']))
        rejects('duplicate_arrays',lambda:ids_equal(['a','a'],['a']))
        rejects('bad_normalization',lambda:verify.valid_array(np.ones((1,2,3)),[1,2,3],True))
        rejects('wrong_parameter_slice',lambda:verify.Checker().check('x',x,x[::-1]))
        rejects('wrong_prediction',lambda:verify.Checker().check('x',b,b+.001))
        rejects('wrong_evidence_weight',lambda:verify.Checker().check('x',w,w+.001))
        rejects('wrong_aggregation',lambda:verify.Checker().check('x',np.mean(-np.log(b)), -np.log(np.mean(b))))
        atomic(root/'x.start.json',dict(id='x',meta={}));atomic(root/'x.complete.json',dict(id='x',meta={},success=False,finite=True))
        rejects('nonconvergence',lambda:validate_records(root,{'x':{}}))
    check('qualification_incomplete',lambda:float(qualification('INCOMPLETE',True,{r:{k:True for k in ('gain','recovery','contrast','inactive')} for r in REAL})),1e-12)
    check('qualification_missing_realization',lambda:float(qualification('VERIFIED_COMPLETE',True,{})),1e-12)
    check('exact_budget',lambda:abs(sum(v['person_solves'] for r in REAL for st in STAGES for v in expected(r,st).values())-1664),1e-12)
    return results

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path,required=True);a=p.parse_args();start=time.process_time()
    try:r=checks();atomic(a.receipt,dict(passed=True,checks=r,cpu_seconds=time.process_time()-start,fixture='PCG64(903) toy sizes k=0,1,3,6; no scientific fixture; exact source hash pins full specification',source_hash=file_hash(__file__)))
    except Exception as e:atomic(a.receipt,dict(passed=False,error=repr(e),cpu_seconds=time.process_time()-start));raise
