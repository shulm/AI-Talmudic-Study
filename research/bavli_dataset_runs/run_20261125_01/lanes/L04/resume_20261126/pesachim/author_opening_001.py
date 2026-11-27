"""Manually authored source readings; helpers only serialize exact anchored records.

This is a proposal authoring artifact, not an alternate semantic runner.
Use the frozen common runner for validation, promotion, replay and exports.
"""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
spec = importlib.util.spec_from_file_location('production', ROOT / 'bavli_production_v1/runner.py')
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
JOB = Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_pesachim')
meta, segments = r.load(JOB)
refs = {s['ref'].split(' ', 1)[1]: s for s in segments.values()}
records = []
def ev(ref, quote=None):
    s=refs[ref]; text=s['text']; quote=text if quote is None else quote
    assert text.count(quote)==1, (ref,quote)
    start=text.index(quote)
    return dict(segment_id=s['id'],start_char=start,end_char=start+len(quote),quote=quote)
def add(key,layer,content,evidence,links=(),uncertainty=(),origin='source_paraphrase'):
    rid='pe.r001.'+key
    records.append(dict(id=rid,layer=layer,content=content,evidence=evidence,links=list(links),uncertainty=list(uncertainty),origin=origin))
    return rid
def claim(key,ref,quote,proposition,holder=None,mode='asserted',conditions=(),scope='Local lexical argument about אור',role=None,chain=(),uncertainty=()):
    evidence=[ev(ref,quote)]
    u=add(key+'.u','utterances',dict(textual_voice=holder or 'anonymous discussion',discourse_role=role or mode,composition='atomic'),evidence)
    c=add(key+'.c','claims',dict(proposition=proposition,conditions=list(conditions),scope=scope,assertion_mode=mode),evidence,[u],uncertainty)
    a=add(key+'.a','attributions',dict(surface=holder or '',role='speaker' if holder else 'anonymous',candidates=[holder] if holder else [],scope='Textual voice of '+c,transmission_chain=list(chain)),evidence,[c])
    if role!='biblical quotation':
        add(key+'.p','positions',dict(holder_candidates=[holder] if holder else [],claim_id=c,question_id=None,conditions=list(conditions),local_status=mode+' in this local discussion; not a later halakhic ruling'),evidence,[c,a])
    return c
def question(key,ref,quote,text,conditions=(),status='none'):
    return add(key,'questions',dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status=status),[ev(ref,quote)])
def edge(key,a,b,relation,ref,quote=None):
    return add(key,'edges',dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),[ev(ref,quote)],[a,b])

