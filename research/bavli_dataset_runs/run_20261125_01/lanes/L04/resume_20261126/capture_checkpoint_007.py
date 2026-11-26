"""Freeze the seventh selected production cohort; no inherited review acceptance."""
from pathlib import Path
from author_remaining_openings_001 import r
lane=Path(__file__).parent;checkpoint=r.read(lane/'LANE_CHECKPOINT_006.json')
selected=dict(taanit='98227d0f36f0c69ce2c343bd7a69948d5335972435bd39b8b0e98b26bf3de725',pesachim='ecb3dc24813b3635bbd1b9c61c96b44acafd94ed133d5cd8641d001b1efb36e5',avodah_zarah='23f7de6f6f446b16b545c2285cdc1bc416d191739cf446cd464ad173dd0cd007',nedarim='df84ce6f2c20a5619e68b3f101ef9723a05dc323322968db91b8b7e749eb63c1',moed_katan='a4d8aca5d16580152fa53a43f01782453580cf6ef6404ee0ff72a4b083c286bb')
for item in checkpoint['packages']:
    slug=item['tractate']
    if slug not in selected:continue
    path=lane/'packages'/slug/selected[slug]/'PACKAGE.json';package=r.read(path)
    item.update(package=path.relative_to(lane).as_posix(),package_sha256=r.sha(path.read_bytes()),snapshot_sha256=selected[slug])
    for key in ['active_records','superseded_records','open_tails','owner']:item[key]=package[key]
    for key in ['completed_by_layer','next_unprocessed_by_layer']:item[key]=package['replay'][key]
checkpoint['completed_unique_segments']=sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments']=13593-checkpoint['completed_unique_segments']
checkpoint.update(previous_checkpoint='LANE_CHECKPOINT_006.json',review_manifest='reviews/capture_008/MANIFEST.json',review_manifest_sha256=r.sha((lane/'reviews/capture_008/MANIFEST.json').read_bytes()),qualification_notes='All eligibility false. Prior targeted repairs independently verified within their exact scope; no acceptance inherited for the new production windows. Moed Katan graves correction independently rechecked; fresh 51-core supplement accepted partially with exceptions at0990865 only. Its initial reviewer criticism is withdrawn by required addendum001. No required producer changes in effective verdict. Metadata026 separately checked at100fd875. No later-snapshot admission. Supplemental 20 original-plan overlaps and31 outside-plan cores are not a fresh draw. Two new original-plan30-core reading batches pending. Coordinator additive answer-set guidance preserved in audit; 238 reported risk candidates are not a confirmed-error estimate. Source-based adjudication remains outstanding.')
checkpoint['review_manifests'].extend(['reviews/capture_007/MANIFEST.json','reviews/capture_008/MANIFEST.json'])
r.immutable(lane/'LANE_CHECKPOINT_007.json',r.encoded(checkpoint))
print(checkpoint['completed_unique_segments'],checkpoint['remaining_source_segments'])
for x in checkpoint['packages']:print(x['tractate'],x['completed_by_layer']['structure'],x['next_unprocessed_by_layer']['structure'])
