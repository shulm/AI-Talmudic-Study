"""Complete independent final-state checks; never invoke solve or historical executor."""
from common import *
from objective import independent,probability,error_bounds
from suite import inputs,derivative_checks,engineering_checks
import terminal
class Checks:
    def __init__(self):self.values={}
    def add(self,key,a,b,tol=1e-12):
        if key in self.values:raise ValueError('Duplicate check')
        self.values[key]=close(a,b,tol)
def scalar_metrics(p,y,o):
    en=nn=acc=br=0.;n=p.shape[0]*p.shape[1]
    for i in range(len(p)):
        for q in range(p.shape[1]):
            vals=p[i,q];en-=sum(float(o[i,q,c])*np.log(max(float(vals[c]),1e-12)) for c in range(3));nn-=np.log(max(float(vals[y[i,q]]),1e-12));acc+=int(np.argmax(vals)==y[i,q]);br+=sum((float(vals[c])-int(c==y[i,q]))**2 for c in range(3))
    return dict(expected_nll=en/n,sampled_nll=nn/n,accuracy=acc/n,brier=br/n)
def verify(private,derived,out):
    checks=Checks();frozen();checks.add('source',True,True);before=hashes(derived)
    available=read(out/'INPUT_BINDINGS.json')['availability']=='AVAILABLE'
    if available:
        old_before=verify_inputs(private);checks.add('inputs_before',old_before,read(out/'INPUT_HASH_RECEIPT.json')['before'])
        from diagnosis import calculate,old_forward
        from analysis import calculate as ablate
        close(old_forward(private),read(out/'HISTORICAL_FORWARD.json'))
        residual,data=calculate(private);exact([r['id'] for r in residual['rows']],expected()['residual_row_ids']);exact([r['id'] for r in residual['batch_comparisons']],expected()['batch_comparison_ids'])
        for row in residual['rows']:
            for k,s in expected()['residual_numeric_shapes'][row['model']].items():close(list(np.asarray(row[k]).shape),s)
        checks.add('diagnosis',residual,read(out/'RESIDUALS.json'))
        new,co,table=ablate(data,residual);saved=load(derived/'uncapped_predictions.npz');coeff=load(derived/'coefficients.npz');exact(list(saved),expected()['ablation_keys']);exact(list(coeff),expected()['coefficient_keys'])
        for k in saved:close(new[k],saved[k]);close(list(saved[k].shape),expected()['ablation_keys'][k])
        for k in co:
            if k.endswith('log_weight'):
                if not np.array_equal(np.isneginf(co[k]),np.isneginf(coeff[k])):raise ValueError('Log zero coefficient mismatch')
                ix=np.isfinite(co[k]);close(co[k][ix],coeff[k][ix])
            else:close(co[k],coeff[k])
            close(list(coeff[k].shape),expected()['coefficient_keys'][k])
        exact([r['id'] for r in table['rows']],expected()['stratum_rows']);exact([r['id'] for r in table['aggregates']],expected()['aggregate_rows'])
        for row in table['rows']:
            r,h=row['real'],row['history'];ev=data[r]['evaluator'];ix=ev['active'] if row['stratum']=='active' else ~ev['active']
            for m in ARMS:
                p=saved[f'{r}_{h}'] if m=='ES_UNCAPPED' else data[r]['predictions'][f'{h}_{m}'];scalar=scalar_metrics(p[ix],ev['y'][ix],ev['oracle'][ix]);close(scalar,{k:row['methods'][m][k] for k in scalar})
        checks.add('ablation',table,read(out/'ABLATION.json'))
        checks.add('inputs_after',hashes(private),old_before)
    else:
        for key in ('inputs_before','inputs_after','diagnosis','ablation'):checks.add(key,'PRIVATE_ARTIFACTS_UNAVAILABLE','PRIVATE_ARTIFACTS_UNAVAILABLE')
    fixture={k:np.array(v) for k,v in read(out/'FIXTURE.json').items()};checks.add('derivatives',derivative_checks(fixture),read(out/'DERIVATIVES.json'))
    arrays=load(derived/'engineering.npz');exact(list(arrays),expected()['engineering_arrays'])
    for k,v in arrays.items():close(list(v.shape),expected()['engineering_arrays'][k]);assert np.isfinite(v).all()
    records={};ee=attempts();exact([p.name.removesuffix('.start.json') for p in (out/'attempts').glob('*.start.json')],ee);exact([p.name.removesuffix('.complete.json') for p in (out/'attempts').glob('*.complete.json')],ee)
    if list((out/'attempts').glob('*.failure.json')):raise ValueError('Nonfinite/incomplete formal attempt')
    for key,spec in ee.items():
        start=read(out/'attempts'/(key+'.start.json'));r=read(out/'attempts'/(key+'.complete.json'));records[key]=r
        close(start['spec'],spec);close(r['spec'],spec)
        if start['fixture_hash']!=digest(out/'FIXTURE.json') or start['source_hash']!=digest(LAB/'solver.py'):raise ValueError('Attempt binding mismatch')
        prefix=spec['layout']+'_'+spec['model'];p=spec['person'];theta=arrays[prefix+'_theta'][p];a,g,y,d,q,qg=inputs(fixture,p,spec['model']);eb=error_bounds(theta,a,g,y,d,q);rr=eb['R'];pb=probability(theta,q,qg)
        close(pb,arrays[prefix+'_probabilities'][p]);close(rr,r['R_recomputed']);close(rr,r['R']);close(float(eb['K'].max()*rr),r['KR'])
        close(eb['K']*rr/2,r['probability_bounds']);close(np.sqrt(2)*eb['K']*rr,r['log_probability_bounds'])
        for t in r['trace']:
            val,grad=independent(np.array(t['theta']),a,g,y,d);close(val,t['objective']);close(float(np.linalg.norm(grad/np.sqrt(d))),t['R'])
        for t in r['guarded']:
            allowance=64*2.**-52*max(1,abs(t['J_old']));close(allowance,t['allowance']);assert 0<t['predicted_decrease']<=allowance and t['R_new']<t['R_old'] and t['J_new']<=t['J_old']+allowance
        passing=bool(r['success'] and rr<=1e-10 and r['KR']<=1e-8 and r['residual_agreement']);checks.add('engineering/'+key,passing,r['engineering_pass'])
    eng=engineering_checks(fixture,arrays,records);close(eng,read(out/'engineering_checks.json'))
    for m in ('B3','M1'):checks.add('layout/'+m,eng['checks'][m+'_layout_bitwise'],True)
    checks.add('terminal_tests',terminal.tests(),read(out/'TERMINAL_TESTS.json'))
    exact([p.name.removesuffix('.start.json') for p in (out/'wrappers').glob('*.start.json')],[w['id'] for w in wrappers()]);exact([p.name.removesuffix('.complete.json') for p in (out/'wrappers').glob('*.complete.json')],[w['id'] for w in wrappers()])
    for w in wrappers():close(read(out/'wrappers'/(w['id']+'.complete.json')),dict(**w,attempts=[f'{w["id"]}_p{p}' for p in w['people']]))
    complete=dict(attempts=len(records),wrappers=len(wrappers()));term=read(out/'EXECUTION_TERMINAL.json');close(term['completed_inventory'],complete);assert term['qualification'] is False
    files=['engineering.npz']+(['uncapped_predictions.npz','coefficients.npz'] if available else [])
    exact(list(before),files)
    if available:
        man=read(out/'DIAGNOSTIC_MANIFEST.json');close(man['files'],{n:digest(derived/n) for n in files if n!='engineering.npz'})
    close(read(out/'engineering_manifest.json')['hash'],digest(derived/'engineering.npz'))
    checks.add('inventory',complete,dict(attempts=384,wrappers=114))
    hist=read(out/'HISTORICAL_BLOBS.json');actual=subprocess.run(['git','hash-object','--stdin-paths'],input='\n'.join(hist)+'\n',cwd=ROOT,text=True,capture_output=True,check=True).stdout.splitlines();checks.add('preservation',dict(zip(hist,actual)),hist)
    after=hashes(derived);close(before,after);exact(list(checks.values),expected()['comparison_ids'])
    return dict(diagnostic_evidence='COMPLETE' if available else 'PRIVATE_ARTIFACTS_UNAVAILABLE',integrity='PASS',engineering='PASS' if eng['passed'] else 'FAIL',ablation='DESCRIPTIVE_COMPLETE' if available else 'UNAVAILABLE',historical_status='INCOMPLETE / NUMERICALLY_UNRESOLVED',scientific_qualification=False,comparison_count=len(checks.values),checks=checks.values,max_abs=max(checks.values.values()),derived_hashes_before_after=before,historical_private_hashes_unchanged=available,historical_blobs_unchanged=len(hist))
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--derived-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);p.add_argument('--receipt',type=Path,required=True);a=p.parse_args()
    if a.receipt.exists():raise FileExistsError('Fresh verification receipt required')
    try:r=verify(a.private_root,a.derived_root,a.output_root)
    except BaseException as e:atomic(a.receipt,dict(diagnostic_evidence='INCOMPLETE',integrity='FAIL',scientific_qualification=False,error=repr(e)));raise
    atomic(a.receipt,r)
