import json, hashlib, re
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).parent
JOB=ROOT/'jobs/bavli_meilah_supplement003a.json'
j=json.loads(JOB.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(j['source']['path'])==j['source']['sha256']
for x in j['common_documents']: assert sha(x['path'])==x['sha256']
source=json.loads(Path(j['source']['path']).read_bytes())
texts={f'Meilah {i//2+1}{"a" if i%2==0 else "b"}:{n+1}':s for i,page in enumerate(source['text']) for n,s in enumerate(page)}
records=[]; ids={}; serial=Counter(); questions={}; notes={}; voices={}; contexts=[]
def ref(r): return r if r.startswith('Meilah ') else 'Meilah '+r
def ev(r,quote=None):
 r=ref(r);s=texts[r];quote=s if quote is None else quote;start=s.index(quote)
 return {'segment_id':r,'start_char':start,'end_char':start+len(quote),'quote':quote}
def rec(layer,r,content,quote=None,unc=None,links=None,origin='source_paraphrase',key=None):
 serial[layer]+=1; id=f'meilah_supplement003a.{layer}.{serial[layer]:04}'
 records.append(dict(id=id,layer=layer,evidence=[ev(r,quote)],content=content,origin=origin,uncertainty=unc or [],links=links or [],supersedes=None))
 if key: ids[key]=id
 return id
def q(key,r,form,conditions=None,quote=None,explicit=True):
 id=rec('questions',r,dict(formulation=form,question_origin='explicit' if explicit else 'editorial_reconstruction',conditions=conditions or [],answer_set_status='topic_inventory'),quote,origin='source_paraphrase' if explicit else 'editorial_inference',key=key)
 questions[key]=id; return id
def c(key,r,prop,quote=None,cond=None,holder='anonymous',mode='asserted',question=None,status=None,unc=None,chain=None):
 cond=cond or [];id=rec('claims',r,dict(proposition=prop,conditions=cond,scope=ref(r),assertion_mode=mode),quote,unc,key=key)
 holders=holder if isinstance(holder,list) else [holder]
 rec('attributions',r,dict(surface=' / '.join(holders),role='anonymous' if holders==['anonymous'] else 'position_holder',candidates=holders,scope=id,transmission_chain=chain or []),quote,unc,links=[id])
 if chain:
  for person in chain[:-1]:rec('attributions',r,dict(surface=person,role='transmitter',candidates=[person],scope=id,transmission_chain=chain),quote,unc,links=[id])
 rec('positions',r,dict(holder_candidates=holders,claim_id=id,question_id=questions.get(question),conditions=cond,local_status=status or mode),quote,unc,links=[id]+([questions[question]] if question else []))
 return id
def e(a,b,rel,r,quote=None,explicit=True):
 return rec('edges',r,dict(source_id=ids.get(a,questions.get(a,a)),target_id=ids.get(b,questions.get(b,b)),relation=rel,explicitness='source_explicit' if explicit else 'editorial_reconstruction'),quote,links=[ids.get(a,questions.get(a,a)),ids.get(b,questions.get(b,b))],origin='source_paraphrase' if explicit else 'editorial_inference')
def stages(r,prefix,subject,initial=None,stage=None,invalid=None,liability=None,liability_stage=None,meilah=None):
 if initial:c(prefix+'.initial',r,subject+': subject to meilah from consecration',initial,cond=['from consecration'],holder='anonymous Mishnah')
 if invalid:
  for name in invalid:
   c(prefix+'.invalid.'+str(invalid.index(name)),r,subject+': susceptible to disqualification by '+name,stage,cond=[invalid[name]],holder='anonymous Mishnah')
 if liability:
  for typ in liability:c(prefix+'.liable.'+typ,r,subject+': liability for '+typ,liability_stage,cond=[liability[typ]],holder='anonymous Mishnah')
def tri(r,prefix,subject,anchor,condition):
 for typ in ['piggul','notar','tumah']:c(prefix+'.'+typ,r,subject+': liability for '+typ,anchor,[condition],holder='anonymous Mishnah')
def inv(r,prefix,subject,anchor,condition,lina=True):
 for typ in ['tevul yom','mechusar kippurim']+(['overnight delay'] if lina else []):c(prefix+'.'+typ.replace(' ','_'),r,subject+': susceptible to disqualification by '+typ,anchor,[condition],holder='anonymous Mishnah')

# Source-first reading: clauses are manually inventoried, not extracted by a heuristic.
c('birdsin.start','8a:3','Bird sin-offering is subject to meilah from consecration','העוף מועלין בה משהוקדשה',holder='anonymous Mishnah')
inv('8a:3','birdsin.invalid','Bird sin-offering','נמלקה הוכשרה להפסל בטבול יום ובמחוסר כפורים ובלינה','after melikah')
tri('8a:4','birdsin.liable','Bird sin-offering','הוזה דמה חייבין עליו משום פיגול נותר וטמא','after blood sprinkling')
c('birdsin.no','8a:4','Bird sin-offering no longer subject to meilah','ואין בה מעילה',['after blood sprinkling'],holder='anonymous Mishnah')
c('invalidonly','8a:5','Mishnah implies disqualification, not power to transmit impurity','ליפסל אין אבל לטמויי לא',status='inference accepted and assigned to Rabbis in continuation')
q('tanna','8a:6','Whose position is the Mishnah?',quote='מתניתין מני')
c('rabbis','8a:6','Mishnah follows the Rabbis','רבנן היא',question='tanna');e('rabbis','tanna','answer','8a:6','רבנן היא')
c('abba.first','8b:1','Tevul yom has first-degree status regarding sacred food',cond=['for sacred food'],holder='אבא שאול',unc=['Sentence begins at 8a:6; תחלה interpreted by Rava at 8b:3.'])
records[-3]['evidence'].insert(0,ev('8a:6','דתניא אבא שאול אומר טבול יום'))
c('meir.sacred','8b:2','Tevul yom renders sacred food impure','ר"מ אומר  מטמא את הקדש',holder='ר"מ')
c('meir.terumah','8b:2','Tevul yom disqualifies terumah','ופוסל את התרומה',holder='ר"מ')
for item in ['terumah liquids','terumah foods','sacred liquids','sacred foods']:
 c('rabbis.'+item,'8b:2','Tevul yom disqualifies '+item,'וחכ"א  כשם שהוא פוסל משקה תרומה ואוכלי תרומה כך הוא פוסל משקה קדש ואוכלי קדש',holder='חכמים')
c('rava.abba','8b:3','Abba Shaul: rabbinic elevation of sacred status treats tevul yom as first-degree impurity',holder='רבא')
c('rava.meir','8b:4','R. Meir: tevul yom treated as second-degree food','לר"מ כאוכל שני',holder='רבא')
c('rava.rabbis','8b:4','Rabbis: immersion weakens impurity, allowing disqualification but not making others impure','לרבנן כיון דטבל קלש טומאה פסול משוי טמא לא משוי',holder='רבא')
for key,r,name in [('rava.abba','8b:3','אבא שאול'),('rava.meir','8b:4','ר"מ'),('rava.rabbis','8b:4','רבנן')]:
 rec('attributions',r,dict(surface=name,role='quoted_authority',candidates=[name],scope='authority whose view Rava explains: '+ids[key],transmission_chain=[]),links=[ids[key]])
q('tevulyom','8b:2','What impurity effect does a tevul yom have on sacred food and terumah?',explicit=False)
for z in records:
 if z['layer']=='positions' and z['content']['claim_id'] in [ids[k] for k in ['abba.first','meir.sacred','meir.terumah','rabbis.terumah liquids','rabbis.terumah foods','rabbis.sacred liquids','rabbis.sacred foods']]:
  z['content']['question_id']=questions['tevulyom'];z['links'].append(questions['tevulyom'])
e('rava.abba','abba.first','qualification','8b:3');e('rava.meir','meir.sacred','qualification','8b:4','לר"מ כאוכל שני');e('rava.rabbis','invalidonly','support','8b:4')
c('prohibit','8b:5','Mishnah implies benefit remains prohibited despite absence of meilah','מעילה הוא דליכא אבל איסורא איכא',status='scope restricted to exited meat by next answer')
q('priests','8b:5','Why prohibit benefit when this is priests’ property?',quote='ואמאי הא ממונא דכהנים הוא')
c('exit','8b:6','The clause concerns meat taken outside, under R. Akiva: sprinkling is effective for such meat though it is inedible',holder='רבי חנינא',cond=['meat taken outside','R. Akiva’s rule'],question='priests')
c('akiva','8b:6','Sprinkling benefits meat taken outside','ור"ע היא דאמר זריקה מועלת ליוצא',holder='ר"ע',chain=['רבי חנינא','ר"ע'])
c('exit.inedible','8b:6','Exited meat is not fit to eat','דלאו בת אכילה היא',cond=['taken outside'],holder='רבי חנינא')
e('exit','priests','answer','8b:6');e('exit','prohibit','qualification','8b:6')
q('squeeze','8b:7','Does omission of squeezing blood invalidate the bird sin-offering?',explicit=False)
c('huna','8b:7','Squeezing bird sin-offering blood is not indispensable','אמר רב הונא אמר רב מיצוי חטאת העוף אינו מעכב',holder='רב',chain=['רב הונא','רב'],question='squeeze',status='one transmitted Rav report; contrary report preserved')
c('huna.text','8b:7','Rav teaches the Mishnah as הוזה דמה','דתני רב הוזה דמה',holder='רב',chain=['רב הונא','רב'])
c('adda','8b:8','Squeezing bird sin-offering blood is indispensable','רב אדא בר אהבה אמר רב מיצוי חטאת העוף מעכב',holder='רב',chain=['רב אדא בר אהבה','רב'],question='squeeze',status='alternative transmitted Rav report; not a Rav–Shmuel dispute')
c('adda.text','8b:8','Rav teaches the Mishnah as מיצה דמה','ותני רב מיצה דמה',holder='רב',chain=['רב אדא בר אהבה','רב'])
e('huna.text','huna','support','8b:7');e('adda.text','adda','support','8b:8')
c('verse','8b:9','Leviticus 5:9 directs remaining blood to be squeezed to altar base; חטאת היא is cited','(ויקרא ה, ט) והנשאר בדם ימצה אל יסוד המזבח [חטאת היא]',holder='quoted scripture')
c('verse.adda','8b:9','The verse is straightforward according to Rav Adda bar Ahava’s report','בשלמא לרב אדא בר אהבה היינו דכתיב והנשאר בדם ימצה חטאת היא')
q('remain','8b:9','How does Rav Huna explain והנשאר?',quote='אלא לרב הונא מאי והנשאר')
c('ifremain','8b:10','School of R. Ishmael reads the squeezing condition as if blood remains','כדתניא דבי ר\' ישמעאל שאם נשאר',holder="דבי ר' ישמעאל",question='remain')
q('sinis','8b:10','What does חטאת היא refer to?',quote='ומאי (ויקרא ה, יא) חטאת היא')
c('firstpart','8b:10','חטאת היא refers to the earlier part','ארישא',question='sinis')
e('ifremain','remain','answer','8b:10');e('firstpart','sinis','answer','8b:10');e('verse.adda','adda','support','8b:9')
q('mealremain','8b:11','Would והנותרת for the meal-offering likewise mean only if some is left?',quote='אלא מעתה גבי מנחה דכתיב (ויקרא ב, ג) והנותרת הכי נמי שאם ניתותר',conditions=['Rav Huna’s conditional reading'])
rec('attributions','8b:11',dict(surface='רב אחא בריה דרבא',role='speaker',candidates=['רב אחא בריה דרבא'],scope=questions['mealremain'],transmission_chain=[]),'א"ל רב אחא בריה דרבא לרב אשי',links=[questions['mealremain']])
rec('attributions','8b:11',dict(surface='רב אשי',role='quoted_authority',candidates=['רב אשי'],scope='addressee, not holder of the objection',transmission_chain=[]),'לרב אשי',unc=['Schema has no addressee role; no position assigned.'])
c('mealhyp','8b:11','Possible reply: meal-offering remainder is also conditional','וכי תימא ה"נ',mode='hypothetical',status='challenged by baraita in 9a:1')
for substance,anchor in [('flour','פרט שחסרה סלתה'),('oil','וחסרה שמנה'),('frankincense','וחסרה לבונתה')]:
 c('meal.lack.'+substance,'9a:1','A meal-offering lacking '+substance+' is excluded by the cited verse',anchor,holder='anonymous baraita',cond=['missing required '+substance])
c('meal.extra','9a:2','Meal-offering case has an additional והנותרת verse',question='mealremain')
e('meal.lack.flour','mealhyp','objection','9a:1');e('meal.extra','mealremain','answer','9a:2')
q('bothsqueeze','9a:3','Does the baraita’s מיצה דמן for both bird offerings refute Rav Huna?',quote='קתני מיהת מיצה דמן')
for place in ['outside designated place','outside designated time']:
 c('baraita.'+place,'9a:3','Bird sin-offering and bird burnt-offering subjected to melikah and blood squeezing: '+('invalid, with no karet' if place.endswith('place') else 'piggul, with karet'),'אחד חטאת העוף ואחד עולת העוף שמלקן ומיצה דמן חוץ למקומן פסול ואין בו כרת חוץ לזמנן פיגול וחייבין עליו כרת',cond=[place+' intention'],holder='anonymous baraita',status='wording challenged; לצדדין limits operations by offering')
rec('attributions','9a:3',dict(surface='אבוה דשמואל (ור\' אבין)',role='speaker',candidates=['אבוה דשמואל',"ר' אבין (parenthetical)"],scope=questions['bothsqueeze'],transmission_chain=[]),'מתיב אבוה דשמואל (ור\' אבין) לרב הונא',unc=['Parenthetical ור\' אבין is retained; no decision whether variant attribution or additional objector.'],links=[questions['bothsqueeze']])
c('sidewise','9a:4','The objection’s own raiser answers that the baraita is distributed between cases',holder=['אבוה דשמואל',"ר' אבין (parenthetical unresolved)"],question='bothsqueeze',unc=['הוא refers to the preceding objector; exact expanded operation distribution not stated in this sentence.'])
e('sidewise','bothsqueeze','answer','9a:4');e('sidewise','baraita.outside designated place','qualification','9a:4');e('sidewise','baraita.outside designated time','qualification','9a:4')
c('ishmael.repeat','9a:5','School of R. Ishmael repeats: if blood remains',holder='דבי רבי ישמעאל')
q('ishmaelcontradiction','9a:6','How reconcile this with the school of R. Ishmael teaching that remainder is indispensable?',quote='והא תנא דבי רבי ישמעאל התם שיריים מעכבין')
c('ishmael.other','9a:6','School of R. Ishmael elsewhere teaches that remainders are indispensable','תנא דבי רבי ישמעאל התם שיריים מעכבין',holder='דבי רבי ישמעאל',status='second tannaitic transmission retained')
c('pappa','9a:6','The point of difference there is squeezing bird sin-offering blood','ואמר רב פפא מיצוי חטאת העוף איכא בינייהו',holder='רב פפא',unc=['The other external disputants are not named in this local citation.'])
c('twotannaim','9a:6','Two tannaim transmit divergent versions of R. Ishmael','תרי תנאי ואליבא דרבי ישמעאל',question='ishmaelcontradiction',mode='reconciled')
e('twotannaim','ishmaelcontradiction','answer','9a:6');e('ishmael.repeat','ifremain','quotation','9a:5');e('pappa','ishmaelcontradiction','support','9a:6')

for r,prefix,subject,initial,invalidanchor,phase,liableanchor,liablephase in [
 ('9a:7','birdburnt','Bird burnt-offering','עולת העוף מועלין בה משהוקדשה','נמלקה הוכשרה ליפסל בטבול יום ובמחוסר כפורים ובלינה','after melikah','מיצה דמה חייבין עליו משום פיגול נותר וטמא','after blood squeezing'),
 ('9a:8','burned','Burned bulls and goats','פרים הנשרפים ושעירים הנשרפים מועלין בהן משהוקדשו','נשחטו הוכשרו ליפסל בטבול יום ובמחוסר כפורים ובלינה','after slaughter','הוזה דמן חייבין עליהן משום פיגול נותר וטמא','after blood sprinkling'),
 ('9a:9','burnt','Animal burnt-offering','העולה מועלין בה משהוקדשה','נשחטה הוכשרה ליפסל בטבול יום ובמחוסר כפורים ובלינה','after slaughter','משנזרק דמה חייבין עליה משום פיגול נותר וטמא','after blood application'),
 ('9a:10','sinpeace','Sin-, guilt-, and communal peace-offerings','חטאת ואשם וזבחי שלמי ציבור מועלין בהן משהוקדשו','נשחטו הוכשרו ליפסל בטבול יום ובמחוסר כפורים ובלינה','after slaughter','נזרק דמן חייבין עליהן משום פיגול נותר וטמא','after blood application')]:
 c(prefix+'.start',r,subject+': meilah from consecration',initial,holder='anonymous Mishnah');inv(r,prefix+'.invalid',subject,invalidanchor,phase);tri(r,prefix+'.liable',subject,liableanchor,liablephase)
c('birdburnt.end','9a:7','Meilah continues until removal to the ash place','ומועלין בה עד שתצא לבית הדשן',holder='anonymous Mishnah',cond=['bird burnt-offering'],status='literal Mishnah wording; Rav later reads eligible for ash place')
c('burned.end','9a:8','Meilah applies in ash place until flesh is melted','ומועלין בהן בבית הדשן עד שיתיך הבשר',holder='anonymous Mishnah',cond=['burned bulls and goats'])
c('burnt.skin','9a:9','No meilah for hides','ואין מועלין בעורות',holder='anonymous Mishnah',cond=['burnt-offering','after blood application'])
c('burnt.flesh','9a:9','Meilah for flesh until removal to ash place','אבל מועלין בבשר עד שתצא לבית הדשן',holder='anonymous Mishnah',cond=['burnt-offering'],status='literal Mishnah; qualification by Rav below')
c('sinpeace.flesh','9a:10','No meilah for flesh','אין מועלין בבשר',holder='anonymous Mishnah',cond=['sin-, guilt-, communal peace-offerings','after blood application'])
c('sinpeace.emurim','9a:10','Meilah for sacrificial portions until removal to ash place','אבל מועלין באימוריהן עד שיצאו לבית הדשן',holder='anonymous Mishnah',cond=['sin-, guilt-, communal peace-offerings'])
c('loaves.start','9a:11','Two loaves: meilah from consecration','שתי הלחם מועלין בהן משהוקדשו',holder='anonymous Mishnah')
inv('9a:11','loaves.invalid','Two loaves','קרמו בתנור הוכשרו ליפסל בטבול יום ובמחוסר כפורים (ובלינה)','after crust forms in oven')
notes['Meilah 9a:11']='ובלינה is parenthetical in original; retained as textual uncertainty, not silently harmonized.'
for x in records:
 if x['id']==ids['loaves.invalid.overnight_delay']:x['uncertainty'].append('ובלינה appears parenthetically in this edition.')
c('loaves.slaughter','9a:11','Crusting qualifies the two loaves for sacrifice slaughter on their behalf','ולישחוט עליהן את הזבח',cond=['after crust forms in oven'],holder='anonymous Mishnah')
tri('9a:11','loaves.liable','Two loaves','נזרק דמן של כבשים חייבין עליהן משום פיגול נותר וטמא','after lambs’ blood application')
c('loaves.no','9a:11','Two loaves cease meilah','ואין בהן מעילה',['after lambs’ blood application'],holder='anonymous Mishnah')
c('show.start','9a:12','Showbread: meilah from consecration','לחם הפנים מועלין בו משהוקדשה',holder='anonymous Mishnah')
inv('9a:12','show.invalid','Showbread','קרם בתנור הוכשר ליפסל בטבול יום ובמחוסר כפורים','after crust forms in oven',False)
c('show.arrange','9a:12','Showbread qualified for arrangement on table','ולהסדר על גבי השולחן',['after crust forms in oven'],holder='anonymous Mishnah')
tri('9a:13','show.liable','Showbread','קרבו הבזיכין חייבין עליו משום פיגול נותר וטמא','after incense bowls offered')
c('show.no','9a:13','Showbread ceases meilah','ואין בו מעילה',['after incense bowls offered'],holder='anonymous Mishnah')
c('meal.start','9a:14','Meal-offerings: meilah from consecration','המנחות מועלין בהן משהוקדשו',holder='anonymous Mishnah')
inv('9a:14','meal.invalid','Meal-offerings','קדשו בכלי הוכשרו ליפסל בטבול יום ובמחוסר כפורים ובלינה','after sanctification in vessel')
tri('9a:15','meal.liable','Meal-offerings','קרב הקומץ חייבין עליו משום פיגול נותר וטמא','after handful offered')
c('meal.remain.no','9a:15','No meilah for remainder','ואין מועלין בשירים',['after handful offered'],holder='anonymous Mishnah')
c('meal.handful','9a:15','Meilah for handful until removal to ash place','אבל מועלין בקומץ עד שיצא לבית הדשן',holder='anonymous Mishnah')

q('ash','9a:16','Is benefit from mound ashes atop altar subject to meilah?',explicit=False,conditions=['after terumat hadeshen as specified in 9a:17'])
c('ash.rav','9a:16','No meilah for benefit from mound ashes atop altar','רב אמר אין מועלין בו',['after terumat hadeshen'],holder='רב',question='ash',status='maintained after responses to objections')
c('ash.yohanan','9a:16','Meilah for benefit from mound ashes atop altar','ורבי יוחנן אמר מועלין בו',['after terumat hadeshen'],holder='רבי יוחנן',question='ash',status='maintained after alternate-version objection answered')
c('ash.before','9a:17','All agree meilah applies before terumat hadeshen','לפני תרומת הדשן כולי עלמא לא פליגי דמועלין בו',['before terumat hadeshen'],holder=['רב','רבי יוחנן'])
c('ash.scope','9a:17','Disagreement is after terumat hadeshen','כי פליגי לאחר תרומת הדשן',cond=['after terumat hadeshen'])
c('ash.rav.reason','9a:18','Ash service has already been performed','רב אמר אין מועלין בו הרי נעשה מצותו',['after terumat hadeshen'],holder='רב',question='ash')
c('ash.yoh.reason','9a:18','Requirement of priestly garments indicates continuing sanctity','ור\' יוחנן אמר כיון דכתיב (ויקרא ו, ג) ולבש הכהן מדו בד וגו\' כיון דצריך לבגדי כהונה בקדושתיה קאי',holder='רבי יוחנן',question='ash')
q('ash.mishnah','9a:19','Does Mishnah’s until removal to ash place refute Rav?',quote='תנן מועלין בהן עד שתצא לבית הדשן קשיא לרב')
c('ash.rav.read','9a:19','Rav can read Mishnah as until eligible for ash place','אמר לך רב עד שתראה לבית הדשן',holder='רב (anonymous formulated reply)',question='ash.mishnah')
e('ash.scope','ash.rav','qualification','9a:17');e('ash.scope','ash.yohanan','qualification','9a:17');e('ash.rav.reason','ash.rav','support','9a:18');e('ash.yoh.reason','ash.yohanan','support','9a:18');e('ash.rav.read','ash.mishnah','answer','9a:19')
c('fallen.all','9b:1','Items that fly off altar are not returned','וכולן שפקעו מעל גבי המזבח לא יחזיר',holder='anonymous baraita')
c('fallen.coal','9b:1','Coal that flies off altar is not returned','וכן גחלת שפקעה מעל גבי המזבח לא יחזיר',holder='anonymous baraita')
c('coal.infer','9b:1','Inference: on the altar it is returned','הא על גבי המזבח יחזיר',status='first version objection to Rav; restricted to coal')
q('coal.rav','9b:2','The inference suits R. Yohanan but how does Rav answer?',quote='בשלמא לר\' יוחנן ניחא אלא לרב קשיא')
c('coal.distinct','9b:2','Coal differs because it has substance','אמר לך רב שאני גחלת דאית ביה מששא',holder='רב (anonymous formulated reply)',question='coal.rav')
e('coal.distinct','coal.rav','answer','9b:2');e('coal.distinct','coal.infer','distinction','9b:2')
c('ash.altinfer','9b:3','Alternative version infers coal has substance, but ash without substance has no meilah even on altar','טעמא משום גחלת דאית ביה מששא הא אפר דלית ביה מששא אפילו לגבי מזבח אין מועלין בו',status='alternate inference challenged and answered, not final adopted ruling')
q('ash.altq','9b:3','Alternative version suits Rav, but how does R. Yohanan answer?',quote='בשלמא לרב ניחא אלא לרבי יוחנן קשיא')
c('ash.altanswer','9b:4','The same applies to ash; coal is mentioned to teach that even substantial coal is not returned after flying off',holder='רבי יוחנן (anonymous formulated reply)',question='ash.altq')
e('ash.altanswer','ash.altq','answer','9b:4');e('ash.altanswer','ash.altinfer','correction','9b:4')
q('payment','9b:5','Where does the value of benefit go?',conditions=['meat of most-sacred offerings before blood application','or portions of lesser-sacred offerings after blood application'],explicit=False)
c('payment.rav','9b:5','Value of benefit goes to voluntary-offering fund','רב אמר מה שנהנה יפלו לנדבה',['most-sacred flesh before blood application or lesser-sacred portions after it'],holder='רב',question='payment')
c('payment.levi','9b:5','Buy something wholly for altar','ולוי אמר יביא דבר שכולו למזבח',['same benefit cases'],holder='לוי',question='payment')
q('meilah.where','9b:6','Where does this meilah payment go?',quote='מעילה זו להיכן הולכת')
c('levi.support','9b:6','Buy something wholly for altar','הלמידין לפני חכמים אומרים יביא דבר שכולו למזבח',holder='הלמידין לפני חכמים',question='meilah.where')
q('wholly','9b:6','What item is wholly for altar?',quote='מאי ניהו')
c('incense','9b:6','Incense is the identified item','קטרת',question='wholly')
e('levi.support','payment.levi','support','9b:6');e('incense','wholly','answer','9b:6')
for key,prop,quote,condition in [
 ('sin.pre','Add to the money and bring sin-offering','עד שלא קרבה חטאתו יוסיף ויביא חטאתו','sin-offering not yet offered'),
 ('guilt.pre','Add to money and bring guilt-offering','ועד שלא קרבה אשמו יוסיף ויביא אשמו','guilt-offering not yet offered'),
 ('sin.post','Payment goes to Dead Sea','קרב חטאתו ילכו לים המלח','sin-offering already offered; further qualified at 10a:5'),
 ('guilt.post','Payment goes to voluntary-offering fund','כבר קרב אשמו יפלו לנדבה','guilt-offering already offered')]:
 c(key,'9b:7',prop,quote,[condition,'benefit from dedicated offering money'],holder='anonymous cited baraita',status='sin-offering rule assigned to R. Shimon at 9b:10–10a:1' if key.startswith('sin.') else 'cited support for Rav')
c('rav.support','9b:8','Value of benefit goes to voluntary-offering fund','הנהנה מקדשי קדשים לפני זריקת דמים ואימורי קדשים קלים לאחר זריקת דמים מה שנהנה יפלו לנדבה',['most-sacred before blood application','lesser-sacred portions after blood application'],holder='anonymous baraita')
for key,prop,quote in [('altar','Altar-offering payments go to altar','כל קרבנות המזבח למזבח'),('repair','Sanctuary-maintenance payments go to sanctuary maintenance','קרבנות קדשי בדק הבית לבדק הבית'),('communal','Communal-offering payments go to communal voluntary fund','קרבנות צבור לנדבת צבור')]:c('payment.'+key,'9b:8',prop,quote,holder='anonymous baraita',status='latter section attributed to Rabbis in 10a:1')
e('rav.support','payment.rav','support','9b:8')
q('baraita.conflict','9b:9','How can post-atonement sin-offering funds go to Dead Sea if all altar funds go to altar regardless of atonement?')
c('unqualified','9b:9','Last clause appears to apply regardless of whether owners achieved atonement','ול"ש דאיכפור בעלים ול"ש היכא דלא איכפור',status='apparent reading that motivates split-authority solution')
c('shimon.first','9b:10','First clause follows R. Shimon','רישא ר\' שמעון היא',question='baraita.conflict')
c('shimon.die','9b:10','Sin-offering whose owner has achieved atonement must die','דאמר כל חטאת שכיפרו בעליה תמות',holder="ר' שמעון")
c('rabbis.last','10a:1','Latter clause follows Rabbis','וסיפא רבנן',question='baraita.conflict')
c('abaye.split','10a:1','First clause is R. Shimon and latter Rabbis','אמר רב גביהא דבי כתיל לרב אשי הכי אמר אביי רישא רבי שמעון וסיפא רבנן',holder='אביי',chain=['רב גביהא דבי כתיל','אביי'],question='baraita.conflict',unc=['Rav Ashi is addressee, not a transmitter in the stated chain.'])
e('abaye.split','baraita.conflict','answer','10a:1');e('shimon.die','shimon.first','support','9b:10')
for key,prop,quote,cond in [('flesh','Benefit from impure most-sacred meat is exempt','שאם נהנה מבשר קדשי קדשים שנטמא (קודם זריקה)',['impure flesh','before sprinkling is parenthetical in source']),('portions','Benefit from lesser-sacred portions after they were raised is exempt','ומאימורי קדשים קלין לאחר שהעלן דפטור',['after raising portions to altar'])]:
 c('rava.exempt.'+key,'10a:2',prop,quote,cond,holder='רבא',status='Rava says all agree; interpreted against lost-value premise below')
q('obvious','10a:3','Is exemption obvious, since what loss has he caused?')
c('no.loss','10a:3','No compensable loss seems caused',mode='hypothetical',status='premise of obviousness challenge')
c('burn.hyp','10a:4','One might impose liability because priests have a burning command for impure most-sacred meat','מהו דתימא בשר קדשי קדשים שנטמא אית ליה מצות שריפה לכהנים',mode='hypothetical',status='rejected as basis for liability')
c('turn.hyp','10a:4','One might impose liability because of command to turn altar portions with a fork','אימורי קדשים קלין איכא מצוה להפוכי בצינורא',mode='hypothetical',status='rejected as basis for liability')
c('rava.reject','10a:4','These service requirements do not create the proposed liability','קמ"ל דלא',question='obvious',status='asserted negation; preceding liability hypotheses rejected')
e('rava.reject','obvious','answer','10a:4');e('rava.reject','burn.hyp','correction','10a:4');e('rava.reject','turn.hyp','correction','10a:4')
c('rava.known','10a:5','Post-offering sin-offering benefit payment goes to Dead Sea only when benefit became known before atonement','הני מילי דאתידע ליה קמי כפרה',['knowledge before atonement','sin-offering subsequently offered'],holder='רבא')
c('rava.later','10a:5','When knowledge arises after atonement, payment goes to voluntary fund','אבל לאחר כפרה יפלו לנדבה',['knowledge after atonement'],holder='רבא')
q('rava.why','10a:5','Why send the later-known payment to voluntary fund?',quote='מאי טעמא')
c('no.destroy','10a:5','One does not initially designate money for destruction','אין מפרישין מתחלה לאיבוד',holder='רבא',question='rava.why')
e('rava.known','sin.post','qualification','10a:5');e('no.destroy','rava.why','answer','10a:5');e('no.destroy','rava.later','support','10a:5')

c('six.start','10a:6','Handful, frankincense, incense, priest’s meal-offering, anointed priest’s meal-offering, and libation meal-offering: meilah from consecration',holder='anonymous Mishnah')
inv('10a:7','six.invalid','These six sacred items','קדשן בכלי הוכשר ליפסל בטבול יום ובמחוסר כפורים ובלינה','after vessel sanctification')
for typ in ['notar','tumah']:c('six.'+typ,'10a:7','These items incur '+typ+' liability','וחייבין עליו משום נותר ומשום טמא',['after vessel sanctification'],holder='anonymous Mishnah')
c('six.nopiggul','10a:7','These items have no piggul liability','ופיגול אין בה',holder='anonymous Mishnah')
for typ in ['piggul','notar','tumah']:c('matir.'+typ,'10a:8','An item having permitting rites incurs '+typ+' liability only after its permitting rites are offered',cond=['item has matirim','matirim offered'],holder='anonymous Mishnah')
for typ in ['notar','tumah']:c('nomatir.'+typ,'10a:9','An item without permitting rites incurs '+typ+' liability upon sanctification in a vessel','וכל שאין לו מתירין כיון שקידש בכלי חייבין עליו משום נותר וטמא',['no matirim','vessel sanctification'],holder='anonymous Mishnah')
c('nomatir.nopiggul','10a:9','An item without permitting rites has no piggul liability','ופיגול אין בה',holder='anonymous Mishnah',cond=['no matirim'])
q('derive','10b:1','What is the scriptural basis?',quote='מה"מ')
c('tumah.hyp','10b:1','Perhaps tumah liability applies only to items with permitting rites','יכול אין חייבין משום טומאה אלא בדבר שיש לו מתירין',holder='anonymous baraita',mode='hypothetical',status='rejected by inclusive verse in 10b:4')
for key,prop,anchor in [('one','Piggul involves one awareness','פיגול שהוא בידיעה אחת'),('fixed','Piggul has fixed offering','וקרבנו קבוע'),('exception','Piggul has no permitted exception','ולא הותר מכללו'),('matir','Piggul liability applies only to items with permitting rites','אין חייבין אלא על דבר שיש לו מתירין')]:c('piggul.'+key,'10b:2',prop,anchor,holder='anonymous baraita',status='premise of proposed a fortiori')
for key,prop,anchor in [('two','Tumah involves two awarenesses','טומאה שהיא בשתי ידיעות'),('variable','Tumah offering varies by means','וקרבנו עולה ויורד'),('exception','Tumah has a permitted exception','והותרה מכללה')]:c('tumah.'+key,'10b:3',prop,anchor,holder='anonymous baraita',status='premise of rejected a fortiori restriction')
q('afortiori','10b:3','Should not tumah, a fortiori, apply only to items with permitting rites?',quote='אינו דין שלא יהא חייב אלא על דבר שיש לו מתירין')
c('allholy','10b:4','Leviticus 22:3 speaks of all sacred items','תלמוד לומר (ויקרא כב, ג) אמור אליהם לדורותיכם כל איש אשר יקרב מכל זרעכם וגו\' בכל הקדשים הכתוב מדבר',holder='anonymous baraita',question='derive')
c('immediate','10b:4','Perhaps liability begins immediately','יכול יהו חייבין עליהן מיד',holder='anonymous baraita',mode='hypothetical',status='rejected by אשר יקרב')
c('approach','10b:4','אשר יקרב restricts the timing of liability','תלמוד לומר אשר יקרב',holder='anonymous baraita',status='explicated by R. Elazar next')
q('touch','10b:5','Can mere touching incur this liability?',quote='אמר רבי אלעזר וכי יש נוגע שהוא חייב')
c('elazar.matir','10b:5','Where there are permitting rites, no liability until they are offered','כל דבר שיש לו מתירין אינו חייב עד שיקרבו מתירין',['item has matirim'],holder='רבי אלעזר',question='touch')
c('elazar.vessel','10b:5','Where there are no permitting rites, no liability until vessel sanctification','וכל דבר שאין לו מתירין אינו חייב עד שיקדש בכלי',['item has no matirim'],holder='רבי אלעזר',question='touch')
e('allholy','tumah.hyp','correction','10b:4');e('allholy','afortiori','answer','10b:4');e('approach','immediate','correction','10b:4');e('elazar.matir','approach','qualification','10b:5');e('elazar.vessel','approach','qualification','10b:5')

for key,item in [('offspring','Offspring of sin-offering'),('substitute','Substitute of sin-offering'),('deadowner','Sin-offering whose owner died')]:c('die.'+key,'10b:7',item+' must die',holder='anonymous Mishnah')
case=['sin-offering past its year or lost and found blemished as coordinated in source','owners already atoned']
for key,prop,anchor in [('die','Must die','תמות'),('substitute','Does not effect substitution','ואינה עושה תמורה'),('benefit','Benefit prohibited','ולא נהנין'),('meilah','No meilah','ולא מועלין')]:
 c('after.'+key,'10b:8',prop,anchor,case,holder='anonymous Mishnah',unc=['Scope/coordination of שעיברה שנתה ושאבדה ונמצאת בעלת מום retained; no imported harmonization.'])
before=['same coordinated cases as 10b:8','owners not yet atoned']
for key,prop,anchor in [('graze','Graze until blemished','תרעה עד שתסתאב'),('sell','Sell it','ותמכר'),('buy','Buy another offering with its money','ויקחו בדמיה אחרת'),('substitute','Effects substitution','ועושה תמורה'),('meilah','Subject to meilah','ומועלין בה')]:c('before.'+key,'11a:1',prop,anchor,before,holder='anonymous Mishnah',unc=['Temporal condition explicit; coordination of cases inherited without expansion.'])
q('different','11a:2','Why is first clause unqualified whereas the latter distinguishes cases?')
c('first.definite','11a:3','First clause is definite','רישא פסיקא ליה',question='different')
c('last.variable','11a:3','Latter clause is not definite','סיפא לא פסיקא ליה',question='different')
e('first.definite','different','answer','11a:3');e('last.variable','different','answer','11a:3')
q('duplicate','11a:4','Was this not already taught in Temurah?',quote='הא תנא ליה גבי תמורה')
c('there.temurah','11a:4','It was taught there for substitution law','תנא התם משום תמורה',question='duplicate')
c('here.meilah','11a:4','It is taught here for meilah law','תנא הכא משום מעילה',question='duplicate')
e('there.temurah','duplicate','answer','11a:4');e('here.meilah','duplicate','answer','11a:4')
for key,prop,anchor in [('benefit','Benefit from money designated for Nazirite offerings prohibited','המפריש מעות לנזירותו לא נהנין'),('meilah','Money designated for Nazirite offerings has no meilah','ולא מועלין'),('reason','All the funds could be used for peace-offerings','מפני שהן ראוין לבא כולן שלמים')]:c('nazir.'+key,'11a:5',prop,anchor,holder='anonymous Mishnah',cond=['undifferentiated Nazirite funds; clarified by ensuing distinction'])
e('nazir.reason','nazir.meilah','support','11a:5')
c('nazir.dead.unspecified','11a:6','Upon death, unspecified funds go to voluntary offerings','מת והיו לו מעות סתומין יפלו לנדבה',['Nazirite died','unspecified funds'],holder='anonymous Mishnah')
for key,prop,anchor in [('sea','Specified sin-offering money goes to Dead Sea','מעות מפורשים דמי חטאת ילכו לים המלח'),('benefit','Benefit forbidden','לא נהנין'),('meilah','No meilah','ולא מועלין')]:c('nazir.sin.'+key,'11a:6',prop,anchor,['Nazirite died','specified sin-offering funds'],holder='anonymous Mishnah')
for key,prop,anchor,kind in [('burnt','Buy burnt-offering','דמי עולה יביאו עולה','burnt'),('meilah','Meilah applies to its funds','ומועלין בהן','burnt'),('peace','Buy peace-offerings','דמי שלמים יביאו שלמים','peace'),('day','Peace-offerings eaten for one day','ונאכלין ליום אחד','peace'),('bread','No bread required','ואין טעונין לחם','peace')]:c('nazir.'+key,'11a:7',prop,anchor,['Nazirite died','specified '+kind+'-offering funds'],holder='anonymous Mishnah')

# Necessary continuation: comparison is proposed, then rejected on eligibility grounds.
q('birds','11a:8','Why not also teach one designating money for bird pairs?',quote='מתקיף לה ריש לקיש וליתני נמי המפריש מעות לקינים')
rec('attributions','11a:8',dict(surface='ריש לקיש',role='speaker',candidates=['ריש לקיש'],scope=questions['birds'],transmission_chain=[]),'ריש לקיש',links=[questions['birds']])
c('birds.prohibit','11a:9','Proposed bird-pair parallel: benefit forbidden','לא נהנין',['funds for bird pairs'],holder='ריש לקיש',mode='hypothetical',status='parallel rejected by Rava')
c('birds.nomeilah','11a:9','Proposed bird-pair parallel: no meilah','ולא מועלין',['funds for bird pairs'],holder='ריש לקיש',mode='hypothetical',status='parallel rejected by Rava')
c('birds.reason','11a:9','Proposed reason: funds can buy turtledoves too young or pigeons too old','מפני שהן ראוין להביא תורין שלא הגיע זמנן ובני יונה שעבר זמנן',holder='ריש לקיש',mode='hypothetical',status='comparison rejected, not validated use of sacred funds')
c('rava.peace','11a:10','Torah allows unspecified Nazirite funds to buy peace-offerings','אמר רבא אמרה תורה במעות סתומין הבא שלמים',holder='רבא',question='birds')
c('rava.birds','11a:10','Torah does not authorize too-young turtledoves; such birds are unfit for altar','אמרה תורה הבא תורין שלא הגיע זמנן אינן ראויין למזבח',holder='רבא',question='birds',unc=['אמרה תורה הבא תורין is rhetorical in the contrast; not an affirmative command.'])
e('rava.birds','birds','answer','11a:10');e('rava.birds','birds.reason','distinction','11a:10');e('rava.peace','nazir.reason','support','11a:10')

# Explicit relational completion from second omission pass.
for a,b,r in [('rabbis','invalidonly','8a:6'),('ifremain','huna','8b:10'),('firstpart','huna','8b:10'),('meal.lack.oil','mealhyp','9a:1'),('meal.lack.frankincense','mealhyp','9a:1'),('twotannaim','ishmael.repeat','9a:6'),('twotannaim','ishmael.other','9a:6'),('shimon.first','sin.post','9b:10'),('rabbis.last','payment.altar','10a:1')]:
 e(a,b,'qualification' if a in ['twotannaim','shimon.first','rabbis.last','rabbis'] else ('objection' if a.startswith('meal.lack') else 'support'),r)

# Primary ownership: exact whole-segment interval is a deliberate structure granularity.
titles={
 '8a:3':'Mishnah: bird sin-offering stages','8a:4':'Mishnah: post-sprinkling consequences','8a:5':'Gemara: disqualification versus imparting impurity','8a:6':'Identification of Mishnah and beginning Abba Shaul citation','8b:1':'Continuation of Abba Shaul citation','8b:2':'R. Meir and Sages on tevul yom','8b:3':'Rava explains Abba Shaul','8b:4':'Rava explains Meir and Rabbis','8b:5':'Post-sprinkling prohibition inference and question','8b:6':'R. Hanina restricts to exited meat under R. Akiva','8b:7':'Rav Huna reports Rav and Mishnah wording','8b:8':'Rav Adda bar Ahava reports Rav and different wording','8b:9':'Scriptural challenge to Rav Huna','8b:10':'Conditional remainder and earlier-clause interpretation','8b:11':'Rav Aha’s meal-offering comparison','9a:1':'Baraita excludes deficient meal-offering','9a:2':'Additional verse distinguishes meal-offering','9a:3':'Bird-offering baraita objection','9a:4':'Objector’s distributed-case answer','9a:5':'Return to school of R. Ishmael','9a:6':'Contradictory school traditions reconciled as two tannaim','9a:7':'Mishnah: bird burnt-offering stages','9a:8':'Mishnah: burned bulls and goats','9a:9':'Mishnah: animal burnt-offering','9a:10':'Mishnah: sin, guilt and communal peace offerings','9a:11':'Mishnah: two loaves','9a:12':'Mishnah: showbread initial stages','9a:13':'Mishnah: showbread after bowls offered','9a:14':'Mishnah: meal-offering initial stages','9a:15':'Mishnah: meal-offering after handful','9a:16':'Rav/R. Yohanan dispute over altar ash','9a:17':'Agreement before and dispute after ash separation','9a:18':'Reasons for ash positions','9a:19':'Mishnah objection and Rav’s reading','9b:1':'Fallen coal baraita and inference','9b:2':'First-version challenge and coal distinction','9b:3':'Alternative version challenge to R. Yohanan','9b:4':'R. Yohanan’s proposed response','9b:5':'Rav/Levi dispute over destination of payment','9b:6':'Baraita support for Levi and incense identification','9b:7':'Baraita support for Rav: offering-money cases','9b:8':'Baraita continuation: destinations','9b:9':'Internal contradiction in baraita','9b:10':'First clause assigned to R. Shimon','10a:1':'Latter clause Rabbis; transmitted Abaye confirmation','10a:2':'Rava’s agreed exemptions','10a:3':'Obviousness challenge','10a:4':'Rejected service-value grounds for liability','10a:5':'Rava distinguishes timing of knowledge','10a:6':'Mishnah: six altar items','10a:7':'Vessel sanctification consequences','10a:8':'General rule with permitting rites','10a:9':'General rule without permitting rites','10b:1':'Derivation question and restrictive possibility','10b:2':'Piggul premises of a fortiori','10b:3':'Tumah premises and proposed a fortiori','10b:4':'Inclusive verse and timing restriction','10b:5':'R. Elazar explains approach as fitness stage','10b:6':'Chapter completion marker','10b:7':'Mishnah: three sin-offerings that die','10b:8':'Other sin-offerings after atonement','11a:1':'Other sin-offerings before atonement','11a:2':'Why clauses differ in conditional structure','11a:3':'Definite versus variable clauses','11a:4':'Why taught in Temurah and Meilah','11a:5':'Mishnah: unspecified Nazirite money','11a:6':'Nazirite death: unspecified and sin-offering funds','11a:7':'Nazirite death: burnt- and peace-offering funds','11a:8':'Resh Lakish’s bird-pair analogy','11a:9':'Proposed consequences and rationale','11a:10':'Rava rejects invalid-bird comparison'}
annotated=j['core_refs']+[ref(x) for x in ['11a:8','11a:9','11a:10']]
for r in annotated:
 short=r.split(' ',1)[1];boundary='open_both' if short in ['8a:6','8b:1','8b:11','9a:1','9b:10','10a:1','10b:8','11a:1','11a:6','11a:7','11a:8','11a:9'] else 'closed'
 rec('structure',r,dict(title=titles[short],primary=True,boundary=boundary,legacy_ids=[]),origin='editorial_inference')
 if short=='10b:6':continue
 attrib=[z['content']['surface'] for z in records if z['layer']=='attributions' and any(v['segment_id']==r for v in z['evidence'])]
 rec('utterances',r,dict(textual_voice='; '.join(dict.fromkeys(attrib)) or 'anonymous',discourse_role=titles[short],composition='composite' if len([z for z in records if z['layer'] in ['claims','questions'] and any(v['segment_id']==r for v in z['evidence'])])>1 else 'atomic'))

coverage=[]
for r in j['core_refs']:
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  found=[z['id'] for z in records if z['layer']==layer and any(v['segment_id']==r for v in z['evidence'])]
  marker=r=='Meilah 10b:6'
  if layer=='reconciliation':
   found=[z['id'] for z in records if z['layer'] in ['claims','questions'] and any(v['segment_id']==r for v in z['evidence'])]
   rationale='Second source-based omission pass checked each clause, conditional stage, negation, attribution and relation against this original segment and continuation. '+notes.get(r,'')
   result='records_found' if found else 'not_applicable'
  elif found:rationale='Independently inventoried source-grounded records; exact Unicode evidence validated.';result='records_found'
  elif marker:rationale='Chapter completion typography contains no legal proposition, dialogic utterance, attribution, question, position or argument relation.';result='not_applicable'
  elif layer=='questions':rationale='No separate explicit question or necessary additional comparable-answer question after clause-level reading; propositions and conditions inventoried in claims/positions.';result='none_found_after_pass'
  elif layer=='edges':rationale='No additional independently evidenced relation beyond records anchored at responding/continuing segments; adjacency alone not promoted to argument relation.';result='none_found_after_pass'
  else:rationale='No independent record in this layer; continuation evidence and linked records account for the local source function.';result='none_found_after_pass'
  coverage.append(dict(segment_id=r,layer=layer,extraction_state='completed',extraction_result=result,record_ids=found,rationale=rationale))

tails=[
 '9a:3 parenthetical (ור\' אבין): exact objector identity unresolved; father of Shmuel is not Shmuel.',
 'Rav’s squeezing ruling has two explicit divergent transmitters; no reconciliation or final selection is supplied in this local text.',
 '9a:6 refers to an external tannaitic contrast without naming all its parties here; do not reconstruct them from outside knowledge.',
 '9a:11 parenthetical (ובלינה) and 10a:2 parenthetical (קודם זריקה) retained as edition features.',
 '10b:8 coordinated age/loss/blemish cases are preserved without importing alternative editions or resolving their legal combination.',
 '10b:2–3 awareness counts and offering features are inventoried as stated; no expanded external explanations imported.',
 'No practical halakhic ruling or persistent personal opinion inferred from a local objection or hypothetical anonymous אמר לך reply.'
]
proposal=dict(schema_version='2.0.0-production',tractate='Meilah',owner='source_only_independent_reader:/root/reader_meilah_supplement003a',epoch=1,source_sha256=j['source']['sha256'],protocol_sha256=j['common_documents'][0]['sha256'],schema_sha256=j['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id='/root/reader_meilah_supplement003a',model_id=None),records=records,coverage=coverage,open_tails=tails)

# Integrity validation does not substitute for the manual semantic omission pass above.
import jsonschema
jsonschema.validate(proposal,json.loads(Path(j['common_documents'][1]['path']).read_bytes()))
rid={x['id'] for x in records};assert len(rid)==len(records)
for x in records:
 for v in x['evidence']:assert texts[v['segment_id']][v['start_char']:v['end_char']]==v['quote']
 for link in x['links']:assert link in rid,(x['id'],link)
 if x['layer']=='positions':
  assert x['content']['claim_id'] in rid
  assert x['content']['question_id'] is None or x['content']['question_id'] in rid
 if x['layer']=='edges':assert x['content']['source_id'] in rid and x['content']['target_id'] in rid
for r in j['core_refs']:
 primary=[v for x in records if x['layer']=='structure' and x['content']['primary'] for v in x['evidence'] if v['segment_id']==r]
 assert [(v['start_char'],v['end_char']) for v in primary]==[(0,len(texts[r]))]
assert len(coverage)==68*8
read_context=[ref('8a:1'),ref('8a:2')]+[ref(f'11a:{i}') for i in range(8,18)]+[ref(f'11b:{i}') for i in range(1,20)]
artifact=dict(artifact_kind='frozen_source_only_independent_reading',job_id=j['job_id'],cohort=j['cohort'],neutral_job_binding={'path':str(JOB),'sha256':sha(JOB)},source_binding=j['source'],common_document_bindings=j['common_documents'],core_refs=j['core_refs'],core_count=68,context_refs=read_context,semantically_annotated_context_refs=[ref(f'11a:{i}') for i in range(8,11)],incidental_context_note='Displayed original text through 11b:19; only 11a:8–10 needed and semantically inventoried for the final core discussion. Other read context does not enlarge core counts or claimed semantic coverage.',provenance={'agent_id':'/root/reader_meilah_supplement003a','model_id':None,'source_only':True,'production_annotations_read':False,'other_readings_read':False,'annotated_handoff_read':False,'read_materials':['neutral job','three bound common documents','pinned original source'],'initial_reading_preserved':True,'comparison_performed':False,'ml_eligible':False,'scholarly_status':'AI provisional, unreviewed; not human certification','source_edition':{k:source[k] for k in ['title','versionTitle','versionSource','license']}},proposal=proposal,reconciliation={'performed':True,'method':'Manual second pass over all 68 original core strings, comparing each legal stage, prohibition, liability, inference, question, explicit alternative and transmission with the independently built inventory; added relations and preserved edition/identity ambiguities. No producer comparison.','remaining_coverage_gaps':[],'remaining_interpretive_uncertainties':tails},validation={'schema':'passed','source_and_common_hashes':'passed','all_evidence_unicode_slices':'passed','record_ids_and_links':'passed','primary_structure_exact_partition':'passed','core_layer_cells':len(coverage)},counts={'records_by_layer':dict(Counter(x['layer'] for x in records)),'core_refs':68,'context_refs_read':len(read_context),'context_refs_semantically_annotated':3,'core_layer_cells':len(coverage)})
out=ROOT/'readings/meilah_supplement003a.json';out.parent.mkdir(exist_ok=True)
assert not out.exists(),'Frozen artifact must not be overwritten'
data=(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
with out.open('xb') as f:f.write(data)
digest=hashlib.sha256(data).hexdigest()
with Path(str(out)+'.sha256').open('x',encoding='ascii') as f:f.write(digest+'  '+out.name+'\n')
print(json.dumps({'output':str(out),'sha256':digest,'counts':artifact['counts'],'remaining_coverage_gaps':[]},ensure_ascii=False))
