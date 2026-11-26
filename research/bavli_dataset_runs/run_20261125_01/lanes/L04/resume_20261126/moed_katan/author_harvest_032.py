"""Direct source reading12b:2–11: harvest, loss, altered methods and distinct Rav narrative."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r032');c=a.claim;e=a.e
refs=['12b:'+str(i) for i in range(2,12)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Local source-present replies, not exhaustive choices or qualification.');return v
a.structure('huna',refs[:5],'Rav Huna’s harvest, restrictive baraita and altered-method objection')
a.structure('needs',refs[5:8],'Festival needs, leftovers and conflicting evasion rules')
a.structure('rav',refs[8:],'Rav’s harvest and Shmuel’s reaction with alternative explanations')
huna=c('huna','12b:2','רב הונא חצדו ליה חצדא במועדא','A harvest was cut for Rav Huna during the festival.',scope='Narrative action')
challenge=q('challenge','12b:2','איתיביה רבה בר רב הונא לרב הונא','Rabbah son of Rav Huna challenges Rav Huna with the following baraita.',candidates=['רבה בר רב הונא'])
for key,quote,text,conditions in [('flour_yes','טוחנין קמח במועד לצורך המועד','Flour may be ground for festival needs.',['festival need']),('flour_no','ושלא לצורך המועד אסור','Grinding not for festival needs is prohibited.',['not for festival need']),('loss_yes','דבר שאבוד במועד מותר לעשותו במועד','Work preventing loss during the festival is permitted.',['loss during festival']),('loss_no','דבר שאינו אבוד במועד אסור','Work without such loss is prohibited.',['no loss during festival'])]:
 c(key,'12b:2',quote,text,conditions=conditions,scope='Baraita quoted by Rabbah son of Rav Huna')
detached=c('detached','12b:3','במה דברים אמורים בתלושין מן הקרקע','This allowance is limited to produce detached from the ground.',conditions=['detached produce'],scope='Restriction in the quoted baraita')
attached=c('attached','12b:3',"אבל מחובר לקרקע אפי' כולו אבוד אסור",'For produce attached to the ground, even total loss does not permit the work under this baraita.',conditions=['attached produce','even total loss'])
food=c('food','12b:3','ואם אין לו מה יאכל קוצר ומעמר ודש וזורה ובורר וטוחן','If he has nothing to eat, he may harvest, bind, thresh, winnow, select and grind.',conditions=['nothing to eat'],composition='composite')
ox=c('ox','12b:3','ובלבד שלא ידוש בפרות','This permission excludes threshing with cattle.',conditions=['nothing to eat exception'])
e('detached_limits',detached,'mk.r032.loss_yes.c','qualification','12b:3');e('food_exception',food,attached,'qualification','12b:3');e('ox_limits',ox,food,'qualification','12b:3');e('attached_objection',attached,huna,'objection','12b:3')
individual=c('individual','12b:4','אמר ליה יחידאה היא ולא סבירא לן כוותיה','Rav Huna answers that it is an individual opinion which they do not follow.',candidates=['רב הונא'],scope='His reply to the quoted attached-produce restriction')
yose=c('yose','12b:4',"כלל אמר רבן שמעון בן גמליאל משום ר' יוסי דבר התלוש מן הקרקע אפילו מקצתו אבוד מותר והמחובר לקרקע אפי' כולו אבוד אסור",'Rabban Shimon ben Gamliel transmits Rabbi Yose: detached produce is permitted even for partial loss, while attached produce is prohibited even for total loss.',candidates=['רבי יוסי'],role='quoted_authority',chain=['רבן שמעון בן גמליאל','רבי יוסי'],composition='composite',scope='Cited identification of the individual restrictive opinion; not a final universal rule')
e('individual_answer',individual,challenge,'answer','12b:4');e('yose_support',yose,individual,'support','12b:4')
oxq=q('oxq','12b:5',"ואי ר' יוסי ידוש נמי בפרות",'If this is Rabbi Yose’s view, why not thresh with cattle too?')
change=c('change','12b:5',"הא אמר רב יצחק בר אבא מאן תנא שינוי במועד בדבר האבד דלא כר' יוסי",'Rav Yitzhak bar Abba’s statement excludes Rabbi Yose from requiring an altered method for loss-related festival work.',candidates=['רב יצחק בר אבא'],role='quoted_authority',scope='Previously stated principle quoted as a new objection')
normal=c('normal','12b:6','כיון דכל יומא לאו בפרות דיישי האידנא נמי לאו שינוי הוא','The response says that since they normally do not thresh with cattle, avoiding cattle now is not an altered method.',conditions=['ordinary threshing is not with cattle'])
e('change_objection',change,ox,'objection','12b:5');e('normal_answer',normal,oxq,'answer','12b:6')
for key,ref,quote,text,condition in [
('grind','12b:7','טוחנין במועד לצורך המועד','Grinding is allowed for festival needs.','festival need'),
('grind_no','12b:7','ושלא לצורך המועד אסור ואם טחן','Grinding without festival need is prohibited.','not for festival need'),
('grind_left','12b:7','ואם טחן והותיר הרי זה מותר','If he ground and some remains, the remainder is allowed.','genuine festival preparation with leftover'),
('wood','12b:7','קוצצין עצים במועד לצורך המועד','Wood may be cut for festival needs.','festival need'),
('wood_no','12b:7','ושלא לצורך המועד אסור ואם קצץ','Wood cutting without festival need is prohibited.','not for festival need'),
('wood_left','12b:7','ואם קצץ והותיר הרי זה מותר','If he cut and some remains, it is allowed.','genuine festival preparation with leftover'),
('beer','12b:8','מטילין שכר במועד לצורך המועד','Beer may be made for festival needs.','festival need'),
('beer_no','12b:8','ושלא לצורך המועד אסור','Beer making without festival need is prohibited.','not for festival need'),
('beer_left','12b:8','ואם הטיל והותיר הרי זה מותר','If he made beer and some remains, it is permitted.','genuine festival preparation with leftover')]:
 c(key,ref,quote,text,conditions=[condition],scope='Anonymous baraita; quote may include opening of next clause to uniquely locate repeated wording')
evasion=c('evasion','12b:8','ובלבד שלא יערים','The permission requires no contrived evasion.')
e('evasion_limits',evasion,'mk.r032.beer_left.c','qualification','12b:8')
contradict=q('contradict','12b:9','ורמינהו','How is this reconciled with the following contrary baraita?')
need2=c('need2','12b:9','מטילין שכר במועד לצורך המועד ושלא לצורך המועד אסור אחד שכר תמרים ואחד שכר שעורים','The second baraita likewise permits festival-need beer and prohibits other beer, whether dates or barley.',composition='composite')
new=c('new','12b:9','ואע"פ שיש לו ישן מערים ושותה מן החדש','It allows making a contrivance to drink new beer even when old beer is available.',conditions=['old beer already available'],scope='Contrary baraita, not silently combined with the no-evasion rule')
tannaim=c('tannaim','12b:9','תנאי היא','The answer identifies a tannaitic disagreement.')
forbid=c('forbid','12b:9','דתניא אין מערימין בכך','One baraita opinion disallows this evasion.')
ybr=c('ybr','12b:9',"ר' יוסי בר יהודה אומר מערימין",'Rabbi Yose bar Yehuda permits evasion.',candidates=['רבי יוסי בר יהודה'])
e('new_objection',new,evasion,'objection','12b:9');e('tannaim_answer',tannaim,contradict,'answer','12b:9');e('forbid_support',forbid,tannaim,'support','12b:9');e('ybr_support',ybr,tannaim,'support','12b:9')
rav=c('rav','12b:10','רב חצדו ליה חצדא בחולא דמועדא','A harvest was cut for Rav during the festival.',scope='Separate narrative; do not conflate Rav with earlier Rav Huna')
shmuel=c('shmuel','12b:10','שמע שמואל איקפד','Shmuel heard and was displeased.',scope='Reaction in the narrative, not yet an identified legal disagreement')
individualq=q('individualq','12b:10','לימא שמואל כיחידאה סבירא ליה','Does Shmuel follow the individual restrictive opinion?')
wheat=c('wheat','12b:10','לא חצדא דחיטי הוה דלא הוה פסיד','No: it was wheat whose harvest was not at risk of loss.',mode='asserted',conditions=['wheat without threatened loss'],scope='Rejects inference of Shmuel’s adherence to the individual attached-produce rule')
e('wheat_answer',wheat,individualq,'answer','12b:10')
ravq=q('ravq','12b:11','ורב מאי טעמא עביד הכי','Why did Rav act this way?')
nofood=c('nofood','12b:11','אין לו מה יאכל הוה','He had nothing to eat.',conditions=['nothing to eat'],scope='Explanation of Rav’s action')
notold=c('notold','12b:11','ושמואל לא סיימוה קמיה','The full circumstances were not reported to Shmuel.',scope='Explains why his reaction need not constitute disagreement with Rav’s actual case')
important=c('important','12b:11','אי נמי אדם חשוב שאני','Alternatively, an important person is different.',conditions=['important person'],scope='Alternative explanation for Shmuel’s objection, retained alongside incomplete-report account')
e('nofood_answer',nofood,ravq,'answer','12b:11');e('notold_explains',notold,shmuel,'qualification','12b:11');e('important_explains',important,shmuel,'qualification','12b:11')
a.save_window(refs,'resume_moed_katan_harvest032.json','Read12b with earlier named principle and later narratives. Preserve Rav Huna vs Rav distinction, minority attribution and rejected inference, ordinary-method condition, every commodity/leftover/need rule, tannaitic evasion alternatives, and two explanations preventing fabricated Rav–Shmuel dispute.','0e2c7b4397004e2c14bc446214a58bfc7e20009058d9be747ee34147fe640a63')
