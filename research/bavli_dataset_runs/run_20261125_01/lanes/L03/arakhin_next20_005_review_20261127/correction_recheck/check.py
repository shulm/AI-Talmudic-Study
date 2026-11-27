import copy,json,sys
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;lane=out.parents[1];prod=lane/'arakhin/correction_005_20261127';job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');sha=lambda p:runner.sha(p.read_bytes())
version='8e39282c0eb048b6ae558af38ab8cd0b638f2411015a153d36495873ae9371ce';state=runner.read(job/'snapshots'/f'{version}.json');assert runner.sha(runner.encoded(state))==version
base=runner.read(job/'snapshots/323eb4bd621eff893cfd37c67016897d4a4af087b547a7e497b8858a60cab768.json');p=runner.read(prod/'PROPOSAL.json');assert sha(prod/'PROPOSAL.json')=='538164798da90a0b314e5294d14a938a3a2b3d6628845c44b6b4b7e1bee00706';j,src=runner.load(job)
applied=runner.validate_apply(base,p,src,j);applied['proposals']=base['proposals']+[sha(prod/'PROPOSAL.json')];assert runner.encoded(applied)==runner.encoded(state)
revised={r['supersedes'] for r in p['records'] if r.get('supersedes')};now={r['id']:r for r in state['records']};assert len(p['records'])==6 and len(revised)==2
for r in base['records']:
 expected=copy.deepcopy(r)
 if r['id'] in revised:expected['release_state']='superseded'
 assert now[r['id']]==expected
assert {(c['segment_id'],c['layer']) for c in state['coverage']}=={(c['segment_id'],c['layer']) for c in base['coverage']}
q=now['ar.e1.b005fix.eating_q'];assert q['layer']=='questions' and q['content']['question_origin']=='explicit' and 'not endorsed' in q['content']['conditions'][0]
for k in ['omer','two_loaves','showbread']:
 e=now['ar.e1.b005fix.offering_support_'+k]['content'];assert e['source_id']=='ar.e1.b005.priest_offering' and e['target_id']=='ar.e1.b005.ownership_'+k and e['relation']=='support'
a=now['ar.e1.b005fix.bukhri_testimony'];assert a['content']['transmission_chain'][0]=='א"ר יהודה' and a['uncertainty']
rp=runner.replay(job);assert rp['snapshot_sha256']==version and set(rp['completed_by_layer'].values())=={90}
r=runner.read(prod/'RECEIPT.json');ex=runner.read(prod/'EXPORT.json');assert ex['snapshot_sha256']==version
for f,h in ex['files'].items():assert sha(Path(r['export_path'])/f)==h
v=dict(verdict='ACCEPT_BOUNDED_WITH_LIMITATIONS',reader='/root',comparator='/root',producer='/root/blind_review',snapshot_sha256=version,proposal_sha256=sha(prod/'PROPOSAL.json'),prior_verdict_sha256=sha(out.parent/'comparison/VERDICT.json'),resolved_findings=['AR005-01','AR005-02'],source_first_core_findings_reconciled=25,new_core_coverage=0,coverage=rp['completed_by_layer'],next_ref=rp['next_unprocessed_by_layer']['claims'],checks=dict(rows=6,superseded=2,coverage_cells=len(p['coverage']),all_prior_records_preserved=True,exact_proposal_apply=True,replay_pass=True,export_files=len(ex['files'])),limitations=['Previous source/review exposure remains disclosed.','א"ר יהודה title remains unexpanded; reader earlier expansion is qualified too.','Bounded20-core acceptance only, with relevant continuation; no full-tractate delivery or ML eligibility.'],tractate_delivered=False,ml_eligible=False)
runner.immutable(out/'VERDICT.json',runner.encoded(v));runner.immutable(out/'REPLAY.json',runner.encoded(rp));runner.immutable(out/'MANIFEST.json',runner.encoded(dict(files={f.name:sha(f) for f in out.iterdir() if f.is_file() and f.name!='MANIFEST.json'})))
print(json.dumps(dict(verdict=sha(out/'VERDICT.json'),manifest=sha(out/'MANIFEST.json'))))
