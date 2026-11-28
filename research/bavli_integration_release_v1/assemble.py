"""Deterministic, conservative assembly of frozen Bavli production checkpoints.

No source corpora or producer judgments are modified. This is an integrity-valid
partial research export, not a supervised dataset or a full-tractate admission.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research/bavli_production_v1'))
import runner as r


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe(root, relative):
    path = (root / relative).resolve()
    require(not Path(relative).is_absolute() and path.is_relative_to(root.resolve()), 'Unsafe relative path: ' + str(relative))
    return path


def key(job_id, record_id):
    # JSON tuple encoding prevents delimiter collisions and retains both IDs.
    return json.dumps([job_id, record_id], ensure_ascii=False, separators=(',', ':'))


def dependencies(record):
    return set(record.get('links', [])) | {record['content'][k] for k in
        ('claim_id', 'question_id', 'source_id', 'target_id') if record['content'].get(k)}


def exclusion_closure(job_id, records, entries):
    active = {x['id']: x for x in records if x['release_state'] == 'valid'}
    blocked = {}
    for entry in entries:
        if entry['job_id'] != job_id:
            continue
        record = active.get(entry['record_id'])
        if record is not None and r.sha(r.encoded(record)) == entry['record_sha256']:
            blocked[record['id']] = {'kind': 'exact_version_quarantine', 'reason': entry['reason'], 'entry': entry}
    while True:
        added = {}
        for rid, record in active.items():
            causes = sorted(dependencies(record) & blocked.keys())
            if rid not in blocked and causes:
                added[rid] = {'kind': 'dependent_on_excluded_record', 'dependency_ids': causes}
        if not added:
            return blocked
        blocked.update(added)


def gaps(coordinates, completed):
    result = []
    for row in coordinates:
        if row['id'] not in completed:
            if result and result[-1]['end_ordinal'] == row['ordinal'] - 1:
                result[-1].update(end_ref=row['ref'], end_ordinal=row['ordinal'])
                result[-1]['segments'] += 1
            else:
                result.append(dict(start_ref=row['ref'], end_ref=row['ref'], start_ordinal=row['ordinal'], end_ordinal=row['ordinal'], segments=1))
    return result


def verify_inputs(directory):
    manifest = r.read(directory / 'INPUT_MANIFEST.json')
    policy = r.read(directory / 'POLICY_MANIFEST.json')
    require(policy['input_manifest_sha256'] == r.sha((directory / 'INPUT_MANIFEST.json').read_bytes()), 'Policy targets another capture')
    bound = {}
    for entry in manifest['files'] + policy['files']:
        name = entry['path']
        require(name not in bound, 'Duplicate manifest path')
        raw = safe(directory, name).read_bytes()
        require(r.sha(raw) == entry['sha256'] and len(raw) == entry['bytes'], 'Input hash/size mismatch: ' + name)
        bound[name] = entry
    def read_bound(name):
        require(name in bound, 'Unbound input: ' + name)
        return r.read(safe(directory, name))
    return manifest, read_bound


def assemble(input_dir, output_dir, source_root):
    input_dir, output_dir = Path(input_dir).resolve(), Path(output_dir).resolve()
    require(not output_dir.is_relative_to(input_dir) and not input_dir.is_relative_to(output_dir), 'Input and output directories must be disjoint')
    manifest, read = verify_inputs(input_dir)
    assignments = r.read(ROOT / 'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json')
    expected = {j['job_id']: (lane['lane_id'], j) for lane in assignments['lanes'] for j in lane['jobs']}
    jobs = manifest['jobs']
    require(len(jobs) == 37 and {j['job_id'] for j in jobs} == set(expected), 'Expected exactly the pinned 37 jobs')
    require(sum(j['source_segments'] for j in jobs) == 81793, 'Source denominator must remain 81,793')
    source_manifest = ROOT / 'research/bavli_sugya_corpus_v1/source_manifest.json'
    require(r.sha(source_manifest.read_bytes()) == manifest['source_manifest_sha256'] == r.PIN, 'Source manifest pin mismatch')
    exclusions = read('exclusions.json')['entries']
    review_context = read('review_context.json')
    contract = read('RUN_CONTRACT.json')
    require(r.sha(safe(input_dir, 'RUN_CONTRACT.json').read_bytes()) == manifest['contract_sha256'], 'Contract hash mismatch')
    require(contract['schema_sha256'] == r.hashes()['schema_sha256'] and contract['annotation_protocol_sha256'] == r.hashes()['protocol_sha256'], 'Contract tooling mismatch')
    tables = {layer: [] for layer in r.LAYERS[:-1]}
    history, coverage, review, qualified, unresolved, excluded, mentions, crosslinks, source_rows, sugyot = ([] for _ in range(10))
    lineage = []
    licenses = []
    for job in sorted(jobs, key=lambda x: x['job_id']):
        jid = job['job_id']; base = job['path'].rstrip('/')
        require(job['lane_id'] == expected[jid][0], 'Lane mismatch: ' + jid)
        meta = read(base + '/JOB.json'); owner = read(base + '/OWNER.json')
        state = read(base + '/snapshot.json')
        require(owner['owner'] == job['owner'] and owner['epoch'] == job['epoch'], 'Ownership mismatch: ' + jid)
        require(r.sha(r.encoded(state)) == job['snapshot_sha256'], 'Snapshot hash mismatch: ' + jid)
        require(meta['tractate'] == job['tractate'] and meta['source_sha256'] == job['source_sha256'], 'Source identity mismatch')
        require(all(meta[k] == v for k, v in r.hashes().items()), 'Schema/protocol mismatch')
        source_meta, rows = r.source(source_root, source_manifest, job['tractate'])
        require(len(rows) == job['source_segments'] and source_meta['source_sha256'] == job['source_sha256'], 'Source accounting mismatch')
        coords = read(base + '/source_coordinates.json')
        require(coords == [{k: row[k] for k in ('id', 'ref', 'source_index', 'text_sha256')} for row in rows], 'Coordinate/source mismatch')
        coords = [dict(row, ordinal=i) for i, row in enumerate(coords)]
        by_id = {row['id']: row for row in coords}
        rebuilt = r.empty(); introduced = {}
        owner_history = {owner['epoch']: owner}
        for epoch in range(1, owner['epoch']):
            owner_history[epoch] = read(base + '/ownership_history/' + str(epoch) + '.json')
        for proposal_hash in state['proposals']:
            proposal = read(base + '/proposals/' + proposal_hash + '.json')
            require(owner_history[proposal['epoch']]['owner'] == proposal['owner'], 'Historical proposal owner mismatch')
            require(r.sha(safe(input_dir, base + '/proposals/' + proposal_hash + '.json').read_bytes()) == proposal_hash, 'Proposal hash mismatch')
            for record in proposal['records']:
                introduced[record['id']] = proposal_hash
            prior = rebuilt['proposals']
            rebuilt = r.validate_apply(rebuilt, proposal, {row['id']: row for row in rows}, meta)
            rebuilt['proposals'] = prior + [proposal_hash]
        require(r.encoded(rebuilt) == r.encoded(state), 'Replay mismatch: ' + jid)
        licenses.append(dict(job_id=jid, source_sha256=job['source_sha256'], edition='Wikisource Talmud Bavli', metadata=meta.get('metadata', {})))
        source_rows.extend(dict(job_id=jid, **row) for row in coords)
        blocked = exclusion_closure(jid, state['records'], exclusions)
        active = [record for record in state['records'] if record['release_state'] == 'valid']
        accepted = [record for record in active if record['id'] not in blocked]
        for record in state['records']:
            rid = record['id']
            wrapper = dict(corpus_key=key(jid, rid), job_id=jid, native_record_id=rid,
                snapshot_sha256=job['snapshot_sha256'], record_sha256=r.sha(r.encoded(record)),
                introducing_proposal_sha256=introduced[rid], record=record,
                dependency_keys=[key(jid, x) for x in sorted(dependencies(record))],
                assembly_state='excluded' if rid in blocked else 'superseded' if record['release_state'] != 'valid' else 'integrity_valid_partial_unqualified')
            history.append(wrapper)
            if record.get('supersedes'):
                lineage.append(dict(new_key=wrapper['corpus_key'], supersedes_key=key(jid, record['supersedes']), job_id=jid))
            if rid in blocked:
                excluded.append(dict(corpus_key=wrapper['corpus_key'], job_id=jid, record_sha256=wrapper['record_sha256'], **blocked[rid]))
            if record in accepted:
                tables[record['layer']].append(wrapper)
                qualified.append(dict(corpus_key=wrapper['corpus_key'], snapshot_sha256=job['snapshot_sha256'], ml_eligible=False,
                    supervised_task_eligible=False, reason='No frozen task policy or exact-version task qualification admitted'))
            if record['uncertainty']:
                unresolved.append(dict(corpus_key=wrapper['corpus_key'], snapshot_sha256=job['snapshot_sha256'], assembly_state=wrapper['assembly_state'], uncertainty=record['uncertainty']))
            if record['layer'] == 'attributions':
                # One occurrence per evidence span. Same spelling never merges people.
                for index, evidence in enumerate(record['evidence']):
                    mentions.append(dict(mention_key=key(jid, rid) + '/' + str(index), record_key=wrapper['corpus_key'],
                        surface=record['content']['surface'], role=record['content']['role'],
                        identity_candidates=record['content']['candidates'], transmission_chain=record['content']['transmission_chain'],
                        evidence=evidence, assembly_state=wrapper['assembly_state'], resolved_entity_id=None))
            if record['layer'] == 'edges' and record['content'].get('relation') in ('parallel', 'quotation', 'same_report', 'candidate_similarity', 'related_topic'):
                crosslinks.append(dict(record_key=wrapper['corpus_key'], raw_record=record, reconciliation='unreconciled_no_family_merge', assembly_state=wrapper['assembly_state']))
        layer_rows = {}
        for layer in r.LAYERS:
            cells = [cell for cell in state['coverage'] if cell['layer'] == layer]
            completed = {cell['segment_id'] for cell in cells if cell['extraction_state'] == 'completed'}
            layer_rows[layer] = dict(required_segments=len(coords), completed_segments=len(completed), missing_ranges=gaps(coords, completed),
                outcomes={outcome: sum(cell['extraction_result'] == outcome for cell in cells) for outcome in ('records_found', 'none_found_after_pass', 'abstained_ambiguous', 'not_applicable')})
        coverage.append(dict(job_id=jid, tractate=job['tractate'], lane_id=job['lane_id'], owner=job['owner'], epoch=job['epoch'],
            snapshot_sha256=job['snapshot_sha256'], source_segments=len(coords), layers=layer_rows,
            full_tractate_admitted=False, active_records=len(active), included_partial_records=len(accepted), excluded_records=len(blocked)))
        review.append(dict(job_id=jid, snapshot_sha256=job['snapshot_sha256'], full_review_admitted=False,
            status='No complete exact-version independent review admitted by this assembly',
            partial_review_evidence=next((x for x in review_context['jobs'] if x['job_id']==jid), {})))
        for tail in state['open_tails']:
            unresolved.append(dict(job_id=jid, snapshot_sha256=job['snapshot_sha256'], kind='open_tail', value=tail))
        for structure in (x for x in accepted if x['layer'] == 'structure'):
            segment_ids = {e['segment_id'] for e in structure['evidence']}
            # The production structure is an interval in source order, even when
            # its evidence cites only endpoints. These are contextual, not edges.
            first = min(by_id[s]['ordinal'] for s in segment_ids)
            last = max(by_id[s]['ordinal'] for s in segment_ids)
            context_ids = {row['id'] for row in coords[first:last + 1]}
            sugyot.append(dict(sugya_key=key(jid, structure['id']), job_id=jid, native_structure_id=structure['id'],
                title=structure['content']['title'], snapshot_sha256=job['snapshot_sha256'],
                contextual_segment_refs=[row['ref'] for row in coords[first:last + 1]],
                contextual_record_keys=[key(jid, record['id']) for record in accepted if {e['segment_id'] for e in record['evidence']} & context_ids],
                membership_policy='Source-segment overlap only; neither semantic attachment nor unique ownership; shared-segment mentions may belong to adjacent sugyot'))
    generated = {}
    def emit(name, value, jsonl=False):
        raw = b''.join(r.encoded(row) for row in value) if jsonl else r.encoded(value)
        generated[name] = raw
    for layer, records in tables.items(): emit('tables/' + layer + '.jsonl', records, True)
    for name, value in [('history/records', history), ('history/supersession', lineage), ('qualification_ledger', qualified),
        ('unresolved_ledger', unresolved), ('exclusion_ledger', excluded), ('entity_mentions', mentions), ('cross_link_proposals', crosslinks), ('source_coordinates', source_rows)]:
        emit(name + '.jsonl', value, True)
    emit('coverage_matrix.json', coverage); emit('review_matrix.json', review); emit('SOURCE_LICENSES.json', licenses)
    emit('REVIEW_CONTEXT.json', review_context)
    for sugya in sugyot:
        emit('per_sugya/' + r.sha(sugya['sugya_key'].encode()) + '.json', sugya)
    emit('per_sugya/INDEX.json', [dict(sugya_key=s['sugya_key'], file=r.sha(s['sugya_key'].encode()) + '.json') for s in sugyot])
    emit('SUPERVISED_EXPORT_POLICY.json', dict(status='BLOCKED_NO_EXPORT', eligible_records=0,
        required_before_export=['Freeze task question, population, labels and input recipe', 'Admit exact-version qualification and review',
            'Group repeated reports, direct parallels, source overlap and generated derivatives before splits',
            'Audit input cutoffs, titles, summaries, aliases, rationales, continuations and retrieval for answer leakage',
            'Record unknown model pretraining exposure separately'], family_grouping='UNRESOLVED_NO_FAMILIES_INFERRED',
        source_overlap='Coordinates retained; contextual overlap is not a semantic equivalence family',
        optional_enrichment_blocks_core=False))
    emit('ENTITY_AND_LINK_POLICY.json', dict(entity_identity_merges=0, confirmed_cross_tractate_families=0,
        policy='Preserve native occurrences, candidate identity alternatives and transmission roles. No name-based person merge. Raw link proposals retain their own relation; related topics and candidate similarity are not equivalence.',
        global_proposal_status='No separately admitted global entity or cross-tractate link proposals supplied'))
    paragraphs = ['<!doctype html><html lang="he" dir="rtl"><meta charset="utf-8"><title>קורפוס בבלי — תוצר חלקי</title>',
        '<style>body{font:18px serif;max-width:1100px;margin:2em auto;padding:1em}article{border-bottom:1px solid #aaa;padding:1em}code{direction:ltr;unicode-bidi:isolate}blockquote{background:#f4f4f4;padding:1em}small{display:block}summary{cursor:pointer}</style>',
        '<h1>קורפוס בבלי — תוצר מחקר חלקי</h1><p>ציטוטי ראיות מוגבלים מן המהדורה Wikisource Talmud Bavli. ההסברים והכותרות הם נתוני ההפקה, ולא טקסט המקור. אין אישור מלא למסכת או כשירות להערכה מפוקחת. רשומות מוחרגות אינן מוצגות כאן.</p>']
    source_ref = {(row['job_id'], row['id']): row['ref'] for row in source_rows}
    for layer in r.LAYERS[:-1]:
        paragraphs.append('<h2>' + html.escape(layer) + '</h2>')
        for wrapper in tables[layer]:
            record = wrapper['record']; paragraphs.append('<article><details><summary><code>' + html.escape(wrapper['corpus_key']) + '</code></summary>')
            for evidence in record['evidence']:
                ref = source_ref[(wrapper['job_id'], evidence['segment_id'])]
                paragraphs.append('<small>' + html.escape(ref) + '</small><blockquote>' + html.escape(evidence['quote']) + '</blockquote>')
            paragraphs.append('<p>נתוני פרשנות/ייחוס:</p><pre dir="auto">' + html.escape(json.dumps(record['content'], ensure_ascii=False, indent=2)) + '</pre><p>' + html.escape('; '.join(record['uncertainty'])) + '</p></details></article>')
    paragraphs.append('</html>'); generated['reader.html'] = '\n'.join(paragraphs).encode('utf-8')
    totals = {layer: sum(j['layers'][layer]['completed_segments'] for j in coverage) for layer in r.LAYERS}
    result = dict(format_version='1.0', status='PARTIAL_REQUIRED_WORK_REMAINS', run_id=manifest['run_id'],
        input_manifest_sha256=r.sha((input_dir / 'INPUT_MANIFEST.json').read_bytes()), contract_sha256=manifest['contract_sha256'],
        policy_manifest_sha256=r.sha((input_dir / 'POLICY_MANIFEST.json').read_bytes()),
        assembly_code_sha256=r.sha(Path(__file__).read_bytes()), source_manifest_sha256=manifest['source_manifest_sha256'],
        tractates_required=37, full_tractates_admitted=0, source_denominator=81793, completed_segments_by_layer=totals,
        included_partial_records=sum(map(len, tables.values())), preserved_record_versions=len(history), exclusions=len(excluded),
        task_eligible_records=0, entity_identity_merges=0,
        files=[dict(path=name, sha256=r.sha(raw), bytes=len(raw)) for name, raw in sorted(generated.items())])
    emit('OUTPUT_MANIFEST.json', result)
    # Existing outputs must match exactly; never silently mutate an old release.
    if output_dir.exists():
        existing = {str(p.relative_to(output_dir)).replace('\\', '/') for p in output_dir.rglob('*') if p.is_file()}
        require(existing <= generated.keys(), 'Unexpected existing output files')
    for name, raw in sorted(generated.items()): r.immutable(safe(output_dir, name), raw)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-root', type=Path, required=True)
    args = parser.parse_args()
    result = assemble(args.input, args.output, args.source_root)
    print(json.dumps({k: v for k, v in result.items() if k != 'files'}, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__': main()
