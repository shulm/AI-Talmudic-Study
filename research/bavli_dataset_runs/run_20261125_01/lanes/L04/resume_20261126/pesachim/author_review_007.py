"""PE-QA-001: record the source-present vow answer without inventing alternatives."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r007');state=r.current(a.job)
assert r.sha(r.encoded(state))=='6cd74742059e02cbc7f80f4c373838f1779066975af8eae6e422f988930bc72b'
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
targets={'pe.r001.vow.q','pe.r001.vow.answer'}
while True:
    more={k for k,x in active.items() if any(t in x['links'] for t in targets)}-targets
    if not more:break
    targets|=more
mapping={k:k+'.review007' for k in targets}
rows=[]
for old in sorted(targets,key=lambda k:(k!='pe.r001.vow.q',active[k]['layer']=='attributions',k)):
    row=copy.deepcopy(active[old]);row.update(id=mapping[old],supersedes=old)
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row['links']=[mapping.get(k,k) for k in row['links']]
    if row['layer']=='questions':
        row['content']['answer_set_status']='partial'
        row['uncertainty'].append('The source explicitly supplies the vow consequence. Partial marks source-present answer material without asserting an exhaustive alternative inventory or qualification for answer-set tasks.')
    elif row['layer']=='edges':row['content']['target_id']=mapping['pe.r001.vow.q']
    elif row['layer']=='attributions':
        for before,after in mapping.items():
            row['content']['scope']=row['content']['scope'].replace(before,after)
    rows.append(row)
coverage=[]
for prior in state['coverage']:
    if not any(k in targets for k in prior['record_ids']):continue
    item=copy.deepcopy(prior);item.pop('proposal_execution',None)
    item['record_ids']=[mapping.get(k,k) for k in item['record_ids']]
    item['rationale']='PE-QA-001 independent review correction after rereading2a:8: source-present vow answer recorded as partial answer set, with dependent answer edge revised. No additional alternatives inferred.'
    coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'review007.json';r.immutable(out,r.encoded(p));print(out)
