"""Manually authored from pinned original 6a:2–6b:6; not a semantic extractor."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[7]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit')
j,ss=runner.load(JOB)
assert runner.read(JOB/'CURRENT.json')['snapshot_sha256']=='ed262e1b11801771d922c2ae6606f467a8fde3e00c42a9cfe87bb45e10229c17'
assert runner.read(JOB/'OWNER.json')==dict(owner='L04/taanit_resume_20261126',epoch=3)
ix={s['ref'].replace('Taanit ',''):s for s in ss.values()}
P={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
P.update(owner='L04/taanit_resume_20261126',epoch=3,execution=dict(route='interactive_agent',agent_id='/root/taanit_continuation_5',model_id=None),records=[],coverage=[],open_tails=[])
def ev(r,t=None):
 s=ix[r];t=s['text'] if t is None else t;a=s['text'].index(t);return dict(segment_id=s['id'],start_char=a,end_char=a+len(t),quote=t)
def add(k,l,r,c,t=None,links=None,unc=None,origin='source_paraphrase'):
 rid='ta.review020.'+k;P['records'].append(dict(id=rid,layer=l,evidence=[ev(r,t)],content=c,origin=origin,links=links or [],uncertainty=unc or []));return rid
def attr(k,r,target,who,t,chain=None,role=None):
 ch=chain or [];a=add(k+'.a','attributions',r,dict(surface=who or 'anonymous',role=role or ('speaker' if who else 'anonymous'),candidates=[who] if who else [],scope=target,transmission_chain=ch),t,[target])
 for n,person in enumerate(ch[:-1]):add(k+'.tx'+str(n),'attributions',r,dict(surface=person,role='transmitter',candidates=[person],scope=target,transmission_chain=ch),t,[target])
 return a
def c(k,r,t,p,who=None,cond=None,mode='asserted',status=None,chain=None,voice=None,comp='atomic',unc=None):
 cond=cond or [];cid=add(k,'claims',r,dict(proposition=p,conditions=cond,scope='Taanit '+r+' local discussion',assertion_mode=mode),t,unc=unc)
 add(k+'.u','utterances',r,dict(textual_voice=voice or who or 'anonymous discussion',discourse_role=mode,composition=comp),t,[cid],unc)
 attr(k,r,cid,who,t,chain)
 add(k+'.p','positions',r,dict(holder_candidates=[who] if who else [],claim_id=cid,question_id=None,conditions=cond,local_status=status or mode+' locally; no later halakhic adjudication inferred'),t,[cid],unc)
 return cid
def q(k,r,t,p,who=None,voice=None):
 x=add(k,'questions',r,dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'),t)
 add(k+'.u','utterances',r,dict(textual_voice=voice or who or 'anonymous discussion',discourse_role='question',composition='atomic'),t,[x]);attr(k,r,x,who,t);return x
def e(k,r,t,a,b,rel='support'):
 return add(k,'edges',r,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),t,[a,b])

import copy,re
S=runner.current(JOB);BASE=runner.read(JOB/'CURRENT.json')['snapshot_sha256']
active={r['id']:r for r in S['records'] if r['release_state']=='valid'}
changed={}
def edit(rid):
 if rid not in changed:changed[rid]={k:copy.deepcopy(v) for k,v in active[rid].items() if k not in ['review_state','release_state','ml_eligible']}
 return changed[rid]
def narrow(base,ref,t,proposition,voice=None):
 for rid in [base,base+'.a',base+'.p',base+'.u']:
  r=edit(rid);r['evidence']=[ev(ref,t)];r['uncertainty'].append('Delegated020 targeted decomposition; earlier composite preserved as superseded. No independent acceptance inherited.')
 edit(base)['content']['proposition']=proposition
 if voice:
  edit(base+'.a')['content'].update(surface=voice,candidates=[voice])
  edit(base+'.p')['content']['holder_candidates']=[voice]
  edit(base+'.u')['content']['textual_voice']=voice
# P04: keep the valid asserted rejection metaclaim, distinguish its rejected premise.
a=c('benbetera.identity','3a:11','אילימא רבי יהודה בן בתירה','The proposed identity is Rabbi Yehuda ben Beteira.',mode='hypothetical',status='Rejected by the following second-day premise; continuation identifies Yehoshua ben Beteira.')
b=c('benbetera.second','3a:11','הא אמר בשני בחג הוא מזכיר','Rabbi Yehuda ben Beteira says to mention rain on the second festival day.',who='Rabbi Yehuda ben Beteira',voice='anonymous discussion citing Rabbi Yehuda ben Beteira')
e('benbetera.objection','3a:11','אילימא רבי יהודה בן בתירה הא אמר בשני בחג הוא מזכיר',b,a,'objection')
e('benbetera.rejection.support','3a:11','הא אמר בשני בחג הוא מזכיר',b,'ta.resume001.yehuda.bet.reject.tf013')
# P01/P05: grammatical objection is asserted; the geographic proposal is rejected.
a=c('dispersion.proposal','3b:2','אילימא הכי קאמר להו הקב"ה לישראל דבדרתינכו בארבע רוחי דעלמא','Proposed reading: God tells Israel that He scattered them in the four directions of the world.',mode='hypothetical',status='Rejected by the following grammatical objection.',voice='anonymous proposal of an embedded divine address')
b=c('dispersion.grammar','3b:2','אי הכי כארבע בארבע מיבעי ליה','If scattering in four directions were meant, the verse should say בארבע rather than כארבע.')
e('dispersion.objection','3b:2','אי הכי כארבע בארבע מיבעי ליה',b,a,'objection')
r=edit('ta.resume002.winds.correction.tf013');r['content']['target_id']=a;r['links']=[r['content']['source_id'],a]
e('winds.verse.support','3b:2',ix['3b:2']['text'],'ta.resume002.four.winds.verse','ta.resume002.israel.winds.tf013')
# P02: only the initial dictum is unambiguously introduced in Yohanan's name.
narrow('ta.resume004.idolatry.fire','5a:13','א"ל הכי א"ר יוחנן אחת היא שמבערת רשעים בגיהנם','Rabbi Yohanan says that one thing burns the wicked in Gehinnom.')
r=edit('ta.resume004.reporter.ta_resume004_idolatry_fire_a0');r['evidence']=[ev('5a:13','א"ל הכי א"ר יוחנן אחת היא שמבערת רשעים בגיהנם')]
qq=q('idolatry.identity.q','5a:13','מאי היא','What is the one thing that burns the wicked in Gehinnom?')
aa=c('idolatry.identity','5a:13','ע"ז','The one thing is idolatry.')
bb=c('idolatry.sharedword','5a:13','כתיב הכא מוסר הבלים עץ הוא וכתיב התם (ירמיהו י, טו) הבל המה מעשה תעתועים','The continuation links הבלים in Jeremiah 10:8 with הבל המה מעשה תעתועים in Jeremiah 10:15.',voice='anonymous exegetical continuation',comp='composite')
e('idolatry.answer','5a:13','מאי היא ע"ז',aa,qq,'answer');e('idolatry.proof','5a:13',ix['5a:13']['text'],bb,aa)
for r in P['records']:
 if r['id'].startswith('ta.review020.idolatry.'):
  r['uncertainty'].append('Unmarked inner dialogue after Yohanan citation: anonymous continuation or continuation of cited explanation; no unique named ownership assigned.')
# P03: biblical Samuel is an embedded speaker, distinct from amora Shmuel.
voice='Biblical Samuel in the depicted prayer'
narrow('ta.resume004.samuel.prayer','5b:4','אף אני לא יתבטל מעשה ידי בחיי','Samuel petitions that his work not be annulled during his lifetime.',voice)
a=c('samuel.equality','5b:4','שקלתני כמשה ואהרן','Samuel says that God equated him with Moses and Aaron.',who=voice)
b=c('samuel.psalm','5b:4','דכתיב (תהלים צט, ו) משה ואהרן בכהניו ושמואל בקוראי שמו','Psalm 99:6 names Moses and Aaron among His priests and Samuel among those calling His name.',voice='scriptural quotation within the depicted petition',comp='composite')
d=c('samuel.precedent','5b:4','מה משה ואהרן לא בטלו מעשה ידיהם בחייהם','Samuel invokes the precedent that Moses and Aaron did not have their work annulled during their lifetimes.',who=voice)
g=c('saul.divine.regret','5b:4','דכתיב (שמואל א טו, יא) נחמתי כי המלכתי את שאול','The quoted divine speech expresses regret for appointing Saul king.',who='God in the embedded biblical quotation',voice='embedded divine speech quoted in Yohanan narrative')
e('samuel.psalm.support','5b:4',ix['5b:4']['text'],b,a)
e('samuel.analogy','5b:4','מה משה ואהרן לא בטלו מעשה ידיהם בחייהם אף אני לא יתבטל מעשה ידי בחיי',d,'ta.resume004.samuel.prayer','analogy')
for k,target in [('equality',a),('psalm',b),('precedent',d),('regret',g),('petition','ta.resume004.samuel.prayer')]:
 add('narrative.frame.'+k,'attributions','5b:4',dict(surface='א"ל הכי א"ר יוחנן',role='transmitter',candidates=['Rabbi Yitzhak','Rabbi Yohanan'],scope=target,transmission_chain=['Rabbi Yitzhak','Rabbi Yohanan']),t='א"ל הכי א"ר יוחנן',links=[target],unc=['Narrative reporting frame only; original embedded position belongs to depicted speaker, not automatically to the reporting sages.'])
# Close over exact ID tokens in every active content field, including scope strings before semicolons.
def strings(x):
 if isinstance(x,str):yield x
 elif isinstance(x,list):
  for v in x:yield from strings(v)
 elif isinstance(x,dict):
  for v in x.values():yield from strings(v)
def regex(ids):return re.compile(r'(?<![A-Za-z0-9_.:-])(?:'+'|'.join(re.escape(i) for i in sorted(ids,key=len,reverse=True))+r')(?![A-Za-z0-9_.:-])')
while True:
 pat=regex(changed);more=[rid for rid,r in active.items() if rid not in changed and any(pat.search(t) for t in strings([r['links'],r['content']]))]
 if not more:break
 for rid in more:edit(rid)
mapping={rid:rid+'.t020053' for rid in changed};pat=regex(mapping)
def replace(x):
 if isinstance(x,str):return pat.sub(lambda m:mapping[m.group()],x)
 if isinstance(x,list):return [replace(v) for v in x]
 if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
 return x
newrecords=P['records'];records=[]
for rid,r in changed.items():
 r['id']=mapping[rid];r['supersedes']=rid;r['content']=replace(r['content']);r['links']=replace(r['links']);records.append(r)
for r in newrecords:r['content']=replace(r['content']);r['links']=replace(r['links']);records.append(r)
P={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};P.update(owner='L04/taanit_resume_20261126',epoch=3,execution=dict(route='interactive_agent',agent_id='/root/taanit_continuation_5',model_id=None),records=records,coverage=[],open_tails=replace(S['open_tails']))
# Refresh existing coverage only. No source completion count is added by correction.
for cov in S['coverage']:
 affected=any(rid in mapping for rid in cov['record_ids']) or any(r['layer']==cov['layer'] and any(e['segment_id']==cov['segment_id'] for e in r['evidence']) for r in records)
 if not affected:continue
 cc={k:copy.deepcopy(v) for k,v in cov.items() if k!='proposal_execution'};cc['record_ids']=replace(cc['record_ids'])
 for r in records:
  if r['layer']==cc['layer'] and any(e['segment_id']==cc['segment_id'] for e in r['evidence']) and r['id'] not in cc['record_ids']:cc['record_ids'].append(r['id'])
 if cc['record_ids']:cc['extraction_result']='records_found'
 cc['rationale']+=' Delegated020 correction053: source reread, field adjudication and dependency/partition closure; coverage denominator unchanged.';P['coverage'].append(cc)
N=runner.validate_apply(S,P,ss,j)
assert runner.report(S,ss)['completed_by_layer']==runner.report(N,ss)['completed_by_layer']
for r in N['records']:
 if r['release_state']=='valid':assert not any(pat.search(t) for t in strings([r['links'],r['content']])),r['id']

out=JOB/'staging_resume_20261126'/'review_correction053.json';runner.immutable(out,runner.encoded(P))
receipt=dict(status='TARGETED_REPAIR_PENDING_INDEPENDENT_RECHECK',base_snapshot_sha256=BASE,proposal_sha256=runner.sha(out.read_bytes()),proposal_path=str(out),supersession_map=mapping,new_record_ids=[r['id'] for r in newrecords],coverage_inflation=0,all_active_pointer_fields_checked=True,independent_review_claimed=False,findings={'P01':'Separated rejected geographic proposal and asserted grammatical objection; correction retargeted.','P02':'Narrowed Yohanan dictum; inner question, identification, shared-word proof and answer/support links added with attribution uncertainty.','P03':'Narrowed biblical Samuel petition; separate equality, Psalm citation, precedent, divine regret and explicit analogy; narrative reporting frames distinct.','P04':'Separate second-day premise attributed to Rabbi Yehuda ben Beteira and objection to proposed identity.','P05':'Verse-to-exposition support added; existing attribution uncertainty preserved.'})
runner.immutable(pathlib.Path(__file__).with_name('REVIEW_CORRECTION_053.json'),runner.encoded(receipt));print(json.dumps(dict(proposal=str(out),revised=len(mapping),new_records=len(newrecords),total_records=len(records)),indent=2))
