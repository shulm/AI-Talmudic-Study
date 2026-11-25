"""Exact complete-run validation and independent saved-evidence arithmetic. No fitter imports."""
import argparse
from contracts import *

def require_complete(out,private):
 validate_ids((p.name for p in (out/'records').iterdir() if p.is_dir()),all_ledgers(),'ledger stages') if (out/'records').is_dir() else (_ for _ in ()).throw(ValueError('Missing all ledgers'))
 missing=required_public()-{p.name for p in out.iterdir()}
 if missing:raise ValueError('Missing required public outputs '+str(sorted(missing)))
 validate_ids((p.name for p in private.glob('*.npz')),expected_archives(),'private archives')
 frozen=read(out/'EXPECTED.json')
 if frozen['ledgers']!=all_ledgers() or set(frozen['prediction_keys'])!=prediction_keys() or frozen['metric_row_ids']!=metric_row_ids():raise ValueError('Frozen exact contract mismatch')
 records=people=shared=0
 for stage,expected_ids in all_ledgers().items():
  path=out/'records'/stage
  if read(path/'expected.json')!=expected_ids:raise ValueError('Expected ledger IDs altered')
  r=validate_records(path,expected_ids);records+=r['records'];people+=r['person_solves'];shared+=sum(m['kind']=='shared' for m in expected_ids.values())
 if (records,people,shared)!=(P['execution_limits']['optimizer_records'],P['execution_limits']['person_solves'],P['execution_limits']['shared_fits']):raise ValueError('Exact totals mismatch')
 needed={'parameters/'+stage+'/'+key+'.npy' for stage,e in all_ledgers().items() for key in e};validate_ids((p.relative_to(private).as_posix() for p in (private/'parameters').rglob('*.npy')),needed,'private parameter files')
 return dict(records=records,person_solves=people,shared_fits=shared)

def checked_archive(path,manifest,keys):
 if file_hash(path)!=manifest['sha256']:raise ValueError('Archive bytes corrupted')
 a=load_npz(path);validate_ids(a,keys,path.name);validate_ids(manifest['arrays'],keys,'manifest keys')
 for k,v in a.items():
  m=manifest['arrays'][k]
  if list(v.shape)!=m['shape'] or str(v.dtype)!=m['dtype'] or not np.isfinite(v).all() or digest(np.ascontiguousarray(v).tobytes())!=m['sha256']:raise ValueError('Array shape/type/bytes invalid')
 return a

def finite_probability(p,shape=(24,36,3)):
 if p.shape!=shape or not np.isfinite(p).all() or (p<0).any() or np.max(abs(p.sum(-1)-1))>1e-12:raise ValueError('Probability contract')
def cells(p,o):return np.einsum('...c,...c->...',o,-np.log(np.clip(p,1e-12,None)))
def statistics(p,y,o):
 nll=-np.log(np.maximum(p[np.arange(len(y))[:,None],np.arange(y.shape[1])[None,:],y],1e-12))
 return dict(expected_nll=float(cells(p,o).mean()),nll=float(nll.mean()),accuracy=float(np.mean(np.argmax(p,axis=-1)==y)),brier=float(np.mean(np.sum((p-np.eye(3)[y])**2,-1))))
def contrasts(p):
 log=np.log(np.clip(p,1e-12,None));out=[]
 for a,b in [(0,1),(0,2),(1,2)]:
  d=log[:,:,a]-log[:,:,b];d=d[0::2]-d[1::2];out.append(d-d[:,0,None])
 return np.stack(out,-1)
class Compare:
 def __init__(self):self.errors={}
 def __call__(self,key,a,b):
  if key in self.errors:raise ValueError('Duplicate comparison')
  if a is None or b is None:
   if a is not b:raise ValueError('Undefined scalar mismatch')
   self.errors[key]=0.;return
  err=float(np.max(abs(np.asarray(a)-np.asarray(b))))
  if not np.isfinite(err) or err>1e-12:raise ValueError(key+' discrepancy '+str(err))
  self.errors[key]=err

def numeric_tree(c,key,a,b):
 if isinstance(a,dict):
  validate_ids(b,a,key)
  for k in a:numeric_tree(c,key+'/'+k,a[k],b[k])
 elif isinstance(a,(float,int)) or a is None:c(key,a,b)
 elif a!=b:raise ValueError(key+' value mismatch')

