"""Post-run observation only: retain reached frozen-verifier checks on failure.
Does not alter comparisons, create missing scientific evidence, fit, or qualify a run.
"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'labs/decision_functions_evidence_shrinkage_v1'))
from contracts import *
import verify
private=Path('C:/Users/David/.cache/decision_functions/evidence_shrinkage_v1')
before={p.relative_to(private).as_posix():file_hash(p) for p in private.rglob('*') if p.is_file()}
original=verify.Checker;captured=[]
class Observed(original):
    def __init__(self):super().__init__();captured.append(self)
verify.Checker=Observed
start=time.process_time();error=None
try:verify.verify(private,OUT)
except Exception as e:error=repr(e)
finally:verify.Checker=original
after={p.relative_to(private).as_posix():file_hash(p) for p in private.rglob('*') if p.is_file()}
assert before==after
checks=captured[0].results
assert set(checks)<=set(comparison_ids())
atomic(OUT/'partial_replay_capture.json',dict(state='INCOMPLETE',qualification=False,exception=error,observer='Only captures existing Checker instances; frozen verify.py and all scientific code unchanged. No missing summary is supplied.',reached_comparisons=len(checks),declared_comparisons=len(comparison_ids()),missing_comparison_ids=sorted(set(comparison_ids())-set(checks)),max_abs=max(x['max_abs'] for x in checks.values()),checks=checks,private_hashes_before_after=before,hashes_unchanged=True,cpu_seconds=time.process_time()-start,observer_sha256=file_hash(__file__),frozen_verifier_sha256=file_hash(ROOT/'labs/decision_functions_evidence_shrinkage_v1/verify.py')))
print({'reached':len(checks),'missing':sorted(set(comparison_ids())-set(checks)),'max_abs':max(x['max_abs'] for x in checks.values()),'state':'INCOMPLETE'})
