"""Read-only exact evidence validator for a bound neutral job; no semantic admission inferred."""
import hashlib
import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parent
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))

def verify(slug):
    jp = R / 'jobs' / ('bavli_' + slug + '.json')
    rp = R / 'readings' / (slug + '.json')
    job, reading = read(jp), read(rp)
    sp = Path(job['source']['path'])
    assert sha(sp) == job['source']['sha256']
    source = read(sp)
    texts = {f'{source["title"]} {i//2+1}{"a" if i%2==0 else "b"}:{k+1}': t
             for i, page in enumerate(source['text']) for k, t in enumerate(page)}
    cores = set(reading['core_refs'])
    assert len(cores) == len(reading['core_refs']) and cores == set(job['core_refs'])
    count = 0
    bindings = 0
    def walk(x):
        nonlocal count, bindings
        if isinstance(x, dict):
            ref = x.get('ref', x.get('source_ref', x.get('segment_id')))
            a, b = x.get('start_char', x.get('start')), x.get('end_char', x.get('end'))
            if ref is not None and a is not None and b is not None and 'quote' in x:
                assert type(a) is int and type(b) is int and 0 <= a < b <= len(texts[ref])
                assert texts[ref][a:b] == x['quote'], (ref, a, b)
                count += 1
            if isinstance(x.get('path'), str) and isinstance(x.get('sha256'), str):
                p = Path(x['path'])
                if not p.is_absolute():
                    p = R / p
                assert p.is_file() and sha(p) == x['sha256'], str(p)
                bindings += 1
            for y in x.values():
                walk(y)
        elif isinstance(x, list):
            for y in x:
                walk(y)
    walk(reading)
    assert count > 0
    sidecars = [p for p in [rp.with_suffix('.sha256'), Path(str(rp)+'.sha256')] if p.exists()]
    assert sidecars
    for p in sidecars:
        assert p.read_text(encoding='utf-8').split()[0] == sha(rp)
    return dict(reading_path=str(rp), reading_sha256=sha(rp), neutral_job_sha256=sha(jp),
        source_sha256=sha(sp), core_segments=len(cores), evidence_occurrences=count,
        bindings_checked=bindings, cohort=job['cohort'],
        semantic_comparison=False, new_probability_sample_draw=False,
        hidden_context_certification=False, human_scholarly_certification=False)

if __name__ == '__main__':
    print(json.dumps(verify(sys.argv[1])))
