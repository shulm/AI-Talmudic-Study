"""Manual source reading 9b:3–9, with weather continuation through 10a:15."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','06306419f2bc9457a01f42ff4e2dfd9f016b847fb724723d6ec8b861e072bc81').replace('ta.resume008.','ta.resume017.').replace('/root/taanit_continuation_2','/root/taanit_continuation_3')
exec(compile(helper,__file__,'exec'))
A=c('individual','9b:3','ואף ר"ל סבר מטר בשביל יחיד','Resh Lakish too holds that rain comes on account of an individual.',who='Resh Lakish')
Aq=q('individual.q','9b:3','דאמר ר"ל מנין למטר בשביל יחיד','Resh Lakish asks the source for rain on account of an individual.',who='Resh Lakish')
Av=c('individual.verse','9b:3',"דכתיב (זכריה י, א) שאלו מה' מטר בעת מלקוש ה' עושה חזיזים ומטר גשם יתן להם לאיש עשב בשדה",'Zechariah’s rain request culminates in rain given to an individual, vegetation in the field.',voice='biblical quotation',comp='composite');e('individual.answer','9b:3',ix['9b:3']['text'],Av,Aq,'answer');e('individual.proof','9b:3',ix['9b:3']['text'],Av,A);e('individual.agreement','9b:3','ואף ר"ל סבר מטר בשביל יחיד',A,'ta.resume016.rain.individual','support')
Bq=q('all.people.q','9b:4','יכול לכל','Could the rain be for everyone?',voice='quoted exposition')
B=c('person','9b:4','תלמוד לומר לאיש','The exposition limits the reference through לאיש, for an individual.',voice='quoted exposition');e('person.answer','9b:4','תלמוד לומר לאיש',B,Bq,'answer')
Cq=q('all.fields.q','9b:4','ותניא אי לאיש יכול לכל שדותיו','Could an individual’s rain apply to all his fields?',voice='quoted baraita')
C=c('field','9b:4','ת"ל שדה','The word field narrows the scope.',voice='quoted baraita');e('field.answer','9b:4','ת"ל שדה',C,Cq,'answer')
Dq=q('whole.field.q','9b:4','אי שדה יכול לכל השדה','Could this mean the whole field?',voice='quoted baraita')
D=c('vegetation','9b:4','ת"ל עשב','The word vegetation further narrows the scope.',voice='quoted baraita');e('vegetation.answer','9b:4','ת"ל עשב',D,Dq,'answer')
E=c('garden.visits','9b:5','כי הא דרב דניאל בר קטינא הוה ליה ההיא גינתא כל יומא הוה אזיל וסייר לה','Rav Daniel bar Katina had a garden which he inspected every day.',voice='anonymous narrator',status='narrative routine')
F=c('beds.need','9b:5','אמר הא מישרא בעיא מיא והא מישרא לא בעיא מיא','He identified one garden bed as needing water and another as not needing it.',who='Rav Daniel bar Katina',comp='composite',status='narrative speech')
G=c('targeted.rain','9b:5','ואתא מיטרא וקמשקי כל היכא דמיבעי ליה מיא','Rain came and watered wherever water was needed.',voice='anonymous narrator',cond=['location needs water'],status='narrative outcome');e('garden.example','9b:5',ix['9b:5']['text'],G,D,'example')
Hq=q('haziz.action.q','9b:6',"מאי ה' עושה חזיזים",'What does God makes חזיזים mean?')
H=c('personal.haziz','9b:6','א"ר יוסי (בר) חנינא מלמד שכל צדיק וצדיק הקב"ה עושה לו חזיז בפני עצמו','Rabbi Yosi (bar) Hanina says God makes an individual חזיז for each righteous person.',who='Rabbi Yosi (bar) Hanina',unc=['Printed parenthesis around בר preserved; no silent identity normalization.']);e('haziz.action.answer','9b:6','א"ר יוסי (בר) חנינא מלמד שכל צדיק וצדיק הקב"ה עושה לו חזיז בפני עצמו',H,Hq,'answer')
Iq=q('haziz.q','9b:6','מאי חזיזים','What are חזיזים?')
I=c('porhot','9b:6','אמר רב יהודה פורחות','Rav Yehuda explains חזיזים as פורחות.',who='Rav Yehuda',unc=['Lexical term retained; physical definition is supplied below.']);e('haziz.answer','9b:6','אמר רב יהודה פורחות',I,Iq,'answer')
J=c('rain.sign','9b:6','אמר רבי יוחנן סימן למטר פורחות','Rabbi Yohanan calls פורחות a sign of rain.',who='Rabbi Yohanan')
Jq=q('porhot.q','9b:6','מאי פורחות','What are פורחות?')
K=c('cloud.layers','9b:6','אמר רב פפא עיבא קלישא תותי עיבא סמיכתא','Rav Pappa defines them as a thin cloud under a thick cloud.',who='Rav Pappa');e('porhot.answer','9b:6','אמר רב פפא עיבא קלישא תותי עיבא סמיכתא',K,Jq,'answer')
L=c('drizzle.before','9b:7','אמר רב יהודה נהילא מקמי מיטרא אתי מיטרא','Rav Yehuda says נהילא before rain signals coming rain.',who='Rav Yehuda',cond=['נהילא precedes rain'],unc=['נהילא retained; drizzle is a lexical gloss, not an emendation.'])
M=c('drizzle.after','9b:7','בתר מיטרא פסיק מיטרא','He says נהילא after rain signals rain stopping.',who='Rav Yehuda',cond=['נהילא follows rain'])
L1=c('sieve.mnemonic','9b:7','מקמי מיטרא אתי מיטרא וסימניך מהולתא','The before-rain rule is repeated with a sieve as mnemonic.',voice='explanatory repetition',comp='composite');e('sieve.analogy','9b:7','מקמי מיטרא אתי מיטרא וסימניך מהולתא',L1,L,'analogy')
M1=c('goats.mnemonic','9b:7','דבתר מיטרא פסיק מיטרא וסימניך חריא דעיזי:','The after-rain rule is repeated with goat droppings as mnemonic.',voice='explanatory repetition',comp='composite');e('goats.analogy','9b:7','דבתר מיטרא פסיק מיטרא וסימניך חריא דעיזי:',M1,M,'analogy')
N=c('ulla.cloud','9b:8','עולא איקלע לבבל חזא פורחות','Ulla came to Babylonia and saw פורחות.',voice='anonymous narrator',status='narrative setting')
O=c('ulla.prediction','9b:8','אמר להו פנו מאני דהשתא אתי מיטרא','Ulla told them to clear their vessels because rain was about to come.',who='Ulla',comp='composite',status='prediction contradicted by subsequent event')
P1=c('no.rain','9b:8','לסוף לא אתי מיטרא','Ultimately no rain came.',voice='anonymous narrator',status='narrative outcome');e('failed.prediction','9b:8',ix['9b:8']['text'],P1,O,'objection')
Q=c('ulla.rebuke','9b:8','אמר כי היכי דמשקרי בבלאי הכי משקרי מיטרייהו','Ulla disparagingly compares their rain’s false indication with Babylonian lying.',who='Ulla',status='reported character’s rhetoric, not narrator-endorsed claim about a population')
R=c('dates.price','9b:9','עולא איקלע לבבל חזי מלא צנא דתמרי בזוזא','Ulla came to Babylonia and saw a basketful of dates priced at a zuz.',voice='anonymous narrator',status='narrative setting')
S=c('dates.initial','9b:9','אמר מלא צנא דדובשא בזוזא ובבלאי לא עסקי באורייתא','He calls it a basketful of honey for a zuz and criticizes Babylonians for not studying Torah.',who='Ulla',comp='composite',status='initial evaluative speech, reversed after discomfort')
T=c('dates.discomfort','9b:9','בליליא צערוהו','At night the dates caused him discomfort.',voice='anonymous narrator',status='narrative event')
U=c('dates.reversal','9b:9','אמר מלא צנא דסכינא בזוזא ובבלאי עסקי באורייתא','He now calls it a basketful of knives for a zuz and remarks that Babylonians do study Torah.',who='Ulla',comp='composite',status='revised evaluative speech');e('dates.correction','9b:9',ix['9b:9']['text'],U,S,'correction')
# Source-explicit case introduction כי הא supports a common example relation via the schema’s support enum.
next(z for z in P['records'] if z['id']=='ta.resume017.garden.example')['content']['relation']='support'
next(z for z in P['records'] if z['id']==Av+'.a')['content'].update(surface='scriptural quotation',role='quoted_authority',candidates=[])
refs=list(ix);refs=refs[refs.index('9b:3'):refs.index('9b:9')+1]
for k,title,first,last in [('individual','Individual rain and the garden illustration','9b:3','9b:5'),('signs','Hazizim, cloud signs and rainfall mnemonics','9b:6','9b:7'),('ulla','Ulla’s Babylonian cloud and date episodes','9b:8','9b:9')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'9b:3':'Resh Lakish agreement with earlier Yohanan, source question and Zechariah proof retained.','9b:4':'Three narrowing questions and each literal textual answer retained.','9b:5':'Garden visits, distinct bed needs and rain outcome retained as example.','9b:6':'All three questions, named answers, rain-sign assertion and printed parenthetical patronymic retained.','9b:7':'Before/after conditions, repeated rules and both mnemonics retained.','9b:8':'Cloud sighting, prediction, failed outcome and Ulla’s attributed rhetoric retained.','9b:9':'Price, initial criticism, nighttime discomfort and explicit reversal retained.'}
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch017.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
