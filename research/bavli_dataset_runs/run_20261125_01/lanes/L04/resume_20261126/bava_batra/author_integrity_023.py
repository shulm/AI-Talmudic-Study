"""Source reading: collector integrity, fund conditions and local agreements."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r023');c=a.claim;q=a.question;e=a.e
original_span=a.span
def selected_span(ref,quote):
    if (ref,quote)==('9a:1','ואתני עלה'):
        # First occurrence continues Shmuel; second is the unnamed master's action.
        text=a.refs[ref]['text'];assert text.startswith(quote)
        return dict(segment_id=a.refs[ref]['id'],start_char=0,end_char=len(quote),quote=quote)
    return original_span(ref,quote)
a.span=selected_span
parent='b3b44f79fc0b55a905537e63af70ac098ae9ae4192a68022eef1cadf6ed3912a'
a.structure('conduct',['8b:16','8b:17'],'Collector conduct with private money and unneeded charity assets')
a.structure('fund',['8b:18','9a:1'],'Abaye’s reports about מר and conditional pooled funds; Rav Ashi’s discretion')
a.structure('agreement',['9a:2','9a:3'],'Butchers’ workday agreement and sanction under an important authority')
a.structure('accounts',['9a:4','9a:5'],'Trust in public collectors and counting with a trusted household treasurer')
stay=c('stay','8b:16','גבאי צדקה אינן רשאין לפרוש זה מזה','Charity collectors may not separate from one another.')
split=c('split','8b:16','אבל פורש זה לשער וזה לחנות','One may go to a gate while another goes to a shop.',scope='Local exception to the nonseparation rule')
find=c('found','8b:16','מצא מעות בשוק לא יתנם בתוך כיסו','A collector finding money in the market must not put it in his own pocket.',conditions=['private money found in market'])
findbag=c('found_bag','8b:16','מצא מעות בשוק לא יתנם בתוך כיסו אלא נותנן לתוך ארנקי של צדקה ולכשיבא לביתו יטלם','He puts it in the charity purse and takes it out on arriving home.',conditions=['money privately found in market'],composition='composite')
debt=c('debt','8b:16','היה נושה בחבירו מנה ופרעו בשוק לא יתננו לתוך כיסו','A collector repaid a personal debt in the market must not put it in his own pocket.',conditions=['personal loan repaid in market'])
debtbag=c('debt_bag','8b:16','היה נושה בחבירו מנה ופרעו בשוק לא יתננו לתוך כיסו אלא נותנן לתוך ארנקי של צדקה ולכשיבא לביתו יטלם','He deposits that repayment in the charity purse and withdraws it at home.',conditions=['personal loan repaid in market'],composition='composite')
e('split_qualification',split,stay,'qualification','8b:16');e('findbag_qualification',findbag,find,'qualification','8b:16');e('debtbag_qualification',debtbag,debt,'qualification','8b:16')
exchange=c('exchange','8b:17','גבאי צדקה שאין להם עניים לחלק פורטין לאחרים','Charity-fund collectors with no poor recipients may exchange coins through others.',conditions=['no poor recipients to distribute to'])
selfexchange=c('self_exchange','8b:17','ואין פורטין לעצמן','They may not exchange the charity coins for themselves.',conditions=['same unused-fund setting'])
sell=c('sell','8b:17','גבאי תמחוי שאין להם עניים לחלק מוכרין לאחרים','Food-distribution collectors with no poor recipients sell the food to others.',conditions=['no poor recipients to distribute to'])
selfsell=c('self_sell','8b:17','ואין מוכרין לעצמן','They may not sell it to themselves.',conditions=['same unused-food setting'])
count=c('count','8b:17','מעות של צדקה אין מונין אותן שתים אלא אחת אחת','Charity money is counted one coin at a time, not two at a time.',composition='composite')
e('selfexchange_qualification',selfexchange,exchange,'qualification','8b:17');e('selfsell_qualification',selfsell,sell,'qualification','8b:17')
before=c('before','8b:18','אמר אביי מריש לא הוה יתיב מר אציפי דבי כנישתא','Abaye reports that מר initially would not sit on the synagogue mats.',candidates=['אביי'],scope='Narrated previous practice',uncertainty=['Printed מר retained without silently assigning a named teacher.'])
after=c('after','8b:18','כיון דשמעה להא דתניא ולשנותה לכל מה שירצו הוה יתיב','After hearing the teaching allowing redirection, מר sat on them.',candidates=['אביי'],scope='Reported change in practice',uncertainty=['Unnamed מר preserved.'])
two=c('two','8b:18','אמר אביי מריש הוה עביד מר תרי כיסי חד לעניי דעלמא וחד לעניי דמתא','Abaye reports that מר initially maintained separate purses for the general poor and the town’s poor.',candidates=['אביי'],composition='composite',uncertainty=['Printed מר not normalized to a named authority.'])
shmuel=c('shmuel','8b:18','דאמר ליה שמואל לרב תחליפא בר אבדימי עביד חד כיסא','Shmuel instructs Rav Tahlifa bar Avdimi to make one purse.',candidates=['שמואל'],scope='Instruction continued with a stipulation on next page')
condition=c('condition','9a:1','ואתני עלה','Shmuel’s instruction includes making a stipulation over the purse.',candidates=['שמואל'],naming_refs=['8b:18'],scope='Cross-page continuation of instruction')
one=c('one','9a:1','איהו נמי עבד חד כיסא ואתני עלה','The reported מר likewise made one purse and stipulated over it.',candidates=['אביי'],naming_refs=['8b:18'],composition='composite',uncertainty=['The report’s unnamed subject מר remains unresolved.'])
ashi=c('ashi','9a:1','רב אשי אמר אנא אתנויי נמי לא צריכנא','Rav Ashi says he does not need even a stipulation.',candidates=['רב אשי'],scope='His own collection circumstances, not an unqualified cancellation of Shmuel’s instruction')
donors=c('donors','9a:1','דכל דקא אתי אדעתא דידי אתי','Rav Ashi explains that everything received is given subject to his discretion.',candidates=['רב אשי'])
recipient=c('recipient','9a:1','ולמאן דבעינא יהיבנא ליה','He therefore gives it to whichever recipient he chooses.',candidates=['רב אשי'],conditions=['donations entrusted to his discretion'])
e('after_correction',after,before,'correction','8b:18');e('redirection_support','bb.r022.change.c',after,'support','8b:18');e('one_correction',one,two,'correction','9a:1');e('condition_qualification',condition,shmuel,'qualification','9a:1');e('donors_support',donors,ashi,'support','9a:1');e('recipient_qualification',recipient,ashi,'qualification','9a:1')
deal=c('deal','9a:2','הנהו בי תרי טבחי דעבדי עניינא בהדי הדדי דכל מאן דעביד ביומא דחבריה נקרעוה למשכיה','Two butchers agreed to tear the hide of whoever worked on the other’s assigned day.',conditions=['work on other partner’s day'],scope='Narrative agreement, not yet endorsed as enforceable')
c('breach','9a:2','אזל חד מנייהו עבד ביומא דחבריה','One worked on the other’s day.',scope='Narrative event')
c('tear','9a:2','קרעו למשכיה','They tore his hide.',scope='Narrative enforcement')
damages=c('damages','9a:2','אתו לקמיה דרבא חייבינהו רבא לשלומי','Rava required those who tore it to pay compensation.',candidates=['רבא'],scope='Judgment in this agreement case')
challenge=q('challenge','9a:3','איתיביה רב יימר בר שלמיא לרבא ולהסיע על קיצתם','Rav Yeimar bar Shelamya challenges Rava from the authorization to enforce communal terms.',candidates=['רב יימר בר שלמיא'])
c('silent','9a:3','לא אהדר ליה רבא','Rava did not answer him.',scope='Narrated absence of response; no invented concession')
approval=c('approval','9a:3','אמר רב פפא שפיר עבד דלא אהדר ליה מידי','Rav Pappa says Rava acted properly by not answering.',candidates=['רב פפא'])
absent=c('absent','9a:3','ה"מ היכא דליכא אדם חשוב','Rav Pappa limits the stated enforcement authority to a place without an important authority.',candidates=['רב פפא'],conditions=['no אדם חשוב present'])
present=c('present','9a:3','אבל היכא דאיכא אדם חשוב לאו כל כמינייהו דמתנו','Where an important authority exists, the parties lack the same power to stipulate on their own.',candidates=['רב פפא'],conditions=['אדם חשוב present'])
e('challenge_objection',challenge,damages,'objection','9a:3');e('absent_qualification',absent,'bb.r022.enforce.c','qualification','9a:3');e('present_answer',present,challenge,'answer','9a:3');e('present_support',present,approval,'support','9a:3')
noaudit=c('no_audit','9a:4','אין מחשבין בצדקה עם גבאי צדקה','The teaching does not require accounting with charity collectors.',scope='Anonymous baraita’s presumption of trustworthy collectors, not an external administrative recommendation')
treasury=c('treasury','9a:4','ולא בהקדש עם הגזברין','It likewise does not require accounting with consecrated-property treasurers.',scope='Same baraita')
reminder=c('reminder','9a:4','ואע"פ שאין ראיה לדבר זכר לדבר','The text explicitly presents the verse as a reminder, not a proof.',scope='Stated evidentiary limitation')
faithful=c('faithful','9a:4','ולא יחשבו את האנשים אשר יתנו את הכסף על ידם לתת לעושי המלאכה כי באמונה הם עושים','It cites the verse that money given to the workers was not accounted with them because they acted faithfully.',scope='Quoted Kings passage offered as reminder')
e('faithful_reminder',faithful,noaudit,'analogy','9a:4');a.rows[-1]['uncertainty']=['Source explicitly denies full proof: אין ראיה לדבר זכר לדבר.']
e('reminder_qualification',reminder,faithful,'qualification','9a:4')
household=c('household','9a:5','א"ר אלעזר אע"פ שיש לו לאדם גזבר נאמן בתוך ביתו יצור וימנה','Rabbi Elazar says to bundle and count even with a trustworthy household treasurer.',candidates=['רבי אלעזר'],conditions=['trusted treasurer in one’s household'],composition='composite',scope='Household handling instruction; not a forced contradiction with public collector teaching')
countverse=c('count_verse','9a:5','שנאמר (מלכים ב יב, יא) ויצורו וימנו','Rabbi Elazar cites the verse saying they bundled and counted.',candidates=['רבי אלעזר'],scope='Scriptural support for household counting instruction')
e('countverse_support',countverse,household,'support','9a:5')
for row in a.rows:
    if row['layer']=='questions':
        row['content']['answer_set_status']='partial'
        row['uncertainty'].append('Source-present answer retained; this is not an exhaustive or task-qualified answer set.')
a.save_window(['8b:16','8b:17','8b:18']+['9a:'+str(i) for i in range(1,6)],'integrity023.json','Read complete collector-integrity and discretion cases through9a:5 with surrounding9a:6–15. Preserve personal-money scenarios, returned funds, unnamed מר, cross-page stipulation, Rava silence and Rav Pappa qualification, and explicit nonproof reminder language. Source-based reconciliation completed for all eight layers.',parent)

