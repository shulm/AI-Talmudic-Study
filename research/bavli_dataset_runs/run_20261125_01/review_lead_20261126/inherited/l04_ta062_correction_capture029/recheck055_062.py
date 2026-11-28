import json,hashlib,sys,importlib.util,collections
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).parent;P=D.parent.parent/'bavli_taanit';CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return dict(path=str(p),sha256=sha(p))
def write(name,data):
 p=D/name
 with p.open('x',encoding='utf8') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')
 with Path(str(p)+'.sha256').open('x') as f:f.write(sha(p)+'  '+p.name+'\n')
 return bind(p)
oldp=P/'snapshots/ac7c9ec619b963f05c6dc32c42e16511808f6256dea63937f5b5f8e5e96e5cf4.json';bp=P/'snapshots/415494e40a79b4f217d5e265c9d5b126e71677af764a9988013249e571b75888.json';np=P/'snapshots/663ea1da0f7ad381ee844fb537869ef1ebce15930d69048be7b85b064f48a086.json';pp=P/'proposals/feb5147495135f0904423cc5ffc531f093188144ea8123a42cdd7fe75e363f75.json'
for p in [oldp,bp,np,pp]:assert sha(p)==p.stem
old,base,new,proposal=map(read,[oldp,bp,np,pp]);prior=read(D/'ta055_comparison062.json')
for b in prior['bindings']+prior['proposal_bindings']:assert sha(b['path'])==b['sha256']
assert base['proposals'][:len(old['proposals'])]==old['proposals'];assert new['proposals']==base['proposals']+[pp.stem]
runner=CO/'research/bavli_production_v1/runner.py';sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('recheck_exact',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(P)
state=m.empty()
for h in new['proposals']:
 p=P/'proposals'/f'{h}.json';assert sha(p)==h;pr=state['proposals'];state=m.validate_apply(state,read(p),segs,job);state['proposals']=pr+[h]
assert m.encoded(state)==m.encoded(new)
br={r['id']:r for r in base['records']};nr={r['id']:r for r in new['records']};active={i:r for i,r in nr.items() if r['release_state']=='valid'}
sup={r['supersedes']:r['id'] for r in proposal['records'] if r.get('supersedes')};assert len(sup)==37 and len(proposal['records'])==87
for i,r in br.items():
 if i in sup:
  expected=dict(r,release_state='superseded');assert nr[i]==expected
 else:assert nr[i]==r
for r in active.values():
 assert all(i in active for i in r['links'])
 c=r['content']
 for k in ['source_id','target_id','claim_id','question_id']:
  if c.get(k):assert c[k] in active
 if r['layer']=='attributions' and c['scope'] in nr:assert c['scope'] in active
oldcov={(x['segment_id'],x['layer']):x for x in old['coverage']};bcov={(x['segment_id'],x['layer']):x for x in base['coverage']};ncov={(x['segment_id'],x['layer']):x for x in new['coverage']}
new15={sid for sid,layer in bcov if layer=='claims' and bcov[(sid,layer)]['extraction_state']=='completed' and oldcov.get((sid,layer),{}).get('extraction_state')!='completed'};assert len(new15)==15
for sid in new15:
 for l in m.LAYERS:assert bcov[(sid,l)]==ncov[(sid,l)]
new15records=[r for r in base['records'] if any(e['segment_id'] in new15 for e in r['evidence'])]
assert all(nr[r['id']]==r for r in new15records)
assert not any(e['segment_id'] in new15 for r in proposal['records'] for e in r['evidence'])
assert {k for k,v in bcov.items() if v['extraction_state']=='completed'}=={k for k,v in ncov.items() if v['extraction_state']=='completed'}
for r in proposal['records']:
 for e in r['evidence']:assert segs[e['segment_id']]['text'][e['start_char']:e['end_char']]==e['quote']
audit=dict(result='PASS',agent_id='/root/ta_compare062',role='NONBLIND independent bounded correction recheck',prior_comparison=bind(D/'ta055_comparison062.json'),bindings=[bind(p) for p in [oldp,bp,np,pp,runner,Path(__file__)]],exact_readonly_prefix_replay=True,proposals=len(new['proposals']),correction_records=87,supersessions=37,additions=50,prior_records_preserved_except_expected_release_state=True,active_link_and_embedded_endpoint_closure=True,completed_coverage_unchanged=True,newer15_refs=[segs[i]['ref'] for i in sorted(new15)],newer15_record_instances_unchanged=len(new15records),newer15_coverage_unchanged=True,newer15_reviewed=False,report=m.report(state,segs),corrected_record_exact_evidence=sum(len(r['evidence']) for r in proposal['records']),full_admission=False,new_eligibility=False)
print(json.dumps(write('correction055_preflight062.json',audit)))
