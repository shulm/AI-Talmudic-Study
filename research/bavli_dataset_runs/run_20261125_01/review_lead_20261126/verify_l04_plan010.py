import sys
sys.dont_write_bytecode=True
import json,hashlib,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parent
REPO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':p.as_posix(),'sha256':sha(p)}
ip=BASE/'L04_INTAKE_010.json';intake=json.loads(ip.read_bytes())
previousp=BASE/'L04_COMPARISON_PLAN_008.json';assert sha(previousp)=='67116971ae0e057a1fcffe3f739090ee6670bd80dcaaaa4c383d03fcb769be57'
previous=json.loads(previousp.read_bytes());previousjobs={v['job_id']:v for v in previous['jobs']}
cp=REPO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json';contract=json.loads(cp.read_bytes())
rp=REPO/'research/bavli_production_v1/runner.py';assert sha(rp)==contract['production_files']['research/bavli_production_v1/runner.py']
spec=importlib.util.spec_from_file_location('readonly_runner',rp);runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
jobs=[]
for entry in intake['jobs']:
 name=entry['job_id'].removeprefix('bavli_')
 comparisonp=BASE/f'comparisons/{name}_batch001_exact_version.json';comparison=json.loads(comparisonp.read_bytes())
 readingp=BASE/f'readings/{name}_batch001.json';assert sha(readingp)==comparison['bindings']['initial_reading']['sha256'];reading=json.loads(readingp.read_bytes())
 sp=Path(entry['snapshot_path']);assert sha(sp)==entry['snapshot_sha256'];state=json.loads(sp.read_bytes());job=sp.parent.parent
 j,segs=runner.load(job);byref={v['ref']:v for v in segs.values()};order={v['ref']:i for i,v in enumerate(segs.values())}
 def ordered(refs):return sorted(refs,key=lambda ref:order[ref])
 replay=runner.empty();props=[]
 for h in state['proposals']:
  p=job/'proposals'/f'{h}.json';assert sha(p)==h
  replay=runner.validate_apply(replay,json.loads(p.read_bytes()),segs,j);replay['proposals'].append(h);props.append(bind(p))
 assert replay==state and hashlib.sha256(runner.encoded(replay)).hexdigest()==entry['snapshot_sha256']
 complete={l:{segs[c['segment_id']]['ref'] for c in state['coverage'] if c['layer']==l and c['extraction_state']=='completed'} for l in runner.LAYERS}
 cores=set(reading['core_refs']);eligible=cores&complete['claims'];alllayers=cores.intersection(*complete.values())
 prior=set(comparison.get('compared_core_refs',comparison.get('core_refs',comparison.get('layer_matrix',{}).get('compared_core_refs',[]))))
 assert prior<=cores
 oldsp=Path(comparison['bindings']['snapshot']['path']);assert sha(oldsp)==comparison['bindings']['snapshot']['sha256'];old=json.loads(oldsp.read_bytes())
 oldcomplete={segs[c['segment_id']]['ref'] for c in old['coverage'] if c['layer']=='claims' and c['extraction_state']=='completed'}
 new=eligible-prior;newlyproduced=eligible-oldcomplete
 cohorts={}
 planp=BASE/f'frozen_plans/bavli_{name}.json';plan=json.loads(planp.read_bytes())
 expected_plan=comparison['bindings'].get('plan',{}).get('sha256',reading.get('plan_file_sha256'))
 if expected_plan:assert sha(planp)==expected_plan
 for b in plan['review_blocks']:
  refs={v['ref'] for v in b['spans']}
  for role in b['roles']:cohorts.setdefault(role,set()).update(refs)
 checked=[]
 def walk(o):
  if isinstance(o,dict):
   if 'path' in o and 'sha256' in o:
    p=Path(o['path']);assert sha(p)==o['sha256'];checked.append(bind(p))
   for v in o.values():walk(v)
  elif isinstance(o,list):
   for v in o:walk(v)
 walk(reading.get('bindings',{}))
 jobs.append({'job_id':entry['job_id'],'snapshot':bind(sp),'direct_reading':bind(readingp),'prior_exact_comparison':bind(comparisonp),'prior_snapshot':bind(oldsp),'reader_bindings_verified':checked,'proposals':props,'readonly_exact_prefix_replay':'PASS','completed_per_layer':{l:len(v) for l,v in complete.items()},'lane_declared_counts_match':all(len(v)==entry['lane_declared_completed_each_layer'] for v in complete.values()),'direct_sampled_core_count':len(cores),'completed_claim_direct_core_refs':ordered(eligible),'completed_all_layers_direct_core_refs':ordered(alllayers),'prior_compared_direct_core_refs':ordered(prior),'newly_available_for_first_direct_core_comparison_refs':ordered(new),'newly_completed_claim_direct_core_refs_since_prior_snapshot':ordered(newlyproduced),'already_compared_refs_requiring_new_version_check':ordered(eligible&prior),'still_unprocessed_direct_core_refs':ordered(cores-complete['claims']),'per_cohort':{role:{'direct_cores':len(refs&cores),'completed_claim_direct_cores':len(refs&eligible),'new_first_comparison_cores':len(refs&new)} for role,refs in cohorts.items()},'newly_completed_production_refs_without_direct_core_reading':ordered(complete['claims']-oldcomplete-cores),'prior_proposal_prefix_preserved':state['proposals'][:len(old['proposals'])]==old['proposals'],'semantic_verdict':None,'new_source_reading_credit':0,'prior_admission_inherited':False,'task_eligibility_changed':False})
