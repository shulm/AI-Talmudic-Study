"""Freeze exact Nedarim070 and retain all prior version-specific qualifications."""
from pathlib import Path
from author_remaining_openings_001 import r

lane = Path(__file__).parent
checkpoint = r.read(lane / 'LANE_CHECKPOINT_013.json')
snapshot = '7d9b6947557eaf3b807e913f1acde3c82ca39e9124610980288d993b33f1fa3b'
path = lane / 'packages' / 'nedarim' / snapshot / 'PACKAGE.json'
package = r.read(path)
item = next(x for x in checkpoint['packages'] if x['tractate'] == 'nedarim')
item.update(package=path.relative_to(lane).as_posix(), package_sha256=r.sha(path.read_bytes()), snapshot_sha256=snapshot)
for key in ['active_records', 'superseded_records', 'open_tails', 'owner']:
    item[key] = package[key]
for key in ['completed_by_layer', 'next_unprocessed_by_layer']:
    item[key] = package['replay'][key]
checkpoint['completed_unique_segments'] = sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments'] = 13593 - checkpoint['completed_unique_segments']
checkpoint['previous_checkpoint'] = 'LANE_CHECKPOINT_013.json'
for n in [32, 33, 34]:
    checkpoint['review_manifests'].append(f'reviews/capture_{n:03d}/MANIFEST.json')
checkpoint['review_manifest'] = 'reviews/capture_034/MANIFEST.json'
checkpoint['review_manifest_sha256'] = r.sha((lane / checkpoint['review_manifest']).read_bytes())
checkpoint['engineering_verification'] += ['audit/PACKAGE_VERIFICATION_ND069.json', 'audit/PACKAGE_VERIFICATION_ND070.json']
checkpoint['qualification_notes'] = ('Zero of seven delivered; all eligibility false. ND118 frozen source-only30core+15context reading and ND121 exacthistorical1083 comparison preserved;38incidental refs excluded. Four confirmed producer issue groups D1-D4 corrected on1105; original comparator bounded72proposalreplay PASS, parent fullprefix/export PASS.22newsegments233records176cells remain unchangedUNREVIEWED. Nine answer-status cases and optional question links remain uncertainty, not confirmed semantic/schema failures; coordinator conservative policy001/ND121_002 preserved, later recheck exposure disclosed. Reader context-question omission/status/granularity and source-only adapter limitations retained. Initial optional dump failure/recovery chronology and unsubmitted069duplicateID draft preserved. No new review credit or broad acceptance from correction; prior checkpoint restrictions and release015 unchanged.')
r.immutable(lane / 'LANE_CHECKPOINT_014.json', r.encoded(checkpoint))
assert checkpoint['completed_unique_segments'] == 3339
print(checkpoint['completed_unique_segments'], checkpoint['remaining_source_segments'])
