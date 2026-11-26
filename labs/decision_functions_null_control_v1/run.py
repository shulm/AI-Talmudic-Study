"""Auditable stage CLI. Planning never invokes execute/all with authorization."""
import argparse
import os
import subprocess
import sys
import threading
import time
import psutil
from design import *
from engine import fixture, components, verify_stage

def source_files():
    return sorted(list(Path(__file__).parent.glob('*.py'))+[ROOT/'labs/decision_functions_short_history_v1'/f for f in ['core.py','head.py']]+[PACKAGE/f for f in ['PROPOSED_PROTOCOL.json','CANDIDATES.json','SEEDS.json','GENERATOR_CONTRACT.md','SELECTION_AND_CONFIRMATION.md','RESOURCE_PLAN.json']])

def pins():return {p.relative_to(ROOT).as_posix():digest(p) for p in source_files()}

def authorize(auth):
    a=read(auth)
    if a.get('owner_authorized_execution') is not True or a.get('source_hashes')!=pins():raise ValueError('Exact current package authorization required')
    if read(PACKAGE/'PROPOSED_PROTOCOL.json')['status']!='PROTOCOL_FROZEN':raise ValueError('Protocol not frozen')
    return a

def freeze(root,auth):
    authorize(auth)
    if root.exists():raise ValueError('Fresh private output root required')
    write(root/'freeze.json',dict(source_hashes=pins(),authorization_sha256=digest(auth),base=BASE,stages=['development','selection','confirmation','verification']))
    write(root/'dev_expected.json',expected('dev',DEV_N))

def verify_freeze(root,auth):
    authorize(auth)
    f=read(root/'freeze.json')
    if f['source_hashes']!=pins() or f['authorization_sha256']!=digest(auth):raise ValueError('Freeze changed')

def config(root,phase):
    if phase=='dev':
        e=expected(phase,DEV_N)
        if read(root/'dev_expected.json')!=e:raise ValueError('Development expected contract mismatch')
        return e,PAIRS,[.1,.6],CANDIDATES
    s=read(root/'selection.json')
    if s['state']!='SELECTED':raise ValueError('No selected policy')
    c=s['selected']; lbs=sorted({c['lb'],s['common_lb']})
    e=expected(phase,s['confirmation_n'],c,s['common_lb'])
    if read(root/'confirmation_expected.json')!=e:raise ValueError('Confirmation contract mismatch')
    return e,[next(p for p in PAIRS if p['id']==c['pair'])],lbs,[c]

def watchdog(root):
    """One process at a time, sampled whole-process CPU/RSS. No fit retry."""
    proc=psutil.Process(); previous=sum(read(p)['cpu_seconds'] for p in root.glob('resources/*.json'))
    def watch():
        while True:
            cpu=sum(proc.cpu_times()[:2]); rss=proc.memory_info().rss
            if previous+cpu>14400 or rss>4*1024**3:
                write(root/'RESOURCE_STOP.json',dict(state='INCOMPLETE',cpu_seconds=previous+cpu,rss=rss))
                os._exit(3)
            time.sleep(.05)
    threading.Thread(target=watch,daemon=True).start()

def execute(root,phase,index,auth):
    lock=root/'execution.lock'
    with lock.open('x',encoding='utf-8') as f:f.write(str(os.getpid()))
    try:
        return execute_locked(root,phase,index,auth)
    finally:
        lock.unlink()

def execution_boundary(root):
    """Missing failed-attempt accounting is unresolved expenditure, never free CPU."""
    if (root/'EXECUTION_FAILURE.json').exists() or (root/'RESOURCE_STOP.json').exists():
        raise ValueError('Terminal study failure; further execution forbidden')
    attempts={p.stem for p in root.glob('attempts/*.json')}
    complete={p.stem for p in root.glob('complete/*.json')}
    resources={p.stem for p in root.glob('resources/*.json')}
    if attempts!=complete or attempts!=resources:
        raise ValueError('Incomplete attempt/completion/resource inventory; expenditure unresolved')
    previous=[]
    for key in sorted(attempts):
        attempt=read(root/'attempts'/(key+'.json'));done=read(root/'complete'/(key+'.json'))
        if done!=dict(state='COMPLETE',spec=attempt['spec']) or attempt['spec']['id']!=key:
            raise ValueError('Prior completion identity mismatch')
        r=read(root/'resources'/(key+'.json'))
        nums=[r['cpu_seconds'],r['wall_seconds'],r['rss_at_end']]
        if not np.isfinite(nums).all() or min(nums)<0 or r['rss_at_end']>4*1024**3 or r['scientific_retries']!=0:
            raise ValueError('Invalid prior resource account')
        previous.append(r['cpu_seconds'])
    if sum(previous)>=14400:raise ValueError('Exhausted prior resource account')

