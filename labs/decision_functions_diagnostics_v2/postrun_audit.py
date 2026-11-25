"""Post-run independent selection, seed, certificate and preservation audit; no fits."""
import argparse
from core import *
from verify import independent,close,check_archive
from study import RHO,SEEDS,load_npz

def main(private):
 errors=[];out=OUT;before={str(p.relative_to(private)):file_hash(p) for p in private.rglob('*') if p.is_file()};stages={s:read(out/(s+'.json')) for s in ['A_dev','A_test','B_test']};gate_results={}
 for stage,data in stages.items():
  a=check_archive(private/(stage+'_predictions.npz'),data['predictions']);gs={}
  for row in data['rows']:
   r,c,h=row['regime'],row['candidate'],row['condition'];y=a[r+'_y'];o=a[r+'_oracle']
   for seed in SEEDS:
    m=independent(a[f'{r}_{c}_{h}_{seed}'],y,o)
    for k,v in m.items():
     if k in row['seeds'][str(seed)]:errors.append(close(v,row['seeds'][str(seed)][k]))
  for c in data['gates']:
   p=next(x for x in data['rows'] if x['regime']=='positive' and x['candidate']==c and x['condition']=='informative');n=next(x for x in data['rows'] if x['regime']=='null' and x['candidate']==c and x['condition']=='informative')
   gs[c]=dict(gain=p['expected_gain']>=.05,recovery=p['oracle_gap_recovery']>=.5,contrast=p['contrast_normalized_rmse']<=.5,null=n['expected_nll_M1']-n['expected_nll_B3']<=.01)
  assert gs==data['gates'];gate_results[stage]=gs
 eligible=[c for c,g in gate_results['A_dev'].items() if all(g.values())];gains={c:next(r['expected_gain'] for r in stages['A_dev']['rows'] if r['candidate']==c and r['regime']=='positive') for c in eligible};best=max(gains.values());chosen=max((c for c in eligible if best-gains[c]<=1e-5),key=lambda c:RHO[c]);assert chosen==read(out/'SELECTION.json')['candidate']
 pairs={};certificates=[]
 for real in ['A','B']:
  a=load_npz(private/(real+'_fixture.npz'));tr=a['split_train'];z=a['z'][tr];s=48;n=len(tr)
  for r in ['positive','null']:
   bias=np.load(private/'parameters'/(real+'_offsets')/(r+'.npy')).reshape(48,3);y=a['y_'+r][:48][:,tr];logits=a['base'][tr][None]+bias[:,None];ex=np.exp(logits-logits.max(-1,keepdims=True));p=ex/ex.sum(-1,keepdims=True);diff=p-np.eye(3)[y];res=diff.mean(1)+.1*bias
   g=np.stack([np.einsum('ic,id->cd',diff[i],z).reshape(-1) for i in range(s)])/(s*n);sv=np.linalg.svd(g,compute_uv=False)[0];error=np.linalg.norm(z,2)*np.linalg.norm(res)/(2*s*np.sqrt(n)*.1)+100*np.finfo(float).eps*max(1,np.linalg.norm(g))
   for row in read(out/(real+'_certificates.json'))['rows']:
    if row['regime']==r:
     errors+=[close(sv,row['spectral_norm']),close(error,row['error_bound']),close(RHO[row['candidate']]/np.sqrt(s)-sv,row['signed_margin'])];certificates.append(dict(realization=real,**row))
  oracle=a['oracle_positive'];observed=np.eye(3)[a['y_positive']]
  pairs[real]=dict(expected_max_pair_class_frequency_difference=float(np.abs(oracle[::2].mean(1)-oracle[1::2].mean(1)).max()),sampled_max_pair_class_frequency_difference=float(np.abs(observed[::2].mean(1)-observed[1::2].mean(1)).max()),scope='all generated cases; descriptive, not a selection gate; matched offsets do not imply exactly matched class frequencies')
 # Confirm executed source bytes match the published prefit manifest.
 for p,h in read(out/'prefit_source_manifest.json')['files'].items():assert file_hash(ROOT/p)==h
 preserved=[]
 for prefix in ['labs/decision_functions/','labs/decision_functions_diagnostics/','research/decision_functions_2026-11-24/runs/pilot_v1/','research/decision_functions_2026-11-24/runs/interaction_diagnostics_v1/']:
  paths=subprocess.check_output(['git','ls-tree','-r','--name-only','3c93bd5c9ef9c14825e45c089fba0b59106d8a36','--',prefix],text=True).splitlines()
  for p in paths:
   assert git_bytes('3c93bd5c9ef9c14825e45c089fba0b59106d8a36',p)==git_bytes('HEAD',p);preserved.append(p)
 after={str(p.relative_to(private)):file_hash(p) for p in private.rglob('*') if p.is_file()};assert before==after
 records=[read(p) for p in (out/'records').glob('*/*.complete.json')];assert len(records)==88
 assert sum(x['meta']['kind']=='shared' for x in records)==24
 assert sum(x['meta']['person_solves'] for x in records)==1472
 for x in records:
  path=private/'parameters'/next(p.parent.name for p in (out/'records').glob('*/'+x['id']+'.complete.json') if read(p)==x)/(x['id']+'.npy')
  vector=np.load(path);assert len(vector)==x['parameter_count'];errors.append(close(np.linalg.norm(vector),x['parameter_norm']))
 atomic(out/'supplemental_verification.json',dict(status='PASS',zero_new_fits=True,max_discrepancy=max(errors),comparisons=len(errors),selected_candidate=chosen,gates=gate_results,certificates=certificates,matched_pair_frequency_diagnostics=pairs,preserved_files=len(preserved),preserved_paths=preserved,all_prefit_source_hashes_unchanged=True,private_hashes_unchanged=True,parameter_vectors_verified=88,max_optimizer_gradient=max(r['gradient_max'] for r in records),max_person_scaled_gradient=max(r['person_scaled_gradient_max'] for r in records)))
 print('PASS supplemental verification',len(errors),max(errors))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--private-root',type=Path,required=True);a=p.parse_args();main(a.private_root)
