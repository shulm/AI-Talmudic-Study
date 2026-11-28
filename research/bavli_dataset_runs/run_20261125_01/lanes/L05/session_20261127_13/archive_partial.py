"""Archive checkpoint artifacts, excluding original source inventories."""
import hashlib, json, zipfile
from pathlib import Path
S=Path(__file__).resolve().parent
W=Path('F:/Sefaria_QA/bavli_l05_workspace_20261126')
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05')
out=W/'deliveries/L05_session20261127_13_partial.zip'
entries={}
for row in json.loads((S/'CHECKPOINTS.json').read_bytes()):
    name=row['job_id']; job=J/name
    for filename in ['JOB.json','OWNER.json','CURRENT.json']:
        entries[f'jobs/{name}/{filename}']=job/filename
    for folder in ['snapshots','proposals']:
        for p in (job/folder).glob('*.json'):
            entries[f'jobs/{name}/{folder}/{p.name}']=p
    ex=Path(row['export_dir'])
    for p in ex.rglob('*'):
        if p.is_file(): entries[f'exports/{name}/{p.relative_to(ex).as_posix()}']=p
for p in S.rglob('*'):
    if p.is_file() and p.suffix in {'.json','.py','.md','.sha256'} and p.name!='ARTIFACT_RECEIPT.json':
        entries[f'session20261127_13/{p.relative_to(S).as_posix()}']=p
hashes={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in entries.items()}
out.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for k,p in sorted(entries.items()): z.write(p,k)
with zipfile.ZipFile(out) as z:
    assert set(z.namelist())==set(hashes)
    for k,h in hashes.items(): assert hashlib.sha256(z.read(k)).hexdigest()==h,k
receipt=dict(status='PARTIAL_REQUIRED_WORK_REMAINS',path=str(out),sha256=hashlib.sha256(out.read_bytes()).hexdigest(),files=hashes,source_inventory_included=False)
(S/'ARTIFACT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(receipt['sha256'],len(hashes),'verified archive members')
