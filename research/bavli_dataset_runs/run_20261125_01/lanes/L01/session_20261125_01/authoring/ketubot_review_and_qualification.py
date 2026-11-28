"""Explicit source-based corrections after a frozen independent endpoint reading."""
from pathlib import Path
import copy
helpers=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/author_ketubot_opening.py').read_text(encoding='utf-8').split('# Primary ownership')[0]
exec(helpers.replace('kt.open1.','kt.qual1.'))
state=r.current(job); old={x['id']:x for x in state['records'] if x['release_state']=='valid'}
before=r.sha(r.encoded(state))
review=base/'review/l01_session_20261125_ketubot_opening_initial.json'
assert r.sha(review.read_bytes())=='ca6de3979264a3dbd36df3faf231d78a6de7aaae41ffdfcda4d07bd0bce1b59d'
branch='Within the alternative inquiry, assuming the prior branch accepts her misfortune argument for illness; not a finally adopted premise.'
changed={f'kt.open1.c.{k}' for k in ['expected','unexpected_yes','unexpected_no']}
revisions={k:copy.deepcopy(old[k]) for k in changed}
for row in revisions.values(): row['content']['conditions'].append(branch)
# Revise dependent positions/edges and coverage without erasing any prior version.
while True:
    added=[]
    for key,row in old.items():
        deps=row['links']+[row['content'].get(k) for k in ['claim_id','question_id','source_id','target_id']]
        if key not in revisions and any(d in revisions for d in deps if d): added.append(key)
    if not added: break
    for key in added: revisions[key]=copy.deepcopy(old[key])
mapping={k:k+'.condrev1' for k in revisions}
for key,row in revisions.items():
    for field in ['review_state','release_state','ml_eligible']: row.pop(field,None)
    row['id']=mapping[key]; row['supersedes']=key
    row['links']=[mapping.get(k,k) for k in row['links']]
    for field in ['claim_id','question_id','source_id','target_id']:
        if field in row['content']: row['content'][field]=mapping.get(row['content'][field],row['content'][field])
    if row['layer']=='positions': row['content']['conditions'].append(branch)
    records.append(row)
add('s.daily','structure',['3a:12','3a:13','3a:14'],dict(title='Daily courts and completed preparation qualify the Wednesday rule',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('3a:12','Rav Shmuel bar Yitzhak','qualification by court calendar'),('3a:13','anonymous discussion','clarification from historical wording to present daily courts'),('3a:14','anonymous discussion','preparation objection and answer')]:
    add('u.'+ref,'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'))
claim('c.ezra',['3a:12'],'Rav Shmuel bar Yitzhak restricts the stated weekday schedule to the period of Ezra’s enactment fixing courts to Monday and Thursday.',['courts fixed Monday and Thursday'])
claim('c.before',['3a:12'],'In the statement’s initial historical wording, before Ezra’s enactment daily courts allowed marriage any day.',['daily courts'],scope='Historical wording clarified in next segment; no independent historical reconstruction')
claim('c.current',['3a:13'],'The discussion clarifies that where courts now sit daily as before Ezra’s enactment, marriage may occur any day.',['courts currently sit daily'])
claim('c.prepared',['3a:14'],'The any-day case assumes the wedding preparation has already been completed.',['daily courts','already completed preparation'])
question('q.history',['3a:13'],'Why speak of what happened before Ezra rather than a present application?',status='partial')
question('q.preparation',['3a:14'],'Does the requirement of preparation not still apply?',['daily courts'],status='partial')
attr('a.shmuel_bar_yitzhak',[('3a:12','אמר רב שמואל בר יצחק')],'רב שמואל בר יצחק','speaker','weekday qualification; not Shmuel without patronymic')
for k,refs,holder,cond in [('ezra',['3a:12'],'רב שמואל בר יצחק',['post-Ezra fixed court days']),('before',['3a:12'],'רב שמואל בר יצחק',['historical daily courts']),('current',['3a:13'],'anonymous clarification',['current daily courts']),('prepared',['3a:14'],'anonymous answer',['preparation already completed'])]:
    position('p.'+k,refs,holder,'c.'+k,cond,'local qualification')
edge('e.current',['3a:13'],'c.current','q.history','answer')
edge('e.prepared',['3a:14'],'c.prepared','q.preparation','answer')
edge('e.preparation',['3a:14'],'c.prepared','c.current','qualification')
def cross_edge(key,refs,src,target,relation):
    rid=add(key,'edges',refs,dict(source_id=src,target_id=target,relation=relation,explicitness='source_explicit'))
    records[-1]['links']=[src,target]
