"""Diagnostic-only I/O, immutable ledgers, and bounded optimization accounting."""
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
import time
from pathlib import Path
import numpy as np
import scipy
import psutil

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1'
PILOT = 'research/decision_functions_2026-11-24/runs/pilot_v1/'
FREEZE = '4de12a1fb300a7c9e9d927591bc4b101f0e263a2'
FINAL = '0e5c4ea6bba5bca3926c1bc3ab3a1a552f9536a0'

def digest(data): return hashlib.sha256(data).hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def file_hash(path): return digest(Path(path).read_bytes())
def git_bytes(ref,path): return subprocess.check_output(['git','show',ref+':'+path],cwd=ROOT)
def pinned(name,ref=FINAL): return json.loads(git_bytes(ref,PILOT+name))
def head(): return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()

def atomic(path,obj):
    """Publish once via same-filesystem hard link: complete bytes or no destination."""
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    payload=(json.dumps(obj,indent=2,allow_nan=False)+'\n').encode()
    fd,tmp=tempfile.mkstemp(prefix='.pending-',dir=path.parent)
    try:
        with os.fdopen(fd,'wb') as stream:
            stream.write(payload); stream.flush(); os.fsync(stream.fileno())
        os.link(tmp,path)  # atomic create-if-absent; never replace an existing record
    finally:
        os.unlink(tmp)

def environment():
    return dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,psutil=psutil.__version__,platform=platform.platform(),cpu=platform.processor(),threads=1)

def receipt(name,data):
    atomic(OUT/name,dict(code_commit=head(),code_hashes={p.name:file_hash(p) for p in Path(__file__).parent.glob('*.py')},command=sys.argv,environment=environment(),**data))

class Ledger:
    def __init__(self,stage,expected,out=OUT):
        self.path=Path(out)/'records'/stage
        self.expected=expected
        atomic(self.path/'expected.json',expected)

    def start(self,key,meta):
        if key not in self.expected or meta!=self.expected[key]: raise ValueError('Unexpected configuration')
        atomic(self.path/(key+'.start.json'),dict(id=key,meta=meta,utc=time.time()))

    def complete(self,key,result):
        if not (self.path/(key+'.start.json')).exists(): raise ValueError('Missing start')
        atomic(self.path/(key+'.complete.json'),dict(id=key,meta=self.expected[key],**result))

    def validate(self): return validate_records(self.path,self.expected)

def validate_records(path,expected):
    if not expected: raise ValueError('Empty expected ledger')
    path=Path(path)
    starts={p.name.removesuffix('.start.json') for p in path.glob('*.start.json')}
    ends={p.name.removesuffix('.complete.json') for p in path.glob('*.complete.json')}
    if starts!=set(expected) or ends!=set(expected): raise ValueError('Missing/unexpected/interrupted records')
    records=[read(path/(key+'.complete.json')) for key in expected]
    for key,r in zip(expected,records):
        start=read(path/(key+'.start.json'))
        if start['id']!=key or start['meta']!=expected[key]: raise ValueError('Start configuration mismatch')
        if r['id']!=key or r['meta']!=expected[key]: raise ValueError('Configuration identity mismatch')
        if not r['success'] or not r['finite']: raise ValueError('Unsuccessful/nonfinite optimization')
        required=['message','iterations','objective','gradient_max','person_scaled_gradient_max','parameter_count','parameter_norm','feature_shape','feature_norm','cpu_seconds','wall_seconds']
        if any(k not in r for k in required): raise ValueError('Incomplete optimizer evidence')
        numeric=[r[k] for k in required if k not in ['message','feature_shape']]
        if not np.isfinite(numeric).all(): raise ValueError('Nonfinite optimizer evidence')
        if r['parameter_count']<=0 or r['iterations']<0 or not r['feature_shape']: raise ValueError('Invalid optimizer dimensions')
    return dict(audit='VERIFIED_OPTIMIZATION',records=len(records),person_solves=sum(m['person_solves'] for m in expected.values()),stationarity_separate=True)

def meta(kind,lam,seed=None,people=0):
    return dict(kind=kind,lambda_=lam,seed=seed,person_solves=people)
