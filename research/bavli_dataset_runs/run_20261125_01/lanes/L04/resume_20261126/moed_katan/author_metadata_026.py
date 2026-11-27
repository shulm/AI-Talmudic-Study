"""Producer metadata audit: match origin to explicitly editorial relation status."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('moed_katan','Moed Katan','mk.r026');state=r.current(a.job)
assert r.sha(r.encoded(state))=='38bdaa5aaabb437a1835001464e949908a7849d3e3bf4bd58aa7cf78f6e36863'
ids=['mk.r022.answers_alternative','mk.r022.oil_alternatives'];mapping={old:old+'.metadata026' for old in ids};rows=[]
for old in ids:
 row=copy.deepcopy(next(x for x in state['records'] if x['id']==old and x['release_state']=='valid'))
 assert row['content']['explicitness']=='editorial_reconstruction'
 row.update(id=mapping[old],supersedes=old,origin='editorial_inference')
 for key in ['release_state','review_state','ml_eligible']:row.pop(key,None)
 rows.append(row)
assert not any(set(x['links'])&set(ids) for x in state['records'] if x['release_state']=='valid')
coverage=[]
for prior in state['coverage']:
 if not set(prior['record_ids'])&set(ids):continue
 item=copy.deepcopy(prior);item.pop('proposal_execution',None);item['record_ids']=[mapping.get(x,x) for x in item['record_ids']];item['rationale']='Producer metadata consistency audit: alternative-explanation relation remains explicitly editorial, with origin corrected to editorial_inference. All source spans and semantic endpoints unchanged. No independent review acceptance claimed.';coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/moed_katan_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'resume_moed_katan_metadata026.json';r.immutable(out,r.encoded(p));print(out)
