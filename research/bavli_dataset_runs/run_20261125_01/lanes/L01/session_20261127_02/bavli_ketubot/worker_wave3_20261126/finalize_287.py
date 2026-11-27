from pathlib import Path
import sys,subprocess
root=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study');sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner as r
out=Path(__file__).parent;job=out.parent;active=r.read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json')
assert active['contract_sha256']=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
assert active['production_git_commit']=='15bba19d80273232b4554dfe507ceb37e97843a2'
assert next(x for x in r.read(root/active['assignment_ledger'])['jobs'] if x['job_id']=='bavli_ketubot')['lane_id']=='L01'
assert r.sha((root/active['contract_path']).read_bytes())==active['contract_sha256']
code={}
for name in ['runner.py','schema.json','PROTOCOL.md']:
 rel='research/bavli_production_v1/'+name;b=(root/rel).read_bytes();assert b==subprocess.check_output(['git','-C',str(root),'show',active['production_git_commit']+':'+rel]);code[rel]=r.sha(b)
j,segs=r.load(job);state=r.current(job);expected='08798bb1cf9f26dc18830157f1b4120bb4c796f89a160f801dd43ef812b064e5';assert r.sha(r.encoded(state))==expected
r.authorize(job,'/root/ketubot_resume',3)
replay=r.replay(job);r.immutable(out/'replay_287.json',r.encoded(replay));r.export(job,out/'export_287')
valid=[x for x in state['records'] if x['release_state']=='valid']
risks=[dict(record_id=x['id'],layer=x['layer'],uncertainty=x['uncertainty'],source_refs=sorted({segs[e['segment_id']]['ref'] for e in x['evidence']})) for x in valid if x['uncertainty']]
r.immutable(out/'uncertainty_inventory_287.json',r.encoded(dict(snapshot_sha256=expected,records=risks,qualification='Record-level uncertainty inventory, not unique-case count or completed review.')))
packet=dict(run=active,code_hashes=code,owner=r.read(job/'OWNER.json'),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),source_sha256=j['source_sha256'],source_segments=j['source_segments'],inherited_snapshot='7bc6330f2fe638fc45f3fa0a8220c61f21ba228f19bada3f0005c7c027407ffa',snapshot_sha256=expected,completed_by_layer=replay['completed_by_layer'],remaining_segments_per_layer=2751,completed_range='Ketubot2a:1–13a:9',new_core_range='Ketubot11a:15–13a:9',new_core_segments=55,next_ref='Ketubot13a:10',open_tails=state['open_tails'],records=dict(total=len(state['records']),valid=len(valid),superseded=sum(x['release_state']=='superseded' for x in state['records']),with_supported_uncertainty=len(risks)),review=dict(inherited_graph_corrections_verified=True,branch_atomic_independent_verification='Pending exact-version recheck per parent; no acceptance claim',wave3_independent_review=False,full_tractate_review=False,human_certification=False,ml_eligible=False),next_action='Resume13a:10. Source read through14a:10; before completing later unit read full continuation. The13a:10–13b:10 unit distinguishes seclusion/intercourse and explicitly refutes Rav Asi at13b:10. Revalidate owner/current/source/pins. Preserve originals and supersede any corrections with dependencies. Replay accepted proposals using runner.replay, not authoring scripts.',stop_kind='Durable intermediate resume packet; full-tractate mandate remains active and incomplete.',provenance_notes=['Six manually authored source batches; helper code serializes manual judgments and exact evidence spans.','Both Rav/Shmuel transmissions, Rav/Rabbah/Rava distinction and Eliezer/Eleazar distinction preserved.','Earlier independent-review findings and supersession corrections inherited intact; no new review admission claimed.','No shared schema/code, source corpus or other tractate modified; no commit or push.'],export_manifest_sha256=r.sha((out/'export_287/manifest.json').read_bytes()),replay_sha256=r.sha((out/'replay_287.json').read_bytes()),current_proposals=state['proposals'])
r.immutable(out/'RESUME_287.json',r.encoded(packet))
manifest=dict(snapshot_sha256=expected,files={p.relative_to(out).as_posix():r.sha(p.read_bytes()) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='HASHES_287.json'})
r.immutable(out/'HASHES_287.json',r.encoded(manifest))
for rel,h in manifest['files'].items():assert r.sha((out/rel).read_bytes())==h
print(dict(snapshot_sha256=expected,replay_pass=replay['replay_pass'],completed=287,remaining=2751,records=packet['records'],files=len(manifest['files']),resume_sha256=r.sha((out/'RESUME_287.json').read_bytes()),hashes_sha256=r.sha((out/'HASHES_287.json').read_bytes()),export_manifest_sha256=packet['export_manifest_sha256']))
