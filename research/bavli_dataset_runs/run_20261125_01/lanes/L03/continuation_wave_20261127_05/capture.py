import json,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;lane=out.parent
folders=['arakhin/bounded_004_20261127','arakhin_next20_004_review_20261127','arakhin_next20_005_review_20261127','eruvin/bounded_next20_002_20261127','eruvin/correction_next20_002_20261127','eruvin_next20_002_review_20261127/comparison','eruvin_next20_002_review_20261127/correction_verification','kiddushin_next20_004_review_20261127','nazir_next20_004_review_20261127','rh_next20_015_review_20261127','rh_next20_016_review_20261127','rosh_hashanah/bounded_015_20261127','tamid/bounded_006_20261127','tamid/correction_006_20261127','tamid_next20_006_review_20261127','yevamot/bounded012_20261127','yevamot/bounded012_correction_20261127','yevamot_next20_012_review_20261127','yevamot_next20_013_review_20261127']
pins={'rosh_hashanah':'8f3bc0abcd7bcbe41afd058b7f0ab3f241ef96214b28bccbef0268ecc1884fcd','yevamot':'f97f2db903e09ec2a461116ae999eae1133a6dc6dac7b47b0e773d93ef46120e','eruvin':'cb92523c062f1452d686f8be68d35ca9a4961aeadbd0a9603eba66f356f625b2','kiddushin':'5120405f3ba10a4a6863730b405cad2496965e0638120ed57a3b9eddc2f8976d','nazir':'29e5e8c12992c3ce1be4262f59b06d4e1ba312c8ee4699cf1d9998bb15353fc5','arakhin':'99c3b70a4cc439ef4de67a144ba11f840770cc60190f8a0f5b9969dd1a6437c0','tamid':'ca7b86f00e4ee8fc4a5392ec7edee933d7eb3d52ad48b37b4fdc90eb15951c1e'}
states={}
for slug,h in pins.items():
 job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_'+slug);j,src=runner.load(job);raw=(job/'snapshots'/f'{h}.json').read_bytes();assert runner.sha(raw)==h;s=json.loads(raw)
 states[slug]=dict(snapshot_sha256=h,owner=runner.read(job/'OWNER.json'),source_sha256=j['source_sha256'],report=runner.report(s,src),open_tails=s['open_tails'],proposal_sha256=s['proposals'][-1])
assert sum(s['report']['completed_by_layer']['claims'] for s in states.values())==910
runner.immutable(out/'STATE.json',runner.encoded(dict(status='PARTIAL_REQUIRED_WORK_REMAINS',historical_observation=True,total_source_segments=13635,completed_each_layer=910,remaining_each_layer=12725,tractates_delivered=0,states=states,notes=['Immutable bounded states, not a claim that live pointers remain unchanged.','Future source-only preparation does not add coverage.','All initial proposals, failed local validation candidates, reviews, and corrections are preserved.','Previous portable checkpoint810 remains independently replayable; these additional proposals extend it.'])))
files={}
for folder in folders:
 for p in sorted((lane/folder).rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:files[p.relative_to(root).as_posix()]=runner.sha(p.read_bytes())
for p in out.iterdir():
 if p.is_file() and p.name!='PACKAGE_MANIFEST.json':files[p.relative_to(root).as_posix()]=runner.sha(p.read_bytes())
runner.immutable(out/'PACKAGE_MANIFEST.json',runner.encoded(dict(files=files,completed_each_layer=910,scope='Five additional twenty-core batches and independent source/review artifacts; not full tractate delivery')))
print(json.dumps(dict(files=len(files),manifest_sha256=runner.sha((out/'PACKAGE_MANIFEST.json').read_bytes()))))
