import author_horayot_opening as h
import json,hashlib
from pathlib import Path
a=h.a;a.R=[];add=h.add;claim,question,edge=a.claim,a.question,a.edge
for key,lo,hi,title in [('all',60,67,'האם נדרשת הסכמת כל הדיינים: תיובתא ופירוש חלופי'),('responsibility',67,69,'אחריות משתתפי הדין וסיוע למורה'),('mishnah',69,75,'הוראה שחזרו בה ועקירת גוף מצוה'),('retraction',75,87,'שוגג לאחר חזרה: מסורות, גבייה ואשם תלוי'),('partial',87,93,'דבר ולא כל הגוף: דרשות')]:add('b3.'+key,'structure',list(range(lo,hi)),dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
for i in range(60,93):add('b3.u'+str(i),'utterances',[i],dict(textual_voice='משנה' if 69<=i<75 else 'anonymous discussion with named authorities',discourse_role='ruling, narrative, challenge, answer or derivation',composition='composite'))
rows=[
(60,'unanimity','רבי יונתן מצריך שכל מאה היושבים להורות יורו, מן כל עדת ישראל.','רבי יונתן','challenged',['מאה שישבו להורות']),
(60,'huna','רב הונא בריה דרב הושעיא תומך: אף שבכל התורה רובו ככולו, כאן נאמר כל העדה.','רב הונא בריה דרב הושעיא','challenged',[]),
(61,'known','מצוטטת משנת החיוב של היודע בטעות ועושה על פי בית דין.','משנה מצוטטת','asserted',['ידע שטעו']),
(62,'other','מוסקת פטור אחר למרות שהיודע לא הורה; זה מקשה על דרישת הכל.',None,'challenged',[]),
(62,'nod1','הקושיה נענית בהעמדה שהיודע הרכין בראשו.',None,'hypothetical',['הרכין בראשו']),
(63,'protest','בברייתא האומר טועין אתם מביא לפטור בית דין; מכאן מקשים ששתיקה מספיקה.',None,'challenged',[]),
(63,'nod2','גם מקרה הברייתא מועמד בהרכנת ראש.',None,'hypothetical',['הרכין בראשו']),
(64,'decree','רב משרשיא מקשה ממסורת רבותינו שסמכו על רשב״ג ורבי אלעזר ברבי צדוק: אין גוזרים אלא אם רוב הציבור יכול לעמוד.','רבן שמעון בן גמליאל ורבי אלעזר ברבי צדוק','asserted',['רוב הציבור יכולין לעמוד בגזירה']),
(65,'verse','רב אדא בר אבא מביא פסוק הגוי כולו, ובכל זאת רובו ככולו.','רב אדא בר אבא','asserted',[]),
(65,'refuted','הדיון מסיים תיובתא על רבי [יונתן], תוך שימור נוסח (יוחנן) [יונתן].',None,'asserted',[]),
(66,'presence','כל עדת מתפרש כנוכחות כולם, ולא כהסכמת כל אחד: אם כולם נמצאים הוראה, אחרת לא.',None,'asserted',[]),
(67,'collar','רבי יהושע אומר שקולר עשרה היושבים בדין תלוי בצוואר כולם, לרבות תלמיד בפני רבו.','רבי יהושע','asserted',['עשרה שיושבים בדין','אפילו תלמיד בפני רבו']),
(68,'rhunapractice','רב הונא היה מביא עשרה תנאים מבית רב לדין כדי שיישאו עמו באחריות.','רב הונא','asserted',[]),
(68,'ashipractice','רב אשי היה מושיב לפניו עשרה טבחים ממתא מחסיא כשבאה טרפה, באותו דימוי נשיאה בעול.','רב אשי','asserted',['כשמובאת טרפה']),
(69,'simon','לאחר שבית דין ידעו וחזרו, רבי שמעון פוטר את העושה על פיהם, בין שהביאו כפרה ובין שלא.','רבי שמעון','asserted',['בית דין ידעו שטעו וחזרו בהם','היחיד עשה על פיהם']),
(69,'elazar','רבי אלעזר אומר ספק; המשנה מבחינה יושב בביתו חייב, הולך למדינת הים פטור.','רבי אלעזר','asserted',['יושב בביתו לעומת הלך למדינת הים']),
(70,'akiva','רבי עקיבא מודה שהוא קרוב לפטור מן החובה.','רבי עקיבא','asserted',[]),
(70,'hearing','ההסבר מבחין בין יושב בביתו שיכול לשמוע לבין מי שלא יכול לשמוע.',None,'asserted',['אפשרות שמיעת החזרה']),
(71,'whole','בית דין שעקרו כל גוף מצווה, כגון אין נדה, שבת או עבודה זרה בתורה, פטורים.','סתם משנה','asserted',['עקירת כל הגוף']),
(71,'part','אם ביטלו מקצת וקיימו מקצת חייבים.','סתם משנה','asserted',['ביטול מקצת וקיום מקצת']),
(72,'niddah','דוגמת הוראה חלקית מוטעית: יש נדה בתורה אך הבא על שומרת יום כנגד יום פטור.','סתם משנה — דוגמת הוראה שגויה','hypothetical',[]),
(73,'shabbat','דוגמת הוראה חלקית מוטעית: יש שבת בתורה אך המוציא מרשות היחיד לרשות הרבים פטור.','סתם משנה — דוגמת הוראה שגויה','hypothetical',[]),
(74,'avodah','דוגמת הוראה חלקית מוטעית: יש עבודה זרה בתורה אך המשתחווה פטור.','סתם משנה — דוגמת הוראה שגויה','hypothetical',[]),
(74,'proof','דבר ולא כל הגוף משמש מקור לחיוב הוראה חלקית.','סתם משנה','asserted',[]),
(75,'rav1','רב יהודה בשם רב מסביר את פטור רבי שמעון: העושה פועל ברשות בית דין.','רב — מסירה ראשונה','asserted',[]),
(75,'rav2','באיכא דאמרי רב יהודה בשם רב: רבי שמעון פוטר יחיד העושה הוראה שיצאה ברוב ציבור, שלא ניתנה הוראה אלא להבחין שוגג ממזיד.','רב — איכא דאמרי','asserted',['הוראה שיצאה ברוב ציבור']),
(76,'collect','ברייתא ראשונה: רבי שמעון אומר שגובים בתחילה לפר העלם ולשעירי עבודה זרה; רבי יהודה אומר מתרומת הלשכה.','ברייתא — מסורה ראשונה','asserted',[]),
(76,'notice','הקושיה סבורה שהגבייה עצמה הודיעה על הטעות.',None,'challenged',['גבו מן הציבור']),
(77,'plain','תירוץ ראשון: גבו סתם, בלי לפרש למה.',None,'hypothetical',['גבו סתם']),
(78,'absent','תירוץ נוסף: האיש לא היה בעיר.',None,'hypothetical',['לא היה בעיר']),
(79,'reverse','תירוץ נוסף: רב סובר כמסורת הפוכה, רבי יהודה מצריך גבייה ורבי שמעון מתרומת הלשכה.',None,'hypothetical',['גרסה הפוכה בברייתא']),
(80,'meir','ברייתא: רבי מאיר מחייב ורבי שמעון פוטר לאחר חזרת בית דין.','ברייתא מצוטטת','asserted',[]),
(80,'doubt','רבי אלעזר אומר ספק ובשם סומכוס אומרים תלוי.','ברייתא מצוטטת','asserted',[]),
(80,'asham','רבי יוחנן קובע שהמחלוקת בין ספק לתלוי היא אשם תלוי.','רבי יוחנן','asserted',[]),
(81,'zeira','רבי זירא מדמה את רבי אלעזר לאוכל ספק חלב ספק שומן שנודע לו ומביא אשם.','רבי זירא','asserted',[]),
(82,'askable','אף אם בית הדין מביאים ואין פרסום, אילו שאל היו אומרים לו; כל שכן אם הציבור מביאים והדבר מפורסם.',None,'asserted',['אפשרות לשאול ולדעת']),
(83,'sumchos','משל סומכוס: הביא כפרה בין השמשות וספק מתי נתכפר, ואינו מביא אשם תלוי.','רבי יוסי בר אבין או רבי יוסי בר זבידא','asserted',['ספק מבעוד יום או משחשכה']),
(84,'unaskable','גם אם הציבור מביאים והדבר מפורסם, המשל הוא לספק שאפילו שאל לא היה מוצא מי לשאול.',None,'asserted',['אין דרך זמינה לברר']),
(86,'journey','רבא מסביר שהמחלוקת בהחזיק בדרך: בן עזאי מחייב כי עוד בביתו ורבי עקיבא פוטר כי החזיק בדרך.','רבא','asserted',['החזיק בדרך אך עדיין בביתו']),
(87,'wholebar','ברייתא דורשת ונעלם דבר ולא שתתעלם המצווה כולה ומוציאה עקירת כל הגוף.','ברייתא מצוטטת','asserted',[]),
(88,'partbar','ברייתא חוזרת על שלוש דוגמאות חלקיות של נדה, הוצאה והשתחוויה ומחייבת מדבר ולא כל הגוף.','ברייתא מצוטטת','asserted',[]),
(89,'meaning','הדיון מפרש שההוה אמינא היתה שדבר פירושו כל הדבר, ולא פטור בשני המקרים בלי שום חיוב.',None,'asserted',[]),
(90,'ulla','עולא קורא ונעלם מדבר ללימוד מקצת.','עולא','asserted',[]),
(91,'hezekiah','חזקיה לומד מכל מצוות ולא כל מצוות.','חזקיה','asserted',[]),
(91,'spelling','רב נחמן בר יצחק משיב שמצות כתיב ליישב את טענת הריבוי.','רב נחמן בר יצחק','asserted',[]),
(92,'gezerah','רב אשי לומד דבר דבר מזקן ממרא: מן הדבר ולא כל דבר, וכן בהוראה.','רב אשי','asserted',[])]
cs={}
for i,k,p,holder,mode,cond in rows:
 unc=[]
 if i==65:unc=['Parenthesized and bracketed variant preserved in evidence.']
 if i==70:unc=['Response speaker not repeated explicitly in this segment; not inferred solely by order.']
 if i==83:unc=['ואיתימא reporting alternatives retained, no forced selection.']
 cs[k]=claim('b3.'+k,i,p,holder=holder,mode=mode,cond=cond,unc=unc)
qs={}
for i,k,p in [(62,'incomplete','מדוע אחר פטור אם אין הוראת כולם?'),(63,'silent','מדוע משתיקה משתמע חיוב אף שלא הורו כולם?'),(66,'allq','מה אפוא פירוש כל עדת?'),(67,'obvious','מה החידוש באחריות כל היושבים?'),(70,'difference','מה שונה מי שיצא מן היושב בביתו?'),(75,'reason','מה טעם רבי שמעון?'),(76,'noticeq','מדוע פטור אם הגבייה הודיעה?'),(85,'akivaq','הרי תשובת רבי עקיבא על אפשרות השמיעה ראויה?'),(89,'liability','אם גם במקצת וגם בכולו פטור, מתי חייב?'),(90,'meaningq','כיצד משמעות הפסוק מלמדת מקצת?'),(91,'plural','הרי מצוות משמע שתי מצוות?')]:qs[k]=question('b3.q.'+k,i,p)
for n,(i,c,q) in enumerate([(62,'nod1','incomplete'),(63,'nod2','silent'),(66,'presence','allq'),(67,'collar','obvious'),(70,'hearing','difference'),(75,'rav1','reason'),(75,'rav2','reason'),(77,'plain','noticeq'),(78,'absent','noticeq'),(79,'reverse','noticeq'),(86,'journey','akivaq'),(89,'meaning','liability'),(90,'ulla','meaningq'),(91,'hezekiah','meaningq'),(91,'spelling','plural'),(92,'gezerah','meaningq')]):edge('b3.eq'+str(n),i,cs[c],qs[q],'answer')
for n,(i,x,y,rel) in enumerate([(60,'huna','unanimity','support'),(62,'other','unanimity','objection'),(64,'decree','unanimity','objection'),(65,'verse','decree','support'),(65,'refuted','unanimity','local_resolution'),(66,'presence','unanimity','correction'),(74,'proof','part','support'),(76,'notice','rav1','objection'),(81,'zeira','doubt','analogy'),(82,'askable','zeira','support'),(83,'sumchos','doubt','analogy'),(84,'unaskable','sumchos','support'),(87,'wholebar','whole','support'),(88,'partbar','part','support')]):edge('b3.ec'+str(n),i,cs[x],cs[y],rel)
add('b3.ravy','attributions',[75],dict(surface='רב יהודה',role='transmitter',candidates=['רב יהודה'],scope='שתי מסירות טעם רבי שמעון',transmission_chain=['רב יהודה','רב']),[cs['rav1'],cs['rav2']])
add('b3.mesh','attributions',[64],dict(surface='רב משרשיא',role='speaker',candidates=['רב משרשיא'],scope='קושיה ממסורת רבותינו',transmission_chain=[]),[cs['decree']])
C=[]
for i in range(60,93):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in a.R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==a.inv[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=a.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Original source reread: retain תיובתא, presence/consent distinction, alternative Rav reports and inverted collection baraita, uncertain speaker versions, stages of awareness and liability. Read following context through 4a:18 but not counted.'+(' No explicit additional item found in layer.' if not ids else '')))
p={k:a.job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.R,coverage=C,open_tails=[])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=Path(__file__).parent/'horayot_continuation_003.json'
if path.exists():assert path.read_bytes()==b
else:path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),records=len(a.R))))
