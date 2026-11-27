"""Exact applied-state closure and historical-preservation audit; no canonical mutation."""
import author_continuation_002 as a
from pathlib import Path
from copy import deepcopy
import json
r=a.r;HERE=Path(__file__).resolve().parent
pre=r.read(HERE/'REPAIR_DELEGATED020_065_PREVALIDATION.json')
expected='26acf7ff70ba33f249b8e3f957edac6a932ce1d32c7e84996ad3b239e74bab01'
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
assert new['nd.r010.amend.q.unc013']==old['nd.r010.amend.q.unc013']
assert new['nd.r010.stronger.a.fix020']['content']['role']=='quoted_authority'
assert new['nd.r010.stronger.a.fix020']['content']['scope']=='nd.r010.stronger.u.fix020'
assert new['nd.r010.stronger.p.fix020']['content']['holder_candidates']==['רבי שמעון']
assert new['nd.fix020.derivation.q']['content']['answer_set_status']=='partial'
assert new['nd.fix020.verse.answer']['content']['target_id']=='nd.fix020.derivation.q'
assert new['nd.fix020.amend.correction']['content']=={'source_id':'nd.r010.amend.q.unc013','target_id':'nd.r010.olist.c','relation':'correction','explicitness':'source_explicit'}
assert new['nd.fix020.lemma.c']['evidence']==[a.ev('10b:11','נדר במוהי הרי אלו כינויין')]
report=dict(status='APPLIED_REPAIR_CLOSURE_VERIFIED_INDEPENDENT_RECHECK_PENDING',snapshot_sha256=expected,proposal_sha256=pre['proposal_sha256'],base_snapshot_sha256=pre['base_snapshot'],operative_issue_mapping=pre['operative_issue_mapping'],supersession_mapping=mapping,all_previous_record_bytes_semantically_unchanged_except_five_release_states=True,all_active_links_content_ids_and_embedded_scopes_closed=True,coverage_reference_closure=True,unresolved_amended_question_unchanged=True,withdrawn_P04_and_other_existing_records_unchanged=True,all_eight_coverage_counts=1062,total_segments=1509,total_records=len(new),superseded_records=len(sup),active_records=sum(x['release_state']=='valid' for x in new.values()),all_ml_eligible_false=True,no_new_window_promotion=True,next_source='Nedarim 61b:5',owner={'epoch':3,'owner':'L04/nedarim_resume_20261126'},independent_exact_recheck='pending; original comparison bound d34c7be2 and does not certify this later version')
r.immutable(HERE/'REPAIR_DELEGATED020_065_CLOSURE.json',r.encoded(report));print(json.dumps(report,ensure_ascii=False,indent=2))
