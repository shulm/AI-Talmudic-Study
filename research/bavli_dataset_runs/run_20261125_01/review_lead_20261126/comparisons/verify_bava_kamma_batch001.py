"""Reproduce mechanical checks and preserve manually adjudicated mappings.
Read-only candidate replay; never calls runner.replay(), whose lock writes.
"""
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
REPO = Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
JOB = Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L06/bavli_bava_kamma')
SNAP = '89aab343c9b6bb4c302a7a18094c6f1ee229c8b78e77fa8828d5a84d34985ff9'
READ = '7dd63968fa17b405b50d6fa1490504eb96f2dd88aaf8e3e0832ab3041def977d'
def sha(b): return hashlib.sha256(b).hexdigest()
def enc(x): return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',', ':'))+'\n').encode()
def bind(p): return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}
def publish(p,x):
    raw=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists(): assert p.read_bytes()==raw, 'Immutable artifact mismatch'
    else:
        with p.open('xb') as f:f.write(raw)
    return bind(p)
rp=BASE/'readings/bava_kamma_batch001.json'
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
    pp=JOB/'proposals'/f'{h}.json'
    assert sha(pp.read_bytes())==h
    proposal=json.loads(pp.read_bytes())
    replayed=runner.validate_apply(replayed,proposal,segments,j)
    replayed['proposals'].append(h)
    proposals.append(bind(pp))
assert replayed==state and sha(runner.encoded(replayed))==SNAP
byref={v['ref']:v for v in segments.values()}
records={r['id']:r for r in state['records']}
checks={'reading_evidence_slices':0,'producer_evidence_slices':0}
def evidencewalk(obj):
    if isinstance(obj,dict):
        if {'ref','start_char','end_char','quote'}<=obj.keys():
            t=byref[obj['ref']]['text'];a,b=obj['start_char'],obj['end_char']
            assert 0<=a<b<=len(t) and t[a:b]==obj['quote'];checks['reading_evidence_slices']+=1
        for v in obj.values(): evidencewalk(v)
    elif isinstance(obj,list):
        for v in obj:evidencewalk(v)
evidencewalk(reading)
for rec in records.values():
    for e in rec['evidence']:
        t=segments[e['segment_id']]['text'];a,b=e['start_char'],e['end_char']
        assert 0<=a<b<=len(t) and t[a:b]==e['quote'];checks['producer_evidence_slices']+=1
completed={layer:{c['segment_id'] for c in state['coverage'] if c['layer']==layer and c['extraction_state']=='completed'} for layer in runner.LAYERS}
allcompleted=set.intersection(*completed.values())
core=reading['core_refs'];overlap=[ref for ref in core if byref[ref]['id'] in allcompleted]
unprocessed=[ref for ref in core if ref not in overlap]
assert len(overlap)==18 and len(unprocessed)==12
cm={}
groups={'bk01_c_four':[1],'bk01_c_shor_mave':[2],'bk01_c_mave_shor':[3],
 'bk01_c_life':[4,5],'bk01_c_motion':[6,7],'bk01_c_guard':[8,9],'bk01_c_pay':[10,11],
 'bk01_c_exist':[12],'bk01_c_39':[13],'bk01_c_shab_der':[14],
 'bk01_c_sin':[15,16],'bk01_c_stone':[17,18],'bk01_c_two_av':[19],
 'bk01_c_two_tol':[20],'bk01_c_same':[21],'bk01_c_eliezer':[22],
 'bk01_c_mishkan':[23,24],'bk01_c_impav':[25,26],'bk02_c_mazal':[27,28],
 'bk02_c_humanmuad':[29],'bk02_c_animalmuad':[30],'bk02_q_bite':[31],
 'bk02_c_toothbenefit':[32],'bk02_c_bitebenefit':[33],'bk02_q_restkick':[34,35],
 'bk02_c_footfrequency':[36],'bk02_c_restkickfrequency':[37],'bk01_c_pappa':[38],
 'bk02_c_common':[39,40,41,42,43,44],'bk02_c_hornequal':[45],'bk02_c_pappatoothfoot':[46]}
for rid,nums in groups.items():
    for n in nums:cm[f'c{n:02}']=rid
