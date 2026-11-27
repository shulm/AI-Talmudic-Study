"""Freeze the third selected package cohort and existing review receipts."""
from pathlib import Path
from author_remaining_openings_001 import r
lane=Path(__file__).parent
external=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/taanit_frozen_comparison')
review=lane/'reviews/capture_003'
for p in sorted(external.glob('*.json')):
    # Avoid redundant production snapshot copies and internal selection inventory.
    if p.name.startswith('snapshot_') or p.name=='remaining_covered_unreviewed_inputs.json':continue
    r.immutable(review/'taanit_frozen_comparison'/p.name,p.read_bytes())
peer=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
for name in ['comparisons/bava_batra_batch001_exact_version.json','verdicts/bava_batra_batch001_v2_verdict.json','comparisons/taanit_correction001.json']:
    p=peer/name;r.immutable(review/'review_lead'/name,p.read_bytes())
manifest=dict(scope='Exact-version comparisons and targeted checks. Taanit seven corrections verified, three uncertainties retained. Bava Batra initial rework findings retained; correction016 independent recheck pending at capture. No full-tractate acceptance.',files={p.relative_to(review).as_posix():r.sha(p.read_bytes()) for p in sorted(review.rglob('*')) if p.is_file() and p.name!='MANIFEST.json'})
r.immutable(review/'MANIFEST.json',r.encoded(manifest))
checkpoint=r.read(lane/'LANE_CHECKPOINT_002.json')
selected=dict(taanit='9936408e656e02d42c8df7d80f8803e7f37cc0565ec53449e03056cad69ab017',bava_batra='95c61e5e4d60466f3ebb56f5fd491908d64e0f3320e901e9d7220beed5d46940',nedarim='c83f585cd6b9b1b178dbcb7938d843d70e7e51515f32d85093388c0620c15268',moed_katan='8fc9976cc33de5e7d5bfec044e42b7d5eb329a0aad1e5d7f2b0209537b88a40e')
for item in checkpoint['packages']:
    slug=item['tractate']
    if slug not in selected:continue
    path=lane/'packages'/slug/selected[slug]/'PACKAGE.json';package=r.read(path)
    item.update(package=path.relative_to(lane).as_posix(),package_sha256=r.sha(path.read_bytes()),snapshot_sha256=selected[slug])
    for key in ['active_records','superseded_records','open_tails','owner']:item[key]=package[key]
    for key in ['completed_by_layer','next_unprocessed_by_layer']:item[key]=package['replay'][key]
checkpoint['completed_unique_segments']=sum(x['completed_by_layer']['structure'] for x in checkpoint['packages'])
checkpoint['remaining_source_segments']=13593-checkpoint['completed_unique_segments']
checkpoint.update(previous_checkpoint='LANE_CHECKPOINT_002.json',review_manifest='reviews/capture_003/MANIFEST.json',review_manifest_sha256=r.sha((review/'MANIFEST.json').read_bytes()),qualification_notes='All eligibility false. Taanit correction013 targeted independent check passed with three uncertainties preserved; later additions not review-accepted. Bava Batra correction016 awaits independent recheck. Earlier checkpoints retain known pre-correction errors. Moed Katan new risk review pending.')
checkpoint['review_manifests'].append('reviews/capture_003/MANIFEST.json')
r.immutable(lane/'LANE_CHECKPOINT_003.json',r.encoded(checkpoint))
print(checkpoint['completed_unique_segments'],checkpoint['remaining_source_segments'])
