import json,hashlib,sys,importlib.util,datetime,collections
from pathlib import Path
import jsonschema
sys.dont_write_bytecode=True
R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
D=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated047');O=D/'comparisons';T=D.parent/'bavli_moed_katan'
C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p))
def save(n,d):
 p=O/n
 with p.open('x',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
 return bind(p)
jp=R/'jobs/bavli_moed_katan_delegated047.json';rp=D/'moed_katan_delegated047.json';sp=T/'snapshots/e5f88150985e9541e2f1a5def9b2975ab102767f3a5b5b2fe05770b5d3ae12e0.json'
pins=[(jp,'199405c845c21087f234d1778116d9cc8f93093997360960f7ecf642e271f819'),(rp,'0999da36b2aa03178d4e473d26fa26e346c2afe7ce8c63130b26c8af15e37e9d'),(sp,sp.stem),(D/'validation_receipt047.json','f5fb2a9b1e13dfeea144cb960a6ab0a4b09ff6bcadba0c449e2d9f4c21defef5'),(D/'author_validate047.py','ec71a90e55907347d0bfaf5a1a2a2027a3c227ebd77b8a192a2716e43108d418'),(R/'MK047_READING_INTAKE_057.json','6d6aa38d05f179bd7f9abc71943f3f83ea42994a7ef8b509ba49b96fcffb05b5')]
for p,h in pins:assert sha(p)==h,(p,sha(p))
j=read(jp);rd=read(rp);s=read(sp);contract=read(C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json')
for b in rd['bindings']:assert sha(b['path'])==b['sha256']
for p,h in contract['production_files'].items():assert sha(C/p)==h
plan=read(j['frozen_plan']['path']);ph=plan.pop('plan_sha256');assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(plan,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()==ph==j['plan_sha256']
for b in j['selected_blocks']:assert any(x['block_id']==b['block_id'] and [q['ref'] for q in x['spans']]==b['core_refs'] for x in plan['review_blocks'])
runner=C/'research/bavli_production_v1/runner.py';spec=importlib.util.spec_from_file_location('pinned_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(T);br={v['ref']:v for v in segs.values()}
assert read(T/'source_inventory.json')==list(segs.values())
jsonschema.Draft202012Validator(read(R/'source_only_common/schema.json')).validate(rd['proposal'])
def evidence(obj):
 n=0
 def walk(x):
  nonlocal n
  if isinstance(x,dict):
   if all(k in x for k in ['quote','start_char','end_char']):
    k=x.get('segment_id',x.get('ref'));t=(br[k] if k in br else segs[k])['text'];assert t[x['start_char']:x['end_char']]==x['quote'];n+=1
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(obj);return n
ne=evidence(rd);ns=evidence(s)
for r,v in rd['source_coordinate_map'].items():
 z=br[r];assert z['source_index']==[v['page_index'],v['segment_index']] and len(z['text'])==v['unicode_length'] and hashlib.sha256(z['text'].encode()).hexdigest()==v['sha256_utf8']
state=m.empty();prefix=[]
for h in s['proposals']:
 p=T/'proposals'/f'{h}.json';assert sha(p)==h;prev=state['proposals'];state=m.validate_apply(state,read(p),segs,job);state['proposals']=prev+[h];prefix.append(bind(p))
assert m.encoded(state)==m.encoded(s)
validation=dict(stage='INTEGRITY_AND_READONLY_REPLAY_BEFORE_SEMANTIC_COMPARISON',timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),agent_id='/root/mk_compare054',fork='none',role='NONBLIND',pins=[bind(p) for p,h in pins],reading_bindings=rd['bindings'],contract=bind(C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),production_files=contract['production_files'],production_commit=contract['production_git_commit'],runner=bind(runner),prefix=prefix,snapshot=bind(sp),source_segments=len(segs),reading_exact_spans=ne,producer_exact_spans=ns,exact_replay=True,report=m.report(state,segs),CURRENT_read=False,semantic_comparison_started=False)
if __name__=='__main__':print(save('mk047_validation_replay054.json',validation))

