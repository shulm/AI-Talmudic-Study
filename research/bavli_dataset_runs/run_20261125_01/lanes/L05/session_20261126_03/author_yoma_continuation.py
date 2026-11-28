import sys,json,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent.parent/'session_20261126_02'))
import author_yoma_opening as a
a.R=[]
def add(k,l,ii,c,links=(),q=None,origin='source_paraphrase',unc=()):
 rid='yom.s03.'+k;a.R.append(dict(id=rid,layer=l,evidence=[a.ev(i,q) for i in ii],content=c,links=list(links),origin=origin,uncertainty=list(unc)));return rid
a.add=add;claim,edge=a.claim,a.edge
s=add('origin','structure',list(range(39,64)),dict(title='מילואים וסיני: קושיות, ברייתות, זמנים וענן',primary=True,boundary='open_both',legacy_ids=[]),unc=['Continues previous derivation; return to מילואים premise follows at4b:12; no whole-sugya closure asserted.'])
add('speech','structure',[64],dict(title='קריאה לפני דיבור ורשות למסור דברים',primary=True,boundary='closed',legacy_ids=[]))
add('continuation','edges',[39],dict(source_id='yom.s02.derivation.structure',target_id=s,relation='continuation',explicitness='source_explicit'),['yom.s02.derivation.structure',s])
for i in range(39,65):add('u'+str(i),'utterances',[i],dict(textual_voice='explicit dialogue, baraita and anonymous argument',discourse_role='objection, derivation, interpretation or report',composition='composite'))
rows=[
(39,'rlchallenge','ריש לקיש מקשה על לימוד רבי יוחנן ממילואים: לכאורה כל הכתוב צריך לעכב גם כאן.','ריש לקיש','challenged',['אם הפרישה נלמדת ממילואים']),
(40,'substitute','לשון מתקינין כהן אחר, לעומת מפרישין, מקשה על עיכוב כל הפרטים; ניסיון לזהות מתקינין עם מפרישין נדחה מהבדל הלשונות.',None,'asserted',['הכנת כהן אחר תחת הכהן הגדול']),
(41,'sinai','ריש לקיש לומד מסיני בניין אב שכל הנכנס למחנה שכינה טעון פרישת שישה.','ריש לקיש','asserted',['כניסה למחנה שכינה']),
(42,'benbetera','לשיטת סיני, המשנה המציינת שבעה מועמדת כרבי יהודה בן בתירא החושש לטומאת ביתו.',None,'asserted',['יישוב שבעה שבמשנה עם פרישת שישה']),
(43,'house','טומאת ביתו משלימה את משפט ההסבר מן העמוד הקודם.',None,'asserted',['המשך חייש של3b:15']),
(44,'sprinkle','רבי יוחנן מצביע על הזאה כל שבעה, המתאימה למילואים אך לא לסיני.','רבי יוחנן','asserted',['כהן יום הכיפורים וכהן פרה']),
(45,'bloodobjection','ריש לקיש משיב שגם במילואים היה דם וכאן מים.','ריש לקיש','challenged',[]),
(45,'water','מסורת רבי חייא עונה: נכנסו מים תחת דם.','רבי חייא — ברייתא','asserted',[]),
(45,'extra','לשיטת ריש לקיש ההזאה היא מעלה בעלמא.','ריש לקיש','asserted',['הזאה לעומת עצם פרישה מסיני']),
(46,'baraitay','ברייתא תומכת ברבי יוחנן: בזאת מפנה לענין המילואים, שבו אהרן פרש שבעה ושימש יום אחד ומשה לימדו כדי לחנכו.','ברייתא התומכת ברבי יוחנן','asserted',[]),
(47,'later','גם לדורות הכהן הגדול פורש שבעה ומשמש יום אחד, ושני תלמידי חכמים מתלמידי משה ולא צדוקים מלמדים אותו.','ברייתא','asserted',['לדורות']),
(48,'bothseparate','הברייתא משווה שבעת ימי פרישת כהן גדול לפרישת שורף הפרה, כל אחד ללשכתו.','ברייתא','asserted',[]),
(48,'bothsprinkle','שני הכהנים מקבלים הזאה כל שבעה מכל חטאות שהיו שם.','ברייתא','asserted',[]),
(49,'wateragain','הברייתא משיבה לפער בין דם למים שנכנסו מים תחת דם.','ברייתא','asserted',[]),
(49,'twoacts','הברייתא דורשת לעשות למעשי פרה ולכפר למעשי יום הכיפורים.','ברייתא','asserted',[]),
(50,'twoderivations','בחירת בזאת במקום בזה או באלה מאפשרת גם הוראת הקרבנות וגם לימוד הפרישה.',None,'asserted',[]),
(51,'notfirstonly','הפסוק כאשר עשה שולל צמצום הפרישה ליום הכיפורים הראשון או לכהן הגדול הראשון בלבד.',None,'asserted',['לימוד המשכיות לדורות']),
(52,'galilean','רבי יוסי הגלילי מפרש שמשה התכסה ונתקדש בענן לקבל תורה לישראל בקדושה, לאחר עשרת הדברות ובראשית ארבעים יום.','רבי יוסי הגלילי','asserted',[]),
(53,'akiva','רבי עקיבא מפרש וישכון מראש חודש.','רבי עקיבא','asserted',[]),
(54,'akivacont','בפירוש רבי עקיבא הענן מכסה את ההר, משה וכל ישראל עומדים והקריאה חולקת למשה כבוד.','רבי עקיבא — המשך','asserted',[]),
(54,'natan','רבי נתן מפרש את הפרישה כמרוק אכילה ושתייה כדי לשומו כמלאכי השרת.','רבי נתן','asserted',[]),
(55,'matya','רבי מתיא בן חרש מפרש לאיים על משה כדי שהתורה תינתן באימה רתת וזיע.','רבי מתיא בן חרש','asserted',[]),
(55,'rav','רב במסירת רב אדא בר מתנה דורש במקום גילה שם תהא רעדה.','רב','asserted',[]),
(56,'dates','ברייתא: תנא קמא סובר תורה ניתנה בשישה בחודש ורבי יוסי בשבעה; לפי שני הפירושים העלייה בשבעה.','ברייתא','asserted',[]),
(57,'galileanmap','רבי יוסי הגלילי מתפרש כתנא קמא: תורה בשישה, ולכן ששת ימי הענן למשה הם לאחר עשרת הדברות.','רבי יוסי הגלילי — פירוש הדיון','asserted',[]),
(57,'galileanreject','פירוש שהענן מראש חודש על ההר והקריאה ביום השביעי לקבלת הדברות אינו מתאים למתן תורה בשישה והסתלקות הענן אז.',None,'asserted',['לפי שיטת מתן תורה בשישה']),
(58,'akivamap','רבי עקיבא מתפרש כרבי יוסי שתורה בשבעה; עשרים וארבעה ימי סיון ושישה עשר בתמוז הם ארבעים, ובשבעה עשר נשברו הלוחות.','רבי עקיבא — פירוש הדיון','asserted',[]),
(59,'inclusive','רבי יוסי הגלילי משיב שששת ימי הפרישה נכללים בארבעים יום בהר, ואינם נוספים להם.','רבי יוסי הגלילי — תשובה משוחזרת','asserted',[]),
(60,'elazar','רבי אלעזר מפרש את הקריאה למשה כחלוקת כבוד לו בפני כל ישראל.','רבי אלעזר','asserted',[]),
(61,'privatevoice','ברייתא אחרת דורשת קול לו קול אליו: משה שמע וישראל לא שמעו.','ברייתא','asserted',[]),
(61,'sites','תירוץ אחד מבחין בין סיני לאוהל מועד.',None,'asserted',['תירוץ חלופי לסתירת השמיעה']),
(61,'calltalk','תירוץ חלופי מבחין בין קריאה לדיבור.',None,'asserted',['חלופה לתירוץ המקומות']),
(62,'cloud','הסתירה בין ולא יכול משה לבוא לבין ויבא משה בתוך הענן נענית שהקב״ה תפסו והביאו בענן.',None,'asserted',[]),
(63,'path','דבי רבי ישמעאל לומדים בתוך בתוך מקריעת הים: כשם ששם שביל, כך בענן שביל.','דבי רבי ישמעאל','asserted',[]),
(64,'callfirst','הקדמת קריאה לדיבור מלמדת דרך ארץ לקרוא לחבר לפני שמדברים אליו; רבי חנינא אומר כך.','רבי חנינא','asserted',['לפני אמירת דבר לחבר']),
(64,'permission','אין למסור דבר שנאמר לחבר עד שיאמר לו לך אמור; הדרשה מלאמר.','רבה — לצד נוסח מוסגר אחר','asserted',['ללא אמירת לך אמור'])]
cs={}
for i,k,p,holder,mode,cond in rows:
 un=[]
 if k=='permission':un=['Printed parenthetical alternative attribution preserved; no silent choice between רבה and musya transmission.']
 if k in ['sites','calltalk']:un=['Do not conflate alternative resolutions or infer a universal hearing rule.']
 cs[k]=claim(k,i,p,holder=holder,mode=mode,cond=cond,unc=un)
 # Full cross-amud evidence belongs to the interrupted proposition.
 if k=='benbetera':
  for r in a.R:
   if r['id'].startswith('yom.s03.'+k):r['evidence'].append(a.ev(43))
 if k=='akivacont':
  for r in a.R:
   if r['id'].startswith('yom.s03.'+k):r['evidence'].append(a.ev(53))
