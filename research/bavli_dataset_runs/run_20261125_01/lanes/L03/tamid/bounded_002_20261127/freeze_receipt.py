import json,sys,hashlib
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,v):
 f=out/n;assert not f.exists();f.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rp=runner.replay(job);assert rp['snapshot_sha256']=='5e6f2550823618653e9e09320c2880e8146407c46a509b4cada13217bd768b33'
exdir=job/'exports/bounded_002_20261127';ex=runner.export(job,exdir)
for f,h in ex['files'].items():assert sha(exdir/f)==h
save('REPLAY.json',rp);save('EXPORT.json',ex)
save('RECEIPT.json',dict(status='BOUNDED_PRODUCTION_COMPLETE_PENDING_COMPARISON',**rp,proposal_sha256=sha(out/'PROPOSAL.json'),owner=json.loads((job/'OWNER.json').read_text()),execution_agent='/root',core_start='Tamid 26a:8',core_end='Tamid 26b:7',new_core_segments=10,new_rows=93,superseded_structure='tam001.guard_derivation',scope='Closed guard derivation; upper rooms and above/below arrangement; adjacent gates; stone tiers',open_tails=runner.current(job)['open_tails'],remaining_per_layer=187,next_ref='Tamid 26b:8',context_read_through='Tamid 28a:10',source_pins=json.loads((out.parent/'bounded_001_20261127/PINS.json').read_text(encoding='utf-8')),base_correction_snapshot='82d494b4dd71ba8c26cd774abe128eabab1dc84cbdd79561bba5e92b5543dcc2',export_path=str(exdir),export_manifest_sha256=sha(exdir/'manifest.json'),independence='New source notes frozen by comparator before new labels; producer did not view them',independent_review='pending',ml_eligible=False,new_metered_api_calls=0))
(out/'RESUME.md').write_text('''Tamid bounded002:20/207cores per eight passes,187remain. Snapshot5e6f2550823618653e9e09320c2880e8146407c46a509b4cada13217bd768b33; accepted proposal ee40ae0586c4258957f872a6e6680e40fae8cc69d17515c840a24931ef18ecaf. Owner /root/lead_l01_l03 epoch1, execution /root. Next26b8; open tam002.stones must extend with Abaye answer already represented as context row tam002.prepared_context. Preserve context row/revision lineage rather than duplicating its assertion. Former guard derivation structure is superseded by closed tam002.guard_closed; six previous structure/reconciliation coverage references updated. Original proposals remain unchanged. Verify live CURRENT and replay shared runner before next packet/submit. Do not rerun builder on changed CURRENT. Independent new-batch comparison pending; earlier review is exact scope only, no whole-tractate or task qualification. Keep draft unmerged. Export/source pins and exact hashes are in RECEIPT/MANIFEST.
''',encoding='utf-8')
save('MANIFEST.json',{'files':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}})
print(json.dumps({'receipt_sha256':sha(out/'RECEIPT.json'),'manifest_sha256':sha(out/'MANIFEST.json')}))
