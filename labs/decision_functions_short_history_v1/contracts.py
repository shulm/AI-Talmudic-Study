"""Protocol-derived exact contracts; no data-dependent counts or selection."""
from core import *
P=read(OUT/'PROTOCOL.json')
REAL=[x['id'] for x in P['realizations']]
SEEDS=P['shared_model']['initialization_seeds'];REG=P['generator']['regimes'];SCHEDULES=P['support']['schedule_seeds']
POLICIES=P['policies'];MODELS=['B1','B2','B3','M1'];HEADS=['B3']+[f'M1_{s}' for s in SEEDS]
def conditions(include_zero=True):
 rows=[]
 for r in REG:
  for policy,config in POLICIES.items():
   for k in config['budgets']:
    for schedule in (['anchor'] if k==96 else SCHEDULES):rows.append((r,policy,k,str(schedule),'informative'))
  for schedule in SCHEDULES:rows.append((r,'primary',16,str(schedule),'uninformative'))
  if include_zero:rows.append((r,'primary',0,'zero','informative'))
 return rows
def ident(cond):return '_'.join(map(str,cond))
def metadata(kind,real,cond=None,model=None,n=0):
 d=dict(kind=kind,realization=real,person_solves=n,model=model)
 if cond:
  r,pol,k,h,info=cond;d.update(regime=r,policy=pol,k=k,schedule=h,condition=info,rho=POLICIES[pol]['rho_adapt'],lambda_b=POLICIES[pol]['lambda_b_adapt'])
 return d
def expected(real,stage):
 e={}
 if stage=='shared':
  for r in REG:
   for seed in SEEDS:e[f'{r}_{seed}']=dict(kind='shared',realization=real,regime=r,seed=seed,rho=.01,lambda_b=.1,rank=2,person_solves=0)
 elif stage=='support':
  for c in conditions(False):
   for m in (['B3'] if c[4]=='uninformative' else HEADS):e[ident(c)+'_'+m]=metadata('adapt',real,c,m,24)
 elif stage=='batch':
  for pol in POLICIES:
   c=('positive',pol,16,str(SCHEDULES[0]),'informative')
   for m in HEADS:
    for n in [1,7]:e[ident(c)+'_'+m+f'_n{n}']=metadata('batch',real,c,m,n)
 else:raise ValueError('Unexpected stage')
 return e
def all_ledgers():return {r+'_'+s:expected(r,s) for r in REAL for s in ['shared','support','batch']}
def prediction_keys():
 keys=set()
 for c in conditions():
  key=ident(c);keys|={key+'_'+m for m in MODELS}
  if c[4]=='informative':
   keys|={key+'_'+m+'_donor' for m in MODELS}
   if c[2]>0:keys|={key+f'_M1_{s}' for s in SEEDS}
 return keys
def metric_row_ids():return [ident(c) for c in conditions()]
def bootstrap_keys():return {'person_pairs','query_groups','positive_gain','null_degradation','positive_donor'}
def curvature_keys():
 return {ident(c)+f'_M1_{s}' for c in conditions(False) if c[4]=='informative' for s in SEEDS}
def expected_archives():
 return {f'{r}_{suffix}.npz' for r in REAL for suffix in ['fixture','learner','support','evaluator','models','predictions','bootstrap','curvature','batch']}
def required_public():return {'PROTOCOL.json','EXPECTED.json','preflight.json','prefit_sources.json','publication.json'}|{f'{r}_{s}.json' for r in REAL for s in ['schedules','manifest','scores','batch','curvature']}
def qualification(verification,numerical,gates):
 return verification=='VERIFIED_COMPLETE' and numerical is True and set(gates)==set(REAL) and all(set(gates[r])=={'gain','recovery','contrast','null'} and all(v is True for v in gates[r].values()) for r in REAL)
