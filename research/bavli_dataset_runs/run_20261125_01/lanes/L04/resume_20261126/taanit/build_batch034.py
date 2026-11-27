"""Manual reading16b:15–17a:9, with continuation read through17b:13."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','04c393dc2da7d3ec92ca948cdf3fadf667aa585c95723e274f423069dde1369c').replace('ta.resume008.','ta.resume034.').replace('/root/taanit_continuation_2','/root/taanit_continuation_4')
exec(compile(helper,__file__,'exec'))
Aq=q('yehuda.reason.q','16b:15',ix['16b:15']['text'][ix['16b:15']['text'].index('מאי טעמא'):ix['16b:15']['text'].index('לפי שאין')],'What is Rabbi Yehuda’s reason for replacing remembrances and shofars?')
A=c('restricted.days','17a:1',ix['17a:1']['text'],'Rabbi Adda of Jaffa explains that remembrances and shofars are said only on Rosh Hashanah, jubilees and during war.',who='Rabbi Adda of Jaffa',cond=['Rosh Hashanah, jubilee or wartime'],comp='composite',status='explanation of Rabbi Yehuda’s view; sentence begins on preceding folio')
for z in P['records']:
 if z['id'] in [A,A+'.u',A+'.a',A+'.p']:z['evidence'].insert(0,ev('16b:15',ix['16b:15']['text'][ix['16b:15']['text'].index('א"ר אדא'):]))
e('yehuda.reason.answer','17a:1',ix['17a:1']['text'],A,Aq,'answer');e('yehuda.reason.support','17a:1',ix['17a:1']['text'],A,'ta.resume030.yehuda.replacement')
B=c('formula.exchange','17a:2','תנא יש מחליפין צעקה לאליהו ותפלה לשמואל','A teaching reports an alternate arrangement assigning cry to Elijah and prayer to Samuel.',voice='anonymous teaching',comp='composite',status='alternative liturgical arrangement, earlier ordering retained')
C=c('samuel.both','17a:2','בשלמא גבי שמואל כתיב ביה תפלה וכתיב ביה צעקה','The discussion accepts Samuel’s case because Scripture uses both prayer and cry for him.',comp='composite')
Cq=q('elijah.cry.q','17a:3','אלא גבי אליהו תפלה כתיב צעקה לא כתיב','For Elijah, prayer is written but where is cry written?')
D=c('elijah.answer','17a:3',"(מלכים א יח, לז) ענני ה' ענני לשון צעקה היא:",'Elijah’s answer me, answer me is interpreted as language of crying out.',voice='anonymous scriptural explanation');e('elijah.cry.answer','17a:3',ix['17a:3']['text'],D,Cq,'answer');e('exchange.support','17a:3',ix['17a:3']['text'],D,B)
Eq=q('jonah.order.q','17a:4','מכדי יונה בתר דוד ושלמה הוה מאי טעמא מקדים ליה ברישא','Since Jonah lived after David and Solomon, why place him first in the liturgical ordering?')
E=c('earth.ending','17a:4','משום דבעי למיחתם מרחם על הארץ','The reason is to end with Merciful toward the land.');e('jonah.order.answer','17a:4','משום דבעי למיחתם מרחם על הארץ',E,Eq,'answer')
F=c('sumkhus.ending','17a:4','תנא משום סומכוס אמרו ברוך משפיל הרמים:','A teaching in Sumkhus’s name gives the conclusion Blessed is He who lowers the exalted.',who='Sumkhus',chain=['unnamed teaching','Sumkhus'],status='alternative conclusion formula')
Fq=q('watch.wine.q','17a:5','מפני מה אמרו אנשי משמר מותרין לשתות יין בלילות אבל לא בימים','Why may watch members drink wine at night but not by day?',voice='baraita')
G=c('watch.assistance','17a:5','שמא תכבד העבודה על אנשי בית אב ויבואו ויסייעו להם','The concern is that the daily family’s work becomes heavy and watch members need to help.',voice='baraita',mode='conditional',cond=['daily family may need assistance']);e('watch.wine.answer','17a:5',ix['17a:5']['text'],G,Fq,'answer')
Gq=q('family.wine.q','17a:6','מפני מה אמרו אנשי בית אב לא ביום ולא בלילה','Why may the daily family drink neither day nor night?',voice='baraita')
H=c('constant.service','17a:6','מפני שהן עסוקין תמיד בעבודה','They are continually engaged in service.',voice='baraita');e('family.wine.answer','17a:6','מפני שהן עסוקין תמיד בעבודה',H,Gq,'answer')
I=c('known.day','17a:7','מכאן אמרו כל כהן שמכיר משמרתו ומשמרת בית אב שלו ויודע שבתי אבותיו קבועין שם אסור לשתות יין כל אותו היום','A priest knowing his watch and daily family and their established placement may not drink throughout that day.',voice='baraita',cond=['knows watch','knows daily family','family established there','that day'])
J=c('known.week','17a:7','במכיר משמרתו ואין מכיר משמרת בית אב שלו ויודע שבתי אבותיו קבועין שם אסור לשתות יין כל אותה שבת','Knowing the watch but not daily family, with family established there, prohibits drinking all that week.',voice='baraita',cond=['knows watch','does not know daily family','family established there','that week'])
K=c('unknown.year','17a:8',ix['17a:8']['text'],'Not knowing either watch or daily family while knowing the family is established there prohibits wine throughout the year.',voice='baraita',cond=['knows neither watch nor daily family','family established there','entire year'])
L=c('rabbi.wine','17a:9','רבי אומר אומר אני אסור לשתות יין לעולם אבל מה אעשה שתקנתו קלקלתו','Rabbi says he would prohibit wine always, but adds that the person’s remedy is his impairment.',who='Rabbi',comp='composite',status='compact explanation linked by Abaye to present priestly drinking',unc=['תקנתו קלקלתו retained as paradoxical wording; no extra historical narrative supplied.'])
Lq=q('present.wine.q','17a:9','אמר אביי כמאן שתו האידנא כהני חמרא','Whose view do present-day priests follow when drinking wine?',who='Abaye')
M=c('abaye.rabbi','17a:9','כרבי:','Abaye identifies Rabbi as the basis for present practice.',who='Abaye')
for z in P['records']:
 if z['id'] in [M,M+'.u',M+'.a',M+'.p']:z['evidence'].insert(0,ev('17a:9','אמר אביי כמאן שתו האידנא כהני חמרא'))
e('present.wine.answer','17a:9','כרבי:',M,Lq,'answer')
refs=list(ix);refs=refs[refs.index('16b:15'):refs.index('17a:9')+1]
for k,title,first,last in [('formulas','Yehuda’s replacement reason and alternative formula order/conclusions','16b:15','17a:4'),('wine','Priestly wine restrictions by service knowledge and present practice','17a:5','17a:9')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'16b:15':'Reason question and Adda named explanation linked across folio.','17a:1':'All three occasions for remembrances/shofars retained.','17a:2':'Alternate cry/prayer allocations and Samuel dual-language premise retained.','17a:3':'Elijah cry question and answer-me verse interpretation retained.','17a:4':'Jonah chronology/order question, land-ending rationale and Sumkhus alternative retained.','17a:5':'Watch wine timing question and possible-assistance rationale retained.','17a:6':'Daily-family question and continuous-service rationale retained.','17a:7':'Both knowledge-conditioned day/week rules retained.','17a:8':'Unknown-watch/family yearly restriction retained.','17a:9':'Rabbi prohibition/qualification wording and Abaye present-practice question/answer retained; later comparison read through17b13.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial inventory covers represented local source-supported response only; no exhaustive alternatives or task eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch034.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
