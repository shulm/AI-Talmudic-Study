"""Bounded development; opens only training/development evaluator files."""
import os
for name in ['OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS']: os.environ[name]='1'
import itertools
import numpy as np
from common import *
from models import *

def data(split):
    splits=read(PRIVATE/'splits.json'); ids=[r['item_id'] for r in read(PRIVATE/'learner.json')]
    z=np.load(PRIVATE/'embeddings.npy')
    tr=[ids.index(q) for q in splits['items']['train']]; qr=[ids.index(q) for q in splits['items'][split]]
    return splits,z[tr],z[qr],np.load(PRIVATE/f'{split}_support.npz')['y'],np.load(PRIVATE/f'{split}_evaluator.npz')['y']

def main():
    grid=read(Path(__file__).with_name('grid.json'))
    splits,ztr,zd,ys,yd=data('development')
    yt=np.load(PRIVATE/'train_evaluator.npz')['y']
    support=read(PRIVATE/'supports.json')
    indices=[[splits['items']['train'].index(q) for q in support[str(seed)][:16]] for seed in [101,211,307]]
    pop=(np.bincount(yt.ravel(),minlength=3)+1)/(yt.size+3)
    results=[]; b2s=[]
    for lam in grid['B2']:
        w,b=fit_b2(ztr,yt,lam); p=np.broadcast_to(softmax(zd@w+b,axis=-1),(*yd.shape,3))
        score=metrics(p,yd); results.append(dict(model='B2',config=lam,**score)); b2s.append((score['nll'],lam,w,b))
    _,b2lam,w,b=min(b2s,key=lambda x:x[0]); base_s=ztr@w+b; base_q=zd@w+b
    def assess(name,config,vs=None):
        ps=[predict(name,config,ztr[ix],zd,ys[:,ix],base_s[ix],base_q,pop,vs) for ix in indices]
        score={k:float(np.mean([metrics(p,yd)[k] for p in ps])) for k in ['nll','accuracy','brier']}
        results.append(dict(model=name,config=config,**score)); return score['nll']
    selected=dict(B0=None,B2=b2lam)
    assess('B0',None)
    for name,configs in [('B1',grid['B1']),('B3',grid['B3']),('B4',list(itertools.product(grid['B4_neighbors'],grid['B4_shrinkage'])))]:
        scores=[(assess(name,c),c) for c in configs]; selected[name]=min(scores,key=lambda x:x[0])[1]
    center=ztr.mean(0); best=None
    for rank,lam in itertools.product(grid['M1_rank'],grid['M1_l2']):
        vs=[fit_m1(ztr-center,yt,base_s,rank,lam,seed) for seed in grid['M1_seeds']]
        # Only interaction features are centered; B4 retains normalized raw vectors.
        ps=[predict('M1',dict(l2=lam),ztr[ix]-center,zd-center,ys[:,ix],base_s[ix],base_q,pop,vs) for ix in indices]
        score={k:float(np.mean([metrics(p,yd)[k] for p in ps])) for k in ['nll','accuracy','brier']}
        config=dict(rank=rank,l2=lam)
        results.append(dict(model='M1',config=config,**score))
        print(json.dumps(results[-1]),flush=True)
        if best is None or score['nll']<best[0]: best=(score['nll'],config,vs)
    selected['M1']=best[1]
    baseline=min([r for r in results if r['model']!='M1'],key=lambda r:r['nll'])
    write(OUT/'development_results.json',dict(grid_sha256=manifest(Path(__file__).with_name('grid.json'))['sha256'],all_configurations=results,selected=selected,primary_baseline=baseline['model'],optimizations=OPT_LOG,shared_fits=sum(x['kind']=='shared' for x in OPT_LOG),adaptation_person_solves=sum(x.get('person_solves',0) for x in OPT_LOG)))
    np.savez(PRIVATE/'selected_models.npz',w=w,b=b,pop=pop,center=center,vs=np.array(best[2]))
    write(OUT/'model_artifact_manifest.json',manifest(PRIVATE/'selected_models.npz'))
    (OUT/'DEV_RESULTS.md').write_text('# Bounded development results\n\nSelection used development only; test-query labels were not opened.\n\n```json\n'+json.dumps(dict(selected=selected,primary_baseline=baseline,all_configurations=results),indent=2)+'\n```\n',encoding='utf-8')
    print('DONE',json.dumps(selected),baseline['model'],flush=True)

if __name__=='__main__': main()
