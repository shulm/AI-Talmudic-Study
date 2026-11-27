"""Sick-visiting narratives/rewards and explicit Rav/Shmuel river disagreement."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r042.';a.OUTPUT='continuation_042.json'
c=a.c;q=b.q;e=a.edge
a.structure('care',['39b:18']+['40a:'+str(i) for i in range(1,11)],'Sick-visiting care, prayer, rewards and presence')
a.structure('river',['40a:11','40b:1','40b:2'],'River sources and purification: Rav/Shmuel disagreement and Shmuel tension')
helbo=c('helbo','39b:18',None,'Rav Helbo falls ill and Rav Kahana goes out to announce it.',composition='composite',scope='Narrative opening; announcement completed40a:1')
announcement=c('announcement','40a:1','רב חלבו באיש לא איכא דקא אתי','Rav Kahana announces Rav Helbo’s illness, but nobody comes.',composition='composite',scope='Cross-page narrative continuation')
student=c('student','40a:1',"אמר להו לא כך היה מעשה בתלמיד אחד מתלמידי ר' עקיבא שחלה לא נכנסו חכמים לבקרו ונכנס ר' עקיבא לבקרו",'He recalls a sick student whom the sages did not visit, while Rabbi Akiva did.',composition='composite',scope='Embedded precedent, distinct from Rav Helbo episode')
clean=c('clean','40a:1','ובשביל שכיבדו וריבצו לפניו חיה','The account links the student’s recovery to sweeping and sprinkling the room for him.',scope='Source-reported care and recovery, not a quantified clinical claim')
thanks=c('thanks','40a:1','א"ל רבי החייתני','The student says his teacher restored his life.',scope='Reported gratitude, not narrator’s independent efficacy measurement')
akiva=c('akiva','40a:1',"יצא ר' עקיבא ודרש כל מי שאין מבקר חולים כאילו שופך דמים",'Rabbi Akiva expounds that failure to visit the sick is like shedding blood.',holder="ר' עקיבא",scope='Attributed ethical comparison, not literal criminal liability ruling')
dimi=c('dimi','40a:2','כי אתא רב דימי אמר כל המבקר את החולה גורם לו שיחיה וכל שאינו מבקר את החולה גורם לו שימות','Rav Dimi says visiting contributes to life and not visiting contributes to death.',holder='רב דימי',composition='composite',scope='Causal ethical formulation clarified through prayer below')
how=q('how','40a:2','מאי גרמא','What kind of contribution is meant?')
pray=c('pray','40a:2','אילימא כל המבקר את החולה מבקש עליו רחמים שיחיה','The proposed explanation has the visitor praying for the patient’s life.',mode='hypothetical',scope='First part of proposed prayer contrast')
death=c('death','40a:2','וכל שאין מבקר את החולה מבקש עליו רחמים שימות שימות ס"ד','The proposal that a nonvisitor prays for death is immediately rejected as untenable.',mode='rejected',scope='Do not record this as endorsed behavior')
none=c('none','40a:2','אלא כל שאין מבקר חולה אין מבקש עליו רחמים לא שיחיה ולא שימות','The correction is that a nonvisitor offers no prayer for the patient, either for life or death.',scope='Final explanation of omission, not malicious prayer')
e('none.answer',none,how,'answer','40a:2');e('none.correction',none,death,'correction','40a:2')
hide=c('hide','40a:3','רבא יומא קדמאה דחליש אמר להון לא תיגלו לאיניש דלא לתרע מזליה','On the first day of illness Rava asks that it not be disclosed so his fortune not be harmed.',holder='רבא',scope='Narrative personal practice and stated rationale, not contemporary health advice')
public=c('public','40a:3',"מכאן ואילך אמר להון פוקו ואכריזו בשוקא דכל דסני לי ליחדי לי וכתיב (משלי כד, יז) בנפול אויבך אל תשמח וגו' ודרחים לי ליבעי עלי רחמי",'Afterward he requests public announcement so enemies’ rejoicing invokes the cited warning and friends pray for him.',holder='רבא',composition='composite',scope='Both explicitly stated motives retained')
rav=c('rav','40a:4','אמר רב כל המבקר את החולה ניצול מדינה של גיהנם','Rav promises rescue from Gehinnom’s judgment for visiting the sick.',holder='רב',scope='Attributed religious reward assertion')
poor=c('poor','40a:4','אין דל אלא חולה שנאמר (ישעיהו לח, יב) מדלה יבצעני','The first lexical support identifies דל with a sick person via Isaiah.',scope='Part of interpretation of Psalm41:2')
poor2=c('poor2','40a:4',"אי נמי מן הדין קרא (שמואל ב יג, ד) מדוע אתה ככה דל בן המלך בבקר בבקר וגו'",'An alternative support for דל as sick comes from the king’s son verse.',scope='Explicit alternative prooftext, not deduplicated')
evil=c('evil','40a:4','אין רעה אלא גיהנם שנאמר (משלי טז, ד) כל פעל י"י למענהו וגם רשע ליום רעה','רעה is interpreted as Gehinnom through the wicked-for-a-day-of-evil verse.',scope='Second lexical step in Rav’s reward exposition')
for key,claim in [('poor',poor),('poor2',poor2),('evil',evil)]:e(key+'.support',claim,rav,'support','40a:4')
rewardq=q('rewardq','40a:5','ואם ביקר מה שכרו','What is the visitor’s reward?')
already=c('already','40a:5','מה שכרו כדאמר ניצול מדינה של גיהנם','The discussion notes that rescue from Gehinnom was already stated.',scope='Correction of redundant question')
worldq=q('worldq','40a:5','אלא מה שכרו בעוה"ז','What is the reward in this world?')
protect=c('protect','40a:6',"יי' ישמרהו מיצר הרע",'The verse’s protection is read as protection from the evil inclination.',scope='This-world reward exposition')
alive=c('alive','40a:6','ויחייהו מן היסורין','Its life-preservation is read as rescue from suffering.',scope='Second reward clause')
honored=c('honored','40a:6','ואושר בארץ שיהו הכל מתכבדין בו','Its earthly flourishing is read as everyone finding honor in him.',scope='Third reward clause')
friends=c('friends','40a:6','ואל תתנהו בנפש אויביו שיזדמנו לו רועים כנעמן שריפו את צרעתו ואל יזדמנו לו ריעים כרחבעם שחילקו את מלכותו','The final clause is interpreted as companions like Naaman’s who helped cure him, rather than Rehoboam’s who divided his kingdom.',composition='composite',scope='Two biblical exemplars in attributed reward exposition; printed רועים/ריעים retained')
e('already.answer',already,rewardq,'answer','40a:5')
for key,claim in [('protect',protect),('alive',alive),('honored',honored),('friends',friends)]:e(key+'.answer',claim,worldq,'answer','40a:6')
elders=c('elders','40a:7',None,'Rabbi Shimon ben Elazar advises following elders who say demolish over youths who say build, because the apparent outcomes reverse, with Rehoboam as the sign.',holder='ר"ש בן אלעזר',composition='composite',scope='Attributed proverbial advice and exemplar, not an unconditional modern age-based rule')
hours=c('hours','40a:8','אמר רב שישא בריה דרב אידי לא ליסעוד איניש קצירא לא בתלת שעי קדמייתא ולא בתלת שעי בתרייתא דיומא כי היכי דלא ליסח דעתיה מן רחמי','Rav Shisha son of Rav Idi discourages visits in the day’s first or final three hours to avoid neglecting prayer.',holder='רב שישא בריה דרב אידי',composition='composite',scope='Source’s visit-timing instruction, not clinical scheduling guidance')
cycle=c('cycle','40a:8','תלת שעי קדמייתא רווחא דעתיה בתרייתא תקיף חולשיה','The stated rationale is relative ease early and intense illness late.',scope='Ancient source’s illness-cycle premise')
sustainq=q('sustainq','40a:9','מניין שהקב"ה זן את החולה','What supports the claim that God sustains the sick?',voice='רב')
sustain=c('sustain','40a:9',"שנאמר (תהלים מא, ד) יי' יסעדנו על ערש דוי וגו'",'Rav cites divine support on the sickbed.',holder='רב',scope='Ravin transmits this theological derivation')
presenceq=q('presenceq','40a:9','מניין שהשכינה שרויה למעלה ממטתו של חולה','What supports divine presence above the sickbed?',voice='רב')
presence=c('presence','40a:9',"שנאמר יי' יסעדנו על ערש דוי",'The same sickbed-support verse is cited for divine presence above the bed.',holder='רב',scope='Second distinct derivation reported by Ravin')
for key,claim in [('sustain',sustain),('presence',presence)]:a.add(key+'.chain','attributions',dict(surface='אמר רבין אמר רב',role='transmitter',candidates=['רבין'],scope=claim,transmission_chain=['רבין','רב']),[a.ev('40a:9',('אמר רבין אמר רב',0 if key=='sustain' else 1))],[claim])
e('sustain.answer',sustain,sustainq,'answer','40a:9');e('presence.answer',presence,presenceq,'answer','40a:9')
floor=c('floor','40a:10',None,'A corroborating baraita instructs the visitor to sit wrapped on the ground rather than bed, bench or chair, because the divine presence is above the sickbed.',composition='composite',scope='Specific reverence instruction and scriptural rationale')
e('floor.support',floor,presence,'support','40a:10')
rain=c('rain','40a:11','ואמר רבין אמר רב מטרא במערבא סהדא רבה פרת','Rav, via Ravin, treats the Euphrates as strong evidence of rain in the West.',holder='רב',scope='Source’s river-rise interpretation')
a.add('rain.chain','attributions',dict(surface='אמר רבין אמר רב',role='transmitter',candidates=['רבין'],scope=rain,transmission_chain=['רבין','רב']),[a.ev('40a:11','אמר רבין אמר רב')],[rain])
source=c('source','40a:11','ופליגא דשמואל דאמר שמואל נהרא מכיפיה מתבריך','Shmuel disagrees, saying the river increases from its own source.',holder='שמואל',scope='Explicit ופליגא marks actual Rav/Shmuel contrast')
restrict=c('restrict','40a:11','ופליגא דשמואל אדשמואל דאמר שמואל אין המים מטהרין בזוחלין','A contrary statement of Shmuel permits flowing-water purification only for the Euphrates in Tishrei.',extra=[('40b:1',None)],holder='שמואל',conditions=['Euphrates','Tishrei'],scope='Source explicitly flags Shmuel-versus-Shmuel tension; no reconciliation supplied here',uncertainty=['Do not erase the explicit internal contradiction or infer a retraction.'])
father=c('father','40b:2',None,'Shmuel’s father prepares immersion pools for his daughters in Nisan and mats in Tishrei.',composition='composite',scope='Father’s seasonal practice, distinct person from Shmuel; precise mats function not supplied in this clause')
e('source.objection',source,rain,'objection','40a:11');e('restrict.objection',restrict,source,'objection','40a:11')
a.notes={
'39b:18':'Reread Helbo illness and Kahana announcement introduction spanning page.',
'40a:1':'Reread absent visitors, embedded Akiva student narrative, room care, gratitude and ethical bloodshed analogy.',
'40a:2':'Reread Dimi causal formulation, how question, rejected death-prayer inference and no-prayer correction.',
'40a:3':'Reread Rava first-day privacy and later publicity with both enemy/friend rationales.',
'40a:4':'Reread Rav reward claim, both דל prooftexts and רעה derivation.',
'40a:5':'Reread redundant reward question and explicit narrowing to this world.',
'40a:6':'Reread all four reward interpretations and Naaman/Rehoboam companions comparison.',
'40a:7':'Reread Shimon ben Elazar elders/youth proverb and Rehoboam exemplar.',
'40a:8':'Reread Shisha timing instruction and source’s two daily illness phases, kept as attributed ancient rationale.',
'40a:9':'Reread both Ravin/Rav questions and separate sickbed-verse derivations.',
'40a:10':'Reread bed/bench/chair exclusions, ground-wrapped posture and divine-presence support.',
'40a:11':'Reread Ravin/Rav rain statement, explicit Shmuel disagreement and explicit Shmuel/self tension spanning page.',
'40b:1':'Reread Euphrates/Tishrei restriction completing Shmuel statement; no invented harmonization.',
'40b:2':'Reread Shmuel’s father seasonal pools/mats practice, distinct from son.'}
if __name__=='__main__':a.save()
