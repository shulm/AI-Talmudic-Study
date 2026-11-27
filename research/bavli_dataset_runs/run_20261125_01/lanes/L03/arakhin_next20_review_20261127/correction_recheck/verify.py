import json,hashlib,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
sha=lambda b:hashlib.sha256(b).hexdigest();read=lambda p:json.loads(p.read_text(encoding='utf-8'))
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');P=OUT.parent.parent/'arakhin/review_correction_20261127_002'
BASE='12a61d3b490ae865f3e631714c93578718741065a7767dece107bf23d5743b6e';HEAD='18bb932d660d694686e98f376d9aa8e2feeedb8e1e328affb1cd3ab0cee49cf5';PH='2b23018b71f036525d29568ea9e58ca0631f2b7c99a160786cfe2e7ce0abc9eb'
assert sha((P/'PROPOSAL.json').read_bytes())==PH
for h in [BASE,HEAD]:assert sha((J/'snapshots'/f'{h}.json').read_bytes())==h
base=read(J/'snapshots'/f'{BASE}.json');head=read(J/'snapshots'/f'{HEAD}.json');p=read(P/'PROPOSAL.json');job,segs=runner.load(J)
rebuilt=runner.validate_apply(base,p,segs,job);rebuilt['proposals']=base['proposals']+[PH];assert runner.encoded(rebuilt)==runner.encoded(head)
assert runner.report(base,segs)['completed_by_layer']==runner.report(head,segs)['completed_by_layer']=={k:30 for k in runner.LAYERS}
rows={r['id']:r for r in head['records']};active={i:r for i,r in rows.items() if r['release_state']=='valid'}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
 elif isinstance(v,list):
  for x in v:yield from strings(x)
assert not [(i,s) for i,r in active.items() for s in strings([r['content'],r['links']]) if s in rows and s not in active]
assert len(p['records'])==22 and sum(bool(r.get('supersedes')) for r in p['records'])==7
response=read(P/'RESPONSE.json');assert response['reader_verdict_sha256']==sha((OUT.parent/'VERDICT.json').read_bytes())
ep=Path(response['export_path'])
for n,h in read(ep/'manifest.json')['files'].items():assert sha((ep/n).read_bytes())==h
assert active['ar.e1.r002.initial.retracted']['content']['relation']=='retraction'
assert active['ar.e1.r002.initial.retracted']['content']['target_id']=='ar.e1.r002.initial'
assert active['ar.e1.r002.father']['content']['conditions']==active['ar.e1.r002.coowners']['content']['conditions']==['Shared verse for foreigner and other person']
out={'verdict':'ACCEPT_PARTIAL_WITH_EXCEPTIONS','verification_scope':'AR01/AR02 changed records and dependencies only; no new core review or coverage','base_snapshot_sha256':BASE,'snapshot_sha256':HEAD,'proposal_sha256':PH,'original_verdict_sha256':sha((OUT.parent/'VERDICT.json').read_bytes()),'response_sha256':sha((P/'RESPONSE.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'findings':[{'id':'AR01','disposition':'verified corrected','evidence':'2b1 father exclusion and co-owner inclusion now separately anchored to distinct source clauses, with inherited second-alternative conditions and separate support edges.'},{'id':'AR02','disposition':'verified corrected','evidence':'2b14 initial Beit Hillel alternating service,2b15 Beit Shammai objection,2b16 freeing/debt solution and explicit Beit Hillel retraction preserved; retraction edge targets original view and chronology receives source-backed support. No forced Ravina-stage assignment.'},{'id':'AR04','disposition':'retained task limitation','evidence':'No scholar-choice shared-question admission.'}],'checks':{'replay_exact':True,'coverage_unchanged_all8passes':30,'new_records':22,'superseded_records':7,'active_record_references_valid':True,'export_all_bytes':True},'caveats':['Added context is not counted as core production/review. Next source batch must reuse context claims and complete the remaining passes for2b14–16.','Paired procedural solution is retained as one contextual account; no fine-grained normative task eligibility.'],'reader_method':'Nonblind correction verification; no new random or fresh-reader cohort','qualification':{'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0},'tractate_acceptance':False,'next_source':'Arakhin2b:14','remaining_per_layer':1153}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict_sha256':m['VERDICT.json'],'manifest_sha256':sha((OUT/'MANIFEST.json').read_bytes())}))
