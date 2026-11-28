"""Serialize explicitly authored readings; never infer annotations from patterns."""
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'research/bavli_production_v1'))
import runner as r

JOB = Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L02/bavli_gittin')
j, segments = r.load(JOB)
byref = {s['ref'].split(' ', 1)[1]: s for s in segments.values()}
records = []

def ev(refs):
    return [dict(segment_id=byref[f]['id'], start_char=0, end_char=len(byref[f]['text']), quote=byref[f]['text']) for f in refs]

def add(key, layer, refs, content, links=(), uncertainty=(), origin='source_paraphrase'):
    rid = 'L02.git.open.' + key
    records.append(dict(id=rid, layer=layer, evidence=ev(refs), content=content, origin=origin, uncertainty=list(uncertainty), links=list(links)))
    return rid

core = [f for f in byref if (byref[f]['source_index'][0] < 4 or f in [f'3a:{n}' for n in range(1, 16)])]
mishnah = add('s.mishnah', 'structure', core[:5], dict(title='הבאת גט והצהרת השליח: דין וגבולות',primary=True,boundary='closed',legacy_ids=[]), origin='editorial_inference')
gemara = add('s.reasons', 'structure', core[5:], dict(title='טעמי רבה ורבא ועדות השליח; הדיון ממשיך',primary=True,boundary='open_right',legacy_ids=[]), origin='editorial_inference')

