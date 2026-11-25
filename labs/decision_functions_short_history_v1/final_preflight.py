"""Recheck final pre-fit code while preserving earlier test receipts."""
import tempfile
from contracts import *
from preflight import main
with tempfile.TemporaryDirectory() as temp:
 path=Path(temp);main(path)
 assert read(path/'EXPECTED.json')==read(OUT/'EXPECTED.json')
 atomic(OUT/'preflight_final.json',read(path/'preflight.json'))
