import json,hashlib,pathlib,datetime
out=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/avodah_source_only')
root=pathlib.Path('C:/Users/David/.codex/worktrees/bavli-l04-production/AI Talmudic Study')
source=pathlib.Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nezikin/Avodah Zarah/Hebrew/Wikisource Talmud Bavli.json')
b=source.read_bytes(); sha=hashlib.sha256(b).hexdigest(); assert sha=='2ec254680a7711f122b072f08e556174ec536a48b0b9ac1f575994bf06aaa7a0'
d=json.loads(b); a=[(i,j,t) for i,pg in enumerate(d['text']) for j,t in enumerate(pg) if t]
planpath=root/'research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/frozen_plans/bavli_avodah_zarah.json'; plan=json.loads(planpath.read_text(encoding='utf8')); cp=dict(plan); ph=cp.pop('plan_sha256'); assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(cp,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()==ph
core=set(range(10))|set(range(110,130))
def anchor(n):
 i,j,t=a[n]; return dict(ordinal=n,ref='Avodah Zarah %d%s:%d'%(i//2+1,'a' if i%2==0 else 'b',j+1),page_index=i,segment_index=j,start_char=0,end_char=len(t),quote=t,span_sha256=hashlib.sha256(t.encode()).hexdigest(),cohort='core' if n in core else 'context')
rows='''0|סתם משנה|בשלושה ימים לפני אידיהן אסור לשאת ולתת עמהם.|שלושה ימים לפני אידיהן|asserted
0|סתם משנה|אסור להשאילן ולשאול מהן.|שלושה ימים לפני אידיהן|asserted
0|סתם משנה|אסור להלוותן וללוות מהן.|שלושה ימים לפני אידיהן|asserted
0|סתם משנה|אסור לפורען ולפרוע מהן.|שלושה ימים לפני אידיהן|asserted
0|רבי יהודה|נפרעין מהן משום שמיצר לו.|שלושה ימים לפני אידיהן; פירעון מן הנכרי|asserted
0|אמרו לו|אף שמיצר עכשיו שמח לאחר זמן.|תשובה לטעם רבי יהודה|asserted
1|רב או שמואל, לא מוכרע|אחד שנה אידיהן ואחד עידיהן.|אין שיוך על פי סדר שמות|unresolved
1|סתם|שתי הגרסאות אינן משובשות.||asserted
2|סתם|כי קרוב יום אידם תומך בגרסת אידיהן.||asserted
2|סתם|יתנו עידיהם ויצדקו תומך לכאורה בגרסת עידיהן.|הראיה מוחלפת בהמשך|challenged
3|שונה אידיהן, לא מזוהה|תברא עדיף כטעם לגרסה.|נימוק משוחזר בלשון אמר לך|asserted
3|שונה עידיהן, לא מזוהה|העדות היא הגורמת לשבר ולכן עדות עדיפה.|נימוק משוחזר בלשון אמר לך|asserted
4|ריב״ל|מצוות שישראל עושים בעולם הזה מעידות להם לעולם הבא.|ישראל; מצוות|asserted
4|ריב״ל|יתנו עידיהם ויצדקו אלו ישראל; ישמעו ויאמרו אמת אלו עובדי כוכבים.||asserted
5|רב הונא בריה דרב יהושע|הראיה לעידיהן היא מיוצרי פסל...ועידיהם המה.|תחליף לראיה הקודמת|asserted
6|ר׳ חנינא בר פפא או ר׳ שמלאי|לעתיד הקב״ה מביא ספר תורה ומזמין את העוסק בה ליטול שכר.|ייחוס חלופי מפורש; דרשה סיפורית|asserted
7|קול הקב״ה בתוך הדרשה|האומות נדרשות להיכנס כל אומה בפני עצמה.|לעתיד לבוא בתוך הסיפור|asserted
8|סתם בתוך הדרשה|לאום מפורש כמלכות.||asserted
8|סתם|הכניסה הנפרדת מונעת ערבוב האומות זו עם זו כדי שישמעו; אינה מונעת בלבול אצל הקב״ה.|הסבר לקושי|asserted
9|סתם בתוך הדרשה|רומי נכנסת תחילה מפני חשיבותה.|סדר הדין העתידי|asserted
9|רבי יוחנן|המלכות המתוארת בדניאל היא רומי שטבעה יצא בכל העולם.|פירוש הפסוק|asserted
110|רבי יוסי בתשובת אמר לך|כשאין מיתה אין טובה גדולה מזו.|תשובה ללמען ייטב; במסגרת מחלוקת קבלת התורה|asserted
111|תנא קמא בתשובת הסתם|אכן כאדם תמותון מתפרש כעניות.|ניגוד לקריאת מיתה ממש|asserted
111|מר, לא מזוהה|עני חשוב כמת.||asserted
111|מר, לא מזוהה|סומא חשוב כמת.||asserted
111|מר, לא מזוהה|מצורע חשוב כמת.||asserted
111|מר, לא מזוהה|מי שאין לו בנים חשוב כמת.||asserted
112|סתם|כי מתו כל האנשים מתייחס לדתן ואבירם שירדו מנכסיהם ולא מתו.||asserted
113|סתם|במחשכים הושיבני כמתי עולם מובא לראיית סומא כמת.||asserted
113|סתם|אל נא תהי כמת מובא לראיית מצורע כמת.||asserted
113|סתם|הבה לי בנים ואם אין מתה אנכי מובא לראיית חסר בנים כמת.||asserted
114|ברייתא, תנו רבנן|אם בחקתי תלכו הוא לשון תחנונים.|פירוש אם בפסוק זה; אין להכליל לכל אם|asserted
115|ברייתא המצטטת את משה|ישראל היו צריכים להשיב תן אתה על מי יתן והיה לבבם זה להם.||asserted
115,116,117|משה בתוך הברייתא|ישראל מכונים כפויי טובה בני כפויי טובה.|ראיית כפויי טובה מהלחם וראיית בני כפויי טובה מאדם|asserted
118|סתם|משה רמז להם רק לאחר ארבעים שנה.|אף משה; פסוקי דברים כט|asserted
118|רבה|אין אדם עומד על דעת רבו עד ארבעים שנה.|שמע מינה מן הסיפור; רבה ולא רבא|asserted
119|רבי בנאה באמצעות רבי יוחנן|כשישראל עוסקים בתורה ובגמילות חסדים יצרם מסור בידם ואינם מסורים ביד יצרם.|תורה וגמילות חסדים יחד|conditional
119|רבי בנאה באמצעות רבי יוחנן|זריעה מתפרשת כצדקה ומים כתורה בפסוק אשריכם זורעי.|דרשת הפסוק|asserted
120|תנא דבי אליהו|ישים אדם עצמו על דברי תורה כשור לעול וכחמור למשאוי.|לעולם|asserted
122|משנה מצוטטת|המוכר בהמה לחבירו צריך להודיע שמכר אמה או בתה לשחוט.|ארבעה פרקים בשנה|asserted
123|משנה מצוטטת|הפרקים הם ערב יום טוב אחרון של חג, ראשון של פסח, עצרת וראש השנה.||asserted
123|רבי יוסי הגלילי|גם ערב יום הכיפורים בכלל ההודעה.|בגליל|asserted
124|סתם|הכנה לאכילה די ביום אחד; להקרבה נצרכים שלושה ימים.|הבחנה ראשונה להצדקת שלושת הימים|asserted
124|משנה מצוטטת, תנא קמא|שואלין בהלכות הפסח שלושים יום לפני פסח.||asserted
124|רשב״ג|שואלין בהלכות הפסח שתי שבתות לפני פסח.||asserted
125|סתם|ישראל צריכים שלושים יום בשל ריבוי מומים הפוסלים אף בדוקין שבעין.|לקרבנות ישראל|asserted
125|סתם|לבני נח שיש להם פסול מחוסר אבר די בשלושה ימים.|הכנת קרבן שלהם|asserted
126|רבי אלעזר|מחוסר אבר אסור לבני נח ונלמד ממכל החי: חיין ראשי אברים שלה.|קרבנות בני נח|asserted
127|סתם|פסול טריפה יכול להילמד מלחיות זרע.|רק למאן דאמר טריפה אינה יולדת; נבחן בהמשך|conditional
128|סתם|למאן דאמר טריפה יולדת לומדים מאתך, בדומין לך.|ההנחה שנח אינו טריפה נידונה בהמשך|asserted
128|סתם|תמים כתיב בנח משמש מענה לחשש שהיה טריפה.|מענה מאותגר בהמשך|challenged
129|סתם|צדיק כתיב ביה משמש מענה לטענה שתמים רק בדרכיו.|המענה אינו סוף הדיון; המשך ב6a:3|challenged'''
claims=[]
for k,line in enumerate(rows.splitlines(),1):
 ns,h,p,c,m=line.split('|'); ns=[int(n) for n in ns.split(',')]; claims.append(dict(id=f'az_r1_c{k:03}',evidence=[anchor(n) for n in ns],holder=h,proposition=p,conditions=c.split('; ') if c else [],assertion_mode=m,origin='source_paraphrase',core_claim=any(n in core for n in ns),local_status='source-local only; no practical halakhic ruling inferred'))
questions=[]
for n,q in [(3,'מדוע כל שונה אינו שונה את הגרסה האחרת?'),(4,'האם יתנו עידיהם עוסק בעובדי כוכבים והלא בישראל?'),(8,'האם יש ערבוביא לפני הקב״ה?'),(9,'מדוע רומי ראשונה ומנין שהיא חשובה?'),(110,'כיצד רבי יוסי מפרש למען ייטב אם מדובר בביטול המיתה?'),(111,'כיצד תנא קמא מפרש אכן כאדם תמותון?'),(112,'האם דתן ואבירם מתו?'),(119,'מה פירוש אשריכם זורעי על כל מים משלחי רגל השור והחמור?'),(121,'מדוע נצרכים כל שלושת הימים?'),(124,'האם די בשלושה ימים להקרבה מול שלושים יום בהלכות הפסח?'),(126,'מנין למחוסר אבר שאסור לבני נח?'),(127,'האם מכל החי נצרך למעט טריפה?'),(128,'כיצד נלמד טריפה למאן דאמר שיולדת?'),(128,'שמא נח עצמו טריפה?'),(129,'שמא תמים פירושו בדרכיו?')]: questions.append(dict(id=f'az_r1_q{len(questions)+1:03}',evidence=[anchor(n)],formulation=q,origin='explicit',answer_scope='local continuation read; see context notes'))
edges=[]
for x,y,r,note in [(2,1,'support','proof texts support permissibility of readings'),(4,2,'objection','Israel referent undermines first עידיהם proof'),(5,4,'answer','replacement verse; not identification of Rav versus Shmuel'),(8,7,'qualification','separate entrance explained by hearers, not divine confusion'),(110,109,'answer','absence of death itself maximal good'),(111,107,'qualification','first tanna reads death as poverty; doctrinal opposition preserved'),(112,111,'support','poverty exemplum'),(113,111,'support','three further scriptural proofs'),(116,115,'support','ingratitude proof continues over page'),(117,115,'support','ancestral ingratitude proof'),(118,115,'continuation','delayed rebuke then Rabbah inference'),(120,119,'continuation','second part of same verse; different authority'),(122,121,'objection','one-day food preparation challenges three-day requirement'),(124,122,'distinction','food versus sacrifice'),(124,124,'objection','thirty-day counterexample challenges sacrifice sufficiency'),(125,124,'answer','different blemish standards'),(126,125,'support','missing-limb scriptural derivation'),(127,126,'objection','verse may exclude terefa'),(128,127,'answer','אתך for view terefa bears young'),(129,128,'objection','תמים may be moral description'),(130,129,'answer','rejects Noah-as-terefa by absurd implication'),(131,128,'qualification','לחיות זרע adds exclusion of old and sterile beyond resemblance')]: edges.append(dict(id=f'az_r1_e{len(edges)+1:03}',source_ord=x,target_ord=y,relation=r,evidence=[anchor(x),anchor(y)] if x!=y else [anchor(x)],explanation=note,explicitness='source_explicit',note='Endpoints are source intervals, not producer records. Same-segment edge refers to distinct clauses.'))
obj=dict(review_schema='source-only-independent-reading-v1',reviewer='/root/review_avodah',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),blind=True,prior_producer_labels_seen=False,source_path=str(source),source_sha256=sha,source_version_title=d.get('versionTitle'),plan_sha256=ph,plan_file_sha256=hashlib.sha256(planpath.read_bytes()).hexdigest(),contract_hashes={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in ['research/bavli_production_v1/schema.json','research/bavli_production_v1/PROTOCOL.md']},core_blocks=['block_000000','block_000011','block_000012'],core_ordinals=sorted(core),context_read_ordinals=list(range(10,46))+list(range(98,110))+list(range(130,143)),claims=claims,questions=questions,edges=edges,transmissions=[dict(evidence=[anchor(1)],holder_candidates=['רב','שמואל'],resolution='No individual mapping from order; alternate wording retained'),dict(evidence=[anchor(6)],speaker_candidates=['ר׳ חנינא בר פפא','ר׳ שמלאי'],resolution='ואיתימא; not jointly asserted by both'),dict(evidence=[anchor(119)],reporter='רבי יוחנן',authority='רבי בנאה',order=['רבי יוחנן','רבי בנאה']),dict(evidence=[anchor(120)],collective='תנא דבי אליהו'),dict(evidence=[anchor(118)],speaker='רבה',note='Not רבא')],boundaries=[dict(start=0,end=0,material='mishnah legal dispute',status='closed at colon; later discussion returns'),dict(start=1,end=5,material='wording and scriptural derivation',status='closed'),dict(start=6,end=44,material='future judgment aggadic narrative with anonymous interventions, quoted divine/national dialogue, alternative placement of Rabbi Yitzhak dictum',status='read through 45; broader laughter discussion open right'),dict(start=100,end=113,material='Sinai, mortality, descendants and poverty',status='context plus sampled tail; resolved readings in core depend on preceding tannaitic alternatives'),dict(start=114,end=114,material='baraita: conditional wording as supplication',status='closed'),dict(start=115,end=118,material='ingratitude, Moses delayed understanding, Rabbah inference',status='closed'),dict(start=119,end=120,material='Torah and charity; verse continuation and yoke simile',status='closed'),dict(start=121,end=131,material='three-day preparation and Noah sacrifice fitness',status='closed after context; sampled core cuts before last objections'),dict(start=132,end=140,material='whether festival day included',status='context only; not extracted as sampled claims'),dict(start=141,end=142,material='benefit versus stumbling-block reason',status='context only; open right')],context_notes=['Opening narrative quotes Rome and Persia self-serving assertions which are rejected inside narrative, not maintained historical assertions by darshan.','At 2b:17–3a:3 initial no-reward interpretation is narrowed to reward as uncommanded; must not flatten into no reward.','At 3b:1 distressed person exemption is distinguished from kicking sukkah.','5a:6 initially no descendants is corrected at 5a:11 to as though we had not come; core 5a:16 depends on mortality debate.','6a:3 rejects Noah-as-terefa hypothesis; 6a:4 explains why לחיות זרע remains needed (old/sterile exclusion).','Core claim inventory is independently identified finite denominator, not a guarantee of exhaustive atomic splitting. Context readings not counted as core extraction.'],counts=dict(core_segments=30,endpoint_segments=10,probability_segments=20,claims=len(claims),questions=len(questions),edges=len(edges),context_segments=61),limitations=['Only first three planned blocks reviewed; 28 remain.','No human scholarly certification.','No production or task eligibility acceptance.','Full narrative continuation beyond 3b:7 not read.'])
assert len(obj['context_read_ordinals'])==61
p=out/'reading_001_frozen.json'; p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8'); digest=hashlib.sha256(p.read_bytes()).hexdigest(); (out/'reading_001_frozen.sha256').write_text(digest+'  reading_001_frozen.json\n',encoding='ascii'); print(json.dumps({'sha256':digest,'claims':len(claims),'questions':len(questions),'edges':len(edges),'core_segments':30,'context':61}))
