"""Isolated immutable I/O and exact diagnostic contracts."""
import json,hashlib,os,sys,time,tempfile,subprocess,platform
from pathlib import Path
import numpy as np
import scipy,psutil
ROOT=Path(__file__).resolve().parents[2]
LAB=Path(__file__).parent
OUT=ROOT/'research/decision_functions_2026-11-24/runs/post_es_diagnostics_v1'
OLD=ROOT/'research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1'
BASE='2f1cae3e894bec16c9c5cd280356a4e051029031'
HISTORICAL='f18255c5fad37f704881ff1f9ad50cd113497236'
REAL='EFGH';HIST=(101,211);SEEDS=(11,29,47);HEADS=('B3','M1_11','M1_29','M1_47')
ARMS=('B3','M1','FIXED_MIX','ES','ES_UNCAPPED')
LABEL='POST_HOC_EXPOSED_DIAGNOSTIC'
NAMES=('common.py','objective.py','solver.py','suite.py','diagnosis.py','analysis.py','terminal.py','preflight.py','prepare.py','execute_new.py','verify_new.py','report_new.py','run_profiled.py')
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(p):return sha(Path(p).read_bytes())
def read(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def git(ref,p):return subprocess.check_output(['git','show',ref+':'+p],cwd=ROOT)
def head():return subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
def atomic(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);fd,tmp=tempfile.mkstemp(dir=p.parent,prefix='.pending-')
    try:
        with os.fdopen(fd,'w',encoding='utf-8',newline='\n') as f:f.write(json.dumps(x,indent=2,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
        os.link(tmp,p)
    finally:os.unlink(tmp)
def save(p,x):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('xb') as f:np.savez_compressed(f,**x)
def load(p):
    with np.load(p,allow_pickle=False) as a:
        exact(a.files,set(a.files));return {k:a[k] for k in a.files}
def exact(a,b):
    if len(a)!=len(set(a)) or set(a)!=set(b):raise ValueError('Missing/duplicate/unexpected identities')
def diff(a,b):
    if isinstance(a,dict):exact(list(a),list(b));return max([diff(a[k],b[k]) for k in a]+[0.])
    if isinstance(a,(list,tuple)):return diff(np.array(a),np.array(b)) if all(isinstance(x,(int,float)) for x in a) else max([diff(x,y) for x,y in zip(a,b)]+([0.] if len(a)==len(b) else [float('inf')]))
    if isinstance(a,(np.ndarray,np.number,float,int)) and not isinstance(a,(bool,np.bool_)):
        a=np.asarray(a);b=np.asarray(b)
        if a.shape!=b.shape or not np.isfinite(a).all() or not np.isfinite(b).all():raise ValueError('Shape/nonfinite mismatch')
        return float(np.max(abs(a.astype(float)-b.astype(float)),initial=0))
    if a!=b:raise ValueError('Value mismatch')
    return 0.
def close(a,b,tol=1e-12):
    d=diff(a,b)
    if d>tol:raise ValueError(f'Discrepancy {d} exceeds {tol}')
    return d
def environment():return dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__,psutil=psutil.__version__,platform=platform.platform(),threads=1)
def wrappers():
    out=[]
    for layout in ('singletons','chunks7','all48','reverse48'):
        groups=([[i] for i in range(48)] if layout=='singletons' else ([list(range(i,min(i+7,48))) for i in range(0,48,7)] if layout=='chunks7' else [list(range(48)) if layout=='all48' else list(range(47,-1,-1))]))
        for model in ('B3','M1'):
            for i,people in enumerate(groups):out.append(dict(id=f'{layout}_{model}_{i}',layout=layout,model=model,people=people))
    return out
def attempts():return {f'{w["id"]}_p{p}':dict(wrapper=w['id'],layout=w['layout'],model=w['model'],person=p) for w in wrappers() for p in w['people']}
def personal_specs():
    out={}
    for r in REAL:
        for h in HIST:
            for m in HEADS:out[f'{r}_support_{h}_{m}_48']=dict(real=r,history=h,model=m,n=48)
        for n in (1,7):
            for m in HEADS:out[f'{r}_numerical_101_{m}_{n}']=dict(real=r,history=101,model=m,n=n)
    return out
def expected():
    keys=[f'{key}/p{i}' for key,v in personal_specs().items() for i in range(v['n'])]
    checks=['inputs_before','inputs_after','preservation','source','diagnosis','ablation','derivatives','terminal_tests','inventory']+[f'engineering/{k}' for k in attempts()]+[f'layout/{m}' for m in ('B3','M1')]
    return dict(attempts=attempts(),wrappers=wrappers(),residual_row_ids=keys,residual_numeric_shapes={m:dict(gradient=[3 if m=='B3' else 5],R=[],R_allowance=[],R_used=[],gradient_comparison=[],theta_D_norm=[],K=[36],probability_bound=[36],log_probability_bound=[36]) for m in HEADS},batch_comparison_ids=[f'{r}_{m}_{n}_p{p}' for r in REAL for m in HEADS for n in (1,7) for p in range(n)],ablation_keys={f'{r}_{h}':[48,36,3] for r in REAL for h in HIST},coefficient_keys={f'{r}_{h}_{k}':[48] for r in REAL for h in HIST for k in ('h','log_beta','log_weight','weight','baseline_underflow','cap_changed')},engineering_arrays={f'{l}_{m}_{k}':s for l in ('singletons','chunks7','all48','reverse48') for m in ('B3','M1') for k,s in [('theta',[48,3 if m=='B3' else 5]),('probabilities',[48,12,3])]},stratum_rows=[f'{r}_{h}_{a}' for r in REAL for h in HIST for a in ('active','inactive')],aggregate_rows=[f'{r}_{a}' for r in REAL for a in ('active','inactive')],compared_methods=list(ARMS),private_output_files=['engineering.npz','uncapped_predictions.npz','coefficients.npz'],comparison_ids=checks,counts=dict(personal_rows=1664,engineering_attempts=384,wrappers=114,gradient_blocks=96,hessian_blocks=96,new_primary_arrays=8,scientific_fits=0,historical_refits=0))
def hashes(root):return {p.relative_to(root).as_posix():digest(p) for p in Path(root).rglob('*') if p.is_file()}
def verify_inputs(private):
    binding=read(OUT/'INPUT_BINDINGS.json');got=hashes(private)
    exact(list(got),binding['private_files']);close(got,binding['private_files'])
    for p,h in binding['public_files'].items():
        if sha(git(HISTORICAL,p))!=h or sha((ROOT/p).read_bytes().replace(b'\r\n',b'\n'))!=h:raise ValueError('Historical public input changed: '+p)
    return got
def frozen():
    f=read(OUT/'FREEZE.json');exact(list(f['source']),NAMES)
    close({n:digest(LAB/n) for n in NAMES},f['source'])
    for n,h in f['artifacts'].items():
        if digest(OUT/n)!=h:raise ValueError('Frozen artifact changed: '+n)
    return f
