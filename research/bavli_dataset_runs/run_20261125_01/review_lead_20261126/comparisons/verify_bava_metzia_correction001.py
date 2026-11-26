"""Read-only exact-version validation of BM001-SCOPE correction only."""
import sys
sys.dont_write_bytecode=True
import json,hashlib,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L02/bavli_bava_metzia')
OLD='25ffca05e9a6f9445ac1f1b285f70d8e113e962353c02e0e108ce4aa2d5e5990'
NEW='1de0ef2ed8f9cd4fc22791162f92e7d59d276dc09dd9c50336dd8fe0a3940a92'
FIX='2e20df67437e4104ac430da8fa2cb98778e4c20a45a2fa172d0c7f42f9b16e69'
def sha(b):return hashlib.sha256(b).hexdigest()
def bind(p):return {'path':p.as_posix(),'sha256':sha(p.read_bytes())}
preserved=[]
for rel,h in [('readings/bava_metzia_batch001.json','a5ebe400aafc2e27d6bc065e381899570ed1eea21fb9ed6f3c981508203d2e35'),('comparisons/bava_metzia_batch001.json','5ac8b873f2c15e7f1c532916290ed1e35b3330e09773c57653467411c7448e12'),('verdicts/bava_metzia_batch001.json','0a830742f5c4a3b75344e9952436e0dcc6cdb79e23b13d1a61fbd78dc114ada7')]:
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
assert new['proposals'][-1]==FIX and new['proposals'][:len(old['proposals'])]==old['proposals']
replayed=runner.empty();chain=[]
for h in new['proposals']:
    p=JOB/'proposals'/f'{h}.json';assert sha(p.read_bytes())==h
    replayed=runner.validate_apply(replayed,json.loads(p.read_bytes()),segments,j)
    replayed['proposals'].append(h);chain.append(bind(p))
assert replayed==new and sha(runner.encoded(replayed))==NEW
oldrows={r['id']:r for r in old['records']};rows={r['id']:r for r in new['records']}
transitions=[]
for rid,record in oldrows.items():
    assert {k:v for k,v in rows[rid].items() if k!='release_state'}=={k:v for k,v in record.items() if k!='release_state'}
    if record['release_state']!=rows[rid]['release_state']:
        assert record['release_state']=='valid' and rows[rid]['release_state']=='superseded'
        transitions.append({'record_id':rid,'superseding_record_ids':[r['id'] for r in rows.values() if r.get('supersedes')==rid]})
active={k:r for k,r in rows.items() if r['release_state']=='valid'}
prefix='bm.gemara001.opening.';targets=[]
for cn,pn in [(17,19),(44,46),(54,56)]:
    cid=prefix+f'claims.{cn}';pid=prefix+f'positions.{pn}'
    c=active[cid+'.bm001scope'];p=active[pid+'.bm001scope']
    assert c['supersedes']==cid and p['supersedes']==pid
    assert c['content']['assertion_mode']=='conditional'
    assert c['content']['conditions'] and 'combined-clause' in c['content']['conditions'][0]
    assert p['content']['claim_id']==c['id'] and p['content']['conditions']==c['content']['conditions']
    assert 'displaced' in p['content']['local_status'] and 'not rejected' in p['content']['local_status']
    targets += [cid,pid]
for rec in active.values():
    assert not(set(rec['links']) & set(targets)), 'Active link still points to superseded scope record'
    if rec['layer']=='positions':assert rec['content']['claim_id'] not in targets
    if rec['layer']=='edges':assert rec['content']['source_id'] not in targets and rec['content']['target_id'] not in targets
    if rec['layer']=='attributions':assert rec['content']['scope'] not in targets
