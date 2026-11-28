import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');P=OUT.parent.parent/'kiddushin/correction_002_20261127'
HEAD='d59c50b72b2ad028953c9cbec3254c13236f421f8894754b0ed2e4ed592c99fb';BASE='21a1e44469c765dae8c72260c2d90e0e9681b14284defe1d0a0e9ba841871126';PH='f5ca7f3f3fa2ce277ab5e2985bcf0576e7a4198ed82b4736f1552cd1bf94c313'
assert sha((P/'RECEIPT.json').read_bytes())=='4ba91f3b14992cbcd6394dd7283460da19f8229a5ca42a2b34734d14d29ae083'
receipt=read(P/'RECEIPT.json');assert sha((OUT.parent/'comparison/VERDICT.json').read_bytes())==receipt['review_sha256']
head=read(J/'snapshots'/f'{HEAD}.json');base=read(J/'snapshots'/f'{BASE}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(J/'proposals'/f'{PH}.json');assert len(p['records'])==25;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==18
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
assert not [(k,x) for k in active for x in strings(rows[k]['content']) if 'Rabbi Eliezer' in x]
assert {(c['segment_id'],c['layer']) for c in base['coverage']}=={(c['segment_id'],c['layer']) for c in head['coverage']}
report=runner.report(head,segs);assert report['completed_by_layer']=={k:30 for k in runner.LAYERS}
ep=Path(receipt['export_directory']);em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
for r in p['records']:
 if r['id'].startswith('kidfix002.final_scope.'):
  assert len({e['segment_id'] for e in r['evidence']})>=2
out={'verdict':'ACCEPT_BOUNDED_WITH_LIMITATIONS','snapshot_sha256':HEAD,'base_snapshot_sha256':BASE,'proposal_sha256':PH,'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'original_verdict_sha256':receipt['review_sha256'],'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':'Nonblind exact-version correction recheck; root original reader, separate comparator. No fresh/random cohort claim. Raw source and prior frozen comparison remain basis.','dispositions':[{'id':'K01','status':'resolved','evidence':'Printed ר״א preserved with explicit unresolved expansion in attribution, claim, position, utterance and dependent references. No active content asserts Rabbi Eliezer categorically.'},{'id':'K02','status':'resolved','evidence':'Earlier and final position statuses distinguish explanatory sufficiency; Rabbi Shimon is explicitly alternative-stage. Seven qualification edges anchor original and final source portions with narrow uncertainty text preserving substantive truths.'}],'new_records':25,'superseded_records':18,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':2376,'next_source':'Kiddushin 3b:4','open_tails':head['open_tails'],'integrity':{'full_exact_replay':True,'source_quotes_offsets':True,'export_files':True,'unrelated_records_unchanged':True,'coverage_keys_unchanged':True,'active_dependencies':True},'required_repairs':[],'limitations':['Printed ר״א disambiguation remains unresolved; no verified expanded identity claim.','Final-stage qualification is limited to explanatory sufficiency, not rejection of underlying quoted law or analogy.','Answer sets partial; no task qualification or representative recall claim.'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Coordinator may resume next source3b4; retain original rework verdict and immutable lineage. Full tractate remains incomplete.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
