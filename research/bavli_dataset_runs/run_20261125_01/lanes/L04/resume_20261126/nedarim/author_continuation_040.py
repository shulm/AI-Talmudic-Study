"""Maintenance, marriage and visiting restrictions: direction and exceptions preserved."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r040.';a.OUTPUT='continuation_040.json'
c=a.c;q=b.q;e=a.edge
a.structure('maintenance',['38a:17']+['38b:'+str(i) for i in range(1,8)],'Dependent maintenance, mature daughter’s consent and limited personal services')
a.structure('visit',['38b:8']+['39a:'+str(i) for i in range(1,7)]+['39b:1'],'Standing/sitting visits under opposite directions of benefit restriction')
family=c('family','38a:17','וזן את אשתו ואת בניו אף על פי שהוא חייב במזונותן','One may feed the restricted person’s wife and sons even though he owes their maintenance.',composition='composite',scope='Mishnah permission distinguished from animal maintenance')
animals=c('animals','38a:17','ולא יזון את בהמתו בין טמאה בין טהורה','One may not feed his animal, whether of an impure or pure species.',composition='composite',scope='Anonymous Mishnah rule')
el=c('el','38a:17','רבי אליעזר אומר זן את הטמאה ואינו זן את הטהורה','Rabbi Eliezer allows feeding the impure animal but not the pure animal.',holder='רבי אליעזר',composition='composite',scope='Explicit disagreement on one category')
why=q('why','38a:17','אמרו לו מה בין טמאה לטהורה','What distinguishes impure and pure animals?')
pure=c('pure','38a:17','אמר להו שהטהורה נפשה לשמים וגופה שלו','Rabbi Eliezer distinguishes a pure animal’s life as Heaven’s and body as the owner’s.',holder='רבי אליעזר',scope='Source’s ownership/benefit rationale')
impure=c('impure','38a:17','וטמאה','He treats the impure animal’s life and body as Heaven’s.',extra=[('38b:1','נפשה וגופה לשמים')],holder='רבי אליעזר',scope='Cross-page completion of his contrast')
object=c('object','38b:1','אמרו לו אף הטמאה נפשה לשמים וגופה שלו שאם ירצה הרי הוא מוכרה לנוכרים או מאכילה לכלבים','The reply says the impure animal’s body also benefits its owner, who can sell it to non-Jews or feed it to dogs.',composition='composite',scope='Two specific counterexamples to Eliezer’s body classification')
e('el.objection',el,animals,'objection','38a:17');e('pure.answer',pure,why,'answer','38a:17');e('impure.answer',impure,why,'answer','38b:1');e('object.objection',object,impure,'objection','38b:1')
marry=c('marry','38b:2','אמר רב יצחק בר חנניה אמר רב הונא המודר הנאה מחבירו מותר להשיא לו בתו','Rav Huna, through Rav Yitzhak bar Hananya, allows marrying one’s daughter to the benefit-restricted person.',holder='רב הונא',scope='Initial broad statement limited to mature daughter acting by her consent')
a.add('marry.chain','attributions',dict(surface='אמר רב יצחק בר חנניה אמר רב הונא',role='transmitter',candidates=['רב יצחק בר חנניה'],scope=marry,transmission_chain=['רב יצחק בר חנניה','רב הונא']),[a.ev('38b:2','אמר רב יצחק בר חנניה אמר רב הונא')],[marry])
direction=q('direction','38b:2','הוי בה רבי זירא במאי עסקינן','Rabbi Zeira asks which direction of benefit restriction this concerns.',voice='רבי זירא')
father=c('father','38b:2','אילימא בשנכסי אבי כלה אסורין על החתן הרי מוסר לו שפחה לשמשו','If the bride’s father’s property is forbidden to the groom, the objection describes the marriage as providing domestic service.',mode='challenged',scope='Source’s hypothetical characterization; corrected by mature daughter’s independent consent')
groom=c('groom','38b:3',None,'If the groom’s property is forbidden to the father, the allowance seems obvious from the stronger permission to feed his dependents.',mode='challenged',scope='Opposite-direction construction challenged as unnecessary')
mature=c('mature','38b:4',None,'The answer retains the father-property-forbidden-to-groom direction but specifies a mature daughter and her own consent.',conditions=['daughter בוגרת','her consent'],scope='Essential limitation, not unilateral paternal transfer')
baraita=c('baraita','38b:5',None,'A supporting baraita prohibits marrying a daughter to the restricted person generally, but permits a mature daughter with her consent.',composition='composite',scope='Explicit prohibition/exception corroboration')
e('mature.answer',mature,direction,'answer','38b:4');e('mature.qualification',mature,marry,'qualification','38b:4');e('baraita.support',baraita,mature,'support','38b:5')
water=c('water','38b:6','אמר רבי יעקב המדיר בנו לתלמוד תורה מותר למלאות לו חבית של מים ולהדליק לו את הנר','Rabbi Yaakov permits filling a barrel of water and lighting a lamp in the case of one imposing a vow on his son for Torah study.',holder='רבי יעקב',composition='composite',scope='Narrow study-vow service exception; pronoun direction not expanded beyond source')
fish=c('fish','38b:6','רבי יצחק אמר לצלות לו דג קטן','Rabbi Yitzhak permits roasting a small fish in that setting.',holder='רבי יצחק',scope='Separate stated service, not generalized food allowance')
cup=c('cup','38b:6','אמר רבי ירמיה אמר רבי יוחנן המודר הנאה מחבירו מותר להשקותו כוס של שלום','Rabbi Yohanan, via Rabbi Yirmeya, permits giving the restricted person a cup of peace.',holder='רבי יוחנן',scope='Meaning clarified by two regional explanations')
a.add('cup.chain','attributions',dict(surface='אמר רבי ירמיה אמר רבי יוחנן',role='transmitter',candidates=['רבי ירמיה'],scope=cup,transmission_chain=['רבי ירמיה','רבי יוחנן']),[a.ev('38b:6','אמר רבי ירמיה אמר רבי יוחנן')],[cup])
cupq=q('cupq','38b:6','מאי ניהו','What is the cup of peace?')
mourn=c('mourn','38b:6','הכא תרגימו כוס של בית האבל','Here it is explained as a cup in a mourning house.',scope='Local collective explanation')
bath=c('bath','38b:6','במערבא אמרי כוס של בית המרחץ','In the West it is explained as a bathhouse cup.',scope='Explicit regional alternative')
e('mourn.answer',mourn,cupq,'answer','38b:6');e('bath.answer',bath,cupq,'answer','38b:6')
slaves=c('slaves','38b:7','תניא יהושע איש עוזא אומר זן עבדיו ושפחותיו הכנענים ולא יזון את בהמתו בין טמאה בין טהורה','Yehoshua of Uzza permits feeding Canaanite male and female slaves, but not animals of either category.',holder='יהושע איש עוזא',composition='composite',scope='Attributed ancient legal categories')
reasonq=q('reasonq','38b:7','מאי טעמא','What explains that distinction?')
reason=c('reason','38b:7','עבדיו ושפחותיו הכנענים למנחרותא עבידן בהמה לפטומא עבידא','The explanation contrasts slaves as למנחרותא עבידן with animals kept for fattening.',scope='Exact unusual למנחרותא retained rather than imposing an uncertain lexical gloss')
e('reason.answer',reason,reasonq,'answer','38b:7')
visit=c('visit','38b:8','המודר הנאה מחבירו ונכנס לבקרו עומד אבל לא יושב','A visitor under the benefit restriction may stand but may not sit during the visit.',scope='Restriction direction and fee setting debated below')
heal=c('heal','38b:8','ומרפאו רפואת נפש אבל לא רפואת ממון','He may provide personal healing but not property-related healing.',scope='Mishnah’s distinction, elaborated later; not contemporary treatment advice')
which=q('which','39a:1','במאי עסקינן','Which restriction direction explains standing but not sitting?')
visitor=c('visitor','39a:1','אי בשנכסי מבקר אסורין על חולה אפילו יושב נמי','If visitor property is prohibited to the patient, why not allow sitting too?',mode='hypothetical',scope='First branch of challenge')
patient=c('patient','39a:1','אי בשנכסי חולה אסורין על המבקר אפילו עומד נמי לא','If patient property is prohibited to the visitor, even standing should be prohibited.',mode='hypothetical',scope='Opposite-direction branch')
shmuel=c('shmuel','39a:1','אמר שמואל לעולם בשנכסי מבקר אסורין על החולה ובמקום שנוטלין שכר על הישיבה ואין נוטלין שכר על העמידה','Shmuel uses the visitor-property-forbidden-to-patient direction, where sitting visits are paid and standing visits are not.',holder='שמואל',conditions=['sitting fee','no standing fee'])
e('shmuel.answer',shmuel,which,'answer','39a:1')
fixed=q('fixed','39a:2','מאי פסקא','Why is that payment distinction fixed?')
fees=c('fees','39a:2','הא קא משמע לן דאף במקום שנוטלין שכר על הישיבה בעי למשקל על העמידה לא בעי למשקל','The answer permits sitting fees where customary but does not permit charging for standing.',scope='Normative fee distinction')
linger=c('linger','39a:2','ואיבעית אימא כדרבי שמעון בן אליקים גזירה שמא ישהא בעמידה הכא נמי גזירה שמא ישהא בישיבה','An alternative invokes Rabbi Shimon ben Elyakim’s concern about lingering, applying a decree against prolonged sitting here.',scope='Analogical alternative, not a direct Shimon ben Elyakim ruling on this exact Mishnah')
e('fees.answer',fees,fixed,'answer','39a:2');e('linger.answer',linger,fixed,'answer','39a:2')
ulla=c('ulla','39a:3','עולא אמר לעולם בשנכסי חולה אסורין על המבקר וכגון דלא אדריה מן חיותיה','Ulla instead uses the patient-property-forbidden-to-visitor direction, where life-supporting benefit was not included in the vow.',holder='עולא',conditions=['vow did not include מן חיותיה'],scope='Different restriction direction from Shmuel')
sitq=q('sitq','39a:3','אי הכי אפילו יושב נמי','Why not then permit sitting too?')
stand=c('stand','39a:3','הא אפשר בעמידה','Standing is sufficient.',scope='Limits necessity exception to what the visit requires')
e('ulla.answer',ulla,which,'answer','39a:3');e('stand.answer',stand,sitq,'answer','39a:3')
son=c('son','39a:4','מיתיבי חלה הוא נכנס לבקרו חלה בנו שואלו בשוק','A baraita allows entry when he himself is ill, but only inquiry in the marketplace when his son is ill.',composition='composite',scope='Patient-versus-son distinction used to test two constructions')
fit=c('fit','39a:4','בשלמא לעולא דאמר בשנכסי חולה אסורין על המבקר וכגון דלא אדריה מן חיותיה שפיר','The baraita is said to fit Ulla’s life-support exception.',scope='Explicit concession')
sonq=q('sonq','39a:5','אלא לשמואל דאמר בשנכסי מבקר אסורין על החולה מאי שנא הוא ומאי שנא בנו','For Shmuel, why distinguish the patient from his son?')
split=c('split','39a:5','אמר לך מתניתין בשנכסי מבקר אסורין על החולה ברייתא בשנכסי חולה אסורין על המבקר','The reply gives opposite restriction directions to Mishnah and baraita: visitor-to-patient in the former, patient-to-visitor in the latter.',composition='composite',scope='Defense of Shmuel by separate case assignments')
e('split.answer',split,sonq,'answer','39a:5')
splitq=q('splitq','39a:6','מאי פסקא','What warrants those separate assignments?')
derive=c('derive','39a:6','אמר רבא (אמר) שמואל','Rava explains Shmuel’s construction from the Mishnah’s standing-versus-sitting distinction, which points to the visitor’s property being prohibited to the patient.',extra=[('39b:1',None)],scope='Cross-page explanation; printed parenthetical אמר retained rather than normalizing transmission syntax')
e('derive.answer',derive,splitq,'answer','39b:1')
a.notes={
'38a:17':'Reread family maintenance, animal ban, Eliezer distinction and question; joined dangling impure rationale to38b:1.',
'38b:1':'Reread impure rationale completion and sale/dog-food counterexamples.',
'38b:2':'Reread Yitzhak/Hananya-to-Huna chain, Zeira question and first-direction objection.',
'38b:3':'Reread opposite-direction objection as already covered by stronger maintenance permission.',
'38b:4':'Reread essential mature-daughter and own-consent conditions.',
'38b:5':'Reread supporting general prohibition and mature-consenting-daughter exception.',
'38b:6':'Reread Yaakov water/lamp, Yitzhak fish, Yirmeya/Yohanan cup and two regional definitions.',
'38b:7':'Reread Yehoshua of Uzza slave/animal distinction and precise uncertain למנחרותא rationale.',
'38b:8':'Reread standing/sitting and personal/property healing Mishnah distinctions.',
'39a:1':'Reread both restriction-direction challenges and Shmuel fee-based construction.',
'39a:2':'Reread payment question, normative fee answer and separate lingering-decree alternative.',
'39a:3':'Reread Ulla opposite direction, life exception, sitting question and standing sufficiency.',
'39a:4':'Reread patient/son baraita and explicit fit with Ulla.',
'39a:5':'Reread Shmuel challenge and separate Mishnah/baraita direction assignment.',
'39a:6':'Reread why-separate question and Rava/(אמר)Shmuel introduction spanning page.',
'39b:1':'Reread standing/sitting inference completing Rava explanation; preserved parenthetical uncertainty.'}
if __name__=='__main__':a.save()