def execute_locked(root,phase,index,auth):
    verify_freeze(root,auth); e,pairs,lbs,candidates=config(root,phase)
    execution_boundary(root)
    if index<0 or index>=e['n']:raise ValueError('Realization outside frozen budget')
    spec=bank(phase)[index]; key=spec['id']
    # Atomic attempt claim disallows repeats even if an optimizer was interrupted.
    write(root/'attempts'/(key+'.json'),dict(spec=spec,source_hashes=pins(),state='STARTED'))
    start=time.monotonic()
    try:
        watchdog(root); generated=fixture(spec)
        for contract in [s for s in e['stages'] if s['id'].startswith(key+'/')]:
            reg=contract['id'].split('/')[1]; folder=root/'worlds'/contract['id']; folder.mkdir(parents=True)
            components(key,reg,generated[reg],contract,folder,pairs,lbs)
        cpu=sum(psutil.Process().cpu_times()[:2])
        write(root/'resources'/(key+'.json'),dict(cpu_seconds=cpu,wall_seconds=time.monotonic()-start,rss_at_end=psutil.Process().memory_info().rss,scope='entire fitting process CPU; end RSS not peak; watchdog samples cap',scientific_retries=0))
        write(root/'complete'/(key+'.json'),dict(state='COMPLETE',spec=spec))
    except BaseException as error:
        # Preserve partial CPU even on ordinary exceptions/KeyboardInterrupt.
        # Hard termination can bypass this handler: the unmatched attempt still
        # blocks every later index even if someone removes execution.lock.
        measured=None; measurement_error=None
        try:
            proc=psutil.Process(); measured=sum(proc.cpu_times()[:2])
            if not np.isfinite(measured) or measured<0:raise ValueError('Invalid failed-process CPU')
            if not (root/'resources'/(key+'.json')).exists():
                write(root/'resources'/(key+'.json'),dict(cpu_seconds=measured,wall_seconds=time.monotonic()-start,rss_at_end=proc.memory_info().rss,scope='failed process CPU measured at exception; teardown unmeasured',scientific_retries=0,state='FAILED'))
        except BaseException as accounting_error:
            measured=None;measurement_error=repr(accounting_error)
        write(root/'EXECUTION_FAILURE.json',dict(state='INCOMPLETE',realization=key,error=repr(error),cpu_seconds_measured=measured,expenditure_status='PARTIALLY_MEASURED' if measured is not None else 'UNRESOLVED',accounting_error=measurement_error,retry_or_replacement_allowed=False))
        raise

def replay(root,phase):
    e,pairs,lbs,candidates=config(root,phase); out=[]
    for spec in bank(phase)[:e['n']]:
        if read(root/'complete'/(spec['id']+'.json'))!=dict(state='COMPLETE',spec=spec):raise ValueError('Completion identity mismatch')
        if read(root/'attempts'/(spec['id']+'.json'))['source_hashes']!=pins():raise ValueError('Attempt source mismatch')
        resource=read(root/'resources'/(spec['id']+'.json'))
        nums=[resource['cpu_seconds'],resource['wall_seconds'],resource['rss_at_end']]
        if not np.isfinite(nums).all() or min(nums)<0 or resource['rss_at_end']>4*1024**3 or resource['scientific_retries']!=0:raise ValueError('Invalid resource receipt')
        rows={}
        for c in [s for s in e['stages'] if s['id'].startswith(spec['id']+'/')]:
            rows[c['id'].split('/')[1]]=verify_stage(root/'worlds'/c['id'],c,candidates,lbs)
        if set(rows)!=set(REGIMES):raise ValueError('Missing regime')
        out.append(rows)
    if sum(read(p)['cpu_seconds'] for p in root.glob('resources/*.json'))>14400 or (root/'RESOURCE_STOP.json').exists():raise ValueError('Resource ceiling exceeded')
    return out

