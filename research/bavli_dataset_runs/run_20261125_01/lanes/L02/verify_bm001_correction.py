"""Read-only regression/replay of BM001-SCOPE; not independent semantic review."""
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[4]/'research/bavli_production_v1'))
import runner as r

receipt=r.read(HERE/'bm001_scope_correction_receipt.json')
old=r.read(HERE/'frozen/bavli_bava_metzia/snapshot.json')
assert r.sha(r.encoded(old))==receipt['previous_snapshot_sha256']
raw=(HERE/'bm001_scope_correction_proposal.json').read_bytes()
assert r.sha(raw)==receipt['proposal_sha256']
proposal=json.loads(raw)
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L02/bavli_bava_metzia')
j,segments=r.load(job)
new=r.validate_apply(old,proposal,segments,j)
new['proposals']=old['proposals']+[receipt['proposal_sha256']]
assert r.sha(r.encoded(new))==receipt['snapshot_sha256']
assert r.encoded(new)==(HERE/'bm001_scope_corrected_snapshot.json').read_bytes()
before={x['id']:x for x in old['records']}
after={x['id']:x for x in new['records']}
replaced={x['supersedes'] for x in proposal['records'] if x.get('supersedes')}
for rid,record in before.items():
    assert after[rid]==(dict(record,release_state='superseded') if rid in replaced else record)
for n in [17,44,54]:
    record=after[f'bm.gemara001.opening.claims.{n}.bm001scope']
    assert record['content']['assertion_mode']=='conditional'
    assert record['content']['conditions']
    assert '2a:10' in record['content']['scope']
principle=after['bm.bm001scope.sight_nonacquisition.claim']
assert principle['content']['assertion_mode']=='asserted'
assert all(not x['ml_eligible'] for x in after.values())
assert r.report(old,segments)['completed_by_layer']==r.report(new,segments)['completed_by_layer']
assert old['open_tails']==new['open_tails']
assert r.replay(job)['snapshot_sha256']==receipt['snapshot_sha256']
print(json.dumps({'status':'PASS_CORRECTION_REPLAY_AND_INVARIANTS','snapshot_sha256':receipt['snapshot_sha256'],'superseded_records':len(replaced),'coverage_per_layer':47,'independent_re_review_completed':False,'tractate_delivered':False}))
