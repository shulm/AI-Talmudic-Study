"""Source-read Yoma opening proposal; uses the unchanged shared production schema."""
import json,hashlib
from pathlib import Path
BASE=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma')
OUT=Path(__file__).parent
inv=json.loads((BASE/'source_inventory.json').read_bytes()); job=json.loads((BASE/'JOB.json').read_bytes())
assert json.loads((BASE/'OWNER.json').read_bytes())=={'owner':'L05/yoma','epoch':2}
R=[]
def ev(i,q=None):
 t=inv[i]['text'];q=t if q is None else q;a=t.index(q)
 return dict(segment_id=inv[i]['id'],start_char=a,end_char=a+len(q),quote=q)
def add(k,l,ii,c,links=(),q=None,origin='source_paraphrase',unc=()):
 rid='yom.s02.'+k; R.append(dict(id=rid,layer=l,evidence=[ev(i,q) for i in ii],content=c,links=list(links),origin=origin,uncertainty=list(unc)));return rid
def claim(k,i,p,q=None,holder=None,cond=(),mode='asserted',unc=()):
 rid=add(k,'claims',[i],dict(proposition=p,conditions=list(cond),scope=inv[i]['ref'],assertion_mode=mode),q=q,unc=unc)
 if holder:
  add(k+'.a','attributions',[i],dict(surface=holder,role='position_holder',candidates=[holder],scope=p,transmission_chain=[]),[rid],q=q)
  add(k+'.p','positions',[i],dict(holder_candidates=[holder],claim_id=rid,question_id=None,conditions=list(cond),local_status=mode+'; AI provisional; subsequent discussion retained separately'),[rid],q=q)
 return rid