for v in jobs:
 priorplan=previousjobs.get(v['job_id'])
 if priorplan:
  old008p=Path(priorplan['snapshot']['path']);assert sha(old008p)==priorplan['snapshot']['sha256'];old008=json.loads(old008p.read_bytes())
  _,ss=runner.load(Path(v['snapshot']['path']).parent.parent)
  oldrefs={ss[c['segment_id']]['ref'] for c in old008['coverage'] if c['layer']=='claims' and c['extraction_state']=='completed'}
  now=json.loads(Path(v['snapshot']['path']).read_bytes());nowrefs={ss[c['segment_id']]['ref'] for c in now['coverage'] if c['layer']=='claims' and c['extraction_state']=='completed'}
  rank={s['ref']:i for i,s in enumerate(ss.values())}
  v['difference_from_plan008']={'job_present_in_008':True,'snapshot008':priorplan['snapshot'],'completed_claim_count_increase':len(nowrefs)-len(oldrefs),'newly_completed_production_claim_refs':sorted(nowrefs-oldrefs,key=rank.get),'no_longer_completed_claim_refs':sorted(oldrefs-nowrefs,key=rank.get),'new_direct_claim_overlap_refs':sorted(set(v['completed_claim_direct_core_refs'])-set(priorplan['completed_claim_direct_core_refs']),key=rank.get),'removed_direct_claim_overlap_refs':sorted(set(priorplan['completed_claim_direct_core_refs'])-set(v['completed_claim_direct_core_refs']),key=rank.get),'proposal_prefix008_preserved':now['proposals'][:len(old008['proposals'])]==old008['proposals']}
 else:
  v['difference_from_plan008']={'job_present_in_008':False,'note':'New job in intake010; compare to bound prior exact comparison, not zero historical review.'}
out={'artifact_kind':'hash_bound_coverage_overlap_plan_only','intake':bind(ip),'run_contract':bind(cp),'runner':bind(rp),'planning_script':bind(Path(__file__)),'jobs':jobs,'totals':{'completed_claim_direct_sampled_cores':sum(len(v['completed_claim_direct_core_refs']) for v in jobs),'new_first_direct_comparison_cores':sum(len(v['newly_available_for_first_direct_core_comparison_refs']) for v in jobs),'newly_completed_claim_direct_cores':sum(len(v['newly_completed_claim_direct_core_refs_since_prior_snapshot']) for v in jobs),'previously_compared_cores_needing_new_version_check':sum(len(v['already_compared_refs_requiring_new_version_check']) for v in jobs),'new_source_reading_credit':0},'restrictions':['Integrity and set intersections only; no semantic comparison, admission or correction verification.','Prior comparisons bind older snapshots; overlapping refs require new-version review and do not inherit clearance.','Only existing direct readings used for coordinate planning; no new source-reader independence or reading credit claimed.','Context refs and producer risk tips excluded from direct sampled core counts.','Existing originals and bound outputs unchanged.']}
out['previous_plan008']=bind(previousp)
out['pending_supplement002']={'job_id':'bavli_moed_katan','status':'EXCLUDED_PENDING_FREEZE_AND_COMPARISON','reading_inspected':False,'new_reading_credit':0,'scope_note':'No supplement reading opened; no supplement semantic review or capacity counted.'}
out['separate_graves_correction_receipt']='Not checked by this coverage plan; no correction clearance.'
p=BASE/'L04_COMPARISON_PLAN_010.json'
with p.open('x',encoding='utf8',newline='\n') as f:json.dump(out,f,ensure_ascii=False,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'artifact':bind(p),'totals':out['totals'],'jobs':[{'job_id':v['job_id'],'completed_direct':len(v['completed_claim_direct_core_refs']),'new':v['newly_available_for_first_direct_core_comparison_refs'],'prior':len(v['already_compared_refs_requiring_new_version_check']),'count_match':v['lane_declared_counts_match']} for v in jobs]}))
