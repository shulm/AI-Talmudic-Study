"""Direct reading15b15–16a2; offerings and competing scriptural readings."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r046');c=a.claim;e=a.e
refs=['15b:'+str(i) for i in range(15,19)]+['16a:1','16a:2']
def q(*args,**kw):
 v=a.question(*args,**kw);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Local evidence and replies only; no completeness or settled banned-person ruling.');return v
a.structure('offerings',refs,'Sending offerings: mourning, ban, leprosy and different readings')
m=c('mourner','15b:15','אבל אינו משלח קרבנותיו','A mourner does not send his offerings.',scope='Preserve source אבל and proof אונן without silently treating all stages of mourning as identical')
rs=c('rshimon','15b:15','ר"ש אומר שלמים בזמן שהוא שלם ולא בזמן שהוא אונן','Rabbi Shimon reads shelamim as applicable when one is whole, not an onen.',candidates=['רבי שמעון'],role='quoted_authority',scope='Baraita cited as support for preceding rule')
e('rs_support',rs,m,'support','15b:15')
bq=q('banq','15b:16','מנודה מהו שישלח קרבנותיו','May a banned person send offerings?')
p=c('proof','15b:16','אמר רב יוסף ת"ש כל אותן שנים שהיו ישראל במדבר מנודין היו ושלחו קרבנותיהן','Rav Yosef adduces the desert years: Israel were under a ban and sent offerings.',candidates=['רב יוסף'],scope='Proposed historical analogy')
obj=c('object','15b:16','א"ל אביי ודלמא מנודה לשמים שאני דקיל','Abaye objects that a heavenly ban may differ because it is lighter.',candidates=['אביי'],mode='hypothetical',scope='Repeated occurrence of a possible distinction, not settled severity ranking')
cq=q('contradiction','15b:17','קיל והאמרת חמיר','Lighter? Was it not called stricter?')
u=c('uncertain','15b:17','ספוקי מספקא ליה ומדחי ליה','He is uncertain and deflects the proof.',scope='Explains Abaye’s challenge without resolving severity or offerings')
e('proof_answer',p,bq,'answer','15b:16');e('object_proof',obj,p,'objection','15b:16');e('uncertain_answer',u,cq,'answer','15b:17');e('uncertain_qualifies',u,obj,'qualification','15b:17')
lq=q('leperq','15b:18','מצורע מהו שישלח קרבנותיו','May a leper send offerings?')
purity=c('purity','15b:18',"ואחרי טהרתו אחר פרישתו מן המת שבעת ימים יספרו לו אלו ז' ימי ספירו",'The cited teaching interprets purification as separation from a corpse and seven days as his counting period.',composition='composite',scope='Quoted exposition continues across page boundary; do not conflate corpse and leprosy categories')
verse=c('verse','15b:18','וביום באו אל הקודש אל החצר הפנימית לשרת בקודש יקריב חטאתו','The cited verse links entry into the inner court for service with bringing his offering.')
y=c('yehuda','16a:1','זו עשירית האיפה שלו דברי רבי יהודה','Rabbi Yehuda identifies the offering as his tenth of an ephah.',candidates=['רבי יהודה'],role='quoted_authority',scope='Cross-page baraita exposition')
s=c('shimon','16a:2','ר"ש אומר','Rabbi Shimon introduces a different reading.',candidates=['רבי שמעון'],role='quoted_authority')
ready=c('ready','16a:2','בזמן שראוי לביאה ראוי להקרבה','When fit for entry, one is fit for offering.',candidates=['רבי שמעון'],role='quoted_authority',conditions=['fit for entry'])
notready=c('notready','16a:2','בזמן שאינו ראוי לביאה אינו ראוי להקרבה','When unfit for entry, one is unfit for offering.',candidates=['רבי שמעון'],role='quoted_authority',conditions=['unfit for entry'],scope='Local derivation relevant to sending the leper’s offerings')
e('verse_y',verse,y,'support','16a:1');e('verse_ready',verse,ready,'support','16a:2');e('ready_distinction',ready,notready,'distinction','16a:2');e('readings',s,y,'distinction','16a:2');e('notready_answer',notready,lq,'answer','16a:2')
a.save_window(refs,'resume_moed_katan_offerings046.json','Read through17a26. Preserve mourning/onen terminology, repeated heavenly-ban analogy and unresolved severity, both named baraita readings across15b/16a, and positive/negative entry fitness conditions; no invented practical final ruling.','fea09f89683d31177e7b552960ded6aa24fce3b6dedcd0d5ed4c1ea944832d2a')
