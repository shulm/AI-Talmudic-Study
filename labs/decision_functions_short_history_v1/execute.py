"""Fresh synthetic fitting with explicit learner/support/evaluator interfaces."""
import argparse
from contracts import *
from fixture import generate
from head import fit,adapt,probabilities
from scoring import score,bootstrap,cell_loss

class RunLedger(Ledger):
 def __init__(self,real,stage,private,out):
  super().__init__(real+'_'+stage,expected(real,stage),out);self.parameter_root=private/'parameters'/(real+'_'+stage)
def prepare(real,private,out):
 cfg=next(x for x in P['realizations'] if x['id']==real);z,base,b,u,v,sp,ys,ps=generate(cfg['generator_seed'],cfg['label_seed']);tr=sp['train'];su=sp['support'];qu=sp['test']
 fixture=dict(z=z,base=base,bias=b,u=u,v=v,**{'split_'+k:x for k,x in sp.items()},**{'y_'+k:x for k,x in ys.items()},**{'oracle_'+k:x for k,x in ps.items()})
 learner=dict(z=z[tr],base=base[tr],query_z=z[qu],query_base=base[qu],train_ids=tr,query_ids=qu,**{r+'_y':ys[r][:48][:,tr] for r in REG})
 support=dict(z=z[su],base=base[su],ids=su,**{r+'_y':ys[r][72:][:,su] for r in ys})
 evaluator={**{r+'_y':ys[r][72:][:,qu] for r in REG},**{r+'_oracle':ps[r][72:][:,qu] for r in REG}}
 manifest={real+'_'+name+'.npz':save_npz(private/(real+'_'+name+'.npz'),a) for name,a in [('fixture',fixture),('learner',learner),('support',support),('evaluator',evaluator)]}
 schedules=support_schedules(real,su,z);atomic(out/(real+'_schedules.json'),schedules)
 return learner,support,schedules,manifest

def source_view(support,schedules,c):
 selected=ids(schedules,c);lookup={int(i):j for j,i in enumerate(support['ids'])};ix=np.array([lookup[int(i)] for i in selected],dtype=int);r,pol,k,h,info=c
 z=support['z'][ix] if info=='informative' else np.zeros((k,2));labels=support[r+('' if info=='informative' else '_uninformative')+'_y'][:,ix]
 return z,support['base'][ix],labels,selected

def shared(learner,ledger):
 models={}
 for r in REG:
  for seed in SEEDS:models[f'{r}_{seed}']=fit(learner['z'],learner[r+'_y'],learner['base'],2,.01,.1,seed,ledger,f'{r}_{seed}')
 ledger.validate();return models

def predict(learner,support,schedules,models,ledger):
 arrays={};provenance={};zq=learner['query_z'];bq=learner['query_base'];donors=np.arange(24)^1
 for c in conditions():
  r,pol,k,h,info=c;key=ident(c);rho=POLICIES[pol]['rho_adapt'];lb=POLICIES[pol]['lambda_b_adapt'];z,bs,y,selected=source_view(support,schedules,c);prior=np.bincount(learner[r+'_y'].ravel(),minlength=3)/learner[r+'_y'].size
  freq=(np.eye(3)[y].sum(1)+4*prior)/(k+4);arrays[key+'_B1']=np.broadcast_to(freq[:,None],(24,36,3)).copy();arrays[key+'_B2']=np.broadcast_to(__import__('scipy').special.softmax(bq,-1)[None],(24,36,3)).copy()
  if k==0:arrays[key+'_B3']=arrays[key+'_B2'].copy();arrays[key+'_M1']=arrays[key+'_B2'].copy()
  else:
   b=adapt(z,y,bs,rho,lb,None,ledger,key+'_B3');arrays[key+'_B3']=probabilities(zq,bq,b)
   if info=='uninformative':arrays[key+'_M1']=arrays[key+'_B3'].copy()
   else:
    pp=[]
    for seed in SEEDS:
     v=models[f'{r}_{seed}'];p=adapt(z,y,bs,rho,lb,v,ledger,key+f'_M1_{seed}');a=probabilities(zq,bq,p,v);arrays[key+f'_M1_{seed}']=a;pp.append(a)
    arrays[key+'_M1']=np.mean(pp,axis=0)
  if info=='informative':
   for m in MODELS:arrays[key+'_'+m+'_donor']=arrays[key+'_'+m][donors].copy()
  provenance[key]=dict(support_ids=list(map(int,selected)),support_label_sha256=digest(y.tobytes()),donor_support_label_sha256=digest(y[donors].tobytes()),support_feature_sha256=digest(z.tobytes()),base_sha256=digest(bs.tobytes()),recipient_to_donor=donors.tolist(),label_source=r+('' if info=='informative' else '_uninformative')+'_y',source_rows=list(range(72,96)),donor_source_rows=(72+donors).tolist())
 validate_ids(arrays,prediction_keys(),'predictions');ledger.validate();return arrays,provenance

