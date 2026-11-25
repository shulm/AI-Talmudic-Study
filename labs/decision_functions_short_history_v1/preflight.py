"""Zero-fit checks, including destructive omissions only in isolated toy directories."""
import argparse
import importlib.util
import tempfile
from copy import deepcopy
from contracts import *
from fixture import generate
from head import shared_objective,personal_objective,probabilities
from scoring import bootstrap,cell_loss,score
from verify import require_complete,checked_archive,finite_probability

def rejected(fn):
 try:fn()
 except (ValueError,FileNotFoundError,FileExistsError,AssertionError,KeyError):return True
 raise AssertionError('Invalid evidence accepted')
def synthetic_complete(root):
 out=root/'public';private=root/'private';out.mkdir();private.mkdir()
 for name in required_public():atomic(out/name,{})
 # Test fixtures may overwrite their own placeholders; actual scientific publication never does.
 (out/'EXPECTED.json').write_text(json.dumps(dict(ledgers=all_ledgers(),prediction_keys=sorted(prediction_keys()),metric_row_ids=metric_row_ids())))
 for name in expected_archives():(private/name).write_bytes(b'toy')
 result=dict(success=True,finite=True,message='mock only; no optimizer',iterations=1,objective=1.,gradient_max=1e-9,person_scaled_gradient_max=1e-8,parameter_count=5,parameter_norm=.1,feature_shape=[16,2],feature_norm=1.,cpu_seconds=0.,wall_seconds=0.)
 for stage,e in all_ledgers().items():
  ledger=Ledger(stage,e,out)
  for key,meta in e.items():
   ledger.start(key,meta);ledger.complete(key,result);pp=private/'parameters'/stage/(key+'.npy');pp.parent.mkdir(parents=True,exist_ok=True);pp.write_bytes(b'toy')
 return out,private

