"""Zero-fit preflight. Never generates realization B."""
import importlib.util
import tempfile
from unittest.mock import patch
from types import SimpleNamespace
from core import *
from head import shared_objective,personal_objective,certificate,ce,solve
from study import *
from verify import close,valid_probability,check_archive

def reject(fn):
 try:fn()
 except (ValueError,FileExistsError,FileNotFoundError,TypeError,KeyError):return
 raise AssertionError('Failure accepted')
def main():
 rng=np.random.default_rng(123);z=rng.normal(size=(5,2));y=rng.integers(0,3,(4,5));base=rng.normal(size=(5,3));x=rng.normal(size=32)*.1
 f,unpack,_=shared_objective(z,y,base,2,.01,.1);value,g=f(x);eps=1e-6
 fd=np.array([(f(x+np.eye(len(x))[j]*eps)[0]-f(x-np.eye(len(x))[j]*eps)[0])/(2*eps) for j in range(len(x))]);assert np.max(np.abs(fd-g))<1e-8
 v,u,b=unpack(x);p=rng.normal(size=20)*.1;pf,_=personal_objective(z,y,base,.01,.1,v);gv=pf(p)[1]
 fd2=np.array([(pf(p+np.eye(20)[j]*eps)[0]-pf(p-np.eye(20)[j]*eps)[0])/(2*eps) for j in range(20)]);assert np.max(abs(fd2-gv))<1e-8
 # General two-factor identity, training and adaptation; no optimize call.
 t=10.;vp=v/np.sqrt(t);up=u*np.sqrt(t);log=lambda vv,uu:base[None]+b[:,None]+np.einsum('sr,crd,nd->snc',uu,vv,z)
 close(log(v,u),log(vp,up));oldpen=.01/2*(np.sum(v*v)+np.sum(u*u)/4)+.1/8*np.sum(b*b);newpen=.1/2*np.sum(vp*vp)+.001/8*np.sum(up*up)+.1/8*np.sum(b*b);close(oldpen,newpen)
 pp=p.reshape(4,5);pps=pp.copy();pps[:,3:]*=np.sqrt(t)
 close(probabilities(z,base,pp,v),probabilities(z,base,pps,vp));close(.01*np.sum(pp[:,3:]**2),.001*np.sum(pps[:,3:]**2));close(f(x)[0],f(x)[0]);close(f(x)[1],f(x)[1])
 spec=importlib.util.spec_from_file_location('old_head',ROOT/'labs/decision_functions_diagnostics/head_v1.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
 for lam in [.001,.1,1,10]:
  f1=shared_objective(z,y,base,2,lam,lam)[0];f0=old.shared_objective(z,y,base,2,lam)[0];close(f1(x)[0],f0(x)[0]);close(f1(x)[1],f0(x)[1]);f1=personal_objective(z,y,base,lam,lam,v)[0];f0=old.personal_objective(z,y,base,lam,v)[0];close(f1(p)[0],f0(p)[0]);close(f1(p)[1],f0(p)[1])
 a=generate(20261126,2719);zz,bb,bias,uu,vv,sp,ys,ps=a
 assert zz.shape==(192,2) and bias.shape==(96,3);close(bias[::2],bias[1::2]);close(uu[::2],-uu[1::2])
 for s,n in [('train',120),('development',36),('test',36),('support',96)]:
  assert len(sp[s])==n
  assert all(sum(sp[s]//3==g)==3 for g in set(sp[s]//3))
 assert set(sp['support'])<=set(sp['train']);assert not set(sp['train'])&set(sp['test']);assert not set(sp['development'])&set(sp['test'])
 # Certificate: changing rho affects threshold only, not intercept uncertainty.
 c1=certificate(z,y,base,b,.01,.1);c2=certificate(z,y,base,b,.1,.1);close(c1['error_bound'],c2['error_bound']);close(c2['threshold'],10*c1['threshold'])
 records=dict(success=True,finite=True,message='mock',iterations=1,objective=.5,gradient_max=1e-9,person_scaled_gradient_max=2e-9,parameter_count=6,parameter_norm=.1,feature_shape=[5,2],feature_norm=1.,cpu_seconds=.01,wall_seconds=.01)
 tests=[]
 # Generator-equivalence check executes only the legacy generator definition.
 legacy=(ROOT/'labs/decision_functions_diagnostics/synthetic.py').read_text();scope={'np':np,'softmax':__import__('scipy').special.softmax};exec(legacy[legacy.index('def generate():'):legacy.index('def expected_nll')],scope)
 oldgen=scope['generate']();newgen=generate(20261125,2718)
 for oldvalue,newvalue in zip(oldgen,newgen):
  if isinstance(oldvalue,dict):
   for k in oldvalue:close(oldvalue[k],newvalue[k])
  else:close(oldvalue,newvalue)
 for mode in ['valid','empty','missing','nonconvergence','fields','identity','nonfinite','collision']:
  with tempfile.TemporaryDirectory() as tmp:
   e={'a':meta2('mock',n=2)};l=Ledger('test',e,Path(tmp));r=records.copy()
   if mode!='empty':l.start('a',e['a'])
   if mode=='nonconvergence':r['success']=False
   if mode=='fields':del r['iterations']
   if mode=='nonfinite':r['gradient_max']=None
   if mode not in ['empty','missing']:l.complete('a',r)
   if mode=='identity':l.expected={'other':e['a']}
   if mode=='valid':l.validate()
   else:reject(lambda:l.complete('a',r) if mode=='collision' else l.validate())
   tests.append(mode)
 with tempfile.TemporaryDirectory() as tmp:
  d=Path(tmp);reject(lambda:publication(d,'selection'));path=d/'x.npz';m=save_npz(path,{'p':np.full((24,36,3),1/3)});check_archive(path,m);reject(lambda:save_npz(path,{}));m2={**m,'arrays':{}};reject(lambda:check_archive(path,m2));path.write_bytes(b'corrupted');reject(lambda:check_archive(path,m))
 reject(lambda:valid_probability(np.full((24,36,3),.4)));reject(lambda:close(.1,.2))
 def rows(gain):
  return [dict(candidate=c,regime=r,condition='informative',expected_gain=gain if r=='positive' else 0.,oracle_gap_recovery=.9,contrast_normalized_rmse=.1) for c in RHO for r in REGIMES]
 assert select(rows(.1))=='p2';assert select(rows(.01)) is None
 totals=[expected('A_offsets'),expected('A_dev'),expected('A_batch','p0'),expected('A_test','p0'),expected('B_offsets'),expected('B_test','p0')];assert sum(map(len,totals))==88;assert sum(v['person_solves'] for e in totals for v in e.values())==1472
 with tempfile.TemporaryDirectory() as tmp:
  l=Ledger('mock',{'a':meta2('mock')},Path(tmp))
  with patch('head.minimize',return_value=SimpleNamespace(x=x,success=False,message='mock interruption',nit=0)):
   reject(lambda:solve(f,x,l,'a',z,4))
 # Function interfaces prohibit oracle/query outcomes as fitting inputs.
 import inspect
 assert list(inspect.signature(fit).parameters)==['z','y','base','rank','rho','lambda_b','seed','ledger','key']
 atomic(OUT/'preflight_final.json',dict(status='PASS',shared_gradient_error=float(np.max(abs(fd-g))),adaptation_gradient_error=float(np.max(abs(fd2-gv))),checks=['rescaling_training_and_adaptation','old_objective_equivalence','group_pair_support_boundaries','certificate_separate_scaling','deterministic_objectives','corrupted_bytes','missing_arrays','normalization','aggregation','publication_access','selection_ties_and_none','mock_optimizer_failure']+tests,optimizer_calls=0,B_materialized=False,environment=environment()))
 atomic(OUT/'stage_templates_final.json',dict(A_offsets=expected('A_offsets'),A_dev=expected('A_dev'),conditional={c:{s:expected(s,c) for s in ['A_batch','A_test','B_offsets','B_test']} for c in RHO}))
 print('PASS preflight; no optimizer invoked')
if __name__=='__main__':main()
