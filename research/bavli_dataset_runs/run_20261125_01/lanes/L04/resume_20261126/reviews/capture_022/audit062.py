import json,hashlib,sys,importlib.util,collections
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).parent; R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126'); P=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit'); CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p))
def write(name,data):
 p=D/name
 with p.open('x',encoding='utf8') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
 return bind(p)
J=R/'jobs/bavli_taanit_delegated055.json';j=read(J);rp=D.parent/'taanit_delegated055.json';rd=read(rp);sp=P/'snapshots/ac7c9ec619b963f05c6dc32c42e16511808f6256dea63937f5b5f8e5e96e5cf4.json';s=read(sp)
assert sha(J)=='56b184adee73bf0bb185586419c42f72b395a9a761ede0d2fd8645b70d5ba81b'
assert sha(rp)=='19e60727e4c13a8cecb90c13e2afe68a035368bfa18cc23b3ce19d67af8cdd3e' and sha(sp)==sp.stem
bindings=[j['source'],j['original_source_schema'],j['frozen_plan']]+j['common_documents']
for b in bindings:assert sha(b['path'])==b['sha256']
contract=CO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json';ct=read(contract)
for p,h in ct['production_files'].items():assert sha(CO/p)==h
plan=read(j['frozen_plan']['path']); pc={k:v for k,v in plan.items() if k!='plan_sha256'}
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(pc,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==j['plan_sha256']==plan['plan_sha256']
runner=CO/'research/bavli_production_v1/runner.py';sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('exact062',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(P);br={v['ref']:v for v in segs.values()}
state=m.empty()
for h in s['proposals']:
 pp=P/'proposals'/f'{h}.json';assert sha(pp)==h;prev=state['proposals'];state=m.validate_apply(state,read(pp),segs,job);state['proposals']=prev+[h]
assert m.encoded(state)==m.encoded(s)
import jsonschema
schema=read(runner.parent/'schema.json'); count=0
for r in rd['records']:
 jsonschema.validate(r,schema['properties']['records']['items'])
 for e in r['evidence']:
  assert br[e['segment_id']]['text'][e['start_char']:e['end_char']]==e['quote'];count+=1
ids={r['id'] for r in rd['records']}
for r in rd['records']:
 assert set(r['links'])<=ids
 if r['layer']=='edges':assert {r['content']['source_id'],r['content']['target_id']}<=ids
for c in rd['coverage']:jsonschema.validate(c,schema['properties']['coverage']['items'])
assert count==503 and len(rd['coverage'])==256 and len([c for c in rd['coverage'] if c['segment_id'] in j['core_refs']])==240
core=set(j['core_refs']);active=[r for r in s['records'] if r['release_state']=='valid' and any(segs[e['segment_id']]['ref'] in core for e in r['evidence'])]
audit=dict(result='PASS',role='NONBLIND',agent_id='/root/ta_compare062',fork_turns='none',bindings=bindings+[bind(J),bind(rp),bind(sp),bind(contract),bind(runner)],proposal_bindings=[bind(P/'proposals'/f'{h}.json') for h in s['proposals']],exact_readonly_replay=True,proposal_count=len(s['proposals']),reading_evidence_slices=count,total_reading_coverage=256,core_reading_coverage=240,context_reading_coverage=16,source_segments=len(segs),production_report=m.report(state,segs),reading_unchanged=sha(rp)=='19e60727e4c13a8cecb90c13e2afe68a035368bfa18cc23b3ce19d67af8cdd3e')
if '--preflight' in sys.argv:print(json.dumps(write('preflight062.json',audit)));sys.exit()
if '--dump' in sys.argv:
 for ref in j['core_refs']:
  print('\nSOURCE',ref,br[ref]['text'])
  for label,rows in [('READER',rd['records']),('PRODUCER',active)]:
   for r in rows:
    refs=[e['segment_id'] if label=='READER' else segs[e['segment_id']]['ref'] for e in r['evidence']]
    if ref in refs and r['layer'] in ['claims','questions','positions','edges','attributions']:print(label,r['id'],r['layer'],json.dumps(r['content'],ensure_ascii=False),json.dumps(r.get('uncertainty',[]),ensure_ascii=False))
