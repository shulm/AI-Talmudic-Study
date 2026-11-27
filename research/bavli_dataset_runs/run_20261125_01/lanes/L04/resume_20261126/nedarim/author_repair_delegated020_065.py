"""Four adjudicated local repairs only; exact-base additive dependency closure."""
import author_continuation_024 as b
from copy import deepcopy
from pathlib import Path
import hashlib,json
a=b.a;r=a.r;JOB=a.JOB;HERE=Path(__file__).resolve().parent
BASE='5e76010e8585d01a7ede4e1c6924d085ffad622bd6e9bac0ecfd6200861e9b1b'
assert r.read(JOB/'CURRENT.json')['snapshot_sha256']==BASE
assert r.read(JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
reviewdir=JOB.parent/'review_20261127_delegated020/comparisons'
reviewhashes={'nedarim_delegated020_v2_verdict.json':'2ee810abafccf1a47ac6725e6ff22e22752516cf8b9521b4abd16217d46578c5','nedarim_delegated020_additive_adjudication.json':'fa3fadc6be354e12e8e4429534f19cf890fa3a9624da2245d32fdd6c2dd53bb6'}
for name,h in reviewhashes.items():assert sha(reviewdir/name)==h
verdict=r.read(reviewdir/'nedarim_delegated020_v2_verdict.json')
adjudication=r.read(reviewdir/'nedarim_delegated020_additive_adjudication.json')
assert adjudication['operative_required_producer_issue_ids']==['ND020-P01','ND020-P02','ND020-P03','ND020-P05']
contractpath=a.ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
contract=r.read(contractpath);pointer=r.read(a.ROOT/'bavli_dataset_runs/ACTIVE_RUN.json')
assert sha(contractpath)==pointer['contract_sha256']
for name in ['runner.py','schema.json','PROTOCOL.md']:
    path=a.ROOT/'bavli_production_v1'/name
    assert sha(path)==contract['production_files']['research/bavli_production_v1/'+name]
    assert sha(path)==verdict['bindings'][{'runner.py':'runner','schema.json':'schema','PROTOCOL.md':'protocol'}[name]]['sha256']
for binding in verdict['bindings']['common']:
    assert sha(Path(binding['path']))==binding['sha256']
state=r.current(JOB);by={x['id']:x for x in state['records']}
assert r.sha(r.encoded(state))==BASE
assert a.meta['source_sha256']==verdict['bindings']['source']['sha256']
a.records=[];a.notes={};a.PREFIX='nd.fix020.'

# P01: quoted authority continues across the folio, including the a-fortiori.
changed={}
for suffix in ['u','a','c','p']:
    ident='nd.r010.stronger.'+suffix;row=deepcopy(by[ident]);assert row['release_state']=='valid'
    row['evidence']=[a.ev('10a:14','ותניא רבי שמעון אומר'),a.ev('10b:2')]
    changed[ident]=row
changed['nd.r010.stronger.u']['content']['textual_voice']='רבי שמעון (quoted baraita authority)'
changed['nd.r010.stronger.a']['content'].update(surface='רבי שמעון',role='quoted_authority',candidates=['רבי שמעון'])
changed['nd.r010.stronger.c']['content']['scope']='Rabbi Shimon’s uninterrupted quoted baraita, introduced at10a:14, continues through this explicit a-fortiori argument at10b:2; no new anonymous holder inferred.'
changed['nd.r010.stronger.p']['content']['holder_candidates']=['רבי שמעון']

def strings(value):
    if isinstance(value,str):return [value]
    if isinstance(value,list):return [z for x in value for z in strings(x)]
    if isinstance(value,dict):return [z for x in value.values() for z in strings(x)]
    return []
while True:
    extra={ident:deepcopy(row) for ident,row in by.items() if row['release_state']=='valid' and ident not in changed and any(x in changed for x in row['links']+strings(row['content']))}
    if not extra:break
    changed.update(extra)
mapping={ident:ident+'.fix020' for ident in changed}
def remap(value):
    if isinstance(value,str):return mapping.get(value,value)
    if isinstance(value,list):return [remap(x) for x in value]
    if isinstance(value,dict):return {k:remap(v) for k,v in value.items()}
    return value
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row.update(id=mapping[old],supersedes=old)
    row['content']=remap(row['content']);row['links']=remap(row['links']);a.records.append(row)

# P02: source-explicit מניין and its narrowly anchored תלמוד לומר response.
question=b.q('derivation','10b:1',"מניין שלא יאמר אדם לה' עולה לה' מנחה לה' תודה לה' שלמים",'From where is it derived that one should not say the divine name before עולה, מנחה, תודה or שלמים?',voice='רבי שמעון')
answer=a.c('verse','10b:1',"תלמוד לומר קרבן לה'",'The baraita derives the offering-before-divine-name order from קרבן לה׳.',holder='רבי שמעון',extra=[('10a:14','ותניא רבי שמעון אומר')],scope='Rabbi Shimon’s explicit scriptural answer to the preceding מניין; no independent anonymous authority substituted')
for row in a.records:
    if row['id'] in ['nd.fix020.derivation.u','nd.fix020.derivation.a','nd.fix020.derivation.q']:
        row['evidence'].append(a.ev('10a:14','ותניא רבי שמעון אומר'))
    if row['id'] in ['nd.fix020.derivation.a','nd.fix020.verse.a']:row['content']['role']='quoted_authority'
a.edge('verse.answer',answer,question,'answer','10b:1',"תלמוד לומר קרבן לה'")

# P03: corrected form is still a question, not answered by differently spelled Shmuel cases.
amend='nd.r010.amend.q.unc013';assert by[amend]['content']['answer_set_status']=='none'
a.edge('amend.correction',amend,'nd.r010.olist.c','correction','10b:10','אלא שבובאל שבותיאל שקוקאל מהו')
a.records[-1]['uncertainty']=['אלא replaces initial שבואל with שבובאל; שבותיאל and שקוקאל are unchanged. The subsequent מהו remains unresolved; this edge does not identify Shmuel’s differently spelled rulings as its answers.']

# P05: distinct repeated lemma occurrence with its own exact quotation.
lemma=a.c('lemma','10b:11','נדר במוהי הרי אלו כינויין','The discussion repeats the Mishnah lemma that נדר במוהי is among the substitute expressions.',scope='Repeated Mishnah lemma at10b:11, distinct from the earlier10a:11 list; following baraita limits the bare/full expression')
a.edge('lemma.quotation',lemma,'nd.r010.oath.c','quotation','10b:11','נדר במוהי הרי אלו כינויין')
a.edge('bare.qualification','nd.r010.bare.c',lemma,'qualification','10b:11','תניא רבן שמעון בן גמליאל אומר האומר במוהי לא אמר כלום')

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
    row['rationale']+=' Delegated020 adjudicated local repair after pinned-source reread10a11–10b11 and11a1: preserve Shimon continuation, explicit derivation question/answer, unresolved amended-form correction and repeated lemma. Full surviving inventory and supersession dependencies retained.'
    coverage.append(row)
assert len(coverage)==len(affected),'Repairs may touch only existing completed coverage cells.'
p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/nedarim_continuation',model_id=None),records=a.records,coverage=coverage,open_tails=remap(state['open_tails']))
preview=r.validate_apply(state,p,a.ss,a.meta)
sup={x['id'] for x in preview['records'] if x['release_state']=='superseded'}
for row in preview['records']:
    if row['release_state']=='valid':assert not set(row['links']+strings(row['content']))&sup,row['id']
assert r.report(preview,a.ss)['completed_by_layer']==r.report(state,a.ss)['completed_by_layer']
assert next(x for x in preview['records'] if x['id']==amend)==by[amend]
assert all(not x['ml_eligible'] for x in preview['records'])
out=JOB/'staging'/'repair_delegated020_065.json';r.immutable(out,r.encoded(p))
report=dict(status='TARGETED_REPAIR_PREVALIDATED_NOT_INDEPENDENTLY_ACCEPTED',base_snapshot=BASE,source_sha256=a.meta['source_sha256'],review_artifact_hashes=reviewhashes,proposal_path=str(out),proposal_sha256=sha(out),supersession_mapping=mapping,dependent_reference_and_embedded_scope_closure=True,coverage_cells_updated=len(coverage),coverage_count_unchanged=1062,unresolved_amended_question_preserved_exactly=amend,all_ml_eligible_false=True,operative_issue_mapping={'ND020-P01':[mapping['nd.r010.stronger.'+x] for x in ['u','a','c','p']],'ND020-P02':[question,answer,'nd.fix020.verse.answer'],'ND020-P03':['nd.fix020.amend.correction'],'ND020-P05':[lemma,'nd.fix020.lemma.quotation','nd.fix020.bare.qualification']},withdrawn_P04_unchanged=True,next_unprocessed='Nedarim 61b:5',no_new_window_promotion=True)
r.immutable(HERE/'REPAIR_DELEGATED020_065_PREVALIDATION.json',r.encoded(report))
print(json.dumps(report,ensure_ascii=False,indent=2))
