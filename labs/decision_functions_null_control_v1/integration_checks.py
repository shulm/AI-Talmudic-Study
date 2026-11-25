"""Mocked complete development-stop integration; never a scientific run."""
import copy
import sys
import tempfile
import time
from unittest.mock import patch
import scipy.optimize
from scipy.special import softmax
from design import *
import run
import engine
import design
sys.path.insert(0,str(ROOT/'labs/decision_functions_short_history_v1'))
import head

def analytic_fixture(spec):
    angles=np.tile(np.arange(3)*2*np.pi/3,64);z=np.column_stack([np.cos(angles),np.sin(angles)])
    base=np.zeros((192,3));y=np.tile(np.arange(192)%3,(96,1));p=np.full((96,192,3),1/3)
    tr=np.arange(120);su=np.arange(96);qu=np.arange(156,192)
    d=dict(oracle=p[72:][:,qu],query_y=y[72:][:,qu],query_ids=qu,support_ids=su,train_ids=tr,support_y=y[72:][:,su],support_z=z[su],support_base=base[su],train_y=y[:48][:,tr],train_z=z[tr],train_base=base[tr],query_z=z[qu],query_base=base[qu],source_y=y,source_oracle=p,source_z=z,source_base=base)
    out={}
    for j,r in enumerate(REGIMES):
        out[r]=copy.deepcopy(d)
        marker=int(spec['id'][-3:])*.001+j*.00001
        for k in ['source_base','train_base','support_base','query_base']:out[r][k].fill(marker)
    return out

def mock_record(ledger,key,n,z):
    ledger.start(key,ledger.expected[key]);x=np.zeros(n);path=ledger.parameter_root/(key+'.npy');path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:np.save(f,x)
    ledger.complete(key,dict(success=True,finite=True,message='MOCK ZERO FIT',iterations=0,objective=0.,gradient_max=0.,person_scaled_gradient_max=0.,parameter_count=n,parameter_norm=0.,feature_shape=list(z.shape),feature_norm=float(np.linalg.norm(z)),cpu_seconds=0.,wall_seconds=0.))
    return x

def mock_fit(z,y,base,rank,rho,lb,seed,ledger,key):
    mock_record(ledger,key,12+len(y)*5,z);return np.zeros((3,2,2))

def mock_adapt(z,y,base,rho,lb,v,ledger,key):
    shape=(len(y),3 if v is None else 5);return mock_record(ledger,key,int(np.prod(shape)),z).reshape(shape)

def mock_shared(*args):return (lambda x:(0.,np.zeros_like(x))),lambda x:(x[:12].reshape(3,2,2),None,None),None
def mock_personal(*args):return (lambda x:(0.,np.zeros_like(x))),None

