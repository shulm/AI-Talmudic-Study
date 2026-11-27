"""Six ND085 repairs; source reread18b1–19b11 and20b1–14; no new window."""
import author_continuation_024 as b
from copy import deepcopy
from pathlib import Path
import hashlib,json
a=b.a;r=a.r;JOB=a.JOB;HERE=Path(__file__).resolve().parent
BASE='65c63fc9a312d505232e0044e5a68129015d8acba73c0b167a0af5eb305f0e8a'
assert r.read(JOB/'CURRENT.json')['snapshot_sha256']==BASE
assert r.read(JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
reviewdir=JOB.parent/'review_20261127_delegated081/comparisons'
reviewhashes={'comparison_085.json':'50e17fef783347e9611a165471feb95d92f337633b3718f39aef5123f32408cf','verdict_v2_085.json':'e7f0fea6a0a4945bf141f12b6e41b02121b50af558d0124629b07cb3c45e9a4d'}
for name,h in reviewhashes.items():assert sha(reviewdir/name)==h
contractpath=a.ROOT/'bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json'
contract=r.read(contractpath)
assert sha(contractpath)=='6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174'
for name,h in contract['production_files'].items():assert sha(a.ROOT.parent/name)==h
state=r.current(JOB);by={x['id']:x for x in state['records']}
assert r.sha(r.encoded(state))==BASE
a.records=[];a.notes={};a.PREFIX='nd.fix085.'
changed={}
def edit(ident):
    if ident not in changed:changed[ident]=deepcopy(by[ident]);assert changed[ident]['release_state']=='valid'
    return changed[ident]
def unit(stem,ref,quote):
    for suffix in ['u','a','c','p']:edit(stem+'.'+suffix)['evidence']=[a.ev(ref,quote)]
# P01 retains anonymous challenge act; legal scopes get their own quoted holders below.
unit('nd.r018.liquids','19a:5','אלא אי קשיא הא קשיא')
edit('nd.r018.liquids.c')['content'].update(proposition='The discussion replaces the previous challenge with the following liquid-impurity difficulty.',scope='Anonymous objection introduction; Meir rules and Elazar agreement represented separately.',assertion_mode='challenged')
edit('nd.r018.liquids.u')['content'].update(composition='atomic',discourse_role='challenged')
# P02 explicit nesting, not reassignment of original testimony.
edit('nd.r018.testimony.a')['content'].update(role='quoted_authority',transmission_chain=['רבי אלעזר','יוסי בן יועזר איש צרידה'])
edit('nd.r018.testimony.a')['evidence'].insert(0,a.ev('19a:7','והתניא רבי אלעזר אומר'))
edit('nd.r018.testimony.c')['content']['scope']+='; cited within Rabbi Elazar’s תדע proof; Yosei remains original testimony holder.'
# P04 inherited discourse identity separate from editorial-list uncertainty.
for suffix in ['u','a','c','p']:
    row=edit('nd.r020.labels.'+suffix);row['evidence'].insert(0,a.ev('20b:8','אמר רבי לוי אלו בני תשע מדות'))
    row['uncertainty'].append('List inherits Rabbi Levi’s preceding discourse; whether every expansion is his verbatim wording or editorial explication is not established. Nine heading and ten printed members remain unreconciled.')
edit('nd.r020.labels.a')['content'].update(surface='רבי לוי',role='speaker',candidates=['רבי לוי'])
edit('nd.r020.labels.u')['content']['textual_voice']='רבי לוי'
edit('nd.r020.labels.p')['content']['holder_candidates']=['רבי לוי']
edit('nd.r020.labels.c')['content']['scope']+='; inherited explanation of Rabbi Levi’s immediately preceding heading, with editorial-expansion uncertainty.'
# P05 separate Abaye’s act of challenge from anonymous quoted ruling.
unit('nd.r018.abaye','19a:2','אמר ליה אביי במאי אוקימתא לספק נזירות להקל כרבי אליעזר אימא סיפא')
edit('nd.r018.abaye.c')['content'].update(proposition='Abaye challenges the allocation of lenient doubtful naziriteship to Rabbi Eliezer by directing attention to the source’s concluding firstborn teaching.',scope='Abaye is challenger and citer; he is not assigned original authorship of the anonymous firstborn rule.',assertion_mode='challenged')
edit('nd.r018.abaye.u')['content'].update(composition='atomic',discourse_role='challenged')
# P06 Rav Ashi’s allocation distinguished from underlying Tarfon rule.
unit('nd.r018.tarfon','19b:7','רב אשי אמר ההיא רבי יהודה משום רבי טרפון היא')
edit('nd.r018.tarfon.c')['content'].update(proposition='Rav Ashi allocates the preceding teaching to Rabbi Yehuda reporting in Rabbi Tarfon’s name.',scope='Rav Ashi’s alternative allocation; the cited legal rule and its Tarfon holder are represented separately.')
edit('nd.r018.tarfon.u')['content']['composition']='atomic'
def strings(value):
    if isinstance(value,str):return [value]
    if isinstance(value,list):return [z for x in value for z in strings(x)]
    if isinstance(value,dict):return [z for x in value.values() for z in strings(x)]
    return []
while True:
    extra={ident:deepcopy(row) for ident,row in by.items() if row['release_state']=='valid' and ident not in changed and any(x in changed for x in row['links']+strings(row['content']))}
    if not extra:break
    changed.update(extra)
mapping={ident:ident+'.fix085' for ident in changed}
def remap(value):
    if isinstance(value,str):return mapping.get(value,value)
    if isinstance(value,list):return [remap(x) for x in value]
    if isinstance(value,dict):return {k:remap(v) for k,v in value.items()}
    return value
for old,row in changed.items():
    for k in ['release_state','review_state','ml_eligible']:row.pop(k,None)
    row.update(id=mapping[old],supersedes=old)
    row['content']=remap(row['content']);row['links']=remap(row['links']);a.records.append(row)


def quoted(key,ref,quote,text,holder,**kw):
    ident=a.c(key,ref,quote,text,holder=holder,**kw)
    next(x for x in a.records if x['id']==a.PREFIX+key+'.a')['content']['role']='quoted_authority'
    return ident
selfimp=quoted('selfimp','19a:5','ספק משקין ליטמא טמא','Rabbi Meir rules that doubtful liquids are impure with respect to their own impurity.','רבי מאיר',extra=[('19a:5','דברי רבי מאיר')],conditions=['ספק משקין','ליטמא'],scope='Quoted rule raised as a difficulty, not a final resolution.')
others=quoted('others','19a:5','לטמא אחרים טהור','Rabbi Meir rules that doubtful liquids are pure with respect to imparting impurity to others.','רבי מאיר',extra=[('19a:5','ספק משקין'),('19a:5','דברי רבי מאיר')],conditions=['ספק משקין','לטמא אחרים'],scope='Second scope of quoted distinction; no negation of own impurity inferred.')
agree=quoted('agree','19a:5','וכן היה רבי אלעזר אומר כדבריו','Rabbi Elazar is reported as agreeing with Rabbi Meir’s preceding two-scope liquid rule.','רבי אלעזר',scope='Reported agreement challenged in19a6–9; printed אלעזר is not silently normalized to earlier אליעזר.',uncertainty=['Edition alternates אלעזר/אליעזר; no historical identity resolution.'])
for k,c in [('self',selfimp),('others',others)]:a.edge(k+'.agree',agree,c,'support','19a:5','וכן היה רבי אלעזר אומר כדבריו')
a.edge('liquids.challenge',selfimp,mapping['nd.r018.liquids.c'],'support','19a:5','אלא אי קשיא הא קשיא')
a.edge('elazar.objection','nd.r018.impureq.q',agree,'objection','19a:6')
# P03 distinct repeated occurrence with all alternatives and rationale.
regional=quoted('regional','19a:12','רבי יהודה אומר סתם תרומה ביהודה אסורה ובגליל מותרת שאין אנשי הגליל מכירין את תרומת הלשכה','Rabbi Yehuda’s cited ruling prohibits unspecified terumah in Judea and permits it in Galilee, because Galileans do not recognize the chamber terumah.','רבי יהודה',composition='composite',conditions=['סתם תרומה','Judea: prohibited','Galilee: permitted because chamber terumah is unfamiliar'],scope='Repeated quoted occurrence supporting the objection, distinct from18b6; linked inference and subsequent Rava/Rav Ashi replies retained.')
a.edge('regional.objection',regional,'nd.r018.conflict.q','objection','19a:12','ורמינהי')
a.edge('regional.inference','nd.r018.known.c',regional,'qualification','19a:12','טעמא דאין מכירין')
question=b.q('abayeq','19a:2','במאי אוקימתא לספק נזירות להקל כרבי אליעזר','On what allocation did you establish lenient doubtful naziriteship—as Rabbi Eliezer?',voice='אביי')
rule=a.c('firstborn','19a:2','ספק בכורות אחד בכורי אדם ואחד בכורי בהמה בין טמאה בין טהורה המוציא מחבירו עליו הראייה','For doubtful firstborn status, human or animal, whether an impure or pure animal, the claimant bears the burden of proof.',conditions=['doubtful firstborn','human or animal','animal: impure or pure'],scope='Anonymous cited teaching presented by Abaye; no named original holder supplied.')
a.edge('firstborn.quotation',rule,mapping['nd.r018.abaye.c'],'quotation','19a:2','אימא סיפא')
a.edge('abaye.question',question,'nd.r018.zera.c','objection','19a:2','במאי אוקימתא לספק נזירות להקל כרבי אליעזר')
a.edge('abaye.answer','nd.r018.automatic.q',question,'answer','19a:4')
# The rhetorical distinction is represented as response; partial answer inventory only.
tarfon=quoted('tarfonrule','19b:7','רבי יהודה משום רבי טרפון אומר אין אחד מהם נזיר לפי שלא ניתנה נזירות אלא להפלאה','Rabbi Tarfon’s rule reported by Rabbi Yehuda says neither is a nazirite, because naziriteship was given only for definite specification.','רבי טרפון',scope='Cited baraita; no reconstructed unnamed pair or practical outcome supplied beyond אין אחד מהם.',composition='composite')
next(x for x in a.records if x['id']=='nd.fix085.tarfonrule.a')['content']['transmission_chain']=['רב אשי','רבי יהודה','רבי טרפון']
a.edge('tarfon.support',tarfon,mapping['nd.r018.tarfon.c'],'support','19b:7','דתניא')
a.edge('levi.list',mapping['nd.r020.labels.c'],'nd.r020.nine.c','qualification','20b:9')
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
    row['rationale']+=' ND085 six targeted repairs after original-source reread18b1–19b11 and20b1–14: preserve named holders, nested testimony, repeated regional ruling, inherited Levi scope, explicit Abaye question and separate Tarfon rule. Full surviving inventory and supersession dependencies retained.'
    coverage.append(row)
assert len(coverage)==len(affected),'Repairs may touch only existing completed coverage cells.'
p=dict(schema_version=r.VERSION,tractate='Nedarim',owner='L04/nedarim_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/nedarim_continuation',model_id=None),records=a.records,coverage=coverage,open_tails=remap(state['open_tails']))
preview=r.validate_apply(state,p,a.ss,a.meta)
sup={x['id'] for x in preview['records'] if x['release_state']=='superseded'}
for row in preview['records']:
    if row['release_state']=='valid':assert not set(row['links']+strings(row['content']))&sup,row['id']
