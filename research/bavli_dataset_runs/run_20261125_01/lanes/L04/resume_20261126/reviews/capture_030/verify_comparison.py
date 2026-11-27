import sys, pathlib, json, hashlib, importlib.util, collections
sys.dont_write_bytecode=True
BASE=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
WT=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study')
PJ=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit')
RD=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated101/reading.json')
SH='663ea1da0f7ad381ee844fb537869ef1ebce15930d69048be7b85b064f48a086'
def h(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
def freeze(p,x):
 b=(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
 if p.exists(): assert p.read_bytes()==b
 else: p.write_bytes(b)
 side=p.with_name(p.name+'.sha256'); sb=(hashlib.sha256(b).hexdigest()+'  '+p.name+'\n').encode()
 if side.exists(): assert side.read_bytes()==sb
 else: side.write_bytes(sb)
checks=[]
def pin(p,expected):
 actual=h(p); assert actual==expected,(str(p),actual,expected); checks.append({'path':str(p),'sha256':actual})
j=read(ROOT/'jobs/bavli_taanit_delegated101.json')
pin(ROOT/'jobs/bavli_taanit_delegated101.json','4429756dfd1d57fbbf1d56e9d6454ee8ac25e33cfde11819f42156bae4d922e4')
for x in [j['source'],j['original_source_schema'],j['frozen_plan']]+j['common_documents']: pin(x['path'],x['sha256'])
for x in read(ROOT/'TA101_READING_INTAKE_105.json')['captured_artifacts']: pin(x['path'],x['sha256'])
pin(RD,'299e38161a7cd72d86abd8d3232b85ade3b0b0a3d02d1c977d29e1721e016d8d'); pin(PJ/'snapshots'/f'{SH}.json',SH)
contractp=WT/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'; contract=read(contractp)
for p,v in contract['production_files'].items(): pin(WT/p,v)
spec=importlib.util.spec_from_file_location('frozen_runner',WT/'research/bavli_production_v1/runner.py'); r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
meta,segs=r.load(PJ); snap=read(PJ/'snapshots'/f'{SH}.json'); state=r.empty()
for n,ph in enumerate(snap['proposals']):
 pp=PJ/'proposals'/f'{ph}.json'; assert h(pp)==ph
 prev=state['proposals']; state=r.validate_apply(state,read(pp),segs,meta); state['proposals']=prev+[ph]
print('replay complete',len(snap['proposals']),flush=True)
assert r.encoded(state)==r.encoded(snap) and hashlib.sha256(r.encoded(state)).hexdigest()==SH
rd=read(RD); sr={v['ref']:v for v in segs.values()}; import copy
converted=copy.deepcopy(rd)
for rec in converted['records']:
 for e in rec['evidence']: e['segment_id']=sr[e['segment_id']]['id']
for c in converted['coverage']: c['segment_id']=sr[c['segment_id']]['id']
expected=sorted(x['id'] for x in converted['records'] if x['layer']=='structure' and x['content']['boundary']!='closed')
actual=converted['open_tails']; tail_error={'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected))}
try:
 r.validate_apply(r.empty(),converted,segs,meta); reading_contract='PASS'
except ValueError as ex:
 reading_contract='FAIL: '+str(ex)
 assert str(ex)=='open tails must exactly match active open structure'
 converted['open_tails']=expected
 r.validate_apply(r.empty(),converted,segs,meta)
 # Diagnostic adapter only. Neither original reading nor production has been changed.

active=[x for x in snap['records'] if x['release_state']=='valid']; scope=j['core_refs']; context=['Taanit 9b:1','Taanit 9b:3','Taanit 9b:4','Taanit 9b:5']
counts=lambda rr,refs:dict(collections.Counter(x['layer'] for x in rr if any(e['segment_id'] in refs for e in x['evidence'])))
result={'status':'PRODUCTION_REPLAY_PASS_READER_TAIL_CONTRACT_FAIL','chronology':'Source/input pins checked before semantic inspection; actual tooling/run-contract validation and exact historical replay completed after semantic inspection and before comparison freeze. No claim of pre-inspection replay.','snapshot_sha256':SH,'accepted_proposals':len(snap['proposals']),'snapshot_records':len(snap['records']),'active_records':len(active),'input_checks':checks,'run_contract_sha256':h(contractp),'production_git_commit':contract['production_git_commit'],'source_segments':len(segs),'reading_contract':reading_contract,'reading_tail_difference':tail_error,'reading_schema_graph_source_partition':'PASS after diagnostic-only expected-tail substitution; original reading fails tail contract and remains unchanged','reading_evidence_intervals':sum(len(x['evidence']) for x in rd['records']),'core_reader_counts':counts(rd['records'],scope),'context_reader_counts':counts(rd['records'],context),'core_producer_counts':counts(active,[sr[t]['id'] for t in scope]),'context_producer_counts':counts(active,[sr[t]['id'] for t in context]),'production_mutated':False,'CURRENT_read_or_used':False,'replay_method':'load exact production JOB/source contract, hash and validate_apply every proposal in pinned snapshot accepted prefix in memory; byte-equal final canonical snapshot; no replay CLI lock or CURRENT access','semantic_accuracy_certified':False}
freeze(BASE/'validation.json',result)
print(json.dumps(result,ensure_ascii=False))
