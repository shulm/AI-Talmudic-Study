"""Explicit source readings 9a:1–9b:9. No automatic extraction."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r015');a.agent_id='/root/pesachim_continuation_2'
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
refs=['9a:'+str(i) for i in range(1,12)]+['9b:'+str(i) for i in range(1,10)]
a.structure('certainty',['9a:'+str(i) for i in range(1,12)]+['9b:'+str(i) for i in range(1,5)],'Unseen animal movement, observed leaven, and uncertainty versus certainty')
a.structure('safekeep',['9b:'+str(i) for i in range(5,10)],'Keeping remaining leaven concealed: differing explanations')
mishnah=c('mishnah','9a:1','אין חוששין שמא גיררה חולדה מבית לבית וממקום למקום','The Mishnah does not require concern that a weasel dragged leaven between houses or places.',conditions=['movement merely suspected, not observed'],scope='Suspicion boundary clarified by Gemara')
endless=c('endless','9a:1','דא"כ מחצר לחצר ומעיר לעיר אין לדבר סוף','Otherwise concern would extend between courtyards and towns without end.',scope='Mishnah rationale')
e('endless.support',endless,mishnah,'support','9a:1')
seen=c('seen','9a:2','טעמ\' דלא חזינא דשקל הא חזינא דשקל חיישינן ובעי בדיקה','The discussion infers that observing the animal take leaven creates concern and requires searching.',conditions=['animal observed taking leaven'],scope='Anonymous inference')
e('seen.qualification',seen,mishnah,'qualification','9a:2')
eatenq=q('eatenq','9a:3','ואמאי נימא אכלתיה','Why not presume that it ate the leaven?')
house=c('house','9a:3','מי לא תנן מדורו\' העכו"ם טמאים וכמה ישהה במדור ויהא המדור צריך בדיקה ארבעים יום','A cited Mishnah treats gentile dwellings as impure and gives a forty-day residence threshold for investigation.',composition='composite',conditions=['forty-day residence threshold'],scope='Quoted impurity rule, not leaven-search law')
nospouse=c('nospouse','9a:4','ואע"פ שאין לו אשה','The investigation applies even if he has no wife.',conditions=['absence of wife'],scope='Continuation of quoted dwelling rule')
animals=c('animals','9a:4','וכל מקום שחולדה וחזיר יכולין להלוך א"צ בדיקה','A place accessible to a weasel or pig needs no investigation in that setting.',conditions=['animal access'],scope='Quoted impurity exception')
e('animals.support',animals,eatenq,'support','9a:4')
zeira=c('zeira','9a:5',a.refs['9a:5']['text'],'Rabbi Zeira distinguishes flesh, which the animal does not leave over, from bread, which it does leave over.',candidates=['רבי זירא'],composition='composite',conditions=['flesh versus bread'],scope='First reply to the analogy')
e('zeira.answer',zeira,eatenq,'answer','9a:5')
rava=c('rava','9a:6',a.refs['9a:6']['text'],'Rava distinguishes uncertainty whether flesh was present at all from certainty that leaven was taken: uncertain eating cannot remove established certainty.',candidates=['רבא'],composition='composite',conditions=['known taking versus uncertain original presence'],scope='Alternative certainty-based explanation')
e('rava.answer',rava,eatenq,'answer','9a:6');e('rava.distinction',rava,zeira,'distinction','9a:6')
produceq=q('produceq','9a:7','ואין ספק מוציא מידי ודאי','Does uncertainty never remove certainty in this setting?')
produce=c('produce','9a:7','והא תניא חבר שמת והניח מגורה מליאה פירות ואפילו הן בני יומן הרי הן בחזקת מתוקנין','A baraita presumes produce left by a deceased haver is tithed even if it is one day old.',conditions=['produce left by deceased haver'],scope='Quoted challenge')
tentative=c('tentative','9a:7','והא הכא דודאי טבילי הני פירי וספק מעושרין וספק לא מעושרין וקאתי ספק ומוציא מידי ודאי','The objection assumes certain untithed status and uncertain subsequent tithing.',mode='challenged',scope='Challenger characterization, not accepted final analysis')
e('produce.objection',produce,rava,'objection','9a:7');e('tentative.support',tentative,produceq,'support','9a:7')
certain=c('certain','9a:8','התם ודאי וודאי הוא דודאי מעשרי','The first reply treats this as certainty against certainty because the produce was certainly tithed.',scope='Presumptive certainty, not direct observation')
haver=c('haver','9a:8','כדר\' חנינא חוזאה דא"ר חנינא חוזאה חזקה על חבר שאין מוציא מתחת ידו דבר שאינו מתוקן','Rabbi Hanina Hozaa states the presumption that a haver does not release an untithed item from his control.',candidates=['רבי חנינא חוזאה'],scope='Quoted presumption')
e('certain.answer',certain,produceq,'answer','9a:8');e('haver.support',haver,certain,'support','9a:8')
doubt=c('doubt','9a:9',a.refs['9a:9']['text'],'An alternative reply treats both stages as uncertain because the produce may never have become subject to tithing.',scope='Explicit alternative, not combined with certainty reply')
e('doubt.answer',doubt,produceq,'answer','9a:9');e('doubt.distinction',doubt,certain,'distinction','9a:9')
oshaia=c('oshaia','9a:10',a.refs['9a:10']['text'],'Rabbi Oshaya describes bringing produce in with its chaff so that an animal may eat it exempt from tithing.',candidates=['רבי אושעיא'],conditions=['brought in with chaff','animal eating'],scope='Quoted possible exemption mechanism')
e('oshaia.support',oshaia,doubt,'support','9a:10')
pitq=q('pitq','9a:11','ואין ספק מוציא מידי ודאי','Does the certainty principle withstand the following incident?')
incident=c('incident','9a:11','והתניא אמר ר\' יהודה מעשה בשפחתו של מציק אחד ברימון שהטילה נפל לבור','Rabbi Yehuda reports an incident in Rimmon involving a tyrant’s maidservant and a fetus cast into a pit.',candidates=['רבי יהודה'],scope='Initial narrative wording, interpreted differently in the replies')
priest=c('priest','9b:1','ובא כהן והציץ בו לידע אם זכר הוא אם נקבה היא','A priest looked into the pit to determine whether it was male or female.',scope='Narrative continuation; no name supplied')
purify=c('purify','9b:1','ובא מעשה לפני חכמים וטיהרוהו מפני שחולדה וברדלס מצויין שם','The sages ruled him pure because a weasel and bardelas were present there.',candidates=['חכמים'],conditions=['animals present'],scope='Narrative ruling; ברדלס not assigned an unsupported zoological identification')
e('purify.objection',purify,rava,'objection','9b:1')
conflict=c('conflict','9b:2','והא הכא דודאי הטילה וספק גררוהו וספק לא גררוהו ההיא שעתא וקאתי ספק ומוציא מידי ודאי','The challenge characterizes casting as certain but timely animal removal as uncertain.',mode='challenged',scope='Initial description of the conflict')
like=c('like','9b:2','לא תימא שהטילה נפל לבור אלא אימא שהפילה כמין נפל לבור והוי ספק וספק','The first reply revises the narrative to something resembling a fetus, making original impurity and removal both uncertain.',scope='Explicit reinterpretation preserves the initial report')
e('like.answer',like,pitq,'answer','9b:2');e('like.correction',like,incident,'correction','9b:2')
sexq=q('sexq','9b:3','והא לידע אם זכר הוא אם נקבה היא קתני','Does the inquiry about male or female not presume an actual fetus?')
explain=c('explain','9b:3','הכי קאמר לידע אם רוח הפילה אם נפל הפילה ואם תמצא לומר נפל הפילה לידע אם זכר הוא ואם נקבה היא','The inquiry is reconstructed in stages: empty formation or fetus, and only if fetus, male or female.',composition='composite',conditions=['sex inquiry conditional on actual fetus'],scope='Reconstruction supporting first reply')
e('explain.answer',explain,sexq,'answer','9b:3')
certainremove=c('certainremove','9b:4','ואיבעית אימא התם ודאי וודאי הוא כיון דחולדה וברדלס מצויין שם ודאי גררוהו בההיא שעתא','The alternative reply treats timely removal as certain because the animals were present.',conditions=['animals present'],scope='Alternative certainty-against-certainty resolution')
e('certainremove.answer',certainremove,pitq,'answer','9b:4');e('certainremove.distinction',certainremove,like,'distinction','9b:4')
drag=c('drag','9b:4','נהי דשיורי משיירא מיגרר מיהת ודאי גררום בההיא שעתא','Even if some is left uneaten, dragging away is treated as certain at that time.',scope='Distinction between eating and removal')
variant=c('variant','9b:4','(לישנא אחרינא נהי דודאי אכלום לא אמרינן ודאי גררוהו לחורייהו אמרינן)','The parenthetical alternative wording denies certain eating but asserts certain dragging into their holes.',scope='Explicit alternate wording preserved separately')
e('drag.support',drag,certainremove,'support','9b:4');e('variant.qualification',variant,drag,'qualification','9b:4')
concealq=q('concealq','9b:5',a.refs['9b:5']['text'],'How does no concern for suspected weasel movement fit concealing remaining leaven to avoid another search?')
abaye=c('abaye','9b:6',a.refs['9b:6']['text'],'Abaye distinguishes the thirteenth, when bread is common and the weasel does not hide it, from the fourteenth, when bread is scarce and it hides it.',candidates=['אביי'],composition='composite',conditions=['thirteenth versus fourteenth','bread availability'],mode='challenged',scope='Proposed explanation challenged by Rava')
e('abaye.answer',abaye,concealq,'answer','9b:6')
prophet=q('prophet','9b:7','אמר רבא וכי חולדה נביאה היא דידעא דהאידנא ארביסר ולא אפי עד לאורתא ומשיירא ומטמרא','Rava asks whether the weasel is prophetic and knows it is the fourteenth and bread will not be baked until evening.')
for row in a.rows[-3:]:
    if row['layer']=='utterances':row['content']['textual_voice']='רבא'
    if row['layer']=='attributions':row['content'].update(surface='רבא',role='speaker',candidates=['רבא'])
e('prophet.objection',prophet,abaye,'objection','9b:7')
rava2=c('rava2','9b:7','אלא אמר רבא מה שמשייר יניחנו בצנעה שמא תטול חולדה בפנינו ויהא צריך בדיקה אחריו','Rava instead requires concealment lest the weasel take leaven before us and thereby require another search.',candidates=['רבא'],conditions=['observed taking'],scope='Replacement rationale')
e('rava2.answer',rava2,concealq,'answer','9b:7');e('rava2.correction',rava2,abaye,'correction','9b:7')
baraita=c('baraita','9b:8',a.refs['9b:8']['text'],'A supporting baraita tells one eating leaven after searching to conceal what remains lest a weasel take it before us and require another search.',conditions=['eating after search','observed taking risk'],scope='Explicit supporting baraita')
e('baraita.support',baraita,rava2,'support','9b:8')
mari=c('mari','9b:9',a.refs['9b:9']['text'],'Rav Mari explains the precaution as concern that one leave ten pieces and find nine.',candidates=['רב מרי'],conditions=['count falls from ten to nine'],scope='Additional rationale; no forced rejection or harmonization')
e('mari.answer',mari,concealq,'answer','9b:9')
a.save_window(refs,'pesachim_certainty_015.json','Read original 9a–10b before annotation; reread covered scope for observed/unobserved conditions, both certainty analyses, narrative and parenthetical version, and explicit Abaye-to-Rava correction.',expected_parent='15cf51f9628df2874af2e3b109e93a2da57f60a1e496301ac8186acdee1de0c3')
