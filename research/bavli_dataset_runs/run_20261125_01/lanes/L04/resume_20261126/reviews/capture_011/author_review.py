import json, hashlib, re
from pathlib import Path
import jsonschema
OUT=Path(__file__).parent
JOB=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_taanit_delegated020.json')
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8'))
j=load(JOB)
assert sha(JOB.read_bytes())=='14b290933383dd991d34522afefabcf1708c8753965322a3e633915f352f5d56'
bindings=[j['source'],*j['common_documents'],j['frozen_plan'],j['original_source_schema']]
for b in bindings: assert sha(Path(b['path']).read_bytes())==b['sha256']
s=load(j['source']['path']); plan=load(j['frozen_plan']['path']); schema=load(j['common_documents'][1]['path'])
ph={k:v for k,v in plan.items() if k!='plan_sha256'}
assert sha(b'bavli-source-only-review-plan-v1\0'+json.dumps(ph,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())==j['plan_sha256']
source={f'Taanit {p//2+1}{"a" if p%2==0 else "b"}:{i+1}':t for p,page in enumerate(s['text']) for i,t in enumerate(page)}
core=j['core_refs']; records=[]; coverage=[]; lookup={}
def ev(r,q=None):
 r=r if r.startswith('Taanit') else 'Taanit '+r
 t=source[r]; q=t if q is None else q; a=t.index(q)
 return {'segment_id':r,'start_char':a,'end_char':a+len(q),'quote':q}
def add(k,layer,e,content,links=[],unc=[],origin='source_paraphrase'):
 id='taanit020.'+k
 assert id not in lookup
 d={'id':id,'layer':layer,'evidence':e,'content':content,'origin':origin,'uncertainty':unc,'links':['taanit020.'+x for x in links]}
 records.append(d);lookup[id]=d;return k
def c(k,r,q,p,holder='anonymous',chain=[],cond=[],mode='asserted',unc=[]):
 e=[ev(r,q)];add(k,'claims',e,{'proposition':p,'conditions':cond,'scope':'Local source exposition; not an enduring personal view or later practical ruling','assertion_mode':mode},unc=unc)
 add(k+'.u','utterances',e,{'textual_voice':holder,'discourse_role':'claim/explanation or reported narrative','composition':'atomic'},[k],unc)
 holders=holder.split('|')
 add(k+'.a','attributions',e,{'surface':holder,'role':'anonymous' if holder=='anonymous' else 'position_holder','candidates':[] if holder=='anonymous' else holders,'scope':'taanit020.'+k,'transmission_chain':chain},[k],unc)
 if chain:
  add(k+'.trans','attributions',e,{'surface':' → '.join(chain),'role':'transmitter','candidates':chain[:-1],'scope':'taanit020.'+k,'transmission_chain':chain},[k],unc)
 add(k+'.p','positions',e,{'holder_candidates':holders,'claim_id':'taanit020.'+k,'question_id':None,'conditions':cond,'local_status':mode},[k],unc)
def q(k,r,quote,p,holder='anonymous'):
 e=[ev(r,quote)];add(k,'questions',e,{'formulation':p,'question_origin':'explicit','conditions':[],'answer_set_status':'topic_inventory'})
 add(k+'.u','utterances',e,{'textual_voice':holder,'discourse_role':'question/challenge','composition':'atomic'},[k])
 add(k+'.a','attributions',e,{'surface':holder,'role':'anonymous' if holder=='anonymous' else 'speaker','candidates':[] if holder=='anonymous' else [holder],'scope':'taanit020.'+k,'transmission_chain':[]},[k])
def edge(k,a,b,rel,r,quote=None):
 add(k,'edges',[ev(r,quote)],{'source_id':'taanit020.'+a,'target_id':'taanit020.'+b,'relation':rel,'explicitness':'source_explicit'},[a,b])

c('ben.report','3a:11','ר\' יהודה אומר משום בן בתירה העובר לפני התיבה ביום טוב האחרון של חג האחרון מזכיר','On the last festival day the latter prayer leader mentions rain.','בן בתירה',['ר\' יהודה','בן בתירה'],['last festival day','latter prayer leader'])
q('ben.q','3a:11','הי בן בתירה אילימא רבי יהודה בן בתירה הא אמר בשני בחג הוא מזכיר','Which Ben Beteira? Identifying him as R. Judah b. Beteira conflicts with his second-day commencement.')
c('ben.rejected','3a:11','אילימא רבי יהודה בן בתירה','The cited Ben Beteira is R. Judah b. Beteira.','anonymous',mode='rejected')
c('ben.second','3a:11','הא אמר בשני בחג הוא מזכיר','R. Judah b. Beteira starts mentioning on the second festival day.','רבי יהודה בן בתירה')
c('ben.resolve','3a:12',None,'The authority is R. Yehoshua b. Beteira, called sometimes by his name and sometimes by his father’s, before/after ordination.','רב נחמן בר יצחק',unc=['Text states before/after ordination without explicitly pairing each label with an occasion; no pairing assigned.'])
edge('ben.e1','ben.second','ben.rejected','objection','3a:11');edge('ben.e2','ben.resolve','ben.q','answer','3a:12')
c('dew.optional','3a:13','בטל וברוחות לא חייבו חכמים להזכיר','The sages did not require mentioning dew or winds.','anonymous')
c('dew.permit','3a:13','ואם בא להזכיר מזכיר','One may mention dew/winds if one wishes.','anonymous',cond=['chooses to mention'])
q('dew.why','3a:13','מ"ט','Why were dew and wind mentions not required?')
c('dew.reason','3a:13','א"ר חנינא לפי שאין נעצרין','Dew and winds are not withheld.','ר\' חנינא')
edge('dew.reason.e','dew.reason','dew.why','answer','3a:13')
q('dew.proofq','3a:14','וטל מנלן דלא מיעצר','What proves dew is not withheld?')
c('dew.elijah','3a:14','ויאמר אליהו התשבי מתושבי גלעד אל אחאב חי ה\' אלהי ישראל אשר עמדתי לפניו אם יהיה השנים האלה טל ומטר כי אם לפי דברי','Scripture reports Elijah’s oath to Ahab denying dew and rain except by his word.','אליהו',cond=['embedded scriptural speech'])
c('dew.restore','3a:14','לך הראה אל אחאב ואתנה מטר על פני האדמה ואילו טל לא קאמר ליה','The restoration command mentions rain, not dew.','anonymous')
q('dew.omitq','3a:14','מאי טעמא','Why is dew omitted from the restoration command?')
c('dew.notheld','3b:1','דלא מיעצר','Dew was not withheld.','anonymous')
q('dew.oathq','3b:1','וכי מאחר דלא מיעצר אליהו אשתבועי למה ליה','Why swear about dew if it cannot be withheld?')
c('dew.bless','3b:1','הכי קא"ל אפילו טל דברכה נמי לא אתי','Elijah meant that even beneficial dew would not come.','אליהו',chain=['anonymous explanation','אליהו'],cond=['dew of blessing'],mode='reconciled')
q('dew.returnq','3b:1','וליהדריה לטל דברכה','Why not announce restoration of beneficial dew?')
c('dew.invisible','3b:1','משום דלא מינכרא מילתא','The distinction would not be perceptible.','anonymous')
for k,a,b,r in [('d1','dew.notheld','dew.omitq','3b:1'),('d2','dew.bless','dew.oathq','3b:1'),('d3','dew.invisible','dew.returnq','3b:1'),('d4','dew.restore','dew.proofq','3a:14')]:edge(k,a,b,'answer',r)
q('wind.proofq','3b:2','רוחות מנא לן דלא מיעצרי','What proves winds are not withheld?')
c('wind.verse','3b:2','א"ר יהושע בן לוי דאמר קרא (זכריה ב, י) כי כארבע רוחות השמים פרשתי אתכם נאם ה\'','R. Yehoshua b. Levi adduces Zechariah’s comparison to the four winds.','ר\' יהושע בן לוי')
q('wind.meanq','3b:2','מאי קאמר להו','What does the comparison mean?')
c('wind.scatter','3b:2','אילימא הכי קאמר להו הקב"ה לישראל דבדרתינכו בארבע רוחי דעלמא','God means that Israel was scattered into four directions.','anonymous',mode='rejected')
c('wind.grammar','3b:2','אי הכי כארבע בארבע מיבעי ליה','Scattering into four directions would require בארבע, not כארבע.','anonymous')
c('wind.analogy','3b:2','אלא הכי קאמר כשם שאי אפשר לעולם בלא רוחות כך א"א לעולם בלא ישראל','Just as the world cannot exist without winds, it cannot exist without Israel.','anonymous',mode='reconciled')
edge('w1','wind.grammar','wind.scatter','objection','3b:2');edge('w2','wind.analogy','wind.meanq','answer','3b:2');edge('w3','wind.verse','wind.proofq','support','3b:2')
c('summer.wind','3b:3','א"ר חנינא הלכך בימות החמה אמר משיב הרוח אין מחזירין אותו','Saying “He causes wind to blow” in summer does not require repetition.','ר\' חנינא',cond=['summer','said משיב הרוח'])
c('summer.rain','3b:3','אמר מוריד הגשם מחזירין אותו','Saying “He causes rain to fall” in summer requires repetition.','ר\' חנינא',cond=['summer','said מוריד הגשם'])
c('winter.wind','3b:4','בימות הגשמים לא אמר משיב הרוח אין מחזירין אותו','Omitting wind in the rainy season does not require repetition.','ר\' חנינא',cond=['rainy season','omitted משיב הרוח'])
c('winter.rain','3b:4','לא אמר מוריד הגשם מחזירין אותו','Omitting rain in the rainy season requires repetition.','ר\' חנינא',cond=['rainy season','omitted מוריד הגשם'])
c('winter.reverse','3b:4','ולא עוד אלא אפילו אמר מעביר הרוח ומפריח הטל אין מחזירין אותו','Even saying that God removes wind and disperses dew does not require repetition.','ר\' חנינא',cond=['said מעביר הרוח ומפריח הטל'],unc=['Season follows the rainy-season clause; formulation may have wider application, not decided here.'])
edge('season.reason','dew.reason','summer.wind','support','3b:3','הלכך');edge('winter.cont','winter.wind','summer.wind','continuation','3b:4')
c('cloud.optional','3b:5','בעבים וברוחות לא חייבו חכמים להזכיר','Sages did not require mention of clouds and winds.','anonymous')
c('cloud.permit','3b:5','ואם בא להזכיר מזכיר','Mention of clouds/winds is permitted if desired.','anonymous',cond=['voluntary mention'])
q('cloud.why','3b:5','מ"ט','Why is cloud/wind mention optional?')
c('cloud.reason','3b:5','משום דלא מיעצרי','Clouds and winds are not withheld.','anonymous',mode='challenged')
q('cloud.challenge','3b:6','ולא מיעצרי והתני רב יוסף','Are they not withheld? Rav Yosef’s teaching challenges this.')
c('cloud.derash','3b:6','ועצר את השמים מן העבים ומן הרוחות','“He shall shut the heavens” concerns withholding clouds and winds.','anonymous baraita',['רב יוסף','anonymous baraita'])
q('cloud.derashq','3b:6','אתה אומר מן העבים ומן הרוחות או אינו אלא מן המטר','Does shutting heaven refer to clouds/winds or rain alone?','anonymous baraita')
c('cloud.rainonly','3b:6','או אינו אלא מן המטר','Shutting the heavens refers only to rain.','anonymous baraita',mode='rejected')
c('cloud.redundancy','3b:6','כשהוא אומר ולא יהיה מטר הרי מטר אמור הא מה אני מקיים ועצר את השמים מן העבים ומן הרוחות','Since “there will be no rain” states rain separately, shutting heaven refers to clouds and winds.','anonymous baraita',['רב יוסף','anonymous baraita'])
edge('cloud.e1','cloud.reason','cloud.why','answer','3b:5');edge('cloud.e2','cloud.derash','cloud.reason','objection','3b:6');edge('cloud.e3','cloud.redundancy','cloud.rainonly','objection','3b:6')
q('cloud.contrad','3b:7','קשיא רוחות ארוחות קשיא עבים אעבים','Both wind claims and cloud claims contradict one another.')
c('cloud.distinct','3b:7','עבים אעבים לא קשיא הא בחרפי הא באפלי','Cloud statements distinguish early from late clouds.','anonymous',mode='reconciled',unc=['Bare הא...הא does not explicitly assign each source; no unmarked mapping supplied.'])
c('wind.distinct','3b:8','רוחות ארוחות לא קשיא הא ברוח מצויה הא ברוח שאינה מצויה','Wind statements distinguish usual and unusual wind.','anonymous',mode='reconciled',unc=['Usual wind is read as not withheld; directional mapping is contextual inference.'])
q('wind.threshq','3b:8','רוח שאינה מצויה חזיא לבי דרי','Does unusual wind not benefit threshing floors, warranting prayer?')
c('wind.fans','3b:8','אפשר בנפוותא','Fans can serve instead for threshing.','anonymous')
edge('cloud.e4','cloud.distinct','cloud.contrad','distinction','3b:7');edge('cloud.e5','wind.distinct','cloud.contrad','distinction','3b:8');edge('wind.e6','wind.fans','wind.threshq','answer','3b:8')
c('after.rank','3b:9','תנא העבים והרוחות שניות למטר','Clouds and winds are second to rain.','anonymous baraita')
q('after.q','3b:9','היכי דמי','In which circumstance are clouds and winds second to rain?')
c('after.good','3b:9','אמר עולא ואיתימא רבי יהודה דבתר מיטרא','The ranking concerns clouds/winds after rain.','עולא|רבי יהודה',unc=['Explicit alternative attribution; first spelling is רבי יהודה, retained.'])
q('after.challenge','3b:9','למימרא דמעליותא היא והכתיב (דברים כח, כד) יתן ה\' את מטר ארצך אבק ועפר','Is post-rain wind beneficial, given the curse of dust and dirt rain?')
c('after.bad','3b:9','ואמר עולא ואיתימא רב יהודה זיקא דבתר מטרא','The curse is interpreted as wind after rain.','עולא|רב יהודה',unc=['Second alternate spelling is רב יהודה; no silent harmonization with רבי יהודה earlier.'])
c('after.gentle','3b:10','לא קשיא הא דאתא ניחא הא דאתא רזיא','The accounts distinguish gentle from forceful wind.','anonymous',mode='reconciled',cond=['gentle versus forceful'])
c('after.dust','3b:10','(ואי בעית אימא) הא דמעלה אבק הא דלא מעלה אבק','Alternatively, the distinction is whether wind raises dust.','anonymous',mode='reconciled',cond=['dust-raising versus non-dust-raising'],unc=['Parenthetical alternative marker retained as printed.'])
edge('after.e1','after.good','after.q','answer','3b:9');edge('after.e2','after.bad','after.good','objection','3b:9');edge('after.e3','after.gentle','after.challenge','distinction','3b:10');edge('after.e4','after.dust','after.challenge','distinction','3b:10')
c('rain.wind','3b:11','ואמר רב יהודה זיקא דבתר מיטרא כמיטרא','Wind after rain is as beneficial as rain.','רב יהודה',cond=['after rain'])
c('rain.cloud','3b:11','עיבא דבתר מיטרא כמיטרא','Cloud after rain is as beneficial as rain.','רב יהודה',cond=['after rain'])
c('rain.sun','3b:11','שימשא דבתר מיטרא כתרי מטרי','Sun after rain is like two rains.','רב יהודה',cond=['after rain'])
q('rain.excludeq','3b:11','למעוטי מאי','What circumstances are excluded?')
c('rain.exclude','3b:11','למעוטי גילהי דליליא ושמשא דביני קרחי','The comparison excludes nocturnal gleams and sun between clouds.','anonymous',unc=['Precise meteorological senses of גילהי דליליא and ביני קרחי remain lexical interpretation.'])
edge('rain.e','rain.exclude','rain.excludeq','answer','3b:11')
c('snow.five','3b:12','אמר רבא מעלי תלגא לטורי כחמשה מטרי לארעא','Snow benefits mountains like five rains benefit earth.','רבא')
c('snow.proof','3b:12','שנאמר (איוב לז, ו) כי לשלג יאמר הוא ארץ וגשם מטר וגשם מטרות עוזו','Job 37:6 is cited for the five-rain snow comparison.','רבא')
edge('snow.e','snow.proof','snow.five','support','3b:12')
c('terrain.snow','3b:13','ואמר רבא תלגא לטורי','Snow is beneficial for mountains.','רבא')
c('terrain.trees','3b:13','מטרא רזיא לאילני','Forceful rain benefits trees.','רבא')
c('terrain.fruit','3b:13','מטרא ניחא לפירי','Gentle rain benefits fruit.','רבא')
c('mist.seed','4a:1','עורפילא אפילו לפרצידא דתותי קלא מהניא ליה','Mist benefits even a seed beneath a clod.','רבא',unc=['Attribution inherited from preceding ואמר רבא; no new name at opening.'])
q('mist.q','4a:1','מאי עורפילא','What does עורפילא mean?')
c('mist.word','4a:1','עורו פילי','עורפילא is expounded as עורו פילי.','anonymous',unc=['Wordplay preserved literally without resolving its meteorological mechanics.'])
c('scholar.seed','4a:1','ואמר רבא האי צורבא מרבנן דמי לפרצידא דתותי קלא דכיון דנבט נבט','A young scholar is like a seed under a clod: once sprouting, it sprouts.','רבא')
edge('mist.e','mist.word','mist.q','answer','4a:1');edge('scholar.e','scholar.seed','mist.seed','analogy','4a:1')
c('anger.torah','4a:2','ואמר רבא האי צורבא מרבנן דרתח אורייתא הוא דקא מרתחא ליה','When a young scholar becomes heated, Torah heats him.','רבא',cond=['scholar becomes heated'])
c('anger.fire','4a:2','שנאמר (ירמיהו כג, כט) הלא כה דברי כאש נאם ה\'','“My words are like fire” supports the scholar’s Torah-induced heat.','רבא')
c('scholar.iron','4a:2','ואמר רב אשי כל ת"ח שאינו קשה כברזל אינו ת"ח','A scholar who is not hard as iron is not a scholar.','רב אשי')
c('scholar.hammer','4a:2','שנא\' (ירמיהו כג, כט) וכפטיש יפוצץ סלע','The hammer shattering rock is the proof for hardness.','רב אשי')
edge('anger.e','anger.fire','anger.torah','support','4a:2');edge('iron.e','scholar.hammer','scholar.iron','support','4a:2')
c('iron.alternate','4a:3','א"ל רבי אבא לרב אשי אתון מהתם מתניתו לה אנן מהכא מתנינן לה דכתיב (דברים ח, ט) ארץ אשר אבניה ברזל אל תקרי אבניה אלא בוניה','R. Abba tells Rav Ashi that his group derives this from reading “its stones” as “its builders” of iron.','רבי אבא',unc=['This is an alternative proof, not a disagreement over the hardness proposition.'])
c('anger.gentle','4a:3','אמר רבינא אפ"ה מיבעי ליה לאיניש למילף נפשיה בניחותא','Nevertheless a person must train himself in gentleness.','רבינא')
c('anger.proof','4a:3','שנאמר (קהלת יא, י) והסר כעס מלבך וגו\'','“Remove anger from your heart” supports training in gentleness.','רבינא')
edge('iron.e2','iron.alternate','scholar.iron','support','4a:3');edge('anger.e2','anger.gentle','anger.torah','qualification','4a:3');edge('anger.e3','anger.proof','anger.gentle','support','4a:3')

chain=['ר\' יצחק','רבי יוחנן']
foods=[('שנה ראשונה אכלו מה שבבתים','first','food stored in houses'),('שניה אכלו מה שבשדות','second','food in fields'),('שלישית בשר בהמה טהורה','third','meat of clean animals'),('רביעית בשר בהמה טמאה','fourth','meat of unclean animals'),('חמישית בשר שקצים ורמשים','fifth','flesh of vermin and creeping creatures'),('ששית בשר בניהם ובנותיהם','sixth','flesh of their sons and daughters'),('שביעית בשר זרועותיהם','seventh','flesh of their own arms')]
for i,(quote,year,food) in enumerate(foods):c('famine.'+str(i+1),'5a:10',quote,f'In the {year} year of the seven-year famine they ate {food}.','רבי יוחנן',chain,cond=[year+' year of famine'])
c('famine.proof','5a:10','לקיים מה שנאמר (ישעיהו ט, יט) איש בשר זרועו יאכלו','Eating their own arms fulfills Isaiah’s verse.','רבי יוחנן',chain)
edge('famine.e','famine.proof','famine.7','support','5a:10')
q('jerusalem.q','5a:11','מאי דכתיב (הושע יא, ט) בקרבך קדוש ולא אבוא בעיר משום דבקרבך קדוש לא אבוא בעיר','Does the presence of the Holy One explain non-entry into the city?','רב נחמן')
c('jerusalem.claim','5a:11','א"ל הכי א"ר יוחנן אמר הקב"ה לא אבוא בירושלים של מעלה עד שאבוא לירושלים של מטה','God says He will not enter heavenly Jerusalem until entering earthly Jerusalem.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','הקב"ה'],cond=['until entry into earthly Jerusalem'])
edge('jerusalem.e','jerusalem.claim','jerusalem.q','answer','5a:11')
q('jerusalem.existsq','5a:12','ומי איכא ירושלים למעלה','Is there a Jerusalem above?')
c('jerusalem.exists','5a:12','אין דכתיב (תהלים קכב, ג) ירושלם הבנויה כעיר שחוברה לה יחדיו','Yes: Psalm 122:3 supports the existence of heavenly Jerusalem.','anonymous')
edge('jerusalem.e2','jerusalem.exists','jerusalem.existsq','answer','5a:12')
q('idolatry.q','5a:13','מאי דכתיב (ירמיהו י, ח) ובאחת יבערו ויכסלו מוסר הבלים עץ הוא','What does Jeremiah 10:8 mean?','רב נחמן')
c('idolatry.burn','5a:13','א"ל הכי א"ר יוחנן אחת היא שמבערת רשעים בגיהנם','One thing burns the wicked in Gehinnom.','רבי יוחנן',chain)
q('idolatry.which','5a:13','מאי היא','Which thing?')
c('idolatry.ident','5a:13','ע"ז כתיב הכא מוסר הבלים עץ הוא וכתיב התם (ירמיהו י, טו) הבל המה מעשה תעתועים','The thing is idolatry, identified by the shared language of vanity in Jeremiah 10:8 and 10:15.','anonymous',unc=['Explanation follows R. Yohanan’s transmitted dictum; whether the question/answer is part of that transmission is not explicit.'])
edge('idol.e','idolatry.burn','idolatry.q','answer','5a:13');edge('idol.e2','idolatry.ident','idolatry.which','answer','5a:13')
q('two.q','5a:14','מ"ד (ירמיהו ב, יג) כי שתים רעות עשה עמי תרתין הוא דהוו עשרין וארבע שביקא להו','Why does Jeremiah speak of two evils—were there only two, leaving twenty-four aside?','רב נחמן')
c('two.start','5a:14','א"ל הכי א"ר יוחנן אחת שהיא','R. Yohanan’s answer begins: one evil which is…','רבי יוחנן',chain,unc=['Sentence continues into 5b:1; not a separate completed proposition.'])
c('two.end','5b:1','שקולה כשתים ומאי ניהו ע"ז','Idolatry is one evil equivalent to two.','רבי יוחנן',chain)
c('two.proof','5b:1','דכתיב (ירמיהו ב, יג) כי שתים רעות עשה עמי אותי עזבו מקור מים חיים לחצוב להם בארות בארות נשברים','The two evils are abandoning the living-water source and digging broken cisterns, in the idolatry interpretation.','רבי יוחנן',chain)
c('two.nations','5b:1','וכתיב בהו (ירמיהו ב, י) כי עברו איי כתיים וראו וקדר שלחו והתבוננו מאד וגו\' ההימיר גוי אלהים והמה לא אלהים ועמי המיר כבודו בלא יועיל','Jeremiah contrasts nations that do not change their non-gods with Israel exchanging its glory for the useless.','anonymous scriptural citation')
edge('two.e1','two.end','two.start','continuation','5b:1');edge('two.e2','two.end','two.q','answer','5b:1');edge('two.e3','two.proof','two.end','support','5b:1')
c('nations.fire','5b:2','תנא כותיים עובדים לאש','The taught tradition says the כותיים worship fire.','anonymous baraita',unc=['Keep כותיים as printed; no imported ethnic identification.'])
c('nations.water','5b:2','וקדריים עובדין למים','The Kedarites worship water.','anonymous baraita')
c('nations.unchanged','5b:2','ואע"פ שיודעים שהמים מכבין את האש לא המירו אלהיהם','Despite knowing water extinguishes fire, they did not exchange their gods.','anonymous baraita',cond=['knowledge that water extinguishes fire'])
c('nations.israel','5b:2','ועמי המיר כבודי בלא יועיל','Israel exchanged divine glory for the useless.','anonymous baraita',unc=['Scriptural/divine first-person embedded in anonymous teaching.'])
edge('nations.e','nations.unchanged','two.nations','support','5b:2');edge('nations.e2','nations.israel','two.end','support','5b:2')
q('samuel.q','5b:3','מ"ד (שמואל א ח, א) ויהי כאשר זקן שמואל ומי סיב שמואל כולי האי והא בר נ"ב הוה','How can Samuel be described as old when he was only 52?','רב נחמן')
c('samuel.age','5b:3','דאמר מר מת בנ"ב שנה זהו מיתתו של שמואל הרמתי','An unnamed authority states that death at 52 was Samuel of Ramah’s age at death.','מר (unnamed quoted authority)')
c('samuel.aged','5b:4','א"ל הכי א"ר יוחנן זקנה קפצה עליו','Samuel was prematurely overtaken by old age.','רבי יוחנן',chain)
c('saul.regret','5b:4','דכתיב (שמואל א טו, יא) נחמתי כי המלכתי את שאול','God regretted having made Saul king, in the cited verse.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','scripture','הקב"ה'])
c('samuel.equal','5b:4','אמר לפניו רבש"ע שקלתני כמשה ואהרן דכתיב (תהלים צט, ו) משה ואהרן בכהניו ושמואל בקוראי שמו','Samuel argues before God that God equated him with Moses and Aaron.','שמואל הרמתי',chain=['ר\' יצחק','רבי יוחנן','שמואל הרמתי'],unc=['Biblical Samuel, not the amora Shmuel.'])
c('samuel.precedent','5b:4','מה משה ואהרן לא בטלו מעשה ידיהם בחייהם','Moses and Aaron’s handiwork was not annulled in their lifetimes.','שמואל הרמתי',chain=['ר\' יצחק','רבי יוחנן','שמואל הרמתי'])
c('samuel.plea','5b:4','אף אני לא יתבטל מעשה ידי בחיי','Samuel asks that his handiwork likewise not be annulled during his lifetime.','שמואל הרמתי',chain=['ר\' יצחק','רבי יוחנן','שמואל הרמתי'],mode='queried')
edge('samuel.e','samuel.aged','samuel.q','answer','5b:4');edge('samuel.e2','samuel.precedent','samuel.plea','analogy','5b:4')
q('god.q','5b:5','אמר הקב"ה היכי אעביד','What should God do, within the reported exposition?','הקב"ה')
c('god.saul','5b:5','לימות שאול לא קא שביק שמואל','Letting Saul die is prevented by Samuel’s plea.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','הקב"ה'],mode='rejected')
c('god.samuel','5b:5','לימות שמואל אדזוטר מרנני אבתריה','Letting Samuel die while young would cause people to speak disparagingly about him.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','הקב"ה'],mode='rejected')
c('god.neither','5b:5','לא לימות שאול ולא לימות שמואל כבר הגיעה מלכות דוד','Keeping both alive conflicts with the arrival of David’s reign.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','הקב"ה'],mode='rejected')
c('god.kingdom','5b:5','ואין מלכות נוגעת בחברתה אפילו כמלא נימא','One reign cannot encroach on another even a hair’s breadth.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','הקב"ה'])
edge('god.e','god.kingdom','god.neither','support','5b:5')
# Necessary context-only ending of the Samuel discussion, with no sampled-core credit.
c('context.aging','5b:6','אמר הקב"ה אקפיץ עליו זקנה','God resolves to bring premature old age upon Samuel.','הקב"ה',chain=['ר\' יצחק','רבי יוחנן','הקב"ה'])
c('context.delay','5b:6','אלא לומר לך מי גרם לשאול שישב בגבעה שתי שנים ומחצה תפלתו של שמואל הרמתי','Samuel’s prayer enabled Saul to remain in Gibeah two and a half years.','anonymous explanatory voice')
q('context.displaceq','5b:7','ומי מידחי גברא מקמי גברא','May one person be displaced for another?')
c('context.displace','5b:7',None,'Yes: the exposition of Hosea 6:5 attributed through R. Samuel b. Nahmani to R. (Yohanan) supports displacement by divine words rather than their deeds.','ר\' (יוחנן)',['ר\' שמואל בר נחמני','ר\' (יוחנן)'],unc=['Parenthetical authority preserved; not silently normalized.'])
edge('context.e1','context.aging','god.q','answer','5b:6');edge('context.e2','context.displace','context.displaceq','answer','5b:7');edge('context.e3','context.aging','samuel.aged','local_resolution','5b:6')