qm=dict(zip([f'q{i:02}' for i in range(1,8)],['bk01_q_equiv','bk01_q_shab_diff','bk01_q_eliezer','bk02_q_vocabulary','bk02_q_bite','bk02_q_restkick','bk02_q_pappa']))
em=dict(zip([f'e{i:02}' for i in range(2,17)],['bk01_e_two','bk01_e_twot','bk01_e_diff','bk01_e_mishkan','bk01_e_mishkan','bk02_e_mazal','bk02_e_mazal','bk02_e_biteanswer','bk02_e_restanswer','bk02_e_restanswer','bk02_e_hornequality','bk02_e_hornequality','bk02_e_hornequality',None,'bk02_e_provisional']))
mappings=[];used=set()
for layer,items,lookup in [('claims',reading['claims'],cm),('questions',reading['questions'],qm),('argument_edges',reading['argument_edges'],em)]:
    for item in items:
        if item['id'] not in lookup:continue
        rid=lookup[item['id']];related=[]
        if rid:
            related=[rid]+[r['id'] for r in records.values() if r['layer']=='positions' and r['content']['claim_id']==rid]
            erefs={e['ref'] for e in item['evidence']}
            related += [r['id'] for r in records.values() if r['layer']=='attributions' and any(segments[e['segment_id']]['ref'] in erefs for e in r['evidence'])]
        status='SUPPORTED_CONTENT_REPRESENTED'
        note='Checked proposition, conditions, local status, holder and source evidence; no incompatible attribution or maintained conclusion found.'
        if item['id'] in ['c31','c34','c35','e09','e10','e11']:
            status='REPRESENTATIONAL_DIFFERENCE_NOT_OMISSION'
            note='Reader models rejected proposal plus objection; producer models the same challenge as a question with an answer edge and contrast. Rejection is preserved by the answer and source; no maintained alternative is invented.'
        elif item['id']=='c38':
            status='RECALL_LINKED_TO_EARLIER_CLAIM'
            related+=['bk02_a_pappa','bk02_q_pappa']
            note='Recalled Rav Pappa claim occurs at 2b:16 in attribution evidence linked to bk01_c_pappa; preserved occurrence and holder, not a new anonymous statement assigned to Rav Pappa.'
        elif item['id']=='e15':
            status='MISSING_TYPED_RELATION_IN_COMPLETED_EDGE_PASS'
            related=['bk02_c_hornequal','bk02_q_pappa','bk02_e_provisional','bk02_e_hornequality']
            note='Both conclusion and question exist, but no edge makes the horn-equality conclusion qualify the scope question by excluding horn from unequal derivatives. The provisional tooth/foot answer does not encode this distinct negative elimination.'
        elif item['id'] in ['c20','c23','c24']:
            note='Reader uncertainty is preserved in producer record uncertainty; no new resolution is asserted here.'
        elif item['id']=='c46':
            note='Producer marks hypothetical/provisional and leaves structure open. Later supersession is in unprocessed source, so absent continuation edges are not counted as omissions in this snapshot.'
        elif layer=='claims' and len(groups.get(rid,[]))>1:
            status='CONTENT_PRESERVED_COARSER_CLAIM_GRANULARITY'
            note='Multiple independent atomic propositions share this producer record. Source content is retained, but atomic downstream use requires finer splitting and fresh task qualification.'
        related=sorted(set(related));used.update(related)
        mappings.append({'independent_layer':layer,'independent_id':item['id'],'independent_reading':item,
                         'producer_record_ids':related,'status':status,'assessment':note})
for m in mappings:
    m['producer_record_hashes']={rid:sha(enc(records[rid])) for rid in m['producer_record_ids']}
e15=next(x for x in reading['argument_edges'] if x['id']=='e15')
discrepancy={'id':'BK001-E15','category':'argument_relation_omission','severity':'moderate_local',
 'resolution_state':'OPEN_TARGETED_REWORK','independent_id':'e15','refs':['Bava Kamma 2b:16','Bava Kamma 2b:18'],
 'evidence':e15['evidence'],'producer_record_ids':['bk02_c_hornequal','bk02_q_pappa'],
 'finding':'Missing typed qualification relation from horn-equality conclusion to Rav Pappa scope question in a completed edges/reconciliation segment.',
 'required_change':'Add a new source-evidenced qualification edge from bk02_c_hornequal to bk02_q_pappa (or a semantically equivalent explicit elimination relation allowed by schema). Preserve all old records, proposal hashes, and reader judgments; submit through authorized producer ownership and rerun exact-source and schema/replay validation.',
 'regression_check':'Verify the resulting candidate includes an active source-anchored edge encoding that horn derivatives are excluded from Rav Pappa unequal-derivative scope, without making provisional tooth/foot assignment final.',
 'blast_radius':'Local graph relation at 2b:18 and argument/QA views depending on that elimination. No evidence here of shared source, offset, schema, or named-attribution failure.'}
