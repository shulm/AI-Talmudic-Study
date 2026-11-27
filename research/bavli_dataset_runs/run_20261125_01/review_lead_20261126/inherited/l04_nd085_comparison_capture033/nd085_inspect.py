import json, hashlib, importlib.util, sys
from pathlib import Path
sys.dont_write_bytecode=True
base=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04')
out=base/'review_20261127_delegated081/comparisons'; out.mkdir(exist_ok=True)
root=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
wt=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study')
read=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
job=read(root/'jobs/bavli_nedarim_delegated081.json'); checks=[]
def check(p,h):
 a=sha(p); assert a==h,(p,a,h); checks.append({'path':str(p),'sha256':a})
check(root/'jobs/bavli_nedarim_delegated081.json','011325327ca3a8e64c4c479ebbf75a5f146bba4ee8a68b375a893c13326205dc')
for x in [job['source'],job['original_source_schema'],job['frozen_plan']]+job['common_documents']:check(x['path'],x['sha256'])
intake=read(root/'ND081_READING_INTAKE_085.json')
for x in intake['captured_artifacts']:check(x['path'],x['sha256'])
for name,h in [('reading_initial.json','0816bfc2616c30efa02c881a8ba8257bdeb527bb3597c9a73adad679a25f7312'),('validation_receipt_initial.json','1cdf6f78e750b89ea4195a0e1605eaf2f1c91de3203c7dc1629ff33c4ed5f4d8'),('build_initial.py','d9548cf40af0583a5a5b5e404fe7700679e2fcd11680c85391e77c60d4f40bbd')]:check(base/'review_20261127_delegated081'/name,h)
contract=read(wt/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json')
for p,h in contract['production_files'].items():check(wt/p,h)
target='26acf7ff70ba33f249b8e3f957edac6a932ce1d32c7e84996ad3b239e74bab01'; prod=base/'bavli_nedarim';sp=prod/'snapshots'/f'{target}.json';check(sp,target)
spec=importlib.util.spec_from_file_location('runner',wt/'research/bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
j,segs=r.load(prod);s=read(sp);reading=read(base/'review_20261127_delegated081/reading_initial.json');refs={v['ref']:v for v in segs.values()}
if '--replay' in sys.argv:
 state=r.empty()
 for h in s['proposals']:
  p=prod/'proposals'/f'{h}.json';check(p,h);old=state['proposals'];state=r.validate_apply(state,read(p),segs,j);state['proposals']=old+[h]
 assert r.encoded(state)==sp.read_bytes()
 result={'status':'PASS','target':target,'proposal_count':len(s['proposals']),'production_commit':contract['production_git_commit'],'checks':checks,'report':r.report(s,segs),'reading_counts':{l:sum(x['layer']==l for x in reading['records']) for l in r.LAYERS}}
 (out/'validation_085.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
else:
 for ref in job['core_refs']:
  v=refs[ref];print('\nSOURCE',ref,v['text'])
  for label,rr in [('READER',reading['records']),('PRODUCER',s['records'])]:
   print(label)
   for x in rr:
    if x.get('release_state','valid')!='valid' or not any(e['segment_id'] in (ref,v['id']) for e in x['evidence']):continue
    if x['layer'] in ('claims','questions','edges','attributions','positions'):print(x['id'],json.dumps(x['content'],ensure_ascii=False))
