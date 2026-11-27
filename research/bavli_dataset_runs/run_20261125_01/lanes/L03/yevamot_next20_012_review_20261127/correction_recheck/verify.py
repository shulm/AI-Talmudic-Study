import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');P=OUT.parent.parent/'yevamot/bounded012_correction_20261127'
HEAD='f97f2db903e09ec2a461116ae999eae1133a6dc6dac7b47b0e773d93ef46120e';BASE='158c0ee79953dc4ebffc59a7c1b25f2bcc7660fa3eb8dc4b3d78980814ead124';PH='6a3ddeb9393a9a64b6afd53ef938157f297f4cbbe02b4c85511df9c49a38821a'
assert sha((P/'PROPOSAL.json').read_bytes())==PH
assert sha((P/'RECEIPT.json').read_bytes())=='1dee1d247125391101398c39eea07aaa81da1fe7ec313920483e14ca347aed6b'
assert sha((P/'MANIFEST.json').read_bytes())=='fe48a0da171617cb154d87c6f92ad733da1405c8b1d3aa2e2befc246d34569d9'
for n,h in read(P/'MANIFEST.json').items():assert sha((P/n).read_bytes())==h
assert sha((OUT.parent/'comparison/VERDICT.json').read_bytes())=='85900e7e2f4cde9dec6cc75891e99fb4e42b2d8320204dc2972c189a2bdada98'
prep=read(OUT.parent/'SOURCE_READING.json');job,segs=runner.load(J);runner.authorize(J,'L03/yevamot',2);assert job['source_sha256']==prep['source_sha256']
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['ref']==f['ref'] and s['source_index']==f['source_index'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
base=read(J/'snapshots'/f'{BASE}.json');p=read(P/'PROPOSAL.json');assert len(p['records'])==100
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'};revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==28
for r in base['records']:
 expected=dict(r)
 if r['id'] in revised:expected['release_state']='superseded'
 assert rows[r['id']]==expected
assert {(c['segment_id'],c['layer']) for c in head['coverage']}=={(c['segment_id'],c['layer']) for c in base['coverage']}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
assert not [(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active]
for c in head['coverage']:assert all(k in active for k in c['record_ids'])
required=['abaye_why','rebuke_why','mother_duplication','six_severe','others_marriage','cowives_permitted','list_mother','list_father_wife','list_father_sister','married_mother_hypothesis','duplicate_category','rape_mother','others_yes','brothers_no','judah_rape_prohibition','judah_identification','abaye_shimon','abaye_sages','ashi_disputed','yibbum_option','rl_brother_cowife','yh_brother_chalutzah','yh_brother_cowife','rl_brothers_prior','rl_cowife_prior']
assert all('yvfix012.'+k in active for k in required)
assert rows['yvfix012.married_mother_hypothesis']['content']['assertion_mode']=='rejected'
for k in ['abaye_why','rebuke_why','mother_duplication']:assert rows['yvfix012.'+k]['content']['answer_set_status']=='partial'
for k in ['abaye_answer','rebuke_answer','rape_answer']:assert rows['yvfix012.'+k]['content']['relation']=='answer'
assert rows['yvfix012.yev012.context.man_support']['content']['source_id']=='yvfix012.rl_brothers_prior'
assert rows['yvfix012.yev012.context.woman_support']['content']['source_id']=='yvfix012.rl_cowife_prior'
assert rows['yvfix012.cowife_other_prior_support']['content']['target_id']=='yvfix012.rl_brother_cowife'
receipt=read(P/'RECEIPT.json');ep=Path(receipt['export_directory']);em=read(ep/'manifest.json')
for n,h in receipt['export_files'].items():assert sha((ep/n).read_bytes())==h
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:238 for k in runner.LAYERS}
out={'verdict':'ACCEPT_BOUNDED','snapshot_sha256':HEAD,'base_snapshot_sha256':BASE,'proposal_sha256':PH,'initial_comparison_sha256':sha((OUT.parent/'comparison/VERDICT.json').read_bytes()),'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'producer_receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':'Nonblind exact-version targeted correction recheck against original source and frozen independent reading; prior011context exposure disclosed. No new cohort credit.','scope':prep['scope'],'dispositions':[{'id':'Y012-01','status':'resolved','evidence':'Three explicit question records and answer edges added; six-relatives and co-wife premise, three named categories, rejected duplicate mother hypothesis, rape-mother alternative, others/brothers inference and Yehudah identification present with source evidence. Original broad summary retained as historical context, with new atomic reasoning linked.'},{'id':'Y012-02','status':'resolved','evidence':'Shimon/sages feasibility, Ashi assertions, alternative procedural options, person/woman liability cells, and limiting scope versus prior status split immutably. Positions and dependent edges refreshed. Prior-status premises explicitly support corresponding karet conclusions; both co-wife party cells have source-supported links. Yohanan own-view/interlocutor qualification preserved.'}],'checks':{'exact_full_replay':True,'raw_source_and_original_indices':True,'proposal_and_manifest_hashes':True,'export_hashes':True,'unrelated_old_records_unchanged':True,'active_content_and_link_references':True,'coverage_keys_unchanged':True,'all_coverage_refs_active':True,'superseded_records_preserved':True},'proposal_rows':100,'superseded_records':28,'completed_by_layer':report['completed_by_layer'],'next_source':'Yevamot10b:6','open_tails':head['open_tails'],'remaining_per_layer':3631,'limits':['Only exact bounded correction accepted, not entire tractate.','Context10b6–12 remains uncounted;10b13–11a6 read but unproduced.','Eligibility and comparable answer-set qualification remain false.','Producer correction receipt retains independent_reading_seen:false from initial receipt. This recheck does not interpret that as blindness: correction was explicitly informed by frozen comparator findings.','Retained broad summaries alongside atomic expansions are not extra independent topic occurrences; downstream counting must respect lineage and evidence.'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'tractate_acceptance':False,'resume':'Production may resume under coordinator next-wave instructions at10b6, reusing context with precise original indices and source-first review. No blanket semantic production block imposed.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
