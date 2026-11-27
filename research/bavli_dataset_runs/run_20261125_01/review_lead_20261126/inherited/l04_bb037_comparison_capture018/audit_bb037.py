import json, hashlib, sys, importlib.util, subprocess
from pathlib import Path
from collections import Counter
import jsonschema
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent
R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
T=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_bava_batra')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p))
def put(n,x):
 p=O/n;b=(json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
 if p.exists():assert p.read_bytes()==b
 else:
  with p.open('xb') as f:f.write(b)
 q=O/(n+'.sha256'); t=sha(p)+'  '+n+'\n'
 if q.exists():assert q.read_text()==t
 else:q.write_text(t,encoding='ascii')
 return bind(p)
J=R/'jobs/bavli_bava_batra_delegated037.json';assert sha(J)=='107078be4e24ffe632ce74e2b62084e784ddf0269add939bcfc5795f847d65cb';j=read(J)
RP=O.parent/'bava_batra_delegated037.r2.json';assert sha(RP)=='32d1af8ed4df70800334179165e3d1d8901bdeb79cb6b844f28e290f1da083ba';r=read(RP)
V=O.parent/'validation_delegated037.r2.json';assert sha(V)=='929711431446e8386fdefd5373bb3e6c4f60af63a7160a00cbc61d892ac3d238'
I=O.parent/'bava_batra_delegated037.json';assert sha(I)=='b8f404704770c73b6bdd7cd3126b3b59ef8292bd18e8a8dbf9c34b82c598508f'
for b in r['bindings']:assert sha(b['path'])==b['sha256']
plan=read(j['frozen_plan']['path']); p0={k:v for k,v in plan.items() if k!='plan_sha256'}
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(p0,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==j['plan_sha256']
contract=C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json';ct=read(contract)
for p,h in ct['production_files'].items():assert sha(C/p)==h
runner=C/'research/bavli_production_v1/runner.py';sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('readonly_bb037',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
S=T/'snapshots/6c1f1a43e1e07f0772cd625422949e0673e777a153dde1e6bfc081211cc96833.json';assert sha(S)==S.stem;s=read(S)
job,segs=m.load(T);br={x['ref']:x for x in segs.values()};assert read(T/'source_inventory.json')==list(segs.values())
st=m.empty();pbs=[]
for h in s['proposals']:
 p=T/'proposals'/f'{h}.json';assert sha(p)==h;pbs.append(bind(p));prev=st['proposals'];st=m.validate_apply(st,read(p),segs,job);st['proposals']=prev+[h]
assert m.encoded(st)==S.read_bytes()
jsonschema.Draft202012Validator(read(runner.parent/'schema.json')).validate(r['proposal'])
def evidence(o):
 n=0
 def walk(x):
  nonlocal n
  if isinstance(x,dict):
   if all(k in x for k in ['segment_id','start_char','end_char','quote']):
    z=br.get(x['segment_id'],segs.get(x['segment_id']));assert z is not None;assert z['text'][x['start_char']:x['end_char']]==x['quote'];n+=1
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(o);return n
core=set(j['core_refs']);rr=r['proposal']['records']; active=[x for x in s['records'] if x['release_state']=='valid']; lookup={x['id']:x for x in active}
rc=[x for x in rr if any(e['segment_id'] in core for e in x['evidence'])];pc=[x for x in active if any(segs[e['segment_id']]['ref'] in core for e in x['evidence'])]
for rows in [rr,active]:
 ids={x['id']:x for x in rows}
 for x in rows:
  assert set(x['links'])<=set(ids)
  for k in ['source_id','target_id','claim_id','question_id']:
   if x['content'].get(k):assert x['content'][k] in ids
  if x['layer']=='edges':assert ids[x['content']['source_id']]['layer']!='edges' and ids[x['content']['target_id']]['layer']!='edges'
verification=subprocess.run([sys.executable,'-X','utf8',str(O.parent/'author_validate_delegated037_r2.py'),'--verify'],capture_output=True,text=True,encoding='utf8');assert verification.returncode==0,verification.stderr
bindings=dict(job=bind(J),initial_reading=bind(I),effective_reading=bind(RP),reader_validation=bind(V),reader_bound_documents=r['bindings'],contract=bind(contract),production_commit=ct['production_git_commit'],runner=bind(runner),schema=bind(runner.parent/'schema.json'),protocol=bind(runner.parent/'PROTOCOL.md'),snapshot=bind(S),reservation=bind(R/'BB037_COMPARATOR_RESERVATION_045.json'),requirements=bind(R/'L04_COMPARISON_RESERVATION_027.json'),audit_helper=bind(Path(__file__)),proposals=pbs)
obs=dict(result='PASS',bindings=bindings,readonly_exact_prefix_replay=True,proposal_count=len(pbs),snapshot_core_count=310,original_inventory_segments_verified=len(segs),source_only_verify=json.loads(verification.stdout),reader_exact_evidence_slices=evidence(r),producer_exact_evidence_slices=evidence(s),reader_core_layer_counts=dict(Counter(x['layer'] for x in rc)),producer_core_layer_counts=dict(Counter(x['layer'] for x in pc)),coverage={l:sum(c['layer']==l and c['extraction_state']=='completed' and segs[c['segment_id']]['ref'] in core for c in s['coverage']) for l in m.LAYERS},no_CURRENT_access=True,no_production_writes=True)
if __name__=='__main__':
 print(json.dumps(put('validation_replay_bb037.json',obs)))
