import author_horayot_opening as h
import json,hashlib
from pathlib import Path
a=h.a;a.R=[];add=h.add;claim,question,edge=a.claim,a.question,a.edge
for key,lo,hi,title in [('sequence',19,21,'סדר לא זו אף זו לעומת זו ואין צריך לומר זו'),('student',21,26,'תלמיד ראוי להוראה וטעות במצות שמיעה'),('general',26,28,'ריבויי זה הכלל'),('tanna',28,48,'ייחוס המשנה ומחלוקת חיוב יחיד: מסורות וחלופות'),('population',48,53,'רוב יושבי הארץ ושינוי מספר החוטאים'),('combine',53,57,'צירוף מיעוטים: שרשרת אם תמצא לומר'),('court',57,60,'צירוף לאחר החלפת בית הדין')]:
 add('b2.'+key,'structure',list(range(lo,hi)),dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
for i in range(19,60):add('b2.u'+str(i),'utterances',[i],dict(textual_voice='anonymous discussion and explicit attributed reports',discourse_role='question, distinction, derivation or alternative explanation',composition='composite'))
# Entries below are manually authored after reading original 2a:20–3b:1 and following context.
rows=[
(19,'first','ברישא סדר המקרים מוצג כלא זו אף זו.',None,'asserted',[]),
(20,'last','בסיפא סדר המקרים הוא זו ואין צריך לומר זו.',None,'asserted',[]),
(21,'rava','רבא מציע שהכפילות נצרכת להבחין בין גמיר וסביר לבין גמיר ולא סביר.','רבא','hypothetical',[]),
(22,'abaye','אביי מקשה שראוי להוראה משמע גמיר וסביר.','אביי','asserted',[]),
(22,'rava2','רבא מבהיר שיתור המשנה מרבה גם גמיר ולא סביר וגם סביר ולא גמיר.','רבא','asserted',[]),
(23,'examples','רבא מדגים ראוי להוראה בשמעון בן עזאי ושמעון בן זומא.','רבא','asserted',[]),
(23,'intent','אביי מקשה שבמקרה כזה העושה הוא מזיד.','אביי','challenged',[]),
(24,'baraita','ברייתא דורשת בעשותה אחת: עושה מפי עצמו חייב ובהוראת בית דין פטור; היא כוללת תלמיד כבן עזאי היודע את הטעות.','ברייתא מצוטטת','asserted',['ידע שטעו']),
(25,'obedience','היישוב בשני המקורות הוא מי שיודע שאסור וטועה במצווה לשמוע דברי חכמים.',None,'conditional',['ידע שאסור','טעה במצווה לשמוע דברי חכמים']),
(26,'rejector','התולה בעצמו מרבה מבעט בהוראה.',None,'asserted',[]),
(27,'retract','התולה בבית דין מרבה עשייה לאחר שבית הדין ידעו שטעו וחזרו; אף שהדבר מפורש בהמשך, כאן נשנה ואחר כך מתפרש.',None,'asserted',['בית דין ידעו שטעו וחזרו בהם']),
(28,'judah','רב יהודה בשם שמואל מייחס את משנת הפטור לרבי יהודה.','שמואל — מסירת רב יהודה','asserted',[]),
(28,'sages','באותה מסירה חכמים מחייבים יחיד שעשה בהוראת בית דין.','חכמים — במסירת שמואל','asserted',['יחיד שעשה בהוראת בית דין']),
(28,'three','ברייתת אם נפש אחת תחטא בשגגה בעשותה דורשת שלושה מיעוטים לחיוב מפי עצמו ופטור בהוראה.','ברייתא מצוטטת','asserted',[]),
(29,'minor','הברייתא מניחה חיוב מיעוט קהל החוטאים מאחר שאין בית הדין מביאים עליהם פר.','ברייתא מצוטטת','asserted',[]),
(29,'major','הברייתא מעלה אפשרות לפטור רוב מפני שבית הדין מביאים עליהם פר, ודורשת מעם הארץ לרבות אפילו רובו וכולו.','ברייתא מצוטטת','asserted',[]),
(30,'difficulty','הדיון מתקשה אם הברייתא בשגגת מעשה או בהוראה: פר בית הדין מצריך הוראה, ומעם הארץ עוסק בשגגת מעשה.',None,'unresolved',[]),
(31,'reconstruct','מוצע לקרוא: מיעוט בשגגת מעשה חייב; אין בית הדין מביאים עליו פר בהוראה, אך המיעוט עצמו חייב.',None,'hypothetical',[]),
(32,'majoragain','בהמשך הקריאה המוצעת: גם רוב בשגגת מעשה חייב אף שבמקרה הוראה מביאים עליו פר.',None,'hypothetical',[]),
(33,'pappa','רב פפא מציע שאולי לא המיעוט ולא בית הדין חייבים במקרה הוראה.','רב פפא','hypothetical',[]),
(34,'ordering','הדיון טוען שסדר הברייתא, החוזר דווקא לרוב, מניח כבר חיוב מיעוט בהוראה.',None,'asserted',[]),
(35,'inference','מוסקת מן הסדר חובת מיעוט בהוראה בכשבה או שעירה וכן חובתו בשגגת מעשה ללא הוראה.',None,'asserted',[]),
(36,'identify','התגובה לאפשרות איפוך היא שדרשת שלושה מיעוטים מאפיינת את רבי יהודה.',None,'asserted',[]),
(37,'olah','רבי יהודה דורש זאת תורת העולה היא כשלושה מיעוטים.','רבי יהודה','asserted',[]),
(38,'alternative','תשובה חלופית: ברייתת עדיין אני אומר אינה רבי יהודה, כי היא תולה את הפר בבית דין והוא תולהו בציבור.',None,'asserted',[]),
(38,'tribes','רבי יהודה אומר ששבעה שבטים שחטאו מביאים שבעה פרים.','רבי יהודה','asserted',['שבעה שבטים שחטאו']),
(39,'meir','רב נחמן בשם שמואל מייחס את משנת הפטור לרבי מאיר, וחכמים מחייבים יחיד בהוראה.','שמואל — מסירת רב נחמן','asserted',[]),
(39,'bara','בברייתת הורו ועשו רבי מאיר פוטר וחכמים מחייבים.','ברייתא מצוטטת','asserted',['הורו ועשו; זהות העושים נידונה בהמשך']),
(40,'courtact','העמדת עשו בבית דין מוקשית מדרשת הקהל ועשו: המעשה תלוי בקהל וההוראה בבית דין.',None,'challenged',[]),
(41,'majorreject','העמדת עשו ברוב קהל מוקשית משום שאין טעם לפטור רבי מאיר.',None,'challenged',[]),
(41,'minorread','הדיון מציע שעשו מיעוט קהל ונחלקו אם יחיד שעשה בהוראה פטור או חייב.',None,'hypothetical',[]),
(42,'papparead','רב פפא מציע שכולם פוטרים יחיד, והמחלוקת היא אם בית דין משלים לרוב הציבור.','רב פפא','hypothetical',[]),
(43,'majorityviews','מר סבר בית דין משלים לרוב ציבור ומר סבר אינו משלים; השמות אינם מפורשים בקטע.',None,'unresolved',[]),
(44,'simonread','חלופה: הורו ועשו רוב קהל וחכמים הם רבי שמעון, המחייב הן ציבור הן בית דין.',None,'hypothetical',['עשו רוב קהל']),
(45,'triberead','חלופה: שבט עשה בהוראת בית דינו וחכמים הם רבי יהודה, המחייב אותו שבט.',None,'hypothetical',['שבט שעשה בהוראת בית דינו']),
(46,'sixseven','חלופה: שישה שבטים שהם רוב הקהל או שבעה אף שאינם רוב; המשנה מיוחסת לרבי שמעון בן אלעזר.',None,'hypothetical',['שישה ורוב קהל או שבעה ללא רוב קהל']),
(47,'sixsevenbar','רבי שמעון בן אלעזר אומר משמו שחטאו שישה והם רוב קהל או שבעה אף שאינם רוב חייבים.','רבי שמעון בן אלעזר','asserted',['שישה ורוב קהל או שבעה ללא רוב קהל']),
(48,'israel','רב אסי קובע שבהוראה הולכים אחר רוב יושבי ארץ ישראל.','רב אסי','asserted',['הוראה']),
(48,'verse','היתור מלבוא חמת עד נחל מצרים מלמד שאלה נקראים קהל ולא האחרים.',None,'asserted',[]),
(49,'decrease','מרובים שנתמעטו מוצג כמחלוקת רבי שמעון וחכמים.',None,'asserted',[]),
(50,'increase','מוצע שמועטים שנתרבו יהיו מחלוקת אם הולכים אחר הידיעה או החטא.',None,'hypothetical',['מועטים ונתרבו']),
(51,'notknowledge','הדיון דוחה ייחוס חיוב על סמך ידיעה בלבד לרבי שמעון: נשמע שהוא דורש גם ידיעה במקום שחטאו בחיוב.',None,'asserted',[]),
(52,'both','המסקנה המקומית היא שרבי שמעון מצריך חטאה וידיעה.',None,'asserted',[]),
(53,'fatoptions','במיעוטים שחטאו בהיתרי חלב נפרדים לאחר חזרת בית הדין נשקלות שתי ידיעות מול שם חלב אחד.',None,'unresolved',['הוראה, מיעוט, חזרה, הוראה ומיעוט אחר']),
(54,'twofats','אם מצטרפים באותו חלב, נשאל בחלב שעל הקבה וחלב שעל הדקין: שני פסוקים לעומת שם חלב אחד.',None,'unresolved',['אם תמצא לומר שהמקרה הקודם מצטרף']),
(55,'blood','אם שם חלב מצרף, נשאל בחלב ודם: שני איסורים לעומת קרבן שווה.',None,'unresolved',['אם תמצא לומר שהמקרה הקודם מצטרף']),
(56,'idolatry','אם קרבן שווה מצרף, נשאל בחלב ועבודה זרה: איסור וקרבן שונים לעומת כרת משותף; תיקו.',None,'unresolved',['אם תמצא לומר שהמקרה הקודם מצטרף']),
(57,'newcourt','נשאל צירוף שני מיעוטים שעשו בהוראות חלב של בתי דין שונים לאחר מות הראשון.',None,'unresolved',['מת בית דין ראשון ועמד אחר']),
(58,'courtbrings','למאן דאמר בית דין מביאים אין בעיה, כי הראשון איננו; הספק למאן דאמר ציבור מביאים.',None,'asserted',['שיטות שונות בזהות מביא הקרבן']),
(58,'publicexists','צד אחד של הספק הוא שהציבור עדיין קיים.',None,'hypothetical',['למאן דאמר ציבור מביאים']),
(59,'knowledge','הצד השני מצריך ידיעת אותו בית דין שהורה; הספק מסיים בתיקו.',None,'unresolved',['למאן דאמר ציבור מביאים'])]
cs={}
for i,k,p,holder,mode,cond in rows:
 unc=[]
 if i==43:unc=['Do not assign anonymous alternatives by order.']
 if i==47:unc=['משמו has no explicit named referent inside this segment; no referent invented.']
 if i in [55,56]:unc=['Printed bracketed/parenthesized variants retained in full source evidence; no silent textual emendation.']
 cs[k]=claim('b2.'+k,i,p,holder=holder,mode=mode,cond=cond,unc=unc)
qs={}
for i,k,p in [(19,'order','מדוע כל שלושת המקרים ובסיפא לא בסדר הפוך?'),(21,'double','מדוע גם דיין היודע וגם תלמיד ראוי?'),(23,'who','כגון מי הוא תלמיד ראוי להוראה?'),(25,'how','כיצד תימצא שגגה אצל תלמיד היודע שהדין אסור?'),(26,'include','מה מרבה התולה בעצמו?'),(27,'repeat','מדוע לרבות מקרה שמפורש בהמשך?'),(28,'judahq','מה המקור לזיהוי רבי יהודה?'),(29,'sagesq','מה המקור לשיטת חכמים?'),(30,'case','באיזה מקרה עוסקת הברייתא?'),(33,'maybe','אולי לא המיעוט ולא בית הדין חייבים?'),(36,'reverse','מדוע לא להחליף את ייחוס שתי הברייתות?'),(39,'meirq','מה המקור לרבי מאיר וחכמים?'),(40,'actors','מי הם עשו בברייתא?'),(48,'extra','מדוע פורטו גבולות הארץ אחרי כל ישראל?'),(50,'increaseq','האם מועטים שנתרבו מחלוקת?'),(53,'combineq','האם שני מיעוטים אחרי שתי הוראות חלב מצטרפים?'),(54,'twofatsq','האם חלב הקבה וחלב הדקין מצטרפים?'),(55,'bloodq','האם חלב ודם מצטרפים?'),(56,'idolq','האם חלב ועבודה זרה מצטרפים?'),(57,'courtsq','האם מצטרפים שני מיעוטים לאחר מות בית דין והחלפתו?')]:qs[k]=question('b2.q.'+k,i,p)
for n,(i,c,q,rel) in enumerate([(20,'last','order','answer'),(21,'rava','double','answer'),(23,'examples','who','answer'),(25,'obedience','how','answer'),(26,'rejector','include','answer'),(27,'retract','repeat','answer'),(28,'three','judahq','answer'),(29,'minor','sagesq','answer'),(31,'reconstruct','case','answer'),(35,'inference','maybe','answer'),(36,'identify','reverse','answer'),(38,'alternative','reverse','answer'),(39,'bara','meirq','answer'),(41,'minorread','actors','answer'),(42,'papparead','actors','answer'),(44,'simonread','actors','answer'),(45,'triberead','actors','answer'),(46,'sixseven','actors','answer'),(48,'verse','extra','answer'),(52,'both','increaseq','answer'),(56,'idolatry','idolq','unresolved_outcome'),(59,'knowledge','courtsq','unresolved_outcome')]):edge('b2.eq'+str(n),i,cs[c],qs[q],rel)
for n,(i,x,y,rel) in enumerate([(22,'abaye','rava','objection'),(22,'rava2','abaye','answer'),(23,'intent','examples','objection'),(25,'obedience','intent','answer'),(33,'pappa','reconstruct','objection'),(35,'inference','pappa','answer'),(37,'olah','identify','support'),(38,'tribes','alternative','support'),(42,'papparead','minorread','objection'),(43,'majorityviews','papparead','qualification'),(47,'sixsevenbar','sixseven','support'),(48,'verse','israel','support'),(51,'notknowledge','increase','objection'),(52,'both','notknowledge','local_resolution'),(58,'courtbrings','newcourt','qualification')]):edge('b2.ec'+str(n),i,cs[x],cs[y],rel)
for i,name,chain,targets in [(28,'רב יהודה',['רב יהודה','שמואל'],['judah','sages']),(39,'רב נחמן',['רב נחמן','שמואל'],['meir'])]:add('b2.report'+str(i),'attributions',[i],dict(surface=name,role='transmitter',candidates=[name],scope='ייחוס המשנה ושיטת חכמים',transmission_chain=chain),[cs[x] for x in targets])
C=[]
for i in range(19,60):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in a.R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==a.inv[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=a.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source reread for omissions: retain alternative reconstructions, argument reversals, transmission chains, Rav Asi identity, population conditions and if-you-say branches without converting them into rulings; both teiku preserved. Context through 3b:5 read separately.'+(' No further explicit item of this layer found.' if not ids else '')))
p={k:a.job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.R,coverage=C,open_tails=[])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=Path(__file__).parent/'horayot_continuation_002.json'
if path.exists():assert path.read_bytes()==b
else:path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),records=len(a.R))))
