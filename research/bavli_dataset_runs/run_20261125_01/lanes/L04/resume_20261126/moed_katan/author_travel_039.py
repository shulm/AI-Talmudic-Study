"""Direct source reading14a:11–15: travel motives and careful attribution of agreement."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r039');c=a.claim;e=a.e
refs=['14a:'+str(i) for i in range(11,16)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Represented local argument replies only, not exhaustive choices.');return v
a.structure('travel',refs,'Overseas haircut permission: travel purpose and a reformulated agreement report')
noty=c('noty','14a:11',"מתניתין דלא כר' יהודה",'The Mishnah is identified as not Rabbi Yehuda’s view.',scope='Anonymous initial identification')
y=c('yehuda','14a:11',"ר' יהודה אומר הבא ממדינת הים לא יגלח מפני שיצא שלא ברשות",'Rabbi Yehuda says the overseas traveler may not cut hair because he departed without permission.',candidates=['רבי יהודה'],conditions=['departure without permission'],scope='Baraita restriction whose scope Rava explains below')
tour=c('tour','14a:12','אמר רבא לשוט דברי הכל אסור','Rava says all agree that travel for touring entails prohibition.',candidates=['רבא'],conditions=['touring'])
food=c('food','14a:12','למזונות דברי הכל מותר','Rava says all agree that travel for livelihood entails permission.',candidates=['רבא'],conditions=['livelihood'])
profit=c('profit','14a:12','לא נחלקו אלא להרויחא','They disagree only about travel for profit.',candidates=['רבא'],conditions=['additional profit'],scope='Rava’s bounded dispute characterization')
compare=c('compare','14a:12','מר מדמי ליה כלשוט ומר מדמי ליה כלמזונות','One compares profit travel to touring and the other to livelihood.',composition='composite',scope='Anonymous comparative formulations; later source explicitly states concessions',uncertainty=['The two מר clauses are not assigned by name order.'])
e('rava_qualifies',profit,y,'qualification','14a:12')
report=c('report','14a:13',"אמר ר' נראין דברי ר' יהודה כשיצא שלא ברשות ודברי חכמים כשיצא ברשות",'Rabbi says Rabbi Yehuda’s words appear when departure was without permission and the sages’ words when with permission.',candidates=['רבי'],role='quoted_authority',composition='composite',scope='Initial quoted wording, interpreted by the following discussion')
what=q('what','14a:13','מאי שלא ברשות','What does departure without permission mean?')
touring=c('touring','14a:13','אילימא לשוט והאמרת דברי הכל אסור','If it means touring, all were said to prohibit it.',mode='challenged',scope='First rejected interpretation of the quoted endorsement')
livelihood=c('livelihood','14a:13','ואלא למזונות והאמרת דברי הכל מותר','If it means livelihood, all were said to permit it.',mode='challenged',scope='Second rejected interpretation')
profitassume=c('profitassume','14a:13','אלא פשיטא להרויחא','The discussion therefore assumes it means profit.',mode='challenged',scope='Intermediate assumption contradicted by reading the second clause')
e('profitassume_answer',profitassume,what,'answer','14a:13')
what2=q('what2','14a:14','מאי ברשות','What does departure with permission mean?')
food2=c('food2','14a:14','אילימא למזונות הא אמרת דברי הכל מותר','If livelihood, everyone was already said to permit it.',mode='challenged',scope='Rejected interpretation of the second clause')
profitq=q('profitq','14a:14','ואלא להרויחא והא אמרת נראין דברי רבי יהודה בהא','If profit, was Rabbi Yehuda’s view not just preferred in that same case?')
e('profit_objection',profitq,profitassume,'objection','14a:14')
agree_y=c('agree_y','14a:15',"נראין דברי ר' יהודה לרבנן כשיצא שלא ברשות ומאי ניהו לשוט",'The reformulation says Rabbi Yehuda’s words appear to the sages when departure was without permission, namely touring.',composition='composite',scope='Explicit agreement attribution in the source, not assignment from name order')
concede_y=c('concede_y','14a:15','שאפילו חכמים לא נחלקו עליו אלא להרויחא אבל לשוט מודו ליה','The sages dispute him only for profit but concede touring.',conditions=['profit disputed','touring conceded'],composition='composite')
agree_s=c('agree_s','14a:15',"ונראין דברי רבנן לר' יהודה כשיצא ברשות ומאי ניהו למזונות",'The sages’ words appear to Rabbi Yehuda when departure was permitted, namely livelihood.',composition='composite',scope='Explicit counterpart agreement in reformulation')
concede_s=c('concede_s','14a:15','שאפילו רבי יהודה לא נחלק עליהם אלא להרויחא אבל למזונות מודה להו','Rabbi Yehuda disputes them only for profit but concedes livelihood.',conditions=['profit disputed','livelihood conceded'],composition='composite')
e('agree_y_corrects',agree_y,report,'correction','14a:15');e('agree_s_corrects',agree_s,report,'correction','14a:15');e('agree_y_answer',agree_y,what,'answer','14a:15');e('agree_s_answer',agree_s,what2,'answer','14a:15');e('profitq_answer',agree_s,profitq,'answer','14a:15');e('concede_y_support',concede_y,agree_y,'support','14a:15');e('concede_s_support',concede_s,agree_s,'support','14a:15')
a.save_window(refs,'resume_moed_katan_travel039.json','Read through15a:25. Preserve Rava three-purpose distinctions, initial baraita wording, all rejected interpretations and intermediate profit assumption, and explicit reformulation of who concedes what. Do not invent a named mapping merely from מר/מר order.','67f9195365b272474279ca7297dde550d5dc7981cdb9336510ae06863a507b6c')
