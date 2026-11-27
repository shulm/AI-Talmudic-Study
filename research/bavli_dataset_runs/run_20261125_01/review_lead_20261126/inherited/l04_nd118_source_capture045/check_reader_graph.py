"""Readonly supplementary graph checks for standalone frozen source readings.

This does not alter the common runner, validate semantics, or admit a reading.
Checks mirror its position/edge endpoint constraints; standalone reader IDs and
context inventories need not constitute a production job or proposal.
"""
import argparse
import hashlib
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('reading', type=Path)
args = parser.parse_args()
raw = args.reading.read_bytes()
reading = json.loads(raw)
records = {row['id']: row for row in reading['records']}
failures = []

def require(ok, ident, rule):
    if not ok:
        failures.append(dict(id=ident, rule=rule))

require(len(records) == len(reading['records']), None, 'unique record IDs')
argument_layers = {'claims', 'utterances', 'questions', 'positions'}
for ident, row in records.items():
    content = row['content']
    require(all(link in records for link in row['links']), ident, 'links resolve')
    if row['layer'] == 'positions':
        require(records.get(content['claim_id'], {}).get('layer') == 'claims', ident, 'position claim foreign key')
        if content['question_id']:
            require(records.get(content['question_id'], {}).get('layer') == 'questions', ident, 'position question foreign key')
    if row['layer'] == 'edges':
        layers = [records.get(content[key], {}).get('layer') for key in ('source_id', 'target_id')]
        if content['relation'] == 'continuation':
            require(layers == ['structure', 'structure'], ident, 'continuation endpoints must be structure')
        else:
            require(all(layer in argument_layers for layer in layers), ident, 'argument endpoint type')

print(json.dumps(dict(status='FAIL_LOCAL_RECORDS' if failures else 'PASS',
    reading_sha256=hashlib.sha256(raw).hexdigest(), records=len(records),
    failures=failures, scope='supplementary standalone graph endpoint checks only',
    schema_validation_included=False, semantic_accuracy_certified=False,
    production_mutated=False), indent=2))
raise SystemExit(1 if failures else 0)
