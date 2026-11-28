import json,hashlib,sys,importlib.util
from pathlib import Path
from collections import Counter
R=Path(__file__).resolve().parents[1]
CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
RT=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_moed_katan')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def canon(x):return hashlib.sha256((json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
rp=R/'readings/moed_katan_supplement002.json';assert sha(rp)=='4b17f31d2bc87ca7ef63607c1b8182f46cf3db211e24401a8e915e0f4e98d77c'
rd=json.loads(rp.read_text());dp=R/'jobs/bavli_moed_katan_supplement002.json';assert sha(dp)==rd['neutral_job']['sha256'];d=json.loads(dp.read_text())
for x in [d['source']]+d['common_documents']:assert sha(x['path'])==x['sha256']
sp=RT/'snapshots/100fd875fc82430d801f2800899a60070090305935f1b74f30a6efe29b9b9f66.json';assert sha(sp)==sp.stem;s=json.loads(sp.read_text())
inv=json.loads((RT/'source_inventory.json').read_text());src=json.loads(Path(d['source']['path']).read_text());bi={x['id']:x for x in inv};br={x['ref']:x for x in inv}
for x in inv:assert src['text'][x['source_index'][0]][x['source_index'][1]]==x['text']
def slices(obj):
 n=0
 def walk(x):
  nonlocal n
  if isinstance(x,dict):
   if all(k in x for k in ['quote','start_char','end_char']):
    z=br[x['ref']] if 'ref' in x else bi[x['segment_id']];assert z['text'][x['start_char']:x['end_char']]==x['quote'];n+=1
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(obj);return n
rv=slices(rd);sv=slices(s)
runner=CO/'research/bavli_production_v1/runner.py';before=sha(runner);sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('exact_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(RT);state=m.empty()
for h in s['proposals']:
 pp=RT/'proposals'/f'{h}.json';assert sha(pp)==h;prev=state['proposals'];state=m.validate_apply(state,json.loads(pp.read_text()),segs,job);state['proposals']=prev+[h]
assert m.encoded(state)==m.encoded(s);assert sha(runner)==before
initialp=RT/'snapshots/09908653624cc6ad0a45a5261a2ffa41b90fb6a681708943a5aedb814801304b.json';assert sha(initialp)==initialp.stem;initial=json.loads(initialp.read_text());old={x['id']:x for x in initial['records']};new={x['id']:x for x in s['records']};assert s['proposals'][:len(initial['proposals'])]==initial['proposals'];ph='f4f69c4146460df24a76d2a9cc099c7a54bf90bda28372b2d6e8ca92df45e196';assert s['proposals'][-1]==ph;proposal=json.loads((RT/'proposals'/f'{ph}.json').read_text());assert len(proposal['records'])==2
ids=['mk.r022.answers_alternative','mk.r022.oil_alternatives'];changes=[]
for rid in ids:
 a=old[rid];b=new[rid+'.metadata026'];assert new[rid]['release_state']=='superseded' and b['release_state']=='valid' and b['supersedes']==rid and a['origin']=='source_paraphrase' and b['origin']=='editorial_inference'
 for k in ['content','evidence','links','uncertainty']:assert a[k]==b[k]
 for endpoint in [b['content']['source_id'],b['content']['target_id']]:assert old[endpoint]==new[endpoint] and new[endpoint]['release_state']=='valid'
 coverage=[x for x in s['coverage'] if x['layer']=='edges' and x['segment_id']==b['evidence'][0]['segment_id']];assert len(coverage)==1 and b['id'] in coverage[0]['record_ids'] and rid not in coverage[0]['record_ids']
 changes.append({'old_id':rid,'new_id':b['id'],'old_record_sha256':canon(a),'superseded_record_sha256':canon(new[rid]),'new_record_sha256':canon(b),'only_semantic_metadata_change':'origin source_paraphrase to editorial_inference; explicitness already editorial_reconstruction','source_ref':bi[b['evidence'][0]['segment_id']]['ref'],'endpoints_unchanged':True,'dependent_coverage_repoints_to_new_id':True})
refs=[f'Moed Katan 9b:{i}' for i in range(13,21)];evidence=[]
for ref in refs:
 z=br[ref];t=src['text'][z['source_index'][0]][z['source_index'][1]];assert t==z['text'];evidence.append({'ref':ref,'original_text_sha256':hashlib.sha256(t.encode()).hexdigest()})
doc={'artifact_kind':'targeted_exact_version_metadata_correction_receipt','result':'VERIFIED_TARGETED_METADATA_CORRECTION','bindings':{'initial_reading':bind(rp),'descriptor':bind(dp),'source':d['source'],'common_documents':d['common_documents'],'initial_snapshot':bind(initialp),'new_snapshot':bind(sp),'targeted_proposal':bind(RT/'proposals'/f'{ph}.json'),'intake':bind(R/'MOED_KATAN_METADATA026_INTAKE.json'),'initial_comparison':bind(R/'comparisons/moed_katan_supplement002_exact_version.json'),'initial_verdict':bind(R/'verdicts/moed_katan_supplement002_v2_verdict.json'),'reviewer_correction':bind(R/'comparisons/moed_katan_supplement002_reviewer_correction001.json'),'verdict_addendum':bind(R/'verdicts/moed_katan_supplement002_v2_verdict_addendum001.json'),'runner':bind(runner),'schema':bind(runner.parent/'schema.json'),'protocol':bind(runner.parent/'PROTOCOL.md'),'run_contract':bind(CO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),'audit_script':bind(Path(__file__)),'new_prefix_proposals':[bind(RT/'proposals'/f'{h}.json') for h in s['proposals'][len(initial['proposals']):]]},'changes':changes,'source_refs_reread':refs,'source_hash_receipts':evidence,'semantic_findings':['Both distinctions are reasonable editorial comparisons between adjacent explanations; original source does not explicitly declare an exhaustive opposition. Corrected origin matches existing explicitness and uncertainty.','Rav Nahman bar Yitzhak answers through festival-law scope; Ravina answers through repayment distress. These remain distinct explanatory moves, not a forced personal retraction.','Myrrh-oil definitions belong to Rav Huna bar Hiyya and Rav Yirmeya bar Ami. Their adjacency supports editorial alternative linkage, without assigning any additional position or exclusivity.','Initial comparison did not flag these origin-field inconsistencies. This targeted receipt records the correction without rewriting that historical review or claiming a newly discovered source proposition error.'],'read_only_replay':{'exact_snapshot_match':True,'proposal_count':len(s['proposals']),'initial_prefix_preserved':True,'runner_unchanged':True},'mechanical_evidence_validation':{'reader_exact_slices':rv,'new_snapshot_exact_slices':sv,'failures':0,'mechanical_validation_does_not_admit_new_content':True},'newly_compared_core_segments':0,'new_independent_reading_core_segments':0,'new_task_eligibility':False,'full_tractate_admission':False,'prior_comparison_inherited_to_new_snapshot':False,'later_versions_inherit_review':False,'human_certification':False,'producer_modified':False,'prior_artifacts_modified':False,'scope':'Only two metadata corrections and dependent endpoints/coverage. Three intervening production proposals receive replay/evidence validation only, no semantic admission.'}
cp=R/'comparisons/moed_katan_metadata026_correction001.json';assert not cp.exists();cp.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf8');assert sha(sp)==sp.stem and sha(initialp)==initialp.stem;print(json.dumps({'receipt':bind(cp),'script':bind(Path(__file__)),'evidence':doc['mechanical_evidence_validation'],'proposal_count':len(s['proposals'])}))
