"""Verify capped window receipt and freeze its exact version before separate repairs."""
import author_continuation_002 as a
from pathlib import Path
import hashlib,json
r=a.r;HERE=Path(__file__).resolve().parent
START='26acf7ff70ba33f249b8e3f957edac6a932ce1d32c7e84996ad3b239e74bab01'
END='65c63fc9a312d505232e0044e5a68129015d8acba73c0b167a0af5eb305f0e8a'
assert r.read(a.JOB/'CURRENT.json')['snapshot_sha256']==END
owner=r.read(a.JOB/'OWNER.json');assert owner=={'owner':'L04/nedarim_resume_20261126','epoch':3}
start=r.read(HERE/'START_INTAKE085_066.json')
for name,h in start['actual_nine_file_hashes'].items():assert hashlib.sha256((a.ROOT.parent/name).read_bytes()).hexdigest()==h
assert hashlib.sha256((a.ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json').read_bytes()).hexdigest()==start['contract_sha256']
before=r.read(a.JOB/'snapshots'/(START+'.json'));after=r.current(a.JOB)
prior={x['id']:x for x in before['records']};now={x['id']:x for x in after['records']}
assert all(now[k]==v for k,v in prior.items())
new=[x for k,x in now.items() if k not in prior]
assert len(new)==306 and all(x['review_state']=='unreviewed' and not x['ml_eligible'] for x in new)
oldcov={(x['segment_id'],x['layer']):x for x in before['coverage']};newcov={(x['segment_id'],x['layer']):x for x in after['coverage']}
assert all(newcov[k]==v for k,v in oldcov.items())
assert len(newcov)-len(oldcov)==21*8
cp=HERE/'CHECKPOINT_1083_65c63fc9a312.json';checkpoint=r.read(cp)
assert checkpoint['snapshot_sha256']==END and checkpoint['replay_pass'] and checkpoint['export_exact_content_pass']
receipt=dict(status='CAPPED_WINDOW_FROZEN_UNREVIEWED',owner=owner,start_snapshot=START,snapshot_sha256=END,proposal_sha256='30690a8d7b4bdc610e4d55ba7fd79667e5aae5a17b66323f752de170a03e7cec',source_sha256=a.meta['source_sha256'],contract_sha256=start['contract_sha256'],all_nine_actual_implementation_hashes_match=True,scope=['Nedarim 61b:5','Nedarim 62b:4'],new_segments=21,max_authorized=30,coherent_boundary='Before new Mishnah62b5',new_records=306,all_prior_records_and_coverage_unchanged=True,all_eight_layers=1083,total_segments=1509,next_source='Nedarim 62b:5',replay_pass=True,exact_export_pass=True,checkpoint_path=str(cp),checkpoint_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),export_path=checkpoint['export_path'],export_manifest_sha256=checkpoint['export_manifest_sha256'],all_ml_eligible_false=True,new_window_independent_review='UNREVIEWED; historical1062 comparison cannot certify new21',hold='No further source-window promotion; subsequent ND085 corrections must be a separate proposal preserving new21.',staging_note='continuation_066.json was staged but never submitted;066b is accepted, refining three non-interrogative objection statements into claim nodes before submission.')
r.immutable(HERE/'FROZEN_INTAKE085_066.json',r.encoded(receipt));print(json.dumps(receipt,indent=2))
