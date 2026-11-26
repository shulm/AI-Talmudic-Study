"""Direct reading10b:5–11a:3: intention evidence, loss and technical work."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r025');c=a.claim;e=a.e
refs=['10b:'+str(i) for i in range(5,15)]+['11a:1','11a:2','11a:3']
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Local source-supported reply only, not exhaustive alternatives or certification.');return v
a.structure('intention',refs[:6],'Work purpose and observable distinctions')
a.structure('loss',refs[6:11],'Perishable merchandise, collection opportunity and market comparison')
a.structure('technical',refs[11:],'Nets, ovens and the seasonal reconciliation')
for key,ref,quote,text,condition in [
('thresh','10b:5','אדעתא דבי דרי שרי','Rava permits leveling for a threshing floor.','purpose: threshing floor'),
('soil','10b:5','אדעתא דארעא אסיר','Rava prohibits leveling to improve the soil.','purpose: soil improvement'),
('wood','10b:7','אדעתא דציבי שרי','Rava permits gathering twigs for firewood.','purpose: firewood'),
('clear','10b:7','אדעתא דארעא אסיר','Rava prohibits gathering to clear the soil.','purpose: soil improvement'),
('fish','10b:8','אדעתא דכוורי שרי','Rava permits opening water for fish.','purpose: fish'),
('water','10b:8','אדעתא דארעא אסיר','Rava prohibits opening water for irrigation.','purpose: soil'),
('animals','10b:10','אדעתא דחיותא שרי','Rava permits cutting palm material for animals.','purpose: animal feed'),
('palm','10b:10','אדעתא דדיקלא אסיר','Rava prohibits cutting for the palm’s improvement.','purpose: palm improvement')]:
 c(key,ref,quote,text,candidates=['רבא'],conditions=[condition],scope='Festival labor distinction in Rava’s sequence')
for key,ref,quote,text,targets in [
('groundtest','10b:6','מוליא במוליא ונצא בנצא אדעתא דבי דרי שקל מוליא ושדא בנצא אדעתא דארעא','Treating elevations separately and depressions separately indicates a threshing floor; moving earth from elevations into depressions indicates improving the soil.',['thresh','soil']),
('woodtest','10b:7','שקיל רברבי ושביק זוטרי אדעתא דציבי שקל רברבי וזוטרי אדעתא דארעא','Taking large twigs and leaving small ones indicates firewood; taking both indicates clearing the soil.',['wood','clear']),
('watertest','10b:9','פתח תרי בבי חד מעילאי וחד מתתאי אדעתא דכוורי פתח חד בבא אדעתא דארעא','Opening two outlets, above and below, indicates fish; opening one indicates irrigation.',['fish','water']),
('palmtest','10b:10','שקיל כוליה מחד גיסא אדעתא דחיותא מהאי גיסא ומהאי גיסא אדעתא דדיקלא ואסיר','Taking everything from one side indicates animal feed; taking from both sides indicates improving the palm and is prohibited.',['animals','palm'])]:
 cl=c(key,ref,quote,text,composition='composite',scope='Anonymous diagnostic explanation following Rava’s ruling')
 question=q(key+'_q',ref,'היכי דמי','How is the purpose distinguished?')
 e(key+'_answer',cl,question,'answer',ref)
 for target in targets:e(key+'_'+target,cl,'mk.r025.'+target+'.c','qualification',ref)
cut=c('cut','10b:11','הני תמרי תוחלני מיגזרינהו שרי','Rava permits cutting the תמרי תוחלני.',candidates=['רבא'],uncertainty=['The date category is retained literally rather than assigned an unsupported botanical stage.'])
press=c('press','10b:11','מייצינהו אסיר','Rava prohibits pressing them.',candidates=['רבא'],naming_refs=['10b:11'])
pappa=c('pappa','10b:11','רב פפא אמר כיון דמתלעי כפרקמטיא האבד דמי ושרי','Rav Pappa permits this because they become wormy and resemble perishable merchandise.',candidates=['רב פפא'],conditions=['risk of worms/spoilage'])
e('pappa_qualifies',pappa,press,'qualification','10b:11')
trade=c('trade','10b:12','ואמר רבא לפרקמטיא כל שהוא אסור','Rava prohibits trade even in a small amount.',candidates=['רבא'],scope='General local statement subject to the following loss exception')
loss=c('loss','10b:12','א"ר יוסי בר אבין ובדבר האבד מותר','Rabbi Yose bar Avin permits it in a case of loss.',candidates=['רבי יוסי בר אבין'],conditions=['loss'])
e('loss_exception',loss,trade,'qualification','10b:12')
profit=c('profit','10b:12','רבינא הוה ליה ההוא עיסקא דהוה מזדבן בשיתא אלפי שהייה לזבוניה בתר חולא דמועדא וזבניה בתריסר אלפי','Ravina deferred an investment sale from during the festival to afterward and sold for twelve thousand rather than the earlier six thousand.',scope='Reported particular narrative, not a promise of returns or an additional price rule',composition='composite')
debt=c('debt','10b:13','רבינא הוה מסיק זוזי בבני אקרא דשנואתא אתא לקמיה דרב אשי','Ravina had money owed by the inhabitants of Akra deShenavata and came to Rav Ashi.',scope='Collection narrative circumstances')
go=q('go','10b:13','א"ל מהו למיזל האידנא עלייהו','May he go to them now?',candidates=['רבינא'])
chance=c('chance','10b:13','א"ל כיון דהאידנא הוא דמשכחת להו ביומי אחריני לא משכחת להו כפרקמטיא האבד דמי ושרי','Rav Ashi permits because they can be found now but not on other days, so this resembles perishable merchandise.',candidates=['רב אשי'],conditions=['debtors available now and unavailable on other days'])
e('chance_answer',chance,go,'answer','10b:13')
parallel=c('parallel','10b:14','תניא נמי גבי ע"ז כי האי גוונא הולכין','A baraita concerning idolatry is introduced as a similar supporting case, continuing on the next page.',scope='Anonymous cross-page introduction')
market=c('market','11a:1','ליריד של עכו"ם ולוקחים בהמה עבדים ושפחות בתים שדות וכרמים','The baraita permits going to the market and purchasing animals, male and female slaves, houses, fields and vineyards.',scope='Historical source list retained in the quoted market rule',composition='composite')
record=c('record','11a:1','וכותב ומעלה בערכאות שלהן מפני שהוא כמציל מידן','It permits writing and registering in their courts because this is considered rescuing from their possession.',scope='Quoted rationale of the historical market rule',composition='composite')
e('market_support',market,chance,'analogy','11a:1');e('record_reason',record,market,'support','11a:1')
net=c('net','11a:2','רב שרא לחייא בר אשי למיגדל אוהרי בחולא דמועדא','Rav permitted Hiyya bar Ashi to weave אוהרי during the festival.',candidates=['רב'],scope='Reported permission; Hiyya bar Ashi is recipient, not Rav himself')
netwhy=q('netwhy','11a:2','מאי טעמא מעשה הדיוט הוא','Why? It is unskilled work.')
netreason=c('netreason','11a:2','מעשה הדיוט הוא','The work is classed as unskilled.')
izli=c('izli','11a:2','אבל איזלי אסור','איזלי work is prohibited.',uncertainty=['Technical distinction אוהרי/איזלי retained without an unsupported specific craft reconstruction.'])
izliwhy=q('izliwhy','11a:2','מאי טעמא מעשה אומן הוא','Why? It is skilled work.')
izlireason=c('izlireason','11a:2','מעשה אומן הוא','This operation is classed as skilled.')
for key,reason,question,target in [('net',netreason,netwhy,net),('izli',izlireason,izliwhy,izli)]:
 e(key+'_reason',reason,target,'support','11a:2');e(key+'_answer',reason,question,'answer','11a:2')
oven=c('oven','11a:3','רב יהודה שרא לאמי תנורא למיגדל תנורי','Rav Yehuda permitted Ami the oven maker to construct ovens.',candidates=['רב יהודה'])
sieve=c('sieve','11a:3',"ולרב' בר עשבי למיגדל מהולתא",'He permitted the person printed as רב\' בר עשבי to construct sieves.',candidates=['רב יהודה'],uncertainty=['Recipient’s abbreviated printed name retained, not silently expanded.'])
bar=c('bar','11a:3','והא תני רבה בר שמואל ושוין שאין גודלין תנור לכתחילה','Rabbah bar Shmuel teaches agreement that an oven is not newly constructed.',candidates=['רבה בר שמואל'],role='quoted_authority')
challenge=q('challenge','11a:3','איני','Is that so?')
season=c('season','11a:3','לא קשיא כאן בימות החמה כאן בימות הגשמים','The answer distinguishes summer from the rainy season.',composition='composite',scope='Seasonal reconciliation',uncertainty=['The compact כאן/כאן response is retained without assigning its clauses by order alone.'])
e('bar_objection',bar,oven,'objection','11a:3');e('season_answer',season,challenge,'answer','11a:3');e('season_distinguishes',season,bar,'distinction','11a:3')
a.save_window(refs,'resume_moed_katan_intention025.json','Source read through11b:13; directly annotate10b:5–11a:3 with every purpose test, loss condition, money narrative, cross-page market quotation and craft distinction. Preserve technical terms, abbreviated name and unassigned seasonal clauses rather than inventing specificity.','bfb93face7cc8abab771ae0191470236065820f5172f01dcb1662c767de4649e')
