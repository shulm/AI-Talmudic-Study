"""Versioned objective adapter from pilot 4de12a1 models.py; no historical writes.

Same mean CE and factor/intercept penalty. New optimizer tolerances and receipts
are diagnostics, not a reproduction of missing historical optimizer records.
"""
import time
import numpy as np
from scipy.optimize import minimize
from scipy.special import softmax,logsumexp

def ce(logits,y):
    loss=(logsumexp(logits,-1)-np.take_along_axis(logits,y[...,None],-1)[...,0]).mean()
    return loss,(softmax(logits,-1)-np.eye(3)[y])/y.size

def shared_objective(z,y,base,rank,lam):
    s,n=y.shape; d=z.shape[1]; a=3*rank*d; b=s*rank
    def unpack(x): return x[:a].reshape(3,rank,d),x[a:a+b].reshape(s,rank),x[a+b:].reshape(s,3)
    def fun(x):
        v,u,bias=unpack(x); f=np.einsum('nd,crd->ncr',z,v)
        loss,g=ce(base[None]+bias[:,None]+np.einsum('sr,ncr->snc',u,f),y)
        loss+=lam/2*(np.sum(v*v)+(np.sum(u*u)+np.sum(bias*bias))/s)
        gv=np.einsum('snc,sr,nd->crd',g,u,z,optimize=True)+lam*v
        gu=np.einsum('snc,ncr->sr',g,f)+lam*u/s
        gb=g.sum(1)+lam*bias/s
        return loss,np.r_[gv.ravel(),gu.ravel(),gb.ravel()]
    return fun,unpack,(a,b,s*3)

def personal_objective(z,y,base,lam,v=None):
    s,n=y.shape; rank=0 if v is None else v.shape[1]
    f=np.zeros((n,3,0)) if v is None else np.einsum('nd,crd->ncr',z,v)
    def fun(flat):
        x=flat.reshape(s,3+rank)
        loss,g=ce(base[None]+x[:,:3,None].transpose(0,2,1)+np.einsum('sr,ncr->snc',x[:,3:],f),y)
        loss+=lam/2*np.sum(x*x)/s
        grad=np.concatenate([g.sum(1),np.einsum('snc,ncr->sr',g,f)],axis=1)+lam*x/s
        return loss,grad.ravel()
    return fun,(s,3+rank)

def solve(fun,initial,ledger,key,feature,person_scale):
    ledger.start(key,ledger.expected[key]); start=time.process_time(); wall=time.monotonic()
    r=minimize(fun,initial.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=1000,ftol=1e-12,gtol=1e-8,maxls=50))
    value,grad=fun(r.x)
    finite=bool(np.isfinite(value) and np.isfinite(r.x).all() and np.isfinite(grad).all())
    ledger.complete(key,dict(success=bool(r.success),finite=finite,message=str(r.message),iterations=int(r.nit),objective=float(value),gradient_max=float(np.abs(grad).max()),person_scaled_gradient_max=float(np.abs(grad).max()*person_scale),parameter_count=len(r.x),parameter_norm=float(np.linalg.norm(r.x)),feature_shape=list(feature.shape),feature_norm=float(np.linalg.norm(feature)),cpu_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall))
    if not finite: raise ValueError('Nonfinite solve')
    return r.x

def fit(z,y,base,rank,lam,seed,ledger,key):
    fun,unpack,sizes=shared_objective(z,y,base,rank,lam); rng=np.random.default_rng(seed)
    initial=np.r_[rng.normal(0,.05,sizes[0]+sizes[1]),np.zeros(sizes[2])]
    return unpack(solve(fun,initial,ledger,key,z,len(y)))[0]

def adapt(z,y,base,lam,v,ledger,key):
    fun,shape=personal_objective(z,y,base,lam,v)
    return solve(fun,np.zeros(shape),ledger,key,z,len(y)).reshape(shape)

def probabilities(z,base,personal,v=None):
    logits=base[None]+personal[:,:3,None].transpose(0,2,1)
    if v is not None: logits=logits+np.einsum('sr,crd,nd->snc',personal[:,3:],v,z)
    return softmax(logits,-1)

def certificate(z,y,base,b,lam):
    s,n=y.shape; p=softmax(base[None]+b[:,None],-1); residual=(p-np.eye(3)[y]).mean(1)+lam*b
    g=np.einsum('snc,nd->scd',p-np.eye(3)[y],z).reshape(s,-1)/(s*n)
    singular=float(np.linalg.svd(g,compute_uv=False)[0]); threshold=lam/np.sqrt(s)
    # Strong convexity per person: ||delta b||F <= ||residual||F/lambda.
    # Softmax Jacobian operator norm <= 1/2 gives this Frobenius bound on delta G.
    intercept_bound=np.linalg.norm(z,2)*np.linalg.norm(residual)/(2*s*np.sqrt(n)*lam)
    roundoff=100*np.finfo(float).eps*max(1,float(np.linalg.norm(g)))
    error=float(intercept_bound+roundoff); margin=threshold-singular
    status='ZERO_INTERACTION_OPTIMAL' if margin>error else ('NONZERO_DESCENT_AVAILABLE' if margin < -error else 'NUMERICALLY_UNRESOLVED')
    return dict(status=status,S=s,N=n,d=z.shape[1],spectral_norm=singular,threshold=float(threshold),signed_margin=float(margin),error_bound=error,intercept_residual_max=float(np.abs(residual).max()),intercept_residual_frobenius=float(np.linalg.norm(residual)),svd_roundoff_allowance=float(roundoff),feature_norm=float(np.linalg.norm(z)),feature_spectral_norm=float(np.linalg.norm(z,2)))
