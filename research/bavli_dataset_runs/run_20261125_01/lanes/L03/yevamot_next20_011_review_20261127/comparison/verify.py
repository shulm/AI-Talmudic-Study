import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');P=OUT.parent.parent/'yevamot/bounded011_20261127'
HEAD='56f41af1f27aca3e247b91801831b865ce44e832a2dd06a2a56a04e9dcc452a9';PH='0372c3b7b534a6eea5c07652433ea11e78a7fca71477c4aaf609bbb5e797951d'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='8ab7d3fa45cab00a9131a6191ae411a944ce554ccee95611f40729279ce4d36c'
receipt=read(P/'RECEIPT.json');pins=read(P/'PINS.json');assert sha((P/'RECEIPT.json').read_bytes())=='0692c49beac570f031f041483d37c64bf57a53dffa0eebf436a7cc675b2cbd3e'
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);assert job['source_sha256']==prep['source_sha256']
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['source_index']==f['source_index'] and s['ref']==f['ref'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
proposal=read(J/'proposals'/f'{PH}.json');assert len(proposal['records'])==163;revised={r['supersedes'] for r in proposal['records'] if 'supersedes' in r};assert len(revised)==1
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
base=read(J/'snapshots'/(pins['parent_snapshot']+'.json'))
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
ep=Path(receipt['export_directory']);em=read(ep/'manifest.json');assert sha((ep/'manifest.json').read_bytes())==receipt['export_manifest_sha256']
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:218 for k in runner.LAYERS}
names=['@yev010.context_different_offerings @yev010.context_one_law','@yev010.context_challenge u199','@yev010.context_elimination.bull','@yev010.context_elimination.ewe','@yev010.context_elimination.male_goat','@yev010.context_elimination.pair','@yev010.context_elimination.female_goat','@yev010.context_inverted','@yev010.context_no_remedy','levi_sixteen levi','rabbi u203','mother_candidate','mother_disputed','avoid_disputes ashi_limits_initial','prohibitions_counterexample','akiva_dispute akiva_objection','current_chapter chapter_qualification','shammai_cowives hillel_cowives','houses_counterexample houses_objection','shammai_standing','noncontemporary_counterexample','shimon_noncontemporary','born_then_yibbum','born_then_yibbum sequence_answer','oshaya_report oshaya_objection','oshaya_refuted oshaya_correction','rav_route hiyya_parallel','forbidden_one forbidden_other sister_yibbum','general_rule_objection general_objection','rav_yehuda_scope','first_six_excluded rav_yehuda_why','u216 daughter_rape daughter_not_marriage','daughter_rape daughter_not_marriage','marriage_scope','context.abaye_daughter','context.abaye_exclusion','context.rav_safra','context.rav_safra','context.rava_rules rava_report','context.two_sisters','context.two_unrelated','context.ashi_rules rules_alternatives','context.judah_identification','context.judah_identification','context.judah_identification','context.transgressive_marriage context.if_excluded','context.other_construction ashi_kahana','context.lawful_sister context.levi_adds','context.levi_adds','context.levi_adds']
assert len(names)==50
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=[n[1:] if n.startswith('@') else 'yev011.'+n for n in ns.split()];assert all(n in rows for n in ids),(f['id'],ids)
 mapping.append({'reader_id':f['id'],'scope':f['scope'],'producer_ids':ids,'disposition':'content represented; see atomicity and scope repairs'})
findings=[{'id':'Y011-01','severity':'medium','category':'atomic_opposite_outcomes','refs':['Yevamot9b:5','Yevamot10a:3–4','Yevamot10a:12–10b:1'],'records':['yev011.sister_yibbum','yev011.context.two_sisters','yev011.context.two_unrelated','yev011.context.levi_adds'],'judgment':'The sister rule stores chalitzah/yibbum as one outcome; the two constructed cases each bundle one realizable and one non-realizable configuration; Levi’s concluding teaching bundles exemption and non-exemption under different marriage histories. These are independently queryable outcomes/conditions and need atomic representation. Textual content is preserved but not decomposed.','required_action':'Split the two permitted procedural options without turning them into simultaneous obligations; split positive/negative configuration outcomes; split Levi’s two opposite exemption cases with exact histories and distinct occurrences. Preserve original composites/lineage and refresh all dependent edges/positions/coverage. Context remains uncounted.'},
 {'id':'Y011-02','severity':'medium','category':'partial_rule_scope_linkage','refs':['Yevamot9b:5–8'],'records':['yev011.forbidden_one','yev011.forbidden_other','yev011.sister_yibbum','yev011.limited_rule','yev011.excluded_rule'],'judgment':'Rav Yehuda’s mother-in-law-onward/first-six exclusion concerns the entire quoted configuration. Current qualification edges reach forbidden_one and sister_yibbum, but not forbidden_other. The second reciprocal statement thus lacks its corresponding structured scope qualification.','required_action':'Link the source-supported Rav Yehuda restriction to every applicable reciprocal/procedural atom, including split successors; retain as his interpretation, with Abaye/Rav Safra alternatives separate. Do not impose this restriction as unanimous final scope.'},
 {'id':'Y011-03','severity':'none','category':'correct_attribution_chronology_and_continuation','judgment':'Born-before-yibbum order correct; Oshaya report rejected explicitly. RavYehuda→Rav and Hiyya parallel separate. RavAdda→Rava report correctly treats RavKahana as audience. Earlier no-dispute account remains challenged, Rava and Ashi alternatives and Levi followup attached. Source offering candidates, inverted pair and no-remedy hypothesis reused from exact prior context, not duplicated.'},
 {'id':'Y011-04','severity':'task_limitation','judgment':'34core and16context findings have content represented. Reader findings are purposive prompts, not exhaustive atomic gold labels. Rebuke retained as source speech in utterance and speaker attribution, not narrator medical assertion. No entire-sugya or full-tractate acceptance; future context coverage remains pending.'}]
out={'verdict':'REWORK_TARGETED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'reviewer':'/root/rosh_hashanah','method':prep['exposure']+' Source reading frozen before new producer labels; this exact comparison is now nonblind.','scope':prep['scope'],'mapping':mapping,'source_findings':{'core':34,'context':16,'content_represented':50},'findings':findings,'required_repairs':['Y011-01','Y011-02'],'integrity':{'full_exact_replay':True,'source_offsets_indices':True,'export_files':True,'prior_records_preserved':True,'active_dependencies':True},'new_records':162,'superseded_records':1,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':3651,'next_source':'Yevamot9b:9','open_tails':head['open_tails'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Producer alone performs immutable targeted atomicity/scope repairs, preserving original evidence and no context coverage increase. Independent recheck exact corrected version.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
