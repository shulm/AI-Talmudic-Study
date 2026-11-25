"""Staged synthetic-only execution. No human cache imports."""
import argparse
import io
from core import *
from head import fit,adapt,probabilities,certificate
from fixture import generate,contrast,expected_nll
RHO={f'p{i}':float(np.sqrt(p)) for i,p in enumerate([1e-5,1e-4,1e-3])}
SEEDS=[11,29,47]
REGIMES=['positive','null']
BaseLedger=Ledger
class Ledger(BaseLedger):
 def __init__(self,stage,expected,out):
  super().__init__(stage,expected,out)
  if os.environ.get('DIAGNOSTIC_PRIVATE_ROOT'):
   self.parameter_root=Path(os.environ['DIAGNOSTIC_PRIVATE_ROOT'])/'parameters'/stage

def meta2(kind,c=None,seed=None,n=0):
 return dict(kind=kind,candidate=c,rho=RHO.get(c),lambda_b=.1,seed=seed,person_solves=n)
def expected(stage,c=None):
 e={}
 if stage.endswith('offsets'):
  for r in REGIMES:e[r]=meta2('offset',n=48)
 elif stage=='A_batch':
  for m in ['B3','11','29','47']:
   for n in [1,7]:e[f'{m}_{n}']=meta2('adapt',c,None if m=='B3' else int(m),n)
 else:
  dev=stage=='A_dev'; cs=list(RHO) if dev else [c]; conditions=['informative'] if dev else ['informative','uninformative']
  for r in REGIMES:
   for h in conditions:e[f'{r}_{h}_B3']=meta2('adapt',n=24)
   for cc in cs:
    for seed in SEEDS:
     if dev or stage=='B_test':e[f'{r}_{cc}_{seed}_shared']=meta2('shared',cc,seed)
     for h in conditions:e[f'{r}_{cc}_{seed}_{h}']=meta2('adapt',cc,seed,24)
 return e

def save_npz(path,arrays):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 buffer=io.BytesIO();np.savez_compressed(buffer,**arrays)
 with path.open('xb') as f:f.write(buffer.getvalue())
 return dict(sha256=file_hash(path),arrays={k:dict(shape=list(v.shape),dtype=str(v.dtype)) for k,v in arrays.items()})
def load_npz(path):
 with np.load(path,allow_pickle=False) as a:return {k:a[k] for k in a.files}
def materialize(private,real):
 z,base,b,u,v,sp,ys,ps=generate(20261126 if real=='A' else 20261127,2719 if real=='A' else 2720)
 a=dict(z=z,base=base,bias=b,u=u,v=v,**{'split_'+k:x for k,x in sp.items()},**{'y_'+k:x for k,x in ys.items()},**{'oracle_'+k:x for k,x in ps.items()})
 return a,save_npz(private/(real+'_fixture.npz'),a)
def views(a,partition,r,h):
 people=slice(48,72) if partition=='dev' else slice(72,96)
 su=a['split_support'];qu=a['split_development' if partition=='dev' else 'split_test']
 zs=a['z'][su] if h=='informative' else np.zeros_like(a['z'][su])
 y=a['y_'+r+('' if h=='informative' else '_uninformative')][people][:,su]
 return zs,y,a['base'][su],a['z'][qu],a['base'][qu],a['y_'+r][people][:,qu],a['oracle_'+r][people][:,qu]
def sampled(p,y):
 return dict(nll=float(-np.log(np.maximum(np.take_along_axis(p,y[...,None],-1)[...,0],1e-12)).mean()),accuracy=float((p.argmax(-1)==y).mean()),brier=float(((p-np.eye(3)[y])**2).sum(-1).mean()))
