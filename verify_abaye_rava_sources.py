"""Checks text/address/provenance consistency, not whether each passage is a dispute."""
import hashlib
import json
from pathlib import Path
from abaye_rava_search import load_works

P=Path(__file__).parent/'abaye_rava_results'
d=json.loads((P/'abaye_rava_index.json').read_text(encoding='utf-8'))
works={w['work']:w for w in load_works()}
assert len(works)==76
assert sum(len(w['units']) for w in works.values())==d['metadata']['units_scanned']
assert len(d['entries'])==d['metadata']['entries']
assert len({e['ref'] for e in d['entries']})==len(d['entries'])
count=0
for e in d['entries']:
 w=works[e['work']];us={u['ref']:u for u in w['units']}
 assert e['source_sha256']==w['source_sha256'],e['ref']
 assert e['json_index']==list(us[e['ref']]['index']),e['ref']
 for u in e['source_units']:
  assert u['text']==us[u['ref']]['text'],u['ref']
  count+=1
 for ev in e['evidence']:assert ev in w['text'],e['ref']
# Six familiar subjects are regression coverage checks, not completeness evidence.
for prefix in ['Bava Metzia 21b:','Bava Kamma 72b:','Eruvin 15a:','Kiddushin 51a:','Gittin 34a:','Sanhedrin 27a:']:
 assert any(e['ref'].startswith(prefix) for e in d['entries']),prefix
print(f"PASS: {len(d['entries'])} entries, {count} context segments, references and source hashes; 6 coverage probes.")
