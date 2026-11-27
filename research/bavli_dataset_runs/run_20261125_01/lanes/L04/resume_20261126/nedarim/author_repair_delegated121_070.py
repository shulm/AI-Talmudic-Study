"""ND121 D1–D4 bounded corrections; no source-window promotion."""
import author_continuation_024 as b
from copy import deepcopy
from pathlib import Path
import hashlib,json
a=b.a;r=a.r;JOB=a.JOB;HERE=Path(__file__).resolve().parent
BASE='5168ca1425eb9ef707abb189482125b347fb49a65fc7e7effcec2309dbf96ce4'
assert r.read(JOB/'CURRENT.json')['snapshot_sha256']==BASE
assert r.read(JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
reviewdir=JOB.parent/'review_20261127_delegated118/comparisons'
reviewhashes={'DELIVERY.json':'b5aace3f2bb293bf3bbba4728dd5061d87729875ed0c3eaa4e7c0a19ce9bfa8e','COMPARISON.md':'c86b8c504c18290725f69ba4b861429a99f22873ea11b6f28c94dd8b71f7f782'}
for name,h in reviewhashes.items():assert sha(reviewdir/name)==h
contractpath=a.ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
contract=r.read(contractpath)
assert sha(contractpath)=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for name,h in contract['production_files'].items():assert sha(a.ROOT.parent/name)==h
state=r.current(JOB);by={x['id']:x for x in state['records']}
assert r.sha(r.encoded(state))==BASE
a.records=[];a.notes={};a.PREFIX='nd.fix121.'
changed={}
def edit(ident):
    if ident not in changed:changed[ident]=deepcopy(by[ident]);assert changed[ident]['release_state']=='valid'
    return changed[ident]
def unit(stem,ref,quote):
    for suffix in ['u','a','c','p']:edit(stem+'.'+suffix)['evidence']=[a.ev(ref,quote)]

# D3 bounded named roles; reporters and original holders remain separate.
edit('nd.r021.report.u')['content']['textual_voice']='רבי אבא בר ממל'
edit('nd.r021.report.a')['content'].update(surface='רבי אבא בר ממל',role='speaker',candidates=['רבי אבא בר ממל'])
edit('nd.r021.report.p')['content'].update(holder_candidates=['רבי יהודה נשיאה'],local_status='Reported attribution of the four-vow teaching to Rabbi Yehuda, transmitted by Rabbi Ami and recalled by Rabbi Abba bar Mamal; distinct from the tanna Rabbi Yehuda.')
edit('nd.r021.tarfon.a')['content'].update(role='quoted_authority',transmission_chain=['רבי יהודה','רבי טרפון'])
edit('nd.r021.tarfon.a')['evidence']=[a.ev('21a:2','רבי יהודה היא דאמר משום רבי טרפון')]+by['nd.r021.tarfon.a']['evidence']
for suffix in ['u','a']:
    edit('nd.r021.invitation.'+suffix)['evidence'].insert(0,a.ev('21a:4','אמר ליה רבינא לרב אשי'))
edit('nd.r021.invitation.u')['content']['textual_voice']='רב אשי'
edit('nd.r021.invitation.a')['content'].update(surface='רב אשי',role='speaker',candidates=['רב אשי'])
edit('nd.r021.invitation.c')['content']['scope']+='; Rav Ashi is the dialogue speaker citing the anonymous teaching, not an identified original author.'
edit('nd.r021.invitation.p')['content']['local_status']='Cited anonymous example; original teaching holder not identified. Rav Ashi is the citing dialogue speaker only.'
for suffix in ['u','a','p']:
    edit('nd.r023.wouldnot.'+suffix)['evidence'].insert(0,a.ev('23a:4','רבי ישמעאל בר רבי יוסי הוה ליה נדרא למישרא'))
edit('nd.r023.wouldnot.u')['content']['textual_voice']='רבי ישמעאל בר רבי יוסי'
edit('nd.r023.wouldnot.a')['content'].update(surface='רבי ישמעאל בר רבי יוסי',role='speaker',candidates=['רבי ישמעאל בר רבי יוסי'])
edit('nd.r023.wouldnot.p')['content']['holder_candidates']=['רבי ישמעאל בר רבי יוסי']
def strings(value):
    if isinstance(value,str):return [value]
    if isinstance(value,list):return [z for x in value for z in strings(x)]
    if isinstance(value,dict):return [z for x in value.values() for z in strings(x)]
    return []
while True:
    extra={ident:deepcopy(row) for ident,row in by.items() if row['release_state']=='valid' and ident not in changed and any(x in changed for x in row['links']+strings(row['content']))}
    if not extra:break
    changed.update(extra)
mapping={ident:ident+'.fix121' for ident in changed}
def remap(value):
    if isinstance(value,str):return mapping.get(value,value)
    if isinstance(value,list):return [remap(x) for x in value]
    if isinstance(value,dict):return {k:remap(v) for k,v in value.items()}
    return value
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row.update(id=mapping[old],supersedes=old)
    row['content']=remap(row['content']);row['links']=remap(row['links']);a.records.append(row)



# Separate reported authority for allocation; existing full Nesia transmission is retained/remapped.
a.add('nesia.authority','attributions',dict(surface='רבי יהודה נשיאה',role='quoted_authority',candidates=['רבי יהודה נשיאה'],scope=mapping['nd.r021.report.c'],transmission_chain=['רבי אבא בר ממל','רבי אמי','רבי יהודה נשיאה']),[a.ev('21a:2','אמר ליה רבי אבא בר ממל לרבי אמי אמרת לן משמיה דרבי יהודה נשיאה')],[mapping['nd.r021.report.c']])
a.add('tarfon.transmitter','attributions',dict(surface='רבי יהודה',role='transmitter',candidates=['רבי יהודה'],scope='nd.r021.tarfon.c',transmission_chain=['רבי יהודה','רבי טרפון']),[a.ev('21a:2','רבי יהודה היא דאמר משום רבי טרפון')],['nd.r021.tarfon.c'])
# D1 repeated questions grouped as an explicitly qualified repeated occurrence.
question=b.q('repeated','23a:4','נדרת אדעתא דהכי','Did you vow with these circumstances in mind?',voice='רבנן',conditions=['Repeated counterfactual questions; particular circumstances are unspecified'])
for row in a.records:
    if row['id'].startswith('nd.fix121.repeated.'):
        row['evidence'] += [a.ev('23a:4','נדרתא אדעתא דהכי'),a.ev('23a:4','אתא לקמייהו דרבנן אמרו ליה'),a.ev('23a:4','כמה זימנין')]
        row['uncertainty'].append('Both printed formulations and repetition retained in one repeated-question unit; unknown specific proposed circumstances not reconstructed.')
a.edge('repeated.answer','nd.r023.questions.c',question,'answer','23a:4','אמרו ליה נדרת אדעתא דהכי אמר להו אין נדרתא אדעתא דהכי אמר להו אין כמה זימנין')
# D2 proposed interpretation, distinct from subsequent private naming and its rejection.
premise=a.c('premise','25a:8','מאי אמר להו משה לישראל לאו הכי קאמר להו דלמא עבידתון מילי ואמריתון על דעתינו משום הכי אמר להו על דעתי','The discussion proposes that Moses said on my intention because Israel might act and then claim to have acted according to their own intention.',mode='hypothetical',scope='Anonymous proposed interpretation of the cited speech, not a new certified historical speech by Moses. Subsequent private-idol-name hypothesis and lexical rebuttal remain distinct.',composition='composite',conditions=['Proposed explanation of Moses’s warning'])
a.edge('premise.qualification',premise,'nd.r025.moses.c','qualification','25a:8','מאי אמר להו משה לישראל לאו הכי קאמר להו דלמא עבידתון מילי ואמריתון על דעתינו משום הכי אמר להו על דעתי')
# D4 core relations; context relations explicitly separated in receipt.
a.edge('invitation.objection','nd.r024.ob.q','nd.r024.m.c','objection','23a:9','וכיוון דאמר כל נדר שאני עתיד לידור יהא בטל לא שמע ליה ולא אתי בהדיה')
a.edge('private.inference.objection','nd.r025.infer.c','nd.r025.common.c','objection','25a:3','ומדקאמר על דעתינו מכלל דעביד אינש דמשתבע אדעתא דנפשיה')
a.edge('moses.objection','nd.r025.mosesq.q','nd.r025.common.c','objection','25a:7','ואכתי לא עביד דמישתבע אדעתא דנפשיה')
a.edge('moses.support','nd.r025.moses.c','nd.r025.mosesq.q','support','25a:7',"והתניא וכן מצינו במשה רבינו כשהשביע את ישראל בערבות מואב אמר להם הוו יודעים שלא על דעתכם אני משביע אתכם אלא על דעתי ועל דעת המקום שנאמר ולא אתכם לבדכם וגו' (דברים כט יג)")
a.edge('context.private.objection','nd.r025.private.q','nd.r025.common.c','objection','25a:2','ועל דעתא דנפשיה לא עביד איניש דמשתבע')
a.edge('context.court.support','nd.r025.court.c','nd.r025.private.q','support','25a:2','והתניא כשהן משביעין אותו אומרים לו הוי יודע שלא על תנאי שבלבך אנו משביעין אותך אלא על דעתינו ועל דעת בית דין')
# Rebuild only affected existing coverage cells from the complete surviving local inventory.
active={x['id']:deepcopy(x) for x in state['records'] if x['release_state']=='valid' and x['id'] not in mapping}
active.update({x['id']:x for x in a.records})
affected={(ev['segment_id'],row['layer']) for row in a.records for ev in row['evidence']}
affected.update((cell['segment_id'],cell['layer']) for cell in state['coverage'] if any(i in mapping for i in cell['record_ids']))
coverage=[]
for cell in state['coverage']:
    if (cell['segment_id'],cell['layer']) not in affected:continue
    row=deepcopy(cell);row.pop('proposal_execution',None)
    row['record_ids']=sorted(x['id'] for x in active.values() if x['layer']==row['layer'] and any(ev['segment_id']==row['segment_id'] for ev in x['evidence']))
    row['extraction_result']='records_found' if row['record_ids'] else 'none_found_after_pass'
    row['rationale']+=' ND121 D1–D4 targeted repairs after original-source reread21a–21b,22b–23b,24b–25a: repeated question, hypothetical interpretive premise, four bounded role groups and specified argument edges; context25a2 remains separately marked. Full surviving inventory and supersession dependencies retained.'
    coverage.append(row)
assert len(coverage)==len(affected),'Repairs may touch only existing completed coverage cells.'
p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/nedarim_continuation',model_id=None),records=a.records,coverage=coverage,open_tails=remap(state['open_tails']))
preview=r.validate_apply(state,p,a.ss,a.meta)
sup={x['id'] for x in preview['records'] if x['release_state']=='superseded'}
for row in preview['records']:
    if row['release_state']=='valid':assert not set(row['links']+strings(row['content']))&sup,row['id']
assert r.report(preview,a.ss)['completed_by_layer']==r.report(state,a.ss)['completed_by_layer']
assert all(next(x for x in preview['records'] if x['id']==ident)==row for ident,row in by.items() if ident.startswith('nd.r069.'))
assert all(not x['ml_eligible'] for x in preview['records'])
out=JOB/'staging'/'repair_delegated121_070.json';r.immutable(out,r.encoded(p))


new_sids={e['segment_id'] for ident,row in by.items() if ident.startswith('nd.r069.') for e in row['evidence']}
assert len([x for x in state['records'] if x['id'].startswith('nd.r069.')])==233
assert [x for x in state['coverage'] if x['segment_id'] in new_sids]==[x for x in preview['coverage'] if x['segment_id'] in new_sids]
# Explicitly preserve all pre-existing question contents and both null interfaces.
for row in preview['records']:
    if row['id'] in by and by[row['id']]['layer']=='questions':assert row==by[row['id']]
for ident in ['nd.r024.abaye.p','nd.r024.rava.p']:assert next(x for x in preview['records'] if x['id']==ident)==by[ident]
report=dict(status='ND121_TARGETED_PREVALIDATED_RECHECK_PENDING',base_snapshot=BASE,proposal_path=str(out),proposal_sha256=sha(out),review_artifact_hashes=reviewhashes,supersession_mapping=mapping,coverage_count_unchanged=1105,new233_records_and176_cells_unchanged=True,all_nine_actual_hashes_match=True,all_ml_eligible_false=True,next_unprocessed='Nedarim 64a:1',operative_issue_mapping={'D1':[question,'nd.fix121.repeated.answer'],'D2':[premise,'nd.fix121.premise.qualification'],'D3':[mapping['nd.r021.report.a'],'nd.fix121.nesia.authority',mapping['nd.r021.tarfon.a'],'nd.fix121.tarfon.transmitter',mapping['nd.r021.invitation.a'],mapping['nd.r023.wouldnot.a']],'D4_core':['nd.fix121.invitation.objection','nd.fix121.private.inference.objection','nd.fix121.moses.objection','nd.fix121.moses.support'],'D4_context25a2':['nd.fix121.context.private.objection','nd.fix121.context.court.support']},U1_all_existing_questions_unchanged=True,U2_null_links_unchanged=True,reader_R1_and_status_uncertainty_granularity_and_comparison_chronology_preserved=True,independent_acceptance=False)
r.immutable(HERE/'REPAIR_DELEGATED121_070_PREVALIDATION.json',r.encoded(report));print(json.dumps(report,ensure_ascii=False,indent=2))
