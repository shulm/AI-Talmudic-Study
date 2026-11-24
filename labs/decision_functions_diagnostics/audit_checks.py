"""Additional fail-closed record-field tests; no fits or evidence replacement."""
import tempfile
from core import *

def main():
    valid=dict(success=True,finite=True,message='toy convergence',iterations=1,objective=.5,gradient_max=1e-9,person_scaled_gradient_max=2e-9,parameter_count=6,parameter_norm=.1,feature_shape=[3,2],feature_norm=1.,cpu_seconds=.01,wall_seconds=.01)
    results=[]
    for mode in ['valid','empty','missing','nonconvergence','fields','identity','nonfinite','collision']:
        with tempfile.TemporaryDirectory() as tmp:
            expected={'a':meta('toy',.1,people=2)}; ledger=Ledger('case',expected,Path(tmp))
            if mode!='empty': ledger.start('a',expected['a'])
            r=valid.copy()
            if mode=='nonconvergence': r['success']=False
            if mode=='fields': del r['iterations']
            if mode=='nonfinite': r['gradient_max']=None
            if mode not in ['empty','missing']: ledger.complete('a',r)
            if mode=='identity': ledger.expected={'a':meta('toy',10.,people=2)}
            try:
                if mode=='collision': ledger.complete('a',valid)
                else: ledger.validate()
                accepted=True
            except (ValueError,FileExistsError,TypeError): accepted=False
            assert accepted==(mode=='valid'),mode
            results.append(dict(case=mode,accepted=accepted))
    actual={}
    for stage in ['synthetic','human_certificate']:
        path=OUT/'records'/stage; actual[stage]=validate_records(path,read(path/'expected.json'))
    receipt('audit_validation.json',dict(status='PASS',failure_paths=results,actual_ledgers=actual,original_pilot_state='RECOVERED_SELECTION_ONLY; original convergence logs remain unavailable'))
    print('PASS',actual)

if __name__=='__main__': main()
