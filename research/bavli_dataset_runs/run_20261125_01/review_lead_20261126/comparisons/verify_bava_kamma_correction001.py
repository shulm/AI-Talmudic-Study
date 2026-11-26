"""Targeted nonblind correction verification; no additional semantic admission."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L06/bavli_bava_kamma')
OLD='89aab343c9b6bb4c302a7a18094c6f1ee229c8b78e77fa8828d5a84d34985ff9'
NEW='63544b016a98524c2e65d7d615c9204c6648d1839ba2f22a453d318b18951347'
FIX='40d6100e255fa06393a6e56f097871d978ec83a07d3e015c371d87e0d6fe1c1d'
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}
preserved=[]
for rel,h in [('readings/bava_kamma_batch001.json','7dd63968fa17b405b50d6fa1490504eb96f2dd88aaf8e3e0832ab3041def977d'),('comparisons/bava_kamma_batch001.json','c10b9eff039ed12aa9f300f452142b2c5724a523694477e5c89d9ff09fd764e7'),('verdicts/bava_kamma_batch001.json','4e5f7c8aabb66cb6a7b2cc02d5fbc74289ab48162d0dbdee39e658c2aea8bd92')]:
    p=BASE/rel;assert sha(p.read_bytes())==h;preserved.append(bind(p))
contractp=REPO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
pointer=json.loads((REPO/'research/bavli_dataset_runs/ACTIVE_RUN.json').read_bytes())
assert sha(contractp.read_bytes())==pointer['contract_sha256']
contract=json.loads(contractp.read_bytes());runnerp=REPO/'research/bavli_production_v1/runner.py'
assert sha(runnerp.read_bytes())==contract['production_files']['research/bavli_production_v1/runner.py']
spec=importlib.util.spec_from_file_location('frozen_readonly_runner',runnerp)
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
j,segments=runner.load(JOB)
oldp=JOB/'snapshots'/f'{OLD}.json';newp=JOB/'snapshots'/f'{NEW}.json';fixp=JOB/'proposals'/f'{FIX}.json'
assert sha(oldp.read_bytes())==OLD and sha(newp.read_bytes())==NEW and sha(fixp.read_bytes())==FIX
old=json.loads(oldp.read_bytes());new=json.loads(newp.read_bytes());fix=json.loads(fixp.read_bytes())
assert FIX in new['proposals'] and new['proposals'][-1]==FIX
assert new['proposals'][:len(old['proposals'])]==old['proposals']
replayed=runner.empty();chain=[]
for h in new['proposals']:
    p=JOB/'proposals'/f'{h}.json';assert sha(p.read_bytes())==h
    replayed=runner.validate_apply(replayed,json.loads(p.read_bytes()),segments,j)
    replayed['proposals'].append(h);chain.append(bind(p))
assert replayed==new and sha(runner.encoded(replayed))==NEW
oldrows={r['id']:r for r in old['records']};newrows={r['id']:r for r in new['records']}
status_transitions=[]
for rid,record in oldrows.items():
    assert {k:v for k,v in newrows[rid].items() if k!='release_state'}=={k:v for k,v in record.items() if k!='release_state'},'Old substantive record changed'
    if record['release_state']!=newrows[rid]['release_state']:
        assert record['release_state']=='valid' and newrows[rid]['release_state']=='superseded'
        status_transitions.append({'record_id':rid,'before':'valid','after':'superseded','superseding_record_ids':[r['id'] for r in newrows.values() if r.get('supersedes')==rid]})
edge=newrows['bk06_e_horn_elimination']
assert edge['release_state']=='valid' and edge['layer']=='edges'
assert edge['content']==dict(explicitness='source_explicit',relation='qualification',source_id='bk02_c_hornequal',target_id='bk02_q_pappa')
assert set(edge['links'])=={'bk02_c_hornequal','bk02_q_pappa'}
assert len(fix['records'])==1 and fix['records'][0]['id']==edge['id']
for rid in edge['links']:
    assert newrows[rid]['release_state']=='valid' and newrows[rid]==oldrows[rid]
assert newrows['bk02_c_pappatoothfoot']==oldrows['bk02_c_pappatoothfoot']
assert newrows['bk02_c_pappatoothfoot']['content']['assertion_mode']=='hypothetical'
evidence=[]
for e in edge['evidence']:
    seg=segments[e['segment_id']];a,b=e['start_char'],e['end_char']
    assert seg['ref']=='Bava Kamma 2b:18' and 0<=a<b<=len(seg['text']) and seg['text'][a:b]==e['quote']
    evidence.append(dict(e,ref=seg['ref']))
sid=edge['evidence'][0]['segment_id']
for layer in ['edges','reconciliation']:
    c=next(c for c in new['coverage'] if c['segment_id']==sid and c['layer']==layer)
    assert c['extraction_state']=='completed' and edge['id'] in c['record_ids']
receipt={'artifact_kind':'targeted_nonblind_correction_verification','status':'TARGETED_DISCREPANCY_RESOLVED',
 'discrepancy_id':'BK001-E15','execution':{'agent_id':'/root/prepare_review','route':'interactive_agent','role':'nonblind_comparison_auditor'},
 'initial_artifacts_preserved':preserved,'original_snapshot':bind(oldp),'corrected_snapshot':bind(newp),'correction_proposal':bind(fixp),
 'contract':bind(contractp),'runner':bind(runnerp),'schema':bind(REPO/'research/bavli_production_v1/schema.json'),
 'protocol':bind(REPO/'research/bavli_production_v1/PROTOCOL.md'),'source_sha256':j['source_sha256'],
 'verification_script':bind(Path(__file__)),'accepted_proposal_chain':chain,
 'corrected_edge':edge,'corrected_edge_sha256':sha(runner.encoded(edge)),
 'dependency_hashes':{rid:sha(runner.encoded(newrows[rid])) for rid in edge['links']},'original_evidence':evidence,
 'intervening_release_state_transitions_not_adjudicated':status_transitions,
 'checks':{'snapshot_and_proposal_file_hashes':True,'in_memory_exact_candidate_replay':True,
 'schema_source_protocol_and_evidence_validation':True,'all_original_substantive_record_fields_preserved':True,
 'both_dependencies_active_and_unchanged':True,'edge_and_reconciliation_coverage_include_fix':True,
 'tooth_foot_assignment_remains_hypothetical':True},
 'assessment':'The new source-explicit qualification edge now encodes the horn-equality conclusion restricting Rav Pappa unequal-derivative scope. BK001-E15 is resolved for this exact snapshot.',
 'semantic_scope':'Only this correction and its immediate dependencies were semantically rechecked. Intervening/new source content was mechanically replayed, not independently semantically accepted.',
 'initial_verdict_preserved':'Original REWORK_TARGETED verdict remains immutable and describes its original snapshot. This receipt resolves its named local issue only.',
 'full_tractate_acceptance':False,'full_review_receipt':False,'new_content_globally_accepted':False,
 'human_certification':False,'task_eligibility':{k:False for k in ['retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice','ml']},
 'admission_owner':'global coordinator'}
out=BASE/'comparisons/bava_kamma_correction001.json'
raw=(json.dumps(receipt,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
if out.exists():assert out.read_bytes()==raw
else:
    with out.open('xb') as f:f.write(raw)
print(json.dumps({'status':receipt['status'],'receipt':bind(out),'preserved_original_records':len(oldrows),'new_records_not_semantically_admitted':len(newrows)-len(oldrows)-1}))
