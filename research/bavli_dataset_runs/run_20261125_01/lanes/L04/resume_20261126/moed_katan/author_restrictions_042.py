"""Direct reading14b:21–15a:13: haircut, head covering, tefillin and greetings."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r042');c=a.claim;e=a.e
refs=['14b:21']+['15a:'+str(i) for i in range(1,14)]
def q(*args,answered=True,**kwargs):
 v=a.question(*args,**kwargs)
 if answered:a.rows[-1]['content']['answer_set_status']='partial'
 a.rows[-1]['uncertainty'].append('Only source-present proof/reply inventory; rejected proofs do not certify final resolution.' if answered else 'Explicit unresolved question; no answer fabricated.')
 return v
a.structure('hair',refs[:3],'Haircut restrictions and the coffin-stone qualification')
a.structure('head',refs[3:10],'Head covering and tefillin: different statuses and rejected inference')
a.structure('greeting',refs[10:],'Greeting restrictions and limits of analogy to a banned person')
for key,ref,quote,text in [('hair','14b:21','אבל אסור בתספורת','A mourner is prohibited from haircutting.'),('head','15a:3','אבל חייב בעטיפת הראש','A mourner is required to cover the head.'),('tefillin','15a:6','אבל אסור להניח תפילין','A mourner is prohibited from wearing tefillin.'),('greeting','15a:10','אבל אסור בשאילת שלום','A mourner is prohibited from greeting.')]:
 c(key,ref,quote,text,scope='Local source rule; do not add unstated duration or subsequent halakhic qualifications')
for key,ref,quote,text,target in [('aaron','14b:21','מדקאמר להו רחמנא לבני אהרן (ויקרא י, ו) ראשיכם אל תפרעו מכלל דכולי עלמא אסור','The exception commanding Aaron’s sons not to let their heads grow wild implies the general prohibition.','hair'),('ezekiel_head','15a:3','מדקאמר ליה רחמנא ליחזקאל (יחזקאל כד, יז) ולא תעטה על שפם מכלל דכולי עלמא מיחייבי','The exceptional command to Ezekiel not to cover the upper lip implies the general obligation.','head'),('ezekiel_tefillin','15a:6','מדקאמר ליה רחמנא ליחזקאל (יחזקאל כד, יז) פארך חבוש עליך מכלל דכ"ע אסור','Ezekiel’s exceptional instruction to wear his adornment implies the general prohibition.','tefillin'),('ezekiel_greeting','15a:10','דקאמר ליה רחמנא ליחזקאל (יחזקאל כד, יז) האנק דום','Ezekiel’s instruction האנק דום is cited for the greeting restriction.','greeting')]:
 cl=c(key,ref,quote,text,scope='Source’s derivation from a biblical instruction, not an independent biblical speaker’s amoraic opinion');e(key+'_support',cl,'mk.r042.'+target+'.c','support',ref)
hairq=q('hairq','15a:1','מנודין ומצורעין מה הן בתספורת','What are the haircut rules for banned persons and lepers?',composition='composite')
hairrule=c('hairrule','15a:1','מנודין ומצורעין אסורין לספר ולכבס','A baraita prohibits haircutting and washing for banned persons and lepers.',composition='composite')
e('hair_answer',hairrule,hairq,'answer','15a:1')
coffin=c('coffin','15a:2','מנודה שמת ב"ד סוקלין את ארונו','For a person who dies under a ban, the court stones his coffin.',scope='Quoted rule with immediate Rabbi Yehuda clarification')
heap=c('heap','15a:2',"ר' יהודה אומר לא שיעמידו עליו גל אבנים כגלו של עכן",'Rabbi Yehuda excludes making a heap like Achan’s heap of stones.',candidates=['רבי יהודה'])
stone=c('stone','15a:2','אלא ב"ד שולחין ומניחין אבן גדולה על ארונו','Instead the court sends and places a large stone on the coffin.',candidates=['רבי יהודה'])
lesson=c('lesson','15a:2','ללמדך שכל המתנדה ומת בנידויו ב"ד סוקלין את ארונו','The explanation presents this as the sign that one who dies under a ban has the coffin stoned.',scope='Source explanation of the symbolic practice')
e('heap_limits',heap,coffin,'qualification','15a:2');e('stone_explains',stone,coffin,'qualification','15a:2');e('lesson_reason',lesson,stone,'support','15a:2')
banhead=q('banhead','15a:4','מנודה מהו בעטיפת הראש','Does a banned person cover the head?')
wrap=c('wrap','15a:4','אמר רב יוסף ת"ש והן מתעטפין ויושבין כמנודין וכאבלים עד שירחמו עליהם מן השמים','Rav Yosef adduces people wrapping themselves and sitting like banned persons and mourners until heaven has mercy.',candidates=['רב יוסף'],role='quoted_authority',scope='Contested analogy, not a decisive general rule')
severe=c('severe','15a:4','א"ל אביי דלמא מנודה לשמים שאני דחמיר','Abaye responds that a person banned by heaven may be different because that status is more severe.',candidates=['אביי'],mode='hypothetical',scope='Distinction that blocks the proposed inference')
e('wrap_answer',wrap,banhead,'answer','15a:4');e('severe_objection',severe,wrap,'objection','15a:4')
leperhead=q('leperhead','15a:5','מצורע מהו בעטיפת הראש','Does a leper cover the head?')
headproof=c('headproof','15a:5','ועל שפם יעטה מכלל שחייב בעטיפת הראש ש"מ','The verse requiring covering the upper lip establishes the head-covering obligation.')
e('headproof_answer',headproof,leperhead,'answer','15a:5')
bant=q('bant','15a:7','מנודה מהו בתפילין','What is the tefillin rule for a banned person?',answered=False)
remain=c('remain','15a:7','תיקו','The banned-person tefillin question is left unresolved.',mode='unresolved')
e('remain_outcome',remain,bant,'unresolved_outcome','15a:7')
lepert=q('lepert','15a:7','מצורע מהו בתפילין','What is the tefillin rule for a leper?')
include=c('include','15a:7','והצרוע לרבות כ"ג','The cited exposition includes the High Priest as a leper.')
torn=c('torn','15a:7','בגדיו יהיו פרומים שיהו מקורעים','His garments shall be פרומים means torn.')
hairgrow=c('hairgrow','15a:7','וראשו יהיה פרוע אין פריעה אלא גידול שער דברי ר"א','The authority printed ר"א explains the uncovered-head wording as growing hair.',candidates=['ר"א (printed abbreviation)'],role='quoted_authority',uncertainty=['Do not expand the abbreviated personal name without further textual evidence.'])
akiva=c('akiva','15a:8','ר"ע אומר נאמרה הוייה בראש ונאמרה הוייה בבגד מה הוייה האמורה בבגד דבר שחוץ מגופו אף הוייה בראש דבר שחוץ מגופו','Rabbi Akiva compares the wording for head and garment, inferring something external to the body for the head too.',candidates=['רבי עקיבא'],composition='composite')
tefillinq=q('tefillinq','15a:8','מאי לאו אתפילין','Does this not refer to tefillin?')
cap=c('cap','15a:9','אמר רב פפא לא אכומתא וסודרא','Rav Pappa rejects that identification and refers it to cap and cloth.',candidates=['רב פפא'],composition='composite',scope='Defeats this proof about tefillin; no opposite tefillin ruling invented')
e('akiva_answer',akiva,lepert,'answer','15a:8');e('cap_answer',cap,tefillinq,'answer','15a:9')
bang=q('bang','15a:11','מנודה מהו בשאילת שלום','May a banned person exchange greetings?')
reproof=c('reproof','15a:11','אמר רב יוסף ת"ש ובשאילת שלום שבין אדם לחברו כבני אדם הנזופין למקום','Rav Yosef adduces greeting behavior like people rebuked by heaven.',candidates=['רב יוסף'],role='quoted_authority')
severe2=c('severe2','15a:11','א"ל אביי דלמא מנודה לשמים שאני דחמיר','Abaye again distinguishes possible greater severity of being banned by heaven.',candidates=['אביי'],mode='hypothetical')
e('reproof_answer',reproof,bang,'answer','15a:11');e('severe2_objection',severe2,reproof,'objection','15a:11')
leperg=q('leperg','15a:12','מצורע מהו בשאילת שלום','May a leper exchange greetings?')
lips=c('lips','15a:12','ועל שפם יעטה שיהו שפתותיו מדובקות זו בזו שיהא כמנודה וכאבל ואסור בשאילת שלום ש"מ','The exposition requires joined lips, like a banned person and mourner, and prohibits greeting.',composition='composite',scope='Proof for leper; extension to banned persons is explicitly challenged below')
e('lips_answer',lips,leperg,'answer','15a:12')
baninfer=q('baninfer','15a:13','וניפשוט מינה למנודה','Should this also resolve the banned-person question?')
separate=c('separate','15a:13','אמר רב אחא בר פנחס משמיה דרב יוסף מי קתני שאסור שיהא כמנודה וכאבל [קתני] במילי אחרנייתא ואסור נמי בשאילת שלום','Rav Aha bar Pinhas transmits Rav Yosef: the text does not say that similarity is because of greeting prohibition; the similarity can concern other matters, with greeting additionally prohibited for the leper.',candidates=['רב יוסף'],role='quoted_authority',chain=['רב אחא בר פנחס','רב יוסף'],composition='composite',scope='Blocks extension of this leper proof; bracketed קתני preserved')
e('separate_answer',separate,baninfer,'answer','15a:13')
a.save_window(refs,'resume_moed_katan_restrictions042.json','Readthrough16a:23. Preserve every status separately, symbolic stone qualification, biblical proofs, twice-blocked heavenly-ban analogy, explicit tefillin תיקו, unexpanded ר"א, rejected tefillin inference and limited greeting comparison without fabricating unresolved rulings.','581a719940c69f6efbbf515180a51cd35798eb22574a3dfc65618d7318854241')
