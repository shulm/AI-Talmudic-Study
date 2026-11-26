"""Additive delivery freeze; run only after queue007 comparators finish."""
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parent
def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name, value):
    with (R / name).open('x', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write('\n')

previous = read(R / 'DELIVERY_MANIFEST_005.json')
for row in previous['files']:
    assert sha(R / row['path']) == row['sha256'], row['path']
queue = read(R / 'COMPARISON_QUEUE_007.json')
rows = []
binding_checks = []
def check_bindings(x):
    if isinstance(x, dict):
        if isinstance(x.get('path'), str) and isinstance(x.get('sha256'), str):
            p = Path(x['path'])
            if not p.is_absolute():
                p = R / p
            assert p.is_file(), str(p)
            assert sha(p) == x['sha256'], str(p)
            binding_checks.append(str(p))
        for y in x.values():
            check_bindings(y)
    elif isinstance(x, list):
        for y in x:
            check_bindings(y)

for entry in queue:
    row = dict(entry)
    row['full_tractate_admission'] = False
    row['task_eligibility_changed'] = False
    if 'snapshot_path' not in entry:
        row['compared_core_refs'] = []
        row['unique_compared_cores'] = 0
        rows.append(row)
        continue
    p = R / 'comparisons' / (entry['job_id'][6:] + '_batch001_exact_version.json')
    d = read(p)
    check_bindings(d['bindings'])
    assert d['bindings']['snapshot']['sha256'] == entry['snapshot_sha256']
    refs = d.get('compared_core_refs', d.get('layer_matrix', {}).get('compared_core_refs'))
    assert isinstance(refs, list), p
    assert len(refs) == len(set(refs)), p
    job = read(R / 'jobs' / (entry['job_id'] + '.json'))
    blocks = job.get('selected_blocks', job.get('review_blocks'))
    prob = {ref for b in blocks if 'probability_sample' in b['roles'] for ref in b['core_refs']}
    end = {ref for b in blocks if any(s in b['roles'] for s in ['opening_check', 'closing_check']) for ref in b['core_refs']}
    rs = set(refs)
    row.update(comparison_path=str(p.relative_to(R)), comparison_sha256=sha(p),
               compared_core_refs=refs, unique_compared_cores=len(rs),
               probability_compared=len(rs & prob), endpoint_compared=len(rs & end),
               probability_endpoint_overlap=len(rs & prob & end))
    vp = R / 'verdicts' / (entry['job_id'][6:] + '_batch001_v2_verdict.json')
    if rs:
        vd = read(vp)
        check_bindings(vd.get('bindings', {}))
        row.update(status=vd['verdict'], verdict_path=str(vp.relative_to(R)), verdict_sha256=sha(vp))
    else:
        assert not vp.exists(), vp
        row['status'] = 'PENDING_PRODUCTION_ZERO_SAMPLED_OVERLAP'
    rows.append(row)

new_count = sum(r['unique_compared_cores'] for r in rows)
report = dict(artifact_kind='exact_version_comparison_checkpoint', jobs=rows,
    previous_compared_cores=242, new_compared_cores=new_count,
    cumulative_direct_compared_cores=242 + new_count,
    source_inventory_segments=81793, direct_fresh_reading_cores=1050,
    declared_reading_union_including_inherited=1601,
    extraction_observation='PRODUCTION_OBSERVATION_006.json; sequential version pins, not atomic release; 3538 claim-completed segments',
    full_tractates_admitted=0, new_task_eligible_records=0, human_scholarly_certification=False,
    checked_binding_occurrences=len(binding_checks), previous193files_unchanged=True,
    remaining_selected_coordinates='COVERAGE_CHECKPOINT_007.json',
    later_l04_versions='L04_INTAKE_008.json; pending separate review',
    risk_screen='RISK_SCREEN_006.json:238 risk candidates, not confirmed errors or probability estimates')
write('COMPARISON_CHECKPOINT_008.json', report)
text = f'''# Independent review checkpoint 008

All37 tractates have frozen bounded source-only readings:1050 direct cores and3344 exact evidence occurrences. Including591 inherited lane-declared cores and40 overlaps, the declared reading union is1601. Inherited provenance remains distinct from fresh-reader provenance.

Queue007 now has17 exact-version comparison receipts. New comparison coverage is{new_count} unique cores; cumulative direct comparison coverage is{242 + new_count}. Zero sampled overlap receives a pending-production receipt, not a semantic verdict or omission claim. Six jobs had no CURRENT at the pinned observation. Probability, opening/closing and overlap counts remain separate in COMPARISON_CHECKPOINT_008.json.

Temurah and Niddah require targeted corrections. Both initial readings, reader errors, producer findings and unresolved alternatives remain preserved. Pesachim correction001 was verified at its exact version. Historical rework verdicts remain immutable. Chullin's unsupported addressee-as-quoted-authority exclusion remains uncleared.

Source inventory:81793 segments. Extraction observation006:3538 claim-completed segments across sequential individual pins, distinct from the earlier2450-segment integration assembly and historical1048 audit. Review coverage is not extraction coverage. Full admission remains0/37; no new task eligibility and no human scholarly certification.

Resume from COVERAGE_CHECKPOINT_007.json for precise remaining selected blocks, COMPARISON_CHECKPOINT_008.json for pinned outcomes, and L04_INTAKE_008.json plus L04_COMPARISON_PLAN_008.json for newer production awaiting review. Original queue007 pins must not be replaced by CURRENT. RISK_SCREEN_006.json contains238 automated candidates only; policy impact006 forbids automatic relabeling or treating them as confirmed source errors. Never pass this annotated checkpoint to fresh source-only readers.
'''
with (R / 'REVIEW_CHECKPOINT_008.md').open('x', encoding='utf-8') as f:
    f.write(text)
files = []
for p in sorted(R.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix == '.pyc' or p.name.startswith('DELIVERY_MANIFEST_'):
        continue
    files.append(dict(path=p.relative_to(R).as_posix(), sha256=sha(p), bytes=p.stat().st_size))
manifest = dict(artifact_kind='independent_review_delivery_manifest', checkpoint=6,
    run_id='run_20261125_01', absolute_artifact_root=str(R),
    previous_manifest_sha256=sha(R / 'DELIVERY_MANIFEST_005.json'), files=files,
    file_count=len(files), total_bytes=sum(x['bytes'] for x in files), full_tractates_admitted=0)
write('DELIVERY_MANIFEST_006.json', manifest)
print(json.dumps(dict(files=len(files), bytes=manifest['total_bytes'], manifest_sha256=sha(R / 'DELIVERY_MANIFEST_006.json'), new_compared=new_count, total_compared=242+new_count)))
