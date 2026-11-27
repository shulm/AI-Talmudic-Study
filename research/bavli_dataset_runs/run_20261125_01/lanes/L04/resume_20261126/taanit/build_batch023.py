"""Manual reading 11b:4–12a:4, full continuation through 12b:9 read."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','ab2c2bdc54e29f24ca6908f95c4920c3b28d2ee58ef2db9940318c766be6c936').replace('ta.resume008.','ta.resume023.').replace('/root/taanit_continuation_2','/root/taanit_continuation_3')
exec(compile(helper,__file__,'exec'))
add('mishnah.lemma','utterances','11b:4',dict(textual_voice='Mishnah lemma quoted by discussion',discourse_role='quoted lemma',composition='atomic'),"אוכלין ושותין משחשיכה כו':")
A=c('huna.night.eating','11b:4','אמר רבי זעירא אמר רב הונא יחיד שקיבל עליו תענית אפילו אכל ושתה כל הלילה למחר הוא מתפלל תפלת תענית','Rav Huna, transmitted by Rabbi Zeira, says one who accepted an individual fast says the fast prayer the next day even if he ate and drank all night.',who='Rav Huna',chain=['Rabbi Zeira','Rav Huna'],cond=['individual accepted a fast','even after eating/drinking all night'])
B=c('huna.overnight','11b:4','לן בתעניתו אינו מתפלל של תענית','One who remains overnight in his fast does not say the fast prayer.',who='Rav Huna',chain=['Rabbi Zeira','Rav Huna'],cond=['remained overnight in fast'],status='rule explained by Abaye’s prior-acceptance distinction below')
Cq=q('yosef.alternatives','11b:5','אמר רב יוסף מאי קסבר רב הונא סבירא ליה אין מתענין לשעות או דלמא מתענין לשעות והמתענה לשעות אינו מתפלל תפלת תענית','Rav Yosef asks whether Huna rejects fasting for hours or allows it while excluding the fast prayer.',who='Rav Yosef')
C=c('no.hourly.hypothesis','11b:5','סבירא ליה אין מתענין לשעות','Rav Yosef proposes that Huna may disallow fasting for hours.',who='Rav Yosef',mode='hypothetical',status='interpretive option subsequently rejected by Abaye')
D=c('hourly.no.prayer.hypothesis','11b:5','או דלמא מתענין לשעות והמתענה לשעות אינו מתפלל תפלת תענית','Alternatively, Huna may allow fasting for hours but not the fast prayer for such a fast.',who='Rav Yosef',mode='hypothetical',comp='composite',status='interpretive option subsequently rejected by Abaye')
E=c('abaye.hourly','11b:6','אמר ליה אביי לעולם קסבר רב הונא מתענין לשעות והמתענה לשעות מתפלל תפלת תענית','Abaye explains that Huna permits fasting for hours and saying the fast prayer.',who='Abaye',comp='composite',status='Abaye’s interpretation of Huna, not direct Huna quotation');e('yosef.answer','11b:6',ix['11b:6']['text'],E,Cq,'answer');e('hourly.correction','11b:6',ix['11b:6']['text'],E,C,'correction');e('prayer.correction','11b:6',ix['11b:6']['text'],E,D,'correction')
F=c('unaccepted.night','11b:6','ושאני הכא דאיכא שעות דליליא דלא קביל עליה מעיקרא','This case differs because it includes nighttime hours not accepted at the outset.',who='Abaye',cond=['nighttime hours not initially accepted']);e('night.explains','11b:6','ושאני הכא דאיכא שעות דליליא דלא קביל עליה מעיקרא',F,B,'qualification')
G=c('ukva.visit','11b:7','מר עוקבא איקלע לגינזק','Mar Ukva visited Ginzak.',voice='anonymous narrator',status='narrative setting')
Gq=q('ukva.hourly.q','11b:7','בעו מיניה מתענין לשעות או אין מתענין לשעות','They asked Mar Ukva whether fasting for hours is valid.',voice='unnamed Ginzak questioners')
G1=c('hourly.unknown','11b:7','לא הוה בידיה','Mar Ukva did not have an answer about hourly fasting.',voice='anonymous narrator',status='temporary knowledge gap, answered by academy later')
Hq=q('jars.q','11b:7','קנקנין של נכרים אסורין או מותרין','Are gentiles’ jars prohibited or permitted?',voice='unnamed Ginzak questioners')
H=c('jars.unknown','11b:7','לא הוה בידיה','He did not have an answer about the jars.',voice='anonymous narrator',status='temporary knowledge gap')
Iq=q('moses.garment.q','11b:7','במה שימש משה כל שבעת ימי המלואים','In what did Moses serve during the seven inauguration days?',voice='unnamed Ginzak questioners')
I=c('garment.unknown','11b:7','לא הוה בידיה','He did not have an answer about Moses’ garment.',voice='anonymous narrator',status='temporary knowledge gap')
# Each repeated no-answer occurrence is anchored separately.
text=ix['11b:7']['text'];starts=[];p=0
while True:
 p=text.find('לא הוה בידיה',p)
 if p<0:break
 starts.append(p);p+=1
for cid,a in zip([G1,H,I],starts):
 for z in P['records']:
  if z['id'] in [cid,cid+'.u',cid+'.a',cid+'.p']:z['evidence']=[dict(segment_id=ix['11b:7']['id'],start_char=a,end_char=a+len('לא הוה בידיה'),quote='לא הוה בידיה')]
J=c('academy.inquiry','11b:8','אזל ושאיל בי מדרשא','He went and asked at the study house.',voice='anonymous narrator',status='narrative inquiry')
K=c('academy.hourly','11b:8','אמרו ליה הלכתא מתענין לשעות ומתפללין תפלת תענית','They ruled that fasting for hours is valid and the fast prayer is said.',voice='unnamed academy respondents',comp='composite',status='explicit academy halakhic ruling');e('academy.hourly.answer','11b:8','אמרו ליה הלכתא מתענין לשעות ומתפללין תפלת תענית',K,Gq,'answer')
L=c('academy.jars','11b:8','והלכתא קנקנין של נכרים לאחר שנים עשר חדש מותרין','They ruled that gentiles’ jars are permitted after twelve months.',voice='unnamed academy respondents',cond=['twelve months elapsed'],status='explicit academy halakhic ruling');e('academy.jars.answer','11b:8','והלכתא קנקנין של נכרים לאחר שנים עשר חדש מותרין',L,Hq,'answer')
Mq=q('moses.garment.repeat','11b:8',"במה שימש משה כל ז' ימי המלואים",'In what did Moses serve during the seven inauguration days?',voice='question restated in academy report')
M=c('white.garment','11b:8','בחלוק לבן','The answer is a white tunic.',voice='unnamed academy respondents');e('academy.garment.answer','11b:8','בחלוק לבן',M,Iq,'answer');e('garment.repeat.answer','11b:8','בחלוק לבן',M,Mq,'answer')
N=c('kahana.variant','11b:8','רב כהנא מתני בחלוק לבן שאין לו אימרא','Rav Kahana transmits a white tunic without an אימרא.',who='Rav Kahana',status='alternative detailed transmission',unc=['אימרא retained; exact construction of the edging is not elaborated.']);e('kahana.qualifies','11b:8','רב כהנא מתני בחלוק לבן שאין לו אימרא',N,M,'qualification')
O=c('hisda.hourly','12a:1','הא דאמרת מתענין לשעות והוא שלא טעם כלום עד הערב','Rav Hisda qualifies hourly fasting: nothing must have been tasted until evening.',who='Rav Hisda',cond=['nothing tasted until evening'],status='named introduction on previous folio')
for z in P['records']:
 if z['id'] in [O,O+'.u',O+'.a',O+'.p']:z['evidence'].insert(0,ev('11b:9','אמר רב חסדא'))
e('hisda.qualifies','12a:1','הא דאמרת מתענין לשעות והוא שלא טעם כלום עד הערב',O,K,'qualification')
Oq=q('abaye.whole.q','12a:1','א"ל אביי הא תענית מעלייתא היא','Abaye objects that this is a full fast.',who='Abaye')
P1=c('changed.mind','12a:1','לא צריכא דאימלך אימלוכי','The reply explains that the person changed his mind to fast.',voice='anonymous reply',cond=['decision to fast made after abstention already underway'],unc=['Reply speaker unprinted; do not automatically make it Rav Hisda’s personal statement.']);e('changed.mind.answer','12a:1','לא צריכא דאימלך אימלוכי',P1,Oq,'answer');e('changed.mind.qualifies','12a:1','לא צריכא דאימלך אימלוכי',P1,O,'qualification')
Q=c('sunset.required','12a:2','ואמר רב חסדא כל תענית שלא שקעה עליו חמה לאו שמיה תענית','Rav Hisda says a fast on which the sun has not set is not called a fast.',who='Rav Hisda',cond=['sunset has not been reached'])
Qq=q('watch.challenge.q','12a:2','מיתיבי אנשי משמר מתענין ולא משלימין','An objection cites watch personnel fasting without completing the fast.')
R=c('watch.incomplete','12a:2','אנשי משמר מתענין ולא משלימין','The cited teaching has watch personnel fast without completing it.',voice='quoted teaching',cond=['watch personnel'],comp='composite');e('watch.objection','12a:2','מיתיבי אנשי משמר מתענין ולא משלימין',R,Q,'objection')
S=c('watch.affliction','12a:2','התם לצעורי נפשיה בעלמא הוא','The reply says that case is merely self-affliction.',status='distinction between self-affliction and full fast status');e('watch.answer','12a:2','התם לצעורי נפשיה בעלמא הוא',S,Qq,'answer');e('watch.qualifies','12a:2','התם לצעורי נפשיה בעלמא הוא',S,R,'qualification')
T=c('zadok.descent','12a:3','תא שמע דא"ר אליעזר (בן) צדוק אני מבני בניו של סנאב בן בנימין','Rabbi Eliezer (ben) Tzadok identifies himself as a descendant of Senaav ben Binyamin.',who='Rabbi Eliezer (ben) Tzadok',status='first-person lineage report',unc=['Printed parenthetical בן retained.'])
U=c('postponed.fast','12a:3','ופעם אחת חל ט\' באב להיות בשבת ודחינוהו לאחר השבת והתענינו בו ולא השלמנוהו','He recounts a Ninth of Av falling on Sabbath, postponed until after Sabbath; they fasted then without completing it.',who='Rabbi Eliezer (ben) Tzadok',comp='composite',cond=['Ninth of Av on Sabbath','fast postponed to following day'],status='reported historical occurrence')
V=c('family.festival','12a:3','מפני שיו"ט שלנו הוא','The reason given is that it was their festival.',who='Rabbi Eliezer (ben) Tzadok',cond=['their festival day'],unc=['Festival identified only as ours in this segment; no imported calendar detail.']);e('festival.reason','12a:3','מפני שיו"ט שלנו הוא',V,U);e('postponed.objection','12a:3',ix['12a:3']['text'],U,Q,'objection')
W=c('festival.affliction','12a:3','התם נמי לצעורי נפשיה בעלמא הוא','The reply again says this was only self-affliction.');e('festival.qualifies','12a:3','התם נמי לצעורי נפשיה בעלמא הוא',W,U,'qualification')
X=c('yohanan.until.home','12a:4','תא שמע דאמר רבי יוחנן אהא בתענית עד שאבוא לביתי','Rabbi Yohanan is cited as saying he will fast until arriving home.',who='Rabbi Yohanan',cond=['until arrival home'],status='reported declaration cited as challenge');e('home.objection','12a:4','תא שמע דאמר רבי יוחנן אהא בתענית עד שאבוא לביתי',X,Q,'objection')
Y=c('avoid.nasi','12a:4','התם לשמוטיה נפשיה מבי נשיאה הוא דעבד','The reply explains that he did this to extricate himself from the Nasi’s house.',voice='anonymous narrative explanation',status='limits evidentiary use of reported declaration');e('home.qualifies','12a:4','התם לשמוטיה נפשיה מבי נשיאה הוא דעבד',Y,X,'qualification')
refs=list(ix);refs=refs[refs.index('11b:4'):refs.index('12a:4')+1]
for k,title,first,last in [('hourly','Night eating, hourly fasting and academy answers','11b:4','12a:1'),('sunset','Sunset requirement and three apparent incomplete-fast counterexamples','12a:2','12a:4')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'11b:4':'Mishnah lemma, Zeira–Huna report and two overnight cases distinguished.','11b:5':'Yosef question and both proposed Huna interpretations retained as hypotheses.','11b:6':'Abaye rejects both alternatives and explains unaccepted night hours.','11b:7':'Ginzak visit, three separate questions and all three temporary knowledge gaps separately anchored.','11b:8':'Academy inquiry, both halakhic rulings with conditions, repeated garment question, white-tunic answer and Kahana variant retained.','11b:9':'Named Hisda introduction joined to exact next-folio proposition.','12a:1':'No-tasting condition, Abaye challenge and changed-mind explanation retained.','12a:2':'Sunset requirement, watch counterexample and self-affliction response retained.','12a:3':'Tzadok lineage, postponed fast event, family-festival reason and self-affliction response retained.','12a:4':'Yohanan declaration and narrator’s extrication explanation retained, with restricted inferential use.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial inventory represents only the locally supported answers included here; no exhaustive alternatives or choice-task eligibility claimed.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch023.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
