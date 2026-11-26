import json,copy,hashlib
from pathlib import Path
B=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_yoma');O=Path(__file__).parent
expected='33b8a981a43e6030e2fb4658122b281dbe1befeef219d5fcf9256a3eb62c24df';assert json.loads((B/'CURRENT.json').read_bytes())['snapshot_sha256']==expected
s=json.loads((B/'snapshots'/f'{expected}.json').read_bytes());job=json.loads((B/'JOB.json').read_bytes());inv=json.loads((B/'source_inventory.json').read_bytes());old={r['id']:r for r in s['records'] if r['release_state']=='valid'};changes={}
def rev(k):
 r={x:copy.deepcopy(y) for x,y in old[k].items() if x not in ['review_state','release_state','ml_eligible','supersedes']};r.update(id=k+'.review1',supersedes=k);changes[k]=r;return r
prefix='yom.s02.derivation.'
r=rev(prefix+'c35b');r['content']['assertion_mode']='asserted';r['uncertainty']=['Accepted rejection rationale, not a rejected assertion. The rejected interpretation itself is תחילה בכהן גדול as a distinct second version.']
for k,p in [('c7a','לעשות נדרש למעשי פרה במסירת רבי מניומי בשם רבי מחסיא בשם רבי יוחנן; ההמשך מייחס מסירה זו לרבו רבי ישמעאל.'),('c7b','לכפר נדרש למעשי יום הכיפורים באותה מסירה; ההמשך מייחס מסירת שתי הדרשות לרבי יוחנן בשם רבי ישמעאל.')]:
 c=rev(prefix+k);c['content']['proposition']=p;c['links']=[prefix+'c38b'];c['uncertainty']=['Initial report and subsequent reporting-role clarification both retained; not a new personal ruling inferred from transmitter.']
 at=rev(prefix+k+'.a');at['content'].update(surface='רבי יוחנן',role='transmitter',candidates=['רבי יוחנן'],scope='מסירת דרשת רבי ישמעאל, מזוהה בהמשך',transmission_chain=['רבי יוחנן','רבי ישמעאל']);at['uncertainty']=['Teacher attribution supplied by continuation at Yoma3b:11.']
 pos=rev(prefix+k+'.p');pos['content']['holder_candidates']=['רבי ישמעאל'];pos['content']['local_status']='reported teaching of Rabbi Yishmael via Rabbi Yohanan, clarified in continuation; AI provisional';pos['uncertainty']=['Preserves initial attribution wording without conflating transmitter and teaching holder.']
 for r in [c,at,pos]:r['evidence'].append(dict(segment_id=inv[38]['id'],start_char=0,end_char=len(inv[38]['text']),quote=inv[38]['text']))
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
 c.update(record_ids=ids,extraction_result='records_found' if ids else 'none_found_after_pass',rationale='Source-first review correction: accepted rejection rationale has asserted mode; initial Yohanan report reconciled structurally with teacher attribution in continuation. All original versions retained and dependent graph links revised.');coverage.append(c)
p={k:job[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/yoma',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=s['open_tails'])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();path=O/'yoma_review_correction_003.json';assert not path.exists();path.write_bytes(b);print(len(records),hashlib.sha256(b).hexdigest())
