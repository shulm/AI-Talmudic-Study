"""Manually retained unresolved abbreviated-declaration questions and conditions."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r006.';a.OUTPUT='continuation_006b.json'
c=a.c;q=a.q;e=a.edge
a.structure('betrothal',['6b:1','6b:2'],'Rav Pappa’s question concerning abbreviated betrothal')
a.structure('peah',['6b:'+str(i) for i in range(3,7)]+['7a:1'],'Abbreviated peah declarations and the scope of comparison to offerings')
a.structure('charity',['7a:2','7a:3'],'Unresolved abbreviated charity declaration')
a.structure('ownerless',['7a:4','7a:5'],'Conditional extension from charity to ownerless property')
a.structure('privy',['7a:6','7a:7','7a:8'],'Ravina’s nested doubts about designation and abbreviated designation of a privy')
kq=q('kq','6b:1','בעי רב פפא  יש יד לקידושין או לא','Rav Pappa asks whether betrothal can have an abbreviated declaration.',voice='רב פפא')
caseq=q('caseq','6b:1','היכי דמי','What is the case of the question?')
full=c('full','6b:1','אילימא דאמר לה לאשה הרי את מקודשת לי ואמר לחבירתה ואת נמי פשיטא היינו קידושין עצמן','Saying הרי את מקודשת לי to one woman and ואת נמי to the other is full betrothal language, not the disputed abbreviation.',conditions=['first woman explicitly betrothed','second addressed ואת נמי'],scope='Rejected candidate for question, not denial of validity')
short=c('short','6b:1','אלא כגון דאמר לה לאשה הרי את מקודשת לי ואמר לה לחבירתה ואת','The actual case omits נמי: after the first betrothal formula he says ואת to the other woman.',conditions=['second woman addressed only ואת'],scope='Question’s defined factual case')
yes=c('yes','6b:1','מי אמרינן  ואת נמי אמר לה לחבירתה ותפסי בה קידושין לחבירתה','One possibility understands ואת as “you too,” making the second betrothal effective.',mode='queried',conditions=['short second formula ואת'],scope='Unresolved branch of Rav Pappa question')
no=c('no','6b:1','או דלמא  ואת חזאי אמר לה לחבירתה ולא תפסי בה קידושין בחבירתה','The alternative understands ואת as “you observe,” so the second betrothal is ineffective.',mode='queried',conditions=['short second formula ואת'],scope='Unresolved branch, not a rejected answer')
e('short.answer',short,caseq,'answer','6b:1');e('yes.distinction',yes,no,'distinction','6b:1')
contradict=q('contradict','6b:2','ומי מיבעי ליה לרב פפא','Does Rav Pappa really have this doubt?')
prior=q('prior','6b:2','מי סבר שמואל ידים שאין מוכיחות הויין ידים','Did Shmuel consider nonindicative abbreviated declarations effective?',voice='רב פפא')
c('prior.context','6b:2','מדאמר ליה רב פפא לאביי','The discussion reports Rav Pappa addressing his question to Abaye.',scope='Narrated dialogue context; Abaye is addressee, not asserted position holder')
infer=c('infer','6b:2','מכלל דסבירא ליה לרב פפא דיש יד לקידושין','The objection infers from Rav Pappa’s earlier question to Abaye that he accepts abbreviated betrothal.',mode='rejected',scope='Anonymous inference from a reported question, corrected immediately')
reply=c('reply','6b:2','חדא מגו מאי דסבירא ליה לשמואל אמר ליה לאביי','The reply explains that Rav Pappa asked Abaye within what Shmuel holds; this need not establish Rav Pappa’s own conclusion.',scope='Distinguishes interlocutor’s assumed view from questioner’s view')
e('infer.support',infer,contradict,'support','6b:2');e('reply.answer',reply,contradict,'answer','6b:2');e('reply.correction',reply,infer,'correction','6b:2')
pq=q('pq','6b:3','בעי רב פפא  יש יד לפאה או אין יד לפאה','Rav Pappa asks whether peah has an abbreviated declaration.',voice='רב פפא')
pcase=q('pcase','6b:3','היכי דמי','What is the peah case?')
pfull=c('pfull','6b:3','אילימא דאמר הדין אוגיא ליהוי פאה והדין נמי ההיא פיאה מעלייתא היא','Designating one patch as peah and adding והדין נמי for another is full peah designation.',conditions=['explicit first designation','second includes נמי'],scope='Excluded as too explicit to be the question')
pshort=q('pshort','6b:3','כי קא מיבעיא ליה כגון דאמר והדין ולא אמר נמי מאי','What if he says only והדין for the second patch, omitting נמי?',conditions=['second patch','נמי omitted'])
wholeq=q('wholeq','6b:4',None,'Does this imply that declaring the whole field peah is effective?')
whole=c('whole','6b:5',None,'Yes: the cited baraita derives from פאת שדך that one may make the whole field peah.',conditions=['owner wishes to designate entire field'],scope='Answered side-question, distinct from unresolved abbreviated designation')
e('whole.answer',whole,wholeq,'answer','6b:5')
panalog=c('panalog','6b:6','מי אמרינן  כיון דאיתקש לקרבנות מה קרבנות יש להם יד אף פאה יש לה יד','Perhaps peah has abbreviated declarations because it is compared with offerings, which have them.',mode='queried',scope='Unresolved derivation branch')
pdelay=c('pdelay','6b:6','או דלמא כי איתקש לבל תאחר הוא דאיתקש','Perhaps that comparison concerns only delay, and does not establish abbreviated declarations.',mode='queried',scope='Unresolved limitation branch')
where=q('where','6b:6','והיכא איתקש','Where is that comparison made?')
verse=c('verse','6b:6','דתניא','The cited teaching interprets מעמך as gleanings, forgotten produce and peah.',extra=[('7a:1',None)],composition='composite',scope='Cross-page baraita citation with three explicitly enumerated gifts')
e('verse.answer',verse,where,'answer','7a:1');e('panalog.distinction',panalog,pdelay,'distinction','6b:6')
cq=q('cq','7a:2','יש יד לצדקה או אין יד לצדקה','Is there an abbreviated declaration for charity?')
ccase=q('ccase','7a:2','היכי דמי','What is the charity case?')
cfull=c('cfull','7a:2','אילימא דאמר הדין זוזא לצדקה והדין נמי ההוא צדקה עצמה היא','Calling one coin charity and adding והדין נמי for another is itself complete charity language.',conditions=['coin explicitly designated','second includes נמי'])
cshort=q('cshort','7a:2','אלא כגון דאמר הדין ולא אמר נמי מאי','What if הדין is said without נמי for the second coin?',conditions=['second coin','נמי omitted'])
cyes=c('cyes','7a:2','הדין נמי צדקה קאמר','Perhaps the incomplete expression means this coin too is charity.',mode='queried',scope='Unresolved interpretation')
cno=c('cno','7a:2','או דלמא [מאי] והדין (נמי) לנפקותא בעלמא קאמר ודבורא הוא דלא אסקיה','Perhaps it refers instead to ordinary expenditure, and the speaker left his speech unfinished.',mode='queried',scope='Alternative reading; source brackets/parentheses retained')
canalog=c('canalog','7a:3','מי אמרינן  כיון דאיתקש לקרבנות דכתיב (דברים כג כד) בפיך זו צדקה מה קרבנות יש להן יד אף צדקה יש לה יד','Perhaps the בפיך זו צדקה comparison with offerings extends abbreviated declarations to charity.',mode='queried',scope='Unresolved analogy branch, with its explicit verse interpretation')
cdelay=c('cdelay','7a:3','או דלמא לבל תאחר הוא דאיתקש','Perhaps the comparison is only for the prohibition of delay.',mode='queried',scope='Unresolved alternative scope of scriptural comparison')
e('cyes.distinction',cyes,cno,'distinction','7a:2');e('canalog.distinction',canalog,cdelay,'distinction','7a:3')
hq=q('hq','7a:4','יש יד להפקר או דלמא אין יד להפקר','Is an abbreviated declaration effective for ownerless property?')
same=q('same','7a:4','היינו צדקה','Is that not the same question as charity?')
ifc=c('ifc','7a:5','אם תמצא לומר קאמר  אם תמצא לומר יש יד לצדקה דאין היקש למחצה','The ownerless-property question is posed conditionally: suppose charity does have abbreviated declarations because the comparison is not partial.',mode='conditional',conditions=['suppose charity has abbreviated declarations'],scope='Conditional hierarchy of doubts; no positive resolution inferred from אם תמצא לומר')
hsame=c('hsame','7a:5','הפקר מי אמרינן היינו צדקה','Perhaps ownerless property is equivalent to charity for this purpose.',mode='queried',conditions=['conditional affirmative charity branch'])
hdiff=c('hdiff','7a:5','או דלמא שאני צדקה דצדקה לא חזיא אלא לעניים אבל הפקר בין לעניים בין לעשירים','Perhaps charity differs because only the poor qualify, whereas ownerless property is available to both poor and rich.',mode='queried',composition='composite',conditions=['same conditional charity branch'],scope='Explicit two-beneficiary-class contrast in unresolved alternative')
e('ifc.answer',ifc,same,'answer','7a:5');e('hsame.distinction',hsame,hdiff,'distinction','7a:5')
tq=q('tq','7a:6','בעי רבינא  יש יד לבית הכסא או לא','Ravina asks whether abbreviated designation is effective for a privy.',voice='רבינא')
tcase=q('tcase','7a:6','היכי דמי','What is the privy-designation case?')
tfull=c('tfull','7a:6','אילימא דאמר הדין ביתא ליהוי בית הכסא והדין נמי ההוא בית הכסא נמי הוה','If the first house is designated as a privy and the second includes והדין נמי, the second is expressly included.',conditions=['second includes נמי'],scope='Within the designation question, effectiveness of designation itself remains a nested doubt below')
tshort=q('tshort','7a:6','אלא כגון דאמר והדין ולא אמר נמי מאי','What if only והדין is said about the second house?',conditions=['second designation omits נמי'])
tyes=c('tyes','7a:6','הדין דאמר והדין נמי בית הכסא','Perhaps it means this house too is a privy.',mode='queried',scope='Unresolved interpretation')
tno=c('tno','7a:6','או דלמא מאי והדין לתשמישא בעלמא קאמר','Perhaps the second house is intended for ordinary use.',mode='queried',scope='Unresolved alternative interpretation')
known=c('known','7a:7','מכלל דפשיטא ליה לרבינא דיש זימון לבית הכסא','The objection infers that Ravina must already regard designation of a privy as effective.',mode='rejected',scope='Inference challenged by Ravina’s earlier doubt')
oldq=q('oldq','7a:7','והא מיבעיא ליה לרבינא  הזמינו לבית הכסא מהו  הזמינו לבית המרחץ מהו  זימון מועיל או אין זימון מועיל','But Ravina asked whether designation for a privy or bathhouse is effective.',voice='רבינא')
nested=c('nested','7a:8',"רבינא חדא מגו חדא קמיבעיא ליה  זימון מועיל או אין זימון מועיל את''ל יש זימון יש יד או אין יד",'Ravina asks nested questions: first whether designation works, and if it does, whether an abbreviated designation works.',composition='composite',conditions=['second question conditional on first affirmative'],scope='Anonymous explanation of Ravina’s doubts; no assumed affirmative resolution')
open=c('open','7a:8','תיבעי ליה:','The discussion leaves the question for inquiry.',mode='unresolved',scope='Explicit local unresolved ending; not a historical decision')
e('nested.correction',nested,known,'correction','7a:8');e('tyes.distinction',tyes,tno,'distinction','7a:6')
a.notes={
'6b:1':'Reread named main question, explicit/abbreviated cases and both legal outcomes; no forced answer.',
'6b:2':'Reread prior question to Abaye, inferred personal stance and correction distinguishing Shmuel’s assumed view.',
'6b:3':'Reread named peah question, full formulation and abbreviated formulation; second remains open.',
'6b:4':'Reread whole-field implication question, distinct from main abbreviation question.',
'6b:5':'Reread affirmative whole-field baraita and source verse.',
'6b:6':'Reread competing scope of analogy and derivation-source question; baraita continues7a:1.',
'7a:1':'Reread all three poor-gift items in cross-page citation; no fabricated answer to main peah doubt.',
'7a:2':'Reread charity main question, explicit/short formulas, charity/ordinary-expenditure alternatives and source brackets.',
'7a:3':'Reread both analogy scopes and בפיך interpretation as unresolved branches.',
'7a:4':'Reread ownerless-property question and redundancy objection.',
'7a:5':'Reread conditional question hierarchy and poor/rich distinction; אם תמצא לומר not converted into final ruling.',
'7a:6':'Reread Ravina question, explicit/short designation and both interpretations.',
'7a:7':'Reread inference of certainty and earlier privy/bathhouse doubt; no fabricated resolution.',
'7a:8':'Reread nested designation/abbreviation doubts and תיבעי ליה unresolved ending.'}
if __name__=='__main__':a.save()
