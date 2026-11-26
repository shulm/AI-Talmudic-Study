"""Manual source-first Horayot opening: preserve alternative versions as alternatives."""
import author_yoma_opening as a
import json,hashlib
from pathlib import Path
BASE=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_horayot')
a.inv=json.loads((BASE/'source_inventory.json').read_bytes());a.job=json.loads((BASE/'JOB.json').read_bytes());a.R=[]
assert json.loads((BASE/'OWNER.json').read_bytes())=={'owner':'L05/horayot','epoch':2}
def add(k,l,ii,c,links=(),q=None,origin='source_paraphrase',unc=()):
 rid='hor.s02.'+k;a.R.append(dict(id=rid,layer=l,evidence=[a.ev(i,q) for i in ii],content=c,links=list(links),origin=origin,uncertainty=list(unc)));return rid
a.add=add
claim,question,edge=a.claim,a.question,a.edge
add('mishnah','structure',[0,1],dict(title='התולה בבית דין לעומת היודע שטעו',primary=True,boundary='closed',legacy_ids=[]))
add('instruction','structure',list(range(2,9)),dict(title='מותרין אתם או מותרין אתם לעשות: שתי מסורות',primary=True,boundary='closed',legacy_ids=[]))
add('fat','structure',list(range(9,19)),dict(title='נתחלף חלב בשומן לאחר הוראה: שתי מסורות רבא ומחלוקת רב ורבי יוחנן',primary=True,boundary='closed',legacy_ids=[]))
for i in range(19):add('u'+str(i),'utterances',[i],dict(textual_voice='משנה' if i<2 else 'anonymous framing with named speakers and variant reports',discourse_role='mishnah' if i<2 else 'argument/report',composition='composite'))
c0=claim('c0',0,'יחיד שעשה בשוגג על הוראת בית דין פטור משום שתלה בהם: בין שעשו עמו, שעשה אחריהם או שלא עשו.',holder='סתם משנה',cond=['הורו בית דין לעבור על מצווה','היחיד עשה שוגג על פיהם'],unc=['At 2b:9 Shmuel limits this Mishnah to Rabbi Yehudah and reports a contrary Sages view; not an unqualified final rule.'])
c1a=claim('c1a',1,'אחד הדיינים שידע שטעו או תלמיד הראוי להוראה ועשה על פיהם חייב בכל שלושת מצבי עשיית בית הדין.',holder='סתם משנה',cond=['ידע שטעו','אחד מהם או תלמיד ראוי להוראה'],unc=['Later discussion 2b:3–6 qualifies the knowledge case by error concerning obligation to obey sages.'])
c1b=claim('c1b',1,'הכלל במשנה: התולה בעצמו חייב והתולה בבית דין פטור.',holder='סתם משנה');edge('e1',1,c1b,c1a,'support')
c2a=claim('c2a',2,'במסורה הראשונה שמואל מצריך שבית דין יאמרו מותרין אתם לחיובם.',holder='שמואל — מסורה ראשונה',cond=['בית דין אמרו מותרין אתם'])
c2b=claim('c2b',2,'במסורה הראשונה רב דימי מנהרדעא מצריך מותרין אתם לעשות, משום שבלא זה לא נגמרה הוראה.',holder='רב דימי מנהרדעא — מסורה ראשונה',cond=['בית דין אמרו מותרין אתם לעשות'])
q2=question('q2',2,'מה הטעם לדרישת לעשות?',q='מ"ט');c2c=claim('c2c',2,'בהיעדר ההוראה לעשות טרם נגמרה ההוראה.',q='לפי שלא נגמרה הוראה');edge('e2',2,c2c,q2,'answer')
c3=claim('c3',3,'אביי מביא סיוע מהמשנה: חזר לעירו ושנה ולימד כדרך שלימד פטור, הורה לעשות חייב.',holder='אביי — מסורה ראשונה');edge('e3',3,c3,c2b,'support')
c4=claim('c4',4,'רבי אבא מסייע מהיתר להינשא: אם הלכה וקלקלה חייבת בקרבן כי ההיתר היה רק להינשא.',holder='רבי אבא — מסורה ראשונה',cond=['בית דין התירו לה להינשא','הלכה וקלקלה']);edge('e4',4,c4,c2b,'support')
c5=claim('c5',5,'רבינא מסייע מלשון משנתנו הורו בית דין לעבור.',holder='רבינא — מסורה ראשונה');edge('e5',5,c5,c2b,'support')
c6a=claim('c6a',6,'במסורת איכא דאמרי שמואל מצריך מותרין אתם לעשות.',holder='שמואל — איכא דאמרי',cond=['מותרין אתם לעשות'])
c6b=claim('c6b',6,'במסורת איכא דאמרי רב דימי מנהרדעא אומר שגם מותרין אתם בלבד גומר הוראה.',holder='רב דימי מנהרדעא — איכא דאמרי',cond=['אפילו מותרין אתם'])
c6c=claim('c6c',6,'במסורת איכא דאמרי אביי מקשה על ההסתפקות במותרין אתם מן ההבדל בין לימוד להוראה לעשות.',holder='אביי — איכא דאמרי');edge('e6',6,c6c,c6b,'objection')
c7=claim('c7',7,'רבי אבא מקשה במסורת השנייה מן האשה שהותרה להינשא ולא לקלקל.',holder='רבי אבא — איכא דאמרי');edge('e7',7,c7,c6b,'objection')
c8=claim('c8',8,'רבינא מקשה במסורת השנייה מלשון הורו בית דין לעבור.',holder='רבינא — איכא דאמרי');edge('e8',8,c8,c6b,'objection')
q9=question('q9',9,'מדוע משנת היחיד מוסיפה שוגג?');c9=claim('c9',9,'במסורה הראשונה רבא דורש שוגג לכלול פטור אם בית הדין התירו חלב והוא החליפו בשומן ואכלו.',holder='רבא — מסורה ראשונה',cond=['הורו בית דין שחלב מותר','נתחלף לו חלב בשומן ואכלו'],unc=['The printed closing על פיהם על פיהם ממש is retained as a separate qualification candidate, not silently omitted.'])
c9b=claim('c9b',9,'המקור מסיים על פיהם על פיהם ממש.',q='על פיהם על פיהם ממש',mode='unresolved',unc=['Scope of this brief closing phrase alongside first-version exemption requires review; no forced harmonization.']);edge('e9',9,c9,q9,'answer')
c10=claim('c10',10,'לפי איכא דאמרי רבא פוטר דווקא שוגג על פיהם ומחייב אם נתחלף חלב בשומן.',holder='רבא — איכא דאמרי',cond=['הבחנה בין שגגה על פיהם לבין החלפת חלב בשומן']);edge('e10',10,c10,q9,'answer')
q11=question('q11',11,'רמי בר חמא שואל מה דין מי שהחליף חלב בשומן לאחר שבית דין התירו חלב.');add('a11','attributions',[11],dict(surface='רמי בר חמא',role='speaker',candidates=['רמי בר חמא'],scope='בעיית נתחלף חלב בשומן',transmission_chain=[]),[q11]);c11=claim('c11',11,'הדיון מציין שהדבר שפשוט לרבא מסופק לרמי בר חמא.',unc=['What is plain to Rava has two reported versions; no unique result assigned.'])
c12a=claim('c12a',12,'בגרסה הראשונה של תשובת רבא הוא מציע להוכיח מן המשנה פטור בנתחלף חלב בשומן.',holder='רבא — תשובה במסורה ראשונה',mode='hypothetical');c12b=claim('c12b',12,'הדיון דוחה אפשרות ההוכחה: אולי הפטור רק לשוגג על פיהם, ונתחלף חייב.',mode='hypothetical');edge('e12a',12,c12a,q11,'answer');edge('e12b',12,c12b,c12a,'objection')
c13a=claim('c13a',13,'באיכא דאמרי של תשובת רבא הוא מציע להוכיח מן המשנה חיוב בנתחלף חלב בשומן.',holder='רבא — תשובה באיכא דאמרי',mode='hypothetical');c13b=claim('c13b',13,'הדיון דוחה: אולי לשון המשנה היא או שוגג או על פיהם, ואין מכאן הוכחה לחיוב.',mode='hypothetical');edge('e13a',13,c13a,q11,'answer');edge('e13b',13,c13b,c13a,'objection')
c14a=claim('c14a',14,'רב פוטר נתחלף חלב בשומן לאחר הוראת היתר חלב.',holder='רב',cond=['הורו בית דין שחלב מותר','נתחלף לו חלב בשומן ואכלו'])
c14b=claim('c14b',14,'רבי יוחנן מחייב באותו מקרה.',holder='רבי יוחנן',cond=['הורו בית דין שחלב מותר','נתחלף לו חלב בשומן ואכלו'])
c14c=claim('c14c',14,'ברייתת מעם הארץ בעשותה מוציאה מומר.',holder='ברייתא מצוטטת')
c15=claim('c15',15,'רבי שמעון בן יוסי בשם רבי שמעון דורש: השב מידיעתו מביא קרבן על שגגתו, והלא שב מידיעתו אינו מביא.',holder='רבי שמעון',cond=['השב מידיעתו לעומת לא שב מידיעתו'])
add('a15','attributions',[15],dict(surface='רבי שמעון בן יוסי',role='transmitter',candidates=['רבי שמעון בן יוסי'],scope='דרשת השב מידיעתו',transmission_chain=['רבי שמעון בן יוסי','רבי שמעון']),[c15])
c16=claim('c16',16,'הקושיה סבורה שהאוכל בעקבות היתר בית הדין אינו שב מידיעתו.',mode='challenged');edge('e16',16,c16,c14b,'objection');edge('e16b',16,c15,c16,'support')
c17=claim('c17',17,'רב פפא מסביר שלרבי יוחנן אם ייוודע לבית דין יחזרו בהם וגם היחיד יחזור, ולכן הוא שב מידיעתו וחייב.',holder='רבי יוחנן — לפי הסבר רב פפא',cond=['אם ייוודע לבית דין ויחזרו בהם','גם היחיד יחזור'])
add('a17','attributions',[17],dict(surface='ר"פ',role='speaker',candidates=['רב פפא'],scope='הסבר סברת רבי יוחנן',transmission_chain=[]),[c17],unc=['Abbreviation expanded provisionally from local conventional reading.']);edge('e17',17,c17,c16,'answer')
c18a=claim('c18a',18,'רבא אומר שרב מודה שהמחליף אינו משלים לרוב ציבור.',holder='רב — במסירת רבא',cond=['מקרה נתחלף חלב בשומן'])
add('a18','attributions',[18],dict(surface='רבא',role='speaker',candidates=['רבא'],scope='מודה רב שאינו משלים לרוב ציבור',transmission_chain=[]),[c18a])
q18=question('q18',18,'מה הטעם שאינו משלים לרוב ציבור?',q='מ"ט');c18b=claim('c18b',18,'בשגגה נדרש עד שיהיו כולם בשגגה אחת.');edge('e18a',18,c18b,q18,'answer');edge('e18b',18,c18b,c18a,'support');edge('e18c',18,c18a,c14a,'qualification')
C=[]
for i in range(19):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in a.R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==a.inv[i]['id'] for e in r['evidence'])]
  note='Second source reading performed: no name-order assignment; two instruction versions and two Rava reports/argument versions kept separate; rejected proofs not conclusions; Rav distinct from Rava; conditional return and majority qualification retained. Context read through 2b:15, not counted in core.'
  C.append(dict(segment_id=a.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+(' No explicit additional record found in this layer.' if not ids else '')))
p={k:a.job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.R,coverage=C,open_tails=[])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=Path(__file__).parent/'horayot_opening_001.json'
if path.exists():assert path.read_bytes()==b
else:path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),records=len(a.R))))
