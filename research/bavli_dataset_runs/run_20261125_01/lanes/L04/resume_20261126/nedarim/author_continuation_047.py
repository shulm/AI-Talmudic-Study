"""Partnership courtyard, corrected Zeiri report and unresolved substitute-produce inquiry."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r047.';a.OUTPUT='continuation_047.json'
c=a.c;q=b.q;e=a.edge
a.structure('partners',['45b:1']+['46a:'+str(i) for i in range(1,10)]+['46b:'+str(i) for i in range(1,6)],'Courtyard partners, voluntary/coerced vows and divisible-property correction')
a.structure('future',['47a:1','47a:2'],'Prohibition of another’s entry after ownership ends')
a.structure('substitute',['47a:3','47a:4']+['47b:'+str(i) for i in range(1,5)],'Substitutes and growths: self/other prohibition and inconclusive proofs')
ban=c('ban','45b:1','שנדרו הנאה זה מזה אסורין ליכנס לחצר','Partners who vow against mutual benefit may not enter the courtyard.',scope='Anonymous Mishnah rule; divisibility clarified below')
own=c('own','45b:1','ר"א בן יעקב אומר זה נכנס לתוך שלו וזה נכנס לתוך שלו','Rabbi Eliezer ben Yaakov permits each to enter his own portion.',holder='ר"א בן יעקב',composition='composite',scope='Competing account of joint courtyard use')
fixtures=c('fixtures','46a:1',None,'Both may not install a mill or oven or raise chickens there.',composition='composite',scope='Three named uses prohibited despite entry controversy')
one=c('one','46a:2','היה אחד מהם מודר הנאה מחבירו לא יכנס לחצר','Where only one partner is benefit-restricted, he may not enter.',scope='Second Mishnah case; מודר wording discussed below')
oneOwn=c('oneOwn','46a:2','רבי אליעזר בן יעקב אומר יכול הוא לומר לו לתוך שלי אני נכנס ואיני נכנס לתוך שלך','Rabbi Eliezer ben Yaakov permits him to say that he enters his own portion rather than the other’s.',holder='רבי אליעזר בן יעקב',scope='One-sided restriction case')
sell=c('sell','46a:2','וכופין את הנודר למכור את חלקו','The vower is compelled to sell his share.',scope='Who initiated the vow is central to46a:8 argument')
outsider=c('outsider','46a:3','היה אחד מן השוק מודר באחד מהם הנאה לא יכנס לחצר','An outsider prohibited from benefit from one partner may not enter the courtyard.',scope='Third Mishnah case')
friend=c('friend','46a:3','רבי אליעזר בן יעקב אומר יכול לומר לו לתוך של חבירך אני נכנס ואיני נכנס לתוך שלך','Rabbi Eliezer ben Yaakov permits the outsider to invoke entry into the other partner’s share.',holder='רבי אליעזר בן יעקב',scope='Distinguished from entering one’s own share')
lease=c('lease','46a:4',None,'Use of a leased bathhouse or oil press is prohibited if the restricted owner retains a share and permitted if he does not.',composition='composite',conditions=['leased property','retained stake criterion'],scope='Measure of תפיסת יד debated46b:5')
your=c('your','46a:5','האומר לחבירו קונם לביתך שאני נכנס ושדך שאני לוקח מת או שמכרו לאחר מותר','A vow against entering your house or buying your field ends for these purposes after the owner dies or sells to another.',composition='composite',conditions=['possessive wording'])
this=c('this','46a:5','קונם בית זה שאני נכנס שדה זו שאני לוקח מת או שמכרו לאחר אסור','A vow specifying this house or this field persists after death or sale.',composition='composite',conditions=['demonstrative wording'])
for key,x,y,ref in [('own',own,ban,'45b:1'),('oneOwn',oneOwn,one,'46a:2'),('friend',friend,outsider,'46a:3')]:e(key+'.objection',x,y,'objection',ref)
coerce=a.q('coerce','46a:6',None,'Does the courtyard dispute concern voluntary vows only, with agreement to permit when each imposes on the other, or do sages disagree even in the imposed case?')
next(x for x in a.records if x['id']==coerce)['uncertainty'].append('The proposed proof from מודר is deflected by reading נדור; no final explicit resolution of the imposed-vow branch appears here.')
proof=c('proof','46a:7','ת"ש היה אחד מהן מודר הנאה מחבירו ופליגי רבנן','The proposed proof uses the Mishnah’s מודר wording to show sages disagree in an imposed case.',mode='challenged',scope='Proof rests on passive-form reading')
read=c('read','46a:7','תני נדור מחבירו הנאה','The answer reads נדור, a self-imposed benefit vow.',scope='Explicit textual reading rather than silent normalization')
support=c('support','46a:8',None,'The compulsory-sale clause supports the voluntary reading: it fits one who vowed himself, whereas compelling an involuntarily restricted person would be unwarranted.',composition='composite',scope='Supporting argument for reading נדור, not definitive resolution of all imposed cases')
e('read.correction',read,proof,'correction','46a:7');e('read.unresolved',read,coerce,'unresolved_outcome','46a:7');e('support.support',support,read,'support','46a:8')
first=c('first','46a:9',None,'Rabbah reports Zeiri as locating the dispute in a divisible courtyard and unanimous permission in an indivisible one.',extra=[('46b:1',None)],holder='זעירי',mode='rejected',composition='composite',scope='Initial report corrected after synagogue objection; רבה is transmitter')
a.add('first.chain','attributions',dict(surface='אמר רבה אמר זעירי',role='transmitter',candidates=['רבה'],scope=first,transmission_chain=['רבה','זעירי']),[a.ev('46a:9')],[first])
synagogue=q('synagogue','46b:2',None,'Rav Yosef objects that a synagogue resembles indivisible property, yet both are forbidden communal-town property.',voice='רב יוסף')
correct=c('correct','46b:3',None,'Rav Yosef reports the corrected Zeiri statement: dispute concerns an indivisible courtyard, while a divisible one is unanimously prohibited.',holder='זעירי',composition='composite',scope='Explicit אלא correction reverses the initial allocation')
a.add('correct.chain','attributions',dict(surface='אמר רב יוסף אמר זעירי',role='transmitter',candidates=['רב יוסף'],scope=correct,transmission_chain=['רב יוסף','זעירי']),[a.ev('46b:3','אמר רב יוסף אמר זעירי')],[correct])
e('correct.answer',correct,synagogue,'answer','46b:3');e('correct.correction',correct,first,'correction','46b:3')
huna=c('huna','46b:4','אמר רב הונא הלכה כר"א בן יעקב','Rav Huna rules according to Rabbi Eliezer ben Yaakov.',holder='רב הונא',scope='Local courtyard ruling with corrected scope')
elazar=c('elazar','46b:4',"וכן א\"ר אלעזר הלכה כר' אליעזר בן יעקב",'Rabbi Elazar gives the same ruling.',holder='רבי אלעזר',scope='Separate agreeing report, not disagreement')
stakeq=q('stakeq','46b:5','וכמה תפיסת יד','How large a retained stake counts?')
nahman=c('nahman','46b:5','אמר רב נחמן למחצה לשליש ולרביע אבל בבציר לא','Rav Nahman includes a half, third or quarter, but not a smaller share.',holder='רב נחמן',composition='composite',scope='Threshold view')
abaye=c('abaye','46b:5','אביי אמר אפילו בבציר אסור','Abaye prohibits even a smaller retained share.',holder='אביי',scope='Contrary threshold')
permittedq=q('permittedq','46b:5','היכי דמי דשרי','What arrangement then permits use?')
fixed=c('fixed','46b:5','דמקבל בטסקא','The answer specifies receipt of a fixed rental payment.',scope='טסקא arrangement distinguished from retained proportional interest')
e('nahman.answer',nahman,stakeq,'answer','46b:5');e('abaye.answer',abaye,stakeq,'answer','46b:5');e('fixed.answer',fixed,permittedq,'answer','46b:5')
avimi=q('avimi','47a:1','בעי אבימי קונם לבית זה שאתה נכנס מת או שמכרו לאחר מהו אדם אוסר דבר שברשותו לכשיצא מרשותו או לא','Avimi asks whether prohibiting another’s entry into this house persists after the owner dies or sells, testing prohibition after ownership ends.',voice='אבימי')
inherit=c('inherit','47a:2','אמר רבא ת"ש האומר לבנו קונם שאי אתה נהנה לי ומת יירשנו בחייו ובמותו ומת לא יירשנו','Rava cites the son-inheritance contrast between unqualified prohibition and explicit life-and-death prohibition.',composition='composite',scope='Two-wording proof, not identical to self-imposed entry vow')
yes=c('yes','47a:2','ש"מ אדם אוסר דבר שברשותו לכשיצא מרשותו שמע מינה','The discussion accepts that one can prohibit property while owning it for after ownership ends.',scope='Explicit accepted שמע מינה')
e('yes.answer',yes,avimi,'answer','47a:2');e('inherit.support',inherit,yes,'support','47a:2')
sub=c('sub','47a:3',None,'A cited Mishnah prohibits substitutes and growths of produce under the specified self-directed konam formulations.',composition='composite',scope='Three printed self-vow phrasings, common substitute/growth outcome')
other=a.q('other','47a:4','בעי רמי בר חמא אמר קונם פירות האלו על פלוני מהו בחילופיהן','Rami bar Hama asks whether substitutes are prohibited when these fruits are prohibited to another.',voice='רמי בר חמא')
next(x for x in a.records if x['id']==other)['uncertainty'].append('Both subsequent proofs are deflected by an ex-ante/ex-post distinction; no definitive answer is supplied before the next Mishnah.')
limits=c('limits','47a:4','מי אמרינן גבי דיליה הואיל ואדם אוסר פירות חבירו על עצמו אדם אוסר דבר שלא בא לעולם על עצמו גבי חבירו הואיל ואין אדם אוסר פירות חבירו על חבירו אין אדם אוסר דבר שלא בא לעולם על חבירו','One alternative distinguishes self-vows, which can prohibit another’s produce and future items, from prohibiting future items to another.',mode='hypothetical',composition='composite',scope='Proposed self/other asymmetry')
growth=c('growth','47b:1',None,'The other alternative treats substitutes like growths and makes no difference between self and other.',mode='hypothetical',scope='Cross-page second branch')
wife=c('wife','47b:2','אמר רב אחא בר מניומי ת"ש האומר לאשתו קונם שאני נהנה ליך לווה ובעלי חובין באין ונפרעין','Rav Aha bar Minyumi cites the wife-loan case under the exact declaration קונם שאני נהנה ליך, with creditors collecting.',scope='Printed vow direction retained without silently rewriting its syntax')
infer=c('infer','47b:2','מ"ט בעלי חובין נפרעין לאו משום דחילופין לאו כגידולין דמי','The attempted inference is that substitutes are unlike growths.',mode='challenged',scope='Proposed answer to Rami’s question')
post=c('post','47b:3',None,'Rava replies that it may be prohibited initially while effective after the fact.',holder='רבא',scope='Deflects inference of ex-ante permission from ex-post collection')
orla=c('orla','47b:4','אלא ת"ש המקדש בערלה אינה מקודשת מכרן וקידש בדמיהן הרי זו מקודשת','The next proof contrasts invalid betrothal with orla itself and valid betrothal with proceeds after its sale.',composition='composite',scope='Second proposed proof about substitutes')
post2=c('post2','47b:4','הכא נמי לכתחילה הוא דלא ואי עבד עבד','The reply again distinguishes initial prohibition from ex-post effect.',scope='Second proof deflection, not final permission for substitutes')
e('post.correction',post,infer,'correction','47b:3');e('post2.qualification',post2,orla,'qualification','47b:4');e('post2.unresolved',post2,other,'unresolved_outcome','47b:4')
a.notes={
'45b:1':'Reread reciprocal partner courtyard rule and Eliezer ben Yaakov own-share alternative.',
'46a:1':'Reread mill/oven/chicken restrictions as separate uses.',
'46a:2':'Reread one-sided restriction, own-share response and compelled sale of vower share.',
'46a:3':'Reread outsider case and entry into unrestricted partner’s share rationale.',
'46a:4':'Reread leased bath/oil-press retained-stake criterion.',
'46a:5':'Reread possessive/demonstrative house/field contrast after death/sale.',
'46a:6':'Reread voluntary/imposed-vow question and both alternatives, left unresolved after proof deflection.',
'46a:7':'Reread מודר proof and explicit נדור reading.',
'46a:8':'Reread forced-sale support for voluntary wording and involuntary-case objection.',
'46a:9':'Reread Rabbah-to-Zeiri report introduction attached to46b:1.',
'46b:1':'Reread initial divisible-dispute/indivisible-consensus report, later corrected.',
'46b:2':'Reread Yosef synagogue counterexample.',
'46b:3':'Reread corrected Yosef/Zeiri indivisible-dispute/divisible-prohibition statement.',
'46b:4':'Reread Huna and Elazar separate agreeing local rulings.',
'46b:5':'Reread Nahman threshold, Abaye smaller-share disagreement and fixed-rent exception.',
'47a:1':'Reread Avimi other-person prohibition question, distinct from self-vow Mishnah.',
'47a:2':'Reread Rava inheritance contrast and explicit accepted post-ownership principle.',
'47a:3':'Reread three self-directed formulations and substitutes/growths prohibition.',
'47a:4':'Reread Rami bar Hama question and self/other asymmetry hypothesis.',
'47b:1':'Reread substitute-as-growth alternative completing prior question.',
'47b:2':'Reread Aha/Minyumi wife-loan proof and proposed substitute/growth distinction.',
'47b:3':'Reread Rava initial/ex-post deflection.',
'47b:4':'Reread orla/betrothal proof and repeated deflection; no final Rami answer invented.'}
if __name__=='__main__':a.save()
