import sys
sys.dont_write_bytecode=True
from mk047_compare054 import *
import re,copy
NEW='74e823dfebc019ed21e3a5706bd2e8fbbeccb9272268637b1c506e4d7b8acc26';PH='fd2feeb84813a2e22202d2b2b82aa01eb3987921daa8a7e610fbcbac5d8796f4'
np=T/'snapshots'/f'{NEW}.json';pp=T/'proposals'/f'{PH}.json';assert sha(np)==NEW and sha(pp)==PH
new=read(np);p=read(pp);assert new['proposals']==s['proposals']+[PH]
oldi={x['id']:x for x in s['records']};ni={x['id']:x for x in new['records']};sup={x['supersedes']:x['id'] for x in p['records'] if x.get('supersedes')}
assert len(sup)==18 and len(p['records'])==50 and len(p['coverage'])==36
# The old prefix was independently replayed by imported validation helper.
state2=m.validate_apply(copy.deepcopy(state),p,segs,job);state2['proposals']=state['proposals']+[PH]
assert m.encoded(state2)==m.encoded(new)
for ident,old in oldi.items():
 expected=copy.deepcopy(old)
 if ident in sup:expected['release_state']='superseded'
 assert ni[ident]==expected,(ident,'history mutated beyond supersession state')
assert set(ni)-set(oldi)=={x['id'] for x in p['records']}
oldcov={(x['segment_id'],x['layer']):x for x in s['coverage']};newcov={(x['segment_id'],x['layer']):x for x in new['coverage']};changed={(x['segment_id'],x['layer']) for x in p['coverage']}
assert set(oldcov)==set(newcov)
for k,v in oldcov.items():
 if k not in changed:assert newcov[k]==v
assert all(v==512 for v in m.report(new,segs)['completed_by_layer'].values())
def strings(v):
 if isinstance(v,str):yield v
 elif isinstance(v,list):
  for z in v:yield from strings(z)
 elif isinstance(v,dict):
  for z in v.values():yield from strings(z)
all_sup={x['id'] for x in new['records'] if x['release_state']=='superseded'}
patterns={k:re.compile(r'(?<![A-Za-z0-9_.])'+re.escape(k)+r'(?![A-Za-z0-9_.])') for k in all_sup}
active={k:v for k,v in ni.items() if v['release_state']=='valid'}
for x in active.values():
 for value in list(strings(x['content']))+x['links']:
  assert not any(pat.search(value) for pat in patterns.values()),(x['id'],value)
 assert set(x['links'])<=set(active)
 if x['layer']=='edges':assert {x['content']['source_id'],x['content']['target_id']}<=set(active)
 if x['layer']=='positions':assert x['content']['claim_id'] in active and (x['content']['question_id'] is None or x['content']['question_id'] in active)
for k in changed:
 cell=newcov[k];assert set(cell['record_ids'])=={x['id'] for x in active.values() if x['layer']==k[1] and any(e['segment_id']==k[0] for e in x['evidence'])}
spans=evidence(p);newspans=evidence(new)
root=Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/moed_katan')
pre=read(root/'REPAIR_MK054_047_PREVALIDATION.json');assert pre['proposal_sha256']==PH and pre['supersession_mapping']==sup
original=read(O/'mk047_exact_version_comparison054.json')
assert sha(O/'mk047_exact_version_comparison054.json')=='c3f33bf6c8cdf02f343cef43a444aa5b0e7ed718d2936d720e80b03a4e7fd655'
# Compact source reread for bounded correction assessment.
refs=['13b:'+str(i) for i in range(7,14)]+['14a:'+str(i) for i in range(11,18)]+['14b:'+str(i) for i in range(1,8)]+['15a:'+str(i) for i in range(15,18)]+['15b:3','15b:4']
refs=['Moed Katan '+z for z in refs]
checks=dict(exact_corrected_replay=True,base_prefix_count=len(s['proposals']),corrected_prefix_count=len(new['proposals']),proposal_exact_spans=spans,corrected_snapshot_exact_spans=newspans,all_old_records_preserved_except18_release_state_transitions=True,transitive_content_links_positions_edges_closure=True,existing_coverage_cells_revised=len(changed),new_coverage_cells=0,completed_by_layer=m.report(new,segs)['completed_by_layer'],new_records_without_supersession=32,superseding_records=18,current_pointer_read=False)
if __name__=='__main__':
 print(json.dumps(checks))
 for ref in refs:print(ref,br[ref]['text'])
