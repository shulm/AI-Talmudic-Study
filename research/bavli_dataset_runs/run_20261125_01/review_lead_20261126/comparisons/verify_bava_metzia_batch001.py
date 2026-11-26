"""Exact candidate read-only replay, source QA, and manually adjudicated mappings."""
import sys
sys.dont_write_bytecode=True
import json, hashlib, importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L02/bavli_bava_metzia')
SNAP='25ffca05e9a6f9445ac1f1b285f70d8e113e962353c02e0e108ce4aa2d5e5990'
READ='a5ebe400aafc2e27d6bc065e381899570ed1eea21fb9ed6f3c981508203d2e35'
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
def bind(p):return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}
def publish(p,x):
    raw=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():assert p.read_bytes()==raw
    else:
        with p.open('xb') as f:f.write(raw)
    return bind(p)
rp=BASE/'readings/bava_metzia_batch001.json'
assert sha(rp.read_bytes())==READ
reading=json.loads(rp.read_bytes())
sp=JOB/'snapshots'/f'{SNAP}.json'
assert sha(sp.read_bytes())==SNAP
state=json.loads(sp.read_bytes())
contractp=REPO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
contract=json.loads(contractp.read_bytes())
pointer=json.loads((REPO/'research/bavli_dataset_runs/ACTIVE_RUN.json').read_bytes())
assert sha(contractp.read_bytes())==pointer['contract_sha256']
runnerp=REPO/'research/bavli_production_v1/runner.py'
assert sha(runnerp.read_bytes())==contract['production_files']['research/bavli_production_v1/runner.py']
spec=importlib.util.spec_from_file_location('pinned_runner_readonly',runnerp)
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
j,segments=runner.load(JOB)
replayed=runner.empty();proposals=[]
for h in state['proposals']:
    pp=JOB/'proposals'/f'{h}.json';assert sha(pp.read_bytes())==h
    replayed=runner.validate_apply(replayed,json.loads(pp.read_bytes()),segments,j)
    replayed['proposals'].append(h);proposals.append(bind(pp))
assert replayed==state and sha(runner.encoded(replayed))==SNAP
byref={v['ref']:v for v in segments.values()}
records={r['id']:r for r in state['records']}
active={k:r for k,r in records.items() if r['release_state']=='valid'}
checks={'reading_evidence_slices':0,'producer_evidence_slices':0}
def evidencewalk(obj):
    if isinstance(obj,dict):
        if {'ref','start_char','end_char','quote'}<=obj.keys():
            t=byref[obj['ref']]['text'];a,b=obj['start_char'],obj['end_char']
            assert 0<=a<b<=len(t) and t[a:b]==obj['quote'];checks['reading_evidence_slices']+=1
        for v in obj.values():evidencewalk(v)
    elif isinstance(obj,list):
        for v in obj:evidencewalk(v)
evidencewalk(reading)
for rec in records.values():
    for e in rec['evidence']:
        t=segments[e['segment_id']]['text'];a,b=e['start_char'],e['end_char']
        assert 0<=a<b<=len(t) and t[a:b]==e['quote'];checks['producer_evidence_slices']+=1
completed={layer:{c['segment_id'] for c in state['coverage'] if c['layer']==layer and c['extraction_state']=='completed'} for layer in runner.LAYERS}
allcompleted=set.intersection(*completed.values())
overlap=[ref for ref in reading['core_refs'] if byref[ref]['id'] in allcompleted]
unprocessed=[ref for ref in reading['core_refs'] if ref not in overlap]
assert len(overlap)==10 and len(unprocessed)==10 and all(len(v)==47 for v in completed.values())
findings={x['id']:x for x in reading['findings']}
relations={x['id']:x for x in reading['directed_relations']}
G='bm.gemara001.opening.';M='bm.opening.'
cm={'c01':[M+'claims.19',M+'claims.23'],'c02':[M+'claims.27'],
 'c03':[M+'claims.41'],'c04':[M+'claims.45'],'c05':[M+'claims.49'],'c06':[M+'claims.54'],
 'c07':[M+'claims.67',M+'claims.71'],'c08':[M+'claims.75'],'c09':[M+'claims.81'],
 'c10':[G+'claims.3'],'c11':[G+'claims.17'],'c12':[G+'claims.24'],
 'c13':[G+'claims.30',G+'claims.35'],'c14':[G+'claims.44'],'c15':[G+'claims.54']}
