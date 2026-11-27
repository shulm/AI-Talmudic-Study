"""Manual21a15–21b13; continuation through22a12."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','23d58d1c3850ab253e5690f93e24651f1be70e9a948ea32406b35f3673b78aea').replace('ta.resume008.','ta.resume044.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('large.plague','21a:15','ת"ר עיר המוציאה חמש מאות ואלף רגלי כגון כפר עכו ויצאו הימנה תשעה מתים בשלשה ימים זה אחר זה הרי זה דבר','For a city of fifteen hundred footmen, such as Kefar Akko, nine deaths in three consecutive days constitute plague.',voice='baraita',cond=['1500 footmen','nine deaths','three consecutive days'])
B=c('large.exclusion','21a:16','ביום אחד או בד\' ימים אין זה דבר','The nine-death threshold in one or four days does not constitute plague.',voice='baraita',cond=['nine deaths in one or four days'])
C=c('small.plague','21a:16','ועיר המוציאה חמש מאות רגלי כגון כפר עמיקו ויצאו ממנה שלשה מתים בג\' ימים זה אחר זה הרי זה דבר','For five hundred footmen, such as Kefar Amiko, three deaths in three consecutive days constitute plague.',voice='baraita',cond=['500 footmen','three deaths','three consecutive days'])
D=c('small.exclusion','21b:1',ix['21b:1']['text'],'Three deaths in one or four days do not constitute plague.',voice='baraita',cond=['three deaths in one or four days'])
E=c('derokeret.fast','21b:2','דרוקרת עיר המוציאה חמש מאות רגלי הוה ויצאו ממנה שלשה מתים ביום אחד גזר רב נחמן בר רב חסדא תעניתא','Derokeret had five hundred footmen and three deaths in one day; Rav Nahman bar Rav Hisda decreed a fast.',voice='narrative',comp='composite')
Eq=q('nahman.whose.q','21b:2','אמר רב נחמן בר יצחק כמאן','Rav Nahman bar Yitzhak asks whose view this follows.',who='Rav Nahman bar Yitzhak')
F=c('meir.analogy','21b:2','כר"מ','Nahman bar Yitzhak identifies Rabbi Meir’s reasoning.',who='Rav Nahman bar Yitzhak')
for z in P['records']:
 if z['id'] in [F,F+'.u',F+'.a',F+'.p']:z['evidence'].insert(0,ev('21b:2','אמר רב נחמן בר יצחק כמאן'))
e('nahman.whose.answer','21b:2',ix['21b:2']['text'],F,Eq,'answer')
G=c('goring.inference','21b:3',ix['21b:3']['text'],'Meir reasons that if spaced gorings incur liability, closely spaced gorings all the more so.',who='Rabbi Meir',chain=['Rav Nahman bar Yitzhak','Rabbi Meir'])
for z in P['records']:
 if z['id'] in [G,G+'.u',G+'.a',G+'.p']:z['evidence'].insert(0,ev('21b:2','אמר רב נחמן בר יצחק כמאן כר"מ'))
e('goring.support','21b:3',ix['21b:3']['text'],G,F,'analogy')
H=c('invitation','21b:4','א"ל רב נחמן בר רב חסדא לרב נחמן בר יצחק ליקום מר ליתי לגבן','Nahman bar Rav Hisda invites Nahman bar Yitzhak to join him.',who='Rav Nahman bar Rav Hisda')
I=c('yosi.honor','21b:4','א"ל תנינא רבי יוסי אומר לא מקומו של אדם מכבדו אלא אדם מכבד את מקומו','Nahman bar Yitzhak quotes Yosi: a person honors his place, not the place the person.',who='Rabbi Yosi',chain=['Rav Nahman bar Yitzhak','Rabbi Yosi'])
J=c('sinai.proof','21b:4','שכן מצינו בהר סיני שכל זמן שהשכינה שרויה עליו אמרה תורה (שמות לד, ג) גם הצאן והבקר אל ירעו אל מול ההר ההוא נסתלקה שכינה ממנו אמרה תורה (שמות יט, יג) במשוך היובל המה יעלו בהר','Sinai’s restrictions applied while the divine presence rested there, but ascent was allowed upon its departure.',voice='quoted teaching continuation',comp='composite');e('sinai.support','21b:4',ix['21b:4']['text'],J,I)
K=c('tent.proof','21b:5',ix['21b:5']['text'],'Similarly the erected Tent of Meeting required exclusion of the afflicted; when curtains were rolled up, zavim and lepers could enter.',voice='quoted teaching continuation',comp='composite');e('tent.support','21b:5',ix['21b:5']['text'],K,I)
L=c('reverse.invitation','21b:6','אמר ליה אי הכי ניקום אנא לגבי מר','Nahman bar Rav Hisda proposes coming to Nahman bar Yitzhak instead.',who='Rav Nahman bar Rav Hisda')
M=c('ancestry.reply','21b:6','אמר ליה מוטב יבא מנה בן פרס אצל מנה בן מנה ואל יבא מנה בן מנה אצל מנה בן פרס','Nahman bar Yitzhak replies that a maneh son of a half-maneh should visit a maneh son of a maneh rather than the reverse.',who='Rav Nahman bar Yitzhak',comp='composite',unc=['Figurative ancestry comparison retained without external biographical expansion.'])
N=c('sura.exception','21b:7','בסורא הוות דברתא בשיבבותיה דרב לא הוות דברתא','Plague struck Sura but not Rav’s neighborhood.',voice='narrative')
O=c('rav.assumption','21b:7','סברו מיניה משום זכותיה דרב דנפיש','People attributed the protection to Rav’s great merit.',voice='unnamed people inference',status='initial attribution replaced by dream report')
R=c('burial.lender','21b:7','איתחזי להו בחילמא רב דנפישא זכותיה טובא הא מילתא זוטרא ליה לרב אלא משום ההוא גברא דשייל מרא וזבילא לקבורה','A dream says this was too small for Rav’s immense merit; protection was due to a man lending a hoe and shovel for burial.',voice='reported dream',comp='composite');e('rav.correction','21b:7',ix['21b:7']['text'],R,O,'correction')
S=c('fire.exception','21b:8','בדרוקרת הוות דליקתא ובשיבבותיה דרב הונא לא הוות דליקתא','Fire struck Derokeret but not Huna’s neighborhood.',voice='narrative')
T=c('huna.assumption','21b:8','סבור מינה בזכותא דרב הונא דנפיש','People attributed this to Rav Huna’s great merit.',voice='unnamed people inference',status='initial attribution replaced by dream report')
U=c('oven.lender','21b:8','איתחזי להו בחילמא האי זוטרא ליה לרב הונא אלא משום ההיא איתתא דמחממת תנורא ומשיילי לשיבבותיה','A dream attributes it instead to a woman heating her oven and lending it to neighbors, the event being too small for Huna.',voice='reported dream',comp='composite');e('huna.correction','21b:8',ix['21b:8']['text'],U,T,'correction')
V=c('locust.fast','21b:9','אמרו ליה לרב יהודה אתו קמצי גזר תעניתא','Rav Yehuda decrees a fast on a report of locusts arriving.',voice='narrative')
Vq=q('no.damage.q','21b:9','אמרו ליה לא קא מפסדן','People object that the locusts are not causing damage.',voice='unnamed people objection')
W=c('locust.provisions','21b:9','אמר להו זוודא אייתו בהדייהו','Rav Yehuda replies rhetorically that they have brought provisions with them.',who='Rav Yehuda',status='rhetorical response to no-damage objection, not factual insect luggage');e('locust.answer','21b:9',ix['21b:9']['text'],W,Vq,'answer')
X=c('pig.fast','21b:10','אמרו ליה לרב יהודה איכא מותנא בחזירי גזר תעניתא','Rav Yehuda decrees a fast after reports of pig mortality.',voice='narrative')
Xq=q('species.q','21b:10','נימא קסבר רב יהודה מכה משולחת ממין אחד משולחת מכל המינין','Does this imply Yehuda thinks an affliction in one species affects every species?')
Y=c('pigs.special','21b:10','לא שאני חזירי דדמיין מעייהו לבני אינשי','No: pigs are different because their intestines resemble humans’.',status='source’s explanatory comparison, no modern medical claim');e('species.answer','21b:10',ix['21b:10']['text'],Y,Xq,'answer')
Z=c('shmuel.hozai','21b:11','אמרו ליה לשמואל איכא מותנא בי חוזאי גזר תעניתא','Shmuel decrees a fast on a report of mortality in Bei Hozai.',voice='narrative')
Zq=q('distance.q','21b:11','א"ל והא מרחק','But is it not distant?',voice='unnamed interlocutor')
AA=c('shmuel.barrier','21b:11','אמר ליכא מעברא הכא דפסיק ליה','Shmuel says no crossing barrier here interrupts it.',who='Shmuel',unc=['Compact מעברא wording retained without imposing transmission mechanism.']);e('distance.answer','21b:11',ix['21b:11']['text'],AA,Zq,'answer')
AB=c('israel.fast','21b:12','אמרו ליה לרב נחמן איכא מותנא בארעא דישראל גזר תעניתא','Rav Nahman decrees a fast on news of mortality in the Land of Israel.',voice='narrative')
AC=c('mistress.servant','21b:12','אמר אם גבירה לוקה שפחה לא כל שכן','Nahman reasons that if the mistress is stricken, all the more the maidservant.',who='Rav Nahman',mode='conditional',cond=['mistress stricken']);e('israel.fast.reason','21b:12',ix['21b:12']['text'],AC,AB)
ACq=q('servant.servant.q','21b:13','טעמא דגבירה ושפחה הא שפחה ושפחה לא והא אמרו ליה לשמואל איכא מותנא בי חוזאי גזר תעניתא','Does this limit concern to mistress/servant rather than two servant regions, despite Shmuel’s Bei Hozai fast?')
AD=c('caravans','21b:13','שאני התם כיון דאיכא שיירתא דלווי ואתיא בהדיה','That case differs because caravans accompany and bring it along.');e('caravans.answer','21b:13',ix['21b:13']['text'],AD,ACq,'answer');e('hozai.qualification','21b:13',ix['21b:13']['text'],AD,AA,'qualification')
refs=list(ix);refs=refs[refs.index('21a:15'):refs.index('21b:13')+1]
for k,title,first,last in [('plague','Plague thresholds, Derokeret fast and Meir analogy','21a:15','21b:3'),('honor','Nahman invitation and place/honor teaching','21b:4','21b:6'),('protection','Neighborhood protection dream attributions','21b:7','21b:8'),('spread','Locust, animal and distant mortality fasts','21b:9','21b:13')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'21a:15':'1500-footmen/nine-deaths/three-day threshold and Kefar Akko example retained.','21a:16':'Large-city one/four-day exclusion and smaller-city threshold/example retained.','21b:1':'Small-city one/four-day exclusion retained across folio.','21b:2':'Derokeret actual fast, two Nahmans distinct and Meir identification retained.','21b:3':'Meir goring analogy retained across folio with transmission.','21b:4':'Invitation, Yosi honor principle and Sinai conditions/verses retained.','21b:5':'Tent erected/curtains rolled conditions and affected entrants retained.','21b:6':'Reversed invitation and figurative pedigree response retained.','21b:7':'Sura exception, initial Rav-merit assumption and dream burial-lender correction retained.','21b:8':'Derokeret fire exception, initial Huna-merit assumption and oven-lender correction retained.','21b:9':'Locust fast, no-damage objection and rhetorical provisions answer retained.','21b:10':'Pig-mortality fast, all-species inference question and pig-specific rejection retained.','21b:11':'Shmuel Bei Hozai fast, distance objection and barrier reply retained.','21b:12':'Nahman Israel fast and mistress/servant inference retained.','21b:13':'Servant-region objection and caravan distinction retained.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local source response only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch044.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
