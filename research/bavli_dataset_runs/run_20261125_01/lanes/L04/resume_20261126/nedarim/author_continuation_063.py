"""Manual time-formula reading, release decree and unresolved bare-day inquiry."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r063.';a.OUTPUT='continuation_063.json'
c=a.c;e=a.edge;q=b.q
a.structure('time',['60a:'+str(i) for i in range(4,10)]+['60b:'+str(i) for i in range(1,8)],'Calendar formulas, release requirement and included boundary days')
a.structure('bareday',['60b:'+str(i) for i in range(8,12)]+['61a:1','61a:2'],'Unqualified day inquiry and two deflected proof attempts')
today=c('today','60a:4','יין שאני טועם היום אינו אסור אלא עד שתחשך','A wine-tasting vow for today lasts only until dark.',scope='Mishnah duration; additional release requirement follows')
week=c('week','60a:4','שבת זו אסור בכל השבת ושבת שעברה','This week prohibits for the whole week, including its concluding Sabbath.',composition='composite',scope='Printed ושבת שעברה interpreted as Sabbath counted with departing week, not retroactive prohibition')
month=c('month','60a:4','חדש זה אסור בכל החדש ור"ח להבא','This month prohibits for the month, while the new-moon day belongs to the coming month.',composition='composite',scope='Calendar boundary rule with later two-day-new-moon clarification')
year=c('year','60a:5','שנה זו אסור בכל השנה וראש השנה לעתיד לבא','This year prohibits for the year, while Rosh Hashana belongs to the coming year.',composition='composite',scope='Explicit year boundary')
cycle=c('cycle','60a:5','שבוע זה אסור בכל השבוע ושביעית שעברה','This seven-year cycle prohibits for the cycle, including its concluding sabbatical year.',composition='composite',scope='שבוע here seven-year cycle; seventh counted with departing cycle')
one=c('one','60a:6',None,'One day, one week, one month, one year or one seven-year cycle runs for the corresponding full interval from its starting point.',composition='composite',scope='All five explicit unit formulas contrasted with this-calendar-unit formulas')
passover=c('passover','60a:7','עד הפסח אסור עד שיגיע עד שיהא אסור עד שיצא','Until Passover ends at its arrival, while until it shall be continues until its departure.',composition='composite',scope='Two formulations and distinct endpoints')
meir=c('meir','60a:7','עד לפני הפסח רבי מאיר אומר אסור עד שיגיע','The printed Mishnah assigns Rabbi Meir the arrival endpoint for עד לפני הפסח.',holder='רבי מאיר',mode='rejected',scope='Printed assignment preserved but explicitly reversed by Rav61b4 after actual continuation reread')
yosei=c('yosei','60a:7','רבי יוסי אומר אסור עד שיצא','The printed Mishnah assigns Rabbi Yosei the departure endpoint.',holder='רבי יוסי',mode='rejected',scope='Printed assignment preserved but explicitly reversed by Rav61b4; not current final attribution')
release=c('release','60a:8','אמר רבי ירמיה לכשתחשך צריך שאלה לחכם','Rabbi Yirmeya requires release by a sage when darkness arrives.',holder='רבי ירמיה',scope='Additional requirement despite today-vow duration; later transmitter names Rav Yirmeya bar Abba differently')
why=q('why','60a:9','מאי טעמא','Why require release at darkness?')
decree=c('decree','60a:9','אמר רב יוסף גזירה היום משום יום אחד','Rav Yosef explains a decree on today because of possible confusion with one day.',holder='רב יוסף',scope='Protects full-day vow from premature release at sunset')
reverseq=q('reverseq','60b:1',None,'If so, why not decree the converse, on one day because of today?')
asymmetry=c('asymmetry','60b:2','א"ל היום ביום אחד מיחלף יום אחד בהיום לא מיחלף','The answer says today can be confused with one day, but not conversely.',composition='composite',scope='Explicit asymmetry of confusion, not a symmetric decree')
e('decree.answer',decree,why,'answer','60a:9');e('asymmetry.answer',asymmetry,reverseq,'answer','60b:2');e('release.qualification',release,today,'qualification','60a:8')
transmission=c('transmission','60b:3','אמר רבינא אמר לי מרימר הכי אמר אבוך משמיה דרב [יוסף]','Ravina reports that Merimar told him his father had transmitted in the name of Rav [Yosef].',composition='composite',scope='Full multi-step chain and bracketed Yosef retained; no father name invented')
according=q('according','60b:3','כמאן אזלא שמעתיה דרב ירמיה בר אבא','With whom does Rav Yirmeya bar Abba’s teaching accord?')
natan=c('natan','60b:3','כרבי נתן דתניא רבי נתן אומר כל הנודר כאילו בנה במה והמקיימו כאילו מקטיר עליה','The answer aligns it with Rabbi Natan, who likens vowing to building an altar and maintaining a vow to offering on it.',holder='רבי נתן',composition='composite',scope='Alignment and both repeated analogies; Rav Yirmeya bar Abba surface not silently equated with earlier רבי ירמיה')
e('natan.answer',natan,according,'answer','60b:3')
weekq=q('weekq','60b:4','פשיטא','Why need the Mishnah specify the whole week?')
weekdays=c('weekdays','60b:4','מהו דתימא יומי דשבתא קאמר קמ"ל','It excludes the proposed reading that only the weekdays were intended.',scope='Rejects Sabbath exclusion from this-week vow')
e('weekdays.answer',weekdays,weekq,'answer','60b:4');e('weekdays.qualification',weekdays,week,'qualification','60b:4')
monthq=q('monthq','60b:5','פשיטא','Why specify that the new-moon day belongs to the coming month?')
short=c('short','60b:5','כי איצטריכא לחדש חסר','The reply invokes the case printed as חדש חסר.',scope='Exact compressed calendar label retained; no silent emendation')
old=c('old','60b:6','מהו דתימא ראש חדש לשעבר הוי ולא ליתסר','One might have treated the new-moon day as belonging to the previous month and therefore not prohibited.',mode='rejected',scope='Printed proposed consequence ולא ליתסר retained without replacing it with inferred opposite')
ordinary=c('ordinary','60b:6','קמ"ל קרו אינשי ריש ירחא','The answer stresses that people call it the beginning of the month.',scope='Ordinary naming determines calendar classification')
e('short.answer',short,monthq,'answer','60b:5');e('ordinary.answer',ordinary,monthq,'answer','60b:6');e('ordinary.correction',ordinary,old,'correction','60b:6')
repeat=c('repeat','60b:7',None,'The discussion repeats that this year prohibits the whole year.',scope='Separate repeated lemma occurrence')
day=a.q('day','60b:8','איבעיא להו אמר קונם יין שאני טועם יום מאי דיניה כהיום או כיום אחד','Does an unqualified day in a wine-tasting vow mean today or one full day?')
for row in a.records:
    if row['id']==day:row['uncertainty'].append('Both ensuing proof attempts are deflected; no explicit local resolution before the jubilee inquiry.')
first=c('first','60b:9','ת"ש ממתניתין קונם יין שאני טועם היום אין אסור אלא עד שתחשך הא יום כיום אחד דמי','The first proof infers from today ending at darkness that bare day means one full day.',mode='rejected',composition='composite',scope='Quoted premise and proposed contrast defeated by opposite inference from latter clause')
second=c('second','60b:10','אימא סיפא אמר יום אחד אסור מיום ליום הא יום כהיום דמי','The counter-inference from one day running a full interval would make bare day mean today.',mode='rejected',composition='composite',scope='Opposite inference is also not accepted as resolution')
neither=c('neither','60b:10','אלא מהא ליכא למשמע מינה','The discussion concludes nothing can be inferred from this Mishnah.',scope='Explicit failure of first proof, not an answer to bare-day semantics')
e('neither.correction',neither,first,'correction','60b:10');e('neither.correction2',neither,second,'correction','60b:10')
leap=c('leap','60b:11','אמר רב אשי ת"ש קונם יין שאני טועם השנה נתעברה השנה אסור בה ובעיבורה','Rav Ashi adduces a teaching that this-year wine prohibition includes the leap extension when the year is intercalated.',holder='רב אשי',scope='Quoted second proof text, not yet proof of bare-year wording')
simpleq=q('simpleq','61a:1','אילימא כדקתני למה לי למימרא','If it literally means this year, why must the leap extension be taught?')
analogy=c('analogy','61a:1','אלא לאו דאמר שנה אלמא שנה כהשנה דמי ויום נמי כהיום דיניה','The proposed reading substitutes bare year, inferring year means this year and bare day similarly means today.',mode='rejected',composition='composite',scope='Two-step proposed analogy rejected next')
literal=c('literal','61a:2','לא לעולם דאמר השנה ומהו דתימא הלך אחר רוב השנים ולא אית בהו עיבור קא משמע לן','The reply retains this year: the novelty is to reject following the majority of years, which lack intercalation.',composition='composite',scope='Deflects year-to-day proof while retaining the literal intercalated-year rule')
e('literal.answer',literal,simpleq,'answer','61a:2');e('literal.correction',literal,analogy,'correction','61a:2')
a.notes={
'60a:4':'Reread today/week/month formulas with sunset, Sabbath and new-moon boundaries.',
'60a:5':'Reread year/Rosh Hashana and seven-year-cycle/seventh-year boundaries.',
'60a:6':'Reread all five one-unit full-interval formulas.',
'60a:7':'Reread Passover arrival/departure formulas and printed Meir/Yosei assignments; actual61b4 continuation reverses named positions, marked rejected pending explicit correction records.',
'60a:8':'Reread Rabbi Yirmeya release requirement and preserved distinct later Rav Yirmeya bar Abba surface.',
'60a:9':'Reread reason question and Yosef today/one-day confusion decree.',
'60b:1':'Reread converse-decree objection.',
'60b:2':'Reread asymmetric confusion answer.',
'60b:3':'Reread Ravina/Merimar/father/Rav [Yosef] chain, Rav Yirmeya bar Abba alignment question and Natan dual analogy.',
'60b:4':'Reread whole-week lemma, obviousness question and rejected weekdays-only reading.',
'60b:5':'Reread new-moon lemma, obviousness question and exact חדש חסר answer.',
'60b:6':'Reread printed previous-month/ולא ליתסר proposal and ordinary beginning-of-month reply without emending.',
'60b:7':'Reread whole-year repeated lemma.',
'60b:8':'Reread bare-day alternatives; subsequent proofs fail to resolve.',
'60b:9':'Reread first today-to-full-day inference as rejected.',
'60b:10':'Reread opposite latter-clause inference and explicit no-inference conclusion.',
'60b:11':'Reread Ashi literal this-year leap-extension proof and opening how-case inquiry.',
'61a:1':'Reread literal-reading obviousness objection and proposed bare-year-to-bare-day analogy.',
'61a:2':'Reread literal-this-year retention and rejected majority-nonleap presumption; day inquiry remains unresolved.'}
if __name__=='__main__':a.save()
