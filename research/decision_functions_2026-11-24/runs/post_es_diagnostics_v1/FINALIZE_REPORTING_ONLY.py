"""Versioned reporting-only completion adapter; no solve or prediction functions.

The frozen executor completed all analysis and engineering, then its final dict()
duplicated the qualification keyword. Preserve that failed command and original
source. This adapter repairs only the new run's missing terminal serialization.
It must never be used to create PR20's missing scientific summary.
"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'labs/decision_functions_post_es_diagnostics_v1'))
from common import *
import terminal
def compose(metadata=None,**kwargs):
    result=terminal.result(**kwargs)
    if set(result)&set(metadata or {}):raise ValueError('Metadata cannot overwrite terminal axes')
    result.update(metadata or {});return result
def tests():
    checks={}
    for name,i,n,s,c in [('success','PASS','PASS','PASS',384),('numerical_failure','PASS','FAIL','PASS',384),('scientific_failure','PASS','PASS','FAIL',384),('incomplete_evidence','INCOMPLETE','NOT_RUN','NOT_RUN',4),('resource_stop','INCOMPLETE','INCOMPLETE','NOT_RUN',4)]:
        x=compose(metadata=dict(path=name),completed=dict(attempts=c),expected=dict(attempts=384),integrity=i,numerical=n,scientific=s,reason=None if name=='success' else name,confirmatory=True)
        assert x['qualification']==(name=='success');checks[name]=x
    try:compose(metadata=dict(qualification=True),completed={},expected={},integrity='FAIL',numerical='FAIL',scientific='NOT_RUN')
    except ValueError:checks['duplicate_axis_override_rejected']=True
    else:raise AssertionError('Overwrite allowed')
    return checks
if __name__=='__main__':
    start=time.process_time();frozen();private=Path('C:/Users/David/.cache/decision_functions/evidence_shrinkage_v1');before=verify_inputs(private)
    ee=attempts();exact([p.name.removesuffix('.complete.json') for p in (OUT/'attempts').glob('*.complete.json')],ee)
    exact([p.name.removesuffix('.start.json') for p in (OUT/'attempts').glob('*.start.json')],ee)
    wrappers_done=list((OUT/'wrappers').glob('*.complete.json'));assert len(wrappers_done)==114
    eng=read(OUT/'engineering_checks.json');man=read(OUT/'DIAGNOSTIC_MANIFEST.json')
    assert man['residual_rows']==1664 and man['table_rows']==16 and man['aggregate_rows']==8
    original_receipts=[read(p) for p in (OUT/'commands').glob('*.complete.json')];failed=[r for r in original_receipts if r['exit_code']!=0]
    assert len(failed)==1
    evidence=dict(recovery='REPORTING_ONLY_AFTER_ALL_ATTEMPTS',original_error="TypeError: dict() got multiple values for keyword argument 'qualification'",original_failed_commands=failed,frozen_scientific_sources_unchanged=True,solver_invocations_in_recovery=0,diagnostic_recalculations_in_recovery=0,adapter_sha256=digest(__file__),tests=tests())
    atomic(OUT/'REPORTING_RECOVERY.json',evidence)
    t=compose(completed=dict(attempts=384,wrappers=114),expected=dict(attempts=384,wrappers=114),integrity='NOT_RUN',numerical='PASS' if eng['passed'] else 'FAIL',scientific='NOT_RUN',reason=None if eng['passed'] else 'ENGINEERING_CRITERION_FAILED',metadata=dict(axes=dict(diagnostic='COMPLETE',engineering='PASS' if eng['passed'] else 'FAIL',ablation='DESCRIPTIVE_COMPLETE'),historical_status='INCOMPLETE / NUMERICALLY_UNRESOLVED',reporting_recovery='REPORTING_RECOVERY.json'))
    close(hashes(private),before);atomic(OUT/'EXECUTION_TERMINAL.json',t)
    print(json.dumps(dict(terminal_written=True,engineering=eng['passed'],cpu_seconds=time.process_time()-start,scientific_qualification=False)))