def question(k,i,p,q=None):return add(k,'questions',[i],dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'),q=q)
def edge(k,i,a,b,rel,q=None):return add(k,'edges',[i],dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b],q=q)
add('mishnah','structure',[0,1],dict(title='משנת הפרשת כהן גדול והתקנת ממלא מקום ואשה',primary=True,boundary='closed',legacy_ids=[]))
add('parah','structure',[2,3,4,5,6],dict(title='לשכת הפרה: כלי אבן, מיקום ופירוש בירה',primary=True,boundary='closed',legacy_ids=[]))
for i in range(7):add('u'+str(i),'utterances',[i],dict(textual_voice='משנה; רבי יהודה וחולקיו' if i==1 else 'anonymous textual framing with explicit quoted speakers where present',discourse_role='mishnah' if i<2 else 'discussion including quotation, question and explanation',composition='composite'))
c0=claim('separation',0,'שבעה ימים לפני יום הכיפורים מפרישים את הכהן הגדול מביתו ללשכת פרהדרין.',q='שבעת</strong></big> ימים קודם יום הכפורים מפרישין כהן גדול מביתו ללשכת פרהדרין',holder='סתם משנה')
c1=claim('substitute',0,'מתקינים כהן אחר תחת הכהן הגדול שמא ייפסל.',q='ומתקינין לו כהן אחר תחתיו שמא יארע בו פסול',holder='סתם משנה',cond=['שמא יארע בו פסול'])
c2=claim('wife',1,'רבי יהודה מצריך התקנת אשה אחרת מחשש מות אשתו.',q="ר' יהודה אומר אף אשה אחרת מתקינין לו שמא תמות אשתו",holder="ר' יהודה",cond=['שמא תמות אשתו'])
c3=claim('house',1,'ביתו בפסוק הכפרה נדרש כאשתו.',q='שנאמר (ויקרא טז, ו) וכפר בעדו ובעד ביתו ביתו זו אשתו',holder="ר' יהודה")
c4=claim('regress',1,'המשיבים לרבי יהודה טוענים שהתקנה זו אינה מסתיימת.',q='אמרו לו אם כן אין לדבר סוף',holder='אמרו לו — משיבים בלתי מזוהים',cond=['אם כן — אם מתקינים אשה אחרת'])
edge('house_support',1,c3,c2,'support');edge('regress_objection',1,c4,c2,'objection')
c5=claim('parah_separate',2,'שבעה ימים קודם שריפת הפרה מפרישים את הכהן השורף מביתו ללשכה שעל פני הבירה צפונה מזרחה.',q='תנן התם שבעת ימים קודם שריפת הפרה היו מפרישין כהן השורף את הפרה מביתו ללשכה שעל פני הבירה צפונה מזרחה',holder='משנה מצוטטת')
c6=claim('stone_name',2,'הלשכה נקראת לשכת בית האבן.',q='ולשכת בית האבן היתה נקראת',holder='משנה מצוטטת')
q0=question('stone_q',2,'מדוע נקראת לשכת בית האבן?',q='ולמה נקרא שמה לשכת בית האבן')
c7=claim('stone_vessels',2,'השם מוסבר בכך שכל מעשי הפרה בכלי גללים, אבנים ואדמה.',q='שכל מעשיה בכלי גללים בכלי אבנים ובכלי אדמה')
edge('stone_answer',2,c7,q0,'answer')
q1=question('vessels_q',3,'מה טעם השימוש בכלים אלה?',q='מאי טעמא')
c8=claim('tevul',3,'טבול יום כשר בפרה.',q='כיון דטבול יום כשר בפרה')
c9=claim('defile',3,'היו מטמאים ומטבילים את הכהן השורף כדי להוציא מלב הצדוקים.',q='דתנן מטמאין היו הכהן השורף את הפרה ומטבילין אותו להוציא מלבן של צדוקין',holder='משנה מצוטטת')
c10=claim('sadducees',3,'הצדוקים הצריכו מעורבי השמש למעשה הפרה.',q='שהיו אומרים במעורבי השמש היתה נעשית',holder='צדוקין')
edge('tevul_support',3,c9,c8,'support');edge('anti_sadducees',3,c9,c10,'objection')
c11=claim('rabbinic_vessels',4,'חכמים תיקנו כלי גללים אבנים ואדמה שאינם מקבלים טומאה כדי שלא יזלזלו בפרה.',holder='רבנן',cond=['על רקע הכשר טבול יום'])
edge('vessels_answer',4,c11,q1,'answer');edge('vessels_reason',4,c8,c11,'support')
q2=question('location_q',5,'מדוע לשכת הפרה צפונה מזרחה?',q='מאי שנא צפונה מזרחה')
c12=claim('north',5,'כינוי הפרה חטאת מקשר אותה לצפון הנדרש בחטאת.',q='כיון דחטאת היא וחטאת טעונה צפונה')
c13=claim('east',5,'בפרה נאמר אל נכח פני אהל מועד.',q='וכתיב בה (במדבר יט, ד) אל נכח פני אהל מועד')
c14=claim('location',5,'חכמים תיקנו לשכה צפונה מזרחה כדי ליצור היכר.',q='תקינו לה רבנן לשכה צפונה מזרחה כי היכי דלהוי לה היכירא',holder='רבנן')
edge('location_answer',5,c14,q2,'answer');edge('north_support',5,c12,c14,'support');edge('east_support',5,c13,c14,'support')
q3=question('birah_q',6,'מה היא בירה?',q='מאי בירה')
c15=claim('birah_yohanan',6,'בירה היא מקום בהר הבית ששמו בירה.',q='אמר רבה בר בר חנה א"ר יוחנן מקום היה בהר הבית ובירה שמו',holder='רבי יוחנן')
add('birah_reporter','attributions',[6],dict(surface='רבה בר בר חנה',role='transmitter',candidates=['רבה בר בר חנה'],scope='מקום היה בהר הבית ובירה שמו',transmission_chain=['רבה בר בר חנה','רבי יוחנן']),[c15],q='אמר רבה בר בר חנה א"ר יוחנן')
c16=claim('birah_rl',6,'כל המקדש קרוי בירה.',q='ור"ל אמר כל המקדש כולו קרוי בירה',holder='ריש לקיש')
c17=claim('birah_proof',6,'הפסוק הבירה אשר הכינותי מובא לראיית ריש לקיש.',q='שנאמר (דברי הימים א כט, יט) הבירה אשר הכינותי')
edge('birah_y_answer',6,c15,q3,'answer');edge('birah_rl_answer',6,c16,q3,'answer');edge('birah_support',6,c17,c16,'support')
C=[]
notes={0:'Separate seven-day separation from preparation of substitute; latter is not asserted to be separation. Relevant objection read at 3b:13.',1:'Preserved Rabbi Yehudah, anonymous respondents, death contingency, proof and regress; no final halakhic adjudication.',2:'Kept quoted Mishnah, place, timing, chamber name and explanation distinct.',3:'Kept tevul-yom validity, deliberate defilement/immersion, polemical purpose and opposing Sadducee position.',4:'Kept rabbinic safeguard and non-susceptibility purpose; connected explicit answer to preceding question.',5:'Kept north/east rationales and practical identifying purpose; no Torah-level chamber-location claim.',6:'Rabbah bar bar Hana is transmitter, not competing holder; both alternative meanings and proof retained.'}
for i in range(7):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==inv[i]['id'] for e in r['evidence'])]
  C.append(dict(segment_id=inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Actual second source-based omission reading: '+notes[i] if l=='reconciliation' else 'Read full original segment and continuation. '+notes[i]+(' No explicit item in this layer found.' if not ids else ''))))
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=R,coverage=C,open_tails=[])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=OUT/'yoma_opening_001.json'
if path.exists(): assert path.read_bytes()==b
else:path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),records=len(R))))
