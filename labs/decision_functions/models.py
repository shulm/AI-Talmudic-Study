"""Categorical baselines and PAL/PReF-inspired interaction, analytic gradients."""
import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp, softmax

OPT_LOG=[]

def solve(fun,x,kind):
    r=minimize(fun,x.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=300 if kind=='shared' else 100,ftol=1e-10,gtol=1e-6,maxls=30))
    OPT_LOG.append(dict(kind=kind,success=bool(r.success),message=str(r.message),iterations=int(r.nit),loss=float(r.fun),gradient_max=float(np.abs(r.jac).max())))
    if not np.isfinite(r.fun): raise ValueError('Nonfinite optimization')
    return r.x

def ce(logits,y):
    loss=(logsumexp(logits,axis=-1)-np.take_along_axis(logits,y[...,None],axis=-1)[...,0]).mean()
    g=softmax(logits,axis=-1)
    g-=np.eye(3)[y]; g/=y.size
    return loss,g

def fit_b2(z,y,lam):
    n,d=z.shape; counts=np.eye(3)[y].mean(axis=0)
    def fun(x):
        w=x[:d*3].reshape(d,3); b=x[d*3:]
        logits=z@w+b; p=softmax(logits,axis=-1)
        loss=np.mean(logsumexp(logits,axis=-1)-(counts*logits).sum(-1)) +lam/2*np.sum(w*w)
        g=(p-counts)/n
        return loss,np.r_[((z.T@g)+lam*w).ravel(),g.sum(0)]
    x=solve(fun,np.zeros(d*3+3),'shared')
    return x[:d*3].reshape(d,3),x[d*3:]

def fit_m1(z,y,base,rank,lam,seed):
    s,n=y.shape; d=z.shape[1]; rng=np.random.default_rng(seed)
    sizes=(3*rank*d,s*rank,s*3)
    def unpack(x):
        a,b,_=sizes
        return x[:a].reshape(3,rank,d),x[a:a+b].reshape(s,rank),x[a+b:].reshape(s,3)
    def fun(x):
        v,u,b=unpack(x); f=np.einsum('nd,crd->ncr',z,v)
        logits=base[None]+b[:,None,:]+np.einsum('sr,ncr->snc',u,f)
        loss,g=ce(logits,y)
        loss+=lam/2*(np.sum(v*v)+(np.sum(u*u)+np.sum(b*b))/s)
        gv=np.einsum('snc,sr,nd->crd',g,u,z,optimize=True)+lam*v
        gu=np.einsum('snc,ncr->sr',g,f)+lam*u/s
        gb=g.sum(1)+lam*b/s
        return loss,np.r_[gv.ravel(),gu.ravel(),gb.ravel()]
    x=np.r_[rng.normal(0,.05,sizes[0]+sizes[1]),np.zeros(sizes[2])]
    result=solve(fun,x,'shared')
    return unpack(result)[0]

def adapt(base_s,base_q,zs,zq,ys,lam,v=None):
    s,k=ys.shape
    if k==0: return np.broadcast_to(softmax(base_q,axis=-1),(s,len(zq),3)).copy()
    rank=0 if v is None else v.shape[1]
    fs=np.zeros((k,3,0)) if v is None else np.einsum('nd,crd->ncr',zs,v)
    fq=np.zeros((len(zq),3,0)) if v is None else np.einsum('nd,crd->ncr',zq,v)
    def fun(x):
        x=x.reshape(s,3+rank); b=x[:,:3]; u=x[:,3:]
        logits=base_s[None]+b[:,None]+np.einsum('sr,ncr->snc',u,fs)
        loss,g=ce(logits,ys); loss+=lam/2*np.sum(x*x)/s
        grad=np.concatenate([g.sum(1),np.einsum('snc,ncr->sr',g,fs)],axis=1)+lam*x/s
        return loss,grad.ravel()
    x=solve(fun,np.zeros((s,3+rank)),'adapt').reshape(s,3+rank)
    OPT_LOG[-1]['person_solves']=s
    return softmax(base_q[None]+x[:,:3,None].transpose(0,2,1)+np.einsum('sr,ncr->snc',x[:,3:],fq),axis=-1)

def predict(name,config,zs,zq,ys,base_s,base_q,pop,vs=None):
    s,k=ys.shape; nq=len(zq)
    if name=='B0': return np.broadcast_to(pop,(s,nq,3)).copy()
    if name=='B1':
        p=(np.eye(3)[ys].sum(1)+config*pop)/(k+config)
        return np.broadcast_to(p[:,None],(s,nq,3)).copy()
    if name=='B2': return np.broadcast_to(softmax(base_q,axis=-1),(s,nq,3)).copy()
    if name=='B3': return adapt(base_s,base_q,zs,zq,ys,config)
    if name=='B4':
        if k==0: return predict('B2',None,zs,zq,ys,base_s,base_q,pop)
        neighbors,alpha=config; sim=zq@zs.T
        idx=np.argsort(-sim,axis=1,kind='stable')[:,:min(k,neighbors)]
        weights=np.exp(np.take_along_axis(sim,idx,axis=1)-1)
        votes=(np.eye(3)[ys[:,idx]]*weights[None,:,:,None]).sum(2)
        return (votes+alpha*softmax(base_q,axis=-1)[None])/(weights.sum(1)[None,:,None]+alpha)
    if name=='M1': return np.mean([adapt(base_s,base_q,zs,zq,ys,config['l2'],v) for v in vs],axis=0)
    raise ValueError(name)

def losses(p,y):
    assert p.shape==(*y.shape,3)
    assert np.isfinite(p).all() and (p>=0).all() and np.allclose(p.sum(-1),1)
    return -np.log(np.maximum(np.take_along_axis(p,y[...,None],axis=-1)[...,0],1e-12))

def metrics(p,y):
    return dict(nll=float(losses(p,y).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))
