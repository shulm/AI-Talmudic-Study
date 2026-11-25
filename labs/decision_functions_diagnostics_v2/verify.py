"""Independent saved-array arithmetic, no optimization."""
import argparse
from core import *
from study import RHO,SEEDS,expected,load_npz

def close(a,b):
 e=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
 if not np.isfinite(e) or e>1e-12:raise ValueError('Arithmetic mismatch '+str(e))
 return e
def check_archive(path,manifest):
 if file_hash(path)!=manifest['sha256']:raise ValueError('Corrupted artifact')
 a=load_npz(path)
 if set(a)!=set(manifest['arrays']):raise ValueError('Missing/unexpected arrays')
 for k,v in a.items():
  if list(v.shape)!=manifest['arrays'][k]['shape'] or str(v.dtype)!=manifest['arrays'][k]['dtype'] or not np.isfinite(v).all():raise ValueError('Shape/dtype/nonfinite')
 return a
def valid_probability(p):
 if p.shape!=(24,36,3) or (p<0).any() or not np.isfinite(p).all():raise ValueError('Invalid probability')
 close(p.sum(-1),1)
def independent(p,y,o):
 nll=-np.log(np.clip(p[np.arange(24)[:,None],np.arange(36)[None,:],y],1e-12,None)).mean()
 return dict(nll=float(nll),accuracy=float(np.mean(np.argmax(p,axis=2)==y)),brier=float(np.mean(np.sum((p-np.eye(3)[y])**2,axis=2))),expected_nll=float(np.mean(-np.sum(o*np.log(np.clip(p,1e-12,None)),axis=2))))
def con(p):
 lp=np.log(np.clip(p,1e-12,None));out=[]
 for i,j in [(0,1),(0,2),(1,2)]:
  d=(lp[::2,:,i]-lp[::2,:,j])-(lp[1::2,:,i]-lp[1::2,:,j]);out.append(d-d[:,0,None])
 return np.stack(out,-1)
def verify(private,out):
 before={str(p.relative_to(private)):file_hash(p) for p in private.rglob('*') if p.is_file()};errors=[];counts={};stages=[]
 for real in ['A','B']:
  if (out/(real+'_fixture_manifest.json')).exists():check_archive(private/(real+'_fixture.npz'),read(out/(real+'_fixture_manifest.json')))
 for stage in ['A_dev','A_test','B_test']:
  if not (out/(stage+'.json')).exists():continue
  result=read(out/(stage+'.json'));a=check_archive(private/(stage+'_predictions.npz'),result['predictions']);check_archive(private/(stage+'_models.npz'),result['models']);stages.append(stage)
  for k,p in a.items():
   if not k.endswith('_y'):valid_probability(p)
  for row in result['rows']:
   r,c,h=row['regime'],row['candidate'],row['condition'];o=a[r+'_oracle'];y=a[r+'_y'];p=sum(a[f'{r}_{c}_{h}_{s}'] for s in SEEDS)/3
   for m,q in dict(M1=p,B3=a[f'{r}_{h}_B3'],B1=a[f'{r}_{h}_B1'],B2=a[f'{r}_{h}_B2'],oracle=o).items():
    for k,v in independent(q,y,o).items():errors.append(close(v,row['metrics'][m][k]))
   eb=row['metrics']['B3']['expected_nll'];em=row['metrics']['M1']['expected_nll'];eo=row['metrics']['oracle']['expected_nll'];errors.append(close(eb-em,row['expected_gain']))
   if row['oracle_gap_recovery'] is not None:errors.append(close((eb-em)/(eb-eo),row['oracle_gap_recovery']))
   t=con(o);e=con(p);den=np.mean(t*t)
   errors.append(close(np.sqrt(np.mean(e*e)),row['predicted_contrast_rms']))
   if row['contrast_normalized_rmse'] is not None:errors.append(close(np.sqrt(np.mean((e-t)**2)/den),row['contrast_normalized_rmse']))
 for path in (out/'records').iterdir():
  exp=read(path/'expected.json');c=next((v['candidate'] for v in exp.values() if v['candidate'] is not None),None)
  if exp!=expected(path.name,c):raise ValueError('Manifest differs from predeclared IDs')
  counts[path.name]=validate_records(path,exp)
 after={str(p.relative_to(private)):file_hash(p) for p in private.rglob('*') if p.is_file()}
 if before!=after:raise ValueError('Private artifacts changed')
 n=sum(x['records'] for x in counts.values());people=sum(x['person_solves'] for x in counts.values())
 if n>88 or people>1472:raise ValueError('Scientific budget exceeded')
 atomic(out/'verification.json',dict(status='PASS',comparisons=len(errors),max_error=max(errors,default=0),ledgers=counts,optimizer_records=n,person_solves=people,private_hashes_before=before,private_hashes_after=after,stages=stages))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args();verify(a.private_root,a.output_root)
