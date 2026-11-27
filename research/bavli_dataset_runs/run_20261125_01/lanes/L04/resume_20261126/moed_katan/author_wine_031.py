"""Source reading12a:12–12b:1: loss, sealing and nonuniform festival rules."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r031');c=a.claim;e=a.e
refs=['12a:'+str(i) for i in range(12,20)]+['12b:1']
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Only actual local source replies; not exhaustive answer inventory or qualification.');return v
a.structure('wine',refs[:5],'Wine Mishnah, oil comparison and sealing beer')
a.structure('rules',refs[5:],'Local variation, vessel-size disagreement and Sabbath analogy')
yose=c('yose','12a:12',"וכן מי שהיה יינו בתוך הבור ואירעו אבל או אונס או שהטעוהו זולף וגומר וגף כדרכו דברי ר' יוסי",'When wine remains in the pit and mourning, unavoidable circumstances or failed arrangements intervene, Rabbi Yose permits drawing off, finishing and sealing normally.',candidates=['רבי יוסי'],conditions=['wine in pit','mourning, unavoidable event or failed arrangements'],composition='composite')
y=c('yehuda','12a:12',"ר' יהודה אומר עושה לו לימודים בשביל שלא יחמיץ",'Rabbi Yehuda permits making לימודים so it does not sour.',candidates=['רבי יהודה'],conditions=['prevent souring'],uncertainty=['לימודים technical arrangement retained without choosing a reconstruction.'])
need=c('need','12a:13','וצריכא','Both the oil and wine Mishnayot are needed.',scope='Anonymous statement followed by two distinct counterfactuals')
oil=c('oil','12a:13',"דאי אשמעינן קמייתא בההיא קאמר ר' יוסי משום דמישחא נפיש פסידיה אבל חמרא דלא נפיש פסידיה אימא מודי ליה לרבי יהודה",'If only the first case were taught, Rabbi Yose might permit only oil because its loss is greater and concede Rabbi Yehuda’s wine restriction.',mode='hypothetical',composition='composite',scope='Rejected inference from a single Mishnah, not Rabbi Yose’s final concession')
wine=c('wine','12a:13',"ואי אשמעינן בתרייתא בההיא קאמר רבי יהודה אבל בהך אימא מודה לר' יוסי צריכא",'If only the latter case were taught, Rabbi Yehuda might restrict wine but concede Rabbi Yose’s oil permission; therefore both are needed.',mode='hypothetical',composition='composite',scope='Second counterfactual, not an actual concession')
e('oil_need',oil,need,'support','12a:13');e('wine_need',wine,need,'support','12a:13')
changeq=q('changeq','12a:14','מאן תנא שינוי במועד בדבר האבד','Whose view requires an altered method for festival work involving loss?',candidates=['רב יצחק בר אבא'])
change=c('change','12a:14',"אמר רב יצחק בר אבא מאן תנא שינוי במועד בדבר האבד דלא כר' יוסי",'Rav Yitzhak bar Abba says such a requirement is not Rabbi Yose’s position.',candidates=['רב יצחק בר אבא'],conditions=['loss-related festival work'],uncertainty=['Printed name differs from Yitzhak bar Avdimi at11a:12; no silent name harmonization.'])
ruling=c('ruling','12a:14',"אמר רב יוסף הלכה כר' יוסי",'Rav Yosef rules in accordance with Rabbi Yose.',candidates=['רב יוסף'],scope='Explicit local ruling')
e('change_answer',change,changeq,'answer','12a:14');e('yose_ruling',ruling,yose,'local_resolution','12a:14')
beerq=q('beerq','12a:15','מהו למישע חביתא דשיכרא בחולא דמועדא','May one seal a beer barrel during the festival?')
reply=c('reply','12a:15',"אמר להו סיני אמר הלכה כר' יוסי",'Rav Nahman bar Yitzhak replies that Sinai said the halakha follows Rabbi Yose.',candidates=['רב נחמן בר יצחק'],scope='Reply invokes the title Sinai rather than inventing an explicitly printed personal name',uncertainty=['Identification of the title Sinai with Rav Yosef is contextual, not a name stated in this clause.'])
challenge=q('challenge','12a:15','אימור דאמר רבי יוסי בחמרא בשיכרא מי אמר','Rabbi Yose spoke about wine; did he say this about beer?')
why=q('why','12a:16','חמרא טעמא מאי','What is the reason for wine?')
loss=c('loss','12a:16','משום דנפיש פסידיה שיכרא נמי אית בה פסידא','Because its loss is substantial; beer too involves loss.',composition='composite',conditions=['loss from leaving unsealed'])
mother=c('mother','12a:16','דאמר אביי אמרה לי אם בר שית סאוי ושייע מבר תמני ולא שייע','Abaye transmits his mother’s comparison favoring a sealed six-sea vessel over an unsealed eight-sea vessel.',candidates=['אם (Abaye’s reported mother)'],role='quoted_authority',chain=['אביי','אם'],scope='Proverbial source comparison used to establish loss; relationship retained without supplying a personal name')
e('reply_answer',reply,beerq,'answer','12a:15');e('challenge_reply',challenge,reply,'objection','12a:15');e('loss_answer',loss,challenge,'answer','12a:16');e('loss_reason',loss,why,'answer','12a:16');e('mother_support',mother,loss,'support','12a:16')
analogy=c('analogy','12a:17','אמר רב חמא בר גוריא אמר רב הלכות מועד כהלכות כותים בהלכה','Rav Hama bar Gurya transmits Rav’s comparison of festival laws to the laws of כותים in the printed formulation.',candidates=['רב'],role='quoted_authority',chain=['רב חמא בר גוריא','רב'],scope='Comparison explained below; printed wording retained')
meaning=q('meaning','12a:17','למאי הלכתא','In what respect?')
separate=c('separate','12a:17','אמר רב דניאל בר קטינא (אמר רב) לומר שהן עקורות ואין למידות זו מזו','Rav Daniel bar Katina, with parenthetical אמר רב, explains that the laws are individually fixed and not derived from one another.',candidates=['רב (parenthetical)'],role='quoted_authority',chain=['רב דניאל בר קטינא','רב (parenthetical)'],scope='Source’s warning against transporting rules across cases',uncertainty=['Parenthetical transmission is preserved as printed.'])
e('separate_answer',separate,meaning,'answer','12a:17');e('separate_explains',separate,analogy,'qualification','12a:17')
small=c('small','12a:18','דאמר שמואל זופתין כוזתא ואין זופתין חביתא','Shmuel permits pitching a small vessel but excludes a barrel.',candidates=['שמואל'],composition='composite')
large=c('large','12a:18','רב דימי מנהרדעא אמר זופתין חביתא ואין זופתין כוזתא','Rav Dimi of Nehardea permits pitching a barrel but excludes the small vessel.',candidates=['רב דימי מנהרדעא'],composition='composite')
consider=c('consider','12a:18','מר חייש לפסידא ומר חייש לטירחא','One weighs loss and the other effort.',composition='composite',scope='Anonymous comparative explanation',uncertainty=['The compact מר/מר clause is retained without assigning the two motives by order alone.'])
e('vessel_distinction',large,small,'distinction','12a:18');e('vessels_example',consider,separate,'support','12a:18')
abbaye=c('abaye','12a:19','אמר אביי נקטינן הלכות מועד כהלכות שבת','Abaye says festival laws resemble Sabbath laws.',candidates=['אביי'],scope='Analogy limited by the cross-page explanation')
classes=c('classes','12b:1','יש מהן פטור אבל אסור ויש מהן מותר לכתחלה','Some cases are exempt yet prohibited and others permitted initially.',composition='composite',scope='Cross-page specification of Abaye’s analogy')
e('classes_explain',classes,abbaye,'qualification','12b:1')
a.save_window(refs,'resume_moed_katan_wine031.json','Read12a:12 through12b:1 with ensuing harvest discussion. Preserve both Mishnah opinions and counterfactuals, distinct named Yitzhak variants, local Yose outcome, Sinai title, beer loss proof, mother transmission, parenthetical Rav, opposing vessels and unassigned comparative motives.','fc14c5fd7845821f2613a3ed535e5097c38ffc4be3e059fb5ae13a4594f37091')
