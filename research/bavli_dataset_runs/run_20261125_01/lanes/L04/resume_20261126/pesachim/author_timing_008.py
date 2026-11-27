"""Explicit source reading 4b:8–5b:1; continuation through 6a:17 inspected."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r008');a.agent_id='/root/pesachim_continuation_2'
def c(k,ref,quote,text,**kw):
    cid=a.claim(k,ref,quote,text,**kw)
    for row in a.rows[-2:]:row['evidence']=[a.span(ref,quote)]
    return cid
def q(k,ref,quote,text):
    qid=a.question(k,ref,quote,text)
    a.rows[-1]['evidence']=[a.span(ref,quote)]
    return qid
def e(k,x,y,rel,ref):
    if rel=='answer':
        for row in a.rows:
            if row['id']==y and row['layer']=='questions':
                row['content']['answer_set_status']='partial'
                row['uncertainty']=['An actual local answer inventory is represented by linked records; no exhaustiveness or choice eligibility is claimed.']
    return a.e(k,x,y,rel,ref)
refs=['4b:'+str(i) for i in range(8,11)]+['5a:'+str(i) for i in range(1,21)]+['5b:1']
a.structure('timing',refs,'Derivations of removal before Passover: temporal readings, first-language, and tannaitic proofs')
meir=c('meir','4b:8','ר"מ אומר אוכלין כל חמש ושורפין בתחלת שש','Rabbi Meir permits eating throughout the fifth hour and requires burning at the beginning of the sixth.',candidates=['רבי מאיר'],composition='composite',conditions=['eve of Passover'],scope='Quoted Mishnah; two timed actions retained together')
yehuda=c('yehuda','4b:8',"ר' יהודה אומר אוכלין כל ארבע ותולין כל חמש ושורפין בתחלת שש",'Rabbi Yehuda permits eating throughout the fourth hour, suspends during the fifth, and burns at the beginning of the sixth.',candidates=['רבי יהודה'],composition='composite',conditions=['eve of Passover'],scope='Quoted Mishnah; three timed actions retained together')
e('timing.distinction',yehuda,meir,'distinction','4b:8')
common=c('common','4b:8','דכולי עלמא מיהא חמץ משש שעות ולמעלה אסור','The discussion states that all agree leaven is forbidden from six hours upward.',scope='Exact common time expression, contrasted with earlier rabbinic schedules')
source=q('source','4b:8','מנלן','What is the source of the common prohibition from six hours upward?')
abaye=c('abaye','4b:9','הא כיצד לרבות ארבעה עשר לביעור','Abaye reconciles the seven-day absence verse with removal on the first day by including the fourteenth for removal.',candidates=['אביי'],scope='Abaye’s juxtaposition of Exodus 12:19 and 12:15, not identification of biblical authorship')
e('abaye.answer',abaye,source,'answer','4b:9')
night=q('night','4b:10','ואימא לרבות לילי חמשה עשר לביעור','Why not interpret the extra wording as including the night of the fifteenth for removal?')
nightpremise=c('nightpremise','4b:10','דסלקא דעתך אמינא ימים כתיב ימים אין לילות לא','One might have read days as excluding nights.',mode='hypothetical',scope='Hypothesis motivating the rejected extra-night interpretation')
notneeded=c('notneeded','4b:10','ההוא לא איצטריכא ליה','An extra derivation for the night of the fifteenth is unnecessary.',scope='Reply developed by the scriptural associations in 5a:1–3')
e('night.answer',notneeded,night,'answer','4b:10')
links=c('links','5a:1','דהא איתקש השבתת שאור לאכילת חמץ ואכילת חמץ לאכילת מצה','Removal of leaven is scripturally associated with eating leaven, which is associated with eating matza.',composition='composite',scope='Two-step scriptural association supporting inclusion of night')
e('links.support',links,notneeded,'support','5a:1')
removal=c('removal','5a:2',a.refs['5a:2']['text'],'Exodus 12:19 juxtaposes absence of leaven with punishment for eating leaven, supporting the first association.',scope='Anonymous scriptural argument; the verse is evidence, not a human position holder')
matza=c('matza','5a:3',a.refs['5a:3']['text'],'Exodus 12:20 juxtaposes leaven and matza, and Exodus 12:18 places matza eating in the evening.',composition='composite',scope='Second association plus explicit evening premise')
e('removal.support',removal,links,'support','5a:2');e('matza.support',matza,links,'support','5a:3')
n14=q('n14','5a:4','ואימא לרבות ליל י"ד לביעור','Why not include the night of the fourteenth for removal?')
day=c('day','5a:4','ביום כתיב','The wording ביום specifies daytime.',scope='Reply excluding the night of the fourteenth')
e('day.answer',day,n14,'answer','5a:4')
morn=q('morn','5a:5','ואימא מצפרא','Why not require removal from the morning?')
half=c('half','5a:5','אך חלק','אך is read as dividing the day.',scope='Local interpretation giving the mid-day division')
e('half.answer',half,morn,'answer','5a:5');e('half.support',half,common,'support','5a:5')
ishmael=c('ishmael','5a:6','דבי רבי ישמעאל תנא מצינו י"ד שנקרא ראשון שנאמר (שמות יב, יח) בראשון בארבעה עשר יום לחדש','The school of Rabbi Ishmael teaches that the fourteenth is called first, citing Exodus 12:18.',candidates=['דבי רבי ישמעאל'],scope='School attribution, not an individually transmitted statement of Rabbi Ishmael')
nh=c('nh','5a:6','רב נחמן בר יצחק אמר ראשון דמעיקרא משמע דאמר קרא (איוב טו, ז) הראשון אדם תולד','Rav Nahman bar Yitzhak explains first as preceding, citing Job 15:7.',candidates=['רב נחמן בר יצחק'],scope='Lexical route for the preceding day')
e('ishmael.support',ishmael,abaye,'support','5a:6');e('nh.support',nh,abaye,'support','5a:6')
sukkah=q('sukkah','5a:7',a.refs['5a:7']['text'],'Would the same preceding-day interpretation apply to taking the species on the first day?')
e('sukkah.objection',sukkah,nh,'objection','5a:7')
seven=c('seven','5a:8',a.refs['5a:8']['text'],'The seven days of rejoicing identify first and seventh as days within the festival.',scope='Answer distinguishing the species passage')
e('seven.answer',seven,sukkah,'answer','5a:8')
parallel=q('parallel','5a:9','הכי נמי כתיב (שמות יב, טו) אך ביום הראשון תשביתו שבעת ימים מצות תאכלו','Does the removal passage not also have first together with seven days of matza?')
e('parallel.objection',parallel,seven,'objection','5a:9')
article=c('article','5a:9','אם כן נכתוב קרא ראשון הראשון למה לי שמע מינה לכדאמרן','The initial reply derives the preceding day from the extra definite article in הראשון.',mode='challenged',scope='Extra-letter account challenged in the next segments')
e('article.answer',article,parallel,'answer','5a:9')
extraq=q('extraq','5a:10','אי הכי התם נמי הראשון למה לי','If so, why is the definite article also present in the species passage?')
e('extraq.objection',extraq,article,'objection','5a:10')
restq=q('restq','5a:10','ותו התם דכתיב (ויקרא כג, לט) ביום הראשון שבתון וביום השמיני שבתון אימר ראשון דמעיקרא משמע','Would first in the festival rest verse likewise mean the preceding day?')
rest=c('rest','5a:10','שאני התם דאמר קרא וביום השמיני שבתון מה שמיני שמיני דחג אף ראשון ראשון דחג','The eighth-day rest anchors the first day as the first day of the festival.',scope='Reply about the festival-rest verse')
e('rest.answer',rest,restq,'answer','5a:10')
restarticle=q('restarticle','5a:11','הראשון למה לי','What does the definite article in the rest verse add?')
exclude=c('exclude','5a:11','למעוטי חולו של מועד','The proposed answer excludes the intermediate festival days.',mode='challenged',scope='Proposed function of the definite article')
e('exclude.answer',exclude,restarticle,'answer','5a:11')
redundant=c('redundant','5a:11','חולו של מועד מראשון ושמיני נפקא','Exclusion of intermediate days is already derived from first and eighth.',scope='Redundancy objection')
e('redundant.objection',redundant,exclude,'objection','5a:11')
vav=c('vav','5a:12',a.refs['5a:12']['text'],'The reply proposes that the connecting vav could extend the earlier matter to intermediate days, requiring an exclusion.',mode='challenged',scope='Hypothetical inclusive reading, not an accepted intermediate-day prohibition',composition='composite')
e('vav.answer',vav,redundant,'answer','5a:12')
letters=q('letters','5a:13','ולא לכתוב רחמנא לא וי"ו ולא ה"א','Why write either the vav or the definite article?')
e('letters.objection',letters,vav,'objection','5a:13')
holy=q('holy','5a:13','ותו התם דכתיב (ויקרא כג, ז) ביום הראשון מקרא קדש יהיה לכם ראשון דמעיקרא משמע','Would first in the holy convocation verse mean the preceding day?')
e('holy.objection',holy,nh,'objection','5a:13')
three=c('three','5a:14','אלא הני שלשה ראשון מיבעי ליה לכדתני דבי רבי ישמעאל','The discussion instead assigns these three occurrences of first to the teaching of the school of Rabbi Ishmael.',scope='Replacement account of the three festival occurrences; avoids a forced preceding-day interpretation')
e('three.answer',three,extraq,'answer','5a:14');e('three.answer2',three,letters,'answer','5a:14');e('three.answer3',three,holy,'answer','5a:14');e('three.correction',three,exclude,'correction','5a:14')
reward=c('reward','5a:14','דתנא דבי ר\' ישמעאל בשכר שלשה ראשון זכו לשלשה ראשון להכרית זרעו של עשו לבנין בית המקדש ולשמו של משיח','The school teaches that three firsts earned three firsts: cutting off Esau’s seed, building the Temple, and the name of the Messiah.',candidates=['דבי רבי ישמעאל'],composition='composite',scope='Aggadic reward teaching; three distinct referents retained, not a halakhic choice')
e('reward.support',reward,three,'support','5a:14')
for k,quote,text in [('esau','להכרית זרעו של עשו דכתיב (בראשית כה, כה) ויצא הראשון אדמוני כולו כאדרת שער','Genesis 25:25 supplies first for Esau’s seed.'),('temple','ולבנין בית המקדש דכתיב (ירמיהו יז, יב) כסא כבוד מרום מראשון מקום מקדשנו','Jeremiah 17:12 supplies first for the Temple.'),('messiah','ולשמו של משיח דכתיב (ישעיהו מא, כז) ראשון לציון הנה הנם','Isaiah 41:27 supplies first for the Messiah’s name.')]:
    x=c(k,'5a:15',quote,text,scope='Anonymous displayed scriptural support for the preceding school teaching');e(k+'.support',x,reward,'support','5a:15')
rava=c('rava','5a:16',a.refs['5a:16']['text'],'Rava derives that the Paschal offering must not be slaughtered while leaven remains, from Exodus 34:25.',candidates=['רבא'],scope='Alternative derivation of the removal deadline')
e('rava.answer',rava,source,'answer','5a:16')
individual=q('individual','5a:17','ואימא כל חד וחד כי שחיט','Why not apply this only when each person actually slaughters?')
time=c('time','5a:17','זמן שחיטה אמר רחמנא','The verse refers to the time for slaughtering.',scope='Common time rather than each person’s actual act')
e('time.answer',time,individual,'answer','5a:17');e('time.qualification',time,rava,'qualification','5a:17')
barq=q('barq','5a:18','מערב יום טוב או אינו אלא ביום טוב עצמו','Does removal on the first day mean before the festival or on the festival itself?')
bar=c('bar','5a:18','ת"ל לא תשחט על חמץ דם זבחי לא תשחט את הפסח ועדיין חמץ קיים דברי רבי ישמעאל','Rabbi Ishmael derives pre-festival removal from the prohibition on slaughtering the Paschal offering while leaven remains.',candidates=['רבי ישמעאל'],role='quoted_authority',scope='Quoted baraita, distinct from the earlier school report')
e('bar.answer',bar,barq,'answer','5a:18');e('bar.support',bar,rava,'support','5a:18')
akiva=c('akiva','5a:19',a.refs['5a:19']['text'],'Rabbi Akiva says the slaughter verse is unnecessary: removal cannot be on the festival because labor is prohibited and kindling is a primary labor.',candidates=['רבי עקיבא'],role='quoted_authority',composition='composite',scope='Alternative tannaitic derivation; premises interpreted by Rava in 5b:1')
e('akiva.answer',akiva,barq,'answer','5a:19');e('akiva.distinction',akiva,bar,'distinction','5a:19')
yosi=c('yosi','5a:20','רבי יוסי אומר אינו צריך הרי הוא אומר אך ביום הראשון תשביתו שאור מבתיכם מערב יום טוב או אינו אלא בי"ט תלמוד לומר אך חלק ואי ביום טוב עצמו מי שרי הא איתקש השבתת שאור לאכילת חמץ ואכילת חמץ לאכילת מצה','Rabbi Yosi uses אך to divide the day and the association of removal, leaven eating and matza eating to exclude a division within the festival day itself.',candidates=['רבי יוסי'],role='quoted_authority',composition='composite',scope='Third tannaitic derivation; internal rhetorical question is separately retained')
yq=q('yosiquestion','5a:20','ואי ביום טוב עצמו מי שרי','If the divided day were the festival itself, could any of it permit leaven?')
e('yosi.answer',yosi,barq,'answer','5a:20');e('yosi.reason',yosi,yq,'answer','5a:20');e('yosi.distinction',yosi,akiva,'distinction','5a:20')
for key,quote,text in [('burn','שמע מינה אין ביעור חמץ אלא שריפה','Rava infers from Rabbi Akiva that leaven removal requires burning.'),('division','ושמע מינה הבערה לחלק יצאת','Rava infers that the separate prohibition of kindling distinguishes labors.'),('need','ושמע מינה לא אמרינן הואיל והותרה הבערה לצורך הותרה נמי שלא לצורך','Rava infers that permission to kindle for a need is not extended to kindling without a need.')]:
    x=c(key,'5b:1',quote,text,candidates=['רבא'],naming_refs=['5a:20'],scope='Rava’s stated inference from Rabbi Akiva, not a general final ruling');e(key+'.support',akiva,x,'support','5b:1')
a.save_window(refs,'pesachim_timing_008.json','Read 4b:8–6a:17 original context, reread covered clauses for omitted proofs, challenges, reward material, and named/anonymous scope. The Rava attribution begins at 5a:20 and continues into 5b:1.',expected_parent='0e3faae411fe501c3dd3ea74d588088304ac353359690d28dd61066455942902')
