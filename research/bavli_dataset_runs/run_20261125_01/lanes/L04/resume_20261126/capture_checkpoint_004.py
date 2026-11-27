"""Freeze targeted repairs after the third package selection."""
from pathlib import Path
from author_remaining_openings_001 import r
lane=Path(__file__).parent;review=lane/'reviews/capture_004'
external=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/moed_marking_source_only')
for p in sorted(external.glob('*')):
    if p.name in ['production_cohort.json','artifact_hashes.json'] or not p.is_file():continue
    r.immutable(review/'moed_marking_source_only'/p.name,p.read_bytes())
peer=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
for name in ['comparisons/bava_batra_correction001.json','comparisons/pesachim_batch001_exact_version.json','verdicts/pesachim_batch001_v2_verdict.json']:
    r.immutable(review/'review_lead'/name,(peer/name).read_bytes())
manifest=dict(scope='Bounded Moed Katan fresh source-only risk review and exact targeted repair rechecks; Bava Batra targeted correction verification; Pesachim initial targeted finding. No whole-tractate acceptance.',files={p.relative_to(review).as_posix():r.sha(p.read_bytes()) for p in sorted(review.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'})
r.immutable(review/'MANIFEST.json',r.encoded(manifest))
checkpoint=r.read(lane/'LANE_CHECKPOINT_003.json')
selected=dict(moed_katan='849a65e15c05ec5ea4dc6c6d82462aef15507e8d6c2a4b59c8fe8141681b7e1c',pesachim='0e3faae411fe501c3dd3ea74d588088304ac353359690d28dd61066455942902')
for item in checkpoint['packages']:
    slug=item['tractate']
    if slug not in selected:continue
    path=lane/'packages'/slug/selected[slug]/'PACKAGE.json';package=r.read(path)
    item.update(package=path.relative_to(lane).as_posix(),package_sha256=r.sha(path.read_bytes()),snapshot_sha256=selected[slug])
    for key in ['active_records','superseded_records','open_tails','owner']:item[key]=package[key]
    for key in ['completed_by_layer','next_unprocessed_by_layer']:item[key]=package['replay'][key]
checkpoint.update(previous_checkpoint='LANE_CHECKPOINT_003.json',review_manifest='reviews/capture_004/MANIFEST.json',review_manifest_sha256=r.sha((review/'MANIFEST.json').read_bytes()),qualification_notes='All eligibility false. Taanit correction013, Bava Batra correction016 and Moed Katan marking011b/metadata012 targeted rechecks passed with bounded scope and supported uncertainty preserved. Pesachim review007 awaits exact independent recheck. Earlier checkpoints retain known pre-correction errors. Later production is not automatically admitted.')
checkpoint['review_manifests'].append('reviews/capture_004/MANIFEST.json')
r.immutable(lane/'LANE_CHECKPOINT_004.json',r.encoded(checkpoint))
print(checkpoint['completed_unique_segments'],checkpoint['remaining_source_segments'])
