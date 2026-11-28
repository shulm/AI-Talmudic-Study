import copy,json,sys
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'kiddushin/correction_004_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');sha=lambda p:runner.sha(p.read_bytes())
version='22fcc9db9d44621f894e577bd245b76213e59027322fe50868f6635e2eee39a7';state=runner.read(job/'snapshots'/f'{version}.json');assert runner.sha(runner.encoded(state))==version
base=runner.read(job/'snapshots/a1a0d044030d74c61d84376a6feb004f2dec4a8fb36d6c246fd326013859742b.json');p=runner.read(prod/'PROPOSAL.json');assert sha(prod/'PROPOSAL.json')=='db8682a097b2f4c18f31836151ad8b58101e2d072a62af6cebedfcb84e416514';j,src=runner.load(job)
applied=runner.validate_apply(base,p,src,j);applied['proposals']=base['proposals']+[sha(prod/'PROPOSAL.json')];assert runner.encoded(applied)==runner.encoded(state)
assert len(p['records'])==1;r=p['records'][0];assert r['supersedes']=='kid004.revised.kid003.sale_corrects';assert r['content']['source_id']=='kid003.context.aylonit_sale' and r['content']['target_id']=='kid004.no_signs_no_sale' and r['content']['relation']=='correction'
now={r['id']:r for r in state['records']}
for old in base['records']:
 expected=copy.deepcopy(old)
 if old['id']==r['supersedes']:expected['release_state']='superseded'
 assert now[old['id']]==expected
assert {(c['segment_id'],c['layer']) for c in state['coverage']}=={(c['segment_id'],c['layer']) for c in base['coverage']}
rp=runner.replay(job);assert rp['snapshot_sha256']==version and set(rp['completed_by_layer'].values())=={70}
receipt=runner.read(prod/'RECEIPT.json');ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
for f,h in ex['files'].items():assert sha(Path(receipt['export_directory'])/f)==h
v=dict(verdict='ACCEPT_BOUNDED_WITH_LIMITATIONS',reader='/root',comparator='/root',producer='/root/yevamot',snapshot_sha256=version,proposal_sha256=sha(prod/'PROPOSAL.json'),prior_verdict_sha256=sha(out.parent/'comparison/VERDICT.json'),resolved_findings=['K004-01'],source_first_core_findings_reconciled=20,new_core_coverage=0,coverage=rp['completed_by_layer'],next_ref=rp['next_unprocessed_by_layer']['claims'],checks=dict(rows=1,superseded=1,coverage_cells=len(p['coverage']),prior_records_preserved=True,exact_proposal_apply=True,replay_pass=True,export_files=len(ex['files'])),limitations=['Prior003context review overlap disclosed.','Positive branch remains an element of the proposed restriction, not a refuted actual valid-sale rule.','Bounded20-core acceptance with relevant continuation; no full-tractate delivery or ML eligibility.'],tractate_delivered=False,ml_eligible=False)
runner.immutable(out/'VERDICT.json',runner.encoded(v));runner.immutable(out/'REPLAY.json',runner.encoded(rp));runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={f.name:sha(f) for f in out.iterdir() if f.is_file() and f.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict=sha(out/'VERDICT.json'),manifest=sha(out/'MANIFEST.json'))))
