"""Direct reading14a:16–14b:7: Shmuel’s two reports and qualified negative inference."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r040');c=a.claim;e=a.e
refs=['14a:16','14a:17']+['14b:'+str(i) for i in range(1,8)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Local represented reply only, not exhaustive alternatives.');return v
a.structure('first',refs[:5],'Birth during festival: restrictive inference and Rav Ashi’s response')
a.structure('second',refs[5:],'Alternative Shmuel transmission, support inference and repeated response')
first=c('first','14a:16','אמר שמואל קטן הנולד במועד מותר לגלח במועד','Shmuel permits cutting the hair of a child born during the festival.',candidates=['שמואל'],conditions=['child born during festival'],scope='First transmission')
prison=c('prison','14a:16','שאין לך בית האסורין גדול מזה','The reason compares birth to release from the greatest confinement.',scope='Reason in Shmuel’s statement, not literal penal confinement')
infer=c('infer','14a:16','במועד אין מעיקרא לא','The discussion infers permission for birth during the festival but not beforehand.',mode='challenged',composition='composite',scope='Anonymous restrictive inference in first version')
e('prison_reason',prison,first,'support','14a:16');e('infer_qualifies',infer,first,'qualification','14a:16')
proof=c('proof','14a:17',"מתיב ר' פנחס כל אלו שאמרו מותר לגלח במועד מותר לגלח בימי אבלו",'Rabbi Pinhas objects from the rule permitting haircutting during mourning for those permitted during the festival.',candidates=['רבי פנחס'],role='quoted_authority',conditions=['permitted festival haircut category'])
negative=c('negative','14a:17','הא אסור לגלח במועד אסור לגלח בימי אבלו','The objection infers that those prohibited during the festival are prohibited during mourning.',mode='challenged',scope='Negative inference challenged by Rav Ashi below')
child=c('child','14b:1','ואי אמרת קטן אית ביה פלוגתא נמצאת אבילות נוהגת בקטן','If children differ by birth timing, the inference would make mourning restrictions apply to a child.',mode='hypothetical',scope='Consequence used against restrictive inference')
tear=c('tear','14b:2','והתניא מקרעין לקטן מפני עגמת נפש','A baraita says garments are torn for a child for the sake of grief.',scope='Contrasting baraita; does not assert that the child bears full mourning obligations')
question=q('question','14b:3','אמר רב אשי מי קתני הא אסורין','Rav Ashi asks whether the source actually states the negative inference.',candidates=['רב אשי'])
mixed=c('mixed','14b:3','דלמא יש מהן אסור ויש מהן מותר','Perhaps some excluded cases are prohibited during mourning and others permitted.',mode='hypothetical',composition='composite',scope='Rav Ashi’s rebuttal to the blanket inverse, not a complete list of cases')
e('tear_objection',tear,child,'objection','14b:2');e('question_objection',question,negative,'objection','14b:3');e('mixed_answer',mixed,question,'answer','14b:3')
report=c('report','14b:4','אמימר ואי תימא רב שישא בריה דרב אידי מתני הכי','Amemar, alternatively Rav Shisha son of Rav Idi, transmits another version.',composition='composite',scope='Explicit alternative transmitter attribution; do not collapse the alternatives')
second=c('second','14b:4','אמר שמואל קטן מותר לגלחו במועד לא שנא נולד במועד ולא שנא נולד מעיקרא','Shmuel permits a child’s haircut during the festival whether born during it or beforehand.',candidates=['שמואל'],role='quoted_authority',chain=['אמימר / alternatively רב שישא בריה דרב אידי','שמואל'],composition='composite',scope='Second transmission, not a personal retraction inferred from the first',uncertainty=['The alternative transmitter chain is retained as one explicitly uncertain chain entry.'])
proof2=c('proof2','14b:5','אמר רב פנחס אף אנן נמי תנינא כל אלו שאמרו מותר לגלח במועד מותר לגלח בימי אבלו','Rav Pinhas presents the same category rule as support for this version.',candidates=['רב פנחס'],role='quoted_authority',scope='Second occurrence with different argumentative direction; printed Rav rather than earlier Rabbi retained')
negative2=c('negative2','14b:5','הא אסורין לגלח במועד אסורין לגלח בימי אבלו','Again the argument infers that festival-prohibited categories are mourning-prohibited.',mode='challenged',scope='Repeated negative inference, again challenged')
child2=c('child2','14b:6','אי אמרת קטן אסור נמצאת אבילות נוהגת בקטן','If a child were prohibited, the inference would imply mourning applies to a child.',mode='hypothetical')
tear2=c('tear2','14b:6','ותניא מקרעין לקטן מפני עגמת נפש','The grief explanation of tearing a child’s garment is cited again.',scope='Repeated source occurrence')
question2=q('question2','14b:7','אמר רב אשי מי קתני הא אסורין','Rav Ashi again challenges whether the negative inference is actually stated.',candidates=['רב אשי'])
mixed2=c('mixed2','14b:7','דלמא יש מהן אסור ויש מהן מותר','Perhaps some cases are prohibited and others permitted.',mode='hypothetical',composition='composite',scope='Second rebuttal of the blanket inverse, preserving repeated occurrence')
e('tear2_objection',tear2,child2,'objection','14b:6');e('question2_objection',question2,negative2,'objection','14b:7');e('mixed2_answer',mixed2,question2,'answer','14b:7');e('proof2_support',proof2,second,'support','14b:5')
a.save_window(refs,'resume_moed_katan_children040.json','Read14a–15a continuation. Retain two Shmuel transmissions and explicit alternative transmitters, birth timing, prison analogy, opposed use of repeated mourning-category proof, both negative inferences and both Rav Ashi objections. No manufactured retraction or child mourning obligation.','bc5a4d0ae1362a651a294bcede56dcd124b2b4bc3557e8d0b05eb7a80840b206')
