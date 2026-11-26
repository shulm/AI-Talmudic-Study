import author_horayot_opening as h
import json,hashlib
from pathlib import Path
a=h.a;a.R=[];add=h.add;claim,question,edge=a.claim,a.question,a.edge
for k,lo,hi,title in [('known',93,103,'דבר שהצדוקים מודין בו: פירוש דוגמאות המשנה'),('plow',103,110,'עקירת מלאכה אחת ושאלת חרישה'),('seventh',110,113,'אין שבת בשביעית'),('court',113,118,'מופלא והרכב בית הדין'),('intention',118,121,'שגגת בית הדין ושגגת הציבור')]:add('b4.'+k,'structure',list(range(lo,hi)),dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
for i in range(93,121):add('b4.u'+str(i),'utterances',[i],dict(textual_voice='משנה' if i in [113,114,118] else 'anonymous dialectic and explicit reports',discourse_role='ruling, quoted error, objection or interpretation',composition='composite'))
rows=[
(93,'shmuel','שמואל במסירת רב יהודה פוטר הוראה בדבר שהצדוקים מודין בו ומחייב רק בדבר שאינם מודין בו.','שמואל','asserted',['דבר שהצדוקים מודין בו לעומת אינם מודין']),
(93,'read','טעם הפטור הוא זיל קרי בי רב — דבר מפורש שהיה אפשר ללמוד.',None,'asserted',[]),
(94,'count','הקושיה טוענת ששומרת יום מפורשת בוספרה לה, שסופרת אחד לאחד.',None,'asserted',[]),
(95,'haarah1','מוצע שההוראה השגויה התירה העראה ואסרה רק גמר ביאה.',None,'hypothetical',[]),
(95,'haarahverse','נדחה שהעראה עצמה מפורשת באת מקורה הערה.',None,'asserted',[]),
(96,'unnatural','מוצע שהתירו שלא כדרכה ואסרו כדרכה, ונשאל ממשכבי אשה.',None,'hypothetical',[]),
(97,'combine','מוצע שהתירו דווקא העראה שלא כדרכה ולא גמר ביאה, ונשאל מדוע לא גם נדה.',None,'hypothetical',[]),
(98,'niddahonly','תשובה אחת מעמידה כדרכה, בטעות שהעראה נאסרה רק באשה דוה.',None,'hypothetical',[]),
(98,'days','תשובה חלופית: טעו שזבה רק בימים, מכל ימי זובה.',None,'hypothetical',[]),
(99,'carryingverse','הקושיה להוצאה היא שהיא כתובה בלא תוציאו משא מבתיכם.',None,'asserted',[]),
(100,'inward','לפי הקטע שבסוגריים המרובעים טעו להתיר הכנסה ולא הוצאה.',None,'hypothetical',[]),
(100,'throw','חלופה: אסרו הוצאה והכנסה והתירו מושיט וזורק.',None,'hypothetical',[]),
(101,'bowverse','הקושיה להשתחוויה היא שנאמר לא תשתחוה לאל אחר.',None,'asserted',[]),
(102,'custom','העמדה אחת: אסרו השתחוויה כדרכה והתירו שלא כדרכה.',None,'hypothetical',[]),
(102,'limbs','חלופה: אסרו רק השתחוויה בפישוט ידיים ורגליים והתירו בלא פישוט.',None,'hypothetical',[]),
(103,'plowoptions','רב יוסף מסתפק אם ביטול חרישה בלבד הוא מקצת ביחס לשבת, או כל הגוף ביחס לחרישה.','רב יוסף','unresolved',['הורו שאין חרישה בשבת']),
(104,'guardproof','מוצע להוכיח משומרת יום, שלכאורה נעקרה לגמרי.',None,'hypothetical',[]),
(105,'guardanswer','התשובה המיוחסת לרב יוסף מפנה לפירושים החלקיים שכבר ניתנו לשומרת יום.','רב יוסף — תשובה משוחזרת בדיון','asserted',[]),
(106,'carryproof','מוצע להוכיח מעקירת הוצאה בדוגמת המשנה.',None,'hypothetical',[]),
(107,'carryanswer','הדיון מפנה גם בהוצאה לפירושים החלקיים הקודמים.',None,'asserted',[]),
(108,'bowproof','מוצע להוכיח מעקירת השתחוויה בדוגמת המשנה.',None,'hypothetical',[]),
(109,'bowanswer','גם השתחוויה נדחית באמצעות הפירושים הקודמים; אין כאן הכרעה מפורשת בספק חרישה.',None,'asserted',[]),
(110,'seventherror','טעות ההוראה אין שבת בשביעית דורשת בחריש ובקציר תשבות כאילו שבת נוהגת רק בזמן חרישה.',None,'hypothetical',['הוראה שגויה; אינה דין מאומץ']),
(111,'seventhoptions','הספק הוא אם קיום שבת בשאר שנים הוא קיום מקצת, או עקירת שבת בשביעית היא עקירת הגוף.',None,'unresolved',[]),
(112,'prophet','ברייתא: נביא העוקר דבר תורה חייב; בביטול מקצת וקיום מקצת רבי שמעון פוטר, ובעבודה זרה אף היתר זמני חייב.','ברייתא מצוטטת','asserted',[]),
(112,'seventhresult','רבינא מסיק מן הברייתא שאין שבת בשביעית הוא ביטול מקצת וקיום מקצת.','רבינא','asserted',[]),
(113,'dissent','משנה פוטרת אם היודע בטעות אמר להם טועים אתם.','סתם משנה','asserted',['אמר להם טועים אתם']),
(113,'absent','משנה פוטרת אם המופלא של בית הדין לא היה שם.','סתם משנה','asserted',['מופלא של בית דין נעדר']),
(113,'members','משנה פוטרת אם אחד מהדיינים גר, ממזר, נתין או זקן שאינו ראוי לבנים.','סתם משנה','asserted',['אחד מההרכב נמנה ברשימה']),
(114,'edah','לימוד עדה עדה מחייב שכולם יהיו ראויים להוראה.','סתם משנה','asserted',[]),
(115,'learning','רב ששת ותנא דבי רבי ישמעאל מסבירים שבדבר הצדוקים הפטור מפני שהיה להם ללמוד ולא למדו, וכך גם בהיעדר המופלא.','רב ששת ותנא דבי רבי ישמעאל','asserted',[]),
(116,'chasda','רב חסדא לומד עמך בדומים לך מן והתיצבו שם עמך.','רב חסדא','challenged',[]),
(117,'shekhinah','הדיון מקשה שאולי עמך הוא לשכינה.',None,'hypothetical',[]),
(117,'nachman','רב נחמן בר יצחק מציע במקום זאת ונשאו אתך, בדומים לך.','רב נחמן בר יצחק','asserted',[]),
(118,'botherror','אם בית דין הורו שוגגים וכל הקהל עשו שוגגים מביאים פר.','סתם משנה','asserted',['בית דין שוגגים','כל הקהל שוגגים']),
(118,'courtintent','אם בית דין מזידים והקהל שוגגים מביאים כשבה ושעירה.','סתם משנה','asserted',['בית דין מזידים','הקהל שוגגים']),
(118,'peopleintent','אם בית דין שוגגים והקהל מזידים פטורים.','סתם משנה','asserted',['בית דין שוגגים','הקהל מזידים']),
(119,'inference','מוצע לדייק ששוגג הדומה למזיד חייב, ולהעמידו בנתחלף חלב בשומן לאחר היתר בית דין.',None,'hypothetical',[]),
(120,'rejectinference','הדיוק אינו מכריע את בעיית רמי בר חמא: הסיפא נוקטת מזידים אגב השוגגים שברישא.',None,'asserted',[])]
cs={}
for i,k,p,holder,mode,cond in rows:
 unc=['Printed bracketed variant retained without choosing textual authenticity.'] if i==100 else []
 cs[k]=claim('b4.'+k,i,p,holder=holder,mode=mode,cond=cond,unc=unc)
qs={}
for i,k,p in [(93,'why','מדוע פטורים בדבר שהצדוקים מודין בו?'),(94,'guard','מדוע דוגמת שומרת יום מחייבת אם מפורשת בכתוב?'),(95,'haarah','הרי גם העראה מפורשת בכתוב?'),(96,'unnatural','הרי משכבי אשה מפורש?'),(97,'niddah','מדוע לא להעמיד גם בנדה?'),(99,'carry','הרי איסור הוצאה מפורש?'),(101,'bow','הרי השתחוויה מפורשת?'),(103,'plow','האם אין חרישה בשבת הוא ביטול מקצת או עקירת הגוף?'),(110,'seventh','מה דין אין שבת בשביעית?'),(115,'absent','מנין הפטור בהיעדר המופלא?'),(116,'fit','מנין שעדה האחרת ראויים להוראה?'),(117,'shekhinah','אולי עמך לשכינה?'),(120,'settle','האם דיוק המשנה יפשוט את בעיית רמי בר חמא?')]:qs[k]=question('b4.q.'+k,i,p)
for n,(i,c,q) in enumerate([(93,'read','why'),(95,'haarah1','guard'),(96,'unnatural','haarah'),(97,'combine','unnatural'),(98,'niddahonly','niddah'),(98,'days','guard'),(100,'inward','carry'),(100,'throw','carry'),(102,'custom','bow'),(102,'limbs','bow'),(112,'seventhresult','seventh'),(115,'learning','absent'),(116,'chasda','fit'),(117,'nachman','shekhinah'),(120,'rejectinference','settle')]):edge('b4.eq'+str(n),i,cs[c],qs[q],'answer')
for n,(i,x,y,rel) in enumerate([(95,'haarahverse','haarah1','objection'),(105,'guardanswer','guardproof','objection'),(107,'carryanswer','carryproof','objection'),(109,'bowanswer','bowproof','objection'),(112,'prophet','seventhresult','support'),(114,'edah','members','support'),(115,'learning','absent','support'),(117,'shekhinah','chasda','objection'),(117,'nachman','chasda','correction'),(120,'rejectinference','inference','objection')]):edge('b4.ec'+str(n),i,cs[x],cs[y],rel)
add('b4.report','attributions',[93],dict(surface='רב יהודה',role='transmitter',candidates=['רב יהודה'],scope='דבר שהצדוקים מודין בו',transmission_chain=['רב יהודה','שמואל']),[cs['shmuel']])
add('b4.zeira','attributions',[110],dict(surface='רבי זירא',role='speaker',candidates=['רבי זירא'],scope='בעיית אין שבת בשביעית',transmission_chain=[]),[qs['seventh']])
C=[]
for i in range(93,121):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in a.R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==a.inv[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=a.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Actual source omission reread: all quoted erroneous permissions remain hypothetical, objections and alternative answers separate, plowing question unresolved, seventh-year question resolved, qualifications of court and differing intentions retained; later continuation read to 5a:15 without counting it.'+(' No further item found in layer.' if not ids else '')))
p={k:a.job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.R,coverage=C,open_tails=[])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=Path(__file__).parent/'horayot_continuation_004.json'
if path.exists():assert path.read_bytes()==b
else:path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),records=len(a.R))))
