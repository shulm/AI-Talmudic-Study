"""Explicit second reading of Gittin 3a:16–4b:17; context through 5a."""
import gittin_opening_proposal as a

a.records.clear()
r, j, JOB, byref = a.r, a.j, a.JOB, a.byref
add, claims, questions = a.add, {}, {}
refs = list(byref)
core = refs[refs.index('3a:16'):refs.index('4b:17')+1]
tanna = core[:core.index('4a:6')]
tests = core[core.index('4a:6'):]
s1 = add('s.tanna','structure',tanna,dict(title='בירור התנא המחייב כתיבה וחתימה לשמה',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
s2 = add('s.tests','structure',tests,dict(title='בדיקת הטעמים מתוך המשנה והודאת רבה בטעם רבא',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference')

# proposition; explicit conditions; holder/voice; local status. Attributions
# to the tannaim inside a proposed explanation stay conditional explanations.
rows = [
('d1',['3a:16','3b:1'],'לפי רבה נדרשת זיהוי שיטה המחייבת כתיבה וחתימה לשמה',['קושיית הגמרא על פירוש רבה'],'קול הדיון הסתמי','queried'),
('d2',['3b:1'],'רבי מאיר דורש חתימה ולא כתיבה לשמה לפי הצגת הגמרא',['הצעת זיהוי התנא נבחנת כאן'],'רבי מאיר כפי שהגמרא מציגה','asserted'),
('d3',['3b:1'],'המשנה המצוטטת אוסרת כתיבה במחובר אך מכשירה אם כתבו במחובר, תלשו, חתמו ונתנו',['כתיבה במחובר ולאחריה תלישה חתימה ונתינה'],'קול המשנה המצוטטת','asserted'),
('d4',['3b:2'],'רבי אלעזר דורש כתיבה ולא חתימה לשמה לפי הצגת הגמרא',['הצעת זיהוי תנאי שנייה'],'רבי אלעזר כפי שהגמרא מציגה','asserted'),
('d5',['3b:2'],'מוצע שרבי אלעזר דורש חתימה לשמה מדרבנן אף שאינו דורש מן התורה',['הצעה הנדחית בצורתה זו מתוך המשנה המצוטטת'],'קול הדיון הסתמי','rejected'),
('d6',['3b:3'],'גט בכתב ידו בלי עדים פסול, ואם נישאה הולד כשר',['כתב יד הבעל; אין עדים'],'קול המשנה המצוטטת','conditional'),
('d7',['3b:3'],'גט שיש עליו עדים ואין בו זמן פסול, ואם נישאה הולד כשר',['יש עדים; אין זמן'],'קול המשנה המצוטטת','conditional'),
('d8',['3b:3'],'גט שיש בו זמן ועד אחד פסול, ואם נישאה הולד כשר',['יש זמן; עד אחד'],'קול המשנה המצוטטת','conditional'),
('d9',['3b:4'],'רבי אלעזר מכשיר גט שאין עליו עדים אם נתנו בפני עדים',['אין עדים חתומים; נתינה בפני עדים'],'רבי אלעזר','conditional'),
('d10',['3b:4'],'רבי אלעזר מוסיף שגובה מנכסים משועבדים',['במסגרת המקרה המצוטט'],'רבי אלעזר','asserted'),
('d11',['3b:4'],'לדברי רבי אלעזר חתימת העדים על הגט היא מפני תיקון העולם',['נימוק בתוך המשנה המצוטטת'],'רבי אלעזר','asserted'),
('d12',['3b:5'],'מוצע שרבי מאיר דורש כתיבה לשמה מדרבנן בלבד',['הצעת זיהוי חלופית שנדחית בהמשך'],'קול הדיון הסתמי','rejected'),
('d13',['3b:5','4a:1'],'רב נחמן מדווח שרבי מאיר מכשיר אף גט שמצאו באשפה וחתמו ונתנו',['נמצא באשפה; חתימה ונתינה לאחר מכן'],'רבי מאיר מפי רב נחמן','asserted'),
('d14',['4a:1'],'העמדת דברי רב נחמן בדין תורה בלבד נדחית כי אז היה צריך לומר דבר תורה',['דחיית צמצום היקף הדיווח'],'קול הדיון הסתמי','asserted'),
('d15',['4a:2'],'העמדה ברבי אלעזר מתוקנת: אינו צריך חתימה כשאין עדים כלל, אך כשיש עדים צריך',['הבחנה בין העדר חתימות לבין חתימות קיימות'],'קול הדיון הסתמי המעמיד ברבי אלעזר','asserted'),
('d16',['4a:2'],'רבי אבא אומר שרבי אלעזר מודה שמזויף מתוכו פסול',['מזויף מתוכו'],'רבי אלעזר מפי רבי אבא','conditional'),
('d17',['4a:3'],'רב אשי מזהה את התנא עם רבי יהודה',['חלופה להעמדה ברבי אלעזר'],'רב אשי','asserted'),
('d18',['4a:3'],'רבי יהודה פוסל עד שכתיבה וחתימה יהיו בתלוש',['כתיבה וחתימה בתלוש'],'רבי יהודה במשנה המצוטטת','asserted'),
('d19',['4a:5'],'תחילה חיפשו העמדה ברבי מאיר מפני שסתם משנה רבי מאיר',['הסבר סדר בירור הגמרא'],'קול הדיון הסתמי','asserted'),
('d20',['4a:5'],'חיפשו העמדה ברבי אלעזר מפני שנוקטים שהלכה כמותו בגיטין',['הנמקת סדר הבירור; אמירה מקומית של הגמרא'],'קול הדיון הסתמי','asserted'),
('t1',['4a:6'],'המשנה חוזרת ומובאת: רבן גמליאל מחייב מרקם וחגר ורבי אליעזר מכפר לודים ללוד',['מובאה חוזרת, לא מחיקת ההופעה הקודמת'],'רבן גמליאל ורבי אליעזר במובאה','asserted'),
('t2',['4a:6'],'אביי מעמיד בעיירות הסמוכות לארץ ישראל ומובלעות בתחום ארץ ישראל',['פירוש תחום המקרים במשנה'],'אביי','asserted'),
('t3',['4a:7'],'רבה בר בר חנה מעיד שראה את המקום והמרחק כמבי כובי לפומבדיתא',['תיאור ראייה אישית והקבלת מרחק; לא רבה סתם'],'רבה בר בר חנה','asserted'),
('t4',['4a:8'],'מוסקת דעת תנא קמא שאין צורך במקרים אלו ומוצע לתלות המחלוקת בבקיאות לשמה לעומת זמינות עדי קיום',['העמדת מחלוקת מוצעת שנדחית; אין שיוך אוטומטי למר סבר'],'קול הדיון הסתמי','rejected'),
('t5',['4a:9'],'נדחית הראיה למחלוקת הטעמים: רבה ורבא יכולים כל אחד לפרש לפי טעמו',['לא; כל מסלול פירוש נבדל'],'קול הדיון הסתמי','asserted'),
('t6',['4a:9'],'בפירוש רבה כולם חוששים לבקיאות לשמה, ותנא קמא מניח שהסמוכות למדו',['בתוך פירוש רבה בלבד'],'תנא קמא בפירוש רבה','conditional'),
('t7',['4a:10'],'בפירוש רבה רבן גמליאל סובר שמובלעות למדו וסמוכות לא',['בתוך פירוש רבה בלבד'],'רבן גמליאל בפירוש רבה','conditional'),
('t8',['4a:10'],'בפירוש רבה רבי אליעזר מחייב גם במובלעות כדי שלא לחלק במדינת הים',['בתוך פירוש רבה בלבד'],'רבי אליעזר בפירוש רבה','conditional'),
('t9',['4a:11'],'בפירוש רבא כולם חוששים לזמינות עדי קיום ותנא קמא מניח שבסמוכות מצויים',['בתוך פירוש רבא בלבד'],'תנא קמא בפירוש רבא','conditional'),
('t10',['4a:12'],'בפירוש רבא רבן גמליאל סובר שבמובלעות מצויים ובסמוכות לא',['בתוך פירוש רבא בלבד'],'רבן גמליאל בפירוש רבא','conditional'),
('t11',['4a:12'],'בפירוש רבא רבי אליעזר מחייב אף במובלעות כדי שלא לחלק במדינת הים',['בתוך פירוש רבא בלבד'],'רבי אליעזר בפירוש רבא','conditional'),
('t12',['4a:13','4b:1'],'מן הזכרת מוליך בחכמים מוסק שתנא קמא פוטר, ומוצע לתלות את המחלוקת בשני הטעמים',['ראיה מוצעת בלבד, נענית בשני מסלולים'],'קול הדיון הסתמי','challenged'),
('t13',['4b:2','4b:3'],'רבה מפרש שכולם חוששים לשמה, ותנא קמא אינו גוזר מוליך אטו מביא',['פירוש רבה למחלוקת מוליך'],'תנא קמא בפירוש רבה','conditional'),
('t14',['4b:2','4b:4'],'רבה מפרש שחכמים האחרונים גוזרים מוליך אטו מביא',['פירוש רבה; חכמים בתראי'],'חכמים בפירוש רבה','conditional'),
('t15',['4b:5'],'רבא מפרש שכולם חוששים לקיום וחכמים האחרונים באו לפרש את תנא קמא',['אין מחלוקת מוליך לפי פירוש זה'],'קול הדיון בשם פירוש רבא','asserted'),
('t16',['4b:6'],'מדיוק ממדינה למדינה מוצע פטור באותה מדינה בחוץ לארץ, שנוח לרבא וקשה לרבה',['לשון ראשונה של הקושיה; דיוק מוצע'],'קול הדיון הסתמי','challenged'),
('t17',['4b:7'],'התשובה מחליפה את הדיוק לפטור ממדינה למדינה בארץ ישראל',['מענה לפי המסלול הראשון'],'קול הדיון הסתמי','asserted'),
('t18',['4b:8'],'הכפילות עם פטור ארץ ישראל נענית: בלעדיה היה אפשר להבין פטור בדיעבד בלבד, והדיוק מלמד גם לכתחילה',['הוה אמינא בדיעבד נדחית'],'קול הדיון הסתמי','asserted'),
('t19',['4b:9','4b:10'],'יש מקשים בנוסח אחר: דיוק פטור ממדינה למדינה בארץ ישראל נוח לרבה וקשה לרבא',['איכא דמותיב; גרסת קושיה חלופית'],'קול הדיון הסתמי','queried'),
('t20',['4b:10'],'בנוסח החלופי מוחלף הדיוק לפטור באותה מדינה במדינת הים',['תשובה ראשונית בנוסח השני'],'קול הדיון הסתמי','asserted'),
('t21',['4b:11'],'כנגד חובת העברה בין מדינות בארץ ישראל מקשים שהיה צריך לשנות ממדינה למדינה סתם',['קושיית ניסוח על ההשלכה של התשובה'],'קול הדיון הסתמי','queried'),
('t22',['4b:12'],'למסקנת המענה גם ממדינה למדינה בארץ ישראל פטור, מפני שעולי רגלים מצויים',['תנועת עולי רגלים מאפשרת קיום'],'קול הדיון הסתמי','asserted'),
('t23',['4b:13'],'בזמן שאין בית המקדש קיים בתי דין קבועים מספקים מציאות עדים',['מענה לתקופה בלי עלייה לרגל למקדש'],'קול הדיון הסתמי','asserted'),
('t24',['4b:14'],'רשב״ג מחייב אפילו מהגמוניא להגמוניא',['מובאה חוזרת של משנה'],'רשב״ג','asserted'),
('t25',['4b:14'],'רבי יצחק מפרש שהיתה בעיר עססיות בארץ ישראל חלוקה לשתי הגמוניות המקפידות זו על זו ולכן נדרשה הצהרה',['שתי הגמוניות נפרדות באותה עיר'],'רבי יצחק','asserted'),
('t26',['4b:15'],'המקרה נוח לרבא וקשה לרבה, ונענה שרבה מקבל גם את טעם רבא',['אין להציג את רבה כמי ששולל צורך קיום'],'קול הדיון הסתמי','asserted'),
('t27',['4b:16'],'לאחר הודאת רבה בטעם רבא נשאר הבדל כשהביאו שניים',['הבדל מתוקן בשלב זה; אין כל שלוש הנפקויות הראשונות נשארות'],'קול הדיון הסתמי','asserted'),
('t28',['4b:17'],'לאחר הודאת רבה בטעם רבא נשאר גם הבדל באותה מדינה במדינת הים',['הבדל מתוקן בשלב זה'],'קול הדיון הסתמי','asserted'),
]

for key, rr, proposition, conditions, holder, mode in rows:
    uid=add('u.'+key,'utterances',rr,dict(textual_voice=holder,discourse_role='quoted_source' if key in ['d3','d6','d7','d8','d9','d10','d11','d18','t1','t24'] else 'argument_stage',composition='composite' if key in ['d3','t1','t4','t12','t26'] else 'atomic'),origin='editorial_inference')
    cid=add('c.'+key,'claims',rr,dict(proposition=proposition,conditions=conditions,scope='This local stage and named interpretive branch; no independent halachic certification.',assertion_mode=mode),[uid])
    claims[key]=cid
    anonymous=holder.startswith('קול')
    aid=add('a.'+key,'attributions',rr,dict(surface=holder,role='anonymous' if anonymous else 'position_holder',candidates=[] if anonymous else [holder],scope=proposition,transmission_chain=[]),[cid,uid])
    add('p.'+key,'positions',rr,dict(holder_candidates=[] if anonymous else [holder],claim_id=cid,question_id=None,conditions=conditions,local_status=mode+'; preserve explanatory branch'),[cid,aid])

for key,rr,transmitter,authority in [('d13',['3b:5','4a:1'],'רב נחמן','רבי מאיר'),('d16',['4a:2'],'רבי אבא','רבי אלעזר')]:
    add('transmitter.'+key,'attributions',rr,dict(surface=transmitter,role='transmitter',candidates=[transmitter],scope=claims[key],transmission_chain=[transmitter,authority]),[claims[key]])
    add('authority.'+key,'attributions',rr,dict(surface=authority,role='quoted_authority',candidates=[authority],scope=claims[key],transmission_chain=[transmitter,authority]),[claims[key]])

qs=[
('tanna',['3a:16','3b:1'],'מי התנא המצריך כתיבה וחתימה לשמה?'),
('elazar',['3b:2','3b:3','3b:4'],'כיצד יידרש רבי אלעזר לחתימה מדרבנן אם הוא מכשיר בלי עדים חתומים?'),
('meir',['3b:5','4a:1'],'כיצד תידרש כתיבה לשמה מדרבנן לרבי מאיר לאור מצאו באשפה?'),
('torah',['4a:1'],'האם אפשר לצמצם את הדיווח לדין תורה אף שהלשון לא ציינה זאת?'),
('first',['4a:4'],'מדוע לא הועמדה המשנה ברבי יהודה מתחילה?'),
('places',['4a:8'],'האם מחלוקת התנאים על הסמוכות והמובלעות היא מחלוקת טעמים?'),
('outgoing',['4a:13','4b:1'],'האם מחלוקת מוליך מוכיחה מחלוקת על הטעם?'),
('same',['4b:6'],'האם פטור באותה מדינה במדינת הים סותר את רבה?'),
('repeat',['4b:8'],'הרי הפטור בארץ ישראל נשנה במפורש, למה דיוק נוסף?'),
('alternative',['4b:9','4b:10'],'בנוסח אחר, האם הפטור בין מדינות בארץ ישראל סותר את רבא?'),
('wording',['4b:11'],'אם בין מדינות בארץ ישראל צריך, למה לא שנה ממדינה למדינה סתם?'),
('temple',['4b:13'],'מה הדין כשאין בית המקדש קיים?'),
('gov',['4b:14','4b:15'],'כיצד יסביר רבה חיוב בין הגמוניות בארץ ישראל?'),
('remaining',['4b:16'],'מה ההבדל בין רבה לרבא אחרי שרבה מקבל גם את טעם רבא?')]
for key,rr,form in qs:
    questions[key]=add('q.'+key,'questions',rr,dict(formulation=form,question_origin='explicit',conditions=['Local stage; retain alternative version where stated.'],answer_set_status='unreviewed_alternatives'))

edge_rows=[
('d3','d2','support',['3b:1']),('d9','d5','objection',['3b:2','3b:4']),('d13','d12','objection',['3b:5','4a:1']),
('d14','torah','answer',['4a:1']),('d15','tanna','answer',['4a:2']),('d16','d15','support',['4a:2']),
('d17','tanna','answer',['4a:3']),('d18','d17','support',['4a:3']),('d19','first','answer',['4a:5']),('d20','first','answer',['4a:5']),
('t5','t4','objection',['4a:9']),('t6','places','answer',['4a:9']),('t7','t6','distinction',['4a:10']),('t8','t7','qualification',['4a:10']),
('t9','places','answer',['4a:11']),('t10','t9','distinction',['4a:12']),('t11','t10','qualification',['4a:12']),
('t13','outgoing','answer',['4b:2','4b:3']),('t14','t13','distinction',['4b:4']),('t15','outgoing','answer',['4b:5']),
('t17','same','answer',['4b:7']),('t18','repeat','answer',['4b:8']),('t20','alternative','answer',['4b:10']),
('t21','t20','objection',['4b:11']),('t22','wording','answer',['4b:12']),('t23','temple','answer',['4b:13']),
('t25','t24','qualification',['4b:14']),('t26','gov','answer',['4b:15']),('t27','remaining','answer',['4b:16']),('t28','remaining','answer',['4b:17'])]
for n,(src,tgt,rel,rr) in enumerate(edge_rows):
    x=claims[src];y=questions[tgt] if tgt in questions else claims[tgt]
    add('e.next.'+str(n),'edges',rr,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
for n,(x,y,rr) in enumerate([('L02.git.open.s.reasons',s1,['3a:16']),(s1,s2,['4a:5','4a:6'])]):
    add('e.cont.'+str(n),'edges',rr,dict(source_id=x,target_id=y,relation='continuation',explicitness='editorial_reconstruction'),[x,y],origin='editorial_inference')
add('e.revised_difference','edges',['4b:15','4b:16','4b:17'],dict(source_id=claims['t26'],target_id='L02.git.open.c.n2',relation='correction',explicitness='source_explicit'),[claims['t26'],'L02.git.open.c.n2'])

coverage=[]
for f in core:
    sid=byref[f]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in a.records if (x['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in x['evidence'])]
        rationale='Source-based rereading of '+f+'; original continuation through 5a:17 read. Preserved rejected proposals, alternate objection version, transmission roles and revised differences. No full tractate claim.'
        if not ids:rationale+=' No explicit '+layer+' object found in this segment after the bounded pass.'
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='/root/L02_gittin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.records,coverage=coverage,open_tails=['L02.git.open.s.reasons',s2])
r.immutable(JOB/'authored/L02_continuation_v1.json',r.encoded(p))
print(JOB/'authored/L02_continuation_v1.json')
