"""Full temporary pipeline test with zero-parameter stubs and legacy-only data. Zero optimizer calls."""
import tempfile
from unittest.mock import patch
from contracts import *
import execute
import verify
from fixture import generate

def mock_solve(ledger,key,shape,features):
 ledger.start(key,ledger.expected[key]);x=np.zeros(shape);path=ledger.parameter_root/(key+'.npy');path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('xb') as f:np.save(f,x.ravel())
 ledger.complete(key,dict(success=True,finite=True,message='ZERO-FIT TEST STUB; not scientific evidence',iterations=0,objective=1.,gradient_max=0.,person_scaled_gradient_max=0.,parameter_count=x.size,parameter_norm=0.,feature_shape=list(features.shape),feature_norm=float(np.linalg.norm(features)),cpu_seconds=0.,wall_seconds=0.))
 return x
def stub_fit(z,y,base,rank,rho,lb,seed,ledger,key):
 mock_solve(ledger,key,(3*rank*z.shape[1]+len(y)*rank+len(y)*3,),z);return np.zeros((3,rank,z.shape[1]))
def stub_adapt(z,y,base,rho,lb,v,ledger,key):return mock_solve(ledger,key,(len(y),3+(0 if v is None else v.shape[1])),z)
def main():
 with tempfile.TemporaryDirectory() as temp:
  out=Path(temp)/'out';private=Path(temp)/'private';out.mkdir();private.mkdir()
  for name in ['PROTOCOL.json','EXPECTED.json','preflight.json']:atomic(out/name,read(OUT/name))
  atomic(out/'prefit_sources.json',dict(files={}));atomic(out/'publication.json',dict(test_stub=True))
  with patch.object(execute,'generate',side_effect=lambda *_:generate(20261125,2718)),patch.object(execute,'fit',side_effect=stub_fit),patch.object(execute,'adapt',side_effect=stub_adapt):
   for r in REAL:execute.run(r,private,out)
  verify.verify(private,out);r=read(out/'verification.json');assert r['state']=='VERIFIED_COMPLETE' and r['qualification'] is False
  atomic(OUT/'integration_preflight_final.json',dict(status='PASS',scientific_optimizer_calls=0,legacy_only_generator_seeds=[20261125,2718],no_fresh_C_D_labels_scored=True,temporary_stub_records=196,expected_comparison_count=expected_comparison_count(),actual_comparison_count=r['comparison_count'],maximum_discrepancy=r['maximum_discrepancy'],complete_failure_does_not_qualify=True))
 print('PASS full zero-fit integration',flush=True)
if __name__=='__main__':main()
