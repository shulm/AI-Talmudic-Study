"""Manual source reading: amaltara and the explicit reversed transmission."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6];sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
j,ss=runner.load(JOB);byref={r['ref'].removeprefix('Eruvin '):r for r in ss.values()};records=[]
def add(key,layer,refs,content,links=(),uncertainty=(),origin='source_paraphrase'):
    rid='er.versions.001.'+layer+'.'+key
    evidence=[dict(segment_id=byref[r]['id'],start_char=0,end_char=len(byref[r]['text']),quote=byref[r]['text']) for r in refs]
    records.append(dict(id=rid,layer=layer,evidence=evidence,content=content,links=list(links),uncertainty=list(uncertainty),origin=origin));return rid
def c(key,ref,text,mode='asserted',conditions=(),scope='Amaltara and partly-above-height-limit discussion'):
    return add(key,'claims',[ref],dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode))
def q(key,ref,text):return add(key,'questions',[ref],dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='unreviewed_alternatives'))
def e(key,refs,src,tgt,rel):return add(key,'edges',refs,dict(source_id=src,target_id=tgt,relation=rel,explicitness='source_explicit'),[src,tgt])
def a(key,ref,surface,role,names,scope,chain=()):return add(key,'attributions',[ref],dict(surface=surface,role=role,candidates=names,scope=scope,transmission_chain=list(chain)))
def p(key,ref,holder,cid,status,conditions=()):return add(key,'positions',[ref],dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(conditions),local_status=status),[cid])
am=['3a:'+str(i) for i in range(12,16)]
ht=['3a:'+str(i) for i in range(16,28)]+['3b:'+str(i) for i in range(1,6)]
refs=am+ht
add('amaltara','structure',am,dict(title='מהי אמלתרא ומדוע היא ניכרת',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('height.versions','structure',ht,dict(title='מקצת הקורה והסכך מעל עשרים: שתי מסורות ודיון בחלל',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rows=[
 ('am.kini','3a:12','Rav Hama son of Rabbah bar Avuha defines amaltara as קיני.'),
 ('am.cedar','3a:12','Rav Dimi reports that in the West amaltara is explained as פסקי דארזא.'),
 ('am.inclusion','3a:13','The view accepting cedar pieces certainly accepts קיני; the view specifying קיני does not accept cedar pieces.'),
 ('am.length','3a:14','The proposed rationale for cedar pieces is their large length.','rejected'),
 ('am.sukkah.counter','3a:14','The objection notes that a sukkah also has great length, yet the Rabbis do not permit the excess height.'),
 ('am.importance','3a:15','The replacement explanation is that the important feature attracts notice or publicity, אית ליה קלא.'),
 ('v1.mavoi','3a:16','In the first transmission Rabbah validates a mavoi whose beam is partly within twenty cubits and partly above.'),
 ('v1.sukkah','3a:16','In that first transmission Rabbah invalidates a sukkah whose covering is partly within twenty cubits and partly above.'),
 ('v1.trim','3a:17','The question proposes notional thinning as the reason to validate the mavoi and asks to apply it to sukkah.','hypothetical'),
 ('v1.sun','3a:18','The proposed answer says thinning would leave more sunlight than shade in the sukkah.'),
 ('v1.wind','3a:19','The objection says thinning would likewise leave a beam removable by wind.'),
 ('v1.notional','3a:19','The reply argues that if the beam is notionally treated as metal rods, the sukkah covering could likewise be treated as giving more shade than sunlight.','hypothetical'),
 ('v1.memory.sukkah','3a:20','Rava of Parzakya explains that an individual’s sukkah lacks another person to remind its user.'),
 ('v1.memory.mavoi','3a:20','In the first explanation a public mavoi has users who remind each other.'),
 ('v1.ravina.sukkah','3a:21','Ravina explains that the Rabbis were stringent with sukkah because it is Torah law.'),
 ('v1.ravina.mavoi','3a:21','Ravina explains that they were not stringent with mavoi because it is rabbinic law.'),
 ('v2.mavoi','3a:22','Rav Adda bar Mattana transmits Rabbah’s statement in reverse: the mavoi is invalid.'),
 ('v2.sukkah','3a:22','In Rav Adda bar Mattana’s reversed transmission, Rabbah validates the sukkah.'),
 ('v2.trim','3a:23','The reversed-version question proposes notional thinning for sukkah and asks to apply it also to mavoi.','hypothetical'),
 ('v2.wind','3a:24','The proposed answer says thinning leaves a beam removable by wind.'),
 ('v2.sun','3a:24','The objection says thinning the sukkah likewise leaves more sunlight than shade.'),
 ('v2.notional','3a:24','The argument says notional restoration of shade in sukkah could equally treat the beam as metal rods.','hypothetical'),
 ('v2.memory.sukkah','3a:25','In the reversed version Rava of Parzakya says the individual takes responsibility and remembers.'),
 ('v2.memory.mavoi','3a:25','In the reversed version the public mavoi’s users rely on one another and fail to remember.'),
 ('v2.proverb','3a:25','The saying about partners’ pot being neither hot nor cold illustrates the mutual reliance explanation.'),
 ('v2.ravina.sukkah','3a:26','In the reversed version Ravina says Torah-law sukkah needs no reinforcement.'),
 ('v2.ravina.mavoi','3a:26','In the reversed version Ravina says rabbinic mavoi needs reinforcement.'),
 ('final.rabbahula','3a:27','Rabbah bar Rav Ulla declares both cases invalid.'),
 ('final.rava','3a:27','Rava declares both cases valid.'),
 ('clear.space','3b:1','The explanation measures the clear interior height of sukkah and mavoi.'),
 ('pappa.support','3b:2','Rav Pappa cites to Rava a baraita measuring excess height against the Heikhal opening and observes its interior was twenty cubits.'),
 ('shimi.challenge','3b:3','Rav Shimi bar Rav Ashi challenges Rav Pappa with a teaching placing the beam from the twenty-cubit edge downward.'),
 ('amend.up','3b:4','The proposed answer reads the teaching as upward instead.','challenged'),
 ('text.down','3b:4','The counter-objection insists that the source actually says downward.'),
 ('analogy.clearance','3b:5','The answer treats downward like upward: as the upper limit concerns twenty cubits of clear space, the lower limit concerns ten of clear space.')]
cs={}
for row in rows:
    key,ref,text,*mode=row
    cond=['beam/covering partly within twenty cubits and partly above'] if key.startswith(('v1.','v2.','final.')) else []
    if key.startswith('v1.'):scope='First transmission of Rabbah; reversed version separately preserved at 3a:22-26'
    elif key.startswith('v2.'):scope='Reversed transmission by Rav Adda bar Mattana; not an inferred retraction'
    else:scope='Amaltara or final clear-space discussion'
    cs[key]=c(key,ref,text,mode[0] if mode else 'asserted',cond,scope)
qs={}
for key,ref,text in [
 ('am.definition','3a:12','What is amaltara?'),
 ('am.reason','3a:14','Why do cedar pieces suffice, if the proposed length explanation also applies to sukkah?'),
 ('v1.difference','3a:17','Why validate mavoi by thinning but not apply thinning to sukkah?'),
 ('v1.beam.counter','3a:19','Would thinning not also make the beam liable to wind, requiring the same notional repair?'),
 ('v2.difference','3a:23','Why validate sukkah by thinning but not apply thinning to mavoi?'),
 ('v2.cover.counter','3a:24','Would thinning not also diminish the sukkah shade, requiring the same notional repair?'),
 ('final','3a:27','What is the outcome for these two partly-above-height cases?'),
 ('shimi','3b:3','Does the teaching to place the beam downward from twenty contradict the clear-space reading?'),
 ('literal.down','3b:4','How can the answer say upward when the teaching says downward?')]:qs[key]=q(key,ref,text)
voices={
'3a:12':'anonymous question; Rav Hama and Rav Dimi’s Western report','3a:13':'anonymous comparison of definitions','3a:14':'anonymous rationale question and counterexample','3a:15':'anonymous replacement rationale','3a:16':'Rabbah, first transmission','3a:17':'anonymous question, first transmission','3a:18':'anonymous answer, first transmission','3a:19':'anonymous counterargument, first transmission','3a:20':'Rava of Parzakya, first transmission','3a:21':'Ravina, first transmission','3a:22':'Rav Adda bar Mattana reports Rabbah in reverse','3a:23':'anonymous question, reversed transmission','3a:24':'anonymous argument, reversed transmission','3a:25':'Rava of Parzakya, reversed transmission','3a:26':'Ravina, reversed transmission','3a:27':'anonymous outcome question followed by Rabbah bar Rav Ulla and Rava','3b:1':'anonymous explanation of clear-space reading','3b:2':'Rav Pappa speaking to Rava','3b:3':'Rav Shimi bar Rav Ashi challenging Rav Pappa','3b:4':'anonymous proposed reading and textual counter-objection','3b:5':'anonymous resolution by comparison'}
for ref,voice in voices.items():
    add('u.'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=voice,composition='composite'),origin='editorial_inference')
    if ref in ['3a:12','3a:13','3a:14','3a:15','3a:17','3a:18','3a:19','3a:23','3a:24','3a:27','3b:1','3b:4','3b:5']:
        a('anonymous.'+ref.replace(':','_'),ref,'anonymous discourse','anonymous',[],'Local question, inference, or explanation; no identified historical author')
for key,ref,surface,role,names,scope,chain in [
 ('hama','3a:12','רב חמא בריה דרבה בר אבוה אמר','speaker',['רב חמא בריה דרבה בר אבוה'],'קיני definition',[]),
 ('dimi','3a:12','כי אתא רב דימי אמר','transmitter',['רב דימי'],'Western cedar-piece explanation',['רב דימי','אמרי במערבא']),
 ('west','3a:12','אמרי במערבא','collective',['anonymous Western authorities'],'Cedar-piece explanation',[]),
 ('rabbah.v1','3a:16','אמר רבה','speaker',['רבה'],'First transmission only',[]),
 ('parzakya.v1','3a:20',"אמר רבא מפרזקי'",'speaker',['רבא מפרזקיא'],'First memory rationale; textual label retained',[]),
 ('ravina.v1','3a:21','רבינא אמר','speaker',['רבינא'],'First stringency rationale',[]),
 ('adda','3a:22','רב אדא בר מתנה מתני','transmitter',['רב אדא בר מתנה'],'Explicitly reversed Rabbah report',['רב אדא בר מתנה','רבה']),
 ('rabbah.v2','3a:22','אמר רבה','quoted_authority',['רבה'],'Reversed transmission only',['רב אדא בר מתנה','רבה']),
 ('parzakya.v2','3a:25','אמר רבא מפרזקיא','speaker',['רבא מפרזקיא'],'Reversed-version memory rationale',[]),
 ('ravina.v2','3a:26','רבינא אמר','speaker',['רבינא'],'Reversed-version reinforcement rationale',[]),
 ('rabbahula','3a:27','רבה בר רב עולא אמר','speaker',['רבה בר רב עולא'],'Both invalid; distinct from Rabbah',[]),
 ('rava','3a:27','רבא אמר','speaker',['רבא'],'Both valid; distinct from רבה',[]),
 ('pappa','3b:2','א"ל רב פפא לרבא','speaker',['רב פפא'],'Support offered to Rava; addressee not misclassified',[]),
 ('shimi','3b:3','איתיביה רב שימי בר רב אשי','speaker',['רב שימי בר רב אשי'],'Challenges Rav Pappa; father Rav Ashi is not the speaker',[])]:a(key,ref,surface,role,names,scope,chain)
for key,ref,holder in [
 ('am.kini','3a:12','רב חמא בריה דרבה בר אבוה'),('am.cedar','3a:12','anonymous Western authorities'),
 ('v1.mavoi','3a:16','רבה'),('v1.sukkah','3a:16','רבה'),('v1.memory.sukkah','3a:20','רבא מפרזקיא'),('v1.memory.mavoi','3a:20','רבא מפרזקיא'),('v1.ravina.sukkah','3a:21','רבינא'),('v1.ravina.mavoi','3a:21','רבינא'),
 ('v2.mavoi','3a:22','רבה'),('v2.sukkah','3a:22','רבה'),('v2.memory.sukkah','3a:25','רבא מפרזקיא'),('v2.memory.mavoi','3a:25','רבא מפרזקיא'),('v2.ravina.sukkah','3a:26','רבינא'),('v2.ravina.mavoi','3a:26','רבינא'),
 ('final.rabbahula','3a:27','רבה בר רב עולא'),('final.rava','3a:27','רבא'),('pappa.support','3b:2','רב פפא'),('shimi.challenge','3b:3','רב שימי בר רב אשי')]:
    row=next(r for r in records if r['id']==cs[key])
    status='First transmission; opposed version separately retained' if key.startswith('v1.') else 'Reversed transmission; not a retraction' if key.startswith('v2.') else 'Stated local position'
    p(key,ref,holder,cs[key],status,row['content']['conditions'])
for key,ref,src,tgt,rel in [
 ('am.kini.answer','3a:12','am.kini','am.definition','answer'),('am.cedar.answer','3a:12','am.cedar','am.definition','answer'),('am.reason.answer','3a:15','am.importance','am.reason','answer'),
 ('v1.sun.answer','3a:18','v1.sun','v1.difference','answer'),('v1.memory.answer','3a:20','v1.memory.mavoi','v1.difference','answer'),('v1.ravina.answer','3a:21','v1.ravina.sukkah','v1.difference','answer'),
 ('v2.wind.answer','3a:24','v2.wind','v2.difference','answer'),('v2.memory.answer','3a:25','v2.memory.sukkah','v2.difference','answer'),('v2.ravina.answer','3a:26','v2.ravina.mavoi','v2.difference','answer'),
 ('final.invalid','3a:27','final.rabbahula','final','answer'),('final.valid','3a:27','final.rava','final','answer'),('final.down.answer','3b:5','analogy.clearance','literal.down','answer')]:e(key,[ref],cs[src],qs[tgt],rel)
for key,ref,src,tgt,rel in [
 ('am.length.reject','3a:14','am.sukkah.counter','am.length','objection'),('am.reason.replace','3a:15','am.importance','am.length','correction'),
 ('v1.beam.objection','3a:19','v1.wind','v1.sun','objection'),('v1.notional.objection','3a:19','v1.notional','v1.sun','objection'),
 ('v2.cover.objection','3a:24','v2.sun','v2.wind','objection'),('v2.notional.objection','3a:24','v2.notional','v2.wind','objection'),
 ('v2.proverb.support','3a:25','v2.proverb','v2.memory.mavoi','support'),('clear.space.support','3b:1','clear.space','final.rava','support'),
 ('pappa.support','3b:2','pappa.support','final.rava','support'),('shimi.objection','3b:3','shimi.challenge','pappa.support','objection'),('text.objection','3b:4','text.down','amend.up','objection')]:e(key,[ref],cs[src],cs[tgt],rel)
for key in ['v1.mavoi','v1.sukkah','v2.mavoi','v2.sukkah']:
    next(r for r in records if r['id']==cs[key])['uncertainty']=['Two explicit textual transmissions retained; no historical chronology or preferred Rabbah version inferred.']
next(r for r in records if r['id']==cs['am.kini'])['uncertainty']=['Technical term קיני retained as source wording; no uncited architectural identification forced.']
next(r for r in records if r['id']==cs['analogy.clearance'])['uncertainty']=['The raw segment says עשרה without an explicit unit; lower minimum convention not inserted into the literal source or treated as explicit here.']
coverage=[]
for ref in refs:
    seg=byref[ref]['id']
    for layer in runner.LAYERS:
        ids=[r['id'] for r in records if (layer=='reconciliation' or r['layer']==layer) and any(x['segment_id']==seg for x in r['evidence'])]
        coverage.append(dict(segment_id=seg,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Manual source and omission reread; first/reversed transmissions and their different explanations preserved, named transmitters distinguished, conditional thinning arguments retained. Next sugya inspected from 3b:6.' if ids else 'Actual layer pass found no separate '+layer+' object in this segment; source arguments retained in other applicable layers.'))
proposal=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=Path(__file__).with_name('eruvin_versions_001.json');runner.immutable(out,runner.encoded(proposal));print(runner.submit(JOB,out,'L03/eruvin',2));print(runner.replay(JOB))
