import pathlib,json,hashlib,datetime
out=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/avodah_source_only');b=json.loads((out/'reading_001_frozen.json').read_bytes());a=[(i,j,t) for i,pg in enumerate(json.loads(pathlib.Path(b['source_path']).read_bytes())['text']) for j,t in enumerate(pg) if t];core=set(range(340,350))|set(range(360,370))
def an(n):
 i,j,t=a[n];return dict(ordinal=n,ref='Avodah Zarah %d%s:%d'%(i//2+1,'a' if i%2==0 else 'b',j+1),page_index=i,segment_index=j,start_char=0,end_char=len(t),quote=t)
rows='''340|רבי זירא בתשובה לרבי ירמיה|מסתבר שעבדים המותרים בלקיחה מן היריד הם עבדים ישראלים.|הצעה מאותגרת בהמשך; אין לצרף לשאלה הקודמת של רבי יונה לרבי עילאי|challenged
340|רשב״ל באמצעות רבין|מותר גם עבד עכו״ם מפני שמכניסו תחת כנפי השכינה.|דיווח כי אתא רבין|asserted
341|רב אשי|ההיתר בבהמה אינו הכנסת כנפי שכינה אלא מיעוטם וכך גם בעבדים.|נימוק חלופי; לא היפוך תוצאת היתר רשב״ל|asserted
342|מספר|רבי יעקב קנה סנדל ורבי ירמיה פת; כל אחד ביקר את חברו כי חשב שקנה מתגר.|שניהם בפועל קנו מבעל הבית; אין מחלוקת הלכתית מוכחת|asserted
342|רבי אבא בריה דרבי חייא בר אבא|האיסור בלוקח מן התגר שגובים ממנו מכס; מבעל הבית שאינו מחויב מכס מותר.|תנאי המכס מהותי|asserted
343|רבי אבא בריה דרבי חייא בר אבא|אילו רבי יוחנן היה במקום ובזמן שגובים מכס גם מבעל הבית היה אוסר.|היפותזה מפורשת, לא פסיקה מדווחת של רבי יוחנן באותו מקום|hypothetical
343|סתם|הקניות היו מבעל בית שאינו קבוע.|יישוב הסיפור עם מכס אף מבעל הבית|asserted
344|סתם משנה|אסור למכור לעכו״ם אצטרובלין, בנות שוח ופטוטרות, לבונה ותרנגול לבן.|רשימת חפצים; פירושי המינים בהמשך|asserted
344|רבי יהודה|מותר למכור תרנגול לבן בין התרנגולים.|המשך מפרש כגון זה וזה; לא כל נוסח בקשה|conditional
344|רבי יהודה|כשבפני עצמו קוטע אצבעו ומוכרו כי אין מקריבים חסר לעבודה זרה.|בעל מום; אין להשליך אוטומטית על בקשת קטוע שנידונה בתיקו|conditional
345|סתם משנה|שאר דברים סתמם מותר ופירושם אסור.|המשך סתמם אפילו חיטי חוורתא; פירושם לעבודה זרה|conditional
345|רבי מאיר|גם דקל טב וחצב ונקלב אסור למכור.|נקלב כתוב במשנה בסוגריים; המשך נקלס. דקל טב מפורש כפירות|asserted
346|סתם בהצעה|אצטרובלין הם תורניתא.|נדחה ממשנת שביעית|rejected
347|רב ספרא|אצטרובלין הם פירי דארזא.|תיקון הזיהוי|asserted
347|רבי אלעזר באמצעות רבין|אצטרובלין הם פירי דארזא.|מסירה מקבילה לרב ספרא|asserted
348|רבי יוחנן באמצעות רבה בר בר חנה|בנות שוח הן תאיני חיוראתא.||asserted
348|רבי יוחנן באמצעות רבה בר בר חנה|בפטוטרותיהן שנו.|תנאי בפריטים הנמכרים; משמר לשון בלי זיהוי בוטני חיצוני|asserted
349|רשב״ל באמצעות רבי יצחק|לבונה האסורה היא לבונה זכה.||asserted
349|ברייתא|מכולן מוכרים חבילה.|המשך מקשה על מכירה לאחרים; לפני דלפני|asserted
349|רבי יהודה בן בתירא|חבילה אינה פחותה משלושה מנין.|יחידת המקור נשמרת|asserted
360|סתם|פירושן לעבודה זרה אסור גם כשהיה אפשר לחשוב שהלקוח רק מתבטא כך מרוב דבקותו כדי שימכרו לו.|ההיתר המדומה נדחה; אין ייחוס ודאי למניע הפסיכולוגי|asserted
361|רב אשי|מבקש תרנגול לבן קטוע: האם מותר לתת שלם כי אינו לע״ז, או שהוא מערים?|ספק, לא היתר|queried
362|רב אשי בהמשך|מבקש לבן ולוקח שחור ואדום: האם מותר למכור לבן כי אינו לע״ז או מערים?|את״ל בשאלה הראשונה שהוא מערים; תיקו בסוף|unresolved
363|רב חסדא לאבימי|גמירי שעבודה זרה של אברהם ארבע מאות פרקים ואנו חמישה ולא יודעים הפירוש.|אמירה מטא-לימודית; אין להפוך לקובץ אבוד מאומת|asserted
364|אבימי בתשובת השיחה|דקל טב הוא פירות דקל טב.|יישוב קושיית איסור מכירה במחובר; שם המשיב נלמד מסגרת השיחה ולא נאמר בפסוקית|asserted
364|רב הונא|דקל טב הוא פירות דקל טב.|מסירה נוספת מפורשת|asserted
365|סתם|חצב מתבאר קשבא.|זיהוי לשוני מקור, ללא זיהוי מין מודרני|asserted
365|רבי חמא בר יוסף באמצעות רב דימי|נקלס מתבאר קורייטי.||asserted
365|אביי|זיהוי נקלס בקורייטי אינו מועיל למי שאינו מכיר גם קורייטי.|קושיה על תועלת תרגום|asserted
365|רב דימי|שם קורייטי מועיל במקום שמכירים אותו ויראו את הדבר.|תועלת מקומית של שם חלופי|asserted
366|סתם משנה|מכירת בהמה דקה תלויה במנהג המקום להתיר או לאסור.|מנהג מקומי|conditional
366|סתם משנה|בכל מקום אין מוכרים בהמה גסה עגלים וסייחים שלמים ושבורים.|אין להסיק שכל הנימוקים כבר סופיים; דיון גסה ממשיך|asserted
366|רבי יהודה|מתיר בבהמה שבורה.|חולק על כלל שבורים|asserted
366|בן בתירא|מתיר בסוס.|לא היתר כללי בגסה|asserted
367|סתם בשאלה|משתמע שבבהמה דקה יש מנהג ואין איסור עצמי.|הנחת פתיחה נבחנת בייחוד|queried
368|משנה מצוטטת בקושיה|אין מעמידים בהמה בפונדקאות עכו״ם מפני שחשודים ברביעה.|מעמת עם מנהג היתר מכירה|asserted
368|רב|במקום שהתירו למכור התירו לייחד ובמקום שאסרו לייחד אסרו למכור.|רב חוזר בו ב15a:1|retracted
369|ר״א|אף במקום שאסרו לייחד מותר למכור כי עכו״ם חס על בהמתו שלא תיעקר.|הבדל בעלות; קיצור ר״א נשמר בלי הכרעה חיצונית|asserted
369|רב באמצעות רב תחליפא בשם רבי שילא בר אבימי|עכו״ם חס על בהמתו שלא תיעקר.|עדות לחזרת רב, לא שמירת מחלוקת רב–ר״א כתוצאה סופית|asserted'''
cs=[]
for row in rows.splitlines():
 n,h,p,c,m=row.split('|');cs.append(dict(id=f'az_r4_c{len(cs)+1:03}',evidence=[an(int(n))],holder=h,proposition=p,conditions=[c] if c else [],assertion_mode=m,origin='source_paraphrase'))
qs=[]
for n,q in [(340,'עבד ישראל בלבד או אפילו עבד עכו״ם?'),(341,'כיצד טעם הכנסת שכינה חל על בהמה?'),(343,'כיצד קנו אם גובים מכס גם מבעל בית?'),(346,'מהם אצטרובלין וכיצד תורניתא חייבת בשביעית?'),(349,'כמה חבילה?'),(361,'מבקש לבן קטוע האם מותר לתת שלם?'),(362,'נוטל שחור ואדום האם מותר לבן?'),(364,'למה משתמע דקל רע מותר אף שאסור במחובר?'),(365,'מה הועיל שם קורייטי שאינו ידוע?'),(367,'האם רק מנהג ולא איסור?')]:qs.append(dict(id=f'az_r4_q{len(qs)+1:03}',evidence=[an(n)],formulation=q,origin='explicit'))
edges=[]
for x,y,r,t in [(340,340,'correction','Ravin reports broader permission than R Zeira proposal'),(341,340,'qualification','alternative rationale reducing gentile holdings'),(342,342,'answer','mutual rebuke rests on mistaken assumptions; both bought privately'),(343,342,'qualification','tax situation limits private vendor permission'),(347,346,'correction','cedar fruit replaces tree identification'),(350,349,'answer','before-before prohibition not commanded'),(354,344,'qualification','this and this interpretation of mixed chickens'),(359,345,'qualification','explicit idol purpose rather than merely white wheat'),(360,359,'answer','novelty excludes proposed innocent explanation'),(362,361,'continuation','second question conditional on first suspicion'),(362,362,'unresolved_outcome','teiku'),(364,345,'qualification','good palm fruit, not rooted palm'),(365,365,'answer','local recognition answers Abaye'),(368,367,'objection','seclusion Mishnah challenges custom-only premise'),(369,368,'retraction','explicit ואף רב הדר ביה with transmission'),(369,368,'distinction','sale entails owners interest in animal survival')]:edges.append(dict(id=f'az_r4_e{len(edges)+1:03}',source_ordinal=x,target_ordinal=y,relation=r,evidence=[an(x),an(y)],reason=t))
o=dict(review_schema='source-only-independent-reading-v1',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),blind=True,source_path=b['source_path'],source_sha256=b['source_sha256'],plan_sha256=b['plan_sha256'],core_blocks=['block_000034','block_000036'],core_ordinals=sorted(core),context_read_ordinals=[n for n in range(317,377) if n not in core],claims=cs,questions=qs,edges=edges,boundaries=[dict(start=339,end=341,status='closed',material='slave sanction then purchasing gentile slaves; distinct questioners'),dict(start=342,end=343,status='closed',material='two purchases and tax conditions'),dict(start=344,end=345,status='closed textual Mishnah',material='prohibited sale objects'),dict(start=346,end=347,status='closed',material='itztrubalin identification'),dict(start=348,end=348,status='closed short interpretations',material='white figs and stalks'),dict(start=349,end=350,status='closed after context',material='frankincense bulk sales and indirect stumbling-block'),dict(start=351,end=362,status='unresolved end',material='white chicken wording and evasive requests'),dict(start=363,end=365,status='closed',material='plant names and utility of translations'),dict(start=366,end=366,status='closed textual Mishnah',material='animal sales'),dict(start=367,end=369,status='closed',material='small animal sales/seclusion and Rav retraction'),dict(start=370,end=376,status='open right context',material='large animals, rental and Shabbat testing')],notes=['Do not assign חד לחבריה dialogue insults at 342 by name order.','Unresolved chicken queries must not become affirmative permissions.','All transmission chains remain textual roles; no inferred identity merges.','Context 317–331 reconciles baraitot by taxed merchant vs untaxed householder under Yohanan; needed for 342–343.'],counts=dict(core_segments=20,probability_segments=20,context_segments=40,claims=len(cs),questions=len(qs),edges=len(edges)),limitations=['No full-tractate or eligibility claim','Large-animal continuation remains open beyond 15a:8','Source ambiguity of abbreviated ר״א and plant names preserved'])
p=out/'reading_004_frozen.json';p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf8');h=hashlib.sha256(p.read_bytes()).hexdigest();(out/'reading_004_frozen.sha256').write_text(h+'  '+p.name+'\n');print(h,len(cs))