def numerical(learner,support,schedules,models,ledger):
 out={}
 for pol in POLICIES:
  c=('positive',pol,16,str(SCHEDULES[0]),'informative');key=ident(c);z,bs,y,_=source_view(support,schedules,c);rho=POLICIES[pol]['rho_adapt'];lb=POLICIES[pol]['lambda_b_adapt']
  for m in HEADS:
   v=None if m=='B3' else models['positive_'+m.split('_')[1]]
   for n in [1,7]:
    name=key+'_'+m+f'_n{n}';p=adapt(z,y[:n],bs,rho,lb,v,ledger,name);out[name]=probabilities(learner['query_z'],learner['query_base'],p,v)
 ledger.validate();return out

def curvature(support,schedules,models,real,private):
 Q=np.column_stack([np.array([1.,-1.,0.])/np.sqrt(2),np.array([1.,1.,-2.])/np.sqrt(6)]);out={};report=[]
 for c in conditions(False):
  if c[4]!='informative':continue
  r,pol,k,h,info=c;z,bs,y,_=source_view(support,schedules,c);rho=POLICIES[pol]['rho_adapt'];lb=POLICIES[pol]['lambda_b_adapt']
  for seed in SEEDS:
   name=ident(c)+f'_M1_{seed}';p=np.load(private/'parameters'/(real+'_support')/(name+'.npy')).reshape(24,5);v=models[f'{r}_{seed}'];prob=probabilities(z,bs,p,v);features=np.einsum('crd,id->icr',v,z);J=np.concatenate([np.broadcast_to(Q,(k,3,2)),features],axis=2);eigs=[]
   for person in range(24):
    w=prob[person];cov=np.array([np.diag(q)-np.outer(q,q) for q in w]);H=np.einsum('icr,icd,idt->rt',J,cov,J)/k;H=(H+H.T)/2;data=np.linalg.eigvalsh(H);ridge=np.linalg.eigvalsh(H+np.diag([lb,lb,rho,rho]));eigs.append(np.stack([data,ridge]))
    report.append(dict(id=name,person=person,k=k,policy=pol,seed=seed,units='mean support loss',data_min=float(data[0]),data_condition=float(data[-1]/data[0]) if data[0]>1e-12 else None,data_singular=bool(data[0]<=1e-12),penalized_min=float(ridge[0]),penalized_condition=float(ridge[-1]/ridge[0]) if ridge[0]>0 else None))
   out[name]=np.array(eigs)
 validate_ids(out,curvature_keys(),'curvature');return out,report

def run(real,private,out):
 learner,support,schedules,manifest=prepare(real,private,out)
 models=shared(learner,RunLedger(real,'shared',private,out));manifest[real+'_models.npz']=save_npz(private/(real+'_models.npz'),models)
 arrays,prov=predict(learner,support,schedules,models,RunLedger(real,'support',private,out));manifest[real+'_predictions.npz']=save_npz(private/(real+'_predictions.npz'),arrays)
 batches=numerical(learner,support,schedules,models,RunLedger(real,'batch',private,out));manifest[real+'_batch.npz']=save_npz(private/(real+'_batch.npz'),batches)
 # All prediction arrays are on disk before evaluator arrays are loaded or scored.
 evaluator=load_npz(private/(real+'_evaluator.npz'));num=[]
 for key,a in batches.items():
  ref=arrays[key.rsplit('_n',1)[0]];diff=float(np.max(abs(a[0]-ref[0])));nll=abs(float(cell_loss(a[:1],evaluator['positive_oracle'][:1]).mean()-cell_loss(ref[:1],evaluator['positive_oracle'][:1]).mean()));num.append(dict(id=key,max_probability_difference=diff,first_person_expected_nll_difference=nll))
 atomic(out/(real+'_batch.json'),dict(rows=num,passed=all(x['max_probability_difference']<=1e-6 and x['first_person_expected_nll_difference']<=1e-5 for x in num)))
 scored=score(arrays,evaluator);boots,intervals=bootstrap(arrays,evaluator);manifest[real+'_bootstrap.npz']=save_npz(private/(real+'_bootstrap.npz'),boots);scored['bootstrap']=intervals;atomic(out/(real+'_scores.json'),scored)
 curves,cr=curvature(support,schedules,models,real,private);manifest[real+'_curvature.npz']=save_npz(private/(real+'_curvature.npz'),curves);atomic(out/(real+'_curvature.json'),dict(rows=cr,zero_fit=True,units='mean support loss; not a calibrated posterior'))
 parameters={p.relative_to(private).as_posix():dict(sha256=file_hash(p),shape=list(np.load(p).shape)) for p in (private/'parameters').glob(real+'_*/*.npy')}
 atomic(out/(real+'_manifest.json'),dict(archives=manifest,parameters=parameters,provenance=prov,source_hashes=read(out/'prefit_sources.json'),no_query_inputs_to_learner=True))
 print(real,scored['gates']['primary']['values'],scored['gates']['primary']['passed'],flush=True)

def main():
 p=argparse.ArgumentParser();p.add_argument('--realization',choices=REAL,required=True);p.add_argument('--private-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args();pub=read(a.output_root/'publication.json')
 if pub['commit']!=head() or not pub['verified']:raise ValueError('Published prefit checkpoint required')
 for path,h in read(a.output_root/'prefit_sources.json')['files'].items():
  if file_hash(ROOT/path)!=h:raise ValueError('Frozen scientific file changed')
 run(a.realization,a.private_root,a.output_root)
if __name__=='__main__':main()
