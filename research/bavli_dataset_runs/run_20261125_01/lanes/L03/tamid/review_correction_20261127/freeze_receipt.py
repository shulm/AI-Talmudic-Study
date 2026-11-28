import json,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
 f=out/n;assert not f.exists();f.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rp=runner.replay(job);assert rp['snapshot_sha256']=='82d494b4dd71ba8c26cd774abe128eabab1dc84cbdd79561bba5e92b5543dcc2'
exdir=job/'exports/review_correction_20261127';ex=runner.export(job,exdir)
for f,h in ex['files'].items():assert sha(exdir/f)==h
save('REPLAY.json',rp);save('EXPORT.json',ex)
save('RESPONSE.json',dict(status='TARGETED_CORRECTIONS_SUBMITTED_PENDING_RECHECK',**rp,proposal_sha256=sha(out/'VALIDATED_PROPOSAL.json'),lineage_sha256=sha(out/'LINEAGE.json'),owner=json.loads((job/'OWNER.json').read_text()),execution_agent='/root',new_rows=23,superseded_rows=7,scope='T01 separate garment voices and quoted precedent; T02 separate numerical argument components',unchanged_limits=['T03 benefit QA not qualified','T04 shared lottery question not admitted'],no_added_source_coverage=True,remaining_per_layer=197,next_ref='Tamid 26a:8',export_path=str(exdir),export_manifest_sha256=sha(exdir/'manifest.json'),independent_recheck='pending',ml_eligible=False))
(out/'RESUME.md').write_text('''Tamid targeted correction checkpoint82d494b4dd71ba8c26cd774abe128eabab1dc84cbdd79561bba5e92b5543dcc2. Replay with shared runner, verify owner /root/lead_l01_l03 epoch1 and current pointer. Do not rerun builders. Accepted proposal309a1a796445af9cb6e10fc9e5a0fec640afa5061da244005ffc211c0f7a21c0,23new/7superseded; initial rejected correction retained separately. First opening proposal, initial review and errors remain immutable. Coverage10/207 all8passes, next26a8, open tam001.guard_derivation. Await independent exact-version recheck then resume source sequentially; no benefit-QA or lottery-comparable-set qualification, no whole-tractate acceptance. Export and pins are linked via RESPONSE.json and preceding bounded_001 package. Keep draft unmerged.
''',encoding='utf-8')
save('MANIFEST.json',{'files':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(json.dumps({'response_sha256':sha(out/'RESPONSE.json'),'manifest_sha256':sha(out/'MANIFEST.json')}))
