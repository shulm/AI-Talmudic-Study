"""Freeze exact replay-bound production checkpoint; no review qualification."""
from authoring import *
from collections import Counter
base=Path(__file__).parent
out=JOB/'worker_epoch2_20261126'
r=runner.read(out/'receipt_032.json')
s=runner.current(JOB)
assert r['replay_pass'] and r['snapshot_sha256']==runner.sha(runner.encoded(s))
assert all(v==735 for v in r['completed_by_layer'].values())
assert not s['open_tails']
export_path=JOB/'exports'/'worker_epoch2_checkpoint_032'
e=runner.export(JOB,export_path)
runner.immutable(out/'export_receipt_032.json',runner.encoded(e))
files={p.name:runner.sha(p.read_bytes()) for p in sorted(out.iterdir()) if p.is_file() and p.suffix in ['.py','.json']}
manifest=dict(snapshot_sha256=r['snapshot_sha256'],accepted_proposal_sha256=s['proposals'],mirrored_artifacts_sha256=files,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],export_manifest_sha256=runner.sha((export_path/'manifest.json').read_bytes()))
runner.immutable(out/'proposal_manifest_032.json',runner.encoded(manifest))
resume=dict(status='WHOLE_TRACTATE_REQUIRED_PASSES_COMPLETE_AWAITING_INDEPENDENT_REVIEW',run_id='run_20261125_01',owner='/root/chagigah_production',epoch=2,snapshot_sha256=r['snapshot_sha256'],source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],completed_by_layer=r['completed_by_layer'],record_counts=dict(Counter(x['layer'] for x in s['records'])),semantic_records=r['semantic_records'],accepted_proposal_count=len(s['proposals']),completed_source_range=[rows[0]['ref'],rows[-1]['ref']],remaining_segments=0,next_zero_based_source_index=None,next_ref=None,next_batch=33,open_tails=s['open_tails'],independent_review_completed=False,tractate_delivered=False,ml_eligible=False,git_owner='/root',export_path=str(export_path),notes=['All 735 original pinned segments received eight manual production passes; coverage is not scholarly completeness certification.','Independent source-only reviewer labels were not read by producer. Independent review, adjudication, and any qualification remain outstanding.','Anonymous alternatives, rejected arguments, retractions, repeated transmissions and source uncertainty are retained, including esoteric and aggadic material.','Unknown actual model identity remains null. Source abbreviations and text variants retain uncertainty where not established.','Rejected schema/typed-edge attempts remain immutable with corrected accepted revisions; accepted proposal hashes are listed in proposal_manifest_032.json.','All accepted authoring scripts/proposals/receipts mirrored under external job worker_epoch2_20261126. Author scripts execute from repository path with authoring.py; mirrors preserve bytes.','Hold further promotions at this exact boundary for independent review as coordinator requested; root owns Git packaging.'])
runner.immutable(out/'resume_032.json',runner.encoded(resume))
runner.immutable(out/'finalize_032.py',Path(__file__).read_bytes())
print(r['snapshot_sha256'],r['semantic_records'],resume['record_counts'],manifest['export_manifest_sha256'],flush=True)
