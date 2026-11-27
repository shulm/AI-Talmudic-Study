"""Source reading11a:4–13: unskilled repairs and competing reconciliations."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r027');c=a.claim;e=a.e
refs=['11a:'+str(i) for i in range(4,14)]
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Source-present replies only; no exhaustive alternative inventory or certification.');return v
a.structure('mishna',refs[:3],'Mishnah of parapets, repairs and pickling')
a.structure('explanations',refs[3:],'Definitions, corrected wording, hammering prohibition and alternative resolutions')
parapet=c('parapet','11a:4','עושין מעקה לגג ולמרפסת מעשה הדיוט אבל לא מעשה אומן','The Mishnah permits a parapet for a roof or balcony as unskilled but not skilled work.',conditions=['unskilled work'],composition='composite')
cracks=c('cracks','11a:4','שפין את הסדקין ומעגילין אותן במעגילה ביד וברגל אבל לא במחלצים','The Mishnah describes treating cracks with a roller, hand and foot, excluding מחלצים; the apparent wording is clarified below.',composition='composite',scope='Printed Mishnah wording before the explicit reformulation')
repairs=c('repairs','11a:5','הציר והצינור והקורה והמנעול והמפתח שנשברו מתקנן במועד','The Mishnah permits repair of the listed broken hinge, צינור, beam, lock and key during the festival.',conditions=['broken items'],composition='composite',uncertainty=['צינור is retained without imposing a particular reconstruction of the door fitting.'])
planned=c('planned','11a:5','ובלבד שלא יתכוין לעשות מלאכתו במועד','The permission requires not intentionally scheduling the work for the festival.',conditions=['not deliberately scheduled for the festival'])
e('planned_limits',planned,repairs,'qualification','11a:5')
pickle=c('pickle','11a:6','וכל כבשין שהוא יכול לאכול מהן במועד כובשן','Pickling is permitted when the pickled items can be eaten during the festival.',conditions=['can be eaten during the festival'],scope='Mishnah; following fish discussion treated in next window')
what=q('what','11a:7','היכי דמי מעשה הדיוט','What counts as unskilled work?')
branches=c('branches','11a:7','רב יוסף אמר בהוצא ודפנא','Rav Yosef describes a construction using הוצא ודפנא.',candidates=['רב יוסף'],uncertainty=['Materials retained literally rather than silently choosing a botanical/craft gloss.'])
stones=c('stones','11a:7','במתניתא תנא צר בצרור ואינו טח בטיט','A baraita describes arranging stones without coating them with mortar.',composition='composite')
e('branches_answer',branches,what,'answer','11a:7');e('stones_answer',stones,what,'answer','11a:7')
rollerq=q('roller_q','11a:8','השתא במעגילה אמרת שרי ביד וברגל מיבעיא','If a roller is allowed, need hand and foot be stated?')
reword=c('reword','11a:8','הכי קאמר שפין את הסדקין ומעגילין אותן כעין מעגילה ביד וברגל אבל לא במחלצים','The reformulation allows smoothing like a roller with hand and foot, but not מחלצים.',composition='composite',scope='Explicit interpretive reformulation; original wording retained')
e('reword_answer',reword,rollerq,'answer','11a:8');e('reword_corrects',reword,cracks,'correction','11a:8')
hammer=c('hammer','11a:9',"עד ימיו היה פטיש מכה בירושלים כו'",'The cited source says that until his days a hammer struck in Jerusalem.',scope='Abbreviated quotation; the figure referred to by his days is not named in this excerpt',uncertainty=['Do not fill the quotation’s כו\' or infer a named person from this excerpt alone.'])
then=c('then','11a:9','עד ימיו אין מכאן ואילך לא','The discussion infers permission only until that time, and prohibition afterward.',scope='Anonymous inference used as contradiction')
e('hammer_objection',then,repairs,'objection','11a:9');e('hammer_support',hammer,then,'support','11a:9')
smith=c('smith','11a:10','לא קשיא כאן בדנפחי כאן בדנגרי','The initial answer distinguishes smiths from carpenters.',composition='composite',mode='challenged',scope='Initial anonymous reconciliation challenged next')
loudq=q('loud_q','11a:11','מתקיף לה רב חסדא יאמרו קלא רבה אסיר קלא זוטר שרי','Rav Hisda objects that people would say a loud sound is prohibited but a quiet sound permitted.',candidates=['רב חסדא'])
e('loud_objection',loudq,smith,'objection','11a:11')
tools=c('tools','11a:11','אלא אמר רב חסדא לא קשיא הא במגלי הא בחציני','Rav Hisda instead distinguishes מגלי from חציני.',candidates=['רב חסדא'],composition='composite',uncertainty=['Technical tool names and compact הא/הא mapping retained without imposing an unsupported detailed reconstruction.'])
e('tools_corrects',tools,smith,'correction','11a:11');e('tools_answer',tools,loudq,'answer','11a:11')
time=c('time','11a:11','רב פפא אמר כאן קודם גזירה כאן לאחר גזירה','Rav Pappa distinguishes before the decree from after it.',candidates=['רב פפא'],composition='composite',scope='Alternative historical reconciliation')
opinions=c('opinions','11a:12',"רב אשי אמר הא ר' יהודה הא ר' יוסי",'Rav Ashi distinguishes Rabbi Yehuda’s and Rabbi Yose’s opinions.',candidates=['רב אשי'],composition='composite',scope='Alternative attribution-based reconciliation with supporting transmission below')
change=c('change','11a:12',"דאמר ר' יצחק בר אבדימי מאן תנא שינוי במועד בדבר האבד דלא כר' יוסי",'Rabbi Yitzhak bar Avdimi says that requiring an altered method for festival work involving loss is not Rabbi Yose’s position.',candidates=['רבי יצחק בר אבדימי'],role='quoted_authority',chain=['רב אשי','רבי יצחק בר אבדימי'],conditions=['work involving loss'],scope='Quoted support for Rav Ashi’s attribution distinction')
whoq=q('who','11a:12','מאן תנא שינוי במועד בדבר האבד','Whose view requires an altered method for festival work involving loss?',candidates=['רבי יצחק בר אבדימי'])
e('change_answer',change,whoq,'answer','11a:12');e('change_support',change,opinions,'support','11a:12')
practiceq=q('practice','11a:13','אמר רבינא כמאן מדלינן האידנא קביותא דדשא בחולא דמועדא','Ravina asks whose opinion supports the present practice of lifting the door fitting during the festival.',candidates=['רבינא'])
yose=c('yose','11a:13',"כמאן כר' יוסי",'The practice is identified with Rabbi Yose.',candidates=['רבינא'],scope='Ravina’s report about contemporary practice in the source, not later practical adjudication')
e('yose_answer',yose,practiceq,'answer','11a:13')
contradiction=q('contradiction','11a:9','ורמינהי','How is the repair permission reconciled with the cited hammer prohibition?')
for key,answer,ref in [('smith',smith,'11a:10'),('tools',tools,'11a:11'),('time',time,'11a:11'),('opinions',opinions,'11a:12')]:e(key+'_reconciliation',answer,contradiction,'answer',ref)
a.save_window(refs,'resume_moed_katan_repairs027b.json','Read complete11a and11b continuation. Preserve full Mishnah list/condition, literal abbreviated quotation, rejected initial reconciliation and distinct Hisda/Pappa/Ashi alternatives, Yitzhak transmission and Ravina practice; no unsupported name or technical gloss.','100fd875fc82430d801f2800899a60070090305935f1b74f30a6efe29b9b9f66')
