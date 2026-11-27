"""Manual reading of grain, revenue, Rava/Yosef narrative and growth terminology."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r057.';a.OUTPUT='continuation_057.json'
c=a.c;e=a.edge;q=b.q
a.structure('grain',['55a:'+str(i) for i in range(1,5)],'Grain and produce categories; qualified scriptural phrase')
a.structure('revenue',['55a:'+str(i) for i in range(5,10)]+['55b:1'],'Rava revenue inquiry and Rav Yosef reconciliation narrative')
a.structure('growth',['55b:2','55b:3','55b:4'],'Year/earth produce versus growth and mushroom distinction')
meir=c('meir','55a:1','הנודר מן הדגן אסור בפול המצרי יבש דברי רבי מאיר','Rabbi Meir includes dry Egyptian beans in a grain vow.',holder='רבי מאיר',scope='דגן category dispute')
sages=c('sages','55a:1','וחכ"א אינו אסור אלא בחמשת המינין','The sages restrict the prohibition to the five grain species.',holder='חכמים',scope='Contrary scope of דגן')
produce=c('produce','55a:1','רבי מאיר אומר הנודר מן התבואה אינו אסור אלא מחמשת המינין','Rabbi Meir limits a תבואה vow to the five species.',holder='רבי מאיר',scope='Distinct term from דגן')
wide=c('wide','55a:1','אבל הנודר מן הדגן אסור בכל ומותר בפירות האילן ובירק','His דגן vow has broader scope but permits tree fruit and vegetables.',holder='רבי מאיר',composition='composite',scope='Broad statement explicitly bounded by two exclusions')
e('sages.objection',sages,meir,'objection','55a:1')
verseq=q('verseq','55a:2','למימרא דדגן כל דמידגן משמע מתיב רב יוסף (דברי הימים ב לא, ה) וכפרוץ הדבר הרבו בני ישראל [ראשית] דגן תירוש ויצהר וכל תבואת שדה לרוב וגו\' ואי אמרת דגן כל דמידגן משמע מאי כפרוץ הדבר הרבו','Rav Yosef asks how the verse describes expanded contributions if דגן already includes all gathered produce.',voice='רב יוסף')
abaye=c('abaye','55a:2','אמר אביי לאתויי פירות האילן וירק','Abaye answers that the expansion adds tree fruit and vegetables.',holder='אביי',composition='composite',scope='Two categories outside the stated broad grain meaning')
e('abaye.answer',abaye,verseq,'answer','55a:2')
yohanan=c('yohanan','55a:3','אמר ר\' יוחנן הכל מודים בנודר מן התבואה שאין אסור אלא מחמשת המינין','Rabbi Yohanan says all agree a תבואה vow covers only the five species.',holder="ר' יוחנן",scope='Explicit agreement on narrower term, not a new dispute')
bar=c('bar','55a:3','תניא נמי הכי שוין בנודר מן התבואה שאין אסור אלא מה\' המינין','A baraita likewise states agreement that תבואה covers only the five species.',scope='Independent quoted supporting occurrence')
obvious=q('obvious','55a:3','פשיטא','Why is this agreement not obvious?')
possible=c('possible','55a:3','מהו דתימא תבואה כל מילי משמע','One might have thought תבואה means everything.',mode='rejected',scope='Explicit rejected semantic supposition')
limit=c('limit','55a:3','קמשמע לן דלא משמע כל מילי','The teaching excludes that all-inclusive meaning.',scope='Answer defending the need for Yohanan’s statement')
e('bar.support',bar,yohanan,'support','55a:3');e('limit.answer',limit,obvious,'answer','55a:3');e('limit.correction',limit,possible,'correction','55a:3')
again=q('again','55a:4','מתיב רב יוסף וכפרוץ הדבר הרבו בני ישראל כו\'','Rav Yosef again challenges from the contributions verse.',voice='רב יוסף')
rava=c('rava','55a:4','אמר רבא תבואה לחוד תבואת שדה לחוד','Rava distinguishes תבואה alone from תבואת שדה.',holder='רבא',composition='composite',scope='Qualified scriptural phrase need not share unqualified vow meaning; Rava not Rabbah')
e('rava.answer',rava,again,'answer','55a:4')
bequest=c('bequest','55a:5','בר מר שמואל פקיד דליתנון תליסר אלפי זוזי לרבא מן עללתא דנהר פניא','The son of Mar Shmuel directs that thirteen thousand zuz be given to Rava from the עללתא of Nehar Panya.',composition='composite',scope='Named donor relation, amount, recipient and revenue source; not a ruling of Shmuel himself')
revenueq=q('revenueq','55a:5','שלחה רבא לקמיה דרב יוסף עללתא היכי מיקריא','Rava asks Rav Yosef what falls under עללתא.',voice='רבא')
yosef=c('yosef','55a:5','אמר רב יוסף מתניתין היא ושוין בנודר מן התבואה שאין אסור אלא מחמשת המינין','Rav Yosef invokes the Mishnah limiting תבואה to the five species.',holder='רב יוסף',mode='challenged',scope='Proposed analogy for עללתא challenged by Abaye')
contrast=c('contrast','55a:5','א"ל אביי מי דמי תבואה לא משמע אלא מחמשת המינין עללתא כל מילי משמע','Abaye objects that תבואה denotes only the five species whereas עללתא includes everything.',holder='אביי',composition='composite',scope='Explicit lexical distinction against Yosef analogy')
known=c('known','55a:6','אהדרוהו לקמיה דרבא אמר הא לא קא מיבעיא לי דעללתא כל מילי משמע','When the reply reaches Rava, he says he already knew עללתא has broad scope.',holder='רבא',scope='Clarifies that the broad-category issue was not his doubt')
rents=a.q('rents','55a:6','הדא הוא דאיבעיא לי שכר בתים ושכר ספינות מאי מי אמרינן כיון דפחתן לאו עללתא היא או דילמא כיון דלא ידיע פחתייהו עללתא היא','Rava’s question is whether house and ship rents count as עללתא: does asset depreciation exclude them, or does imperceptible depreciation permit their inclusion?',voice='רבא')
for row in a.records:
    if row['id']==rents:row['uncertainty'].append('The following personal reconciliation and exposition do not decide the two rental alternatives.')
angry=c('angry','55a:6','אמרוה רבנן קמיה דרב יוסף אמר וכי מאחר דלא צריך לן אמאי שלח לן איקפד רב יוסף','Hearing this, Rav Yosef asks why Rava sent to him if he did not need him, and becomes angry.',holder='רב יוסף',composition='composite',scope='Reported rhetorical complaint and emotional response; not a revenue ruling')
e('yosef.answer',yosef,revenueq,'answer','55a:5');e('contrast.objection',contrast,yosef,'objection','55a:5');e('known.qualification',known,revenueq,'qualification','55a:6')
visit=c('visit','55a:7','שמע רבא ואתא לקמיה במעלי יומא דכפורי','Rava hears and visits Rav Yosef on the eve of Yom Kippur.',scope='Narrative response to anger')
pour=c('pour','55a:7','אשכחיה לשמעיה דהוה קא מזיג קמיה כסא דחמרא אמר ליה הב לי דאמזיג ליה אנא יהב ליה וקא מזיג איהו כסא דחמרא','Rava takes over from the servant in mixing Rav Yosef’s cup of wine.',composition='composite',scope='Encounter, request and performed service')
recognize=c('recognize','55a:7','כי קא שתי אמר הדין מיזגא דמי למיזגא דרבא בריה דרב יוסף בר חמא אמר ליה הוא ניהו','Rav Yosef recognizes the mixture as like Rava son of Rav Yosef bar Hama’s, and Rava confirms it is he.',composition='composite',scope='Full patronymic distinguishes Rava’s father from the teacher Rav Yosef')
explain=q('explain','55a:8','אמר ליה לא תיתיב אכרעך עד דאמרת לי פירושא דהדין מילתא מאי דכתיב (במדבר כא, יח) וממדבר מתנה וממתנה נחליאל ומנחליאל במות','Rav Yosef asks Rava to explain the wilderness/gift/Nahaliel/Bamot verse before sitting.',voice='רב יוסף')
humble=c('humble','55a:9','א"ל כיון שעושה אדם את עצמו כמדבר שהוא מופקר לכל תורה ניתנה לו במתנה שנאמר וממדבר מתנה','Rava interprets becoming like an ownerless wilderness as receiving Torah as a gift.',holder='רבא',scope='Attributed homiletic mapping of the first phrase')
inherit=c('inherit','55a:9','וכיון שניתנה לו במתנה נחלו אל שנאמר וממתנה נחליאל','The next mapping says that once Torah is given as a gift, God grants him an inheritance.',holder='רבא',scope='Exact נחלו אל wording anchors interpretive paraphrase without resolving every grammatical nuance')
rise=c('rise','55a:9','וכיון שנחלו אל עולה לגדולה שנאמר ומנחליאל במות','The next mapping connects divine inheritance with rising to greatness.',holder='רבא',scope='Nahaliel-to-Bamot homiletic sequence')
pride=c('pride','55a:9','ואם הגביה עצמו הקב"ה משפילו שנאמר (במדבר כא, כ) ומבמות הגיא','If he exalts himself, God lowers him, read through the heights-to-valley verse.',holder='רבא',mode='conditional',scope='Homiletic warning about pride')
sink=c('sink','55a:9','ולא עוד אלא ששוקעין אותו בקרקע שנאמר (במדבר כא, כ) ונשקפה על פני הישימון','The exposition adds being sunk into the ground, citing the wilderness outlook phrase.',holder='רבא',scope='Further attributed consequence in homily')
repent=c('repent','55a:9','ואם חוזר בו הקב"ה מגביהו','If he turns back, God raises him.',holder='רבא',mode='conditional',scope='Final restorative condition with proof citation across folio',extra=[('55b:1','שנאמר (ישעיהו מ, ד) כל גיא ינשא')])
e('humble.answer',humble,explain,'answer','55a:9');e('rise.answer',rise,explain,'answer','55a:9');e('repent.answer',repent,explain,'answer','55b:1')
dry=c('dry','55b:2','תניא הנודר מן הדגן אסור אף בפול המצרי יבש ומותר בלח','A baraita includes dry Egyptian beans in a grain vow but permits moist ones.',composition='composite',scope='Dry/moist contrast, no explicit named holder supplied')
exclusions=c('exclusions','55b:2','ומותר באורז בחילקא בטרגיס ובטיסני','The baraita permits rice, חילקא, טרגיס and טיסני.',composition='composite',scope='All four exclusions retained; prepared-grain terms not collapsed into raw grain')
year=c('year','55b:2','הנודר מן פירות השנה אסור בכל פירות השנה ומותר בגדיים ובטלאים ובחלב ובביצים ובגוזלות','A vow against the year’s produce prohibits its produce but permits kids, lambs, milk, eggs and young birds.',composition='composite',scope='Produce category and complete five-item exclusion inventory')
yeargrowth=c('yeargrowth','55b:2','ואם אמר גידולי שנה עלי אסור בכולן','The phrase growths of the year prohibits all those items.',scope='Broader formulation includes preceding animal-derived inventory')
earth=c('earth','55b:3','הנודר מן פירות הארץ אסור בכל פירות הארץ ומותר בכמהין ופטריות','A vow against earth’s produce prohibits earth produce but permits כמהין and פטריות.',composition='composite',scope='Two named fungi categories excepted')
earthgrowth=c('earthgrowth','55b:3','ואם אמר גידולי קרקע עלי אסור בכולן','A vow against growths of the ground prohibits them all, including the fungi.',scope='Broader growth formula')
blessingq=q('blessingq','55b:4','ורמינהי על דבר שאין גידולו מן הארץ אומר שהכל נהיה בדברו ותניא על המלח ועל הזמית ועל כמהין ופטריות אומר שהכל נהיה בדברו','How can fungi be ground growths if the blessing rule lists salt, הזמית and both fungi under things not growing from the earth?')
nourish=c('nourish','55b:4','אמר אביי מירבא רבו מארעא מינק מאוירא ינקי ולא מארעא','Abaye distinguishes growing from the earth from drawing nourishment: fungi grow from earth but nourish from air.',holder='אביי',composition='composite',scope='Attributed ancient explanatory distinction, not modern biological assertion')
wordq=q('wordq','55b:4','והא קתני על דבר שאין גידולו מן הארץ','But the blessing teaching literally says not growing from the earth.')
read=c('read','55b:4','תני על דבר שאין יונק מן הארץ','The answer instructs reading: something not drawing nourishment from the earth.',scope='Explicit תני correction preserved without silently changing the quoted text')
e('nourish.answer',nourish,blessingq,'answer','55b:4');e('read.answer',read,wordq,'answer','55b:4')
a.notes={
'55a:1':'Reread Meir/sages grain dispute, Meir narrower produce formula and tree-fruit/vegetable exclusions.',
'55a:2':'Reread Yosef broad-grain verse objection and Abaye two-category expansion answer.',
'55a:3':'Reread Yohanan unanimity, supporting baraita, obviousness question and rejected all-inclusive meaning.',
'55a:4':'Reread repeated Yosef verse objection and Rava unqualified/qualified produce distinction.',
'55a:5':'Reread son-of-Mar-Shmuel bequest amount/place, Rava question, Yosef analogy and Abaye objection.',
'55a:6':'Reread Rava clarification, both house/ship depreciation alternatives and Yosef anger; rentals unresolved.',
'55a:7':'Reread eve-of-Yom-Kippur visit, mixing service, recognition and full Rava patronymic.',
'55a:8':'Reread Yosef exposition request and all three cited place names.',
'55a:9':'Reread all six homiletic stages with citations and final repentance condition.',
'55b:1':'Reread Isaiah citation completing preceding repentance-restoration claim.',
'55b:2':'Reread dry/moist beans, four grain-preparation exclusions and five year-produce exclusions versus growths.',
'55b:3':'Reread earth produce/fungi distinction and broader ground-growth formula.',
'55b:4':'Reread complete blessing objection list, Abaye growth/nourishment distinction, literal-wording objection and explicit corrected reading.'}
if __name__=='__main__':a.save()
