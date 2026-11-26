"""Zero-optimizer derivative/value and failure-path tests only."""
from common import *
from suite import fixture,derivative_checks
import terminal
def run():
    f=fixture();der=derivative_checks(f)
    if not der['passed']:raise ValueError('Derivative checks failed')
    tests=terminal.tests()
    tests['no_query_labels']=not any('query_y' in k for k in f)
    assert tests['no_query_labels']
    assert len(wrappers())==114 and len(attempts())==384 and len(expected()['residual_row_ids'])==1664
    # Static failure tests: no formal solver calls or private scientific calculations.
    for key,fn in [('missing_ids',lambda:exact([],['a'])),('duplicate_ids',lambda:exact(['a','a'],['a'])),('nonfinite',lambda:close(np.array([np.nan]),np.zeros(1))),('wrong_shape',lambda:close(np.zeros(2),np.zeros(3))),('bad_value',lambda:close(0.,1.))]:
        try:fn()
        except ValueError:tests[key]=True
        else:raise AssertionError(key)
    return dict(passed=True,optimizer_calls=0,derivatives=der,terminal_tests=tests,fixture_sha256=sha((json.dumps({k:v.tolist() for k,v in f.items()},indent=2)+'\n').encode()))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path,required=True);a=p.parse_args();start=time.process_time()
    try:r=run();r['cpu_seconds']=time.process_time()-start;atomic(a.receipt,r)
    except BaseException as e:atomic(a.receipt,dict(passed=False,optimizer_calls=0,error=repr(e),cpu_seconds=time.process_time()-start));raise
