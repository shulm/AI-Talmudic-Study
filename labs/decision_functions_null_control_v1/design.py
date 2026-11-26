"""Finite design and statistical decisions. No optimization or fresh-data access."""
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.stats import t

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT/'research/decision_functions_2026-11-24/proposals/short_history_null_control_v1'
BASE = 'ee2b0a5a2f0916fed3dd59f720b902eb332eecc3'
REGIMES = ['population', 'offset', 'strong', 'weak', 'nontransfer', 'mixed']
NULLS = REGIMES[:2]
SEEDS = [11, 29, 47]
SCHEDULES = [101, 211]
PAIRS = [dict(id=f'p{i}', rho=r, lb=b) for i,(r,b) in enumerate([(0.01,0.1),(0.01,0.6),(0.06,0.1),(0.06,0.6)])]
CANDIDATES = [dict(id=f'{p["id"]}_w{j}', pair=p['id'], rho=p['rho'], lb=p['lb'], w=w) for p in PAIRS for j,w in enumerate([0,.25,.5,.75,1])]
DEV_N, MIN_N, MAX_N = 12, 24, 96
ALPHA = .05/3  # simultaneous two null upper bounds AND one strong gain lower bound
PRECISION = .005
FLOOR = 1e-8

def bank(phase):
    if phase not in ['dev','confirmation']: raise ValueError('Unknown bank')
    n = DEV_N if phase=='dev' else MAX_N
    start = 610000 if phase=='dev' else 710000
    return [dict(id=f'{phase}{i:03d}', generator_seed=start+i, label_seed=start+1000+i) for i in range(n)]

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def write(path, value):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('x',encoding='utf-8',newline='\n') as f: json.dump(value,f,indent=2,allow_nan=False); f.write('\n')

def bounds(values):
    x=np.asarray(values,dtype=float)
    if x.ndim!=1 or len(x)<2 or not np.isfinite(x).all(): raise ValueError('Invalid independent-realization vector')
    sd=float(x.std(ddof=1))
    # Zero observed variance is not proof of zero population variance.
    if sd<=0: raise ValueError('Zero variance: inference unresolved')
    h=float(t.ppf(1-ALPHA,len(x)-1)*sd/np.sqrt(len(x)))
    return dict(mean=float(x.mean()), sd=sd, half_width=h, lower=float(x.mean()-h), upper=float(x.mean()+h))

def count_from_dev(vectors):
    s=max(bounds(x)['sd'] for x in vectors)
    for n in range(MIN_N,MAX_N+1):
        if t.ppf(1-ALPHA,n-1)*s/np.sqrt(n)<=PRECISION: return n
    return None

def expected(phase, n, selected=None, common_lb=None):
    if phase not in ['dev','confirmation'] or n<=0 or n>len(bank(phase)): raise ValueError('Invalid stage count')
    if phase=='dev' and n!=DEV_N: raise ValueError('Development budget fixed')
    pairs=PAIRS if phase=='dev' else [next(p for p in PAIRS if p['id']==selected['pair'])]
    lbs=[.1,.6] if phase=='dev' else sorted({selected['lb'],common_lb})
    rows=[]
    for real in bank(phase)[:n]:
        for reg in REGIMES:
            prefix=f'{real["id"]}/{reg}'
            shared=[f'shared_{s}' for s in SEEDS]
            adapt=[f'h{h}_B3_{lb}' for h in SCHEDULES for lb in lbs]+[f'h{h}_{p["id"]}_{s}' for h in SCHEDULES for p in pairs for s in SEEDS]
            arrays=['oracle','query_y','query_ids','support_ids','train_ids','support_y','support_z','support_base','train_y','train_z','train_base','query_z','query_base','source_y','source_oracle','source_z','source_base','B2']
            arrays += [f'V_{s}' for s in SEEDS]
            for h in SCHEDULES:
                arrays += [f'h{h}_B1']+[f'h{h}_B3_{lb}' for lb in lbs]+[f'h{h}_{p["id"]}_{s}' for p in pairs for s in SEEDS]
            rows.append(dict(id=prefix, records=shared+adapt, shared_fits=len(shared), adaptation_batches=len(adapt), person_solves=24*len(adapt), archive=prefix+'/components.npz', arrays=arrays))
    return dict(phase=phase,n=n,stages=rows,shared_fits=sum(r['shared_fits'] for r in rows),adaptation_batches=sum(r['adaptation_batches'] for r in rows),person_solves=sum(r['person_solves'] for r in rows),optimizer_records=sum(len(r['records']) for r in rows),archives=len(rows),array_keys=sum(len(r['arrays']) for r in rows))

