"""Manual source reading 12b:9–13a:1; continuation read through 13b:16."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','32bcf629046f104ec121ba829715249cb950f910fccadc3d989be9ea6592d300').replace('ta.resume008.','ta.resume025.').replace('/root/taanit_continuation_2','/root/taanit_continuation_4')
exec(compile(helper,__file__,'exec'))
A=c('second.three','12b:9',"עברו אלו ולא נענו בית דין גוזרין ג' תעניות אחרות על הצבור",'After these fasts pass without response, the court decrees three further public fasts.',voice='Mishnah',cond=['earlier fasts passed without response'])
B=c('day.before.food','12b:9','אוכלין ושותין מבעוד יום','Eating and drinking are restricted to the preceding daytime.',voice='Mishnah',cond=['second set of three public fasts'])
for k,t,meaning in [('work','במלאכה','work'),('bathing','ברחיצה','bathing'),('anointing','בסיכה','anointing'),('sandals','בנעילת הסנדל','sandal wearing'),('intercourse','בתשמיש המטה','sexual intercourse')]:
 c('prohibit.'+k,'12b:9','ואסורין במלאכה וברחיצה ובסיכה ובנעילת הסנדל ובתשמיש המטה','The Mishnah prohibits '+meaning+'.',voice='Mishnah',cond=['second set of three public fasts'])
C=c('bathhouses','12b:9','ונועלין את המרחצאות','The bathhouses are closed.',voice='Mishnah',cond=['second set of three public fasts'])
D=c('seven','12b:10',ix['12b:10']['text'].split('הרי אלו')[0],'After these pass without response, seven further fasts bring the public total to thirteen.',voice='Mishnah',cond=['second set also unanswered'],comp='composite')
E=c('alarm','12b:10','שבאלו מתריעין','The last seven include sounding an alarm.',voice='Mishnah',cond=['last seven fasts'])
F=c('shops','12b:10','ונועלין את החנויות','The shops are closed in these later fasts.',voice='Mishnah',cond=['last seven fasts'])
G=c('monday','12b:10','בשני מטין עם חשיכה','On Monday the shops may be opened partly toward dark.',voice='Mishnah',cond=['Monday','toward dark'],unc=['מטין paraphrased as partial opening; detailed shop geometry not supplied.'])
H=c('thursday','12b:10','ובחמישי מותרין מפני כבוד השבת','On Thursday opening is permitted out of honor for the Sabbath.',voice='Mishnah',cond=['Thursday before Sabbath']);e('shops.exception1','12b:10','בשני מטין עם חשיכה',G,F,'qualification');e('shops.exception2','12b:10','ובחמישי מותרין מפני כבוד השבת',H,F,'qualification')
I=c('reduced.activity','12b:11','עברו אלו ולא נענו ממעטין במשא ומתן בבנין ובנטיעה באירוסין ובנישואין ובשאילת שלום בין אדם לחבירו כבני אדם הנזופין למקום','If these also pass unanswered, commerce, building, planting, betrothal, marriage and greetings are reduced, like people rebuked by God.',voice='Mishnah',cond=['all public fasts passed unanswered'],comp='composite',status='explicit list preserved; no individual binary choices inferred')
J=c('individuals','12b:11','היחידים חוזרין ומתענין עד שיצא ניסן','Individuals resume fasting until Nisan ends.',voice='Mishnah',cond=['after public series','before end of Nisan'])
K=c('late.rain','12b:11','יצא ניסן וירדו גשמים סימן קללה','Rain after Nisan ends is a sign of a curse.',voice='Mishnah',cond=['Nisan has ended'])
L=c('harvest.verse','12b:11',"שנא' (שמואל א יב, יז) הלא קציר חטים היום וגו':",'The Mishnah cites the wheat-harvest verse of I Samuel 12:17.',voice='Mishnah quoting Scripture',status='abbreviated quotation, continuation not fabricated');e('late.rain.support','12b:11',ix['12b:11']['text'],L,K)
M=c('pleasure','12b:12','בשלמא כולהו אית בהו תענוג רחיצה וסיכה ותשמיש המטה','The discussion regards bathing, anointing and intercourse as pleasurable.',comp='composite')
Mq=q('work.q','12b:12','אבל מלאכה צער הוא','Why prohibit work when it involves discomfort rather than pleasure?')
N=c('assembly.analogy','12b:12','אמר רב חסדא אמר רב ירמיה בר אבא אמר קרא (יואל א, יד) קדשו צום קראו עצרה אספו זקנים כעצרת מה עצרת אסור בעשיית מלאכה אף תענית אסור בעשיית מלאכה','Rav Yirmeya bar Abba, transmitted by Rav Hisda, uses Joel’s עצרה to analogize the fast to a solemn festival assembly whose work is prohibited.',who='Rav Yirmeya bar Abba',chain=['Rav Hisda','Rav Yirmeya bar Abba'],comp='composite');e('work.answer','12b:12',ix['12b:12']['text'],N,Mq,'answer')
Oq=q('night.q','12b:13','אי מה עצרת מאורתא אף תענית נמי מאורתא','Should the analogy also begin the fast restriction at night like the festival?')
O=c('day.assembly','12b:13',"אמר רבי זירא לדידי מיפרשא לי מיניה דר' ירמיה בר אבא אמר קרא אספו זקנים דומיא דאסיפת זקנים מה אסיפת זקנים ביום אף צום נמי ביום",'Rabbi Zeira reports Yirmeya bar Abba’s explanation: assemble the elders makes the fast restriction daytime, like that assembly.',who='Rav Yirmeya bar Abba',chain=['Rabbi Zeira','Rav Yirmeya bar Abba'],cond=['work prohibition under discussion; not a general permission to eat at night'],comp='composite');e('night.answer','12b:13',ix['12b:13']['text'],O,Oq,'answer')
Pq=q('noon.q','12b:13','ואימא מטיהרא','Why not begin at noon?')
P1=c('huna.morning','12b:13','דאמר מצפרא כינופיא','Rav Huna states that the gathering begins in the morning.',who='Rav Huna',cond=['morning fast assembly'])
for z in P['records']:
 if z['id'] in [P1,P1+'.u',P1+'.a',P1+'.p']:z['evidence']=[ev('12b:13','מסייע ליה לרב הונא דאמר מצפרא כינופיא')]
P2=c('shisha.support','12b:13','אמר רב שישא בריה דרב אידי מסייע ליה לרב הונא','Rav Shisha son of Rav Idi identifies this as support for Rav Huna.',who='Rav Shisha son of Rav Idi');e('morning.support','12b:13',ix['12b:13']['text'],P2,P1);e('noon.answer','12b:13','דאמר מצפרא כינופיא',P1,Pq,'answer')
Qq=q('schedule.q','12b:14','היכי עבדי','How is the fast-day gathering conducted?')
Q=c('morning.affairs','12b:14','אמר אביי מצפרא עד פלגא דיומא מעיינינן במילי דמתא','Abaye says the morning until midday is spent investigating the town’s affairs.',who='Abaye',cond=['morning until midday'])
R=c('reading','12b:14','מכאן ואילך ריבעא דיומא קרינן בספרא ואפטרתא','Abaye’s schedule then assigns a quarter day to Torah and prophetic reading.',who='Abaye',cond=['following morning inquiry'])
S=c('mercy','12b:14','מכאן ואילך בעינן רחמי','The remainder is devoted to seeking mercy.',who='Abaye',cond=['after reading'])
for k,z in [('affairs',Q),('reading',R),('mercy',S)]:e('schedule.'+k,'12b:14',ix['12b:14']['text'],z,Qq,'answer')
T=c('nehemiah','12b:14',ix['12b:14']['text'][ix['12b:14']['text'].index('שנא'):],'The quoted Nehemiah verse assigns a quarter day to reading and a quarter to confession and prostration.',voice='Abaye citing Scripture',comp='composite');e('schedule.scripture','12b:14',ix['12b:14']['text'],T,R)
Uq=q('reverse.q','13a:1','איפוך אנא','Could the order of inquiry and prayer be reversed?')
U=c('ezra.order','13a:1',ix['13a:1']['text'],'The reply rejects reversal, citing gathering around Ezra and his rising at the evening offering to spread his hands to God.',comp='composite',status='accepted rejection of proposed reversal, not itself a rejected claim');e('reverse.answer','13a:1',ix['13a:1']['text'],U,Uq,'answer');e('schedule.order','13a:1',ix['13a:1']['text'],U,S)
refs=list(ix);refs=refs[refs.index('12b:9'):refs.index('13a:1')+1]
for k,title,first,last in [('public','Escalating public fasts and post-series restrictions','12b:9','12b:11'),('assembly','Work restriction and fast-day assembly schedule','12b:12','13a:1')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'12b:9':'Second three, previous-day eating, each five restrictions and bathhouse closing retained.','12b:10':'Seven/thirteen count, alarm, shops and Monday/Thursday exceptions retained.','12b:11':'All reduced activities and rebuke simile, individuals until Nisan, late-rain curse and verse retained.','12b:12':'Pleasure premise, work question, Hisda transmission and assembly analogy retained.','12b:13':'Night/noon objections, Zeira direct report and Shisha/Huna support retained.','12b:14':'Question, all three daily stages and scriptural rationale retained.','13a:1':'Proposed reversal and both Ezra citations retained as a rejected proposal and accepted answer.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial inventory refers only to represented local source-supported responses; no exhaustive choice set or task eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch025.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
