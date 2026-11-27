import json, hashlib, sys
from pathlib import Path
OUT=Path(__file__).parent; ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists(): ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
P=OUT.parent.parent/'eruvin/bounded_next20_20261127'
HEAD='35b7ebfcb7db5043158ff0c726dcc652b35c89703a6622f26fea2383c8faa007'
PH='7e89ab0ef6162d98a031e30e767d768ce4e637dbec6dc601729c06d66f6e2bf2'
assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='427dabe97357c1bdfe142f7312218cd3957e9f7eff97281c171e07f1dc6bfcc1'
prep=read(OUT.parent/'SOURCE_READING.json');receipt=read(P/'RECEIPT.json')
assert sha((P/'RECEIPT.json').read_bytes())=='153485dcf18fa0667d75fd91a7e368b0575023cca6843ea76a7caac601f0f827'
assert sha((P/'MANIFEST.json').read_bytes())=='6f8b5f2805fcafc43a7fdd83e6066aafba020f0565c33575cb69727d896f0bd9'
assert sha((P/'PROPOSAL.json').read_bytes())==PH
assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
head=read(J/'snapshots'/f'{HEAD}.json');job,segs=runner.load(J)
source=Path(prep['source_path']).read_bytes();assert sha(source)==prep['source_sha256'];raw=json.loads(source)['text']
for e in prep['core_source']+prep['context']:
 i,j=e['source_index'];assert raw[i][j][e['start_char']:e['end_char']]==e['quote']
rebuilt=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=rebuilt['proposals'];rebuilt=runner.validate_apply(rebuilt,json.loads(b),segs,job);rebuilt['proposals']=prev+[h]
assert runner.encoded(rebuilt)==runner.encoded(head)
base=read(J/'snapshots'/(receipt['pins']['base_snapshot']+'.json'))
head_by_id={r['id']:r for r in head['records']}
assert all(head_by_id[r['id']]==r for r in base['records'])
ep=Path(receipt['export_path']);em=read(ep/'manifest.json')
assert sha((ep/'manifest.json').read_bytes())==receipt['export_manifest_sha256']
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:130 for k in runner.LAYERS}
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,dict):
  for x in v.values():yield from strings(x)
stale=[(k,s) for k in active for s in strings([rows[k]['content'],rows[k].get('links',[])]) if s in rows and s not in active]
assert not stale
names=['height_amount_q height_needed width_q','width_yosef width_abaye','use_hyp_yosef use_hyp_abaye reject_yosef_explanation reject_abaye_explanation','all_permit','recognition partition','all_recognition same_recognition different_recognition','all_equate diminish','depth_q depth_needed length_q','length_yosef length_abaye','alignment_hyp align_correct','ami_asi.a','strip_four','no_strip_under no_strip_three','existing_new initial_four','homes homes_support','four_feasible','middle_hyp middle_object','nahman.a longer nahman_homes','corner corner_answer','abaye_second.a first.transmission second_proof','project_short','project_four','lose_lehi become_alley threshold_distinction','repeat.transmission projecting','repeat_short repeat_four repeat_quote_short repeat_quote_four','place_q alongside_problem opposite_answer different_answer','opposite_context different_context','seven_context','','','','ashi_context','equal_context','','','','','','']
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=['er.next20.'+n for n in ns.split()];assert all(i in rows for i in ids)
 mapping.append({'reader_id':f['id'],'scope':f['scope'],'producer_ids':ids,'disposition':'represented with repair caveats' if ids else 'context read; no core omission claimed; see ER03 for necessary qualification'})
