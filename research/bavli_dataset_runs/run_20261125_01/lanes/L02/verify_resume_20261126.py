"""Read-only exact frozen replay; never advances live pointers."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[4]/'research/bavli_production_v1'))
import runner as r
root=HERE/'resume_20261126'
raw=(root/'RECEIPT.json').read_bytes()
assert r.sha(raw)=='4ae242f5558c4a74863c6c0a9c04ed43256f764de10d5cc5b4f2eaadc9b8d0d0'
receipt=json.loads(raw)
for name,h in receipt['artifact_files'].items():
    assert r.sha((root/name).read_bytes())==h,name
for job in receipt['jobs']:
    local=root/job['job_id'];meta,segments=r.load(Path(job['job_path']))
    state=r.empty()
    for h in job['accepted_proposal_sha256']:
        data=(local/'proposals'/f'{h}.json').read_bytes();assert r.sha(data)==h
        chain=state['proposals'];state=r.validate_apply(state,json.loads(data),segments,meta);state['proposals']=chain+[h]
    assert r.sha(r.encoded(state))==job['snapshot_sha256']
    assert r.encoded(state)==(local/'snapshot.json').read_bytes()
    assert r.report(state,segments)['completed_by_layer']==job['report']['completed_by_layer']
print(json.dumps(dict(status='PASS_FROZEN_REPLAY_ALL_FIVE',completed_each_layer=receipt['completed_each_layer'],tractates_delivered=0,independent_review_completed=False)))