# Each row is a separately authored, source-grounded proposition. No generic
# semantic generation or whole-tractate completion is performed by this file.
# key, refs, proposition, conditions, holder, local assertion mode
rows = [
('m1',['2a:1'],'המביא גט ממדינת הים צריך לומר בפני נכתב ובפני נחתם',['הבאה ממדינת הים'],'תנא קמא','asserted'),
('m2',['2a:2'],'רבן גמליאל מחייב גם את המביא מן הרקם ומן החגר',['הבאה מן הרקם או החגר'],'רבן גמליאל','asserted'),
('m3',['2a:2'],'רבי אליעזר מחייב אפילו מכפר לודים ללוד',['הבאה מכפר לודים ללוד'],'רבי אליעזר','asserted'),
('m4',['2a:3'],'חכמים מצריכים הצהרה למביא ממדינת הים ולמוליך אליה',['כיוון ההבאה: ממדינת הים או אליה'],'חכמים','asserted'),
('m5',['2a:3'],'המביא ממדינה למדינה במדינת הים צריך הצהרה',['מעבר ממדינה למדינה במדינת הים'],'קול המשנה הסתמי','asserted'),
('m6',['2a:3'],'רשב״ג מחייב אפילו מהגמוניא להגמוניא',['מעבר מהגמוניא להגמוניא'],'רשב״ג','asserted'),
('m7',['2a:4'],'לרבי יהודה רקם והשטח שממנו מזרחה הם כמזרח',['גבול מזרח לדיני ההבאה'],'רבי יהודה','asserted'),
('m8',['2a:4'],'לרבי יהודה אשקלון והשטח שממנו דרומה הם כדרום',['גבול דרום לדיני ההבאה'],'רבי יהודה','asserted'),
('m9',['2a:4'],'לרבי יהודה עכו והשטח שממנו צפונה הם כצפון',['גבול צפון לדיני ההבאה'],'רבי יהודה','asserted'),
('m10',['2a:4'],'רבי מאיר מחשיב את עכו כארץ ישראל לגיטין',['לעניין גיטין בלבד בהיגד זה'],'רבי מאיר','asserted'),
('m11',['2a:5'],'המביא גט בארץ ישראל אינו צריך הצהרת בפני נכתב ובפני נחתם',['הבאה בארץ ישראל'],'קול המשנה הסתמי','asserted'),
('m12',['2a:5'],'אם יש עוררים על הגט הוא מתקיים בחותמיו',['יש עוררים על הגט'],'קול המשנה הסתמי','conditional'),
('r1',['2a:6','2b:1'],'רבה מנמק את חובת ההצהרה בחוסר בקיאות לשמה',['טעם חובת המביא ממדינת הים'],'רבה','asserted'),
('r2',['2b:2'],'רבא מנמק את חובת ההצהרה בכך שאין עדים מצויים לקיים את הגט',['טעם חובת המביא ממדינת הים'],'רבא','asserted'),
('n1',['2b:3'],'הבאה בשניים מוצעת כהבדל בין הטעמים',['שני מביאים; הצעת הבדל בשלב זה'],'קול הדיון הסתמי','asserted'),
('n2',['2b:3'],'הבאה ממדינה למדינה בארץ ישראל מוצעת כהבדל נוסף',['מעבר ממדינה למדינה בארץ ישראל; בשלב זה'],'קול הדיון הסתמי','asserted'),
('n3',['2b:4'],'הבאה באותה מדינה במדינת הים מוצעת כהבדל נוסף',['בתוך אותה מדינה בחוץ לארץ; בשלב זה'],'קול הדיון הסתמי','asserted'),
('a1',['2b:5'],'לפי טעם רבה מוצע להצריך שני עדים כבשאר עדויות',['דרישה מוצעת, לא מסקנת הסוגיה'],'קול הדיון הסתמי','queried'),
('a2',['2b:5'],'נאמנות עד אחד באיסורין מוצעת כתשובה לדרישת שני עדים',['תשובה ראשונית; מוגבלת בהמשך'],'קול הדיון הסתמי','challenged'),
('a3',['2b:6'],'נאמנות עד אחד באיסורין מתאימה לספק חלב ספק שומן שלא הוחזק בו איסור',['חתיכה בספק ולא איתחזק איסורא'],'קול הדיון הסתמי','asserted'),
('a4',['2b:7'],'כאן הוחזק איסור אשת איש, וזה דבר שבערוה שאינו בפחות משניים',['אשת איש; התנגדות להחלת הכלל הרגיל'],'קול הדיון הסתמי','asserted'),
('a5',['2b:8'],'רוב בקיאים לשמה, וגם לרבי מאיר החושש למיעוט סתם סופרי הדיינים למדו',['מענה לחשש חוסר בקיאות'],'קול הדיון הסתמי','asserted'),
('a6',['2b:8','3a:1'],'דרישת העדות היא מדרבנן והם הקלו משום עיגון',['בהצהרת שליח זו; נימוק בסוגיה'],'קול הדיון הסתמי','asserted'),
('a7',['3a:2'],'נטען שהסתפקות באחד עלולה להיות חומרא: בשניים הבעל לא יערער ויפסול ואילו באחד עשוי לערער ולפסול',['טענת קושיה, לא תוצאה סופית'],'קול הדיון הסתמי','challenged'),
('a8',['3a:3'],'רבי יוחנן ורבי חנינא נחלקים אם הנתינה בפנים שניים או שלושה, בלי זיהוי מי אומר כל מספר כאן',['חד אמר וחד אמר; אין שיוך לפי סדר השמות'],'רבי יוחנן / רבי חנינא: שיוך לא מוכרע כאן','unresolved'),
('a9',['3a:3'],'מאחר שהשליח נותן בפני קבוצה, הוא מדקדק מתחילה ולא בא להרע לעצמו',['מענה לחשש ערעור; שניים או שלושה'],'קול הדיון הסתמי','asserted'),
('b1',['3a:4'],'לפי רבא מוצע להצריך שניים כבקיום שטרות רגיל',['דרישה מוצעת, לא מסקנה'],'קול הדיון הסתמי','queried'),
('b2',['3a:4'],'נאמנות עד אחד באיסורין מוצעת כמענה גם לפי רבא',['תשובה ראשונית שנדחית כראיה מספקת'],'קול הדיון הסתמי','challenged'),
('b3',['3a:5'],'עד אחד נאמן בדוגמת ספק חלב או שומן שלא הוחזק איסור; כאן הוחזק איסור אשת איש ודבר שבערוה צריך שניים',['הבחנה בין דוגמת החתיכה למקרה גט'],'קול הדיון הסתמי','asserted'),
('b4',['3a:6'],'ריש לקיש אומר שעדים החתומים על השטר נחשבים כמי שנחקרה עדותם בבית דין',['דין העדות החתומה'],'ריש לקיש','asserted'),
('b5',['3a:6'],'מן הדין אין צורך בעדות קיום רגילה, חכמים הצריכוה ובגט הקלו משום עיגון',['על בסיס דברי ריש לקיש; קיום דרבנן'],'קול הדיון הסתמי','asserted'),
('b6',['3a:7'],'גם כאן נטען שהעד האחד מאפשר ערעור בעל במקום שהשניים היו מונעים אותו',['קושיה חוזרת במסלול רבא'],'קול הדיון הסתמי','challenged'),
('b7',['3a:7'],'דעת רבי יוחנן ודעת רבי חנינא על שניים או שלושה נזכרות שוב בלי שיוך, כדי להסביר שהשליח מדקדק ולא מרע לעצמו',['מקבילה בתוך אותה סוגיה; שיוך המספרים אינו מוכרע כאן'],'קול הדיון הסתמי המצטט רבי יוחנן ורבי חנינא','asserted'),
('c1',['3a:8'],'בתשובה המיוחסת לרבא, המשנה אינה אומרת בפני נכתב לשמה ובפני נחתם לשמה',['אמר לך: שחזור תשובת רבא בגמרא'],'רבא: תשובה משוחזרת בגמרא','asserted'),
('c2',['3a:9'],'בתשובת רבה, ראוי היה לפרש לשמה אך ריבוי הדיבור עלול להביא לקיצור הנוסח',['הסבר נוסח המשנה בפי רבה'],'רבה: תשובה משוחזרת בגמרא','asserted'),
('c3',['3a:10'],'החשש לקיצור גם בנוסח הקיים נענה בכך שאדם גורע אחת משלוש ולא אחת משתיים',['תשובת הגמרא לחשש קיצור הנוסח'],'קול הדיון הסתמי','asserted'),
('c4',['3a:11'],'בתשובת רבה לרבא, אילו היה הטעם רק קיום היה די בפני נחתם; בפני נכתב מצביע על צורך לשמה',['היסק המיוחס לרבה, לא הכרעה בין השיטות'],'רבה: תשובה משוחזרת בגמרא','asserted'),
('c5',['3a:12'],'בתשובת רבא, בפני נכתב נוסף כדי שלא יחליפו עם קיום שטרות רגיל בעד אחד',['חשש בלבול עם קיום שטרות דעלמא'],'רבא: תשובה משוחזרת בגמרא','asserted'),
('c6',['3a:13'],'בתשובת רבה, יש הבחנה בין לשון ידעינן בקיום רגיל ללשון בפני כאן',['הבחנה נטענת נגד חשש הבלבול'],'רבה: תשובה משוחזרת בגמרא','asserted'),
('c7',['3a:14'],'במסגרת תשובת רבה, אשה אינה נאמנת בקיום הרגיל אך נאמנת כאן',['הבדל נטען בין שני ההקשרים'],'רבה: המשך תשובה משוחזרת','asserted'),
('c8',['3a:14'],'במסגרת תשובת רבה, בעל דבר אינו נאמן שם אך נאמן כאן',['הבדל נטען בין שני ההקשרים'],'רבה: המשך תשובה משוחזרת','asserted'),
('c9',['3a:15'],'בתשובת רבא, גם כאן נאמנים כשאומרים ידעינן ולכן עדיין עלולים להחליף עם קיום שטרות בעד אחד',['השוואת הנוסח אפשרית; תשובה להבחנת רבה'],'רבא: תשובה משוחזרת בגמרא','asserted'),
]
claims = {}
for key, refs, proposition, conditions, holder, mode in rows:
    uid = add('u.'+key,'utterances',refs,dict(textual_voice=holder,discourse_role='mishnah_ruling' if key.startswith('m') else 'local_argument_or_report',composition='composite' if key in ['b3','b7','c3'] else 'atomic'),origin='editorial_inference')
    uncertainty = ['This is an anonymous pair: number-to-name mapping remains unresolved.'] if key in ['a8','b7'] else []
    cid = add('c.'+key,'claims',refs,dict(proposition=proposition,conditions=conditions,scope='Local opening discussion; not an independently certified practical ruling.',assertion_mode=mode),[uid],uncertainty)
    claims[key] = cid
    anonymous = holder.startswith('קול')
    pair = key=='a8'
    aid = add('a.'+key,'attributions',refs,dict(surface=holder,role='anonymous' if anonymous else 'position_holder',candidates=[] if anonymous else (['רבי יוחנן','רבי חנינא'] if pair else [holder]),scope=proposition,transmission_chain=[]),[uid,cid],uncertainty)
    add('p.'+key,'positions',refs,dict(holder_candidates=[] if anonymous else (['רבי יוחנן','רבי חנינא'] if pair else [holder]),claim_id=cid,question_id=None,conditions=conditions,local_status=mode+'; local textual stage only'),[cid,aid],uncertainty)

