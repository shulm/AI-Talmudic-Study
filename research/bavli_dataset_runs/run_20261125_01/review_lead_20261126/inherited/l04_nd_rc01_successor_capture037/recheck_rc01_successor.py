"""Bounded RC01 successor delta recheck; no production writes or CURRENT access."""
from pathlib import Path
from copy import deepcopy
import re
exec((Path(__file__).parent/'nd085_inspect.py').read_text(encoding='utf8').split("if '--replay'")[0])
here=Path(__file__).parent
frozen={p.name:sha(p) for p in here.iterdir() if p.is_file() and p.name!='recheck_rc01_successor.py'}
for side in here.glob('*.sha256'):assert sha(side.with_name(side.name[:-7]))==side.read_text().split()[0]
check(here/'recheck_1083_audit.json','9cd7c55acffe0399b6ff16c4638d96da1efbf90e211f435065a4d450db84375a')
check(here/'recheck_1083_receipt.json','ff3d2f417fcf79cd8a51693b22465d182ee1c60d55ceeeee7c9dd94957a20a60')
bh='4b131b8bae8fb66e16c8b3745781812346dd392110e6da2dd345e4178add9712';nh='b6421aabe6cab3ce7d705b4e1dd71fa6f1dab74a7a6122db508b95ce954e8b74';ph='8f67ae54ce50f51bcec3a7e865f056d1103a77fe4ccfe89b7c1e34301523c212'
for h in [bh,nh]:check(prod/'snapshots'/f'{h}.json',h)
check(prod/'proposals'/f'{ph}.json',ph)
bs=read(prod/'snapshots'/f'{bh}.json');ns=read(prod/'snapshots'/f'{nh}.json');p=read(prod/'proposals'/f'{ph}.json')
assert ns['proposals']==bs['proposals']+[ph] and len(p['records'])==3
preview=r.validate_apply(bs,p,segs,j);preview['proposals']=bs['proposals']+[ph]
assert r.encoded(preview)==(prod/'snapshots'/f'{nh}.json').read_bytes()
ob={x['id']:x for x in bs['records']};nb={x['id']:x for x in ns['records']};mapping={x['supersedes']:x['id'] for x in p['records']}
assert set(mapping)=={'nd.fix085.tarfonrule.c','nd.fix085.tarfonrule.p','nd.fix085.tarfon.support'}
def remap(v):
 if isinstance(v,str):return mapping.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
for new in p['records']:
 expected=deepcopy(ob[new['supersedes']])
 for k in ['release_state','review_state','ml_eligible']:expected.pop(k)
 oldid=expected['id'];expected=remap(expected);expected['supersedes']=oldid
 if expected['layer']=='claims':expected['content']['proposition']=expected['content']['proposition'].replace('neither','none of them')
 assert new==expected,new['id']
for ident,x in ob.items():
 expected=deepcopy(x)
 if ident in mapping:expected['release_state']='superseded'
 assert nb[ident]==expected
def strings(v):
 if isinstance(v,str):return [v]
 if isinstance(v,list):return [z for x in v for z in strings(x)]
 if isinstance(v,dict):return [z for x in v.values() for z in strings(x)]
 return []
active={k:v for k,v in nb.items() if v['release_state']=='valid'};dep=0
for row in active.values():
 for value in row['links']+strings(row['content']):
  for ident in set([value] if value in nb else re.findall(r'nd\.[A-Za-z0-9_.]+',value)):
   if ident in nb:assert ident in active;dep+=1
for c in ns['coverage']:assert all(i in active for i in c['record_ids'])
assert all(not x['ml_eligible'] and x['review_state']=='unreviewed' for x in ns['records'])
np=read(prod/'proposals/30690a8d7b4bdc610e4d55ba7fd79667e5aae5a17b66323f752de170a03e7cec.json')
assert len(np['records'])==306 and all(nb[x['id']]==ob[x['id']] for x in np['records'])
bc={(x['segment_id'],x['layer']):x for x in bs['coverage']};nc={(x['segment_id'],x['layer']):x for x in ns['coverage']}
newcells={(x['segment_id'],x['layer']) for x in np['coverage']};assert len(newcells)==168 and all(bc[k]==nc[k] for k in newcells)
changedcells={k for k in bc if bc[k]!=nc[k]};assert changedcells=={(refs['Nedarim 19b:7']['id'],l) for l in ['claims','positions','edges']}
assert r.report(ns,segs)['completed_by_layer']==dict.fromkeys(r.LAYERS,1083)
source=refs['Nedarim 19b:7'];assert 'אין אחד מהם' in source['text']
result=dict(status='RC01_TARGETED_FIX_VERIFIED',target_snapshot_sha256=nh,base_snapshot_sha256=bh,proposal_sha256=ph,comparator='/root/nd_compare085',scope='RC01 wording only plus necessary lineage/dependency/history checks; Nedarim19b7 context only',source_ref=source['ref'],source_text_sha256=source['text_sha256'],source_evidence=p['records'][0]['evidence'],semantic_finding='none of them preserves unspecified cardinality in אין אחד מהם. Tarfon holder, Yehuda transmission, Rav Ashi allocation, evidence, scope and all other content unchanged.',successor_record_ids=list(mapping.values()),exact_delta_replay='PASS against previously independently full-replayed immutable base4b131b8b; full69-proposal base replay not repeated',accepted_proposal_count=len(ns['proposals']),prior_replay_audit_sha256=sha(here/'recheck_1083_audit.json'),previous_records_preserved=len(ob),active_dependency_checks=dep,coverage_by_layer=dict.fromkeys(r.LAYERS,1083),changed_coverage_cells=3,newwindow_records_unchanged=306,newwindow_cells_unchanged=168,newwindow_review='UNREVIEWED',prior_restrictions_verbatim=read(here/'recheck_1083_audit.json')['restrictions_verbatim'],original_findings_preserved=True,first_residual_receipt_preserved=True,checks=checks,all_prior_artifacts=frozen,helper_sha256=sha(__file__),new_core_credit=0,newwindow_review_credit=0,full_admission=False,task_eligibility_change=False,production_writes=0)
def freeze(name,obj):
 path=here/name
 with path.open('x',encoding='utf8') as f:f.write(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 with path.with_name(path.name+'.sha256').open('x',encoding='ascii') as f:f.write(sha(path)+'  '+path.name+'\n')
 return dict(path=str(path),sha256=sha(path))
a=freeze('recheck_rc01_successor_audit.json',result)
receipt=freeze('recheck_rc01_successor_receipt.json',dict(status='RC01_TARGETED_FIX_VERIFIED',target_snapshot_sha256=nh,audit=a,scope=result['scope'],original_residual_event_unchanged=True,new_core_credit=0,newwindow_review_credit=0,full_admission=False,task_eligibility_change=False,production_writes=0))
with Path(__file__+'.sha256').open('x',encoding='ascii') as f:f.write(sha(__file__)+'  '+Path(__file__).name+'\n')
assert all(sha(here/k)==v for k,v in frozen.items())
print(json.dumps([a,receipt]))
