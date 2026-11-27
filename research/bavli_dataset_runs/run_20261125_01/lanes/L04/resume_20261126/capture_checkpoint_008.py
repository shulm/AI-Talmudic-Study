"""Freeze the eighth selected production cohort; no inherited review acceptance."""
from pathlib import Path
from author_remaining_openings_001 import r
lane=Path(__file__).parent;checkpoint=r.read(lane/'LANE_CHECKPOINT_007.json')
selected=dict(taanit='59c62a6064a816524290a464e500ca6e82b6b0fe2b540a8f9b385ee533dff776',nedarim='d34c7be2fd11ac6af344a3d49a15486b294390b51c6132e8a41984328f786a81',avodah_zarah='645f4014fe2302172a05550c12c5580518f107ba703d09ada268cf8ad5e19a06',makkot='bf3f3242d3a8c9e476640240788bc653646a232e2362fb1f34d2b6d1cf5ba172',moed_katan='e719c80465f2dc92a32289acd3443e1ede878d0ee22d6a06a495b5f034f7ab2d')
for item in checkpoint['packages']:
    slug=item['tractate']
    if slug not in selected:continue
    path=lane/'packages'/slug/selected[slug]/'PACKAGE.json';package=r.read(path)
    item.update(package=path.relative_to(lane).as_posix(),package_sha256=r.sha(path.read_bytes()),snapshot_sha256=selected[slug])
    for key in ['active_records','superseded_records','open_tails','owner']:item[key]=package[key]
    for key in ['completed_by_layer','next_unprocessed_by_layer']:item[key]=package['replay'][key]
checkpoint['completed_unique_segments']=sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments']=13593-checkpoint['completed_unique_segments']
checkpoint.update(previous_checkpoint='LANE_CHECKPOINT_007.json',review_manifest='reviews/capture_009/MANIFEST.json',review_manifest_sha256=r.sha((lane/'reviews/capture_009/MANIFEST.json').read_bytes()),qualification_notes='All eligibility false; zero full tractates delivered. Review delivery010 all397files verified. Three30-core original probability batches MK003-005 compared only at their exact historical versions, with context and overlaps qualified separately. Batch005 original Abaye authority/holder exclusion retained. Additive citation044 correction independently verified only at e719c804; no coverage credit or acceptance inherited by other records. New windows unreviewed. Existing answer-set risk screen remains unadjudicated; no bulk relabeling. Next bounded production wave coordinated with review capacity.')
checkpoint['review_manifests'].append('reviews/capture_009/MANIFEST.json')
r.immutable(lane/'LANE_CHECKPOINT_008.json',r.encoded(checkpoint))
print(checkpoint['completed_unique_segments'],checkpoint['remaining_source_segments'])
for x in checkpoint['packages']:print(x['tractate'],x['completed_by_layer']['structure'],x['next_unprocessed_by_layer']['structure'])
