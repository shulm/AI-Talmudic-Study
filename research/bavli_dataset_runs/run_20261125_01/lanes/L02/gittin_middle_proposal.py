"""Authored source pass bridging 4b:18–5b:6; preserve successive hypotheses."""
import gittin_opening_proposal as a
a.records.clear()
r,j,JOB,add=a.r,a.j,a.JOB,a.add
refs=list(a.byref);core=refs[refs.index('4b:18'):refs.index('5b:6')+1]
s=add('s.learned','structure',core,dict(title='לאחר שלמדו, שליח שנשתתק ושני שליחים; דיווח רבי יהושע בן לוי',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rows=[
('f1',['4b:18'],'המביא מחוץ לארץ ואינו יכול לומר את ההצהרה, אם יש עדים יתקיים בחותמיו',['אינו יכול להצהיר; יש עדי קיום'],'קול המשנה המצוטטת','conditional'),
('f2',['5a:1'],'העמדה בחרש כבר מתחילה נדחית: חרש שוטה וקטן אינם כשרים להביא גט',['חרש מתחילת השליחות; לא פקח שנעשה חרש'],'קול הדיון המצטט משנה','asserted'),
('f3',['5a:2'],'רב יוסף מעמיד בפקח שנתן את הגט ולא הספיק להצהיר עד שנתחרש',['היה פקח בנתינה; נתחרש לפני ההצהרה'],'רב יוסף','asserted'),
('f4',['5a:2'],'האפשרות להסתפק בקיום נוחה לרבא וקשה לרבה',['שליח נתחרש אחרי נתינה'],'קול הדיון הסתמי','queried'),
('f5',['5a:3'],'התשובה מעמידה לאחר שלמדו לשמה',['אחרי שלמדו; אין לקבוע שבכל תקופה די בקיום'],'קול הדיון הסתמי','asserted'),
('f6',['5a:3'],'גם לאחר שלמדו, שליח היכול להצהיר צריך להצהיר שמא יחזור הדבר לקלקולו',['יכול להצהיר; לאחר שלמדו'],'קול הדיון הסתמי','asserted'),
('f7',['5a:4'],'פקח ונתחרש אינו מצוי, ובמקרה לא שכיח זה לא גזרו',['פקח בנתינה שנעשה חרש לפני ההצהרה'],'קול הדיון הסתמי','asserted'),
('f8',['5a:5'],'האשה עצמה יכולה להביא גיטה אך צריכה להצהיר אף שהמקרה אינו מצוי',['האשה מביאה גיטה בשליחות לפי המקרה המצוטט'],'קול המשנה המצוטטת','conditional'),
('f9',['5a:5'],'חובת האשה להצהיר מוסברת שלא לחלק בשליחות',['מענה לאי-שכיחות; דין שליחות'],'קול הדיון הסתמי','asserted'),
('f10',['5a:6'],'הברייתא פוטרת את הבעל עצמו המביא גיטו מן ההצהרה',['הבעל עצמו מביא גט'],'קול הברייתא המצוטטת','conditional'),
('f11',['5a:7'],'טעם ההצהרה הוא חשש שהבעל יערער ויפסול, ואין לחשוש כן כשהוא עצמו אוחז בגט ומביאו',['נימוק הפטור לבעל עצמו'],'קול הדיון הסתמי','asserted'),
('f12',['5a:8'],'שמואל שואל את רב הונא אם שני מביאים מחוץ לארץ צריכים להצהיר',['שני מביאים מחוץ לארץ'],'שמואל','queried'),
('f13',['5a:8'],'רב הונא משיב ששני המביאים אינם צריכים להצהיר',['שני מביאים; רב הונא משיב לשמואל'],'רב הונא','asserted'),
('f14',['5a:8'],'רב הונא מנמק שאילו אמרו בפנינו גרשה היו נאמנים',['נימוק נאמנות שני המביאים'],'רב הונא','asserted'),
('f15',['5a:9'],'גם את פטור שני המביאים מעמידים לאחר שלמדו כדי ליישב לפי רבה',['אוקימתא לפי רבה; אחרי שלמדו'],'קול הדיון הסתמי','asserted'),
('f16',['5a:10'],'שליח יחיד עדיין חייב לאחר שלמדו משום חשש חזרה לקלקול',['שליח אחד; לאחר שלמדו'],'קול הדיון הסתמי','asserted'),
('f17',['5a:11'],'שני מביאים הם מקרה לא שכיח ולכן לא גזרו בו',['שניים המביאים גט; תשובה בהקשר לאחר שלמדו'],'קול הדיון הסתמי','asserted'),
('f18',['5a:12'],'שוב מובאת חובת האשה המביאה גיטה למרות אי שכיחות, ושוב מוסבר שלא לחלק בשליחות',['הופעה חוזרת במסלול שני מביאים; אין למחוק ככפילות'],'קול הדיון המצטט משנה','asserted'),
('f19',['5a:13'],'שוב נידון פטור הבעל המביא בעצמו: החזקתו בגט מסלקת את חשש ערעורו',['הופעה חוזרת; בעל עצמו מביא'],'קול הדיון המצטט ברייתא','asserted'),
('f20',['5a:14'],'אם נתן גט מחוץ לארץ בלי ההצהרה והוא מתקיים בחותמיו, כשר; אם אינו מתקיים, פסול',['הנתינה כבר נעשתה; קיום או העדרו'],'קול המקור המצוטט','conditional'),
('f21',['5a:14'],'המקור אומר שההצהרה נצרכה להקל ולא להחמיר',['נימוק הדין המצוטט; פירושו מתברר בהמשך'],'קול המקור המצוטט','asserted'),
('f22',['5a:15'],'גם את הכשר הגט בקיום בלי הצהרה מעמידים לאחר שלמדו',['תשובת הגמרא לקושי על רבה'],'קול הדיון הסתמי','asserted'),
('f23',['5a:16'],'נוכח גזירת חזרה לקלקול מעמידים כשנישאת',['אחרי נישואין; הגבלה על הכשר ללא הצהרה'],'קול הדיון הסתמי','asserted'),
('f24',['5a:17'],'המשפט להקל מתפרש כנגד הצעה להוציאה לאחר שנישאת',['אם נשקול להוציאה בגלל ההצהרה החסרה'],'קול הדיון הסתמי','asserted'),
('f25',['5b:1'],'טעם ההצהרה חשש ערעור בעל; כשהבעל אינו מערער אין אנו קמים לערער עליה',['במסגרת דיון הגט שכבר נישאת בו'],'קול הדיון הסתמי','asserted'),
('f26',['5b:2'],'רבי יוחנן ורבי יהושע בן לוי מובאים בזוג חד אמר לשמה וחד אמר קיום',['טרם הזיהוי שבהמשך; אין שיוך לפי סדר השמות'],'זוג רבי יוחנן / רבי יהושע בן לוי','unresolved'),
('f27',['5b:3','5b:4'],'תסתיים מזהה את רבי יהושע בן לוי עם הטעם שאין בקיאים לשמה, מתוך תשובתו לרבי שמעון בר אבא',['הראיה והסבר המעשה מקבלים קושיה מיד בהמשך'],'קול הדיון הסתמי','asserted'),
('f28',['5b:3'],'רבי שמעון בר אבא שואל את רבי יהושע בן לוי אם עליו להצהיר',['הביא גט בפניו'],'רבי שמעון בר אבא','queried'),
('f29',['5b:4'],'רבי יהושע בן לוי משיב שאין צורך, ואומר שהדרישה נאמרה בדורות הראשונים שאינם בקיאים, לא באחרונים שבקיאים',['מעשה זה; ההמשך מגביל את הבנת הפטור'],'רבי יהושע בן לוי','asserted'),
('f30',['5b:5'],'הגמרא מקשה שהרי רבה מקבל גם את טעם רבא, ועוד קיימת גזירת חזרה לקלקול',['קושיה על הסתפקות בבקיאות להסביר פטור ההצהרה'],'קול הדיון הסתמי','queried'),
('f31',['5b:6'],'התשובה מוסיפה שהיה עם רבי שמעון בר אבא אדם אחר שלא נמנה מפני כבוד רבי שמעון',['שני מביאים; לא היתר גורף לכל יחיד לאחר שלמדו'],'קול הדיון הסתמי','asserted'),
]
claims={}
for key,rr,prop,cond,holder,mode in rows:
    uid=add('u.'+key,'utterances',rr,dict(textual_voice=holder,discourse_role='question' if mode=='queried' else 'quoted_ruling_or_argument',composition='composite' if key in ['f18','f19','f20','f27'] else 'atomic'),origin='editorial_inference')
    cid=add('c.'+key,'claims',rr,dict(proposition=prop,conditions=cond,scope='Local argument stage and explicitly stated conditions only.',assertion_mode=mode),[uid]);claims[key]=cid
    pair=key=='f26'; anon=holder.startswith('קול')
    candidates=['רבי יוחנן','רבי יהושע בן לוי'] if pair else ([] if anon else [holder])
    aid=add('a.'+key,'attributions',rr,dict(surface=holder,role='anonymous' if anon else ('speaker' if mode=='queried' else 'position_holder'),candidates=candidates,scope=prop,transmission_chain=[]),[uid,cid],['Name-order attribution prohibited; later stages must be linked.'] if pair else [])
    add('p.'+key,'positions',rr,dict(holder_candidates=candidates,claim_id=cid,question_id=None,conditions=cond,local_status=mode+'; not a final practical ruling'),[cid,aid])
qs=[('unable',['4b:18','5a:1'],'מהו אינו יכול לומר?'),('rabbah_again',['5a:2'],'כיצד מועיל קיום לפי רבה?'),('capable',['5a:3'],'אם לאחר שלמדו, מדוע יכול חייב?'),('rare',['5a:4'],'מדוע לא לגזור גם בפקח שנתחרש?'),('woman',['5a:5'],'והרי אשה אינה שכיחה ואף היא צריכה לומר?'),('husband',['5a:6'],'אם לא לחלק בשליחות, למה הבעל עצמו פטור?'),('two',['5a:8'],'האם שני מביאים צריכים להצהיר?'),('two_rabbah',['5a:9'],'כיצד פטור שניים מתאים לרבה?'),('single',['5a:10'],'אם למדו, מדוע היחיד אינו פטור?'),('both',['5a:11'],'אם גוזרים, מדוע לא גם בשניים?'),('woman_repeat',['5a:12'],'והרי האשה אינה שכיחה וחייבת?'),('husband_repeat',['5a:13'],'מדוע שוב פטור בעל עצמו?'),('validate',['5a:15'],'כיצד קיום בלי הצהרה מועיל לרבה?'),('decree',['5a:16'],'הרי גוזרים חזרה לקלקול, ומה פשר להקל אם ההיתר בגלל שנישאת?'),('identification',['5b:5'],'האם די בבקיאות לאור קיום וגזירת חזרה לקלקול?')]
questions={}
for key,rr,form in qs:questions[key]=add('q.middle.'+key,'questions',rr,dict(formulation=form,question_origin='explicit',conditions=['Local case and current proposed interpretation'],answer_set_status='unreviewed_alternatives'))
edges=[('f2','unable','objection',['5a:1']),('f3','unable','answer',['5a:2']),('f5','rabbah_again','answer',['5a:3']),('f6','capable','answer',['5a:3']),('f7','rare','answer',['5a:4']),('f9','woman','answer',['5a:5']),('f11','husband','answer',['5a:7']),('f13','two','answer',['5a:8']),('f14','f13','support',['5a:8']),('f15','two_rabbah','answer',['5a:9']),('f16','single','answer',['5a:10']),('f17','both','answer',['5a:11']),('f18','woman_repeat','answer',['5a:12']),('f19','husband_repeat','answer',['5a:13']),('f22','validate','answer',['5a:15']),('f23','decree','answer',['5a:16']),('f24','f23','qualification',['5a:17']),('f25','f24','support',['5b:1']),('f29','f27','support',['5b:3','5b:4']),('f30','f29','objection',['5b:5']),('f31','identification','answer',['5b:6'])]
for n,(x,y,rel,rr) in enumerate(edges):
    src=claims[x];tgt=questions[y] if y in questions else claims[y]
    add('e.middle.'+str(n),'edges',rr,dict(source_id=src,target_id=tgt,relation=rel,explicitness='source_explicit'),[src,tgt])
add('e.middle_cont','edges',['4b:18'],dict(source_id='L02.git.open.s.tests',target_id=s,relation='continuation',explicitness='editorial_reconstruction'),['L02.git.open.s.tests',s],origin='editorial_inference')
coverage=[]
for f in core:
    sid=a.byref[f]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in a.records if (x['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Actual original-source reading and omission rereading of '+f+' with continuation through 6a:19. Preserve rare-case conditions, repetitions and dialectical stages; no generic whole-tractate completion.'))
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='/root/L02_gittin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.records,coverage=coverage,open_tails=r.current(JOB)['open_tails'])
r.immutable(JOB/'authored/L02_middle_v2.json',r.encoded(p))
print(JOB/'authored/L02_middle_v2.json')