def select(scores):
    if len(scores)!=DEV_N: raise ValueError('Incomplete development')
    # Common B3 is selected first, equally weighting only the three primary conditions.
    losses={lb:float(np.mean([s[r][f'B3_{lb}']['loss'] for s in scores for r in REGIMES[:3]])) for lb in [.1,.6]}
    best=min(losses.values()); common=min(lb for lb in losses if losses[lb]<=best+1e-12)
    table=[]
    for c in CANDIDATES:
        risks=[[s[r][c['id']]['loss']-s[r][f'B3_{common}']['loss'] for s in scores] for r in NULLS]
        gains=[s['strong'][f'B3_{common}']['loss']-s['strong'][c['id']]['loss'] for s in scores]
        gap=float(np.mean([s['strong'][f'B3_{common}']['loss']-s['strong']['oracle_loss'] for s in scores]))
        mse=float(np.mean([s['strong'][c['id']]['contrast_mse'] for s in scores])); den=float(np.mean([s['strong']['contrast_den'] for s in scores]))
        try:
            rb=[bounds(x) for x in risks]; gb=bounds(gains)
            recovery=gb['mean']/gap if gap>FLOOR else None
            nr=math.sqrt(mse/den) if den>FLOOR else None
            eligible=c['w']>0 and all(b['upper']<=.01 for b in rb) and gb['mean']>=.05 and gb['lower']>0 and recovery is not None and recovery>=.5 and nr is not None and nr<=.5
            row=dict(candidate=c,eligible=eligible,risks=rb,gain=gb,recovery=recovery,nrmse=nr)
        except ValueError as e: row=dict(candidate=c,eligible=False,reason=str(e))
        table.append(row)
    eligible=[r for r in table if r['eligible']]
    if not eligible: return dict(state='DEV_NO_CANDIDATE',qualification=False,common_lb=common,common_losses={str(k):v for k,v in losses.items()},table=table)
    top=max(r['gain']['mean'] for r in eligible)
    chosen=min([r for r in eligible if r['gain']['mean']>=top-1e-12],key=lambda r:(r['candidate']['w'],-r['candidate']['rho'],-r['candidate']['lb'],r['candidate']['id']))
    c=chosen['candidate']; vectors=[[s[r][c['id']]['loss']-s[r][f'B3_{common}']['loss'] for s in scores] for r in NULLS]+[[s['strong'][f'B3_{common}']['loss']-s['strong'][c['id']]['loss'] for s in scores]]
    n=count_from_dev(vectors)
    return dict(state='SELECTED' if n else 'DEV_INSUFFICIENT_PRECISION',qualification=False,selected=c,common_lb=common,common_losses={str(k):v for k,v in losses.items()},table=table,confirmation_n=n)

def confirm(scores, selection):
    if selection.get('state')!='SELECTED' or selection.get('selected') not in CANDIDATES or selection.get('common_lb') not in [.1,.6]:raise ValueError('Invalid selection')
    n=selection['confirmation_n']; c=selection['selected']; lb=selection['common_lb']
    if n is None or len(scores)!=n or n<MIN_N or n>MAX_N: raise ValueError('Incomplete confirmation')
    rb={r:bounds([s[r][c['id']]['loss']-s[r][f'B3_{lb}']['loss'] for s in scores]) for r in NULLS}
    gb=bounds([s['strong'][f'B3_{lb}']['loss']-s['strong'][c['id']]['loss'] for s in scores])
    gap=float(np.mean([s['strong'][f'B3_{lb}']['loss']-s['strong']['oracle_loss'] for s in scores])); den=float(np.mean([s['strong']['contrast_den'] for s in scores]))
    if gap<=FLOOR or den<=FLOOR: raise ValueError('Undefined strong recovery')
    recovery=gb['mean']/gap; nr=math.sqrt(np.mean([s['strong'][c['id']]['contrast_mse'] for s in scores])/den)
    point=gb['mean']>=.05 and recovery>=.5 and nr<=.5 and all(v['mean']<=.01 for v in rb.values())
    precision=all(v['half_width']<=PRECISION for v in [*rb.values(),gb])
    qualified=point and precision and c['w']>0 and gb['lower']>0 and all(v['upper']<=.01 for v in rb.values())
    matched=[]
    for s in scores:
        own=s['strong'][c['id']]; b=s['strong'][f'B3_{c["lb"]}']; g=b['loss']-own['loss']; d=b['loss']-s['strong']['oracle_loss']
        matched.append(dict(gain=g,recovery=g/d if d>FLOOR else None,nrmse=math.sqrt(own['contrast_mse']/s['strong']['contrast_den']) if s['strong']['contrast_den']>FLOOR else None,null_harms={r:s[r][c['id']]['loss']-s[r][f'B3_{c["lb"]}']['loss'] for r in NULLS}))
    return dict(state='COMPLETE_PREDICTIVE_SUCCESS' if qualified else ('COMPLETE_INSUFFICIENT_PRECISION' if not precision else 'COMPLETE_PRIMARY_FAILURE'),qualification=bool(qualified),null_bounds=rb,strong_gain=gb,recovery=float(recovery),nrmse=float(nr),new_common_B3_point_gates=bool(point),historical_matched_B3_continuity=matched,precision_pass=precision,claim='Expected risk over generated realizations, conditional on fixed selected policy; approximate t inference, not every-world safety')
