"""Package only this lane's immutable partial artifacts and verification receipts."""
import json,hashlib,shutil,subprocess,sys
from pathlib import Path
WT=Path.cwd();L=WT/'research/bavli_dataset_runs/run_20261125_01/lanes/L05';S=L/'session_20261126_03';W=Path('F:/Sefaria_QA/bavli_l05_workspace_20261126');J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True)
 if dst.exists():assert dst.read_bytes()==src.read_bytes(),str(dst)
 else:shutil.copyfile(src,dst)
for name in ['direct_shabbat','direct_temurah']:
 for p in (W/name).glob('*'):
  if p.is_file() and p.suffix in ['.json','.py']:put(p,S/name/p.name)
for p in (W/'review_session03').rglob('*'):
 if p.is_file() and p.suffix in ['.json','.sha256','.md']:put(p,S/'review'/p.relative_to(W/'review_session03'))
records=[]
for j in ['chullin','shabbat','yoma','shevuot','temurah','horayot']:
 job=J/('bavli_'+j)
 rep=json.loads(subprocess.check_output([sys.executable,'-X','utf8','research/bavli_production_v1/runner.py','replay','--job-dir',str(job)]))
 assert rep['replay_pass']; sh=rep['snapshot_sha256'];assert sha(job/'snapshots'/f'{sh}.json')==sh
 owner=json.loads((job/'OWNER.json').read_bytes());meta=json.loads((job/'JOB.json').read_bytes());assert owner==dict(epoch=2,owner='L05/'+j)
 ex=W/'exports/session03_delivery'/('bavli_'+j)
 if not ex.exists(): subprocess.check_output([sys.executable,'-X','utf8','research/bavli_production_v1/runner.py','export','--job-dir',str(job),'--output',str(ex)])
 manifest=json.loads((ex/'manifest.json').read_bytes())
 for rel,h in manifest['files'].items():assert sha(ex/rel)==h
 assert manifest['snapshot_sha256']==sh
 snap=json.loads((job/'snapshots'/f'{sh}.json').read_bytes())
 r=dict(job_id='bavli_'+j,owner=owner,source_sha256=meta['source_sha256'],schema_sha256=meta['schema_sha256'],protocol_sha256=meta['protocol_sha256'],replay=rep,export_dir=str(ex),export_manifest_sha256=sha(ex/'manifest.json'),open_tails=snap['open_tails'],active_records=sum(x['release_state']=='valid' for x in snap['records']),superseded_records=sum(x['release_state']=='superseded' for x in snap['records']),qualified_task_rows=0,required_review_complete=False)
 records.append(r)
 # Exact proposals, including original attempts; no source inventory/full source files in Git.
 for p in (job/'proposals').glob('*.json'):put(p,S/'accepted_and_attempted_proposals'/('bavli_'+j)/p.name)
(S/'CHECKPOINTS.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print([(x['job_id'],x['replay']['completed_by_layer']['claims'],x['replay']['next_unprocessed_by_layer']['claims']) for x in records])
print('all six replay/export manifests PASS')