cross_edge('e.weekday',['3a:12'],'kt.qual1.c.ezra','kt.open1.c.virgin','qualification')
cross_edge('e.sunday_answer',['2a:6'],'kt.open1.c.sunday_final','kt.open1.q.sunday_pay','answer')
cross_edge('e.achai_case',['2b:2','2b:3'],'kt.open1.c.achai_proof','kt.open1.q.case','answer')
cross_edge('e.achai_elimination',['2b:3'],'kt.open1.c.her_delay','kt.open1.c.achai_proof','support')
claim('c.deadline_repeat',['2a:6'],'The deadline Mishnah is quoted again: if the time arrives without marriage, women receive maintenance and eat terumah.',['appointed time arrived','marriage not performed'],scope='Repeated quotation of deadline rule; relevant priestly eligibility presupposed')
position('p.deadline_repeat',['2a:6'],'quoted Mishnah','c.deadline_repeat',['appointed time arrived without marriage'],'repeated textual occurrence; composite entitlements retained')
combined={k:v for k,v in old.items() if k not in revisions}; combined.update({x['id']:x for x in records})
affected={e['segment_id'] for x in records for e in x['evidence']}
coverage=[]
for sid in affected:
    for layer in r.LAYERS:
        ids=[x['id'] for x in combined.values() if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source re-read after frozen independent endpoint reading. Explicit conditional ancestry restored for menstruation alternatives; repeated quotation and three missing argument links retained. 3a:12–14 daily-court and completed-preparation qualifications read in full. '+('Omission reconciliation checked these corrections against original source.' if layer=='reconciliation' else 'All extant valid layer objects in scope listed; no additional independent object found if empty.')))
p=dict(schema_version=r.VERSION,tractate='Ketubot',owner='/root/l01_ketubot',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
r.validate_apply(state,p,rows,j)
out=base/'ketubot_proposals'/'endpoint_correction_and_daily_courts_001.json'; r.immutable(out,r.encoded(p))
comparison=dict(artifact_type='producer_comparison_after_frozen_source_only_reading',review_sha256=r.sha(review.read_bytes()),producer_snapshot_sha256=before,comparer='/root',comparison_independent_of_production=False,scope='15 opening core segments, with continuation qualifications; not full-tractate review',claim_mapping={f'C{i:02d}':v for i,v in enumerate(['c.virgin','c.widow','c.courts','c.complaint','c.deadline','c.deadline','c.initial_derivation+c.sunday_initial','c.direction','c.court_reform','c.feast','c.sunday_final','c.ill_him','c.ill_her','c.niddah','c.him_excuse','c.him_distinguish','c.her_ready','c.her_misfortune','c.expected','c.unexpected_yes','c.unexpected_no','c.achai_proof','c.her_delay','c.ashi_exemption','c.ashi_men','c.ashi_style'],1)},findings=[dict(id='K01',severity='condition_precision',finding='Prior conditional branch absent from three menstruation claim condition arrays, though questions and context preserved it.',action='Explicit conditions added with dependent graph revisions.'),dict(id='K02',severity='occurrence_coverage',finding='Repeated deadline quotation at2a:6 not separately claim-linked.',action='Added repeated composite claim and position; both entitlements were already present in initial quotation.'),dict(id='K03',severity='edge_omission',finding='Missing direct final Sunday answer, Achai case answer, and elimination support links.',action='Added three source-explicit edges.'),dict(id='K04',severity='boundary_disagreement',finding='Reviewer attaches2a:7 to corrected-report block; producer groups it with ensuing accident discussion.',action='Both readings retained; primary character partition exact. Difference is editorial grouping, not omitted text.'),dict(id='K05',severity='continuation_qualification',finding='Opening weekday assertion needs daily-court/preparation continuation for downstream interpretation.',action='Added3a:12–14 and qualification edge; no new task eligibility.'),dict(id='K06',severity='granularity',finding='Reviewer splits maintenance and terumah into separate claims; producer retains explicit composite claim.',action='Both entitlements preserved; record count is not semantic omission count.')],initial_reading_preserved=True,correction_proposal_sha256=r.sha(out.read_bytes()),review_verdict='partial_endpoint_comparison_corrections_require_independent_verification',random_review_completed=False,ml_eligible=False)
r.immutable(base/'review/ketubot_opening_comparison_001.json',r.encoded(comparison))
print(json.dumps(dict(proposal=str(out),sha256=r.sha(out.read_bytes()),records=len(records))))
