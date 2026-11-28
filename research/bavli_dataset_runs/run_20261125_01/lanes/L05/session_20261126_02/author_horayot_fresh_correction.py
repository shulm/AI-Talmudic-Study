import json,copy,hashlib
from pathlib import Path
B=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_horayot');O=Path(__file__).parent
expected='0f78c631df94608fcb666f2b2bc946096d800728349d594a848d91fd38cb2726';assert json.loads((B/'CURRENT.json').read_bytes())['snapshot_sha256']==expected
s=json.loads((B/'snapshots'/f'{expected}.json').read_bytes());job=json.loads((B/'JOB.json').read_bytes());inv=json.loads((B/'source_inventory.json').read_bytes());old={r['id']:r for r in s['records'] if r['release_state']=='valid'};changes={}
def rev(k):
 r={x:copy.deepcopy(y) for x,y in old[k].items() if x not in ['review_state','release_state','ml_eligible','supersedes']};r.update(id=k+'.review2',supersedes=k);changes[k]=r;return r
spec=[
('b3.q.reason',['בית דין ידעו בטעות וחזרו בהם','היחיד עשה על פיהם לאחר החזרה','בין שהביאו כפרתם ובין שלא הביאו'],['b3.simon','b3.rav1','b3.rav2'],[69,75]),
('b3.q.difference',['עשייה בעקבות הוראה אחרי שבית הדין חזרו','השוואת יושב בביתו להולך למדינת הים','בהמשך רבא ממקד בהחזיק בדרך אך עדיין בביתו'],['b3.elazar','b3.hearing','b3.journey'],[69,70,86]),
('b3.q.noticeq',['לשיטת רבי שמעון הפוטרת לאחר חזרת בית דין','לפי המסורה שגובים מהציבור לפר העלם ולשעירי עבודה זרה','הקושיה מניחה שהגבייה הודיעה על החזרה; הנחה שנענית בשלוש חלופות'],['b3.simon','b3.collect','b3.notice','b3.plain','b3.absent','b3.reverse'],[69,75,76]),
('b4.q.plow',['בית דין הורו בטעות שאין איסור חרישה בשבת','מקיימים את שאר ענייני שבת','עוקרים חרישה כולה: נבחנת מקצת שבת מול גוף מלאכת חרישה'],['b4.plowoptions','b4.guardanswer','b4.carryanswer','b4.bowanswer'],[103]),
('b4.q.seventh',['בית דין הורו בטעות שאין שבת בשנת השמיטה','הוראתם מקיימת שבת בשאר שנות המחזור','הטעות נקשרת לדרשת בחריש ובקציר תשבות'],['b4.seventherror','b4.seventhoptions','b4.seventhresult'],[110,111]),
('b4.q.settle',['בית דין הורו בטעות שחלב מותר','היחיד החליף חלב בשומן ואכלו','דיוק מוצע מלשון שוגגים ועשו מזידים; אינו מסקנה מוכרעת'],['b4.inference','b4.rejectinference','q11'],[119,120])]
for key,conds,links,ii in spec:
 r=rev('hor.s02.'+key);r['content']['conditions']=conds;r['links']=['hor.s02.'+k for k in links];r['evidence']=[dict(segment_id=inv[i]['id'],start_char=0,end_char=len(inv[i]['text']),quote=inv[i]['text']) for i in ii];r['uncertainty']=['Standalone question requires these context conditions; source alternatives are not silently resolved.']
def deps(r):return set(r['links'])|{r['content'].get(k) for k in ['claim_id','question_id','source_id','target_id'] if r['content'].get(k)}
while True:
 more=[k for k,r in old.items() if k not in changes and deps(r)&changes.keys()]
 if not more:break
 for k in more:rev(k)
for r in changes.values():
 r['links']=[changes[x]['id'] if x in changes else x for x in r['links']]
 for k in ['claim_id','question_id','source_id','target_id']:
  x=r['content'].get(k)
  if x in changes:r['content'][k]=changes[x]['id']
records=list(changes.values());active=[r for k,r in old.items() if k not in changes]+records;scopes={e['segment_id'] for r in records for e in r['evidence']};coverage=[]
for c0 in s['coverage']:
 if c0['segment_id'] not in scopes:continue
 c={k:v for k,v in c0.items() if k!='proposal_execution'};ids=[r['id'] for r in active if (c['layer']=='reconciliation' or r['layer']==c['layer']) and any(e['segment_id']==c['segment_id'] for e in r['evidence'])]
 c.update(record_ids=ids,extraction_result='records_found' if ids else 'none_found_after_pass',rationale='Fresh source-first risk review found recurring standalone-question context omissions. Six questions and dependent edges explicitly revised; original versions preserved. This affected scope reread, but broader question-layer task qualification remains blocked pending condition audit.');coverage.append(c)
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=s['open_tails'])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=O/'horayot_fresh_review_correction_006.json';assert not path.exists();path.write_bytes(b);print(len(records),hashlib.sha256(b).hexdigest())
