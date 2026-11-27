"""Support-only prediction/evidence. Evaluator truth is never accepted."""
from common import *
from scipy.special import softmax,logsumexp
import evidence,objective

def schedule(seed,pool):
    rng=np.random.Generator(np.random.PCG64(int(seed)))
    groups=rng.permutation(sorted(set((pool//3).tolist())));phases=rng.integers(0,3,size=32)
    return np.array([3*int(g)+(int(p)+j)%3 for g,p in zip(groups,phases) for j in range(3)][:16],dtype=np.int64)

def views(f,seeds):
    t=f['train'];q=f['test'];y=f['y'][:96][:,t]
    learner=dict(z=f['z'][t],base=f['base'][t],y=y,query_z=f['z'][q],query_base=f['base'][q],query_ids=q,training_prior=np.bincount(y.ravel(),minlength=3)/y.size)
    support={}
    for h in HIST:
        ids_=schedule(seeds[h+'_support'],f['pool'])
        close(np.linalg.eigvalsh(f['z'][ids_].T@f['z'][ids_]/16),[.46875,.53125],1e-12)
        support.update({f'{h}_ids':ids_,f'{h}_z':f['z'][ids_],f'{h}_base':f['base'][ids_],f'{h}_y':f['y'][144:][:,ids_]})
    evaluator=dict(y=f['y'][144:][:,q],oracle=f['oracle'][144:][:,q],active=f['active'][144:],person_ids=np.arange(144,192),query_ids=q)
    return learner,support,evaluator

def stable_mix(b,m,log_e):
    require(np.isfinite(log_e).all(),'Nonfinite evidence')
    h=np.zeros_like(log_e);ix=log_e>0
    with np.errstate(over='raise',invalid='raise'):h[ix]=.009*np.expm1(log_e[ix])
    require(np.isfinite(h).all(),'Nonfinite uncapped coefficient')
    lb=-h;w=-np.expm1(lb)
    with np.errstate(divide='ignore'):lw=np.log(w);logp=np.logaddexp(lb[:,None,None]+np.log(b),lw[:,None,None]+np.log(m))
    p=np.exp(logp);p[h==0]=b[h==0]
    require(np.isfinite(logp).all(),'Nonfinite log probability')
    close(np.maximum(logp,np.log(1e-12)),np.log(np.maximum(p,1e-12)),1e-12)
    return p,logp,dict(log_e=log_e,h=h,log_beta=lb,w=w)

def predict(learner,support,models,personal):
    pred={};logs={};ev={};donor=np.arange(48)^1
    for h in HIST:
        counts=np.stack([(support[h+'_y']==c).sum(1) for c in range(3)],-1)
        pred[h+'_B1']=np.broadcast_to(((counts+4*learner['training_prior'])/20)[:,None,:],(48,36,3)).copy()
        pred[h+'_B2']=np.broadcast_to(softmax(learner['query_base'],-1),(48,36,3)).copy()
        for name in HEADS:
            v=None if name=='B3' else models[name[3:]+'_V'];a=objective.design(learner['query_z'],v)
            pred[h+'_'+name]=np.stack([objective.probability(theta,a,learner['query_base']) for theta in personal[h+'_'+name]])
        seedlogs=[]
        for seed in SEEDS:
            e=evidence.seed_evidence(support[h+'_z'],support[h+'_base'],support[h+'_y'],models[str(seed)+'_V'],models[str(seed)+'_U'])
            ev.update({f'{h}_{seed}_{k}':v for k,v in e.items()});seedlogs.append(e['log_e'])
        le=logsumexp(seedlogs,axis=0)-np.log(3)
        b=pred[h+'_B3'];m=np.mean([pred[h+'_M1_'+str(s)] for s in SEEDS],axis=0);pred[h+'_M1']=m
        pred[h+'_FIXED_MIX']=.1*b+.9*m
        _,hc,wc=evidence.mixture_weights(np.array(seedlogs));pred[h+'_ES']=(1-wc[:,None,None])*b+wc[:,None,None]*m
        p,lp,co=stable_mix(b,m,le);pred[h+'_ES_UNCAPPED']=p;logs[h+'_ES_UNCAPPED']=lp
        ev.update({h+'_'+k:v for k,v in co.items()});ev[h+'_capped_h']=hc
        for name in METHODS:pred[h+'_'+name+'_donor']=pred[h+'_'+name][donor].copy()
        logs[h+'_ES_UNCAPPED_donor']=lp[donor].copy()
    exact(pred,prediction_keys());exact(logs,log_keys())
    for p in pred.values():probabilities(p)
    return pred,logs,ev

def log_enclosures(pred,bounds,ev):
    out={}
    for h in HIST:
        logb=np.log(pred[h+'_B3']);eb=bounds[h+'_B3_log_probability_bound'][:,:,None]
        lm=np.stack([np.log(pred[h+'_M1_'+str(s)]) for s in SEEDS]);em=np.stack([bounds[h+'_M1_'+str(s)+'_log_probability_bound'][:,:,None] for s in SEEDS])
        mlo=logsumexp(lm-em,axis=0)-np.log(3);mhi=logsumexp(lm+em,axis=0)-np.log(3)
        with np.errstate(divide='ignore'):lw=np.log(ev[h+'_w'])[:,None,None]
        lb=ev[h+'_log_beta'][:,None,None]
        for name,lo,hi in [('B3',logb-eb,logb+eb),('ES_UNCAPPED',np.logaddexp(lb+logb-eb,lw+mlo),np.logaddexp(lb+logb+eb,lw+mhi))]:
            out[h+'_'+name+'_lower']=np.maximum(lo,np.log(1e-12));out[h+'_'+name+'_upper']=np.maximum(hi,np.log(1e-12))
    return out
