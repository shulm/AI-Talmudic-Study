"""Manual21b14–22a7 complete Abba and Broka narratives; following context22a12 read."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','dc45b950e867409e496bf4779682071e97a1d74369a1d2e574a4e475a4642915').replace('ta.resume008.','ta.resume045.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('heavenly.greetings','21b:14','אבא אומנא הוה אתי ליה שלמא ממתיבתא דרקיעא כל יומא ולאביי כל מעלי יומא דשבתא לרבא כל מעלי יומא דכיפורי','Heavenly greetings came daily to Abba the practitioner, weekly on Sabbath eve to Abaye, and on Yom Kippur eve to Rava.',voice='narrative',comp='composite')
B=c('abaye.distress','21b:14','הוה קא חלשא דעתיה דאביי משום דאבא אומנא','Abaye was distressed over Abba’s greater frequency of greetings.',voice='narrative')
C=c('abaye.response','21b:14','אמרו ליה לא מצית למיעבד כעובדיה','He is told he cannot perform Abba’s deeds.',voice='unnamed response',unc=['Source does not name the responding speaker.'])
Cq=q('abba.deeds.q','21b:15','ומאי הוו עובדיה דאבא אומנא','What were Abba’s deeds?')
D=c('patients.separate','21b:15','דכי הוה עביד מילתא הוה מחית גברי לחוד ונשי לחוד','When treating patients Abba placed men and women separately.',voice='narrative')
E=c('garment.privacy','21b:15','ואית ליה לבושא דאית ביה קרנא דהוות בזיעא כי כוסילתא כי הוות אתיא ליה איתתא הוה מלביש לה כי היכי דלא ניסתכל בה','He had a garment with an opening for treatment and clothed women in it so as not to look at them.',voice='narrative',comp='composite')
F=c('payment.privacy','21b:15','ואית ליה דוכתא דצניעא דשדי ביה פשיטי דשקיל דאית ליה שדי ביה דלית ליה לא מיכסיף','He provided a private place for payments so those unable to pay would not be embarrassed.',voice='narrative',comp='composite',cond=['able to pay versus unable']);e('abba.deeds.answer','21b:15',ix['21b:15']['text'],F,Cq,'answer')
G=c('scholar.support','21b:16','כי הוה אתרמי ליה צורבא מרבנן אגרא מיניה לא שקיל ובתר דקאי יהיב ליה פשיטי ואמר ליה זיל בריא נפשך','He took no fee from a scholar and gave money afterward to recuperate.',voice='narrative',comp='composite',cond=['scholar patient'])
H=c('abaye.test','21b:16','יומא חד שדר אביי זוגא דרבנן למיבדקיה','Abaye sent two scholars to test Abba.',voice='narrative')
I=c('abba.hospitality','21b:16','אותבינהו ואכלינהו ואשקינהו ומך להו ביסתרקי בליליא','Abba hosted them, fed and gave them drink, and spread bedding for the night.',voice='narrative',comp='composite')
J=c('bedding.taken','22a:1','לצפרא כרכינהו ושקלינהו וקמו ונפקו להו לשוקא ואשכחינהו','In the morning they took the bedding to the market, where Abba encountered them.',voice='narrative',comp='composite')
Jq=q('value.q','22a:1','א"ל לשיימיה מר היכי שוו','They ask him to assess the bedding’s value.',voice='two scholars')
K=c('value.reply','22a:1','א"ל הכי והכי','Abba gives a valuation, reported only as such and such.',who='Abba the practitioner');e('value.answer','22a:1',ix['22a:1']['text'],K,Jq,'answer')
Kq=q('higher.value.q','22a:1','א"ל ודלמא שוו טפי','They ask whether it might be worth more.',voice='two scholars')
L=c('purchase.price','22a:1','א"ל בהכי שקלינהו','Abba says he bought it for that amount.',who='Abba the practitioner');e('higher.value.answer','22a:1',ix['22a:1']['text'],L,Kq,'answer')
M=c('test.disclosure','22a:1','אמרו ליה דידך ניהו ושקלינהו מינך','They disclose that it is his and they took it.',voice='two scholars')
Mq=q('suspicion.q','22a:2','אמרו ליה במטותא מינך במאי חשדתינן','They ask what he suspected them of.',voice='two scholars')
N=c('favorable.inference','22a:2','א"ל אמינא פדיון שבויים איקלע להו לרבנן ואכסיפו למימר לי','Abba thought the scholars needed ransom money and were embarrassed to ask him.',who='Abba the practitioner',status='reported charitable interpretation, not established actual need');e('suspicion.answer','22a:2',ix['22a:2']['text'],N,Mq,'answer')
O=c('return.offer','22a:2','אמרו ליה השתא נשקלינהו מר','They offer that he take the bedding back.',voice='two scholars')
R=c('charity.release','22a:2','אמר להו מההוא שעתא אסחתינהו מדעתאי לצדקה','Abba says he had already relinquished it for charity.',who='Abba the practitioner')
S=c('rava.distress','22a:3','הוה קא חלשא דעתיה דרבא משום דאביי','Rava was distressed over Abaye’s more frequent greetings.',voice='narrative')
T=c('rava.protection','22a:3','אמרו ליה מסתייך דקא מגנית אכולה כרכא','He is told it is enough that he protects the entire city.',voice='unnamed response',unc=['Responding speaker not named.'])
U=c('broka.elijah','22a:4',"ר' ברוקא חוזאה הוה שכיח בשוקא דבי לפט הוה שכיח אליהו גביה",'Rabbi Broka Hozaa frequented Bei Lefet market, where Elijah visited him.',voice='narrative')
Uq=q('world.come.q','22a:4','א"ל איכא בהאי שוקא בר עלמא דאתי','Broka asks whether anyone in the market is destined for the world to come.',who='Rabbi Broka Hozaa')
V=c('elijah.no','22a:4','א"ל לא','Elijah initially says no.',who='Elijah',status='local initial answer before later people arrive');e('world.come.answer','22a:4',ix['22a:4']['text'],V,Uq,'answer')
W=c('jailer.appearance','22a:4','אדהכי והכי חזא לההוא גברא דהוה סיים מסאני אוכמי ולא רמי חוטא דתכלתא בגלימיה','A man appears wearing black shoes and lacking a tekhelet thread on his cloak.',voice='narrative',comp='composite')
X=c('jailer.eligible','22a:4','א"ל האי בר עלמא דאתי הוא','Elijah identifies this man as destined for the world to come.',who='Elijah')
Xq=q('work.first.q','22a:5','רהט בתריה א"ל מאי עובדך','Broka runs after him and asks his occupation.',who='Rabbi Broka Hozaa')
Y=c('return.tomorrow','22a:5','א"ל זיל האידנא ותא למחר','The man tells him to return tomorrow.',who='unnamed jailer');e('work.first.answer','22a:5',ix['22a:5']['text'],Y,Xq,'answer')
Yq=q('work.second.q','22a:5','למחר א"ל מאי עובדך','The next day Broka asks again about his occupation.',who='Rabbi Broka Hozaa')
Z=c('jailer.separation','22a:5','א"ל זנדוקנא אנא ואסרנא גברי לחוד ונשי לחוד ורמינא פורייאי בין הני להני כי היכי דלא ליתו לידי איסורא','He says he is a jailer, separates men and women, and puts his bed between them to prevent transgression.',who='unnamed jailer',comp='composite');e('work.second.answer','22a:5',ix['22a:5']['text'],Z,Yq,'answer')
AA=c('rescue.practice','22a:5','כי חזינא בת ישראל דיהבי נכרים עלה עינייהו מסרנא נפשאי ומצילנא לה','He risks himself to rescue a Jewish woman targeted by non-Jews.',who='unnamed jailer',cond=['Jewish woman targeted'])
AB=c('betrothed.rescue','22a:5','יומא חד הוות נערה מאורסה גבן דיהבו בה נכרים עינייהו שקלי דורדייא דחמרא ושדאי לה בשיפולה ואמרי דיסתנא היא','He recounts placing wine sediment on a targeted betrothed girl’s lower garment and claiming she was menstruating.',who='unnamed jailer',comp='composite',status='reported protective deception')
ABq=q('clothing.q','22a:6','א"ל מאי טעמא לית לך חוטי ורמית מסאני אוכמי','Broka asks why he lacks threads and wears black shoes.',who='Rabbi Broka Hozaa')
AC=c('disguise.purpose','22a:6','א"ל עיילנא ונפיקנא ביני נכרים כי היכי דלא לידעו דיהודאה אנא כי הוו גזרי גזירתא מודענא להו לרבנן ובעו רחמי ומבטלי לגזירתייהו','He conceals his Jewish identity among non-Jews to learn decrees, alert the rabbis, and enable prayers for their cancellation.',who='unnamed jailer',comp='composite');e('clothing.answer','22a:6',ix['22a:6']['text'],AC,ABq,'answer')
ACq=q('delay.q','22a:6','ומאי טעמא כי אמינא לך אנא מאי עובדך ואמרת לי זיל האידנא ותא למחר','Why did he postpone answering Broka until tomorrow?',who='Rabbi Broka Hozaa')
AD=c('urgent.decree','22a:6','א"ל בההיא שעתא גזרי גזירתא ואמינא ברישא איזיל ואשמע להו לרבנן דלבעי רחמי עלה דמילתא','A decree was being issued, so he prioritized notifying the rabbis to pray.',who='unnamed jailer');e('delay.answer','22a:6',ix['22a:6']['text'],AD,ACq,'answer')
AE=c('two.arrive','22a:7','אדהכי והכי אתו הנך תרי אתי א"ל הנך נמי בני עלמא דאתי נינהו','Two more arrive and Elijah identifies them too as destined for the world to come.',who='Elijah')
AEq=q('two.work.q','22a:7','אזל לגבייהו אמר להו מאי עובדייכו','Broka asks their occupation.',who='Rabbi Broka Hozaa')
AF=c('cheer.sad','22a:7','אמרו ליה אינשי בדוחי אנן מבדחינן עציבי','They say they are cheerful people who cheer the sad.',voice='two unnamed men collective')
AG=c('make.peace','22a:7','אי נמי כי חזינן בי תרי דאית להו תיגרא בהדייהו טרחינן ועבדינן להו שלמא:','They also describe working to reconcile two people in conflict.',voice='two unnamed men collective',cond=['two people in conflict'],unc=['אי נמי wording retained; no forced exclusion between practices.']);e('two.work.answer1','22a:7',ix['22a:7']['text'],AF,AEq,'answer');e('two.work.answer2','22a:7',ix['22a:7']['text'],AG,AEq,'answer')
for cid in [AF,AG]:next(z for z in P['records'] if z['id']==cid+'.a')['content'].update(surface='two unnamed men',role='collective',candidates=[])
refs=list(ix);refs=refs[refs.index('21b:14'):refs.index('22a:7')+1]
for k,title,first,last in [('abba','Abba’s practices, bedding test and heavenly greetings','21b:14','22a:3'),('broka','Broka/Elijah market, protective jailer and peacemakers','22a:4','22a:7')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'21b:14':'All three greeting frequencies, Abaye distress and unnamed response retained.','21b:15':'Deeds question, separate patients, privacy garment and confidential payment retained.','21b:16':'Scholar free treatment/recovery funds, Abaye test and hospitality retained.','22a:1':'Bedding removal, valuation question/reply, higher-value question/purchase-price reply and disclosure retained.','22a:2':'Suspicion question, favorable ransom inference, return offer and prior charitable release retained.','22a:3':'Rava distress and unnamed city-protection reply retained.','22a:4':'Broka/Elijah market question, initial no, man’s appearance and subsequent identification retained.','22a:5':'Both work questions, postponement, jailer separation, rescue practice and betrothed-girl protective deception retained.','22a:6':'Clothing and delayed-answer questions with distinct concealment/decree-notification explanations retained.','22a:7':'Two arrivals, Elijah identification, occupation question and cheering/peace practices retained.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local source response only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch045.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