def support_schedules(real,pool,z):
 groups=sorted(set(int(i)//3 for i in pool));out={}
 for seed in SCHEDULES:
  hashes={g:hashlib.sha256(f'short_history_v1|{real}|{seed}|group|{g}'.encode()).hexdigest() for g in groups}
  order=sorted(groups,key=lambda g:(hashes[g],g));ph={g:int(hashlib.sha256(f'short_history_v1|{real}|{seed}|phase|{g}'.encode()).hexdigest(),16)%3 for g in order}
  cases=[3*g+(ph[g]+j)%3 for g in order for j in range(3)];revealed={str(k):cases[:k] for k in P['policies']['primary']['budgets']};spectra={}
  for k,indices in revealed.items():
   eig=np.linalg.eigvalsh(z[indices].T@z[indices]/int(k));assert np.max(abs(eig-P['support']['gram_eigenvalues'][k]))<=1e-12;spectra[k]=eig.tolist()
  out[str(seed)]=dict(group_order=order,group_hashes=hashes,start_phases=ph,case_order=cases,revealed=revealed,raw_gram_eigenvalues=spectra,case_order_sha256=digest(np.array(cases,dtype='<i8').tobytes()))
 return dict(realization=real,schedules=out,canonical_96=list(map(int,pool)),donor_map=[i^1 for i in range(24)],reuse_96='one canonical pool fit per head; shared across schedules')
def ids(schedule,c):
 k=c[2];h=c[3]
 return np.array(schedule['canonical_96'] if k==96 else ([] if k==0 else schedule['schedules'][h]['revealed'][str(k)]),dtype=int)

def save_npz(path,arrays):
 import io
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);buf=io.BytesIO();np.savez_compressed(buf,**arrays)
 with path.open('xb') as f:f.write(buf.getvalue())
 return dict(sha256=file_hash(path),arrays={k:dict(shape=list(v.shape),dtype=str(v.dtype),sha256=digest(np.ascontiguousarray(v).tobytes())) for k,v in arrays.items()})
def load_npz(path):
 with np.load(path,allow_pickle=False) as a:return {k:a[k] for k in a.files}
def validate_ids(actual,required,label):
 actual=list(actual);required=list(required)
 if len(actual)!=len(set(actual)) or len(required)!=len(set(required)):raise ValueError(label+' duplicate IDs')
 if set(actual)!=set(required):raise ValueError(label+' exact set mismatch: missing '+str(sorted(set(required)-set(actual)))+' extra '+str(sorted(set(actual)-set(required))))


def expected_comparison_count():
 # Derived from exact protocol conditions and declared metric schemas, including None checks.
 cc=conditions();inform=[c for c in cc if c[4]=='informative'];nonzero=[c for c in inform if c[2]>0];null=[c for c in inform if c[0]=='null'];zero=[c for c in cc if c[2]==0];unin=[c for c in cc if c[4]=='uninformative'];aggs={(c[0],c[1],c[2],c[4]) for c in cc};ai=sum(a[3]=='informative' for a in aggs);au=len(aggs)-ai
 per=(len(SCHEDULES)*4+len(REG)*3+4 # geometry and source joins
      +len(cc)*(25+2) # row metric schema and independent B1/B2 replay
      +len(inform)*(4+16+1)+len(null)*4 # donor arrays, metrics, B2 invariance, null identities
      +len(nonzero)*(1+len(SEEDS)*4) # seed ensemble and statistics
      +len(zero)*2+len(unin) # zero-support and uninformative analytic identities
      +ai*36+au*21 # aggregate schemas
      +len(POLICIES)*(8+len(SCHEDULES)*8+4) # gate tables
      +2+3*3 # bootstrap indices, vectors, points, intervals
      +len(expected(REAL[0],'batch'))*2
      +sum(len(expected(REAL[0],s)) for s in ['shared','support','batch'])
      +len(curvature_keys())*24*5)
 return len(REAL)*per


def archive_shapes(real,kind):
 if kind=='fixture':return dict(z=(192,2),base=(192,3),bias=(96,3),u=(96,2),v=(3,2,2),split_train=(120,),split_support=(96,),split_development=(36,),split_test=(36,),**{k:(96,192) for k in ['y_positive','y_null','y_positive_uninformative','y_null_uninformative']},oracle_positive=(96,192,3),oracle_null=(96,192,3))
 if kind=='learner':return dict(z=(120,2),base=(120,3),query_z=(36,2),query_base=(36,3),train_ids=(120,),query_ids=(36,),positive_y=(48,120),null_y=(48,120))
 if kind=='support':return dict(z=(96,2),base=(96,3),ids=(96,),**{k:(24,96) for k in ['positive_y','null_y','positive_uninformative_y','null_uninformative_y']})
 if kind=='evaluator':return dict(positive_y=(24,36),null_y=(24,36),positive_oracle=(24,36,3),null_oracle=(24,36,3))
 if kind=='models':return {f'{r}_{seed}':(3,2,2) for r in REG for seed in SEEDS}
 if kind=='predictions':return {k:(24,36,3) for k in prediction_keys()}
 if kind=='curvature':return {k:(24,2,4) for k in curvature_keys()}
 if kind=='bootstrap':return {k:(2000,12) if k in ['person_pairs','query_groups'] else (2000,) for k in bootstrap_keys()}
 if kind=='batch':return {k:(v['person_solves'],36,3) for k,v in expected(real,'batch').items()}
 raise ValueError('Unknown archive')
