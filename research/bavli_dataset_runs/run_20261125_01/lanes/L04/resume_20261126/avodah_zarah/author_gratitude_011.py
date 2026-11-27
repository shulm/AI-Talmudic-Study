"""Source reading through the end of the opening aggadic series."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('avodah_zarah','Avodah Zarah','az.r011');a.agent_id='/root/avodah_continuation_2'
c=a.claim;q=a.question;e=a.e
parent='52d8e45b62ed36e971815cb9f4956a5e59df8279226ae373a984b0ce65da7e38'
a.structure('plea',['5a:20'],'Conditional wording as supplication')
a.structure('gratitude',['5a:21','5a:22','5b:1','5b:2'],'Ingratitude, the omitted request, and forty years of understanding')
a.structure('study',['5b:3','5b:4'],'Torah, charitable action and disciplined study')
plea=c('plea','5a:20','אין אם אלא לשון תחנונים','The baraita interprets אם in אם בחקתי תלכו as supplication.',scope='Local interpretation of Leviticus26:3; no universal lexical rule independently inferred')
psalm=c('psalm','5a:20','וכן הוא אומר (תהלים פא, יד) לו עמי שומע לי [וגו\'] כמעט אויביהם אכניע','The baraita supports this with the Psalm’s wish for Israel’s obedience and subduing its enemies.',composition='composite',scope='Scriptural support')
isaiah=c('isaiah','5a:20','ואומר (ישעיהו מח, יח) לו הקשבת למצותי ויהי כנהר שלומך וגו\' ויהי כחול זרעך וצאצאי מעיך וגו\'','A second proof quotes Isaiah’s wish for obedience with peace and descendants.',composition='composite',scope='Scriptural support')
rebuke=c('rebuke','5a:21','אמר להן משה לישראל כפויי טובה בני כפויי טובה','The baraita portrays Moses rebuking Israel as ungrateful descendants of the ungrateful.',candidates=['משה'],scope='Quoted Moses speech within baraita, not producer evaluation')
request=c('request','5a:21','בשעה שאמר הקדוש ברוך הוא לישראל מי יתן והיה לבבם זה להם היה להם לומר תן אתה','At God’s wish for their enduring heart, Israel should have answered: You give it.',conditions=['when God said מי יתן'],scope='The baraita’s stated missed response, not a reply actually uttered')
breadstart=c('breadstart','5a:22','כפויי טובה דכתיב (במדבר כא, ה) ונפשנו קצה','The proof for ingratitude begins the verse complaining of revulsion, completed next page.',scope='Cross-page scriptural quotation; no completed independent object inferred from truncated wording')
bread=c('bread','5b:1','בלחם הקלוקל','The preceding complaint is completed with the despised bread wording.',scope='Completion of Numbers21:5 quoted at5a:22')
adam=c('adam','5b:1','בני כפויי טובה דכתיב (בראשית ג, יב) האשה אשר נתתה עמדי היא נתנה לי מן העץ ואוכל','The proof for ungrateful ancestry cites Adam’s blaming the woman given to him for the fruit he ate.',scope='Baraita’s scriptural argument from Genesis3:12; quoted Adam voice within the proof')
forty=c('forty','5b:2','אף משה רבינו לא רמזה להן לישראל אלא לאחר ארבעים שנה','Even Moses did not hint it to Israel until forty years later.',scope='Narrative/exegetical claim in the discussion')
fortyverse=c('fortyverse','5b:2','שנאמר (דברים כט, ד) ואולך אתכם במדבר ארבעים שנה וכתיב (דברים כט, ג) ולא נתן ה\' לכם לב וגו\'','The proof juxtaposes forty years in the wilderness with the statement that God had not given them a heart.',composition='composite')
rabbah=c('rabbah','5b:2','אמר רבה ש"מ לא קאי איניש אדעתיה דרביה עד ארבעין שנין','Rabbah infers that a person does not grasp the teacher’s intention until forty years.',candidates=['רבה'],scope='Named inference; רבה preserved distinctly from רבא')
waterq=q('water_q','5b:3','מאי דכתיב (ישעיהו לב, כ) אשריכם זורעי על כל מים משלחי רגל השור והחמור','Rabbi Yohanan in Rabbi Bena’a’s name asks the meaning of sowing beside all waters and sending the ox and donkey.',candidates=['רבי בנאה'],chain=['רבי יוחנן'])
inclination=c('inclination','5b:3','אשריהם ישראל בזמן שעוסקין בתורה ובגמילות חסדים יצרם מסור בידם ואין הם מסורים ביד יצרם','When Israel engages in Torah and acts of kindness, its inclination is under its control, rather than the reverse.',candidates=['רבי בנאה'],chain=['רבי יוחנן'],conditions=['engaging in Torah and acts of kindness'],scope='Transmitted exposition',composition='composite')
sow=c('sow','5b:3','ואין זריעה אלא צדקה שנאמר (הושע י, יב) זרעו לכם לצדקה וקצרו לפי חסד','Sowing is interpreted as charity, supported by Hosea10:12.',candidates=['רבי בנאה'],chain=['רבי יוחנן'],scope='Local scriptural word mapping')
water=c('water','5b:3','ואין מים אלא תורה שנאמר (ישעיהו נה, א) הוי כל צמא לכו למים','Water is interpreted as Torah, supported by Isaiah55:1.',candidates=['רבי בנאה'],chain=['רבי יוחנן'],scope='Local scriptural word mapping')
discipline=c('discipline','5b:4','תנא דבי אליהו לעולם ישים אדם עצמו על דברי תורה כשור לעול וכחמור למשאוי','The school of Elijah teaches applying oneself to Torah like an ox to a yoke and a donkey to a load.',candidates=['תנא דבי אליהו'],scope='Teaching attached to the ox/donkey clause; school formula not silently converted to direct Elijah speech',composition='composite')
e('psalm_support',psalm,plea,'support','5a:20');e('isaiah_support',isaiah,plea,'support','5a:20');e('request_support',request,rebuke,'support','5a:21');e('breadstart_support',breadstart,rebuke,'support','5a:22');e('bread_completion',bread,breadstart,'qualification','5b:1');e('adam_support',adam,rebuke,'support','5b:1');e('fortyverse_support',fortyverse,forty,'support','5b:2');e('forty_support',forty,rabbah,'support','5b:2');e('inclination_answer',inclination,waterq,'answer','5b:3');e('sow_support',sow,inclination,'support','5b:3');e('water_support',water,inclination,'support','5b:3');e('discipline_answer',discipline,waterq,'answer','5b:4')
for row in a.rows:
 if row['id']==waterq:
  row['content']['answer_set_status']='partial';row['uncertainty'].append('Represented interpretations of this verse only; no certified alternatives.')
a.save_window(['5a:20','5a:21','5a:22','5b:1','5b:2','5b:3','5b:4'],'gratitude011.json','Original5a:20–5b:4 reread with continuation through6a:16; preserve unuttered response as normative counterfactual, Moses/Adam scriptural voices, split bread quotation, Rabbah identity, Yohanan/Benaa transmission and school-of-Elijah formula. All layers reread; linked earlier tails deliberately preserved pending explicit complete-scope structural revisions.',parent)
