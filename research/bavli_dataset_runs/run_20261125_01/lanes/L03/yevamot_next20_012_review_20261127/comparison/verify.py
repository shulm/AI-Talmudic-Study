import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');P=OUT.parent.parent/'yevamot/bounded012_20261127'
HEAD='158c0ee79953dc4ebffc59a7c1b25f2bcc7660fa3eb8dc4b3d78980814ead124';PH='a3462a2f0b81f036b3c2774cde829da1ca9cb7be86e9d466a69ac983c2d5a258'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='6730f3bcf4a37851913b03d3ee72da21da3210a215fb2be500f8df5b4e842e6e'
receipt=read(P/'RECEIPT.json');assert sha((P/'RECEIPT.json').read_bytes())=='74fcc8bb2b73289f301c57eabab31da4dda76f94771afc93b5370838de4c80b6'
assert sha((P/'VALIDATION_REVISED_PROPOSAL.json').read_bytes())==PH
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);assert job['source_sha256']==prep['source_sha256'];runner.authorize(J,'L03/yevamot',2)
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['source_index']==f['source_index'] and s['ref']==f['ref'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
byref={s['ref']:s for s in segs.values()}
for e in prep['source_evidence']:assert byref[e['ref']]['text']==e['text'] and byref[e['ref']]['source_index']==e['source_index']
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
proposal=read(J/'proposals'/f'{PH}.json');assert len(proposal['records'])==89;revised={r['supersedes'] for r in proposal['records'] if 'supersedes' in r};assert len(revised)==1
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
base=read(J/'snapshots'/(receipt['parent_snapshot']+'.json'))
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
ep=Path(receipt['export_directory']);em=read(ep/'manifest.json')
for n,h in receipt['export_files'].items():assert sha((ep/n).read_bytes())==h
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:238 for k in runner.LAYERS}
# Explicit manually assessed alignment, not lexical or regex agreement scoring.
names=[
'yev011.context.abaye_daughter','yev011.context.abaye_daughter','yev011.context.abaye_exclusion','yev011.context.abaye_exclusion','yev011.context.abaye_exclusion','yev011.context.rav_safra','yev011.context.rav_safra','yev011.context.rav_safra',
'yev011.context.rabbi_principles','yev011.rava_report','yev011.context.rava_rules','yev011.context.rava_rules','yvfix011.context.two_sisters','yvfix011.context.two_sisters_negative','yvfix011.context.two_unrelated','yvfix011.context.two_unrelated_negative',
'yev011.context.ashi_rules','yev011.context.ashi_rules','yev012.u225','yev011.context.judah_identification','yev012.u227','yev012.u227','yev012.u227','yev011.context.judah_identification yev012.u228','yev012.u228','yev011.context.judah_identification',
'yev011.context.transgressive_marriage yev011.ravina','yev011.context.if_excluded','yev011.ashi_kahana','yev011.context.other_construction','yev011.context.other_construction','yev011.context.lawful_sister','yev011.levi_teaching yev012.u231',
'yvfix011.context.levi_adds yvfix011.context.levi_exemption','yvfix011.context.levi_adds','yvfix011.context.levi_exemption','yev012.sixteenth_conclusion','yev012.additional_case yev012.rl_question','yev012.additional_case yev012.interlocutor_premise',
'yev012.no_further_cowife','yev012.negative_commandment_objection','yev012.negative_commandment_eligibility','yev012.interlocutor_premise','yev012.yohanan_own_classification yev012.negative_commandment_eligibility','yev012.interlocutor_premise yev012.no_further_cowife',
'yev012.context.rl_self','yev012.context.rl_brothers yev012.context.rl_cowife','yev012.context.yohanan_chalutzah yev012.context.yohanan_cowife','yev012.context.no_rebuild','yev012.context.performer_only','yev012.context.chalutzah_only','yev012.context.yohanan_objection','yev012.context.brother_agency yev012.context.cowife_agency']+['']*10
assert len(names)==63
partial={3,4,17,18,19,21,22,23,24,25,42,44,47,48}
mapping=[]
for i,(f,ns) in enumerate(zip(prep['findings'],names),1):
 ids=ns.split();assert all(n in active for n in ids),(f['id'],ids)
 status='future_context_not_claimed_as_covered' if i>53 else ('partial_or_bundled_see_required_repairs' if i in partial else 'represented')
 mapping.append({'reader_id':f['id'],'scope':f['scope'],'producer_ids':ids,'disposition':status})
