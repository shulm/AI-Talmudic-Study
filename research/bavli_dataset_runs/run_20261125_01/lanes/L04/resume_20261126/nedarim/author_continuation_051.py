"""Manual narrative reading: Akiva, found wealth and appearance dialogues."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r051.';a.OUTPUT='continuation_051.json'
c=a.c;e=a.edge;q=b.q
a.structure('akiva',['50a:'+str(i) for i in range(2,9)]+['50b:1'],'Akiva marriage, study and narrated sources of wealth')
a.structure('gifts',['50b:2','50b:3','50b:4','50b:5'],'Found pearls, wine-vessel analogy and Shmuel insult narrative')
betroth=c('betroth','50a:2',None,'Rabbi Akiva becomes betrothed to Kalba Savua’s daughter; her father prohibits her benefit from his property, and she goes and marries Akiva.',composition='composite',scope='Three narrative events; parenthetical דבר/בר name wording preserved in evidence without harmonization')
straw=c('straw','50a:3','בסיתוא הוה גנו בי תיבנא הוה קא מנקיט ליה תיבנא מן מזייה','In winter they sleep in straw, and Akiva removes straw from her hair.',composition='composite',scope='Reported poverty scene')
gold=c('gold','50a:3','אמר לה אי הואי לי רמינא ליך ירושלים דדהבא','Akiva says that if he had the means he would give her a golden Jerusalem ornament.',holder="ר' עקיבא",mode='conditional',conditions=('If he had the means',),scope='Personal conditional promise in narrative')
elijah=c('elijah','50a:3','אתא אליהו אידמי להון כאנשא וקא קרי אבבא','The narrator identifies Elijah as appearing in human guise at their door.',scope='Narrator’s supernatural identification retained as source narrative')
request=c('request','50a:3','אמר להו הבו לי פורתא דתיבנא דילדת אתתי ולית לי מידעם לאגונה','The visitor asks for straw, saying his wife has given birth and he has no bedding for her.',holder='אליהו',composition='composite',scope='Visitor’s speech within the disguise narrative, not independently asserted biography')
poorer=c('poorer','50a:3','אמר לה ר\' עקיבא לאנתתיה חזי גברא דאפילו תיבנא לא אית ליה','Akiva tells his wife to observe someone who lacks even straw.',holder="ר' עקיבא",scope='Narrative comparison of deprivation')
go=c('go','50a:4','אמרה ליה זיל הוי בי רב','Akiva’s wife tells him to go study.',scope='Wife’s explicit initiative in narrative')
study=c('study','50a:4','אזל תרתי סרי שנין קמי דר\' אליעזר ור\' יהושע','Akiva goes for twelve years before Rabbi Eliezer and Rabbi Yehoshua.',composition='composite',scope='Duration and both named teachers')
home=c('return','50a:4','למישלם תרתי סרי שנין קא אתא לביתיה שמע מן אחורי ביתיה','At the end of twelve years he approaches home and overhears speech from behind the house.',composition='composite',scope='Narrative setting for renewed permission')
taunt=c('taunt','50a:4','דקאמר לה חד רשע לדביתהו שפיר עביד ליך אבוך חדא דלא דמי ליך ועוד [שבקך] ארמלות חיות כולהון שנין','A man characterized as wicked tells her that her father acted rightly because Akiva is beneath her and has left her in living widowhood all these years.',composition='composite',scope='Interlocutor’s taunt, not narrator’s endorsement; bracketed verb preserved')
permission=c('permission','50a:4','אמרה ליה אי צאית לדילי ליהוי תרתי סרי שנין אחרנייתא','She replies that if he would listen to her he would remain another twelve years.',mode='conditional',scope='Wife’s expressed preference overheard by Akiva')
again=c('again','50a:4','אמר הואיל ויהבת לי רשותא איהדר לאחורי הדר אזל הוה תרתי סרי שני אחרנייתא','Akiva treats this as permission, turns back, and spends another twelve years studying.',holder="ר' עקיבא",composition='composite',scope='Quoted inference and narrated action kept together explicitly')
e('permission.objection',permission,taunt,'objection','50a:4');e('permission.support',permission,again,'support','50a:4')
crowd=c('crowd','50a:5','אתא בעשרין וארבעה אלפין זוגי תלמידי נפוק כולי עלמא לאפיה ואף היא קמת למיפק לאפיה','He returns with twenty-four thousand pairs of students; people go to meet him and his wife rises to do so too.',composition='composite',scope='Printed זוגי retained as pairs, not silently changed to students alone')
where=q('where','50a:5','אמר לה ההוא רשיעא ואת להיכא','The man asks his wife where she is going.')
animal=c('animal','50a:5','אמרה ליה (משלי יב, י) יודע צדיק נפש בהמתו','She replies with the verse that a righteous person knows the soul of his animal.',scope='Wife’s scriptural reply in narrative')
push=c('push','50a:5','אתת לאיתחזויי ליה קא מדחן לה רבנן','When she comes to be seen by him, the sages push her away.',scope='Narrative obstacle before Akiva’s intervention')
hers=c('hers','50a:5','אמר להון הניחו לה שלי ושלכם שלה הוא','Akiva tells them to leave her alone, saying that his and their learning belongs to her.',holder="ר' עקיבא",scope='Acknowledgment of her contribution; object learning inferred from study narrative, not property adjudication')
release=c('release','50a:5','שמע (בר) כלבא שבוע אתא ואיתשיל על נידריה ואשתריי ואשתרי','Kalba Savua hears, comes to seek release of his vow, and it is released.',scope='Narrated release; duplicate printed release wording and parenthetical בר preserved, unstated legal grounds not supplied')
e('animal.answer',animal,where,'answer','50a:5');e('hers.correction',hers,push,'correction','50a:5')
six=c('six','50a:6','מן שית מילי איעתר רבי עקיבא','The narrator says Akiva became wealthy from six things.',scope='Source’s stated count retained without imposing a conjectural reconciliation on following list')
kalba=c('kalba','50a:6','מן כלבא שבוע','Kalba Savua is listed as a source of Akiva’s wealth.',scope='Named list item; amount and mechanism unstated here')
ship=c('ship','50a:6','מן אילא דספינתא דכל ספינתא עבדין ליה מין עינא זימנא חדא אנשיוה על כיף ימא אתא הוא אשכחיה','The list describes a ship’s אילא, an eye-like fitting, forgotten on the seashore and found by Akiva.',composition='composite',scope='Narrated object and discovery; no unstated material or precise modern identification supplied')
log=c('log','50a:7','ומן גווזא דזימנא חדא יהיב ארבעה זוזי לספונאי אמר להו אייתי לי מדעם ולא אשכחו אלא גווזא על כיף ימא אתיוה ליה אמרו ליה עביד מרנא עליה','Akiva gives sailors four zuz to bring him something; they find only a log on the shore, bring it and suggest sitting on it.',composition='composite',scope='Purchase errand and explicit sailor suggestion in wealth narrative')
coins=c('coins','50a:7','אישתכח דהוה מלי דינרי דזימנא חדא טבעת ספינתא וכולי עיסקא הוה מחית בההוא גווזא ואישתכח בההוא זימנא','The log is found full of dinars, explained as cargo placed there before a ship sank.',composition='composite',scope='Narrative discovery and retrospective explanation')
serukita=c('serukita','50a:8','דמן דסרוקיתא','The printed list includes the fragment דמן דסרוקיתא.',scope='Opaque printed fragment retained without supplying an unattested story or confident separate-item count',uncertainty=('Fragment’s relation to the preceding item is not resolved by this local passage.',))
matron=c('matron','50a:8','ומן מטרוניתא','A matron is listed as a source of wealth.',scope='Bare list item; no further story supplied here')
wife=c('wife','50b:1','ומן אשתו של טורנוסרופוס','The wife of Turnus Rufus is listed as a source of wealth.',scope='Bare list item; no further story supplied here')
ketia=c('ketia','50b:1','ומן קטיעא בר שלום','Ketia bar Shalom is listed as a source of wealth.',scope='Bare list item; no further story supplied here')
gamda=c('gamda','50b:2','רב גמדא יהיב ד\' זוזי לספונאי לאתויי בהון מידעם לא אשכחו אתיוה ליה בהון קופא','Rav Gamda gives sailors four zuz to bring something; they bring him a monkey.',composition='composite',scope='Separate named narrative, not assigned to Akiva')
pearls=c('pearls','50b:2','אישתמיט על לחרתא חפרו בתריה אשכחוה דרביע על מרגלייתא אייתינון ליה כולהון','The monkey escapes into a hole; digging after it they find it on pearls and bring all the pearls to Rav Gamda.',composition='composite',scope='Narrative sequence and recipient from immediately preceding clause')
beauty=c('beauty','50b:3','אמרה ליה בת קיסר לרבי יהושע בן חנניה תורה מפוארה בכלי מכוער','Caesar’s daughter addresses Rabbi Yehoshua ben Hananya as splendid Torah in an ugly vessel.',scope='Attributed insult/contrast, not narrator’s assessment')
vesselq=q('vesselq','50b:3','א"ל למדי מבית אבוך במה מניחין יין','Yehoshua asks what vessels her father’s household uses for wine.',voice='רבי יהושע בן חנניה')
earthen=c('earthen','50b:3','אמרה ליה במאני דפחרא','She answers: earthen vessels.',scope='Caesar’s daughter’s answer')
silver=c('silver','50b:3','אמר לה כולי עלמא בפחרא ואתון במאני דפחרא אתון אחיתון במאני דכספא ודהבא','Yehoshua proposes that the imperial household distinguish itself by putting wine in silver and gold vessels.',holder='רבי יהושע בן חנניה',scope='Narrative experiment proposed to expose the beauty analogy, not practical wine-storage advice')
spoiled=c('spoiled','50b:4','אזלת ורמת חמרא במאני דכספא ודהבא וסרי','She puts wine in silver and gold vessels, and it spoils.',composition='composite',scope='Reported result of the experiment')
torah=c('torah','50b:4','אמר לה אף אורייתא כן','Yehoshua says Torah is likewise.',holder='רבי יהושע בן חנניה',scope='Analogy to the vessel experiment, explained by the following challenge')
handsome=q('handsome','50b:4','והאיכא שפירין וגמירין','But are there not attractive people who are learned?')
more=c('more','50b:4','אמר לה אי הוו סנו הוו גמירין טפי','He answers that if they were unattractive they would have learned more.',holder='רבי יהושע בן חנניה',mode='conditional',scope='Attributed counterfactual response; not an endorsed empirical generalization')
e('earthen.answer',earthen,vesselq,'answer','50b:3');e('torah.analogy',torah,spoiled,'analogy','50b:4');e('more.answer',more,handsome,'answer','50b:4')
case=c('case','50b:5','ההיא דאתיא לקמיה דרב יהודה מנהרדעא לדינא ואיתחייבת מן דינא','A woman comes before Rav Yehuda of Nehardea and loses her case.',scope='Specific litigant narrative, not Rav himself')
shmuelq=q('shmuelq','50b:5','אמרה ליה שמואל רבך הכי דנן','She asks whether his teacher Shmuel judges this way.')
knowq=q('knowq','50b:5','אמר לה ידעת ליה','Rav Yehuda asks whether she knows Shmuel.',voice='רב יהודה מנהרדעא')
description=c('description','50b:5','אמרה ליה אין גוצא ורבה כריסיה אוכם ורבה שיניה','She answers yes and describes Shmuel as short, large-bellied, dark and large-toothed.',composition='composite',scope='Litigant’s disparaging description, not endorsed characterization')
rebuke=c('rebuke','50b:5','אמר לה לבזוייה קאתית תיהוי ההיא אתתא בשמתא','Rav Yehuda accuses her of coming to insult Shmuel and pronounces a ban.',holder='רב יהודה מנהרדעא',composition='composite',scope='Narrated response, not a general rule for litigants')
death=c('death','50b:5','פקעה ומתה','The narrator reports that she bursts and dies.',scope='Narrated extraordinary outcome; no clinical causation inferred')
e('description.answer',description,knowq,'answer','50b:5');e('rebuke.objection',rebuke,description,'objection','50b:5')
for row in a.records:
    if row['id']==shmuelq:
        row['content']['answer_set_status']='none';row['uncertainty']=['Rav Yehuda responds to the insult; the passage does not answer whether Shmuel would decide this case the same way.']
a.notes={
'50a:2':'Reread betrothal, father property vow and marriage; parenthetical name variants retained.',
'50a:3':'Reread straw scene, conditional ornament promise, narrator Elijah identification, disguised request and poverty comparison.',
'50a:4':'Reread wife initiative, both teachers/twelve-year periods, insulting speech, renewed permission and return decision.',
'50a:5':'Reread twenty-four thousand PAIRS, wife verse, sages rebuff, Akiva acknowledgment and father vow-release without inventing legal grounds.',
'50a:6':'Reread six-source declaration, Kalba Savua and ship fitting; no forced numerical reconciliation.',
'50a:7':'Reread four-zuz sailor errand, sitting suggestion, log contents and shipwreck backstory.',
'50a:8':'Reread opaque serukita fragment and bare matron item without importing extraneous narratives.',
'50b:1':'Reread Turnus Rufus wife and Ketia bar Shalom bare wealth items.',
'50b:2':'Reread separate Rav Gamda monkey-and-pearls narrative with all transaction steps.',
'50b:3':'Reread imperial daughter insult, wine-vessel question and answer, silver/gold experiment proposal.',
'50b:4':'Reread spoiled wine, Torah analogy, attractive-scholars objection and counterfactual answer as attributed rhetoric.',
'50b:5':'Reread litigant loss, unanswered Shmuel judicial comparison, knowledge question/description, Rav Yehuda ban and reported death; no Rav-Shmuel dispute.'}
if __name__=='__main__':a.save()
