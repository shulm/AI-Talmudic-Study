"""Three training-only offset batches; never reads held-out label files."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import argparse
from core import *
from head_v1 import adapt,certificate

def main(private):
    names=['splits.json','learner.json','embeddings.npy','selected_models.npz','train_evaluator.npz']
    missing=[n for n in names if not (private/n).exists()]
    if missing:
        receipt('human_certificate.json',dict(status='CACHE_UNAVAILABLE',missing=missing)); return
    hashes={n:file_hash(private/n) for n in names}; protocol=pinned('experiment_protocol.json')
    for n in names:
        if n in protocol['private_files'] and hashes[n]!=protocol['private_files'][n]['sha256']: raise ValueError('Input hash mismatch')
    splits=read(private/'splits.json'); ids=[r['item_id'] for r in read(private/'learner.json')]
    indices=[ids.index(q) for q in splits['items']['train']]
    z=np.load(private/'embeddings.npy')[indices]; model=np.load(private/'selected_models.npz'); y=np.load(private/'train_evaluator.npz')['y']
    assert y.shape==(62,207) and z.shape==(207,384)
    if not np.allclose(z.mean(0),model['center'],atol=1e-15,rtol=0): raise ValueError('Training center mismatch')
    base=z@model['w']+model['b']; centered=z-model['center']
    expected={f'lambda{lam}':meta('human_training_intercept',lam,people=62) for lam in [.1,1.,10.]}
    ledger=Ledger('human_certificate',expected); results=[]
    for lam in [.1,1.,10.]:
        b=adapt(centered,y,base,lam,None,ledger,f'lambda{lam}')
        result=certificate(centered,y,base,b,lam); result['lambda']=lam; results.append(result)
        print(result,flush=True)
    try: audit=ledger.validate()
    except ValueError as e: audit=dict(audit='INCOMPLETE_OR_FAILED',reason=str(e))
    for n,h in hashes.items(): assert file_hash(private/n)==h
    receipt('human_certificate.json',dict(status='COMPUTED',audit=audit,results=results,hashes_before=hashes,hashes_after=hashes,training_only=True,new_intercept_batches=3,person_solves=186,training_label_provenance='train_evaluator.npz lacked a pinned historical digest; hash captured now, shape/joins checked. Not represented as a historical hash match.',bound='||delta G||op <= ||Z||op ||r||F / (2 S sqrt(N) lambda), r is per-person intercept gradient; plus 100 eps max(1,||G||F) roundoff allowance. This is a floating-point diagnostic, not interval-arithmetic certification.',scope='Original training objective only; no generalization conclusion; no replacement for lost logs'))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--private-root',required=True,type=Path); args=parser.parse_args(); main(args.private_root)
