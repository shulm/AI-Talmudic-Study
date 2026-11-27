"""RC01 only: unspecified group wording; exact additive dependency closure."""
import author_continuation_024 as b
from copy import deepcopy
from pathlib import Path
import hashlib,json
a=b.a;r=a.r;JOB=a.JOB;HERE=Path(__file__).resolve().parent
BASE='4b131b8bae8fb66e16c8b3745781812346dd392110e6da2dd345e4178add9712'
assert r.read(JOB/'CURRENT.json')['snapshot_sha256']==BASE
assert r.read(JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
reviewdir=JOB.parent/'review_20261127_delegated081/comparisons'
reviewhashes={'recheck_1083_receipt.json':'ff3d2f417fcf79cd8a51693b22465d182ee1c60d55ceeeee7c9dd94957a20a60','recheck_1083_audit.json':'9cd7c55acffe0399b6ff16c4638d96da1efbf90e211f435065a4d450db84375a'}
for name,h in reviewhashes.items():assert sha(reviewdir/name)==h
contractpath=a.ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
contract=r.read(contractpath)
assert sha(contractpath)=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for name,h in contract['production_files'].items():assert sha(a.ROOT.parent/name)==h
state=r.current(JOB);by={x['id']:x for x in state['records']}
assert r.sha(r.encoded(state))==BASE
a.records=[];a.notes={};a.PREFIX='nd.fix085.'
changed={}
def edit(ident):
    if ident not in changed:changed[ident]=deepcopy(by[ident]);assert changed[ident]['release_state']=='valid'
    return changed[ident]
def unit(stem,ref,quote):
    for suffix in ['u','a','c','p']:edit(stem+'.'+suffix)['evidence']=[a.ev(ref,quote)]

print(a.refs['19b:7']['text'])
row=edit('nd.fix085.tarfonrule.c')
before=row['content']['proposition']
assert before.count('neither')==1
row['content']['proposition']=before.replace('neither','none of them')
def strings(value):
    if isinstance(value,str):return [value]
    if isinstance(value,list):return [z for x in value for z in strings(x)]
    if isinstance(value,dict):return [z for x in value.values() for z in strings(x)]
    return []
while True:
    extra={ident:deepcopy(row) for ident,row in by.items() if row['release_state']=='valid' and ident not in changed and any(x in changed for x in row['links']+strings(row['content']))}
    if not extra:break
    changed.update(extra)
mapping={ident:ident+'.rc01' for ident in changed}
def remap(value):
    if isinstance(value,str):return mapping.get(value,value)
    if isinstance(value,list):return [remap(x) for x in value]
    if isinstance(value,dict):return {k:remap(v) for k,v in value.items()}
    return value
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row.update(id=mapping[old],supersedes=old)
    row['content']=remap(row['content']);row['links']=remap(row['links']);a.records.append(row)


# Rebuild only affected existing coverage cells from the complete surviving local inventory.
active={x['id']:deepcopy(x) for x in state['records'] if x['release_state']=='valid' and x['id'] not in mapping}
active.update({x['id']:x for x in a.records})
affected={(ev['segment_id'],row['layer']) for row in a.records for ev in row['evidence']}
affected.update((cell['segment_id'],cell['layer']) for cell in state['coverage'] if any(i in mapping for i in cell['record_ids']))
coverage=[]
for cell in state['coverage']:
    if (cell['segment_id'],cell['layer']) not in affected:continue
    row=deepcopy(cell);row.pop('proposal_execution',None)
    row['record_ids']=sorted(x['id'] for x in active.values() if x['layer']==row['layer'] and any(ev['segment_id']==row['segment_id'] for ev in x['evidence']))
    row['extraction_result']='records_found' if row['record_ids'] else 'none_found_after_pass'
    row['rationale']+=' RC01 minimal English wording correction after rereading19b7: none of them preserves unspecified group cardinality; no other semantic change. Full surviving inventory and supersession dependencies retained.'
    coverage.append(row)
assert len(coverage)==len(affected),'Repairs may touch only existing completed coverage cells.'
p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/nedarim_continuation',model_id=None),records=a.records,coverage=coverage,open_tails=remap(state['open_tails']))
preview=r.validate_apply(state,p,a.ss,a.meta)
sup={x['id'] for x in preview['records'] if x['release_state']=='superseded'}
for row in preview['records']:
    if row['release_state']=='valid':assert not set(row['links']+strings(row['content']))&sup,row['id']
assert r.report(preview,a.ss)['completed_by_layer']==r.report(state,a.ss)['completed_by_layer']
assert all(next(x for x in preview['records'] if x['id']==ident)==row for ident,row in by.items() if ident.startswith('nd.r066.'))
assert all(not x['ml_eligible'] for x in preview['records'])
out=JOB/'staging'/'repair_rc01_068.json';r.immutable(out,r.encoded(p))


new_sids={e['segment_id'] for ident,row in by.items() if ident.startswith('nd.r066.') for e in row['evidence']}
assert len([c for c in state['coverage'] if c['segment_id'] in new_sids])==168
assert [c for c in state['coverage'] if c['segment_id'] in new_sids]==[c for c in preview['coverage'] if c['segment_id'] in new_sids]
report=dict(status='RC01_PREVALIDATED_RECHECK_PENDING',base_snapshot=BASE,proposal_path=str(out),proposal_sha256=sha(out),review_artifact_hashes=reviewhashes,supersession_mapping=mapping,coverage_count_unchanged=1083,new306_records_and168_cells_unchanged=True,all_nine_actual_hashes_match=True,all_ml_eligible_false=True,next_unprocessed='Nedarim 62b:5',operative_issue_mapping={'RC01':mapping['nd.fix085.tarfonrule.c']},independent_acceptance=False)
r.immutable(HERE/'REPAIR_RC01_068_PREVALIDATION.json',r.encoded(report));print(json.dumps(report,indent=2))
