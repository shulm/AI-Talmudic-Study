import json,hashlib,copy,importlib.util
from pathlib import Path
W=Path('F:/Sefaria_QA/worktrees/bavli-l05-production-20261126');H=W/'research/bavli_dataset_runs/run_20261125_01/lanes/L05/session_20261127_21';J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shevuot')
review=Path('F:/Sefaria_QA/bavli_l05_workspace_20261126/review_session20261127_21/shevuot/EXACT_VERSION_COMPARISON.json')
assert hashlib.sha256(review.read_bytes()).hexdigest()=='dd27852aeb6afb56b05eff327eb9f28791253f95c8573b1794ac7e537bf344d4'
old='ea0ef5e0d235439ba6f9d0968eda730670846cadbdcaabf1c7e47be3dc29d091';assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shevuot','epoch':2}
S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
mp={'she.s2708.revision':'she.s2721.w01.revision.closed','she.s2708.e.continuation':'she.s2721.w01.continuation'}
def remap(x):
 if isinstance(x,str):return mp.get(x,x)
 if isinstance(x,list):return [remap(y) for y in x]
 if isinstance(x,dict):return {k:remap(v) for k,v in x.items()}
 return x
R=[]
for r in S['records']:
 if r['id'] not in mp:continue
 n={k:copy.deepcopy(v) for k,v in r.items() if k not in ['release_state','review_state','ml_eligible']};n=remap(n);n['supersedes']=r['id']
 if r['id']=='she.s2708.revision':n['content']['boundary']='closed'
 R.append(n)
CV=[]
for v in S['coverage']:
 if not any(x in mp for x in v['record_ids']):continue
 n=remap({k:copy.deepcopy(t) for k,t in v.items() if k!='proposal_execution'});n['rationale']+=' S21-W01 boundary maintenance: same evidence completed at5a5 before5a6 Gufa; explicit closed successor and dependent remap. No new extraction coverage.';CV.append(n)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shevuot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=CV,open_tails=[x for x in S['open_tails'] if x!='she.s2708.revision'])
sp=importlib.util.spec_from_file_location('runner',W/'research/bavli_production_v1/runner.py');mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod);out=mod.validate_apply(S,P,{r['id']:r for r in I},M)
b=(json.dumps(P,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode();f=H/'shevuot_S21_W01_boundary_correction.json';assert not f.exists();f.write_bytes(b)
print(json.dumps({'proposal':hashlib.sha256(b).hexdigest(),'records':len(R),'coverage_updates':len(CV),'open_tails':P['open_tails'],'validation':'PASS'}))

