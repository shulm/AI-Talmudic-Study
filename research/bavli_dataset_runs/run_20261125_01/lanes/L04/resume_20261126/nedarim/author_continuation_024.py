"""Individually read annual conditions and urging-vow proof sequence."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r024.';a.OUTPUT='continuation_024d.json'
c=a.c;e=a.edge
def q(key,ref,quote,text,voice=None,conditions=()):
    ident=a.q(key,ref,quote,text,voice=voice,conditions=conditions)
    row=next(x for x in a.records if x['id']==ident)
    row['content']['answer_set_status']='partial'
    row['uncertainty'].append('Source-present response is recorded; the answer set is not certified exhaustive.')
    return ident
a.structure('condition',['23a:8','23a:9']+['23b:'+str(i) for i in range(1,5)],'Annual advance conditions: reconstructed Mishnah and alternative readings')
a.structure('proofs',['23b:5']+['24a:'+str(i) for i in range(1,10)]+['24b:1','24b:2'],'Whether sages dispute Rabbi Eliezer ben Yaakov and the local ruling')
m=c('m','23a:8','רבי אליעזר בן יעקב אומר אף הרוצה להדיר את חבירו שיאכל אצלו יאמר לו כל נדר שאני עתיד לידור הוא בטל ובלבד שיהא זכור בשעת הנדר','Rabbi Eliezer ben Yaakov presents an advance declaration voiding future vows in connection with urging a friend to eat, conditioned on remembering when vowing.',holder='רבי אליעזר בן יעקב',composition='composite',scope='Printed Mishnah formulation; reconstruction and two readings follow')
ob=q('ob','23a:9','וכיוון דאמר כל נדר שאני עתיד לידור יהא בטל לא שמע ליה ולא אתי בהדיה','If he announces that future vows are void, why would the friend listen and come?')
urge=c('urge','23b:1','הרוצה שיאכל אצלו חבירו ומסרב בו ומדירו נדרי זירוזין הוא','The reconstructed teaching treats a vow made while pressing a friend to eat as an urging vow.',scope='First clause of explicit חסורי מיחסרא reconstruction')
annual=c('annual','23b:1','והרוצה שלא יתקיימו נדריו כל השנה יעמוד בראש השנה ויאמר כל נדר שאני עתיד לידור יהא בטל','The second reconstructed clause permits one seeking to prevent the year’s vows from standing to declare at the year’s beginning that future vows are void.',scope='Separate purpose from hospitality; ensuing memory condition disputed')
remember=c('remember','23b:1','ובלבד שיהא זכור בשעת הנדר','The reconstructed text retains the condition of remembering when vowing.',scope='Literal condition before Abaye and Rava explain it')
e('urge.answer',urge,ob,'answer','23b:1');e('annual.correction',annual,m,'correction','23b:1')
memory=q('memory','23b:2','אי זכור עקריה לתנאיה וקיים ליה לנדריה','Would remembering the condition mean that the later vow overrides it and stands?')
abaye=c('abaye','23b:2','אמר אביי תני ובלבד שלא יהא זכור בשעת הנדר','Abaye reads the condition as not remembering at the time of the vow.',holder='אביי',scope='Explicit תני correction, not silently substituted into quoted Mishnah')
rava=c('rava','23b:3','רבא אמר לעולם כדאמרינן מעיקרא הכא במאי עסקינן כגון שהתנה בראש השנה ולא ידע במה התנה','Rava retains the original reading and places it where one made an annual condition but does not know what was stipulated.',holder='רבא',scope='Alternative explanation of retained wording')
invoke=c('invoke','23b:3','אי זכור בשעת הנדר ואמר על דעת הראשונה אני נודר נדריה לית ביה ממשא','If at the vow he remembers and invokes his original intention, the vow has no substance.',holder='רבא',conditions=['earlier condition whose content was forgotten','explicit invocation of original intention'],scope='Rava’s conditional branch')
omit=c('omit','23b:3','לא אמר על דעת הראשונה אני נודר עקריה לתנאיה וקיים לנדריה','If he does not invoke his original intention, he overrides the condition and establishes the vow.',holder='רבא',conditions=['Rava’s described case','no invocation of original intention'])
e('abaye.answer',abaye,memory,'answer','23b:2');e('rava.answer',rava,memory,'answer','23b:3');e('rava.distinction',rava,abaye,'distinction','23b:3')
public=c('public','23b:4','רב הונא בר חיננא סבר למידרשיה בפירקא','Rav Huna bar Hinnana considers publicly expounding this teaching.',scope='Narrated intention, not a completed public sermon')
oppose=c('oppose','23b:4','אמר ליה רבא תנא קא מסתים לה סתומי כדי שלא ינהגו קלות ראש בנדרים ואת דרשת ליה בפירקא','Rava objects that the tanna concealed it to prevent frivolity toward vows, whereas he proposes teaching it publicly.',holder='רבא',scope='Rhetorical objection with explicit rationale')
e('oppose.objection',oppose,public,'objection','23b:4')
dispute=q('dispute','23b:5','איבעיא להו פליגי רבנן עליה דרבי אליעזר בן יעקב או לא','Do the sages disagree with Rabbi Eliezer ben Yaakov?')
law=q('law','23b:5','ואם תימצי לומר פליגי הלכתא כוותיה או לא','If they disagree, is the ruling in accordance with him?',conditions=['sages disagree'])
gift=c('gift','24a:1','קונם שאיני נהנה לך אם אי אתה נוטל לבנך כור של חיטין ושתי חביות של יין','The cited case prohibits the speaker’s benefit from his friend unless the friend accepts for his son a kor of wheat and two barrels of wine.',conditions=['specified gift not accepted'],scope='Citation introduced by23b:5 האומר לחבירו; exact pronoun directions retained')
honor=c('honor','24a:1','הרי זה יכול להתיר את נדרו שלא על פי חכם שיכול לומר לו כלום אמרת אלא בשביל כבודי זה הוא כבודי','The recipient can resolve this without a sage by saying the proposal was for his honor and that declining is his honor.',composition='composite',scope='Cited mechanism, not general self-annulment')
infer=c('infer','24a:2','טעמא דאמר זה הוא כבודי הא לאו הכי נדר הוא','The discussion infers that without the honor declaration the vow would stand.',mode='challenged',scope='Proposed evidence toward disagreement; next segment deflects it')
proof=c('proof','24a:2','מני אי רבי אליעזר בן יעקב נדרי זירוזין הוי אלא שמע מינה פליגי רבנן עליה','The initial proof reasons that Rabbi Eliezer ben Yaakov would treat it as urging, so the cited rule must show sages disagreeing.',mode='rejected',composition='composite',scope='Rejected proof of authorial identification')
deflect=c('deflect','24a:3','לעולם רבי אליעזר בן יעקב היא ומודה רבי אליעזר בן יעקב בהאי דנדרא הוי','The reply permits attribution to Rabbi Eliezer ben Yaakov: he agrees that this case creates an actual vow.',scope='Deflection, not denial that sages disagree elsewhere')
dog=c('dog','24a:3','דאמר ליה לא כלבא אנא דמיתהנינא מינך ולא מיתהנית מינאי','The rationale is the speaker’s objection to benefiting from the other without reciprocating, expressed as לא כלבא אנא.',scope='Quoted rationale in hypothetical vow dialogue')
e('proof.support',proof,dispute,'support','24a:2');e('deflect.rejection',deflect,proof,'correction','24a:3');e('dog.support',dog,deflect,'support','24a:3')
give=c('give','24a:4','האומר לחבירו קונם שאתה נהנית לי אם אי אתה נותן לבני כור של חיטין ושתי חביות של יין','A second cited case prohibits the friend’s benefit from the speaker unless the friend gives the speaker’s son a kor of wheat and two barrels of wine.',conditions=['specified gift not given'],scope='Reversed direction from previous gift case')
meir=c('meir','24a:4','רבי מאיר אומר עד שיתן','Rabbi Meir requires actual giving.',holder='רבי מאיר',scope='Second cited conditional-gift case')
sages=c('sages','24a:4','וחכמים אומרים אף זה יכול להתיר את נדרו שלא על פי חכם שיכול לומר הריני כאילו התקבלתי','The sages permit resolution without a sage through the declaration that it is as though he has received the gift.',holder='חכמים',scope='Specific acceptance-substitute declaration')
e('sages.dispute',sages,meir,'objection','24a:4')
infer2=c('infer2','24a:5','טעמא דאמר הריני כאילו התקבלתי הא לאו הכי נדר הוא','The discussion infers that absent the receipt declaration this vow stands.',mode='challenged',scope='Second proposed proof')
proof2=c('proof2','24a:5','מני אי רבי אליעזר בן יעקב נדרי זירוזין הוי אלא לאו רבנן ופליגי','The proof again proposes that sages other than Rabbi Eliezer ben Yaakov must be responsible and disagree with him.',mode='rejected',scope='Deflected next segment')
deflect2=c('deflect2','24a:6','לא לעולם רבי אליעזר בן יעקב ומודה רבי אליעזר בהאי דנדרא הוי','The reply again allows Rabbi Eliezer ben Yaakov to regard this case as an actual vow.',scope='Printed shortened רבי אליעזר in repeated clause is contextual, not a new disputant')
king=c('king','24a:6','משום דאמר ליה לאו מלכא אנא דמהנינא לך ואת לא מהנית לי','The rationale is the speaker’s objection to giving benefit without receiving benefit, expressed as לאו מלכא אנא.',scope='Reciprocity rationale, distinct direction from dog comparison')
e('proof2.support',proof2,dispute,'support','24a:5');e('deflect2.rejection',deflect2,proof2,'correction','24a:6');e('king.support',king,deflect2,'support','24a:6')
force=c('force','24a:7','נדרי אונסין הדירו חבירו שיאכל אצלו וחלה הוא או חלה בנו או שעכבו נהר','Mar Kashisha son of Rav Hisda cites to Rav Ashi a meal vow prevented by illness of the person or his son, or by a river.',holder='מר קשישא בריה דרב חסדא',composition='composite',scope='Three alternative compulsion grounds in cited teaching')
proof3=c('proof3','24a:7','הא לאו הכי נדר הוא מני אי רבי אליעזר בן יעקב זירוזין הוי אלא לאו רבנן ופליגי','He proposes that because absent compulsion the vow stands, the teaching establishes sages disagreeing with Rabbi Eliezer ben Yaakov.',holder='מר קשישא בריה דרב חסדא',mode='rejected',scope='Third proof, rejected by reversing assumed vow direction')
deflect3=c('deflect3','24a:8','לעולם רבי אליעזר בן יעקב ומי סברת דאדריה מזמנא לזמינא לא דזמינא אדריה למזמנא','The response retains Rabbi Eliezer ben Yaakov and reverses the assumed direction: the prospective guest made the host vow, rather than host imposing on guest.',scope='Explicit correction of the hypothesized interaction')
host=c('host','24a:8','דאמר ליה מזמנת לי לסעודתיך אמר ליה אין נדר זה עליך ונדר','The guest asks whether he has been invited, receives assent, and demands a vow, which the host makes.',composition='composite',scope='Reconstructed dialogue supporting reversed direction')
unable=c('unable','24a:8','וחלה הוא או שחלה בנו או שעכבו נהר הרי אלו נדרי אונסין','Illness of him or his son, or obstruction by a river, then makes this a compulsion vow.',composition='composite',conditions=['reconstructed host vow','one of three stated impediments'])
e('proof3.support',proof3,dispute,'support','24a:7');e('deflect3.rejection',deflect3,proof3,'correction','24a:8')
more=c('more','24a:9','יתר על כן אמר רבי אליעזר בן יעקב האומר לחבירו קונם שאני נהנה לך אם אי אתה מתארח אצלי ותאכל עמי פת חמה ותשתה עמי כוס חמין והלה הקפיד כנגדו אף אלו נדרי זירוזין','A further teaching of Rabbi Eliezer ben Yaakov treats as urging vows a benefit prohibition unless the friend accepts hospitality, warm bread and a warm cup, where the friend reacts insistently in return.',holder='רבי אליעזר בן יעקב',composition='composite',scope='Explicit multi-clause case; direction retained from printed שאני נהנה לך')
no=c('no','24a:9','ולא הודו לו חכמים','The sages did not agree with him.',holder='חכמים',scope='Explicit nonagreement in cited further case')
meaning=q('meaning','24a:9','מאי לא הודו לו חכמים לאו','Does their nonagreement extend even to the earlier case?',conditions=['sentence completed24b:1'])
for row in a.records:
    if row['id'] in [meaning,a.PREFIX+'meaning.u',a.PREFIX+'meaning.a']:
        row['evidence'].append(a.ev('24b:1','דאפילו בקמייתא'))
final=c('final','24b:1','דאפילו בקמייתא ושמע מינה פליגי רבנן עליה שמע מינה','The conclusion accepts that the sages disagree even in the earlier case.',scope='Accepted שמע מינה after three deflected proofs')
e('no.dispute',no,more,'objection','24a:9');e('final.answer',final,meaning,'answer','24b:1');e('final.answer2',final,dispute,'answer','24b:1')
outcome=q('outcome','24b:2','מאי הוי עלה','What is the ruling on the matter?')
huna=c('huna','24b:2','דאמר רב הונא הלכה כרבי אליעזר בן יעקב','Rav Huna rules according to Rabbi Eliezer ben Yaakov.',holder='רב הונא',scope='Local resolution of urging-vow dispute')
adda=c('adda','24b:2','וכן אמר רב אדא בר אהבה הלכה כרבי אליעזר בן יעקב','Rav Adda bar Ahava gives the same ruling.',holder='רב אדא בר אהבה',scope='Separate agreeing occurrence, not a dispute with Rav Huna')
for key,claim in [('huna',huna),('adda',adda)]:
    e(key+'.answer',claim,outcome,'answer','24b:2');e(key+'.law',claim,law,'answer','24b:2')
a.notes={
'23a:8':'Reread exact Mishnah with memory condition, retained as composite and read both subsequent explanations.',
'23a:9':'Reread hospitality objection; reconstructed clauses provide source response.',
'23b:1':'Reread explicit חסורי מיחסרא separating hospitality from annual declaration and retained memory wording.',
'23b:2':'Reread condition-overriding objection and Abaye negative-memory emendation.',
'23b:3':'Reread Rava original-wording retention, forgotten condition content and both invocation branches.',
'23b:4':'Reread proposed public exposition and Rava rationale against it; did not convert intention to completed event.',
'23b:5':'Reread two distinct questions and citation introduction, followed complete proof sequence through24b:2.',
'24a:1':'Reread first gift direction, quantities and honor declaration allowing resolution without sage.',
'24a:2':'Reread conditional inference and proposed identification, kept provisional pending deflection.',
'24a:3':'Reread retained tanna and explicit reciprocity rationale; no final denial of disagreement inferred.',
'24a:4':'Reread reversed gift direction and actual Rabbi Meir/sages disagreement with specific declaration.',
'24a:5':'Reread second conditional inference and proposed proof, not accepted conclusion.',
'24a:6':'Reread second deflection and reversed benefit direction; preserved shortened name within exact quote.',
'24a:7':'Reread Mar Kashisha addressing Rav Ashi, all three compulsion alternatives and provisional proof.',
'24a:8':'Reread reversal of host/guest vow roles, reconstructed dialogue and repeated three grounds.',
'24a:9':'Reread further warm-food hospitality teaching, reciprocal reaction and explicit sages nonagreement; question spans next segment.',
'24b:1':'Reread cross-page question completion and accepted disagreement conclusion.',
'24b:2':'Reread final question and two separately named agreeing rulings; source answers partial/nonexhaustive.'}
if __name__=='__main__':a.save()
