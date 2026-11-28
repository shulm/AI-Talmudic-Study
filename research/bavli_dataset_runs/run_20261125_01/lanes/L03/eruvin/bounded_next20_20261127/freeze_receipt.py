import json,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
 f=out/n;assert not f.exists();f.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rp=runner.replay(job);assert rp['snapshot_sha256']=='35b7ebfcb7db5043158ff0c726dcc652b35c89703a6622f26fea2383c8faa007'
exdir=job/'exports/bounded_next20_20261127';ex=runner.export(job,exdir)
for f,h in ex['files'].items():assert sha(exdir/f)==h
save('REPLAY.json',rp);save('EXPORT.json',ex)
save('RECEIPT.json',dict(status='BOUNDED_PRODUCTION_COMPLETE_PENDING_COMPARISON',**rp,proposal_sha256=sha(out/'PROPOSAL.json'),pins=json.loads((out/'PINS.json').read_text()),core_start='Eruvin 4b:18',core_end='Eruvin 5b:2',new_core_segments=20,new_rows=169,prior_rows_unchanged=True,open_tails=runner.current(job)['open_tails'],remaining_per_layer=3516,next_ref='Eruvin 5b:3',export_path=str(exdir),export_manifest_sha256=sha(exdir/'manifest.json'),independent_review='pending',ml_eligible=False,new_metered_api_calls=0))
(out/'RESUME.md').write_text('''Eruvin next20:130/3646cores per eightpasses,3516remain. Snapshot35b7ebfcb7db5043158ff0c726dcc652b35c89703a6622f26fea2383c8faa007; accepted7e89ab0ef6162d98a031e30e767d768ce4e637dbec6dc601729c06d66f6e2bf2. OwnerL03/eruvin epoch2, executor/root. Next5b3; open er.next20.projecting must be continued. Source-backed context rows5b3/4/9/10 already qualify placement and need for additional lehi; reuse or explicitly revise them when these become cores. Initial and alternative explanations are separate. Anonymous mar positions are unassigned, never named by order. Quoted Ami/Asi, Rami bar Hama reporting Rav Huna, and Rav Huna son of Rav Yehoshua remain distinct. Current new20 comparison pending, no full-tractate/task acceptance. Verify live pointer and shared-runner replay before nextproposal. Do not rerun builder against changedCURRENT. Exactpins,exports and hashmanifest retained. Keep draft unmerged.
''',encoding='utf-8')
save('MANIFEST.json',{'files':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(json.dumps({'receipt_sha256':sha(out/'RECEIPT.json'),'manifest_sha256':sha(out/'MANIFEST.json')}))
