import json,hashlib,sys,importlib.util
from pathlib import Path
from collections import Counter
OUT=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261127_delegated020/comparisons');RT=OUT.parents[1]/'bavli_taanit';CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
def read(p):return json.loads(Path(p).read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def canonical(x):return hashlib.sha256((json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
cp=OUT/'taanit_delegated020_exact_version.json';vp=OUT/'taanit_delegated020_v2_verdict.json';rp=OUT.parent/'taanit_delegated020.json';old_audit=OUT/'taanit_delegated020_audit.py'
for p,h in [(cp,'a4f9d255edeef833b5d90d30b4ee8a70f4d64b30522963867ce06ba2aff4c758'),(vp,'72f1a1357a9d3ffa5fb0c9b0fd8dbd68d7c321c90b72419fe17171513596d415'),(rp,'ec23e3c7ccd57938ebc9fbd36847c5237f55282838c0035cb6856e52aabb7712'),(old_audit,'2b639a59242dd071febdf5adc184a0cb0b057c71ba6a7d72ddc73bee62fcac08')]:assert sha(p)==h
old=read(cp);rd=read(rp)
for b in rd['bindings']:assert sha(b['path'])==b['sha256']
sp=RT/'snapshots/ac7c9ec619b963f05c6dc32c42e16511808f6256dea63937f5b5f8e5e96e5cf4.json';pp=RT/'proposals/23819ba4040a0057738fb2cf23a5f962a0dacdc74c6dd4af29e48aa5169501d2.json';assert sha(sp)==sp.stem and sha(pp)==pp.stem;s=read(sp);p=read(pp)
ckp=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/taanit/CHECKPOINT_053.json');ck=read(ckp);assert ck['snapshot_sha256']==sp.stem and ck['proposal_sha256']==pp.stem
basepath=RT/'snapshots'/f"{ck['base_snapshot_sha256']}.json";assert sha(basepath)==basepath.stem;base=read(basepath);originalpath=Path(old['bindings']['snapshot']['path']);assert sha(originalpath)==old['bindings']['snapshot']['sha256'];original=read(originalpath)
assert s['proposals']==base['proposals']+[pp.stem];assert base['proposals'][:len(original['proposals'])]==original['proposals']
inv=read(RT/'source_inventory.json');bi={x['id']:x for x in inv};br={x['ref']:x for x in inv};src=read(rd['bindings'][0]['path'])
for x in inv:assert src['text'][x['source_index'][0]][x['source_index'][1]]==x['text']
def spans(obj):
 n=0
 def walk(x):
  nonlocal n
  if isinstance(x,dict):
   if all(k in x for k in ['segment_id','quote','start_char','end_char']):
    z=bi.get(x['segment_id'],br.get(x['segment_id']));assert z['text'][x['start_char']:x['end_char']]==x['quote'];n+=1
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(obj);return n
span_counts={'frozen_reading':spans(rd),'corrective_proposal':spans(p),'corrected_snapshot':spans(s)}
contract=Path(old['bindings']['run_contract']['path']);assert sha(contract)==old['bindings']['run_contract']['sha256'];ct=read(contract);runner=Path(old['bindings']['runner']['path']);assert sha(runner)==old['bindings']['runner']['sha256']
for name in ['schema','protocol']:assert sha(old['bindings'][name]['path'])==old['bindings'][name]['sha256']
sys.dont_write_bytecode=True;sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('correction001_exact_runner',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);job,segs=m.load(RT);state=m.empty()
for h in s['proposals']:
 q=RT/'proposals'/f'{h}.json';assert sha(q)==h;prev=state['proposals'];state=m.validate_apply(state,read(q),segs,job);state['proposals']=prev+[h]
assert m.encoded(state)==m.encoded(s)
active={x['id']:x for x in s['records'] if x['release_state']=='valid'};allrows={x['id']:x for x in s['records']};oldrows={x['id']:x for x in base['records']};newids={x['id'] for x in p['records']};sup={x['supersedes'] for x in p['records'] if x.get('supersedes')}
assert len(newids)==68 and len(sup)==12
for x in p['records']:
 assert x['id'] in active
 if x.get('supersedes'):assert allrows[x['supersedes']]['release_state']=='superseded'
# No unrelated records are silently changed by this corrective proposal.
for i,x in oldrows.items():
 y=allrows[i]
 if i not in sup:assert x==y
 else:
  xx={k:v for k,v in x.items() if k!='release_state'};yy={k:v for k,v in y.items() if k!='release_state'};assert xx==yy
# Check all active dependencies mechanically, semantic closure limited to correction.
links_checked=0; freeform_scopes=[]
for x in active.values():
 deps=list(x['links']);c=x['content']
 if x['layer']=='edges':deps += [c['source_id'],c['target_id']]
 if x['layer']=='positions':deps += [c['claim_id']]+([c['question_id']] if c['question_id'] else [])
 if x['layer']=='attributions':
  if c['scope'] in active:deps += [c['scope']]
  elif c['scope'].split(';',1)[0] in active:
   deps += [c['scope'].split(';',1)[0]];freeform_scopes.append({'id':x['id'],'scope':c['scope'],'recognized_prefix':c['scope'].split(';',1)[0]})
  else:freeform_scopes.append({'id':x['id'],'scope':c['scope'],'recognized_prefix':None})
 for z in deps:assert z in active,(x['id'],z);links_checked+=1
before={(x['segment_id'],x['layer']):x for x in base['coverage']};after={(x['segment_id'],x['layer']):x for x in s['coverage']};assert set(before)==set(after)
changed_cov={k for k in before if before[k]!=after[k]};assert changed_cov=={(x['segment_id'],x['layer']) for x in p['coverage']}
assert Counter(x['layer'] for x in base['coverage'] if x['extraction_state']=='completed')==Counter(x['layer'] for x in s['coverage'] if x['extraction_state']=='completed')
for row in s['coverage']:
 for rid in row['record_ids']:assert rid in active
# Every new semantic row is represented by completed coverage at each evidence coordinate.
for x in p['records']:
 for e in x['evidence']:
  crow=after[(e['segment_id'],x['layer'])];assert crow['extraction_state']=='completed' and x['id'] in crow['record_ids'],(x['id'],e['segment_id'])
def edge(i,a,b,rel):
 x=active[i];assert x['content']=={'source_id':a,'target_id':b,'relation':rel,'explicitness':'source_explicit'}
edge('ta.resume002.winds.correction.tf013.t020053','ta.resume002.israel.winds.tf013','ta.review020.dispersion.proposal','correction')
edge('ta.review020.dispersion.objection','ta.review020.dispersion.grammar','ta.review020.dispersion.proposal','objection')
edge('ta.review020.winds.verse.support','ta.resume002.four.winds.verse','ta.resume002.israel.winds.tf013','support')
edge('ta.review020.idolatry.answer','ta.review020.idolatry.identity','ta.review020.idolatry.identity.q','answer')
edge('ta.review020.idolatry.proof','ta.review020.idolatry.sharedword','ta.review020.idolatry.identity','support')
edge('ta.review020.samuel.analogy','ta.review020.samuel.precedent','ta.resume004.samuel.prayer.t020053','analogy')
edge('ta.review020.samuel.psalm.support','ta.review020.samuel.psalm','ta.review020.samuel.equality','support')
edge('ta.review020.benbetera.objection','ta.review020.benbetera.second','ta.review020.benbetera.identity','objection')
assert active['ta.review020.idolatry.identity.q']['content']['question_origin']=='explicit';assert active['ta.review020.idolatry.identity.a']['uncertainty'];assert active['ta.review020.idolatry.sharedword.a']['uncertainty'];assert active['ta.resume002.israel.winds.a.tf013']['uncertainty']
assert active['ta.review020.benbetera.second.a']['content']['candidates']==['Rabbi Yehuda ben Beteira']
assert active['ta.review020.saul.divine.regret.a']['content']['candidates']==['God in the embedded biblical quotation']
assert active['ta.review020.samuel.precedent.a']['content']['candidates']==['Biblical Samuel in the depicted prayer']
refs=['Taanit 3a:11','Taanit 3b:2','Taanit 5a:13','Taanit 5b:4'];contexts=['Taanit 3a:12','Taanit 5b:3','Taanit 5b:5','Taanit 5b:6']
adjudications=[
 ('TA020-P01',['ta.review020.dispersion.proposal','ta.review020.dispersion.grammar','ta.review020.dispersion.objection','ta.resume002.winds.correction.tf013.t020053'],'CLOSED_TARGETED','Corrected edge targets the hypothetical geographic reading. Grammatical objection is asserted separately; rejected local status resides on proposal position. The accepted rejection metaclaim is no longer mistakenly corrected.'),
 ('TA020-P02',['ta.resume004.idolatry.fire.t020053','ta.review020.idolatry.identity.q','ta.review020.idolatry.identity','ta.review020.idolatry.sharedword','ta.review020.idolatry.answer','ta.review020.idolatry.proof'],'CLOSED_TARGETED','Explicit מאי היא question and its answer/support edges now represented. Narrowed Yohanan dictum retains Yitzhak transmission; unmarked inner explanation preserves anonymous versus inherited attribution uncertainty. No scholar-choice comparability inferred.'),
 ('TA020-P03',['ta.resume004.samuel.prayer.t020053','ta.review020.samuel.equality','ta.review020.samuel.psalm','ta.review020.samuel.precedent','ta.review020.saul.divine.regret','ta.review020.samuel.analogy','ta.review020.samuel.psalm.support'],'CLOSED_TARGETED','Equality, scriptural support, precedent, divine regret and petition separated. Precedent-to-petition analogy is explicit. Embedded God/biblical Samuel voices distinguish original utterance from Yitzhak/Yohanan narrative frames. Petition asserted mode now describes occurrence of petition, not approval of a proposition; no enduring personal ruling follows.'),
 ('TA020-P04',['ta.review020.benbetera.identity','ta.review020.benbetera.second','ta.review020.benbetera.objection','ta.review020.benbetera.rejection.support'],'CLOSED_TARGETED','Second-day view is independently represented at this occurrence with Yehuda ben Beteira holder. Anonymous identity proposal and objection separated; 3a:12 supplies Yehoshua resolution and rejected local status. No arbitrary naming-order assignment.'),
 ('TA020-P05',['ta.review020.winds.verse.support'],'CLOSED_TARGETED','Typed verse-to-exposition support now exists, with inherited-versus-anonymous attribution uncertainty retained unchanged.')]
entries=[]
for i,ids,status,note in adjudications:entries.append({'issue_id':i,'status':status,'independent_assessment':note,'corrected_records':[{'id':rid,'sha256':canonical(active[rid]),'content':active[rid]['content'],'evidence':active[rid]['evidence']} for rid in ids]})
bindings={'source_only_reading':bind(rp),'original_comparison':bind(cp),'original_verdict':bind(vp),'original_audit':bind(old_audit),'original_snapshot':bind(originalpath),'immediate_predecessor_snapshot':bind(basepath),'corrected_snapshot':bind(sp),'corrective_proposal':bind(pp),'producer_checkpoint_mapping':bind(ckp),'reader_bound_documents':rd['bindings'],'run_contract':bind(contract),'runner':bind(runner),'schema':old['bindings']['schema'],'protocol':old['bindings']['protocol'],'audit':bind(__file__),'accepted_proposals':[bind(RT/'proposals'/f'{h}.json') for h in s['proposals']]}
receipt={'artifact_kind':'bounded_nonblind_correction001_recheck','actual_agent_id':'/root/taanit_compare020','model_id':None,'role':'independent NONBLIND original comparator recheck, not producer','verdict':'TARGETED_CORRECTIONS_VERIFIED_WITH_RETAINED_QUALIFICATIONS','release_scope':'Additive NEXT-release evidence only; coordinator release015 remains closed and unchanged.','bindings':bindings,'issue_adjudications':entries,'scope':{'operative_groups_rechecked':5,'affected_original_core_refs':refs,'necessary_context_refs':contexts,'dependency_only_context':'Taanit 5b:6 prayer-support edge retargeted after petition supersession','new_sample_credit':0,'new_source_reading_credit':0,'new_comparison_core_credit':0,'original_denominators_unchanged':old['independent_denominators'],'intervening_proposals_since_original':base['proposals'][len(original['proposals']):],'intervening_work_semantically_reaccepted':False},'validation':{'source_inventory_segments':len(inv),'exact_unicode_spans':span_counts,'replay_exact':True,'replayed_proposal_count':len(s['proposals']),'correction_record_count':len(newids),'new_record_ids_net':len(newids)-len(sup),'superseded_records_preserved':len(sup),'changed_coverage_rows':len(changed_cov),'completed_coverage_by_layer':dict(Counter(x['layer'] for x in s['coverage'] if x['extraction_state']=='completed')),'coverage_inflation':0,'active_dependency_references_checked':links_checked,'freeform_attribution_scopes':freeform_scopes,'audit_preflight_correction':'First audit attempt wrongly treated every free-text attribution scope as a literal record ID; failed on historical opening attribution. Diagnostic saved separately. Final checker validates exact IDs and semicolon-delimited known ID prefixes; reports unparsed scope text, without claiming it is a graph pointer.','dangling_or_superseded_active_dependencies':0,'all_new_records_in_completed_evidence_coverage':True,'non_target_record_content_preserved_against_immediate_predecessor':True,'CURRENT_not_used':True,'source_spans_and_replay_do_not_certify_semantics':True},'reader_corrections_retained':old['reader_corrections'],'all_original_qualifications_retained':old['unresolved_qualifications'],'reader_uncertainties_retained':rd['uncertainties'],'condition_review_retained':old['condition_review'],'remaining_limits':['Only five operative issue groups closed on the pinned correction; this is not acceptance of the whole snapshot or intervening production.','Prior reader polarity, identity-typing, fragment, analogy-target and continuation qualifications remain.','Typed conditions and composite internal argument limitations outside five groups remain; no scholarly accuracy percentage or exhaustive choice inventory certified.','No exports independently replayed; producer export assertion is not adopted.','No future snapshot inherits this receipt.'],'task_eligibility':old['task_eligibility'],'whole_snapshot_accepted':False,'whole_tractate_accepted':False,'human_certification':False,'production_modified':False,'release015_modified':False}
for b in [bindings['source_only_reading'],bindings['original_comparison'],bindings['original_verdict'],bindings['original_audit'],bindings['original_snapshot'],bindings['corrected_snapshot']]:assert sha(b['path'])==b['sha256']
out=OUT/'taanit_delegated020_correction001_receipt.json';assert not out.exists();out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for q in [out,Path(__file__)]:
 side=q.with_suffix(q.suffix+'.sha256');assert not side.exists();side.write_text(sha(q)+'  '+q.name+'\n',encoding='utf8')
print(json.dumps({'receipt':bind(out),'audit':bind(__file__),'validation':receipt['validation']},ensure_ascii=False))