findings=[
{'id':'Y012-01','severity':'medium','category':'core_question_and_argument_omissions','refs':['Yevamot9b:9','Yevamot10a:5','Yevamot10a:7–8'],'records':['yev011.context.abaye_exclusion','yev011.context.judah_identification','yev012.u225','yev012.u227','yev012.u228'],'judgment':'Explicit why-Abaye-excludes question, how-Rabbi-rebuke-is-explained question, and mother-versus-father-wife duplication question have no question-layer records. The six-severe-relatives/co-wives-permitted premise, separately named mother/father-wife/father-sister categories, rejected mother-as-married-father-wife hypothesis, resulting mother-as-rape-victim reading and others-yes/brothers-no inference are only incompletely represented in a broad prior context summary or utterance source evidence. Core promotion now claims full passes for these segments.','required_action':'Add source-supported explicit questions and their answer links. Represent the distinct list/permission premise, rejected duplicate interpretation and rape-mother/inclusion-exclusion argument with precise source conditions and support links to Rabbi Yehudah identification. Preserve exact source brackets and original summary lineage; do not force confirmed answer sets.'},
{'id':'Y012-02','severity':'medium','category':'atomic_core_and_produced_context_outcomes','refs':['Yevamot9b:10','Yevamot10a:5','Yevamot10b:4–5','Yevamot10b:7–10'],'records':['yev011.context.abaye_exclusion','yev011.context.ashi_rules','yev012.negative_commandment_eligibility','yev012.context.rl_cowife','yev012.context.yohanan_chalutzah','yev012.context.yohanan_cowife','yev012.context.performer_only','yev012.context.chalutzah_only'],'judgment':'Some opposing or independently queryable outcomes remain combined: configuration possible for Shimon versus impossible for sages; Rabbi lacks general principles versus discusses disputed cases; halitzah and yibbum procedural options; distinct performer/brothers liability cells; and positive לא יבנה scope versus excluded party prior status. Previous 011 repaired two-sisters/unrelated and Levi opposite outcomes correctly, but these remaining composites became core or were newly produced as context.','required_action':'Make minimal immutable atomic successors for the listed independent outcomes, retaining branching conditions and holders. Keep halitzah/yibbum as distinct procedural alternatives, not simultaneous requirements or unrestricted practical permission. Split only source-supported person/woman cells; refresh all dependent positions/edges/coverage, including own-view/interlocutor qualification. Context coverage must remain uncounted.'},
{'id':'Y012-03','severity':'none','category':'correct_transmission_and_interlocutor_scope','judgment':'Rav Adda→Rava is preserved with Kahana as audience; Ashi→Kahana and RL→Yohanan are direct dialogue, not transmission. Rav Safra six-brother Shimon condition and death/birth/yibbum order retained. Prior two-sisters/unrelated opposite outcomes and Levi histories reuse corrected records. Yohanan own negative-commandment classification is distinguished from answering on RL karet premise, and no-co-wife-of-co-wife answer is properly qualified.'},
{'id':'Y012-04','severity':'task_limitation','judgment':'Reading has45core+18context findings. Context54–63 (10b13–11a6) was read but not produced and is not a current omission claim. Existing produced context46–53 receives targeted atomicity review without coverage credit. Reader is not blind to earlier011context labels; no fresh/random cohort credit or full-tractate acceptance.'}]
out={'verdict':'REWORK_TARGETED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':prep['exposure']+' Frozen reading preceded new012labels; exact-version comparison is nonblind. Prior context acceptance did not certify all later core passes.','scope':prep['scope'],'mapping':mapping,'source_findings':{'core':45,'context':18,'future_context_unproduced':10},'findings':findings,'required_repairs':['Y012-01','Y012-02'],'integrity':{'full_exact_replay':True,'source_offsets_indices':True,'export_files':True,'prior_records_preserved':True,'active_dependencies':True},'new_records':88,'superseded_records':1,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':3631,'next_source':'Yevamot10b:6','open_tails':head['open_tails'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Producer alone performs immutable targeted omissions/atomicity repairs without coverage growth. Preserve prior source records, rejected initial proposal and validation recovery. Independently recheck exact corrected version.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
