"""Direct reading13a:6–13, poverty wages and invalid analogy to Passover eve."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r035');c=a.claim;e=a.e
refs=['13a:'+str(i) for i in range(6,14)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Local source replies only; no exhaustive comparable inventory.');return v
a.structure('wages',refs[:3],'Purchase exception, worker’s food need and competing proof readings')
a.structure('eve',refs[3:],'Passover-eve crafts challenge and limits of cross-regime inference')
purchases=c('purchases','13a:6','אין לוקחין בתים עבדים ובהמה אלא לצורך המועד או לצורך המוכר שאין לו מה יאכל','The Mishnah excludes purchasing houses, slaves or animals except for festival needs or a seller who has nothing to eat.',conditions=['festival need or seller lacks food'],composition='composite')
wageq=q('wageq','13a:7','בעא מיניה רבא מרב נחמן שכר פעולה שאין לו מה יאכל מהו','Rava asks Rav Nahman about work wages when the worker has nothing to eat.',candidates=['רבא'])
first=c('first','13a:7','א"ל תנינא או לצורך המוכר שאין לו מה יאכל','Rav Nahman proposes the Mishnah’s food-need exception as evidence.',candidates=['רב נחמן'],scope='Initial proposed proof, challenged as a possible explanatory phrase')
includeq=q('includeq','13a:7','לאתויי מאי לאו לאתויי שכר פעולה','What does it include—does it not include wages?',candidates=['רב נחמן'])
reject=c('reject','13a:7','א"ל לא פרושי קא מפרש','Rava replies that it may simply explain the seller exception.',candidates=['רבא'],scope='Rejection of this proof, not a final denial of worker permission',uncertainty=['Speaker follows the Rava/Rav Nahman dialogue; clause itself uses א"ל.'])
e('first_answer',first,wageq,'answer','13a:7');e('reject_first',reject,first,'objection','13a:7');e('reject_include',reject,includeq,'answer','13a:7')
debts=c('debts','13a:8','איתיביה אביי אין כותבין שטרי חוב במועד ואם אינו מאמינו או שאין לו מה יאכל ה"ז יכתוב','Abaye adduces the rule against writing debt documents during the festival, with exceptions for lack of trust or having nothing to eat.',candidates=['אביי'],role='quoted_authority',conditions=['lack of trust or no food for exception'],composition='composite')
include2=q('include2','13a:8','שאין לו מה יאכל לאתויי מאי לאו לאתויי שכר פעולה','What does the food-need clause include, if not the worker’s wages?')
infer=c('infer','13a:8','שמע מינה','The inference is accepted.',scope='Acceptance of the wage inference from the debt-document proof')
e('infer_answer',infer,include2,'answer','13a:8');e('infer_wages',infer,wageq,'answer','13a:8');e('debts_support',debts,infer,'support','13a:8')
crafts=c('crafts','13a:9','מותיב רב ששת וחכ"א שלש אומניות עושין מלאכה בערבי פסחים עד חצות החייטין והספרין והכובסין','Rav Sheshet objects from the sages permitting three crafts until midday on Passover eve: tailors, barbers and launderers.',candidates=['חכמים'],role='quoted_authority',chain=['רב ששת','חכמים'],conditions=['Passover eve','until midday'],composition='composite')
tailor=c('tailor','13a:9','החייטין שכן הדיוט תופר כדרכו בחולו של מועד','Tailors are explained by ordinary sewing permitted to an unskilled person during the festival.')
barber=c('barber','13a:9','הספרין והכובסין שכן הבאין ממדינת הים והיוצא מבית האסורין מותרין לספר ולכבס בחולו של מועד','Barbers and launderers are explained by festival permission for those arriving from overseas or leaving prison.',conditions=['overseas arrival or release from prison'],composition='composite')
e('tailor_reason',tailor,crafts,'support','13a:9');e('barber_reason',barber,crafts,'support','13a:9')
allq=q('allq','13a:10','ואי ס"ד שכר פעולה שאין לו מה יאכל שרי כל מלאכות נמי לישתרו','If poverty wages are permitted, why not permit all crafts too?')
allreason=c('allreason','13a:10','דהא איכא שכר פעולה שאין לו מה יאכל','The challenge reasons that a worker needing food can arise in every craft.',scope='Premise of objection, not the final cross-regime rule')
e('all_objection',allq,infer,'objection','13a:10');e('all_reason',allreason,allq,'support','13a:10')
buildq=q('buildq','13a:11','מתקיף לה רב פפא אלא מעתה בנין לישתרי','Rav Pappa challenges: then construction should also be permitted.',candidates=['רב פפא'])
wall=c('wall','13a:11','שכן כותל הגוהה לרה"ר סותר ובונה כדרכו מפני הסכנה','A wall leaning toward the public domain may be demolished and rebuilt normally because of danger.',conditions=['wall leaning toward public domain','danger'],scope='Counterexample to deriving the Passover-eve craft list directly from festival exceptions')
e('wall_build',wall,buildq,'support','13a:11')
scribeq=q('scribeq','13a:12','מתקיף לה רבינא אלא מעתה לבלר לישתרי','Ravina challenges: then a scribe should also be permitted.',candidates=['רבינא'])
documents=c('documents','13a:12','שכן כותבין קידושי נשים גיטין ושוברין','Betrothal documents, divorce documents and receipts may be written.',composition='composite',scope='Further festival counterexample in the analogy debate')
e('documents_reason',documents,scribeq,'support','13a:12')
compareq=q('compareq','13a:13','אלא אמר רב אשי מועד אארבעה עשר קא רמית','Rav Ashi asks whether the festival is being compared with the fourteenth.',candidates=['רב אשי'])
festival=c('festival','13a:13','מועד משום טירחא הוא ובמקום פסידא שרו רבנן','For the festival, the restriction concerns effort and the sages permit in cases of loss.',candidates=['רב אשי'],conditions=['loss exception'],scope='Rav Ashi’s local distinction between regulatory settings')
eve=c('eve','13a:13','ארבעה עשר משום צורך יום טוב הוא מידי דצורך יו"ט שרו רבנן מידי דלאו צורך יום טוב לא שרו רבנן','On the fourteenth the criterion is festival need: the sages permit what serves it and exclude what does not.',candidates=['רב אשי'],conditions=['Passover eve','festival need'],composition='composite')
e('settings_distinction',eve,festival,'distinction','13a:13')
for key,question in [('all',allq),('build',buildq),('scribe',scribeq),('compare',compareq)]:e(key+'_answer',eve,question,'answer','13a:13')
a.save_window(refs,'resume_moed_katan_wages035.json','Read13a–14a source continuation. Preserve both distinct wage proofs, first rejected and second accepted, seller/worker conditions, sages quote via Rav Sheshet, all craft counterexamples, danger clause and Rav Ashi’s distinction without flattening different dates into identical rules.','b835b45014d8a28639db7a345f291e1e9949e4d8a9ee2181f14291635ceac3ef')