def main():
    start=time.process_time();checks=[]
    with tempfile.TemporaryDirectory(prefix='null_control_mock_') as td:
        root=Path(td)/'run';auth=Path(td)/'auth.json';write(auth,dict(mock_only=True))
        def invoke(args,**kwargs):
            with patch.object(sys,'argv',args[1:]):run.main()
        with patch.object(design,'DEV_N',2),patch.object(design,'MIN_N',2),patch.object(design,'MAX_N',2),patch.object(run,'DEV_N',2),patch.object(scipy.optimize,'minimize',side_effect=AssertionError('Scientific optimizer forbidden')),patch.object(head,'minimize',side_effect=AssertionError('Scientific optimizer forbidden')),patch.object(head,'fit',mock_fit),patch.object(head,'adapt',mock_adapt),patch.object(head,'shared_objective',mock_shared),patch.object(head,'personal_objective',mock_personal),patch.object(run,'fixture',analytic_fixture),patch.object(engine,'fixture',side_effect=AssertionError('Fresh generator forbidden')),patch.object(run,'authorize',return_value=dict(mock_only=True)),patch.object(run,'watchdog',return_value=None),patch.object(run.subprocess,'run',side_effect=invoke):
            with patch.object(sys,'argv',['run.py','all','--root',str(root),'--authorization',str(auth)]):run.main()
            result=read(root/'verification.json')
            assert result['state']=='VERIFIED_DECLARED_EARLY_STOP' and result['qualification'] is False
            assert len(list((root/'complete').glob('*.json')))==2
            checks.append('Full all orchestrator: reduced MOCK2x6 stages, exact ledgers, selection, complete no-candidate stop and replay')
            e,pairs,lbs,candidates=run.config(root,'dev');c=e['stages'][0];folder=root/'worlds'/c['id']
            original=(folder/'manifest.json').read_bytes()
            # Each corruption is isolated, tested, then restored in temporary mock data.
            for target in [folder/'components.npz',folder/'records/fits'/(c['records'][0]+'.complete.json'),folder/'parameters'/(c['records'][0]+'.npy')]:
                backup=target.read_bytes();target.unlink()
                try:engine.verify_stage(folder,c,candidates,lbs)
                except (ValueError,FileNotFoundError):checks.append('Missing '+target.name+' rejected')
                else:raise AssertionError('Missing evidence accepted')
                target.write_bytes(backup)
            m=read(folder/'manifest.json');m['contract']['records'].append('duplicate')
            (folder/'manifest.json').write_text(json.dumps(m))
            try:engine.verify_stage(folder,c,candidates,lbs)
            except ValueError:checks.append('Changed exact contract rejected')
            else:raise AssertionError('Changed contract accepted')
            (folder/'manifest.json').write_bytes(original)
            # No successful-looking flag may authorize confirmation after a stop.
            try:run.config(root,'confirmation')
            except ValueError:checks.append('Confirmation after no-candidate stop rejected')
            else:raise AssertionError('Confirmation after stop accepted')
            # Full selected-confirmation branch on reduced mocked counts.
            actual_score=engine.score_arrays
            def fake_scores(a,candidates,lbs):
                row=actual_score(a,candidates,lbs);marker=int(round(a['query_base'][0,0]*100000));i=marker//100;j=marker%100
                row['oracle_loss']=.3;row['contrast_den']=10.
                for key,v in row.items():
                    if not isinstance(v,dict):continue
                    loss=1.+(.002 if key=='B3_0.1' else 0)
                    if key.startswith('p'):loss=1.+(.001 if j<2 else -.4)+(i-.5)*.0001
                    v['loss']=loss;v['contrast_mse']=.1;v['person_losses']=[loss]*24
                    for s in v['schedules']:s['loss']=loss;s['person_losses']=[loss]*24;s['contrast_mse']=.1
                return row
            root2=Path(td)/'selected'
            with patch.object(engine,'score_arrays',side_effect=fake_scores),patch.object(sys,'argv',['run.py','all','--root',str(root2),'--authorization',str(auth)]):run.main()
            result=read(root2/'verification.json')
            assert result['state']=='COMPLETE_PREDICTIVE_SUCCESS' and result['audit_state']=='VERIFIED_COMPLETE'
            assert len(list((root2/'complete').glob('*.json')))==4
            checks.append('Full selected-confirmation orchestrator with MOCK2 development+2 confirmation worlds and fabricated score responses; replay/selection freeze/verification passed')
            (root2/'resources/confirmation000.json').unlink()
            try:run.replay(root2,'confirmation')
            except FileNotFoundError:checks.append('Missing resource receipt rejected')
            else:raise AssertionError('Missing resource receipt accepted')
            write(root2/'RESOURCE_STOP.json',dict(mock=True))
            try:run.execute(root2,'confirmation',1,auth)
            except ValueError:checks.append('Previous resource stop rejects execution before fits')
            else:raise AssertionError('Resource stop accepted')
            write(root2/'execution.lock',dict(mock=True))
            try:run.verify(root2,auth)
            except ValueError:checks.append('Outstanding execution lock rejects final verification')
            else:raise AssertionError('Outstanding lock accepted')
    write(PACKAGE/'MOCK_INTEGRATION_CHECKS.json',dict(status='PASS',checks=checks,scientific_fits=0,fresh_generator_calls=0,human_evaluations=0,mock_design='2 development worlds; selected branch adds2 confirmation worlds; real 12/24-96 counts separately checked analytically',python_cpu_seconds=time.process_time()-start,source_hashes={p.name:digest(p) for p in Path(__file__).parent.glob('*.py')},limitations='Fit/adapt/objective replay replaced by analytic mocks; selected-path scores fabricated. Tests orchestration and evidence integrity, not predictive success, optimizer convergence or statistical coverage. Real finite-difference objective separately checked.'))

if __name__=='__main__':main()
