"""Shared use and sabbatical-property formulations, ending with explicit no-disagreement."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r044.';a.OUTPUT='continuation_044.json'
c=a.c;q=b.q;e=a.edge
a.structure('shared',['41b:'+str(i) for i in range(5,10)],'Shared bath, bed, food and agricultural work')
a.structure('property',['42a:'+str(i) for i in range(1,7)]+['42b:'+str(i) for i in range(1,8)],'Property wording across ownership changes: rejected dispute reconstructions and final reconciliation')
bath=c('bath','41b:5','ורוחץ עמו באמבטי גדולה אבל לא בקטנה','The Mishnah permits sharing a large bath but not a small one.',composition='composite',scope='Benefit-restriction case')
bed=c('bed','41b:5','וישן עמו במטה','It permits sharing a bed.',scope='Rabbi Yehuda qualifies by season in next segment')
season=c('season','41b:6',"ר' יהודה אומר בימות החמה אבל לא בימות הגשמים מפני שהוא מהנהו",'Rabbi Yehuda permits it in summer but not winter because it confers benefit.',holder="ר' יהודה",composition='composite',scope='Seasonal qualification of bed-sharing')
recline=c('recline','41b:6','ומיסב עמו על המטה ואוכל עמו על השולחן','Reclining on a bed and eating at the same table are permitted.',composition='composite',scope='Shared setting distinguished from shared serving dish')
dish=c('dish','41b:6','אבל לא מן התמחוי אבל אוכל הוא עמו מן התמחוי החוזר','Eating from the same serving dish is prohibited except for the returning dish.',composition='composite',scope='Returning-dish meaning clarified by Yosei bar Hanina')
e('season.qualification',season,bed,'qualification','41b:6')
meir=c('meir','41b:7','תניא לא ירחץ עמו באמבטי ולא ישן עמו במטה בין גדולה בין קטנה דברי רבי מאיר','Rabbi Meir’s baraita prohibits sharing the bath or bed, whether large or small.',holder='רבי מאיר',composition='composite',scope='Distinct baraita formulation, not silently harmonized with Mishnah')
yehuda=c('yehuda','41b:7','רבי יהודה אומר גדולה בימות הגשמים וקטנה בימות החמה מותר','Rabbi Yehuda permits a large bed in winter and a small one in summer.',holder='רבי יהודה',composition='composite',scope='Baraita’s size/season differentiation')
steam=c('steam','41b:7','רוחץ עמו באמבטי גדולה ומזיע עמו בקטנה','The baraita permits bathing together in a large bath and sweating together in a small one.',composition='composite',scope='Bathing distinguished from sweating')
table=c('table','41b:7','אבל מיסב עמו על המטה ואוכל עמו על השולחן אבל לא מן התמחוי אבל אוכל הוא מן התמחוי החוזר','The baraita repeats reclining/table permission and common-dish restriction with returning-dish exception.',composition='composite',scope='Separate repeated occurrence')
returnc=c('return','41b:7','א"ר יוסי בר חנינא מן התמחוי החוזר לבעה"ב','Rabbi Yosei bar Hanina defines the dish as one returning to the host.',holder='רבי יוסי בר חנינא',scope='Clarifies technical החוזר, no unstated serving arrangement invented')
e('yehuda.objection',yehuda,meir,'objection','41b:7');e('return.qualification',returnc,dish,'qualification','41b:7')
trough=c('trough','41b:8','לא יאכל עמו מן האבוס שלפני הפועלים','He may not eat with him from the workers’ common trough.',scope='Mishnah shared-food restriction')
work=c('work','41b:8','ולא יעשה עמו באומן דברי רבי מאיר','Rabbi Meir prohibits working with him in the same row.',holder='רבי מאיר',scope='Distance clarified next segment')
far=c('far','41b:8','וחכ"א עושה והוא ברחוק ממנו','The sages permit working at a distance.',holder='חכמים',conditions=['far from him'])
near=c('near','41b:9','בקרוב לא פליגי דאסיר','All agree that nearby work is prohibited.',scope='Explicit non-disagreement for close proximity')
decree=c('decree','41b:9','כי פליגי ברחוק ר"מ סבר גזרינן רחוק משום קרוב דקא מרפי לה לארעא קמיה','Rabbi Meir extends a decree to distant work because nearby work loosens the other’s soil.',holder='רבי מאיר',scope='Exact locus and reason of dispute')
noDecree=c('noDecree','41b:9',"ורבנן סברי לא גזרי'",'The sages do not enact that decree for distant work.',holder='רבנן',scope='Shared nearby prohibition retained')
e('far.objection',far,work,'objection','41b:8');e('decree.support',decree,work,'support','41b:9');e('noDecree.support',noDecree,far,'support','41b:9')
before=c('before','42a:1','המודר הנאה מחבירו לפני שביעית אינו יורד לתוך שדהו ואינו אוכל מן הנוטות','Before the sabbatical year, a general-benefit restriction prohibits entering the field and eating overhanging produce.',composition='composite',conditions=['before seventh year'])
seventh=c('seventh','42a:1','ובשביעית אינו יורד לתוך שדהו אבל אוכל הוא מן הנטיעות הנוטות','In the seventh year it still prohibits entry but permits the overhanging produce.',composition='composite',conditions=['seventh year'],scope='Wording and timing of vow resolved in ensuing discussion')
foodBefore=c('foodBefore','42a:1','נדר הימנו מאכל לפני שביעית יורד לתוך שדהו ואינו אוכל מן הפירות','A food-only vow before the seventh year permits entry but not the produce.',composition='composite',conditions=['food-only vow','before seventh year'])
foodSeventh=c('foodSeventh','42a:1','ובשביעית יורד ואוכל','In the seventh year the food-only case permits entry and eating.',composition='composite',conditions=['food-only vow','seventh year'])
ravshmuel=c('ravshmuel','42a:2','רב ושמואל דאמרי תרוייהו נכסים אלו עליך לפני שביעית אין יורד לתוך שדהו ואינו אוכל מן הנוטות אע"פ שהגיע שביעית','Rav and Shmuel jointly prohibit field entry and overhanging produce even after the seventh year arrives when these properties were prohibited beforehand.',composition='composite',conditions=['נכסים אלו wording','vow before seventh year'],scope='Explicit joint view, not Rav–Shmuel dispute')
vowDuring=c('vowDuring','42a:2','ואם בשביעית נדר אין יורד לתוך שדהו אבל אוכל מן הנוטות','If the vow is made during the seventh year, entry is prohibited but overhanging produce is permitted.',composition='composite',conditions=['vow during seventh year'],scope='Second branch of Rav/Shmuel joint statement')
yohanan=c('yohanan','42a:3',None,'Rabbi Yohanan and Reish Lakish jointly distinguish my property: both entry and produce are prohibited before the seventh year, but produce becomes permitted when it arrives.',composition='composite',conditions=['נכסי wording'],scope='Joint view on different wording, finally reconciled with Rav/Shmuel')
a.add('rs.holders','attributions',dict(surface='רב ושמואל דאמרי תרוייהו',role='speaker',candidates=['רב','שמואל'],scope=ravshmuel,transmission_chain=[]),[a.ev('42a:2','רב ושמואל דאמרי תרוייהו')],[ravshmuel])
a.add('yl.holders','attributions',dict(surface="ור' יוחנן וריש לקיש דאמרי תרוייהו",role='speaker',candidates=["ר' יוחנן",'ריש לקיש'],scope=yohanan,transmission_chain=[]),[a.ev('42a:3',"ור' יוחנן וריש לקיש דאמרי תרוייהו")],[yohanan])
proposed=c('proposed','42a:4',None,'The first reconstruction proposes disagreement over whether a prohibition imposed during ownership can persist after ownership ends.',mode='rejected',composition='composite',scope='לימא hypothesis, not final positions of either pair')
whyNot=q('whyNot','42a:5',None,'Can anyone deny post-ownership prohibition entirely? If so, why not dispute these properties and all the more my property?')
inherit=c('inherit','42a:6','דתנן האומר לבנו קונם שאתה נהנה לי מת יירשנו','The cited Mishnah allows the son to inherit after the father dies under an unqualified benefit vow.',scope='First inheritance wording case')
lifeDeath=c('lifeDeath','42a:6','בחייו ובמותו','If the father specifies in life and death, the son may not inherit for benefit after death.',extra=[('42b:1','אם מת לא יירשנו')],conditions=['explicit life-and-death wording'],scope='Cross-page contrasting inheritance rule')
special=c('special','42b:1','שאני הכא דקא א"ל בחייו ובמותו','An attempted distinction invokes the explicit life-and-death wording.',mode='challenged',scope='Does not remove all objections; next segment retains difficulty')
consensus=c('consensus','42b:2','מכל מקום קשיא אלא בנכסים אלו כ"ע לא פליגי כי פליגי בנכסי','The next reconstruction concedes agreement on these properties and proposes a dispute only over my property.',mode='rejected',composition='composite',scope='Intermediate repair, itself displaced by final לא פליגי')
second=c('second','42b:3',None,'The second reconstruction assigns Rav/Shmuel persistence under either wording and Yohanan/Reish Lakish persistence only for properties, not my property.',mode='rejected',composition='composite',scope='Proposed assignment rejected by next Mishnah proof')
counterq=q('counterq','42b:4','ומי איכא למ"ד ל"ש נכסים אלו ול"ש נכסי','Can anyone really equate these properties with my property?')
your=c('your','42b:4','והא תנן האומר לחבירו קונם לתוך ביתך שאני נכנס שדך שאני לוקח מת או שמכרו לאחר מותר','A cited Mishnah permits your house/your field after the owner dies or sells to another.',composition='composite',conditions=['possessive wording','death or sale'])
this=c('this','42b:4','לבית זה שאני נכנס שדה זו שאני לוקח מת או שמכרו לאחר אסור','This house/this field remain prohibited after death or sale.',composition='composite',conditions=['demonstrative wording','death or sale'])
final=c('final','42b:5',None,'The final explanation assigns my property to Yohanan/Reish Lakish and these properties to Rav/Shmuel, expressly concluding they do not disagree.',mode='reconciled',composition='composite',scope='Final לא פליגי supersedes both proposed disputes; neither pair internally disputes')
e('final.answer',final,whyNot,'answer','42b:5');e('final.answer2',final,counterq,'answer','42b:5');e('final.correction',final,proposed,'correction','42b:5');e('final.correction2',final,second,'correction','42b:5');e('your.support',your,final,'support','42b:4');e('this.support',this,final,'support','42b:4')
landq=q('landq','42b:6','מאי שנא דאוכל מן הנוטות דפירי דהפקירא אינון ארעא נמי אפקרה','If seventh-year produce is ownerless, why is entry forbidden when the land too is made available?')
boundary=c('boundary','42b:7','אמר עולא בעומדין אילנות על הגבולים','Ulla places the trees at the boundary.',holder='עולא',scope='Fruit can be reached without entry')
linger=c('linger','42b:7',"ר' שמעון בן אליקים אמר גזירה שמא ישהא בעמידה",'Rabbi Shimon ben Elyakim explains a decree against lingering while standing.',holder="ר' שמעון בן אליקים",scope='Alternative rationale for entry restriction')
e('boundary.answer',boundary,landq,'answer','42b:7');e('linger.answer',linger,landq,'answer','42b:7')
a.notes={
'41b:5':'Reread large/small bath rule and unqualified bed clause.',
'41b:6':'Reread Yehuda seasonal limit, reclining/table allowance and returning-dish exception.',
'41b:7':'Reread Meir baraita, Yehuda size/season branches, bath/sweat distinction and Yosei/Hanina host-return explanation.',
'41b:8':'Reread common trough restriction and Meir/sages distance dispute.',
'41b:9':'Reread explicit close-distance agreement and precise decree disagreement for far work.',
'42a:1':'Reread all four general/food-vow and pre/seventh-year combinations.',
'42a:2':'Reread joint Rav/Shmuel demonstrative-property statement and vow-during-year branch.',
'42a:3':'Reread joint Yohanan/Reish Lakish possessive-property statement.',
'42a:4':'Reread first proposed post-ownership dispute, kept rejected after full continuation.',
'42a:5':'Reread conceptual and wording objection to first reconstruction.',
'42a:6':'Reread inheritance counterexample and life/death clause spanning page.',
'42b:1':'Reread inheritance prohibition completion and insufficient explicit-wording distinction.',
'42b:2':'Reread continuing difficulty and intermediate these-properties consensus/my-property dispute proposal.',
'42b:3':'Reread second proposed assignment to both pairs, later rejected.',
'42b:4':'Reread objection and exact possessive/demonstrative house/field contrast after death or sale.',
'42b:5':'Reread final separate-wording interpretation and explicit לא פליגי; no false inter-pair dispute retained as final.',
'42b:6':'Reread ownerless-fruit versus land-access question.',
'42b:7':'Reread Ulla boundary-trees and Shimon/Elyakim lingering-decree alternatives.'}
if __name__=='__main__':a.save()
