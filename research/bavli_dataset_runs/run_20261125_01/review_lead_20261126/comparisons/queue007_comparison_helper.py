import json,hashlib,importlib.util,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p): return {'path':str(p),'sha256':sha(p)}
def canon(x): return hashlib.sha256((json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def load(name):
 q=next(x for x in json.loads((R/'COMPARISON_QUEUE_007.json').read_text()) if x['job_id']=='bavli_'+name)
 rp=Path(q['reading_path']); assert sha(rp)==q['reading_sha256']; rd=json.loads(rp.read_text())
 dp=R/('jobs/bavli_'+name+'.json');d=json.loads(dp.read_text())
 for x in [d['source'],d['frozen_plan']]+d['common_documents']: assert sha(x['path'])==x['sha256']
 sp=Path(q['snapshot_path']);assert sha(sp)==q['snapshot_sha256'];s=json.loads(sp.read_text()); rt=Path(q['job_path'])
 inv=json.loads((rt/'source_inventory.json').read_text()); src=json.loads(Path(d['source']['path']).read_text()); byid={x['id']:x for x in inv}; byref={x['ref']:x for x in inv}
 for x in inv: assert src['text'][x['source_index'][0]][x['source_index'][1]]==x['text']
 core=set(rd['core_refs']);done={byid[x['segment_id']]['ref'] for x in s['coverage'] if x['layer']=='claims' and x['extraction_state']=='completed'}
 return q,rd,d,s,rt,inv,src,byid,byref,core,done

def freeze(name,semantic):
 q,rd,d,s,rt,inv,src,byid,byref,core,done=load(name)
 def evidence(obj):
  out=[]
  def walk(x):
   if isinstance(x,dict):
    if all(k in x for k in ['quote','start_char','end_char']):
     seg=byid[x['segment_id']] if 'segment_id' in x else byref[x['ref']]
     assert seg['text'][x['start_char']:x['end_char']]==x['quote'];out.append(x)
    for v in x.values():walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(obj);return len(out)
 ev={'reader_exact_slices':evidence(rd),'producer_all_exact_slices':evidence(s),'failures':0,'inventory_original_source_segments_verified':len(inv)}
 runner=CO/'research/bavli_production_v1/runner.py'; before=sha(runner);sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('frozen_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 job,segs=m.load(rt);state=m.empty()
 for h in s['proposals']:
  pp=rt/'proposals'/f'{h}.json';assert sha(pp)==h
  prev=state['proposals'];state=m.validate_apply(state,json.loads(pp.read_text()),segs,job);state['proposals']=prev+[h]
 assert m.encoded(state)==m.encoded(s);assert sha(runner)==before
 bindings={'initial_reading':bind(q['reading_path']),'snapshot':bind(q['snapshot_path']),'source':d['source'],'plan':d['frozen_plan'],'plan_embedded_sha256':d['plan_sha256'],'descriptor':bind(R/('jobs/bavli_'+name+'.json')),'run_contract':bind(CO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),'contract_production_commit':'15bba19d80273232b4554dfe507ceb37e97843a2be97843a2','runner':bind(runner),'schema':bind(runner.parent/'schema.json'),'protocol':bind(runner.parent/'PROTOCOL.md'),'proposals':[bind(rt/'proposals'/f'{h}.json') for h in s['proposals']],'policy':bind(CO/'research/bavli_dataset_runs/run_20261125_01/policy_notes/ANSWER_SET_STATUS_001.json')}
 bindings['contract_production_commit']='15bba19d80273232b4554dfe507ceb37e97843a2'
 if name=='niddah':bindings['reader_coverage_correction']=bind(R/'readings/niddah_batch001.coverage_correction.json')
 prob=set();end=set()
 for b in rd.get('selected_blocks',[]):
  if 'probability_sample' in b['roles']:prob.update(b['core_refs'])
  if any(x in b['roles'] for x in ['opening_check','closing_check']):end.update(b['core_refs'])
 matrix={'source_total_segments':len(inv),'sampled_unique_cores':len(core),'compared_unique_cores':len(core&done),'pending_production_cores':len(core-done),'probability_core_segments_compared':len(prob&done),'endpoint_core_segments_compared':len(end&done),'overlap_core_segments_compared':len(prob&end&done),'producer_completed_claims_segments':len(done),'per_layer_completed_sampled_cores':{l:len({byid[x['segment_id']]['ref'] for x in s['coverage'] if x['layer']==l and x['extraction_state']=='completed'}&core) for l in sorted({x['layer'] for x in s['coverage']})},'compared_core_refs':sorted(core&done),'pending_core_refs':sorted(core-done)}
 records=[x for x in s['records'] if any(byid[e['segment_id']]['ref'] in core for e in x.get('evidence',[]))]
 doc={'artifact_kind':'exact_version_nonblind_bounded_comparison' if core&done else 'pending_production_receipt','bindings':bindings,'layer_matrix':matrix,'source_evidence_validation':ev,'readonly_prefix_replay':{'matched_exact_snapshot':True,'proposal_count':len(s['proposals']),'runner_unchanged':True,'report':m.report(state,segs)},'original_records_preserved':[{'id':x['id'],'layer':x['layer'],'release_state':x['release_state'],'canonical_sha256':canon(x),'supersedes':x.get('supersedes')} for x in records],'semantic_review':semantic,'task_eligibility':{k:False for k in ['argument_extraction','attribution','ml','qa','retrieval','scholar_choice','segmentation']},'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'later_versions_inherit_review':False,'other_lane_readers_inspected':False}
 cp=R/('comparisons/'+name+'_batch001_exact_version.json'); assert not cp.exists();cp.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 if core&done:
  v={k:doc[k] for k in ['bindings','layer_matrix','task_eligibility','tractate_accepted','full_review_receipt','human_certification','later_versions_inherit_review']};v.update({'verdict':semantic.get('verdict','ACCEPT_PARTIAL_WITH_EXCEPTIONS'),'comparison':bind(cp),'exceptions':semantic.get('exceptions',[]),'required_changes':semantic.get('required_changes',[]),'admission_owner':'global coordinator','remaining':'Uncompared cores, context-only readings, policy gates and later revisions confer no admission.'});vp=R/('verdicts/'+name+'_batch001_v2_verdict.json');assert not vp.exists();vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print('VERDICT',bind(vp))
 print('COMPARISON',bind(cp));print('COUNTS',matrix);print('EVIDENCE',ev)
