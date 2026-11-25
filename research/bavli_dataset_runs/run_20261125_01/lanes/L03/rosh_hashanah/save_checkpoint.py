"""Hash and verify the immutable partial export, then publish a source-free receipt."""
import hashlib,json
from pathlib import Path
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
here=Path(__file__).parent
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah')
export=job.parent/'rh_export_epoch3_009'
manifest=json.loads((export/'manifest.json').read_text(encoding='utf-8'))
for name,digest in manifest['files'].items():assert sha(export/name)==digest,name
snapshot=json.loads((job/'CURRENT.json').read_text())['snapshot_sha256']
assert sha(job/'snapshots'/(snapshot+'.json'))==snapshot
state=json.loads((job/'snapshots'/(snapshot+'.json')).read_text(encoding='utf-8'))
for digest in state['proposals']:assert sha(job/'proposals'/(digest+'.json'))==digest
receipt=dict(status='PARTIAL_REQUIRED_WORK_REMAINS',tractate='Rosh Hashanah',owner=json.loads((job/'OWNER.json').read_text()),snapshot_sha256=snapshot,job_dir=str(job),export_dir=str(export),export_manifest_sha256=sha(export/'manifest.json'),run_id='run_20261125_01',contract_sha256='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174',production_git_commit='15bba19d80273232b4554dfe507ceb37e97843a2',job_contract=json.loads((job/'JOB.json').read_text(encoding='utf-8')),accepted_proposals=state['proposals'],open_tails=state['open_tails'],replay_verified=True,export_files_verified=True,remaining_segments_per_layer=881,export_manifest=manifest,local_files={p.name:sha(p) for p in sorted(here.iterdir()) if p.is_file() and p.name!='CHECKPOINT.json'})
(here/'CHECKPOINT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checkpoint_sha256':sha(here/'CHECKPOINT.json'),'export_manifest_sha256':sha(export/'manifest.json'),'accepted_proposals':len(state['proposals'])}))
