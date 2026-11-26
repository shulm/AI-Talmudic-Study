import sys
sys.dont_write_bytecode=True
import json, hashlib, importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p): return {'path':p.as_posix(),'sha256':sha(p)}
def load(name):
 q=BASE/'COMPARISON_QUEUE_007.json'; e=next(x for x in json.loads(q.read_bytes()) if x['job_id']=='bavli_'+name)
 rp=Path(e['reading_path']); assert sha(rp)==e['reading_sha256']; reading=json.loads(rp.read_bytes())
 sp=Path(e['snapshot_path']); assert sha(sp)==e['snapshot_sha256']; state=json.loads(sp.read_bytes())
 cp=REPO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'; contract=json.loads(cp.read_bytes())
 runnerp=REPO/'research/bavli_production_v1/runner.py'; assert sha(runnerp)==contract['production_files']['research/bavli_production_v1/runner.py']
 spec=importlib.util.spec_from_file_location('readonly_runner',runnerp); runner=importlib.util.module_from_spec(spec); spec.loader.exec_module(runner)
 job=Path(e['job_path']); j,segs=runner.load(job); byref={v['ref']:v for v in segs.values()}
 replay=runner.empty(); proposals=[]
 for h in state['proposals']:
  p=job/'proposals'/f'{h}.json'; assert sha(p)==h
  replay=runner.validate_apply(replay,json.loads(p.read_bytes()),segs,j); replay['proposals'].append(h); proposals.append(bind(p))
 assert replay==state and hashlib.sha256(runner.encoded(replay)).hexdigest()==e['snapshot_sha256']
 checked=[]; qa={'reader_slices':0,'producer_slices':0}
 def walk(o):
  if isinstance(o,dict):
   if 'path' in o and 'sha256' in o:
    p=Path(o['path']); assert sha(p)==o['sha256']; checked.append(bind(p))
   if {'ref','start_char','end_char','quote'}<=o.keys():
    s=byref[o['ref']]; assert s['text'][o['start_char']:o['end_char']]==o['quote']; qa['reader_slices']+=1
   for v in o.values(): walk(v)
  elif isinstance(o,list):
   for v in o: walk(v)
 walk(reading)
 for r in state['records']:
  for v in r['evidence']:
   assert segs[v['segment_id']]['text'][v['start_char']:v['end_char']]==v['quote']; qa['producer_slices']+=1
 completed={l:{c['segment_id'] for c in state['coverage'] if c['layer']==l and c['extraction_state']=='completed'} for l in runner.LAYERS}
 cores=reading['core_refs']; overlap=[r for r in cores if all(byref[r]['id'] in ids for ids in completed.values())]
 policy=REPO/'research/bavli_dataset_runs/run_20261125_01/policy_notes/ANSWER_SET_STATUS_001.json'
 assert sha(policy)=='774d409907e8d441ca76d670342a395b42d7a4ee7195ae23643b37cf2e6beb4b'
 bindings={'queue':bind(q),'initial_reading':bind(rp),'snapshot':bind(sp),'run_contract':bind(cp),'runner':bind(runnerp),'policy':bind(policy),'policy_impact':bind(BASE/'POLICY_IMPACT_006.json'),'reader_bindings_verified':checked,'proposals':proposals,'verification_script':bind(Path(__file__))}
 result={'artifact_kind':'exact_version_pending_production_receipt','job_id':e['job_id'],'bindings':bindings,'completed_counts_by_layer':{l:len(v) for l,v in completed.items()},'independent_core_refs':cores,'compared_core_refs':overlap,'unprocessed_core_refs':[r for r in cores if r not in overlap],'qa':qa,'exact_readonly_prefix_replay':'PASS','semantic_verdict':None,'omission_count':None,'eligibility':{'full_tractate_admission':False,'choice_qa':False,'training':False,'human_certification':False,'later_version_inheritance':False},'scope_note':'Only completed sampled cores may support semantic comparison. Zero overlap is pending production, not omission or semantic acceptance. No alternative reader inspected. answer_set_status none alone is not a source error.'}
 return result,reading,state,segs,runner
if __name__=='__main__':
 name=sys.argv[1]; result,reading,state,segs,runner=load(name)
 if result['compared_core_refs']: print(json.dumps({'scope':result,'reading_keys':list(reading)},ensure_ascii=False,indent=2))
 else:
  result['status']='PENDING_PRODUCTION_NO_COMPLETED_SAMPLED_CORES'
  p=BASE/'comparisons'/f'{name}_batch001_exact_version.json'
  with p.open('x',encoding='utf8',newline='\n') as f: json.dump(result,f,ensure_ascii=False,sort_keys=True,indent=2); f.write('\n')
  print(json.dumps({'receipt':bind(p),'scope':0,'qa':result['qa'],'completed_counts':result['completed_counts_by_layer']}))
