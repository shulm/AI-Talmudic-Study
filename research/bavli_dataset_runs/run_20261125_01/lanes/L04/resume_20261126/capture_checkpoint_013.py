"""Freeze exact Taanit057 and retain all prior version-specific qualifications."""
from pathlib import Path
from author_remaining_openings_001 import r

lane = Path(__file__).parent
checkpoint = r.read(lane / 'LANE_CHECKPOINT_012.json')
snapshot = '13b774a3766f6b05e5f389181b3c07eebd62a4f48698a95c300b80f64a6d20b9'
path = lane / 'packages' / 'taanit' / snapshot / 'PACKAGE.json'
package = r.read(path)
item = next(x for x in checkpoint['packages'] if x['tractate'] == 'taanit')
item.update(package=path.relative_to(lane).as_posix(), package_sha256=r.sha(path.read_bytes()), snapshot_sha256=snapshot)
for key in ['active_records', 'superseded_records', 'open_tails', 'owner']:
    item[key] = package[key]
for key in ['completed_by_layer', 'next_unprocessed_by_layer']:
    item[key] = package['replay'][key]
checkpoint['completed_unique_segments'] = sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments'] = 13593 - checkpoint['completed_unique_segments']
checkpoint['previous_checkpoint'] = 'LANE_CHECKPOINT_012.json'
for n in [29, 30, 31]:
    checkpoint['review_manifests'].append(f'reviews/capture_{n:03d}/MANIFEST.json')
checkpoint['review_manifest'] = 'reviews/capture_031/MANIFEST.json'
checkpoint['review_manifest_sha256'] = r.sha((lane / checkpoint['review_manifest']).read_bytes())
checkpoint['engineering_verification'] += ['audit/PACKAGE_VERIFICATION_TA056.json', 'audit/PACKAGE_VERIFICATION_TA057.json']
checkpoint['qualification_notes'] = ('Zero of seven delivered; all eligibility false. TA101 frozen source-only reading and TA105 exact historical712 comparison preserved. Initial comparison and additive auxiliary-ID revision2 remain immutable; comparator output-directory deviation and replay-after-semantic-inspection chronology disclosed. Five producer findings corrected on721: shared fear/exposure mistranslation, three speaker-layer omissions, one qualification edge. Original comparator bounded recheck and parent full-prefix replay/export PASS on exact057. Latest nine segments/182records remain unchanged and UNREVIEWED. Shared reader error, other reader errors,24-open-tail adapter restriction, unresolved scopes and granularity remain locally restricted. Additional Rashi commentary is separately pinned nonblind evidence, not original source-only reader input. No new review credit or acceptance from correction. Prior checkpoint qualifications and release015 unchanged.')
r.immutable(lane / 'LANE_CHECKPOINT_013.json', r.encoded(checkpoint))
assert checkpoint['completed_unique_segments'] == 3317
print(checkpoint['completed_unique_segments'], checkpoint['remaining_source_segments'])
