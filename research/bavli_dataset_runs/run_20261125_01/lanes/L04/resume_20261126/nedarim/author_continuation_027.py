"""Compulsion, conditional forfeiture and constrained declarations to coercers."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r027.';a.OUTPUT='continuation_027b.json'
c=a.c;q=b.q;e=a.edge
a.structure('compulsion',['27a:'+str(i) for i in range(5,10)]+['27b:'+str(i) for i in range(1,9)],'Compulsion, expected impediments and conditional forfeiture')
a.structure('coercers',['27b:9']+['28a:'+str(i) for i in range(1,14)],'Declarations under coercion, tax collectors and two readings of oath teaching')
meal=c('meal','27a:5','הדירו חבירו שיאכל אצלו וחלה הוא או שחלה בנו או שעכבו נהר הרי אלו נדרי אונסין','The Mishnah classifies a meal vow prevented by illness of the person or his son, or by a river, as a compulsion vow.',composition='composite',conditions=['one of three listed impediments'],scope='Repeated Mishnah occurrence retained')
deposit=c('deposit','27a:6','ההוא גברא דאתפיס זכוותא בבי דינא ואמר אי לא אתינא עד תלתין יומין ליבטלון הני זכוותאי','A man deposits his rights documentation in court and stipulates its cancellation if he does not come within thirty days.',composition='composite',scope='Narrative conditional forfeiture; exact זכוותא retained without inventing document contents')
prevented=c('prevented','27a:6','איתניס ולא אתא','He is prevented by compulsion and does not come.',scope='Source explicitly supplies compulsion, without its type')
huna=c('huna','27a:6','אמר רב הונא בטיל זכוותיה','Rav Huna declares his rights canceled.',holder='רב הונא',scope='Local ruling challenged by Rava')
rava=c('rava','27a:7',None,'Rava objects that he was compelled and Scripture exempts the compelled person, citing ולנערה לא תעשה דבר.',holder='רבא',scope='Source’s analogy from biblical case')
capital=c('capital','27a:8','וכי תימא קטלא שאני','One might distinguish the biblical case as capital punishment.',mode='hypothetical',scope='Anticipated reply, not final distinction')
vowproof=c('vowproof','27a:8','והתנן נדרי אונסין הדירו חבירו שיאכל אצלו וחלה הוא או שחלה בנו או שעיכבו נהר הרי אלו נדרי אונסין','The Mishnah’s meal-vow impediments are cited to show compulsion also matters beyond capital punishment.',composition='composite',scope='Repeated quotation supplies analogy')
e('rava.objection',rava,huna,'objection','27a:7');e('vowproof.support',vowproof,rava,'support','27a:8')
deathq=q('deathq','27a:9','ולרבא מאי שנא מהא דתנן הרי זה גיטיך מעכשיו אם לא באתי מכאן עד י"ב חדש ומת בתוך י"ב חדש הרי זה גט אמאי והא מינס איתניס','How does Rava distinguish a divorce effective now if he fails to return within twelve months, which stands even when he dies during that period?')
death=c('death','27b:1',None,'The possible distinction is that, knowing he would die, he would have resolved to give the divorce immediately.',mode='hypothetical',scope='Tentative דלמא distinction begun at27a:9, not an unqualified rule about all compulsion')
e('death.answer',death,deathq,'answer','27b:1')
ferry=c('ferry','27b:2','מאי שנא מההוא דאמר להו אי לא אתינא מכאן עד תלתין יומין ליהוי גיטא אתא ופסקיה מעברא אמר להו חזו דאתאי חזו דאתאי','A further comparison concerns a thirty-day return condition: a ferry prevents arrival and he calls out that he has come.',composition='composite',scope='Narrative premises of objection, repeated cry retained')
shmuel=c('shmuel','27b:2','ואמר שמואל לא שמיה מתייא','Shmuel rules that this does not count as arrival.',holder='שמואל',scope='Reported ruling in ferry case, no Rav/Shmuel dispute inferred')
ferryq=q('ferryq','27b:2','אמאי והא מינס אניס','Why does that failure count when he was compelled?')
foresee=c('foresee','27b:3',None,'The reply suggests that foreseeable compulsion differs, and the ferry impediment is foreseeable.',mode='hypothetical',scope='Explicit דלמא distinction')
e('foresee.answer',foresee,ferryq,'answer','27b:3')
asmq=q('asmq','27b:4','ולרב הונא מכדי אסמכתא היא ואסמכתא לא קניא','For Rav Huna, why does this conditional undertaking bind when an asmakhta does not acquire?')
held=c('held','27b:4','שאני הכא דמיתפסן זכותן','The first answer distinguishes the case because the rights documentation is deposited.',mode='challenged',scope='First distinction tested immediately below')
e('held.answer',held,asmq,'answer','27b:4')
deposq=q('deposq','27b:5','והיכא דמיתפסין לאו אסמכתא היא','Does deposit remove the asmakhta problem?')
debt=c('debt','27b:5',"והתנן מי שפרע מקצת חובו והשליש את שטרו ואמר אם אין אני נותן לו מכאן עד ל' יום תן לו שטרו",'The objection cites partial repayment with a debt note in third-party custody, to be handed over if the balance is not paid within thirty days.',composition='composite',scope='Counterexample to deposit alone sufficing')
yosei=c('yosei','27b:6','הגיע זמן ולא נתן רבי יוסי אומר יתן','Rabbi Yosei requires handing over the note when the deadline passes unpaid.',holder='רבי יוסי',conditions=['deadline passed without payment'])
yehuda=c('yehuda','27b:6','ורבי יהודה אומר לא יתן','Rabbi Yehuda says not to hand it over.',holder='רבי יהודה',scope='Same deposited-note case')
rav=c('rav','27b:6','ואמר רב נחמן אמר רבה בר אבוה אמר רב אין הלכה כרבי יוסי דאמר אסמכתא קניא','Rav, transmitted by Rabbah bar Avuha through Rav Nahman, rules against Rabbi Yosei’s position that asmakhta acquires.',holder='רב',scope='Explicit transmission distinguishes Rav from transmitters')
a.add('rav.chain','attributions',dict(surface='אמר רב נחמן אמר רבה בר אבוה אמר רב',role='transmitter',candidates=['רב נחמן','רבה בר אבוה'],scope=rav,transmission_chain=['רב נחמן','רבה בר אבוה','רב']),[a.ev('27b:6','אמר רב נחמן אמר רבה בר אבוה אמר רב')],[rav])
cancel=c('cancel','27b:7',None,'The reply distinguishes an explicit cancellation of his rights.',scope='Specific forfeiture wording, beyond merely depositing the document')
final=c('final','27b:8',None,'The final local rule allows asmakhta to acquire provided there was no compulsion and the undertaking was acquired from him before a significant court.',composition='composite',conditions=['not compelled','formal acquisition before בית דין חשוב'],scope='Both express qualifications required; does not preserve Rav Huna’s compelled-case result without qualification')
e('yehuda.objection',yehuda,yosei,'objection','27b:6');e('rav.support',rav,deposq,'support','27b:6');e('cancel.answer',cancel,deposq,'answer','27b:7');e('final.qualification',final,huna,'qualification','27b:8')
coerce=c('coerce','27b:9','נודרין להרגין ולחרמין ולמוכסין שהיא תרומה  אף על פי שאינו תרומה שהן של בית המלך אף על פי שאינן של בית המלך','The Mishnah allows declarations to violent coercers, seizure agents and tax collectors claiming produce is teruma or royal property even when it is not.',composition='composite',scope='Coercion setting; tax-collector scope narrowed28a:5, not permission concerning every tax levy')
bs=c('bs','27b:9','בית שמאי אומרים בכל נודרין','Beit Shammai permit vow forms but exclude an oath.',holder='בית שמאי',extra=[('28a:1','חוץ מבשבועה')],scope='Sentence crosses page boundary')
bh=c('bh','28a:1','ובית הלל אומרים אף בשבועה','Beit Hillel also allow an oath.',holder='בית הלל',scope='Mishnah’s coercion case')
bsOpen=c('bsOpen','28a:2','בית שמאי אומרים לא יפתח לו בנדר','Beit Shammai prohibit initiating the vow.',holder='בית שמאי')
bhOpen=c('bhOpen','28a:2','ובית הלל אומרים אף יפתח לו','Beit Hillel allow initiating it.',holder='בית הלל')
bsExtra=c('bsExtra','28a:2','בית שמאי אומרים במה שהוא מדירו','Beit Shammai limit allowance to what the coercer demands.',holder='בית שמאי')
bhExtra=c('bhExtra','28a:2','ובית הלל אומרים אף במה שאינו מדירו','Beit Hillel also allow adding what the coercer did not demand.',holder='בית הלל')
example=c('example','28a:3','כיצד אמר לו אמור קונם אשתי נהנית לי ואמר קונם אשתי ובני נהנין לי','The example adds sons to a demanded wife-benefit vow.',scope='Mishnah illustrates excess wording under coercion')
bsFamily=c('bsFamily','28a:3','בית שמאי אומרים אשתו מותרת ובניו אסורין','Beit Shammai permit the wife but prohibit the sons.',holder='בית שמאי',composition='composite',conditions=['sons added to demanded wife vow'])
bhFamily=c('bhFamily','28a:3','ובית הלל אומרים אלו ואלו מותרין','Beit Hillel permit wife and sons.',holder='בית הלל',conditions=['same excess declaration'])
for key,x,y,ref in [('oath',bh,bs,'28a:1'),('open',bhOpen,bsOpen,'28a:2'),('extra',bhExtra,bsExtra,'28a:2'),('family',bhFamily,bsFamily,'28a:3')]:e(key+'.objection',x,y,'objection',ref)
lawq=q('lawq','28a:4',None,'How does the tax-collector allowance fit Shmuel’s rule that the kingdom’s law is law?')
law=c('law','28a:4','דינא דמלכותא דינא','Shmuel’s principle is that the kingdom’s law is law.',holder='שמואל',scope='Quoted principle generating objection to undifferentiated tax-collector reading')
unfixed=c('unfixed','28a:5','אמר רב חיננא אמר רב כהנא אמר שמואל במוכס שאין לו קצבה','Shmuel, via Rav Kahana and Rav Hinnana, limits the case to a collector without a fixed assessment.',holder='שמואל',conditions=['collector lacks fixed assessment'],scope='First answer to tax-law objection')
a.add('unfixed.chain','attributions',dict(surface='אמר רב חיננא אמר רב כהנא אמר שמואל',role='transmitter',candidates=['רב חיננא','רב כהנא'],scope=unfixed,transmission_chain=['רב חיננא','רב כהנא','שמואל']),[a.ev('28a:5','אמר רב חיננא אמר רב כהנא אמר שמואל')],[unfixed])
self=c('self','28a:5',"דבי ר' ינאי אמר במוכס העומד מאליו",'The school of Rabbi Yannai explains a self-appointed collector.',holder="דבי ר' ינאי",conditions=['self-appointed collector'],scope='Alternative explanation, not forced identification with Shmuel’s condition')
e('unfixed.answer',unfixed,lawq,'answer','28a:5');e('self.answer',self,lawq,'answer','28a:5')
form=q('form','28a:6','היכי נדר','What form does the royal-property vow take?')
ravform=c('ravform','28a:6','אמר רב עמרם אמר רב באומר יאסרו פירות העולם עלי אם אינן של בית המלך','Rav, through Rav Amram, explains a declaration prohibiting the world’s produce to him if it is not royal property.',holder='רב',scope='Hypothetical vow formulation; time restriction supplied below')
a.add('ravform.chain','attributions',dict(surface='אמר רב עמרם אמר רב',role='transmitter',candidates=['רב עמרם'],scope=ravform,transmission_chain=['רב עמרם','רב']),[a.ev('28a:6','אמר רב עמרם אמר רב')],[ravform])
e('ravform.answer',ravform,form,'answer','28a:6')
allq=q('allq','28a:7','כיון דאמר יאסרו איתסרו עליה כל פירי עלמא','Would that declaration not prohibit all the world’s produce to him?')
today=c('today','28a:7','באומר היום','The first answer limits the declaration to today.',mode='challenged',scope='Requires further clarification because spoken limitation would fail')
acceptq=q('acceptq','28a:7','אי דאמר היום לא מקבל מיניה מוכס','If he says today, would the collector not reject the declaration?')
mental=c('mental','28a:8','באומר בלבו היום ומוציא בשפתיו סתם','He limits it mentally to today while speaking without that limitation.',conditions=['coercive setting'],scope='Explicit distinction between inward qualification and spoken form')
exception=c('exception','28a:8','ואף על גב דסבירא לן דברים שבלב אינם דברים לגבי אונסין שאני','Although unspoken intentions ordinarily do not count, the source distinguishes compulsion.',conditions=['compulsion'],scope='Express exception, not general validity of secret qualifications')
e('today.answer',today,allq,'answer','28a:7');e('mental.answer',mental,acceptq,'answer','28a:8');e('exception.support',exception,mental,'support','28a:8')
repeat=c('repeat','28a:9',None,'The discussion repeats the Mishnah’s excess wife-and-sons declaration and the two schools’ different outcomes.',composition='composite',scope='Repeated source occurrence retained; not an additional independent dispute')
baraita=c('baraita','28a:10','אמר רב הונא תנא בית שמאי אומרים לא יפתח לו בשבועה ובית הלל אומרים אף יפתח לו בשבועה','Rav Huna cites a teaching prohibiting initiation of an oath for Beit Shammai and allowing it for Beit Hillel.',composition='composite',scope='Narrated report of both school positions; Rav Huna is transmitter, not holder of either view; alternative reading28a:13')
a.add('baraita.chain','attributions',dict(surface='אמר רב הונא תנא',role='transmitter',candidates=['רב הונא'],scope=baraita,transmission_chain=['רב הונא']),[a.ev('28a:10','אמר רב הונא תנא')],[baraita])
initq=q('initq','28a:10','לבית שמאי בשבועה הוא דלא יפתח לו הא בנדר יפתח לו והא תנן בית שמאי אומרים לא יפתח לו בנדר','Does the oath-specific ban imply permission to initiate a vow, contrary to the Mishnah?')
swearq=q('swearq','28a:11',None,'Does banning initiation alone imply that a demanded oath is allowed, contrary to Beit Shammai’s exclusion of oaths?')
emphasis=c('emphasis','28a:12',None,'The reply says the Mishnah uses vows to show the strength of Beit Shammai’s restriction, while the baraita uses oaths to show Beit Hillel’s permission.',composition='composite',scope='Different illustrative emphasis, not acceptance of the challenged inferences')
ashi=c('ashi','28a:13','רב אשי אמר הכי קתני בית שמאי אומרים אין שאלה בשבועה ובית הלל אומרים יש שאלה בשבועה','Rav Ashi instead reads the teaching as Beit Shammai denying release inquiry for an oath and Beit Hillel allowing it.',holder='רב אשי',composition='composite',scope='Alternative interpretation about release, not initiating a declaration under coercion')
for key,question in [('init',initq),('swear',swearq)]:
    e(key+'.answer',emphasis,question,'answer','28a:12');e(key+'.alternate',ashi,question,'answer','28a:13')
a.notes={
'27a:5':'Reread three compulsion grounds and meal-vow category as fresh source occurrence.',
'27a:6':'Reread thirty-day undertaking, deposited rights, unstated compulsion type and Rav Huna cancellation.',
'27a:7':'Reread Rava objection and exact biblical exemption citation.',
'27a:8':'Reread anticipated capital-case distinction and quoted Mishnah counterproof.',
'27a:9':'Reread twelve-month conditional divorce, death and compulsion objection across page boundary.',
'27b:1':'Reread tentative counterfactual intent distinction, not universal compulsion denial.',
'27b:2':'Reread ferry case, repeated arrival cry, Shmuel ruling and renewed compulsion question.',
'27b:3':'Reread tentative foreseeable-impediment distinction.',
'27b:4':'Reread asmakhta question and initial document-deposit distinction.',
'27b:5':'Reread deposit challenge and thirty-day partial-debt counterexample.',
'27b:6':'Reread Yosei/Yehuda disagreement and complete Nahman/Rabbah bar Avuha/Rav transmission.',
'27b:7':'Reread explicit rights-cancellation distinction.',
'27b:8':'Reread final asmakhta rule with both no-compulsion and significant-court acquisition conditions.',
'27b:9':'Reread coercer categories, two factual declarations and Beit Shammai clause continuing28a:1.',
'28a:1':'Reread cross-page oath exclusion and Beit Hillel allowance.',
'28a:2':'Reread separate initiation and excess-wording disagreements.',
'28a:3':'Reread wife/sons example and both differential/all-permitted outcomes.',
'28a:4':'Reread Shmuel kingdom-law quotation as explicit objection.',
'28a:5':'Reread exact Hinnana/Kahana/Shmuel chain and distinct Yannai-school alternative.',
'28a:6':'Reread form question and Amram-to-Rav conditional produce prohibition.',
'28a:7':'Reread prohibition objection, today answer and collector-acceptance challenge.',
'28a:8':'Reread inward/spoken distinction and compulsion-only exception to ordinary mental-intention rule.',
'28a:9':'Reread repeated Mishnah quotation; retained as expressly composite repeated occurrence.',
'28a:10':'Reread Rav Huna quoted two-school baraita and first contradiction inference.',
'28a:11':'Reread second initiation-versus-demanded-oath contradiction.',
'28a:12':'Reread asymmetric pedagogic emphasis resolving both inferences.',
'28a:13':'Reread Rav Ashi alternative release-inquiry interpretation, separate from first answer.'}
if __name__=='__main__':a.save()
