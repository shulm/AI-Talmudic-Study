"""Close the independent recheck's inference-origin and coverage-rationale findings."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('moed_katan','Moed Katan','mk.r012');state=r.current(a.job)
assert r.sha(r.encoded(state))=='bfa62bc7c2c8cf5ac8327caac77d9439224a048cca92518fce1e8cccc259f50c'
old='mk.r010.student_example.review011';new=old+'.metadata012'
row=copy.deepcopy(next(x for x in state['records'] if x['id']==old))
row.update(id=new,supersedes=old,origin='editorial_inference')
for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
coverage=[]
for prior in state['coverage']:
    if old not in prior['record_ids'] and not (prior['segment_id']==a.refs['5a:18']['id'] and prior['layer']=='questions'):continue
    item=copy.deepcopy(prior);item.pop('proposal_execution',None)
    item['record_ids']=[new if x==old else x for x in item['record_ids']]
    item['rationale']='Independent repair recheck: preserved supported records; rhetorical doubled-word question is explicitly represented at5a:18. Narrative-to-homily support is editorial inference, with both narrative segments as evidence.'
    coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/moed_katan_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=[row],coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'review_metadata012.json';r.immutable(out,r.encoded(p));print(out)
