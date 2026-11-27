"""Manual study oaths, dream sanctions, agency, and transmitted sun exposition."""
import author_continuation_007 as t
a=t.a;a.records=[];a.notes={};a.PREFIX='nd.r008.';a.OUTPUT='continuation_008b.json'
c=a.c;q=a.q;e=a.edge;transmission=t.transmission
a.structure('study',['7b:9']+['8a:'+str(i) for i in range(1,6)],'Oaths to fulfill commandments and study; obligation of the initiator')
a.structure('dream',['8a:'+str(i) for i in range(6,10)]+['8b:1'],'Dream excommunication and its release')
a.structure('agency',['8b:2','8b:3','8b:4'],'Husband’s agency for wife’s vow-regret and local authority for release')
a.structure('sun',['8b:5','8b:6','8b:7'],'Divine-name reverence, healing sunlight, and a contrasting future-sun exposition')
oath=c('oath','7b:9',None,'Rav, transmitted by Rav Giddel, teaches that one may swear to fulfill a commandment, citing נשבעתי ואקיימה לשמור משפטי צדקך.',holder='רב',extra=[('8a:1',None)],composition='composite',scope='Cross-page authority introduction and complete teaching')
transmission('giddel',oath,'7b:9',None,['רב גידל','רב'])
sinai=q('sinai','8a:2','והלא מושבע ועומד מהר סיני הוא','Is he not already bound by an oath from Sinai?')
urge=c('urge','8a:2',"אלא הא קמ''ל דשרי ליה לאיניש לזרוזי נפשיה",'The teaching permits a person to encourage himself through such an oath.',scope='Answer concerning self-encouragement, not a new independent obligation inferred here')
e('sinai.objection',sinai,oath,'objection','8a:2');e('urge.answer',urge,sinai,'answer','8a:2')
study=c('study','8a:3',"ואמר רב גידל אמר רב האומר אשכים ואשנה פרק זה אשנה מסכתא זו נדר גדול נדר לאלהי ישראל",'Rav, reported by Rav Giddel, calls a commitment to rise and study this chapter or tractate a great vow to the God of Israel.',holder='רב',conditions=['specified study undertaking'],composition='composite',scope='Paired chapter/tractate formulations, not an invented generic course requirement')
transmission('giddel2',study,'8a:3','ואמר רב גידל אמר רב',['רב גידל','רב'])
already=q('already','8a:3','והלא מושבע ועומד הוא ואין שבועה חלה על שבועה','Is he not already sworn, with no oath taking effect upon an oath?')
repeat=q('repeat','8a:3',"מאי קמ''ל דאפי' זרוזי בעלמא היינו דרב גידל קמייתא",'If this teaches mere encouragement, is it not the preceding Rav Giddel teaching?')
minimal=c('minimal','8a:4',None,'Because he could discharge the relevant prior obligation with morning and evening Shema, the stated study oath can take effect.',conditions=['specific additional study undertaking'],scope='Local explanation of oath taking effect; not a general pedagogical or halakhic conclusion about all study duties')
e('already.objection',already,study,'objection','8a:3');e('repeat.objection',repeat,study,'objection','8a:3');e('minimal.answer',minimal,already,'answer','8a:4');e('minimal.answer2',minimal,repeat,'answer','8a:4')
rise=c('rise','8a:5',"א''ר גידל א''ר האומר לחבירו נשכים ונשנה פרק זה עליו להשכים",'Rav, reported by Rabbi Giddel, requires the person who proposes rising to study a chapter together to rise first.',holder='רב',conditions=['person proposes נשכים ונשנה פרק זה to companion'],scope='Responsibility of initiator in this study arrangement')
transmission('giddel3',rise,'8a:5',"א''ר גידל א''ר",['רבי גידל','רב'])
ezekiel=c('ezekiel','8a:5',"שנאמר (יחזקאל ג כב-כג) ויאמר אלי (בן אדם) קום צא אל הבקעה ושם אדבר אותך ואצא אל הבקעה והנה שם כבוד ה' עומד",'The proof cites the summons to the valley followed by the divine glory already standing there.',composition='composite',scope='Quoted biblical narrative used by the source as support')
e('ezekiel.support',ezekiel,rise,'support','8a:5')
ten=c('ten','8a:6',"אמר רב יוסף נידוהו בחלום צריך י' בני אדם להתיר לו",'Rav Yosef requires ten people to release someone excommunicated in a dream.',holder='רב יוסף',conditions=['excommunication in a dream'])
learn=c('learn','8a:6','והוא דתנו הלכתא אבל מתנו ולא תנו לא','The ten must be דתנו הלכתא; מתנו ולא תנו are initially insufficient.',holder='רב יוסף',conditions=['suitable learned group available'],composition='composite',scope='Source’s learning-category distinction retained without imposing an unverified modern qualification taxonomy')
fallback=c('fallback','8a:6','ואי ליכא דתנו הלכתא אפילו מתנו ולא תנו','If the first group is unavailable, even מתנו ולא תנו suffice.',holder='רב יוסף',conditions=['no דתנו הלכתא available'],scope='Explicit fallback qualification')
crossroads=c('crossroads','8a:7',None,'If none are available, he should sit at a crossroads and greet groups of ten until encountering ten who learned halakha.',conditions=['preceding suitable group unavailable'],composition='composite',scope='Continuation of fallback procedure, not a separately invented guarantee of release')
e('learn.qualification',learn,ten,'qualification','8a:6');e('fallback.qualification',fallback,learn,'qualification','8a:6');e('crossroads.qualification',crossroads,fallback,'qualification','8a:7')
known=q('known','8a:8','ידע מאן שמתיה מהו דלישרי ליה','If he knows who excommunicated him in the dream, may that person release him?',conditions=['dream excommunicator identified'],voice='רבינא')
delegation=c('delegation','8a:8','אמר ליה לשמותיה שויוה שליח למישרי ליה לא שויוה שליח','Rav Ashi answers that the person was made an agent to excommunicate, not an agent to release.',holder='רב אשי',conditions=['identified dream excommunicator'],scope='Source’s distinction of agency in this dream case')
e('delegation.answer',delegation,known,'answer','8a:8')
dreamq=q('dreamq','8a:9','שמתיה ושרו ליה בחלמיה מאי','What if both excommunication and release occurred in his dream?',voice='רב אחא')
straw=c('straw','8a:9',"א''ל כשם שאי אפשר לבר בלא תבן",'Rav Ashi compares dreams to grain with straw: a dream cannot be without meaningless material.',holder='רב אשי',extra=[('8b:1',None)],composition='composite',scope='Cross-page analogy answering why dreamed release cannot simply settle the sanction; do not identify which detail is false with certainty')
e('straw.answer',straw,dreamq,'answer','8b:1')
wife=c('wife','8b:2','רבינא הוה לה נדרא לדביתהו אתא לקמיה דרב אשי','Ravina’s wife had a vow, and he came before Rav Ashi.',composition='composite',scope='Narrated consultation; wife not erased from the event')
agency=q('agency','8b:2','אמר ליה בעל מהו שייעשה שליח לחרטת אשתו','May a husband act as an agent for his wife’s regret concerning her vow?',voice='רבינא')
assembled=c('assembled','8b:2','אמר ליה אי מכנפין אין אי לא לא','Rav Ashi permits it if they are already assembled, but otherwise not.',holder='רב אשי',conditions=['decision-makers already assembled versus not assembled'],composition='composite',scope='Answer to the husband-agency question, preserving condition without inventing its rationale')
e('assembled.answer',assembled,agency,'answer','8b:2')
infer1=c('infer1','8b:3','שמע מינה תלת שמע מינה בעל נעשה שליח לחרטת אשתו','The discussion derives that a husband may act as agent for his wife’s regret.',conditions=['as qualified by already-assembled setting'],scope='First explicit inference from narrative')
infer2=c('infer2','8b:3','ושמע מינה לא שרי למישרי נדרא באתרא דרביה','It derives that one should not release a vow in the place of one’s teacher.',scope='Second narrative inference')
infer3=c('infer3','8b:3','ושמע מינה כי מכנפין שפיר דמי','It derives that the already-assembled setting is permitted.',conditions=['already assembled'],scope='Third explicit inference')
for key,claim in [('agency',infer1),('teacher',infer2),('assembled',infer3)]:e(key+'.support',wife,claim,'support','8b:3')
ban=c('ban','8b:4','ושמתא אפילו באתרא דרביה','Excommunication release is permitted even in the place of one’s teacher.',scope='Contrast to vow release in preceding inference')
expert=c('expert','8b:4','ויחיד מומחה שרי שמתא','A single expert can release excommunication.',conditions=['יחיד מומחה'],scope='Separate excommunication-release rule')
e('ban.distinction',ban,infer2,'distinction','8b:4')
chain=['רבי שמעון בר זביד','רב יצחק בר טבלא','רבי חייא אריכא דבי רבי אחא','רבי זירא','רבי אלעזר','רבי חנינא','רבי מיאשה','רבי יהודה בר אילעאי']
fear=c('fear','8b:5',"מאי דכתיב וזרחה לכם יראי שמי (שמש צדקה וגו') אלו בני אדם שהן יראין להוציא שם שמים לבטלה",'The transmitted exposition identifies those who fear the divine name as people afraid to utter it in vain.',holder='רבי יהודה בר אילעאי',scope='Teaching transmitted through the explicit long chain; רבי אחא remains part of דבי label, not an extra transmitter')
transmission('chain',fear,'8b:5','אמר רבי שמעון בר זביד אמר רב יצחק בר טבלא אמר רבי חייא אריכא דבי רבי אחא אמר רבי זירא אמר רבי אלעזר אמר רבי חנינא אמר רבי מיאשה משמיה דרבי יהודה בר אילעאי',chain)
aq=q('aq','8b:5',"מאי דכתיב וזרחה לכם יראי שמי (שמש צדקה וגו')",'What is the meaning of וזרחה לכם יראי שמי?',voice='רבי יהודה בר אילעאי')
sun=c('sun','8b:5','שמש צדקה ומרפא אמר אביי שמע מינה חירגא דיומא מסי','Abaye infers from the healing-sun wording that the sun’s rays heal.',holder='אביי',scope='Source’s stated inference, not present medical advice')
e('fear.answer',fear,aq,'answer','8b:5')
hell=c('hell','8b:6','ופליגא דרבי שמעון בן לקיש דאמר אין גיהנם לעולם הבא','Rabbi Shimon ben Lakish says there is no Gehinnom in the world to come.',holder='רבי שמעון בן לקיש',scope='Contrasting eschatological exposition; meaning limited by subsequent sun mechanism')
release=c('release','8b:6','לא הקדוש ברוך הוא מוציא חמה מנרתיקה','Rather, God brings the sun out of its sheath.',holder='רבי שמעון בן לקיש',scope='Source’s eschatological account; printed לא retained without emendation')
righteous=c('righteous','8b:6','צדיקים מתרפאין בה','The righteous are healed by it.',holder='רבי שמעון בן לקיש',conditions=['future sun exposition'])
wicked=c('wicked','8b:6','ורשעים נידונין בה','The wicked are judged by it.',holder='רבי שמעון בן לקיש',conditions=['same future sun'])
healverse=c('healverse','8b:6',"שנאמר וזרחה לכם יראי שמי שמש וגו'",'The exposition supports healing with וזרחה לכם יראי שמי שמש.',scope='Scriptural evidence in Rabbi Shimon ben Lakish account')
pleasure=c('pleasure','8b:6','ולא עוד אלא שמתעדנין בה שנאמר ויצאתם ופשתם כעגלי מרבק','The righteous also delight in it, supported by ויצאתם ופשתם כעגלי מרבק.',holder='רבי שמעון בן לקיש',scope='Additional outcome and explicit proof',composition='composite')
judgment=c('judgment','8b:7',None,'The text repeats that the wicked are judged by the sun, citing הנה יום בא בוער כתנור.',holder='רבי שמעון בן לקיש',scope='Repeated conclusion and separate proof, not deduplicated',composition='composite')
e('hell.objection',hell,sun,'objection','8b:6','ופליגא דרבי שמעון בן לקיש');e('healverse.support',healverse,righteous,'support','8b:6');e('judgment.support',judgment,wicked,'support','8b:7')
a.notes={
'7b:9':'Reread authority introduction together with8a:1; Rav Giddel transmitter, Rav authority; no empty sentence invented.',
'8a:1':'Reread complete transmitted teaching and Psalm evidence across preceding daf.',
'8a:2':'Reread Sinai-oath objection and self-encouragement answer.',
'8a:3':'Reread chapter/tractate undertaking, transmission and both independent objections.',
'8a:4':'Reread Shema-minimum rationale in its local oath context; no universal conclusion about study duties.',
'8a:5':'Reread proposer’s responsibility, transmission and Ezekiel narrative proof.',
'8a:6':'Reread dream-sanction rule, learning distinction and first availability fallback.',
'8a:7':'Reread crossroads procedure, groups of ten and eventual learned group.',
'8a:8':'Reread Ravina-to-Rav Ashi question and asymmetric agency answer.',
'8a:9':'Reread Rav Aha’s question and Rav Ashi answer completed8b:1.',
'8b:1':'Reread dream/grain analogy in full; no claim specifying which dreamed item was false.',
'8b:2':'Reread Ravina’s wife narrative, agency question and assembled/not-assembled condition.',
'8b:3':'Reread all three explicit inferences, preserving conditions and teacher-locality limit.',
'8b:4':'Reread excommunication distinction and separate single-expert rule.',
'8b:5':'Reread entire eight-name transmission, דבי label, verse question, reverence interpretation and separate Abaye sunlight inference.',
'8b:6':'Reread explicit contrast, future sun mechanism, two groups, proof and added delight; no empirical-medical assertion by annotator.',
'8b:7':'Reread repeated wicked-judgment conclusion and independent verse proof.'}
if __name__=='__main__':a.save()
