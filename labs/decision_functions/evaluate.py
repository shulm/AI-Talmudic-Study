"""Declared final batch, gated on a pushed protocol freeze; preserve probabilities."""
import os
for name in ['OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS']: os.environ[name]='1'
import argparse
import subprocess
import numpy as np
from common import *
from models import *
from develop import data

def verify_freeze(commit):
    protocol=read(OUT/'experiment_protocol.json')
    rel=str((OUT/'experiment_protocol.json').relative_to(ROOT)).replace('\\','/')
    committed=subprocess.check_output(['git','show',commit+':'+rel],cwd=ROOT)
    assert sha(committed)==sha((OUT/'experiment_protocol.json').read_bytes()), 'Protocol differs from freeze commit'
    assert protocol['status']=='PROTOCOL_FROZEN'
    assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==commit
    remote=subprocess.check_output(['git','ls-remote','origin','refs/heads/codex/decision-functions-execution-v1'],cwd=ROOT,text=True).split()[0]
    assert remote==commit, 'Freeze must be pushed before scoring'
    for rel,digest in protocol['integrity_files'].items():
        assert sha((ROOT/rel).read_bytes())==digest, rel
    for name,expected in protocol['private_files'].items():
        assert manifest(PRIVATE/name)==expected,name
    assert read(OUT/'validation_results.json')['status']=='PASS'
    return protocol

def bootstrap(diff,group_ids):
    groups=sorted(set(group_ids)); gi=np.array([groups.index(x) for x in group_ids])
    rng=np.random.default_rng(1701); vals=[]; rejected=0; s,q=diff.shape
    for attempt in range(20000):
        ws=rng.multinomial(s,np.ones(s)/s); vg=rng.multinomial(len(groups),np.ones(len(groups))/len(groups)); v=vg[gi]
        mask=np.isfinite(diff); denom=(mask*v).sum(1)
        if ((denom==0)&(ws>0)).any(): rejected+=1; continue
        person=(np.nan_to_num(diff)*v).sum(1)/np.maximum(denom,1)
        vals.append(float((person*ws).sum()/ws.sum()))
        if len(vals)==2000: break
    return dict(delta=float(np.nanmean(diff,axis=1).mean()),interval95=np.quantile(vals,[.025,.975]).tolist(),valid_resamples=len(vals),rejected=rejected)

def derangements(n):
    rng=np.random.default_rng(919); result=[]
    while len(result)<10:
        perm=rng.permutation(n)
        if (perm!=np.arange(n)).all(): result.append(perm)
    return result

