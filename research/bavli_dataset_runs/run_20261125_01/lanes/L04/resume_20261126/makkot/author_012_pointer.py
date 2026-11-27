from author_lib import Author,r
import copy
a=Author('r012');state=r.current(a.job);old=next(x for x in state['records'] if x['id']=='ma.r001.seed.a.scope002')
row={k:copy.deepcopy(v) for k,v in old.items() if k not in ['review_state','release_state','ml_eligible']};row['id']='ma.r001.seed.a.scope012';row['supersedes']=old['id'];row['content']['scope']='ma.r001.seed.c.scope002; printed attribution variant unresolved'
cov=[]
for x in state['coverage']:
 if old['id'] in x['record_ids']:
  z={k:copy.deepcopy(v) for k,v in x.items() if k!='proposal_execution'};z['record_ids']=[row['id'] if i==old['id'] else i for i in z['record_ids']];z['rationale']+=' Mechanical embedded scope-ID correction; unchanged scholarly attribution alternatives.';cov.append(z)
p=dict(schema_version=r.VERSION,tractate='Makkot',owner='L04/makkot_resume_20261126',epoch=3,source_sha256=a.j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/makkot_continuation',model_id=None),records=[row],coverage=cov,open_tails=state['open_tails'])
out=a.job/'staging'/'scope_pointer_r012.json';r.immutable(out,r.encoded(p));print(r.submit(a.job,out,p['owner'],3))
