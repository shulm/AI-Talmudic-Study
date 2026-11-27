"""Charity narratives and residential-status variants, explicitly read."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r030');c=a.claim;q=a.question;e=a.e
parent='5621e864d323793a63173754dd83f58a22c6f5308adc562479fd4bf8cc3a4437'
a.structure('benjamin',['11a:2'],'Binyamin the righteous supports a woman and her children')
a.structure('monobaz',['11a:3','11a:4'],'King Monobaz’s expenditure and six contrasts about storing wealth')
a.structure('residence',['11a:5','11a:6'],'Property purchase and two reports of Rabban Shimon ben Gamliel')
admin=c('admin','11a:2','בנימין הצדיק שהיה ממונה על קופה של צדקה','Binyamin the righteous administered the charity fund.',scope='Narrative introduction')
request=c('request','11a:2','פעם אחת באתה אשה לפניו בשני בצורת אמרה לו רבי פרנסני','During years of drought a woman came and asked him to sustain her.',scope='Narrative with quoted request')
empty=c('empty','11a:2','העבודה שאין בקופה של צדקה כלום','Binyamin swears that the charity fund is empty.',candidates=['בנימין הצדיק'],scope='Quoted statement in the narrative')
plea=c('plea','11a:2','רבי אם אין אתה מפרנסני הרי אשה ושבעה בניה מתים','The woman says that unless he sustains her, she and her seven children will die.',conditions=['no support provided'],scope='Woman’s quoted conditional plea; not an event said to have occurred')
private=c('private','11a:2','עמד ופרנסה משלו','He supports her from his own resources.',scope='Narrative action')
ill=c('ill','11a:2','לימים חלה ונטה למות','Later he becomes ill and approaches death.',scope='Narrative event')
life=c('life','11a:2','כל המקיים נפש אחת מישראל כאילו קיים עולם מלא','The ministering angels invoke the divine teaching that sustaining one life from Israel is like sustaining an entire world.',candidates=['הקב"ה'],role='quoted_authority',chain=['מלאכי השרת','הקב"ה'],scope='Divine teaching quoted within the angels’ represented speech; printed מישראל retained')
angelq=q('angel_q','11a:2','ובנימין הצדיק שהחיה אשה ושבעה בניה ימות בשנים מועטות הללו','The ministering angels ask whether Binyamin, who sustained a woman and seven children, should die after so few years.',candidates=['מלאכי השרת'])
decree=c('decree','11a:2','מיד קרעו לו גזר דינו','The narrative says his decree was immediately torn up.',scope='Source narrative outcome')
years=c('years','11a:2','תנא הוסיפו לו עשרים ושתים שנה על שנותיו','A teaching adds that twenty-two years were added to his life.',scope='Explicit appended teaching; not an independent longevity estimate')
e('angel_reason',life,angelq,'support','11a:2');e('decree_answer',decree,angelq,'answer','11a:2');e('years_continuation',years,decree,'qualification','11a:2')
spend=c('spend','11a:3','מעשה במונבז המלך שבזבז אוצרותיו ואוצרות אבותיו בשני בצורת','King Monobaz spent his treasures and his ancestors’ treasures during years of drought.',scope='Narrated event')
complaint=c('complaint','11a:3','אבותיך גנזו והוסיפו על של אבותם ואתה מבזבזם','His brothers and family object that the ancestors accumulated wealth while he dissipates it.',scope='Quoted family objection')
items=[('above','11a:3','אבותי גנזו למטה ואני גנזתי למעלה','His ancestors stored below; he stores above.','אמת מארץ תצמח וצדק משמים נשקף'),('secure','11a:3','אבותי גנזו במקום שהיד שולטת בו ואני גנזתי במקום שאין היד שולטת בו','They stored where hands can reach; he stores beyond their reach.','צדק ומשפט מכון כסאך'),('fruit','11a:4','אבותי גנזו דבר שאין עושה פירות ואני גנזתי דבר שעושה פירות','They stored what bears no fruit; he stores what bears fruit.','אמרו צדיק כי טוב כי פרי מעלליהם יאכלו'),('lives','11a:4','אבותי גנזו [אוצרות] ממון ואני גנזתי אוצרות נפשות','They stored monetary treasure; he stores lives.','פרי צדיק עץ חיים ולוקח נפשות חכם'),('self','11a:4','אבותי גנזו לאחרים ואני גנזתי לעצמי','They stored for others; he stores for himself.','ולך תהיה צדקה'),('future','11a:4','אבותי גנזו לעולם הזה ואני גנזתי לעולם הבא','They stored for this world; he stores for the world to come.',"והלך לפניך צדקך כבוד ה' יאספך")]
for key,ref,quote,text,verse in items:
 cid=c(key,ref,quote,'Monobaz’s reply: '+text,candidates=['מונבז המלך'],naming_refs=['11a:3'],composition='composite',scope='Paired contrast in the king’s stated justification; not two independently inferred attitudes')
 vid=c(key+'_verse',ref,verse,'Quoted scriptural support for the '+key+' contrast.',scope='Evidence text retained verbatim in the source span')
 e(key+'_support',vid,cid,'support',ref);e(key+'_reply',cid,complaint,'answer',ref)
mishnah=c('mishnah','11a:5','ואם קנה בה בית דירה הרי הוא כאנשי העיר','The recalled Mishnah grants town-member status when a dwelling is purchased there.',conditions=['purchases a dwelling in the town'],scope='Recalled Mishnah clause')
notrsg=c('not_rsg','11a:5','מתניתין דלא כרשב"ג','The discussion initially says this Mishnah does not follow Rabban Shimon ben Gamliel.',mode='challenged',scope='Initial comparison against one report; next segment preserves two reports')
anyland=c('anyland','11a:5','רבן שמעון ב"ג אומר אם קנה בה קרקע כל שהוא הרי הוא כאנשי העיר','One baraita reports Rabban Shimon ben Gamliel granting town-member status for purchasing any amount of land.',candidates=['רבן שמעון ב"ג'],conditions=['purchases any amount of land in town'],scope='First tannaitic report')
suitable=c('suitable','11a:6','רבן שמעון בן גמליאל אומר אם קנה שם קרקע הראויה לבית דירה הרי הוא כאנשי העיר','Another baraita reports him requiring land suitable for a dwelling.',candidates=['רבן שמעון בן גמליאל'],conditions=['purchases land suitable for a dwelling'],scope='Second tannaitic report; no silent harmonization')
versions=c('versions','11a:6','תרי תנאי ואליבא דרבן שמעון בן גמליאל','The resolution identifies two tannaitic transmitters reporting Rabban Shimon ben Gamliel differently.',scope='Explicit alternative transmission accounts; no retraction assigned to the authority')
e('first_support',anyland,notrsg,'support','11a:5');e('second_objection',suitable,notrsg,'objection','11a:6');e('versions_resolution',versions,suitable,'local_resolution','11a:6');e('versions_qualification',versions,anyland,'qualification','11a:6')
for row in a.rows:
 if row['layer']=='questions':row['content']['answer_set_status']='partial';row['uncertainty'].append('Narrative response represented; not a choice inventory or task qualification.')
a.save_window(['11a:'+str(i) for i in range(2,7)],'charityend030b.json','Read original11a:2–12b:14, then reread narratives and status discussion. Keep requests, stated motives, source outcomes, six distinct paired contrasts, exact scriptural supports and contradictory reports as transmission variants. No invented retraction or harmonization.',parent)