def batch(split,freeze=None):
    if split=='test': verify_freeze(freeze)
    destination=PRIVATE/(split+'_predictions.npz')
    if destination.exists(): raise RuntimeError('Batch already exists; preserve it, do not overwrite exposed evaluation')
    dev=read(OUT/'development_results.json'); selected=dev['selected']
    splits,ztr,zq,ys,y=data(split)
    model=np.load(PRIVATE/'selected_models.npz'); w,b,pop,center,vs=[model[k] for k in ['w','b','pop','center','vs']]
    base_s=ztr@w+b; base_q=zq@w+b
    supports=read(PRIVATE/'supports.json'); predictions={}; summaries=[]; paired={}
    savedir=PRIVATE/(split+'_probability_cells'); savedir.mkdir(exist_ok=True)
    def save_prediction(key,p):
        # Persist each probability array before any metric aggregation.
        np.save(savedir/(key+'.npy'),p)
        predictions[key]=p
    # Disagreement is evaluator-only and never used for selection or fitting.
    disagreement=np.array([len(set(y[:,j]))>1 for j in range(y.shape[1])])
    def prediction(name,k,seed,permutation=None,seed_index=None):
        ix=[splits['items']['train'].index(q) for q in supports[str(seed)][:k]]
        yy=ys[:,ix] if permutation is None else ys[permutation][:,ix]
        zzs=ztr[ix]-center if name=='M1' else ztr[ix]
        zzq=zq-center if name=='M1' else zq
        vv=vs if seed_index is None else [vs[seed_index]]
        return predict(name,selected[name],zzs,zzq,yy,base_s[ix],base_q,pop,vv)
    for name in ['B0','B1','B2','B3','B4','M1']:
        for k in [0,4,16,64]:
            ps=[]
            for seed in [101,211,307]:
                p=prediction(name,k,seed); save_prediction(f'{name}_k{k}_draw{seed}',p); ps.append(p)
            score={metric:float(np.mean([metrics(p,y)[metric] for p in ps])) for metric in ['nll','accuracy','brier']}
            subset={metric:float(np.mean([metrics(p[:,disagreement],y[:,disagreement])[metric] for p in ps])) for metric in ['nll','accuracy','brier']} if disagreement.any() else None
            summaries.append(dict(model=name,k=k,**score,disagreement_subset=subset))
            paired[f'{name}_k{k}']=np.mean([losses(p,y) for p in ps],axis=0)
    diagnostics=[]
    for i,fit_seed in enumerate([11,29,47]):
        ps=[]
        for draw in [101,211,307]:
            p=prediction('M1',16,draw,seed_index=i); save_prediction(f'M1_seed{fit_seed}_draw{draw}',p); ps.append(p)
        diagnostics.append(dict(seed=fit_seed,nll=float(np.mean([losses(p,y).mean() for p in ps]))))
    controls=[]
    perms=derangements(len(y))
    for name in ['B3','B4','M1']:
        shuffled=[]
        for j,perm in enumerate(perms):
            for draw in [101,211,307]:
                p=prediction(name,16,draw,permutation=perm)
                save_prediction(f'{name}_shuffle{j}_draw{draw}',p); shuffled.append(losses(p,y))
        sl=np.mean(shuffled,axis=0)
        controls.append(dict(model=name,true_nll=float(paired[name+'_k16'].mean()),shuffled_nll=float(sl.mean()),true_history_advantage=float((sl-paired[name+'_k16']).mean())))
    groups=[splits['item_to_group'][q] for q in splits['items'][split]]
    contrasts={name:bootstrap(paired[name+'_k16']-paired['M1_k16'],groups) for name in set([dev['primary_baseline'],'B2','B3'])}
    primary=contrasts[dev['primary_baseline']]; lo,hi=primary['interval95']
    status='VALID_PILOT_POSITIVE_PRIMARY' if lo>0 else ('VALID_PILOT_NONPOSITIVE_PRIMARY' if hi<=0 else 'VALID_PILOT_INCONCLUSIVE')
    np.savez_compressed(destination,**predictions)
    np.savez_compressed(PRIVATE/(split+'_paired_losses.npz'),**paired)
    result=dict(status=status if split=='test' else 'DEVELOPMENT_DIAGNOSTIC',freeze_commit=freeze,split=split,people=len(y),items=y.shape[1],groups=len(set(groups)),disagreement_items=int(disagreement.sum()),primary_baseline=dev['primary_baseline'],primary=primary,contrasts=contrasts,support_curve=summaries,seed_diagnostics=diagnostics,history_controls=controls,per_person_nll={key:value.mean(1).tolist() for key,value in paired.items()},optimizations=OPT_LOG,adaptation_person_solves=sum(o.get('person_solves',0) for o in OPT_LOG),artifacts=[manifest(destination),manifest(PRIVATE/(split+'_paired_losses.npz'))])
    write(OUT/('development_controls.json' if split=='development' else 'test_results.json'),result)
    write(OUT/(split+'_prediction_manifest.json'),dict(artifacts=result['artifacts'],regenerate=f'python labs/decision_functions/evaluate.py {split}'+(' --freeze '+freeze if freeze else ''),local_only=True,warning='Reruns require a separate private output directory; never overwrite an exposed evaluation'))
    (OUT/('TEST_RESULTS.md' if split=='test' else 'DEV_CONTROLS.md')).write_text('# '+split.title()+' results\n\n```json\n'+json.dumps({k:v for k,v in result.items() if k not in ['optimizations','per_person_nll']},indent=2)+'\n```\n',encoding='utf-8')
    print(json.dumps(dict(status=result['status'],primary=primary,controls=controls)),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('split',choices=['development','test']); parser.add_argument('--freeze'); args=parser.parse_args(); batch(args.split,args.freeze)
