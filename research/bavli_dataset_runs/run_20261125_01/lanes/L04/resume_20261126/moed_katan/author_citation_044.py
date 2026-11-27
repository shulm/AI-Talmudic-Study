"""Independent batch005 repair: distinguish Abaye as citing speaker from anonymous teaching holder."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('moed_katan','Moed Katan','mk.r044');state=r.current(a.job)
assert r.sha(r.encoded(state))=='d2998ee775ffbbc66382e5c58bdbf0ccd0c435156e5f1f1fe89f2e829f1e82d5'
ids=['mk.r035.debts.a','mk.r035.debts.p'];mapping={old:old+'.citation044' for old in ids};rows=[]
for old in ids:
 row=copy.deepcopy(next(x for x in state['records'] if x['id']==old and x['release_state']=='valid'))
 row.update(id=mapping[old],supersedes=old)
 if row['layer']=='attributions':row['content']['role']='speaker'
 else:row['content']['holder_candidates']=[]
 row['uncertainty'].append('Abaye is the citing speaker at13a:8; the cited teaching has no named original authority in this passage.')
 for key in ['release_state','review_state','ml_eligible']:row.pop(key,None)
 rows.append(row)
assert not any(set(x['links'])&set(ids) for x in state['records'] if x['release_state']=='valid')
coverage=[]
for prior in state['coverage']:
 if not set(prior['record_ids'])&set(ids):continue
 item=copy.deepcopy(prior);item.pop('proposal_execution',None);item['record_ids']=[mapping.get(x,x) for x in item['record_ids']];item['rationale']='Independent batch005 exclusion repair: retain Abaye as citing speaker and leave original teaching holder unnamed. Exact source spans and claim preserved. Pending exact-version independent recheck.';coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/moed_katan_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'resume_moed_katan_citation044.json';r.immutable(out,r.encoded(p));print(out)
