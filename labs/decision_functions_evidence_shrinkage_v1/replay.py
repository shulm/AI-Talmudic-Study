"""Independent zero-optimization implementation of forward/evidence arithmetic."""
import numpy as np
from scipy.special import logsumexp

def probs(z,g,x,v):
    logits=np.broadcast_to(g,(len(x),*g.shape)).copy()+x[:,:3,None].transpose(0,2,1)
    if v is not None:
        for c in range(3):logits[:,:,c]+=x[:,3:]@v[c]@z.T
    a=np.exp(logits-logits.max(-1,keepdims=True));return a/a.sum(-1,keepdims=True)

def dp(logits):
    # Dense two-count polynomial recursion, with class 2 implicit.
    a,k,_=logits.shape;prev=np.full((a,k+1,k+1),-np.inf);prev[:,0,0]=0
    for t in range(k):
        nxt=prev+logits[:,t,2,None,None]
        nxt[:,1:,:]=np.logaddexp(nxt[:,1:,:],prev[:,:-1,:]+logits[:,t,0,None,None])
        nxt[:,:,1:]=np.logaddexp(nxt[:,:,1:],prev[:,:,:-1]+logits[:,t,1,None,None])
        # Impossible states already remain -inf; each recurrence consumes one item.
        prev=nxt
    counts=np.array([(i,j,k-i-j) for i in range(k+1) for j in range(k-i+1)])
    return counts,prev[:,counts[:,0],counts[:,1]]

def evidence(z,g,y,v,u):
    atoms=np.vstack((u,-u));weights=np.ones(len(atoms))/len(atoms)
    aa=np.vstack((atoms,np.zeros((1,2))));logits=np.stack([g+np.stack([aa[t]@v[c]@z.T for c in range(3)],-1) for t in range(len(aa))])
    counts,norm=dp(logits);obs=np.array([np.bincount(row,minlength=3) for row in y]);cols=np.array([np.where((counts==n).all(1))[0][0] for n in obs])
    suff=np.array([sum((v[int(c)]@zi for zi,c in zip(z,row)),start=np.zeros(2)) for row in y])
    le=[]
    for row,idx in zip(y,cols):
        chosen=logits[:,np.arange(len(z)),row].sum(1)-norm[:,idx]
        le.append(logsumexp(chosen[:-1]-chosen[-1])-np.log(len(atoms)))
    return dict(atoms=atoms,weights=weights,count_order=counts,normalizers=norm,counts=obs,columns=cols,sufficient=suff,log_e=np.array(le))

def weights(logs):
    # Arithmetic mean evaluated after subtracting max for stability.
    top=np.max(logs,axis=0);le=top+np.log(np.exp(logs-top).sum(0)/len(logs))
    h=np.array([0 if x<=0 else (np.log(10) if x>=np.log1p(np.log(10)/.009) else .009*np.expm1(x)) for x in le])
    w=-np.expm1(-h);return le,h,w