titles=['Identity of Ben Beteira']*2+['Dew and wind prayer mentions']*8+['Clouds and winds: contradiction and distinction']*2+['Conditions for post-rain benefit']*3+['Snow and rain by terrain']*2+['Mist and scholars']+['Scholars: heat, hardness, gentleness']*2+['Seven-year famine']+['Heavenly Jerusalem']*2+['Idolatry and Gehinnom']+['Idolatry as two evils']*3+['Samuel premature aging']*3
assert len(titles)==30
recon={
'3a:11':'Preserved latter-leader report, rejected identification, and second-day counterclaim; contextual 3a:8–10 explains competing Rabbi Yehoshua identifications.',
'3a:12':'Resolved Ben Beteira identity; retained uncertainty on before/after ordination mapping.',
'3a:13':'Separated non-obligation, permission, question, and reason.',
'3a:14':'Retained Elijah oath and restoration quotation separately; sentence resolves in 3b:1. Printed biblical locator preserved without external correction.',
'3b:1':'Captured non-withholding, beneficial-dew qualification and perceptibility answer; no unqualified endorsement of oath contradiction.',
'3b:2':'Separated verse, rejected geographic reading, grammatical objection and Israel/wind analogy.',
'3b:3':'Both summer cases preserved with opposite outcomes.',
'3b:4':'Both rainy-season omissions and reversed dew/wind formula preserved; inherited R. Hanina attribution marked by continuity.',
'3b:5':'Preserved obligation, voluntary permission, and challenged non-withholding reason.',
'3b:6':'Rav Yosef is transmitter of baraita; rejected rain-only interpretation and redundancy proof retained.',
'3b:7':'Both contradiction branches retained; early/late cloud mapping left unassigned.',
'3b:8':'Usual/unusual distinction and threshing-floor challenge/fan substitute retained.',
'3b:9':'Preserved both alternate attributions exactly; rank, after-rain condition, curse and challenge separately.',
'3b:10':'Both gentle/forceful and dust/non-dust resolutions kept as alternatives.',
'3b:11':'Wind, cloud, sun ratios separate; excluded conditions preserved with lexical uncertainty.',
'3b:12':'Five-rain comparison and its cited support retained.',
'3b:13':'Three different beneficiaries separated.',
'4a:1':'Initial mist continuation, lexical question/answer and scholar analogy all inventoried.',
'4a:2':'Rava heat and Rav Ashi hardness distinguished, with separate scriptural supports.',
'4a:3':'R. Abba offers alternate proof; Ravina qualifies conduct with gentleness, not cancellation of all prior claims.',
'5a:10':'Seven years independently inventoried; inherited R. Isaac → R. Yohanan chain recovered from 5a:9; cannibalism narrative not omitted.',
'5a:11':'Rav Nahman asks, R. Isaac transmits R. Yohanan, embedded God speech distinct.',
'5a:12':'Anonymous existence question and affirmative verse argument preserved.',
'5a:13':'Interpretive question, burning claim, identification question and shared-word proof preserved; explanation attribution uncertain.',
'5a:14':'Question about two versus twenty-four retained; answer explicitly incomplete until 5b:1.',
'5b:1':'Continuation joins one evil/two evils; both scriptural passages retained.',
'5b:2':'Fire and water worship, knowledge, non-exchange and Israel contrast separately retained.',
'5b:3':'Biblical Samuel distinguished from amora; unnamed age authority retained.',
'5b:4':'Premature aging, divine regret, comparison with Moses/Aaron and plea separately recorded; original exposition R. Yohanan distinguished from embedded speakers.',
'5b:5':'Three rejected options and no-overlap principle retained; resolution read in context 5b:6–7.'}
for r,title in zip(core,titles):
 boundary='open_both' if r in ['Taanit 3a:14','Taanit 5a:14'] else 'open_left' if r in ['Taanit 3a:11','Taanit 3b:1','Taanit 4a:1','Taanit 5a:10','Taanit 5b:1'] else 'open_right' if r=='Taanit 5b:5' else 'closed'
 add('structure.'+r.split()[1].replace(':','.'),'structure',[ev(r)],{'title':title,'primary':True,'boundary':boundary,'legacy_ids':[]},origin='editorial_inference')
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==r for e in x['evidence'])]
  rationale=recon[r.split()[1]] if layer=='reconciliation' else 'All independently identified '+layer+' in this original core inventoried; unresolved ambiguities retained explicitly.' if ids else 'Source reread: no separate '+layer+' record originated in this core; adjacent-source relations remain anchored to their own evidence.'
  coverage.append({'segment_id':r,'layer':layer,'extraction_state':'completed','extraction_result':'records_found' if ids else 'none_found_after_pass','record_ids':ids,'rationale':rationale})
