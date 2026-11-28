import sys,json
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');P=OUT.parent.parent/'tamid/correction_007_20261127';HEAD='35bb1acb1f779ee16a8009686c416cc82473636665062f23710af1119073745e';PH='06d6853c04c1293186d8ac6b11cf1e26c61def73dd7c78a8fa011c1371bc954b'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='bda874755bb2ffdb5f6b653e470579b6d267356ef67c7cbec013a135daaebf70'
assert sha((P/'PROPOSAL.json').read_bytes())==PH;assert sha((P/'MANIFEST.json').read_bytes())=='3be6f4bbd916b608fbc5d5fa6338399c84662ba57c26c67faf315a92e3c0a4df'
for n,h in read(P/'MANIFEST.json')['files'].items():assert sha((P/n).read_bytes())==h
job,segs=runner.load(J);assert job['source_sha256']==prep['source_sha256']
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['ref']==f['ref'] and s['source_index']==f['source_index'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(P/'PROPOSAL.json');assert len(p['records'])==2;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==0
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
assert not [(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active]
report=runner.report(head,segs);assert report['completed_by_layer']=={k:110 for k in runner.LAYERS};assert head['open_tails']==[]
ep=Path('F:/Sefaria_QA/bavli_l03_exports_20261127/tamid_007_corrected');em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h

base=read(J/'snapshots/55ad0ef1292bac17b7d14cdd24337f609b6ebed5366aaa3420b0dbaeb1e072164507e.json') if False else read(J/'snapshots/55ad0ef1292bac17b7d14cdd24337f609b6ebed5366aaa3420b0dbaeb1ae7e77.json')
assert all(rows[r['id']]==r for r in base['records'])
q=rows['tam007fix.wood_q'];e=rows['tam007fix.wood_answer'];assert q['content']['question_origin']=='explicit' and q['content']['answer_set_status']=='partial'
assert e['content']['relation']=='answer' and e['content']['source_id']=='tam007.wood_repeat' and e['content']['target_id']==q['id']
for r in [q,e]:
 for ev in r['evidence']:
  seg=segs[ev['segment_id']];assert seg['ref']=='Tamid 29b:6' and seg['text'][ev['start_char']:ev['end_char']]==ev['quote']
assert len(p['coverage'])==3
prior=OUT.parent/'comparison/VERDICT.json';assert sha(prior.read_bytes())=='ccc03ec5f7896374302b44f8ccc851e96e7b0e17b3b2857687750624d6af20dc'
out={'verdict':'ACCEPT_BOUNDED_WITH_LIMITATIONS','snapshot_sha256':HEAD,'proposal_sha256':PH,'initial_verdict_sha256':sha(prior.read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':'Targeted nonblind independent correction verification against original raw source and frozen initial finding; no new cohort.','dispositions':[{'finding':'T007-01','status':'resolved','judgment':'Exact repeated29b6 question is represented independently from earlier occurrence, with source-explicit answer edge from unchanged wood_repeat; partial answer set preserved.'},{'finding':'T007-02','status':'retained_limitation','judgment':'Palm-fibre and internal-smoke lexical glosses remain unqualified; no contrary interpretation invented.'}],'checks':{'full_exact_replay':True,'source_evidence':True,'active_dependencies':True,'all_initial_records_unchanged':True,'export_files':True,'only_three_coverage_cells_updated':True},'new_records':2,'superseded_records':0,'completed_by_layer':report['completed_by_layer'],'required_repairs':[],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'resume':'Coordinator next-wave instructions; next30a5,97source segments remain per layer. Preserve lexical qualification limits and original REWORK history.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
