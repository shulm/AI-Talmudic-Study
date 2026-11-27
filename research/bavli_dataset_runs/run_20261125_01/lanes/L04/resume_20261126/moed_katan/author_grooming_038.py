"""Direct reading13b:15–14a:10: grooming exceptions and two lost-property versions."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r038');c=a.claim;e=a.e
refs=['13b:15','13b:16']+['14a:'+str(i) for i in range(1,11)]
def q(*args,answered=True,**kwargs):
 v=a.question(*args,**kwargs)
 if answered:a.rows[-1]['content']['answer_set_status']='partial'
 a.rows[-1]['uncertainty'].append('Local represented reply only; no exhaustive alternatives or certification.' if answered else 'Explicit תיקו retained, no answer invented.')
 return v
a.structure('mishna',refs[:4],'Named categories allowed festival haircutting and washing')
a.structure('reason',refs[4:7],'General restriction and preparation before the festival')
a.structure('lost',refs[7:],'Lost property, public recognizability and unresolved artisan variant')
for key,quote,text,condition in [('overseas','הבא ממדינת הים','One arriving from overseas may cut hair.','arrival from overseas'),('captivity','ומבית השביה','One returning from captivity may cut hair.','return from captivity'),('prison','והיוצא מבית האסורין','One leaving prison may cut hair.','release from prison'),('ban','והמנודה שהתירו לו חכמים','One whose ban the sages permitted to be lifted may cut hair.','sages permitted lifting the ban'),('vow','וכן מי שנשאל לחכם והותר','One who consulted a sage and was released from the vow may cut hair.','release after consultation'),('nazir','והנזיר והמצורע מטומאתו לטהרתו','The nazir and leper moving from impurity to purity may perform the required haircut.','transition from impurity to purity')]:
 c('cut_'+key,'13b:15',quote,text,conditions=[condition],scope='Mishnah festival haircut permission; later qualifications not collapsed',composition='composite' if key=='nazir' else 'atomic')
for key,ref,quote,text,condition in [('overseas','13b:16','הבא ממדינת הים','One arriving from overseas may wash garments.','arrival from overseas'),('captivity','13b:16','ומבית השביה','One returning from captivity may wash garments.','return from captivity'),('prison','13b:16','והיוצא מבית האסורין','One leaving prison may wash garments.','release from prison'),('ban','14a:1','ומנודה שהתירו לו חכמים','One whose ban the sages permitted to be lifted may wash garments.','sages permitted lifting the ban'),('vow','14a:1','וכן מי שנשאל לחכם והותר','One released after consulting a sage may wash garments.','vow release')]:
 c('wash_'+key,ref,quote,text,conditions=[condition],scope='Mishnah washing permission, continuing across page boundary')
cloths=c('cloths','14a:2','מטפחות הידים ומטפחות הספרים ומטפחות הספג','Hand towels, the cloths called מטפחות הספרים, and bathing cloths are included in the washing permissions.',composition='composite',uncertainty=['מטפחות הספרים is retained without choosing between possible vocalization-dependent glosses.'])
impure=c('impure','14a:2','הזבין והזבות והנדות והיולדות וכל העולין מטומאה לטהרה הרי אלו מותרין','The listed zavim, zavot, menstruants, postpartum women and all going from impurity to purity are permitted washing.',conditions=['listed purification categories'],composition='composite')
others=c('others','14a:2','ושאר כל אדם אסורין','Other people are prohibited.',scope='Mishnah general rule alongside enumerated exceptions')
why=q('why','14a:3','ושאר כל אדם מאי טעמא אסורין','Why are other people prohibited?')
watch=c('watch','14a:4','אנשי משמר ואנשי מעמד אסורין לספר ולכבס ובחמישי מותרין מפני כבוד השבת','The cited Mishnah prohibits haircutting and washing for the watch and maamad members but permits Thursday for Sabbath honor.',conditions=['Thursday exception for Sabbath honor'],composition='composite',scope='Analogous rule cited to explain preparation incentives')
prepare=c('prepare','14a:5',"ואמר רבה בר בר חנה אמר ר' אלעזר מ\"ט כדי שלא יכנסו למשמרתן כשהן מנוולין",'Rabbah bar bar Hana transmits Rabbi Elazar that the reason is to avoid entering the watch unkempt.',candidates=['רבי אלעזר'],role='quoted_authority',chain=['רבה בר בר חנה','רבי אלעזר'])
festival=c('festival','14a:5','הכא נמי כדי שלא יכנסו לרגל כשהן מנוולין','The same rationale is applied to avoiding entering the festival unkempt.',scope='Anonymous application of the quoted rationale')
e('prepare_support',prepare,festival,'analogy','14a:5');e('festival_answer',festival,why,'answer','14a:5')
lostq=q('lostq','14a:6',"בעי ר' זירא אבדה לו אבידה ערב הרגל כיון דאניס מותר או דלמא כיון דלא מוכחא מילתא לא",'Rabbi Zeira asks whether someone occupied by lost property before the festival is permitted because he was prevented, or prohibited because the circumstance is not publicly apparent.',candidates=['רבי זירא'],composition='composite')
shapes=c('shapes','14a:7','אמר אביי יאמרו כל הסריקין אסורין סריקי בייתוס מותרין','Abaye objects through the analogy: people would say all patterned loaves are prohibited but those of Baitos permitted.',candidates=['אביי'],scope='Analogy about an apparently arbitrary exception, not a new ruling on loaves')
e('shapes_answer',shapes,lostq,'answer','14a:7')
one=c('one','14a:8','הא דאמר רבי אסי אמר רבי יוחנן כל מי שאין לו אלא חלוק אחד מותר לכבסו בחולו של מועד','Rabbi Asi transmits Rabbi Yohanan permitting washing for one who has only one garment.',candidates=['רבי יוחנן'],role='quoted_authority',chain=['רבי אסי','רבי יוחנן'],conditions=['only one garment'])
challenge=q('challenge','14a:8','התם נמי יאמרו כל הסריקין אסורין סריקי בייתוס מותרין','Would the same complaint not apply to that case too?')
belt=c('belt','14a:9','אמר מר בר רב אשי איזורו מוכיח עליו','Mar son of Rav Ashi says his belt demonstrates his circumstance.',candidates=['מר בר רב אשי'],scope='Publicly recognizable evidence distinguishing the one-garment case')
e('challenge_objection',challenge,shapes,'objection','14a:8');e('belt_answer',belt,challenge,'answer','14a:9')
artisan=q('artisan','14a:10',"רב אשי מתני בעי ר' זירא אומן שאבדה לו אבידה ערב הרגל מהו כיון דאומן הוא מוכחא מילתא או דלמא כיון דלא מוכחא מילתא כי הנך לא",'Rav Ashi transmits a version of Rabbi Zeira’s question about an artisan who lost property before the festival: does his status make the interruption apparent, or is it insufficiently apparent compared with the listed cases?',candidates=['רבי זירא'],role='quoted_authority',chain=['רב אשי','רבי זירא'],composition='composite',answered=False)
unresolved=c('unresolved','14a:10','תיקו','The artisan-version question remains unresolved.',mode='unresolved')
e('artisan_unresolved',unresolved,artisan,'unresolved_outcome','14a:10')
a.save_window(refs,'resume_moed_katan_grooming038.json','Readthrough15a:25 before annotating13b:15–14a:10. Retain complete exception lists and cross-page washing continuation, distinct named transmission versus anonymous application, first lost-property version with recognition objection and belt reply, and Rav Ashi’s artisan version left תיקו.','365745a34ed08488f09656c6052fb5fea7a82fce641a84a5a5e4a1528c90fb33')