assert r.report(preview,a.ss)['completed_by_layer']==r.report(state,a.ss)['completed_by_layer']
assert all(next(x for x in preview['records'] if x['id']==ident)==row for ident,row in by.items() if ident.startswith('nd.r066.'))
assert all(not x['ml_eligible'] for x in preview['records'])
out=JOB/'staging'/'repair_delegated085_067.json';r.immutable(out,r.encoded(p))

report=dict(status='TARGETED_REPAIR_PREVALIDATED_NOT_INDEPENDENTLY_ACCEPTED',base_snapshot=BASE,proposal_path=str(out),proposal_sha256=sha(out),review_artifact_hashes=reviewhashes,supersession_mapping=mapping,coverage_count_unchanged=1083,new21_records_unchanged=True,all_nine_actual_hashes_match=True,all_ml_eligible_false=True,next_unprocessed='Nedarim 62b:5',operative_issue_mapping={'P01':[selfimp,others,agree,mapping['nd.r018.liquids.c']],'P02':[mapping['nd.r018.testimony.a'],mapping['nd.r018.testimony.c']],'P03':[regional],'P04':[mapping['nd.r020.labels.'+s] for s in ['u','a','c','p']],'P05':[question,rule,mapping['nd.r018.abaye.c']],'P06':[tarfon,mapping['nd.r018.tarfon.c']]},preserved_comparison_categories={'reader_errors':2,'reasonable_granularity':4,'unresolved':2},independent_acceptance=False)
r.immutable(HERE/'REPAIR_DELEGATED085_067_PREVALIDATION.json',r.encoded(report))
print(json.dumps(report,ensure_ascii=False,indent=2))
