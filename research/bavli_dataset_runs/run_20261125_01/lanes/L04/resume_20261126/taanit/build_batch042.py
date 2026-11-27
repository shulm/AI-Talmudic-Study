"""Manual20b4–21a1; full following narratives read through21a14."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','ee216dfc696d4b2f9cfc5aff49549779fd6f172d8938caa6c18c2ca41ffc97fe').replace('ta.resume008.','ta.resume042.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('collapse.rule','20b:4','תנו רבנן מפולת שאמרו בריאות ולא רעועות שאינן ראויות ליפול ולא הראויות ליפול','The collapse rule concerns sound, not unsound, structures: those not expected to fall rather than those expected to fall.',voice='baraita',comp='composite');e('collapse.qualification','20b:4',ix['20b:4']['text'],A,'ta.resume038.plague.city','qualification')
Aq=q('redundancy.q','20b:5','הי ניהו בריאות הי ניהו שאינן ראויות ליפול הי ניהו רעועות הי ניהו ראויות ליפול','Are sound/not expected to fall and unsound/expected to fall not redundant pairs?')
B=c('height.river','20b:5','לא צריכא דנפלו מחמת גובהייהו אי נמי דקיימן אגודא דנהרא','The answer concerns collapse from excessive height or standing on a riverbank.',comp='composite',cond=['height or riverbank']);e('redundancy.answer','20b:5',ix['20b:5']['text'],B,Aq,'answer')
C=c('nehardea.wall','20b:6','כי ההיא אשיתא רעועה דהואי בנהרדעא דלא הוה חליף רב ושמואל תותה אע"ג דקיימא באתרה תליסר שנין','Rav and Shmuel avoided passing under an unsound Nehardea wall despite its standing thirteen years.',voice='narrative',comp='composite')
D=c('adda.arrival','20b:6','יומא חד איקלע רב אדא בר אהבה להתם','Rav Adda bar Ahava arrived one day.',voice='narrative')
E=c('shmuel.detour','20b:6','אמר ליה שמואל לרב ניתי מר נקיף','Shmuel proposes to Rav that they go around.',who='Shmuel')
F=c('rav.merit','20b:6','אמר ליה לא צריכנא האידנא דאיכא רב אדא בר אהבה בהדן דנפיש זכותיה ולא מסתפינא','Rav declines that day because Adda bar Ahava is with them, whose great merit removes his fear.',who='Rav',cond=['Adda present']);e('detour.distinction','20b:6',ix['20b:6']['text'],F,E,'distinction')
G=c('huna.wine','20b:7',"רב הונא הוה ליה ההוא חמרא בההוא ביתא רעיעא ובעי לפנוייה עייליה לרב אדא בר אהבה להתם משכי' בשמעתא עד דפנייה",'Rav Huna wished to remove wine from an unstable house and kept Adda engaged in teaching there until the wine was removed.',voice='narrative',comp='composite')
H=c('house.fell','20b:7','בתר דנפק נפל ביתא ארגיש רב אדא בר אהבה איקפד','After Adda left, the house fell; he realized what had happened and was angry.',voice='narrative',comp='composite')
I=c('yannai.danger','20b:8','סבר לה כי הא דאמר רבי ינאי לעולם אל יעמוד אדם במקום סכנה ויאמר עושין לי נס שמא אין עושין לו נס ואם תימצי לומר עושין לו נס מנכין לו מזכיותיו','Adda follows Rabbi Yannai’s warning against standing in danger expecting a miracle: none may occur, and if one does, merit is deducted.',who='Rabbi Yannai',comp='composite',cond=['entering danger expecting miracle']);e('anger.reason','20b:8',ix['20b:8']['text'],I,H)
Iq=q('merit.verse.q','20b:8','אמר רב חנן מאי קרא','Rav Hanan asks which verse supports this.',who='Rav Hanan')
J=c('merit.verse','20b:8','דכתיב (בראשית לב, יא) קטנתי מכל החסדים ומכל האמת','Rav Hanan cites Genesis32:11, being diminished by all kindness and truth.',who='Rav Hanan');e('merit.verse.answer','20b:8',ix['20b:8']['text'],J,Iq,'answer');e('merit.support','20b:8',ix['20b:8']['text'],J,I)
Jq=q('adda.deeds.q','20b:9','מאי הוה עובדיה דרב אדא בר אהבה','What were Rav Adda bar Ahava’s practices?')
Kq=q('longevity.q','20b:9','כי הא דאתמר שאלו תלמידיו (את רבי זירא ואמרי לה) לרב אדא בר אהבה במה הארכת ימים','Students ask the reported sage how he attained longevity.',voice='students in alternative attribution account')
next(z for z in P['records'] if z['id']==Kq)['uncertainty'].append('Parenthetical alternative Rabbi Zeira versus Rav Adda bar Ahava preserved; no single recipient forced.')
K=c('practice.respect','20b:9','אמר להם מימי לא הקפדתי בתוך ביתי ולא צעדתי בפני מי שגדול ממני','The sage says he never became angry in his household and never walked ahead of someone greater.',voice='sage reply with alternative attribution',comp='composite',unc=['Rabbi Zeira/Rav Adda bar Ahava alternatives unresolved.'])
L=c('practice.torah','20b:10','ולא הרהרתי במבואות המטונפות ולא הלכתי ד\' אמות בלא תורה ובלא תפילין','He avoided Torah thoughts in filthy alleys and did not walk four cubits without Torah and tefillin.',voice='sage reply with alternative attribution',comp='composite',unc=['Rabbi Zeira/Rav Adda bar Ahava alternatives unresolved.'])
M=c('practice.sleep','20b:10','ולא ישנתי בבית המדרש לא שינת קבע ולא שינת עראי','He never slept in the study hall, neither regular sleep nor a nap.',voice='sage reply with alternative attribution',comp='composite',unc=['Rabbi Zeira/Rav Adda bar Ahava alternatives unresolved.'])
N=c('practice.peers','20b:10','ולא ששתי בתקלת חברי ולא קראתי לחבירי בהכינתו ואמרי לה בחניכתו','He did not rejoice at a colleague’s failure or call him by הכינתו, alternatively חניכתו.',voice='sage reply with alternative attribution',comp='composite',unc=['Alternative sage attribution and alternative nickname wording retained.'])
for cid in [K,L,M,N]:
 next(z for z in P['records'] if z['id']==cid+'.a')['content'].update(surface='רבי זירא / רב אדא בר אהבה',role='speaker',candidates=['Rabbi Zeira','Rav Adda bar Ahava'])
 next(z for z in P['records'] if z['id']==cid+'.p')['content']['holder_candidates']=['Rabbi Zeira','Rav Adda bar Ahava']
 if cid!=K:
  for z in P['records']:
   if z['id'] in [cid,cid+'.u',cid+'.a',cid+'.p']:z['evidence'].insert(0,ev('20b:9','כי הא דאתמר שאלו תלמידיו (את רבי זירא ואמרי לה) לרב אדא בר אהבה במה הארכת ימים'))
 e(cid.rsplit('.',1)[-1]+'.longevity','20b:10' if cid!=K else '20b:9',ix['20b:10' if cid!=K else '20b:9']['text'],cid,Kq,'answer')
e('adda.practices.answer','20b:9',ix['20b:9']['text'],K,Jq,'answer')
Oq=q('huna.deeds.q','20b:11','אמר ליה רבא לרפרם בר פפא לימא לן מר מהני מילי מעלייתא דהוה עביד רב הונא','Rava asks Rafram bar Pappa to recount Rav Huna’s good practices.',who='Rava')
O=c('rafram.memory','20b:11','אמר ליה בינקותיה לא דכירנא בסיבותיה דכירנא','Rafram remembers Huna’s old age, not his youth.',who='Rafram bar Pappa',comp='composite')
R=c('wall.inspection','20b:11','דכל יומא דעיבא הוו מפקין ליה בגוהרקא דדהבא וסייר לה לכולה מתא וכל אשיתא דהוות רעיעתא הוה סתר לה','On cloudy days Huna was carried in a golden litter to inspect the city and demolish unsound walls.',voice='Rafram narrative',comp='composite')
S=c('wall.rebuild','20b:11','אי אפשר למרה בני לה ואי לא אפשר בני לה איהו מדידיה','If the owner could afford it, he rebuilt; otherwise Huna rebuilt at his own expense.',voice='Rafram narrative',comp='composite',cond=['owner able versus unable']);e('huna.deeds.answer','20b:11',ix['20b:11']['text'],R,Oq,'answer')
T=c('vegetable.purchase','20b:12','וכל פניא דמעלי שבתא הוה משדר שלוחא לשוקא וכל ירקא דהוה פייש להו לגינאי זבין ליה ושדי ליה לנהרא','Every Sabbath eve Huna sent an agent to buy the growers’ remaining vegetables and throw them into the river.',voice='Rafram narrative',comp='composite')
Tq=q('poor.gift.q','20b:12','וליתביה לעניים','Why not give the vegetables to the poor?')
U=c('poor.dependence','20b:12','זמנין דסמכא דעתייהו ולא אתו למיזבן','They might rely on the distribution and not come to buy.');e('poor.answer','20b:12',ix['20b:12']['text'],U,Tq,'answer')
Uq=q('animal.food.q','20b:12','ולשדייה לבהמה','Why not give them to animals?')
V=c('human.food','20b:12','קסבר מאכל אדם אין מאכילין לבהמה','The discussion explains that Huna holds human food should not be fed to animals.',who='Rav Huna',status='view ascribed by explanatory discussion');e('animal.answer','20b:12',ix['20b:12']['text'],V,Uq,'answer')
Vq=q('no.purchase.q','20b:13','ולא ליזבניה כלל','Why buy the leftovers at all?')
W=c('future.supply','20b:13','נמצאת מכשילן לעתיד לבא','Not buying would cause them difficulty in the future.',unc=['Compact future obstacle kept; specific market mechanism not asserted as explicit.']);e('purchase.answer','20b:13',ix['20b:13']['text'],W,Vq,'answer')
X=c('remedy.water','20b:14','כי הוה ליה מילתא דאסותא הוי מלי כוזא דמיא ותלי ליה בסיפא דביתא ואמר כל דבעי ליתי ולישקול','When Huna had a healing remedy, he filled and hung a water vessel at his doorway, inviting anyone to take.',voice='Rafram narrative',comp='composite')
Y=c('shivta.variant','20b:14','ואיכא דאמרי מילתא דשיבתא הוה גמיר והוה מנח כוזא דמיא ודלי ליה ואמר כל דצריך ליתי וליעול דלא לסתכן','An alternative account says Huna knew a remedy for shivta and placed water with an invitation to enter to avoid danger.',voice='alternative narrative version',comp='composite',unc=['שיבתא retained without medical equivalence.']);e('water.variant','20b:14',ix['20b:14']['text'],Y,X,'qualification')
Z=c('meal.invitation','20b:15','כי הוה כרך ריפתא הוה פתח לבביה ואמר כל מאן דצריך ליתי וליכול','When eating, Huna opened his door and invited anyone in need to eat.',voice='Rafram narrative',comp='composite')
AA=c('rava.exception','20b:15','אמר רבא כולהו מצינא מקיימנא לבר מהא דלא מצינא למיעבד','Rava says he could fulfill all these practices except the open meal invitation.',who='Rava')
AB=c('mahoza.reason','21a:1',ix['21a:1']['text'],'The reason is the many בני חילא in Mahoza.',voice='continuation of Rava explanation',unc=['בני חילא retained without forcing exact social category.']);e('invitation.reason','21a:1',ix['21a:1']['text'],AB,AA)
refs=list(ix);refs=refs[refs.index('20b:4'):refs.index('21a:1')+1]
for k,title,first,last in [('walls','Collapse criteria, dangerous walls and miracle reliance','20b:4','20b:8'),('virtues','Alternative sage longevity report and Huna’s communal practices','20b:9','21a:1')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'20b:4':'Sound/unsound and expected/unexpected collapse conditions retained.','20b:5':'Redundancy objection and height/riverbank alternatives retained.','20b:6':'Joint avoidance of thirteen-year wall, Adda arrival and actual Shmuel/Rav detour exchange retained.','20b:7':'Huna wine removal, Adda engagement, collapse and anger retained.','20b:8':'Yannai danger/miracle/merit warning and Hanan verse question/proof retained.','20b:9':'Adda practices question, students longevity question and printed Zeira/Adda alternatives retained.','20b:10':'All Torah/tefillin/sleep/peer rules and nickname variant retained, with alternative sage attribution.','20b:11':'Rava request, Rafram memory limits, Huna inspection and conditional rebuilding retained.','20b:12':'Vegetable purchase/disposal and both alternative-use objections/answers retained.','20b:13':'No-purchase objection and future-supply response retained.','20b:14':'Healing water and shivta alternative version retained.','20b:15':'Meal invitation and Rava limitation retained across folio.','21a:1':'Mahoza limitation reason retained without forced social-category equivalence.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local source response only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch042.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
