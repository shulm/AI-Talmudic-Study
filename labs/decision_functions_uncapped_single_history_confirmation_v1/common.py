"""Explicit contracts and exclusive durable I/O. No scientific RNG or optimizer."""
import hashlib,json,os,sys,time,subprocess
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
ASSIGNMENT='ae74b9e5604b4905804d25b296097467f6794f14'
STUDY='uncapped_single_history_confirmation_v1'
LAB=ROOT/'labs'/('decision_functions_'+STUDY)
DEFAULT_OUTPUT=ROOT/'research/decision_functions_2026-11-24/runs'/STUDY
WORLDS=tuple(f'U{i:03d}' for i in range(82))
HIST=('H1','H2'); SEEDS=(11,29,47)
HEADS=('B3','M1_11','M1_29','M1_47')
METHODS=('B1','B2','B3','M1','FIXED_MIX','ES','ES_UNCAPPED')
OWN=METHODS+HEADS[1:]
def require(ok,message):
    if not ok:raise ValueError(message)
def digest(data):return hashlib.sha256(data).hexdigest()
def sha(path):return digest(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def clean(x):
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [clean(v) for v in x]
    if isinstance(x,np.ndarray):return clean(x.tolist())
    if isinstance(x,np.generic):return x.item()
    return x
def atomic(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(clean(value),indent=2,allow_nan=False)+'\n').encode()
    temp=path.with_name(path.name+f'.tmp-{os.getpid()}')
    with temp.open('xb') as f:f.write(raw);f.flush();os.fsync(f.fileno())
    try:os.link(temp,path)
    finally:temp.unlink()
def save(path,arrays):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:np.savez(f,**arrays);f.flush();os.fsync(f.fileno())
def load(path):
    with np.load(path,allow_pickle=False) as f:
        require(len(f.files)==len(set(f.files)),'Duplicate archive key')
        return {k:f[k].copy() for k in f.files}
def exact(actual,expected):require(set(actual)==set(expected) and len(actual)==len(expected),'Exact inventory mismatch')
def close(a,b,tol=1e-10):
    if isinstance(b,dict):
        exact(a,b)
        for k in b:close(a[k],b[k],tol)
    elif isinstance(b,(list,tuple)):
        require(len(a)==len(b),'Length mismatch')
        for x,y in zip(a,b):close(x,y,tol)
    elif isinstance(b,(str,bool)) or b is None:require(a==b,'Scalar identity mismatch')
    else:
        aa=np.asarray(a);bb=np.asarray(b)
        require(aa.shape==bb.shape and np.allclose(aa,bb,rtol=0,atol=tol,equal_nan=False),'Arithmetic mismatch')
def probabilities(p):
    require(p.shape==(48,36,3) and p.dtype==np.float64,'Probability shape/dtype')
    require(np.isfinite(p).all() and (p>=0).all() and (p<=1).all(),'Invalid probabilities')
    require(np.max(abs(p.sum(-1)-1))<=1e-12,'Normalization')
def ids(world):
    return [f'{world}/shared/{s}' for s in SEEDS]+[f'{world}/{h}/{head}/{i:02d}' for h in HIST for head in HEADS for i in range(48)]
def prediction_keys():return [f'{h}_{m}' for h in HIST for m in OWN+tuple(m+'_donor' for m in METHODS)]
def log_keys():return [f'{h}_ES_UNCAPPED{s}' for h in HIST for s in ('','_donor')]
def journal(path,record):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('ab') as f:f.write((json.dumps(clean(record),allow_nan=False)+'\n').encode());f.flush();os.fsync(f.fileno())
def records(path):return [json.loads(line) for line in Path(path).read_text().splitlines()]
def inventory(path,expected,complete=True):
    rows=records(path);starts=[r['id'] for r in rows if r['event']=='start'];ends=[r['id'] for r in rows if r['event']=='complete']
    seen=set();finished=set()
    for row in rows:
        require(row['event'] in ('start','complete'),'Unknown journal event')
        if row['event']=='start':require(row['id'] not in seen,'Duplicate start');seen.add(row['id'])
        else:require(row['id'] in seen and row['id'] not in finished,'Completion without unique preceding start');finished.add(row['id'])
    require(len(set(starts))==len(starts) and len(set(ends))==len(ends),'Duplicate journal identity')
    require(set(ends)<=set(starts)<=set(expected),'Unexpected journal identity')
    if complete:exact(starts,expected);exact(ends,expected)
    return rows
def frozen(out):
    freeze=read(out/'FREEZE.json')
    for path,h in freeze['files'].items():require(digest((ROOT/path).read_bytes().replace(b'\r\n',b'\n'))==h,'Frozen file changed: '+path)
    return freeze
def terminal(*,completed,expected,integrity,numerical,scientific,reason=None,qualified=False,**extra):
    reserved={'completed','expected','integrity','numerical','scientific','reason','qualification','inventory_complete'}
    require(not (reserved&set(extra)),'Protected terminal field collision')
    full=completed==expected
    require(not qualified or (full and integrity==numerical==scientific=='PASS' and reason is None),'Invalid qualification')
    return dict(completed=completed,expected=expected,inventory_complete=full,integrity=integrity,numerical=numerical,scientific=scientific,reason=reason,qualification=bool(qualified),**extra)
