"""MG01–MG03 source-based attribution and objection-scope corrections."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('moed_katan','Moed Katan','mk.r019');state=r.current(a.job)
assert r.sha(r.encoded(state))=='a5cb3e7f543f8966e3e26801f2315bbbd11df51a8eaabde399d19498409a6f2f'
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
assumption=a.add('tent_assumption','claims',dict(proposition='The question tests the implication that the marked beit hapras in the current explanation meets the tent-impurity criterion.',conditions=['marked beit hapras under the initial explanation'],scope='Editorially isolated presupposition of5b:10 read with5b:2–3 and5b:9; not a new settled rule about every beit hapras.',assertion_mode='hypothetical'),['5b:2','5b:3','5b:9','5b:10'],['mk.r013.no_tent.c','mk.r013.doubt_kinds.c','mk.r013.plough.c'],['Inference reconstructed from the question and marking criterion; the question challenges this implication, not the fact that ploughing creates a beit hapras.'],origin='editorial_inference')
consequence=a.add('no_marking_consequence','claims',dict(proposition='The distinction is understood to imply that the ploughed-grave field does not require marking under the rule being discussed.',conditions=['ploughed-grave field under Rav Pappa’s distinction'],scope='Editorially isolated consequence challenged at5b:16; not asserted as an unqualified final rule.',assertion_mode='challenged'),['5b:12','5b:16'],['mk.r013.distinguish.c'],['This consequence is expressed as the presupposition of the next question; its scope is inferred, not a separately quoted statement by Rav Pappa.'],origin='editorial_inference')
a.e('ploughed_objection','mk.r013.plough_mark_q.q',consequence,'objection','5b:16')
a.e('consequence_scope',consequence,'mk.r013.distinguish.c','qualification','5b:12')
a.rows[-1]['content']['explicitness']='editorial_reconstruction';a.rows[-1]['origin']='editorial_inference'
targets={'mk.r013.border.u','mk.r013.border.p','mk.r013.field_challenge'}
def deps(row):
    content=row['content'];out=list(row['links'])+[content[k] for k in ['claim_id','question_id','source_id','target_id'] if content.get(k)]
    if row['layer']=='attributions':out.append(content['scope'].split(';')[0].strip())
    return out
while True:
    more={k for k,v in active.items() if any(x in targets for x in deps(v))}-targets
    if not more:break
    targets|=more
mapping={k:k+'.review019' for k in targets}
# Preserve dependency-before-dependent ordering of the existing source records.
pending=set(targets);ordered=[]
while pending:
    ready=sorted(k for k in pending if not (set(deps(active[k]))&pending))
    assert ready,'cyclic dependency requires explicit closure ordering'
    ordered+=ready;pending-=set(ready)
for old in ordered:
    row=copy.deepcopy(active[old]);row.update(id=mapping[old],supersedes=old)
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row['links']=[mapping.get(x,x) for x in row['links']]
    for k in ['claim_id','question_id','source_id','target_id']:
        if k in row['content']:row['content'][k]=mapping.get(row['content'][k],row['content'][k])
    if row['layer']=='attributions':
        scope=row['content']['scope']
        for before,after in mapping.items():
            if scope==before or scope.startswith(before+';'):scope=after+scope[len(before):]
        row['content']['scope']=scope
    if old=='mk.r013.border.u':row['content']['textual_voice']='anonymous application citing Ulla’s explanation'
    if old=='mk.r013.border.p':
        row['content']['holder_candidates']=[]
        row['content']['local_status']='anonymous application of a quoted explanation; not Ulla’s separately transmitted position in this case'
    if old=='mk.r013.border.a':
        row['uncertainty'].append('Quoted-authority role applies only to כדאמר עולא בעומדין על הגבולין; the application הכא נמי is anonymous.')
    if old=='mk.r013.field_challenge':
        row['content']['target_id']=assumption;row['links']=[row['content']['source_id'],assumption]
        row['uncertainty'].append('Target is the editorially isolated tent-impurity/marking implication, not the source’s ploughing terminology claim.')
    a.rows.append(row)
remaining=[x for k,x in active.items() if k not in targets]+a.rows
coverage=[];touched={ev['segment_id'] for row in a.rows for ev in row['evidence']}
for prior in state['coverage']:
    if prior['segment_id'] not in touched and not any(x in targets for x in prior['record_ids']):continue
    item=copy.deepcopy(prior);item.pop('proposal_execution',None)
    item['record_ids']=[x['id'] for x in remaining if x['layer']==item['layer'] and any(ev['segment_id']==item['segment_id'] for ev in x['evidence'])]
    item['extraction_result']='records_found' if item['record_ids'] else 'none_found_after_pass'
    item['rationale']='MG01–MG03 independent review correction after source reread: anonymous application retains Ulla as quoted authority only; objection targets identify the inferred local marking consequences; original quotes and superseded versions preserved.'
    coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/moed_katan_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.rows,coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'graves_review019.json';r.immutable(out,r.encoded(p));print(out)
