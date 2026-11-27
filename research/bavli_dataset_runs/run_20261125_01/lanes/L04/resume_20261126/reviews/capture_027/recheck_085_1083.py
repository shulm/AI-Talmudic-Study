"""Independent additive exact-version recheck; never reads CURRENT or writes production."""
from pathlib import Path
import re
exec((Path(__file__).parent/'nd085_inspect.py').read_text(encoding='utf8').split("if '--replay'")[0])
from copy import deepcopy
here=Path(__file__).parent
old_artifacts={p.name:sha(p) for p in here.iterdir() if p.is_file() and p.name not in ['recheck_085_1083.py'] and not p.name.startswith('recheck_1083_')}
for p in here.glob('*.sha256'):
 target_file=p.with_name(p.name[:-7])
 assert sha(target_file)==p.read_text().split()[0]
before=target
basehash='65c63fc9a312d505232e0044e5a68129015d8acba73c0b167a0af5eb305f0e8a'
newhash='4b131b8bae8fb66e16c8b3745781812346dd392110e6da2dd345e4178add9712'
ph='912aa35064e1f6a304c42ccf7e6d7619782ac122ecc7c3d880ea8b255c340b9c'
nh='30690a8d7b4bdc610e4d55ba7fd79667e5aae5a17b66323f752de170a03e7cec'
for h in [basehash,newhash]:check(prod/'snapshots'/f'{h}.json',h)
for h in [ph,nh]:check(prod/'proposals'/f'{h}.json',h)
old=s;bs=read(prod/'snapshots'/f'{basehash}.json');ns=read(prod/'snapshots'/f'{newhash}.json');p=read(prod/'proposals'/f'{ph}.json');np=read(prod/'proposals'/f'{nh}.json')
assert ns['proposals']==bs['proposals']+[ph]
assert bs['proposals']==old['proposals']+[nh]
state=r.empty()
for h in ns['proposals']:
 pp=prod/'proposals'/f'{h}.json';check(pp,h);prev=state['proposals'];state=r.validate_apply(state,read(pp),segs,j);state['proposals']=prev+[h]
assert r.encoded(state)==(prod/'snapshots'/f'{newhash}.json').read_bytes()
ob={x['id']:x for x in bs['records']};nb={x['id']:x for x in ns['records']};historical={x['id']:x for x in old['records']};active={k:v for k,v in nb.items() if v['release_state']=='valid'}
mapping={x['supersedes']:x['id'] for x in p['records'] if 'supersedes' in x}
assert len(mapping)==26 and len(p['records'])==64
for ident,row in ob.items():
 expected=deepcopy(row)
 if ident in mapping:expected['release_state']='superseded'
 assert nb[ident]==expected,ident
assert all(ob[k]==v for k,v in historical.items())
assert len(np['records'])==306
assert all(nb[x['id']]==ob[x['id']] and not nb[x['id']]['ml_eligible'] and nb[x['id']]['review_state']=='unreviewed' for x in np['records'])
newcells={(c['segment_id'],c['layer']) for c in np['coverage']}
bc={(c['segment_id'],c['layer']):c for c in bs['coverage']};nc={(c['segment_id'],c['layer']):c for c in ns['coverage']}
assert all(bc[k]==nc[k] for k in newcells)
assert len(newcells)==168
def strings(v):
 if isinstance(v,str):return [v]
 if isinstance(v,list):return [z for vv in v for z in strings(vv)]
 if isinstance(v,dict):return [z for vv in v.values() for z in strings(vv)]
 return []
dependencies=0
for row in active.values():
 for value in row['links']+strings(row['content']):
  for ident in set([value] if value in nb else re.findall(r'nd\.[A-Za-z0-9_.]+',value)):
   if ident in nb:assert ident in active,(row['id'],ident);dependencies+=1
 for key in ['claim_id','question_id','source_id','target_id']:
  ident=row['content'].get(key)
  if ident is not None:assert ident in active
for c in ns['coverage']:assert all(i in active for i in c['record_ids'])
for row in p['records']:
 for e in row['evidence']:assert segs[e['segment_id']]['text'][e['start_char']:e['end_char']]==e['quote']
