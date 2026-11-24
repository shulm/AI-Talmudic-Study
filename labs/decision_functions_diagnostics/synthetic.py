"""Fixed planted-interaction diagnostic; no human inputs."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse
from core import *
from head_v1 import *
from replay import metrics

LAMBDAS=[.1,1.,10.,.001]; SEEDS=[11,29,47]

def expected():
    e={}
    for regime in ['positive','null']:
        for lam in LAMBDAS:
            prefix=f'{regime}_lambda{lam}'
            e[prefix+'_training_offset']=meta('synthetic_adapt',lam,people=48)
            for condition in ['informative','uninformative']:
                e[prefix+'_'+condition+'_B3']=meta('synthetic_adapt',lam,people=24)
            for seed in SEEDS:
                e[prefix+f'_seed{seed}_shared']=meta('synthetic_shared',lam,seed)
                for condition in ['informative','uninformative']:
                    e[prefix+f'_seed{seed}_{condition}_M1']=meta('synthetic_adapt',lam,seed,24)
    for model in ['B3','M1_11','M1_29','M1_47']:
        for n in [1,7]: e[f'batch_{model}_{n}']=meta('synthetic_adapt',.001,None,n)
    return e

def generate():
    rng=np.random.default_rng(20261125)
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
    ys={}; ps={}; label_rng=np.random.default_rng(2718)
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

def main(local):
    ledger=Ledger('synthetic',expected()); z,base,bias,u,v,split,ys,ps=generate()
    local.mkdir(parents=True,exist_ok=True); tr=split['train']; su=split['support']; qu=split['test']
    assert len(set(tr)&set(qu))==0 and len(su)==96
    eig=np.linalg.eigvalsh(z[su].T@z[su]/96); assert eig.min()>.1
    results=[]; certificates=[]; selected={}; allpred={}; norms=[]
    for regime in ['positive','null']:
        yt=ys[regime][:48,tr]; oracle=ps[regime][72:,qu]; yq=ys[regime][72:,qu]
        for lam in LAMBDAS:
            prefix=f'{regime}_lambda{lam}'
            offset=adapt(z[tr],yt,base[tr],lam,None,ledger,prefix+'_training_offset')
            certificates.append(dict(regime=regime,lambda_=lam,**certificate(z[tr],yt,base[tr],offset,lam)))
            vectors=[fit(z[tr],yt,base[tr],2,lam,seed,ledger,prefix+f'_seed{seed}_shared') for seed in SEEDS]
            norms.append(dict(regime=regime,lambda_=lam,basis_norms=[float(np.linalg.norm(x)) for x in vectors]))
            for condition in ['informative','uninformative']:
                zs=z[su] if condition=='informative' else np.zeros_like(z[su])
                labels=ys[regime if condition=='informative' else regime+'_uninformative'][72:,su]
                b=adapt(zs,labels,base[su],lam,None,ledger,prefix+'_'+condition+'_B3'); pb=probabilities(z[qu],base[qu],b)
                pred=[]
                for seed,vv in zip(SEEDS,vectors):
                    personal=adapt(zs,labels,base[su],lam,vv,ledger,prefix+f'_seed{seed}_{condition}_M1')
                    pred.append(probabilities(z[qu],base[qu],personal,vv))
                pm=np.mean(pred,axis=0); eb=expected_nll(pb,oracle); em=expected_nll(pm,oracle); eo=expected_nll(oracle,oracle)
                truth=contrast(oracle); estimate=contrast(pm)
                denom=float(np.mean(truth**2)); crmse=float(np.sqrt(np.mean((estimate-truth)**2)/denom)) if denom>1e-20 else None
                result=dict(regime=regime,lambda_=lam,condition=condition,B3=metrics(pb,yq),M1=metrics(pm,yq),oracle=metrics(oracle,yq),expected_nll_B3=eb,expected_nll_M1=em,expected_nll_oracle=eo,expected_gain=eb-em,oracle_gap_recovery=(eb-em)/(eb-eo) if eb-eo>1e-12 else None,contrast_normalized_rmse=crmse,predicted_contrast_rms=float(np.sqrt(np.mean(estimate**2))),oracle_contrast_rms=float(np.sqrt(denom)))
                results.append(result); allpred[prefix+'_'+condition+'_B3']=pb; allpred[prefix+'_'+condition+'_M1']=pm
                if regime=='positive' and lam==.001 and condition=='informative': selected=dict(vs=vectors,b=pb,seed_predictions=pred,labels=labels)
            print(regime,lam,results[-2]['expected_gain'],flush=True)
    batch=[]
    for name,vv,reference in [('B3',None,selected['b'])]+[(f'M1_{seed}',vv,p) for seed,vv,p in zip(SEEDS,selected['vs'],selected['seed_predictions'])]:
        for n in [1,7]:
            personal=adapt(z[su],selected['labels'][:n],base[su],.001,vv,ledger,f'batch_{name}_{n}')
            p=probabilities(z[qu],base[qu],personal,vv)
            batch.append(dict(model=name,batch_size=n,max_first_person_difference=float(np.abs(p[0]-reference[0]).max())))
    positive=next(r for r in results if r['regime']=='positive' and r['lambda_']==.001 and r['condition']=='informative')
    null=next(r for r in results if r['regime']=='null' and r['lambda_']==.001 and r['condition']=='informative')
    gates=dict(positive_NLL=positive['expected_gain']>=.05,oracle_gap_recovery=positive['oracle_gap_recovery']>=.5,contrast_recovery=positive['contrast_normalized_rmse']<=.5,null_behavior=null['expected_gain']>=-.01,batch_invariance=max(r['max_first_person_difference'] for r in batch)<=1e-6)
    try: audit=ledger.validate()
    except ValueError as e: audit=dict(audit='INCOMPLETE_OR_FAILED',reason=str(e))
    np.savez_compressed(local/'synthetic_predictions.npz',**allpred)
    frequencies={}
    for regime in ['positive','null']:
        expected_freq=ps[regime].mean(1); sampled=np.eye(3)[ys[regime]].mean(1)
        frequencies[regime]=dict(expected_pair_max=float(np.abs(expected_freq[::2]-expected_freq[1::2]).max()),sampled_pair_max=float(np.abs(sampled[::2]-sampled[1::2]).max()),expected_class_frequency_min=float(expected_freq.min()),expected_class_frequency_max=float(expected_freq.max()))
    receipt('synthetic_results.json',dict(status='RECOVERY_DEMONSTRATED' if all(gates.values()) else 'BOUNDED_DIAGNOSTIC_FAILURE',gates=gates,audit=audit,results=results,batch_checks=batch,certificates=certificates,basis_norms=norms,support_gram_eigenvalues=eig.tolist(),frequency_balance=frequencies,shared_fits=24,adaptation_person_solves=sum(v['person_solves'] for v in expected().values()),prediction_sha256=file_hash(local/'synthetic_predictions.npz'),generator_sha256=digest(z.tobytes()+bias.tobytes()+u.tobytes()+v.tobytes()),development_policy='Reserved 24 people/12 groups; no selection, tuning, or scoring on them',interpretation='Numerical features only; no encoder or human generalization evidence'))
    print(gates,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output-private-root',required=True,type=Path); args=parser.parse_args(); main(args.output_private_root)