proposal={'schema_version':'2.0.0-production','tractate':'Taanit','owner':'independent-source-only-delegated020','epoch':1,'source_sha256':j['source']['sha256'],'protocol_sha256':j['common_documents'][0]['sha256'],'schema_sha256':j['common_documents'][1]['sha256'],'execution':{'route':'interactive_agent','agent_id':'/root/taanit_source_review020','model_id':None},'records':records,'coverage':coverage,'open_tails':[]}
jsonschema.validate(proposal,schema)
for x in records:
 for e in x['evidence']:assert source[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
 for link in x['links']:assert link in lookup
for r in core:
 spans=[e for x in records if x['layer']=='structure' and x['content']['primary'] for e in x['evidence'] if e['segment_id']==r]
 assert len(spans)==1 and spans[0]['start_char']==0 and spans[0]['end_char']==len(source[r])
for b in plan['review_blocks']:
 if b['block_id'] in [x['block_id'] for x in j['selected_blocks']]:
  for sp in b['spans']:assert sha(source[sp['ref']].encode())==sp['span_sha256_utf8']
read_refs=[r for r in source if int(re.match(r'Taanit (\d+)',r).group(1)) in [3,4,5,6] and r.split()[1].split(':')[0] in ['3a','3b','4a','5a','5b','6a']]
artifact={'artifact_kind':'frozen_source_only_independent_reading','job_id':j['job_id'],'agent_identity':'/root/taanit_source_review020','model_id':None,'blind_to_production':True,'production_comparison_performed':False,'human_certification':False,'ml_eligible':False,'status':'SOURCE_ONLY_READING_COMPLETE_NOT_PRODUCTION_VERDICT','job_sha256':sha(JOB.read_bytes()),'bindings':bindings,'plan_sha256':j['plan_sha256'],'cohort':j['cohort'],'core_refs':core,'core_count':30,'read_source_refs':read_refs,'context_refs':[r for r in read_refs if r not in core],'context_coverage_credit':0,'source_attribution':{k:s[k] for k in ['versionTitle','versionSource','license','title','language']},'independent_review':proposal,'source_omission_reconciliation':recon,'uncertainties':[{'record_id':x['id'],'notes':x['uncertainty']} for x in records if x['layer']=='claims' and x['uncertainty']],'limitations':['AI provisional source-only review; no producer comparison or canonical production validation performed.','Structural ownership is segment-level with explicit open boundaries; does not assert each segment is an independent sugya.','Questions with no question wording in a core are not synthesized as explicit questions.','Source biblical locators and parenthetical/variant authority spellings retained exactly.']}
out=OUT/'taanit_delegated020.json'
raw=(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
with out.open('xb') as f:f.write(raw)
h=sha(raw)
with out.with_suffix('.sha256').open('x',encoding='utf8') as f:f.write(h+'  '+out.name+'\n')
receipt={'artifact':str(out),'sha256':h,'author_script_sha256':sha(Path(__file__).read_bytes()),'checks':{'dependency_hashes':6,'descriptor_hash':True,'plan_domain_hash':True,'core_span_hashes':30,'proposal_json_schema':True,'exact_evidence':sum(len(x['evidence']) for x in records),'resolved_links':True,'primary_structure_full_partition':30,'coverage_cells':240,'source_only_omission_pass':30},'record_counts':{l:sum(x['layer']==l for x in records) for l in ['structure','utterances','claims','attributions','questions','positions','edges']},'no_producer_inspection':True,'context_not_counted':True}
with (OUT/'validation_receipt.json').open('x',encoding='utf8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=False))
