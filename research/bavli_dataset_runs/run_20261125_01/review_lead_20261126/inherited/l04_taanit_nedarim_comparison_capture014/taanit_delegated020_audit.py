import json, hashlib, sys, importlib.util
from pathlib import Path
from collections import Counter
BASE=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04');OUT=BASE/'review_20261127_delegated020/comparisons';RT=BASE/'bavli_taanit';ROOT=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study');R=ROOT/'research/bavli_dataset_runs/run_20261125_01/review_lead_20261126';CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def read(p):return json.loads(Path(p).read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def canon(x):return hashlib.sha256((json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
rp=BASE/'review_20261127_delegated020/taanit_delegated020.json';assert sha(rp)=='ec23e3c7ccd57938ebc9fbd36847c5237f55282838c0035cb6856e52aabb7712';assert rp.with_suffix('.sha256').read_text().split()[0]==sha(rp);rd=read(rp)
reservation=R/'L04_COMPARISON_RESERVATION_027.json';assert sha(reservation)=='9ce101f41098d1a8393474242849f477ea4e15e6e1f0e3355fb239f025851903'
dp=R/'jobs/bavli_taanit_delegated020.json';d=read(dp);assert sha(dp)==rd['job_sha256']
for b in rd['bindings']:assert sha(b['path'])==b['sha256']
assert read(d['frozen_plan']['path'])['plan_sha256']==d['plan_sha256']==rd['plan_sha256']
sp=RT/'snapshots/59c62a6064a816524290a464e500ca6e82b6b0fe2b540a8f9b385ee533dff776.json';assert sha(sp)==sp.stem;s=read(sp);inv=read(RT/'source_inventory.json');bi={x['id']:x for x in inv};br={x['ref']:x for x in inv};src=read(d['source']['path'])
for x in inv:assert src['text'][x['source_index'][0]][x['source_index'][1]]==x['text']
def slices(obj):
 n=0
 def walk(x):
  nonlocal n
  if isinstance(x,dict):
   if all(k in x for k in ['quote','start_char','end_char']):
    z=br.get(x['segment_id'],bi.get(x['segment_id']));assert z is not None;assert z['text'][x['start_char']:x['end_char']]==x['quote'];n+=1
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(obj);return n
rv=slices(rd);sv=slices(s)
contract=CO/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json';ct=read(contract);runner=CO/'research/bavli_production_v1/runner.py'
for rel in ['research/bavli_production_v1/runner.py','research/bavli_production_v1/schema.json','research/bavli_production_v1/PROTOCOL.md']:assert sha(CO/rel)==ct['production_files'][rel]
sys.dont_write_bytecode=True;sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('exact_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(RT);state=m.empty()
for h in s['proposals']:
 pp=RT/'proposals'/f'{h}.json';assert sha(pp)==h;prev=state['proposals'];state=m.validate_apply(state,read(pp),segs,job);state['proposals']=prev+[h]
assert m.encoded(state)==m.encoded(s)
core=set(rd['core_refs']);rr=rd['independent_review']['records'];ri={x['id']:x for x in rr};pr=[x for x in s['records'] if x['release_state']=='valid'];pi={x['id']:x for x in pr};rc=[x for x in rr if any(e['segment_id'] in core for e in x['evidence'])];pc=[x for x in pr if any(bi[e['segment_id']]['ref'] in core for e in x['evidence'])]
# Manually adjudicated semantic correspondences. Composite matches do not establish atomic/typed completeness.
mp={}
def group(prefix,lines):
 for line in lines.splitlines():
  if not line.strip():continue
  a,b=line.split('=');mp['taanit020.'+a]=[prefix+v for v in b.split('+') if v]
group('ta.resume001.','''ben.report=benbetera.parallel
ben.q=which.benbetera.q
ben.rejected=yehuda.bet.reject.tf013
ben.second=yehuda.bet.reject.tf013
ben.resolve=nahman.identity+ordination.names''')
group('ta.resume002.','''dew.optional=dew.optional
dew.permit=dew.optional
dew.why=dew.reason.q
dew.reason=dew.notwithheld
dew.proofq=dew.proof.q
dew.elijah=elijah.oath
dew.restore=rain.restore
dew.omitq=dew.omission.q
dew.notheld=dew.continuation
dew.oathq=oath.q
dew.bless=blessing.dew
dew.returnq=restore.blessing.q
dew.invisible=blessing.unnoticeable
wind.proofq=wind.proof.q
wind.verse=four.winds.verse
wind.meanq=four.winds.meaning.q
wind.scatter=dispersion.reject.tf013
wind.grammar=dispersion.reject.tf013
wind.analogy=israel.winds.tf013
summer.wind=summer.wind
summer.rain=summer.rain
winter.wind=winter.wind
winter.rain=winter.rain
winter.reverse=negative.wind.dew.tf013
cloud.optional=cloud.optional
cloud.permit=cloud.optional
cloud.why=cloud.reason.q
cloud.reason=cloud.notwithheld
cloud.challenge=withheld.challenge.q
cloud.derash=yosef.clouds
cloud.derashq=yosef.rain.q
cloud.rainonly=yosef.rain.q
cloud.redundancy=rain.already
cloud.contrad=double.contradiction.q
cloud.distinct=cloud.distinguish
wind.distinct=wind.distinguish
wind.threshq=unusual.wind.q
wind.fans=winnow.alternative
after.rank=cloud.rain.rank
after.q=rank.case.q
after.good=after.rain
after.challenge=beneficial.q
after.bad=dust.wind
after.gentle=gentle.strong
after.dust=dust.nodust
rain.wind=wind.asrain
rain.cloud=cloud.asrain
rain.sun=sun.tworains
rain.excludeq=excluded.q
rain.exclude=excluded.weather.tf013
snow.five=snow.five
snow.proof=snow.verse
terrain.snow=snow.mountains
terrain.trees=strong.trees
terrain.fruit=gentle.fruits
mist.seed=mist.seed.tf013
mist.q=arphila.q
mist.word=arphila.wordplay
scholar.seed=scholar.seed
anger.torah=scholar.anger
anger.fire=torah.fire
scholar.iron=scholar.iron
scholar.hammer=hammer.verse
iron.alternate=abba.derivation
anger.gentle=ravina.calm
anger.proof=anger.remove''')
group('ta.resume004.','''famine.1=famine.one
famine.2=famine.two
famine.3=famine.three
famine.4=famine.four
famine.5=famine.five
famine.6=famine.six
famine.7=famine.seven
famine.proof=arms.verse
jerusalem.q=holy.city.q
jerusalem.claim=two.jerusalems
jerusalem.existsq=upper.city.q
jerusalem.exists=joined.city
idolatry.q=one.folly.q
idolatry.burn=idolatry.fire
idolatry.which=
idolatry.ident=idolatry.fire
two.q=two.evils.q
two.start=one.as.two
two.end=one.as.two
two.proof=one.as.two
two.nations=nations.unchanged
nations.fire=fire.water.worship.tf013
nations.water=fire.water.worship.tf013
nations.unchanged=fire.water.worship.tf013
nations.israel=fire.water.worship.tf013
samuel.q=samuel.old.q
samuel.age=samuel.age
samuel.aged=aging.sudden
saul.regret=samuel.prayer
samuel.equal=samuel.prayer
samuel.precedent=samuel.prayer
samuel.plea=samuel.prayer
god.q=divine.dilemma.q
god.saul=dilemma.conditions
god.samuel=dilemma.conditions
god.neither=dilemma.conditions
god.kingdom=dilemma.conditions''')
assert set(mp)=={x['id'] for x in rc if x['layer'] in ['claims','questions']};assert all(p in pi for v in mp.values() for p in v)
print('REPLAY PASS',len(s['proposals']),'slices',rv,sv,'corelayers',Counter(x['layer'] for x in rc))
# Additive adjudication: no source/producer/reader changes.
issues=[]
def issue(i,refs,rids,pids,category,finding,action):
 issues.append({'id':i,'refs':refs.split('|'),'reader_ids':['taanit020.'+v for v in rids.split('|') if v],'producer_ids':pids.split('|') if pids else [],'category':category,'severity':'targeted','finding':finding,'required_action':action,'resolution_state':'OPEN_NOT_APPLIED'})
issue('TA020-P01','Taanit 3b:2','w1','ta.resume002.winds.correction.tf013|ta.resume002.dispersion.reject.tf013','confirmed_typed_relation_error','The correction edge targets the asserted metaclaim that the geographic interpretation is rejected. The final analogy does not correct that valid rejection; it replaces the rejected geographic proposal.','Add a separately scoped rejected proposal and grammatical objection, and retarget correction to the proposal. Preserve original IDs/supersession history.')
issue('TA020-P02','Taanit 5a:13','idolatry.which|idol.e2','ta.resume004.idolatry.fire|ta.resume004.folly.answer','confirmed_question_and_edge_omission','Explicit inner question מאי היא and its answer relation are absent. A single idolatry claim answers the earlier verse question but does not preserve the inner question node.','Add exact inner-question evidence and answer edge; distinguish initial burning dictum, identification, and shared-word proof. Preserve uncertainty whether the anonymous explanation belongs to Yohanan transmission.')
issue('TA020-P03','Taanit 5b:4','saul.regret|samuel.equal|samuel.precedent|samuel.plea|samuel.e2','ta.resume004.samuel.prayer','confirmed_atomic_voice_and_relation_omission','Composite prayer mentions analogy but does not separately assert God equated Samuel with Moses/Aaron or the premise that their handiwork was not annulled. It carries only Samuel holder and no typed analogy; the prefatory divine regret is a different quoted voice.','Add equality and precedent claims with exact verse evidence, distinguish divine regret from Samuel petition and Yohanan/Yitzhak narrative frame, and add premise-to-petition analogy edge. Do not label biblical Samuel as amora Shmuel.')
issue('TA020-P04','Taanit 3a:11','ben.second|ben.e1','ta.resume001.yehuda.bet.reject.tf013|ta.resume001.yehuda.bet.reject.a.tf013','confirmed_attributable_claim_graph_omission','The anonymous rejection metaclaim contains the second-day position in prose, but there is no separately typed second-day position held by R. Yehuda ben Beteira at this occurrence or premise-to-rejected-identification objection.','Represent second-day reported position with correct holder and relation to rejected identity; retain anonymous voice for the rejection itself. Earlier parallel occurrence cannot replace this occurrence.')
issue('TA020-P05','Taanit 3b:2','w3','ta.resume002.four.winds.verse|ta.resume002.israel.winds.tf013|ta.resume002.winds.proof.tf013','confirmed_typed_support_omission','The cited Zechariah verse and resulting wind/Israel exposition are both present, but the typed proof path starts only from the exposition; the verse node has no support edge to that exposition or proof question.','Add the evidenced support link from verse to exposition; retain the interpretive stages and anonymous/inherited-attribution uncertainty.')
reader_corrections=[
 {'id':'TA020-R01','reader_ids':['taanit020.god.saul','taanit020.god.samuel','taanit020.god.neither'],'category':'reader_local_status_error','finding':'The propositions state reasons the three courses cannot be chosen. Those reasons are asserted in the narrative, not rejected. Only the courses themselves are rejected. Correct claim assertion_mode and corresponding positions without rewriting freeze.'},
 {'id':'TA020-R02','reader_ids':[x['id'] for x in rc if x['layer']=='attributions' and any(v.startswith('anonymous') or v.startswith('מר (') for v in x['content']['candidates'])],'category':'reader_identity_typing_error','finding':'anonymous baraita, anonymous scriptural citation and unnamed mar are textual voices, not resolved person candidates. Preserve voice labels but use anonymous/quoted-unknown role and empty named-person candidates. This is not Rav Yosef ownership.'},
 {'id':'TA020-R03','reader_ids':['taanit020.two.start','taanit020.two.e1'],'category':'reader_granularity_qualification','finding':'The incomplete אחת שהיא is a fragment of the 5b:1 proposition, not an additional atomic substantive claim. Keep frozen denominator but do not claim 100% atomic units; producer multi-segment evidence is preferable.'},
 {'id':'TA020-R04','reader_ids':['taanit020.scholar.e'],'category':'reader_relation_scope_error','finding':'Source explicitly compares scholar to seed under clod; it does not explicitly compare scholar proposition to meteorological benefit-of-mist proposition. Reframe the edge as editorial linkage or add a proper seed comparator endpoint. Absence of this exact reader edge is not a confirmed producer omission.'},
 {'id':'TA020-R05','reader_ids':['taanit020.winter.cont'],'category':'reader_relation_explicitness_qualification','finding':'Winter and summer cases continue a single teaching, but this particular cross-claim edge is an editorial segmentation decision, not a separately explicit argument relation.'}]
quals=[
 {'id':'TA020-Q01','refs':['Taanit 3a:12','Taanit 3b:7'],'finding':'Neither before/after ordination name mapping nor early/late cloud source mapping is forced by name order. Both versions retain uncertainty.'},
 {'id':'TA020-Q02','refs':['Taanit 3b:1','Taanit 5a:11','Taanit 5b:4','Taanit 5b:5'],'finding':'Reconstructed Elijah intention, embedded divine speech, Samuel petition and Yohanan exposition are different levels. Reader transmission_chain sometimes mixes these levels; producer split reporter fields are legitimate but do not eliminate need for embedded voice separation in P03.'},
 {'id':'TA020-Q03','refs':['Taanit 3b:9'],'finding':'Ulla or Rabbi Yehuda for ranking; Ulla or Rav Yehuda for curse. Exact printed variants preserved, no silent harmonization.'},
 {'id':'TA020-Q04','refs':['Taanit 4a:1','Taanit 4a:2','Taanit 4a:3','Taanit 5a:10','Taanit 5a:13'],'finding':'Inherited Rava mist attribution and attribution of attached verse proofs/anonymous explanatory clauses remain source-bound inference. Reader assigns some verse proofs to preceding authority while producer leaves them anonymous. Neither categorical assignment is independently certified; 5a:13 needs uncertainty instead of unqualified Yohanan ownership of all explanation.'},
 {'id':'TA020-Q05','refs':['Taanit 3b:5','Taanit 3b:7','Taanit 3b:8'],'finding':'Initial cloud non-withholding assertion is subsequently challenged and distinguished. Generic local asserted status requires linked objection/distinction bundle; do not export as an unqualified enduring belief.'},
 {'id':'TA020-Q06','refs':['Taanit 5b:2','Taanit 5b:5'],'finding':'Same-voice composite inventories can be reasonable granularity for narrative retrieval, but cannot establish atomic argument-node or scholar-choice inventory. Typed internal support at 5b:5 is unavailable because the no-overlap principle and consequence are bundled.'}]
# Explicit decisions for every independently supplied argument edge lacking exact mapped endpoints.
edge_notes={
 'ben.e1':('confirmed_omission','P04: second-day premise and rejected identity need separate endpoints.'),
 'd4':('reasonable_graph_granularity','Producer restoration support -> nonwithholding and nonwithholding answer -> proof question supply an indirect path, not an identical answer edge.'),
 'w1':('confirmed_error','P01: metaclaim endpoint correction error; split rejected proposal from valid rejection.'),
 'w3':('confirmed_omission','P05: verse node needs typed proof linkage.'),
 'winter.cont':('reader_qualification','R05: editorial continuation segmentation.'),
 'cloud.e4':('reasonable_endpoint_granularity','Producer distinction targets the contradictory clouds claim instead of the contradiction question; valid local distinction, no claim of exact endpoint identity.'),
 'cloud.e5':('reasonable_endpoint_granularity','Producer distinction targets the joint clouds/winds claim rather than question; same local reconciliation.'),
 'scholar.e':('reader_error','R04: scholar-to-seed explicit; mist-proposition target is editorial.'),
 'idol.e2':('confirmed_omission','P02: inner-question endpoint absent.'),
 'two.e1':('reasonable_boundary_granularity','Multi-segment producer claim joins incomplete sentence; no separate continuation edge needed.'),
 'two.e3':('composite_internal_relation_not_typed','Water/cistern proof and one-as-two exposition bundled; source content represented, atomic proof graph not qualified.'),
 'nations.e2':('reasonable_graph_granularity','Producer composite fire/water teaching supports nations contrast, which supports one-as-two; two-step support path rather than direct edge.'),
 'samuel.e2':('confirmed_omission','P03: analogy premise and petition bundled with missing distinct equality/precedent assertions.'),
 'god.e':('composite_internal_relation_not_typed','No-overlap principle and consequence bundled; reader rejected label incorrect per R01; internal support not separately represented.')}
edges=[]
for x in rc:
 if x['layer']!='edges':continue
 c=x['content'];matches=[p for p in pr if p['layer']=='edges' and p['content']['source_id'] in mp.get(c['source_id'],[]) and p['content']['target_id'] in mp.get(c['target_id'],[])]
 short=x['id'].removeprefix('taanit020.')
 if not matches:assessment,note=edge_notes[short]
 elif short=='cloud.e3':assessment,note='reasonable_question_vs_rejected_proposal','Producer answers the rain-only question; reader objects to a separately rejected rain-only proposition. Distinct node types and polarity retained.'
 elif short in ['after.e3','after.e4']:assessment,note='reasonable_relation_type','Answer to the contradiction question conveys distinction; alternative reconciliations are not opposing personal positions.'
 else:assessment,note='represented_typed_relation','Same typed local relation and mapped endpoint substance; endpoint granularity qualifications still apply.'
 edges.append({'reader_id':x['id'],'reader_version_sha256':canon(x),'reader_content':c,'evidence':x['evidence'],'producer_ids':[p['id'] for p in matches],'assessment':assessment,'note':note})
# Full frozen inventory crosswalk, including dependent attribution/condition/status fields.
comparisons=[]
for x in rc:
 if x['layer'] not in ['claims','questions']:continue
 ids=mp[x['id']];ra=[a for a in rc if a['layer'] in ['attributions','positions'] and (a['content'].get('scope')==x['id'] or a['content'].get('claim_id')==x['id'])];pa=[a for a in pr if a['layer'] in ['attributions','positions'] and (a['content'].get('scope') in ids or a['content'].get('claim_id') in ids)]
 comparisons.append({'reader_id':x['id'],'layer':x['layer'],'reader_content':x['content'],'evidence':x['evidence'],'reader_version_sha256':canon(x),'producer_ids':ids,'producer_contents':[pi[i]['content'] for i in ids],'reader_attribution_positions':[{'id':a['id'],'content':a['content']} for a in ra],'producer_attribution_positions':[{'id':a['id'],'content':a['content']} for a in pa],'assessment':'missing_explicit_question' if not ids else 'substance_correspondence_with_all_adjudications_applicable','not_atomic_equivalence':True,'applicable_findings':[v['id'] for v in issues if x['id'] in v['reader_ids']]})
condition_rows=[]
for x in rc:
 if x['layer']=='claims' and x['content']['conditions']:
  ids=mp[x['id']];condition_rows.append({'reader_id':x['id'],'reader_conditions':x['content']['conditions'],'producer_ids':ids,'producer_condition_arrays':[pi[i]['content'].get('conditions',[]) for i in ids],'assessment':'explicit_fields_present' if all(pi[i]['content'].get('conditions') for i in ids) else 'condition_or_scope_present_in_prose_but_not_separately_typed','qualification':'Reader conditions include actual antecedents, narrative timing, and embedded-quotation scope; these are not all independent halachic conditions.'})
# All question inventories evaluated for comparability, not promoted by answer edge presence.
answers=[]
for x in rc:
 if x['layer']!='questions':continue
 ids=mp[x['id']];ae=[p for p in pr if p['layer']=='edges' and p['content']['target_id'] in ids and p['content']['relation'] in ['answer','local_resolution','distinction']]
 note='Local explanatory answer inventory; no maintained personal choice contrast or exhaustive alternatives certified.'
 if x['id']=='taanit020.after.challenge':note='Two alternative reconciliations answer the same objection. They can be compared as local explanations but are not assigned to named opposing authorities; not certified mutually exclusive or exhaustive.'
 if x['id']=='taanit020.god.q':note='Rejected courses and final premature-aging resolution in context are successive narrative deliberation, not personal response-choice labels.'
 if x['id']=='taanit020.cloud.contrad':note='Cloud and wind distinctions answer different branches; they are complementary rather than competing answers.'
 answers.append({'reader_question':x['id'],'producer_question_ids':ids,'producer_answer_edge_ids':[a['id'] for a in ae],'comparison_assessment':note,'scholar_choice_eligible':False})
priorpath=R/'comparisons/taanit_batch001_exact_version.json';prior=read(priorpath);priorcore=set(prior['core_refs']);priorcontext=set(prior.get('context_refs_not_in_core_denominator',[]));context=['Taanit 3a:8','Taanit 3a:9','Taanit 3a:10','Taanit 5a:9','Taanit 5b:6','Taanit 5b:7','Taanit 5b:8']
claims=[x for x in rc if x['layer']=='claims'];named=[]
for x in claims:
 aa=[a for a in rc if a['layer']=='attributions' and a['content']['scope']==x['id'] and a['content']['role']!='transmitter'];cands=[v for a in aa for v in a['content']['candidates'] if not v.startswith('anonymous') and not v.startswith('מר (')]
 if cands:named.append(x['id'])
counts={'independently_found_core_claim_records':len(claims),'claim_records_are_not_certified_atomic':True,'attributable_named_or_embedded_authority_claims':len(named),'attributable_claim_ids':named,'condition_bearing_claim_records':len(condition_rows),'core_questions':len(answers),'proposed_local_answer_inventories':len(answers),'standalone_explicit_answer_set_objects_in_reading':0,'core_argument_edges':len(edges),'core_records_by_layer':dict(Counter(x['layer'] for x in rc)),'context_claims_not_in_denominators':len([x for x in rr if x['layer']=='claims' and x not in rc])}
coverage={l:len({bi[x['segment_id']]['ref'] for x in s['coverage'] if x['layer']==l and x['extraction_state']=='completed'}&core) for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']}
bindings={'reading':bind(rp),'reading_sidecar':bind(rp.with_suffix('.sha256')),'reservation':bind(reservation),'neutral_job':bind(dp),'reader_bindings':rd['bindings'],'snapshot':bind(sp),'run_contract':bind(contract),'production_commit':ct['production_git_commit'],'runner':bind(runner),'schema':bind(runner.parent/'schema.json'),'protocol':bind(runner.parent/'PROTOCOL.md'),'audit_script':bind(Path(__file__)),'prior_comparison':bind(priorpath),'accepted_proposals':[bind(RT/'proposals'/f'{h}.json') for h in s['proposals']]}
qa={'original_inventory_segments_verified':len(inv),'whole_reading_exact_spans':rv,'whole_snapshot_exact_spans':sv,'source_span_failures':0,'readonly_prefix_replay_matched':True,'accepted_proposal_count':len(s['proposals']),'CURRENT_read_or_substituted':False,'reader_and_producer_bytes_preserved':sha(rp)==bindings['reading']['sha256'] and sha(sp)==sp.stem,'report':m.report(state,segs),'limitations':'Exact span/replay success validates integrity, not semantics. No export/task-specific admission performed.'}
layer_matrix={'total_source_segments':len(inv),'cohort':'original_probability_sample','core_refs':rd['core_refs'],'core_count':30,'unique_probability_cores_compared':30,'endpoint_cores':0,'risk_cores':0,'prior_core_overlap':len(core&priorcore),'prior_context_overlap':len(core&priorcontext),'prior_context_overlap_refs':sorted(core&priorcontext),'context_refs_reread':context,'context_credit':0,'new_source_only_reading_credit':0,'production_completed_core_segments_by_layer':coverage,'all_30_independent_inventories_compared':True,'full_tractate_admission':False}
doc={'artifact_kind':'exact_version_nonblind_comparison','actual_agent_id':'/root/taanit_compare020','launch_provenance':{'parent':'/root','fresh_context':True,'role':'NONBLIND comparator distinct from producer and source-only reader','model_id':None,'source_only_freeze_verified_before_snapshot_read':True},'bindings':bindings,'layer_matrix':layer_matrix,'independent_denominators':counts,'claim_question_crosswalk':comparisons,'condition_review':condition_rows,'argument_edge_review':edges,'answer_comparability_review':answers,'confirmed_producer_findings':issues,'reader_corrections':reader_corrections,'unresolved_qualifications':quals,'reasonable_granularity':'Optional/voluntary clauses, paired distinctions and same-voice narrative lists may share producer nodes. This does not give typed internal argument credit. Reader two.start fragment not atomic; no count reported as certified exhaustive truth.','reader_original_uncertainties_preserved':rd['uncertainties'],'qa':qa,'producer_core_record_versions':[{'id':x['id'],'layer':x['layer'],'sha256':canon(x)} for x in pc],'per_core_inventory':[{'ref':r,'reader_record_ids':[x['id'] for x in rc if any(e['segment_id']==r for e in x['evidence'])],'producer_record_ids':[x['id'] for x in pc if any(bi[e['segment_id']]['ref']==r for e in x['evidence'])],'source_omission_pass':rd['source_omission_reconciliation'][r.split(' ',1)[1]]} for r in rd['core_refs']],'task_eligibility':{k:False for k in ['ml','retrieval','segmentation','attribution','argument_extraction','qa','scholar_choice']},'human_certification':False,'tractate_accepted':False,'later_versions_inherit_review':False,'production_modified':False}
def write_new(p,obj):
 assert not p.exists();p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8');p.with_suffix(p.suffix+'.sha256').write_text(sha(p)+'  '+p.name+'\n',encoding='utf8')
cp=OUT/'taanit_delegated020_exact_version.json';vp=OUT/'taanit_delegated020_v2_verdict.json';qp=OUT/'taanit_delegated020_validation.json'
write_new(cp,doc);write_new(qp,{'bindings':bindings,'qa':qa});write_new(vp,{'artifact_kind':'v2_exact_version_verdict','verdict':'REWORK_TARGETED','actual_agent_id':doc['actual_agent_id'],'comparison':bind(cp),'bindings':bindings,'layer_matrix':layer_matrix,'denominators':counts,'required_producer_changes':issues,'reader_corrections':reader_corrections,'qualifications':quals,'task_eligibility':doc['task_eligibility'],'human_certification':False,'tractate_accepted':False,'full_review_receipt':False,'later_versions_inherit_review':False,'admission_owner':'global coordinator','limitations':['All 30 cores compared; seven extra source segments reread as context only.','Original probability core overlap with prior comparison is zero; 20 cores previously appeared only as context. No independent fresh-reading credit claimed by comparator.','Atomic completeness and scholar-choice comparability not certified.','No producer edits, eligibility changes, export validation or whole-tractate admission.']})
Path(__file__).with_suffix('.py.sha256').write_text(sha(__file__)+'  '+Path(__file__).name+'\n',encoding='utf8');print(json.dumps({'comparison':bind(cp),'verdict':bind(vp),'validation':bind(qp),'audit':bind(__file__),'counts':counts,'qa':{k:v for k,v in qa.items() if k!='report'}},ensure_ascii=False))
