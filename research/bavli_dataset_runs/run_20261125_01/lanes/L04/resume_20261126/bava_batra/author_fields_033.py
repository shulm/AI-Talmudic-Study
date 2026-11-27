"""Field-size standards and geographical reconciliation, read from original."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r033');c=a.claim;q=a.question;e=a.e
parent='34188a006e4a6fb878e7477108a12a5994b3521d9782fb01a13308a9f595c240'
a.structure('fields',['12a:'+str(i) for i in range(7,13)],'Regional minimum field sizes and a day’s work')
regional=c('regional','12a:7','ולא פליגי מר כי אתריה ומר כי אתריה','The anonymous explanation says the Mishnah’s field thresholds do not conflict: each reflects its own locality.',scope='Explicit no-dispute reconciliation of nine-kav and nine-half-kav thresholds')
e('field_region',regional,'bb.r031.field.c','qualification','12a:7');e('yehuda_region',regional,'bb.r031.yehuda.c','qualification','12a:7')
babelq=q('babel_q','12a:8','בבבל מאי','What is the field threshold in Babylonia?')
day=c('day','12a:8','אמר רב יוסף בי רדו יומא','Rav Yosef sets it at a day’s plowing area.',candidates=['רב יוסף'],conditions=['Babylonian field partition'],scope='Source work-capacity measure, not converted into modern area units')
meaningq=q('meaning_q','12a:9','מאי בי רדו יומא','What does the day’s plowing measure mean?')
sow=c('sow_problem','12a:9','אי יומא זרעא תרי יומא כרבא לא הוי','If it is a day’s sowing area, it does not provide two days of plowing.',mode='hypothetical',scope='Worktime mismatch in the objection')
plow=c('plow_problem','12a:9','אי יומא כרבא יומא דזרעא לא הוי','If it is a day’s plowing area, it does not provide a day’s sowing.',mode='hypothetical',scope='Second worktime mismatch')
repeat=c('repeat','12a:10','אי בעית אימא יומא דכרבא דכריב ותני','One answer uses a day’s plowing in a practice involving plowing and repeating.',conditions=['plowing and repeating'],scope='First anonymous alternative explanation')
rock=c('rock','12a:10','ואי בעית אימא יומא דזרעא בהדורי','The other answer uses a day’s sowing in בהדורי.',conditions=['בהדורי terrain/work setting'],scope='Second anonymous alternative; printed term not silently expanded into an uncertain precise agronomy')
water=c('water','12a:11','דוולא אמר רב נחמן בי דאלו יומא','For the water-drawing setting, Rav Nahman sets an area served by a day’s drawing.',candidates=['רב נחמן'],conditions=['דוולא setting'],scope='Work-capacity threshold')
orchard=c('orchard','12a:11','פרדסא אמר אבוה דשמואל בת שלשת קבין','For a vineyard/orchard, Shmuel’s father sets three kav.',candidates=['אבוה דשמואל'],conditions=['פרדסא'],scope='Not attributed to Shmuel himself')
sum=c('sum','12a:12','האומר לחבירו מנת בכרם אני מוכר לך סומכוס אומר לא יפחות מג\' קבין','Sumakhos says a sale of a portion in a vineyard must be no less than three kav.',candidates=['סומכוס'],conditions=['seller says he sells a portion in a vineyard'],scope='Cited corroborating baraita; sale context distinct from partition context')
yose=c('yose','12a:12','א"ר יוסי אין אלו אלא דברי נביאות','Rabbi Yose calls these words prophecy.',candidates=['רבי יוסי'],scope='Printed evaluative response; next discussion develops prophecy, without forcing endorsement or rejection beyond wording')
babelorchq=q('babelorch_q','12a:12','בבבל מאי','What is the vineyard threshold in Babylonia?')
rows=c('rows','12a:12','אמר רבא בר קסנא תלת אציאתה בני תריסר גופני','Rava bar Kisna gives three rows of twelve vines each.',candidates=['רבא בר קסנא'],conditions=['Babylonian vineyard'],scope='Specific named authority, not Rava without patronymic')
hoe=c('hoe','12a:12','כי היכי דרפיק גברא ביומא','The rationale is the amount a man can hoe in a day.',scope='Work-capacity explanation of the vine measure')
e('day_answer',day,babelq,'answer','12a:8');e('sow_objection',sow,day,'objection','12a:9');e('plow_objection',plow,day,'objection','12a:9');e('repeat_answer',repeat,meaningq,'answer','12a:10');e('rock_answer',rock,meaningq,'answer','12a:10');e('sum_support',sum,orchard,'support','12a:12');e('yose_response',yose,sum,'qualification','12a:12');e('rows_answer',rows,babelorchq,'answer','12a:12');e('hoe_support',hoe,rows,'support','12a:12')
for row in a.rows:
 if row['layer']=='questions':row['content']['answer_set_status']='partial';row['uncertainty'].append('Actually represented source alternatives or reply; not a qualified exhaustive answer set.')
a.save_window(['12a:'+str(i) for i in range(7,13)],'fields033.json','Read through12b:14, reread12a:7–12 and prior Mishnah. Explicit no-dispute regional resolution attached to both earlier threshold claims, worktime alternatives unassigned to names, Rav Yosef and Shmuel’s father distinguished. No unsupported area conversion or modern agronomic reconstruction.',parent)
