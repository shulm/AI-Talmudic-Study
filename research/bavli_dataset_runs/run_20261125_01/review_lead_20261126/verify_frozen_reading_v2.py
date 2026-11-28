"""Read-only integrity/cohort checks; does not certify semantics or hidden context."""
import hashlib
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def verify(path):
    path = Path(path)
    reading = json.loads(path.read_bytes())
    tractate = reading['tractate']
    job = next(json.loads(p.read_bytes()) for p in (BASE / 'jobs').glob('*.json')
               if json.loads(p.read_bytes())['tractate'] == tractate)
    source_path = Path(job['source']['path'])
    assert sha(source_path) == job['source']['sha256']
    source = json.loads(source_path.read_bytes())
    text = {f"{source['title']} {i // 2 + 1}{'a' if i % 2 == 0 else 'b'}:{k + 1}": t
            for i, page in enumerate(source['text']) for k, t in enumerate(page)}
    cores = set(reading['core_refs'])
    assert cores and len(cores) == len(reading['core_refs']) and cores <= set(text)
    blocks = job.get('selected_blocks', job.get('review_blocks'))
    probability = {ref for b in blocks if 'probability_sample' in b['roles'] for ref in b['core_refs']}
    endpoints = {ref for b in blocks if any('check' in role for role in b['roles']) for ref in b['core_refs']}
    evidence_count = 0

    def walk(obj):
        nonlocal evidence_count
        if isinstance(obj, dict):
            ref = obj.get('ref', obj.get('source_ref'))
            start = obj.get('start_char', obj.get('start'))
            end = obj.get('end_char', obj.get('end'))
            if ref is not None and start is not None and end is not None and 'quote' in obj:
                assert type(start) is int and type(end) is int
                assert 0 <= start < end <= len(text[ref])
                assert text[ref][start:end] == obj['quote'], (path, ref, start, end)
                evidence_count += 1
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for value in obj:
                walk(value)

    walk(reading)
    assert evidence_count > 0
    sidecars = [Path(str(path) + '.sha256'), path.with_suffix('.sha256')]
    checked_sidecars = []
    for sidecar in sidecars:
        if sidecar.exists():
            assert sidecar.read_text(encoding='utf-8').split()[0] == sha(path)
            checked_sidecars.append(str(sidecar))
    return dict(path=str(path.resolve()), sha256=sha(path), tractate=tractate,
                source_sha256=sha(source_path), core_segments=len(cores),
                probability=len(cores & probability), endpoints=len(cores & endpoints),
                overlap=len(cores & probability & endpoints),
                outside_planned_sample=len(cores - probability - endpoints),
                evidence_occurrences=evidence_count, sidecars_checked=checked_sidecars,
                semantic_comparison=False, hidden_context_certification=False,
                human_scholarly_certification=False)

if __name__ == '__main__':
    print(json.dumps([verify(p) for p in sys.argv[1:]], ensure_ascii=False, indent=2))
