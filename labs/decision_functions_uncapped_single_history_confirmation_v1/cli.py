"""Single real/mock dispatcher; mocks never import the scientific executor."""
from common import *
def mock_execute(out,scenario):
    from boundary import run
    import scipy.optimize
    def forbidden(*a,**k):raise AssertionError('Mock optimizer invoked')
    scipy.optimize.minimize=forbidden
    out.mkdir(parents=True,exist_ok=False)
    def work(progress):
        if scenario=='child-failure':raise RuntimeError('mock child failure')
        if scenario=='sleep':time.sleep(30)
        complete=scenario!='incomplete';progress['completed']=int(complete)
        axes=dict(integrity='PASS' if complete else 'INCOMPLETE',numerical='FAIL' if scenario=='numerical' else 'PASS',scientific='FAIL' if scenario=='scientific' else 'PASS',reason=None if scenario=='success' else scenario,qualified=scenario=='success')
        if scenario=='collision':axes['qualification']=True
        return axes
    run(out,dict(id='MOCK_ONLY',optimizer_stub=True),work,1)
def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('stage',choices=['prepare','preflight','seal','execute','verify','report','recover-report','mock']);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--private-root',type=Path);p.add_argument('--receipt',type=Path);p.add_argument('--scenario');a=p.parse_args();out=a.output_root.resolve()
    if a.stage in ('prepare','seal'):
        import prepare;getattr(prepare,a.stage)(out)
    elif a.stage=='preflight':
        import preflight;preflight.run(out,a.private_root)
    elif a.stage=='execute':
        require(a.private_root is not None,'Explicit private root required');import execution;execution.execute(out,a.private_root)
    elif a.stage=='verify':
        require(a.private_root is not None and a.receipt is not None,'Explicit roots/receipt required');import verify;verify.verify(out,a.private_root,a.receipt)
    elif a.stage in ('report','recover-report'):
        import reporting;reporting.report(out,a.receipt,recovery=a.stage=='recover-report')
    else:mock_execute(out,a.scenario)
if __name__=='__main__':main()
