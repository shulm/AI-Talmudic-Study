"""Manual reading of agent consultation, vegetable/meat categories and qualifications."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r056.';a.OUTPUT='continuation_056.json'
c=a.c;e=a.edge;q=b.q
a.structure('agent',['54a:'+str(i) for i in range(1,8)]+['54b:1'],'Vegetable vow and consultation criterion versus agent authorization')
a.structure('meat',['54b:'+str(i) for i in range(2,7)],'Meat-category dispute and local dietary qualifications')
permit=c('permit','54a:1','מן הירק מותר בדלועין','The anonymous Mishnah permits gourds under a vegetable vow.',scope='Ordinary vegetable formula subsequently qualified')
akiva=c('akiva','54a:1','ורבי עקיבא אוסר','Rabbi Akiva prohibits gourds.',holder='רבי עקיבא',scope='Explicit disagreement on preceding vow')
agentq=q('agentq','54a:1','אמרו לו לרבי עקיבא והלא אומר אדם לשלוחו קח לי ירק והוא אומר לא מצאתי אלא דלועין','The respondents challenge Akiva: does an agent sent for vegetables not report finding only gourds?')
legumes=c('legumes','54a:2','אמר להם כן הדבר או שמא אומר הוא לא מצאתי אלא קיטנית אלא שהדלועין בכלל ירק וקיטנית אינו בכלל ירק','Akiva accepts the report but contrasts legumes, which the agent would not suggest: gourds belong to vegetables and legumes do not.',holder='רבי עקיבא',composition='composite',scope='Counterexample and two category memberships in explicit reply')
bean=c('bean','54a:2','ואסור בפול המצרי לח ומותר ביבש','The vegetable vow prohibits moist Egyptian beans and permits dry ones.',composition='composite',scope='Mishnah’s separate moisture distinction; no unmarked extension of named attribution')
e('akiva.objection',akiva,permit,'objection','54a:1');e('legumes.answer',legumes,agentq,'answer','54a:2')
vegq=q('vegq','54a:3','והא מן ירק נדר','But he vowed against vegetables; why include gourds?')
ulla=c('ulla','54a:3','אמר עולא באומר ירקי קדירה עלי','Ulla construes the vow as pot vegetables upon me.',holder='עולא',scope='First narrowing of vow formula, refined next')
potq=q('potq','54a:3','ודילמא ירק הנאכל בקדרה קאמר','Could this mean vegetables eaten in a pot?')
cooked=c('cooked','54a:3','באומר ירק המתבשל בקדרה עלי','The final construction specifies vegetables cooked in a pot upon me.',scope='Refinement from eaten-in to cooked-in wording')
e('ulla.answer',ulla,vegq,'answer','54a:3');e('cooked.answer',cooked,potq,'answer','54a:3');e('cooked.qualification',cooked,ulla,'qualification','54a:3')
dispute=q('dispute','54a:4','במאי קא מיפלגי','What is the basis of the disagreement?')
rabbis=c('rabbis','54a:4','רבנן סברי כל מילתא דצריך שליחא לאמלוכי עלה לאו מיניה הוא','The sages hold that something requiring an agent to consult is not included in the category.',holder='רבנן',scope='Category rule explains gourd permission')
criterion=c('criterion','54a:4','ורבי עקיבא סבר כל מילתא דמימליך שליחא עלה מיניה הוא','Rabbi Akiva holds that an alternative about which an agent consults belongs to the category.',holder='רבי עקיבא',scope='Contrary category criterion, not automatic authorization to substitute')
lashes=c('lashes','54a:4','אמר אביי מודה רבי עקיבא לענין מלקות שאינו לוקה','Abaye says Akiva concedes there are no lashes.',holder='אביי',scope='Explicit punishment limitation despite prohibition')
e('rabbis.answer',rabbis,dispute,'answer','54a:4');e('criterion.answer',criterion,dispute,'answer','54a:4');e('lashes.qualification',lashes,akiva,'qualification','54a:4')
mission=c('mission','54a:5','תנן התם השליח שעשה שליחותו בעל הבית מעל לא עשה שליחותו שליח מעל','The cited Mishnah assigns misuse liability to the principal when an agent fulfills the mission and to the agent when he does not.',composition='composite',scope='Two mission-compliance cases in sacrificial-property misuse context')
tannaq=q('tannaq','54a:6','מאן תנא','Which tanna taught the agency rule?')
hisda=c('hisda','54a:6','אמר רב חסדא מתניתין דלא כרבי עקיבא','Rav Hisda says this Mishnah does not follow Rabbi Akiva.',holder='רב חסדא',mode='challenged',scope='Attribution exclusion explicitly challenged by Abaye’s alternative')
liver=c('liver','54a:6','דתנן כיצד אמר לו תן בשר לאורחים ונתן להם כבד תן כבד ונתן להם בשר השליח מעל','The Mishnah makes the agent liable when he supplies liver instead of requested meat, or meat instead of requested liver.',composition='composite',scope='Both substitution directions explicitly quoted')
ob=q('ob','54a:6','ואי רבי עקיבא הא א"ר עקיבא כל מילתא דמימליך עלה שליח מיניה הוא למעול בעל הבית ולא למעול שליח','If Akiva includes consultation alternatives in the category, why would the principal not be liable instead of the agent?',voice='רב חסדא')
abaye=c('abaye','54a:7','אמר אביי אפילו תימא רבי עקיבא','Abaye says the Mishnah can follow Rabbi Akiva.',holder='אביי',scope='Alternative attribution preserving agent liability')
consult=c('consult','54b:1','מי לא מודה רבי עקיבא דצריך אימלוכי','Abaye’s reply is that Akiva still requires the agent to consult.',holder='אביי',scope='Cross-folio explanation: category inclusion does not erase consultation requirement',extra=[('54a:7','אמר אביי אפילו תימא רבי עקיבא')])
rava=c('rava','54b:1','איתמר שמעתא קמיה דרבא אמר להון שפיר אמר נחמני','When told the teaching, Rava approves Nahmani’s statement.',holder='רבא',scope='Explicit approval of preceding Abaye explanation; Nahmani alias preserved in quoted wording')
e('hisda.answer',hisda,tannaq,'answer','54a:6');e('abaye.answer',abaye,tannaq,'answer','54a:7');e('abaye.objection',abaye,hisda,'objection','54a:7');e('consult.answer',consult,ob,'answer','54b:1');e('rava.support',rava,consult,'support','54b:1')
opponentq=q('opponentq','54b:2','מאן תנא דפליג עליה דרבי עקיבא','Which tanna disputes Rabbi Akiva?')
gamliel=c('gamliel','54b:2','רבן שמעון בן גמליאל היא','The answer identifies Rabban Shimon ben Gamliel.',scope='Named identification of category-dispute opponent')
included=c('included','54b:2','דתניא הנודר מן הבשר אסור בכל מיני בשר ואסור בראש וברגלים ובקנה ובכבד ובלב ובעופות','The anonymous baraita includes all meat types plus head, feet, windpipe, liver, heart and fowl in a meat vow.',composition='composite',scope='All six explicitly listed supplementary categories retained')
fish=c('fish','54b:2','ומותר בבשר דגים וחגבים','It permits fish and locust meat.',composition='composite',scope='Two exclusions requiring later context qualifications')
other=c('other','54b:3','רשב"ג אומר הנודר מן הבשר אסור בכל מיני בשר ומותר בראש וברגלים ובקנה ובכבד ובלב ובעופות ואין צריך לומר בשר דגים וחגבים','Rabban Shimon ben Gamliel prohibits meat types but permits head, feet, windpipe, liver, heart and fowl, and certainly fish and locusts.',holder='רשב"ג',composition='composite',scope='Full contrasting category inventory; all explicit exclusions retained')
offal=c('offal','54b:3','וכן היה רשב"ג אומר קרביים לאו בשר ואוכליהן לאו בר אינש','He also says entrails are not meat and disparages their eaters.',holder='רשב"ג',composition='composite',scope='Attributed polemic immediately limited by explanatory gloss')
buy=c('buy','54b:3','אוכליהן כבשר לענין זביני לאו בר אינש','The gloss limits the criticism to purchasing entrails as though they were meat.',scope='Price/purchase qualification of polemic, not condemnation of every eater')
e('gamliel.answer',gamliel,opponentq,'answer','54b:2');e('other.objection',other,included,'objection','54b:3');e('buy.qualification',buy,offal,'qualification','54b:3')
fishq=q('fishq','54b:4',None,'If fowl is included because an agent consults about it, why is fish not likewise included as a proposed substitute?')
blood=c('blood','54b:5','אמר אביי כגון שהקיז דם דלא אכיל דגים','Abaye construes the case as someone who underwent bloodletting and does not eat fish.',holder='אביי',scope='Historical dietary premise narrowing vow context, not contemporary advice')
birdq=q('birdq','54b:5','אי הכי אפילו עופות נמי לא אכיל','Then would he not also avoid fowl?')
shmuel=c('shmuel','54b:5','דאמר שמואל דמסוכר ואכיל בישרא דצפרא פרח לביה כצפרא','Shmuel is cited warning that a bloodlet person eating fowl has his heart flutter like a bird.',holder='שמואל',scope='Ancient attributed medical warning, not validated clinical guidance')
pre=c('pre','54b:5','ותניא אין מקיזין לא על דגים ולא על עופות ולא על בשר מליח','A baraita prohibits bloodletting after fish, fowl or salted meat.',composition='composite',scope='Three historical dietary conditions in cited objection')
post=c('post','54b:5','ותניא הקיז דם לא יאכל לא חלב ולא גבינה ולא ביצים ולא שחליים ולא עופות ולא בשר מליח','Another baraita lists milk, cheese, eggs, cress, fowl and salted meat as foods not eaten after bloodletting.',composition='composite',scope='All six source-listed foods, historical medical claim only')
boil=c('boil','54b:5','שאני עופות דאפשר על ידי שליקה','The reply distinguishes fowl because thorough boiling is possible.',scope='Local answer preserves fowl as potential food within bloodletting construction')
e('blood.answer',blood,fishq,'answer','54b:5');e('boil.answer',boil,birdq,'answer','54b:5');e('shmuel.support',shmuel,birdq,'support','54b:5');e('post.support',post,birdq,'support','54b:5')
eyes=c('eyes','54b:6','אביי אמר כגון דכייבין ליה עיניה דדגים קשין לעינים','Abaye alternatively construes the case as eye pain, on the premise that fish are harmful to the eyes.',holder='אביי',scope='Alternative historical dietary context; both source attributions to Abaye retained')
eyeq=q('eyeq','54b:6','אי הכי אכיל דגים דהא אמר שמואל נו"ן סמ"ך עי"ן נונא סמא לעינים','But Shmuel’s mnemonic says fish are medicine for the eyes; should he not eat them?')
end=c('end','54b:6','ההוא סוף אוכלא','The reply limits that beneficial claim to the end of the meal.',scope='Timing qualification of cited Shmuel medical claim, not clinical advice')
e('eyes.answer',eyes,fishq,'answer','54b:6');e('end.answer',end,eyeq,'answer','54b:6')
a.notes={
'54a:1':'Reread gourd dispute and respondents exact agent-report challenge.',
'54a:2':'Reread Akiva legume counterexample, two category memberships and wet/dry Egyptian-bean rule.',
'54a:3':'Reread vegetable objection and successive pot/eaten/cooked formula refinements.',
'54a:4':'Reread both consultation criteria and Abaye no-lashes concession.',
'54a:5':'Reread principal/agent misuse liability conditioned on mission compliance.',
'54a:6':'Reread Hisda attribution exclusion, both liver/meat substitutions and objection to Akiva attribution.',
'54a:7':'Reread Abaye contrary attribution continuing next folio.',
'54b:1':'Reread consultation still required and Rava explicit approval of Nahmani.',
'54b:2':'Reread named opponent question/answer and every anonymous meat inclusion/exclusion.',
'54b:3':'Reread Gamliel full contrary inventory and purchase-qualified entrails polemic.',
'54b:4':'Reread fish-versus-fowl agent-consultation objection.',
'54b:5':'Reread bloodletting construction, fowl objection, Shmuel warning, both complete food lists and boiling reply.',
'54b:6':'Reread second Abaye eye-pain construction, Shmuel mnemonic objection and end-of-meal limitation.'}
if __name__=='__main__':a.save()
