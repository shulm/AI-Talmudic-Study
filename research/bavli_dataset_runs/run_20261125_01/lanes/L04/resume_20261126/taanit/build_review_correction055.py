"""Manually authored from pinned original 6a:2–6b:6; not a semantic extractor."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[7]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit')
j,ss=runner.load(JOB)
assert runner.read(JOB/'CURRENT.json')['snapshot_sha256']=='415494e40a79b4f217d5e265c9d5b126e71677af764a9988013249e571b75888'
assert runner.read(JOB/'OWNER.json')==dict(owner='L04/taanit_resume_20261126',epoch=3)
ix={s['ref'].replace('Taanit ',''):s for s in ss.values()}
P={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
P.update(owner='L04/taanit_resume_20261126',epoch=3,execution=dict(route='interactive_agent',agent_id='/root/taanit_continuation_5',model_id=None),records=[],coverage=[],open_tails=[])
def ev(r,t=None):
 s=ix[r];t=s['text'] if t is None else t;a=s['text'].index(t);return dict(segment_id=s['id'],start_char=a,end_char=a+len(t),quote=t)
def add(k,l,r,c,t=None,links=None,unc=None,origin='source_paraphrase'):
 rid='ta.review062.'+k;P['records'].append(dict(id=rid,layer=l,evidence=[ev(r,t)],content=c,origin=origin,links=links or [],uncertainty=unc or []));return rid
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
splits=[
 ('A1','iron.scholars','7a:8','מה ברזל זה אחד מחדד את חבירו','אף שני תלמידי חכמים מחדדין זה את זה בהלכה','In the analogy, one piece of iron sharpens another.','Two Torah scholars sharpen one another in halakha.',[]),
 ('A2','fire.solitary','7a:9','מה אש אינו דולק יחידי','אף דברי תורה אין מתקיימין ביחידי','In the analogy, fire does not burn alone.','Words of Torah do not endure with a solitary learner.',[]),
 ('A3','small.sharpens','7a:12','מה עץ קטן מדליק את הגדול','אף תלמידי חכמים קטנים מחדדים את הגדולים','In the analogy, small wood ignites large wood.','Lesser Torah scholars sharpen greater ones.',[]),
 ('A4','water.humility','7a:15','מה מים מניחין מקום גבוה והולכין למקום נמוך','אף דברי תורה אין מתקיימין אלא במי שדעתו שפלה','In the analogy, water leaves a high place and goes to a low place.','Words of Torah endure only in a person of humble disposition.',[]),
 ('A5','vessels.humility','7a:16','מה שלשה משקין הללו אין מתקיימין אלא בפחות שבכלים','אף דברי תורה אין מתקיימין אלא במי שדעתו שפלה','In this analogy, these three liquids keep only in lowly vessels.','Words of Torah endure only in a person of humble disposition.',['lowly vessels are necessary for preservation within this analogy']),
 ('A6','attention.liquids','7b:1','דבר אחר מה שלשה משקין הללו אין נפסלין אלא בהיסח הדעת','אף דברי תורה אין משתכחין אלא בהיסח הדעת','The alternative analogy says these three liquids spoil only through inattention.','The alternative explanation says words of Torah are forgotten only through inattention.',['inattention is necessary for spoilage within this analogy'])]
fixes={}
for finding,key,ref,premise,conclusion,ptext,ctext,pcond in splits:
 base='ta.resume010.'+key;newid='ta.review062.'+key+'.premise';oldgroup=[base,base+'.a',base+'.p',base+'.u']
 for rid in oldgroup:
  rr=edit(rid);rr['evidence']=[ev(ref,conclusion)];rr['uncertainty'].append('TA062-'+finding+': composite split into distinct premise/conclusion with typed analogy; original attribution uncertainty retained.')
 edit(base)['content']['proposition']=ctext
 edit(base+'.u')['content']['composition']='atomic'
 if finding=='A6':
  edit(base)['content']['conditions']=['inattention is necessary for forgetting in this alternative explanation'];edit(base+'.p')['content']['conditions']=edit(base)['content']['conditions']
 for suffix in ['', '.a','.p','.u']:
  rr={k:copy.deepcopy(v) for k,v in active[base+suffix].items() if k not in ['review_state','release_state','ml_eligible','supersedes']};rr['id']=newid+suffix;rr['evidence']=[ev(ref,premise)];rr['links']=[newid if v==base else v for v in rr['links']];rr['uncertainty'].append('Separate source-explicit analogy premise; this records the teaching, not empirical certification.')
  if suffix=='':rr['content'].update(proposition=ptext,conditions=pcond,scope='Taanit '+ref+' analogy premise')
  if suffix=='.a':rr['content']['scope']=newid
  if suffix=='.p':rr['content'].update(claim_id=newid,conditions=pcond)
  if suffix=='.u':rr['content']['composition']='atomic'
  P['records'].append(rr)
 e(key+'.analogy',ref,ix[ref]['text'],newid,base,'analogy');fixes['TA062-GRAPH-'+finding]=dict(premise_id=newid,conclusion_id=base,analogy_id='ta.review062.'+key+'.analogy')
# Four quoted proof bases: the citer is not automatically the quoted authority.
for key,ref,quote,proposition,target in [
 ('fire','7a:9',"שנאמר (ירמיהו כג, כט) הלא כה דברי כאש נאם ה'",'The cited Jeremiah verse compares the divine word to fire.','ta.resume010.fire.q'),
 ('foolish','7a:10','שנאמר ונואלו','The quoted ונואלו supplies the scriptural basis for becoming foolish.','ta.resume010.solitary.foolish'),
 ('wood','7a:12','שנאמר (משלי ג, יח) עץ חיים היא למחזיקים בה','The cited Proverbs verse calls Torah a tree of life to those who hold it.','ta.resume010.wood.q'),
 ('water','7a:15','דכתיב הוי כל צמא לכו למים','The quoted invitation calls every thirsty person to water, supplying the water comparison.','ta.resume010.water.humility.q')]:
 v=c('proof.'+key,ref,quote,proposition,voice='quoted scriptural authority')
 next(r for r in P['records'] if r['id']==v+'.a')['content'].update(surface=quote,role='quoted_authority',candidates=[])
 e('proof.'+key+'.support',ref,quote,v,target)
 next(r for r in P['records'] if r['id']=='ta.review062.proof.'+key+'.support')['uncertainty'].append('Verse supplies the comparison basis represented in the question, not by itself the downstream pedagogical inference.' if key!='foolish' else 'Explicit שנאמר supports the foolishness conclusion.')
# Wine outcome illustrates lowly containers; a taunt alone is not that premise.
n=edit('ta.resume010.narrative.illustrates');n['content'].update(source_id='ta.resume010.wine.sours',target_id='ta.review062.vessels.humility.premise',relation='support',explicitness='editorial_reconstruction');n['links']=['ta.resume010.wine.sours','ta.review062.vessels.humility.premise'];n['evidence']=[ev('7a:17'),ev('7a:18')];n['origin']='editorial_inference';n['uncertainty'].append('TA062-ENDPOINT: wine transferred to precious vessels and soured is the relevant narrative outcome; link to the lowly-vessel premise is an editorial account of the narrative illustration, not empirical proof of a universal rule. Taunt retained separately.')
# Do not force the handsome-scholars challenge into an objection against humility.
edit('ta.resume010.handsome.scholars.q')['uncertainty'].append('TA062-OBJECTION-SCOPE: local challenge addresses the narrative implication of physical ugliness; physical beauty is not identical with pride. No definitive objection-to-humility edge is assigned.')
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
mapping={rid:rid+'.t062055' for rid in changed};pat=regex(mapping)
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
 cc['rationale']+=' Delegated055 comparator062 correction055: source reread, field adjudication and dependency/partition closure; coverage denominator unchanged.';P['coverage'].append(cc)
N=runner.validate_apply(S,P,ss,j)
assert runner.report(S,ss)['completed_by_layer']==runner.report(N,ss)['completed_by_layer']
for r in N['records']:
 if r['release_state']=='valid':assert not any(pat.search(t) for t in strings([r['links'],r['content']])),r['id']


# Closure must not alter any of the newest15 source records.
oldnew={r['id']:r for r in S['records'] if r['id'].startswith('ta.resume054.')}
for r in N['records']:
 if r['id'] in oldnew:assert r==oldnew[r['id']]
out=JOB/'staging_resume_20261126'/'review_correction055.json';runner.immutable(out,runner.encoded(P))
fixes.update({'TA062-GRAPH-B1':'Quoted fire basis supports comparison question.','TA062-GRAPH-B2':'Quoted ונואלו supports foolishness conclusion.','TA062-GRAPH-B3':'Quoted tree basis supports comparison question.','TA062-GRAPH-B4':'Quoted water basis supports comparison question.','TA062-ENDPOINT':'Wine-souring outcome supports lowly-vessel premise with editorial scope.','TA062-ONLY-VESSELS':'Separate premise preserves only in lowly vessels.','TA062-ONLY-ATTENTION':'Both premise and conclusion preserve only through inattention; anonymous alternative maintained.'})
receipt=dict(status='PRODUCER_TARGETED_REPAIR_PENDING_INDEPENDENT_RECHECK',base_snapshot_sha256=BASE,comparison_sha256='b126ef13aeb1027ed41a4bcd57470d2ff06301661a45f9d410aeb42ef5162abd',verdict_sha256='9da24aea259f1a4adae3c18d48b6be25379f067e6a3ab8c2b415589fed2b7163',proposal_sha256=runner.sha(out.read_bytes()),proposal_path=str(out),supersession_map=mapping,new_record_ids=[r['id'] for r in newrecords],issue_fix_mapping=replace(fixes),coverage_inflation=0,all_active_pointer_fields_checked=True,newest15_records_byte_equivalent=True,independent_review_claimed=False,reader_qualifications_preserved=['TA062-READER-GLOSS','TA062-READER-SOIL'],unresolved_scope_preserved='TA062-OBJECTION-SCOPE')
runner.immutable(pathlib.Path(__file__).with_name('REVIEW_CORRECTION_055.json'),runner.encoded(receipt));print(json.dumps(dict(proposal=str(out),supersessions=len(mapping),new_records=len(newrecords),total=len(records))))
