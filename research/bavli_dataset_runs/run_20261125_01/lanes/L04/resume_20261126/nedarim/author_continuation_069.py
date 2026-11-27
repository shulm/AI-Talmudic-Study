"""Intake121 one capped source window62b5–63b9, manual semantics."""
import author_continuation_024 as b
from pathlib import Path
import hashlib,json
a=b.a;r=a.r;HERE=Path(__file__).resolve().parent
BASE='b6421aabe6cab3ce7d705b4e1dd71fa6f1dab74a7a6122db508b95ce954e8b74'
assert r.read(a.JOB/'CURRENT.json')['snapshot_sha256']==BASE
assert r.read(a.JOB/'OWNER.json')=={'epoch':3,'owner':'L04/nedarim_resume_20261126'}
start=r.read(HERE/'START_INTAKE121_069.json')
for name,h in start['actual_nine_file_hashes'].items():assert hashlib.sha256((a.ROOT.parent/name).read_bytes()).hexdigest()==h
assert a.meta['source_sha256']==start['source_sha256']
a.records=[];a.notes={};a.PREFIX='nd.r069.';a.OUTPUT='continuation_069b.json'
c=a.c;e=a.edge;q=b.q

def quoted(key,ref,quote,text,holder=None,**kw):
    ident=c(key,ref,quote,text,holder=holder,**kw)
    if holder:next(x for x in a.records if x['id']==a.PREFIX+key+'.a')['content']['role']='quoted_authority'
    return ident

