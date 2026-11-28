import json, hashlib, sys, importlib.util
from pathlib import Path
from collections import Counter
import jsonschema
sys.dont_write_bytecode=True
R=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
RT=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_makkot')
OUT=Path(__file__).parent
def read(p): return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p): return {'path':str(p),'sha256':sha(p)}
def canon(x): return hashlib.sha256((json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
def save(name,x):
 p=OUT/name; data=(json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode();
 if p.exists(): assert p.read_bytes()==data, 'immutable conflict'
 else: p.write_bytes(data)
 side=p.with_name(p.name+'.sha256'); content=(sha(p)+'  '+p.name+'\n').encode()
 if side.exists(): assert side.read_bytes()==content
 else: side.write_bytes(content)
 return bind(p)
rp=OUT.parent/'makkot_delegated020.json'; expected='a5284218178da7378f34407813fc92f5d82c20a896d4c31dbfd37c4504372ac5'
assert sha(rp)==expected and (rp.with_name(rp.name+'.sha256')).read_text().split()[0]==expected
rd=read(rp); receipt=OUT.parent/'makkot_delegated020_validation_receipt.json'; assert read(receipt)['sha256']==expected
dp=R/'jobs/bavli_makkot_delegated020.json'; d=read(dp); assert sha(dp)==rd['job_sha256']
reservation=R/'L04_COMPARISON_RESERVATION_027.json'; assert sha(reservation)=='9ce101f41098d1a8393474242849f477ea4e15e6e1f0e3355fb239f025851903'
for b in rd['bindings']: assert sha(b['path'])==b['sha256']
plan=read(d['frozen_plan']['path']); payload={k:v for k,v in plan.items() if k!='plan_sha256'}
assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(payload,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()==d['plan_sha256']==rd['plan_sha256']
jsonschema.Draft202012Validator(read(d['common_documents'][1]['path'])).validate(rd['proposal'])
sp=RT/'snapshots/bf3f3242d3a8c9e476640240788bc653646a232e2362fb1f34d2b6d1cf5ba172.json'; assert sha(sp)==sp.stem
s=read(sp); inv=read(RT/'source_inventory.json'); src=read(d['source']['path']); bi={x['id']:x for x in inv}; br={x['ref']:x for x in inv}
for x in inv: assert src['text'][x['source_index'][0]][x['source_index'][1]]==x['text']
def slices(obj):
 n=0
 def walk(x):
  nonlocal n
  if isinstance(x,dict):
   if all(k in x for k in ['quote','start_char','end_char']):
    z=br.get(x.get('ref',x.get('segment_id'))) or bi[x['segment_id']]; assert z['text'][x['start_char']:x['end_char']]==x['quote']; n+=1
   for v in x.values(): walk(v)
  elif isinstance(x,list):
   for v in x: walk(v)
 walk(obj); return n
rv=slices(rd); sv=slices(s)
contractp=CO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'; contract=read(contractp)
runner=CO/'research/bavli_production_v1/runner.py'
for rel,h in contract['production_files'].items(): assert sha(CO/rel)==h
sys.path.insert(0,str(runner.parent)); spec=importlib.util.spec_from_file_location('exact_runner',runner); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
job,segs=m.load(RT); state=m.empty()
for h in s['proposals']:
 pp=RT/'proposals'/f'{h}.json'; assert sha(pp)==h
 prev=state['proposals']; state=m.validate_apply(state,read(pp),segs,job); state['proposals']=prev+[h]
assert m.encoded(state)==m.encoded(s)
core=set(rd['core_refs']); rr={x['id']:x for x in rd['proposal']['records']}; pr={x['id']:x for x in s['records'] if x['release_state']=='valid'}
for x in rr.values():
 assert all(z in rr for z in x['links'])
for ref in core:
 spans=sorted((e['start_char'],e['end_char']) for x in rr.values() if x['layer']=='structure' and x['content']['primary'] for e in x['evidence'] if e['segment_id']==ref)
 assert spans[0][0]==0 and spans[-1][1]==len(br[ref]['text']) and all(a[1]==b[0] for a,b in zip(spans,spans[1:]))
mapping={}
for start,prefix,names in [(1,'ma.r006.','resolve resolve forget remind text text text sea concern river seabar seabarreason teruma presumption terumaconcl'),(16,'ma.r007.','meirmoney meirmoney sagesmoney eighty eighty forty onerishah ullameir fineob.q meirakiva version yehuda akiva akiva yehinfer ulla2 dualob.q rl warnq.q combined combined commonfine.q notakiva severe.q method warning yirmeya announce meirannounce divide money lashes abaye rava aggregate aggregate'),(52,'ma.r008.','self contradiction hazama manysets yehuda adda yishmael visibility visibility vision vision')]:
 for i,n in enumerate(names.split(),start): mapping[f'c{i:02}']=prefix+n+('' if n.endswith('.q') else '.c')
mapping['c63']='ma.r007.meirakiva.c'
qm=dict(zip(['q%02d'%i for i in range(1,10)],['ma.r006.likewise.q','ma.r007.meirwhy.q','ma.r007.ywhy.q','ma.r007.notq.q','ma.r007.meirwarningq.q','ma.r007.whydivide.q','ma.r007.moneyq.q','ma.r008.why.q','ma.r008.obviousvis.q']))
mapping.update(qm); assert all(v in pr for v in mapping.values())
coreclaims=[x for x in rr.values() if x['layer']=='claims' and any(e['segment_id'] in core for e in x['evidence'])]
assert len(coreclaims)==63 and {x['id'] for x in coreclaims}==set(mapping)-set(qm)
pe=[x for x in pr.values() if x['layer']=='edges']
edge_review=[]
missing={'e18':'Alternative placement of Ulla qualifies the first placement; explicit איכא דמתני.','e19':'R. Akiva expressly rejects R. Yehuda\'s rationale with לא מן השם.','e21':'The inference about R. Yehuda derives from his preceding reason; מכלל makes this explicit. Prefer support from the baraita reason to the inference, rather than reader continuation direction.','e24':'אלא אמר ריש לקיש replaces the single-source derivation after its objection; add correction with proof-stage scope.','e34':'The sages use the same verse for proclamation rather than the prohibition attributed to R. Meir; preserve this distinction.','e41':'The negative counterexample qualifies the general hazama rule, not only the positive example.','e42':'Explicit אבל distinguishes witness-location hazama from victim/killer contradiction.'}
editorial={'e11','e13','e43'}
for i in range(1,49):
 e=rr[f'e{i:02}']; c=e['content']; a=mapping[c['source_id']]; b=mapping[c['target_id']]
 matches=[z['id'] for z in pe if z['content']['source_id']==a and z['content']['target_id']==b and z['content']['relation']==c['relation']]
 if matches: assessment='typed_relation_present'
 elif e['id'] in missing: assessment='confirmed_typed_relation_omission'
 elif e['id'] in editorial: assessment='reader_explicitness_overclaim_and_unrepresented_editorial_opposition'
 elif a==b: assessment='reasonable_internal_granularity_no_self_edge_required'
 elif e['id']=='e27': assessment='reasonable_relation_target_granularity'; matches=['ma.r007.combined.support']
 else: raise AssertionError((e['id'],a,b))
 edge_review.append({'reader_id':e['id'],'reader_record_sha256':canon(e),'reader_content':c,'producer_endpoint_mapping':[a,b],'producer_edge_ids':matches,'assessment':assessment,'note':missing.get(e['id'],'Tannaitic disagreement is explicit, but directed objection as a discourse event is editorial.' if e['id'] in editorial else '')})
findings=[{'id':'MA020-STATUS01','category':'confirmed_producer_error','severity':'targeted','refs':['Makkot 5a:11'],'producer_ids':['ma.r008.vision.c','ma.r008.vision.p','ma.r008.vision.answer'],'reader_ids':['c61','c62','e47','e48'],'finding':'Producer proposition says the teaching rejects allowing extraordinary vision, but marks that rejection itself rejected. The hypothetical allowance is rejected; the teaching rejecting it is accepted.','required_correction':'Create additive revision separating rejected hava-amina from accepted teaching, or mark the existing negative proposition asserted and its position accordingly. Recheck answer endpoint.'}, {'id':'MA020-ATTR01','category':'restricted_eligibility','severity':'qualification','refs':['Makkot 4b:11'],'producer_ids':['ma.r007.yirmeya.c','ma.r007.yirmeya.p'],'reader_ids':['c42'],'finding':'R. Yirmeya explains a scriptural source for R. Meir. Producer position names Yirmeya while proposition names Meir: valid as explanation-holder, not a direct Meir preference observation. Preserve two levels before scholar-choice use.','required_correction':'No factual speaker replacement required; any future holder-oriented export must distinguish expositor from attributed legal holder.'}]
for eid,note in missing.items(): findings.append({'id':'MA020-EDGE-'+eid,'category':'confirmed_producer_typed_relation_omission','severity':'targeted','refs':list(dict.fromkeys(e['segment_id'] for e in rr[eid]['evidence'])),'reader_ids':[eid],'producer_ids':[mapping[rr[eid]['content']['source_id']],mapping[rr[eid]['content']['target_id']]],'finding':note,'required_correction':'Add evidenced typed relation with stage-appropriate endpoints; preserve old records. Do not treat prose presence as a typed edge.'})
reader_corrections=[{'id':'MA020-READER01','reader_ids':['c09.a'],'category':'unresolved_attribution_scope','finding':'Reader assigns three-log explanatory concern directly to Rav. Production leaves it anonymous. No fresh אמר marks whether חיישינן is included in Rav\'s report or an editorial explanation; preserve uncertainty, not a confirmed false attribution.'},{'id':'MA020-READER02','reader_ids':['c05.a','c06.a'],'category':'restricted_holder_interpretation','finding':'Abaye recalls Rav Yosef\'s report about Rav\'s textual version and RYBN\'s scope. This is not a newly quoted direct speech by either original authority. Transmission and content must remain distinct.'},{'id':'MA020-READER03','reader_ids':sorted(editorial),'category':'reader_error','finding':'Directed objection edges for juxtaposed tannaitic disagreements overstate source-explicit discourse. Retain substantive disagreement, use editorial reconstruction for chosen directional graph encoding.'},{'id':'MA020-READER04','reader_ids':['e21'],'category':'reader_relation_refinement','finding':'מכלל is inference from R. Yehuda\'s reason; a support relation from premise to inference is more precise than the recorded continuation edge.'}]
priorp=R/'comparisons/makkot_batch001_exact_version.json'; prior=read(priorp); priorrefs=set(prior['layer_matrix']['compared_core_refs']); assert not(core&priorrefs)
active=[x for x in pr.values() if any(bi[e['segment_id']]['ref'] in core for e in x['evidence'])]
attrs=[x for x in coreclaims if any(y['content']['claim_id']==x['id'] and y['content']['holder_candidates'] for y in rr.values() if y['layer']=='positions')]
dens={'independently_found_core_claims':63,'core_claims_with_nonempty_holder_candidates':len(attrs),'core_condition_bearing_claims':sum(bool(x['content']['conditions']) for x in coreclaims),'core_questions':9,'proposed_answer_sets':9,'answer_set_definition':'one local question inventory per core question; not nine exhaustive or mutually exclusive choice sets','independent_core_argument_edges':48,'context_claims':15,'context_questions':3,'context_argument_edges':13,'whole_reading_claims':78,'whole_reading_edges':61,'atomicity_certified':False}
bindings={'reading':bind(rp),'reading_sidecar':bind(rp.with_name(rp.name+'.sha256')),'reader_unique_receipt':bind(receipt),'neutral_job':bind(dp),'reservation':bind(reservation),'source_and_common':rd['bindings'],'snapshot':bind(sp),'run_contract':bind(contractp),'production_git_commit':contract['production_git_commit'],'runner':bind(runner),'production_schema':bind(runner.parent/'schema.json'),'production_protocol':bind(runner.parent/'PROTOCOL.md'),'prior_comparison':bind(priorp),'audit_script':bind(Path(__file__)),'source_inventory':bind(RT/'source_inventory.json'),'production_job':bind(RT/'JOB.json'),'proposals':[bind(RT/'proposals'/f'{h}.json') for h in s['proposals']]}
matrix={'source_total_segments':len(inv),'cohort':'original_probability_sample','compared_core_refs':rd['core_refs'],'sampled_unique_cores':30,'compared_unique_cores':30,'probability_core_segments_compared':30,'endpoint_core_segments_compared':0,'prior_comparison_overlap':0,'newly_compared_unique_cores':30,'prior_historical_compared_cores':len(priorrefs),'context_refs_read':rd['context_read_refs'],'context_core_credit':0,'new_source_reading_credit':0,'per_layer_completed_sampled_cores':{l:sum(c['layer']==l and c['extraction_state']=='completed' and bi[c['segment_id']]['ref'] in core for c in s['coverage']) for l in m.LAYERS}}
assert all(n==30 for n in matrix['per_layer_completed_sampled_cores'].values())
answers=[]
for qid,pid in qm.items():
 ans=[e['content']['source_id'] for e in rr.values() if e['layer']=='edges' and e['content']['relation']=='answer' and e['content']['target_id']==qid]
 answers.append({'reader_question_id':qid,'producer_question_id':pid,'reader_answers':ans,'status':'local_partial_inventory_not_exhaustive_choice_set','comparability':'Successive challenged proofs, not interchangeable accepted answers.' if qid=='q03' else 'Alternative derivations of same rule, not opposing legal outcomes.' if qid in ['q06','q08'] else 'Single local explanatory response; no scholar-choice contrast certified.'})
doc={'artifact_kind':'exact_version_nonblind_comparison','actual_comparator_agent_id':'/root/makkot_compare020','launch_provenance':'Parent dispatched fresh fork:none independent NONBLIND comparator; no producer role; reader froze before comparison; reader terminal usage-limit preserved and unique receipt independently verified.','bindings':bindings,'layer_matrix':matrix,'independent_denominators':dens,'source_evidence_validation':{'reader_exact_slices':rv,'snapshot_exact_slices':sv,'original_inventory_segments_verified':len(inv),'failures':0,'reader_schema_links_primary_partition':'passed','exact_quotes_do_not_prove_semantics':True},'readonly_prefix_replay':{'matched_exact_snapshot':True,'proposal_count':len(s['proposals']),'used_CURRENT':False,'report':m.report(state,segs)},'claim_mapping':[{'reader_id':x['id'],'reader_canonical_sha256':canon(x),'producer_ids':[mapping[x['id']]],'assessment':'Substance represented; coarser composite or interrogative formulation allowed; specific findings below remain.'} for x in coreclaims],'question_and_answer_comparability':answers,'relation_review':edge_review,'findings':findings,'reader_corrections_and_uncertainties':reader_corrections,'semantic_review':['All 30 source cores and all 56 listed original context segments read. No additional substantive core omission confirmed beyond relation inventory. The 63 reader claims contain summaries, subclaims and objections, not a certified independent atomic denominator.','Water in Rav report and wine in supporting baraita preserved literally. No emendation or normalization. Rav Judah transmits Rav; river restriction remains anonymous.','Rav Pappa uncertainty and Rava certainty are distinct; Abaye\'s recollection settles a version attributed to Rav Yosef without making Rav Pappa retract. RYBN identity follows prior full name, not amora Yohanan.','Both placements of Ulla retained. No-act derivations proceed through objections, replacement and common-feature reasoning; generic asserted labels require attached argument bundle and do not mean final unchallenged proof.','Scriptural prohibition at 4b:11 differs from personal warning at 4b:6. Page-split public-announcement clause is joined. R. Yirmeya is explanatory speaker for Meir.','Payment division and individual lashes remain different conditions; Abaye and Rava offer proof routes to same outcome, not contrary sanctions.','Victim/killer-location contradiction is distinct from witness-location hazama. Rava visibility rule retains both branches. The extraordinary-vision hypothesis is rejected, its rejection accepted.','5b:1–2 attempts to explain R. Yehuda first-set rule end קשיא. Producer scope explicitly records difficulty; bare asserted position must not become settled halacha. 5b:5 proposed alignment of Reish Lakish/Yohanan with tannaim is rejected by distinct circumstances at 5b:6–7. Context carries zero sampled-core credit.'],'producer_active_core_records_by_layer':dict(Counter(x['layer'] for x in active)),'producer_core_record_versions':[{'id':x['id'],'layer':x['layer'],'sha256':canon(x)} for x in active],'relation_assessment_counts':dict(Counter(x['assessment'] for x in edge_review)),'confirmed_substantive_claim_omissions':0,'confirmed_typed_relation_omissions':len(missing),'confirmed_local_status_errors':1,'task_eligibility':{k:False for k in ['retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice','ml']},'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'later_versions_inherit_review':False,'producer_modified':False,'reader_modified':False}
cp=save('makkot_delegated020_exact_version.json',doc)
vp=save('makkot_delegated020_v2_verdict.json',{'artifact_kind':'v2_exact_version_verdict','verdict':'REWORK_TARGETED','actual_comparator_agent_id':doc['actual_comparator_agent_id'],'bindings':bindings,'comparison':cp,'layer_matrix':matrix,'independent_denominators':dens,'required_producer_changes':[x for x in findings if x['category'].startswith('confirmed')],'reader_corrections':reader_corrections,'qualifications':['All substantive core claim units represented; seven missing typed relations and one local-status reversal require additive correction.','Three reader-directed objection explicitness claims require editorial qualification; one inference relation needs refinement.','No full-tractate admission, task eligibility, human certification or later-version inheritance.','Prior comparison has zero core overlap; 30 new coordinates do not requalify historical versions.'],'task_eligibility':doc['task_eligibility'],'tractate_accepted':False,'full_review_receipt':False,'human_certification':False,'later_versions_inherit_review':False,'admission_owner':'global coordinator'})
assert sha(rp)==expected and sha(sp)==sp.stem
ap=save('makkot_delegated020_validation_replay.json',{'artifact_kind':'validation_replay_observations','actual_agent_id':doc['actual_comparator_agent_id'],'comparison':cp,'verdict':vp,'audit_script':bind(Path(__file__)),'checks':doc['source_evidence_validation'],'readonly_prefix_replay':doc['readonly_prefix_replay'],'input_hashes_preserved':True,'independent_denominators':dens,'relation_assessments':doc['relation_assessment_counts'],'prior_overlap':0})
side=Path(__file__).with_name(Path(__file__).name+'.sha256'); content=(sha(__file__)+'  '+Path(__file__).name+'\n').encode()
if side.exists(): assert side.read_bytes()==content
else: side.write_bytes(content)
print(json.dumps({'comparison':cp,'verdict':vp,'observations':ap,'denominators':dens,'relation_counts':doc['relation_assessment_counts'],'evidence':doc['source_evidence_validation']},ensure_ascii=False))