def factorial_table(scores):
    factorial=[]
    for i,world in enumerate(scores):
        for r in REGIMES:
            for pair in PAIRS:
                b=world[r][f'B3_{pair["lb"]}']['loss']; m=world[r][pair['id']+'_w4']['loss']
                factorial.append(dict(world=bank('dev')[i]['id'],regime=r,pair=pair,matched_B3_loss=b,M1_loss=m,matched_gain=b-m))
    return factorial

def selection(root,auth):
    verify_freeze(root,auth); scores=replay(root,'dev'); decision=select(scores)
    write(root/'development_scores.json',scores)
    write(root/'development_factorial.json',factorial_table(scores))
    write(root/'selection.json',decision)
    if decision['state']=='SELECTED':
        write(root/'confirmation_expected.json',expected('confirmation',decision['confirmation_n'],decision['selected'],decision['common_lb']))
        write(root/'selection_freeze.json',dict(selection_hash=digest(root/'selection.json'),development_hash=digest(root/'development_scores.json'),expected_hash=digest(root/'confirmation_expected.json'),source_hashes=pins()))
    else:write(root/'stop.json',dict(state='VERIFIED_DECLARED_EARLY_STOP',reason=decision['state'],qualification=False,development_worlds=DEV_N,development_hash=digest(root/'development_scores.json'),selection_hash=digest(root/'selection.json')))

def verify_selection(root):
    s=read(root/'selection.json'); scores=replay(root,'dev');actual=select(scores)
    if s!=actual or read(root/'development_scores.json')!=scores or read(root/'development_factorial.json')!=factorial_table(scores):raise ValueError('Selection replay differs')
    if s['state']=='SELECTED':
        f=read(root/'selection_freeze.json')
        if f!=dict(selection_hash=digest(root/'selection.json'),development_hash=digest(root/'development_scores.json'),expected_hash=digest(root/'confirmation_expected.json'),source_hashes=pins()):raise ValueError('Selection freeze changed')
    return s

def distributions(scores,s):
    c=s['selected']['id']; lb=s['common_lb']; report={}
    for r in REGIMES:
        harm=[]; schedules=[]; persons=[]; cb=[]; bb=[]
        for x in scores:
            a=x[r][c]; b=x[r][f'B3_{lb}']; source=x[r]['B2']
            harm.append(a['loss']-b['loss']); cb.append(a['loss']-source['loss']); bb.append(b['loss']-source['loss'])
            schedules.extend([u['loss']-v['loss'] for u,v in zip(a['schedules'],b['schedules'])])
            persons.extend((np.array(a['person_losses'])-b['person_losses']).tolist())
        def dist(v):return dict(values=v,mean=float(np.mean(v)),quantiles=np.quantile(v,[0,.25,.5,.75,.9,.95,1]).tolist(),fraction_positive=float(np.mean(np.array(v)>0)),fraction_over_tolerance=float(np.mean(np.array(v)>.01)))
        report[r]=dict(realizations=dist(harm),schedules=dist(schedules),persons=dist(persons),candidate_minus_source_blind=dist(cb),common_B3_minus_source_blind=dist(bb),independence_unit='realization only')
        sensitivity=[]
        for x in scores:
            gap=x[r][f'B3_{lb}']['loss']-x[r]['oracle_loss']; gain=x[r][f'B3_{lb}']['loss']-x[r][c]['loss']; den=x[r]['contrast_den']
            sensitivity.append(dict(gain=gain,oracle_gap=gap,scaled_recovery=gain/gap if gap>FLOOR else None,contrast_nrmse=math.sqrt(x[r][c]['contrast_mse']/den) if den>FLOOR else None,contrast_error_rms=math.sqrt(x[r][c]['contrast_mse']),gate_role='descriptive only' if r in REGIMES[3:] else 'primary metrics reported separately'))
        report[r]['sensitivity']=sensitivity
    return report