a.structure('seasons',['62b:'+str(i) for i in range(5,9)]+['63a:'+str(i) for i in range(1,6)],'Local harvest endpoints and rain formulations, objection and resolution')
a.structure('leap',['63a:'+str(i) for i in range(6,10)]+['63b:1','63b:2'],'Leap year and first/second Adar formulations, knowledge distinction')
a.structure('intent',['63b:'+str(i) for i in range(3,9)],'Contextual intention in seasonal, reciprocal-benefit and interpersonal vows')
a.structure('colophon',['63b:9'],'Printed chapter ending; no independent legal proposition')
wheat=c('wheat','62b:5','עד הקציר עד שיתחיל העם לקצור קציר חטין אבל לא קציר שעורין','Until harvest lasts until people begin harvesting wheat, not barley.',composition='composite',scope='Positive wheat endpoint and explicit exclusion of barley')
place=c('place','62b:5','הכל לפי מקום נדרו אם היה בהר בהר ואם היה בבקעה בבקעה','The endpoint follows the place of the vow: mountain if in the mountain, valley if in the valley.',composition='composite',scope='Explicit locality rule and both applications')
e('place.qualification',place,wheat,'qualification','62b:5','הכל לפי מקום נדרו')
rain=c('rain','62b:6','עד הגשמים עד שיהו הגשמים עד שתרד רביעה שניה','Until the rains or until the rains shall be lasts until the second rainfall descends.',composition='composite',scope='Two plural rain formulas; actual descent endpoint')
gamliel=quoted('gamliel','62b:6','רשב"ג אומר עד שיגיע זמנה של רביעה','Rabban Shimon ben Gamliel ends the prohibition when the rainfall’s time arrives.',holder='רשב"ג',scope='Contrasting scheduled-time endpoint under the preceding rain formulas')
nisan=quoted('nisan','62b:6',"עד שיפסקו גשמים עד שיצא ניסן כולו דברי ר' מאיר",'Rabbi Meir interprets until the rains cease as lasting through all of Nisan.',holder="ר' מאיר")
pesach=quoted('pesach','62b:6',"ר' יהודה אומר עד שיעבור הפסח",'Rabbi Yehuda ends until the rains cease when Passover passes.',holder="ר' יהודה",scope='Alternative endpoint for the same cessation formula')
e('gamliel.objection',gamliel,rain,'objection','62b:6','רשב"ג אומר עד שיגיע זמנה של רביעה');e('pesach.objection',pesach,nisan,'objection','62b:6',"ר' יהודה אומר עד שיעבור הפסח")
galilee=quoted('galilee','62b:7','תניא הנודר עד הקיץ בגליל וירד לעמקים אע"פ שהגיע הקיץ בעמקים אסור עד שיגיע הקיץ בגליל','One who vows until summer in Galilee and descends to the valleys remains prohibited until summer reaches Galilee, even if it has reached the valleys.',conditions=['vowed in Galilee','subsequently descended to valleys'],scope='Anonymous baraita confirms locality dependence despite subsequent movement')
e('galilee.support',galilee,place,'support','62b:7')
lemma=c('rainlemma','62b:8','עד הגשמים עד שיהו גשמים עד שתרד רביעה שניה רשב"ג אומר וכו\'','The discussion repeats the plural rain formulas and second-rain descent endpoint, abbreviating Gamliel’s alternative.',composition='composite',scope='Distinct repeated lemma; abbreviated alternative not reconstructed as a fresh quotation')
e('rainlemma.quotation',lemma,rain,'quotation','62b:8',"עד הגשמים עד שיהו גשמים עד שתרד רביעה שניה רשב\"ג אומר וכו'")
plural=c('plural','62b:8',"אמר ר' זירא מחלוקת דאמר עד הגשמים",'Rabbi Zeira limits the dispute to saying until the rains in the plural.',holder="ר' זירא",conditions=['עד הגשמים'])
singular=c('singular','62b:8','אבל אמר עד הגשם עד זמן גשמים קאמר','For until the rain in the singular, Zeira interprets the vow as referring to the rainfall season.',holder="ר' זירא",conditions=['עד הגשם'],scope='Contrast within Zeira’s explicitly introduced statement',extra=[('62b:8',"אמר ר' זירא")])
e('plural.qualification',plural,rain,'qualification','62b:8',"אמר ר' זירא מחלוקת דאמר עד הגשמים");e('singular.distinction',singular,plural,'distinction','62b:8','אבל אמר עד הגשם עד זמן גשמים קאמר')
timeq=q('timeq','63a:1','איזוהי זמנה של רביעה','What is the scheduled time of the rainfall?',conditions=['Quoted baraita introduced as objection'])
meir=quoted('meirtimes','63a:1','הבכירה בג\' בינונית בשבעה אפילה בעשרים ושלשה דברי רבי מאיר','Rabbi Meir gives the early, middle and late rain times as the third, seventh and twenty-third.',holder='רבי מאיר',composition='composite',scope='Three explicit dates; no month supplied in this clause')
yehuda=quoted('yehudatimes','63a:1','רבי יהודה אומר בשבעה ובשבעה עשר ובעשרים ושלשה','Rabbi Yehuda gives the corresponding three times as the seventh, seventeenth and twenty-third.',holder='רבי יהודה',composition='composite',scope='Ordered timing slots explicit in preceding clause; no speaker assignment by name order')
yosei=quoted('yoseitimes','63a:2','רבי יוסי אומר בשבעה עשר ובעשרים ושלשה ובחודש כסליו','Rabbi Yosei gives the corresponding times as the seventeenth, twenty-third and Kislev.',holder='רבי יוסי',composition='composite',scope='Printed ובחודש כסליו retained; month-start clarified only by following statement')
fast=quoted('fast','63a:2','וכן היה ר\' יוסי אומר אין היחידים מתענין עד שיגיע ר"ח כסליו','Rabbi Yosei also says individuals do not fast until the beginning of Kislev.',holder="ר' יוסי",scope='Independent fasting threshold in same quoted source')
for k,node,ref in [('meir',meir,'63a:1'),('yehuda',yehuda,'63a:1'),('yosei',yosei,'63a:2')]:e(k+'.schedule.answer',node,timeq,'answer',ref)
first=c('first','63a:3','בשלמא רביעה ראשונה לישאל','The discussion accepts the first rainfall time as relevant to requesting rain.',scope='Anonymous explanatory premise in recalled discussion')
third=c('third','63a:3','שלישית להתענות','It accepts the third rainfall time as relevant to fasting.',scope='Second explanatory premise, not a new named ruling')
secondq=q('secondq','63a:3','אלא שניה למאי','What is the second rainfall time relevant for?')
vower=c('vower','63a:3','ואמר רבי זירא לנודר','Rabbi Zeira answers that it matters for a person who vows.',holder='רבי זירא',scope='Recalled Zeira statement used in objection to preceding singular/plural distinction; scoped by63a5')
e('vower.answer',vower,secondq,'answer','63a:3','ואמר רבי זירא לנודר')
seven=quoted('seven','63a:4','רשב"ג אומר גשמים שירדו שבעה ימים זה אחר זה אתה מונה בהן רביעה ראשונה ושניה','Rabban Shimon ben Gamliel says seven consecutive days of rainfall can count as both first and second rainfall.',holder='רשב"ג',conditions=['rain for seven consecutive days'],scope='Quoted timing teaching within the recalled objection')
who=q('who','63a:4','כמאן אזלא הא דתניא','According to whom does the following teaching about seven consecutive rainy days proceed?')
whoagain=q('whoagain','63a:4',('כמאן',1),'According to whom is that seven-day teaching?',conditions=['Repeated formulation after quoting the baraita'])
yoseianswer=c('yoseianswer','63a:4','כרבי יוסי','The discussion assigns the seven-day teaching to Rabbi Yosei’s timing schedule.',scope='Anonymous identification, not an extra personal ruling attributed to Yosei')
e('yosei.answer',yoseianswer,who,'answer','63a:4','כרבי יוסי');e('yosei.again',yoseianswer,whoagain,'answer','63a:4','כרבי יוסי')
e('seven.objection',seven,singular,'objection','63a:4','רשב"ג אומר גשמים שירדו שבעה ימים זה אחר זה אתה מונה בהן רביעה ראשונה ושניה')
resolution=c('resolution','63a:5','ההוא דאמר עד הגשמים','The recalled case concerns someone who said until the rains in the plural.',scope='Anonymous answer limits the preceding objection to plural wording, preserving Zeira’s distinction')
e('resolution.answer',resolution,seven,'answer','63a:5');e('resolution.qualification',resolution,vower,'qualification','63a:5')
year=c('year','63a:6','קונם יין שאיני טועם לשנה נתעברה השנה אסור בה ובעיבורה','A vow not to taste wine for the year prohibits it throughout that year and its added intercalation if the year is intercalated.',conditions=['לשנה','year is intercalated'],scope='Wine-vow duration includes added period')
startadar=c('startadar','63a:6','עד ראש אדר עד ראש אדר הראשון','Until the beginning of Adar means until the beginning of the first Adar.',scope='Mishnah endpoint; knowledge distinction developed below')
endadar=c('endadar','63a:6','עד סוף אדר עד סוף אדר הראשון','Until the end of Adar means until the end of the first Adar.',scope='Separate ending formula; source’s first-Adar wording retained')
infer=c('infer','63a:7','אלמא סתמא דאדר דקאמר ראשון הוא','The discussion infers that unqualified Adar here means the first Adar.',scope='Anonymous inference from Mishnah, later conditioned on knowledge of leap year')
e('infer.support',startadar,infer,'support','63a:7')
assign=q('assign','63a:8',"לימא מתני' רבי יהודה היא",'Should the Mishnah therefore be identified with Rabbi Yehuda?')
meirdate=quoted('meirdate','63a:8','אדר הראשון כותב אדר הראשון אדר שני כותב אדר סתם דברי ר"מ','Rabbi Meir requires writing first Adar for the first month, but unqualified Adar for the second.',holder='ר"מ',composition='composite',scope='Document dating convention cited as basis of tentative Mishnah allocation')
yehudadate=quoted('yehudadate','63a:8',"ר' יהודה אומר אדר הראשון כותב סתם אדר שני כותב תיניין",'Rabbi Yehuda writes unqualified Adar for the first month and second for the second.',holder="ר' יהודה",composition='composite',scope='Two contrasted document labels')
e('yehudadate.support',yehudadate,assign,'support','63a:8',"ר' יהודה אומר אדר הראשון כותב סתם אדר שני כותב תיניין")
abaye=c('abaye','63a:9','אמר אביי אפילו תימא ר"מ הא דידע דמעברא שתא הא דלא ידע','Abaye allows even Rabbi Meir, distinguishing knowledge of the leap year from lack of that knowledge.',holder='אביי',composition='composite',scope='Knowledge distinction, made explicit by the following baraita and inference; no name-order attribution')
e('abaye.answer',abaye,assign,'answer','63a:9')
barfirst=quoted('barfirst','63b:1','והתניא עד ר"ח אדר עד ר"ח אדר הראשון','The supporting baraita says until the beginning of Adar means the beginning of the first Adar.',scope='Anonymous quoted occurrence distinct from Mishnah')
barsecond=quoted('barsecond','63b:1','אם היתה שנה מעוברת עד ר"ח אדר השני','It adds that if the year is intercalated the endpoint is the beginning of the second Adar.',conditions=['אם היתה שנה מעוברת'],scope='Literal conditional statement; apparent redundancy addressed in next segment')
redundancy=c('redundancy','63b:2','מכלל דרישא לאו במעוברת עסקינן','The discussion observes the implication that the initial clause would concern a non-intercalated year.',mode='challenged',scope='Problematic inference from the baraita wording, not its accepted final interpretation')
knowledge=c('knowledge','63b:2','שמע מינה הא דפשיטא ליה דמעברא שתא הא דלא ידע','The conclusion distinguishes definite knowledge of the intercalation from lack of knowledge.',composition='composite',scope='Known intercalation explains second-Adar clause; lack of knowledge explains first-Adar clause, as required by immediate conditional context',extra=[('63b:1',None)])
e('knowledge.answer',knowledge,redundancy,'answer','63b:2','שמע מינה הא דפשיטא ליה דמעברא שתא הא דלא ידע');e('knowledge.support',knowledge,abaye,'support','63b:2','שמע מינה הא דפשיטא ליה דמעברא שתא הא דלא ידע')
wine=quoted('wine','63b:3','ר\' יהודה אומר קונם יין שאיני טועם עד שיהא הפסח לא נתכוון זה אלא עד ליל פסח עד שעה שדרך בני אדם לשתות יין','Rabbi Yehuda ends a vow against wine until Passover shall be at Passover night, the customary time for drinking wine, as its intended endpoint.',holder="ר' יהודה",scope='Contextual intent limits duration; source does not extend to festival departure',composition='composite')
meat=quoted('meat','63b:4','אמר קונם בשר שאיני טועם עד שיהא הצום אינו אסור אלא עד לילי צום שלא נתכוון זה אלא עד שעה שדרך בני אדם לאכול בשר','The continuing teaching limits a meat vow until the fast shall be to the eve of the fast, the customary time for eating meat, as its intended endpoint.',holder="ר' יהודה",scope='Inherited Mishnah discourse from63b3 before new speaker ר יוסי בנו; translation retains eve wording without inventing another date',extra=[('63b:3',"ר' יהודה אומר")],composition='composite')
garlic=quoted('garlic','63b:4',"ר' יוסי בנו אומר קונם שום שאני טועם עד שתהא שבת אינו אסור אלא עד לילי שבת שלא נתכוון זה אלא עד שעה שדרך בני אדם לאכול בשום",'Rabbi Yosei his son limits a garlic vow until Sabbath shall be to Sabbath eve, the customary time to eat garlic, as its intended endpoint.',holder="ר' יוסי בנו",composition='composite',scope='Explicit new speaker; printed vow formula שאני טועם preserved in evidence')
gift=c('gift','63b:5','האומר לחבירו קונם שאני נהנה לך אם אין את בא ונוטל לבניך כור אחד של חטין ושתי חביות של יין','A person vows not to benefit from his fellow unless that fellow comes and takes a kor of wheat and two wine barrels for his children.',mode='hypothetical',conditions=['fellow is to take gifts for his own children'],scope='Exact conditional direction and quantities in hypothetical case')
release=c('release','63b:5','הרי זה יכול להפר את נדרו שלא ע"פ חכם','This vow can be released without a sage’s instruction.',conditions=['preceding gift-taking condition'],scope='Permission explained by the fellow’s following honor response; no general unilateral annulment rule')
honorq=a.q('honorq','63b:5','כלום אמרת אלא מפני כבודי','Did you say this except for my honor?',voice='hypothetical fellow')
honor=c('honor','63b:5','זהו כבודי','The fellow says this is my honor.',holder='hypothetical fellow',scope='Expressed waiver of receiving the offered gifts explains release, not independent sage ruling')
e('honor.support',honor,release,'support','63b:5','ויאמר לו כלום אמרת אלא מפני כבודי זהו כבודי')
payment=c('payment','63b:6','וכן האומר לחבירו קונם שאת נהנית לי אם אין את בא ונותן לבני כור של חטין ושתי חביות של יין','A person prohibits his fellow’s benefit from him unless the fellow gives his son a kor of wheat and two wine barrels.',mode='hypothetical',conditions=['fellow is to give gifts to the speaker’s son'],scope='Reversed benefit/gift direction, separate from previous case')
meirpay=quoted('meirpay','63b:6','ר"מ אומר אסור עד שיתן','Rabbi Meir maintains prohibition until the gift is given.',holder='ר"מ',conditions=['preceding gift-giving condition'])
sagespay=quoted('sagespay','63b:6','וחכ"א אף זה יכול להפר את נדרו שלא ע"פ חכם','The sages allow this vow too to be released without a sage’s instruction.',holder='חכמים',conditions=['preceding gift-giving condition'],scope='Release through the following deemed-receipt formula')
received=c('received','63b:6','ויאמר לו הרי אני כאילו נתקבלתי','The beneficiary says he regards himself as having received the gift.',holder='hypothetical beneficiary',scope='Deemed receipt formula in the sages’ view, not factual delivery')
e('sagespay.objection',sagespay,meirpay,'objection','63b:6','וחכ"א אף זה יכול להפר את נדרו שלא ע"פ חכם');e('received.support',received,sagespay,'support','63b:6','ויאמר לו הרי אני כאילו נתקבלתי')
niece=c('niece','63b:7','היה מסרב בו לשאת בת אחותו ואמר קונם שהיא נהנית לי לעולם','When pressed to marry his sister’s daughter, he declares she may never benefit from him.',mode='hypothetical',conditions=['pressure to marry niece'],scope='Hypothetical vow in marital context, not narrative event')
divorce=c('divorce','63b:7','וכן המגרש את אשתו אומר קונם אשתי נהנית לי לעולם','The parallel case is a divorcing husband who says his wife may never benefit from him.',mode='hypothetical',conditions=['divorce context'])
marital=c('marital','63b:7','הרי אלו מותרות להנות לו שלא נתכוון זה אלא לשום אישות','In these cases the women may benefit from him because the intended prohibition concerned marriage only.',composition='composite',conditions=['preceding niece-marriage or divorce contexts'],scope='Permission outside marital relation; intent rationale explicit')
e('marital.qualification',marital,niece,'qualification','63b:7','הרי אלו מותרות להנות לו שלא נתכוון זה אלא לשום אישות');e('divorce.qualification',marital,divorce,'qualification','63b:7','הרי אלו מותרות להנות לו שלא נתכוון זה אלא לשום אישות')
meal=c('meal','63b:8','היה מסרב בחבירו שיאכל אצלו אמר קונם לביתך שאני נכנס טיפת צונן שאני טועם לך','When a fellow presses him to eat at his home, he vows against entering the home or tasting a drop of cold water from him.',mode='hypothetical',composition='composite',conditions=['pressure to share a meal'],scope='Two explicit formulations within meal-invitation context')
water=c('water','63b:8','מותר ליכנס לביתו ולשתות ממנו צונן שלא נתכוון זה אלא לשום אכילה ושתיה','He may enter the home and drink cold water because his intended prohibition concerned the offered eating and drinking.',composition='composite',conditions=['preceding meal-invitation context'],scope='Both permissions and express intent limitation retained')
e('water.qualification',water,meal,'qualification','63b:8','מותר ליכנס לביתו ולשתות ממנו צונן שלא נתכוון זה אלא לשום אכילה ושתיה')

