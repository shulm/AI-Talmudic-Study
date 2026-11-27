import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
read=lambda p:json.loads(p.read_text(encoding='utf-8'));sha=runner.sha
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');P=OUT.parent.parent/'tamid/bounded_005_20261127'
HEAD='6c126f20c894521d8cb07372422bef1daa376824ac464dfb9511a98252f60e25';PH='7ec50bb14ea99f92750a1ae3d30019b72aa6aed85e942eb1590529faff224208'
prep=read(OUT.parent/'SOURCE_READING.json');assert sha((OUT.parent/'SOURCE_READING.json').read_bytes())=='6567639ecf7a6531618f9f1af06783432a0bb59aed9927f2cf18d7df856d4258'
receipt=read(P/'RECEIPT.json');pins=read(P/'PINS.json');assert receipt['snapshot_sha256']==HEAD and receipt['proposal_sha256']==PH
head=read(J/'snapshots'/f'{HEAD}.json');assert sha((J/'snapshots'/f'{HEAD}.json').read_bytes())==HEAD
job,segs=runner.load(J);assert job['source_sha256']==prep['source']['sha256']
for f in prep['findings']:
 for e in f['evidence']:
  s=segs[e['segment_id']];assert s['source_index']==e['source_index'] and s['ref']==e['ref'];assert s['text'][e['start_char']:e['end_char']]==e['quote']
s=runner.empty()
for h in head['proposals']:
 b=(J/'proposals'/f'{h}.json').read_bytes();assert sha(b)==h
 prev=s['proposals'];s=runner.validate_apply(s,json.loads(b),segs,job);s['proposals']=prev+[h]
assert runner.encoded(s)==runner.encoded(head)
proposal=read(J/'proposals'/f'{PH}.json');assert len(proposal['records'])==223
revised={r['supersedes'] for r in proposal['records'] if 'supersedes' in r};assert len(revised)==1
rows={r['id']:r for r in head['records']};active={k for k,r in rows.items() if r['release_state']=='valid'}
base=read(J/'snapshots'/(pins['base_snapshot']+'.json'))
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
ep=J/'exports/bounded_005_20261127';em=read(ep/'manifest.json')
for n,h in em['files'].items():assert sha((ep/n).read_bytes())==h
report=runner.report(head,segs);assert report['completed_by_layer']=={k:70 for k in runner.LAYERS}
names=['@tam004.tunnels_context','@tam004.two_camps_context','emission_closed','u51','safra_sitting abba_signal','safra_invite','abba_rebuke','@tam001.locked u52','privacy_objection','danger','column_returns','stream_returns','column_danger stream_danger danger_invite','rav_son huna_son','dark early distance_reason','sit_uncover','cover_rise','wash_drink wash_put','pour_handoff','baraita_pour','teacher_no_pour','student_refused student_died','rule_then','student_pour','pour_deference','no_spit','gourd_exception porridge_exception lead_reason','patrol patrol_torches','sleep_recognition','strike','burn','sound_identification','uncle uncle_burn','hiyya_yohanan','praise_earlier','deliberate_a_fortiori sleep_qal','path_q','love_rebuke','ease','good blessing','evil_departs','prov24 proverb_ground','faithfulness','psalm101 psalm_ground','yonatan_chain','divine_portion','grace','portion_support grace_support','lottery_q','not_lottery_hyp','lottery_hyp','@tam001.lottery_abaye','original_volunteer','race first_wins','tied_signal','fingers','no_thumb','push broken_leg','court_danger lottery_enactment','danger_enactment history_abaye','@tam001.lottery_rava','@tam001.lottery_rava','abaye_answer rava_answer','key gate','entry','priests_follow two_torches']
assert len(names)==66
mapping=[]
for f,ns in zip(prep['findings'],names):
 ids=[n[1:] if n.startswith('@') else 'tam005.'+n for n in ns.split()]
 assert all(n in rows for n in ids),(f['id'],ids)
 mapping.append({'reader_id':f['id'],'producer_ids':ids,'disposition':'represented with attribution-role repair' if f['id']=='tam005.f014' else 'represented; quoted locked-door recurrence retained in utterance, original rule reused' if f['id']=='tam005.f008' else 'represented'})