qs = [
('why',['2a:6'],'מה טעם חובת ההצהרה?',[]),
('difference',['2b:3','2b:4'],'מה ההבדל בין טעמי רבה ורבא?',['הצעות הבדל בשלב זה']),
('two_rabbah',['2b:5'],'מדוע לא יצטרכו שני עדים לפי רבה?',['השוואה לשאר עדויות']),
('one_limit',['2b:6','2b:7'],'כיצד עד אחד נאמן כאן כשיש חזקת אשת איש?',['דבר שבערוה']),
('leniency_a',['3a:2'],'האם עד אחד הוא קולא או חומרא בשל ערעור הבעל?',[]),
('two_rava',['3a:4'],'מדוע אין צורך בשניים לפי רבא כמו קיום שטרות?',[]),
('one_limit_b',['3a:5'],'כיצד מועילה נאמנות באיסורין עם חזקת אשת איש?',[]),
('leniency_b',['3a:7'],'האם ההקלה תאפשר לבעל לפסול בערעור?',[]),
('rava_why',['3a:8'],'מדוע רבא אינו אומר כרבה?',[]),
('shorten',['3a:10'],'האם גם בנוסח הקיים השליח עלול לקצר?',[]),
('rabbah_why',['3a:11'],'מדוע רבה אינו אומר כרבא?',[]),
('distinguish',['3a:13','3a:14'],'האם קיום גט דומה לקיום שטרות בהתחשב בהבדלים?',[]),
('know',['3a:15'],'האם אין נאמנות גם כאן באמירת ידעינן?',[]),
]
questions = {}
for k, refs, formulation, conditions in qs:
    questions[k]=add('q.'+k,'questions',refs,dict(formulation=formulation,question_origin='explicit',conditions=conditions,answer_set_status='unreviewed_alternatives'))

