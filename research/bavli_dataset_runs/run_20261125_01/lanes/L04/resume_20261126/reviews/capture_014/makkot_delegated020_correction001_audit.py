import json,hashlib,sys,importlib.util
from pathlib import Path
from collections import Counter
sys.dont_write_bytecode=True
O=Path(__file__).parent
RT=O.parents[1]/'bavli_makkot'
CO=Path('C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study')
LANE=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/makkot')
def read(p):return json.loads(Path(p).read_text(encoding='utf8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def bind(p):return {'path':str(p),'sha256':sha(p)}
def save(n,x):
 p=O/n;data=(json.dumps(x,ensure_ascii=False,indent=2)+'\n').encode()
 if p.exists():assert p.read_bytes()==data
 else:p.write_bytes(data)
 side=p.with_name(p.name+'.sha256');content=(sha(p)+'  '+p.name+'\n').encode()
 if side.exists():assert side.read_bytes()==content
 else:side.write_bytes(content)
 return bind(p)
pins={'makkot_delegated020_exact_version.json':'55c36eca45705eebd0bae433755fb523b014b1b62314f1ebcb8ea218591aafbf','makkot_delegated020_v2_verdict.json':'030c6647347d51b2cecada017587dd0baccaa57f3fcb876ecceed1f0825e3329','makkot_delegated020_context_addendum.json':'9c47fd47a16b9bd1ee3e57131e4b9b302c34eea1efb99ed6934be43456049e98'}
for n,h in pins.items():assert sha(O/n)==h
old=read(O/'makkot_delegated020_exact_version.json');add=read(O/'makkot_delegated020_context_addendum.json')
for b in old['bindings']['source_and_common']:assert sha(b['path'])==b['sha256']
assert sha(old['bindings']['reading']['path'])==old['bindings']['reading']['sha256']
hp='f6522f7c73ad80da50d40fa889f147bedc49e123ffe375c862f6bcc1af2496bc';hs='e333dd7cc2439e0580d6bb28174c5fe73d28f413663b508fdfbdbf2b5d6345fd';hb='83703222712ce4dda8a900326878ea0351e44318321431771ea10deb69e635a1'
pp=RT/'proposals'/f'{hp}.json';sp=RT/'snapshots'/f'{hs}.json';bp=RT/'snapshots'/f'{hb}.json'
for p,h in [(pp,hp),(sp,hs),(bp,hb)]:assert sha(p)==h
p=read(pp);s=read(sp);base=read(bp);im=read(LANE/'CORRECTION_022_ISSUE_MAP.json');assert len(im['issues'])==12 and im['proposal_sha256']==hp
assert s['proposals']==base['proposals']+[hp]
runner=Path(old['bindings']['runner']['path']);assert sha(runner)==old['bindings']['runner']['sha256']
sys.path.insert(0,str(runner.parent));spec=importlib.util.spec_from_file_location('r022_recheck',runner);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
j,segs=m.load(RT);state=m.empty()
for h in s['proposals']:
 path=RT/'proposals'/f'{h}.json';assert sha(path)==h
 previous=state['proposals'];state=m.validate_apply(state,read(path),segs,j);state['proposals']=previous+[h]
assert m.encoded(state)==m.encoded(s)
pr={x['id']:x for x in s['records']};active={i:x for i,x in pr.items() if x['release_state']=='valid'};br={x['id']:x for x in base['records']}
quote_count=0
for x in s['records']:
 for e in x['evidence']:
  assert segs[e['segment_id']]['text'][e['start_char']:e['end_char']]==e['quote'];quote_count+=1
newids={x['id'] for x in p['records']};assert set(pr)-set(br)==newids and len(newids)==20
revs=im['revision_mapping'];assert len(revs)==10
for k,v in revs.items():assert pr[k]['release_state']=='superseded' and active[v]['supersedes']==k
for k,x in br.items():
 if k not in revs:assert x==pr[k]
bc={(x['segment_id'],x['layer']):x for x in base['coverage']};sc={(x['segment_id'],x['layer']):x for x in s['coverage']}
assert set(bc)==set(sc) and all(bc[k]['extraction_state']==sc[k]['extraction_state'] for k in bc)
assert sum(bc[k]!=sc[k] for k in bc)==30
coverage=Counter(x['layer'] for x in s['coverage'] if x['extraction_state']=='completed');assert all(coverage[l]==253 for l in m.LAYERS)
links_checked=0
for x in active.values():
 refs=list(x['links'])
 for k in ['source_id','target_id','claim_id','question_id']:
  if x['content'].get(k):refs.append(x['content'][k])
 if x['layer']=='attributions' and x['content']['scope'] in pr:refs.append(x['content']['scope'])
 for z in refs:assert z in active;links_checked+=1
for row in s['coverage']:
 assert all(z in active for z in row['record_ids'])
 if row['extraction_state']=='completed':
  expected={x['id'] for x in active.values() if (row['layer']=='reconciliation' or row['layer']==x['layer']) and any(e['segment_id']==row['segment_id'] for e in x['evidence'])}
  if row['layer']!='reconciliation':assert expected==set(row['record_ids'])
expected=[('version.qualification','qualification','ma.r007.version.c','ma.r007.ullameir.c'),('akiva.objection','objection','ma.r007.akiva.c','ma.r007.yehuda.c'),('yehuda.support','support','ma.r007.yehuda.c','ma.r007.yehinfer.c'),('rl.correction','correction','ma.r007.rl.c','ma.r007.ulla2.c'),('announce.distinction','distinction','ma.r007.announce.c','ma.r007.yirmeya.c'),('contradiction.qualification','qualification','ma.r008.contradiction.c','ma.r008.self.c'),('hazama.distinction','distinction','ma.r008.hazama.c','ma.r008.contradiction.c'),('options.distinction','distinction','ma.r006.option2.c','ma.r006.option1.c'),('setq.objection','objection','ma.r008.setq.q','ma.r008.yehuda.c'),('rava.correction','correction','ma.r008.rava.c','ma.r008.avahu.c')]
for n,r,a,b in expected:
 x=active['ma.r022.'+n];assert x['content']==dict(explicitness='source_explicit',relation=r,source_id=a,target_id=b)
for stem,q in [('vision','obviousvis'),('camel','obvioustravel')]:
 prefix='ma.r008.'+stem
 assert active[prefix+'.c.review022']['content']['assertion_mode']=='asserted'
 assert active[prefix+'.p.review022']['content']['local_status'].startswith('asserted rejection')
 assert active[prefix+'.p.review022']['content']['claim_id']==prefix+'.c.review022'
 assert active[prefix+'.answer.review022']['content']['source_id']==prefix+'.c.review022'
 assert active[prefix+'.answer.review022']['content']['target_id']=='ma.r008.'+q+'.q'
 assert active[prefix+'.a.review022']['content']['scope']==prefix+'.u.review022'
 assert active[prefix+'.u.review022']['content']['composition']=='composite'
assert active['ma.r008.rava.c']['content']['assertion_mode']=='challenged'
assert active['ma.r008.difficulty.c']['content']['assertion_mode']=='unresolved'
assert active['ma.r008.avahu.c']['content']['assertion_mode']=='rejected'
cross=active['ma.r022.announce.distinction']['evidence'];assert [segs[e['segment_id']]['ref'] for e in cross]==['Makkot 4b:12','Makkot 5a:1']
sources=sorted({e['segment_id'] for x in p['records'] for e in x['evidence']})
doc={'artifact_kind':'bounded_independent_correction001_receipt','verdict':'BOUNDED_PASS','actual_agent_id':'/root/makkot_compare020','comparison_mode':'NONBLIND correction recheck; same independent comparator, not producer','bindings':{'original_review':[bind(O/n) for n in pins],'reading':old['bindings']['reading'],'source_common':old['bindings']['source_and_common'],'baseline':bind(bp),'snapshot':bind(sp),'proposal':bind(pp),'issue_map':bind(LANE/'CORRECTION_022_ISSUE_MAP.json'),'producer_audit':bind(LANE/'CORRECTION_022_AUDIT.json'),'runner':bind(runner),'contract':old['bindings']['run_contract'],'schema':old['bindings']['production_schema'],'protocol':old['bindings']['production_protocol'],'audit_script':bind(Path(__file__))},'checks':{'exact_prefix_replay':True,'proposal_count':len(s['proposals']),'used_CURRENT':False,'exact_snapshot_evidence_slices':quote_count,'active_link_references_checked':links_checked,'completed_segments_each_layer':dict(coverage),'coverage_coordinates_and_states_unchanged':True,'coverage_cells_revised':30,'coverage_record_closure':True,'new_records':20,'added_edges':10,'revision_closure_records':10,'unchanged_nonrevision_base_records':True,'cross_page_evidence':True},'issue_outcomes':[{'issue_id':i['issue_id'],'new_ids':i['new_ids'],'result':'PASS','semantic_assessment':i['adjudication']} for i in im['issues']],'independent_semantic_conclusions':['Ten new edges have the correct typed endpoints and local stages. Premise-to-inference direction at 4b:4 corrects the reader continuation formulation.','Alternative Ulla placement qualifies transmission without deleting either occurrence. Resh Lakish correction replaces single-source proof, not the rule; later combined proof remains.','Proclamation distinction joins the page boundary and distinguishes the sages from the rule explained by Yirmeya for Meir.','Negative hazama illustration and positive witness-location case correctly qualify/distinguish the general requirement.','Rav Pappa alternatives remain questioned. First-set objection is explicit; Rava replaces Abbahu but remains challenged, with unresolved difficulty retained.','Vision and camel propositions now assert the accepted rejection of exceptional-capacity allowances. Position, utterance, attribution scope and answer endpoint closures agree; no denial of physical possibility is inferred.'],'source_evidence_for_changed_records':[{'ref':segs[z]['ref'],'text':segs[z]['text']} for z in sources],'remaining_targeted_issues':[],'reader_qualifications_preserved':im['reader_qualifications_preserved'],'chronology_qualification_preserved':add['chronology_qualification'],'scope_limits':['PASS concerns only 12 enumerated issues: seven core edges plus three context edges and one core plus one context status correction.','The baseline already included additional production beyond the original frozen comparison. Mechanical replay of that prefix is not independent semantic acceptance of those added passages.','Original 30-core comparison remains bound to its old snapshot; no whole-version inheritance or acceptance.','No new source reading, comparison coverage, unique core, endpoint or context core credit. No task eligibility or human certification.','Producer export byte reproduction was not independently rerun in this bounded recheck; producer audit is bound as reported evidence only.'],'new_core_credit':0,'new_reading_credit':0,'full_tractate_admission':False,'whole_snapshot_semantic_acceptance':False,'task_eligibility':old['task_eligibility'],'producer_modified':False,'initial_artifacts_modified':False}
for n,h in pins.items():assert sha(O/n)==h
result=save('makkot_delegated020_correction001_receipt.json',doc)
side=Path(__file__).with_name(Path(__file__).name+'.sha256');content=(sha(__file__)+'  '+Path(__file__).name+'\n').encode()
if side.exists():assert side.read_bytes()==content
else:side.write_bytes(content)
print(json.dumps({'receipt':result,'checks':doc['checks'],'verdict':doc['verdict']}))
