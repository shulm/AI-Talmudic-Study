"""Explicit source reading 5b:9–6a:5; serialization only, no inferred labels."""
import gittin_opening_proposal as a
a.records.clear()
r,j,JOB=a.r,a.j,a.JOB
def add(key,layer,refs,content,links=(),origin='source_paraphrase'):
    return a.add('resume005.'+key,layer,refs,content,links,origin=origin)
core=[f'5b:{n}' for n in range(9,23)]+[f'6a:{n}' for n in range(1,6)]
s1=add('s.number','structure',core[:11],dict(title='הסברים מתחלפים למספר הנוכחים ותיקון נתינה בלי הצהרה',primary=True,boundary='open_left',legacy_ids=[]),origin='editorial_inference')
s2=add('s.observation','structure',core[11:],dict(title='מידת נוכחות השליח בכתיבה ויציאת הסופר',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
# Separate local stages preserve rejected explanations, rather than overwrite them.
rows=[
('n1',['5b:9'],'מוצע לתלות שני נוכחים בטעם לשמה ושלושה בטעם קיום',['הצעה הנדחית בהמשך'],'קול סתמי','challenged'),
('n2',['5b:10'],'רבי יהושע בן לוי אמר שהטעם חוסר בקיאות לשמה',['ציטוט לצורך הקושיה'],'רבי יהושע בן לוי','asserted'),
('n3',['5b:10'],'רבי יוחנן אמר שהטעם חוסר עדים לקיום, ובכל זאת אמר שניים',['סתירה לשיוך המוצע, לא סתירה פנימית מוכרעת בשיטתו'],'רבי יוחנן','asserted'),
('n4',['5b:11'],'רבה מקבל גם את טעם רבא ולכן אי אפשר להסביר את המספרים כהפרדה בין הטעמים',['קושיה נוספת על ההצעה'],'קול סתמי','asserted'),
('n5',['5b:12'],'מוצע שלכולי עלמא נדרשת אפשרות קיום וכולם מקבלים שליח נעשה עד',['שלב ההסבר השני; מחלוקת דיין מוצעת בהמשך אותו שלב'],'קול סתמי','conditional'),
('n6',['5b:12'],'לפי ההסבר השני האומר שניים סובר עד נעשה דיין',['הסבר מוצע לשיטת שניים; נדחה בהמשך'],'קול סתמי','conditional'),
('n7',['5b:12'],'לפי ההסבר השני האומר שלושה סובר אין עד נעשה דיין',['הסבר מוצע לשיטת שלושה; נדחה בהמשך'],'קול סתמי','conditional'),
('n8',['5b:13'],'בדין דרבנן מקובל שעד נעשה דיין',['קושיה על הסבר המחלוקת השני'],'קול סתמי','asserted'),
('n9',['5b:14'],'המחייב שלושה חושש שאשה הכשרה להביא גט תביא ויסמכו עליה',['הסבר מתוקן למספר הנוכחים; אין להפוך את האשה לדיין'],'קול סתמי','asserted'),
('n10',['5b:15'],'המצריך שניים סובר שיודעים שהיא אשה ולא יסמכו עליה',['תשובת הצד האחר לחשש'],'קול סתמי','asserted'),
('n11',['5b:16'],'רבי מאיר אומר: המביא גט ממדינת הים שנתנו בלי הצהרה יוציא והולד ממזר',['נתינה בלא בפני נכתב ובפני נחתם'],'רבי מאיר','asserted'),
('n12',['5b:17'],'חכמים אומרים שאין הולד ממזר',['אותו מקרה של חסרון ההצהרה'],'חכמים','asserted'),
('n13',['5b:17'],'התיקון הוא ליטול ממנה ולחזור לתת בפני שניים בהצהרת בפני נכתב ובפני נחתם',['כיצד יעשה במקרה הברייתא; תומך ברבי יוחנן'],'חכמים','asserted'),
('n14',['5b:18'],'נשאל האם חסרון ההצהרה אכן גורר לרבי מאיר יוציא והולד ממזר',['קושיה על חומרת רבי מאיר'],'קול סתמי','queried'),
('n15',['5b:19'],'רבי מאיר אומר כל המשנה ממטבע חכמים בגיטין יוציא והולד ממזר',['רב המנונא משמיה דעולא; מסביר את הברייתא'],'רבי מאיר','asserted'),
('o1',['5b:20'],'בר הדיא ביקש להביא גט ופנה לרבי אחי הממונה על גיטין',['אירוע מסופר; תפקיד ממונה נזכר במפורש'],'קול המספר','asserted'),
('o2',['5b:20'],'רבי אחי הצריך את בר הדיא לעמוד על כל אות ואות',['הוראה ראשונה באירוע'],'רבי אחי','asserted'),
('o3',['5b:20'],'רבי אמי ורבי אסי אמרו לבר הדיא שאין צורך בכך',['הוראה מנוגדת לדרישת כל אות'],'רבי אמי ורבי אסי','asserted'),
('o4',['5b:21'],'עשייה לחומרא עלולה להוציא לעז על הגיטין הראשונים',['מענה להצעת החמרה; קול ההמשך אינו מסומן מחדש בשם'],'קול ההמשך','asserted'),
('o5',['5b:22'],'רבה בר בר חנה הביא גט שחציו נכתב בפניו וחציו לא, ופנה לרבי אלעזר',['מקרה מסופר; אינו רבה בעל טעם לשמה'],'קול המספר','asserted'),
('o6',['5b:22'],'רבי אלעזר אמר שאפילו שיטה אחת לשמה מספיקה ושוב אינו צריך',['הוראה לרבה בר בר חנה במצב המתואר'],'רבי אלעזר','asserted'),
('o7',['5b:22','6a:1'],'רב אשי אמר אפילו קן קולמוסא וקן מגילתא',['המשך שם הדובר מעבר לדף; פירוש השמיעה מתבאר ב6א3'],'רב אשי','asserted'),
('o8',['6a:2'],'ברייתא מכשירה כשהשליח בבית והסופר בעלייה או להפך',['המביא גט ממדינת הים; תמיכה מובאת ברב אשי'],'ברייתא אנונימית','asserted'),
('o9',['6a:2'],'ברייתא מכשירה אפילו נכנס ויוצא כל היום',['הנכנס והיוצא מזוהה רק בדיון הבא'],'ברייתא אנונימית','asserted'),
('o10',['6a:3'],'הדיון מסיק שההכשר בלי ראייה הוא כששמע קן קולמוסא וקן מגילתא',['פירוש הברייתא לצורך תמיכה ברב אשי'],'קול סתמי','asserted'),
('o11',['6a:4'],'זיהוי הנכנס והיוצא כשליח נדחה כמיותר לאחר הכשר הבית והעלייה',['הצעת זיהוי הנדחית, אין לקבעה כפירוש הברייתא'],'קול סתמי','challenged'),
('o12',['6a:4'],'מוצע שהנכנס והיוצא הוא הסופר, ונשאל מדוע יציאתו תפסול',['זיהוי הסופר מתקבל עם הבהרת החידוש בהמשך'],'קול סתמי','queried'),
('o13',['6a:5'],'החידוש כשהסופר יצא לשוק וחזר: אין פוסלים מחשש שאדם אחר מצאו ואמר לו',['חשש מוצע הנדחה בקמשמע לן; הכתוב אינו מפרט כאן את נוסח האמירה'],'קול סתמי','asserted'),
]
cs={}
for key,refs,prop,conds,holder,mode in rows:
    u=add('u.'+key,'utterances',refs,dict(textual_voice=holder,discourse_role='local_argument_or_report',composition='composite'))
    c=add('c.'+key,'claims',refs,dict(proposition=prop,conditions=conds,scope='שלב מקומי בלבד; AI provisional',assertion_mode=mode),[u]);cs[key]=c
    anon=holder.startswith('קול') or holder=='ברייתא אנונימית'
    at=add('a.'+key,'attributions',refs,dict(surface=holder,role='anonymous' if anon else 'position_holder',candidates=[] if anon else [holder],scope=prop,transmission_chain=[]),[u,c])
    if key not in ['o1','o5']:
        add('p.'+key,'positions',refs,dict(holder_candidates=[] if anon else [holder],claim_id=c,question_id=None,conditions=conds,local_status=mode+'; source stage retained'),[c,at])
for key,person,chain in [('hamnuna','רב המנונא',['רב המנונא','עולא','רבי מאיר']),('ulla','עולא',['עולא','רבי מאיר'])]:
    add('trans.'+key,'attributions',['5b:19'],dict(surface=person,role='transmitter',candidates=[person],scope=cs['n15'],transmission_chain=chain),[cs['n15']])
qs={}
for key,refs,form in [('reason',['5b:9'],'האם שניים ושלושה תלויים בטעמי לשמה וקיום?'),('yohanan',['5b:10'],'כיצד רבי יוחנן מצריך שניים אם טעמו קיום?'),('judge',['5b:13'],'הרי בדרבנן עד נעשה דיין?'),('repair',['5b:17'],'כיצד יתקן נתינה ללא הצהרה?'),('meir',['5b:18'],'האם חסרון ההצהרה מחייב הוצאה וממזרות לרבי מאיר?'),('sight',['6a:3'],'כיצד מכשירים כשהשליח אינו רואה את הסופר?'),('who',['6a:4'],'מי הנכנס והיוצא, ומה החידוש?')]:
    qs[key]=add('q.'+key,'questions',refs,dict(formulation=form,question_origin='explicit',conditions=['הקשר מקומי'],answer_set_status='unreviewed_alternatives'))
edges=[('n3','n1','objection',['5b:10']),('n4','n1','objection',['5b:11']),('n8','n7','objection',['5b:13']),('n9','n7','correction',['5b:13','5b:14']),('n10','n6','correction',['5b:13','5b:15']),('n13','repair','answer',['5b:17']),('n15','meir','answer',['5b:19']),('o3','o2','objection',['5b:20']),('o10','sight','answer',['6a:3']),('o10','o7','support',['6a:2','6a:3']),('o13','who','answer',['6a:4','6a:5'])]
for n,(src,tgt,rel,refs) in enumerate(edges):
    x,y=cs[src],cs[tgt] if tgt in cs else qs[tgt]
    add('e.'+str(n),'edges',refs,dict(source_id=x,target_id=y,relation=rel,explicitness='source_explicit'),[x,y])
add('e.yohanan','edges',['5b:16','5b:17'],dict(source_id=cs['n13'],target_id='L02.git.open.c.number_yohanan',relation='support',explicitness='source_explicit'),[cs['n13'],'L02.git.open.c.number_yohanan'])
add('e.cont','edges',['5b:8','5b:9'],dict(source_id='L02.git.open.s.number_resolution',target_id=s1,relation='continuation',explicitness='editorial_reconstruction'),['L02.git.open.s.number_resolution',s1],origin='editorial_inference')
coverage=[]
for f in core:
    sid=a.byref[f]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in a.records if (x['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Original 5b:7–6b:10 read, bounded core 5b:9–6a:5 reread for omissions: two rejected explanations, anonymous material, transmission chain, correction procedure, reported encounters and market-exit concern preserved. No explicit object in this layer where zero; no independent review implied.'))
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
state=r.current(JOB)
p.update(owner='/root/L02_gittin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.records,coverage=coverage,open_tails=state['open_tails']+[s1])
out=JOB/'authored/L02_resume_005_v2.json';r.immutable(out,r.encoded(p));print(out)
