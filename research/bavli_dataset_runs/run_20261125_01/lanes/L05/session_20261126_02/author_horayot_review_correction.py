"""Explicit revisions for independently frozen Horayot risk-review discrepancies."""
import json,copy,hashlib
from pathlib import Path
B=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_horayot');O=Path(__file__).parent
cur=json.loads((B/'CURRENT.json').read_bytes())['snapshot_sha256'];assert cur=='2f544def7e5a2e1941ac440ade614f8cb7c902533394087deb3e913e656d7569'
s=json.loads((B/'snapshots'/f'{cur}.json').read_bytes());job=json.loads((B/'JOB.json').read_bytes());inv=json.loads((B/'source_inventory.json').read_bytes())
old={r['id']:r for r in s['records'] if r['release_state']=='valid'};changes={}
def revise(k):
 r=copy.deepcopy(old[k]);r={x:y for x,y in r.items() if x not in ['review_state','release_state','ml_eligible','supersedes']};r['id']=k+'.review1';r['supersedes']=k;changes[k]=r;return r
r=revise('hor.s02.b2.sixsevenbar.a');r['content']['role']='transmitter';r['content']['transmission_chain']=['רבי שמעון בן אלעזר'];r['uncertainty']=['אומר משמו: reported authority antecedent is unresolved; transmitter is not an unqualified holder.']
r=revise('hor.s02.b2.sixsevenbar.p');r['content']['holder_candidates']=[];r['content']['local_status']='reported ruling; authority referred to by משמו unresolved; no holder-evaluation eligibility';r['uncertainty']=['Explicit transmitter Rabbi Shimon ben Elazar; reported holder not resolved.']
base=['הוראה לחלב, עשיית מיעוט, חזרת בית דין, הוראה ועשיית מיעוט אחר','אם תמצא לומר ששתי הוראות לאותו חלב מצטרפות למרות שתי ידיעות']
for key,conditions,links in [
('twofatsq',base,['fatoptions','twofats']),
('bloodq',base+['אם תמצא לומר שחלב שעל הקבה ועל הדקין מצטרפים בשם חלב'],['fatoptions','twofats','blood']),
('idolq',base+['אם תמצא לומר ששני סוגי חלב מצטרפים','אם תמצא לומר שחלב ודם מצטרפים מפני שקרבנם שווה'],['fatoptions','twofats','blood','idolatry']),
('courtsq',['הוראה ראשונה לחלב ועשיית מיעוט','מות בית הדין הראשון והוראה חדשה של בית דין אחר ועשיית מיעוט נוסף','דווקא למאן דאמר ציבור מביאים; למאן דאמר בית דין מביאים הראשון איננו'],['newcourt','courtbrings','publicexists','knowledge'])]:
 r=revise('hor.s02.b2.q.'+key);r['content']['conditions']=conditions;r['links']=['hor.s02.b2.'+k for k in links];r['uncertainty']=['Conditional inquiry; preceding if-you-say premises are not independent settled rulings.'];r['content']['answer_set_status']='unreviewed_alternatives'
 if key=='courtsq':
  for i in [58,59]:r['evidence'].append(dict(segment_id=inv[i]['id'],start_char=0,end_char=len(inv[i]['text']),quote=inv[i]['text']))
# Granularity repair retains the accurate compound source report but replaces its generic holder rows.
r=revise('hor.s02.b2.bara.a');r['content'].update(surface='רבי מאיר וחכמים',role='collective',candidates=['רבי מאיר','חכמים']);r['uncertainty']=['Distinct opposing holders of compound quotation; no joint position implied.']
r=revise('hor.s02.b2.bara.p');r['content']['holder_candidates']=['רבי מאיר','חכמים'];r['content']['local_status']='compound reported alternatives; use separate atomic records for named retrieval';r['uncertainty']=['Not a shared ruling; identity of actors in הורו ועשו has several subsequent readings.']
extra=[]
for tag,name,prop in [('meir','רבי מאיר','רבי מאיר פוטר בברייתת הורו ועשו.'),('sages','חכמים','חכמים מחייבים בברייתת הורו ועשו.')]:
 c=copy.deepcopy(old['hor.s02.b2.bara']);c={k:v for k,v in c.items() if k not in ['review_state','release_state','ml_eligible','supersedes']};c['id']='hor.s02.b2.bara.atomic.'+tag;c['content']['proposition']=prop;c['links']=['hor.s02.b2.bara'];c['uncertainty']=['Actor identity unresolved across alternative subsequent readings; no unconditional personal-case ruling.'];extra.append(c)
 p=copy.deepcopy(changes['hor.s02.b2.bara.p']);p.pop('supersedes');p['id']=c['id']+'.p';p['content']['holder_candidates']=[name];p['content']['claim_id']=c['id'];p['content']['local_status']='asserted reported alternative; actor-interpretation qualification retained';p['links']=[c['id']];extra.append(p)
 at=copy.deepcopy(changes['hor.s02.b2.bara.a']);at.pop('supersedes');at['id']=c['id']+'.a';at['content'].update(surface=name,role='position_holder',candidates=[name],scope=prop);at['links']=[c['id']];at['uncertainty']=list(c['uncertainty']);extra.append(at)
def deps(r):return set(r['links'])|{r['content'].get(k) for k in ['claim_id','question_id','source_id','target_id'] if r['content'].get(k)}
while True:
 more=[k for k,r in old.items() if k not in changes and deps(r)&changes.keys()]
 if not more:break
 for k in more:revise(k)
for r in changes.values():
 r['links']=[changes[x]['id'] if x in changes else x for x in r['links']]
 for k in ['claim_id','question_id','source_id','target_id']:
  x=r['content'].get(k)
  if x in changes:r['content'][k]=changes[x]['id']
records=list(changes.values())+extra
active=[r for k,r in old.items() if k not in changes]+records
scopes={e['segment_id'] for r in records for e in r['evidence']};coverage=[]
for c0 in s['coverage']:
 if c0['segment_id'] not in scopes:continue
 c={k:v for k,v in c0.items() if k!='proposal_execution'}
 ids=[r['id'] for r in active if (c['layer']=='reconciliation' or r['layer']==c['layer']) and any(e['segment_id']==c['segment_id'] for e in r['evidence'])]
 c.update(record_ids=ids,extraction_result='records_found' if ids else 'none_found_after_pass',rationale='Explicit source-based revision after frozen targeted review HR-D01/HR-D02/HR-U01: reporting roles, conditional question scope and atomic alternatives repaired; original records preserved. Other layers reread in this affected source scope.');coverage.append(c)
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/horayot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=s['open_tails'])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=O/'horayot_review_correction_005.json';assert not path.exists();path.write_bytes(b)
print(json.dumps(dict(path=str(path),sha256=hashlib.sha256(b).hexdigest(),revisions=len(changes),added=len(extra))))
