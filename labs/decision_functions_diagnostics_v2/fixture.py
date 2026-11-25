import numpy as np
from scipy.special import softmax
def generate(generator_seed,label_seed):
    rng=np.random.default_rng(generator_seed)
    # Each complete rotational group has isotropic two-dimensional design.
    theta=rng.uniform(0,2*np.pi/3,64)
    angles=(theta[:,None]+np.arange(3)[None]*2*np.pi/3).ravel()
    z=np.column_stack([np.cos(angles),np.sin(angles)])
    group_order=rng.permutation(64); train_groups=group_order[:40]; dev_groups=group_order[40:52]; test_groups=group_order[52:]
    index=lambda groups:np.array([g*3+j for g in groups for j in range(3)])
    splits=dict(train=index(train_groups),development=index(dev_groups),test=index(test_groups),support=index(train_groups[:32]))
    # Consecutive matched pairs have identical nonzero offsets and opposite phases.
    phases=rng.uniform(0,2*np.pi,48); phases=np.column_stack([phases,phases+np.pi]).ravel()
    u=np.column_stack([np.cos(phases),np.sin(phases)])
    bias=np.repeat(rng.normal(0,.12,(48,3)),2,axis=0); bias-=bias.mean(1,keepdims=True)
    v=[]
    for c in range(3):
        a=2*np.pi*c/3
        v.append(2.5*np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]]))
    v=np.array(v)
    base=.25*np.stack([np.cos(angles-2*np.pi*c/3) for c in range(3)],axis=1)
    ys={}; ps={}; label_rng=np.random.default_rng(label_seed)
    for regime in ['positive','null']:
        signal=np.einsum('sr,crd,nd->snc',u,v,z) if regime=='positive' else 0
        p=softmax(base[None]+bias[:,None]+signal,-1)
        ys[regime]=(label_rng.random(p.shape[:2])[...,None]>np.cumsum(p,-1)).sum(-1); ps[regime]=p
        pu=softmax(base[None]+bias[:,None],-1)
        ys[regime+'_uninformative']=(label_rng.random(pu.shape[:2])[...,None]>np.cumsum(pu,-1)).sum(-1)
    return z,base,bias,u,v,splits,ys,ps

def expected_nll(p,oracle): return float(-(oracle*np.log(np.maximum(p,1e-12))).sum(-1).mean())

def contrast(p):
    # Every matched pair, every query, all three pairwise class contrasts,
    # relative to the first query. Shared logits and fixed offsets cancel.
    log=np.log(np.maximum(p,1e-12)); values=[]
    for a,c in [(0,1),(0,2),(1,2)]:
        l=log[:,:,a]-log[:,:,c]; paired=l[::2]-l[1::2]; values.append(paired-paired[:,:1])
    return np.stack(values,-1)

