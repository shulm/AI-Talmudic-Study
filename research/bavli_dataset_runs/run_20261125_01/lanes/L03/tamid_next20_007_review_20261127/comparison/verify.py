import sys,json
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');P=OUT.parent.parent/'tamid/bounded_007_20261127';HEAD='55ad0ef1292bac17b7d14cdd24337f609b6ebed5366aaa3420b0dbaeb1ae7e77';PH='3e8b03a3c40040756690c282d9ad6fcf2e6cd171f963ed7eb89255e38ee38846'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='bda874755bb2ffdb5f6b653e470579b6d267356ef67c7cbec013a135daaebf70'
assert sha((P/'PROPOSAL.json').read_bytes())==PH;assert sha((P/'MANIFEST.json').read_bytes())=='61e19df8b9d0f742cddfe7486f2423a88f17f94f53d9ec72e6eb1e072164507e'
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
p=read(P/'PROPOSAL.json');assert len(p['records'])==145;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==5
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
assert not [(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active]
report=runner.report(head,segs);assert report['completed_by_layer']=={k:110 for k in runner.LAYERS};assert head['open_tails']==[]
ep=Path('F:/Sefaria_QA/bavli_l03_exports_20261127/tamid_007');em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
names=['tam007.heaven_q tam006.heaven_hyper','tam006.rava_mound tam006.rava_cup','tam006.earth_verse tam007.prophetic_hyper','tam006.shmuel_chain','tam006.shmuel_three','tam006.shmuel_cup tam006.cup_dispute','tam006.no_poverty tam006.wealth_cup','tam006.rava_mound','tam007.vine_gold tam007.vine_trellis','tam007.donate_leaf','tam007.donate_grape tam007.donate_cluster','tam006.vine_case tam006.elazar.a','tam006.curtain_chain','tam007.curtain_thick','tam007.curtain_strands tam007.curtain_threads','tam007.curtain_length tam007.curtain_width','tam007.curtain_amount','tam007.curtain_year','tam006.curtain_case tam006.curtain_hyper','tam006.wood_why tam006.wood_knots tam006.wood_settlement','tam007.wood_verse tam007.skewer_wood','tam007.wood_repeat','tam007.fig_repeat tam007.nut_repeat tam007.oil_repeat','tam007.eliezer_maish tam007.eliezer_oak tam007.eliezer_palm tam007.eliezer_carob tam007.eliezer_sycamore','tam007.external_knots_restrict','tam007.external_knots_permit','tam007.palm_q','tam007.fig_q tam007.fruitless_fig','tam007.fruitless_palm tam007.palm_qualifies','tam007.fruitless_exists tam007.fruitless_exists_yes','tam007.white_fig tam007.rahava.a','tam007.rope tam007.bury','tam007.timber tam007.no_fruit','tam007.camel','tam006.orientation_q tam006.wind tam006.lighting','tam007.orientation_unassigned','tam006.gap_objection','tam006.multiple_places tam006.places_resolution','']
assert len(names)==39
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=ns.split();assert all(k in active for k in ids),(f['id'],ids)
 if not ids:ids=[k for k in active if rows[k]['layer'] in ['structure','utterances'] and any(e['segment_id']==f['evidence'][0]['segment_id'] for e in rows[k]['evidence'])];assert ids
 mapping.append({'reader_id':f['id'],'scope':'core','producer_ids':ids,'disposition':'represented_with_lexical_limits'})
sid=next(s['id'] for s in segs.values() if s['ref']=='Tamid 29b:6');question_rows=[k for k in active if rows[k]['layer']=='questions' and any(e['segment_id']==sid for e in rows[k]['evidence'])];assert not question_rows
out={'verdict':'REWORK_TARGETED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':prep['exposure']+' Source reading preceded new007 labels; exact comparison now nonblind.','scope':prep['scope'],'mapping':mapping,'source_findings':{'frozen_core':39,'additional_comparison_findings':1},'required_repairs':['T007-01'],'findings':[{'id':'T007-01','severity':'localized_question_omission','ref':'Tamid29b:6','source_quote':'וכי כל העצים כשרים למערכה הן כל העצים כשרים חוץ מן זית וגפן','records':['tam007.wood_repeat'],'judgment':'The baraita’s explicit question whether all woods are suitable has no question-layer record, although its answer is preserved as wood_repeat. Raw evidence and narrative description do not complete the question pass.','required_action':'Add a narrow explicit question record for the quoted baraita and an answer link from the existing condition-bound wood_repeat claim. Refresh only affected coverage; no new cores, no forced confirmed answer set.'},{'id':'T007-02','severity':'unresolved_lexical_limit','records':['tam007.rope','tam007.skewer_wood'],'judgment':'The exact rope term חבלא דצבתא and clause דלא קטרי ואזלי מקטר מתוכו are preserved in evidence. This comparator has not independently pinned the categorical palm-fibre gloss or precise smoke/burning syntax. No demonstrated contrary reading is asserted; exclude these lexical glosses from qualified gold claims until checked or explicitly qualified. No speculative semantic repair demanded.'},{'id':'T007-03','severity':'none','judgment':'Rava versus Shmuel golden-cup distinction and three hyperbole examples retained. Yannai→Shmuel and RSBG→deputy chains correct. Donation alternatives, curtain dimensions, unspecified82myriad, five added species, internal/external knot options, fig/palm fruitless scopes and Rahava result separated. Huna/Hisda names remain unassigned. Heading preserved with no fabricated legal claims.'}],'checks':{'exact_full_replay':True,'source_offsets_indices':True,'export_files':True,'active_dependencies':True,'primary_partition_validation':True,'heading_retained':True},'proposal_rows':145,'superseded_records':5,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':97,'next_source':'Tamid30a:5','open_tails':[],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'resume':'Producer adds minimal question/answer with coverage refresh, preserves initial proposal and evidence. Independently recheck exact correction. Lexical limitations remain explicit; no whole-tractate acceptance.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
