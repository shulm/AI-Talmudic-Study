import sys,json
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_nazir');P=OUT.parent.parent/'nazir/bounded_004_20261127';HEAD='4399af0015bd61a92fec0117200e87a3a9209b9d5be69a8acc8223e420483309';PH='60631f137abedf3135efb0b0c8f1905edcb210b68c4f2624cd37ff0cb70a63b3'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='6640ada18da20ac29bbfd702326884f9511dd0080c8c843c9cb3d6b28e7b1b7e'
assert sha((P/'VALIDATION_REVISED_PROPOSAL.json').read_bytes())==PH
assert sha((P/'RECEIPT.json').read_bytes())=='ef31a0b782a16728edb428538cbf01dc0a9711da282b9ec99dfcaead6ef275de'
assert sha((P/'MANIFEST.json').read_bytes())=='76e147f118591eea709b52de764993c688d9d866e654bba1be2bd08a7f24a0b7'
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
p=read(P/'VALIDATION_REVISED_PROPOSAL.json');assert len(p['records'])==182;revised={r['supersedes'] for r in p['records'] if 'supersedes' in r};assert len(revised)==8
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
report=runner.report(head,segs);assert report['completed_by_layer']=={k:70 for k in runner.LAYERS}
ep=J/'exports/bounded_004_20261127';em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
names=['naz003.context.oath_drink naz003.rava naz003.oath_replaces','naz003.context.sages_wine_use','naz003.context.extra_shekhar','naz003.context.shimon_temple','naz004.revised.naz003.context.nazir_wine naz004.other_drinks_nazir','naz004.revised.naz003.context.temple_wine naz004.other_drinks_temple','naz003.context.yehuda naz003.yehuda naz004.yehuda_counter_other','naz003.context.nonoverlap','naz003.context.nevelah','naz003.context.sages_allverse','naz003.context.combine','naz003.context.shimon_nojoin naz003.context.any_amount','naz003.context.olive_offering','naz004.samson_formula_rule','naz004.other_samson naz004.manoa_limit','naz004.why_identifiers','naz004.other_samson naz004.manoa_identifier','naz004.manoa_namesake naz004.delilah_identifier naz004.eyes_identifier','naz004.difference','naz004.lifelong_cut','naz004.lifelong_animals','naz004.lifelong_impurity','naz004.samson_no_cut','naz004.samson_no_impurity_offering naz004.style_qualifies','naz004.lifelong_antecedent naz004.lifelong_intro','naz004.lifelong_intro','naz004.lifelong_cut naz004.lifelong_animals naz004.lifelong_impurity','naz004.samson_no_cut','naz004.samson_no_impurity_offering','naz004.samson_effective','naz004.which_tanna','naz004.yehuda_permission','naz004.samson_historical_impurity naz004.context.impurity_tradition','naz004.shimon_ineffective','naz004.samson_no_speech naz004.context.angel_speech','naz004.yehuda_if_objection','naz004.shimon_effect_objection_q','naz004.mishnah_yehuda naz004.if_impure_style','naz004.firstborn_analogy_q','naz004.yaakov_firstborn','naz004.yosi_firstborn','naz004.context.yehuda_yaakov naz004.context.shimon_yosi','naz004.context.all_vow naz004.context.firstborn_special','naz004.context.yosi_sin naz004.context.yosi_guilt','naz004.context.selection naz004.context.offerings_vow naz004.context.firstborn_not_vow','naz004.context.yaakov_vow naz004.context.firstborn_duty','naz004.context.firstborn_automatic','','','','','naz004.context.samson_verse naz004.context.angel_speech','naz004.context.impurity_proof naz004.context.no_touch_possibility','naz004.context.clothes_before naz004.context.verse_order','naz004.context.dying_possibility naz004.context.impurity_tradition']
assert len(names)==55
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=ns.split();assert all(k in active for k in ids),(f['id'],ids)
 mapping.append({'reader_id':f['id'],'scope':f['scope'],'producer_ids':ids,'disposition':'represented' if ids else 'unproduced_context_not_coverage_omission'})
# Repeated Mishnah/reconstruction occurrences retain both evidence addresses rather than disappearing.
for k in ['lifelong_cut','lifelong_animals','lifelong_impurity','samson_no_cut','samson_no_impurity_offering']:assert len(rows['naz004.'+k]['evidence'])==2
out={'verdict':'ACCEPT_BOUNDED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'producer_receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'source_sha256':job['source_sha256'],'reviewer':'/root/rosh_hashanah','method':prep['exposure']+' Frozen reading before new004 labels; exact comparison now nonblind.','scope':prep['scope'],'mapping':mapping,'source_findings':{'core':41,'core_represented':41,'context':14,'context_unproduced':4},'required_repairs':[],'findings':[{'id':'N004-01','status':'pass','judgment':'Rava replacement preserved; alternative Shimon nonoverlap explanation remains alternative. Wine versus other drinks atomic in both nazir/Temple scopes; any-amount lashes distinct from olive-size offering.'},{'id':'N004-02','status':'pass','judgment':'Samson identifiers retain ambiguity constraints; perpetual versus Samson haircut/offering outcomes separate. Reconstructed חסורי מיחסרא explicitly marked; repeated original/reconstructed occurrences retained as separate evidence and utterances, not extra independent rules.'},{'id':'N004-03','status':'pass','judgment':'Mishnah final Yehudah assignment and stylistic if-impure explanation qualify initial reading. Shimon no-personal-speech reason and angel response preserved. Firstborn alignment rejected explicitly; all-require-davar-hanadur answer retained. Samson impurity ultimately tradition; proposed verse-contact proofs remain defeasible.'},{'id':'N004-04','status':'limitation','judgment':'Yehudah intake list remains one quoted liability statement with all listed foods/drinks and no dose claim. Do not treat the slash honey/milk as proof of mixed drink or derive independent minimal-dose sufficiency for each item. No forced repair beyond source support.'}],'checks':{'exact_full_replay':True,'source_offsets_indices':True,'export_files':True,'prior_records_preserved':True,'active_dependencies':True,'primary_partition_validation':True},'proposal_rows':182,'superseded_records':8,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':1229,'next_source':'Nazir4b:7','open_tails':head['open_tails'],'limits':['Only20core bounded scope accepted; no whole-tractate acceptance.','Source questions and answer sets remain provisional; no demanding-task qualification.','4b13–16 dedication question/narrative read but not extracted, explicitly uncounted context. Future core must represent voices and events then.','Shared claim records retain two actual occurrence spans; downstream occurrence counts must use evidence/utterances, not equate record count with unique topics.','Historical owner epoch1 and actual producer /root/yevamot execution remain separate.'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'tractate_acceptance':False,'resume':'Resume under coordinator instructions at4b7, reusing context and preserving rejected mapping and tradition endpoint; full context extraction remains future work.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
