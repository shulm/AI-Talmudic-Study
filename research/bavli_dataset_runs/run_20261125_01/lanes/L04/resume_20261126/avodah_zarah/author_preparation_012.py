"""Three-day preparation and Noahide whole-limb requirement, through full replies."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('avodah_zarah','Avodah Zarah','az.r012');a.agent_id='/root/avodah_continuation_2'
c=a.claim;q=a.question;e=a.e
parent='d3b1a777a71288fcbeab6b0417de20c4771b6a0b6bdc4e571a88bb63571d533a'
a.structure('days',['5b:'+str(i) for i in range(5,10)],'Three-day sacrificial preparation contrasted with ordinary slaughter and Pesah')
a.structure('limbs',['5b:10','5b:11','6a:1','6a:2','6a:3','6a:4'],'Whole limbs, terefa and the eligibility of animals in Noah’s ark')
rule=c('rule','5b:5','ג\' ימים אסור לשאת ולתת עמהם וכו\'','The discussion resumes the Mishnah’s three-day prohibition on dealings.',scope='Quoted Mishnah lemma; not new independent ruling')
longq=q('long_q','5b:5','ומי בעינן כולי האי','Is such a long preparation period needed?')
notify=c('notify','5b:6','בארבעה פרקים בשנה המוכר בהמה לחבירו צריך להודיעו אמה מכרתי לשחוט בתה מכרתי לשחוט','A quoted Mishnah requires a seller at four annual times to disclose sale of the animal’s mother or daughter for slaughter.',conditions=['four listed annual occasions'],composition='composite',scope='Quoted rule supporting the short-preparation objection; mother/daughter alternatives not simultaneous obligatory events')
sukkot=c('sukkot','5b:7','עיו"ט האחרון של חג','The listed times include the eve of the final festival day of Sukkot.',scope='First listed time in quoted Mishnah')
pesah=c('pesah','5b:7','עיו"ט הראשון של פסח','They include the eve of the first festival day of Pesah.',scope='Second listed time')
shavuot=c('shavuot','5b:7','וערב עצרת','They include the eve of Shavuot.',scope='Third listed time')
rosh=c('rosh','5b:7','וערב ר"ה','They include the eve of Rosh Hashanah.',scope='Fourth listed time')
galil=c('galil','5b:7','וכדברי ר\' יוסי הגלילי אף ערב יוה"כ בגליל','Rabbi Yosei HaGelili adds the eve of Yom Kippur in Galilee.',candidates=['רבי יוסי הגלילי'],conditions=['Galilee'],scope='Named additional occasion; geographic restriction retained')
eat=c('eat','5b:8','התם דלאכילה סגיא בחד יומא','For eating, one day of preparation suffices.',conditions=['preparing for eating'],scope='Anonymous distinction answering the timing objection')
offer=c('offer','5b:8','הכא דלהקרבה בעינן תלתא יומי','Here, preparation for sacrifice requires three days.',conditions=['preparing sacrifice'],scope='Reason for the pre-festival prohibition in this argument')
enoughq=q('enough_q','5b:8','ולהקרבה סגי בתלתא יומי','Are three days sufficient for sacrificial preparation?')
thirty=c('thirty','5b:8','והתנן שואלין בהלכות הפסח קודם הפסח שלשים יום','A quoted Mishnah specifies discussing Pesah laws thirty days before Pesah.',scope='First position in quoted Mishnah; not practical ruling outside the argument')
two=c('two','5b:8','רשב"ג אומר שתי שבתות','Rabban Shimon ben Gamliel says two weeks.',candidates=['רבן שמעון בן גמליאל'],scope='Alternative duration in cited Mishnah')
blemish=c('blemish','5b:9','אנן דשכיחי מומין דפסלי אפילו בדוקין שבעין בעינן תלתין יומין','The reply says Israel needs thirty days because disqualifying blemishes are common, even in the eye’s membranes.',conditions=['Israel’s sacrificial requirements'],scope='Argument’s reason for the longer period; דוקין retained without precise modern diagnosis')
limbperiod=c('limbperiod','5b:9','אינהו דמחוסר אבר אית להו בתלתא יומי סגי','For the other group, whose applicable defect is a missing limb, three days suffice.',conditions=['Noahide sacrificial requirements'],scope='Contrast in this discussion; no blanket claim that all other offering rules are absent')
limbq=q('limb_q','5b:10','מנין למחוסר אבר דאסור לבני נח','Rabbi Elazar asks the source prohibiting an animal missing a limb for Noahides.',candidates=['רבי אלעזר'])
life=c('life','5b:10','דכתיב (בראשית ו, יט) ומכל החי מכל בשר שנים מכל וגו\'','The proof cites bringing into the ark from every living thing and flesh.')
whole=c('whole','5b:10','אמרה תורה הבא בהמה שחיין ראשי אברים שלה','The verse is read as requiring an animal whose extremities are alive.',candidates=['רבי אלעזר'],scope='Rabbi Elazar’s interpretation; Torah quotation is interpretive paraphrase, not newly invented biblical wording')
terefa=c('terefa','5b:11','האי מיבעי ליה למעוטי טריפה','The objection says that wording is needed to exclude a terefa.',scope='Proposed competing use of the verse; not final derivation')
seed=c('seed','5b:11','דלא טריפה מלחיות זרע נפקא','The reply derives exclusion of terefa from keeping seed alive.',scope='Initial response, immediately tested against the dispute over reproduction')
infertile=c('infertile','5b:11','הניחא למאן דאמר טריפה אינה יולדת','The reply fits the view that a terefa does not reproduce.',scope='Conditional concession; no named authority assigned')
fertileq=q('fertile_q','6a:1','אלא למ"ד טריפה יולדת מאי איכא למימר','How does the derivation work according to the view that a terefa reproduces?')
like=c('like','6a:1','אמר קרא אתך בדומין לך','The answer derives it from אתך, meaning like you, Noah.')
noahq=q('noah_q','6a:1','ודלמא נח גופיה טריפה הוה','Might Noah himself have been a terefa?')
perfect=c('perfect','6a:1','תמים כתיב ביה','The first reply cites Noah being described as תמים.')
conductq=q('conduct_q','6a:2','ודלמא תמים בדרכיו היה','Might תמים mean perfect in his conduct?')
righteous=c('righteous','6a:2','צדיק כתיב ביה','The reply notes that he is already called righteous.')
twoq=q('two_q','6a:3','דלמא תמים בדרכיו צדיק במעשיו הוה','Perhaps תמים describes his ways and צדיק his deeds?')
absurd=c('absurd','6a:3','לא ס"ד דנח גופיה טריפה הואי דאי ס"ד דנח טריפה הוה א"ל רחמנא כוותך עייל שלמין לא תעייל','The reply rejects the hypothesis because it would have God telling Noah to bring animals like a terefa Noah while excluding sound ones.',mode='hypothetical',scope='Reductio of the Noah-as-terefa hypothesis; not actual divine instruction',composition='composite')
seedq=q('seed_q','6a:4','והשתא דנפקא ליה מאתך לחיות זרע ל"ל','Once אתך excludes terefa, why is keeping seed alive needed?')
companions=c('companions','6a:4','אי מאתך הוה אמינא לצוותא בעלמא ואפילו זקן ואפילו סריס','From אתך alone one might require only companionship and admit even aged or sterile animals.',mode='rejected',conditions=['if only אתך were written'],scope='Hypothetical rejected by the seed requirement',composition='composite')
seedrequire=c('seedrequire','6a:4','כתב רחמנא זרע','The mention of seed therefore requires reproductive capacity.',scope='Conclusion explaining the otherwise redundant seed wording')
e('long_objection',longq,rule,'objection','5b:5');e('notify_support',notify,longq,'support','5b:6');e('eat_answer',eat,longq,'answer','5b:8');e('offer_distinction',offer,eat,'distinction','5b:8');e('thirty_support',thirty,enoughq,'support','5b:8');e('two_qualification',two,thirty,'qualification','5b:8');e('blemish_answer',blemish,enoughq,'answer','5b:9');e('limbperiod_answer',limbperiod,enoughq,'answer','5b:9');e('life_support',life,whole,'support','5b:10');e('whole_answer',whole,limbq,'answer','5b:10');e('whole_support',whole,limbperiod,'support','5b:10');e('terefa_objection',terefa,whole,'objection','5b:11');e('seed_answer',seed,terefa,'answer','5b:11');e('infertile_qualification',infertile,seed,'qualification','5b:11');e('like_answer',like,fertileq,'answer','6a:1');e('perfect_answer',perfect,noahq,'answer','6a:1');e('conduct_objection',conductq,perfect,'objection','6a:2');e('righteous_answer',righteous,conductq,'answer','6a:2');e('two_objection',twoq,righteous,'objection','6a:3');e('absurd_answer',absurd,twoq,'answer','6a:3');e('seedrequire_answer',seedrequire,seedq,'answer','6a:4');e('companions_support',companions,seedrequire,'support','6a:4')
for row in a.rows:
 if row['id'] in {longq,enoughq,limbq,fertileq,noahq,conductq,twoq,seedq}:
  row['content']['answer_set_status']='partial';row['uncertainty'].append('Specific local reply represented; no exhaustive comparable alternatives.')
a.save_window(['5b:'+str(i) for i in range(5,12)]+['6a:'+str(i) for i in range(1,5)],'preparation012.json','Read original through6a:16, reread full5b:5–6a:4 argument. Preserve occasion list and Galilee condition, eating/sacrifice distinction, two Pesah preparation views, unnamed terefa-reproduction alternatives, Noah hypothesis as reductio rather than fact, competing verse uses and final seed requirement. Eight layers reread; prior tails retained.',parent)
