"""Append-only source-only review preparation. No producer annotation inputs.

Run with Python -B -X utf8. Existing output bytes are never replaced.
Re-running verifies all hashes and reproduces the same inventory and queue.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
OUT = Path(__file__).resolve().parent
SOURCE = Path('F:/Sefaria-Export-master')
RUN = ROOT / 'research/bavli_dataset_runs/run_20261125_01'
SEED = 20261125

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def encoded(obj):
    return (json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def binding(path):
    return {'path': path.resolve().as_posix(), 'sha256': sha(path.read_bytes())}

def publish(path, raw):
    require(path.resolve().is_relative_to(OUT), 'Output outside exclusive directory')
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open('xb') as f:
            f.write(raw)
    except FileExistsError:
        require(path.read_bytes() == raw, 'Preserved existing file differs: ' + str(path))
    return binding(path)

def main():
    pointer_path = ROOT / 'research/bavli_dataset_runs/ACTIVE_RUN.json'
    pointer = json.loads(pointer_path.read_bytes())
    contract_path = ROOT / pointer['contract_path']
    require(sha(contract_path.read_bytes()) == pointer['contract_sha256'], 'Exact contract hash mismatch')
    contract = json.loads(contract_path.read_bytes())
    require(contract['run_id'] == pointer['run_id'] == 'run_20261125_01', 'Wrong run')
    require(contract['production_git_commit'] == pointer['production_git_commit'], 'Production commit mismatch')
    require(contract['review_plan_seed'] == SEED, 'Seed mismatch')
    require(contract['review_packet_policy'] == 'fresh_source_only_contexts', 'Packet policy mismatch')
    production_checks = []
    for rel, expected in contract['production_files'].items():
        path = ROOT / rel
        require(sha(path.read_bytes()) == expected, 'Production file hash mismatch: ' + rel)
        production_checks.append(binding(path))
    protocol = ROOT / contract['annotation_protocol_file']
    schema = ROOT / contract['output_schema_files'][0]
    require(sha(protocol.read_bytes()) == contract['annotation_protocol_sha256'], 'Protocol hash mismatch')
    require(sha(schema.read_bytes()) == contract['schema_sha256'], 'Schema hash mismatch')
    require(json.loads(schema.read_bytes())['properties']['schema_version']['const'] == contract['schema_version'], 'Schema version mismatch')
    manifest_path = ROOT / 'research/bavli_sugya_corpus_v1/source_manifest.json'
    require(sha(manifest_path.read_bytes()) == contract['source_manifest_sha256'], 'Source manifest mismatch')
    manifests = {x['title']: x for x in json.loads(manifest_path.read_bytes())['tractates']}
    assignments_path = ROOT / 'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json'
    require(sha(assignments_path.read_bytes().replace(b'\r\n', b'\n')) == contract['assignments_sha256'], 'Assignment canonical-LF hash mismatch')
    jobs_path = ROOT / 'research/bavli_dataset_program_v2/jobs.json'
    jobs = json.loads(jobs_path.read_bytes())['jobs']
    require(len(jobs) == len({j['job_id'] for j in jobs}) == len(manifests) == 37, 'Expected 37 jobs')
    tool_path = ROOT / 'research/bavli_dataset_program_v2/tools/make_review_plan.py'
    spec = importlib.util.spec_from_file_location('source_only_plan', tool_path)
    tool = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tool)
    common = []
    for path in [protocol, schema, ROOT / 'research/bavli_dataset_program_v2/INDEPENDENT_REVIEW_PROMPT.md']:
        copy = publish(OUT / 'source_only_common' / path.name, path.read_bytes())
        common.append({'original': binding(path), 'copy': copy})
    totals = dict(jobs=0, source_nonempty_segments=0, source_segment_positions=0,
                  probability_blocks=0, probability_core_segments=0, endpoint_blocks=0,
                  endpoint_core_segments=0, endpoint_overlap_blocks=0,
                  endpoint_overlap_core_segments=0, endpoint_added_blocks=0,
                  endpoint_added_core_segments=0, union_blocks=0, union_core_segments=0)
    inventory, queue = [], []
    for job in sorted(jobs, key=lambda j: j['queue_priority']):
        jid, title = job['job_id'], job['tractate']
        source_path = SOURCE / job['source_path']
        source_schema = SOURCE / job['source_schema_path']
        require(sha(source_path.read_bytes()) == job['expected_source_sha256'], 'Source hash mismatch: ' + jid)
        require(sha(source_schema.read_bytes()) == job['source_schema_sha256'], 'Original schema hash mismatch: ' + jid)
        manifest = manifests[title]
        require(manifest['source_sha256'] == job['expected_source_sha256'], 'Manifest/job hash mismatch: ' + jid)
        require(manifest['source_path'] == job['source_path'], 'Manifest/job source path mismatch: ' + jid)
        original_plan_path = RUN / 'review_plans' / (jid + '.json')
        original_bytes = original_plan_path.read_bytes()
        original = json.loads(original_bytes)
        rebuilt = tool.make_plan(source_path, title, job['expected_source_sha256'], SEED)
        require(rebuilt == original, 'Plan replay mismatch: ' + jid)
        require(encoded(rebuilt) == original_bytes, 'Byte-exact sorted-key plan replay mismatch: ' + jid)
        require(tool.plan_digest(original) == original['plan_sha256'], 'Plan domain hash mismatch: ' + jid)
        require(original['status'] == 'PLAN_ONLY_NOT_REVIEWED', 'Unexpected plan status')
        require(original['source_inventory']['nonempty_segments'] == job['expected_total_source_segments'], 'Segment count mismatch: ' + jid)
        plan_copy = publish(OUT / 'frozen_plans' / (jid + '.json'), original_bytes)
        blocks = original['review_blocks']
        probability = [b for b in blocks if 'probability_sample' in b['roles']]
        endpoints = [b for b in blocks if {'opening_check', 'closing_check'} & set(b['roles'])]
        overlap = [b for b in endpoints if 'probability_sample' in b['roles']]
        added = [b for b in endpoints if 'probability_sample' not in b['roles']]
        counts = {'source_nonempty_segments': original['source_inventory']['nonempty_segments'],
                  'source_segment_positions': original['source_inventory']['segment_positions']}
        for label, group in [('probability', probability), ('endpoint', endpoints), ('endpoint_overlap', overlap), ('endpoint_added', added), ('union', blocks)]:
            counts[label + '_blocks'] = len(group)
            counts[label + '_core_segments'] = sum(len(b['spans']) for b in group)
        require(counts['union_core_segments'] == counts['probability_core_segments'] + counts['endpoint_added_core_segments'], 'Core union inconsistency')
        descriptor = {'artifact_kind': 'neutral_source_only_review_job_not_a_reading',
                      'status': 'PENDING_SOURCE_FIRST_READING', 'job_id': jid, 'tractate': title,
                      'run_id': contract['run_id'], 'source': binding(source_path),
                      'original_source_schema': binding(source_schema),
                      'frozen_plan': plan_copy, 'original_frozen_plan': binding(original_plan_path),
                      'plan_sha256': original['plan_sha256'], 'seed': SEED,
                      'common_documents': [c['copy'] for c in common],
                      'counts': counts, 'sampling': original['sampling'],
                      'selected_blocks': [{'block_id': b['block_id'], 'roles': b['roles'],
                                           'inclusion_probability': b['inclusion_probability'],
                                           'review_union_inclusion_probability': b['review_union_inclusion_probability'],
                                           'core_refs': [s['ref'] for s in b['spans']]} for b in blocks],
                      'blindness_policy': 'Fresh source-only context required; infrastructure verification is not independent semantic reading.',
                      'context_expansions': [], 'producer_annotations_included': False,
                      'completed_readings': 0, 'risk_review': 'NOT_SELECTED_OR_PERFORMED',
                      'instructions': 'Read selected cores and full relevant original continuations. Freeze source-anchored substantive findings before any producer comparison. Keep probability, endpoint, overlap, and context-expansion denominators separate.'}
        desc = publish(OUT / 'jobs' / (jid + '.json'), encoded(descriptor))
        inventory.append({'job_id': jid, 'tractate': title, 'queue_priority': job['queue_priority'],
                          'source': binding(source_path), 'frozen_plan': plan_copy,
                          'original_frozen_plan': binding(original_plan_path), 'descriptor': desc,
                          'plan_sha256': original['plan_sha256'], 'counts': counts})
        for b in blocks:
            queue.append({'queue_index': len(queue) + 1, 'job_id': jid,
                          'block_id': b['block_id'], 'roles': b['roles'],
                          'core_refs': [s['ref'] for s in b['spans']],
                          'status': 'PENDING_SOURCE_FIRST_READING', 'descriptor_sha256': desc['sha256'],
                          'source_sha256': job['expected_source_sha256'],
                          'plan_file_sha256': plan_copy['sha256']})
        totals['jobs'] += 1
        for key, count in counts.items():
            totals[key] += count
    require(totals['source_nonempty_segments'] == 81793, 'Total source count mismatch')
    inv = publish(OUT / 'inventory.json', encoded({'status': 'PREPARED_NOT_REVIEWED', 'totals': totals, 'jobs': inventory}))
    queued = publish(OUT / 'pending_queue.json', encoded({'status': 'ALL_CORE_READINGS_PENDING', 'queue_order': 'Original jobs queue_priority, then original block source order; no reroll.', 'blocks': queue}))
    results = {'status': 'PASS_INFRASTRUCTURE_ONLY', 'source_sha256_checks': 37,
               'original_source_schema_sha256_checks': 37, 'plan_domain_hash_checks': 37,
               'plan_semantic_replays': 37, 'plan_byte_exact_replays': 37,
               'seed': SEED, 'totals': totals, 'independent_semantic_readings_completed': 0,
               'producer_annotations_inspected': False, 'risk_review_completed': False,
               'active_run': binding(pointer_path), 'run_contract': binding(contract_path),
               'source_manifest': binding(manifest_path), 'jobs_input': binding(jobs_path),
               'assignments': binding(assignments_path), 'production_files': production_checks,
               'plan_generator': binding(tool_path), 'verification_script': binding(Path(__file__)),
               'common_documents': common, 'inventory': inv, 'pending_queue': queued,
               'limitations': ['Plans and source hashes do not establish scholarly accuracy or semantic review.',
                               'No producer comparison, adjudication, full-tractate receipt, or task eligibility is claimed.',
                               'Queue is an immutable initial checkpoint; subsequent readings need a separate append-only progress ledger.']}
    result_binding = publish(OUT / 'verification_results.json', encoded(results))
    checkpoint = {'status': 'READY_FOR_FRESH_SOURCE_ONLY_READERS', 'verification_results': result_binding,
                  'inventory': inv, 'pending_queue': queued, 'next_queue_index': 1,
                  'completed_core_readings': 0, 'pending_blocks': totals['union_blocks'],
                  'pending_unique_source_cores': totals['union_core_segments'],
                  'resume': 'Verify this checkpoint and its hashes; dispatch jobs/<job_id>.json to fresh source-only contexts. Preserve immutable initial queue and append actual completed reading hashes in a separate progress ledger; never infer completion from these descriptors.'}
    publish(OUT / 'RESUME_CHECKPOINT.json', encoded(checkpoint))
    print(json.dumps({'status': results['status'], 'totals': totals, 'checkpoint': str(OUT / 'RESUME_CHECKPOINT.json')}))

if __name__ == '__main__':
    main()