qm={f'q{i:02}':[G+'questions.'+str(n)] for i,n in enumerate([1,7,22,48,59],1)}
em={'e01':[G+'edges.6'],'e02':[G+'edges.20'],'e03':[G+'edges.27',G+'edges.28'],
 'e04':[G+'edges.33',G+'edges.38'],'e05':[G+'edges.57'],'e06':[G+'edges.64']}
mappings=[];used=set()
for kind,lookup,originals in [('claims',cm,findings),('questions',qm,findings),('directed_relations',em,relations)]:
    for fid,rids in lookup.items():
        related=list(rids)
        related += [r['id'] for r in active.values() if r['layer']=='positions' and r['content']['claim_id'] in rids]
        related += [r['id'] for r in active.values() if r['layer']=='attributions' and r['content']['scope'] in rids]
        status='SUPPORTED_CONTENT_REPRESENTED'
        note='Checked source assertion, conditions, holder, status and relation. Anonymous Mishnah/dialectic is not assigned to a named amora.'
        if fid in ['c01','c07','c13']:
            status='GRANULARITY_DIFFERENCE_CONTENT_PRESERVED'
            note='Reader combines propositions which producer separates; all components are represented.'
        if fid in ['c02','c05','c06','c08']:
            status='READER_CONDITION_REFINEMENT'
            note='Producer explicitly includes the specified oath as condition of allocation. Reader allocation atoms omit it although companion oath findings and source evidence retain it. Preserve initial reading and qualify these reader atoms before standalone use.'
        if fid in ['c14','c15']:
            status='PRODUCER_PROVISIONAL_SCOPE_UNDERSPECIFIED'
            note='The sight-acquisition rule is not rejected. This particular account of why the wording is redundant belongs to the combined-clause analysis displaced at 2a:10–11. Producer records an unconditional asserted wording explanation with empty conditions; generic provisional AI status does not preserve this specific dialectical dependence.'
        if fid=='e03':
            status='READER_RELATION_TARGET_ERROR_PRODUCER_MORE_PRECISE'
            note='Ravnai supplies support for the objection to interpreting found as saw; it does not object to nonacquisition by sight itself. Producer support-to-question then objection-to-claims.9 correctly separates that premise. Do not add the reader edge to producer.'
            related += [G+'claims.9',G+'claims.17',G+'questions.22']
        if fid=='e06':
            status='REPRESENTATIONAL_DIFFERENCE_NOT_OMISSION'
            note='Reader uses interrogative q05 as objection source; producer preserves q05 as questions.59 and uses its explicit premise claims.61 as objection source. Both oppose combined-clause claims.3.'
            related += [G+'claims.61',G+'questions.59']
        related=sorted(set(related));assert all(rid in active for rid in related);used.update(related)
        mappings.append({'independent_kind':kind,'independent_id':fid,'initial_reading':originals[fid],
                         'producer_record_ids':related,'producer_record_hashes':{rid:sha(enc(records[rid])) for rid in related},
                         'status':status,'assessment':note})
