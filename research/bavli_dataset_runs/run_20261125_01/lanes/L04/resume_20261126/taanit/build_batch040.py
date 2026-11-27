"""Manual19b15–20a8; next complete reed narrative read through20b3."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','0cafee66208c7fec1200a39f635e2c22b6c470f5104c321cd05d3731f0e3ac3f').replace('ta.resume008.','ta.resume040.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('pilgrim.shortage','19b:15','ת"ר פעם אחת עלו כל ישראל לרגל לירושלים ולא היה להם מים לשתות','A baraita relates that the pilgrims at Jerusalem lacked drinking water.',voice='baraita narrative')
B=c('nakdimon.contract','19b:15','הלך נקדימון בן גוריון אצל אדון אחד אמר לו הלויני שתים עשרה מעיינות מים לעולי רגלים ואני אתן לך שתים עשרה עינות מים ואם איני נותן לך הריני נותן לך שתים עשרה ככר כסף וקבע לו זמן','Nakdimon ben Guryon asked a lord to lend twelve springs of water for pilgrims, promising equivalent water or twelve talents of silver by a fixed time.',who='Nakdimon ben Guryon',comp='composite',cond=['water repayment by deadline','otherwise twelve silver talents'])
C=c('deadline.dry','19b:16','כיון שהגיע הזמן ולא ירדו גשמים','The deadline arrived without rain.',voice='baraita narrative')
# Three separately evidenced demand/reply occurrences, not collapsed into one.
t=ix['19b:16']['text']
for k,start,end,desc in [('morning','בשחרית','בצהרים','morning'),('noon','בצהרים','במנחה','noon'),('afternoon','במנחה','לגלג','afternoon')]:
 a=t.index(start);b=t.index(end);chunk=t[a:b];demand=chunk[:chunk.index('שלח לו עדיין')];reply=chunk[chunk.index('שלח לו עדיין'):]
 cid=c(k+'.demand','19b:16',demand,'At '+desc+' the lord demands either water or the money owed.',who='unnamed lord')
 rid=c(k+'.reply','19b:16',reply,'Nakdimon replies that time remains in the day.',who='Nakdimon ben Guryon')
 # index() alone would return earlier repeated replies; bind actual occurrence offsets.
 for key,aa,bb in [(cid,a,a+len(demand)),(rid,a+len(demand),b)]:
  for z in P['records']:
   if z['id'] in [key,key+'.u',key+'.a',key+'.p']:z['evidence']=[dict(segment_id=ix['19b:16']['id'],start_char=aa,end_char=bb,quote=t[aa:bb])]
D=c('lord.mockery','19b:16','לגלג עליו אותו אדון אמר כל השנה כולה לא ירדו גשמים','The lord mocks the expectation of rain now when none had fallen all year.',who='unnamed lord')
for z in P['records']:
 if z['id'] in [D,D+'.u',D+'.a',D+'.p']:z['evidence'].append(ev('20a:1','ועכשיו ירדו גשמים'))
E=c('bath.temple','20a:1','נכנס לבית המרחץ בשמחה עד שהאדון נכנס בשמחתו לבית המרחץ נקדימון נכנס לבית המקדש כשהוא עצב נתעטף ועמד בתפלה','The lord joyfully enters the bath while distressed Nakdimon enters the Temple, wraps himself and prays.',voice='baraita narrative',comp='composite')
F=c('first.prayer','20a:2','אמר לפניו רבונו של עולם גלוי וידוע לפניך שלא לכבודי עשיתי ולא לכבוד בית אבא עשיתי אלא לכבודך עשיתי שיהו מים מצויין לעולי רגלים','Nakdimon says he acted for God’s honor, not his own or his family’s, to provide water for pilgrims.',who='Nakdimon ben Guryon',comp='composite')
G=c('rain.fulfillment','20a:2','מיד נתקשרו שמים בעבים וירדו גשמים עד שנתמלאו שתים עשרה מעינות מים והותירו','Clouds formed and rain filled the twelve springs with surplus.',voice='baraita narrative',comp='composite')
H=c('meeting','20a:3','עד שיצא אדון מבית המרחץ נקדימון בן גוריון יצא מבית המקדש כשפגעו זה בזה','The lord leaving the bath and Nakdimon leaving the Temple met.',voice='baraita narrative')
I=c('surplus.claim','20a:3','אמר לו תן לי דמי מים יותר שיש לי בידך','Nakdimon demands payment for the surplus water.',who='Nakdimon ben Guryon')
J=c('sunset.objection','20a:3','אמר לו יודע אני שלא הרעיש הקב"ה את עולמו אלא בשבילך אלא עדיין יש לי פתחון פה עליך שאוציא ממך את מעותיי שכבר שקעה חמה וגשמים ברשותי ירדו','The lord acknowledges the divine response for Nakdimon but claims money because the sun had set and the rain came under his ownership.',who='unnamed lord',comp='composite');e('payment.objection','20a:3',ix['20a:3']['text'],J,I,'objection')
K=c('second.prayer','20a:4','חזר ונכנס לבית המקדש נתעטף ועמד בתפלה ואמר לפניו רבונו של עולם הודע שיש לך אהובים בעולמך','Nakdimon returns to pray that God reveal beloved people in His world.',who='Nakdimon ben Guryon')
L=c('sun.appears','20a:4','מיד נתפזרו העבים וזרחה החמה','The clouds disperse and the sun shines.',voice='baraita narrative')
M=c('lord.concession','20a:4','באותה שעה אמר לו האדון אילו לא נקדרה החמה היה לי פתחון פה עליך שאוציא ממך מעותיי','The lord concedes that without the sun breaking through he would have had grounds to collect money.',who='unnamed lord',mode='conditional',cond=['counterfactual: sun had not broken through']);e('sunset.correction','20a:4',ix['20a:4']['text'],M,J,'correction')
N=c('buni.name','20a:4','תנא לא נקדימון שמו אלא בוני שמו','A teaching says his original name was Buni, not Nakdimon.',voice='anonymous teaching')
Nq=q('name.reason.q','20a:4','ולמה נקרא שמו נקדימון','Why was he called Nakdimon?')
O=c('name.reason','20a:4','שנקדרה חמה בעבורו','Because the sun broke through for him.');e('name.answer','20a:4',ix['20a:4']['text'],O,Nq,'answer')
R=c('three.sun','20a:5','תנו רבנן שלשה נקדמה להם חמה בעבורן משה ויהושע ונקדימון בן גוריון','A baraita lists Moses, Joshua and Nakdimon as three for whom the sun was advanced.',voice='baraita',comp='composite',unc=['Printed נקדמה wording retained alongside preceding נקדרה; no harmonization.'])
S=c('nakdimon.tradition','20a:5','בשלמא נקדימון בן גוריון גמרא','Nakdimon’s case is accepted on received account.')
T=c('joshua.verse','20a:5',"יהושע נמי קרא דכתיב (יהושע י, יג) וידם השמש וירח עמד וגו'",'Joshua’s case is based on Joshua10:13, the sun’s stillness and moon’s standing.');e('joshua.support','20a:5',ix['20a:5']['text'],T,R)
Tq=q('moses.basis.q','20a:5','אלא משה מנלן','What establishes Moses’ case?')
U=c('elazar.ahal','20a:6',ix['20a:6']['text'],'Rabbi Elazar compares אחל in Deuteronomy2:25 and Joshua3:7.',who='Rabbi Elazar',comp='composite');e('moses.answer1','20a:6',ix['20a:6']['text'],U,Tq,'answer')
V=c('shmuel.nahmani.tet','20a:7',ix['20a:7']['text'],'Rabbi Shmuel bar Nahmani compares תת in Deuteronomy2:25 and Joshua10:12.',who='Rabbi Shmuel bar Nahmani',comp='composite');e('moses.answer2','20a:7',ix['20a:7']['text'],V,Tq,'answer')
W=c('yohanan.context','20a:8',ix['20a:8']['text'],'Rabbi Yohanan derives it from the verse itself: the nations’ trembling before Moses occurred when the sun was advanced for him.',who='Rabbi Yohanan',comp='composite');e('moses.answer3','20a:8',ix['20a:8']['text'],W,Tq,'answer')
Wq=q('tremble.when.q','20a:8','אימתי רגזו וחלו מפניך','When did they tremble before you?',who='Rabbi Yohanan');e('tremble.answer','20a:8',ix['20a:8']['text'],W,Wq,'answer')
refs=list(ix);refs=refs[refs.index('19b:15'):refs.index('20a:8')+1]
for k,title,first,last in [('nakdimon','Nakdimon’s pilgrim water debt, rainfall and sun narrative','19b:15','20a:4'),('sun','Three sun cases and derivations for Moses','20a:5','20a:8')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'19b:15':'Pilgrim shortage, named borrower, twelve springs/talents and deadline conditions retained.','19b:16':'Dry deadline, all three time-specific demands/replies and mockery retained with exact repeated offsets.','20a:1':'Mockery continuation and contrasting bath/Temple entrances retained.','20a:2':'Prayer’s negated honor motives, pilgrim purpose and fulfilled surplus rain retained.','20a:3':'Meeting, surplus claim, lord acknowledgement and sunset counterclaim retained.','20a:4':'Second prayer, sunlight, concession, Buni name and name-reason question/answer retained.','20a:5':'Three names, Nakdimon tradition, Joshua verse and Moses question retained.','20a:6':'Elazar אחל analogy retained.','20a:7':'Shmuel bar Nahmani תת analogy retained.','20a:8':'Yohanan verse-context explanation and nested when-question retained.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local source response only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch040.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