qs={}
for i,k,p,conds,links in [(39,'from','מהיכן רבי יוחנן לומד פרישה?',[],['rlchallenge']),(41,'rlfrom','מה מקור ריש לקיש לפרישה?',['לאחר קושייתו על מילואים'],['sinai']),(42,'seven','כיצד משנת שבעה מתיישבת עם סיני שישה?',['לשיטת לימוד מסיני'],['sinai','benbetera']),(44,'sprinkleq','היכן הזאה בסיני?',['לריש לקיש','שני הכהנים מוזים כל שבעה'],['sprinkle','extra']),(45,'bloodq','האם מילואים אכן מתאימים אם שם דם וכאן מים?',['לימוד הזאה ממילואים'],['bloodobjection','water']),(50,'bazot','האם בזאת אינו דרוש לקרבנות עצמם?',['דרשת הפרישה מן המילה בזאת'],['baraitay','twoderivations']),(51,'anotherverse','מדוע הוסיפה הברייתא ואומר?',['שתי דרשות הפרישה בברייתא'],['twoacts','notfirstonly']),(55,'joy','מה פירוש וגילו ברעדה?',['צירוף שמחה ויראה בפסוק'],['rav']),(56,'dispute','במה חלוקים רבי יוסי הגלילי ורבי עקיבא?',['לגבי כיסוי הענן וזמנו'],['galilean','akiva','dates']),(59,'fortysix','כיצד שיטת רבי יוסי הגלילי תתאים לשבירת לוחות בשבעה עשר?',['אם שישה נוספים לארבעים היו מגיעים לעשרים ושלושה'],['galilean','inclusive']),(62,'cloudq','כיצד ולא יכול לבוא מתיישב עם ויבא בתוך הענן?',['שני הפסוקים במשה'],['cloud','path']),(64,'order','מדוע קריאה קודמת לדיבור?',[],['callfirst']),(64,'disclose','מניין שאין למסור דבר לחבר ללא רשות?',['עד שיאמר לו לך אמור'],['permission'])]:
 qs[k]=add('q.'+k,'questions',[i],dict(formulation=p,question_origin='explicit',conditions=conds,answer_set_status='partial'),[cs[x] for x in links])