principle=active['bm.bm001scope.sight_nonacquisition.claim']
position=active['bm.bm001scope.sight_nonacquisition.position']
assert principle['content']['assertion_mode']=='asserted' and 'Sight alone does not acquire' in principle['content']['proposition']
assert position['content']['claim_id']==principle['id'] and 'not rejected' in position['content']['local_status']
assert active[prefix+'claims.3']['content']['assertion_mode']=='rejected'
evidence=[]
for raw in fix['records']:
    r=active[raw['id']]
    for e in r['evidence']:
        seg=segments[e['segment_id']];a,b=e['start_char'],e['end_char']
        assert 0<=a<b<=len(seg['text']) and seg['text'][a:b]==e['quote']
        evidence.append(dict(e,ref=seg['ref'],record_id=r['id']))
assert {segments[e['segment_id']]['ref'] for e in principle['evidence']}=={'Bava Metzia 2a:6','Bava Metzia 2a:8','Bava Metzia 2a:9'}
for coverage in new['coverage']:
    assert not(set(coverage['record_ids']) & set(targets)), 'Coverage cites superseded scope record'
for rel in ['schema','protocol']:
    assert sha((REPO/'research/bavli_production_v1'/('schema.json' if rel=='schema' else 'PROTOCOL.md')).read_bytes())==j[rel+'_sha256']
receipt={'artifact_kind':'targeted_nonblind_correction_verification','status':'TARGETED_DISCREPANCY_RESOLVED',
 'discrepancy_id':'BM001-SCOPE','execution':{'agent_id':'/root/prepare_review','route':'interactive_agent','role':'nonblind_comparison_auditor'},
 'initial_artifacts_preserved':preserved,'original_snapshot':bind(oldp),'corrected_snapshot':bind(newp),'correction_proposal':bind(fixp),
 'contract':bind(contractp),'runner':bind(runnerp),'schema':bind(REPO/'research/bavli_production_v1/schema.json'),
 'protocol':bind(REPO/'research/bavli_production_v1/PROTOCOL.md'),'source_sha256':j['source_sha256'],
 'verification_script':bind(Path(__file__)),'accepted_proposal_chain':chain,
 'correction_records':{r['id']:active[r['id']] for r in fix['records']},
 'correction_record_hashes':{r['id']:sha(runner.encoded(active[r['id']])) for r in fix['records']},
 'original_evidence':evidence,'preserved_record_release_transitions':transitions,
 'checks':{'snapshot_proposal_contract_hashes':True,'exact_in_memory_replay':True,'all_original_substantive_record_fields_preserved':True,
 'conditional_scope_in_revised_claims_and_positions':True,'separate_nonacquisition_principle_still_asserted':True,
 'active_links_edges_positions_attributions_and_coverage_do_not_reference_superseded_scope_records':True,
 'exact_original_evidence_slices':len(evidence),'schema_source_protocol_pins':True},
 'assessment':'BM001-SCOPE is resolved: 2a:8–9 wording explanations and the analogous 2a:6 explanation explicitly retain combined-clause dependency, while the distinct sight-nonacquisition principle remains asserted. Dependent positions and graph references are revised consistently.',
 'reader_errors_preserved':['BM001-READER-E03 remains a reader-side relation-target correction; no false objection to nonacquisition is introduced by this repair.',
 'BM001-READER-OATH remains a reader-side missing-condition refinement. This producer receipt does not claim the initial reader file was corrected.'],
 'semantic_scope':'Correction records and immediate dependencies only. Exact replay of other new content is mechanical validation, not independent semantic admission.',
 'initial_verdict_preserved':'Original REWORK_TARGETED verdict and initial producer snapshot remain immutable; this receipt resolves only its named producer issue for the corrected snapshot.',
 'full_tractate_acceptance':False,'full_review_receipt':False,'new_content_globally_accepted':False,'human_certification':False,
 'task_eligibility':{k:False for k in ['retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice','ml']},'admission_owner':'global coordinator'}
out=BASE/'comparisons/bava_metzia_correction001.json'
raw=(json.dumps(receipt,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
if out.exists():assert out.read_bytes()==raw
else:
    with out.open('xb') as f:f.write(raw)
print(json.dumps({'status':receipt['status'],'receipt':bind(out),'correction_records':len(fix['records']),'evidence_slices':len(evidence)}))
