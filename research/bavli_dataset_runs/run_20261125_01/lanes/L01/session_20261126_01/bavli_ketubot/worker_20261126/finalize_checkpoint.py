from pathlib import Path
import sys,subprocess
root=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner as r
out=Path(__file__).parent;job=out.parent
active=r.read(root/'research/bavli_dataset_runs/ACTIVE_RUN.json')
assert r.sha((root/active['contract_path']).read_bytes())==active['contract_sha256']
code_hashes={}
for name in ['runner.py','schema.json','PROTOCOL.md']:
 rel='research/bavli_production_v1/'+name
 original=subprocess.check_output(['git','-C',str(root),'show',active['production_git_commit']+':'+rel])
 assert original==(root/rel).read_bytes()
 code_hashes[rel]=r.sha(original)
j,segs=r.load(job);s=r.current(job);replay=r.replay(job)
r.immutable(out/'replay_68.json',r.encoded(replay))
ex=r.export(job,out/'export_68')
packet=dict(run=active,job='bavli_ketubot',owner=r.read(job/'OWNER.json'),execution_agent='/root/ketubot_resume',source_sha256=j['source_sha256'],code_hashes=code_hashes,inherited_snapshot='107caa00ffc7786eb509da045b06f38c1862bd6ef6ea4714ace19d855ef2cc79',snapshot_sha256=replay['snapshot_sha256'],completed_by_layer=replay['completed_by_layer'],new_core='Ketubot 3b:1–4b:10 (29 original segments)',next_unprocessed='Ketubot 4b:11',next_action='Read 4b:11 and the speaker stub 4b:12 with the full continuation on 5a before proposing another batch. First inspect OWNER/CURRENT and revalidate source/contracts. Wait for lane review allocation before additional expansion.',open_tails=s['open_tails'],preserved_previous_segments=39,proposals=[dict(file=f'batch{n:03d}_proposal.json',sha256=r.sha((out/f'batch{n:03d}_proposal.json').read_bytes())) for n in range(1,4)],qualifications=dict(complete_tractate=False,independent_review_of_new_scope=False,ml_eligible=False,human_certification=False,source_read_context='Through4b:12; later continuation beyond4b:12 not yet read in this worker',unresolved=['3b:5 kohanot is retained without importing an expanded legal explanation.','4a:8 restriction resolves to menstruation in4a:9–4b:1; initial referent not treated as a lasting ruling for bereavement.','4b:4–7 spouse distinction and4b:8 Rav Ashi alternative retained separately.','No full corpus task-specific qualification or independent-review admission.'],original_uncertainty_record_count=sum(bool(x['uncertainty']) and x['release_state']=='valid' for x in s['records'])),stopped_reason='Lane lead requested bounded checkpoint pending next review allocation; no background continuation.',export_manifest_sha256=r.sha((out/'export_68/manifest.json').read_bytes()),replay_sha256=r.sha((out/'replay_68.json').read_bytes()),immutable_policy='Original proposals/snapshots retained; corrections require new record IDs and supersedes lineage. Authoring scripts are provenance, not resume commands; replay accepted proposals through runner instead.')
r.immutable(out/'RESUME_68.json',r.encoded(packet))
files={p.relative_to(out).as_posix():r.sha(p.read_bytes()) for p in sorted(out.rglob('*')) if p.is_file() and p.name!='HASHES_68.json'}
r.immutable(out/'HASHES_68.json',r.encoded(dict(snapshot_sha256=replay['snapshot_sha256'],files=files)))
print(dict(snapshot_sha256=replay['snapshot_sha256'],resume_sha256=r.sha((out/'RESUME_68.json').read_bytes()),manifest_sha256=r.sha((out/'HASHES_68.json').read_bytes()),export_manifest_sha256=packet['export_manifest_sha256'],replay_pass=replay['replay_pass'],files=len(files)))