add('mishnah','structure',dict(title='Mishnah: search for leaven and cellar rows',primary=True,boundary='closed',legacy_ids=[]),[ev('2a:1')],origin='editorial_inference')
core=['2a:'+str(i) for i in range(2,10)]+['2b:'+str(i) for i in range(1,5)]
add('lexical','structure',dict(title='Meaning of אור: initial readings and textual challenges; continues through 3a:9',primary=True,boundary='open_right',legacy_ids=[]),[ev(x) for x in core],uncertainty=['Administrative batch ends at 2b:4, not a sugya ending. Continuation through 3a:9 was read as context.'],origin='editorial_inference')
c=claim('search','2a:1','לאור הנר','Search for leaven by candlelight.',scope='Mishnah search for leaven',conditions=['אור of the fourteenth; subsequent discussion 3a:9 establishes night'])
claim('time','2a:1','לארבעה עשר בודקין את החמץ','The leaven search is on אור of the fourteenth.',scope='Mishnah timing',conditions=['fourteenth of Nisan'],uncertainty=['Night meaning established in later 3a:9; not inferred from word אור alone.'])
claim('exempt','2a:1','כל מקום שאין מכניסין בו חמץ אין צריך בדיקה','A place into which leaven is not brought needs no search.',conditions=['leaven is not brought into the place'],scope='Mishnah search scope')
claim('cellar','2a:1',"ובמה אמרו ב' שורות במרתף מקום שמכניסין בו חמץ",'The two-row cellar rule concerns a place into which leaven is brought.',conditions=['cellar where leaven is brought'],scope='Mishnah cellar scope')
bs=claim('bs','2a:1',"בית שמאי אומרים ב' שורות על פני כל המרתף",'Beit Shammai require two rows across the whole cellar.',holder='בית שמאי',conditions=['cellar where leaven is brought'],scope='Cellar rows; geometry not resolved here')
bh=claim('bh','2a:1','ובית הלל אומרים שתי שורות החיצונות שהן העליונות','Beit Hillel require the two outer rows that are uppermost.',holder='בית הלל',conditions=['cellar where leaven is brought'],scope='Cellar rows; geometry not resolved here')
q=question('meaning.q','2a:2','מאי אור','What does אור mean here?',status='unreviewed_alternatives')
hn=claim('huna','2a:2','רב הונא אמר נגהי','Rav Huna glosses אור as נגהי.',holder='רב הונא',mode='reconciled',uncertainty=['3a:9 identifies this as his local word for night; no maintained disagreement with Rav Yehuda.'])
yh=claim('yehuda','2a:2','ורב יהודה אמר לילי','Rav Yehuda glosses אור as לילי.',holder='רב יהודה',mode='reconciled',uncertainty=['3a:9 explicitly says both mean night.'])
edge('huna.answer',hn,q,'answer','2a:2','רב הונא אמר נגהי');edge('yehuda.answer',yh,q,'answer','2a:2','ורב יהודה אמר לילי')
initial=claim('initial','2a:2','קא סלקא דעתך דמאן דאמר נגהי נגהי ממש ומאן דאמר לילי לילי ממש','The initial supposition takes נגהי literally as day and לילי literally as night.',mode='rejected',role='initial supposition',uncertainty=['Rejected explicitly by 3a:9, which was read as context but is not counted as covered here.'])