def main(output):
 checks=[];rng=np.random.default_rng(12345);z=rng.normal(size=(7,2));y=rng.integers(0,3,(4,7));base=rng.normal(size=(7,3));v=rng.normal(size=(3,2,2));params=rng.normal(size=32)*.1
 spec=importlib.util.spec_from_file_location('v2head',ROOT/'labs/decision_functions_diagnostics_v2/head.py');v2=importlib.util.module_from_spec(spec);spec.loader.exec_module(v2)
 f=shared_objective(z,y,base,2,.01,.1)[0];old=v2.shared_objective(z,y,base,2,.01,.1)[0];assert np.max(abs(f(params)[1]-old(params)[1]))<1e-12 and abs(f(params)[0]-old(params)[0])<1e-12
 eps=1e-6;fd=np.array([(f(params+eps*np.eye(32)[j])[0]-f(params-eps*np.eye(32)[j])[0])/(2*eps) for j in range(32)]);assert max(abs(fd-f(params)[1]))<1e-8
 p=rng.normal(size=20)*.1
 for rho,lb in [(.01,.1),(.06,.6)]:
  fun=personal_objective(z,y,base,rho,lb,v)[0];old=v2.personal_objective(z,y,base,rho,lb,v)[0];assert abs(fun(p)[0]-old(p)[0])<1e-12;assert max(abs(fun(p)[1]-old(p)[1]))<1e-12
  perm=np.array([6,1,0,3,2,5,4]);pf=personal_objective(z[perm],y[:,perm],base[perm],rho,lb,v)[0];assert abs(fun(p)[0]-pf(p)[0])<1e-12 and max(abs(fun(p)[1]-pf(p)[1]))<1e-12
 # Zero-feature identity at arbitrary offsets, not a fitted favorable fixture.
 b=rng.normal(size=(4,3));pp=np.c_[b,np.zeros((4,2))];f1=personal_objective(np.zeros_like(z),y,base,.01,.1,v)[0];f0=personal_objective(np.zeros_like(z),y,base,.01,.1,None)[0];assert abs(f1(pp.ravel())[0]-f0(b.ravel())[0])<1e-12;assert np.max(abs(f1(pp.ravel())[1].reshape(4,5)[:,3:]))==0
 checks+=['v2_objective_gradient_equivalence','finite_difference_shared_gradient','support_order_permutation_invariance','uninformative_analytic_M1_identity']
 # Geometry only from legacy fixture; no new scientific response statistics inspected.
 zz,bb,bias,u,v,sp,ys,ps=generate(20261125,2718)
 assert np.max(abs(bias[::2]-bias[1::2]))==0 and np.max(abs(u[::2]+u[1::2]))<1e-12
 assert set(sp['support'])<=set(sp['train']) and not set(sp['train'])&set(sp['test']) and not set(sp['development'])&set(sp['test'])
 for split in ['train','development','test','support']:assert all(sum(sp[split]//3==g)==3 for g in set(sp[split]//3))
 for r in REAL:
  sch=support_schedules(r,sp['support'],zz)
  for h in SCHEDULES:
   sets=[set(sch['schedules'][str(h)]['revealed'][str(k)]) for k in [4,16,32,96]];assert all(a<=b for a,b in zip(sets,sets[1:]));assert sets[-1]==set(sp['support'])
 checks+=['split_group_pair_preservation','exact_hashed_nested_support_schedules','declared_Gram_spectra','canonical_96_set_reuse']
 # Toy probability arrays and two-history loss aggregation/paired bootstrap identities.
 ev={r+'_y':ys[r][72:][:,sp['test']] for r in REG};ev.update({r+'_oracle':ps[r][72:][:,sp['test']] for r in REG});arrays={};donor=np.arange(24)^1
 for cond in conditions():
  key=ident(cond);prob=rng.dirichlet(np.ones(3),size=(24,36));prob2=rng.dirichlet(np.ones(3),size=(24,36))
  for m in MODELS:arrays[key+'_'+m]=prob.copy() if m!='M1' else prob2.copy()
  if cond[4]=='informative':
   for m in MODELS:arrays[key+'_'+m+'_donor']=arrays[key+'_'+m][donor]
   if cond[2]>0:
    for seed in SEEDS:arrays[key+f'_M1_{seed}']=prob2.copy()
  if cond[0]=='null' and cond[4]=='informative':assert abs((cell_loss(prob[donor],ev['null_oracle'])-cell_loss(prob,ev['null_oracle'])).mean())<1e-12
 boot,summary=bootstrap(arrays,ev);rg=np.random.Generator(np.random.PCG64(1701));pp=rg.integers(0,12,(2000,12));qq=rg.integers(0,12,(2000,12));assert np.array_equal(pp,boot['person_pairs']) and np.array_equal(qq,boot['query_groups'])
 cells=np.mean([cell_loss(arrays[ident(('positive','primary',16,str(h),'informative'))+'_B3'],ev['positive_oracle'])-cell_loss(arrays[ident(('positive','primary',16,str(h),'informative'))+'_M1'],ev['positive_oracle']) for h in SCHEDULES],0)
 reference=[]
 for pi,qi in zip(pp,qq):
  persons=np.array([[2*i,2*i+1] for i in pi]).ravel();queries=np.array([[3*j,3*j+1,3*j+2] for j in qi]).ravel();reference.append(cells[np.ix_(persons,queries)].mean(1).mean())
 assert np.max(abs(np.array(reference)-boot['positive_gain']))<1e-12
 result=score(arrays,ev);positive=next(x for x in result['aggregates'] if x['regime']=='positive' and x['policy']=='primary' and x['k']==16 and x['condition']=='informative');assert abs(positive['expected_gain']-cells.mean())<1e-12
 a,b=[arrays[ident(('positive','primary',16,str(h),'informative'))+'_M1'] for h in SCHEDULES];assert abs(cell_loss((a+b)/2,ev['positive_oracle']).mean()-(cell_loss(a,ev['positive_oracle']).mean()+cell_loss(b,ev['positive_oracle']).mean())/2)>1e-3
 checks+=['donor_recipient_mapping_and_null_identity','bootstrap_indices_and_full_pair_group_resampling','loss_not_probability_history_aggregation']
 for mode in ['valid','empty','missing_ledger','missing_stage','missing_archive','wrong_expected','optimizer_failed']:
  with tempfile.TemporaryDirectory() as temp:
   root=Path(temp)
   if mode=='empty':
    out=root/'out';private=root/'private';out.mkdir();private.mkdir()
   else:
    out,private=synthetic_complete(root)
    if mode=='missing_ledger':(out/'records'/'C_shared').rename(out/'missing_ledger')
    if mode=='missing_stage':(out/'D_scores.json').unlink()
    if mode=='missing_archive':(private/'D_predictions.npz').unlink()
    if mode=='wrong_expected':(out/'records'/'C_shared'/'expected.json').write_text('{}')
    if mode=='optimizer_failed':
     path=next((out/'records'/'C_shared').glob('*.complete.json'));r=read(path);r['success']=False;path.write_text(json.dumps(r))
   if mode=='valid':assert require_complete(out,private)==dict(records=196,person_solves=3776,shared_fits=12)
   else:rejected(lambda:require_complete(out,private))
   checks.append(mode)
 with tempfile.TemporaryDirectory() as temp:
  path=Path(temp)/'test.npz';m=save_npz(path,{'a':np.ones(3)});rejected(lambda:checked_archive(path,m,{'a','b'}));rejected(lambda:save_npz(path,{}));path.write_bytes(b'broken');rejected(lambda:checked_archive(path,m,{'a'}))
 checks+=['missing_array_key','output_collision','corrupted_bytes'];rejected(lambda:finite_probability(np.full((24,36,3),.4)));checks+=['bad_normalization']
 good={r:{k:True for k in ['gain','recovery','contrast','null']} for r in REAL}
 assert qualification('VERIFIED_COMPLETE',True,good)
 assert not qualification('VERIFIED_DECLARED_EARLY_STOP',True,good) and not qualification('INCOMPLETE',True,good) and not qualification('VERIFIED_COMPLETE',False,good) and not qualification('VERIFIED_COMPLETE',True,{})
 for r in REAL:
  bad=deepcopy(good);bad[r]['null']=False;assert not qualification('VERIFIED_COMPLETE',True,bad)
 checks+=['success_requires_all_prerequisites','secondary_cannot_rescue_primary','early_stop_never_qualifies']
 totals=all_ledgers();assert len(totals)==6 and sum(map(len,totals.values()))==196 and sum(m['person_solves'] for e in totals.values() for m in e.values())==3776 and len(prediction_keys())==230
 atomic(output/'preflight.json',dict(status='PASS',checks=checks,scientific_optimizer_calls=0,shared_gradient_max_error=float(max(abs(fd-f(params)[1]))),environment=environment(),exact_prediction_arrays_per_realization=len(prediction_keys()),exact_metric_rows_per_realization=len(metric_row_ids()),exact_curvature_rows_per_realization=len(curvature_keys())*24,expected_replay_comparisons=expected_comparison_count()))
 atomic(output/'EXPECTED.json',dict(ledgers=totals,prediction_keys=sorted(prediction_keys()),metric_row_ids=metric_row_ids(),archives=sorted(expected_archives()),curvature_keys=sorted(curvature_keys()),bootstrap_keys=sorted(bootstrap_keys()),comparison_count=expected_comparison_count()))
 print('PASS preflight',len(checks),'checks; no optimizer calls',expected_comparison_count(),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output-root',type=Path,required=True);a=p.parse_args();main(a.output_root)
