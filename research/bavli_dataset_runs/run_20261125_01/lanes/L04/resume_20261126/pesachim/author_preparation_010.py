"""Explicit source readings 6a:11–6b:11. No automatic extraction."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r010');a.agent_id='/root/pesachim_continuation_2'
def c(k,ref,quote,text,**kw):
    cid=a.claim(k,ref,quote,text,**kw)
    for row in a.rows[-2:]:row['evidence']=[a.span(ref,quote)]
    return cid
def q(k,ref,quote,text):
    qid=a.question(k,ref,quote,text);a.rows[-1]['evidence']=[a.span(ref,quote)];return qid
def e(k,x,y,rel,ref):
    if rel=='answer':
        for row in a.rows:
            if row['id']==y and row['layer']=='questions':
                row['content']['answer_set_status']='partial';row['uncertainty']=['Only actually represented local answers; no exhaustive inventory or choice eligibility.']
    return a.e(k,x,y,rel,ref)
def transmitted(k,ref,quote,text,**kw):
    x=c(k,ref,quote,text,candidates=['רב'],chain=['רב יהודה','רב'],**kw)
    a.add(k+'.transmitter','attributions',dict(surface='רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope=x,transmission_chain=['רב יהודה','רב']),[ref],[x]);return x
refs=['6a:'+str(i) for i in range(11,18)]+['6b:'+str(i) for i in range(1,12)]
a.structure('precautions',['6a:11','6a:12'],'Found leaven and leaven of others: covering, partition, and sacred-property distinctions')
a.structure('departure',['6a:'+str(i) for i in range(13,17)],'Departure and storage before Passover: thirty days and intention to return')
a.structure('study',['6a:17']+['6b:'+str(i) for i in range(1,7)],'Thirty days versus two weeks for studying Passover laws')
a.structure('order',['6b:'+str(i) for i in range(7,12)],'Chronological ordering of Torah passages and general-particular rules')
cover=transmitted('cover','6a:11','אמר רב יהודה אמר רב המוצא חמץ בביתו ביום טוב כופה עליו את הכלי','Rav, transmitted by Rav Yehuda, requires covering leaven found at home on the festival with a vessel.',conditions=['leaven found at home during the festival'],scope='Reported precaution; no invented immediate burning instruction')
sacred=c('sacred','6a:11','אמר רבא אם של הקדש הוא אינו צריך','Rava exempts sacred leaven from that covering requirement.',candidates=['רבא'],conditions=['leaven belongs to the sacred domain'],scope='Exception to vessel covering')
why=q('why','6a:11','מאי טעמא','Why is covering unnecessary for sacred leaven?')
sep=c('sep','6a:11','מיבדל בדילי מיניה','People keep apart from sacred property.',scope='Anonymous rationale for Rava’s exception')
e('sep.answer',sep,why,'answer','6a:11');e('sacred.qualification',sacred,cover,'qualification','6a:11')
wall=transmitted('wall','6a:12','ואמר רב יהודה אמר רב חמצו של נכרי עושה לו מחיצה עשרה טפחים משום היכר','Rav, transmitted by Rav Yehuda, requires a ten-handbreadth partition for gentile-owned leaven as a distinguishing marker.',conditions=['gentile-owned leaven'],scope='Physical marker requirement')
sacredwall=c('sacredwall','6a:12','ואם של הקדש הוא אינו צריך','Sacred leaven does not require that partition.',candidates=['רב'],chain=['רב יהודה','רב'],conditions=['sacred leaven'],scope='Exception continuing the transmitted statement')
whywall=q('whywall','6a:12','מאי טעמא','Why does sacred leaven not require the partition?')
separate=c('separate','6a:12','מיבדל בדילי אינשי מיניה','People keep apart from sacred property.',scope='Repeated rationale, distinct occurrence')
e('separate.answer',separate,whywall,'answer','6a:12');e('sacredwall.qualification',sacredwall,wall,'qualification','6a:12')
depart=transmitted('depart','6a:13','ואמר רב יהודה אמר רב המפרש והיוצא בשיירא קודם שלשים יום אין זקוק לבער תוך שלשים יום זקוק לבער','A sea traveler or caravan traveler leaving more than thirty days before Passover need not remove leaven; within thirty days removal is required.',composition='composite',conditions=['departure for sea travel or caravan','thirty-day threshold'],scope='Rav’s transmitted rule; return-intention qualifications debated next')
abaye=c('abaye','6a:13','אמר אביי הא דאמרת תוך שלשים יום זקוק לבער לא אמרן אלא שדעתו לחזור אבל אין דעתו לחזור אין זקוק לבער','Abaye limits the within-thirty-days requirement to someone intending to return; without that intention he exempts.',candidates=['אביי'],composition='composite',conditions=['departure within thirty days','intention to return versus no such intention'],mode='challenged',scope='Qualification challenged by Rava next')
e('abaye.qualification',abaye,depart,'qualification','6a:13')
returnq=q('returnq','6a:14','ואי דעתו לחזור אפילו מראש השנה נמי','If he intends to return, should removal not be required even from Rosh Hashana?')
for row in a.rows[-3:]:
    if row['layer']=='utterances':row['content']['textual_voice']='רבא'
    if row['layer']=='attributions':row['content'].update(surface='רבא',role='speaker',candidates=['רבא']);row['evidence'].append(a.evidence('6a:14'))
e('returnq.objection',returnq,abaye,'objection','6a:14')
rava=c('rava','6a:14','אלא אמר רבא הא דאמרת קודם שלשים יום אין זקוק לבער לא אמרן אלא שאין דעתו לחזור אבל דעתו לחזור אפילו מראש השנה זקוק לבער','Rava instead limits the pre-thirty-days exemption to one not intending to return; one intending to return requires removal even from Rosh Hashana.',candidates=['רבא'],composition='composite',conditions=['before thirty days','intention to return controls this exemption'],scope='Replacement placement of the return-intention condition')
e('rava.correction',rava,abaye,'correction','6a:14');e('rava.answer',rava,returnq,'answer','6a:14')
store=c('store','6a:15','דאמר רבא העושה ביתו אוצר קודם שלשים יום אין זקוק לבער תוך שלשים יום זקוק לבער','Rava states that making one’s house a storehouse more than thirty days before Passover exempts from removal; within thirty days removal is required.',candidates=['רבא'],composition='composite',conditions=['making the house a storehouse','thirty-day threshold'],scope='Parallel reported case')
e('store.support',store,rava,'support','6a:15')
empty=c('empty','6a:16',a.refs['6a:16']['text'],'The pre-thirty-days storehouse exemption applies only without an intention to empty it; with that intention removal is required even earlier.',composition='composite',conditions=['intention to empty the storehouse versus none'],scope='Anonymous continuation qualifying Rava’s storehouse rule; no new named holder imposed')
e('empty.qualification',empty,store,'qualification','6a:16')
thirtyq=q('thirtyq','6a:17','הני שלשים יום מאי עבידתייהו','What accounts for the thirty-day period?')
thirty=c('thirty','6a:17','כדתניא שואלין ודורשין בהלכות הפסח קודם הפסח שלשים יום','The first tanna requires inquiry and exposition of Passover laws thirty days before Passover.',conditions=['before Passover'],scope='Anonymous first opinion in quoted baraita')
two=c('two','6a:17',"ר' שמעון בן גמליאל אומר שתי שבתות",'Rabban Shimon ben Gamliel specifies two weeks.',candidates=['רבן שמעון בן גמליאל'],conditions=['before Passover'],scope='Source prints ר׳ שמעון בן גמליאל, later abbreviates רשב״ג',uncertainty=['Expanded conventional honorific is not a textual emendation; printed source surface remains in evidence.'])
# Preserve the exact printed honorific rather than silently resolving it.
for row in a.rows[-4:]:
    if row['layer']=='utterances':row['content']['textual_voice']='רבי שמעון בן גמליאל'
    if row['layer']=='attributions':row['content'].update(surface="ר' שמעון בן גמליאל",candidates=['רבי שמעון בן גמליאל'])
    if row['layer']=='positions':row['content']['holder_candidates']=['רבי שמעון בן גמליאל']
e('thirty.answer',thirty,thirtyq,'answer','6a:17');e('two.distinction',two,thirty,'distinction','6a:17')
firstq=q('firstq','6a:17','מאי טעמא דתנא קמא','What is the first tanna’s reason?')
moses=c('moses','6b:1',a.refs['6b:1']['text'],'Moses, while at the first Passover, instructs about the second Passover, supported by the Passover command and the impure persons passage.',composition='composite',scope='Anonymous argument for the thirty-day opinion, not Moses as a present disputant')
e('moses.answer',moses,firstq,'answer','6b:1')
reply=c('reply','6b:2',a.refs['6b:2']['text'],'The discussion gives Shimon ben Gamliel’s reply: while dealing with Passover matters, Moses finishes all of them.',candidates=['רבי שמעון בן גמליאל'],scope='Explicit dialectical reply אמר לך, not an independently attested direct conversation')
e('reply.objection',reply,moses,'objection','6b:2')
twoq=q('twoq','6b:3','מאי טעמא דרשב"ג','What supports Shimon ben Gamliel’s two-week view?')
month=c('month','6b:3','שהרי משה עומד בראש החדש ומזהיר על הפסח שנאמר (שמות יב, ב) החדש הזה לכם ראש חדשים וכתיב דברו אל כל עדת ישראל לאמר בעשור לחדש הזה ויקחו להם איש שה לבית אבות וגו\'','Moses is said to instruct about Passover at the start of the month, using Exodus 12 as initial proof.',mode='challenged',scope='Initial proof of a first-of-month date')
e('month.answer',month,twoq,'answer','6b:3')
dateq=q('dateq','6b:4',a.refs['6b:4']['text'],'How is the first of the month known rather than the fourth or fifth?')
e('dateq.objection',dateq,month,'objection','6b:4')
ravi=c('ravi','6b:5','אלא אמר רבה בר שימי משמיה דרבינא מהכא (במדבר ט, א) וידבר י"י אל משה במדבר סיני בשנה השנית בחדש הראשון וכתיב (במדבר ט, ב) ויעשו בני ישראל את הפסח במועדו','Rabba bar Shimi reports Ravina’s replacement proof from Numbers 9’s first-month setting and Passover command.',candidates=['רבינא'],chain=['רבה בר שימי','רבינא'],mode='challenged',scope='Reported replacement scriptural proof')
a.add('ravi.reporter','attributions',dict(surface='רבה בר שימי משמיה דרבינא',role='transmitter',candidates=['רבה בר שימי'],scope=ravi,transmission_chain=['רבה בר שימי','רבינא']),['6b:5'],[ravi])
e('ravi.answer',ravi,dateq,'answer','6b:5')
date2=q('date2','6b:5','הכא נמי ממאי דבריש ירחא קאי דילמא בארבעה בירחא או בחמשה בירחא קאי','How does this second passage establish the first rather than the fourth or fifth?')
e('date2.objection',date2,ravi,'objection','6b:5')
wilderness=c('wilderness','6b:6',a.refs['6b:6']['text'],'Rav Nahman bar Yitzhak links wilderness wording to the explicitly dated first day of the second month, deriving a first-of-month date here as well.',candidates=['רב נחמן בר יצחק'],scope='Explicit textual comparison',uncertainty=['The source prints Numbers 1:1 for both references even while comparing different month settings. Preserve printed citations; no silent bibliographic correction.'])
e('wilderness.answer',wilderness,date2,'answer','6b:6');e('wilderness.support',wilderness,ravi,'support','6b:6')
orderq=q('orderq','6b:7','וניכתוב ברישא דחדש ראשון והדר ניכתוב דחדש שני','Why not write the first-month passage before the second-month passage?')
order=c('order','6b:7','אמר רב מנשיא בר תחליפא משמיה דרב זאת אומרת אין מוקדם ומאוחר בתורה','Rav, reported by Rav Menashya bar Tahlifa, infers that Torah is not always arranged in chronological order.',candidates=['רב'],chain=['רב מנשיא בר תחליפא','רב'],scope='Ordering inference qualified by Rav Pappa below')
a.add('order.reporter','attributions',dict(surface='רב מנשיא בר תחליפא משמיה דרב',role='transmitter',candidates=['רב מנשיא בר תחליפא'],scope=order,transmission_chain=['רב מנשיא בר תחליפא','רב']),['6b:7'],[order])
e('order.answer',order,orderq,'answer','6b:7')
pappa=c('pappa','6b:8','אמר רב פפא לא אמרן אלא בתרי ענייני אבל בחד עניינא מאי דמוקדם מוקדם ומאי דמאוחר מאוחר','Rav Pappa limits nonchronological ordering to separate matters; within one matter earlier and later retain their order.',candidates=['רב פפא'],composition='composite',conditions=['distinct matters versus one matter'],scope='Explicit qualification of the ordering rule')
e('pappa.qualification',pappa,order,'qualification','6b:8')
general=c('general','6b:8','דאי לא תימא הכי כלל ופרט אין בכלל אלא מה שבפרט דילמא פרט וכלל הוא','Otherwise a general-then-particular rule could instead be particular-then-general, undermining its restrictive interpretation.',candidates=['רב פפא'],scope='Stated hermeneutic consequence of disorder within one matter')
particular=c('particular','6b:9',a.refs['6b:9']['text'],'Conversely, a particular-then-general rule that expands the particular could actually be general-then-particular.',scope='Continuation of the same argument, preserved without forcing a new speaker')
e('general.support',general,pappa,'support','6b:8');e('particular.support',particular,pappa,'support','6b:9')
remoteq=q('remoteq','6b:10',a.refs['6b:10']['text'],'Should order not matter across separate matters too, at least for the view that distant general and particular passages can be interpreted together?')
e('remoteq.objection',remoteq,pappa,'objection','6b:10')
remote=c('remote','6b:11',a.refs['6b:11']['text'],'Even the view allowing distant general-particular interpretation permits it only within one matter, not across two matters.',conditions=['same matter required despite distance'],scope='Anonymous resolution; unnamed sides not assigned identities')
e('remote.answer',remote,remoteq,'answer','6b:11')
a.save_window(refs,'pesachim_preparation_010.json','Read original through 7b:19; reread this window for all clauses, transmitter distinctions, temporal conditions, rejected date proofs and ordered-text qualification. No historical question status relabeling.',expected_parent='2ae5452dc03435b8e2f54c5215750148de56d5f05ebdb026e999c749a6349605')
