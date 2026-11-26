"""Read-only exact-chain verifier and writer for manually adjudicated comparison configs."""
import json,hashlib,importlib.util,sys
from pathlib import Path
B=Path(__file__).resolve().parent.parent;C=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
h=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();bind=lambda p:dict(path=str(Path(p).resolve()),sha256=h(p));read=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
cfg=json.load(sys.stdin);name=cfg['name'];q=next(x for x in read(B/'COMPARISON_QUEUE_007.json') if x['job_id']=='bavli_'+name)
rp=Path(q['reading_path']);pp=Path(q['snapshot_path']);J=Path(q['job_path']);assert h(rp)==q['reading_sha256'] and h(pp)==q['snapshot_sha256'];r=read(rp);p=read(pp)
runner=C/'research/bavli_production_v1/runner.py';sys.dont_write_bytecode=True;sp=importlib.util.spec_from_file_location('queue7runner',runner);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);j,segs=m.load(J);texts={x['ref']:x['text'] for x in segs.values()};refs={k:v['ref'] for k,v in segs.items()}
def evcheck(x):
 n=0
 if isinstance(x,dict):
  if 'quote' in x and ('start_char' in x or 'start' in x):
   ref=x.get('ref',x.get('source_ref'));t=texts[ref] if ref else segs[x['segment_id']]['text'];a=x.get('start_char',x.get('start'));b=x.get('end_char',x.get('end'));assert t[a:b]==x['quote'];n+=1
  for z in x.values():n+=evcheck(z)
 elif isinstance(x,list):
  for z in x:n+=evcheck(z)
 return n
def bindingcheck(x):
 if isinstance(x,dict):
  if 'path' in x and 'sha256' in x:assert h(x['path'])==x['sha256']
  for z in x.values():bindingcheck(z)
 elif isinstance(x,list):
  for z in x:bindingcheck(z)
bindingcheck(r.get('bindings',{}))
for k in ['source','original_source_schema','frozen_plan','common_documents']:bindingcheck(r.get(k,{}))
s=m.empty()
for ph in p['proposals']:
 f=J/'proposals'/f'{ph}.json';assert h(f)==ph;prev=s['proposals'];s=m.validate_apply(s,read(f),segs,j);s['proposals']=prev+[ph]
assert m.encoded(s)==m.encoded(p) and m.sha(m.encoded(s))==q['snapshot_sha256'];report=m.report(s,segs);rn=evcheck(r);pn=evcheck(p)
blocks=r.get('selected_blocks',[]);cores=r.get('core_refs',[])
if not cores:
 for z in blocks:cores+=z.get('core_refs',z.get('refs',[]))
cores=list(dict.fromkeys(cores));assert cores
done={l:{refs[x['segment_id']] for x in p['coverage'] if x['layer']==l and x['extraction_state']=='completed'} for l in m.LAYERS};comp=set.intersection(set(cores),*done.values())
active={x['id']:x for x in p['records'] if x['release_state']=='valid'};rh=lambda x:m.sha(m.encoded(x))
corefinding=lambda x:any(e.get('ref',e.get('source_ref')) in comp for e in x.get('evidence',[]))
findings=r.get('findings',r.get('claims',[]));cf=[x for x in findings if corefinding(x)]
rows=[]
for rid,ts in cfg.get('mapping',{}).items():
 x=next(x for x in findings if x['id']==rid)
 rows.append(dict(reader=x,reader_sha256=rh(x),producer=[dict(record=active[t],sha256=rh(active[t])) for t in ts],positions=[z for z in active.values() if z['layer']=='positions' and z['content']['claim_id'] in ts],assessment=cfg.get('mapping_notes',{}).get(rid,'source meaning compared; granularity differs without implying omission')))
if comp:assert {x['reader']['id'] for x in rows}=={x['id'] for x in cf},'mapping must cover each completed-core finding'
cohorts=dict(independent_core_segments=len(cores),compared_unique_core_segments=len(comp),pending_core_segments=len(set(cores)-comp))
for role,key in [('probability_sample','probability'),('opening_check','opening'),('closing_check','closing')]:
 rr={ref for b in blocks if role in b.get('roles',[]) for ref in b.get('core_refs',b.get('refs',[]))};cohorts[key+'_read_segments']=len(rr);cohorts[key+'_compared_segments']=len(rr&comp)
