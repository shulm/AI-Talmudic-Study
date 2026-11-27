"""Manual reading17b9–18a8; continuation read through19a2."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','58ffbf749866312c4a58d4bf8ab369886081906a1b37f7b574a04161befd9c15').replace('ta.resume008.','ta.resume036.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('mishnah.days','17b:9','כל הכתוב במגילת תענית דלא למיספד לפניו אסור לאחריו מותר','The quoted Mishnah prohibits the day before a no-eulogy Megillat Taanit date, permitting the day after.',voice='quoted Mishnah',comp='composite')
B=c('calendar.preface','17b:9','תנו רבנן אלין יומיא דלא להתענאה בהון ומקצתהון דלא למיספד בהון','The baraita introduces days without fasting, some also without eulogy.',voice='baraita',comp='composite')
C=c('tamid.dates','17b:9','מריש ירחא דניסן ועד תמניא ביה איתוקם תמידא דלא למיספד בהון','From Nisan’s first day through its eighth, the tamid was established: eulogy is prohibited.',voice='baraita',cond=['Nisan1–8'])
D=c('shavuot.dates','17b:9','מתמניא ביה עד סוף מועדא איתותב חגא דשבועיא דלא למיספד בהון','From the eighth through the end of the festival, the Shavuot festival was established: eulogy is prohibited.',voice='baraita',cond=['Nisan8 through end of festival'])
Cq=q('first.day.q','17b:10','למה לי מריש ירחא לימא מתרי בניסן ור"ח גופיה יו"ט הוא ואסור','Why include Nisan1 rather than start on Nisan2, since new moon is already prohibited?')
E=c('rav.before','17b:10','אמר רב לא נצרכה אלא לאסור יום שלפניו','Rav says the inclusion prohibits the preceding day.',who='Rav');e('first.answer','17b:10',ix['17b:10']['text'],E,Cq,'answer')
Eq=q('newmoon.before.q','17b:11','ושלפניו נמי תיפוק ליה דהוה ליה יום שלפני ראש חדש','Would the preceding day not already be prohibited as the day before new moon?')
F=c('torah.strength','17b:11',"ר\"ח דאורייתא הוא ודאוריית' לא בעי חיזוק",'New moon is scriptural, and scriptural law needs no reinforcement.');e('newmoon.answer','17b:11',ix['17b:11']['text'],F,Eq,'answer')
G=c('calendar.adjacent','17b:12','דתניא הימים האלה הכתובין במגילת תענית לפניהם ולאחריהם אסורין','A baraita prohibits the days before and after the listed Megillat Taanit dates.',voice='baraita',comp='composite')
H=c('sabbath.adjacent','17b:12','שבתות וימים טובים הן אסורין לפניהן ולאחריהן מותרין','Sabbaths and festivals themselves are prohibited, with preceding and following days permitted.',voice='baraita',comp='composite')
Hq=q('difference.q','17b:12','ומה הפרש בין זה לזה','What explains the difference?',voice='baraita')
I=c('authority.distinction','17b:12','הללו דברי תורה ודברי תורה אין צריכין חיזוק הללו דברי סופרים ודברי סופרים צריכין חיזוק','Scriptural observances need no reinforcement; scribal ones do.',voice='baraita',comp='composite');e('difference.answer','17b:12',ix['17b:12']['text'],I,Hq,'answer');e('reinforcement.support','17b:12',ix['17b:12']['text'],I,F)
Iq=q('festival.end.q','17b:13','למה לי עד סוף מועד לימא עד המועד ומועד גופיה יום טוב הוא ואסור','Why extend through the festival’s end, since the festival is already prohibited?')
J=c('pappa.after','18a:1','אלא לאסור יום שלפניו ה"נ לא נצרכה אלא לאסור יום שלאחריו','Rav Pappa parallels Rav’s preceding-day explanation by applying it to the day after the festival.',who='Rav Pappa',chain=['Rav Pappa'],comp='composite')
for z in P['records']:
 if z['id'] in [J,J+'.u',J+'.a',J+'.p']:z['evidence'].insert(0,ev('17b:13','אמר רב פפא כדאמר רב לא נצרכא'))
e('festival.end.answer','18a:1',ix['18a:1']['text'],J,Iq,'answer')
Jq=q('whose.q','18a:1','כמאן','Whose view does this follow?')
K=c('yosi.both','18a:1','כרבי יוסי דאמר בין לפניו בין לאחריו אסור','The discussion identifies Rabbi Yosi, who prohibits before and after.',who='Rabbi Yosi',comp='composite');e('whose.answer','18a:1',ix['18a:1']['text'],K,Jq,'answer')
Kq=q('twentynine.q','18a:1','אי הכי בעשרים ותשעה נמי מאי איריא דהוי יומא דמקמי יומא דמיתוקם תמידא תיפוק ליה דה"ל יומא דבתר עשרין ותמניא ביה','Why explain the twenty-ninth by the following tamid day when it is also after the twenty-eighth?')
L=c('good.news','18a:2',"דתניא בעשרים ותמני' ביה אתת בשורתא טבתא ליהודאי דלא יעידון מן אורייתא",'A baraita marks the twenty-eighth as good news that Jews would not be removed from Torah.',voice='baraita narrative')
M=c('decrees','18a:2','שפעם אחת נגזרה גזירה על ישראל שלא יעסקו בתורה ושלא ימולו את בניהם ושיחללו שבתות','A decree prohibited Torah study and circumcision and demanded Sabbath desecration.',voice='baraita narrative',comp='composite')
Mq=q('yehuda.did.q','18a:2','מה עשה יהודה בן שמוע וחביריו','What did Yehuda ben Shamua and his companions do?',voice='baraita narrative')
N=c('consultation','18a:2','הלכו ונטלו עצה ממטרוניתא אחת שכל גדולי רומי מצויין אצלה','They consulted a matron frequented by Rome’s prominent people.',voice='baraita narrative');e('yehuda.did.answer','18a:2',ix['18a:2']['text'],N,Mq,'answer')
O=c('matron.advice','18a:3','אמרה להם עמדו והפגינו בלילה','The matron advises them to protest at night.',who='unnamed matron')
R=c('night.protest','18a:3','הלכו והפגינו בלילה','They went and protested at night.',voice='baraita narrative')
Rq=q('kinship.protest.q','18a:3','אמרו אי שמים לא אחים אנחנו לא בני אב אחד אנחנו לא בני אם אחת אנחנו מה נשתנינו מכל אומה ולשון שאתם גוזרין עלינו גזירות רעות','The protesters rhetorically invoke shared kinship and ask why they are singled out for harmful decrees.',voice='Yehuda ben Shamua and companions collective protest')
next(z for z in P['records'] if z['id']==Rq+'.u')['content']['composition']='composite'
next(z for z in P['records'] if z['id']==Rq+'.a')['content'].update(surface='Yehuda ben Shamua and companions',role='collective',candidates=[])
next(z for z in P['records'] if z['id']==Rq)['content']['answer_set_status']='none'
next(z for z in P['records'] if z['id']==Rq)['uncertainty'].append('Rhetorical protest; no represented answer inventory. None is not a negative assertion about the source. Narrative outcome separately retained.')
S=c('decree.revoked','18a:3','ובטלום ואותו היום עשאוהו יו"ט','The decrees were revoked, and that day was made a festival.',voice='baraita narrative',comp='composite')
T=c('abaye.full','18a:4',ix['18a:4']['text'],'Abaye says Rav’s explanation is needed for a full thirty-day month.',who='Abaye',cond=['full month']);e('twentynine.answer1','18a:4',ix['18a:4']['text'],T,Kq,'answer')
U=c('ashi.short','18a:5',ix['18a:5']['text'],'Rav Ashi permits a short month reading: an ordinary following day prohibits fasting but allows eulogy; sandwiched between two festivals this day prohibits eulogy too.',who='Rav Ashi',cond=['short month','between two festival dates'],comp='composite');e('twentynine.answer2','18a:5',ix['18a:5']['text'],U,Kq,'answer')
Uq=q('eighth.q','18a:6',ix['18a:6']['text'],'Why begin the Shavuot commemoration on the eighth when the eighth is already a tamid commemoration date?')
V=c('eighth.independent','18a:7',ix['18a:7']['text'],'If an event caused cancellation of the seven tamid days, the eighth would remain prohibited as the Shavuot commemoration’s first day.',cond=['hypothetical cancellation of earlier observance']);e('eighth.answer','18a:7',ix['18a:7']['text'],V,Uq,'answer')
W=c('twentynine.independent','18a:8',ix['18a:8']['text'],'Likewise, cancellation of the twenty-eighth would leave the twenty-ninth prohibited as preceding the tamid commemoration.',cond=['hypothetical cancellation of twenty-eighth']);e('twentynine.answer3','18a:8',ix['18a:8']['text'],W,Kq,'answer');e('cancellation.analogy','18a:8',ix['18a:8']['text'],W,V,'analogy')
refs=list(ix);refs=refs[refs.index('17b:9'):refs.index('18a:8')+1]
add('structure.dates','structure',refs[0],dict(title='Megillat Taanit Nisan dates and adjacent-day rationale, with twenty-eighth narrative',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs]
notes={'17b:9':'Mishnah adjacency rule, baraita preface and both commemorative intervals retained.','17b:10':'First-day redundancy question and Rav preceding-day answer retained.','17b:11':'New-moon predecessor objection and scriptural reinforcement distinction retained.','17b:12':'Both baraita adjacency rules, explicit difference question and reinforcement rationale retained.','17b:13':'Festival endpoint question and Pappa transmission linked across folio.','18a:1':'Pappa answer, Yosi identification and twenty-ninth objection retained.','18a:2':'Twenty-eighth commemoration, all three decrees, narrative question and consultation retained.','18a:3':'Matron instruction, actual protest, rhetorical kinship questions and revocation/festival outcome retained.','18a:4':'Abaye full-month answer retained.','18a:5':'Ashi short-month alternative and fasting/eulogy distinction retained.','18a:6':'Overlapping eighth-date objection retained.','18a:7':'Hypothetical cancellation and independent date rationale retained.','18a:8':'Extended cancellation answer for twenty-ninth retained; later named rulings read separately.'}
for z in P['records']:
 if z['layer']=='questions' and z['content']['answer_set_status']=='partial':z['uncertainty'].append('Partial denotes represented local response only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch036.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
