"""Explicit source readings 7a:16–7b:12. No automatic extraction."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('pesachim','Pesachim','pe.r012');a.agent_id='/root/pesachim_continuation_2'
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
refs=['7a:16']+['7b:'+str(i) for i in range(1,13)]
a.structure('form',['7a:16']+['7b:'+str(i) for i in range(1,9)],'Blessing wording for leaven removal: reported alternatives and performance examples')
a.structure('before',['7b:'+str(i) for i in range(9,13)],'Blessings before performance and the immersion exception')
bless=c('bless','7a:16','אמר רב יהודה הבודק צריך שיברך','Rav Yehuda requires the searcher to recite a blessing.',candidates=['רב יהודה'],scope='Direct attribution to Rav Yehuda, with no added Rav transmission')
what=q('what','7a:16','מאי מברך','What blessing is recited?')
pappi=c('pappi','7a:16','רב פפי אמר משמיה דרבא (אומר) לבער חמץ','Rav Pappi reports Rava’s wording לבער חמץ.',candidates=['רבא'],chain=['רב פפי','רבא'],scope='First transmitted version of Rava’s wording',uncertainty=['Conflicting reports of Rava are preserved, not two simultaneous independent choices attributed to him.'])
pappa=c('pappa','7a:16','רב פפא אמר משמיה דרבא על ביעור חמץ','Rav Pappa reports Rava’s wording על ביעור חמץ.',candidates=['רבא'],chain=['רב פפא','רבא'],scope='Second transmitted version of Rava’s wording',uncertainty=['Keep report identity separate from ultimate attributed authority.'])
for key,name,x in [('pappi','רב פפי',pappi),('pappa','רב פפא',pappa)]:a.add(key+'.reporter','attributions',dict(surface=name+' אמר משמיה דרבא',role='transmitter',candidates=[name],scope=x,transmission_chain=[name,'רבא']),['7a:16'],[x]);e(key+'.answer',x,what,'answer','7a:16')
future=c('future','7a:16','בלבער כולי עלמא לא פליגי דודאי להבא משמע','All agree that לבער has a future sense.',scope='Explicit common ground; not an unrestricted disagreement over both forms')
ambig=c('ambig','7b:1',a.refs['7b:1']['text'],'The disagreement concerns על ביעור: one reading is prior-action wording and the other allows a future sense.',composition='composite',scope='Anonymous מר סבר / מר סבר formulation retained without assigning speakers by order',uncertainty=['No name-order assignment; report wording and common ground are separately recorded.'])
e('ambig.qualification',ambig,future,'qualification','7b:1')
circum=c('circum','7b:2',a.refs['7b:2']['text'],'The circumcision blessing uses על המילה, introduced as a challenge.',scope='Quoted blessing formula challenging exclusion of על wording before an act')
e('circum.objection',circum,ambig,'objection','7b:2')
whyform=q('whyform','7b:3','התם היכי נימא','How else could the circumciser phrase the blessing?')
agent=c('agent','7b:3','נימא למול לא סגיא דלאו איהו מהיל','The reply rejects requiring למול because that wording would imply this person must perform the circumcision.',scope='Obligation-of-performer distinction for the circumcision example')
e('agent.answer',agent,whyform,'answer','7b:3');e('agent.distinction',agent,circum,'distinction','7b:3')
fatherq=q('fatherq','7b:3','אבי הבן מאי איכא למימר','What about the child’s father?')
father=c('father','7b:3','אין הכי נמי','The reply accepts the implication for the father.',conditions=['father of the child'],scope='Local concession within this dialectic; no universal final wording ruling supplied')
e('father.answer',father,fatherq,'answer','7b:3')
slaughter=c('slaughter','7b:4','מיתיבי ברוך אשר קדשנו במצותיו וצונו על השחיטה','The slaughter blessing על השחיטה is offered as another challenge.',scope='Second quoted formula')
e('slaughter.objection',slaughter,ambig,'objection','7b:4')
slaughterq=q('slaughterq','7b:4','התם נמי היכי נימא','How else could the slaughterer phrase the blessing?')
slaughterreason=c('slaughterreason','7b:4','נימא לשחוט לא סגיא דלאו איהו שחט','The reply similarly rejects requiring לשחוט because it would imply this person must slaughter.',scope='Performer-obligation distinction')
e('slaughterreason.answer',slaughterreason,slaughterq,'answer','7b:4');e('slaughterreason.distinction',slaughterreason,slaughter,'distinction','7b:4')
sacrificeq=q('sacrificeq','7b:5','פסח וקדשים מאי איכא למימר','What about Passover and other sacrificial offerings?')
sacrifice=c('sacrifice','7b:5','אין הכי נמי','The reply accepts the implication in those sacrificial cases.',conditions=['Passover and other sacrifices'],scope='Second local concession')
e('sacrifice.answer',sacrifice,sacrificeq,'answer','7b:5')
make=c('make','7b:6','מיתיבי העושה לולב לעצמו מברך שהחיינו וקימנו והגיענו לזמן הזה','The cited teaching prescribes שהחיינו when preparing a lulav for oneself.',conditions=['preparing a lulav for oneself'],scope='Quoted preparatory blessing; not inferred from later practice')
lulav=c('lulav','7b:6','נטלו לצאת בו אומר אשר קדשנו במצותיו וצונו על נטילת לולב','Taking the lulav to fulfill the commandment is accompanied by על נטילת לולב.',scope='Baraita wording offered as a challenge')
e('lulav.objection',lulav,ambig,'objection','7b:6')
already=c('already','7b:6','שאני התם דבעידנא דאגבהה נפק ביה','The reply distinguishes lulav: lifting it has already fulfilled the act.',conditions=['lulav lifted'],scope='Timing distinction in the argument')
e('already.distinction',already,lulav,'distinction','7b:6')
wordq=q('wordq','7b:7','אי הכי לצאת בו יצא בו מיבעי ליה','Should the text then say he has fulfilled rather than to fulfill?')
parallel=c('parallel','7b:7','אין הכי נמי ומשום דקא בעי למיתנא סיפא לישב בסוכה תנא רישא נמי לצאת בו','The reply accepts that and explains the wording as matching the later to-sit-in-the-sukka phrase.',scope='Textual parallelism explanation')
e('parallel.answer',parallel,wordq,'answer','7b:7')
sukkamake=c('sukkamake','7b:8',"דקתני סיפא העושה סוכה לעצמו אומר ברוך אתה ה' שהחיינו וקימנו והגיענו לזמן הזה",'The latter teaching prescribes שהחיינו upon making a sukka for oneself.',conditions=['making a sukka for oneself'],scope='Quoted parallel teaching')
sukkasit=c('sukkasit','7b:8','נכנס לישב בה אומר ברוך אשר קדשנו במצותיו וצונו לישב בסוכה','Entering to sit in the sukka is accompanied by לישב בסוכה.',conditions=['entering to sit'],scope='Quoted act blessing')
e('sukkasit.support',sukkasit,parallel,'support','7b:8')
result=c('result','7b:8','והלכתא על ביעור חמץ','The discussion explicitly rules for על ביעור חמץ.',scope='Source-explicit local ruling; no fabricated decision-maker')
e('result.resolution',result,what,'local_resolution','7b:8');e('result.answer',result,what,'answer','7b:8')
prior=c('prior','7b:9','דכולי עלמא מיהא מעיקרא בעינן לברוכי','All agree the blessing is required before the act.',scope='Common timing premise following the formula dispute')
sourceq=q('sourceq','7b:9','מנלן','What is the source for blessing before the act?')
shmuel=c('shmuel','7b:9','דאמר רב יהודה אמר שמואל כל המצות מברך עליהן עובר לעשייתן','Shmuel, transmitted by Rav Yehuda, requires blessing over commandments עובר לעשייתן.',candidates=['שמואל'],chain=['רב יהודה','שמואל'],scope='General reported principle; immersion exception follows')
a.add('shmuel.reporter','attributions',dict(surface='רב יהודה אמר שמואל',role='transmitter',candidates=['רב יהודה'],scope=shmuel,transmission_chain=['רב יהודה','שמואל']),['7b:9'],[shmuel])
e('shmuel.answer',shmuel,sourceq,'answer','7b:9')
lexq=q('lexq','7b:10','מאי משמע דהאי עובר לישנא דאקדומי הוא','How does עובר mean preceding?')
nachman=c('nachman','7b:10','אמר ר"נ בר יצחק דאמר קרא (שמואל ב יח, כג) וירץ אחימעץ דרך הככר ויעבר את הכושי','Rav Nahman bar Yitzhak cites Ahimaatz passing the Cushite as evidence for preceding.',candidates=['רב נחמן בר יצחק'],scope='Lexical proof from II Samuel 18:23, not attribution of that verse to the amora')
abaye=c('abaye','7b:10','אביי אמר מהכא (בראשית לג, ג) והוא עבר לפניהם','Abaye cites he passed before them as an alternative proof.',candidates=['אביי'],scope='Lexical proof from Genesis 33:3')
alt=c('alt','7b:10','ואבע"א מהכא (מיכה ב, יג) ויעבר מלכם לפניהם וה\' בראשם','An alternative proof cites their king passing before them and the Lord at their head.',scope='Anonymous alternative introduced by ואבע״א; not automatically assigned to Abaye')
for k,x in [('nachman',nachman),('abaye',abaye),('alt',alt)]:e(k+'.answer',x,lexq,'answer','7b:10')
exceptions=c('exceptions','7b:11','בי רב אמרי חוץ מן הטבילה ושופר','The school of Rav reports immersion and shofar as exceptions.',candidates=['בי רב'],composition='composite',mode='challenged',scope='Initial two-exception report, corrected below')
e('exceptions.qualification',exceptions,shmuel,'qualification','7b:11')
unfit=c('unfit','7b:11','בשלמא טבילה דאכתי גברא לא חזי','Immersion is understandable because the person is not yet fit.',conditions=['before immersion'],scope='Anonymous explanation without added identity restrictions')
shofarq=q('shofarq','7b:11','אלא שופר מ"ט','Why would shofar be an exception?')
failed=c('failed','7b:11','וכי תימא משום דילמא מיקלקלא תקיעה','One might explain it by possible failure of the blast.',mode='hypothetical',scope='Suggested reason rejected by comparison')
comparison=q('comparison','7b:11','אי הכי אפילו שחיטה ומילה נמי','Would that concern not also apply to slaughter and circumcision?')
e('comparison.objection',comparison,failed,'objection','7b:11')
hisda=c('hisda','7b:12','אלא אמר רב חסדא חוץ מן הטבילה בלבד איתמר','Rav Hisda corrects the report: only immersion was stated as an exception.',candidates=['רב חסדא'],scope='Explicit report correction, not merely another side')
e('hisda.correction',hisda,exceptions,'correction','7b:12');e('hisda.answer',hisda,shofarq,'answer','7b:12')
immersed=c('immersed','7b:12','תניא נמי הכי טבל ועלה בעלייתו אומר ברוך אשר קדשנו במצותיו וצונו על הטבילה','A supporting baraita prescribes על הטבילה upon emerging after immersion.',conditions=['after immersion and emergence'],scope='Explicit supporting teaching')
e('immersed.support',immersed,hisda,'support','7b:12')
a.save_window(refs,'pesachim_blessings_012.json','Reread original 7a:16–7b:12 and following candlelight context. Preserve report/holder roles, common ground, unnamed alternatives, local concessions, source-explicit ruling, and correction of the exception list.',expected_parent='92d796386663a2c15778cc4ea147f6429a92e47ef7b177cf20a4f62eeda84f36')
