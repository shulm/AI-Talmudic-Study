"""Generator/evaluator view; never imported by fitting or evidence functions."""
from contracts import *
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

def schedule(real,seed,pool):
    gs=sorted(set((pool//3).tolist()),key=lambda g:(digest(f'evidence_shrinkage_v1|{real}|{seed}|group|{g}'.encode()),g))
    out=[]
    for g in gs:
        first=int(digest(f'evidence_shrinkage_v1|{real}|{seed}|phase|{g}'.encode()),16)%3
        out.extend([3*g+(first+i)%3 for i in range(3)])
    return np.array(out[:16])

def views(f,real):
    t=f['train'];q=f['test'];y=f['y'][:96][:,t]
    learner=dict(z=f['z'][t],base=f['base'][t],y=y,query_z=f['z'][q],query_base=f['base'][q],query_ids=q,training_prior=np.bincount(y.ravel(),minlength=3)/y.size)
    support={};orders={}
    for h in HIST:
        ids=schedule(real,h,f['pool']);eigs=np.linalg.eigvalsh(f['z'][ids].T@f['z'][ids]/16)
        if not np.allclose(eigs,[.46875,.53125],rtol=0,atol=1e-12):raise ValueError('Support geometry')
        orders[str(h)]=dict(ids=ids.tolist(),gram_eigenvalues=eigs.tolist())
        support.update({f'{h}_ids':ids,f'{h}_z':f['z'][ids],f'{h}_base':f['base'][ids],f'{h}_y':f['y'][144:][:,ids]})
    evaluator=dict(y=f['y'][144:][:,q],oracle=f['oracle'][144:][:,q],active=f['active'][144:],person_ids=np.arange(144,192),query_ids=q)
    return learner,support,evaluator,orders