assert len(mapping)==39
findings=[
 {'id':'ER01','severity':'medium','refs':['Eruvin 5a:2–4'],'records':['er.next20.'+n for n in ['first_heker','first_partition','second_same','second_different','third_decree']],'judgment':'These five source_explicit answer edges target width_q (what width?) although their sources explain why the two numeric rulings differ. They do not themselves answer the quantitative question. The three alternative explanation stages also have no structured premise scoping: all_permit, all_recognition and all_equate are detached from the claims they qualify.','required_action':'Retarget to a source-supported explanatory question (mark editorial formulation if inferred), or replace with accurately scoped explanatory relations. Preserve three alternative accounts, add supported premise/qualification links, keep anonymous mar sides unnamed and answer sets partial.'},
 {'id':'ER02','severity':'medium','refs':['Eruvin 5a:7','Eruvin 5a:13','Eruvin 5b:1','Eruvin 5b:4','Eruvin 5b:9'],'records':['er.next20.'+n for n in ['alignment_hyp','project_short','project_four','repeat_short','repeat_four','seven_context','ashi_context']],'judgment':'Several independently queryable outcomes remain bundled: Rav Yosef acceptance versus proposed Abaye rejection; lehi/alley classification versus additional-lehi obligation in first and repeated occurrences; eight-versus-seven qualification; Rav Ashi standing-majority versus breach-majority branches. repeat_four also omits explicit alley classification from its repeated claim (only the full utterance retains it).','required_action':'Split these outcomes into atomic claims/positions with their actual conditions and local hypothetical status. Preserve both source occurrences and original records; update quotation/support/qualification edges and coverage dependencies immutably. Context splits add no covered cores.'},
 {'id':'ER03','severity':'medium','refs':['Eruvin 5a:6–7','Eruvin 6a:9–10'],'records':['er.next20.strip_four','er.next20.no_strip_under','er.next20.no_strip_three'],'judgment':'The continuation explicitly distinguishes Rabbi Ami/Rav Asi case by remaining wall remnants (גידודי). It is read in producer context but not attached to the earlier represented side-breach teaching; the current structured conditions omit this later qualification. This is a core-rule continuation qualification, not a demand to claim all context covered.','required_action':'Add narrow source-backed context qualification for the reported teaching and its contrast with Rav Huna. Do not merge the two Rav Hunas or import all later breach discussions as completed cores.'},
 {'id':'ER04','severity':'task_limitation','judgment':'All 26 frozen core findings have textual content represented; this does not certify atomic completeness. The other 13 are context findings, of which five have direct representation and eight remain context-only. Width/length units, strict under-three boundary, rejected initial under-beam hypothesis, separate corner-opening scenario, and Rami bar Hama→Rav Huna transmission are preserved. Context-only later authorities are not omitted covered cores. Source reader and comparator are different agents; this is not a new blind/random cohort.'}
]
verdict={'verdict':'REWORK_TARGETED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'pins':receipt['pins'],'scope':'20 original cores Eruvin4b:18–5b:2; context through6a:10 uncounted','source_reader':'/root/blind_review','comparator':'/root/rosh_hashanah','exposure':'Comparator has never produced Eruvin. Read frozen reader and raw source before these production labels. Uses existing independently frozen reading, not a new blind cohort. Reader prior exposure retained in frozen input.','source_findings':{'core':26,'context':13,'core_content_represented':26},'mapping':mapping,'findings':findings,'required_repairs':['ER01','ER02','ER03'],'integrity':{'exact_replay':True,'source_hash_quotes_indices':True,'export_hashes':True,'prior_records_unchanged':True,'active_references_not_superseded':True},'coverage':report['completed_by_layer'],'remaining_per_layer':3516,'next_source':'Eruvin5b:3','open_tails':receipt['open_tails'],'eligibility':{'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'random_cohort_credit':0,'fresh_blind_cohort_credit':0},'tractate_acceptance':False,'resume':'Only producer may repair immutably; no coverage growth. Preserve initial proposal and this finding version, then independent exact-version recheck.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(verdict))
runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}))
m={p.name:sha(p.read_bytes()) for p in OUT.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
runner.immutable(OUT/'MANIFEST.json',runner.encoded(m))
print(json.dumps({'verdict_sha256':m['VERDICT.json'],'manifest_sha256':sha((OUT/'MANIFEST.json').read_bytes())}))
