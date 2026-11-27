"""Timed consecration and redemption: continuations through Rabbi Yohanan restriction."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r028.';a.OUTPUT='continuation_028b.json'
c=a.c;q=b.q;e=a.edge
a.structure('conditional',['28a:14']+['28b:'+str(i) for i in range(1,5)],'Conditional sapling/garment consecration and danger setting')
a.structure('timed',['28b:5']+['29a:'+str(i) for i in range(1,6)]+['29b:'+str(i) for i in range(1,10)]+['30a:1','30a:2','30a:3'],'Timed sanctity, delayed consecration and redeemer identity')
ifcut=c('ifcut','28a:14','הרי נטיעות האלו קרבן אם אינן נקצצות טלית זו קרבן אם אינה נשרפת יש להן פדיון','Saplings consecrated if not cut and a garment consecrated if not burnt have redemption.',composition='composite',scope='First Mishnah case; time and danger conditions supplied below')
until=c('until','28a:14','הרי נטיעות האלו קרבן עד שיקצצו טלית זו קרבן עד שתשרף','Saplings consecrated until cut and a garment until burnt have no redemption in the Mishnah’s formulation.',extra=[('28b:1','אין להם פדיון')],composition='composite',scope='Cross-page second case; no-redemption mechanism interpreted28b:5')
wordq=q('wordq','28b:2','וליתני קדושות ואין קדושות','Why not formulate the Mishnah in terms of consecrated and not consecrated?')
style=c('style','28b:2','איידי דבעי למיתנא סיפא אין להם פדיון תנא נמי רישא יש להם פדיון','The first clause adopts redemption language to parallel the latter clause’s no-redemption wording.',scope='Editorial explanation of Mishnah diction')
e('style.answer',style,wordq,'answer','28b:2')
form=q('form','28b:3','היכי נדר','What is the form of the conditional declaration?')
ameimar=c('ameimar','28b:3','אמר אמימר באומר אם אינן נקצצות היום ועבר היום ולא נקצצו','Ameimar specifies not being cut today, with the day passing and the saplings uncut.',holder='אמימר',conditions=['explicit today deadline','day passed without cutting'])
obvious=q('obvious','28b:3','אם כן למה לי למימר פשיטא','Why must this seemingly obvious consequence be taught?')
wind=c('wind','28b:3','לא צריכא כגון דאיכא זיקא נפישא','The reply places it in a strong wind.',scope='Danger creates potential mistaken assumption about inevitable destruction')
e('ameimar.answer',ameimar,form,'answer','28b:3');e('wind.answer',wind,obvious,'answer','28b:3')
garmentq=q('garmentq','28b:4','והא קתני לה גבי טלית וטלית לשריפה קיימא','Why does the teaching likewise concern a garment: is it destined to burn?')
fire=c('fire','28b:4','[אין] כגון דאיכא דליקה','The answer supposes a fire.',scope='Printed bracketed אין retained; danger scenario')
assume=c('assume','28b:4','הכא נמי דאיכא זיקא נפישא וסלקא דעתך דמסיק אדעתיה דלא מיתנצלן ומשום הכי קא נדר קא משמע לן','Similarly strong wind may lead him to assume the saplings cannot survive and explain his declaration; the teaching rejects treating that expectation as defeating the consecration.',mode='rejected',composition='composite',scope='Rejected expectation-based exemption, not denial that a declaration was made')
e('fire.answer',fire,garmentq,'answer','28b:4')
forever=q('forever','28b:5','ולעולם','Does the no-redemption consequence last forever?')
bar=c('bar','28b:5','אמר בר פדא פדאן חוזרות וקודשות פדאן חוזרות וקודשות עד שיקצצו','Bar Padda says redemption repeatedly causes the saplings to become consecrated again until cut.',holder='בר פדא',conditions=['before cutting'],scope='Mechanism behind no lasting redemption; redeemer restricted30a:2–3')
after=c('after','28b:5','נקצצו פודן פעם אחת ודיו','Once cut, one redemption suffices.',holder='בר פדא',conditions=['after cutting'])
ulla=c('ulla','28b:5','ועולא אמר כיון שנקצצו שוב אין פודן','Ulla says that once cut they need no further redemption.',holder='עולא',conditions=['after cutting'],scope='Disagreement concerning persistence after endpoint')
e('after.answer',after,forever,'answer','28b:5');e('ulla.answer',ulla,forever,'answer','28b:5');e('ulla.objection',ulla,after,'objection','28b:5')
hamnuna=q('hamnuna','29a:1',None,'Rav Hamnuna asks where their sanctity went, comparing a marriage stated to end tomorrow that does not end without divorce.',voice='רב המנונא')
rava=c('rava','29a:2',None,'Rava distinguishes monetary consecration, which can expire by itself, from bodily sanctity, which cannot.',holder='רבא',composition='composite',scope='Proposed distinction challenged by Abaye’s sacrificial teaching')
e('rava.answer',rava,hamnuna,'answer','29a:2')
abaye=q('abaye','29a:3','אמר ליה אביי קדושת הגוף לא פקעה בכדי','Abaye asks whether bodily sanctity indeed cannot expire by itself.',voice='אביי')
ox=c('ox','29a:3','והתניא שור זה עולה כל שלושים יום ולאחר שלושים יום שלמים כל שלושים יום עולה לאחר שלושים יום שלמים','A cited teaching assigns an ox burnt-offering status for thirty days and peace-offering status thereafter.',composition='composite',scope='Declaration and reported result, type of sanctity contested')
bodilyq=q('bodilyq','29a:3','אמאי קדושת הגוף נינהו ופקעה בכדי','How does this bodily sanctity expire by itself?')
value=c('value','29a:4',None,'The reply places the declaration in consecration of the ox’s value.',scope='First answer to sacrificial-status challenge; then challenged by duplication argument')
e('value.answer',value,abaye,'answer','29a:4');e('value.answer2',value,bodilyq,'answer','29a:4')
later=c('later','29a:5','אי הכי אימא סיפא לאחר שלושים יום עולה ומעכשיו שלמים','The latter clause says burnt offering after thirty days and peace offering from now.',scope='Second cited formula introduced as challenge')
two=c('two','29a:5','אי אמרת בשלמא חדא בקדושת הגוף וחדא בקדושת דמים','If one clause concerns bodily sanctity and the other monetary consecration, both clauses have purpose.',mode='hypothetical',scope='Conditional argument completed29b:1',extra=[('29b:1',None)],composition='composite')
redundant=q('redundant','29b:2',None,'If both clauses concern monetary consecration, why repeat the easier transition from lighter to stricter sanctity after teaching the stricter-to-lighter transition?')
refute=q('refute','29b:3',None,'Should this refute Bar Padda’s view that sanctity does not expire by itself?')
pappa=c('pappa','29b:4','אמר רב פפא אמר לך בר פדא הכי קאמר אם לא אמר מעכשיו שלמים לאחר ל\' יום עולה הוי','Rav Pappa offers for Bar Padda a reading: if he did not say peace offering from now, the burnt-offering status takes effect after thirty days.',holder='רב פפא',scope='Rav Pappa’s proposed defense for Bar Padda, not direct quoted speech by Bar Padda')
e('pappa.answer',pappa,refute,'answer','29b:4');e('pappa.answer2',pappa,redundant,'answer','29b:4')
marriage=c('marriage','29b:5',None,'The analogy is delayed betrothal after thirty days, which takes effect even if the money has been consumed.',scope='Source analogy for delayed effect, not timed expiration of existing marriage')
e('marriage.analogy',marriage,pappa,'analogy','29b:5')
plain=q('plain','29b:6','פשיטא','Why is the delayed-effect rule not obvious?')
retract=c('retract','29b:6','לא צריכא דהדר ביה','The reply places it where the declarant retracts.',conditions=['retraction before delayed effect'],scope='Explains need for teaching')
e('retract.answer',retract,plain,'answer','29b:6')
school=q('school','29b:7',None,'How does this work for the view allowing retraction in delayed betrothal, as opposed to the view disallowing it?')
high=c('high','29b:8',None,'Even the view allowing retraction there distinguishes consecration: declaration to the divine is like delivery to an ordinary recipient.',scope='Different binding mechanism answers retraction objection')
e('high.answer',high,school,'answer','29b:8')
scene=c('scene','29b:9','יתיב רבי אבין ורב יצחק ברבי קמיה דרבי ירמיה וקא מנמנם רבי ירמיה','Rabbi Avin and Rav Yitzhak bar Rabbi sit before Rabbi Yirmeya while he dozes.',composition='composite',scope='Narrative setting; exact printed name form retained')
inference=c('inference','29b:9','יתבי וקאמרי לבר פדא דאמר פדאן חוזרות וקודשות','They propose that Bar Padda’s repeated consecration resolves Rav Hoshaya’s two-coin betrothal question affirmatively.',extra=[('30a:1',None)],mode='challenged',composition='composite',scope='Cross-page inference; corrected30a:2, not an accepted answer to Rav Hoshaya')
question=a.q('hoshaya','30a:1','דבעי רב הושעיא הנותן שתי פרוטות לאשה ואמר לה באחת התקדשי לי היום ובאחת התקדשי לי לאחר שאגרשיך','Rav Hoshaya asks about giving two coins, one for betrothal today and the other for betrothal after he divorces her.',voice='רב הושעיא')
next(x for x in a.records if x['id']==question)['uncertainty'].append('Only a proposed analogy and its rejection are represented here; this continuation does not supply a definitive substantive resolution of Rav Hoshaya’s question.')
wake=c('wake','30a:2','איתער בהו רבי ירמיה אמר להו מאי קא מדמיתון פדאן הוא לפדאום אחרים','Rabbi Yirmeya awakens and challenges their comparison between self-redemption and redemption by others.',scope='Narrated response rejecting equivalence')
yohanan=c('yohanan','30a:2','הכי אמר רבי יוחנן פדאן הוא חוזרות וקדושות פדאום אחרים אין חוזרות וקדושות','Rabbi Yohanan’s ruling distinguishes self-redemption, which renews sanctity, from redemption by others, which does not.',holder='רבי יוחנן',composition='composite',conditions=['identity of redeemer'],scope='Reported by Rabbi Yirmeya; restriction on Bar Padda mechanism')
woman=c('woman','30a:2','ואשה כפדאוה אחרים דמיא','A woman in the proposed analogy resembles redemption by others.',scope='Reason proposed betrothal inference does not follow')
e('yohanan.qualification',yohanan,bar,'qualification','30a:2');e('woman.correction',woman,inference,'correction','30a:2')
e('hoshaya.unresolved',woman,question,'unresolved_outcome','30a:2')
ami=c('ami','30a:3',None,'Rabbi Ami also transmits Rabbi Yohanan’s restriction to self-redemption rather than redemption by others.',holder='רבי יוחנן',composition='composite',scope='Independent confirming transmission of same distinction')
a.add('ami.chain','attributions',dict(surface='אמר רבי אמי אמר רבי יוחנן',role='transmitter',candidates=['רבי אמי'],scope=ami,transmission_chain=['רבי אמי','רבי יוחנן']),[a.ev('30a:3','אמר רבי אמי אמר רבי יוחנן')],[ami])
a.add('yirmeya.chain','attributions',dict(surface='רבי ירמיה',role='transmitter',candidates=['רבי ירמיה'],scope=yohanan,transmission_chain=['רבי ירמיה','רבי יוחנן']),[a.ev('30a:2','רבי ירמיה')],[yohanan])
e('ami.support',ami,yohanan,'support','30a:3')
a.notes={
'28a:14':'Reread paired sapling/garment cases and until-clause crossing into28b:1.',
'28b:1':'Reread no-redemption predicate attached to preceding exact Mishnah clause.',
'28b:2':'Reread wording question and parallelism explanation.',
'28b:3':'Reread Ameimar today deadline, obviousness objection and strong-wind scenario.',
'28b:4':'Reread garment/fire objection and answer, bracketed אין, and rejected inevitable-destruction inference.',
'28b:5':'Reread forever question, Bar Padda repetitive redemption and single post-cut redemption, Ulla opposition.',
'29a:1':'Reread Rav Hamnuna disappearance-of-sanctity question and marriage analogy.',
'29a:2':'Reread Rava monetary/bodily distinction and subsequent challenge.',
'29a:3':'Reread Abaye explicit question, full ox declaration/result and expiration challenge.',
'29a:4':'Reread proposed monetary-value answer, not treated as uncontested endpoint.',
'29a:5':'Reread latter formula and conditional bodily/value distinction spanning page.',
'29b:1':'Reread rationale completing the two-types hypothetical argument.',
'29b:2':'Reread redundancy challenge and strict/light direction comparison.',
'29b:3':'Reread proposed refutation of Bar Padda, answered below.',
'29b:4':'Reread Rav Pappa defense for Bar Padda with explicit absence of מעכשיו שלמים condition.',
'29b:5':'Reread delayed betrothal analogy even after money consumption.',
'29b:6':'Reread obviousness question and intervening retraction answer.',
'29b:7':'Reread anonymous alternative schools on betrothal retraction.',
'29b:8':'Reread consecration-versus-private-delivery distinction answering both-school concern.',
'29b:9':'Reread Avin/Yitzhak setting, dozing Yirmeya and cross-page proposed betrothal inference.',
'30a:1':'Reread exact two-coin Rav Hoshaya question and proposed affirmative analogy; no final answer invented.',
'30a:2':'Reread awakening, self/other redemption distinction, Yohanan report and woman analogy rejection.',
'30a:3':'Reread independent Ami-to-Yohanan confirming transmission, retained as separate occurrence.'}
if __name__=='__main__':a.save()
