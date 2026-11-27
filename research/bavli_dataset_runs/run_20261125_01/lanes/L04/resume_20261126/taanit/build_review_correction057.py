"""Manually authored from pinned original 6a:2–6b:6; not a semantic extractor."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[7]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit')
j,ss=runner.load(JOB)
assert runner.read(JOB/'CURRENT.json')['snapshot_sha256']=='e85a80cd47c5b5bc79ec9e5b3346d8b58d5dcf7e53a1555e82862972535819d0'
assert runner.read(JOB/'OWNER.json')==dict(owner='L04/taanit_resume_20261126',epoch=3)
ix={s['ref'].replace('Taanit ',''):s for s in ss.values()}
P={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
P.update(owner='L04/taanit_resume_20261126',epoch=3,execution=dict(route='interactive_agent',agent_id='/root/taanit_continuation_5',model_id=None),records=[],coverage=[],open_tails=[])
def ev(r,t=None):
 s=ix[r];t=s['text'] if t is None else t;a=s['text'].index(t);return dict(segment_id=s['id'],start_char=a,end_char=a+len(t),quote=t)
def add(k,l,r,c,t=None,links=None,unc=None,origin='source_paraphrase'):
 rid='ta.review105.'+k;P['records'].append(dict(id=rid,layer=l,evidence=[ev(r,t)],content=c,origin=origin,links=links or [],uncertainty=unc or []));return rid
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
S=runner.current(JOB);BASE=runner.read(JOB/'CURRENT.json')['snapshot_sha256'];active={r['id']:r for r in S['records'] if r['release_state']=='valid'};changed={}
def edit(rid):
 if rid not in changed:changed[rid]={k:copy.deepcopy(v) for k,v in active[rid].items() if k not in ['review_state','release_state','ml_eligible']}
 return changed[rid]
edit('ta.resume016.abahu.rereading')['content']['proposition']='Rabbi Abahu gives the rereading אל תקרי ויראו אלא וייראו. In the cloud-departure context, this means the congregation became visible/exposed, as explained by Rashi, rather than that they feared.'
for rid in ['ta.resume016.abahu.rereading','ta.resume016.abahu.rereading.a','ta.resume016.abahu.rereading.p','ta.resume016.abahu.rereading.u']:
 edit(rid)['uncertainty'].append('TA101-01: unpointed source spelling preserved. Exposed/visible is explanatory translation supported by original9a10 context and additional Rashi on Taanit9a11:1, Vilna Edition, SHA256 ad17f9782b9a7640aee553eea79e7c54a3cb1808b0b1138c74bb1d53e8c7b1d7, text[16][10][0], נתראו / ואתחזיאו; commentary is not part of original source edition or independent source-only reading.')
mother='Mother of Resh Lakish’s child'
edit('ta.resume016.mother.warning.a')['content'].update(surface='אימיה ... אמרה ליה',role='speaker',candidates=[mother])
edit('ta.resume016.mother.warning.p')['content']['holder_candidates']=[mother]
edit('ta.resume016.mother.warning.u')['content']['textual_voice']=mother
for rid in ['ta.resume016.mother.warning.a','ta.resume016.mother.warning.p','ta.resume016.mother.warning.u']:edit(rid)['uncertainty'].append('TA101-02: explicitly introduced character speaker; warning does not certify narrator-level causal responsibility.')
child='Resh Lakish’s child'
for rid in ['ta.resume016.brothers.proof.a','ta.resume016.hint.challenge.q.a']:
 rr=edit(rid);rr['content'].update(surface='ינוקיה דריש לקיש ... א"ל',role='speaker',candidates=[child]);rr['evidence']=[ev('9a:5'),ev('9a:6')];rr['uncertainty'].append('TA101-03: contextual child interlocutor from9a5 and response to Yohanan in9a6; citation speaker is not original author of Genesis.')
edit('ta.resume016.brothers.proof.p')['uncertainty'].append('TA101-03: child is the citing speaker, not the original holder/author of the embedded Genesis statement; holder remains unassigned at that scriptural level.')
add('brothers.scripture','attributions','9a:6',dict(surface='(בראשית מב, כח)',role='quoted_authority',candidates=[],scope='ta.resume016.brothers.proof',transmission_chain=[]),t='והכתיב (בראשית מב, כח) ויצא לבם ויחרדו איש אל אחיו לאמר מה זאת עשה אלהים לנו',links=['ta.resume016.brothers.proof'],unc=['TA101-03: quoted Genesis authority kept distinct from child speaker.'])
add('folly.reciter','attributions','9a:5',dict(surface='לינוקיה דריש לקיש דיתיב ואמר',role='speaker',candidates=[child],scope='ta.resume016.folly.verse.u',transmission_chain=[]),links=['ta.resume016.folly.verse.u','ta.resume016.folly.verse'],unc=['TA101-04: child explicitly recites Proverbs; existing quoted_authority and unassigned original holder remain, without assigning original authorship to the reciter.'])
e('deeds.before.qualifies','7b:15','ויתרון הכשיר חכמה כל שכן אם הוכשרו מעשיהן מעיקרא','ta.resume011.deeds.before','ta.resume011.mercy.strengthen','qualification')
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
mapping={rid:rid+'.t105057' for rid in changed};pat=regex(mapping)
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
 cc['rationale']+=' Delegated101 comparator105 correction057: source reread, field adjudication and dependency/partition closure; coverage denominator unchanged.';P['coverage'].append(cc)
N=runner.validate_apply(S,P,ss,j)
assert runner.report(S,ss)['completed_by_layer']==runner.report(N,ss)['completed_by_layer']
for r in N['records']:
 if r['release_state']=='valid':assert not any(pat.search(t) for t in strings([r['links'],r['content']])),r['id']



# Preserve all new nine-segment records and coverage without independent acceptance.
for r in N['records']:
 if r['id'].startswith('ta.resume056.'):assert r==active[r['id']]
out=JOB/'staging_resume_20261126'/'review_correction057.json';runner.immutable(out,runner.encoded(P))
receipt=dict(status='TARGETED_REPAIR_PENDING_INDEPENDENT_RECHECK',base_snapshot_sha256=BASE,proposal_sha256=runner.sha(out.read_bytes()),proposal_path=str(out),supersession_map=mapping,new_record_ids=[r['id'] for r in newrecords],comparison_sha256='37b5d1ea044a0d5c57a458456ea9c5193be54396775b54f82a60d37e203a5584',verdict_sha256='c3e3e7178aa9fc250fa2a2ab847860505ecfcb09e6b8a0858bd4b83428f195dd',comparison_final_receipt_sha256='bed62d69ad24da4c59307ddd31075109a508f958f4819b1379d9b72f77a813b7',issue_fix_mapping={'TA101-01':'Exposed/visible gloss with unchanged source spelling and distinct bound Rashi evidence; dependency closure.','TA101-02':'Mother speaker/voice/holder populated, warning epistemic limits retained.','TA101-03':'Contextual child speaker for counter-question and Genesis citation; quoted authority separate and original holder not assigned to citer.','TA101-04':'Added child reciter attribution to quoted utterance without replacing Scripture authority.','TA101-05':'Added source-explicit qualification from deeds-before to mercy remedy.'},coverage_inflation=0,newest9_records_byte_equivalent=True,independent_acceptance_claimed=False,reader_errors_uncertainties_granularity_preserved=['TA101-'+str(i).zfill(2) for i in range(6,16)],comparison_chronology_preserved='Pins before semantic inspection; replay after semantic inspection before initial freeze; auxiliary reader-ID erratum in revision2. No pre-inspection replay claim.',comparison_output_path_deviation='Comparator artifacts read-only in disclosed main-checkout path; producer writes only isolated L04 lane/job.')
runner.immutable(pathlib.Path(__file__).with_name('REVIEW_CORRECTION_057.json'),runner.encoded(receipt));print(json.dumps(dict(proposal=str(out),supersessions=len(mapping),new_records=len(newrecords),total=len(records))))
