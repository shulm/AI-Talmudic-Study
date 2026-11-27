"""Manual vows/excommunication narrative and transmission reading."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r007.';a.OUTPUT='continuation_007.json'
c=a.c;q=a.q;e=a.edge
def transmission(key,claim,ref,quote,chain):
    a.add(key,'attributions',dict(surface=quote if quote is not None else a.refs[ref]['text'],role='transmitter',candidates=chain[:-1],scope=claim,transmission_chain=chain),[a.ev(ref,quote)],[claim])
a.structure('menude',['7a:9','7a:10','7b:1','7b:2'],'Meaning of מנודה and משמתנא and Rabbi Akiva’s qualified stringency')
a.structure('release',['7b:'+str(i) for i in range(3,9)],'Excommunication in presence, misuse of the divine name, and self-release')
lashes=c('lashes','7a:9',"אמר אביי  מודה ר''ע לענין מלקות שאינו לוקה",'Abaye says Rabbi Akiva agrees that this formulation does not incur lashes.',holder='אביי',conditions=['מנודה אני לך'],scope='Explanation of Mishnah’s tendency toward stringency, not an unconditional permission')
wording=c('wording','7a:9',"דאם כן ניתני  ר' עקיבא מחמיר",'The proof is that otherwise the Mishnah should state Rabbi Akiva is stringent without its qualified wording.',scope='Stated textual rationale in Abaye’s report')
e('wording.support',wording,lashes,'support','7a:9')
nd=c('nd','7a:10','אמר רב פפא  בנדינא מינך דכולי עלמא לא פליגי דאסור','Rav Pappa says all agree that נדינא מינך prohibits.',holder='רב פפא',conditions=['נדינא מינך'],scope='Rav Pappa’s account of the tannaitic dispute')
sm=c('sm','7a:10','משמתנא מינך לכולי עלמא שרי','In Rav Pappa’s account all permit משמתנא מינך.',holder='רב פפא',conditions=['משמתנא מינך'],scope='Contrasted below with Rav Hisda’s account')
where=q('where','7a:10','במאי פליגי','In which wording do the tannaim disagree?')
akiva=c('akiva','7b:1','במנודה אני לך דרבי עקיבא סבר  לישנא דנידויא הוא','For מנודה אני לך, Rabbi Akiva reads the wording as language of exclusion.',holder='רבי עקיבא',conditions=['מנודה אני לך'],scope='Rav Pappa’s account, explained in continuation of7a:10; no separate direct speech claim')
sages=c('sages','7b:1','ורבנן סברי  לישנא דמשמתנא הוא','The sages read that wording as language of excommunication.',holder='רבנן',conditions=['מנודה אני לך'],scope='Rav Pappa’s account of their interpretation')
e('akiva.answer',akiva,where,'answer','7b:1');e('sages.distinction',sages,akiva,'distinction','7b:1')
story=c('story','7b:2',"דההוא גברא דאמר משמתנא בנכסיה דבריה דרב ירמיה בר אבא אתא לקמיה דרב חסדא",'A man used משמתנא concerning the property of Rav Yirmeya bar Abba’s son and came before Rav Hisda.',composition='composite',scope='Narrated declaration and consultation; son is property owner, not named ruling authority')
hisda=c('hisda','7b:2',"א''ל לית דחש לה להא דרבי עקיבא",'Rav Hisda told him that no one gives weight here to Rabbi Akiva’s view.',holder='רב חסדא',conditions=['the narrated משמתנא property declaration'],scope='Local response, not a general rejection of Rabbi Akiva in other matters')
account=c('account','7b:2','קסבר במשמתנא פליגי','The discussion infers that Rav Hisda locates the disagreement in משמתנא.',scope='Anonymous inference explicitly contrasting Rav Pappa’s account')
e('account.objection',account,sm,'objection','7b:2','ופליגא דרב חסדא');e('hisda.support',hisda,account,'support','7b:2')
present=c('present','7b:3','אמר רבי אילא אמר רב נדהו בפניו אין מתירין לו אלא בפניו','Rav, reported by Rabbi Ila, requires release in the person’s presence when excommunication was imposed in his presence.',holder='רב',conditions=['excommunication imposed in presence'])
absent=c('absent','7b:3','נדהו שלא בפניו מתירין לו בין בפניו בין שלא בפניו','When imposed in the person’s absence, release can be either in his presence or absence.',holder='רב',conditions=['excommunication imposed in absence'])
transmission('ila',present,'7b:3','אמר רבי אילא אמר רב',['רבי אילא','רב']);transmission('ila2',absent,'7b:3','אמר רבי אילא אמר רב',['רבי אילא','רב'])
name=c('name','7b:4','אמר רב חנין אמר רב השומע הזכרת השם מפי חבירו צריך לנדותו','Rav, reported by Rav Hanin, requires excommunicating someone heard uttering the divine name.',holder='רב',conditions=['hearing the improper use described in this unit'],scope='Context clarified explicitly as לבטלה in7b:6; no blanket ban on legitimate divine-name utterance')
failure=c('failure','7b:4','ואם לא נידהו הוא עצמו יהא בנידוי','If the hearer does not impose excommunication, he himself should be under excommunication.',holder='רב',conditions=['hears the stated improper name-use','does not excommunicate'])
poor=c('poor','7b:4','שכל מקום שהזכרת השם מצויה שם עניות מצויה','The report gives the rationale that habitual such name-use is accompanied by poverty.',holder='רב',scope='Source’s stated religious consequence, not an empirical causal claim by the annotator')
for key,claim in [('hanin',name),('hanin2',failure),('hanin3',poor)]:transmission(key,claim,'7b:4','אמר רב חנין אמר רב',['רב חנין','רב'])
e('poor.support',poor,name,'support','7b:4')
death=c('death','7b:5','ועניות כמיתה שנאמר (שמות ד יט) כי מתו כל האנשים','The discussion compares poverty with death and cites כי מתו כל האנשים.',scope='Source’s interpretive comparison; no external identification supplied')
gaze=c('gaze','7b:5','ותניא כל מקום שנתנו חכמים עיניהם או מיתה או עוני','A cited teaching associates the sages’ directed gaze with death or poverty.',scope='Quoted anonymous teaching, alternative outcomes preserved')
e('gaze.support',gaze,death,'support','7b:5')
abba=c('abba','7b:6','אמר רבי אבא הוה קאימנא קמיה דרב הונא','Rabbi Abba reports standing before Rav Huna.',holder='רבי אבא',scope='First-person narrative frame, Rav Huna is not the reporter')
woman=c('woman','7b:6','שמעה להך איתתא דאפקה הזכרת השם לבטלה שמתה ושרא לה לאלתר באפה','Rav Huna heard a woman utter the divine name in vain, excommunicated her and immediately released her in her presence.',composition='composite',scope='Sequence narrated by Rabbi Abba; no speech quotation or unstated motive invented')
infer1=c('infer1','7b:6',"ש''מ תלת ש''מ השומע הזכרת השם מפי חבירו צריך לנדותו",'The discussion derives that a hearer of such improper name-use must impose excommunication.',scope='First explicit inference from narrated event')
infer2=c('infer2','7b:6',"וש''מ נידהו בפניו אין מתירין לו אלא בפניו",'It derives that excommunication imposed in presence must be released in presence.',scope='Second explicit inference')
infer3=c('infer3','7b:6',"וש''מ אין בין נידוי להפרה ולא כלום",'It derives that no time interval is required between excommunication and its release.',scope='Third explicit inference; not an unrestricted rule beyond local context')
for key,x in [('n',infer1),('p',infer2),('t',infer3)]:e(key+'.support',woman,x,'support','7b:6')
self=c('self','7b:7',"א''ר גידל אמר רב תלמיד חכם מנדה לעצמו ומיפר לעצמו",'Rav, reported by Rabbi Giddel, says a scholar may excommunicate himself and release himself.',holder='רב',conditions=['תלמיד חכם','self-imposed excommunication'],composition='composite')
transmission('giddel',self,'7b:7',"א''ר גידל אמר רב",['רבי גידל','רב'])
obvious=q('obvious','7b:7','פשיטא','Is that not obvious?')
prison=c('prison','7b:7','מהו דתימא אין חבוש מתיר עצמו מבית האסורין','One might have applied the principle that a captive cannot free himself.',mode='rejected',scope='Excluded analogy, not operative prohibition')
e('prison.answer',prison,obvious,'answer','7b:7');e('self.correction',self,prison,'correction','7b:7',"קמ''ל")
how=q('how','7b:8','היכי דמי','What is a case of self-imposed excommunication?')
zutra1=c('zutra1','7b:8','כי הא דמר זוטרא חסידא כי מחייב בר בי רב שמתא משמית נפשיה ברישא והדר משמת בר בי רב','When a scholar incurred excommunication, Mar Zutra the pious first excommunicated himself and then the scholar.',conditions=['another scholar liable to excommunication'],composition='composite',scope='Narrative procedural sequence, no motivation invented')
zutra2=c('zutra2','7b:8','וכי עייל לביתיה שרי לנפשיה והדר שרי ליה','When he entered his house he released himself first and then the other scholar.',composition='composite',scope='Continuation of narrated practice')
e('zutra1.answer',zutra1,how,'answer','7b:8');e('zutra2.support',zutra2,self,'support','7b:8')
a.notes={
'7a:9':'Reread Abaye’s no-lashes limitation and precise Mishnah-wording proof.',
'7a:10':'Reread both consensus formulations and question completed7b:1; Rav Pappa’s account kept distinct from Rav Hisda.',
'7b:1':'Reread two interpretations of מנודה in the same Rav Pappa account.',
'7b:2':'Reread full property-declaration consultation, Rav Hisda response and anonymous inference of disagreement scope; narrative retained.',
'7b:3':'Reread both presence/absence conditions and Rabbi Ila-to-Rav transmission.',
'7b:4':'Reread required sanction, hearer’s failure and poverty rationale; Rav Hanin transmitter kept separate from Rav.',
'7b:5':'Reread poverty/death verse interpretation and gaze teaching without turning them into empirical annotation assertions.',
'7b:6':'Reread Rabbi Abba frame, Rav Huna/woman sequence and all three distinct explicit inferences.',
'7b:7':'Reread Rabbi Giddel-to-Rav chain, paired self-actions, obviousness question and rejected captivity analogy.',
'7b:8':'Reread Mar Zutra’s full ordered procedure and timing; no invented motives.'}
if __name__=='__main__':a.save()
