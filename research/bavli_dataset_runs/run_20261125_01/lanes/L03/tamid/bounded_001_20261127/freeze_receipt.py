import json,hashlib,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
 p=out/name;assert not p.exists();p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rp=runner.replay(job);assert rp['snapshot_sha256']=='2c734e3e48f6686ab6cece6bd52141c56d7b5c3e5dbe71a485262c5642a83c3b'
exdir=job/'exports/bounded_001_20261127';ex=runner.export(job,exdir)
for f,h in ex['files'].items():assert sha(exdir/f)==h,f
save('REPLAY.json',rp);save('EXPORT.json',ex)
save('RECEIPT.json',dict(status='BOUNDED_PRODUCTION_COMPLETE_TRACTATE_INCOMPLETE',**rp,core_start='Tamid 25b:1',core_end='Tamid 26a:7',first_index=[49,0],last_index=[50,6],proposal_sha256=sha(out/'VALIDATED_PROPOSAL.json'),initial_rejected_proposal_sha256=sha(out/'INITIAL_PROPOSAL.json'),pins=json.loads((out/'PINS.json').read_text(encoding='utf-8')),owner=json.loads((job/'OWNER.json').read_text()),remaining_by_layer={l:197 for l in runner.LAYERS},open_tails=runner.current(job)['open_tails'],context_read_through='Tamid 28a:10',context_segments_not_covered=59,export_directory=str(exdir),export_manifest_sha256=sha(exdir/'manifest.json'),independent_review='Pending separate exact-version comparison; production receipt does not grant review',ml_eligible=False,new_metered_api_calls=0,token_cost_telemetry=None))
(out/'RESUME.md').write_text('''# Tamid opening checkpoint

Ten original cores25b:1–26a:7, starting array[49,0], complete across eight production passes;197/207 remain. Next26a:8[50,7]. Owner /root/lead_l01_l03 epoch1; authorized executor /root. Do not initialize again or change owner. Keep draft unmerged.

Replay saved accepted bytes with `python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_tamid`. Verify snapshot2c734e3e48f6686ab6cece6bd52141c56d7b5c3e5dbe71a485262c5642a83c3b before further changes. Resume next source via shared packet/submit, preserving open tam001.guard_derivation and reconciling26a8–10. Do not rerun build_initial.py after CURRENT exists.

INITIAL_PROPOSAL.json was frozen then rejected: continuation edges require structure endpoints. VALIDATED_PROPOSAL.json changes exactly one edge to qualification and was accepted. Both attempts and validation recovery remain immutable. Future semantic corrections need new IDs and explicit supersedes, plus dependent-link and coverage updates.

Read continuation through28a10;59 context segments are not counted as production coverage. Original under-head garment wording and subsequent opposite-head/no-mixed-fibre/stiffness alternatives remain distinct. Ash-removal preparation retains Abaye and Rava explanations without choosing one. Abaye26a5 is not automatically speaker of following anonymous answers. All independent review and demanding-task eligibility remain separate; no tractate delivered. Exact hashes/export inventory in RECEIPT.json and FILES_MANIFEST.json. Source is pinned Wikisource Talmud Bavli via Sefaria, CC-BY-SA metadata as supplied; corpus remains external and unchanged.
''',encoding='utf-8')
save('FILES_MANIFEST.json',{'files':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='FILES_MANIFEST.json'}})
print(json.dumps({'receipt_sha256':sha(out/'RECEIPT.json'),'manifest_sha256':sha(out/'FILES_MANIFEST.json'),'export_manifest_sha256':sha(exdir/'manifest.json')}))
