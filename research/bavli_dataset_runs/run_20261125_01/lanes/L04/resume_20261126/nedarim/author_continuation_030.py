"""Commercial benefit and inspection/broker liability with rejected market assumptions."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r030.';a.OUTPUT='continuation_030.json'
c=a.c;q=b.q;e=a.edge
a.structure('market',['31a:'+str(i) for i in range(9,14)]+['31b:'+str(i) for i in range(1,6)],'Benefit in trades, market demand and outward/return liability')
receive=c('receive','31a:9','שאיני נהנה מישראל לוקח ביותר ומוכר בפחות','One who vows against receiving benefit from Israel buys above and sells below the normal price.',composition='composite',scope='First directional vow; ordinary-demand goods specified31b:1')
give=c('give','31a:9','שישראל נהנין לי לוקח בפחות ומוכר ביותר','One who prohibits Israel’s benefit from him buys below and sells above the normal price.',composition='composite',scope='Reverse directional vow')
refuse=c('refuse','31a:9','ואין שומעין לו','Others do not agree to his terms.',scope='Mishnah’s practical observation following unfavorable prices')
mutual=c('mutual','31a:9','שאיני נהנה להן והן לי יהנה לנוכרים','Where benefit is prohibited in both directions, dealings for benefit are with non-Jews.',scope='Mutual vow category in Mishnah, not general commercial recommendation')
shmuel=c('shmuel','31a:10','אמר שמואל הלוקח כלי מן האומן לבקרו ונאנס בידו חייב','Shmuel makes someone taking an artisan’s vessel for inspection liable for unavoidable loss in his possession.',holder='שמואל',scope='Later restricted to high-demand goods31b:1')
buyer=c('buyer','31a:10','אלמא קסבר הנאת לוקח היא','The discussion infers that the benefit lies with the prospective buyer.',mode='conditional',scope='Inference from Shmuel’s liability ruling, qualified by market demand')
whyq=q('whyq','31a:11','תנן שאיני נהנה מישראל מוכר בפחות אבל שווה בשווה לא ואי הנאת לוקח היא אפילו שוה בשוה','If benefit belongs to the buyer, why does the Mishnah require one prohibited from receiving benefit to sell below rather than at equal value?')
slow=c('slow','31a:11','מתניתין בזבינא דרמי על אפיה','The first answer places the Mishnah in unwanted goods.',mode='rejected',scope='Provisional low-demand explanation, displaced by final intermediate-market account')
e('slow.answer',slow,whyq,'answer','31a:11')
slowq=q('slowq','31a:12',None,'How can low demand explain buying above value and the reverse-vow rule requiring selling above value rather than at equal value?',conditions=['printed bracketed לוקח בפחות preserved'])
fast=c('fast','31a:13','סיפא בזבינא חריפא','The next proposal makes the final clause high-demand goods.',mode='rejected',scope='Partial reconstruction challenged immediately')
fastq=q('fastq','31a:13','אי הכי לוקח בפחות אפילו שווה בשווה','Then why require buying below value rather than at equal value?')
mid=c('mid','31b:1','מתניתין בזבינא מיצעא','The final answer locates the Mishnah in goods with intermediate demand.',scope='Final uniform market condition for Mishnah’s price distinctions')
high=c('high','31b:1','ודשמואל בזבינא חריפא','Shmuel’s inspection rule concerns high-demand goods.',conditions=['high-demand goods'],scope='Final limitation on buyer-benefit inference')
e('fast.answer',fast,slowq,'answer','31a:13');e('mid.answer',mid,fastq,'answer','31b:1');e('mid.answer2',mid,whyq,'answer','31b:1');e('mid.correction',mid,slow,'correction','31b:1');e('high.qualification',high,shmuel,'qualification','31b:1')
gifts=c('gifts','31b:2','הלוקח כלים מן התגר לשגרן לבית חמיו ואמר לו אם מקבלין אותן ממני אני נותן לך דמיהם ואם לאו אני נותן לך לפי טובת הנאה שבהן','A supporting baraita concerns taking vessels to send to his father-in-law’s household, paying full price if accepted and otherwise paying for the benefit received.',composition='composite',scope='Express two-branch arrangement with merchant')
out=c('out','31b:2','נאנסו בהליכה חייב','He is liable for unavoidable loss on the outward trip.',conditions=['specified vessel arrangement','outward journey'])
back=c('back','31b:3',None,'On return he is exempt from unavoidable-loss liability because he is like a paid custodian.',conditions=['return trip'],scope='Exemption is for the stated unavoidable loss; not all custodian duties')
e('out.support',out,shmuel,'support','31b:2')
broker=c('broker','31b:4','ההוא ספסירא דשקל חמרא לזבוני ולא איזבן בהדי דהדר איתניס חמרא','A broker takes חמרא for sale, fails to sell it, and it suffers unavoidable loss on the return.',composition='composite',scope='Exact חמרא retained without resolving wine/donkey vocalization from unpointed excerpt')
nahman=c('nahman','31b:4','חייביה רב נחמן לשלומי','Rav Nahman orders the broker to pay.',holder='רב נחמן',scope='Narrative ruling despite physical return journey')
ob=q('ob','31b:4','איתיביה רבא לרב נחמן נאנסו בהליכה חייב בחזרה פטור','Rava objects to Rav Nahman from the baraita’s outward liability and return exemption.',voice='רבא')
returnc=c('return','31b:5',None,'Rav Nahman treats this broker’s return as outward travel because he would still sell if he found a buyer even at his own doorway.',holder='רב נחמן',scope='Continuing sale opportunity distinguishes broker from completed gift inspection')
e('return.answer',returnc,ob,'answer','31b:5');e('return.support',returnc,nahman,'support','31b:5')
a.notes={
'31a:9':'Reread both price-direction rules, refusal observation and mutual-benefit alternative.',
'31a:10':'Reread Shmuel inspection liability and buyer-benefit inference with later market condition.',
'31a:11':'Reread equal-value challenge and initial unwanted-goods answer.',
'31a:12':'Reread both objections to low-demand reconstruction and bracketed clause.',
'31a:13':'Reread proposed high-demand final clause, immediate counterquestion and dangling אלא.',
'31b:1':'Reread final intermediate Mishnah/high-demand Shmuel distinction.',
'31b:2':'Reread supporting conditional gift arrangement and outward loss liability.',
'31b:3':'Reread return exemption specifically for unavoidable loss and paid-custodian rationale.',
'31b:4':'Reread broker narrative, unpointed חמרא, Nahman ruling and Rava baraita objection.',
'31b:5':'Reread functional return-as-outward answer and doorway sale counterfactual.'}
if __name__=='__main__':a.save()
