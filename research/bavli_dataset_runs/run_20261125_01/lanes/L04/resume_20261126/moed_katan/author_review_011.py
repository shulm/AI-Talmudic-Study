"""Adjudicate fresh source-only marking review MM01–MM05."""
import copy,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('moed_katan','Moed Katan','mk.r011');state=r.current(a.job)
assert r.sha(r.encoded(state))=='8fc9976cc33de5e7d5bfec044e42b7d5eb329a0aad1e5d7f2b0209537b88a40e'
active={x['id']:x for x in state['records'] if x['release_state']=='valid'}
qq=a.question('doubling_q','5a:18','מאי וטמא טמא','Why does the verse repeat טמא?')
a.e('doubling_answer','mk.r010.double.c',qq,'answer','5a:18')
a.e('uzziel_agreement','mk.r010.uzziel.c','mk.r010.abahu.c','support','5a:16')
head=a.add('narrative_head','structure',dict(title='Rabbi Yannai and the student: conduct',primary=False,boundary='closed',legacy_ids=[]),['5a:24'],origin='editorial_inference')
tail=a.add('narrative_tail','structure',dict(title='Rabbi Yannai and the student: verse application',primary=False,boundary='closed',legacy_ids=[]),['5b:1'],origin='editorial_inference')
targets=['mk.r010.student_example','mk.r010.praise_narrative','mk.r010.trad_analogy','mk.r010.analogy_q.a','mk.r010.tradition.a','mk.r010.mark_tradition.a']
assert not any(any(t in x['links'] for t in targets) for x in active.values()),'Unexpected dependent link: extend closure before submission'
for old in targets:
    row=copy.deepcopy(active[old]);row.update(id=old+'.review011',supersedes=old)
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    if old.endswith('student_example'):
        row['content']['explicitness']='editorial_reconstruction'
        row['evidence'].append(a.evidence('5b:1'))
        row['uncertainty'].append('Thematic support inferred from juxtaposition and common Psalm application, not an explicit source claim that the narrative proves the named homily.')
    elif old.endswith('praise_narrative'):
        row['content'].update(relation='continuation',source_id=head,target_id=tail)
        row['links']=[head,tail];row['evidence']=[a.evidence('5a:24'),a.evidence('5b:1')]
    elif old.endswith('trad_analogy'):row['content']['relation']='analogy'
    else:
        row['uncertainty'].append('Rav Ashi is a plausible conversational respondent because Ravina addresses him at5a:14, but the reply has no explicit new speaker label. Anonymous attribution preserves that uncertainty; no named transmission is asserted.')
        row['evidence'].append(a.evidence('5a:14'))
    a.rows.append(row)
remaining=[x for k,x in active.items() if k not in targets]+a.rows
coverage=[];touched={e['segment_id'] for x in a.rows for e in x['evidence']}
for old in state['coverage']:
    if old['segment_id'] not in touched and not any(k in targets for k in old['record_ids']):continue
    item=copy.deepcopy(old);item.pop('proposal_execution',None)
    item['record_ids']=[x['id'] for x in remaining if x['layer']==item['layer'] and any(e['segment_id']==item['segment_id'] for e in x['evidence'])]
    item['extraction_result']='records_found' if item['record_ids'] else 'none_found_after_pass'
    item['rationale']+=' Independent marking risk review MM01–MM05: explicit doubled-word question, inferred narrative support, continuation and analogy relations; plausible respondent uncertainty retained.'
    coverage.append(item)
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/moed_katan_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.rows,coverage=coverage,open_tails=state['open_tails'])
out=a.job/'staging'/'review_marking011b.json';r.immutable(out,r.encoded(p));print(out)
