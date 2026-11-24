"""Shared deterministic I/O; private data never belongs in Git."""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research/decision_functions_2026-11-24/runs/pilot_v1'
PRIVATE = Path(os.environ.get('DECISION_LAB_PRIVATE', str(Path.home() / '.cache/decision_functions/pilot_v1')))
REV = 'b5596d9edd585361967991a591abc7b11fb1f7a3'
CLASSES = {'No': 0, 'Unsure': 1, 'Yes': 2}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def partition(ids, namespace):
    ids = sorted(map(str, ids))
    ids.sort(key=lambda x: (sha(f'20261124|{namespace}|{x}'.encode()), x))
    a, b = int(.6 * len(ids)), int(.2 * len(ids))
    return dict(train=ids[:a], development=ids[a:a+b], test=ids[a+b:])

def manifest(path):
    p = Path(path)
    return dict(filename=p.name, bytes=p.stat().st_size, sha256=sha(p.read_bytes()))
