"""Append-only delivery of supplemental Meilah and existing-source AZ comparisons."""
from pathlib import Path
import hashlib, json
R = Path(__file__).resolve().parent
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(name):
    p = R / name
    return {'path': str(p), 'sha256': sha(p)}
def write(name, obj):
    with (R/name).open('x', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2); f.write('\n')
prior = read(R/'DELIVERY_MANIFEST_010.json')
for x in prior['files']:
    p=R/x['path']
    assert sha(p)==x['sha256'] and p.stat().st_size==x['bytes'], x['path']
comparisons=['comparisons/avodah_zarah_batch001_extension002_exact_version.json','comparisons/meilah_supplement003b_exact_version.json']
verdicts=['verdicts/avodah_zarah_batch001_extension002_v2_verdict.json','verdicts/meilah_supplement003b_v2_verdict.json']
for x in comparisons+verdicts: assert (R/x).is_file(), x
coverage=read(R/'COVERAGE_CHECKPOINT_015.json')
coverage.update(direct_fresh_reader_core_segments=1477, deduplicated_union_core_segments=2028,
    union_probability_core_segments=1465, additional_risk_or_endpoint_expansion_segments=252,
    direct_compared_unique_cores=880,
    comparison_count_status='880 historical direct compared coordinate union across exact pinned versions; Meilah003a interrupted before frozen verdict and receives zero comparison credit.',
    new_wave3_reading='Both Meilah003 fresh readers frozen; earlier waves retained. L04 delegated020 launch state is recorded separately, not credited here.',
    supplement_cohort_note='Meilah003:136 new direct cores,61 overlap original probability-plan coordinates,75 outside plan,0 endpoints,0 prior direct overlap. Supplemental selection is not a new probability draw.',
    later_l06_checkpoint013='921 lane-declared cores retained separately.127 manifest file hashes and131 evidence slices from7 overlapping Meilah files verified.61 overlaps with new direct cores; zero aggregate or direct credit from this capture.',
    current_resume_checkpoint='REVIEW_CHECKPOINT_024.json')
j=next(x for x in coverage['jobs'] if x['job_id']=='bavli_meilah')
j.update(direct_fresh_reader_core_segments=275, union_core_segments=285,
    union_probability_segments=130, additional_risk_or_endpoint_expansion_segments=145,
    new_reading_artifacts=['meilah_supplement002','meilah_supplement003a','meilah_supplement003b'])
