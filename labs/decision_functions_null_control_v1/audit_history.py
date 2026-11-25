"""Read-only public arithmetic and compact original-array replay receipt."""
import subprocess
import time
from design import *

def main():
    start=time.process_time();out=ROOT/'research/decision_functions_2026-11-24/runs/short_history_v1'
    summary=read(out/'results_summary.json');verified=read(out/'verification.json');sources=read(out/'prefit_sources.json')
    checked={}
    for f,h in sources['files'].items():
        if digest(ROOT/f)!=h:raise ValueError('Historical source changed')
        checked[f]=h
    for name in ['RESULTS.md','NEXT_HANDOFF.md','PROTOCOL.json','EXPECTED.json','results_summary.json','verification.json','RESOURCE_USAGE_FINAL.json','prefit_sources.json','delivery_audit.json']:
        path=out/name
        pinned=subprocess.check_output(['git','show',BASE+':'+path.relative_to(ROOT).as_posix()],cwd=ROOT)
        if path.read_bytes()!=pinned:raise ValueError('Pinned public evidence changed')
        checked[path.relative_to(ROOT).as_posix()]=digest(path)
    values={};allg={}
    expected_numbers={'C':[.594196396265,.863611274630,.283460783779,.052185645516],'D':[.602815011497,.877918026354,.248433285313,.057411041409]}
    for real in ['C','D']:
        score=read(out/(real+'_scores.json'))
        if summary['results'][real]!=score:raise ValueError('Summary score mismatch')
        g=score['gates']['primary'];v=g['values'];values[real]=v
        tests=dict(gain=v['gain']>=.05,recovery=v['recovery']>=.5,contrast=v['contrast']<=.5,null=v['null']<=.01)
        if tests!=g['passed'] or tests!=verified['primary_gates'][real] or tests!=summary['primary_gates'][real]:raise ValueError('Gate conjunction mismatch')
        for key,want in zip(['gain','recovery','contrast','null'],expected_numbers[real]):
            if abs(v[key]-want)>5e-13:raise ValueError('Report scalar mismatch')
        allg[real]=tests
    qualification=verified['state']=='VERIFIED_COMPLETE' and verified['numerical_pass'] and all(all(g.values()) for g in allg.values())
    if qualification or summary['qualification'] or summary['status']!='COMPLETED_PRIMARY_FAILURE':raise ValueError('Failure relabeled')
    ex=read(out/'EXPECTED.json')['ledgers'];records=[]
    for stage,expected_rows in ex.items():
        actual=list((out/'records'/stage).glob('*.complete.json'))
        if {p.name.removesuffix('.complete.json') for p in actual}!=set(expected_rows):raise ValueError('Historical exact records mismatch')
        records.extend(read(p) for p in actual)
    if len(records)!=196 or sum(r['meta']['person_solves'] for r in records)!=3776:raise ValueError('Historical counts mismatch')
    write(PACKAGE/'PUBLIC_EVIDENCE_AUDIT.json',dict(state='PASS',base=BASE,checked_files=checked,primary_values=values,primary_gates=allg,qualification=False,records=196,person_solves=3776,python_cpu_seconds=time.process_time()-start,scope='Public arithmetic/identity and historical ledger checks, no refit'))
    replay=Path('C:/Users/David/.cache/decision_functions/short_history_null_control_v1_historical_replay/verification.json');v=read(replay)
    if v['state']!='VERIFIED_COMPLETE' or v['private_before']!=v['private_after'] or v['comparison_count']!=17038:raise ValueError('Historical replay incomplete')
    write(PACKAGE/'HISTORICAL_REPLAY.json',dict(executed=True,receipt_path=str(replay),receipt_sha256=digest(replay),verifier_sha256=digest(ROOT/'labs/decision_functions_short_history_v1/verify.py'),state=v['state'],qualification=v['qualification'],numerical_pass=v['numerical_pass'],comparison_count=v['comparison_count'],maximum_discrepancy=v['maximum_discrepancy'],private_bytes_unchanged=True,private_file_count=len(v['private_before']),scientific_fits=0,new_generator_calls=0,method='Unchanged historical verifier, fresh public receipt directory; original private cache read only'))
    doc=Path('C:/Users/David/Downloads/Individual_Decision_Research_Plan_2026-11-25.docx')
    write(PACKAGE/'INPUTS.json',dict(plan_document=dict(path=str(doc),sha256=digest(doc),interpretation='Proposed direction, not experimental evidence or execution authorization'),assignment=dict(path='C:/Users/David/.codex/attachments/f87c7477-f4e7-4e6c-89bd-eb91e34cfc68/Pasted text.txt',sha256=digest('C:/Users/David/.codex/attachments/f87c7477-f4e7-4e6c-89bd-eb91e34cfc68/Pasted text.txt')),coordination_issue='https://github.com/shulm/AI-Talmudic-Study/issues/2',read_only=True))

if __name__=='__main__':main()