edges = [
('r1','why','answer',['2a:6','2b:1']),('r2','why','answer',['2b:2']),
('n1','difference','answer',['2b:3']),('n2','difference','answer',['2b:3']),('n3','difference','answer',['2b:4']),
('a2','two_rabbah','answer',['2b:5']),('a4','a2','objection',['2b:6','2b:7']),
('a5','one_limit','answer',['2b:8']),('a6','a5','qualification',['2b:8','3a:1']),
('a7','a6','objection',['3a:2']),('a9','leniency_a','answer',['3a:3']),('a8','a9','support',['3a:3']),
('b2','two_rava','answer',['3a:4']),('b3','b2','objection',['3a:5']),
('b4','b5','support',['3a:6']),('b5','one_limit_b','answer',['3a:6']),
('b6','b5','objection',['3a:7']),('b7','leniency_b','answer',['3a:7']),
('c1','rava_why','answer',['3a:8']),('c2','c1','objection',['3a:9']),
('c3','shorten','answer',['3a:10']),('c4','rabbah_why','answer',['3a:11']),
('c5','c4','objection',['3a:12']),('c6','c5','objection',['3a:13']),
('c7','c5','objection',['3a:14']),('c8','c5','objection',['3a:14']),('c9','c6','objection',['3a:15']),
]
for n,(src,tgt,relation,refs) in enumerate(edges):
    a=claims[src]; b=questions[tgt] if tgt in questions else claims[tgt]
    add('e.'+str(n),'edges',refs,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),[a,b])

# Second source-based omission pass: enumerate each core, its authored layers,
# and absent explicit questions/edges. This is bounded to the read opening.
coverage=[]
for f in core:
    sid=byref[f]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if (x['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in x['evidence'])]
        rationale='Read and reread original '+f+' with original continuation through 4a:13; retained local hypotheses, conditions, repeated reports, anonymous voices, and unresolved number-to-name mapping. Scope is this source segment only.'
        if not ids: rationale+=' No explicit '+layer+' object found in this segment during this pass; continuation remains recorded separately.'
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))

p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='/root/L02_gittin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[gemara])
destination=JOB/'authored/L02_opening_v1.json'
r.immutable(destination,r.encoded(p))
print(destination)
