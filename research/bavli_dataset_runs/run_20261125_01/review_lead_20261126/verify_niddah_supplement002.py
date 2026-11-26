"""Mechanical validation only; supplemental cohort never becomes probability sampling."""
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parent
def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

job_path = R / 'jobs/bavli_niddah_supplement002.json'
job = read(job_path)
source_path = Path(job['source']['path'])
assert sha(source_path) == job['source']['sha256']
source = read(source_path)
texts = {f'Niddah {i//2+1}{"a" if i%2==0 else "b"}:{k+1}': t
         for i, page in enumerate(source['text']) for k, t in enumerate(page)}
p = R / 'readings/niddah_supplement002.json'
d = read(p)
assert len(d['core_refs']) == len(set(d['core_refs'])) == 51
assert set(d['core_refs']) == set(job['core_refs'])
count = 0
def walk(x):
    global count
    if isinstance(x, dict):
        ref = x.get('ref', x.get('source_ref'))
        a = x.get('start_char', x.get('start'))
        b = x.get('end_char', x.get('end'))
        if ref is not None and a is not None and b is not None and 'quote' in x:
            assert type(a) is int and type(b) is int and 0 <= a < b <= len(texts[ref])
            assert texts[ref][a:b] == x['quote'], (ref, a, b)
            count += 1
        for y in x.values():
            walk(y)
    elif isinstance(x, list):
        for y in x:
            walk(y)
walk(d)
assert count > 0
sidecars = [q for q in [p.with_suffix('.sha256'), Path(str(p)+'.sha256')] if q.exists()]
assert sidecars
for q in sidecars:
    assert q.read_text(encoding='utf-8').split()[0] == sha(p)
old = read(R / 'readings/niddah_batch001.json')
overlap = set(d['core_refs']) & set(old['core_refs'])
assert len(overlap) == 10
print(json.dumps(dict(reading_path=str(p), reading_sha256=sha(p),
    neutral_job_sha256=sha(job_path), source_sha256=sha(source_path),
    exact_evidence_occurrences=count, supplemental_core_segments=51,
    overlap_with_previous_direct_probability_cores=10,
    new_unique_supplemental_core_segments=41, new_probability_sample_credit=0,
    new_comparison_credit=0, semantic_comparison=False,
    hidden_context_certification=False, human_scholarly_certification=False)))