planp=BASE/'frozen_plans/bavli_bava_kamma.json'
assert sha(planp.read_bytes())==reading['plan_file_sha256']
assert j['source_sha256']==reading['source_sha256']
sourcep=Path(json.loads((BASE/'jobs/bavli_bava_kamma.json').read_bytes())['source']['path'])
assert sha(sourcep.read_bytes())==j['source_sha256']
scope={'source_segments_total':len(segments),'producer_completed_per_layer':{k:len(v) for k,v in completed.items()},
 'independent_core_refs':core,'compared_completed_core_refs':overlap,'unprocessed_independent_core_refs':unprocessed,
 'independent_core_claim_denominator':46,'questions_denominator':7,'argument_relations_denominator':15,
 'represented_core_claim_contents':46,'missing_typed_relations':1,
 'probability_core_segments_compared':8,'endpoint_core_segments_compared':10,
 'context_is_not_probability_sample':True,'full_tractate_review_complete':False}
bindings={'initial_reading':bind(rp),'snapshot':bind(sp),'run_contract':bind(contractp),
 'schema':bind(REPO/'research/bavli_production_v1/schema.json'),'protocol':bind(REPO/'research/bavli_production_v1/PROTOCOL.md'),
 'source':bind(sourcep),'plan':bind(planp),'plan_embedded_sha256':reading['plan_embedded_sha256'],
 'runner':bind(runnerp),'comparison_script':bind(Path(__file__)),'proposals':proposals,
 'contract_production_commit':contract['production_git_commit']}
for k in ['schema','protocol']: assert bindings[k]['sha256']==j[k+'_sha256']
artifact={'artifact_kind':'independent_ai_exact_candidate_partial_comparison','execution':{'agent_id':'/root/prepare_review','route':'interactive_agent','role':'nonblind_comparison_auditor'},
 'bindings':bindings,'scope':scope,'source_first_reading_hash_verified_before_producer_access':True,
 'initial_reading_unchanged':sha(rp.read_bytes())==READ,'omission_pass_performed':True,
 'mappings':mappings,'discrepancies':[discrepancy],
 'producer_record_hash_contract':'SHA256 UTF-8 sorted-key compact JSON, ensure_ascii=false, followed by one LF; matches runner encoded(record).',
 'mapped_producer_records':{rid:records[rid] for rid in sorted(used)},
 'mechanical_checks':{**checks,'exact_candidate_in_memory_replay_pass':True,'replayed_snapshot_sha256':SNAP,
 'read_only_replay':'runner.load and validate_apply only; no CURRENT selection, lock, promotion, or external write',
 'source_schema_protocol_pins_pass':True},
 'interpretation_limits':['Coarser producer claim granularity is reported separately from content omissions; it does not establish atomically qualified examples.',
 'Only 18 completed producer segments overlap independent cores. No omission inference is made for the 12 unprocessed independent cores.',
 'Boundary granularity differs: producer preserves open local structural chunks; reader follows full discussion. Open tails are honest, not false completion.',
 'No full risk-record review, exported-view audit, or whole-tractate acceptance.'],
 'human_certification':False,'task_eligibility':{k:False for k in ['retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice','ml']}}
cp=publish(BASE/'comparisons/bava_kamma_batch001.json',artifact)
verdict={'verdict':'REWORK_TARGETED','scope':'Exact candidate snapshot only; partial independent comparison, not full tractate admission.',
 'bindings':bindings,'comparison':cp,'layer_matrix':scope,'required_changes':[discrepancy],
 'confirmed_false_attributions_in_compared_cores':0,'confirmed_missing_claim_contents':0,
 'confirmed_missing_typed_argument_relations':1,'unresolved_integrity_critical_count':0,
 'full_review_receipt':False,'tractate_accepted':False,'admission_owner':'global coordinator',
 'later_than_integrated004':True,'human_certification':False,'task_eligibility':artifact['task_eligibility'],
 'remaining':'Apply local relation repair through owner, then compare new exact version. Complete unprocessed production scope and remaining probability/endpoint/risk independent reading before full review. Existing source reading remains immutable.'}
vp=publish(BASE/'verdicts/bava_kamma_batch001.json',verdict)
print(json.dumps({'comparison':cp,'verdict':vp,'scope':scope,'checks':checks},ensure_ascii=False))
