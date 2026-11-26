import json,hashlib,importlib.util,sys
from pathlib import Path
B=Path(__file__).resolve().parent.parent;C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study');J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
H='4ce45b2ad3cccff73f11ce5fd4a2a59b41550959f029b587d33e20f22c42c042';RH='54b0d0919bbfd68d73e0a407a7764102958a157f9f45382a96c12a01dc642c4e'
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();bind=lambda p:dict(path=str(Path(p).resolve()),sha256=h(p));read=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
rp=B/'readings/eruvin_batch001.json';pp=J/'snapshots'/f'{H}.json';assert h(rp)==RH and h(pp)==H;r=read(rp);p=read(pp);runner=C/'research/bavli_production_v1/runner.py';sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('ereview_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);j,segs=m.load(J);texts={x['ref']:x['text'] for x in segs.values()};refs={k:v['ref'] for k,v in segs.items()}
def vb(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:assert h(x['path'])==x['sha256']
  for v in x.values():vb(v)
 elif isinstance(x,list):
  for v in x:vb(v)
vb(r['bindings']);state=m.empty()
for ph in p['proposals']:
 f=J/'proposals'/f'{ph}.json';assert h(f)==ph;prev=state['proposals'];state=m.validate_apply(state,read(f),segs,j);state['proposals']=prev+[ph]
assert m.encoded(state)==m.encoded(p) and m.sha(m.encoded(state))==H;report=m.report(state,segs)
def check(x):
 n=0
 if isinstance(x,dict):
  if all(k in x for k in ['quote','start_char','end_char']):
   t=texts[x['ref']] if 'ref' in x else segs[x['segment_id']]['text'];assert t[x['start_char']:x['end_char']]==x['quote'];n+=1
  for v in x.values():n+=check(v)
 elif isinstance(x,list):
  for v in x:n+=check(v)
 return n
rn=check(r);pn=check(p);by={x['id']:x for x in p['records']};active=[x for x in p['records'] if x['release_state']=='valid'];allcore=set(r['core_refs'])
completed={l:{refs[x['segment_id']] for x in p['coverage'] if x['layer']==l and x['extraction_state']=='completed'} for l in m.LAYERS};core=set.intersection(allcore,*completed.values());assert len(core)==10
iscore=lambda x:any(e['ref'] in core for e in x['evidence']);cs=[x for x in r['findings'] if iscore(x)];assert len(cs)==15
maps=[['er.opening.001.'+t] for t in ['height.reduce','height.yehuda','width.reduce','width.form','sukkah.invalid','sukkah.yehuda','answer.legal.level']]
maps += [['er.opening.001.alternative.'+t for t in ['torah','many','few']]]
maps += [['er.derivation.002.claims.'+t] for t in ['rav.rabbis','rav.yehuda','dimensions.heikhal','dimensions.ulam']]
maps += [['er.derivation.002.claims.'+t for t in ts] for ts in [['rabbis.sanctity','rabbis.verse'],['yehuda.sanctity','yehuda.verse'],['alternative.sanctity','alternative.verse']]]
recordhash=lambda x:hashlib.sha256(m.encoded(x)).hexdigest();rows=[]
for x,ts in zip(cs,maps):
 assert all(by[t]['release_state']=='valid' for t in ts)
 rows.append(dict(reader=x,reader_record_sha256=recordhash(x),producer=[dict(record=by[t],sha256=recordhash(by[t])) for t in ts],positions=[z for z in active if z['layer']=='positions' and z['content']['claim_id'] in ts],assessment='Meaning present; producer often splits reader composite reasoning more finely.'))
coreqs=[x for x in r['questions'] if iscore(x)];assert len(coreqs)==2
questions=[dict(reader=coreqs[0],producer=[by['er.opening.001.q.wording']],assessment='Same explicit question; two anonymous answers preserved.'),dict(reader=coreqs[1],producer=[],related_claims=[by['er.derivation.002.claims.rav.rabbis'],by['er.derivation.002.claims.rav.yehuda']],assessment='Reader editorial reconstructed question. No matching explicit producer question is required or scored as an omission.')]
context_edges=[x for x in r['relations'] if (x['source_id'],x['target_id']) in [('c25','c10'),('c27','c04')]]
edge_rows=[dict(reader=context_edges[0],cohort='context_correction_of_opening',producer=[by['er.objections.001.edges.hisda.challenge']],assessment='Correction present; Rav reported view preserved, no self-retraction asserted.'),dict(reader=context_edges[1],cohort='context_correction_of_opening',producer=[by['er.objections.001.edges.form.answer']],assessment='Textual correction exists but answer points to local objection question, not opening exception. See targeted dependency issue.')]
issue=dict(id='ER-WIDTH-CONTEXT',category='cross_context_status_link',severity='targeted',resolution='open; originals immutable',records=[dict(id=t,sha256=recordhash(by[t])) for t in ['er.opening.001.width.form','er.opening.001.p.width.form','er.objections.001.claims.form.rav.correction','er.objections.001.edges.form.answer']],finding='Rav’s contrary reading at 2b:15 is preserved accurately as a correction, but the opening doorway-form exception and its position have only stated in this local text status and no link to that correction. The answer edge targets the doorway objection question. An opening/position-only extraction therefore loses the conflicting textual reading.',required_change='Link the reported textual correction to the precise opening reading and qualify dependent position retrieval. Preserve printed Mishnah and Rav’s alternative reading as distinct evidence; do not overwrite either or claim a universal settled ruling.',regression_check='Retrieving opening width.form or its position surfaces both printed exemption and Rav’s correction with distinct attribution, context and status.')
reader_errors=[
 'c01/c03/c05/c06 omit condition arrays although height/width conditions occur in prose. Producer conditions preserve these; the two nonempty reader arrays are not a condition-completeness denominator.',
 'c08 combines three propositions; c13/c14/c15 combine sanctity premises and verse interpretations. Producer separate claims are not hallucinations and reader fifteen is not an atomic gold standard.',
 'c09/c10 identify Rav as explaining the views, not as independently ruling with either side. Producer distinguishes Rav Yehuda transmitter, Rav origin, Sages and Rabbi Yehuda holders.',
 'q02 is explicitly editorial reconstruction. Missing an identical producer question is not an explicit-source omission.',
 'c25 labels Rav misled; this is Rav Hisda’s statement, not an independently established historical fact or recorded Rav retraction. Producer attribution/status is more precise.',
 'Reader c27 shorthand tells Rav Yehuda omits Hiyya bar Rav as recipient in the quoted narrative; producer retains Hiyya and distinguishes instruction from reported authority.',
 'No reader relation uses opening-core evidence. This is reader graph sparsity: producer explicitly records q01 answers, width qualification and derivational support. Zero reader core edges cannot establish edge completeness.'
]
pending=[x for x in r['core_refs'] if x not in core];pendingclaims=[x for x in r['findings'] if any(e['ref'] in set(pending) for e in x['evidence'])]
den=dict(independently_found_claims=15,attributable_claims=15,named_or_named_collective_holder_claims=7,condition_bearing_claims=sum(bool(x['conditions']) for x in cs),questions=2,explicit_questions=1,editorial_reconstructed_questions=1,proposed_answer_sets=2,supported_core_evidence_edges=0,context_correction_edges_to_core=2,definitions=dict(claims='Reader labeled atomic findings; several composite findings split more finely by producer.',conditions='Nonempty reader arrays only; source conditions embedded in prose separately noted.',unit='Source findings/occurrences, not unique topics.'))
bindings=dict(r['bindings']);bindings.update(initial_reading=bind(rp),snapshot=bind(pp),job_descriptor=bind(B/'jobs/bavli_eruvin.json'),runner=bind(runner),run_contract=bind(C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),contract_production_commit='15bba19d80273232b4554dfe507ceb37e97843a2',proposals=[bind(J/'proposals'/f'{ph}.json') for ph in p['proposals']],comparison_script=bind(__file__))
cohorts=dict(reader_endpoint_core_segments=10,reader_probability_core_segments=20,endpoint_core_segments_compared=10,probability_core_segments_compared=0,overlap_core_segments=0,unique_core_segments_compared=10,producer_uncompleted_sampled_cores=20,context_segments_read_by_reader=66)
out=dict(artifact_kind='nonblind_exact_version_partial_comparison',comparator_provenance=dict(agent_id='/root/compare_zevachim_wave2',blind=False,reader_frozen_before_comparison=True),bindings=bindings,denominators=den,cohorts=cohorts,compared_core_refs=[x for x in r['core_refs'] if x in core],pending_core_refs_not_omissions=pending,pending_reader_claim_count=len(pendingclaims),pending_rule='No semantic omission score, error, or acceptance for 20 uncompleted probability cores at this version. Frozen source-only findings preserved for future exact-version comparison.',claim_comparisons=rows,question_comparisons=questions,answer_sets=[x for x in r['answer_sets'] if x['question_id'] in ['q01','q02']],edge_comparisons=edge_rows,producer_issues=[issue],reader_corrections=reader_errors,uncertainties_preserved=r['uncertainties'],qa=dict(reader_evidence_slices=rn,producer_evidence_slices=pn,all_slices_match_original_source=True,replay=dict(read_only=True,method='load/empty/validate_apply for exact frozen proposal chain; no current/lock/submit/write',replay_pass=True,snapshot_sha256=H,proposal_count=len(p['proposals']),report=report)),source_omission_pass=dict(scope='10 completed opening cores only',absent_reader_claim_meanings=0,distinct_producer_claim_counterparts=len({t for ts in maps for t in ts}),atomic_completeness_claim=False),context_checks=dict(royal_derivation='2b:11 correction attributed to Rav Hisda is represented and linked to initial Rav account.',doorway='2b:15 Rav instruction represented; dependency to opening exception requires targeted work.',limits='Remaining contextual findings selectively inspected, not exhaustively producer-compared. Later probability blocks are pending, not error samples.'),limits=['Original reading and producer snapshot immutable.','No whole-tractate acceptance or accuracy estimate.','Later source-only reads do not establish producer completion; no later-version inheritance.'],human_certification=False,ml_eligible=False)
cp=B/'comparisons/eruvin_batch001_exact_version.json';assert not cp.exists();cp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
v=dict(verdict='REWORK_TARGETED',bindings=bindings,comparison=bind(cp),scope='Only opening ten completed cores; twenty probability cores pending producer completion at this exact version',required_changes=[issue],task_eligibility={k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},layer_matrix=dict(**cohorts,independent_core_denominators=den,producer_completed_per_layer=report['completed_by_layer'],producer_completed_sampled_cores_per_layer={k:len(allcore&z) for k,z in completed.items()},source_segments_total=report['source_segments']),tractate_accepted=False,full_review_receipt=False,human_certification=False,admission_owner='global coordinator',remaining='Review new exact producer snapshot when probability cores complete; source-only reading can resume at block_000020 Eruvin 8a:14–8b:3. Recheck any changed opening records.')
vp=B/'verdicts/eruvin_batch001_v2_verdict.json';assert not vp.exists();vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(comparison=bind(cp),verdict=bind(vp),denominators=den,pending_claims=len(pendingclaims),reader_slices=rn,producer_slices=pn,proposals=len(p['proposals']),completed=report['completed_by_layer']),ensure_ascii=False))
