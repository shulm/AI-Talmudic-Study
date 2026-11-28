import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin');P=OUT.parent.parent/'eruvin/review_correction_next20_20261127'
HEAD='ac177ebe9b17c19442c59991bbe6b5f93c92eb7076aa7a5d80c6c2897f629fc4';BASE='35b7ebfcb7db5043158ff0c726dcc652b35c89703a6622f26fea2383c8faa007';PH='f86840786664c1780440fce16af4b8e1c89ed5e3f14689c17ae232df6a64123b'
assert sha((P/'MANIFEST.json').read_bytes())=='a123371618530f8c832224c36dfd3c398dd5cae163c4f3db9745c7100317a083'
assert sha((P/'PROPOSAL.json').read_bytes())==PH
assert sha((OUT.parent/'comparison/VERDICT.json').read_bytes())=='1d6b48f55cbaf0d6b4e3fd82f8458f17ea1a0a9e90dda04a4aa5dd063599823d'
head=read(J/'snapshots'/f'{HEAD}.json');base=read(J/'snapshots'/f'{BASE}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(P/'PROPOSAL.json');assert len(p['records'])==68;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==28
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
for r in base['records']:
 expected=dict(r)
 if r['id'] in revised:expected['release_state']='superseded'
 assert rows[r['id']]==expected
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
assert not [(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active]
assert {(c['segment_id'],c['layer']) for c in base['coverage']}=={(c['segment_id'],c['layer']) for c in head['coverage']}
report=runner.report(head,segs);assert report['completed_by_layer']=={k:130 for k in runner.LAYERS}
ep=J/'exports/review_correction_next20_20261127';em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
assert rows['er.fix20.explanation_q']['content']['question_origin']=='editorial_reconstruction'
for n in ['first_heker','first_partition','second_same','second_different','third_decree']:
 assert rows['er.fix20.'+n]['content']['target_id']=='er.fix20.explanation_q'
 assert rows['er.fix20.'+n+'.premise']['content']['relation']=='qualification'
out={'verdict':'ACCEPT_BOUNDED_WITH_LIMITATIONS','snapshot_sha256':HEAD,'base_snapshot_sha256':BASE,'proposal_sha256':PH,'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'response_sha256':sha((P/'RESPONSE.json').read_bytes()),'original_verdict_sha256':sha((OUT.parent/'comparison/VERDICT.json').read_bytes()),'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':'Nonblind exact-version correction recheck against previously frozen independent reading and original raw source. No fresh/random cohort claim. No production writes.','dispositions':[{'id':'ER01','status':'resolved','evidence':'Five explanation edges now target an expressly editorial explanatory question. Five premise qualification edges preserve alternatives without assigning anonymous mar sides. Partial answer set retained.'},{'id':'ER02','status':'resolved','evidence':'Hypothetical named alignments split; correction specifically targets Abaye rejection. Original and repeated projection classification/obligation split and quotation links updated. Seven/eight and Rav Ashi relative-width branches split with conditions. Earlier proof now targets alley classification rather than additional-lehi obligation.'},{'id':'ER03','status':'resolved','evidence':'6a9–10 anchors separate remnants/no-remnants claims; three qualification edges attach to earlier Ami/Asi rules. Rav Huna distinct from son of Rav Yehoshua; no new core coverage.'}],'new_records':68,'superseded_records':28,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':3516,'next_source':'Eruvin 5b:3','open_tails':head['open_tails'],'integrity':{'full_exact_replay':True,'original_source_offsets':True,'export_files':True,'unrelated_records_unchanged':True,'coverage_keys_unchanged':True,'active_dependencies':True},'limitations':['Four parallel qualification edge pairs are semantically duplicate retained/additional routes: eight_project/seven_first.revision, eight_repeat/seven_repeat.revision, ashi_project/ashi_first.revision, ashi_repeat/ashi_repeat.revision. They do not contradict source; downstream unique-relation counts must deduplicate endpoint/relation tuples.','Context-only findings remain uncounted. No full-tractate acceptance, shared answer-set certification or representative recall claim.'],'required_repairs':[],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Coordinator may resume next source5b3; retain original rework verdict and correction lineage. Whole-tractate remaining work unchanged.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
