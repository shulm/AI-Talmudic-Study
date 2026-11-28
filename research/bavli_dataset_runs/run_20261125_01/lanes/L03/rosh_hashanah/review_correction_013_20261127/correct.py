import json,sys,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah')
BASE='3837f096c33950a008a08ac518e704fd68e5dd192cbccfb46bea1d037cde062a'
F=OUT.parent.parent/'rh_next20_source_review_20261127/comparison/FINDING_DIRECTION.json'
assert runner.sha(F.read_bytes())=='1ebec75dcae11cc2ab183ff8352657b2e411a230065b692124ceb4299163e03f'
runner.immutable(OUT/'FINDING_DIRECTION.json',F.read_bytes())
job,segs=runner.load(J);runner.authorize(J,'L03/rosh_hashanah',3);state=runner.current(J)
assert runner.sha(runner.encoded(state))==BASE
rows={r['id']:r for r in state['records']};old='rh.e3.b013.e7';new='rh.e3.b013.fix1.e7'
r=copy.deepcopy(rows[old]);r['id']=new;r['supersedes']=old
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r['content']['source_id']='rh.e3.b013.from_start';r['content']['target_id']='rh.e3.b013.no_service'
r['links']=[r['content']['source_id'],r['content']['target_id']]
r['evidence']=copy.deepcopy(rows['rh.e3.b013.from_start']['evidence'])+r['evidence']
assert not [x['id'] for x in state['records'] if x['release_state']=='valid' and old in x.get('links',[])]
coverage=[]
for c in state['coverage']:
 if old in c['record_ids']:
  c=copy.deepcopy(c);c.pop('proposal_execution',None);c['record_ids']=[new if x==old else x for x in c['record_ids']];c['rationale']+=' Independent review correction: year-start sanctity supports interim non-service, following מכאן אמר; original evidence and source coverage retained.';coverage.append(c)
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[r],coverage=coverage,open_tails=state['open_tails'])
runner.validate_apply(state,p,segs,job)
runner.immutable(OUT/'PROPOSAL.json',runner.encoded(p));ph=runner.sha((OUT/'PROPOSAL.json').read_bytes())
promotion=runner.submit(J,OUT/'PROPOSAL.json','L03/rosh_hashanah',3);runner.immutable(OUT/'PROMOTION.json',runner.encoded(promotion))
replay=runner.replay(J);assert replay['completed_by_layer']=={k:222 for k in runner.LAYERS};runner.immutable(OUT/'REPLAY.json',runner.encoded(replay))
ep=J/'exports/review_correction_013_20261127';ex=runner.export(J,ep);runner.immutable(OUT/'EXPORT.json',runner.encoded(ex))
receipt={'status':'TARGETED_CORRECTION_PENDING_INDEPENDENT_RECHECK','base_snapshot_sha256':BASE,'snapshot_sha256':replay['snapshot_sha256'],'proposal_sha256':ph,'finding_sha256':runner.sha(F.read_bytes()),'source_sha256':job['source_sha256'],'schema_sha256':job['schema_sha256'],'protocol_sha256':job['protocol_sha256'],'contract_sha256':'6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174','owner':{'owner':'L03/rosh_hashanah','epoch':3},'new_records':1,'superseded_records':1,'changed_coverage_cells':len(coverage),'new_core_segments':0,'completed_by_layer':replay['completed_by_layer'],'remaining_per_layer':803,'next_ref':'Rosh Hashanah 9b:6','source_index':[17,5],'open_tails':state['open_tails'],'disposition':'Reverse e7 support: year-start Jubilee sanctity in8b9 grounds no-service interim rule introduced מכאן אמר8b10. Both evidence portions retained. No dependent record references found; all dependent coverage refreshed. Original edge and initial proposal preserved.','replay_pass':True,'export_path':str(ep),'export_manifest_sha256':runner.sha((ep/'manifest.json').read_bytes()),'independent_acceptance':False,'tractate_delivered':False,'ml_eligible':False,'all_demanding_tasks':False}
runner.immutable(OUT/'RESPONSE.json',runner.encoded(receipt))
runner.immutable(OUT/'RESUME.md',('Snapshot '+receipt['snapshot_sha256']+'; proposal '+ph+'.\n\n222/1025 per pass unchanged;803 remain. Next Rosh Hashanah9b:6 index[17,5]; open rh.e3.b013.s4. Reuse existing context records9b6–10. Producer resumes only under next coordinator wave; correction independent acceptance pending. Replay exact current head before production. Do not rerun correct.py against advanced CURRENT. No commits or shared edits.\n').encode())
m={p.name:runner.sha(p.read_bytes()) for p in OUT.iterdir() if p.is_file() and p.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m))
print(json.dumps({'snapshot':receipt['snapshot_sha256'],'proposal':ph,'response':m['RESPONSE.json'],'manifest':runner.sha((OUT/'MANIFEST.json').read_bytes()),'coverage_cells':len(coverage)}))