plan=read(R/'frozen_plans/bavli_meilah.json')
covered=set(read(R/'readings/meilah_batch001.json')['core_refs'])
covered.update(read(R/'jobs/bavli_meilah_supplement002.json')['core_refs'])
for x in 'ab': covered.update(read(R/f'jobs/bavli_meilah_supplement003{x}.json')['core_refs'])
# The previously credited inherited Meilah cohort is the ten opening coordinates.
opening=next(b for b in plan['review_blocks'] if b['block_id']==plan['endpoint_checks']['opening_block_id'])
covered.update(s['ref'] for s in opening['spans'])
assert len(covered)==285
remaining=[b for b in plan['review_blocks'] if any(s['ref'] not in covered for s in b['spans'])]
j['remaining_selected_block_ids']=[b['block_id'] for b in remaining]
j['remaining_selected_core_refs']=[s['ref'] for b in remaining for s in b['spans'] if s['ref'] not in covered]
j['next_selected_block']=remaining[0]['block_id'] if remaining else None
assert 1477+591-40==2028==1465+401-90+252
assert 792+20+68==880
write('COVERAGE_CHECKPOINT_023.json',coverage)
checkpoint={
 'artifact_kind':'independent_review_checkpoint','run_id':'run_20261125_01',
 'status':'ALL37_BOUNDED_READINGS_FULL_REVIEWS_INCOMPLETE','source_inventory_segments':81793,
 'direct_unique_reading_cores':1477,'established_declared_reading_union':2028,
 'direct_compared_coordinate_union':880,
 'cohort_coordinate_union':{'original_probability_plan':1465,'endpoints':401,'probability_endpoint_overlap':90,'additional_risk_or_supplement':252},
 'wave':{'new_direct_reading':136,'new_compared':88,'avodah_zarah_new_probability_comparison':20,'meilah_supplemental_comparison':68,'new_probability_draw':False},
 'interrupted_comparison':bind('INTERRUPTION_CHECKPOINT_026.json'),
 'relation_pattern_assessment':bind('comparisons/meilah_supplement003b_relation_pattern001.json'),
 'external_nedarim_reading_intake':bind('NEDARIM_DELEGATED020_INTAKE_025.json'),
 'comparisons':[bind(x) for x in comparisons],'verdicts':[bind(x) for x in verdicts],
 'reading_validation':bind('VALIDATION_CHECKPOINT_022.json'),
 'remaining_coordinates':bind('COVERAGE_CHECKPOINT_023.json'),
 'separate_inherited_intake':bind('L06_INHERITED_INTAKE_019.json'),
 'l04_overlap_plan':bind('L04_COMPARISON_PLAN_018.json'),
 'l04_external_reader_reservation':bind('L04_SOURCE_RESERVATION_020.json'),
 'l04_reported_launches':bind('L04_DISPATCH_CONFIRMATION_021.json'),
 'external_reading_credit_in_this_checkpoint':0,
 'extraction_coverage_note':'Historical exact observations remain separate from review. No refreshed global extraction aggregate inferred from these readings. L04 exact pins/counts in plan018; Meilah exact comparison pin376f00e4 has403 completed production cores per layer.',
 'provenance_note':'Root readers launched fork:none and frozen before comparison. L06 captured package and L04 launches retain separately reported provenance. AI agreement is not human scholarly certification.',
 'version_scope':'Historical unique coordinates across exact snapshots. Corrections and verdicts do not transfer to newer versions or intervening production.',
 'full_tractates_admitted':0,'new_task_eligible_records':0,'human_scholarly_certification':False,
 'resume':['Resume Meilah003a NONBLIND comparison at exact376f00e4 from interruption026; source-only reading already frozen, do not relaunch or overwrite it. No completed verdict or comparison credit yet.',
 'Read this checkpoint and exact verdict artifacts, including any correction addenda emitted after this freeze.',
 'Collect L04 delegated020 frozen outputs and validate source, coordinates, evidence, provenance and overlap before comparison. Comparator must receive producer pins only after source-only freeze.',
 'Continue remaining original sample blocks for all37 tractates; do not reroll or combine supplemental selection with probability estimands.',
 'Prioritize unresolved targeted defects, exact-version rechecks and already frozen readings newly covered by production; recheck production availability before old noCURRENT queues.',
 'Retain Temurah and Chullin unresolved restrictions unless their exact affected records have a verified correction.'],
 'previous_delivery_files_unchanged':len(prior['files'])}
write('REVIEW_CHECKPOINT_024.json',checkpoint)
files=[]
for p in sorted(R.rglob('*'),key=lambda p:p.relative_to(R).as_posix()):
    if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc' or p.name.startswith('DELIVERY_MANIFEST_'):continue
    files.append({'path':p.relative_to(R).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size})
m={'artifact_kind':'independent_review_delivery_manifest','checkpoint':11,'run_id':'run_20261125_01','absolute_artifact_root':str(R),'previous_manifest_sha256':sha(R/'DELIVERY_MANIFEST_010.json'),'files':files,'file_count':len(files),'total_bytes':sum(x['bytes'] for x in files),'full_tractates_admitted':0}
write('DELIVERY_MANIFEST_011.json',m)
print(json.dumps({'manifest_sha256':sha(R/'DELIVERY_MANIFEST_011.json'),'file_count':m['file_count'],'total_bytes':m['total_bytes']}))
