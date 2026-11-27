import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');P=OUT.parent.parent/'yevamot/bounded011_correction_20261127'
HEAD='2a6cbf49cca3c418dcdf5ae8299d5ed2ffdbddc626cbffdbbd456f73ae83d058';BASE='56f41af1f27aca3e247b91801831b865ce44e832a2dd06a2a56a04e9dcc452a9';PH='e017bf68a9e45c4f0f0885836a12e230a78c59f9dac135645e06290e85bebb84'
assert sha((P/'RECEIPT.json').read_bytes())=='fc8a6b300f43a78287c9f5e295fc2d2d8fb79415f4c49cb5a3de7d892b99b294'
receipt=read(P/'RECEIPT.json');assert sha((OUT.parent/'comparison/VERDICT.json').read_bytes())==receipt['review_sha256']
head=read(J/'snapshots'/f'{HEAD}.json');base=read(J/'snapshots'/f'{BASE}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(J/'proposals'/f'{PH}.json');revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==12
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
report=runner.report(head,segs);assert report['completed_by_layer']=={k:218 for k in runner.LAYERS}
ep=Path(receipt['export_directory']);em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
triples={(rows[k]['content']['source_id'],rows[k]['content']['target_id'],rows[k]['content']['relation']) for k in active if rows[k]['layer']=='edges'}
for a in ['yev011.rav_yehuda_scope','yev011.first_six_excluded']:
 for b in ['yev011.forbidden_one','yev011.forbidden_other','yvfix011.sister_yibbum','yvfix011.sister_yibbum_option']:assert (a,b,'qualification') in triples
for n in ['sister_yibbum','sister_yibbum_option']:assert 'Alternative permitted procedure' in rows['yvfix011.'+n]['content']['conditions'][0]
out={'verdict':'ACCEPT_BOUNDED_WITH_LIMITATIONS','snapshot_sha256':HEAD,'base_snapshot_sha256':BASE,'proposal_sha256':PH,'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'original_verdict_sha256':receipt['review_sha256'],'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':'Nonblind exact-version correction recheck against own previously frozen source reading; no fresh/random cohort claim. No Yevamot production authorship.','dispositions':[{'id':'Y011-01','status':'resolved','evidence':'Halitzah/yibbum separated as alternative permitted procedures. Two-sisters and two-unrelated examples each have positive and negative configuration atoms with correct conditions. Levi marriage-to-father non-exemption and father-rape exemption separated at original10a12/10b1 occurrences. Original composites preserved superseded, split lineage in receipt; support/outcome dependencies refreshed.'},{'id':'Y011-02','status':'resolved','evidence':'Both Rav Yehuda scope constraints now qualify all four reciprocal/procedural atoms, including second reciprocal case and split option. Abaye and Rav Safra alternatives unchanged; no universal final restriction imposed.'}],'new_records':len(p['records']),'superseded_records':12,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':3651,'next_source':'Yevamot9b:9','open_tails':head['open_tails'],'integrity':{'full_exact_replay':True,'source_quotes_offsets':True,'export_files':True,'unrelated_records_unchanged':True,'coverage_keys_unchanged':True,'active_dependencies':True,'all_branch_scope_targets':True},'required_repairs':[],'limitations':['Source-only context remains uncounted; open sixteenth-case discussion requires future core passes.','No common-answer-set certification, representative recall claim or full-tractate acceptance.'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Hold all writes for coordinator checkpoint capture. After capture and coordinator instruction resume9b9, reusing existing context atoms and immutable structure/dependency updates.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes()),'new_records':len(p['records'])}))