assert all(not x['ml_eligible'] and x['review_state']=='unreviewed' for x in ns['records'])
assert r.report(bs,segs)['completed_by_layer']==r.report(ns,segs)['completed_by_layer']==dict.fromkeys(r.LAYERS,1083)
lane=wt/'research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/nedarim'
closure=read(lane/'REPAIR_DELEGATED085_067_CLOSURE.json')
assert closure['supersession_mapping']==mapping
comparison=read(here/'comparison_085.json')
restrictions=[x for x in comparison['issues'] if x['id'] in ['R01','R02','U01','U02','G01','G02','G03','G04']]
assert len(restrictions)==8
observations={
 'P01':'Two Meir impurity scopes and Elazar reported agreement now have separate claims, quoted-authority attributions and positions. Original anonymous challenge is separately retained; agreement scope and objection edge preserve the later challenge and spelling uncertainty.',
 'P02':'Yosei remains testimony holder for both objects. Added exact opening evidence and Elazar-to-Yosei chain represent nested proof without conflating original authority.',
 'P03':'Distinct19a12 quoted regional claim now preserves Judea prohibition, Galilee permission and nonrecognition rationale, with Yehuda holder; prior18b6 occurrence and subsequent inferences/replies retained.',
 'P04':'Levi discourse now anchors list utterance, attribution and position, with exact preceding evidence. All ten labels, nine heading and editorial-expansion uncertainty remain; no forced harmonization.',
 'P05':'Explicit Abaye question now has its own question, voice and response links; anonymous firstborn rule is separate and preserves human/animal and pure/impure categories. Revised Abaye act is no longer original authorship of quoted ruling.',
 'P06':'Rav Ashi allocation and Tarfon legal rule are now separate, with Tarfon holder and Rav Ashi/Yehuda/Tarfon chain. Attribution defect repaired; new English neither adds unsupported pair cardinality to אין אחד מהם despite scope disclaiming an unnamed pair.'}
results=[]
for ident,ids in closure['operative_issue_mapping'].items():
 results.append(dict(issue_id=ident,scope='context_only' if ident=='P06' else 'existing_sampled_core',status='ATTRIBUTION_REPAIRED_RESIDUAL_WORDING_DEFECT' if ident=='P06' else 'TARGETED_FIX_VERIFIED',finding=observations[ident],record_ids=ids,records=[active[x] for x in ids]))
residual={'id':'RC01','severity':'low','producer_record_id':'nd.fix085.tarfonrule.c','ref':'Nedarim 19b:7','finding':'English neither entails two persons; the pinned quotation אין אחד מהם does not specify cardinality. Scope says no reconstructed unnamed pair. Use none of them to avoid unsupported information.','evidence':active['nd.fix085.tarfonrule.c']['evidence'],'proposed_action':'New immutable correction replacing neither with none of them; recheck affected dependent IDs, scopes and coverage.','state':'OPEN_NO_PRODUCTION_WRITE','sampled_core_increment':0}
audit=dict(artifact_kind='independent_exact_repair_audit',comparator='/root/nd_compare085',target_snapshot_sha256=newhash,base_snapshot_sha256=basehash,historical_review_target_sha256=before,repair_proposal_sha256=ph,newwindow_proposal_sha256=nh,source_implementation_and_frozen_checks=checks,production_git_commit=contract['production_git_commit'],run_contract_sha256=sha(wt/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'),accepted_prefix_replay='PASS',accepted_proposals=len(ns['proposals']),supersessions_this_repair=26,new_additions_this_repair=38,new_proposal_records=64,total_records=len(ns['records']),active_records=len(active),dependency_checks=dependencies,source_evidence_checks=sum(len(x['evidence']) for x in p['records']),historical_records_preserved=len(historical),previous_records_unchanged_except_release_state=True,newwindow_records_unchanged=306,newwindow_coverage_cells_unchanged=168,newwindow_semantic_review='NOT_PERFORMED_UNREVIEWED',coverage_by_layer=dict.fromkeys(r.LAYERS,1083),results=results,residual_findings=[residual],restrictions_verbatim=restrictions,old_artifacts=old_artifacts,lane_inputs={f:sha(lane/f) for f in ['REPAIR_DELEGATED085_067_CLOSURE.json','REPAIR_DELEGATED085_067_PREVALIDATION.json','author_repair_delegated085_067.py']},helper_sha256=sha(__file__))
def freeze(name,obj):
 path=here/name;raw=(json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode()
 with path.open('xb') as f:f.write(raw)
 with path.with_name(path.name+'.sha256').open('x',encoding='ascii') as f:f.write(sha(path)+'  '+path.name+'\n')
 return {'path':str(path),'sha256':sha(path)}
aa=freeze('recheck_1083_audit.json',audit)
receipt=freeze('recheck_1083_receipt.json',dict(status='REWORK_TARGETED_RESIDUAL_WORDING',audit=aa,exact_target=newhash,producer_findings_rechecked=6,existing_core_findings_repaired=5,context_attribution_repaired=1,context_residual_wording_defects=1,restrictions_preserved_verbatim=True,new_core_credit=0,newwindow_review_credit=0,full_admission=False,task_eligibility_change=False,production_writes=0,historical_verdict_unchanged=True))
with Path(__file__+'.sha256').open('x',encoding='ascii') as f:f.write(sha(__file__)+'  '+Path(__file__).name+'\n')
assert all(sha(here/k)==v for k,v in old_artifacts.items())
print(json.dumps([aa,receipt],ensure_ascii=False))