end={ref for b in blocks if any(x in b.get('roles',[]) for x in ['opening_check','closing_check']) for ref in b.get('core_refs',b.get('refs',[]))};prob={ref for b in blocks if 'probability_sample' in b.get('roles',[]) for ref in b.get('core_refs',b.get('refs',[]))};cohorts['compared_endpoint_probability_overlap']=len(end&prob&comp)
bindings=dict(queue=bind(B/'COMPARISON_QUEUE_007.json'),initial_reading=bind(rp),snapshot=bind(pp),source=bind(Path(j['source_root'])/m.read(J/'source_manifest.json')['tractates'][[x['title'] for x in m.read(J/'source_manifest.json')['tractates']].index(j['tractate'])]['source_path']),job_descriptor=bind(B/'jobs'/f'bavli_{name}.json'),run_contract=bind(C/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),runner=bind(runner),schema=bind(runner.parent/'schema.json'),protocol=bind(runner.parent/'PROTOCOL.md'),plan=bind(B/'frozen_plans'/f'bavli_{name}.json'),proposals=[bind(J/'proposals'/f'{ph}.json') for ph in p['proposals']],policy_impact=bind(B/'POLICY_IMPACT_006.json'),comparison_script=bind(__file__),manual_config_sha256=rh(cfg))
out=dict(artifact_kind='nonblind_exact_version_partial_comparison' if comp else 'pending_production_exact_version_receipt',bindings=bindings,comparator=dict(agent_id='/root/compare_zevachim_wave2',blind=False,reader_frozen_before_comparison=True),cohorts=cohorts,compared_core_refs=[x for x in cores if x in comp],pending_core_refs_not_omissions=[x for x in cores if x not in comp],denominators=cfg.get('denominators',{}),completed_core_reader_findings=len(cf),claim_comparisons=rows,manual_adjudication=cfg,context_records=[dict(record=active[t],sha256=rh(active[t])) for t in cfg.get('context_records',[])],qa=dict(reader_slices=rn,producer_slices=pn,all_slices_match=True,replay=dict(read_only=True,method='load/empty/validate_apply exact frozen proposal chain without lock/current/submit/write',pass_exact=True,snapshot_sha256=q['snapshot_sha256'],proposal_count=len(p['proposals']),report=report)),task_eligibility={k:False for k in ['ml','scholar_choice','attribution','retrieval','qa','argument_extraction','segmentation']},tractate_accepted=False,human_certification=False,full_review_receipt=False,limitations=['No omissions scored on uncompleted sampled cores.','No later snapshot inheritance or whole-tractate admission.','Question answer-set enum none is an interpretation risk, not automatic error or missing answer.','Composite source findings are not automatically atomic claims or supported formal edges.'])
cp=B/'comparisons'/f'{name}_batch001_exact_version.json';assert not cp.exists();cp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8');res=dict(comparison=bind(cp),cohorts=cohorts,reader_slices=rn,producer_slices=pn,core_findings=len(cf),proposals=len(p['proposals']))
if comp:
 v=dict(verdict=cfg['verdict'],bindings=bindings,comparison=bind(cp),scope=cohorts,required_changes=cfg.get('required_changes',[]),exceptions=cfg.get('exceptions',[]),layer_matrix=dict(independent_core_denominators=cfg.get('denominators',{}),producer_completed_per_layer=report['completed_by_layer'],sample_completed_per_layer={k:len(set(cores)&v) for k,v in done.items()},source_segments_total=report['source_segments']),task_eligibility=out['task_eligibility'],tractate_accepted=False,full_review_receipt=False,human_certification=False,admission_owner='global coordinator',remaining=cfg.get('remaining','Continue frozen source sample and new exact-version review; unchanged eligibility.'))
 vp=B/'verdicts'/f'{name}_batch001_v2_verdict.json';assert not vp.exists();vp.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8');res['verdict']=bind(vp)
print(json.dumps(res,ensure_ascii=False))
