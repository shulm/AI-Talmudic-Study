"""Freeze the fifth selected production cohort; no inherited review acceptance."""
from pathlib import Path
from author_remaining_openings_001 import r
lane=Path(__file__).parent;checkpoint=r.read(lane/'LANE_CHECKPOINT_004.json')
selected=dict(taanit='32bcf629046f104ec121ba829715249cb950f910fccadc3d989be9ea6592d300',bava_batra='8218b217ae974cfc0e6e63071e0b4db3a3552b69c028b57e6dab60ece59744a2',nedarim='23ebb13e5f992b93efc184ac5f88c54f8be8a628a0087615786971d732a69ea4',moed_katan='3dab930ef06d5ab7f8bb28e101b06a43d5f30e7d082ae1960ba075709cebd305')
for item in checkpoint['packages']:
    slug=item['tractate']
    if slug not in selected:continue
    path=lane/'packages'/slug/selected[slug]/'PACKAGE.json';package=r.read(path)
    item.update(package=path.relative_to(lane).as_posix(),package_sha256=r.sha(path.read_bytes()),snapshot_sha256=selected[slug])
    for key in ['active_records','superseded_records','open_tails','owner']:item[key]=package[key]
    for key in ['completed_by_layer','next_unprocessed_by_layer']:item[key]=package['replay'][key]
checkpoint['completed_unique_segments']=sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments']=13593-checkpoint['completed_unique_segments']
checkpoint.update(previous_checkpoint='LANE_CHECKPOINT_004.json',review_manifest='reviews/capture_005/MANIFEST.json',review_manifest_sha256=r.sha((lane/'reviews/capture_005/MANIFEST.json').read_bytes()),qualification_notes='All eligibility false. Prior targeted repairs independently verified within their exact scope; no acceptance inherited for the new production windows. Additional Moed Katan source-only risk review pending. Coordinator additive answer-set guidance preserved in audit; 238 reported risk candidates are not a confirmed-error estimate. Source-based adjudication remains outstanding.')
checkpoint['review_manifests'].append('reviews/capture_005/MANIFEST.json')
r.immutable(lane/'LANE_CHECKPOINT_005.json',r.encoded(checkpoint))
print(checkpoint['completed_unique_segments'],checkpoint['remaining_source_segments'])
for x in checkpoint['packages']:print(x['tractate'],x['completed_by_layer']['structure'],x['next_unprocessed_by_layer']['structure'])
