"""Append-only checkpoint and cumulative delivery; no production or source writes."""
from pathlib import Path
import hashlib, json

R = Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(rel):
    p = R / rel
    return {'path': str(p), 'sha256': sha(p)}
def write_new(name, obj):
    with (R / name).open('x', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')

previous = R / 'DELIVERY_MANIFEST_009.json'
old = json.loads(previous.read_text(encoding='utf-8-sig'))
for item in old['files']:
    p = R / item['path']
    assert p.stat().st_size == item['bytes'] and sha(p) == item['sha256'], item['path']

comparison_files = [f'comparisons/moed_katan_batch00{i}_exact_version.json' for i in (3,4,5)] + ['comparisons/meilah_supplement002_exact_version.json']
verdict_files = [f'verdicts/moed_katan_batch00{i}_v2_verdict.json' for i in (3,4,5)] + ['verdicts/meilah_supplement002_v2_verdict.json']
correction = R / 'comparisons/meilah_supplement002_correction001.json'
assert correction.exists(), 'Finish exact correction recheck before freezing delivery010'
assert (R / 'comparisons/moed_katan_batch005_correction001.json').exists(), 'Finish MK targeted correction recheck before freezing'
checkpoint = {
    'artifact_kind': 'independent_review_checkpoint',
    'run_id': 'run_20261125_01',
    'status': 'ALL37_BOUNDED_READINGS_FULL_REVIEWS_INCOMPLETE',
    'source_inventory_segments': 81793,
    'direct_unique_reading_cores': 1341,
    'inherited_declared_reading_cores': 591,
    'direct_inherited_overlap': 40,
    'declared_reading_union': 1892,
    'direct_compared_coordinate_union': 792,
    'coverage_interpretation': 'Historical source-coordinate unions across exact versions, not whole-snapshot or whole-tractate admission.',
    'cohorts': {'probability_plan_coordinate_coverage': 1404, 'endpoint_coordinate_coverage': 401, 'probability_endpoint_overlap': 90, 'additional_risk_or_supplement_outside_plan': 177},
    'wave': {'moed_katan_original_probability_cores': 90, 'meilah_supplement_core_count': 128, 'meilah_prior_reading_overlap': 19, 'meilah_new_reading_cores': 109, 'meilah_prior_comparison_overlap': 0, 'meilah_new_compared_cores': 128, 'meilah_new_reading_original_plan_overlap': 39, 'meilah_new_reading_outside_plan': 70, 'meilah_new_probability_draw': False},
    'separate_inherited_graves_cores': 27,
    'separate_graves_fresh_reading_credit': 0,
    'extraction_coverage': {'note': 'Separate exact-version observations; no refreshed global extraction aggregate inferred from review progress.', 'historical_metadata': bind('COVERAGE_CHECKPOINT_015.json'), 'later_L04_observations': bind('L04_INTAKE_010.json')},
    'comparisons': [bind(x) for x in comparison_files],
    'initial_verdicts': [bind(x) for x in verdict_files],
    'mandatory_moed_katan_exclusion': bind('comparisons/moed_katan_batch005_attribution_exclusion001.json'),
    'moed_katan_excluded_records': ['mk.r035.debts.a', 'mk.r035.debts.p'],
    'moed_katan_exact_correction_recheck': bind('comparisons/moed_katan_batch005_correction001.json'),
    'moed_katan_correction_scope': 'Only the two attribution records; initial exclusion preserved at its original version. Consult receipt for corrected-version disposition; no extra coverage.',
    'meilah_initial_findings': 'Five missing typed objection links at3b13,4a3,5a10,5b5,7a3; zero whole-content omissions. Initial REWORK_TARGETED verdict retained.',
    'meilah_exact_correction_recheck': bind('comparisons/meilah_supplement002_correction001.json'),
    'meilah_correction_scope': 'Only five targeted findings; no coverage credit or later-production inheritance. Consult correction receipt for exact disposition.',
    'reading_preservation': {'base': bind('readings/meilah_supplement002.json'), 'source_only_completion': bind('readings/meilah_supplement002_completion001.json'), 'note': 'Initial incomplete inventory retained. Source-only completion frozen before producer comparison. Seven reader relation-target errors and one condition error remain documented in comparison.'},
    'dispatch_completion': 'All four fresh source-only readers from this wave finished, including previously prepared Moed Katan batch005. No active reader jobs remain.',
    'remaining_coordinates': bind('COVERAGE_CHECKPOINT_015.json'),
    'full_tractates_admitted': 0,
    'tractates_with_bounded_fresh_readings': 37,
    'new_task_eligible_records': 0,
    'human_scholarly_certification': False,
    'pending_work': ['Continue remaining original selected blocks for all37 tractates from coverage015; keep cohorts distinct.', 'Apply correction dispositions only at their immutable exact versions; preserve exclusions in original versions.', 'Temurah targeted correction and Chullin unsupported addressee exclusion remain open at their pinned versions.', 'Refresh production availability before comparing older noCURRENT or zero-overlap queues; no automatic version inheritance.', 'Coordinate bounded intake with six platform leads to prevent unreviewed backlog.'],
    'previous_delivery_files_unchanged': len(old['files'])
}
assert 1341 + 591 - 40 == 1892 == 1404 + 401 - 90 + 177
assert 574 + 90 + 128 == 792
write_new('REVIEW_CHECKPOINT_016.json', checkpoint)
files = []
for p in sorted(R.rglob('*'), key=lambda p: p.relative_to(R).as_posix()):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix == '.pyc' or p.name.startswith('DELIVERY_MANIFEST_'):
        continue
    files.append({'path': p.relative_to(R).as_posix(), 'sha256': sha(p), 'bytes': p.stat().st_size})
manifest = {'artifact_kind': 'independent_review_delivery_manifest', 'checkpoint': 10, 'run_id': 'run_20261125_01', 'absolute_artifact_root': str(R), 'previous_manifest_sha256': sha(previous), 'files': files, 'file_count': len(files), 'total_bytes': sum(x['bytes'] for x in files), 'full_tractates_admitted': 0}
write_new('DELIVERY_MANIFEST_010.json', manifest)
print(json.dumps({'manifest_sha256': sha(R / 'DELIVERY_MANIFEST_010.json'), 'file_count': len(files), 'total_bytes': manifest['total_bytes'], 'previous_files_unchanged': len(old['files'])}))