a.notes={
'62b:5':'Reread wheat-not-barley endpoint and mountain/valley locality conditions separately.',
'62b:6':'Reread two plural rain formulas, actual second rain versus Gamliel scheduled time, and Meir Nisan/Yehuda Passover cessation alternatives.',
'62b:7':'Reread anonymous Galilee-to-valley baraita with movement and early valley harvest conditions; no named tanna invented.',
'62b:8':'Reread repeated abbreviated lemma and Zeira plural/singular distinction; continuation through63a5.',
'63a:1':'Reread explicit timing question, all Meir/Yehuda dates, objection context; no missing month inferred.',
'63a:2':'Reread Yosei three timings and distinct individual-fasting threshold at Kislev beginning.',
'63a:3':'Reread first request/third fast premises, explicit second-time question and recalled Zeira answer.',
'63a:4':'Reread both according-to-whom question occurrences, Gamliel seven-consecutive-day condition and Yosei identification; preserve objection role.',
'63a:5':'Reread plural-form resolution limiting recalled case; no retraction of Zeira invented.',
'63a:6':'Reread wine-year intercalation and distinct beginning/end first-Adar rules.',
'63a:7':'Reread anonymous inference of unqualified first Adar.',
'63a:8':'Reread tentative Yehuda allocation question and both Meir/Yehuda document-label pairs.',
'63a:9':'Reread Abaye even-Meir answer and knowledge contrast with63b1–2, not name-order assignment.',
'63b:1':'Reread repeated first-Adar baraita and conditional second-Adar clause, preserving apparent redundancy.',
'63b:2':'Reread problematic non-leap-year implication and knowledge distinction conclusion, scope grounded in preceding conditional.',
'63b:3':'Reread Yehuda wine restriction, Passover-night endpoint and customary drinking intent rationale.',
'63b:4':'Reread inherited Yehuda meat/fast case and explicit new Yosei-son garlic/Sabbath case, both custom/intent rationales.',
'63b:5':'Reread hypothetical direction of benefit and gifts for fellow’s children, quantities, release without sage, rhetorical honor question and honor formula.',
'63b:6':'Reread reversed gift direction, quantities, Meir actual-giving condition, sages release and hypothetical deemed receipt.',
'63b:7':'Reread niece-marriage pressure and divorce as two hypothetical cases; permission limited by marital intent.',
'63b:8':'Reread meal pressure and both house/water declarations; both permissions and meal-intent explanation retained.',
'63b:9':'Reread printed chapter colophon and markup; structural ownership only, no additional legal claim/question/attribution. Next64a1 begins new chapter.'}
if __name__=='__main__':
    assert len(a.notes)==22<=30
    a.save();proposal=r.read(a.JOB/'staging'/a.OUTPUT);before=r.current(a.JOB)
    assert r.sha(r.encoded(before))==BASE
    after=r.validate_apply(before,proposal,a.ss,a.meta)
    prior={x['id']:x for x in before['records']};now={x['id']:x for x in after['records']}
    assert all(now[k]==v for k,v in prior.items())
    assert all(not x['ml_eligible'] for x in after['records'])
    oldcov={(x['segment_id'],x['layer']):x for x in before['coverage']};newcov={(x['segment_id'],x['layer']):x for x in after['coverage']}
    assert all(newcov[k]==v for k,v in oldcov.items())
    assert len(newcov)-len(oldcov)==176
    report=r.report(after,a.ss);assert set(report['completed_by_layer'].values())=={1105}
    assert set(report['next_unprocessed_by_layer'].values())=={'Nedarim 64a:1'}
    receipt=dict(status='PREVALIDATED_UNREVIEWED_CAPPED_WINDOW',base_snapshot=BASE,proposal_sha256=r.sha(r.encoded(proposal)),new_segments=22,scope=['Nedarim 62b:5','Nedarim 63b:9'],new_records=len(proposal['records']),all_prior_records_and_coverage_unchanged=True,schema_exact_source_spans_graph_closure=True,all_eight_layers=1105,next='Nedarim 64a:1',all_ml_eligible_false=True,independent_review_inherited=False,freeze_after_this_proposal=True)
    r.immutable(HERE/'PREVALIDATION_INTAKE121_069.json',r.encoded(receipt));print(json.dumps(receipt,indent=2))
