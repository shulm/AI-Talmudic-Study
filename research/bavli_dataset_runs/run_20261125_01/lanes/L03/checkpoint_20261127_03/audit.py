import sys,subprocess,datetime
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;coord=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study');sha=lambda p:runner.sha(p.read_bytes())
ap=coord/'research/bavli_dataset_runs/ACTIVE_RUN.json';a=runner.read(ap);cp=coord/a['contract_path'];c=runner.read(cp);assert sha(cp)==a['contract_sha256']==sha(root/a['contract_path'])
assert runner.sha(subprocess.check_output(['git','show',a['contract_commit']+':'+a['contract_path']],cwd=coord))==a['contract_sha256']
files=[]
for f,h in c['production_files'].items():
 row=dict(path=f,expected=h,lane=sha(root/f),coordinator=sha(coord/f),production_commit_blob=runner.sha(subprocess.check_output(['git','show',a['production_git_commit']+':'+f],cwd=coord)))
 assert all(row[k]==h for k in ['lane','coordinator','production_commit_blob']);files.append(row)
ledger=runner.read(coord/a['assignment_ledger']);assert ledger['revision']==a['assignment_revision'];rows=[]
for item in ledger['jobs']:
 if item['lane_id']!='L03':continue
 job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03')/item['job_id'];j,src=runner.load(job);owner=runner.read(job/'OWNER.json');assert owner==dict(owner=item['owner'],epoch=item['epoch'])
 assert j['source_sha256']==item['source_sha256'] and len(src)==item['source_segments']
 m=next(x for x in runner.read(job/'source_manifest.json')['tractates'] if x['title']==j['tractate']);source=Path(j['source_root'])/m['source_path'];schema=Path(j['source_root'])/m['schema_path'];raw=runner.read(source)
 assert sha(source)==m['source_sha256'] and sha(schema)==m['schema_sha256'];assert raw['versionTitle']=='Wikisource Talmud Bavli' and raw['language']=='he'
 state=runner.current(job);row=dict(job_id=item['job_id'],tractate=j['tractate'],owner=owner,source_path=str(source),source_sha256=sha(source),source_schema_path=str(schema),source_schema_sha256=sha(schema),source_segments=len(src),first_ref=next(iter(src.values()))['ref'],first_original_index=next(iter(src.values()))['source_index'],empty_original_page_indices=[i for i,p in enumerate(raw['text']) if not p],empty_original_string_positions=[[i,k] for i,p in enumerate(raw['text']) for k,t in enumerate(p) if not t],current_snapshot_sha256=runner.sha(runner.encoded(state)),ledger_historical_snapshot=item.get('checkpoint'),coverage=runner.report(state,src),live_owner_matches_ledger=True);rows.append(row)
assert sum(r['source_segments'] for r in rows)==13635 and len(rows)==7
audit=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),kind='read_only_actual_coordinator_and_local_production_audit',active_run=a,active_run_sha256=sha(ap),assignment_ledger_sha256=sha(coord/a['assignment_ledger']),ledger_note=ledger['revision_note'],contract_commit_verified=True,production_files=files,jobs=rows,source_corpora_modified=False,shared_files_modified=False,blockers=[],interpretation='Coordinator revision6 is last-observed historical capture, explicitly not simultaneous current production. Owners/epochs and immutable pins agree; later valid lane checkpoints are preserved.')
runner.immutable(out/'COORDINATOR_AUDIT.json',runner.encoded(audit));print(runner.sha((out/'COORDINATOR_AUDIT.json').read_bytes()))
