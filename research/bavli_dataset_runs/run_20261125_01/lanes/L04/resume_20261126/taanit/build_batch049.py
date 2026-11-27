"""Manual23a18–23b7, complete Abba Hilkiah dialogue."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','b5f8c5d85c7041b01e113ca6d6b9702f0573a634ee4dcadf25f7ab6487e4db9c').replace('ta.resume008.','ta.resume049.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
contract=runner.read(ROOT/'research/bavli_dataset_runs/run_20261125_01/RUN_CONTRACT.json')
for p,h in contract['production_files'].items():assert runner.sha((ROOT/p).read_bytes())==h
A=c('hilkiah.background','23a:18','אבא חלקיה בר בריה דחוני המעגל הוה וכי מצטריך עלמא למיטרא הוו משדרי רבנן לגביה ובעי רחמי ואתי מיטרא','Abba Hilkiah was Honi’s grandson; when rain was needed, rabbis sent to him, he prayed and rain came.',voice='narrative',comp='composite')
B=c('delegation','23a:18','זימנא חדא איצטריך עלמא למיטרא שדור רבנן זוגא דרבנן לגביה למבעי רחמי דניתי מיטרא אזול לביתיה ולא אשכחוהו אזול בדברא ואשכחוהו דהוה קא רפיק יהבו ליה שלמא','Two rabbis seeking his rain prayer find him digging in a field after not finding him at home and greet him.',voice='narrative',comp='composite')
C=c('no.greeting','23b:1','ולא אסבר להו אפיה','He does not turn a welcoming face to them.',voice='narrative')
D=c('separate.shoulders','23b:1','בפניא כי הוה מנקט ציבי דרא ציבי ומרא בחד כתפא וגלימא בחד כתפא','In the evening he carries wood and hoe on one shoulder and his cloak on the other.',voice='narrative',comp='composite')
E=c('shoes.water','23b:1','כולה אורחא לא סיים מסאני כי מטי למיא סיים מסאניה','He walks barefoot but puts shoes on at water.',voice='narrative',comp='composite')
F=c('garment.thorns','23b:1','כי מטא להיזמי והיגי דלינהו למניה','At thorns he lifts his garments.',voice='narrative')
G=c('wife.adorned','23b:1','כי מטא למתא נפקא דביתהו לאפיה כי מיקשטא','His adorned wife comes to meet him at town.',voice='narrative')
H=c('entry.order','23b:1','כי מטא לביתיה עלת דביתהו ברישא והדר עייל איהו והדר עיילי רבנן','His wife enters first, then he, then the rabbis.',voice='narrative',comp='composite')
I=c('no.invitation','23b:1','יתיב וכריך ריפתא ולא אמר להו לרבנן תו כרוכו','He eats without inviting the rabbis.',voice='narrative')
J=c('children.portions','23b:1','פלג ריפתא לינוקי לקשישא חדא ולזוטרא תרי','He gives one portion to the elder child and two to the younger.',voice='narrative',comp='composite')
K=c('private.prayer.plan','23b:2','אמר לה לדביתהו ידענא דרבנן משום מיטרא קא אתו ניסק לאיגרא וניבעי רחמי אפשר דמרצי הקדוש ברוך הוא וייתי מיטרא ולא נחזיק טיבותא לנפשין','He tells his wife the rabbis came for rain and proposes rooftop prayer so rain may come without taking credit.',who='Abba Hilkiah',comp='composite')
L=c('wife.cloud.first','23b:2','סקו לאיגרא קם איהו בחדא זויתא ואיהי בחדא זויתא קדים סלוק ענני מהך זויתא דדביתהו','They stand at separate rooftop corners; clouds first rise from his wife’s corner.',voice='narrative',comp='composite')
Lq=q('visit.why.q','23b:2','כי נחית אמר להו אמאי אתו רבנן','On descending he asks why the rabbis came.',who='Abba Hilkiah')
M=c('visit.answer','23b:2','אמרו ליה שדרי לן רבנן לגבי דמר למיבעי רחמי אמיטרא','They explain they were sent to request his rain prayer.',voice='two rabbis');e('visit.answer.edge','23b:2',ix['23b:2']['text'],M,Lq,'answer')
N=c('hilkiah.modesty','23b:2','אמר להו ברוך המקום שלא הצריך אתכם לאבא חלקיה','He blesses God for not making them need Abba Hilkiah.',who='Abba Hilkiah')
O=c('rabbis.recognition','23b:3','אמרו ליה ידעינן דמיטרא מחמת מר הוא דאתא אלא לימא לן מר הני מילי דתמיהא לן','They say they know the rain came through him and request explanations of puzzling actions.',voice='two rabbis',comp='composite')
Oq=q('greeting.q','23b:3','מאי טעמא כי יהיבנא למר שלמא לא אסבר לן מר אפיה','Why did he not respond to their greeting?',voice='two rabbis')
R=c('hired.time','23b:3','אמר להו שכיר יום הואי ואמינא לא איפגר','He was a day laborer and would not waste work time.',who='Abba Hilkiah');e('greeting.answer','23b:3',ix['23b:3']['text'],R,Oq,'answer');e('greeting.reason','23b:3',ix['23b:3']['text'],R,C)
Rq=q('cloak.q','23b:3','ומאי טעמא דרא מר ציבי אחד כתפיה וגלימא אחד כתפיה','Why separate wood and cloak on the shoulders?',voice='two rabbis')
S=c('borrowed.cloak','23b:3','אמר להו טלית שאולה היתה להכי שאלי ולהכי לא שאלי','The cloak was borrowed for its intended use, not for carrying wood.',who='Abba Hilkiah');e('cloak.answer','23b:3',ix['23b:3']['text'],S,Rq,'answer')
Sq=q('shoes.q','23b:4','מאי טעמא כולה אורחא לא סיים מר מסאניה וכי מטי למיא סיים מסאניה','Why wear shoes only at water?',voice='two rabbis')
T=c('water.visibility','23b:4','אמר להו כולה אורחא חזינא במיא לא קא חזינא','He can see the road, but not what is in the water.',who='Abba Hilkiah');e('shoes.answer','23b:4',ix['23b:4']['text'],T,Sq,'answer')
Tq=q('thorns.q','23b:4','מ"ט כי מטא מר להיזמי והיגי דלינהו למניה','Why lift the garments at thorns?',voice='two rabbis')
U=c('skin.heals','23b:4','אמר להו זה מעלה ארוכה וזה אינה מעלה ארוכה','Flesh heals, whereas a garment does not.',who='Abba Hilkiah');e('thorns.answer','23b:4',ix['23b:4']['text'],U,Tq,'answer')
Uq=q('wife.adornment.q','23b:5','מאי טעמא כי מטא מר למתא נפקא דביתהו דמר כי מיקשטא','Why did his wife meet him adorned?',voice='two rabbis')
V=c('wife.reason','23b:5','אמר להו כדי שלא אתן עיני באשה אחרת','So he would not look at another woman.',who='Abba Hilkiah');e('wife.answer','23b:5',ix['23b:5']['text'],V,Uq,'answer')
Vq=q('entry.q','23b:5','מאי טעמא עיילא היא ברישא והדר עייל מר אבתרה והדר עיילינן אנן','Why wife first, then husband, then rabbis?',voice='two rabbis')
W=c('unknown.guests','23b:5','אמר להו משום דלא בדקיתו לי','Because the visitors were not known to him.',who='Abba Hilkiah');e('entry.answer','23b:5',ix['23b:5']['text'],W,Vq,'answer')
Wq=q('meal.q','23b:6','מאי טעמא כי כריך מר ריפתא לא אמר לן איתו כרוכו','Why did he not invite them to eat?',voice='two rabbis')
X=c('food.scarce','23b:6','משום דלא נפישא ריפתא ואמינא לא אחזיק בהו ברבנן טיבותא בחנם','Food was scant; he would not gain gratitude through an empty invitation.',who='Abba Hilkiah',comp='composite');e('meal.answer','23b:6',ix['23b:6']['text'],X,Wq,'answer')
Xq=q('portions.q','23b:6','מאי טעמא יהיב מר לינוקא קשישא חדא ריפתא ולזוטרא תרי','Why one portion for the elder and two for the younger?',voice='two rabbis')
Y=c('children.locations','23b:6','אמר להו האי קאי בביתא והאי יתיב בבי כנישתא','The elder stays at home while the younger studies at the synagogue.',who='Abba Hilkiah',comp='composite');e('portions.answer','23b:6',ix['23b:6']['text'],Y,Xq,'answer')
Yq=q('cloud.first.q','23b:7','ומאי טעמא קדים סלוק ענני מהך זויתא דהוות קיימא דביתהו דמר לעננא דידיה','Why did clouds rise first from his wife’s corner?',voice='two rabbis')
Z=c('food.v.money','23b:7','משום דאיתתא שכיחא בביתא ויהבא ריפתא לעניי ומקרבא הנייתה [ואנא יהיבנא] זוזא ולא מקרבא הנייתיה','His wife gives the poor bread with immediate benefit, while his money provides less immediate benefit.',who='Abba Hilkiah',comp='composite',unc=['Bracketed first-person wording retained.']);e('cloud.answer1','23b:7',ix['23b:7']['text'],Z,Yq,'answer')
AA=c('repentance.v.death','23b:7','אי נמי הנהו ביריוני דהוו בשיבבותן [אנא] בעי רחמי דלימותו והיא בעיא רחמי דליהדרו בתיובתא [ואהדרו]','Alternatively, he prayed for neighborhood troublemakers to die, while she prayed for their repentance, with bracketed text reporting repentance.',who='Abba Hilkiah',comp='composite',unc=['Alternative explanation and bracketed אנא/ואהדרו retained.']);e('cloud.answer2','23b:7',ix['23b:7']['text'],AA,Yq,'answer')
refs=list(ix);refs=refs[refs.index('23a:18'):refs.index('23b:7')+1]
add('structure.hilkiah','structure',refs[0],dict(title='Abba Hilkiah’s observed actions, rain prayer and explanations',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs]
notes={'23a:18':'Lineage, rain-prayer practice, delegated rabbis and field encounter retained.','23b:1':'All eight observed actions retained separately: greeting, loads, shoes, thorns, wife, entry, meal and portions.','23b:2':'Private prayer/no-credit plan, distinct corners, wife-first clouds and visit dialogue retained.','23b:3':'Rabbis recognition, greeting and cloak questions and both explanations retained.','23b:4':'Shoes and thorns questions and visibility/healing answers retained.','23b:5':'Adornment and entry questions with fidelity/unknown-guest answers retained.','23b:6':'Invitation and portions questions with scarce-food and child-location answers retained.','23b:7':'Cloud-priority question, immediate charity and alternative repentance explanations retained with brackets.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local responses only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])];rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch049.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
