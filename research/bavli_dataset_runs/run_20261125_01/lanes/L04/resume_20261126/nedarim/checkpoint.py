"""Read-only audit plus immutable export/receipt for the current accepted state."""
import importlib.util,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[5];REPO=ROOT.parent
spec=importlib.util.spec_from_file_location('r',ROOT/'bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_nedarim')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
contract_path=ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
pointer=r.read(ROOT/'bavli_dataset_runs/ACTIVE_RUN.json');contract=r.read(contract_path)
assert sha(contract_path)==pointer['contract_sha256']
for relative in ['research/bavli_production_v1/runner.py','research/bavli_production_v1/schema.json','research/bavli_production_v1/PROTOCOL.md']:
    assert sha(REPO/relative)==contract['production_files'][relative],relative
owner=r.read(JOB/'OWNER.json');assert owner=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
audit=r.replay(JOB);version=audit['snapshot_sha256'];s=r.current(JOB)
output=JOB/'exports'/version;export=r.export(JOB,output)
for name,h in export['files'].items():assert sha(output/name)==h,name
for layer in r.LAYERS[:-1]:
    rows=[json.loads(line) for line in (output/(layer+'.jsonl')).read_text(encoding='utf-8').splitlines()]
    assert rows==[x for x in s['records'] if x['layer']==layer]
active={x['id']:x for x in s['records'] if x['release_state']=='valid'}
superseded={x['id'] for x in s['records'] if x['release_state']=='superseded'}
assert all(not x['ml_eligible'] for x in s['records'])
for x in active.values():
    if x['layer']=='attributions':assert x['content']['scope'] not in superseded,x['id']
count=audit['completed_by_layer']['structure']
receipt=dict(status='PARTIAL_REQUIRED_WORK_REMAINS',owner=owner,job=str(JOB),snapshot_sha256=version,source_sha256=r.read(JOB/'JOB.json')['source_sha256'],contract_sha256=pointer['contract_sha256'],replay_pass=True,export_exact_content_pass=True,export_path=str(output),export_manifest_sha256=sha(output/'manifest.json'),coverage=audit,active_records=len(active),all_ml_eligible_false=True,superseded_attribution_scope_audit_pass=True,authoring_scripts={p.name:sha(p) for p in sorted(HERE.glob('author_*.py'))},next_work=audit['next_unprocessed_by_layer'],review='Independent opening comparison exists separately; no full-tractate review acceptance claimed.',resume='Verify OWNER and CURRENT, replay; read pinned original next source through relevant continuation with runner.load. Author next immutable manual proposal; preserve rejected/staged variants. No API, git commit or push authorized in this delegate.',rejected_staging_notes=['continuation_006.json: addressee role rejected; corrected006b represents addressee as narrative context without schema changes.','continuation_008.json: null surface rejected; corrected008b carries original authority introduction.','continuation_009.json: staged only, refined to009b before submission.'])
out=HERE/f'CHECKPOINT_{count}_{version[:12]}.json';r.immutable(out,r.encoded(receipt));print(json.dumps(dict(receipt=str(out),snapshot=version,coverage=count,active_records=len(active),next=audit['next_unprocessed_by_layer']['structure']),ensure_ascii=False))
