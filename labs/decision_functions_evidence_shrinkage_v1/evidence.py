"""Conditional count evidence. Inputs contain no activity, oracle, or query labels."""
import numpy as np
from scipy.special import logsumexp

def compositions(k):
    return np.array([(a,b,k-a-b) for a in range(k+1) for b in range(k-a+1)],dtype=int)

def partitions(logits):
    """Atoms x questions x classes -> counts, atoms x counts log partitions."""
    atoms,k,c=logits.shape
    assert c==3
    table=np.zeros((atoms,1)); prev={(0,0,0):0}
    for t in range(1,k+1):
        counts=compositions(t); nxt=np.full((atoms,len(counts)),-np.inf)
        for col,m in enumerate(counts):
            for cls in range(3):
                if m[cls]:
                    old=m.copy();old[cls]-=1
                    nxt[:,col]=np.logaddexp(nxt[:,col],table[:,prev[tuple(old)]]+logits[:,t-1,cls])
        table=nxt;prev={tuple(m):i for i,m in enumerate(counts)}
    return compositions(k),table

def seed_evidence(z,g,y,v,u):
    atoms=np.concatenate([u,-u]);weights=np.full(len(atoms),1/len(atoms))
    all_atoms=np.vstack([atoms,np.zeros((1,u.shape[1]))])
    features=np.einsum('crd,nd->ncr',v,z)
    logits=g[None]+np.einsum('ar,ncr->anc',all_atoms,features)
    counts,normalizers=partitions(logits)
    observed=np.stack([(y==c).sum(1) for c in range(3)],-1)
    lookup={tuple(n):i for i,n in enumerate(counts)}
    columns=np.array([lookup[tuple(n)] for n in observed])
    sufficient=features[np.arange(len(z))[None],y].sum(1)
    log_ratios=sufficient@atoms.T-normalizers[:-1,columns].T+normalizers[-1,columns,None]
    log_e=logsumexp(log_ratios+np.log(weights)[None],axis=1)
    return dict(atoms=atoms,weights=weights,count_order=counts,normalizers=normalizers,counts=observed,columns=columns,sufficient=sufficient,log_e=log_e)

def mixture_weights(seed_logs):
    log_e=logsumexp(seed_logs,axis=0)-np.log(len(seed_logs))
    h=np.zeros_like(log_e); cap=np.log(10.);threshold=np.log1p(cap/.009)
    middle=(log_e>0)&(log_e<threshold)
    h[middle]=.009*np.expm1(log_e[middle]);h[log_e>=threshold]=cap
    return log_e,h,-np.expm1(-h)

def mixtures(b,m,w):
    return .1*b+.9*m,(1-w[:,None,None])*b+w[:,None,None]*m
