"""Exact applied-state closure and historical-preservation audit; no canonical mutation."""
import author_continuation_002 as a
from pathlib import Path
from copy import deepcopy
import json
r=a.r;HERE=Path(__file__).resolve().parent
pre=r.read(HERE/'REPAIR_DELEGATED085_067_PREVALIDATION.json')
expected='4b131b8bae8fb66e16c8b3745781812346dd392110e6da2dd345e4178add9712'
assert r.read(a.JOB/'CURRENT.json')['snapshot_sha256']==expected
assert r.read(a.JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
before=r.read(a.JOB/'snapshots'/(pre['base_snapshot']+'.json'));after=r.current(a.JOB)
old={x['id']:x for x in before['records']};new={x['id']:x for x in after['records']}
mapping=pre['supersession_mapping'];sup={k for k,x in new.items() if x['release_state']=='superseded'}
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,list):return [s for v in x for s in strings(v)]
    if isinstance(x,dict):return [s for v in x.values() for s in strings(v)]
    return []
for key,row in old.items():
    want=deepcopy(row)
    if key in mapping:want['release_state']='superseded'
    assert new[key]==want,key
for row in new.values():
    if row['release_state']=='valid':
        assert not set(row['links']+strings(row['content']))&sup,row['id']
    assert row['ml_eligible'] is False
for cell in after['coverage']:
    assert not set(cell['record_ids'])&sup
    for rid in cell['record_ids']:
        assert any(e['segment_id']==cell['segment_id'] for e in new[rid]['evidence'])
assert r.report(before,a.ss)['completed_by_layer']==r.report(after,a.ss)['completed_by_layer']

assert all(new[k]==v for k,v in old.items() if k.startswith('nd.r066.'))
new_sids={a.refs['61b:'+str(i)]['id'] for i in range(5,10) if '61b:'+str(i) in a.refs}
new_sids={e['segment_id'] for k,v in old.items() if k.startswith('nd.r066.') for e in v['evidence']}
assert [c for c in before['coverage'] if c['segment_id'] in new_sids]==[c for c in after['coverage'] if c['segment_id'] in new_sids]
assert new['nd.r018.testimony.a.fix085']['content']['transmission_chain']==['רבי אלעזר','יוסי בן יועזר איש צרידה']
assert new['nd.fix085.tarfonrule.p']['content']['holder_candidates']==['רבי טרפון']
assert new['nd.fix085.abayeq.q']['content']['answer_set_status']=='partial'
for k in ['nd.r018.impureq.q','nd.r018.conflict.q']:assert new[k]==old[k]
report=dict(status='APPLIED_REPAIR_CLOSURE_VERIFIED_INDEPENDENT_RECHECK_PENDING',snapshot_sha256=expected,proposal_sha256=pre['proposal_sha256'],base_snapshot_sha256=pre['base_snapshot'],operative_issue_mapping=pre['operative_issue_mapping'],supersession_mapping=mapping,all_previous_records_unchanged_except_mapped_release_states=True,all_active_links_content_ids_and_embedded_scopes_closed=True,coverage_reference_closure=True,new21_records_and_coverage_unchanged=True,new21_review='UNREVIEWED',all_eight_coverage_counts=1083,total_segments=1509,total_records=len(new),superseded_records=len(sup),active_records=sum(x['release_state']=='valid' for x in new.values()),all_ml_eligible_false=True,no_new_window_promotion=True,next_source='Nedarim 62b:5',owner={'epoch':3,'owner':'L04/nedarim_resume_20261126'},independent_exact_recheck='pending; historical1062 comparison does not certify this later version',preserved_comparison_categories=pre['preserved_comparison_categories'])
r.immutable(HERE/'REPAIR_DELEGATED085_067_CLOSURE.json',r.encoded(report));print(json.dumps(report,ensure_ascii=False,indent=2))
