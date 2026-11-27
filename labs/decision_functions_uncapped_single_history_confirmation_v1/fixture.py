"""Generator/evaluator view; never imported by fitting or evidence functions."""
import numpy as np
from scipy.special import softmax

def generate(generator_seed,label_seed,mask_seed):
    rng=np.random.Generator(np.random.PCG64(generator_seed))
    theta=rng.uniform(0,2*np.pi/3,64);angles=(theta[:,None]+np.arange(3)[None]*2*np.pi/3).ravel()
    z=np.column_stack([np.cos(angles),np.sin(angles)]);groups=rng.permutation(64)
    phase=rng.uniform(0,2*np.pi,96);phase=np.column_stack([phase,phase+np.pi]).ravel()
    u=np.column_stack([np.cos(phase),np.sin(phase)])
    bias=np.repeat(rng.normal(0,.12,(96,3)),2,axis=0);bias-=bias.mean(1,keepdims=True)
    v=np.array([2.5*np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]]) for a in np.arange(3)*2*np.pi/3])
    base=.25*np.stack([np.cos(angles-2*np.pi*c/3) for c in range(3)],axis=1)
    mask_rng=np.random.Generator(np.random.PCG64(mask_seed));pairs=np.zeros(96,dtype=bool)
    for lo,hi in [(0,48),(48,72),(72,96)]:pairs[mask_rng.permutation(np.arange(lo,hi))[:(hi-lo)//2]]=True
    active=np.repeat(pairs,2);effective=u*active[:,None]
    oracle=softmax(base[None]+bias[:,None]+np.einsum('sr,crd,nd->snc',effective,v,z),-1)
    label_rng=np.random.Generator(np.random.PCG64(label_seed));y=(label_rng.random(oracle.shape[:2])[...,None]>np.cumsum(oracle,-1)).sum(-1)
    index=lambda gs:(gs[:,None]*3+np.arange(3)).ravel()
    return dict(z=z,base=base,bias=bias,u=u,v=v,active=active,y=y,oracle=oracle,train=index(groups[:40]),reserved=index(groups[40:52]),test=index(groups[52:]),pool=index(groups[:32]))