def replay(real,out,private,c):
 man=read(out/(real+'_manifest.json'));archive_keys={
 'fixture':{'z','base','bias','u','v','split_train','split_support','split_development','split_test','y_positive','y_null','y_positive_uninformative','y_null_uninformative','oracle_positive','oracle_null'},
 'learner':{'z','base','query_z','query_base','train_ids','query_ids','positive_y','null_y'},
 'support':{'z','base','ids','positive_y','null_y','positive_uninformative_y','null_uninformative_y'},
 'evaluator':{'positive_y','null_y','positive_oracle','null_oracle'},
 'models':{f'{r}_{s}' for r in REG for s in SEEDS},'predictions':prediction_keys(),'bootstrap':bootstrap_keys(),'curvature':curvature_keys(),'batch':set(expected(real,'batch'))}
 validate_ids(man['archives'],{real+'_'+x+'.npz' for x in archive_keys},'manifest archives')
 data={k:checked_archive(private/(real+'_'+k+'.npz'),man['archives'][real+'_'+k+'.npz'],keys) for k,keys in archive_keys.items()};pred=data['predictions'];ev=data['evaluator'];fx=data['fixture'];sp=data['support'];learn=data['learner'];models=data['models'];schedule=read(out/(real+'_schedules.json'))
 for kind,arrays in data.items():
  shapes=archive_shapes(real,kind)
  for key,value in arrays.items():
   if value.shape!=shapes[key]:raise ValueError('Protocol-derived archive shape mismatch')
 # Independent schedule reconstruction from exact specified byte strings.
 pool=fx['split_support'];validate_ids(schedule['schedules'],map(str,SCHEDULES),'schedules')
 for h in SCHEDULES:
  groups=sorted(set(int(i)//3 for i in pool));order=sorted(groups,key=lambda g:(hashlib.sha256(('short_history_v1|%s|%d|group|%d'%(real,h,g)).encode('utf-8')).digest(),g));cases=[]
  for g in order:
   phase=int.from_bytes(hashlib.sha256(('short_history_v1|%s|%d|phase|%d'%(real,h,g)).encode('utf-8')).digest(),'big')%3;cases.extend([3*g+(phase+j)%3 for j in range(3)])
  s=schedule['schedules'][str(h)];assert s['case_order']==cases and s['group_order']==order
  for k in POLICIES['primary']['budgets']:
   assert s['revealed'][str(k)]==cases[:k];gram=fx['z'][cases[:k]].T@fx['z'][cases[:k]]/k;c(f'{real}/gram/{h}/{k}',np.linalg.eigvalsh(gram),P['support']['gram_eigenvalues'][str(k)])
 assert schedule['donor_map']==[i^1 for i in range(24)] and schedule['canonical_96']==pool.tolist()
 tr=fx['split_train'];qu=fx['split_test'];assert len(tr)==120 and len(qu)==36 and len(pool)==96;assert set(pool)<=set(tr) and not set(tr)&set(qu)
 for r in REG:
  c(real+'/training/'+r,learn[r+'_y'],fx['y_'+r][:48][:,tr]);c(real+'/query/'+r,ev[r+'_y'],fx['y_'+r][72:][:,qu]);c(real+'/oracle/'+r,ev[r+'_oracle'],fx['oracle_'+r][72:][:,qu]);finite_probability(ev[r+'_oracle'])
 for r in ['positive','null','positive_uninformative','null_uninformative']:c(real+'/support/'+r,sp[r+'_y'],fx['y_'+r][72:][:,pool])
 for k,p in pred.items():finite_probability(p)
 rows=read(out/(real+'_scores.json'));validate_ids([r['id'] for r in rows['rows']],metric_row_ids(),'metric rows');byid={r['id']:r for r in rows['rows']};replayed={}
 for condition in conditions():
  r,pol,k,h,info=condition;key=ident(condition);o=ev[r+'_oracle'];y=ev[r+'_y'];m={model:statistics(pred[key+'_'+model],y,o) for model in MODELS};truth=contrasts(o);est=contrasts(pred[key+'_M1']);den=float(np.mean(truth**2));mse=float(np.mean((est-truth)**2));eo=float(cells(o,o).mean());gain=m['B3']['expected_nll']-m['M1']['expected_nll'];gap=m['B3']['expected_nll']-eo
  replayed[key]=dict(metrics=m,oracle_expected_nll=eo,expected_gain=gain,oracle_gap=gap,oracle_gap_recovery=gain/gap if gap>0 else None,contrast_mse=mse,contrast_denominator=den,contrast_nrmse=float(np.sqrt(mse/den)) if den>1e-20 else None,null_contrast_rms=float(np.sqrt(np.mean(est**2))),contrast_square_mean=float(np.mean(est**2)))
  row=byid[key]
  for name,value in replayed[key].items():numeric_tree(c,real+'/'+key+'/'+name,value,row[name])
  selected=ids(schedule,condition);lookup={int(i):j for j,i in enumerate(pool)};ix=[lookup[int(i)] for i in selected];labels=sp[r+('' if info=='informative' else '_uninformative')+'_y'][:,ix];source=man['provenance'][key]
  assert source['support_ids']==selected.tolist() and source['support_label_sha256']==digest(labels.tobytes()) and source['donor_support_label_sha256']==digest(labels[np.arange(24)^1].tobytes()) and source['recipient_to_donor']==list(np.arange(24)^1)
  prior=np.bincount(learn[r+'_y'].ravel(),minlength=3)/learn[r+'_y'].size;freq=(np.eye(3)[labels].sum(1)+4*prior)/(k+4);c(real+'/'+key+'/B1_input_replay',pred[key+'_B1'],np.broadcast_to(freq[:,None],(24,36,3)));bb=np.exp(learn['query_base']-learn['query_base'].max(-1,keepdims=True));bb/=bb.sum(-1,keepdims=True);c(real+'/'+key+'/B2_input_replay',pred[key+'_B2'],np.broadcast_to(bb[None],(24,36,3)))
  if info=='informative':
   donor={}
   for model in MODELS:
    c(real+'/'+key+'/'+model+'/donor_array',pred[key+'_'+model+'_donor'],pred[key+'_'+model][np.arange(24)^1]);dm=statistics(pred[key+'_'+model+'_donor'],y,o);donor[model]={a:dm[a]-m[model][a] for a in dm}
    if r=='null':c(real+'/'+key+'/'+model+'/null_identity',donor[model]['expected_nll'],0.)
   numeric_tree(c,real+'/'+key+'/donor_metrics',donor,row['donor']);replayed[key]['donor']=donor
   c(real+'/'+key+'/B2_donor',pred[key+'_B2'],pred[key+'_B2_donor'])
   if k>0:
    c(real+'/'+key+'/ensemble',pred[key+'_M1'],np.stack([pred[key+f'_M1_{s}'] for s in SEEDS]).mean(0))
    for seed in SEEDS:numeric_tree(c,real+'/'+key+f'/seed{seed}',statistics(pred[key+f'_M1_{seed}'],y,o),row['seeds'][str(seed)])
  if k==0 or info=='uninformative':c(real+'/'+key+'/analytic_M1',pred[key+'_M1'],pred[key+'_B3'])
  if k==0:c(real+'/'+key+'/analytic_B3',pred[key+'_B3'],pred[key+'_B2'])
 # Independently aggregate scalar losses and squared contrasts, never histories' probabilities.
 aggs={}
 for agg in rows['aggregates']:
  r,pol,k,info=agg['regime'],agg['policy'],agg['k'],agg['condition'];rr=[replayed[ident(cc)] for cc in conditions() if cc[0]==r and cc[1]==pol and cc[2]==k and cc[4]==info];assert len(rr)==(1 if k in [0,96] else 2)
  mean=lambda key:float(np.mean([x[key] for x in rr]));gap=mean('oracle_gap');den=mean('contrast_denominator');g=mean('expected_gain');computed=dict(expected_gain=g,oracle_gap_recovery=g/gap if gap>0 else None,contrast_nrmse=float(np.sqrt(mean('contrast_mse')/den)) if den>1e-20 else None,null_contrast_rms=float(np.sqrt(mean('contrast_square_mean'))),metrics={m:{k:float(np.mean([x['metrics'][m][k] for x in rr])) for k in rr[0]['metrics'][m]} for m in MODELS},donor={m:{k:float(np.mean([x['donor'][m][k] for x in rr])) for k in rr[0]['donor'][m]} for m in MODELS} if info=='informative' else None)
  for name,value in computed.items():numeric_tree(c,f'{real}/aggregate/{r}/{pol}/{k}/{info}/{name}',value,agg[name])
  aggs[(r,pol,k,info)]=computed
 expected_aggs={(cc[0],cc[1],cc[2],cc[4]) for cc in conditions()};assert set(aggs)==expected_aggs and len(rows['aggregates'])==len(expected_aggs)
 def gate(p,n):
  val=dict(gain=p['expected_gain'],recovery=p['oracle_gap_recovery'],contrast=p['contrast_nrmse'],null=-n['expected_gain']);mar=dict(gain=val['gain']-.05,recovery=val['recovery']-.5 if val['recovery'] is not None else None,contrast=.5-val['contrast'] if val['contrast'] is not None else None,null=.01-val['null']);return val,mar,{k:bool(v is not None and np.isfinite(v) and v>=0) for k,v in mar.items()}
 gts={}
 for pol in POLICIES:
  val,mar,passed=gate(aggs[('positive',pol,16,'informative')],aggs[('null',pol,16,'informative')]);table=rows['gates'][pol];numeric_tree(c,real+'/'+pol+'/gate_values',val,table['values']);numeric_tree(c,real+'/'+pol+'/gate_margins',mar,table['margins']);assert passed==table['passed'];gts[pol]=passed
  worst=[]
  for h in SCHEDULES:
   val,mar,pa=gate(*[replayed[ident((r,pol,16,str(h),'informative'))] for r in REG]);tab=table['schedules'][str(h)];numeric_tree(c,f'{real}/{pol}/{h}/gate_values',val,tab['values']);numeric_tree(c,f'{real}/{pol}/{h}/gate_margins',mar,tab['margins']);assert pa==tab['passed'];worst.append(mar)
  numeric_tree(c,real+'/'+pol+'/worst',{k:min(w[k] for w in worst) for k in worst[0]},table['worst_schedule_margins'])
 # Bootstrap using independent multiplicity-weight contraction.
 boots=data['bootstrap'];rng=np.random.Generator(np.random.PCG64(1701));pp=rng.integers(0,12,(2000,12));qq=rng.integers(0,12,(2000,12));c(real+'/bootstrap/pairs',boots['person_pairs'],pp);c(real+'/bootstrap/groups',boots['query_groups'],qq)
 for name,r in [('positive_gain','positive'),('null_degradation','null'),('positive_donor','positive')]:
  loss=[]
  for h in SCHEDULES:
   key=ident((r,'primary',16,str(h),'informative'));o=ev[r+'_oracle'];m=cells(pred[key+'_M1'],o);b=cells(pred[key+'_B3'],o);d=cells(pred[key+'_M1_donor'],o);loss.append(b-m if name=='positive_gain' else m-b if name=='null_degradation' else d-m)
  avg=np.stack(loss).mean(0).reshape(12,2,12,3).mean((1,3));pv=np.array([np.bincount(x,minlength=12) for x in pp]);qv=np.array([np.bincount(x,minlength=12) for x in qq]);res=np.einsum('bi,ij,bj->b',pv,avg,qv)/144
  if boots[name].shape!=(2000,):raise ValueError('Incomplete bootstrap')
  c(real+'/bootstrap/'+name,res,boots[name]);c(real+'/bootstrap/'+name+'/point',np.mean(loss),rows['bootstrap'][name]['point']);c(real+'/bootstrap/'+name+'/CI',np.quantile(res,[.025,.975],method='linear'),rows['bootstrap'][name]['interval95']);assert rows['bootstrap'][name]['replicates']==2000
 # Numerical checks independently computed from saved small-batch arrays.
 num=read(out/(real+'_batch.json'));validate_ids([x['id'] for x in num['rows']],expected(real,'batch'),'batch metric rows');num_pass=True
 for row in num['rows']:
  key=row['id'];p=data['batch'][key];n=expected(real,'batch')[key]['person_solves'];finite_probability(p,(n,36,3));ref=pred[key.rsplit('_n',1)[0]];delta=float(abs(p[0]-ref[0]).max());loss=abs(float(cells(p[:1],ev['positive_oracle'][:1]).mean()-cells(ref[:1],ev['positive_oracle'][:1]).mean()));c(real+'/'+key+'/batch_probability',delta,row['max_probability_difference']);c(real+'/'+key+'/batch_loss',loss,row['first_person_expected_nll_difference']);num_pass &= delta<=1e-6 and loss<=1e-5
 assert num_pass==num['passed']
 # Exact parameter evidence; no regeneration of query predictions.
 expected_params={'parameters/'+real+'_'+stage+'/'+key+'.npy':meta for stage in ['shared','support','batch'] for key,meta in expected(real,stage).items()};validate_ids(man['parameters'],expected_params,'parameter manifest')
 for rel in expected_params:
  file=private/rel
  if file_hash(file)!=man['parameters'][rel]['sha256']:raise ValueError('Parameter bytes changed')
  vec=np.load(file);record=read(out/'records'/file.parent.name/(file.stem+'.complete.json'));assert vec.size==record['parameter_count'];c(real+'/parameter/'+rel,np.linalg.norm(vec),record['parameter_norm'])
 # Independent curvature by explicit class Jacobian and saved support parameters.
 Q=np.array([[1/np.sqrt(2),1/np.sqrt(6)],[-1/np.sqrt(2),1/np.sqrt(6)],[0,-2/np.sqrt(6)]]);curverows=read(out/(real+'_curvature.json'))['rows'];validate_ids([(x['id'],x['person']) for x in curverows],{(k,i) for k in curvature_keys() for i in range(24)},'curvature rows');cm={(x['id'],x['person']):x for x in curverows}
 for cc in conditions(False):
  if cc[4]!='informative':continue
  r,pol,k,h,info=cc;indices=ids(schedule,cc);z=fx['z'][indices];base=fx['base'][indices]
  for seed in SEEDS:
   name=ident(cc)+f'_M1_{seed}';v=models[f'{r}_{seed}'];param=np.load(private/'parameters'/(real+'_support')/(name+'.npy')).reshape(24,5);features=np.array([np.einsum('crd,d->cr',v,zi) for zi in z]);J=np.concatenate([np.tile(Q[None],(k,1,1)),features],-1)
   for person in range(24):
    logits=base+param[person,:3]+np.einsum('icr,r->ic',features,param[person,3:]);prob=np.exp(logits-logits.max(-1,keepdims=True));prob/=prob.sum(-1,keepdims=True);H=sum(j.T@(np.diag(q)-np.outer(q,q))@j for j,q in zip(J,prob))/k;H=(H+H.T)/2;e1=np.linalg.eigvalsh(H);lb=POLICIES[pol]['lambda_b_adapt'];rho=POLICIES[pol]['rho_adapt'];e2=np.linalg.eigvalsh(H+np.diag([lb,lb,rho,rho]));c(real+'/curvature/'+name+'/'+str(person),np.stack([e1,e2]),data['curvature'][name][person]);rr=cm[(name,person)]
    for field,value in [('data_min',float(e1[0])),('penalized_min',float(e2[0]))]:c(real+'/curvature/'+name+'/'+str(person)+'/'+field,value,rr[field])
    # Condition numbers amplify eigensolver roundoff: compare recorded ratio to its saved eigenvalues at absolute 1e-12.
    saved=data['curvature'][name][person]
    c(real+'/curvature/'+name+'/'+str(person)+'/data_condition',float(saved[0,-1]/saved[0,0]) if saved[0,0]>1e-12 else None,rr['data_condition']);c(real+'/curvature/'+name+'/'+str(person)+'/ridge_condition',float(saved[1,-1]/saved[1,0]) if saved[1,0]>0 else None,rr['penalized_condition'])
 return dict(gates=gts,numerical_pass=bool(num_pass))

def verify(private,out):
 before={str(p.relative_to(private)):file_hash(p) for p in private.rglob('*') if p.is_file()};c=Compare()
 try:
  audit=require_complete(out,private);states={r:replay(r,out,private,c) for r in REAL};numerical=all(x['numerical_pass'] for x in states.values());gates={r:x['gates']['primary'] for r,x in states.items()};state='VERIFIED_COMPLETE';qualified=qualification(state,numerical,gates)
  for p,h in read(out/'prefit_sources.json')['files'].items():
   if file_hash(ROOT/p)!=h:raise ValueError('Scientific source changed')
  after={str(p.relative_to(private)):file_hash(p) for p in private.rglob('*') if p.is_file()};assert before==after
  if len(c.errors)!=expected_comparison_count():raise ValueError('Exact replay comparison count mismatch '+str(len(c.errors)))
  result=dict(state=state,qualification=qualified,numerical_pass=numerical,primary_gates=gates,secondary_gates={r:x['gates']['count_scaled_secondary'] for r,x in states.items()},audit=audit,comparison_count=len(c.errors),maximum_discrepancy=max(c.errors.values()),comparison_ids=sorted(c.errors),private_before=before,private_after=after,declared_early_stop_paths=[])
 except Exception as e:
  result=dict(state='INCOMPLETE',qualification=False,error=repr(e),comparisons_reached=len(c.errors),private_before=before)
 atomic(out/'verification.json',result)
 print(result['state'],result['qualification'],result.get('error',''),flush=True)
 if result['state']!='VERIFIED_COMPLETE':raise SystemExit(1)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args();verify(a.private_root,a.output_root)
