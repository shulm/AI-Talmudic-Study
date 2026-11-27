import json,sys,hashlib
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');P=OUT.parent.parent/'kiddushin/bounded_002_20261127'
HEAD='21a1e44469c765dae8c72260c2d90e0e9681b14284defe1d0a0e9ba841871126';PH='39d120abd631d59f0f17a365b7827eafa5e291640da4540d4a7e0a6465730909'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='a567d19504a22d528b0d594eeb9706642ef2d20b1f0aefbf712971f0cf3bec51'
receipt=read(P/'RECEIPT.json');assert receipt['snapshot_sha256']==HEAD and receipt['proposal_sha256']==PH
assert sha((P/'INITIAL_PROPOSAL.json').read_bytes())==PH
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);assert job['source_sha256']==prep['source_sha256']
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['source_index']==f['source_index'] and s['ref']==f['ref'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 old=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=old+[h]
assert runner.encoded(s)==runner.encoded(head)
ep=Path(receipt['export_directory']);em=read(ep/'manifest.json');assert sha((ep/'manifest.json').read_bytes())==receipt['export_manifest_sha256']
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:30 for k in runner.LAYERS}
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
stale=[(k,x) for k in active for x in strings([rows[k]['content'],rows[k].get('links',[])]) if x in rows and x not in active];assert not stale
names=['three_gender','feminine_way','seven_gender zav_seven','masculine_way','verse_contradiction teaching_contradiction','torah_gender','war_gender','woman_gender','zav_gender','woman_involuntary','why_ways','intercourse_way','money_deed','money_deed_wording','two_for_one','means_intercourse','alternative_ways','shimon_verse','man_seeks woman_not_seeks','lost_object lost_object_question seeking_analogy','zav_ways','excess_food','excess_drink','etrog_ways etrog_tree_three','etrog_veg_one etrog_ending_wording','etrog_ending_question','veg_water','veg_tithe','etrog_water etrog_tithe','growth_way_answer picking_way_answer','koy.wild koy.domestic koy.both koy.neither','koy_ways','documents_ways documents_shared','ways_criterion things_criterion','eliezer_tree eliezer','ways_criterion criterion_answer.overall','first_count last_count','exclude_chuppah','huna_chuppah','huna_exclusion huna_branch','exclude_chalipin','field_chalipin woman_chalipin_hyp field_hypothesis','chalipin_exclusion','why_not_exchange','chalipin_small','woman_minimum','woman_minimum','woman_minimum','exclude_chalitzah release_count_again','yevamah_no_get yevamah_chalitzah wife_get wife_chalitzah_hyp','release_inference_excluded','why_not_chalitzah','book_severs','book_severs']
assert len(names)==54
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=['kid002.'+x for x in ns.split()];assert all(x in rows for x in ids)
 mapping.append({'reader_id':f['id'],'producer_ids':ids,'disposition':'partial: final replacement relation missing' if f['id'].endswith('036') else 'represented; attribution caveat K01 applies' if f['id'].endswith('035') else 'represented'})
findings=[
 {'id':'K01','severity':'medium','category':'unqualified_identity_expansion','refs':['Kiddushin 3a:3'],'reader_ids':['kid_next20_035'],'records':['kid002.eliezer','kid002.eliezer_tree','kid002.eliezer_tree.p','kid002.etrog_tithe','kid002.etrog_tithe.p'],'judgment':'Pinned text prints ר״א. Producer expands this categorically as Rabbi Eliezer with no uncertainty or supporting witness, describing expansion as local-context fact. This review does not assert that expansion is historically wrong; it is not established by the supplied exact-source evidence.','required_action':'Preserve printed ר״א in the canonical assertion and attribution, marking any proposed expansion as unresolved/editorial, or supply separately pinned authoritative disambiguation provenance. Refresh all dependent semantic/coverage references and occurrences of the expanded name, preserving original records.'},
 {'id':'K02','severity':'medium','category':'missing_argument_revision_scope','refs':['Kiddushin 2b:10–3a:3'],'reader_ids':['kid_next20_017','kid_next20_030','kid_next20_034','kid_next20_036'],'records':['kid002.intercourse_answer','kid002.alternative_ways','kid002.etrog_ending_wording','kid002.ways_criterion','kid002.things_criterion','kid002.criterion_answer.overall'],'judgment':'The final אלא criterion is recorded as an additional answer to why_ways but no correction/qualification relation connects it to the provisional local wording explanations. Generic asserted-locally statuses do not encode which earlier explanation is replaced as a general account. Likewise the Rabbi Shimon branch is an answer edge without structured alternative-stage qualification. Earlier cited substantive teachings must not be treated as rejected legal facts.','required_action':'Add narrow source-backed relations/status qualification identifying the final general wording explanation and superseded explanatory sufficiency of earlier accounts, with evidence at both stages. Preserve Rabbi Shimon as an alternative explanation at its source stage. Do not mark the vegetable/etrog substantive analogy, gender reconciliations or cultural analogy itself false merely because the general wording account changes.'},
 {'id':'K03','severity':'none','category':'supported_atomicity_and_scope','judgment':'Etrog growth and tithe are split; four koy relations split; male/female seeking clauses split; yevamah/get/chalitzah and wife/get premises split from rejected inference. Crossfolio3a7–3b1 evidence preserved. Chuppah exclusion remains initial with Rav Huna branch; halipin minimum-value rationale stays local. Book-severs claim explicitly scopes divorce instrument so does not deny husband-death release. No false named dispute from פלוגתא.'},
 {'id':'K04','severity':'task_limitation','judgment':'Question answer sets remain partial; no scholar-choice/common-set certification. Several explanatory causal propositions retain their explicit reason in prose; this review does not require mechanical splitting of every linguistic clause. No claims about full-tractate completion or representative recall.'}
]
out={'verdict':'REWORK_TARGETED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'source_sha256':job['source_sha256'],'schema_sha256':job['schema_sha256'],'protocol_sha256':job['protocol_sha256'],'source_reader':'/root','comparator':'/root/rosh_hashanah','method':'Comparator has never produced Kiddushin, previously compared opening10 labels. Read existing frozen root reading plus raw2b6–4a6 source before new labels. Distinct reader/comparator; no fresh blind or random cohort credit. Frozen reading provenance retained.','scope':{'first':'Kiddushin 2b:6','last':'Kiddushin 3b:3','original_indices':[[3,5],[5,2]],'core_segments':20,'context_through':'Kiddushin 4a:6','context_coverage':0},'findings_count':54,'fully_represented_findings':53,'partially_represented_findings':1,'mapping':mapping,'findings':findings,'required_repairs':['K01','K02'],'integrity':{'exact_replay':True,'source_quote_offsets_indices':True,'export_hashes':True,'active_dependencies':True},'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':2376,'next_source':'Kiddushin 3b:4','open_tails':[],'eligibility':{'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'random_cohort_credit':0,'fresh_blind_cohort_credit':0},'tractate_acceptance':False,'resume':'Producer alone repairs immutably with dependent coverage refresh and no added cores. Preserve initial bytes and this comparison; independent recheck exact corrected head.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}))
m={p.name:sha(p.read_bytes()) for p in OUT.iterdir() if p.is_file() and p.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
