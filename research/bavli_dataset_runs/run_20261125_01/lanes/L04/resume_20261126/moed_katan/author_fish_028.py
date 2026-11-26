"""Source reading11a:14–21, two fish permission versions and named food reports."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r028');c=a.claim;e=a.e
refs=['11a:'+str(i) for i in range(14,22)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Local source-present answer only; no exhaustive set or certification.');return v
a.structure('fish',refs[:4],'Fish capture and salting: distinct versions and distinct answers')
a.structure('food',refs[4:7],'Rav’s visit and Adda the fisherman’s reported sayings')
a.structure('chapter',[refs[7]],'Explicit end-of-chapter marker')
event=c('event','11a:14','בדיתא לבאי כוורי אזיל כולי עלמא צוד אייתו כוורא','The narrative describes fish becoming available at Bedita and people catching and bringing fish.',scope='Narrative background; place wording preserved in evidence')
permission=c('permission','11a:14','שרא להו רבא למימלח מינייהו','Rava permitted salting some of them.',candidates=['רבא'],scope='First narrative version, after fish had already been brought')
challenge=q('challenge','11a:15','אמר ליה אביי והא תנן כבשין שהוא יכול לאכול מהן במועד כובשן','Abaye challenges from the Mishnah permitting pickling what can be eaten during the festival.',candidates=['אביי'])
loss=c('loss','11a:15','אמר ליה כיון דמעיקרא אדעתא דאכילה אייתינהו ואי שביק להו פסדי כפרקמטיא האבד דמי ושרי','Rava answers that they originally brought the fish to eat, and leaving them would spoil them; they resemble perishable merchandise and are permitted.',candidates=['רבא'],conditions=['originally brought for eating','would spoil if left'],composition='composite')
e('challenge_permission',challenge,permission,'objection','11a:15');e('loss_answer',loss,challenge,'answer','11a:15')
second=c('second','11a:16','ואיכא דאמרי שרי להו רבא מיצד מיזל אייתויי ומימלח','An alternative report says Rava permitted catching, going, bringing and salting the fish.',candidates=['רבא'],composition='composite',scope='Second version; not silently combined with the already-brought condition in the first')
challenge2=q('challenge2','11a:16','אמר ליה אביי והא אנן כבשין שהוא יכול לאכול מהן כובשן תנן','Abaye again challenges from the Mishnah’s festival edibility condition.',candidates=['אביי'])
press=c('press','11a:17','אמר ליה הני נמי מיתאכלי אגב איצצא','Rava answers that these too are edible through איצצא.',candidates=['רבא'],conditions=['edibility via איצצא'],uncertainty=['The preparation technique is retained literally without specifying an unsupported recipe.'])
e('challenge2_permission',challenge2,second,'objection','11a:16');e('press_answer',press,challenge2,'answer','11a:17')
shmuel=c('shmuel','11a:17','כי הא דשמואל עבדו ליה שיתין איצצי ואכל','The illustration reports that sixty איצצי were prepared for Shmuel and he ate.',scope='Illustrative narrative, not a statement by Shmuel or an invented dispute')
rava=c('rava','11a:17','רבא איקלע לבי ריש גלותא עבדי ליה שיתין איצצי ואכל','Rava visited the Exilarch’s house; sixty איצצי were prepared and he ate.',scope='Second illustrative narrative')
e('shmuel_example',shmuel,press,'support','11a:17');e('rava_example',rava,press,'support','11a:17')
visit=c('visit','11a:18','רב איקלע לבי רב שפיר אייתו לקמייהו ההוא כוורא תילתא בישולא תילתא מילחא ותילתא טוויא','Rav visited Rav Shappir’s house; a fish was served one third cooked, one third salted and one third roasted.',composition='composite',scope='Narrative presentation, with both named persons distinct')
good=c('good','11a:19','אמר רב אמר לי אדא ציידא כוורא סמוך למיסרחיה מעלי','Rav reports Adda the fisherman saying fish is good near the point of spoiling.',candidates=['אדא ציידא'],role='quoted_authority',chain=['רב','אדא ציידא'],scope='Historical food saying, not present food-safety guidance')
family=c('family','11a:19','ואמר רב אמר לי אדא ציידא כוורא טווייא באחוה אסוקיה באבוה מיכלי בבריה אשתי עליה אבוה','Rav transmits Adda’s compressed preparation/eating/drinking instructions using brother, father and son imagery.',candidates=['אדא ציידא'],role='quoted_authority',chain=['רב','אדא ציידא'],composition='composite',scope='Literal metaphoric sequence retained; no unstated ingredient identifications supplied',uncertainty=['The source’s compact kinship metaphors need separate commentary review before a specific recipe can be assigned.'])
body=c('body','11a:20','ואמר רב אמר לי אדא ציידא כוורא תחלי וחלבא ליטעון גופא ולא ליטעון פוריא','Rav transmits Adda’s saying about fish, cress and milk: let the body bear them rather than the bed.',candidates=['אדא ציידא'],role='quoted_authority',chain=['רב','אדא ציידא'],composition='composite',scope='Historical food/behavior saying, not present health advice',uncertainty=['Idiomatic contrast retained rather than turned into an unsupported medical claim.'])
drinks=c('drinks','11a:20','ואמר רב אמר לי אדא ציידא כוורא תחלי וחלבא מיא ולא שיכרא שיכרא ולא חמרא','Rav transmits Adda’s ranking for fish, cress and milk: water rather than beer, beer rather than wine.',candidates=['אדא ציידא'],role='quoted_authority',chain=['רב','אדא ציידא'],composition='composite',scope='Historical reported food saying')
a.speech('marker','11a:21','הדרן עלך משקין','',act='chapter-closing formula',uncertainty=['Paratext retained separately; no legal claim or named speaker assigned.'])
a.save_window(refs,'resume_moed_katan_fish028.json','Direct reading11a:14–21 with next chapter11b context. Preserve two versions and distinct loss/edibility answers, Shmuel/Rava illustrative events, Rav versus Rav Shappir, full repeated Adda transmission, food idioms and explicit chapter marker without converting them into medical advice or fabricated rulings.','5ef7d76993382407137ed2532f70f7af1399f3e3e00aecdbb65fbb99004cac96')
