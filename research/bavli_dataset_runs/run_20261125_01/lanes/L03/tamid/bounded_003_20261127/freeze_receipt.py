import json,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
 f=out/n;assert not f.exists();f.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rp=runner.replay(job);assert rp['snapshot_sha256']=='eca024a2346d9a35620f5e97b60a7be3ae891cd88e9897598b3586e9da0b214f'
exdir=job/'exports/bounded_003_20261127';ex=runner.export(job,exdir)
for f,h in ex['files'].items():assert sha(exdir/f)==h
save('REPLAY.json',rp);save('EXPORT.json',ex)
save('RECEIPT.json',dict(status='BOUNDED_PRODUCTION_COMPLETE_PENDING_COMPARISON',**rp,proposal_sha256=sha(out/'PROPOSAL.json'),owner=json.loads((job/'OWNER.json').read_text()),execution_agent='/root',core_start='Tamid 26b:8',core_end='Tamid 27a:7',new_core_segments=10,new_rows=95,superseded_structure='tam002.stones',context_rows_reused=['tam002.prepared_context','tam002.prepared_context.p','tam002.prepared.a','tam002.prepared_answer'],open_tails=runner.current(job)['open_tails'],remaining_per_layer=177,next_ref='Tamid 27a:8',context_read_through='Tamid 28a:10',source_pins=json.loads((out.parent/'bounded_001_20261127/PINS.json').read_text(encoding='utf-8')),base_snapshot='5e6f2550823618653e9e09320c2880e8146407c46a509b4cada13217bd768b33',export_path=str(exdir),export_manifest_sha256=sha(exdir/'manifest.json'),independence='Producer has not viewed existing central frozen Tamid reading. Separate comparator source preparation before new label access.',independent_review='pending',ml_eligible=False,new_metered_api_calls=0))
(out/'RESUME.md').write_text('''Tamid bounded003:30/207cores across all eight passes,177remain. Snapshoteca024a2346d9a35620f5e97b60a7be3ae891cd88e9897598b3586e9da0b214f; accepted858a3fc108ce3e81dec95cf46f292b010ad3efcad728ecef18459fdad12e0a72. Owner /root/lead_l01_l03 epoch1; executor /root. Next27a8, open tam003.levites. The alternative literal24 answer and Rabbi Yehoshua ben Levi precedent27a8–9 are already context records; reuse or explicitly revise them when completing those cores. Initial stone-context records26b8 reused, not duplicated. Prior stone primary superseded and old structure/reconciliation refs updated. Verify live CURRENT and exact shared-runner replay before new work; never rerun author script against changed state. Independent bounded comparison pending. No whole-tractate acceptance or task qualification. Exact pins/export hashes in RECEIPT and MANIFEST. Keep draft unmerged.
''',encoding='utf-8')
save('MANIFEST.json',{'files':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(json.dumps({'receipt_sha256':sha(out/'RECEIPT.json'),'manifest_sha256':sha(out/'MANIFEST.json')}))
