import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');P=OUT.parent.parent/'tamid/correction_005_20261127'
HEAD='9d86f86ca80df56db0f7e799eda50f111fd69562b2e7c73bd29e1bbf3704c6fe';BASE='6c126f20c894521d8cb07372422bef1daa376824ac464dfb9511a98252f60e25';PH='8bc55c9a2fc64017fb316342ba13c05b93445ccd265b15cf64df37143f29e1c9'
assert sha((P/'MANIFEST.json').read_bytes())=='c4643bf2b0067b303f1754e75f261c40cb5b7ab4917aa7a7c0e647a6bd8e5ea0'
assert sha((P/'PROPOSAL.json').read_bytes())==PH
head=read(J/'snapshots'/f'{HEAD}.json');base=read(J/'snapshots'/f'{BASE}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(P/'PROPOSAL.json');assert len(p['records'])==2;revised={r['supersedes'] for r in p['records']};assert revised=={'tam005.rav_son','tam005.huna_son'}
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
for r in base['records']:
 expected=dict(r)
 if r['id'] in revised:expected['release_state']='superseded'
 assert rows[r['id']]==expected
for r in p['records']:
 c=r['content'];assert c['role']=='speaker' and len(c['candidates'])==1 and not c['transmission_chain'] and 'addressee' in c['scope']
assert {(c['segment_id'],c['layer']) for c in base['coverage']}=={(c['segment_id'],c['layer']) for c in head['coverage']}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
assert not [(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active]
report=runner.report(head,segs);assert report['completed_by_layer']=={k:70 for k in runner.LAYERS}
ep=J/'exports/correction_005_20261127';em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
out={'verdict':'ACCEPT_BOUNDED_WITH_LIMITATIONS','snapshot_sha256':HEAD,'base_snapshot_sha256':BASE,'proposal_sha256':PH,'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'original_verdict_sha256':sha((OUT.parent/'comparison/VERDICT.json').read_bytes()),'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':'Nonblind exact-version correction recheck of separately frozen /root/yevamot reading; no fresh/random cohort.','dispositions':[{'id':'T005-01','status':'resolved','evidence':'Both fathers now sole speaker candidates; sons identified as addressees in scope; unsupported chains cleared. Parallel direct-speech occurrences remain separate. Two old records retained superseded; two coverage cells refreshed.'}],'new_records':2,'superseded_records':2,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':137,'next_source':'Tamid28a:12','open_tails':head['open_tails'],'integrity':{'full_exact_replay':True,'source_quotes_offsets':True,'export_files':True,'unrelated_records_unchanged':True,'coverage_keys_unchanged':True,'active_dependencies':True},'required_repairs':[],'limitations':['Original comparison narrative/source-assertion and unresolved historical-identity limits remain.','Open inspection Mishnah requires continuation; no full-tractate acceptance or task eligibility.'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Coordinator may resume next28a12; preserve original comparison and immutable correction lineage.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
