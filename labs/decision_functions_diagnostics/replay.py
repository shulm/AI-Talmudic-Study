"""Offline replay only: never imports a fitter or historical evaluate.batch."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse
from core import *

TOL=1e-12
MODELS=['B0','B1','B2','B3','B4','M1']; BUDGETS=[0,4,16,64]; DRAWS=[101,211,307]

def expected_keys():
    return ({f'{m}_k{k}_draw{d}' for m in MODELS for k in BUDGETS for d in DRAWS}
            |{f'M1_seed{s}_draw{d}' for s in [11,29,47] for d in DRAWS}
            |{f'{m}_shuffle{j}_draw{d}' for m in ['B3','B4','M1'] for j in range(10) for d in DRAWS})

def validate_archive(arrays,keys,shape):
    if set(arrays)!=keys: raise ValueError('Exact array key set mismatch')
    for p in arrays.values():
        if p.shape!=shape or not np.isfinite(p).all() or (p<0).any() or np.max(np.abs(p.sum(-1)-1))>TOL:
            raise ValueError('Invalid shape/probability normalization')

def compare(a,b):
    error=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    if not np.isfinite(error) or error>TOL: raise ValueError(f'Arithmetic mismatch: {error}')
    return error

def verify_hash(path,expected):
    if file_hash(path)!=expected: raise ValueError('Artifact hash mismatch: '+str(path))

def losses(p,y): return -np.log(np.maximum(np.take_along_axis(p,y[...,None],-1)[...,0],1e-12))
def metrics(p,y):
    return dict(nll=float(losses(p,y).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))

def bootstrap(diff,groups):
    unique=sorted(set(groups)); gi=np.array([unique.index(g) for g in groups]); rng=np.random.default_rng(1701)
    values=[]; rejected=0; s=len(diff)
    for _ in range(20000):
        ws=rng.multinomial(s,np.ones(s)/s); vg=rng.multinomial(len(unique),np.ones(len(unique))/len(unique)); v=vg[gi]
        den=(np.isfinite(diff)*v).sum(1)
        if ((den==0)&(ws>0)).any(): rejected+=1; continue
        per=(np.nan_to_num(diff)*v).sum(1)/np.maximum(den,1)
        values.append(float((per*ws).sum()/ws.sum()))
        if len(values)==2000: break
    if len(values)!=2000: raise ValueError('Bootstrap exhausted')
    return dict(delta=float(np.nanmean(diff,axis=1).mean()),interval95=np.quantile(values,[.025,.975]).tolist(),valid_resamples=len(values),rejected=rejected)

def main(private):
    protocol=pinned('experiment_protocol.json',FREEZE); public=[]; hashes={}; errors=[]
    for path,sha in protocol['integrity_files'].items():
        if digest(git_bytes(FREEZE,path))!=sha or git_bytes(FREEZE,path)!=git_bytes(FINAL,path): raise ValueError('Frozen public evidence mismatch')
        public.append(path)
    required=dict(protocol['private_files'])
    for entry in pinned('test_prediction_manifest.json')['artifacts']: required[entry['filename']]=entry
    for entry in pinned('source_manifest.json')['files']:
        name='source/'+entry['url'].split('/'+pinned('source_manifest.json')['revision']+'/')[1]
        required[name]=entry
    missing=[name for name in required if not (private/name).is_file()]
    if missing:
        receipt('replay_receipt.json',dict(status='PUBLIC_MANIFEST_ONLY',cache='CACHE_UNAVAILABLE',missing=missing,public_files=len(public))); return
    for name,m in required.items(): verify_hash(private/name,m['sha256']); hashes[name]=file_hash(private/name)
    arrays=dict(np.load(private/'test_predictions.npz')); paired=dict(np.load(private/'test_paired_losses.npz'))
    y=np.load(private/'test_evaluator.npz')['y']; splits=read(private/'splits.json')
    validate_archive(arrays,expected_keys(),(22,76,3))
    if set(paired)!={f'{m}_k{k}' for m in MODELS for k in BUDGETS}: raise ValueError('Loss keys mismatch')
    reported=pinned('test_results.json'); disagreement=np.array([len(set(y[:,j]))>1 for j in range(y.shape[1])])
    for row in reported['support_curve']:
        m,k=row['model'],row['k']; ps=[arrays[f'{m}_k{k}_draw{d}'] for d in DRAWS]
        ll=np.mean([losses(p,y) for p in ps],axis=0)
        if paired[f'{m}_k{k}'].shape!=(22,76): raise ValueError('Loss shape mismatch')
        errors.append(compare(ll,paired[f'{m}_k{k}']))
        errors.append(compare(ll.mean(1),reported['per_person_nll'][f'{m}_k{k}']))
        for key in ['nll','accuracy','brier']:
            errors.append(compare(np.mean([metrics(p,y)[key] for p in ps]),row[key]))
            errors.append(compare(np.mean([metrics(p[:,disagreement],y[:,disagreement])[key] for p in ps]),row['disagreement_subset'][key]))
    for row in reported['seed_diagnostics']:
        errors.append(compare(np.mean([losses(arrays[f'M1_seed{row["seed"]}_draw{d}'],y).mean() for d in DRAWS]),row['nll']))
    for row in reported['history_controls']:
        m=row['model']; shuffled=np.mean([losses(arrays[f'{m}_shuffle{j}_draw{d}'],y) for j in range(10) for d in DRAWS],axis=0)
        for a,b in [(shuffled.mean(),row['shuffled_nll']),(paired[m+'_k16'].mean(),row['true_nll']),((shuffled-paired[m+'_k16']).mean(),row['true_history_advantage'])]: errors.append(compare(a,b))
    groups=[splits['item_to_group'][q] for q in splits['items']['test']]; contrasts={}
    for m,row in reported['contrasts'].items():
        contrasts[m]=bootstrap(paired[m+'_k16']-paired['M1_k16'],groups)
        for key in row: errors.append(compare(contrasts[m][key],row[key]))
    maximum=max(float(np.abs(arrays[f'M1_k16_draw{d}']-arrays[f'B3_k16_draw{d}']).max()) for d in DRAWS)
    errors.append(compare(maximum,pinned('final_verification.json')['maximum_absolute_M1_vs_B3_probability_difference']))
    rng=np.random.default_rng(919); perms=[]
    while len(perms)<10:
        p=rng.permutation(22)
        if (p!=np.arange(22)).all(): perms.append(p.tolist())
    for name,h in hashes.items(): verify_hash(private/name,h)
    receipt('replay_receipt.json',dict(status='REPLAYED_FROM_SAVED_ARRAYS',cache='AVAILABLE',public_integrity_files=len(public),private_hashes_before=hashes,private_hashes_after=hashes,arrays=171,paired_arrays=24,tolerance=TOL,max_arithmetic_error=max(errors),comparisons=len(errors),contrasts=contrasts,max_M1_B3_probability_difference=maximum,derangement_schedule_sha256=digest(json.dumps(perms).encode()),derangement_limit='Reconstructed fixed schedule; saved arrays alone cannot prove historical assignment execution',mismatches=[],scientific_limit='Identity and arithmetic replay, not reconstruction of predictions from weights; no new control inferential claims'))
    print('REPLAYED_FROM_SAVED_ARRAYS',max(errors))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--private-root',required=True,type=Path); args=parser.parse_args(); main(args.private_root)
