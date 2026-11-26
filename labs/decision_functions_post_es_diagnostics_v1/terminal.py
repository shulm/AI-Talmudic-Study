"""Future-study terminal receipt: reports a verdict, never proves integrity."""
from common import *
def result(completed,expected,integrity,numerical,scientific,reason=None,confirmatory=False):
    allowed=('PASS','FAIL','INCOMPLETE','UNAVAILABLE','NOT_RUN')
    if any(x not in allowed for x in (integrity,numerical,scientific)):raise ValueError('Unknown status axis')
    complete=completed==expected
    return dict(completed_inventory=completed,expected_inventory=expected,inventory_complete=complete,artifact_integrity=integrity,numerical_status=numerical,scientific_status=scientific,failure_reason=reason,qualification=bool(confirmatory and complete and integrity==numerical==scientific=='PASS'),receipt_is_integrity_proof=False)
def publish(path,**kwargs):atomic(path,result(**kwargs))
def tests():
    tests={};expected=dict(attempts=384)
    for name,i,n,s,counts,reason in [('success','PASS','PASS','PASS',expected,None),('numerical_failure','PASS','FAIL','PASS',expected,'residual'),('scientific_failure','PASS','PASS','FAIL',expected,'scientific gate'),('incomplete_evidence','INCOMPLETE','NOT_RUN','NOT_RUN',dict(attempts=4),'missing files'),('resource_stop','INCOMPLETE','INCOMPLETE','NOT_RUN',dict(attempts=4),'resource ceiling')]:
        r=result(counts,expected,i,n,s,reason,confirmatory=True);assert r['qualification']==(name=='success');tests[name]=r
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'mock';p.write_bytes(b'original');binding=digest(p);p.write_bytes(b'corrupt');assert digest(p)!=binding;tests['corrupted_bytes_rejected']=True
        try:read(Path(td)/'missing.json')
        except FileNotFoundError:tests['missing_file_rejected']=True
        p=Path(td)/'terminal.json';publish(p,completed=expected,expected=expected,integrity='PASS',numerical='PASS',scientific='PASS',confirmatory=False)
        try:publish(p,completed=expected,expected=expected,integrity='PASS',numerical='PASS',scientific='PASS')
        except FileExistsError:tests['collision_rejected']=True
        assert read(p)['qualification'] is False
    return tests
