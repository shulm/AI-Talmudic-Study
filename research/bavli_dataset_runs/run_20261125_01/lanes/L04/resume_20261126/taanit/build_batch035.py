"""Manual pinned reading17a10–17b8, continuation through18a4."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','7e7df212d7cd42c7c916d7ac2bcbcfcde3b2d88f303c56afe4294a4b9f0d4680').replace('ta.resume008.','ta.resume035.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('grooming.rule','17a:10','אנשי משמר ואנשי מעמד אסורים לספר ולכבס ובחמישי מותרין מפני כבוד השבת','Watch and maamad members may not cut hair or launder, with Thursday allowed for Sabbath honor.',voice='quoted Mishnah',comp='composite',cond=['watch/maamad membership','Thursday exception'])
Aq=q('grooming.reason.q','17a:10','מאי טעמא','Why the grooming restriction?')
B=c('grooming.reason','17a:10',"אמר רבה בר בר חנה אמר ר' יוחנן כדי שלא יכנסו למשמרתם כשהן מנוולין",'Rabbi Yohanan explains that they should not enter their watch unkempt.',who='Rabbi Yohanan',chain=['Rabbah bar bar Hana','Rabbi Yohanan']);e('grooming.answer','17a:10',ix['17a:10']['text'],B,Aq,'answer')
C=c('king.daily','17a:11','ת"ר מלך מסתפר בכל יום','A baraita requires the king to cut hair daily.',voice='baraita',cond=['king'])
D=c('high.weekly','17a:11','כהן גדול מערב שבת לערב שבת','The high priest cuts hair each Sabbath eve.',voice='baraita',cond=['high priest'])
E=c('priest.monthly','17a:11','כהן הדיוט אחת לשלשים יום','An ordinary priest cuts hair once in thirty days.',voice='baraita',cond=['ordinary priest'])
Cq=q('king.reason.q','17a:11','מלך מסתפר בכל יום מ"ט','Why must the king cut hair daily?')
F=c('king.beauty','17a:11','אמר רבי אבא בר זבדא אמר קרא (ישעיהו לג, יז) מלך ביפיו תחזינה עיניך','Rabbi Abba bar Zavda cites seeing the king in his beauty as the reason.',who='Rabbi Abba bar Zavda');e('king.answer','17a:11',ix['17a:11']['text'],F,Cq,'answer');e('king.support','17a:11',ix['17a:11']['text'],F,C)
Dq=q('high.reason.q','17a:11','כהן גדול מע"ש לערב שבת מ"ט','Why does the high priest cut hair each Sabbath eve?')
G=c('watch.renewal','17a:11','אמר רב שמואל בר יצחק הואיל ומשמרות מתחדשות','Rav Shmuel bar Yitzhak explains that watches are renewed.',who='Rav Shmuel bar Yitzhak');e('high.answer','17a:11',ix['17a:11']['text'],G,Dq,'answer')
Eq=q('ordinary.basis.q','17a:12','כהן הדיוט אחת לשלשים יום מנלן','What establishes thirty days for an ordinary priest?')
H=c('pera.analogy','17a:12','אתיא פרע פרע מנזיר כתיב הכא (יחזקאל מד, כ) וראשם לא יגלחו ופרע לא ישלחו וכתיב התם (במדבר ו, ה) קדוש יהיה גדל פרע שער ראשו מה להלן שלשים אף כאן שלשים','The repeated pera in Ezekiel’s priest rule and Numbers’ nazir rule transfers the thirty-day period.',comp='composite');e('ordinary.answer','17a:12',ix['17a:12']['text'],H,Eq,'answer');e('ordinary.support','17a:12',ix['17a:12']['text'],H,E)
Hq=q('nazir.basis.q','17a:13','ונזיר גופיה מנלן','What establishes the nazir period itself?')
I=c('nazir.thirty','17a:13','אמר רב מתנה סתם נזירות שלשים יום','Rav Matna states that unspecified naziriteship lasts thirty days.',who='Rav Matna')
Iq=q('thirty.basis.q','17a:13','מנלן אמר קרא','What establishes the thirty-day count?',voice='anonymous derivation discussion')
J=c('numerical.yihyeh','17a:13','אמר קרא יהיה בגימטריא תלתין הוי','The numerical value of יהיה is thirty.',voice='scriptural derivation');e('thirty.answer','17a:13',ix['17a:13']['text'],J,Iq,'answer');e('nazir.answer','17a:13',ix['17a:13']['text'],I,Hq,'answer');e('thirty.support','17a:13',ix['17a:13']['text'],J,I)
Jq=q('no.growth.q','17a:13','א"ל רב פפא לאביי ודילמא ה"ק רחמנא לא לירבו כלל','Rav Pappa asks Abaye whether the verse prohibits any hair growth at all.',who='Rav Pappa')
K=c('word.order','17a:13','אמר ליה אי הוה כתב לא ישלחו פרע כדקאמרת השתא דכתיב ופרע לא ישלחו פרע ליהוי שלוחי הוא דלא לישלחו','Abaye distinguishes the actual word order: pera may exist, but further letting it grow is prohibited; the hypothetical reverse order would support Pappa.',who='Abaye',comp='composite');e('growth.answer','17a:13',ix['17a:13']['text'],K,Jq,'answer')
Kq=q('present.hair.q','17a:14','אי הכי אפילו האידנא נמי','Should the hair restriction then apply even nowadays?')
L=c('service.time','17a:14','דומיא דשתויי יין מה שתויי יין בזמן ביאה הוא דאסור שלא בזמן ביאה שרי אף הכא נמי','The initial reply compares wine: the restriction applies at entry for service and not outside that time; likewise hair.',status='initial answer challenged by present-wine prohibition',comp='composite');e('present.hair.answer','17a:14',ix['17a:14']['text'],L,Kq,'answer')
M=c('rabbi.repeat','17a:15','והתניא רבי אומר אומר אני כהנים אסורין לשתות יין לעולם אבל מה אעשה שתקנתו קלקלתו','Rabbi’s prohibition and paradoxical qualification are quoted again in objection.',who='Rabbi',comp='composite')
Mq=q('abaye.repeat.q','17a:15','ואמר אביי כמאן שתו האידנא כהני חמרא','Abaye’s question about whose view permits present priestly drinking is repeated.',who='Abaye')
N=c('abaye.repeat.answer','17b:1','כרבי','The repeated answer identifies Rabbi.',who='Abaye');e('abaye.repeat.edge','17b:1','כרבי',N,Mq,'answer')
for z in P['records']:
 if z['id'] in [N,N+'.u',N+'.a',N+'.p']:z['evidence'].insert(0,ev('17a:15','ואמר אביי כמאן שתו האידנא כהני חמרא'))
O=c('sages.wine','17b:1','מכלל דרבנן אסרי','The discussion infers that the Sages prohibit present priestly drinking.',status='inferred premise of objection')
for z in P['records']:
 if z['id']==O:z['origin']='editorial_inference'
e('wine.objection','17b:1','מכלל דרבנן אסרי',O,L,'objection')
Oq=q('wine.reason.q','17b:1','מ"ט','Why do the Sages prohibit wine now?')
R=c('rebuild.readiness','17b:1','מהרה יבנה בית המקדש ובעינן כהן הראוי לעבודה וליכא','The Temple may soon be rebuilt, requiring a fit priest when none is available.',mode='conditional',cond=['Temple may be rebuilt soon']);e('wine.reason.answer','17b:1',ix['17b:1']['text'],R,Oq,'answer')
S=c('hair.remedy','17b:1','הכא אפשר דמספר ועייל','For hair, a priest can cut it and enter.');e('hair.distinction','17b:1',ix['17b:1']['text'],S,Kq,'answer');e('readiness.distinction','17b:1',ix['17b:1']['text'],S,R,'distinction')
Sq=q('wine.remedy.q','17b:2','אי הכי שתוי יין נמי אפשר דגני פורתא ועייל','Could a wine-drinking priest likewise sleep briefly and enter?')
T=c('wine.dispel','17b:2','כדרמי בר אבא דאמר רמי בר אבא דרך מיל ושינה כל שהוא מפיגין את היין','Rami bar Abba says a mil’s walk or any sleep dispels wine.',who='Rami bar Abba',comp='composite');e('wine.remedy.support','17b:2',ix['17b:2']['text'],T,Sq)
U=c('wine.volume','17b:2','לאו מי איתמר עלה אמר רב נחמן אמר רבה בר אבוה לא שנו אלא כששתה שיעור רביעית אבל שתה יותר מרביעית כל שכן שדרך מטרידתו ושינה משכרתו','Rabbah bar Avuh limits this to a reviit; with more, walking disturbs him and sleep increases drunkenness.',who='Rabbah bar Avuh',chain=['Rav Nahman','Rabbah bar Avuh'],comp='composite',cond=['reviit versus more than reviit']);e('wine.remedy.answer','17b:2',ix['17b:2']['text'],U,Sq,'answer');e('wine.volume.qualification','17b:2',ix['17b:2']['text'],U,T,'qualification')
V=c('ashi.distinction','17b:3',ix['17b:3']['text'],'Rav Ashi distinguishes wine, which invalidates service and was decreed against, from uncut hair, which does not invalidate service and was not.',who='Rav Ashi',comp='composite');e('ashi.present.answer','17b:3',ix['17b:3']['text'],V,Kq,'answer')
W=c('death.both','17b:4','מיתיבי ואלו שהן במיתה שתויי יין ופרועי ראש','A cited teaching lists wine drinkers and uncut-haired priests among those liable to death.',voice='baraita cited in objection',comp='composite');e('death.objection','17b:4',ix['17b:4']['text'],W,V,'objection')
X=c('wine.explicit','17b:4','בשלמא שתויי יין בהדיא כתיב בהו (ויקרא י, ט) יין ושכר אל תשת','The discussion accepts that wine liability is explicitly scriptural, citing Leviticus 10:9.')
Xq=q('hair.death.q','17b:4','אלא פרועי ראש מנלן','What establishes death liability for uncut hair?')
Y=c('death.analogy','17b:5',ix['17b:5']['text'],'Ezekiel’s adjacent hair and wine prohibitions compare uncut hair to wine for death liability.',comp='composite');e('hair.death.answer','17b:5',ix['17b:5']['text'],Y,Xq,'answer')
Yq=q('invalidate.q','17b:6','ומינה אי מה שתויי יין דמחלי עבודה אף פרועי ראש דמחלי עבודה','Should the same comparison also make uncut hair invalidate service?')
Z=c('death.only','17b:6','(לא כי איתקוש למיתה הוא דאיתקוש אבל לאחולי עבודה לא איתקוש)','The parenthetical reply restricts the comparison to death, excluding invalidation of service.',unc=['Parenthetical source wording retained.']);e('invalidate.answer','17b:6',ix['17b:6']['text'],Z,Yq,'answer');e('ashi.support','17b:6',ix['17b:6']['text'],Z,V)
Zq=q('pre.ezekiel.q','17b:7','א"ל רבינא לרב אשי הא מקמי דאתא יחזקאל מאן אמרה','Ravina asks Rav Ashi who stated this before Ezekiel.',who='Ravina')
AA=c('hisda.example','17b:7','הא דאמר רב חסדא דבר זה מתורת משה לא למדנו ומדברי קבלה למדנו (יחזקאל מד, ט) כל בן נכר ערל לב וערל בשר לא יבוא אל מקדשי (לשרתני)','Rav Ashi cites Rav Hisda’s statement that the exclusion of the uncircumcised stranger was learned from prophetic Scripture rather than Moses’ Torah.',who='Rav Hisda',chain=['Rav Ashi','Rav Hisda'],comp='composite')
ABq=q('example.pre.q','17b:7','הא מקמי דאתא יחזקאל מאן אמרה א"ל וליטעמיך','Rav Ashi’s counterquestion applies the same pre-Ezekiel problem to the cited exclusion.',who='Rav Ashi')
# Evidence for the counterquestion includes its framing and actual final repeated question, not a fabricated clause.
next(z for z in P['records'] if z['id']==ABq)['evidence']=[ev('17b:7')]
AB=c('received.law','17b:8','אלא גמרא גמיר לה ואתא יחזקאל ואסמכה אקרא הכא נמי גמרא גמיר לה ואתא יחזקאל ואסמכה אקרא','Rav Ashi answers that each law was received by tradition, and Ezekiel later attached it to Scripture.',who='Rav Ashi',comp='composite');e('pre.answer','17b:8',ix['17b:8']['text'],AB,Zq,'answer');e('example.pre.answer','17b:8',ix['17b:8']['text'],AB,ABq,'answer')
AC=c('tradition.limit','17b:8','(כי גמירי הלכה למיתה לאחולי עבודה לא גמירי):','The parenthetical qualification says the received law concerned death, not invalidation of service.',unc=['Parenthetical formulation retained.']);e('tradition.qualification','17b:8',ix['17b:8']['text'],AC,AB,'qualification');e('invalidity.support','17b:8',ix['17b:8']['text'],AC,V)
refs=list(ix);refs=refs[refs.index('17a:10'):refs.index('17b:8')+1]
for k,title,first,last in [('groom','Watch grooming and royal/priestly haircut schedules','17a:10','17a:13'),('readiness','Priestly present readiness, wine and hair liability versus service validity','17a:14','17b:8')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial inventory denotes represented source-supported local responses only, without exhaustive-choice eligibility.')
notes={'17a:10':'Rule, Thursday exception, reason question and Yohanan transmission retained.','17a:11':'All three haircut schedules and both reason questions/answers retained.','17a:12':'Ordinary-priest derivation question and two-verse analogy retained.','17a:13':'Nazir period and numeric derivation, Pappa question and Abaye word-order response retained.','17a:14':'Present restriction question and initial service-time analogy retained.','17a:15':'Rabbi repeated qualification and Abaye repeated question linked across folio.','17b:1':'Sages inference, reason question, rebuild-readiness answer and hair remedy retained.','17b:2':'Wine-sleep objection, Rami teaching and volume-conditioned Nahman transmission retained.','17b:3':'Ashi decree/service-invalidation distinction retained.','17b:4':'Death-liability objection, wine verse premise and hair derivation question retained.','17b:5':'Adjacent Ezekiel texts and death analogy retained.','17b:6':'Invalidation extension question and parenthetical exclusion retained.','17b:7':'Ravina question, Ashi counterexample, Hisda report and counterquestion retained.','17b:8':'Received-tradition answer and parenthetical death-only qualification retained.'}
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch035.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
