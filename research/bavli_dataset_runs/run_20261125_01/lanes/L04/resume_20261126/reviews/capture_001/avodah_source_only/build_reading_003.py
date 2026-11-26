import pathlib,json,hashlib,datetime
out=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/avodah_source_only');base=json.loads((out/'reading_001_frozen.json').read_bytes());a=[(i,j,t) for i,pg in enumerate(json.loads(pathlib.Path(base['source_path']).read_bytes())['text']) for j,t in enumerate(pg) if t]
def an(n):
 i,j,t=a[n];return dict(ordinal=n,ref='Avodah Zarah %d%s:%d'%(i//2+1,'a' if i%2==0 else 'b',j+1),page_index=i,segment_index=j,start_char=0,end_char=len(t),quote=t)
rows='''289,290|שמואל באמצעות רב יהודה|ברומי יש טקס אחת לשבעים שנה: אדם שלם על אדם חיגר, בגדי אדם הראשון, קרקיפלו של רבי ישמעאל, קישוטי זהב ושווקים והכרזות.|דיווח טקסי; תחילת הדיווח בcontext 289|asserted
290|מכריזי רומי בתוך דיווח שמואל|מכריזים סך קירי פלסתר אחוה דמרנא זייפנא וכו׳ ומסיימים ווי לדין כד יקום דין.|דיבור בתוך סיפור, לא קביעה של שמואל שהכינוי אמת|asserted
291|רב אשי|הכשילן פיהם: סדר המילים שאמרו מאפשר לקרוא מרנא גופיה זייפנא.|פרשנות אירונית להכרזה, לא דיווח עצמאי על זהות זייפן|asserted
292|סתם|התנא מנה חגים המתקיימים כל שנה ולא טקס שאינו בכל שנה.|מסביר השמטת טקס שבעים השנה|asserted
293|סתם|חגי פרס מנויים מוטרדי וטוריסקי מוהרנקי ומוהרין.|שמות מקור ללא תיקון|asserted
293|סתם|חגי בבל מנויים מוהרנקי ואקניתי׳ בחנוני ועשר באדר.|הנוסח הני דפרסאי ודרומאי דבבלאי נשמר; אין הבהרה חיצונית|asserted
294|רב דרך רב חנן בר רב חסדא או ר׳ חנן בר רבא|חמישה בתי עבודה זרה קבועים: בית בל בבבל, בית נבו בכורסי, תרעתא שבמפג, צריפא שבאשקלון, נשרא שבערביא.|שתי שרשרות מסירה מפורשות; לא רב חסדא עצמו כמוסר הראשון|asserted
294|רב דימי בדיווח כשבא|הוסיפו יריד שבעין בכי ונדבכה שבעכו.|נוסח ראשון; אל תערבב עם היפוך רב דימי מנהרדעא|asserted
294|איכא דאמרי|המקום בעכו נקרא נתברא.|וריאנט מפורש|asserted
294|רב דימי מנהרדעא|הנוסח הפוך: יריד שבעכו, נדבכה שבעין בכי.|לא הכרעה בנוסח הראשון|asserted
295|רב חסדא בשם אבוה דאימך|קבועים פירושו שעובדים להם תדיר כל השנה.|משיב לרב חנן בר רב חסדא; אבוה דאימך לא מזוהה בשם מתוך העדות המקומית|asserted
296|שמואל|בגולה אינו אסור אלא יום אידם עצמו.|מסחר עם עכו״ם לפי הקשר; אין הרחבה לארץ ישראל|asserted
296|מספר|רב יהודה התיר לרב ברונא למכור חמרא ולרב גידל למכור חיטים בחגתא דטייעי.|מעשה מובא כקושיה על איסור יום אידם|asserted
296|סתם|חגתא דטייעי שונה משום שאינה קבועה.|יישוב המעשה עם דין שמואל, לא דחייתו|asserted
297|סתם משנה|כשעבודה זרה בעיר, מחוץ לעיר מותר.|אין להסיק היתר בעיר עצמה|conditional
297|סתם משנה|כשעבודה זרה מחוץ לעיר, בתוך העיר מותר.||conditional
297|סתם משנה|דרך המיוחדת למקום העבודה זרה אסורה להליכה לשם.|ייחוד הדרך|conditional
297|סתם משנה|אם אפשר ללכת באותה דרך למקום אחר מותר.|אינה מיוחדת לאותו מקום|conditional
298|ר׳ חנינא באמצעות רשב״ל|חוצה לה כגון עטלוזא של עזה.|נוסח ראשון של דברי רשב״ל משום רבי חנינא|asserted
298,299|רבי חנינא בתשובה לרשב״ל|לשאלת עטלוזא של עזה מפנה לשתי קדירות ישראל ועכו״ם בכירה אחת בצור שלא חששו להן חכמים.|נוסח שני של שאלה ותשובה; מהות החשש מתפרשת בשלוש דרכים בהמשך|asserted'''
cs=[]
for row in rows.splitlines():
 ns,h,p,c,m=row.split('|');cs.append(dict(id=f'az_r3_c{len(cs)+1:03}',evidence=[an(int(n)) for n in ns.split(',')],holder=h,proposition=p,conditions=[c] if c else [],assertion_mode=m,origin='source_paraphrase'))
qs=[dict(id=f'az_r3_q{k+1:03}',evidence=[an(n)],formulation=q,origin='explicit') for k,(n,q) in enumerate([(292,'מדוע אין התנא מונה טקס זה?'),(293,'מה חגי פרס ומה חגי בבל?'),(295,'מה פירוש קבועים?'),(296,'האם אף ביום אידם אסור לאור היתרי רב יהודה?'),(297,'מהו ללכת לעיר זו?'),(298,'מה דוגמת חוצה לה?'),(298,'עטלוזא של עזה מהו לפי הנוסח האחר?'),(299,'איזה חשש לא חששו חכמים בשתי הקדירות?')])]
edges=[]
for x,y,r,why in [(290,289,'continuation','ritual report crosses segment boundary'),(291,290,'qualification','Rav Ashi reads inadvertent self-indictment'),(292,289,'answer','nonannual ritual not listed'),(295,294,'qualification','fixed means year-round worship'),(296,296,'objection','Rav Yehuda practice apparently conflicts'),(296,296,'distinction','unstable festival differs'),(298,297,'answer','Gaza market example'),(299,298,'continuation','Tyre analogy crosses folio'),(300,299,'answer','Abaye: carcass-meat concern; analog idol money'),(301,299,'answer','Rava: gentile cooking; analog festival day follows 302'),(303,299,'answer','Rabbah b Ulla: spittle; analog days before festival follows 304')]:edges.append(dict(id=f'az_r3_e{len(edges)+1:03}',source_ordinal=x,target_ordinal=y,relation=r,evidence=[an(x),an(y)],reason=why))
o=dict(review_schema='source-only-independent-reading-v1',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),blind=True,source_path=base['source_path'],source_sha256=base['source_sha256'],plan_sha256=base['plan_sha256'],core_blocks=['block_000029'],core_ordinals=list(range(290,300)),context_read_ordinals=list(range(280,290))+list(range(300,311)),claims=cs,questions=qs,edges=edges,transmission_notes=['Rav→Rav Hanan b Rav Hisda OR Rav→R Hanan b Rava; do not fuse names.','Rav Dimi vs Rav Dimi of Nehardea retained as text-distinct labels.','Rav Hisda invokes your maternal grandfather; no inferred entity resolution.','Resh Lakish משום R Hanina versus alternate question-response version preserved.'],boundaries=[dict(start=289,end=292,status='closed',material='seventy-year Roman ritual and omission from Mishnah'),dict(start=293,end=293,status='closed',material='festival name inventories'),dict(start=294,end=295,status='closed',material='permanent shrines, variants and meaning'),dict(start=296,end=296,status='closed',material='diaspora festival day restriction and exception'),dict(start=297,end=297,status='closed',material='Mishnah city boundary and roads'),dict(start=298,end=304,status='closed after context',material='Gaza market and Tyre cooking analogy'),dict(start=305,end=310,status='context open right',material='roads and appearance of worship')],context_notes=['At 11a:10 rejected initial framing of burning as forbidden custom replaced by shared honor reading.','Abaye/Rava/Rabbah bar Ulla supply alternative interpretations of analogy; no forced practical disagreement inferred without continuation.'],counts=dict(core_segments=10,probability_segments=10,context_segments=21,claims=len(cs),questions=len(qs),edges=len(edges)),limitations=['Not full tractate; no task eligibility','Ritual names and locations not externally normalized','Source-derived variants retained without resolving edition history'])
p=out/'reading_003_frozen.json';p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf8');h=hashlib.sha256(p.read_bytes()).hexdigest();(out/'reading_003_frozen.sha256').write_text(h+'  '+p.name+'\n');print('FROZEN',h)
for n,(i,j,t) in enumerate(a):
 if 330<=n<357:print('[%d] %d%s:%d %s'%(n,i//2+1,'a' if i%2==0 else 'b',j+1,t))
