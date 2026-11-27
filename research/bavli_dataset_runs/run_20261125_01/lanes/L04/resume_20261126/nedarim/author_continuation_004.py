"""Manual reading of successive reports of Shmuel; discarded stages remain explicit."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r004.';a.OUTPUT='continuation_004.json'
c=a.c;q=a.q;e=a.edge
scope=['4b:'+str(i) for i in range(6,11)]+['5a:'+str(i) for i in range(1,10)]+['5b:'+str(i) for i in range(1,5)]
a.structure('formulas',scope,'Successive interpretations of Shmuel’s formulation requirement and indicative abbreviated vows')
first=c('first','4b:6','אמר שמואל  בכולן עד שיאמר שאני אוכל לך שאני טועם לך','Shmuel requires addition of the eating/tasting wording to all the listed formulations.',holder='שמואל',mode='challenged',conditions=['the Mishnah’s listed relational formulations'],scope='Initial report, subjected to successive reconstructions; do not retain intervening readings as final Shmuel positions')
bar1=c('bar1','4b:7',"מיתיבי  מודר אני ממך מופרשני ממך מרוחקני ממך ה''ז אסור",'A baraita lists מודר אני ממך, מופרשני ממך and מרוחקני ממך and states prohibition.',composition='composite',scope='Quoted three-formula group presented as an objection, independent sufficiency disputed next')
bar2=c('bar2','4b:7',"שאני אוכל לך שאני טועם לך ה''ז אסור",'The baraita then lists eating/tasting wording and separately states prohibition.',composition='composite',scope='Quoted second formula group')
combine=c('combine','4b:7',"הכי קתני  בד''א באומר שאני אוכל לך שאני טועם לך",'The reply construes the first prohibition as applying when eating/tasting wording is also said.',mode='challenged',conditions=['combined formulations'],scope='Attempted harmonization with the initial report')
e('bar1.objection',bar1,first,'objection','4b:7');e('combine.answer',combine,bar1,'answer','4b:7')
reverse=c('reverse','4b:8',"והתניא איפכא  שאני אוכל לך שאני טועם לך אסור מודרני ממך ומופרשני ממך מרוחקני ממך ה''ז אסור",'Another teaching lists the same two groups in reverse order, each with a prohibition.',composition='composite',scope='Full explicit reverse-order baraita, not an atomic substantive rule')
already=c('already','4b:8','תני הכי  וכבר אמר מודרני','The reply reads the latter group as wording already said before the eating/tasting formulation.',mode='rejected',scope='Attempted temporal reconstruction challenged immediately')
e('reverse.objection',reverse,combine,'objection','4b:8');e('already.answer',already,reverse,'answer','4b:8')
same=q('same','4b:9','אי הכי היינו רישא','If so, is this not the same as the first teaching?')
twice=q('twice','4b:9',"ועוד אסור אסור ל''ל למתני",'Why then state אסור twice?')
e('same.objection',same,already,'objection','4b:9');e('twice.objection',twice,combine,'objection','4b:9')
one=c('one','4b:10',None,'The next report of Shmuel says the eating/tasting formulation prohibits only the speaker while the other person remains permitted.',holder='שמואל',mode='rejected',conditions=['שאני אוכל לך / שאני טועם לך'],scope='Intermediate report, rejected after the Rabbi Yosei report is corrected')
both=c('both','5a:1','אבל אמר מודרני הימך לחודיה שניהן אסורין','On this intermediate reading, bare מודרני הימך prohibits both parties.',holder='שמואל',mode='rejected',conditions=['מודרני הימך alone'],scope='Continuation of intermediate Shmuel report, not ultimate ruling')
yosi=c('yosi','5a:1',"כי הא דאמר ר' יוסי בר' חנינא  מודרני הימך שניהן אסורין",'An initial report from Rabbi Yosei son of Rabbi Hanina likewise makes מודרני הימך prohibit both.',holder='ר׳ יוסי בר׳ חנינא',mode='rejected',conditions=['מודרני הימך'],scope='Report expressly corrected at5a:5')
e('one.correction',one,first,'correction','4b:10');e('yosi.support',yosi,both,'support','5a:1')
herem1=c('herem1','5a:2','תנן  הריני עליך חרם המודר אסור אבל מדיר לא','The cited Mishnah prohibits only the addressee for הריני עליך חרם.',conditions=['הריני עליך חרם'],scope='Quoted objection to mutual prohibition')
except1=c('except1','5a:2','כגון דפריש ואת עלי לא','The attempted reply limits this case to an express exclusion: ואת עלי לא.',mode='rejected',conditions=['explicit ואת עלי לא'],scope='Interim interpretation undermined by5a:4')
herem2=c('herem2','5a:3','את עלי חרם הנודר אסור אבל מודר לא','For את עלי חרם the cited rule prohibits the speaker but not the addressee.',conditions=['את עלי חרם'],scope='Second quoted objection')
except2=c('except2','5a:3','כגון דפריש ואנא עלך לא','The attempted reply limits that case to an express exclusion: ואנא עלך לא.',mode='rejected',conditions=['explicit ואנא עלך לא'],scope='Second interim interpretation undermined next')
e('herem1.objection',herem1,yosi,'objection','5a:2');e('except1.answer',except1,herem1,'answer','5a:2');e('herem2.objection',herem2,yosi,'objection','5a:3');e('except2.answer',except2,herem2,'answer','5a:3')
default=q('default','5a:4','אבל סתמא מאי שניהן אסורים','Would the unspecified formula then prohibit both?')
double=c('double','5a:4','הא מדקתני סיפא  הריני עליך ואת עלי שניהן אסורין','The later clause explicitly combines הריני עליך ואת עלי and prohibits both.',conditions=['both directions expressly included'],scope='Quoted Mishnah support for limiting mutual prohibition')
inference=c('inference','5a:4','הדין הוא דשניהם אסורין הא סתמא הוא אסור וחברו מותר','The discussion infers that mutual prohibition belongs to the express two-way formula, while the unspecified case is one-way.',conditions=['comparison with explicit two-way clause'],scope='Anonymous inference in the argument; identities governed by formula direction, not a universal independent rule')
e('double.support',double,inference,'support','5a:4');e('inference.objection',inference,except1,'objection','5a:4');e('inference.objection2',inference,except2,'objection','5a:4')
toyou=c('toyou','5a:5',"אלא הכי אתמר דר' יוסי בר' חנינא  מודר אני לך שניהם אסורין",'The corrected Rabbi Yosei son of Rabbi Hanina report makes מודר אני לך prohibit both.',holder='ר׳ יוסי בר׳ חנינא',conditions=['מודר אני לך'],scope='Corrected report distinguished from הימך')
fromyou=c('fromyou','5a:5','מודרני הימך הוא אסור וחברו מותר','The corrected report makes מודרני הימך prohibit the speaker alone.',holder='ר׳ יוסי בר׳ חנינא',conditions=['מודרני הימך'],scope='Corrected local report, not identical wording to לך')
e('fromyou.correction',fromyou,yosi,'correction','5a:5');e('toyou.distinction',toyou,fromyou,'distinction','5a:5')
conflict=q('conflict','5a:6',None,'But the Mishnah uses הימך, and the intermediate Shmuel interpretation made bare הימך prohibit both—how can that reading stand?')
e('conflict.objection',conflict,both,'objection','5a:6')
eating=c('eating','5a:7','אלא מעיקרא דשמואל הכי איתמר  טעמא דאמר שאני אוכל לך ושאני טועם לך הוא דאין הוא אסור אלא באכילה','Another reconstruction of Shmuel limits the prohibition to eating when eating/tasting wording is specified.',holder='שמואל',mode='rejected',conditions=['eating/tasting wording specified'],scope='Second intermediate reconstruction, questioned at5a:8 and replaced at5a:9')
benefit=c('benefit','5a:7','הא מודרני ממך אסור אפילו בהנאה','In that reconstruction, bare מודרני ממך would prohibit even benefit.',holder='שמואל',mode='rejected',conditions=['מודרני ממך alone'],scope='Rejected intermediate reading, not final Shmuel interpretation')
e('eating.correction',eating,one,'correction','5a:7');e('benefit.correction',benefit,both,'correction','5a:7')
wording=q('wording','5a:8',None,'If that is Shmuel’s meaning, why did he not formulate the eating-only qualification directly?')
e('wording.objection',wording,eating,'objection','5a:8')
final=c('final','5a:9','אלא הכי איתמר  טעמא דאמר שאני אוכל לך ושאני טועם לך הוא דאסור אבל אמר מודרני הימך לא משמע דאמר  אסור','The final local reconstruction requires eating/tasting wording for prohibition, because bare מודרני הימך does not clearly express prohibition.',holder='שמואל',conditions=['eating/tasting supplement versus bare relational wording'],composition='composite',scope='Final local contrast after earlier report reconstructions; restrictions explained by indicative-language discussion next')
talk=c('talk','5a:9','מאי טעמא מודר אני ממך לא משתעינא בהדך משמע','מודר אני ממך can mean that the speaker will not talk with the other person.',scope='Anonymous explanation of nondecisive language; not a categorical vow of silence')
trade=c('trade','5a:9','מופרשני ממך דלא עבידנא עמך משא ומתן משמע','מופרשני ממך can mean the speaker will not do business with the other person.',scope='Alternative natural sense showing eating prohibition is not explicit')
distance=c('distance','5a:9',"מרוחקני ממך דלא קאימנא בד' אמות דילך משמע",'מרוחקני ממך can mean the speaker will not stand within four cubits of the other person.',scope='Alternative sense, not a stand-alone general ruling')
e('final.correction',final,benefit,'correction','5a:9');e('talk.support',talk,final,'support','5a:9');e('trade.support',trade,final,'support','5a:9');e('distance.support',distance,final,'support','5a:9')
indicq=q('indicq','5b:1','לימא קסבר שמואל ידים שאין מוכיחות לא הוויין ידים','Does Shmuel therefore hold that nonindicative abbreviated formulations are ineffective?')
yehuda=c('yehuda','5b:1',"אין שמואל מוקים לה למתני' כר' יהודה דאמר  ידים שאין מוכיחות לא הוויין ידים",'The reply says yes: Shmuel places the Mishnah with Rabbi Yehuda, who rejects nonindicative abbreviated formulations.',scope='Anonymous account of Shmuel’s Mishnah interpretation; later Abaye/Rava debate separately qualified')
e('yehuda.answer',yehuda,indicq,'answer','5b:1')
get=c('get','5b:2','דתנן  גופו של גט הרי את מותרת לכל אדם','The cited Mishnah gives הרי את מותרת לכל אדם as the essential divorce formula.',scope='Quoted anonymous Mishnah position')
yg=c('yg','5b:2','רבי יהודה אומר  ודין דיהוי ליכי מינאי ספר תירוכין ואיגרת שבוקין','Rabbi Yehuda gives the additional explicit divorce wording ודין דיהוי ליכי מינאי ספר תירוכין ואיגרת שבוקין.',holder='רבי יהודה',scope='Quoted exact formulation; no invented translation-based identity of the instrument')
e('yg.support',yg,yehuda,'support','5b:2')
why=q('why','5b:3',None,'Why force the Mishnah into Rabbi Yehuda’s view rather than the sages, allowing nonindicative abbreviations?')
e('why.objection',why,yehuda,'objection','5b:3')
rq=q('rq','5b:4',"אמאי תאני שאני אוכל לך שאני טועם לך  ליתני שאני אוכל שאני טועם",'Why does the Mishnah add לך rather than use only שאני אוכל or שאני טועם?')
reason=c('reason','5b:4',None,'Rava explains Shmuel’s difficulty: the Mishnah’s extra לך shows that indicative abbreviated formulations are required.',holder='רבא',scope='Rava’s explanation of Shmuel’s interpretation, includes explicit formulation comparison; not a direct quotation of Shmuel’s reasoning',composition='composite')
e('reason.answer',reason,why,'answer','5b:4');e('reason.answer2',reason,rq,'answer','5b:4')
a.notes={
'4b:6':'Reread initial Shmuel report through5b:4 and distinguished successive discarded reconstructions.',
'4b:7':'Reread both formula lists, repeated prohibition and attempted combined-formula interpretation.',
'4b:8':'Reread reversed baraita and temporal reconstruction, challenged in next segment.',
'4b:9':'Reread and separately retained duplication and repeated-אסור questions.',
'4b:10':'Reread intermediate one-party report with5a:1 continuation; status rejected after correction.',
'5a:1':'Reread both mutual-prohibition continuation and Rabbi Yosei corroboration; both marked superseded interpretations, not erased.',
'5a:2':'Reread directional herem rule and attempted express-exclusion answer.',
'5a:3':'Reread opposite directional rule and separate express-exclusion answer.',
'5a:4':'Reread unspecified-case challenge, express two-way rule and one-way inference.',
'5a:5':'Reread corrected Rabbi Yosei report; לך and הימך never conflated.',
'5a:6':'Reread full conflict with intermediate Shmuel report; retained question rather than another endorsed position.',
'5a:7':'Reread eating-only/benefit reconstruction and ensuing rejection.',
'5a:8':'Reread formulation challenge to proposed eating-only gloss.',
'5a:9':'Reread final formulation contrast and three distinct nonprohibitory senses; comparison composite expressly qualified.',
'5b:1':'Reread anonymous inference, explicit yes and attribution to Rabbi Yehuda’s Mishnah interpretation.',
'5b:2':'Reread both divorce formulations as quoted source evidence.',
'5b:3':'Reread why-not-sages question without assigning it to a nearby named speaker.',
'5b:4':'Reread Rava’s explanation and its explicit לך wording question; narrator/Rava/Shmuel roles separated.'}
if __name__=='__main__':a.save()
