"""Exact public contracts, constructed without generating research fixtures."""
from core import *
BASE='724be8c49808e1e1b8643d81c73267f7577439c8'
REAL={r:dict(generator_seed=20261201+i,label_seed=2801+i,mask_seed=2901+i) for i,r in enumerate('EFGH')}
SEEDS=(11,29,47); HIST=(101,211)
METHODS=('B1','B2','B3','M1','FIXED_MIX','ES')
HEADS=('B3','M1_11','M1_29','M1_47')
OWN=METHODS+HEADS[1:]
STAGES=('shared','support','numerical')
ROLES=('fixture','learner','support','evaluator','models','predictions','numerical','evidence','bootstrap')
SOURCE_NAMES=('contracts.py','core.py','head.py','evidence.py','fixture.py','execute.py','scoring.py','replay.py','independent_scoring.py','verify.py','preflight.py','integration_preflight.py','freeze.py','report.py','run_logged.py')
def source_paths():
    return ['labs/decision_functions_evidence_shrinkage_v1/'+n for n in SOURCE_NAMES]+['research/decision_functions_2026-11-24/runs/evidence_shrinkage_v1/'+n for n in ('PROTOCOL.json','EXPECTED.json','METHOD_PROOF.md')]
def historical():
    raw=subprocess.check_output(['git','ls-tree','-r',BASE,'--','labs','research/decision_functions_2026-11-24/runs'],cwd=ROOT,text=True)
    return {line.split('\t',1)[1]:line.split()[2] for line in raw.splitlines() if line.split()[1]=='blob'}
def binding_paths(real,stage):
    roles=['fixture','learner','support','evaluator'];keys=[]
    if stage in ('support','numerical'):roles+=['models'];keys+=list(expected(real,'shared'))
    if stage=='numerical':roles+=['evidence','predictions'];keys+=list(expected(real,'support'))
    return [r+'.npz' for r in roles]+['parameters/'+k+'.npy' for k in keys]

def expected(real,stage):
    common=dict(realization=real,**REAL[real],classes=3,rank=2,dtype='float64',maxiter=1000,ftol=1e-12,gtol=1e-8,maxls=50)
    if stage=='shared':return {f'{real}_shared_{s}':dict(**common,kind='shared',seed=s,rho=.01,lambda_b=.1,people=96,questions=120,person_solves=0) for s in SEEDS}
    combos=[(h,m,48) for h in HIST for m in HEADS] if stage=='support' else [(101,m,n) for n in (1,7) for m in HEADS]
    if stage not in STAGES:raise ValueError('Unexpected stage')
    return {f'{real}_{stage}_{h}_{m}_{n}':dict(**common,kind='personal',seed=None if m=='B3' else int(m.split('_')[1]),rho=.06,lambda_b=.6,people=n,questions=16,person_solves=n,history=h,model=m) for h,m,n in combos}

def shapes(role):
    fixture=dict(z=[192,2],base=[192,3],bias=[192,3],u=[192,2],v=[3,2,2],active=[192],y=[192,192],oracle=[192,192,3],train=[120],reserved=[36],test=[36],pool=[96])
    if role=='fixture':return fixture
    if role=='learner':return dict(z=[120,2],base=[120,3],y=[96,120],query_z=[36,2],query_base=[36,3],query_ids=[36],training_prior=[3])
    if role=='support':return {f'{h}_{k}':shape for h in HIST for k,shape in dict(ids=[16],z=[16,2],base=[16,3],y=[48,16]).items()}
    if role=='evaluator':return dict(y=[48,36],oracle=[48,36,3],active=[48],person_ids=[48],query_ids=[36])
    if role=='models':return {f'{s}_{k}':shape for s in SEEDS for k,shape in dict(V=[3,2,2],U=[96,2],b=[96,3]).items()}
    if role=='predictions':return {f'{h}_{m}':[48,36,3] for h in HIST for m in OWN+tuple(x+'_donor' for x in METHODS)}
    if role=='numerical':return {f'{n}_{m}':[1,36,3] for n in (1,7) for m in HEADS+('M1','FIXED_MIX','ES')}
    if role=='evidence':
        out={f'{h}_{s}_{k}':shape for h in HIST for s in SEEDS for k,shape in dict(atoms=[192,2],weights=[192],count_order=[153,3],normalizers=[193,153],counts=[48,3],columns=[48],sufficient=[48,2],log_e=[48]).items()}
        out.update({f'{h}_{k}':[48] for h in HIST for k in ('log_e','h','w')});return out
    if role=='bootstrap':return {**{k:[2000,12] for k in ('active_pairs','inactive_pairs','query_groups')},**{k:[2000] for k in ('active_gain','inactive_degradation','active_donor','active_ES_fixed','inactive_ES_fixed')}}
    raise ValueError(role)

def ids_equal(actual,required):
    if len(actual)!=len(set(actual)) or set(actual)!=set(required):raise ValueError('Missing/duplicate/unexpected identities')

def qualification(complete,numerical,gates):
    return complete=='VERIFIED_COMPLETE' and numerical is True and set(gates)==set(REAL) and all(set(g)=={'gain','recovery','contrast','inactive'} and all(v is True for v in g.values()) for g in gates.values())

def contract():
    return dict(stages={f'{r}_{s}':expected(r,s) for r in REAL for s in STAGES},archives={role:shapes(role) for role in ROLES},score_rows=[f'{h}_{a}_{m}' for h in HIST for a in ('active','inactive') for m in OWN],evidence_rows=[f'{h}_{p}' for h in HIST for p in range(144,192)],comparison_ids=comparison_ids(),totals=dict(shared_fits=12,adaptation_batches=64,person_solves=1664,optimizer_records=76,ledgers=12,prediction_arrays=176))

def comparison_ids():
    # Exact comparison operations; each checks every element of the named object.
    out=[]
    for r in REAL:
        out += [f'{r}/archive/{role}/{key}' for role in ROLES for key in shapes(role)]
        out += [f'{r}/forward/{role}/{key}' for role in ('models','predictions','numerical','evidence','bootstrap') for key in shapes(role)]
        out += [f'{r}/record/{key}' for stage in STAGES for key in expected(r,stage)]
        out += [f'{r}/{x}' for x in ('fixture_join','support_geometry','scores','evidence_summary','bootstrap_summary','numerical_summary','pointwise','manifest')]
    return out+['historical_blobs','frozen_sources','qualification','resource_contract']

if __name__=='__main__':atomic(OUT/'EXPECTED.json',contract())
