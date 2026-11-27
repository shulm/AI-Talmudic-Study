import sys,json
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir');P=OUT.parent.parent/'nazir/bounded_005_20261127';HEAD='ac5716e058444e85f01c14acae5eb787dbdb41ec92f283a9eb999d42856782b7';PH='478781da968a05a0e58dcc7483ee39567fc9fbc4b981ee38809a15b3a998ae25'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='229b4e29868739875b50717b618ebe50dffdbc9d5b72feacaf491932c8766a0d'
assert sha((P/'INITIAL_PROPOSAL.json').read_bytes())==PH
assert sha((P/'RECEIPT.json').read_bytes())=='3ea8b9f5b1b16fdd7f77e4a60ec071ac69cd1f3540d627da006b8102b78cef43'
assert sha((P/'MANIFEST.json').read_bytes())=='477c9465cd59b38314cff82db66ffc88d0c5770cdaa9eca256a81e6e7f76d2bd'
for n,h in read(P/'MANIFEST.json').items():assert sha((P/n).read_bytes())==h
receipt=read(P/'RECEIPT.json');job,segs=runner.load(J);assert job['source_sha256']==prep['source_sha256'];runner.authorize(J,'/root/lead_l01_l03',1)
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['ref']==f['ref'] and s['source_index']==f['source_index'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
p=read(P/'INITIAL_PROPOSAL.json');assert len(p['records'])==180;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==1
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'};base=read(J/'snapshots'/(receipt['parent_snapshot']+'.json'))
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
report=runner.report(head,segs);assert report['completed_by_layer']=={k:90 for k in runner.LAYERS}
ep=J/'exports/bounded_005_20261127';em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h

names=['naz004.context.yehuda_yaakov','naz004.context.shimon_yosi','naz004.context.all_vow','naz004.context.firstborn_special','naz004.context.yosi_sin naz004.context.yosi_guilt','naz004.context.selection','naz004.context.offerings_vow naz004.context.firstborn_not_vow','naz004.context.yaakov_vow','naz004.context.firstborn_duty naz005.firstborn_dedication_source','naz004.context.firstborn_automatic naz005.firstborn_auto_q','naz005.nazir_lahashem','naz005.shimon_policy naz005.southerner_exception','naz005.southerner_appearance','naz005.shimon_hair_question','naz005.shepherd_role naz005.spring_reflection','naz005.pride_danger','naz005.self_rebuke','naz005.heaven_shaving_vow','naz005.shimon_kiss','naz005.shimon_blessing naz005.shimon_verse naz005.narrative_verse_use','naz004.context.samson_verse','naz004.context.angel_speech','naz004.context.impurity_proof','naz005.jawbone_quote naz004.context.no_touch_possibility','naz005.garments_quote','naz004.context.clothes_before naz004.context.verse_order','naz004.context.dying_possibility','naz004.context.impurity_tradition','naz005.lifelong_source','naz005.absalom_lifelong naz005.absalom_vowverse','naz005.rabbi_annual naz005.days_verse','naz005.house_year','naz005.nehorai_thirty','naz005.yosi_weekly naz005.princes_weekly','naz005.rabbi_reason naz005.days_minimum naz005.two_days_objection','naz005.weight_tradition naz005.two_days_no_weight','naz005.two_years','naz005.no_years_filter naz005.years_example_excluded','naz005.context.thirty_days naz005.context.no_months_filter','naz005.context.yamim_yamimah naz005.context.same_form','naz005.context.forms_objection naz005.context.return_arrive naz005.context.yishmael','naz005.context.no_match naz005.context.match_preferred','naz005.context.interval_distribution','naz005.context.priest_weight','naz005.context.weekly_difference','naz005.context.brothers_festival naz005.context.absalom_no_festival naz005.context.brothers_morning naz005.context.absalom_evening','naz005.context.forty_years naz005.context.forty_since_request naz005.context.samuel_tenth']
assert len(names)==len(prep['findings'])==47
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=ns.split();assert all(k in active for k in ids),(f['id'],ids)
 mapping.append({'reader_id':f['id'],'scope':f['scope'],'producer_ids':ids,'disposition':'represented'})
out={'verdict':'ACCEPT_BOUNDED_WITH_LIMITATIONS','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':prep['exposure']+' Exact comparison after initial freeze.','scope':prep['scope'],'mapping':mapping,'source_findings':{'core':38,'core_represented':38,'context':9,'context_represented':9},'required_repairs':[],'checks':{'exact_full_replay':True,'source_offsets_indices':True,'export_files':True,'prior_records_preserved':True,'active_dependencies':True,'primary_partitions':True},'semantic_checks':['Rejected Yehudah/Yaakov and Shimon/Yose mappings preserved; common vow requirement does not erase actual firstborn disagreement.','Shimon the Righteous and quoted youth separate; youth self-address and heavenly shaving purpose preserved without narrator diagnosis or universal offering prohibition.','Samson verse-proof attempts remain qualified by no-touch, prior stripping and dying alternatives; final source is received tradition.','Rabbi annual, Nehorai thirty-day and Yose weekly positions stay separate; matching-word filters retain conditions and exclusions.','Context alternatives and Nehorai reporting Yehoshua remain distinct; no named assignment inferred from order.'],'completed_by_layer':report['completed_by_layer'],'proposal_rows':180,'superseded_records':1,'open_tails':head['open_tails'],'limits':['Only20 core segments accepted; nine context findings are not future coverage certification.','Reported narrative and chronology are not independently historically verified.','Ambiguous alternative distribution at5a10 not forced into a resolved calendar.','Prior context exposure disclosed; zero fresh blind/random cohort credit.','Shared schema question answer sets and model qualification remain provisional.'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'tractate_acceptance':False,'resume':'Next5a6 original[8,5]; reuse context90–98 immutably;1209 segments remain per layer.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))

