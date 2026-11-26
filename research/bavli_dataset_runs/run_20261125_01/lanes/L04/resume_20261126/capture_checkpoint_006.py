"""Freeze the sixth selected production cohort; no inherited review acceptance."""
from pathlib import Path
from author_remaining_openings_001 import r
lane=Path(__file__).parent;checkpoint=r.read(lane/'LANE_CHECKPOINT_005.json')
selected=dict(taanit='152031c028cefa555c2488ab839929968c462dfe11aea270bb4cb513e70f22f2',bava_batra='6c1f1a43e1e07f0772cd625422949e0673e777a153dde1e6bfc081211cc96833',pesachim='d4f6f92c9c9da9f91cdada7903b3c70df900851734610b015e96398ee464018c',nedarim='935ac5b410ac45355b42befc0f6c0656188bccd986f8e2ce1ad0ab08c9080cfd',moed_katan='09908653624cc6ad0a45a5261a2ffa41b90fb6a681708943a5aedb814801304b')
for item in checkpoint['packages']:
    slug=item['tractate']
    if slug not in selected:continue
    path=lane/'packages'/slug/selected[slug]/'PACKAGE.json';package=r.read(path)
    item.update(package=path.relative_to(lane).as_posix(),package_sha256=r.sha(path.read_bytes()),snapshot_sha256=selected[slug])
    for key in ['active_records','superseded_records','open_tails','owner']:item[key]=package[key]
    for key in ['completed_by_layer','next_unprocessed_by_layer']:item[key]=package['replay'][key]
checkpoint['completed_unique_segments']=sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments']=13593-checkpoint['completed_unique_segments']
checkpoint.update(previous_checkpoint='LANE_CHECKPOINT_005.json',review_manifest='reviews/capture_006/MANIFEST.json',review_manifest_sha256=r.sha((lane/'reviews/capture_006/MANIFEST.json').read_bytes()),qualification_notes='All eligibility false. Prior targeted repairs independently verified within their exact scope; no acceptance inherited for the new production windows. Moed Katan graves review MG01–03 corrected at a1975ae0 and independently rechecked within 27 core segments; later narrative source-only review pending. Superseded earlier package versions retain the original errors. Coordinator additive answer-set guidance preserved in audit; 238 reported risk candidates are not a confirmed-error estimate. Source-based adjudication remains outstanding.')
checkpoint['review_manifests'].append('reviews/capture_006/MANIFEST.json')
r.immutable(lane/'LANE_CHECKPOINT_006.json',r.encoded(checkpoint))
print(checkpoint['completed_unique_segments'],checkpoint['remaining_source_segments'])
for x in checkpoint['packages']:print(x['tractate'],x['completed_by_layer']['structure'],x['next_unprocessed_by_layer']['structure'])