context_ids=[G+'claims.66.reviewfix1',G+'claims.70.reviewfix1',G+'attributions.67.reviewfix1',G+'attributions.71.reviewfix1',G+'positions.68.reviewfix1',G+'positions.72.reviewfix1',G+'edges.74.reviewfix1',G+'edges.75.reviewfix1',G+'edges.76.reviewfix1']
assert all(rid in active for rid in context_ids);used.update(context_ids)
answer_sets=[]
for item in reading['proposed_answer_sets'][:4]:
    rids=[]
    for fid in item['members']:
        rids+=cm.get(fid,context_ids if fid=='x01' else [])
    answer_sets.append({'initial_answer_set':item,'producer_record_ids':rids,
      'assessment':'Alternatives preserved as successive explanations, not enduring opposed named positions. The replacement answer is attached to the more specific wording challenge and corrects the combined-clause claim.' if item['id']=='a1' else 'Local question/answer content represented; provisional-scope issue separately recorded for c15.' if item['id']=='a4' else 'Local question/answer content represented.'})
discrepancies=[{'id':'BM001-SCOPE','side':'producer','category':'dialectical_condition_underrepresentation','severity':'moderate_local',
 'resolution_state':'OPEN_TARGETED_REWORK','independent_ids':['c14','c15'],
 'producer_record_ids':[G+'claims.44',G+'positions.46',G+'claims.54',G+'positions.56'],
 'evidence':findings['c14']['evidence']+findings['c15']['evidence']+findings['q05']['evidence']+findings['x01']['evidence'],
 'finding':'Two wording-explanation claims lack the specific combined-clause hypothesis scope, while their argument is displaced by the separate finding/purchase explanation. The general nonacquisition-by-sight rule is not thereby rejected.',
 'required_change':'Supersede the affected claims and positions with explicit wording-analysis scope/condition under the combined-clause hypothesis, or equivalent explicit uncertainty/local-status wording that identifies this dependency. Preserve the nonacquisition rule separately; do not mark it rejected. Repoint affected links through authorized producer correction, preserving immutable originals.',
 'regression_check':'Verify exported claim/position alone cannot be mistaken for the final explanation of the repeated Mishnah wording; preserve c3 rejection and alternative attribution at 2a:11; validate new exact candidate and replay.',
 'blast_radius':'These local wording-analysis claims and dependent QA/argument views only; no shared corpus or attribution failure found.'},
 {'id':'BM001-READER-E03','side':'independent_reader','category':'argument_target_error','severity':'moderate_local',
 'resolution_state':'ADJUDICATED_READER_REFINEMENT_REQUIRED','independent_ids':['e03','c11'],
 'evidence':relations['e03']['evidence'],'finding':'Reader edge objects to c11, which asserts sight nonacquisition. The source objection instead targets the proposed lexical premise found means saw. Producer preserves the proper premise as claims.9 and targets it via questions.22.',
 'required_change':'Keep frozen reader file unchanged. A superseding reader adjudication should target a separately preserved hypothetical lexical premise, using Ravnai claim as support for that objection, rather than treating nonacquisition as refuted.'},
 {'id':'BM001-READER-OATH','side':'independent_reader','category':'allocation_condition_underrepresentation','severity':'minor_local',
 'resolution_state':'ADJUDICATED_READER_REFINEMENT_REQUIRED','independent_ids':['c02','c05','c06','c08'],
 'evidence':sum([findings[fid]['evidence'] for fid in ['c02','c05','c06','c08']],[]),
 'finding':'Independent allocation atoms omit the oath condition supplied by source and companion findings; producer conditions explicitly retain it.',
 'required_change':'Preserve original reading and record oath dependence in a superseding reader refinement before isolated claim use.'}]
planp=BASE/'frozen_plans/bavli_bava_metzia.json'
assert sha(planp.read_bytes())==reading['plan_file_sha256']
sourcep=Path(json.loads((BASE/'jobs/bavli_bava_metzia.json').read_bytes())['source']['path'])
assert sha(sourcep.read_bytes())==reading['source_sha256']==j['source_sha256']
bindings={'initial_reading':bind(rp),'snapshot':bind(sp),'run_contract':bind(contractp),
 'schema':bind(REPO/'research/bavli_production_v1/schema.json'),'protocol':bind(REPO/'research/bavli_production_v1/PROTOCOL.md'),
 'source':bind(sourcep),'plan':bind(planp),'plan_embedded_sha256':reading['plan_sha256'],
 'runner':bind(runnerp),'comparison_script':bind(Path(__file__)),'proposals':proposals,
 'contract_production_commit':contract['production_git_commit']}
