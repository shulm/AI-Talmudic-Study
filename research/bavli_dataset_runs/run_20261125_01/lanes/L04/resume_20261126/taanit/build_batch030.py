"""Manual reading chapter-two Mishnah 15a:4–15b:9; followup read through15b:15."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','152031c028cefa555c2488ab839929968c462dfe11aea270bb4cb513e70f22f2').replace('ta.resume008.','ta.resume030.').replace('/root/taanit_continuation_2','/root/taanit_continuation_4')
exec(compile(helper,__file__,'exec'))
Aq=q('order.q','15a:4','תעניות כיצד','How are the fasts conducted?',voice='Mishnah')
A=c('ark.out','15a:4','מוציאין את התיבה לרחובה של עיר','The ark is taken into the town square.',voice='Mishnah',cond=['public fast ritual; later Gemara limits to last seven'])
B=c('ashes.ark','15a:4','ונותנין אפר מקלה על גבי התיבה','Burnt ashes are placed on the ark.',voice='Mishnah')
C=c('ashes.leaders','15a:4','ובראש הנשיא ובראש אב בית דין','Ashes are placed on the heads of the nasi and court head.',voice='Mishnah',comp='composite')
D=c('ashes.each','15a:4','וכל אחד ואחד נותן בראשו','Each person puts ashes on his own head.',voice='Mishnah');e('order.answer','15a:4',ix['15a:4']['text'],A,Aq,'answer')
E=c('elder.rebuke','15a:5','הזקן שבהן אומר לפניהן דברי כבושין','The elder among them delivers admonition.',voice='Mishnah')
F=c('nineveh.deeds','15a:5','אחינו לא נאמר באנשי נינוה וירא אלהים את שקם ואת תעניתם אלא (יונה ג, י) וירא אלהים את מעשיהם כי שבו מדרכם הרעה','The prescribed exhortation contrasts sackcloth/fasting with Nineveh’s deeds and turning from evil as what God saw.',voice='prescribed elder speech quoting Jonah',comp='composite',status='ritual exhortation, not an identified historical speaker')
G=c('hearts','15a:5','ובקבלה הוא אומר (יואל ב, יג) וקרעו לבבכם ואל בגדיכם','The speech also quotes Joel’s call to rend hearts rather than garments.',voice='prescribed elder speech quoting Joel');e('rebuke.content','15a:5',ix['15a:5']['text'],F,E,'qualification');e('hearts.support','15a:5',ix['15a:5']['text'],G,F)
H=c('leader.qualities','15a:6','עמדו בתפלה מורידין לפני התיבה זקן ורגיל ויש לו בנים וביתו ריקם','For prayer they appoint an elderly, practiced leader with children and an empty home.',voice='Mishnah',cond=['prayer leader selection'],comp='composite',unc=['ביתו ריקם retained as empty home; later interpretation remains to be read.'])
I=c('wholehearted','15a:6','כדי שיהא לבו שלם בתפלה','These qualities aim at wholehearted prayer.',voice='Mishnah rationale');e('leader.reason','15a:6',ix['15a:6']['text'],I,H)
J=c('twentyfour','15a:7','ואומר לפניהן עשרים וארבעה ברכות י"ח שבכל יום ומוסיף עליהן עוד שש','The leader says twenty-four blessings: the daily eighteen plus six.',voice='Mishnah',comp='composite')
K=c('six.contents','15a:7',ix['15a:7']['text'][ix['15a:7']['text'].index('ואלו הן'):],'The six additions are remembrances, shofars and the cited Psalms120,121,130,102 passages.',voice='Mishnah',comp='composite',status='complete six-item inventory preserved with literal citations');e('six.explains','15a:7',ix['15a:7']['text'],K,J,'qualification')
L=c('yehuda.replacement','15a:8',ix['15a:8']['text'],'Rabbi Yehuda replaces remembrances and shofars with the famine/pestilence passage of I Kings8:37 and Jeremiah14:1 on droughts.',who='Rabbi Yehuda',comp='composite',status='alternative liturgical pair, other additions not disputed here');e('six.alternative','15a:8',ix['15a:8']['text'],L,K,'distinction')
# Every enumerated conclusion remains its own ritual-formula unit; biblical figures are invoked, not made contemporary speakers.
items=[('abraham','15a:9','על הראשונה הוא אומר','על השניה הוא אומר','First: invoke Abraham on Moriah; request an answer and hearing today; conclude Redeemer of Israel.'),('sea','15a:9','על השניה הוא אומר',None,'Second: invoke ancestors at the Sea; request an answer and hearing today; conclude Rememberer of forgotten things.'),('joshua','15a:10','על השלישית הוא אומר','על הרביעית הוא אומר','Third: invoke Joshua at Gilgal; request an answer and hearing today; conclude Hearer of alarm.'),('samuel','15a:10','על הרביעית הוא אומר','על החמישית הוא אומר','Fourth: invoke Samuel at Mizpah; request an answer and hearing today; conclude Hearer of cries.'),('elijah','15a:10','על החמישית הוא אומר',None,'Fifth: invoke Elijah at Carmel; request an answer and hearing today; conclude Hearer of prayer.'),('jonah','15a:11','על הששית הוא אומר','על השביעית הוא אומר','Sixth: invoke Jonah from the fish; request an answer and hearing today; conclude Answerer in distress.'),('david.solomon','15a:11','על השביעית הוא אומר',None,'Seventh: invoke David and his son Solomon in Jerusalem; request an answer and hearing today; conclude Merciful toward the land.')]
for key,ref,start,end,prop in items:
 text=ix[ref]['text'];text=text[text.index(start):text.index(end) if end else len(text)]
 c('formula.'+key,ref,text,prop,voice='Mishnah prescribed liturgical formula',comp='composite',status='ordered formula, not seven extra additions inferred')
M=c('halaphta.episode','15b:1',ix['15b:1']['text'].split('תקעו הכהנים')[0],'In the days of Rabbi Halafta and Rabbi Hananya ben Teradyon, a leader completed the blessing and the congregation did not answer amen.',voice='Mishnah narrator',comp='composite',status='narrative begins with מעשה on preceding folio')
for z in P['records']:
 if z['id'] in [M,M+'.u',M+'.a',M+'.p']:z['evidence'].insert(0,ev('15a:12'))
N=c('priests.blast','15b:1','תקעו הכהנים ותקעו','The prescribed call directs the priests to sound a blast.',voice='ritual call within narrative')
O=c('episode.abraham','15b:1',ix['15b:1']['text'][ix['15b:1']['text'].index('מי שענה את אברהם'):ix['15b:1']['text'].index('הריעו בני')],'The Abraham-at-Moriah invocation and request for today’s answer are recited.',voice='ritual speech within narrative',comp='composite')
P1=c('aaron.alarm','15b:1','הריעו בני אהרן הריעו','The call directs Aaron’s descendants to sound the alarm.',voice='ritual call within narrative')
P2=c('episode.sea','15b:1',ix['15b:1']['text'][ix['15b:1']['text'].index('מי שענה את אבותינו'):],'The ancestors-at-the-Sea invocation and request for today’s answer follow.',voice='ritual speech within narrative',comp='composite')
Q=c('sages.location','15b:2',ix['15b:2']['text'],'When the report reached the Sages, they restricted that practice to the eastern gate and Temple Mount.',voice='Sages collective',cond=['eastern gate and Temple Mount'],status='reported collective limitation');next(z for z in P['records'] if z['id']==Q+'.a')['content'].update(surface='חכמים',role='collective',candidates=[]);e('episode.scope','15b:2',ix['15b:2']['text'],Q,M,'qualification')
# Priestly rotation and daily family obligations: each group/stage has a distinct conditional claim.
for key,t,prop,cond in [
 ('y.first.watch','שלש תעניות הראשונות אנשי משמר מתענין ולא משלימין','In the first three, watch members fast without completing.',['first three','watch members']),
 ('y.first.family','ואנשי בית אב לא היו מתענין כלל','The daily family does not fast at all.',['first three','daily family']),
 ('y.middle.watch','שלש שניות אנשי משמר מתענין ומשלימין','In the middle three, watch members complete the fast.',['middle three','watch members']),
 ('y.middle.family','ואנשי בית אב מתענין ולא משלימין','The daily family fasts without completing.',['middle three','daily family']),
 ('y.last.both','שבע אחרונות אלו ואלו מתענין ומשלימין דברי רבי יהושע','In the last seven, both groups complete the fast.',['last seven','both groups'])]:
 cid=c(key,'15b:3',t,'Rabbi Yehoshua: '+prop,who='Rabbi Yehoshua',cond=cond)
 for z in P['records']:
  if z['id'] in [cid+'.a',cid+'.p']:z['evidence'].append(ev('15b:3','דברי רבי יהושע'))
for key,t,prop,cond in [
 ('s.first.both','שלש תעניות הראשונות אלו ואלו לא היו מתענין כלל','Neither group fasts in the first three.',['first three','both groups']),
 ('s.middle.watch','שלש שניות אנשי משמר מתענין ולא משלימין','Watch members fast without completion in the middle three.',['middle three','watch members']),
 ('s.middle.family','ואנשי בית אב לא היו מתענין כלל','The daily family does not fast at all.',['middle three','daily family']),
 ('s.last.watch','שבע אחרונות אנשי משמר מתענין ומשלימין','Watch members complete the last seven fasts.',['last seven','watch members']),
 ('s.last.family','ואנשי בית אב מתענין ולא משלימין','The daily family fasts without completion.',['last seven','daily family'])]:
 cid=c(key,'15b:4',t,prop,voice='Sages collective',cond=cond)
 z=next(z for z in P['records'] if z['id']==cid+'.a');z['content'].update(surface='חכמים',role='collective',candidates=[]);z['evidence'].append(ev('15b:4','וחכמים אומרים'))
R=c('watch.wine','15b:5','אנשי משמר מותרין לשתות יין בלילות אבל לא בימים','Watch members may drink wine at night but not during the day.',voice='Mishnah',cond=['watch members','night/day distinction'],comp='composite')
S=c('family.wine','15b:5','ואנשי בית אב לא ביום ולא בלילה','The daily family may drink wine neither day nor night.',voice='Mishnah',cond=['daily family'],comp='composite')
T=c('grooming','15b:5','אנשי משמר ואנשי מעמד אסורין מלספר ומלכבס','Watch and maamad members may not cut hair or launder.',voice='Mishnah',cond=['watch and maamad members'],comp='composite')
U=c('thursday.grooming','15b:5','ובחמישי מותרין מפני כבוד השבת','Thursday permits these acts for Sabbath honor.',voice='Mishnah',cond=['Thursday','Sabbath honor']);e('grooming.exception','15b:5','ובחמישי מותרין מפני כבוד השבת',U,T,'qualification')
V=c('scroll.eulogy','15b:6','כל הכתוב במגילת תענית דלא למספד לפניו אסור לאחריו מותר','For dates prohibiting eulogy in Megillat Taanit, the previous day is prohibited and the next permitted.',voice='Mishnah first opinion',cond=['date marked no eulogy'],comp='composite')
W=c('yosi.eulogy','15b:6','רבי יוסי אומר לפניו ולאחריו אסור','Rabbi Yosi prohibits both the preceding and following days.',who='Rabbi Yosi',cond=['date marked no eulogy'],comp='composite');e('eulogy.disagreement','15b:6',ix['15b:6']['text'],W,V,'distinction')
X=c('scroll.fast','15b:7','דלא להתענאה לפניו ולאחריו מותר','For dates marked no fasting, both adjacent days are permitted.',voice='Mishnah first opinion',cond=['date marked no fasting'],comp='composite')
Y=c('yosi.fast','15b:7',ix['15b:7']['text'][ix['15b:7']['text'].index("ר' יוסי"):],'Rabbi Yosi prohibits the preceding day but permits the following day.',who='Rabbi Yosi',cond=['date marked no fasting'],comp='composite');e('fast.disagreement','15b:7',ix['15b:7']['text'],Y,X,'distinction')
Z=c('no.thursday.start','15b:8','אין גוזרין תענית על הצבור בתחילה בחמישי שלא להפקיע השערים','A public fast series does not begin Thursday to avoid driving prices up.',voice='Mishnah',cond=['start of public fast series'])
AA=c('first.schedule','15b:8','אלא שלש תעניות הראשונות שני וחמישי ושני','The first three follow Monday, Thursday, Monday.',voice='Mishnah',cond=['first three'],comp='composite')
AB=c('second.schedule','15b:8','ושלש שניות חמישי שני וחמישי','The second three follow Thursday, Monday, Thursday.',voice='Mishnah',cond=['second three'],comp='composite')
AC=c('yosi.schedule','15b:8',ix['15b:8']['text'][ix['15b:8']['text'].index("ר' יוסי"):],'Rabbi Yosi extends the no-Thursday-start rule to the second and final groups.',who='Rabbi Yosi',cond=['start of any fast group'],comp='composite');e('schedule.disagreement','15b:8',ix['15b:8']['text'],AC,AB,'distinction')
AD=c('festival.no.decree','15b:9','אין גוזרין תענית על הצבור בראשי חדשים בחנוכה ובפורים','Public fasts are not decreed on new moons, Hanukkah or Purim.',voice='Mishnah',cond=['new moon/Hanukkah/Purim'],comp='composite')
AE=c('gamliel.started','15b:9','ואם התחילו אין מפסיקין דברי רבן גמליאל','Rabban Gamliel says that if the fast series began, it is not interrupted.',who='Rabban Gamliel',cond=['series already began','overlap with listed festive day'])
AF=c('meir.completion','15b:9','אמר רבי מאיר אף על פי שאמר רבן גמליאל אין מפסיקין מודה היה שאין משלימין','Rabbi Meir reports that although Gamliel says no interruption, he concedes the fast is not completed.',who='Rabban Gamliel',chain=['Rabbi Meir','Rabban Gamliel'],cond=['already-started series overlaps listed festive day'],status='Meir’s report of concession');e('completion.qualifies','15b:9',ix['15b:9']['text'],AF,AE,'qualification')
AG=c('av.friday','15b:9','וכן תשעה באב שחל להיות בערב שבת:','The same noncompletion applies when the Ninth of Av falls on Friday.',voice='Mishnah',cond=['Ninth of Av falls on Friday'],status='local Mishnah continuation; no later halakhic adjudication inferred')
refs=list(ix);refs=refs[refs.index('15a:4'):refs.index('15b:9')+1]
for k,title,first,last in [('ritual','Public fast procession, exhortation and prayer formulas','15a:4','15a:11'),('episode','Halafta/Hananya-era ritual and Sages’ location limitation','15a:12','15b:2'),('priests','Watch/family fast duties and wine/grooming limits','15b:3','15b:5'),('calendar','Scroll dates and fast scheduling','15b:6','15b:9')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'15a:4':'Order question, ark procession and all three ashes recipients retained.','15a:5':'Elder’s admonition, deeds rather than ritual contrast and Joel heart/garment contrast retained.','15a:6':'All four leader qualities and wholeheartedness rationale retained.','15a:7':'24=18+6 and all six passages retained as explicit composite inventory.','15a:8':'Yehuda replacement pair and both citations retained.','15a:9':'First and second formula: figure/place, petition, temporal scope and conclusion retained individually.','15a:10':'Third/fourth/fifth complete formulas retained individually.','15a:11':'Sixth/seventh complete formulas retained individually.','15a:12':'Narrative marker linked to following folio; no invented independent claim.','15b:1':'Narrative names, no amen, priestly calls and repeated Abraham/Sea petitions retained.','15b:2':'Sages collective and eastern gate/Temple Mount limitation retained.','15b:3':'Yehoshua complete five-cell watch/family stage inventory retained.','15b:4':'Sages contrasting five-cell stage inventory retained.','15b:5':'Both wine schedules, grooming groups and Thursday exception retained.','15b:6':'No-eulogy adjacent days and Yosi dissent retained.','15b:7':'No-fast adjacent days and Yosi dissent retained.','15b:8':'No Thursday start and price rationale, both schedules and Yosi extension retained.','15b:9':'All festive dates, Gamliel continuation, Meir-reported noncompletion and Friday Ninth of Av retained.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial inventory is the represented local ritual response, not an exhaustive choice set; no task eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch030.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
