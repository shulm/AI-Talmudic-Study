"""Direct reading13b:3–14: drying figs, private trades and unresolved grain definition."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r037');c=a.claim;e=a.e
refs=['13b:'+str(i) for i in range(3,15)]
def q(*args,answered=True,**kwargs):
 v=a.question(*args,**kwargs)
 if answered:a.rows[-1]['content']['answer_set_status']='partial'
 a.rows[-1]['uncertainty'].append('Only represented source replies; not exhaustive alternatives.' if answered else 'Local challenge left קשיא; no missing answer fabricated.')
 return v
a.structure('figs',refs[:2],'Fig covering terms and unassigned transmitted explanations')
a.structure('trades',refs[2:4],'Self-imposed stringency of named local trades')
a.structure('grain',refs[4:8],'Grain terms, impurity and vow objection')
a.structure('market',refs[8:11],'Shop visibility, festival honor and commodity distinction')
a.structure('chapter',[refs[11]],'Explicit chapter completion marker')
cover=c('cover','13b:3','מחפין את הקציעות בקש','The Mishnah permits covering drying figs with straw.')
thicken=c('thicken','13b:3','רבי יהודה אומר אף מעבין','Rabbi Yehuda also permits מעבין.',candidates=['רבי יהודה'],scope='Term explained by the following alternative reports')
sellers=c('sellers','13b:3','מוכרי פירות כסות וכלים מוכרים בצנעה לצורך המועד','Sellers of fruit, clothing and utensils sell privately for festival needs.',conditions=['private','festival need'],composition='composite')
processors=c('processors','13b:3','הציידין והדשושות והגרוסות עושין בצנעה לצורך המועד','Hunters and grain processors work privately for festival needs.',conditions=['private','festival need'],composition='composite')
yose=c('yose','13b:3','רבי יוסי אומר הם החמירו על עצמן','Rabbi Yose says they imposed stringency upon themselves.',candidates=['רבי יוסי'],scope='Ambiguous extent explicitly questioned below')
report=c('report','13b:4','פליגי בה רבי חייא בר אבא ורבי אסי ותרוייהו משמיה דחזקיה ורבי יוחנן','Rabbi Hiyya bar Abba and Rabbi Asi differ, both reporting in the names of Hizkiya and Rabbi Yohanan.',composition='composite',scope='Transmission report; no assignment of following anonymous formulations by name order',uncertainty=['No one-to-one mapping of formulations to transmitters or authorities is asserted.'])
first=c('first','13b:4','חד אמר מחפין אקלושי מעבין אסמוכי','One account defines covering as a light layer and מעבין as a thick layer.',candidates=['unassigned member of reported pair'],composition='composite')
second=c('second','13b:4','וחד אמר מחפין בין אקלושי בין אסמוכי מעבין עושה אותו כמין כרי','The other includes light and thick layers under covering and defines מעבין as making a heap.',candidates=['unassigned member of reported pair'],composition='composite')
bar=c('bar','13b:4',"תניא נמי הכי מעבין עושה אותו כמין כרי דברי ר' יהודה",'A baraita supports the heap definition as Rabbi Yehuda’s view.',candidates=['רבי יהודה'],role='quoted_authority')
e('bar_support',bar,second,'support','13b:4')
stringency=q('stringency','13b:5','הן החמירו על עצמן דלא הוו עבדי כלל או דלמא דהוו עבדי בצנעה','Was their stringency total abstention from work or working privately?',composition='composite')
for key,quote,text in [('tiberias','תגרי טבריא הן החמירו על עצמן שלא יהו מוכרין כל עיקר','Rabbi Yose says Tiberias merchants abstained from selling altogether.'),('acre','צדי עכו הן החמירו על עצמן שלא יהו צדין כל עיקר','Rabbi Yose says Acre hunters abstained from hunting altogether.'),('sepphoris','דשושי ציפורי הן החמירו על עצמן שלא יהו דוששין כל עיקר','Rabbi Yose says Sepphoris grain processors abstained from processing altogether.')]:
 cl=c(key,'13b:6',quote,text,candidates=['רבי יוסי']);e(key+'_answer',cl,stringency,'answer','13b:6')
for key,quote,text in [('selling','מוכרי פירות כסות וכלים מוכרין בצנעה לצורך המועד','The baraita allows fruit, clothing and utensil sales privately for festival needs.'),('hunting','צדי חיות ועופות ודגים צדין בצנעה לצורך המועד','It allows hunting animals, birds and fish privately for festival needs.'),('processing','דשושי חילקא טרגיס וטיסני דוששין בצנעה לצורך המועד','It allows processing hilka, targis and tisni privately for festival needs.')]:
 c(key,'13b:6',quote,text,conditions=['private','festival need'],composition='composite',scope='Repeated source occurrence with distinct local examples retained')
for key,quote,text in [('hilka','אמר אביי חילקא חדא לתרתי','Abaye defines hilka as one grain split into two.'),('targis','טרגיס חדא לתלת','He defines targis as one split into three.'),('tisni','טיסני חדא לארבעה','He defines tisni as one split into four.')]:c(key,'13b:7',quote,text,candidates=['אביי'])
dimi=c('dimi','13b:7','כי אתא רב דימי אמר כונתא','Rav Dimi reports the definition כונתא.',candidates=['רב דימי'],mode='challenged',scope='Alternative definition facing impurity and vow objections; exact technical term preserved')
impure=c('impure','13b:8','חילקא טרגיס וטיסני טמאין בכל מקום','The cited baraita calls hilka, targis and tisni impure everywhere.',composition='composite',scope='Source rule used as objection')
wet=c('wet','13b:8','בשלמא למ"ד חדא לתרתי לתלת ולארבעה משום הכי טמאין בכל מקום דאתכשור','Under the split-grain definition the impurity rule is understandable because they were made susceptible.',scope='Compatibility argument, not an added finding of actual impurity for a particular item')
why=q('why','13b:8','אלא למ"ד כונתא אמאי טמאין בכל מקום הא לא איתכשור','Under the כונתא definition, why impurity everywhere if they were not made susceptible?')
peeled=c('peeled','13b:9','כגון דמיקלפן דאי לאו דשרא להו במיא לא הוה מיקלפא','The response posits peeled grains, whose peeling presupposes soaking in water.',conditions=['peeled grains'],scope='Reply to susceptibility objection')
nameq=q('nameq','13b:9','ואמאי קרי ליה חילקא','Why is it called hilka?')
part=c('part','13b:9','דשקל חלקיהו','Because their portion was removed.',scope='Etymological explanation in the source')
e('why_objection',why,dimi,'objection','13b:8');e('peeled_answer',peeled,why,'answer','13b:9');e('part_answer',part,nameq,'answer','13b:9')
vow=c('vow','13b:10','הנודר מן הדגן אסור אף בפול המצרי יבש ומותר בלח ומותר באורז בחילקא וטרגיס וטיסני','A grain vow includes dried Egyptian beans but permits fresh beans, rice, hilka, targis and tisni.',composition='composite',scope='Cited vow taxonomy; each allowed/excluded category retained')
changed=c('changed','13b:10','בשלמא למ"ד חדא לתרתי חדא לתלת וחדא לארבעה שפיר דנפקו להו מתורת דגן','Under split-grain definitions, the items have left the category of grain.',scope='Compatibility explanation')
still=q('still','13b:10','אלא למ"ד כונתא דגן מעליא הוא','Under the כונתא definition, is it not ordinary grain?',answered=False)
difficult=c('difficult','13b:10','קשיא','The challenge remains difficult.',mode='unresolved')
e('still_objection',still,dimi,'objection','13b:10');e('difficult_outcome',difficult,still,'unresolved_outcome','13b:10')
market=c('market','13b:11','רב הונא שרא להו להנהו כרופייתא למיזל לזבוני כי אורחייהו בשוקא','Rav Huna permitted the כרופייתא sellers to sell in the market in their usual manner.',candidates=['רב הונא'],scope='Narrative ruling, commodity clarified in following reply')
challenge=q('challenge','13b:11','איתיביה רב כהנא','Rav Kahana challenges with the shop-opening rules.',candidates=['רב כהנא'])
portico=c('portico','13b:11','חנות פתוחה לסטיו פותח ונועל כדרכו','A shop opening to a portico may open and close normally.',conditions=['opens to portico'])
public=c('public','13b:12','פתוחה לרה"ר פותח אחת ונועל אחת','A shop opening to the public domain opens one part and closes one.',conditions=['opens to public domain'])
last=c('last','13b:12','וערב יום טוב האחרון של חג מוציא ומעטר את שוקי העיר בפירות בשביל כבוד י"ט האחרון','On the eve of the festival’s last day, fruit may be displayed to adorn the city markets for its honor.',conditions=['eve of final festival day','honor of final festival day'])
only=c('only','13b:12','מפני כבוד י"ט האחרון אין שלא מפני כבוד י"ט לא','The discussion infers permission for that honor but not otherwise.',scope='Objection inference from the baraita')
dist=c('dist','13b:13','לא קשיא הא בפירי הא בתבלין','The reply distinguishes fruit from spices.',composition='composite',scope='Commodity-based reconciliation, not a denial of either source')
e('only_objection',only,market,'objection','13b:12');e('dist_answer',dist,challenge,'answer','13b:13')
a.speech('marker','13b:14','הדרן עלך מי שהפך',act='chapter-completion formula',uncertainty=['Paratext, not a named legal position.'])
a.save_window(refs,'resume_moed_katan_trades037.json','Read13b through14a continuation. Preserve unassigned paired definitions and baraita support, all self-imposed city/trade examples, grain technical uncertainty, conditional impurity response, unresolved vow challenge, market visibility/occasion rules and chapter marker.','ceecda02f23ef0ad73e8216f715a80896ef0adc2d39ddf261c76fc10fcf9371c')
