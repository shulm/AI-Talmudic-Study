"""Manually authored hyperbole, oath intention, embedded cane narrative and beam shape."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r025.';a.OUTPUT='continuation_025.json'
c=a.c;q=b.q;e=a.edge
a.structure('oath',['24b:'+str(i) for i in range(3,8)]+['25a:'+str(i) for i in range(1,15)],'Hyperbolic vows versus oaths, shared intention and alternative oath wording')
a.structure('snake',['25a:15','25a:16'],'Snake and oil-press beam comparison: flattened back and commercial implication')
crowd=c('crowd','24b:3','נדרי הבאי אמר קונם אם לא ראיתי בדרך הזה כעולי מצרים','The Mishnah exemplifies hyperbolic vows by a konam conditioned on not having seen a crowd like those who left Egypt on this road.',scope='Quoted illustrative condition; not verification of an actual crowd')
snake=c('snake','24b:3','אם לא ראיתי נחש כקורת בית הבד','The second hyperbole example is a snake like an oil-press beam.',scope='Shape clarification follows25a:15–16; not merely length')
vows=c('vows','24b:4','תנא נדרי הבאי מותרין','A teaching permits hyperbolic vows.',scope='Source’s category-specific rule')
oaths=c('oaths','24b:4','שבועות הבאי אסורין','The same teaching prohibits hyperbolic oaths.',scope='Form of oath disputed immediately below')
form=q('form','24b:5','היכי דמי שבועות הבאי','What form constitutes a hyperbolic oath here?')
incomplete=c('incomplete','24b:5','אילימא דאמר שבועה אם לא ראיתי בדרך הזה מידעם קאמר','The conditional wording שבועה אם לא ראיתי בדרך הזה is challenged as failing to say anything operative.',mode='challenged',scope='Rejected initial formulation, not the final oath case')
abaye=c('abaye','24b:6','אמר אביי דאמר שבועה שראיתי','Abaye proposes an oath that he saw the described sight.',holder='אביי',mode='challenged',scope='Proposal challenged by Rava')
obvious=q('obvious','24b:6','אמר ליה רבא אם כן למה לי למימר','Rava asks why such a prohibition needs to be stated.',voice='רבא')
parallel=c('parallel','24b:6','ועוד דומיא דנדר קתני','Rava further objects that the teaching describes an oath analogous to the vow.',holder='רבא',mode='challenged',scope='Objection to Abaye’s formulation')
rava=c('rava','24b:6','אלא אמר רבא באומר ייאסרו פירות העולם עלי בשבועה אם לא ראיתי בדרך הזה כעולי מצרים','Rava explains an oath prohibiting the world’s produce to the speaker if he did not see on this road a crowd like those who left Egypt.',holder='רבא',conditions=['specified conditional oath wording'])
e('abaye.answer',abaye,form,'answer','24b:6');e('parallel.objection',parallel,abaye,'objection','24b:6');e('rava.answer',rava,form,'answer','24b:6');e('rava.answer2',rava,obvious,'answer','24b:6')
ants=q('ants','24b:7','אמר ליה רבינא לרב אשי ודילמא האי גברא קינא דשומשמני חזא ואסיק להון שמא עולי מצרים ושפיר משתבע','Ravina asks Rav Ashi whether the man saw an ant colony, named them those who left Egypt, and swore truthfully.',voice='רבינא')
common=c('common','25a:1','אמר ליה כי משתבע אדעתא דידן משתבע ואנן לא מסקינן נפשין אשומשמני','Rav Ashi answers that the oath follows the listeners’ understanding, which does not identify the people with ants.',holder='רב אשי',scope='Answer to proposed private renaming')
e('common.answer',common,ants,'answer','25a:1')
private=q('private','25a:2','ועל דעתא דנפשיה לא עביד איניש דמשתבע','Do people not swear according to their private intention?')
court=c('court','25a:2','והתניא כשהן משביעין אותו אומרים לו הוי יודע שלא על תנאי שבלבך אנו משביעין אותך אלא על דעתינו ועל דעת בית דין','A cited judicial oath warning specifies the administrators’ and court’s intention rather than the swearer’s private condition.',scope='Quoted formula, challenged interpretation follows')
sticks=q('sticks','25a:2','לאפוקי מאי לאו לאפוקי דאסיק להו לאיסקונדרי ואסיק להון שמא זוזי','Is this to exclude someone naming pieces of wood coins?')
infer=c('infer','25a:3','ומדקאמר על דעתינו מכלל דעביד אינש דמשתבע אדעתא דנפשיה','The argument infers from the warning that people can swear with their own private meaning.',mode='challenged',scope='Inference from proposed explanation, deflected by cane narrative')
cane=c('cane','25a:4','לא לאפוקי מקניא דרבא','The answer says the warning instead excludes the maneuver in Rava’s cane incident.',scope='Deflection of private lexical-renaming proof')
e('cane.answer',cane,private,'answer','25a:4');e('cane.answer2',cane,sticks,'answer','25a:4');e('cane.correction',cane,infer,'correction','25a:4')
debt=c('debt','25a:4','דההוא גברא דהוה מסיק בחבריה זוזי אתא לקמיה דרבא','A creditor brings a monetary claim against another before Rava.',scope='Embedded narrative setting')
pay=c('pay','25a:4','אמר ליה ללווה זיל פרע לי','The narrative records the demand to the debtor זיל פרע לי.',scope='Exact demand retained; this clause does not explicitly name its speaker')
paid=c('paid','25a:4','אמר ליה פרעתיך','The debtor claims he already repaid.',scope='Reported litigant claim, not independently established repayment')
swear=c('swear','25a:4','אמר ליה רבא אם כן זיל אישתבע ליה דפרעתיה','Rava directs him, if so, to swear to repayment.',holder='רבא',conditions=['debtor claims repayment'])
hide=c('hide','25a:5','אזל ואייתי קניא ויהיב זוזי בגויה','The debtor brings a cane and puts money inside it.',scope='Preparatory action in narrative of deceptive compliance')
lean=c('lean','25a:5','והוה מסתמיך ואזיל ואתי עליה לבי דינא','He leans on the cane while going to court.',scope='Narrative physical action')
hold=c('hold','25a:5','אמר ליה למלוה נקוט האי קניא בידך','He asks the creditor to hold the cane.',scope='Debtor’s request gives creditor temporary possession')
oath=c('oath','25a:5','נסב ספר תורה ואישתבע דפרעיה כל מה דהוה ליה בידיה','He takes a Torah scroll and swears that he repaid everything owed.',composition='composite',scope='Narrative ritual action and assertion, with concealed money temporarily held by creditor')
breakc=c('break','25a:6','ההוא מלוה רגז ותברה לההוא קניא','The creditor becomes angry and breaks the cane.',composition='composite',scope='Narrated reaction, not an endorsed action')
spill=c('spill','25a:6','ואישתפך הנהו זוזי לארעא','The concealed money spills onto the ground.',scope='Discovery event')
literal=c('literal','25a:6','ואישתכח דקושטא אישתבע','The account says his oath was found literally true.',scope='Narrative exposes maneuver; it is the conduct the court’s intention clause excludes')
mosesq=q('mosesq','25a:7','ואכתי לא עביד דמישתבע אדעתא דנפשיה','Does another source still show swearing with private intention?')
moses=c('moses','25a:7',"והתניא וכן מצינו במשה רבינו כשהשביע את ישראל בערבות מואב אמר להם הוו יודעים שלא על דעתכם אני משביע אתכם אלא על דעתי ועל דעת המקום שנאמר ולא אתכם לבדכם וגו' (דברים כט יג)",'A baraita reports Moses warning Israel in the plains of Moab that his oath follows his and God’s intention, citing ולא אתכם לבדכם.',holder='משה רבינו',composition='composite',scope='Embedded reported speech plus citation; historical claim attributed to the baraita')
idols=q('idols','25a:8','לאפוקי מאי לאו לאפוקי דאסיקו שמא לעבודת כוכבים אלוה','Was Moses excluding privately calling an idol god?')
inferred=c('inferred','25a:8','מכלל דעביד איניש דמשתבע אדעתא דנפשיה','The proposed reading infers that people may swear using private intention.',mode='challenged',scope='Second proposed private-renaming inference')
normal=c('normal','25a:9',None,'The reply says idols are actually called gods in Scripture, citing ובכל אלהי מצרים.',scope='Normal attested lexical use, not proof of private renaming')
e('normal.answer',normal,idols,'answer','25a:9');e('normal.answer2',normal,mosesq,'answer','25a:9');e('normal.correction',normal,inferred,'correction','25a:9')
commands=q('commands','25a:10','ולשבע יתהון דמקיימיתון מצוות','Why not make them swear to keep commandments?')
royal=c('royal','25a:10','משמע מצוַת המלך','That wording could mean the king’s command.',scope='Ambiguity of proposed oath formulation')
allq=q('allq','25a:11','ולשבע יתהון דמקיימיתון כל מצוות','Why not say all commandments?')
fringes=c('fringes','25a:11','משמע מצוַת ציצית','That could mean the commandment of fringes.',scope='Proposed ambiguity explained by next quoted maxim')
equal=c('equal','25a:11','דאמר מר שקולה מצוַת ציצית כנגד כל מצוות שבתורה','An unnamed cited authority says fringes equal all the Torah’s commandments.',scope='Quoted valuation supplies lexical rationale, not a practical exemption from other commandments')
torahq=q('torahq','25a:12','ולשבע יתהון דמקיימיתון תורה','Why not swear to uphold Torah?')
one=c('one','25a:12','משמע תורה אחת','It could mean one teaching.',scope='Ambiguity of singular תורה')
pluralq=q('pluralq','25a:12','ולשבע יתהון דמקיימיתון תורות','Why not use plural teachings?')
offerings=c('offerings','25a:12','משמע תורת מנחה תורת חטאת תורת אשם','It could mean only the laws of meal, sin and guilt offerings.',composition='composite',scope='Enumerated examples of restricted plural reading')
bothq=q('bothq','25a:12','ולשבע יתהון דמקיימיתון [תורות] ומצוות','Why not combine teachings and commandments?',conditions=['printed bracketed תורות retained'])
both=c('both','25a:12','[תורות] משמע תורת המנחה מצוות משמע מצות המלך','The combined formula could still mean the meal-offering teaching and royal commands.',composition='composite',scope='Printed bracketed wording retained without emendation')
wholeq=q('wholeq','25a:13','ולשבע יתהון דמקיימיתון תורה כולה','Why not say the entire Torah?')
idolonly=c('idolonly','25a:13','תורה כולה משמע עבודת כוכבים','Even the entire Torah could be understood through the command concerning idolatry.',scope='Lexical argument about the proposed oath, explained by following baraita')
denial=c('denial','25a:13','דתניא חמורה עבודת כוכבים שכל הכופר בה כאילו מודה בתורה כולה','The cited baraita says idolatry is so grave that denying it is as though affirming the entire Torah.',scope='Quoted equivalence used in oath-wording argument')
explicit=q('explicit','25a:14','ולשבע יתהון דמקיימיתון עבודת כוכבים ותורה כולה אי נמי שש מאות ושלוש עשרה מצוות','Why not specify idolatry and the entire Torah, or 613 commandments?')
brief=c('brief','25a:14','אלא משה רבינו מילתא דלא טריחא נקט','The conclusion says Moses chose a formulation that was not cumbersome.',scope='Final wording rationale after alternative formulations; not claim that all explicit formulations fail')
for key,answer,question,ref in [('royal',royal,commands,'25a:10'),('fringes',fringes,allq,'25a:11'),('one',one,torahq,'25a:12'),('offerings',offerings,pluralq,'25a:12'),('both',both,bothq,'25a:12'),('idolonly',idolonly,wholeq,'25a:13'),('brief',brief,explicit,'25a:14')]:e(key+'.answer',answer,question,'answer',ref)
e('equal.support',equal,fringes,'support','25a:11');e('denial.support',denial,idolonly,'support','25a:13')
exist=q('exist','25a:15','ולא והא ההוא חויא דהוה בשני שבור מלכא רמו ליה תליסר אורוותא דתיבנא ובלע יתהון','Does the snake example really exaggerate, given the reported snake in Shapur’s time that swallowed thirteen loads of straw?',conditions=['reported narrative challenges the scale interpretation'])
flat=c('flat','25a:15','אמר שמואל בטרוף','Shmuel explains that the comparison concerns flattening.',holder='שמואל',scope='First compressed explanation, refined to the back below')
allflat=q('allflat','25a:15','כולהו נחשי מיטרף טרפי','Are not all snakes flattened?')
back=c('back','25a:15','אגבו טרוף קאמרינן','The answer specifies a flattened back.',scope='Anonymous clarification of Shmuel’s explanation')
e('flat.answer',flat,exist,'answer','25a:15');e('back.answer',back,allflat,'answer','25a:15');e('back.qualification',back,flat,'qualification','25a:15')
sayq=q('sayq','25a:16','ולתני טרוף','Why does the Mishnah not simply say flattened?')
beam=c('beam','25a:16','מילתא אגב אורחיה קא משמע לן דקורת בית הבד גבו טרוף','The comparison incidentally teaches that an oil-press beam has a flattened back.',scope='Explanation of chosen comparison')
useq=q('useq','25a:16','למאי נפקא מינה','What practical difference does the beam’s shape make?')
sale=c('sale','25a:16','למקח וממכר לומר לך המוכר קורת בית הבד לחבירו אי גבו טרוף אין ואי לא לא','In sale of an oil-press beam, one with a flattened back meets the description and one without it does not.',conditions=['sale designated as an oil-press beam'],composition='composite',scope='Explicit commercial application of the descriptive feature')
e('beam.answer',beam,sayq,'answer','25a:16');e('sale.answer',sale,useq,'answer','25a:16')
a.notes={
'24b:3':'Reread both hyperbole examples and followed snake comparison through25a:16.',
'24b:4':'Reread permitted vows/prohibited oaths contrast without conflation.',
'24b:5':'Reread explicit form question and challenged incomplete conditional wording.',
'24b:6':'Reread Abaye proposal, both Rava objections and replacement conditional fruit prohibition.',
'24b:7':'Reread Ravina-to-Rav Ashi ant-colony private-renaming question.',
'25a:1':'Reread common-intention answer and maintained interlocutor attribution.',
'25a:2':'Reread private-intention objection, full judicial oath formula and wood/coins proposed interpretation.',
'25a:3':'Reread inference as challenged by following cane explanation.',
'25a:4':'Reread cane answer and complete court dialogue; unexpressed demand speaker left unspecified.',
'25a:5':'Reread concealment, leaning, creditor holding cane, scroll and oath actions separately.',
'25a:6':'Reread anger, breakage, spilled money and literal-truth conclusion in anti-evasion context.',
'25a:7':'Reread renewed question and baraita Moses setting, speech and source citation.',
'25a:8':'Reread proposed private-idol-naming interpretation and challenged inference.',
'25a:9':'Reread attested biblical terminology answer; private renaming inference not accepted.',
'25a:10':'Reread commandments proposal and royal-command ambiguity.',
'25a:11':'Reread all-commandments proposal, fringes answer and unnamed equivalence maxim.',
'25a:12':'Reread all three proposals and replies, preserving bracketed text and offering list.',
'25a:13':'Reread entire-Torah proposal and idolatry-denial equivalence with its source attribution.',
'25a:14':'Reread two explicit alternatives and final noncumbersome-formulation explanation.',
'25a:15':'Reread Shapur-era snake report as source-reported challenge, Shmuel answer, second question and flattened-back clarification.',
'25a:16':'Reread wording question, incidental beam shape teaching, practical-difference question and both sale branches.'}
if __name__=='__main__':a.save()
