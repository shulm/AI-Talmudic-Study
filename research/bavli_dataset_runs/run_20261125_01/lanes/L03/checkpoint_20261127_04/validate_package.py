import sys,zipfile,json
from pathlib import Path
sys.path.insert(0,'research/bavli_production_v1');import runner
out=Path(__file__).resolve().parent;r=runner.read(out/'SESSION_CHECKPOINT.json');package=Path(r['package_dir']);archive=Path(r['archive_path'])
assert runner.sha(archive.read_bytes())==r['archive_sha256'];manifest=runner.read(package/'PACKAGE_MANIFEST.json');assert runner.sha((package/'PACKAGE_MANIFEST.json').read_bytes())==r['package_manifest_sha256']
assert manifest['source_corpora_included'] is False
assert {p.relative_to(package).as_posix() for p in package.rglob('*') if p.is_file()}==set(manifest['files'])|{'PACKAGE_MANIFEST.json'}
with zipfile.ZipFile(archive) as z:
 assert len(z.namelist())==len(set(z.namelist())) and set(z.namelist())==set(manifest['files'])|{'PACKAGE_MANIFEST.json'}
 for name,h in manifest['files'].items():assert runner.sha((package/name).read_bytes())==h==runner.sha(z.read(name))
 assert runner.sha(z.read('PACKAGE_MANIFEST.json'))==r['package_manifest_sha256']
assert len(r['release']['jobs'])==7
for j in r['release']['jobs']:
 actual=runner.read(Path(j['job_dir'])/'CURRENT.json')['snapshot_sha256'];assert actual==j['snapshot_sha256'],'Live producer advanced during capture'
 assert runner.read(Path(j['job_dir'])/'OWNER.json')==dict(owner=j['owner'],epoch=j['epoch'])
 assert j['coverage']['replay_pass']
 for h in j['proposal_sha256']:assert runner.sha((package/'run/proposals'/f'{h}.json').read_bytes())==h
totals={l:sum(j['coverage']['completed_by_layer'][l] for j in r['release']['jobs']) for l in runner.LAYERS}
v=dict(archive_sha256=r['archive_sha256'],package_manifest_sha256=r['package_manifest_sha256'],manifest_file_count=len(manifest['files']),zip_member_count=len(manifest['files'])+1,all_directory_and_zip_member_hashes_verified=True,live_pointers_and_owners_unchanged=True,accepted_proposals=sum(len(j['proposal_sha256']) for j in r['release']['jobs']),source_segments=13635,completed_by_layer=totals,remaining_by_layer={l:13635-v for l,v in totals.items()},tractates_delivered=0,source_corpora_included=False)
runner.immutable(out/'VALIDATION.json',runner.encoded(v));print(json.dumps(v))
