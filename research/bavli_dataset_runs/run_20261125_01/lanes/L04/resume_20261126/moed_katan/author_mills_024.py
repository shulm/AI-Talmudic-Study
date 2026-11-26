"""Direct source reading10a:11–10b:4, festival equipment and animal care."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r024');c=a.claim;e=a.e
refs=['10a:'+str(i) for i in range(11,17)]+['10b:'+str(i) for i in range(1,5)]
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Source-supported local replies only; no exhaustive alternative inventory.');return v
a.structure('mills',refs[:7],'Equipment permissions, mill-dressing definitions and opinions')
a.structure('animals',refs[7:],'Contrasting mill-animal permission, animal treatment and skilled work')
setup=c('setup','10a:11','מעמידין תנור וכירים וריחים במועד','The Mishnah permits setting up an oven, stove and mill during the festival.',composition='composite')
new=c('new','10a:11',"ר' יהודה אומר אין מכבשין את הריחים בתחילה",'Rabbi Yehuda excludes initial מכבשין of mills.',candidates=['רבי יהודה'],conditions=['initial treatment of the mills'],scope='Mishnah prohibition; the technical verb is analyzed immediately afterward')
what=q('what','10a:12','מאי מכבשין','What does מכבשין mean?')
dress=c('dress','10a:12','רב יהודה אמר מנקר ריחיא','Rav Yehuda explains it as dressing the millstone.',candidates=['רב יהודה'])
eye=c('eye','10a:12','רב יחיאל אמר בת עינא','Rav Yehiel explains it in terms of the mill’s eye/opening.',candidates=['רב יחיאל'])
e('dress_answer',dress,what,'answer','10a:12');e('eye_answer',eye,what,'answer','10a:12')
eliezer=c('eliezer','10a:13','מעמידין תנור וכירים במועד ובלבד שלא יגמור מלאכתן דברי רבי אליעזר','Rabbi Eliezer permits setting up oven and stove provided their work is not completed.',candidates=['רבי אליעזר'],conditions=['do not complete the work'],composition='composite')
sages=c('sages','10a:13','וחכמים אומרים אף יגמור','The sages permit completing it too.',candidates=['חכמים'])
old=c('old','10a:13','רבי יהודה אומר משמו מעמידין את החדשה ומכבשין את הישנה','Rabbi Yehuda reports in his name that the new item may be set up and the old one subjected to מכבשין.',candidates=['רבי אליעזר'],role='quoted_authority',chain=['רבי יהודה','רבי אליעזר'],composition='composite',uncertainty=['משמו is contextually read as the earlier Rabbi Eliezer; the source does not repeat his name here.'])
none=c('none','10a:13','ויש אומרים אין מכבשין כל עיקר','The other opinion excludes מכבשין entirely.',candidates=['יש אומרים'])
fits=c('fits','10a:14','בשלמא למאן דאמר מכבשין מנקר ריחיא היינו דמשכחת לה בישנה','Dressing the millstone is intelligible for an old mill.',scope='Compatibility observation for Rav Yehuda’s interpretation')
oldq=q('old_q','10a:14','אלא למאן דאמר בת עינא ישנה בת עינא למה לה','Why would an old mill need an eye/opening under the other explanation?')
widen=c('widen','10a:14','כגון דקא בעי לארווחי טפי פורתא','The reply posits that its opening needs slight widening.',conditions=['slight widening of an existing opening'])
e('old_question',oldq,eye,'objection','10a:14');e('widen_answer',widen,oldq,'answer','10a:14')
heard=c('heard','10a:15','רב הונא שמעיה לההוא גברא דקא מנקר ריחיא בחולא דמועדא','Rav Huna heard a man dressing a millstone during the festival.',scope='Narrative report')
rebuke=c('rebuke','10a:15','אמר מאן האי איתחיל גופיה דקא מחיל חולא דמועדא','Rav Huna denounced the person desecrating the festival, invoking harm upon his body.',candidates=['רב הונא'],scope='Reported rebuke, not endorsement or a separate forecast')
view=c('view','10a:15','סבר לה כיש אומרים','The anonymous explanation says Rav Huna followed the other restrictive opinion.',scope='Anonymous attribution of the narrative actor’s rationale')
e('view_explains',view,rebuke,'support','10a:15');e('view_quote',view,none,'quotation','10a:15')
hama=c('hama','10a:16','דרש רב חמא נוקרין ריחים במועד','Rav Hama taught that millstones may be dressed during the festival.',candidates=['רב חמא'])
riding=c('riding','10a:16','משום רבי מאיר אמר אפילו סוס שרוכב עליו וחמור שרוכב עליו (ומותר) ליטול צפרנים בחולו של מועד','In Rabbi Meir’s name, Rav Hama permits clipping the hooves of a horse or donkey ridden by the person during the festival.',candidates=['רבי מאיר'],role='quoted_authority',chain=['רב חמא','רבי מאיר'],conditions=['animal used for riding'],composition='composite',uncertainty=['The parenthetical (ומותר) is retained in evidence, without selecting another textual version.'])
millnot=c('millnot','10b:1','אבל חמרא דריחיא לא','The mill donkey is excluded from that permission.',conditions=['mill donkey'],scope='Cross-page limitation on the preceding hoof-trimming permission')
e('millnot_limits',millnot,riding,'qualification','10b:1')
for key,quote,text in [('hoof','רב יהודה שרי למישקל טופריה לחמרא דריחיא','Rav Yehuda permitted trimming the mill donkey’s hooves.'),('set','ולאוקומי ריחיא','Rav Yehuda permitted setting up a mill.'),('build','ולמיבני ריחיא','Rav Yehuda permitted building a mill.'),('channel','ולמיבני אמת ריחיא','Rav Yehuda permitted constructing the mill water channel.'),('stable','ולמיבני אוריא','Rav Yehuda permitted building a stable.')]:
    c(key,'10b:2',quote,text,candidates=['רב יהודה'],scope='Reported festival permission')
for key,quote,text in [('comb','(רבא) שרא לסרוקי סוסיא','The parenthetically printed Rava permitted combing a horse.'),('manger','ולמיבני אקרפיטא','He permitted constructing an אקרפיטא.'),('platform','ולמיבני איצטבא','He permitted constructing a platform.')]:
    c(key,'10b:2',quote,text,candidates=['רבא (parenthetical)'],scope='Reported permission with parenthetical name retained',uncertainty=['Printed parenthetical attribution is preserved without textual emendation.']+(['אקרפיטא technical object not expanded beyond the source.'] if key=='manger' else []))
blood=c('blood','10b:3','רבא שרא למישקל דמא לבהמה בחולא דמועדא','Rava permitted bloodletting for an animal during the festival.',candidates=['רבא'])
support=c('support','10b:3','א"ל אביי תניא דמסייע לך מקיזין דם לבהמה','Abaye cites a baraita supporting animal bloodletting.',candidates=['אביי'])
medicine=c('medicine','10b:3','ואין מונעין רפואה לבהמה בחולו של מועד','The cited baraita says medical treatment is not withheld from an animal during the festival.',scope='Baraita cited by Abaye')
e('abaye_support',support,blood,'support','10b:3');e('medicine_support',medicine,blood,'support','10b:3')
cloth=c('cloth','10b:4','רבא שרא לכסכוסי קירמי','Rava permitted rubbing the garments.',candidates=['רבא'],uncertainty=['כסכוסי קירמי is paraphrased conservatively; no reconstruction of the textile operation.'])
why=q('why','10b:4','מ"ט מעשה הדיוט הוא','Why? Because it is unskilled work.')
unskilled=c('unskilled','10b:4','מעשה הדיוט הוא','The operation is classed as unskilled work.')
knot=c('knot','10b:4','אמר רב יצחק בר אמי אמר רב חסדא קיטורי בירי אסיר','Rav Yitzhak bar Ami transmits Rav Hisda’s prohibition of קיטורי בירי.',candidates=['רב חסדא'],role='quoted_authority',chain=['רב יצחק בר אמי','רב חסדא'],uncertainty=['The technical operation קיטורי בירי is retained without an unsupported precise gloss.'])
why2=q('why2','10b:4','מ"ט מעשה אומן הוא','Why? Because it is skilled work.')
skilled=c('skilled','10b:4','מעשה אומן הוא','That operation is classed as skilled work.')
e('unskilled_answer',unskilled,why,'answer','10b:4');e('unskilled_reason',unskilled,cloth,'support','10b:4');e('skilled_answer',skilled,why2,'answer','10b:4');e('skilled_reason',skilled,knot,'support','10b:4')
a.save_window(refs,'resume_moed_katan_mills024.json','Read10a:11–10b:4 with allfollowing10b distinctions as context. Preserve technical ambiguity, named transmissions, minority opinions, cross-page exclusion, contrary Rav Yehuda permission, reported rebuke and narrative, parenthetical Rava, and work-skill rationales.','4c3543bb55fe94163a73b98c695ee3706a08047326bc6c8790797ce4a95d9ff3')
