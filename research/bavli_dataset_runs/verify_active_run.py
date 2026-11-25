"""Resolve the active pointer through its immutable Git contract and verify pins."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    pointer=json.loads((ROOT/'research/bavli_dataset_runs/ACTIVE_RUN.json').read_bytes())
    rel=pointer['contract_path']
    assert rel.startswith('research/bavli_dataset_runs/') and '..' not in Path(rel).parts
    commit=pointer['contract_commit'];assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
    raw=subprocess.check_output(['git','show',commit+':'+rel],cwd=ROOT)
    assert sha(raw)==pointer['contract_sha256'], 'Immutable contract hash mismatch'
    assert (ROOT/rel).read_bytes()==raw, 'Working contract differs from immutable committed contract'
    contract=json.loads(raw)
    assert contract['run_id']==pointer['run_id']
    assert contract['production_git_commit']==pointer['production_git_commit']
    for path,expected in contract['production_files'].items():
        assert sha((ROOT/path).read_bytes())==expected, 'Changed production dependency: '+path
        blob=subprocess.check_output(['git','show',contract['production_git_commit']+':'+path],cwd=ROOT)
        assert sha(blob)==expected,'Production commit/file hash mismatch: '+path
    source=(ROOT/'research/bavli_sugya_corpus_v1/source_manifest.json').read_bytes()
    assert sha(source)==contract['source_manifest_sha256']
    assignments=(ROOT/'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json').read_bytes().replace(b'\r\n',b'\n')
    assert sha(assignments)==contract['assignments_sha256']
    assert len(contract['tractate_assignment_epochs'])==37
    assert contract['schema_sha256']==sha((ROOT/contract['output_schema_files'][0]).read_bytes())
    assert contract['annotation_protocol_sha256']==sha((ROOT/contract['annotation_protocol_file']).read_bytes())
    print(json.dumps(dict(status='VERIFIED_ACTIVE_RUN',run_id=pointer['run_id'],contract_sha256=sha(raw),production_git_commit=contract['production_git_commit'],ready_lanes=contract['ready_lanes'])))
if __name__=='__main__':main()
