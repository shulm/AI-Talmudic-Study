"""Manual continuation of growth cancellation, vow release and original-part obligations."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r062.';a.OUTPUT='continuation_062.json'
c=a.c;e=a.edge;q=b.q
a.structure('konam',['59a:'+str(i) for i in range(2,8)],'Vow release and teruma: two rejected ownership constructions then mitzva distinction')
a.structure('original',['59a:8','59b:1','59b:2','59b:3'],'Yohanan original tithed onion, Rabbah/Hisda dialogue and effort distinction')
a.structure('yanai',['59b:4','60a:1','60a:2','60a:3'],'Yannai teruma onion qualified to second growth and predominant growth; chapter end')
rami=q('rami','59a:2','מתיב רמי בר חמא','Rami bar Hama objects from the Mishnah’s persistent-seed vow prohibition.',voice='רמי בר חמא')
vows=c('vows','59a:2','קונם פירות האלו עלי קונם הן על פי קונם הן לפי אסור בחילופיהן ובגידוליהן שאני אוכל ושאני טועם מותר בחילופיהן ובגידוליהן בדבר שזרעו כלה אבל בדבר שאין זרעו כלה אפילו גידולי גידולין אסורין','The quoted Mishnah contrasts item/mouth vows with eating/tasting vows for exchanges and growths, but prohibits even second growth when the seed persists.',composition='composite',scope='Full repeated proof occurrence with all formulas/seed conditions, not a new unique rule')
abba=c('abba','59a:3','אמר רבי אבא שאני קונמות הואיל ואי בעי מתשיל עלייהו הוו להו כדבר שיש לו מתירין ואין בטיל ברוב','Rabbi Abba distinguishes konam vows because they can be released, making them items with a route to permission that do not cancel in a majority.',holder='רבי אבא',scope='Initial release-based distinction subsequently refined to a mitzva-to-release distinction')
e('abba.answer',abba,rami,'answer','59a:3')
terumaq=q('terumaq','59a:4','והרי תרומה דאי בעי מיתשיל עלה ובטלי ברוב','But teruma can also be released and nevertheless cancels in a sufficient mixture.')
measure=c('measure','59a:4','דתנן סאה תרומה טמאה שנפלה לפחות ממאה חולין תרקב הא למאה תעלה','The cited rule leaves one sea of impure teruma to rot if mixed into fewer than one hundred sea of ordinary produce, implying cancellation at one hundred.',composition='composite',scope='Exact ratio and implication; majority language not mistaken for simple two-to-one here')
priest=c('priest','59a:4','אמרי בתרומה ביד כהן עסקינן דלא מצי מיתשיל עלה','The first reply places the teruma in a priest’s possession, where release is unavailable.',mode='rejected',scope='Ownership construction rejected by next sale clause')
saleq=q('saleq','59a:5','אי הכי אימא סיפא אם היתה טהורה תמכר לכהן','If so, why does the continuation say pure teruma is sold to a priest?')
inherit=c('inherit','59a:5','אלא בישראל שנפלו לו מבית אבי אמו כהן עסקינן','The second construction places it with an Israelite who inherited it from his priestly maternal grandfather.',mode='rejected',scope='Revised ownership construction also rejected by next price-exclusion clause')
priceq=q('priceq','59a:6',None,'Why then does the continuation exclude the value of the original sea from the sale price?')
mitzva=c('mitzva','59a:7','אלא אימא בשלמא קונמות מצוה לאיתשולי עליהן','The final distinction says there is a mitzva to seek release from konam vows.',scope='Replaces failed ownership explanations; expected release rather than mere abstract availability')
natan=c('natan','59a:7','משום דרבי נתן דאמר רבי נתן כל הנודר כאילו בנה במה והמקיימו כאילו מקטיר עליה','Rabbi Natan likens vowing to building a private altar and maintaining the vow to offering upon it.',holder='רבי נתן',composition='composite',scope='Two attributed analogies used to motivate seeking release')
notmitzva=c('notmitzva','59a:7','תרומה מאי מצוה לאיתשולי עלה','There is no corresponding mitzva to seek release of teruma.',scope='Rhetorical conclusion distinguishing teruma from konam vows')
e('priest.answer',priest,terumaq,'answer','59a:4');e('inherit.answer',inherit,saleq,'answer','59a:5');e('inherit.correction',inherit,priest,'correction','59a:5');e('mitzva.answer',mitzva,priceq,'answer','59a:7');e('notmitzva.answer',notmitzva,terumaq,'answer','59a:7');e('mitzva.correction',mitzva,inherit,'correction','59a:7');e('mitzva.qualification',mitzva,abba,'qualification','59a:7');e('natan.support',natan,mitzva,'support','59a:7')
yohanan=c('yohanan','59a:8','גופא אמר רבי יוחנן ליטרא בצלים שתיקנה וזרעה מתעשרת לפי כולה','Rabbi Yohanan’s rule is restated: a tithed litra of onions replanted is tithed on the whole crop.',holder='רבי יוחנן',scope='Separate repeated occurrence of earlier proof rule')
rabbah=c('rabbah','59a:8','יתיב רבה וקאמר להא שמעתא','Rabbah sits and repeats this teaching.',holder='רבה',scope='Printed רבה retained; not Rava of earlier revenue narrative')
hisdaq=q('hisdaq','59a:8','אמר ליה רב חסדא מאן צאית לך ולר\' יוחנן רבך היתר שבהן להיכן הלך','Rav Hisda challenges Rabbah and his teacher Yohanan: where has the original permitted portion gone?',voice='רב חסדא')
rain=c('rain','59b:1','אם היו עלין שלהן שחורין אסורין הוריקו מותרין','Rabbah’s cited rainfall-onion parallel prohibits with dark leaves and permits with green/pale leaves.',composition='composite',scope='Citation begins59a8; separate repeated proof occurrence',extra=[('59a:8','אמר ליה מי לא תנן דכוותה בצלים שירדו עליהם גשמים וצימחו')])
counterq=q('counterq','59b:1','וכי שחורין אמאי אסורין לימא היתר שבהן להיכן הלך','Why, on Hisda’s reasoning, would the dark-leaf onions be prohibited when their original part was permitted?',voice='רבה')
addition=c('addition','59b:1','א"ל מי סברת על עיקר קתני אתוספת קתני אסורין','The reply says the prohibition concerns only the added growth, not the original part.',holder='רב חסדא',scope='Dialogic respondent inferred from alternating Rabbah/Hisda exchange')
gamliel=c('gamliel','59b:1','דתניא רשב"ג אומר הגדל בחיוב חייב הגדל בפטור פטור','Rabban Shimon ben Gamliel distinguishes growth under obligation from growth under exemption.',holder='רשב"ג',composition='composite',scope='Two growth-period statuses in quoted baraita')
sameq=q('sameq','59b:1','אי הכי מאי אתא רשב"ג למימר','If so, what does Rabban Shimon ben Gamliel add beyond the first tanna?')
whole=c('whole','59b:2','כולה מתני\' רבן שמעון בן גמליאל קתני לה','The reply attributes the whole Mishnah to Rabban Shimon ben Gamliel.',scope='Eliminates proposed duplication between two distinct holders')
effort=c('effort','59b:2','ועד כאן לא שמעת ליה לרבן שמעון בן גמליאל דלא קא טרח אבל היכא דקא טרח בטיל ברובא','The discussion limits his preserved-original-part rule to growth without effort; where one labors, the original cancels in the majority.',composition='composite',scope='Rainfall versus deliberate replanting distinction protecting Yohanan’s rule')
e('rain.answer',rain,hisdaq,'answer','59b:1');e('addition.answer',addition,counterq,'answer','59b:1');e('whole.answer',whole,sameq,'answer','59b:2');e('effort.qualification',effort,gamliel,'qualification','59b:2');e('effort.answer',effort,hisdaq,'answer','59b:2')
effortq=q('effortq','59b:3','וכל היכא דקא טרח בטיל ברובא והרי ליטרא מעשר טבל דקטרח וקתני ואותה ליטרא מעשר עליו ממקום אחר לפי חשבון','Does labor always yield cancellation, given the replanted untithed-tithe litra still requires proportionate external separation?')
verse=c('verse','59b:3','שאני גבי מעשר דאמר קרא (דברים יד, כב) עשר תעשר וגו\'','The reply distinguishes tithe by its explicit scriptural requirement.',scope='Specific tithe exception to proposed effort-based cancellation')
sowing=c('sowing','59b:3','והיתירא זרעי אינשי איסורא לא זרעי אינשי','The explanation contrasts people’s sowing permitted produce with their not sowing prohibited produce.',composition='composite',scope='Source’s behavioral distinction; not a universal empirical claim about agriculture')
e('verse.answer',verse,effortq,'answer','59b:3');e('sowing.qualification',sowing,effort,'qualification','59b:3')
yanai=c('yanai','59b:4','גופא א"ר חנינא תירתאה א"ר ינאי בצל של תרומה שנטעו ורבו גידוליו על עיקרו מותר','Rabbi Hanina Tirtah reports Yannai’s permission for a replanted teruma onion whose growth exceeds its original part.',holder='רבי ינאי',scope='Repeated rule; spelling תירתאה retained rather than earlier תריתאה normalized')
terumagrowthq=q('terumagrowthq','60a:1','היתר מעלין את האיסור והתנן גידולי תרומה תרומה','How can permitted growth cancel prohibition when teruma growths are themselves teruma?',conditions=('Yannai’s majority-growth onion case',))
second=c('second','60a:1','בגידולי גידולין קאמרינן','The reply says Yannai refers to growths of growths.',scope='Explicit second-generation qualification')
alreadyq=q('alreadyq','60a:1','הא נמי תנינא גידולי גידולין חולין','Is it not already taught that growths of growths are ordinary produce?')
persistent=c('persistent','60a:1','הא קמ"ל אפילו בדבר שאין זרעו כלה','Yannai adds that the rule applies even when the seed persists.',scope='Novel persistent-seed application, subject to following majority clarification')
tevelq=q('tevelq','60a:2','והתנן הטבל גידוליו מותרין בדבר שזרעו כלה אבל דבר שאין זרעו כלה גידולי גידולין אסורין','But the Mishnah permits tevel growths only where the seed is consumed, and prohibits even second growth where it persists.')
majority=c('majority','60a:2','רבויא דרבו גידולין על עיקרו מותר קא משמע לן','The final answer emphasizes permission when the new growth exceeds the original.',scope='Final majority condition distinguishes the cited persistent-seed prohibition')
e('second.answer',second,terumagrowthq,'answer','60a:1');e('second.qualification',second,yanai,'qualification','60a:1');e('persistent.answer',persistent,alreadyq,'answer','60a:1');e('majority.answer',majority,tevelq,'answer','60a:2');e('majority.qualification',majority,persistent,'qualification','60a:2')
a.add('chapter.u','utterances',dict(textual_voice='anonymous textual marker',discourse_role='chapter conclusion',composition='atomic'),[a.ev('60a:3')])
a.add('chapter.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'chapter.u',transmission_chain=[]),[a.ev('60a:3')],[a.PREFIX+'chapter.u'])
a.notes={
'59a:2':'Reread Rami objection and full repeated fruit/mouth/eating/tasting formulas with both seed conditions.',
'59a:3':'Reread Abba release-availability distinction and no-majority-cancellation consequence.',
'59a:4':'Reread teruma-release objection, precise one-to-hundred ratio and first rejected priest-possession construction.',
'59a:5':'Reread sale-to-priest objection and second rejected Israelite-inheritance construction.',
'59a:6':'Reread bracketed introduction and excluded-original-sea-price objection.',
'59a:7':'Reread final mitzva-to-release distinction and both Natan altar analogies; no teruma release mitzva.',
'59a:8':'Reread Yohanan full-crop tithe rule, printed Rabbah repeater, Hisda challenge and cross-folio rainfall proof.',
'59b:1':'Reread rainfall leaf outcomes, Rabbah counterchallenge, Hisda added-growth-only answer and Gamliel duplication question.',
'59b:2':'Reread entire-Mishnah Gamliel attribution and no-effort/effort distinction.',
'59b:3':'Reread untithed-tithe counterexample, scriptural exception and permitted/prohibited sowing explanation.',
'59b:4':'Reread Hanina Tirtah/Yannai rule and cross-folio permitted-growth inquiry.',
'60a:1':'Reread teruma-growth contradiction, second-growth correction, already-taught objection and persistent-seed novelty.',
'60a:2':'Reread tevel persistent-seed counterexample and final predominant-growth condition.',
'60a:3':'Reread chapter conclusion marker only.'}
if __name__=='__main__':a.save()
