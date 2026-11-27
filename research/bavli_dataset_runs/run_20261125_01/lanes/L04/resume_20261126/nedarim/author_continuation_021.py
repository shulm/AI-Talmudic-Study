"""Manual bargaining vows, Rav Asi reports, and individually preserved release narratives."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r021.';a.OUTPUT='continuation_021.json'
c=a.c;q=a.q;e=a.edge
a.structure('bargaining',['20b:14']+['21a:'+str(i) for i in range(1,8)]+['21b:1','21b:2'],'Four permitted vow categories and uncertain extended bargaining formulas')
a.structure('release',['21b:'+str(i) for i in range(3,10)]+['22a:1'],'Alternative Rav Asi reports and examples of regret/counterfactual release')
four=c('four','20b:14','נדרים התירו חכמים נדרי זרוזין ונדרי הבאי ונדרי שגגות ונדרי אונסין','The sages permit vows of urging, exaggeration, error and compulsion.',composition='composite',scope='Four named Mishnah categories; later detailed cases not invented here')
seller=c('seller','20b:14','נדרי זרוזין כיצד היה מוכר חפץ ואמר קונם שאיני פוחת לך מן הסלע','The bargaining example has a seller vow not to reduce the price below a sela.',conditions=['sale negotiation'],scope='Seller’s quoted negotiating formula')
buyer=c('buyer','20b:14','והלה אומר קונם שאיני מוסיף לך על השקל','The buyer vows not to increase above a shekel.',conditions=['same negotiation'],scope='Buyer’s contrasting negotiating formula')
three=c('three','21a:1',None,'Both want a price of three dinars.',scope='Mishnah’s stated present intent, not an inferred later change of mind')
report=c('report','21a:2','אמר ליה רבי אבא בר ממל לרבי אמי אמרת לן משמיה דרבי יהודה נשיאה מאן תנא ארבעה נדרים רבי יהודה היא','Rabbi Abba bar Mamal reminds Rabbi Ami of his report in Rabbi Yehuda Nesia’s name assigning the four-vow teaching to Rabbi Yehuda.',composition='composite',scope='Explicit nested report; Nesia and the tanna Rabbi Yehuda remain distinct labels')
a.add('nesia.chain','attributions',dict(surface='אמר ליה רבי אבא בר ממל לרבי אמי אמרת לן משמיה דרבי יהודה נשיאה',role='transmitter',candidates=['רבי אבא בר ממל','רבי אמי'],scope=report,transmission_chain=['רבי אבא בר ממל','רבי אמי','רבי יהודה נשיאה']),[a.ev('21a:2','אמר ליה רבי אבא בר ממל לרבי אמי אמרת לן משמיה דרבי יהודה נשיאה')],[report])
tarfon=c('tarfon','21a:2','דאמר משום רבי טרפון לעולם אין אחד מהן נזיר לפי שלא ניתנה נזירות אלא להפלאה','Rabbi Yehuda’s report in Rabbi Tarfon’s name requires definite articulation before any of the described parties becomes a nazirite.',holder='רבי טרפון',scope='Cited principle supporting proposed Mishnah attribution')
e('tarfon.support',tarfon,report,'support','21a:2')
rava=c('rava','21a:3',None,'Rava says the Mishnah can fit the sages: it says both want three dinars, not that they later wanted it.',holder='רבא',scope='Present-intent wording permits alternative attribution',composition='composite')
e('rava.objection',rava,report,'objection','21a:3')
extended=q('extended','21a:4',None,'Ravina asks Rav Ashi whether demanding more than a sela and offering less than a shekel creates a true vow or bargaining urging.',voice='רבינא')
invitation=c('invitation','21a:5','אמר ליה תנינא היה מסרב בחבירו שיאכל אצלו ואמר לו קונם ביתך שאני נכנס טיפת צונן שאני טועם','Rav Ashi cites a person urged to dine who vows against entering the house or tasting a drop of cold water.',composition='composite',scope='Quoted refusal example offered as analogy')
permitted=c('permitted','21a:5','מותר ליכנס לביתו ולשתות הימנו צונן שלא נתכוון זה אלא לשום אכילה ושתיה','He may enter and drink cold water because the intended refusal concerned eating and drinking a meal.',conditions=['dining invitation context'],scope='Cited contextual-intent ruling')
why=q('why','21a:6','ואמאי והא טיפת צונן קאמר','Why, when he expressly said a drop of cold water?')
idiom=c('idiom','21a:6','אלא משתעי איניש הכי הכא נמי משתעי איניש הכי','The proposed answer treats the expression as ordinary expansive speech and analogizes the bargaining wording.',mode='challenged',scope='Proposed analogy, rejected as insufficient next')
e('idiom.answer',idiom,why,'answer','21a:6');e('permitted.analogy',permitted,extended,'analogy','21a:5')
unlike=c('unlike','21a:7',None,'The reply distinguishes cold-water language because righteous people say little and do much.',extra=[('21b:1',None)],scope='Cross-page counterargument: small offered amount can mask fuller hospitality')
open=c('open','21b:2',None,'The bargaining case remains uncertain: the parties may mean a price between the endpoints or may mean the expanded statements literally; the question remains open.',mode='unresolved',composition='composite',scope='Explicit תיבעי outcome',uncertainty=['Extended bargaining formula is not resolved in this unit.'])
e('unlike.objection',unlike,idiom,'objection','21b:1');e('open.qualification',open,extended,'qualification','21b:2')
asi=c('asi','21b:3','אמר רב יהודה אמר רב אסי ארבעה נדרים הללו צריכין שאלה לחכם','Rav Asi, reported by Rav Yehuda, initially requires sage consultation for these four vow categories.',holder='רב אסי',mode='challenged',scope='Initial version disputed by Shmuel; Rav Asi is not Rav')
a.add('asi.chain','attributions',dict(surface='אמר רב יהודה אמר רב אסי',role='transmitter',candidates=['רב יהודה'],scope=asi,transmission_chain=['רב יהודה','רב אסי']),[a.ev('21b:3','אמר רב יהודה אמר רב אסי')],[asi])
shmuel=q('shmuel','21b:3','כי אמריתא קמיה דשמואל אמר תנא תני ארבעה נדרים התירו חכמים ואת אמרת צריכין שאלה לחכם','When Rav Yehuda reports it, Shmuel objects: the tanna says the sages permitted four vows, yet you require consultation?',voice='שמואל')
e('shmuel.objection',shmuel,asi,'objection','21b:3')
alt=c('alt','21b:4','רב יוסף מתני לה להא שמעתא בהאי לישנא אמר רב יהודה אמר רב אסי אין חכם רשאי להתיר אלא כעין ארבעה נדרים הללו','Rav Yosef transmits another version: Rav Asi through Rav Yehuda permits a sage to release only cases like these four vows.',holder='רב אסי',scope='Alternative report, not a second statement asserted in the same historical delivery')
a.add('alternate.chain','attributions',dict(surface='רב יוסף מתני לה להא שמעתא בהאי לישנא אמר רב יהודה אמר רב אסי',role='transmitter',candidates=['רב יוסף','רב יהודה'],scope=alt,transmission_chain=['רב יוסף','רב יהודה','רב אסי']),[a.ev('21b:4','רב יוסף מתני לה להא שמעתא בהאי לישנא אמר רב יהודה אמר רב אסי')],[alt])
regret=c('regret','21b:4','קסבר אין פותחין בחרטה','The discussion infers that this report does not allow opening release through regret alone.',scope='Local inference about alternative Rav Asi report; later ruling at22b:7 is separate')
e('alt.support',alt,regret,'support','21b:4')
hunaq=q('hunaq','21b:5','אמר ליה ליבך עלך','Rav Huna asks whether the petitioner’s original disposition remains.',voice='רב הונא')
hunar=c('hunar','21b:5','אמר ליה לא ושרייה','The petitioner says no, and Rav Huna releases him.',composition='composite',scope='Narrated answer and release, not anonymous general ruling')
e('hunar.answer',hunar,hunaq,'answer','21b:5')
rabbahq=q('rabbahq','21b:6','אמר ליה אילו היו עשרה בני אדם שיפייסוך באותה שעה מי נדרת','Rabbah bar Rav Huna asks whether he would have vowed if ten people had appeased him then.',voice='רבה בר רב הונא')
rabbahr=c('rabbahr','21b:6','אמר ליה לא והתירו','The petitioner says no, and is released.',scope='Second distinct consultation')
e('rabbahr.answer',rabbahr,rabbahq,'answer','21b:6')
yehuda=c('yehuda','21b:7','תניא רבי יהודה אומר אומרים לו לאדם לב זה עליך אם אמר לאו מתירין אותו','Rabbi Yehuda directs asking whether the same heart remains; if he says no, release is granted.',holder='רבי יהודה',conditions=['negative reply about continuing disposition'],scope='Baraita rule corresponding to first narrative')
yosei=c('yosei','21b:7','רבי ישמעאל ברבי יוסי אומר משום אביו אומרים לו לאדם אילו היו עשרה בני אדם שיפייסוך באותה שעה מי נדרת אם אמר לאו מתירין אותו','Rabbi Yishmael ben Rabbi Yosei reports his father’s ten-appeasers counterfactual, allowing release if the answer is no.',holder='רבי יוסי',conditions=['would not have vowed if ten appeasers were present'],scope='Explicit father transmission, not Yishmael as original holder')
a.add('yosei.chain','attributions',dict(surface='רבי ישמעאל ברבי יוסי אומר משום אביו',role='transmitter',candidates=['רבי ישמעאל ברבי יוסי'],scope=yosei,transmission_chain=['רבי ישמעאל ברבי יוסי','רבי יוסי']),[a.ev('21b:7','רבי ישמעאל ברבי יוסי אומר משום אביו')],[yosei])
a.speech('mnemonic',[a.ev('21b:8')],None,'printed mnemonic','composite')
asiq=q('asiq','21b:9','אמר ליה כדו תהית','Rabbi Asi addresses the petitioner with the printed question כדו תהית.',voice='רבי אסי')
asir=c('asir','21b:9','אמר ליה לא ושרייה','The printed account gives the reply לא and release.',composition='composite',scope='First narrative in segment; reply retained without emending it to yes',uncertainty=['Precise force of כדו תהית requires further philological review; source’s לא and release preserved.'])
elazarq=q('elazarq','21b:9','אמר ליה בעית נדור','Rabbi Elazar asks whether the petitioner wanted to vow.',voice='רבי אלעזר')
anger=c('anger','21b:9','אמר ליה אילו לא מרגזין לי לא בעינן כלום','The petitioner says that without others provoking him he would not have wanted any of it.',conditions=['absence of provocation'],scope='Reported counterfactual motive explicitly stated by petitioner')
release=c('release','21b:9','אמר ליה תהא כבעית','Rabbi Elazar responds תהא כבעית.',holder='רבי אלעזר',scope='Release response retained in source wording')
mother=c('mother','21b:9','ההיא איתתא דאדרתה לברתה אתאי לקמיה דרבי יוחנן','A woman who imposed a vow concerning her daughter came before Rabbi Yohanan.',scope='Third separate narrative; neither woman nor daughter named')
gossip=q('gossip','21b:9','אמר לה אילו הוה ידעת דאמרן מגירתיך עלה דברתך','Rabbi Yohanan asks whether she would have vowed had she known neighbors would attribute the vow to perceived improper conduct of her daughter.',voice='רבי יוחנן')
for ident in ['nd.r021.gossip.u','nd.r021.gossip.a','nd.r021.gossip.q']:
    next(x for x in a.records if x['id']==ident)['evidence'].append(a.ev('22a:1','אילו לא חמאת בה אימה מילין דעזיבה בכדי לא אדרתה מי אדרתה'))
noMother=c('noMother','22a:1','אמרה ליה לא ושרייה','She says no, and he releases her.',scope='Narrative reply and outcome; no finding that the daughter actually behaved improperly')
e('asir.answer',asir,asiq,'answer','21b:9');e('anger.answer',anger,elazarq,'answer','21b:9');e('noMother.answer',noMother,gossip,'answer','22a:1')
a.notes={
'20b:14':'Reread all four categories and both bargaining declarations.',
'21a:1':'Reread present common three-dinar intent, linked to next grammatical contrast.',
'21a:2':'Reread nested Abba bar Mamal/Ami/Yehuda Nesia report and separate tanna Yehuda/Tarfon principle.',
'21a:3':'Reread Rava alternative based on present רוצין, not past רצו.',
'21a:4':'Reread extended endpoint question with both alternatives.',
'21a:5':'Reread invitation-refusal case, house/water permission and stated meal-intent reason.',
'21a:6':'Reread express-drop objection and proposed idiom analogy.',
'21a:7':'Reread dialogue connector with21b:1; not a stand-alone substantive claim.',
'21b:1':'Reread small-speech/large-action distinction undermining analogy.',
'21b:2':'Reread between-endpoints/literal alternatives and תיבעי, explicitly unresolved.',
'21b:3':'Reread Rav Yehuda-to-Rav Asi chain and Shmuel challenge; no conflation with Rav.',
'21b:4':'Reread Rav Yosef alternate version, its chain and no-regret inference.',
'21b:5':'Reread Rav Huna question, negative reply and release.',
'21b:6':'Reread Rabbah bar Rav Huna ten-appeasers hypothetical and reply.',
'21b:7':'Reread both baraita rules and Yishmael’s father transmission.',
'21b:8':'Reread printed four-name mnemonic; no substantive legal claims or historical meeting fabricated.',
'21b:9':'Reread all three narratives separately, preserve unusual כדו תהית/לא reply, provocation explanation and cross-page daughter-neighbor question.',
'22a:1':'Reread completion of quoted hypothetical gossip and mother’s negative reply/release, without endorsing gossip as fact.'}
if __name__=='__main__':a.save()