def verify(root,auth):
    if (root/'execution.lock').exists():raise ValueError('Execution still active or interrupted')
    if (root/'RESOURCE_STOP.json').exists():raise ValueError('Resource stop cannot qualify')
    if (root/'EXECUTION_FAILURE.json').exists():raise ValueError('Failed execution cannot qualify')
    verify_freeze(root,auth); before={p.relative_to(root).as_posix():digest(p) for p in root.rglob('*') if p.is_file()}; s=verify_selection(root)
    if s['state']!='SELECTED':
        stop=read(root/'stop.json')
        if stop!=dict(state='VERIFIED_DECLARED_EARLY_STOP',reason=s['state'],qualification=False,development_worlds=DEV_N,development_hash=digest(root/'development_scores.json'),selection_hash=digest(root/'selection.json')):raise ValueError('Invalid stop evidence')
        if any((root/'attempts').glob('confirmation*')):raise ValueError('Confirmation after stop')
        result=stop
    else:
        scores=replay(root,'confirmation'); result=confirm(scores,s)
        result.update(audit_state='VERIFIED_COMPLETE',distributions=distributions(scores,s),scores=scores)
    # Exact world and attempt inventories: extra/missing stages cannot qualify.
    ids=[x['id'] for x in bank('dev')]
    if s['state']=='SELECTED':ids += [x['id'] for x in bank('confirmation')[:s['confirmation_n']]]
    if {p.stem for p in (root/'attempts').glob('*.json')}!=set(ids) or {p.stem for p in (root/'complete').glob('*.json')}!=set(ids):raise ValueError('Exact realization inventory mismatch')
    if {p.stem for p in (root/'resources').glob('*.json')}!=set(ids):raise ValueError('Exact resource inventory mismatch')
    if {p.relative_to(root/'worlds').as_posix() for p in (root/'worlds').glob('*/*') if p.is_dir()}!={i+'/'+r for i in ids for r in REGIMES}:raise ValueError('Exact world inventory mismatch')
    after={p.relative_to(root).as_posix():digest(p) for p in root.rglob('*') if p.is_file()}
    if before!=after:raise ValueError('Replay mutated evidence')
    # The original audit receipt is not part of its own scientific evidence.
    # Repeat audits recompute everything and compare, never replace that receipt.
    result['evidence_hashes']={k:v for k,v in before.items() if k!='verification.json'}
    receipt=root/'verification.json'
    if receipt.exists():
        if read(receipt)!=result:raise ValueError('Existing verification receipt differs from replay')
    else:write(receipt,result)
    return result

def main():
    p=argparse.ArgumentParser(); p.add_argument('stage',choices=['freeze','execute','select','verify','all','contracts']);p.add_argument('--root',type=Path);p.add_argument('--authorization',type=Path);p.add_argument('--phase',choices=['dev','confirmation']);p.add_argument('--index',type=int)
    a=p.parse_args()
    if a.stage=='contracts':print(json.dumps(expected('dev',DEV_N),indent=2));return
    if a.root is None or a.authorization is None:raise ValueError('Root and authorization required')
    a.root=a.root.resolve()
    if a.root==ROOT or ROOT in a.root.parents:raise ValueError('Raw artifacts must stay outside repository')
    if a.stage=='freeze':freeze(a.root,a.authorization)
    elif a.stage=='execute':
        if a.phase=='confirmation':verify_selection(a.root)
        execute(a.root,a.phase,a.index,a.authorization)
    elif a.stage=='select':selection(a.root,a.authorization)
    elif a.stage=='verify':verify(a.root,a.authorization)
    else:
        if not (a.root/'freeze.json').exists():freeze(a.root,a.authorization)
        execution_boundary(a.root)
        for phase in ['dev','confirmation']:
            if phase=='confirmation':
                if not (a.root/'selection.json').exists():selection(a.root,a.authorization)
                if verify_selection(a.root)['state']!='SELECTED':break
            e,*_=config(a.root,phase)
            for i,spec in enumerate(bank(phase)[:e['n']]):
                if (a.root/'complete'/(spec['id']+'.json')).exists():continue
                env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
                subprocess.run([sys.executable,__file__,'execute','--root',str(a.root),'--authorization',str(a.authorization),'--phase',phase,'--index',str(i)],check=True,env=env)
        verify(a.root,a.authorization)

if __name__=='__main__':main()