findings=[{'id':'T005-01','severity':'medium','category':'speaker_addressee_not_transmission','refs':['Tamid27b:14'],'reader_ids':['tam005.f014'],'records':['tam005.rav_son','tam005.huna_son'],'judgment':'Source א״ל רב לחייא בריה וכן א״ל רב הונא לרבה בריה reports direct instructions from fathers to sons. The two records currently use role transmitter and chains [Rav,Hiyya] and [RavHuna,Rabbah], with both father and son in candidate lists. Their prose correctly states direction but structured transmission implies a reporting chain not stated here.','required_action':'Immutably revise as speaker/direct-address attribution: father is speaker; son is addressee explicitly in scope or separate supported role if schema permits. Clear unsupported transmission chains. Keep two parallel occurrences separate; refresh dependent coverage without new cores.'},
 {'id':'T005-02','severity':'task_limitation','category':'identity_resolution','refs':['Tamid27b:13'],'judgment':'Reader retains רשב״ג unresolved. Producer transparently expands standard acronym to Rabban Shimon ben Gamliel while preserving exact source surface; no generation, external entity ID or order-based assignment is asserted. This review does not require changing transparent expansion, but does not certify a unique historical person. Source reader caution preserved; no identity-task eligibility.'},
 {'id':'T005-03','severity':'none','category':'narrative_schema_recovery','judgment':'Narrative events use allowed asserted mode with reported local_status and narrator holder. The rejected reported-mode candidate is preserved. Read these as assertions by source narrator, not external historical verification. No claim of medical validation or current behavioral instruction is introduced.'},
 {'id':'T005-04','severity':'none','category':'continuation_and_alternatives','judgment':'Earlier tunnel and two-camp context records are reused at same source occurrence; Abaye and Rava context claims reused at28a6/10. Both unrejected reconciliations answer shared explicit question. Before/after ordinance, injured-runner motivation, crossfolio watch sentence and open inspection Mishnah are preserved. New core28a11 does not count following inspection procedure.'}]
out={'verdict':'REWORK_TARGETED','snapshot_sha256':HEAD,'proposal_sha256':PH,'source_reading_sha256':sha((OUT.parent/'SOURCE_READING.json').read_bytes()),'receipt_sha256':sha((P/'RECEIPT.json').read_bytes()),'producer_manifest_sha256':sha((P/'MANIFEST.json').read_bytes()),'source_sha256':job['source_sha256'],'export_manifest_sha256':sha((ep/'manifest.json').read_bytes()),'source_reader':'/root/yevamot','comparator':'/root/rosh_hashanah','exposure':'Comparator never produced Tamid; previously compared opening correction and prepared next10source. Read this frozen source reading and raw27b9–28b8 before005labels. Reader004/27b10priorcontext exposure disclosed in frozen input. Distinct reader/comparator; no fresh/random cohort.','scope':prep['scope'],'mapping':mapping,'source_findings':66,'represented_findings':66,'finding_count_not_atomic_claim_count':True,'findings':findings,'required_repairs':['T005-01'],'integrity':{'full_exact_replay':True,'source_offsets_indices':True,'export_files':True,'prior_records_preserved':True,'active_dependencies':True},'new_records':223,'superseded_records':1,'completed_by_layer':report['completed_by_layer'],'remaining_per_layer':137,'next_source':'Tamid28a:12','open_tails':head['open_tails'],'ml_eligible':False,'all_demanding_tasks':False,'eligible_records':0,'tractate_acceptance':False,'resume':'Producer alone corrects two attribution roles and dependent coverage; no coverage expansion. Preserve initial schema-rejected candidate, validated initial and this exact verdict. Independent recheck follows.'}
runner.immutable(OUT/'VERDICT.json',runner.encoded(out));runner.immutable(OUT/'REPLAY.json',runner.encoded({'snapshot_sha256':HEAD,'replay_pass':True,**report}));m={f.name:sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'verdict':m['VERDICT.json'],'manifest':sha((OUT/'MANIFEST.json').read_bytes())}))
