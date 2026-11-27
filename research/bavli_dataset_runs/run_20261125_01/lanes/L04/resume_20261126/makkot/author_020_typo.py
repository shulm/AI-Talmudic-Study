"""Exact typography correction with dependency, embedded-scope and coverage closure."""
import copy,json
from author_lib_cont2 import Author,r
a=Author('r020');state=r.current(a.job)
assert r.sha(r.encoded(state))=='371c380822ad4a6c3f6cb41af5e696c76d104724bdfbae7cd83816869d3c372e'
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
bad='dialogue counterargument in Rava/Hिसda exchange';good='dialogue counterargument in Rava/Rav Hisda exchange'
affected={rid for rid,x in active.items() if bad in json.dumps(x,ensure_ascii=False)}
assert affected=={'ma.r018.counter.u','ma.r018.counter.a','ma.r018.counter.p'}
while True:
 added={rid for rid,x in active.items() if any(old in json.dumps({'content':x['content'],'links':x['links']},ensure_ascii=False) for old in affected)}-affected
 if not added:break
 affected |= added
mapping={old:old+'.typo020' for old in affected}
def replace(x):
 if isinstance(x,str):
  x=x.replace(bad,good)
  for old,new in sorted(mapping.items(),key=lambda kv:-len(kv[0])):x=x.replace(old,new)
  return x
 if isinstance(x,list):return [replace(v) for v in x]
 if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
 return x
rows=[]
for rid in sorted(affected):
 old=active[rid];new=replace({k:copy.deepcopy(v) for k,v in old.items() if k not in ['review_state','release_state','ml_eligible','supersedes']});new['supersedes']=rid;rows.append(new)
cov=[]
for old in state['coverage']:
 if set(old['record_ids']) & affected:
  new=replace({k:copy.deepcopy(v) for k,v in old.items() if k!='proposal_execution'});new['rationale']+=' Exact typographic speaker-label repair with unchanged evidence and all dependent IDs revised.';cov.append(new)
p=dict(schema_version=r.VERSION,tractate='Makkot',owner='L04/makkot_resume_20261126',epoch=3,source_sha256=a.j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/makkot_continuation_2',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'])
out=a.job/'staging'/'continuation_r020_typo.json';r.immutable(out,r.encoded(p));print(r.submit(a.job,out,p['owner'],3))
