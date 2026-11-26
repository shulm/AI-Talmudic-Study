"""Fresh-world stages; called only after explicit execution authorization.

Learning receives train/support labels, never oracle/query labels. Regime names
route evaluator bookkeeping; identical fitting rules apply to every regime.
"""
import sys
import numpy as np
from scipy.special import softmax
from design import *

def fixture(spec):
    rng=np.random.default_rng(spec['generator_seed'])
    theta=rng.uniform(0,2*np.pi/3,64)
    angles=(theta[:,None]+np.arange(3)[None]*2*np.pi/3).ravel()
    z=np.column_stack([np.cos(angles),np.sin(angles)])
    groups=rng.permutation(64)
    ix=lambda g: np.array([3*int(a)+j for a in g for j in range(3)])
    tr,su,qu=ix(groups[:40]),ix(groups[:32]),ix(groups[52:])
    phases=rng.uniform(0,2*np.pi,48)
    phases=np.column_stack([phases,phases+np.pi]).ravel()
    u=np.column_stack([np.cos(phases),np.sin(phases)])
    bias=np.repeat(rng.normal(0,.12,(48,3)),2,axis=0); bias-=bias.mean(1,keepdims=True)
    v=np.array([2.5*np.array([[np.cos(2*np.pi*c/3),-np.sin(2*np.pi*c/3)],[np.sin(2*np.pi*c/3),np.cos(2*np.pi*c/3)]]) for c in range(3)])
    base=.25*np.stack([np.cos(angles-2*np.pi*c/3) for c in range(3)],axis=1)
    signal=np.einsum('sr,crd,nd->snc',u,v,z)
    # Balanced pair membership in each train/unused/heldout block, outcome-blind.
    member=np.zeros(48)
    for a,b in [(0,24),(24,36),(36,48)]: member[rng.permutation(np.arange(a,b))[:(b-a)//2]]=1
    member=np.repeat(member,2)
    # Hidden target mechanism changes only for heldout people; no model can
    # observe this phase. It is a sensitivity test, never a detection gate.
    newphase=rng.uniform(0,2*np.pi,12); newphase=np.column_stack([newphase,newphase+np.pi]).ravel()
    unew=np.column_stack([np.cos(newphase),np.sin(newphase)])
    shifted=signal.copy(); shifted[72:,qu,:]=np.einsum('sr,crd,nd->snc',unew,v,z[qu])
    logit=[np.broadcast_to(base,(96,192,3)),base[None]+bias[:,None],base[None]+bias[:,None]+signal,base[None]+bias[:,None]+signal*.2,base[None]+bias[:,None]+shifted,base[None]+bias[:,None]+signal*member[:,None,None]]
    streams=np.random.SeedSequence(spec['label_seed']).spawn(len(REGIMES))
    out={}
    for r,l,stream in zip(REGIMES,logit,streams):
        p=softmax(l,-1); y=(np.random.default_rng(stream).random((96,192,1))>np.cumsum(p,-1)).sum(-1)
        out[r]=dict(oracle=p[72:][:,qu],query_y=y[72:][:,qu],query_ids=qu,support_ids=su,train_ids=tr,support_y=y[72:][:,su],support_z=z[su],support_base=base[su],train_y=y[:48][:,tr],train_z=z[tr],train_base=base[tr],query_z=z[qu],query_base=base[qu],source_y=y,source_oracle=p,source_z=z,source_base=base)
    return out

def schedule(real, seed, pool):
    groups=sorted(set(int(i)//3 for i in pool))
    def h(kind,g):return hashlib.sha256(f'short_history_v1|{real}|{seed}|{kind}|{g}'.encode()).hexdigest()
    order=sorted(groups,key=lambda g:(h('group',g),g))
    cases=[3*g+(int(h('phase',g),16)%3+j)%3 for g in order for j in range(3)][:16]
    return np.array([int(np.where(pool==i)[0][0]) for i in cases])

def components(real,reg,data,contract,folder,pairs,lbs):
    sys.path.insert(0,str(ROOT/'labs/decision_functions_short_history_v1'))
    from head import fit,adapt,probabilities
    from core import Ledger,validate_records
    class Records(Ledger):
        def __init__(self):
            super().__init__('fits',{k:dict(person_solves=0 if k.startswith('shared') else 24) for k in contract['records']},folder)
            self.parameter_root=folder/'parameters'
    ledger=Records(); arrays=dict(data)
    for seed in SEEDS:
        # Canonical v2 objective units; no post-fit rescaling/rotation of V.
        arrays[f'V_{seed}']=fit(data['train_z'],data['train_y'],data['train_base'],2,.01,.1,seed,ledger,f'shared_{seed}')
    arrays['B2']=np.broadcast_to(softmax(data['query_base'],-1),(24,36,3)).copy()
    prior=np.bincount(data['train_y'].ravel(),minlength=3)/data['train_y'].size
    for h in SCHEDULES:
        ix=schedule(real,h,data['support_ids']); z=data['support_z'][ix]; b=data['support_base'][ix]; y=data['support_y'][:,ix]
        if not np.allclose(np.linalg.eigvalsh(z.T@z/16),[.46875,.53125],atol=1e-12,rtol=0):raise ValueError('Geometry mismatch')
        f=(np.eye(3)[y].sum(1)+4*prior)/20
        arrays[f'h{h}_B1']=np.broadcast_to(f[:,None],(24,36,3)).copy()
        for lb in lbs:
            key=f'h{h}_B3_{lb}'; param=adapt(z,y,b,.01,lb,None,ledger,key)
            arrays[key]=probabilities(data['query_z'],data['query_base'],param)
        for pair in pairs:
            for seed in SEEDS:
                key=f'h{h}_{pair["id"]}_{seed}'; v=arrays[f'V_{seed}']
                param=adapt(z,y,b,pair['rho'],pair['lb'],v,ledger,key)
                arrays[key]=probabilities(data['query_z'],data['query_base'],param,v)
    ledger.validate()
    if set(arrays)!=set(contract['arrays']):raise ValueError('Exact archive keys mismatch')
    with (folder/'components.npz').open('xb') as f:np.savez_compressed(f,**arrays)
    files={p.relative_to(folder).as_posix():digest(p) for p in folder.rglob('*') if p.is_file()}
    write(folder/'manifest.json',dict(id=contract['id'],files=files,contract=contract,realization=real,regime=reg))

def contrast(p):
    log=np.log(np.maximum(p,1e-12)); out=[]
    for a,b in [(0,1),(0,2),(1,2)]:
        q=log[:,:,a]-log[:,:,b]; q=q[::2]-q[1::2]; out.append(q-q[:,:1])
    return np.stack(out,-1)

def validate_probs(p):
    if p.shape!=(24,36,3) or not np.isfinite(p).all() or (p<0).any() or not np.allclose(p.sum(-1),1,atol=1e-12,rtol=0):raise ValueError('Malformed probabilities')

def metric(p,oracle,y):
    validate_probs(p); validate_probs(oracle)
    loss=-(oracle*np.log(np.maximum(p,1e-12))).sum(-1)
    donor=-(oracle*np.log(np.maximum(p[np.arange(24)^1],1e-12))).sum(-1)
    return dict(loss=float(loss.mean()),person_losses=loss.mean(1).tolist(),nll=float(-np.take_along_axis(np.log(np.maximum(p,1e-12)),y[...,None],-1).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()),contrast_mse=float(((contrast(p)-contrast(oracle))**2).mean()),donor_minus_own=float((donor-loss).mean()))

def score_arrays(a,candidates,lbs):
    oracle=a['oracle']; y=a['query_y']; co=contrast(oracle)
    out=dict(oracle_loss=float(-(oracle*np.log(np.maximum(oracle,1e-12))).sum(-1).mean()),contrast_den=float((co**2).mean()))
    by={}
    for h in SCHEDULES:
        pp={'B1':a[f'h{h}_B1'],'B2':a['B2'],**{f'B3_{lb}':a[f'h{h}_B3_{lb}'] for lb in lbs}}
        for c in candidates:
            m=np.mean([a[f'h{h}_{c["pair"]}_{s}'] for s in SEEDS],axis=0)
            pp[c['id']]=(1-c['w'])*a[f'h{h}_B3_{c["lb"]}']+c['w']*m
        by[str(h)]={k:metric(p,oracle,y) for k,p in pp.items()}
    for key in by[str(SCHEDULES[0])]:
        rows=[by[str(h)][key] for h in SCHEDULES]
        out[key]={k:float(np.mean([r[k] for r in rows])) for k in rows[0] if k!='person_losses'}
        out[key]['person_losses']=np.mean([r['person_losses'] for r in rows],axis=0).tolist()
        out[key]['schedules']=[r for r in rows]
    return out

def verify_stage(folder,contract,candidates,lbs):
    sys.path.insert(0,str(ROOT/'labs/decision_functions_short_history_v1'))
    from core import validate_records
    from head import probabilities,shared_objective,personal_objective
    m=read(folder/'manifest.json')
    if m['contract']!=contract or m['id']!=contract['id']:raise ValueError('Manifest contract mismatch')
    if m['realization']+'/'+m['regime']!=contract['id']:raise ValueError('Manifest realization/regime mismatch')
    files={p.relative_to(folder).as_posix():digest(p) for p in folder.rglob('*') if p.is_file() and p.name!='manifest.json'}
    required_files={'components.npz','records/fits/expected.json'}|{f'parameters/{k}.npy' for k in contract['records']}|{f'records/fits/{k}.{suffix}.json' for k in contract['records'] for suffix in ['start','complete']}
    if set(files)!=required_files:raise ValueError('Exact stage file inventory mismatch')
    if files!=m['files']:raise ValueError('Missing, extra or changed stage bytes')
    expected_records={k:dict(person_solves=0 if k.startswith('shared') else 24) for k in contract['records']}
    validate_records(folder/'records'/'fits',expected_records)
    if read(folder/'records/fits/expected.json')!=expected_records:raise ValueError('Ledger expected mismatch')
    for key in contract['records']:
        x=np.load(folder/'parameters'/(key+'.npy'),allow_pickle=False); rec=read(folder/'records/fits'/(key+'.complete.json'))
        if not np.isfinite(x).all() or x.size!=rec['parameter_count'] or abs(np.linalg.norm(x)-rec['parameter_norm'])>1e-12 or min(rec['cpu_seconds'],rec['wall_seconds'])<0:raise ValueError('Parameter/record evidence mismatch')
    with np.load(folder/'components.npz',allow_pickle=False) as f:a={k:f[k] for k in f.files}
    if set(a)!=set(contract['arrays']) or not all(np.isfinite(v).all() for v in a.values()):raise ValueError('Archive incomplete/nonfinite')
    shapes=dict(oracle=(24,36,3),query_y=(24,36),query_ids=(36,),support_ids=(96,),train_ids=(120,),support_y=(24,96),support_z=(96,2),support_base=(96,3),train_y=(48,120),train_z=(120,2),train_base=(120,3),query_z=(36,2),query_base=(36,3),source_y=(96,192),source_oracle=(96,192,3),source_z=(192,2),source_base=(192,3),B2=(24,36,3))
    for k,v in a.items():
        shape=shapes.get(k,(3,2,2) if k.startswith('V_') else (24,36,3))
        if v.shape!=shape:raise ValueError('Shape mismatch: '+k)
    for key in ['source_y','train_y','support_y','query_y']:
        if a[key].dtype.kind not in 'iu' or (a[key]<0).any() or (a[key]>2).any():raise ValueError('Invalid labels')
    for key,n in [('train_ids',120),('query_ids',36),('support_ids',96)]:
        ids=a[key]
        if ids.dtype.kind not in 'iu' or len(set(ids.tolist()))!=n or (ids<0).any() or (ids>=192).any():raise ValueError('Bad identities')
        if len(set(ids//3))!=n//3:raise ValueError('Incomplete semantic groups')
    if set(a['train_ids']//3)&set(a['query_ids']//3) or not set(a['support_ids']).issubset(a['train_ids']):raise ValueError('Group leakage')
    for role,people in [('train',slice(0,48)),('support',slice(72,96)),('query',slice(72,96))]:
        ids=a[role+'_ids']
        for k in ['z','base']:
            if not np.array_equal(a[role+'_'+k],a['source_'+k][ids]):raise ValueError('Input feature join mismatch')
        if not np.array_equal(a[role+'_y'],a['source_y'][people][:,ids]):raise ValueError('Input label join mismatch')
    if not np.array_equal(a['oracle'],a['source_oracle'][72:][:,a['query_ids']]):raise ValueError('Oracle join mismatch')
    for seed in SEEDS:
        key=f'shared_{seed}'; x=np.load(folder/'parameters'/(key+'.npy'),allow_pickle=False)
        fun,unpack,_=shared_objective(a['train_z'],a['train_y'],a['train_base'],2,.01,.1)
        value,grad=fun(x); record=read(folder/'records/fits'/(key+'.complete.json'))
        if not np.isfinite(x).all() or not np.isfinite(value) or not np.isfinite(grad).all():raise ValueError('Nonfinite shared objective replay')
        if not np.array_equal(unpack(x)[0],a[f'V_{seed}']) or abs(value-record['objective'])>1e-12 or abs(np.max(abs(grad))-record['gradient_max'])>1e-12:raise ValueError('Shared objective replay')
    for h in SCHEDULES:
        ix=schedule(m['realization'],h,a['support_ids'])
        if not np.allclose(np.linalg.eigvalsh(a['support_z'][ix].T@a['support_z'][ix]/16),[.46875,.53125],atol=1e-12,rtol=0):raise ValueError('Schedule geometry')
        for key in [k for k in contract['records'] if k.startswith(f'h{h}_')]:
            isb='_B3_' in key; seed=int(key.rsplit('_',1)[1]) if not isb else None
            v=None if isb else a[f'V_{seed}']
            param=np.load(folder/'parameters'/(key+'.npy'),allow_pickle=False).reshape(24,3 if isb else 5)
            pair=None if isb else next(p for p in PAIRS if p['id']==key.split('_')[1]); lb=float(key.rsplit('_',1)[1]) if isb else pair['lb']; rho=.01 if isb else pair['rho']
            fun,_=personal_objective(a['support_z'][ix],a['support_y'][:,ix],a['support_base'][ix],rho,lb,v)
            val,grad=fun(param.ravel()); rec=read(folder/'records/fits'/(key+'.complete.json'))
            if abs(val-rec['objective'])>1e-12 or abs(np.max(abs(grad))-rec['gradient_max'])>1e-12 or 24*np.max(abs(grad))>1e-4:raise ValueError('Adaptation objective/stationarity replay')
            p=probabilities(a['query_z'],a['query_base'],param,v)
            if not np.allclose(p,a[key],atol=1e-12,rtol=0):raise ValueError('Prediction replay mismatch')
        prior=np.bincount(a['train_y'].ravel(),minlength=3)/a['train_y'].size
        f=(np.eye(3)[a['support_y'][:,ix]].sum(1)+4*prior)/20
        if not np.allclose(a[f'h{h}_B1'],f[:,None],atol=1e-12,rtol=0):raise ValueError('B1 replay mismatch')
    if not np.allclose(a['B2'],softmax(a['query_base'],-1)[None],atol=1e-12,rtol=0):raise ValueError('B2 replay mismatch')
    return score_arrays(a,candidates,lbs)
