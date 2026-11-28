"""Freeze verified production proposals without editing producer state."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'research/bavli_production_v1'))
import runner as r

def capture(ledger_path, output):
    ledger_path, output = Path(ledger_path), Path(output)
    ledger = r.read(ledger_path)
    run = ledger_path.parent
    contract = r.read(run / 'RUN_CONTRACT.json')
    expected = r.read(ROOT / 'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json')
    ids = {j['job_id'] for lane in expected['lanes'] for j in lane['jobs']}
    assert len(ledger['jobs']) == 37 and {j['job_id'] for j in ledger['jobs']} == ids
    jobs = []
    for job in ledger['jobs']:
        directory = Path(job['job_dir'])
        dest = output / 'jobs' / job['job_id']
        with r.lock(directory):
            meta, source = r.load(directory)
            owner = r.read(directory / 'OWNER.json')
            previous = dict(owner=job['owner'], epoch=job['epoch'])
            assert owner['epoch'] >= previous['epoch']
            history = {owner['epoch']: owner}
            for p in sorted((directory / 'ownership_history').glob('*.json')):
                entry = r.read(p)
                assert str(entry['epoch']) == p.stem
                history[entry['epoch']] = entry
                r.immutable(dest / 'ownership_history' / p.name, p.read_bytes())
            assert history[previous['epoch']] == previous, 'ledger owner is not in preserved lineage'
            assert set(history) == set(range(1, owner['epoch'] + 1)), 'ownership history gap'
            state = r.current(directory)
            rebuilt = r.empty()
            for h in state['proposals']:
                raw = (directory / 'proposals' / (h + '.json')).read_bytes()
                assert r.sha(raw) == h
                proposal = json.loads(raw)
                assert history[proposal['epoch']]['owner'] == proposal['owner'], 'proposal owner/epoch not admitted in history'
                prior = rebuilt['proposals']
                rebuilt = r.validate_apply(rebuilt, proposal, source, meta)
                rebuilt['proposals'] = prior + [h]
                r.immutable(dest / 'proposals' / (h + '.json'), raw)
            assert r.encoded(state) == r.encoded(rebuilt), 'deterministic replay mismatch'
            r.immutable(dest / 'snapshot.json', r.encoded(state))
            r.immutable(dest / 'JOB.json', (directory / 'JOB.json').read_bytes())
            r.immutable(dest / 'OWNER.json', r.encoded(owner))
            coordinates = [{k: x[k] for k in ['id', 'ref', 'source_index', 'text_sha256']} for x in source.values()]
            r.immutable(dest / 'source_coordinates.json', r.encoded(coordinates))
            jobs.append(dict(job_id=job['job_id'], tractate=job['tractate'], lane_id=job['lane_id'],
                **owner, previous_owner=previous, path='jobs/' + job['job_id'],
                snapshot_sha256=r.sha(r.encoded(state)), source_segments=len(source),
                source_sha256=meta['source_sha256'], proposal_count=len(state['proposals']),
                validation=dict(source_integrity='PASS', schema_and_replay='PASS', ownership_lineage='PASS'),
                completed_source_segments_by_layer={layer: sum(c['layer']==layer and c['extraction_state']=='completed' for c in state['coverage']) for layer in r.LAYERS}))
    assert sum(j['source_segments'] for j in jobs) == 81793
    r.immutable(output / 'coordinator_ledger_at_capture.json', ledger_path.read_bytes())
    r.immutable(output / 'RUN_CONTRACT.json', (run / 'RUN_CONTRACT.json').read_bytes())
    files = [dict(path=p.relative_to(output).as_posix(), sha256=r.sha(p.read_bytes()), bytes=p.stat().st_size)
             for p in sorted(output.rglob('*')) if p.is_file() and p.name != 'INPUT_MANIFEST.json']
    manifest = dict(run_id=contract['run_id'], contract_sha256=r.sha((run/'RUN_CONTRACT.json').read_bytes()),
        source_manifest_sha256=r.PIN, source_segments=81793, assignment_revision=ledger['revision'],
        capture_script_sha256=r.sha(Path(__file__).read_bytes()), jobs=jobs, files=files,
        scope='Per-job immutable capture; not a simultaneous wall-clock snapshot or full scholarly review. Later producer versions excluded.')
    r.immutable(output / 'INPUT_MANIFEST.json', r.encoded(manifest))
    print(json.dumps(dict(jobs=len(jobs), files=len(files), manifest_sha256=r.sha(r.encoded(manifest)),
        completed_by_layer={layer:sum(j['completed_source_segments_by_layer'][layer] for j in jobs) for layer in r.LAYERS})))

if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--ledger',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();capture(a.ledger,a.output)