g=claim('genesis44','2a:3','מיתיבי (בראשית מד, ג) הבקר אור והאנשים שולחו אלמא אור יממא הוא','Genesis 44:3 is offered as evidence that אור denotes day.',mode='challenged',role='scriptural inference')
edge('gen44.challenge',g,yh,'objection','2a:3','מיתיבי (בראשית מד, ג) הבקר אור והאנשים שולחו אלמא אור יממא הוא')
q3=question('wordorder.q','2a:3','מי כתיב האור בקר','Does the verse say האור בקר?')
reply=claim('gen44reply','2a:3','הבקר אור כתיב כמאן דאמר צפרא נהר','It says הבקר אור: the morning became light, not that אור means morning.',role='rebuttal')
edge('gen44reply.edge',reply,g,'answer','2a:3','מי כתיב האור בקר הבקר אור כתיב כמאן דאמר צפרא נהר')
travel=claim('travel','2a:3','וכדרב יהודה אמר רב דאמר רב יהודה אמר רב לעולם יכנס אדם בכי טוב ויצא בכי טוב','A person should enter and depart while it is light.',holder='רב',chain=['רב יהודה','רב'],scope='Travel in daylight; Rav Yehuda transmits Rav',conditions=['travel entry and departure'])
add('travel.transmitter','attributions',dict(surface='רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope=travel,transmission_chain=['רב יהודה','רב']),[ev('2a:3','וכדרב יהודה אמר רב דאמר רב יהודה אמר רב לעולם יכנס אדם בכי טוב ויצא בכי טוב')],[travel])
edge('travel.support',travel,reply,'support','2a:3','וכדרב יהודה אמר רב דאמר רב יהודה אמר רב לעולם יכנס אדם בכי טוב ויצא בכי טוב')
s=claim('samuel23','2a:4','מיתיבי (שמואל ב כג, ד) וכאור בקר יזרח שמש אלמא אור יממא הוא','II Samuel 23:4 is offered as evidence for the daytime sense.',mode='challenged')
edge('sam23.challenge',s,yh,'objection','2a:4','מיתיבי (שמואל ב כג, ד) וכאור בקר יזרח שמש אלמא אור יממא הוא')
question('sam23.q','2a:4','מי כתיב אור בקר','Does it say אור בקר without the comparative כ?')
sr=claim('sam23reply','2a:4','וכאור בקר כתיב והכי קאמר וכאור בקר בעולם הזה כעין זריחת שמש לצדיקים לעולם הבא','The comparative wording describes this-world morning light as resembling the sun shining for the righteous in the world to come.',scope='Anonymous exposition of II Samuel 23:4')
edge('sam23reply.edge',sr,s,'answer','2a:4','מי כתיב אור בקר וכאור בקר כתיב והכי קאמר וכאור בקר בעולם הזה כעין זריחת שמש לצדיקים לעולם הבא')
gen=claim('gen1','2a:5','מיתיבי (בראשית א, ה) ויקרא אלהים לאור יום אלמא אור יממא הוא','Genesis 1:5 is offered as evidence that אור means day.',mode='challenged')
edge('gen1.challenge',gen,yh,'objection','2a:5','מיתיבי (בראשית א, ה) ויקרא אלהים לאור יום אלמא אור יממא הוא')
dawn=claim('dawn','2a:5','הכי קאמר למאיר ובא קראו יום','The first reply interprets day as that which progressively becomes light.',mode='rejected')
edge('dawn.answer',dawn,gen,'answer','2a:5','הכי קאמר למאיר ובא קראו יום')
q5=question('dark.q','2a:5','אלא מעתה ולחשך קרא לילה למחשיך ובא קרא לילה','Would parallel reasoning name the progressively darkening period night?')
dark=claim('darkhyp','2a:5','אלא מעתה ולחשך קרא לילה למחשיך ובא קרא לילה','The proposed analogy would classify the darkening period as night.',mode='rejected',conditions=['apply the first reply to the parallel clause'])
stars=claim('starslimit','2a:5','והא קיימא לן דעד צאת הכוכבים יממא הוא','It is established here that daytime lasts until the stars emerge.',conditions=['before emergence of stars'],scope='Day/night boundary cited against the first reply')
edge('dark.objection',dark,dawn,'objection','2a:5','אלא מעתה ולחשך קרא לילה למחשיך ובא קרא לילה');edge('stars.objection',stars,dark,'objection','2a:5','והא קיימא לן דעד צאת הכוכבים יממא הוא')
light=claim('lightcommand','2a:6','אלא הכי קאמר קרייה רחמנא לנהורא ופקדיה אמצותא דיממא','The revised exposition says God summoned light and assigned it daytime service.',scope='Anonymous exposition of Genesis 1:5')
night=claim('darkcommand','2a:6','וקרייה רחמנא לחשוכא ופקדיה אמצותא דלילה','God summoned darkness and assigned it nighttime service.',scope='Anonymous exposition of Genesis 1:5')
edge('light.correction',light,dawn,'correction','2a:6');edge('light.answer',light,gen,'answer','2a:6');edge('dark.distinction',night,dark,'correction','2a:6')
ps=claim('ps148','2a:7','מיתיבי (תהלים קמח, ג) הללוהו כל כוכבי אור אלמא אור אורתא הוא','The stars of אור verse is proposed as evidence that אור means night.',mode='challenged')
edge('ps148.objection',ps,initial,'objection','2a:7','מיתיבי (תהלים קמח, ג) הללוהו כל כוכבי אור אלמא אור אורתא הוא')
psr=claim('psreply','2a:7','הכי קאמר הללוהו כל כוכבים המאירים','The reply reads the phrase as all shining stars.',mode='challenged')
edge('psreply.answer',psr,ps,'answer','2a:7','הכי קאמר הללוהו כל כוכבים המאירים')
question('nonshining.q','2a:7','אלא מעתה כוכבים המאירים הוא דבעו שבוחי שאינן מאירין לא בעו שבוחי','Would only shining stars need to praise, but nonshining stars not?')
allhosts=claim('allhosts','2a:7','והא כתיב (תהלים קמח, ב) הללוהו כל צבאיו','The verse calls on all His hosts to praise, challenging an exclusive restriction to shining stars.',scope='Anonymous citation of Psalms 148:2')
edge('allhosts.objection',allhosts,psr,'objection','2a:7','אלא מעתה כוכבים המאירים הוא דבעו שבוחי שאינן מאירין לא בעו שבוחי והא כתיב (תהלים קמח, ב) הללוהו כל צבאיו')
starlight=claim('starlight','2a:8','אלא הא קמ"ל דאור דכוכבים נמי אור הוא','The phrase instead teaches that starlight also counts as light.',scope='Meaning of light for vows')
edge('starlight.answer',starlight,psr,'qualification','2a:8','אלא הא קמ"ל דאור דכוכבים נמי אור הוא')
vq=question('vow.q','2a:8','למאי נפקא מינה','What practical difference follows?')
vow=claim('vow','2a:8','לנודר מן האור (דתנן) הנודר מן האור אסור באורן של כוכבים','One who vows against light is prohibited from starlight.',conditions=['vow against light'],scope='Quoted vow rule; source prints parenthetical דתנן')
edge('vow.answer',vow,vq,'answer','2a:8','לנודר מן האור (דתנן) הנודר מן האור אסור באורן של כוכבים');edge('vow.application',starlight,vow,'support','2a:8')
ju=add('job24.u','utterances',dict(textual_voice='anonymous discussion quoting Job 24:14',discourse_role='biblical evidence introduced as objection',composition='composite'),[ev('2a:9')])
add('job24.authority','attributions',dict(surface='איוב כד, יד',role='quoted_authority',candidates=[],scope='Bibliographic source Job 24:14, not an identified human speaker',transmission_chain=[]),[ev('2a:9')],[ju])
job=claim('jobinference','2b:1','הא מדקאמר ובלילה יהי כגנב אלמא אור יממא הוא','Contrasting אור with night in Job 24:14 is offered as proof that אור means day.',mode='challenged')
edge('job.quotation',ju,job,'quotation','2a:9');edge('job.objection',job,yh,'objection','2b:1','הא מדקאמר ובלילה יהי כגנב אלמא אור יממא הוא')
sure=claim('sure','2b:1','התם הכי קאמר אי פשיטא לך מילתא כנהורא דאנפשות קאתי רוצח הוא וניתן להצילו בנפשו','If it is as clear as daylight that he comes to kill, he is a murderer and saving the threatened person by taking his life is permitted.',conditions=['clear that the intruder comes to take life'],scope='Metaphorical reading of Job 24:14')
unsure=claim('unsure','2b:1','ואי מספקא לך מילתא כליליא יהי בעיניך כגנב ולא ניתן להצילו בנפשו','If the matter is doubtful like night, regard him as a thief and do not save by taking his life.',conditions=['doubt about lethal intent'],scope='Metaphorical reading of Job 24:14')
edge('sure.answer',sure,job,'answer','2b:1');edge('unsure.distinction',unsure,sure,'distinction','2b:1')
j3=claim('job3','2b:2','מיתיבי (איוב ג, ט) יחשכו כוכבי נשפו יקו לאור ואין ואל יראה בעפעפי שחר מדקאמר יקו לאור ואין אלמא אור יממא הוא','Job 3:9 is offered as evidence that אור denotes day.',mode='challenged')
edge('job3.objection',j3,yh,'objection','2b:2')
jr=claim('job3reply','2b:2','התם מילט הוא דקא לייט ליה איוב למזליה אמר יהא רעוא דליצפיה הך גברא לנהורא ולא לישכחיה','Job is cursing his fortune: may that man look for light and not find it.',holder='איוב',scope='Job as speaker explicitly identified by the Gemara, unlike a mere book label')
edge('job3.answer',jr,j3,'answer','2b:2','התם מילט הוא דקא לייט ליה איוב למזליה אמר יהא רעוא דליצפיה הך גברא לנהורא ולא לישכחיה')
ps139=claim('ps139','2b:3','מיתיבי (תהלים קלט, יא) ואומר אך חשך ישופני ולילה אור בעדני אלמא אור יממא הוא','Psalms 139:11 is offered as evidence that אור denotes day.',mode='challenged')
edge('ps139.objection',ps139,yh,'objection','2b:3')
david=claim('david','2b:3','התם הכי קאמר דוד אני אמרתי אך חשך ישופני לעוה"ב שהוא דומה ליום עכשיו העולם הזה שהוא דומה ללילה אור בעדני','David is interpreted as saying he had feared darkness in the world to come, likened to day, but now this world, likened to night, is light around him.',holder='דוד',scope='Explicit named voice in anonymous exposition, not a lexical identification of אור with day')
edge('david.answer',david,ps139,'answer','2b:3','התם הכי קאמר דוד אני אמרתי אך חשך ישופני לעוה"ב שהוא דומה ליום עכשיו העולם הזה שהוא דומה ללילה אור בעדני')
ry=claim('rabbiyehuda','2b:4','מיתיבי ר\' יהודה אומר בודקין אור (לארבעה) עשר ובארבעה עשר שחרית ובשעת הביעור','Rabbi Yehuda lists searching on אור of the fourteenth, on its morning, and at removal time.',holder='רבי יהודה',conditions=['the fourteenth'],scope='Quoted tannaitic search schedule; not Rav Yehuda')
proof=claim('nightproof','2b:4','מדקאמר רבי יהודה בודקין אור ארבעה עשר ובארבעה עשר שחרית אלמא אור אורתא הוא ש"מ','The separate references to אור and morning establish here that אור means night.',mode='asserted')
edge('nightproof.support',ry,proof,'support','2b:4');edge('nightproof.answer',proof,q,'answer','2b:4')

notes={
'2a:1':'Reread all six legal units: timing, candlelight, place exemption, cellar precondition and two school positions; do not resolve cellar geometry from this opening.',
'2a:2':'Compared lexical glosses with original 3a:9: no Rav Huna/Rav Yehuda dispute survives; initial supposition rejected. Names remain distinct from Rabbi Yehuda in 2b:4.',
'2a:3':'Reread verse challenge, word-order rebuttal and travel maxim. Rav is holder; Rav Yehuda is transmitter. Citation is not a scholar name.',
'2a:4':'Reread comparative kaf objection and eschatological reading; rhetorical question retained.',
'2a:5':'Reread both tentative daytime interpretation and its nightfall reductio; first reply rejected by 2a:6.',
'2a:6':'Reread revised parallel assignments of light and darkness; both assertions preserved, without taking initial reply as maintained.',
'2a:7':'Reread night inference, luminous-star response and all-hosts objection. The restrictive implication is a rhetorical question, not endorsed doctrine.',
'2a:8':'Reread corrected starlight interpretation, practical question and conditional vow application.',
'2a:9':'Introductory biblical citation connects into 2b:1. The quoted discourse is retained as a composite utterance, not asserted as an independent narrator rule.',
'2b:1':'Reread day inference and two conditioned metaphorical cases; lethal and doubtful intent distinguished.',
'2b:2':'Reread day inference and curse explanation; Job speaker is explicitly identified in the Gemara.',
'2b:3':'Reread day inference and the named David exposition; this-world/world-to-come contrast retained.',
'2b:4':'Reread three search times and accepted night inference; distinguish tannaitic Rabbi Yehuda from Rav Yehuda.'}
coverage=[]
for ref,note in notes.items():
    sid=refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Layer '+layer+' read directly; '+('listed records retained.' if ids else 'no additional independent record for this layer after the stated source pass.')))
p=dict(schema_version=r.VERSION,tractate='Pesachim',owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=['pe.r001.lexical'])
out=JOB/'staging'/'opening_001.json'
r.immutable(out,r.encoded(p))
print(out)