for k in ['schema','protocol']:assert bindings[k]['sha256']==j[k+'_sha256']
scope={'source_segments_total':len(segments),'producer_completed_per_layer':{k:len(v) for k,v in completed.items()},
 'compared_completed_core_refs':overlap,'unprocessed_independent_core_refs':unprocessed,
 'independent_core_claim_denominator':15,'attributable_claim_denominator':10,'condition_bearing_claim_denominator':11,
 'questions_denominator':5,'proposed_answer_set_denominator':4,'directed_relation_denominator':6,
 'represented_core_claim_contents':15,'probability_core_segments_compared':0,'endpoint_core_segments_compared':10,
 'context_comparison':'2a:11 replacement explanation only, to resolve opening scope and answer set; no context counted as sampled core.',
 'full_tractate_review_complete':False}
eligibility={k:False for k in ['retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice','ml']}
artifact={'artifact_kind':'independent_ai_exact_candidate_partial_comparison',
 'execution':{'agent_id':'/root/prepare_review','route':'interactive_agent','role':'nonblind_comparison_auditor'},
 'bindings':bindings,'scope':scope,'source_first_reading_hash_verified_before_producer_access':True,
 'initial_reading_unchanged':sha(rp.read_bytes())==READ,'omission_pass_performed':True,
 'mappings':mappings,'answer_set_mappings':answer_sets,'discrepancies':discrepancies,
 'producer_record_hash_contract':'SHA256 UTF-8 sorted-key compact JSON, ensure_ascii=false, followed by one LF; runner encoded(record).',
 'mapped_producer_records':{rid:records[rid] for rid in sorted(used)},
 'mapped_producer_record_hashes':{rid:sha(enc(records[rid])) for rid in sorted(used)},
 'mechanical_checks':{**checks,'exact_candidate_in_memory_replay_pass':True,'replayed_snapshot_sha256':SNAP,
 'active_records':len(active),'all_preserved_records':len(records),'read_only_replay':'runner.load and validate_apply only; no lock, CURRENT selection, or external writes',
 'source_schema_protocol_pins_pass':True},
 'confirmed_missing_claim_contents':0,'confirmed_false_attributions_in_compared_cores':0,
 'interpretation_limits':['Only opening endpoint cores overlap production; no representative sample accuracy is available.',
 '11a:12–21 remains unprocessed and is excluded from omission denominator.',
 'Producer provisional scope issue and reader mistakes are distinct; no adjudication overwrites either initial judgment.',
 'No full risk-record review, exported-view audit, or full-tractate admission.'],
 'human_certification':False,'task_eligibility':eligibility}
cp=publish(BASE/'comparisons/bava_metzia_batch001.json',artifact)
verdict={'verdict':'REWORK_TARGETED','scope':'Exact candidate snapshot; partial independent comparison, not full tractate admission.',
 'bindings':bindings,'comparison':cp,'layer_matrix':scope,'required_changes':discrepancies,
 'confirmed_false_attributions_in_compared_cores':0,'confirmed_missing_claim_contents':0,
 'producer_issue_groups':1,'reader_issue_groups':2,'unresolved_integrity_critical_count':0,
 'full_review_receipt':False,'tractate_accepted':False,'admission_owner':'global coordinator',
 'later_than_integrated004':True,'human_certification':False,'task_eligibility':eligibility,
 'remaining':'Apply specific dialectical scope clarification through producer owner; preserve initial reader and record its refinements separately. Recompare changed exact candidate. Complete remaining production, sampled/endpoint/risk reviews before full review.'}
vp=publish(BASE/'verdicts/bava_metzia_batch001.json',verdict)
print(json.dumps({'comparison':cp,'verdict':vp,'scope':scope,'checks':checks}))
