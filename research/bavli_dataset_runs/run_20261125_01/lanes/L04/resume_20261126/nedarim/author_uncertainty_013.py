"""Version explicit unresolved flags for already-read questions; preserve first records."""
import importlib.util
from pathlib import Path
from copy import deepcopy
ROOT=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('r',ROOT/'bavli_production_v1/runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_nedarim')
meta,source=r.load(JOB);state=r.current(JOB)
assert r.sha(r.encoded(state))=='e7737f912cbe1fe79a87fd5c0ffc4f6c3e58161d6e8218429a9bc03800e991d8','Replay frozen proposal after this revision; do not re-author against a later base.'
by={x['id']:x for x in state['records']}
targets={}
for key in ['kq','pq','pshort','cq','cshort','hq','tq','tshort','oldq']:
    targets['nd.r006.'+key+'.q']='The original source continuation through7a:8 leaves this substantive abbreviated-declaration/designation question unresolved; conditional אם תמצא לומר branches are not final answers.'
for key in ['mif','mit','miz','kin','kin2']:
    targets['nd.r010.'+key+'.q']='The original lexical discussion through10b:11 supplies no settled answer to this queried form; the explicit תיבעי at10b:9 is retained. No unrelated later form is silently substituted.'
targets['nd.r010.amend.q']='No source-explicit equation of these queried spellings with Shmuel’s separately spelled rulings is asserted; the question remains unqualified for an answer task.'
changed={}
for ident,note in targets.items():
    row=deepcopy(by[ident]);assert row['release_state']=='valid'
    for ev in row['evidence']:
        original=source[ev['segment_id']]['text'];assert original[ev['start_char']:ev['end_char']]==ev['quote']
    row['uncertainty']=row['uncertainty']+[note];changed[ident]=row
def deps(row):
    out=list(row['links']);c=row['content']
    if row['layer']=='positions':out += [c['claim_id']]+([c['question_id']] if c['question_id'] else [])
    if row['layer']=='edges':out += [c['source_id'],c['target_id']]
    if row['layer']=='attributions' and c['scope'] in by:out.append(c['scope'])
    return out
while True:
    extra={ident:deepcopy(row) for ident,row in by.items() if row['release_state']=='valid' and ident not in changed and any(d in changed for d in deps(row))}
    if not extra:break
    changed.update(extra)
mapping={ident:ident+'.unc013' for ident in changed};rows=[]
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row.update(id=mapping[old],supersedes=old);row['links']=[mapping.get(x,x) for x in row['links']]
    for field in {'positions':['claim_id','question_id'],'edges':['source_id','target_id'],'attributions':['scope']}.get(row['layer'],[]):
        row['content'][field]=mapping.get(row['content'][field],row['content'][field])
    rows.append(row)
coverage=[]
for old in state['coverage']:
    if any(ident in changed for ident in old['record_ids']):
        row=deepcopy(old);row.pop('proposal_execution',None);row['record_ids']=[mapping.get(x,x) for x in row['record_ids']]
        row['rationale']+=' Explicit unresolved flag added after checking the original continuation; all reference dependencies remapped.';coverage.append(row)
p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/nedarim_continuation',model_id=None),records=rows,coverage=coverage,open_tails=[mapping.get(x,x) for x in state['open_tails']])
out=JOB/'staging'/'uncertainty_013.json';r.immutable(out,r.encoded(p));print(out)
