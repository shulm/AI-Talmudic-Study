"""Pinned checkpoint/replay/export audit; no source or canonical graph mutations."""
import json,re,hashlib
from pathlib import Path
from author_lib_cont2 import Author,r
a=Author('audit253');root=Path.cwd();here=Path(__file__).resolve().parent
expected='83703222712ce4dda8a900326878ea0351e44318321431771ea10deb69e635a1'
assert r.read(a.job/'CURRENT.json')['snapshot_sha256']==expected
assert r.read(a.job/'OWNER.json')==dict(owner='L04/makkot_resume_20261126',epoch=3)
contract_path=root/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
contract_sha=r.sha(contract_path.read_bytes());assert contract_sha=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
contract=r.read(contract_path)
for name,h in contract['production_files'].items():assert r.sha((root/name).read_bytes())==h,name
state=r.current(a.job);active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
scope_count=0
for row in active.values():
 if row['layer']=='attributions':
  for rid in re.findall(r'ma\.[A-Za-z0-9_.]+',row['content']['scope']):
   assert rid.rstrip('.') in active,(row['id'],rid)
   scope_count+=1
replay=r.replay(a.job);assert replay['replay_pass'] and replay['snapshot_sha256']==expected
out=a.job/'exports'/'resume_20261127_253';result=r.export(a.job,out)
export_hashes={str(p.relative_to(out)).replace('\\','/'):r.sha(p.read_bytes()) for p in out.rglob('*') if p.is_file()}
attempts={'author_013.py':'Prevalidation rejected unsupported assertion enum counterfactual; proposal preserved as rejected_prevalidation_r013.json; accepted013b uses hypothetical.', 'author_014.py':'Prevalidation rejected unsupported relation alternative; proposal preserved as rejected_prevalidation_r014.json; accepted014b links actual alternative replies to the question.', 'author_015.py':'Exact-span uniqueness assertion failed on first repeated inspection phrase; preserved author; accepted015b uses unique whitespace-bounded original span.', 'author_017.py':'Exact-span uniqueness assertion failed on repeated דגמיר; preserved author.', 'author_017b.py':'Exact-span uniqueness assertion failed on repeated sub-peruta phrase; preserved author.', 'author_017c.py':'Prevalidation rejected claim continuation endpoints; proposal preserved as rejected_prevalidation_r017c.json; accepted017d uses qualification.'}
checkpoint=dict(status='PARTIAL_REQUIRED_WORK_REMAINS',snapshot_sha256=expected,job=str(a.job),owner=r.read(a.job/'OWNER.json'),source_sha256=a.j['source_sha256'],source_schema_sha256=r.sha(Path('F:/Sefaria-Export-master/schemas/Makkot.json').read_bytes()),run_contract_sha256=contract_sha,production_git_commit=contract['production_git_commit'],production_hashes_verified=contract['production_files'],replay=replay,covered_by_each_required_layer=253,total_source_segments=709,remaining_by_each_required_layer=456,last_completed='Makkot 10a:9',next_source='Makkot 10a:10',source_read_context_through='Makkot 10a:24',active_records=len(active),all_record_versions=len(state['records']),superseded_records=len(state['records'])-len(active),open_tails=state['open_tails'],proposal_chain=state['proposals'],export_directory=str(out),export_hashes=export_hashes,author_scripts={p.name:r.sha(p.read_bytes()) for p in here.glob('author_*.py')},checkpoint_script_sha256=r.sha(Path(__file__).read_bytes()),rejected_attempts=attempts,embedded_scope_references_verified=scope_count,new_paid_api_calls=0,ml_eligible=False,review_state='All new coverage013b–021 remains independently unreviewed. Earlier review retains only its own exact scope/version.',promotion_status='Holding further canonical promotion at parent request to match independent review capacity; no ownership change.',notes=['New production used actual agent /root/makkot_continuation_2.','r020 corrects only malformed English Rav Hisda label and revises all dependent records, content scopes and coverage.','No common runner/schema/protocol/source corpus changes; no commit or push.','No claim of exhaustive answer inventories: partial only where actual source-supported answer inventory is represented.','Readiness and replay verify integrity, not scholarly completeness.'])
r.immutable(here/'CHECKPOINT_253.json',r.encoded(checkpoint));print(json.dumps({k:checkpoint[k] for k in ['snapshot_sha256','covered_by_each_required_layer','active_records','all_record_versions','next_source','export_directory','embedded_scope_references_verified']},ensure_ascii=False))