for n,(i,c,q,rel) in enumerate([(41,'sinai','rlfrom','answer'),(42,'benbetera','seven','answer'),(45,'extra','sprinkleq','answer'),(45,'water','bloodq','answer'),(50,'twoderivations','bazot','answer'),(51,'notfirstonly','anotherverse','answer'),(55,'rav','joy','answer'),(57,'galileanmap','dispute','answer'),(58,'akivamap','dispute','answer'),(59,'inclusive','fortysix','answer'),(62,'cloud','cloudq','answer'),(63,'path','cloudq','answer'),(64,'callfirst','order','answer'),(64,'permission','disclose','answer')]):edge('eq'+str(n),i,cs[c],qs[q],rel)
for n,(i,x,y,rel) in enumerate([(40,'substitute','rlchallenge','support'),(45,'bloodobjection','sprinkle','objection'),(45,'water','bloodobjection','answer'),(46,'baraitay','rlchallenge','objection'),(49,'wateragain','bothsprinkle','support'),(52,'galilean','sinai','support'),(57,'galileanreject','galileanmap','support'),(61,'privatevoice','elazar','objection'),(61,'sites','privatevoice','answer'),(61,'calltalk','privatevoice','answer')]):edge('ec'+str(n),i,cs[x],cs[y],rel)
add('ravreport','attributions',[55],dict(surface='רב אדא בר מתנה',role='transmitter',candidates=['רב אדא בר מתנה'],scope='במקום גילה שם תהא רעדה',transmission_chain=['רב אדא בר מתנה','רב']),[cs['rav']])
add('zerika_versions','attributions',[62],dict(surface='רבי זריקא / רבי אלעזר',role='speaker',candidates=['רבי זריקא','רבי אלעזר'],scope='סתירת פסוקי הענן: שתי מסירות מי רמי קראי',transmission_chain=[]),[qs['cloudq']],unc=['First version Zerika asks before Elazar; alternative Zerika reports that Elazar posed it. No single speaker chosen.'])
C=[]
for i in range(39,65):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in a.R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==a.inv[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=a.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Actual source omission reread: six/seven-day distinction, substitute preparation, blood/water rejoinder, two supporting baraitot, chronology-inclusive six days, two hearing resolutions and variant speakers retained. Question conditions and linked source claims explicitly provided. Context read through5a:9; next return to מילואים premise unprocessed.'))
p={k:a.job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.R,coverage=C,open_tails=['yom.s02.derivation.structure',s])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=Path(__file__).parent/'yoma_continuation_004.json';assert not out.exists();out.write_bytes(b);print(len(a.R),hashlib.sha256(b).hexdigest())
