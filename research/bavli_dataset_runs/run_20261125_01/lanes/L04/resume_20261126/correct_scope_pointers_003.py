"""Repair exact-ID attribution scopes through preserved revision lineage.

This is a mechanical reference repair, not new source interpretation. Run once
per intended checkpoint; reproduce from the immutable saved proposal instead.
"""
from author_remaining_openings_001 import r, Reading
from copy import deepcopy
import sys

slug = sys.argv[1]
title = {'nedarim':'Nedarim','moed_katan':'Moed Katan','makkot':'Makkot'}[slug]
a = Reading(slug,title,'unused')
state = r.current(a.job)
by = {x['id']:x for x in state['records']}
successors = {x['supersedes']:x['id'] for x in state['records'] if x.get('supersedes')}
def final(id):
    seen=set()
    while id in successors:
        assert id not in seen
        seen.add(id);id=successors[id]
    assert by[id]['release_state']=='valid'
    return id
changed={}
for id,row in by.items():
    if row['release_state']=='valid' and row['layer']=='attributions':
        scope=row['content']['scope']
        if scope in by and by[scope]['release_state']!='valid':
            changed[id]=deepcopy(row)
            changed[id]['content']['scope']=final(scope)
assert changed, 'No stale exact-ID scopes; do not rerun correction authoring.'
def deps(row):
    c=row['content'];out=list(row['links'])
    if row['layer']=='positions':out += [c['claim_id']]+([c['question_id']] if c['question_id'] else [])
    if row['layer']=='edges':out += [c['source_id'],c['target_id']]
    if row['layer']=='attributions' and c['scope'] in by:out.append(c['scope'])
    return out
while True:
    new={id:deepcopy(row) for id,row in by.items() if row['release_state']=='valid' and id not in changed and any(d in changed for d in deps(row))}
    if not new:break
    changed.update(new)
mapping={id:id+'.ptr003' for id in changed}
rows=[]
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row.update(id=mapping[old],supersedes=old)
    row['links']=[mapping.get(x,x) for x in row['links']]
    fields={'positions':['claim_id','question_id'],'edges':['source_id','target_id'],'attributions':['scope']}.get(row['layer'],[])
    for k in fields:row['content'][k]=mapping.get(row['content'][k],row['content'][k])
    rows.append(row)
cov=[]
for old in state['coverage']:
    if any(x in changed for x in old['record_ids']):
        row=deepcopy(old);row.pop('proposal_execution',None)
        row['record_ids']=[mapping.get(x,x) for x in row['record_ids']]
        row['rationale']+=' Exact-ID attribution scope follows preserved supersession lineage; no semantic change.'
        cov.append(row)
p=dict(schema_version=r.VERSION,tractate=title,owner='L04/'+slug+'_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=[mapping.get(x,x) for x in state['open_tails']])
out=a.job/'staging'/'scope_pointer_correction_003.json'
r.immutable(out,r.encoded(p));print(out)