def summarize(arrays,r,c,h):
 key=f'{r}_{c}_{h}';oracle=arrays[r+'_oracle'];y=arrays[r+'_y']; b=arrays[f'{r}_{h}_B3'];p=np.mean([arrays[f'{key}_{seed}'] for seed in SEEDS],axis=0)
 eb,em,eo=[expected_nll(x,oracle) for x in [b,p,oracle]];truth=contrast(oracle);est=contrast(p);den=float(np.mean(truth**2))
 return dict(regime=r,candidate=c,rho=RHO[c],condition=h,expected_nll_B3=eb,expected_nll_M1=em,expected_nll_oracle=eo,expected_gain=eb-em,oracle_gap_recovery=(eb-em)/(eb-eo) if eb-eo>1e-12 else None,contrast_normalized_rmse=float(np.sqrt(np.mean((est-truth)**2)/den)) if den>1e-20 else None,predicted_contrast_rms=float(np.sqrt(np.mean(est**2))),metrics={m:dict(**sampled(q,y),expected_nll=expected_nll(q,oracle)) for m,q in {'M1':p,'B3':b,'B1':arrays[f'{r}_{h}_B1'],'B2':arrays[f'{r}_{h}_B2'],'oracle':oracle}.items()},seeds={str(s):dict(**sampled(arrays[f'{key}_{s}'],y),expected_nll=expected_nll(arrays[f'{key}_{s}'],oracle)) for s in SEEDS})
def gates(rows,c):
 p=next(x for x in rows if x['candidate']==c and x['regime']=='positive' and x['condition']=='informative');n=next(x for x in rows if x['candidate']==c and x['regime']=='null' and x['condition']=='informative')
 return dict(gain=p['expected_gain']>=.05,recovery=p['oracle_gap_recovery'] is not None and p['oracle_gap_recovery']>=.5,contrast=p['contrast_normalized_rmse'] is not None and p['contrast_normalized_rmse']<=.5,null=-n['expected_gain']<=.01)
def select(rows):
 ok=[c for c in RHO if all(gates(rows,c).values())]
 if not ok:return None
 gain={c:next(x['expected_gain'] for x in rows if x['candidate']==c and x['regime']=='positive') for c in ok};best=max(gain.values())
 return max([c for c in ok if best-gain[c]<=1e-5],key=lambda c:RHO[c])
def publication(out,name):
 p=read(out/(name+'_publication.json'))
 if p['commit']!=head():raise ValueError('Publication HEAD mismatch')
 if not p['issue_url'] or not p['pr_url']:raise ValueError('Publication links required')
 return p

def offsets(a,real,cs,out):
 ledger=Ledger(real+'_offsets',expected(real+'_offsets'),out); tr=a['split_train'];rows=[]
 for r in REGIMES:
  y=a['y_'+r][:48][:,tr];b=adapt(a['z'][tr],y,a['base'][tr],0,.1,None,ledger,r)
  for c in cs:rows.append(dict(regime=r,candidate=c,**certificate(a['z'][tr],y,a['base'][tr],b,RHO[c],.1)))
 atomic(out/(real+'_certificates.json'),dict(rows=rows,audit=ledger.validate()))
def evaluate(a,stage,cs,private,out,models=None):
 ledger=Ledger(stage,expected(stage,None if stage=='A_dev' else cs[0]),out);models={} if models is None else models;arrays={};dev=stage=='A_dev';conditions=['informative'] if dev else ['informative','uninformative'];tr=a['split_train']
 for r in REGIMES:
  yt=a['y_'+r][:48][:,tr];prior=np.bincount(yt.ravel(),minlength=3)/yt.size
  for c in cs:
   for seed in SEEDS:
    key=f'{r}_{c}_{seed}'
    if dev or stage=='B_test':models[key]=fit(a['z'][tr],yt,a['base'][tr],2,RHO[c],.1,seed,ledger,key+'_shared')
  for h in conditions:
   zs,y,bs,zq,bq,yq,oracle=views(a,'dev' if dev else 'test',r,h)
   arrays[r+'_oracle']=oracle;arrays[r+'_y']=yq
   b=adapt(zs,y,bs,0,.1,None,ledger,f'{r}_{h}_B3');arrays[f'{r}_{h}_B3']=probabilities(zq,bq,b)
   freq=(np.eye(3)[y].sum(1)+4*prior)/(y.shape[1]+4);arrays[f'{r}_{h}_B1']=np.broadcast_to(freq[:,None],oracle.shape).copy();arrays[f'{r}_{h}_B2']=np.broadcast_to(__import__('scipy').special.softmax(bq,-1)[None],oracle.shape).copy()
   for c in cs:
    for seed in SEEDS:
     v=models[f'{r}_{c}_{seed}'];p=adapt(zs,y,bs,RHO[c],.1,v,ledger,f'{r}_{c}_{seed}_{h}');arrays[f'{r}_{c}_{h}_{seed}']=probabilities(zq,bq,p,v)
 audit=ledger.validate();manifest=save_npz(private/(stage+'_predictions.npz'),arrays);mm=save_npz(private/(stage+'_models.npz'),models)
 rows=[summarize(arrays,r,c,h) for r in REGIMES for c in cs for h in conditions]
 atomic(out/(stage+'.json'),dict(rows=rows,gates={c:gates(rows,c) for c in cs},audit=audit,predictions=manifest,models=mm))
 return rows,models,arrays

