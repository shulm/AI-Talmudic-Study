"""Rebuild into a temporary isolated directory; compare data byte-for-byte."""
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
import pipeline as p
def main():
    start=time.perf_counter()
    inputs=['pipeline.py','make_schema.py','compile_annotations.py','annotation_initial.py','annotation_completion.py','revisions.json']
    expected=['source_manifest.json','schema_v1.json','annotation_manifest.json']+[f'data/{t}.jsonl' for t in p.TABLES]+['context/segments.jsonl','context/windows.jsonl']
    with tempfile.TemporaryDirectory(prefix='bavli_pilot_reproduction_') as tmp:
        temp=Path(tmp)
        for f in inputs:shutil.copyfile(p.HERE/f,temp/f)
        for cmd in [['pipeline.py','build'],['make_schema.py'],['compile_annotations.py']]:
            result=subprocess.run([sys.executable,'-X','utf8',*cmd],cwd=temp,capture_output=True,text=True,encoding='utf-8')
            assert result.returncode==0,result.stderr
        for f in expected:assert (temp/f).read_bytes()==(p.HERE/f).read_bytes(),f+' differs'
    result=dict(passed=True,byte_identical_outputs=len(expected),outputs=expected,wall_seconds=time.perf_counter()-start,semantic_regeneration=False,note='Replays preserved authored decisions; not a fresh independent model annotation.')
    p.write(p.HERE/'reproduction_report.json',result);print(result)
if __name__=='__main__':main()
