"""Direct reading13a:14–13b:2: moving, craftsman items and rejected trust explanation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r036');c=a.claim;e=a.e
refs=['13a:'+str(i) for i in range(14,18)]+['13b:1','13b:2']
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Source-present local replies only, including challenged intermediate proposals; no exhaustive comparable inventory.');return v
a.structure('moving',refs[:2],'House-to-house restriction and courtyard-house clarification')
a.structure('craftsmen',refs[2:],'Contradictory transport baraitot, two proposals and return to the first')
house=c('house','13a:14','אין מפנין מבית לבית','The Mishnah prohibits moving from house to house.')
court=c('court','13a:14','אבל מפנה הוא לחצרו','It permits moving to his courtyard.',scope='Mishnah phrase clarified below as a house in the courtyard')
items=c('items','13a:14','אין מביאין כלים מבית האומן','It prohibits bringing items from the craftsman’s house.')
fear=c('fear','13a:14','אם חושש להם מפנן לחצר אחרת','If concerned for the items, he may move them to another courtyard.',conditions=['concern for items'])
e('fear_limits',fear,items,'qualification','13a:14')
houseq=q('houseq','13a:15','והאמרת רישא אין מפנין כלל','Does the opening not prohibit moving altogether?')
abaye=c('abaye','13a:15','אמר אביי סיפא אתאן לבית שבחצר','Abaye explains the latter clause as a house within the courtyard.',candidates=['אביי'])
e('abaye_answer',abaye,houseq,'answer','13a:15');e('abaye_qualifies',abaye,court,'qualification','13a:15')
test=c('test','13a:16','אמר רב פפא בדיק לן רבא','Rav Pappa reports that Rava tested them.',candidates=['רב פפא'],scope='Teaching narrative; Pappa reports, Rava poses the test')
contradict=q('contradict','13a:16','תנן אין מביאין כלים מבית האומן ורמינהו','How can the Mishnah’s prohibition on bringing craftsman items be reconciled with the contrary source?',candidates=['רבא'],role='quoted_authority',chain=['רב פפא','רבא'])
bring=c('bring','13a:16','מוליכין ומביאין כלים מבית האומן ואע"פ שאינן לצורך המועד','The contrary source permits taking and bringing craftsman items even without festival need.',composition='composite',scope='Quoted source with scope debated below')
first=c('first','13a:17','ושנינן ליה כאן בארבעה עשר כאן בחולו של מועד','The respondents distinguish the fourteenth from the festival’s intermediate days.',composition='composite',scope='First reconciliation; speaker group not assigned individual names')
second=c('second','13a:17','איבעית אימא הא והא בחולו של מועד כאן במאמינו כאן בשאינו מאמינו','Alternatively, both concern the intermediate days and distinguish trusting the craftsman from not trusting him.',mode='challenged',composition='composite',scope='Second reconciliation later rejected as insufficient for taking items to the craftsman')
e('bring_objection',bring,items,'objection','13a:16');e('first_answer',first,contradict,'answer','13a:17');e('second_answer',second,contradict,'answer','13a:17')
allow=c('allow','13b:1','מביאין כלים מבית האומן כגון כד מבית הכדר וכוס מבית הזגג','A baraita allows bringing items such as a jug from the potter and a cup from the glassworker.',composition='composite')
exclude=c('exclude','13b:1','אבל לא צמר מבית הצבע ולא כלים מבית האומן','It excludes wool from the dyer and other items from the craftsman.',composition='composite',scope='Specific contrast in the quoted list, not a denial of the preceding named allowances')
wages=c('wages','13b:1','ואם אין לו מה יאכל נותן לו שכרו ומניחו אצלו','If the craftsman has nothing to eat, he pays the wages and leaves the items with him.',conditions=['craftsman lacks food'],composition='composite')
near=c('near','13b:1','ואם אינו מאמינו מניחו בבית הסמוך לו','If he does not trust him, he places them in the adjacent house.',conditions=['does not trust craftsman'])
thieves=c('thieves','13b:1','ואם חושש להם שמא יגנבו (מפנן לחצר אחרת ואם אינו מאמינו) מביאן בצנעה בתוך ביתו','If concerned they may be stolen, the text permits bringing them privately home, retaining its parenthetical intermediate courtyard/trust wording.',conditions=['fear of theft','private transport'],composition='composite',uncertainty=['Parenthetical (מפנן לחצר אחרת ואם אינו מאמינו) is retained rather than normalized away.'])
challenge=q('challenge','13b:2','תרצת מביאין מוליכין קשיא','Bringing has been explained, but taking remains difficult.')
reason=c('reason','13b:2','דקתני אין מביאין וכל שכן שאין מוליכין','The prohibition on bringing implies all the more a prohibition on taking.',scope='Anonymous reason that the trust explanation is insufficient')
returnfirst=c('returnfirst','13b:2','אלא מחוורתא כדשניין מעיקרא','The first reconciliation is therefore preferred.',scope='Explicit return to the fourteenth-versus-festival distinction; no silent retention of both as equally final')
e('challenge_second',challenge,second,'objection','13b:2');e('reason_challenge',reason,challenge,'support','13b:2');e('return_answer',returnfirst,challenge,'answer','13b:2');e('return_correction',returnfirst,second,'correction','13b:2');e('return_first',returnfirst,first,'local_resolution','13b:2')
a.save_window(refs,'resume_moed_katan_moving036.json','Read13a:14–13b:2 plus ensuing chapter continuation. Preserve house/courtyard distinction, Rav Pappa narrative about Rava test, both initial reconciliations, detailed poverty/trust/theft baraita and parenthesis, and final explicit preference for first reconciliation after taking remains difficult.','87eaa81e941a2c52291f1955b1b4a46d8b79656ebc857de0e999126d18a58ef2')
