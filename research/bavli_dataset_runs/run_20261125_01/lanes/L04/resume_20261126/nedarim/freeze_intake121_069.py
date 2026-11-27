"""Verify capped window receipt and freeze its exact version before separate repairs."""
import author_continuation_002 as a
from pathlib import Path
import hashlib,json
r=a.r;HERE=Path(__file__).resolve().parent
START='b6421aabe6cab3ce7d705b4e1dd71fa6f1dab74a7a6122db508b95ce954e8b74'
END='5168ca1425eb9ef707abb189482125b347fb49a65fc7e7effcec2309dbf96ce4'
assert r.read(a.JOB/'CURRENT.json')['snapshot_sha256']==END
owner=r.read(a.JOB/'OWNER.json');assert owner=={'owner':'L04/nedarim_resume_20261126','epoch':3}
start=r.read(HERE/'START_INTAKE121_069.json')
for name,h in start['actual_nine_file_hashes'].items():assert hashlib.sha256((a.ROOT.parent/name).read_bytes()).hexdigest()==h
assert hashlib.sha256((a.ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json').read_bytes()).hexdigest()==start['contract_sha256']
before=r.read(a.JOB/'snapshots'/(START+'.json'));after=r.current(a.JOB)
prior={x['id']:x for x in before['records']};now={x['id']:x for x in after['records']}
assert all(now[k]==v for k,v in prior.items())
new=[x for k,x in now.items() if k not in prior]
assert len(new)==233 and all(x['review_state']=='unreviewed' and not x['ml_eligible'] for x in new)
oldcov={(x['segment_id'],x['layer']):x for x in before['coverage']};newcov={(x['segment_id'],x['layer']):x for x in after['coverage']}
assert all(newcov[k]==v for k,v in oldcov.items())
assert len(newcov)-len(oldcov)==22*8
cp=HERE/'CHECKPOINT_1105_5168ca1425eb.json';checkpoint=r.read(cp)
assert checkpoint['snapshot_sha256']==END and checkpoint['replay_pass'] and checkpoint['export_exact_content_pass']
receipt=dict(status='CAPPED_WINDOW_FROZEN_UNREVIEWED',owner=owner,start_snapshot=START,snapshot_sha256=END,proposal_sha256='fc11ee225355a9f4d89572039eb562e0fa326dc4dbe191b522cf4bf92cc1fb0d',source_sha256=a.meta['source_sha256'],contract_sha256=start['contract_sha256'],all_nine_actual_implementation_hashes_match=True,scope=['Nedarim 62b:5','Nedarim 63b:9'],new_segments=22,max_authorized=30,coherent_boundary='Chapter ending63b9 before new chapter64a1',new_records=233,all_prior_records_and_coverage_unchanged=True,all_eight_layers=1105,total_segments=1509,next_source='Nedarim 64a:1',replay_pass=True,exact_export_pass=True,checkpoint_path=str(cp),checkpoint_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),export_path=checkpoint['export_path'],export_manifest_sha256=checkpoint['export_manifest_sha256'],all_ml_eligible_false=True,new_window_independent_review='UNREVIEWED; historical1083 comparison cannot certify new22',hold='No further source-window promotion or targeted repairs pending parent instruction.',staging_note='continuation_069.json failed local prevalidation for duplicate edge ID and was never submitted;069b is the sole accepted proposal, with distinct timing-answer ID.')
r.immutable(HERE/'FROZEN_INTAKE121_069.json',r.encoded(receipt));print(json.dumps(receipt,indent=2))