if __name__=='__main__' and '--freeze' in sys.argv:
 def version(x):return dict(id=x['id'],layer=x['layer'],canonical_sha256=hashlib.sha256(m.encoded(x)).hexdigest())
 prior_verdict=O/'mk047_v2_verdict054.json';assert sha(prior_verdict)=='e55a09160f83a74e1b712186f2cd9b211c9a12217006c8e953820716553165b6'
 groups=[
 dict(issue='MK054-001',bounded_status='CORRECTED_AT_EXACT_NEW_VERSION',source_refs=['Moed Katan 14b:3','Moed Katan 14b:7'],assessment='The explicit אמר רב אשי governs דלמא יש מהן אסור ויש מהן מותר in both occurrences. Both reply utterances now name Rav Ashi; attribution speaker and holder match. Hypothetical/composite status remains, with no exhaustive list or final-case allocation. The second occurrence is context only and earns no additional core credit.',direct_ids=['mk.r040.mixed.u.review054','mk.r040.mixed.a.review054','mk.r040.mixed.p.review054'],context_parallel_ids=['mk.r040.mixed2.u.review054','mk.r040.mixed2.a.review054','mk.r040.mixed2.p.review054']),
 dict(issue='MK054-002',bounded_status='CORRECTED_AT_EXACT_NEW_VERSION',source_refs=['Moed Katan 15b:4'],assessment='ושונין לו is now a separate proposition permitting others to teach the person under niddui, with explicit niddui condition and anonymous original authority. The repeated 15b:4 occurrence remains separate from 15a:15. This addition does not assert that study permission is itself the labor proof or settle the separate metzora question.',direct_ids=['mk.r047.teaching.u','mk.r047.teaching.a','mk.r047.teaching.c','mk.r047.teaching.p']),
 dict(issue='MK054-003',bounded_status='SIX_TARGETED_RELATION_PATTERNS_CORRECTED_WITH_RETAINED_RESTRICTIONS',source_refs=['Moed Katan 13b:8','Moed Katan 13b:10','Moed Katan 14a:12','Moed Katan 14a:16','Moed Katan 14a:17','Moed Katan 14b:1'],assessment='Eight typed edges now encode the six reported relation patterns: susceptibility support; changed-grain support expanded to three permitted-product endpoints; two profit analogies; child consequence as objection; converse as its support. Endpoint predicates and evidence are source supported. Child consequence explicitly depends on both birth restriction and challenged converse and stays hypothetical. Rava describes the comparison rather than holding a tannaitic choice. Profit endpoint holder fields remain unassigned, so original MK054-010 named-holder restriction is retained; correcting graph presence does not certify complete scholar attribution.',direct_ids=pre['issue_mapping']['MK054-003'],additional_endpoint_ids=['mk.r047.vow_hilka.c','mk.r047.vow_targis.c','mk.r047.vow_tisni.c','mk.r047.profit_tour.c','mk.r047.profit_food.c','mk.r040.child.c.review054','mk.r040.child.p.review054']),
 dict(issue='MK054-004',bounded_status='CORRECTED_AT_EXACT_NEW_VERSION',source_refs=['Moed Katan 13b:11','Moed Katan 13b:12','Moed Katan 13b:13'],assessment='רב הונא שרא is now anonymous narration of Rav Huna’s permission; attribution is position_holder and the claim/position remain Rav Huna’s reported ruling. The market objection dependency now targets the replacement claim. The fruit/spice qualification remains in its contextual bundle rather than becoming unrestricted public trade.',direct_ids=['mk.r037.market.u.review054','mk.r037.market.a.review054','mk.r037.market.c.review054','mk.r037.market.p.review054'])]
 relation_checks=[]
 for ident in pre['issue_mapping']['MK054-003']:
  x=active[ident];a=active[x['content']['source_id']];b=active[x['content']['target_id']]
  relation_checks.append(dict(edge=x,source_endpoint=a,target_endpoint=b,local_semantics='source-supported typed relation under endpoint scopes/conditions; no new finality or scholar-choice interpretation'))
 changes=[]
 for x in p['records']:
  assigned=[]
  for g in groups:
   if x['id'] in g.get('direct_ids',[])+g.get('context_parallel_ids',[])+g.get('additional_endpoint_ids',[]):assigned.append(g['issue'])
  if not assigned:
   if 'mixed' in x['id']:assigned=['MK054-001 dependency closure']
   elif 'market' in x['id'] or 'only_objection' in x['id']:assigned=['MK054-004 dependency closure']
   elif 'child' in x['id'] or 'tear_objection' in x['id'] or any(z in x['id'] for z in ['vow_hilka','vow_targis','vow_tisni','profit_tour','profit_food']):assigned=['MK054-003 endpoint/dependency closure']
  assert assigned,x['id']
  changes.append(dict(record=active[x['id']],version=version(active[x['id']]),supersedes=x.get('supersedes'),reviewed_for=assigned))
 helper=Path(__file__);hs=Path(str(helper)+'.sha256')
 with hs.open('x') as f:f.write(sha(helper)+'  '+helper.name+'\n')
 bindings=dict(initial_comparison=bind(O/'mk047_exact_version_comparison054.json'),initial_verdict=bind(prior_verdict),initial_reading=bind(rp),prior_snapshot=bind(sp),corrected_snapshot=bind(np),correction_proposal=bind(pp),source=j['source'],common_and_plan=rd['bindings'],runner=bind(runner),run_contract=validation['contract'],production_commit=contract['production_git_commit'],prior_readonly_replay=bind(O/'mk047_validation_replay054.json'),root_author_script=bind(root/'author_review054_047.py'),root_prevalidation=bind(root/'REPAIR_MK054_047_PREVALIDATION.json'),independent_recheck_helper=bind(helper),prior_prefix=prefix)
 audit=dict(artifact_kind='bounded_correction_independent_replay_audit',agent_id='/root/mk_compare054',role='NONBLIND_ORIGINAL_COMPARATOR_CORRECTION_RECHECK',new_fresh_reader=False,bindings=bindings,checks=checks,supersession_mapping=sup,record_changes=changes,typed_relation_endpoint_checks=relation_checks,source_refs_reread=refs,source_evidence=[dict(ref=ref,text_sha256=br[ref]['text_sha256'],source_index=br[ref]['source_index']) for ref in refs],coverage_change_coordinates=[dict(ref=segs[sid]['ref'],layer=layer,old=oldcov[(sid,layer)],new=newcov[(sid,layer)]) for sid,layer in sorted(changed)],new_core_credit=0)
 ap=save('mk047_correction_recheck054_audit.json',audit)
 retained=[f for f in original['findings'] if f['id'] in ['MK054-005','MK054-006','MK054-007','MK054-008','MK054-009','MK054-010']]
 receipt=dict(artifact_kind='additive_bounded_correction_recheck_receipt',status='TARGETED_CORRECTIONS_VERIFIED_WITH_RETAINED_RESTRICTIONS',agent_id='/root/mk_compare054',role='NONBLIND_ORIGINAL_COMPARATOR',bindings=bindings,audit=ap,corrected_issues=groups,retained_original_findings_verbatim=retained,original_verdict_history='REWORK_TARGETED remains the historical verdict on e5f88150. This receipt verifies only the four specified corrections at74e823df; it neither rewrites that verdict nor admits the corrected snapshot wholesale.',checks=checks,original_core_refs=original['compared_core_refs'],original_cohort='original_probability_sample',new_comparison_core_credit=0,new_reading_core_credit=0,context_parallel14b7_extra_credit=0,original_denominators_unchanged=original['denominators'],full_admission=False,task_eligibility_change=False,human_certification=False,current015_unchanged=True,production_mutated_by_rechecker=False,later_versions_inherit_review=False,limitations=['Only specified changed records and transitive dependencies rechecked; unchanged scope does not inherit broader acceptance.','Original reader question omissions007 and status ambiguity008 remain unchanged.','Composite atomicity005, qualifier/attribution uncertainty006, granularity009 and holder/stage010 restrictions remain.','Additional decompositions do not increase independent topic counts.','Schema, evidence, replay and dependency integrity pass; these are not a claim of human scholarly certification.'])
 result=save('mk047_correction_recheck054_receipt.json',receipt)
 for b in [bindings['initial_comparison'],bindings['initial_verdict'],bindings['initial_reading'],bindings['prior_snapshot'],bindings['corrected_snapshot'],bindings['correction_proposal'],bindings['source']]:assert sha(b['path'])==b['sha256']
 print(json.dumps(dict(receipt=result,audit=ap,helper=bind(helper)),ensure_ascii=False))