def batch(a,c,models,arrays,out):
 ledger=Ledger('A_batch',expected('A_batch',c),out);zs,y,bs,zq,bq,yq,oracle=views(a,'dev','positive','informative');rows=[]
 for m in ['B3','11','29','47']:
  v=None if m=='B3' else models[f'positive_{c}_{m}'];ref=arrays['positive_informative_B3' if m=='B3' else f'positive_{c}_informative_{m}']
  for n in [1,7]:
   p=adapt(zs,y[:n],bs,RHO[c],.1,v,ledger,f'{m}_{n}');pr=probabilities(zq,bq,p,v)
   rows.append(dict(model=m,n=n,probability_difference=float(np.max(np.abs(pr[0]-ref[0]))),expected_nll_difference=abs(expected_nll(pr[:1],oracle[:1])-expected_nll(ref[:1],oracle[:1]))))
 passed=all(x['probability_difference']<=1e-6 and x['expected_nll_difference']<=1e-5 for x in rows)
 atomic(out/'A_batch.json',dict(rows=rows,passed=passed,audit=ledger.validate()));return passed

def main():
 parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['development','freeze','heldout-a','heldout-b']);parser.add_argument('--private-root',type=Path,required=True);parser.add_argument('--output-root',type=Path,required=True);args=parser.parse_args();private=args.private_root;out=args.output_root
 os.environ['DIAGNOSTIC_PRIVATE_ROOT']=str(private)
 if args.stage=='development':
  publication(out,'prefit');a,manifest=materialize(private,'A');atomic(out/'A_fixture_manifest.json',manifest);offsets(a,'A',list(RHO),out);rows,models,arrays=evaluate(a,'A_dev',list(RHO),private,out);c=select(rows)
  passed=batch(a,c,models,arrays,out) if c else False
  atomic(out/'development_decision.json',dict(candidate=c,status='ELIGIBLE' if c and passed else ('NUMERICALLY_UNRESOLVED' if c else 'NO_QUALIFIED_INTERACTION'),batch_passed=passed))
 elif args.stage=='freeze':
  d=read(out/'development_decision.json')
  if d['status']!='ELIGIBLE':raise ValueError('No valid selection')
  c=d['candidate'];atomic(out/'SELECTION.json',dict(**d,rho=RHO[c],lambda_b=.1,development_hash=file_hash(out/'A_dev.json'),model_hash=file_hash(private/'A_dev_models.npz'),later_manifests={s:expected(s,c) for s in ['A_test','B_offsets','B_test']}))
 else:
  publication(out,'selection');s=read(out/'SELECTION.json');c=s['candidate']
  if file_hash(private/'A_dev_models.npz')!=s['model_hash']:raise ValueError('Model hash mismatch')
  if args.stage=='heldout-a':evaluate(load_npz(private/'A_fixture.npz'),'A_test',[c],private,out,load_npz(private/'A_dev_models.npz'))
  else:
   if not (out/'A_test.json').exists():raise ValueError('A evaluation required first')
   a,m=materialize(private,'B');atomic(out/'B_fixture_manifest.json',m);offsets(a,'B',[c],out);evaluate(a,'B_test',[c],private,out)
if __name__=='__main__':main()
