import json, hashlib, importlib.util, sys
from pathlib import Path
B=Path(__file__).resolve().parent.parent
C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim')
H='0ca186f5d15caef7d17399b21fd0464a8f22b9ded849d454f08b6460c4e00c64'
RH='0fd673049af4f37d4c0e8efc2ef9ad2ec856c1fab194bf48a7be786ca60994ab'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
bind=lambda p:dict(path=str(Path(p).resolve()),sha256=h(p))
read=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
rp=B/'readings/zevachim_batch001.json';pp=J/'snapshots'/f'{H}.json'
assert h(rp)==RH and h(pp)==H
r=read(rp);p=read(pp);runner=C/'research/bavli_production_v1/runner.py'
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('zreview_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
j,segs=m.load(J);texts={v['ref']:v['text'] for v in segs.values()};refs={k:v['ref'] for k,v in segs.items()}
for v in r['bindings'].values():
 if isinstance(v,dict) and 'path' in v and 'sha256' in v: assert h(v['path'])==v['sha256']
state=m.empty()
for ph in p['proposals']:
 f=J/'proposals'/f'{ph}.json';assert h(f)==ph
 prev=state['proposals'];state=m.validate_apply(state,read(f),segs,j);state['proposals']=prev+[ph]
assert m.encoded(state)==m.encoded(p) and m.sha(m.encoded(state))==H
report=m.report(state,segs)
def check(x):
 n=0
 if isinstance(x,dict):
  if all(k in x for k in ['quote','start','end','source_ref']): assert texts[x['source_ref']][x['start']:x['end']]==x['quote'];n+=1
  if all(k in x for k in ['quote','start_char','end_char','segment_id']): assert segs[x['segment_id']]['text'][x['start_char']:x['end_char']]==x['quote'];n+=1
  for v in x.values(): n+=check(v)
 elif isinstance(x,list):
  for v in x:n+=check(v)
 return n
rn=check(r);pn=check(p)
by={x['id']:x for x in p['records']};active=[x for x in p['records'] if x['release_state']=='valid'];core=set(r['core_refs'])
completed={layer:{refs[x['segment_id']] for x in p['coverage'] if x['layer']==layer and x['extraction_state']=='completed'} for layer in m.LAYERS}
assert all(core<=v for v in completed.values())
cs=[x for x in r['findings'] if x['cohort']=='core']
targets=['zev_open_c_'+x for x in ['valid','valid','pesach','chatat','asham','sin','yosi','high','high','high_examples','high_examples','high_examples','high_examples','sanctity','sanctity','rava','reason']]
targets+=['zev_avodot_carrying']+['zev_baalim_'+x for x in ['pinchas','todah','todah','todah','zvach','chatatasham','two','no_slaughter','analogy']]
targets+=['zv.20261126.b3.'+x for x in ['c8a','c8','c9','c10','c10','c11','c12a','c12b','c12b','c13','c14','c16']]
assert len(cs)==len(targets)==39
recordhash=lambda x:hashlib.sha256(m.encoded(x)).hexdigest()
rows=[]
for x,t in zip(cs,targets):
 z=by[t];assert z['release_state']=='valid'
 pos=[v for v in active if v['layer']=='positions' and v['content']['claim_id']==t]
 rows.append(dict(reader_id=x['id'],reader_record_sha256=recordhash(x),producer_id=t,producer_record_sha256=recordhash(z),reader=x,producer=z,positions=pos,result='source_content_present; atomicity and local-status caveats apply'))
qmap={'Q01':['zev_open_q_word'],'Q02':['zev_avodot_q_carrying'],'Q03':['zev_baalim_q_source'],'Q04':['zev_baalim_q_works'],'Q05':['zv.20261126.b3.q5'],'Q06':['zv.20261126.b3.q15','zv.20261126.b3.q16'],'Q07':['zv.20261126.b3.q24']}
# Match the main inquiry by source evidence, independent of naming convention.
qmap['Q05']=[x['id'] for x in active if x['layer']=='questions' and any(refs[e['segment_id']]=='Zevachim 6a:12' for e in x['evidence'])]
questions=[dict(reader=x,cohort='core' if any(e['source_ref'] in core for e in x['evidence']) else 'context',producer=[by[t] for t in qmap[x['id']]],assessment='Same local question; Q06 preserves producer separate original/corrected formulations; partial answer status is not settled law.') for x in r['questions']]
emap={('C05','C01'):['zev_open_e_asham_disagreement_v2'],('C06','C05'):['zev_open_e_analogy'],('C16','C15'):['zev_open_e_rava'],('C17','C16'):['zev_open_e_reason'],('C18','C16'):['zev_open_e_nedava'],('C25','C21'):['zev_baalim_e_zvach'],('C27','C26'):['zev_baalim_e_two'],('C49','C48'):['zv.20261126.b3.e10_9'],('C51','C48'):['zv.20261126.b3.e11_9'],('C53','C52'):[],('C55','C51'):['zv.20261126.b3.e12_11','zv.20261126.b3.e13_12'],('C56','C55'):['zv.20261126.b3.e14_13'],('C57','Q06'):['zv.20261126.b3.e16_15']}
edges=[]
for x in r['relations']:
 if any(e['source_ref'] in core for e in x['evidence']):
  ts=emap[(x['source_id'],x['target_id'])]
  edges.append(dict(reader=x,producer=[by[t] for t in ts],assessment='Compared argument role, with reader-target and missing-disagreement caveats below.'))
def issue(i,cat,ids,finding,change):
 return dict(id=i,category=cat,severity='targeted',resolution='open; no production mutation',records=[dict(id=t,sha256=recordhash(by[t])) for t in ids],finding=finding,required_change=change,regression_check='Re-read exact source and new successor/dependent records; do not inherit this version review.')
issues=[
 issue('ZV-ATOMIC','atomic_representation',['zev_open_c_valid','zev_open_c_high','zev_open_c_high_examples','zev_open_c_sanctity','zev_baalim_todah','zv.20261126.b3.c10','zv.20261126.b3.c12b'],'All 39 reader core claim meanings have counterparts, but validity/non-discharge, opposite sanctity rulings, four examples, retained sanctity/prohibition, three Abba Chanin propositions, temporal boundary/inquiry scope, and atonement/as-if-not-atoned are bundled. This is atomic representation deficit, not absent text; 39 matches cannot be counted as 39 distinct atomic producer claims.','Create separately anchored atomic claims/positions where required, preserving conditions and source occurrences; retained composite summaries must not double count.'),
 issue('ZV-STATUS','local_position_status',['zv.20261126.b3.p11','zv.20261126.b3.p13'],'Proposed person/before-Heaven interpretation and the challenged oil inference have generic Local statement; objections and qualifications retained status. Claims c11/c13 use asserted although the local reading is offered and counter-interpreted at 6b:4. Existing objection e14_13 preserves graph history but a position-only view loses it.','Mark proposed/challenged interpretation explicitly in successor position status, and scope assertion mode as interpretive proposal rather than settled conclusion.'),
 issue('ZV-OIL-RELATION','argument_relation_omission',['zv.20261126.b3.c12a','zv.20261126.b3.c12b'],'Distinct Rabbi Akiva and Rabbi Yohanan [ben Nuri] claims/positions exist, but no typed edge between these competing outcomes for omitted oil was found. The reader qualification edge also understates the disagreement on atonement.','Add a source-supported relation/common question for the incompatible outcomes under omitted oil; preserve bracketed attribution and quoted status.')]
reader_errors=[
 'C20 compresses two independently quoted lexical interpretations and the resulting inference; its transmission_chain entries are cited anonymous teachings, not a serial personal transmission chain. Producer separates limbs, blood and carrying claims correctly.',
 'C05->C01 qualification and C53->C52 qualification understate actual competing outcomes. Producer opening objection is more precise; oil relation remains missing.',
 'C25->C21 answer is shorthand: the immediate question concerns a competing use of the verse. Producer targets q_todah, correctly. Likewise C27 answers q_chatat rather than denying the quoted inclusion.',
 'C18->C16 support requires C19 (even a voluntary offering may not be altered); producer nedava support retains that intermediate premise. Do not classify its different endpoint as omission.',
 'Reader C14/C15/C17 have empty conditions despite contextual prior alteration; producer preserves this scope. C52/C53/C54 asserted locally are quoted views, not adjudicated law.',
 'Q02/Q05/Q07 begin in context; their answers may touch core but their question counts must not be added to core-origin denominators.',
 'Reader C65/C66 holders combine reporter and quoted holder in a label; producer separates Rabbi Shimon/Sages and the four-person transmission chain more clearly. Context check only.'
]
qs=[x for x in questions if x['cohort']=='core']
den=dict(independently_found_atomic_claims=39,attributable_claims=39,named_holder_claims=sum(not all(y.startswith(('anonymous','cited anonymous')) for y in x['holders']) for x in cs),condition_bearing_claims=sum(bool(x['conditions']) for x in cs),questions=len(qs),proposed_answer_sets=len(qs),supported_edges=len(edges),attributable_definition='Includes anonymous and quoted voices; named-holder subset separate.',condition_definition='Nonempty reader condition arrays, not condition completeness; contextual missing conditions noted separately.',edge_definition='Reader relation evidence intersects a sampled core; context-only relations excluded. Counts are occurrences, not unique topics.')
bindings={k:v for k,v in r['bindings'].items()}
bindings.update(initial_reading=bind(rp),snapshot=bind(pp),runner=bind(runner),run_contract=bind(C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),contract_production_commit='15bba19d80273232b4554dfe507ceb37e97843a2',proposals=[bind(J/'proposals'/f'{x}.json') for x in p['proposals']],comparison_script=bind(__file__),plan_embedded_sha256=r['plan_sha256'])
cohorts=dict(endpoint_core_segments=10,probability_core_segments=20,overlap_core_segments=0,unique_core_segments=30,context_expansion_segments=r['coverage']['context_expansion_segments'])
out=dict(artifact_kind='nonblind_exact_version_partial_comparison',comparator_provenance=dict(agent_id='/root/compare_zevachim_wave2',blind=False,reader_frozen_before_comparison=True),bindings=bindings,denominators=den,cohorts=cohorts,core_refs=r['core_refs'],context_refs_not_in_denominator=r['context_refs'],claim_comparisons=rows,question_comparisons=questions,answer_sets=r['answer_sets'],edge_comparisons=edges,producer_issues=issues,reader_corrections=reader_errors,uncertainties_preserved=r['uncertainties'],qa=dict(reader_evidence_slices=rn,producer_evidence_slices=pn,all_slices_match_original_source=True,replay=dict(read_only=True,method='load + empty + validate_apply for exactly frozen proposal list; no lock/current/submit/write to production',replay_pass=True,snapshot_sha256=H,proposal_count=len(p['proposals']),report=report)),source_omission_pass=dict(scope='All 30 independently read cores, all 8 producer layers completed at this exact snapshot',absent_reader_core_claim_meanings=0,distinct_producer_claim_counterparts=len(set(targets)),atomic_completeness_pass=False,additional_source_claims='Producer limbs/blood lexical claims at 4a:16 exceed reader compressed C20; not hallucinations.'),context_checks=dict(ownership_analogy='4a:26–4b:4 objections, two remaining distinctions, and replacement Rav Ashi derivation retained; no final adoption inferred.',atonement='6b:12–7a:4 transmitter/holder distinction and conditional deflection retained; no Rav–Shmuel dispute inferred.',limits='Context selected continuation check, not exhaustive context review or expansion of sampled denominator.'),limits=['Initial reading and producer snapshot preserved immutable.','No whole-tractate accuracy estimate or full admission.','Bundled counterparts and reader omissions prevent numeric precision/recall claim.'],human_certification=False,ml_eligible=False)
cp=B/'comparisons/zevachim_batch001_exact_version.json'
assert not cp.exists();cp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
v=dict(verdict='REWORK_TARGETED',bindings=bindings,comparison=bind(cp),scope='30 unique cores: opening 10 and two probability blocks totaling 20; selected context checks only',required_changes=issues,task_eligibility={k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},layer_matrix=dict(**cohorts,independent_core_denominators=den,producer_completed_per_layer=report['completed_by_layer'],producer_completed_sampled_cores_per_layer={k:len(core&v) for k,v in completed.items()},source_segments_total=report['source_segments']),tractate_accepted=False,full_review_receipt=False,human_certification=False,admission_owner='global coordinator',remaining='Authorized owner may produce new revisions; recheck changed versions. Resume independent source reading at block_000022, Zevachim 7b:16–25; do not reuse this comparison as blind evidence.')
vp=B/'verdicts/zevachim_batch001_v2_verdict.json';assert not vp.exists();vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(comparison=bind(cp),verdict=bind(vp),denominators=den,qa=out['qa'],source_omission_pass=out['source_omission_pass']),ensure_ascii=False))
