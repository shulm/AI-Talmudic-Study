"""Manual Mishnah18b14–19a11, continuation read through20a8."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','98227d0f36f0c69ce2c343bd7a69948d5335972435bd39b8b0e98b26bf3de725').replace('ta.resume008.','ta.resume038.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('rainfall.scope','18b:14','תעניות אלו האמור ברביעה ראשונה','The Mishnah situates the preceding fast order in the first rainfall.',voice='Mishnah',status='compact wording clarified by Rav Yehuda in19a13')
B=c('changed.crops','18b:14','אבל צמחים ששנו מתריעין עליהן מיד','Changed crops require immediate alarm.',voice='Mishnah',cond=['crops have changed'])
C=c('forty.day','18b:14','וכן שפסקו גשמים בין גשם לגשם ארבעים יום מתריעין עליהן מפני שהיא מכת בצורת','A forty-day interruption between rains requires alarm because it is a drought affliction.',voice='Mishnah',cond=['forty days between rains'])
D=c('partial.rain','18b:15','ירדו לצמחין אבל לא ירדו לאילן לאילן ולא לצמחין לזה ולזה אבל לא לבורות לשיחין ולמערות מתריעין עליהן מיד','Immediate alarm applies when rain meets crop but not tree needs, tree but not crop needs, or both but not cistern/pit/cavern needs.',voice='Mishnah',comp='composite',cond=['any listed rain insufficiency'])
E=c('one.city','18b:15',"וכן עיר שלא ירדו עליה גשמים דכתיב (עמוס ד, ז) והמטרתי על עיר אחת ועל עיר אחת לא אמטיר חלקה אחת תמטר וגו'",'A city without rain is likewise addressed, citing Amos’s selective rain.',voice='Mishnah quoting Scripture')
F=c('dry.city','19a:1','אותה העיר מתענה ומתרעת וכל סביבותיה מתענות ולא מתריעות','The dry city fasts and sounds alarm; surrounding cities fast without alarm.',voice='Mishnah',comp='composite',cond=['city without rain'])
G=c('akiva.dry','19a:1','רבי עקיבא אומר מתריעות ולא מתענות','Rabbi Akiva says the surrounding cities sound alarm without fasting.',who='Rabbi Akiva',cond=['surroundings of city without rain']);e('dry.distinction','19a:1',ix['19a:1']['text'],G,F,'distinction')
H=c('plague.city','19a:1','וכן עיר שיש בה דבר או מפולת אותה העיר מתענה ומתרעת וכל סביבותיה מתענות ולא מתריעות','For plague or collapse, the affected city fasts and sounds alarm; its surroundings fast without alarm.',voice='Mishnah',comp='composite',cond=['city plague or collapse'])
I=c('akiva.plague','19a:1','רבי עקיבא אומר מתריעות ולא מתענות','Akiva says the surroundings of the plague/collapse city sound alarm without fasting.',who='Rabbi Akiva',cond=['surroundings of city with plague or collapse'])
# This repeated Akiva statement is the second occurrence, not the dry-city occurrence.
for z in P['records']:
 if z['id'] in [I,I+'.u',I+'.a',I+'.p']:
  t=ix['19a:1']['text'];a=t.rindex('רבי עקיבא');z['evidence']=[dict(segment_id=ix['19a:1']['id'],start_char=a,end_char=len(t),quote=t[a:])]
e('plague.distinction','19a:1',ix['19a:1']['text'],I,H,'distinction')
Iq=q('plague.definition.q','19a:2','איזהו דבר','What counts as plague?',voice='Mishnah')
J=c('plague.definition','19a:2',"עיר המוציאה חמש מאות רגלי ויצאו ממנה ג' מתים בג' ימים זה אחר זה הרי זה דבר פחות מכאן אין זה דבר",'For a city with five hundred footmen, three deaths over three consecutive days count as plague; fewer do not.',voice='Mishnah',comp='composite',cond=['city of five hundred footmen','three deaths over three consecutive days']);e('plague.definition.answer','19a:2',ix['19a:2']['text'],J,Iq,'answer')
K=c('spreading.afflictions','19a:3',ix['19a:3']['text'],'Alarm is sounded everywhere for blight, yellowing, locusts, hasil, dangerous beasts and sword because the affliction spreads.',voice='Mishnah',comp='composite',unc=['Enumerated composite, not atomic evaluation sample.'])
L=c('ashkelon','19a:4','מעשה שירדו זקנים מירושלים לעריהם וגזרו תענית על שנראה כמלא פי תנור שדפון באשקלון','Elders returning from Jerusalem decreed a fast for oven-mouth-sized blight seen at Ashkelon.',voice='Mishnah narrative')
M=c('wolves.children','19a:4','ועוד גזרו תענית על שאכלו זאבים שני תינוקות בעבר הירדן','They also decreed a fast because wolves ate two children across the Jordan.',voice='Mishnah narrative')
N=c('yosi.wolves','19a:4','רבי יוסי אומר לא על שאכלו אלא על שנראו:','Rabbi Yosi says the reason was the wolves being seen, not their eating the children.',who='Rabbi Yosi');e('wolves.correction','19a:4',ix['19a:4']['text'],N,M,'correction')
O=c('sabbath.emergencies','19a:5','על אלו מתריעין בשבת על עיר שהקיפוה נכרים או נהר ועל הספינה המיטרפת בים','Sabbath alarm applies to a city surrounded by non-Jews or a river and to a ship tossed at sea.',voice='Mishnah',comp='composite',cond=['Sabbath','listed emergencies'])
R=c('yosi.assistance','19a:5',"ר' יוסי אומר לעזרה ולא לצעקה",'Rabbi Yosi allows calling for assistance, not crying out.',who='Rabbi Yosi');e('sabbath.qualification','19a:5',ix['19a:5']['text'],R,O,'qualification')
S=c('shimon.plague','19a:5','שמעון התימני אומר אף על הדבר','Shimon the Timnite includes plague.',who='Shimon the Timnite',status='not accepted by Sages')
T=c('sages.refuse','19a:5','ולא הודו לו חכמים:','The Sages did not agree with Shimon.',voice='Sages collective');next(z for z in P['records'] if z['id']==T+'.a')['content'].update(surface='חכמים',role='collective',candidates=[]);e('plague.objection','19a:5',ix['19a:5']['text'],T,S,'objection')
U=c('excess.rain','19a:6','על כל צרה שלא תבא על הצבור מתריעין עליהן חוץ מרוב גשמים','Alarm is raised for any communal affliction except excessive rain.',voice='Mishnah',cond=['exception: excessive rain'])
V=c('honi.request','19a:6','מעשה שאמרו לו לחוני המעגל התפלל שירדו גשמים','People asked Honi the Circle Maker to pray for rain.',voice='Mishnah narrative')
W=c('honi.ovens','19a:6','אמר להם צאו והכניסו תנורי פסחים בשביל שלא ימוקו','Honi told them to bring in their Passover ovens so they would not dissolve.',who='Honi')
X=c('honi.initial','19a:6','התפלל ולא ירדו גשמים','Honi prayed, but rain did not fall.',voice='Mishnah narrative')
Xq=q('honi.did.q','19a:7','מה עשה','What did Honi do?',voice='Mishnah narrative')
Y=c('honi.circle','19a:7','עג עוגה ועמד בתוכה','He drew a circle and stood inside.',voice='Mishnah narrative');e('honi.did.answer','19a:7',ix['19a:7']['text'],Y,Xq,'answer')
Z=c('honi.oath','19a:7','ואמר לפניו רבש"ע בניך שמו פניהם עלי שאני כבן בית לפניך נשבע אני בשמך הגדול שאיני זז מכאן עד שתרחם על בניך','Honi says God’s children rely on him as a household intimate and swears not to move until mercy is shown.',who='Honi',comp='composite')
AA=c('drizzle','19a:7','התחילו גשמים מנטפין','Rain began to drip.',voice='Mishnah narrative')
AB=c('reservoir.request','19a:7','אמר לא כך שאלתי אלא גשמי בורות שיחין ומערות','Honi says he asked for rain filling cisterns, pits and caverns.',who='Honi')
AC=c('violent.rain','19a:7','התחילו לירד בזעף','Rain began to fall violently.',voice='Mishnah narrative')
AD=c('gentle.request','19a:7','אמר לא כך שאלתי אלא גשמי רצון ברכה ונדבה','Honi asks instead for rain of favor, blessing and generosity.',who='Honi');e('violent.qualification','19a:7',ix['19a:7']['text'],AD,AB,'qualification')
AE=c('rain.escape','19a:8','ירדו כתיקנן עד שיצאו ישראל מירושלים להר הבית מפני הגשמים','Rain fell properly until people left Jerusalem for the Temple Mount because of it.',voice='Mishnah narrative',comp='composite')
AF=c('stop.request','19a:8','באו ואמרו לו כשם שהתפללת עליהם שירדו כך התפלל שילכו להן','They asked Honi to pray for rain to stop as he had prayed for it to come.',voice='quoted unnamed people request')
AG=c('claimants.stone','19a:8','אמר להם צאו וראו אם נמחית אבן הטועין','Honi tells them to see whether the claimants’ stone has dissolved.',who='Honi',unc=['Response preserved without inferred unconditional rain-stop prayer.'])
AH=c('shimon.censure','19a:9','שלח לו שמעון בן שטח אלמלא חוני אתה גוזרני עליך נידוי','Shimon ben Shetah says that were he not Honi, he would decree excommunication.',who='Shimon ben Shetah',mode='conditional',cond=['counterfactual: not Honi'])
AI=c('shimon.favor','19a:9','אבל מה אעשה לך שאתה מתחטא לפני המקום ועושה לך רצונך כבן שהוא מתחטא על אביו ועושה לו רצונו','Shimon describes Honi’s intimacy with God as a child whose father fulfills his requests.',who='Shimon ben Shetah',comp='composite')
AJ=c('shimon.verse','19a:9','ועליך הכתוב אומר (משלי כג, כה) ישמח אביך ואמך ותגל יולדתך:','Shimon applies Proverbs23:25, parental rejoicing, to Honi.',who='Shimon ben Shetah');e('verse.support','19a:9',ix['19a:9']['text'],AJ,AI)
AK=c('sunrise.threshold','19a:10','היו מתענין וירדו להם גשמים קודם הנץ החמה לא ישלימו לאחר הנץ החמה ישלימו','If rain falls before sunrise during a fast, they do not complete it; after sunrise, they complete.',voice='Mishnah',comp='composite',cond=['rain during fast','sunrise threshold'])
AL=c('eliezar.noon','19a:10','ר"א אומר קודם חצות לא ישלימו לאחר חצות ישלימו','The printed R. Eliezer abbreviation gives noon as the completion threshold: before noon do not finish, after noon finish.',who='Rabbi Eliezer',comp='composite',cond=['rain during fast','noon threshold'],unc=['Source abbreviation ר"א retained; expanded identity provisional.']);e('threshold.distinction','19a:10',ix['19a:10']['text'],AL,AK,'distinction')
AM=c('lod.rain','19a:11','מעשה שגזרו תענית בלוד וירדו להם גשמים קודם חצות','At Lod a decreed fast was followed by rain before noon.',voice='Mishnah narrative')
AN=c('tarfon.instruction','19a:11',"אמר להם ר' טרפון צאו ואכלו ושתו ועשו יו\"ט",'Rabbi Tarfon instructed them to eat, drink and celebrate.',who='Rabbi Tarfon',comp='composite')
AO=c('lod.celebration','19a:11','ויצאו ואכלו ושתו ועשו יום טוב ובאו בין הערבים וקראו הלל הגדול:','They ate, drank and celebrated, then returned toward evening to recite the Great Hallel.',voice='Mishnah narrative',comp='composite')
refs=list(ix);refs=refs[refs.index('18b:14'):refs.index('19a:11')+1]
for k,title,first,last in [('distress','Mishnah: immediate alarms, spreading afflictions and Sabbath exceptions','18b:14','19a:5'),('honi','Excess rain exception and Honi narrative','19a:6','19a:9'),('rainfast','Rain during fast and Lod/Tarfon precedent','19a:10','19a:11')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'18b:14':'Rainfall scope, changed crops and forty-day interruption retained; Gemara clarification read.','18b:15':'All partial-rain categories, singled-out city and Amos evidence retained.','19a:1':'Dry-city and plague/collapse rules separately retained, including both distinct Akiva occurrences.','19a:2':'Definition question, population/death/day conditions and below-threshold exclusion retained.','19a:3':'All six spreading afflictions and geographic rationale retained as composite inventory.','19a:4':'Ashkelon blight, wolves/two children and Yosi corrected reason retained.','19a:5':'Sabbath emergencies, Yosi assistance qualification and Shimon plague/Sages rejection retained.','19a:6':'Excess-rain exclusion, Honi request, oven instruction and failed first prayer retained.','19a:7':'Narrative question, circle, oath, drizzle, violent rain and both revised requests retained.','19a:8':'Proper rainfall, Temple Mount escape, stop request and stone response retained.','19a:9':'Shimon ben Shetah conditional censure, child/father analogy and verse retained.','19a:10':'Sunrise and noon alternatives retained without final adjudication.','19a:11':'Lod rain, Tarfon instruction, celebration and evening Great Hallel retained.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local source response only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch038.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
