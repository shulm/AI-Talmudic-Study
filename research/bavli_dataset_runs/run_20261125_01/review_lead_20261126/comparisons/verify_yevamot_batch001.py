import json,hashlib,importlib.util,sys
from pathlib import Path
B=Path(__file__).resolve().parent.parent
C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot')
H='d2e871c3e71086468534d07c26eda7351bc26789286d55d371a5b95016a22821';RH='a804e597b4942e1b1d2c60321f1131d07148e812208dff0acb8e1a41d59fbc1f'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
bind=lambda p:dict(path=str(Path(p).resolve()),sha256=h(p))
read=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
rp=B/'readings/yevamot_batch001.json';pp=J/'snapshots'/f'{H}.json';assert h(rp)==RH and h(pp)==H
r=read(rp);p=read(pp);runner=C/'research/bavli_production_v1/runner.py';sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('yreview_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
j,segs=m.load(J);texts={x['ref']:x['text'] for x in segs.values()};refs={k:v['ref'] for k,v in segs.items()}
def verify_bind(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:assert h(x['path'])==x['sha256']
  for v in x.values():verify_bind(v)
 elif isinstance(x,list):
  for v in x:verify_bind(v)
verify_bind(r['bindings'])
state=m.empty()
for ph in p['proposals']:
 f=J/'proposals'/f'{ph}.json';assert h(f)==ph;prev=state['proposals'];state=m.validate_apply(state,read(f),segs,j);state['proposals']=prev+[ph]
assert m.encoded(state)==m.encoded(p) and m.sha(m.encoded(state))==H
report=m.report(state,segs)
def check(x):
 n=0
 if isinstance(x,dict):
  if all(k in x for k in ['quote','start_char','end_char']):
   t=texts[x['ref']] if 'ref' in x else segs[x['segment_id']]['text'];assert t[x['start_char']:x['end_char']]==x['quote'];n+=1
  for v in x.values():n+=check(v)
 elif isinstance(x,list):
  for v in x:n+=check(v)
 return n
rn=check(r);pn=check(p);by={x['id']:x for x in p['records']};active=[x for x in p['records'] if x['release_state']=='valid'];core=set(r['core_refs'])
completed={l:{refs[x['segment_id']] for x in p['coverage'] if x['layer']==l and x['extraction_state']=='completed'} for l in m.LAYERS};assert all(core<=v for v in completed.values())
iscore=lambda x:any(e.get('ref') in core for e in x['evidence'])
cs=[x for x in r['findings'] if iscore(x)];assert len(cs)==50
mapping={f'c{i:02}':['yev001.'+t] for i,t in enumerate(['exemption','exemption','exemption','permission','permission','permission','permission','exclude','exclude','firstcase'],1)}
mapping['c03']+=['yev001.secondcase','yev001.hundred']
n=1
for group,size in enumerate([4,5,4,2]):
 for k in range(size):mapping[f'list{group}_{k}']=[f'yev001.category{n}'];n+=1
names=['benazzai_stoning','judah_objection','judah_stoning','father_permission','father_permission','son_permission','son_permission','father_prohibition','father_prohibition','father_skirt','rape_adjacency','intervening','awaiting','awaiting','placement_alt','free_alt','tzitzit_placement','tzitzit_free','wearing_qualifies','both_needed','materials_free','all_garments','all_mixtures','same_shaatnez']
mapping.update({f'c{i:02}':['yev004.'+t] for i,t in enumerate(names,15)});mapping['c34']+=['yev004.wearing_only'];mapping['c39']=['yev005.blue_wool']
recordhash=lambda x:hashlib.sha256(m.encoded(x)).hexdigest()
rows=[]
for x in cs:
 ts=mapping[x['id']];zs=[by[t] for t in ts];assert all(z['release_state']=='valid' for z in zs)
 rows.append(dict(reader_id=x['id'],reader_record_sha256=recordhash(x),reader=x,producer=[dict(record=z,sha256=recordhash(z)) for z in zs],positions=[z for z in active if z['layer']=='positions' and z['content']['claim_id'] in ts],result='meaning_in_question_not_separate_claim' if x['id']=='c16' else 'source_meaning_present_with_atomicity_caveats'))
qmap={'q01':['yev004.outside'],'q02':['yev004.deuteronomy'],'q03':[],'q04':['yev004.rape_context'],'q05':['yev004.why_deut'],'q06':['yev005.school_need'],'q07':['yev005.sages_source']}
questions=[dict(reader=x,cohort='core' if iscore(x) else 'context',producer=[by[t] for t in qmap[x['id']]],result='explicit_question_node_missing; explanation survives in father_skirt claim' if x['id']=='q03' else 'same question, partial answer-set status preserved') for x in r['questions']]
enames=[['judah_obj'],['alternative_derivation'],['outside_answer'],['judah_basis'],['rape_ans'],['sages_obj'],['sages_interpretation'],['placement_ans'],['free_ans'],['needwear','two_needed'],['needbring','two_needed'],['new_free'],['mixture_obj'],['same_answer']]
core_edges=[x for x in r['relations'] if iscore(x)];assert len(core_edges)==len(enames)==14
edges=[dict(reader=x,producer=[by['yev004.'+t] for t in ts],assessment='Compare semantic role and scope; shared correction edge and reader continuation caveats below.') for x,ts in zip(core_edges,enames)]
def issue(i,cat,ids,txt,change):return dict(id=i,category=cat,severity='targeted',resolution='open; original versions preserved',records=[dict(id=t,sha256=recordhash(by[t])) for t in ids],finding=txt,required_change=change,regression_check='Re-read source and new records/dependencies; no inherited qualification.')
issues=[
 issue('YV-ATOMIC','atomic_representation',['yev001.exemption','yev001.permission','yev001.exclude','yev004.father_permission','yev004.son_permission','yev004.father_prohibition','yev004.awaiting','yev004.judah_objection'],'Core findings preserve substantive content but multiple separately conditioned outcomes share claim nodes. Halitzah/yibum/recursive exemption, four release cases, two exception classes, raped/seduced cases and awaiting-yibum/two prohibitions are bundled. c16 rejection appears only as a rhetorical question. No source meaning is wholly absent; do not count 50 reader matches as 50 atomic claims.','Split outcomes or explicitly document allowed granularity. Add source-anchored rhetorical rejection claim if atomic assertion coverage requires it, preserving original question and quoted attribution.'),
 issue('YV-QUESTION','explicit_question_omission',['yev004.father_skirt','yev004.judah_basis'],'Reader q03 identifies explicit מ״ט דרבי יהודה at 4a:9. No active question represents this question; the explanation and support edge survive. This is a typed question omission within a completed sampled core.','Add the explicit question and answer edge through new immutable records; preserve Rav as explaining Rabbi Judah via Rav Giddel, not independently choosing the ruling.'),
 issue('YV-DERIVATION-SCOPE','argument_relation_scope',['yev004.alternative_derivation','yev004.judah_stoning','yev004.benazzai_stoning'],'The correction edge from Rabbi Judah to Ben Azzai can imply replacement of Ben Azzai’s position. Both retain stoning; Rabbi Judah rejects adjacency as its basis and offers his own derivation. Reader c17->c15 repeats this ambiguity.','Scope the relation as competing derivations, not a retraction or contrary penalty. Preserve Ben Azzai’s view as maintained by him; revise relation/endpoint representation as appropriate.')]
reader_errors=[
 'c17->c15 correction shares the producer ambiguity: Rabbi Judah disputes the derivation, not the stoning outcome. The answer-set note correctly recognizes this and must govern interpretation.',
 'c27->c26 continuation is natural-language discourse succession, but production continuation is reserved for structure-to-structure links. Producer instead links the alternative interpretation to father_skirt; absence of a claim continuation edge is not a production error.',
 'c05/c07 reuse a death/divorce chronology condition that does not determine miun/aylonit timing. Reader uncertainty preserves this; do not generalize that condition to all four exceptions.',
 'c18–c23 encode the father/son and rape/seduction case conditions in prose while operative_conditions are empty. Therefore the  condition-array denominator understates source-conditioned claims and cannot be treated as condition recall.',
 'c03 combines several source occurrences (opening, example and hundred continuation). Count as one reader finding with multiple occurrence anchors, not one unique topic per producer match.',
 'Reader omits explicit כיצד question at 2b:5, secondary material question at 4b:10, and repeated school garment claim at 4b:10. Producer q.how, blue_material, school_garments preserve these; reader list is not exhaustive.',
 'c34 summarizes the result of mutual textual necessity. Producer both_needed plus wearing_only supplies the result/premise combination; treating wearing_only alone as a maintained permission would misread its hypothetical status.',
 'c24 holder Rav is explanation attribution only, as the reader condition states. Producer giddel transmitter and rav quoted authority are correct; no Rav–Shmuel dispute or adoption of Rabbi Judah inferred.'
]
coreqs=[x for x in r['questions'] if iscore(x)]
den=dict(independently_found_atomic_claims=len(cs),attributable_claims=len(cs),named_or_named_collective_holder_claims=sum(not x['holder_candidates'][0].startswith('anonymous') for x in cs),condition_bearing_claims=sum(bool(x['operative_conditions']) for x in cs),questions=len(coreqs),proposed_answer_sets=len(coreqs),supported_edges=len(core_edges),definitions=dict(attributable='Includes anonymous voices; named/named collective subset separate.',conditions='Nonempty reader operative_conditions arrays; known prose conditions are separately noted, so not source condition recall.',edges='Relation evidence intersects core; context-only links excluded.',unit='Reader finding occurrences including separately split list membership; not unique topics.'))
bindings=dict(r['bindings']);bindings.update(initial_reading=bind(rp),snapshot=bind(pp),runner=bind(runner),run_contract=bind(C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),contract_production_commit='15bba19d80273232b4554dfe507ceb37e97843a2',proposals=[bind(J/'proposals'/f'{ph}.json') for ph in p['proposals']],comparison_script=bind(__file__))
cohorts=dict(endpoint_core_segments=10,probability_core_segments=20,overlap_core_segments=0,unique_core_segments=30,context_only_segments=55)
targets={t for v in mapping.values() for t in v};claims={t for t in targets if by[t]['layer']=='claims'}
out=dict(artifact_kind='nonblind_exact_version_partial_comparison',comparator_provenance=dict(agent_id='/root/compare_zevachim_wave2',blind=False,reader_frozen_before_comparison=True),bindings=bindings,denominators=den,cohorts=cohorts,core_refs=r['core_refs'],context_refs_not_in_denominator=r['context_refs'],claim_comparisons=rows,question_comparisons=questions,answer_sets=r['answer_sets'],edge_comparisons=edges,producer_issues=issues,reader_corrections=reader_errors,uncertainties_preserved=r['uncertainties'],qa=dict(reader_evidence_slices=rn,producer_evidence_slices=pn,all_slices_match_original_source=True,replay=dict(read_only=True,method='load/empty/validate_apply for exact frozen proposal list; no current/lock/submit/write',replay_pass=True,snapshot_sha256=H,proposal_count=len(p['proposals']),report=report)),source_omission_pass=dict(scope='All 30 cores producer-completed in every layer',wholly_absent_reader_core_claim_meanings=0,reader_claims_only_in_questions=1,missing_explicit_reader_core_questions=1,distinct_producer_claim_counterparts=len(claims),atomic_completeness_pass=False),context_checks=dict(opening='2b:7 chronology and 2b:8 unexercised-refusal distinction preserved by chronology and unexercised_refusal.',tzitzit='4b:11–14 full Rava formulation, school objection, limited hypothetical inference and cross-material answer preserved. No final adoption of all Rava by school inferred.',limits='Context checked for scope and continuation; no exhaustive context-layer claim or whole-tractate halachic conclusion.'),limits=['Initial independent reading and production snapshot immutable.','No numeric precision/recall from counterpart mapping; granularity and reader omissions remain.','All task eligibility remains false; no full admission.'],human_certification=False,ml_eligible=False)
cp=B/'comparisons/yevamot_batch001_exact_version.json';assert not cp.exists();cp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
v=dict(verdict='REWORK_TARGETED',bindings=bindings,comparison=bind(cp),scope='30 unique cores, 10 opening and 20 probability; 55 context segments do not inflate denominator',required_changes=issues,task_eligibility={k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},layer_matrix=dict(**cohorts,independent_core_denominators=den,producer_completed_per_layer=report['completed_by_layer'],producer_completed_sampled_cores_per_layer={k:len(core&z) for k,z in completed.items()},source_segments_total=report['source_segments']),tractate_accepted=False,full_review_receipt=False,human_certification=False,admission_owner='global coordinator',remaining='Owner may produce new revisions for exact-version recheck; continue source-only reading at block_000019, Yevamot 9a:6–15. No inheritance to newer snapshots.')
vp=B/'verdicts/yevamot_batch001_v2_verdict.json';assert not vp.exists();vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(comparison=bind(cp),verdict=bind(vp),denominators=den,source_omission_pass=out['source_omission_pass'],reader_slices=rn,producer_slices=pn,replay_proposals=len(p['proposals']),completed=report['completed_by_layer']),ensure_ascii=False))
