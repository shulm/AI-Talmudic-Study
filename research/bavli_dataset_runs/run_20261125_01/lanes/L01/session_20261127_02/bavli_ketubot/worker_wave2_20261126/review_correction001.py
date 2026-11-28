from pathlib import Path
import sys,copy
sys.path.insert(0,'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
out=Path(__file__).parent;job=out.parent;j,segs=r.load(job);state=r.current(job);current=r.sha(r.encoded(state));byid={x['id']:x for x in state['records']};byref={x['ref']:x for x in segs.values()}
review=Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
bindings={'comparisons/ketubot_batch001_exact_version.json':'de33fc9e6996e4c062c737ddef3b6a788ff67b44f1cd46aa2cfa95d4ce54dd00','verdicts/ketubot_batch001_v2_verdict.json':'9fa11af293dec4e270e97c66b87220b14ba6ad6322e2748a0711ff75ae072e0a'}
for rel,h in bindings.items():assert r.sha((review/rel).read_bytes())==h
reviewed=r.read(job/'snapshots/feaf61875f433691257d835a4681cfa805156825c0725a7d47dec13a4a84eea9.json');rb={x['id']:x for x in reviewed['records']}
prefix='kt.wave2.review1.';records=[];mapping={};lineage=[]
def ev(ref,quote):
 s=byref['Ketubot '+ref];a=s['text'].index(quote);return dict(segment_id=s['id'],start_char=a,end_char=a+len(quote),quote=quote)
def clean(x):return copy.deepcopy({k:v for k,v in x.items() if k not in ['release_state','review_state','ml_eligible','supersedes']})
def split(oldc,oldp,branches):
 for old in [oldc,oldp]:assert byid[old]==rb[old] and byid[old]['release_state']=='valid'
 cids=[];pids=[]
 for index,b in enumerate(branches):
  key,text,conditions,evidence,status=b
  c=clean(byid[oldc]);c.update(id=prefix+'c.'+key,evidence=evidence,links=[]);c['content'].update(proposition=text,conditions=conditions)
  p=clean(byid[oldp]);p.update(id=prefix+'p.'+key,evidence=evidence,links=[c['id']]);p['content'].update(claim_id=c['id'],conditions=conditions,local_status=status)
  if index==0:c['supersedes']=oldc;p['supersedes']=oldp
  records.extend([c,p]);cids.append(c['id']);pids.append(p['id'])
 mapping[oldc]=cids;mapping[oldp]=pids;lineage.append(dict(old_claim=oldc,old_position=oldp,new_claims=cids,new_positions=pids,policy='First branch succeeds original under one-successor schema; companion branch is new. This manifest records complete one-to-many semantic lineage.'))
water_context=[ev('3b:9','הרי שהיה פתו אפוי וטבחו טבוח ויינו מזוג ומת אביו של חתן או אמה של כלה'),ev('4a:4','אמר רב אשי כגון מתא מחסיא דמפקא מכרך ומפקא מכפר')]
split('kt.resume26.b2.c.water','kt.resume26.b2.p.water',[
 ('water_present','Rav Hisda’s prepared-feast bereavement concession applies when water has been put on the meat, in the intermediate locality clarified by Rav Ashi.',['Bread baked, animal slaughtered, wine mixed','Groom’s father or bride’s mother died','Intermediate locality such as Mata Mehasya','Water has been put on meat; not saleable under the local distinction'],[ev('4a:3','לא שנו אלא שנתן מים על גבי בשר')]+water_context,'Water-present concession; Rav Hisda via Rafram bar Pappa; city and village differences retained separately'),
 ('water_absent','Rav Hisda says meat without water on it can be sold, in the intermediate locality clarified by Rav Ashi.',['Intermediate locality such as Mata Mehasya','Water has not been put on meat'],[ev('4a:3','אבל לא נתן מים על גבי בשר מזדבן'),ev('4a:4','אמר רב אשי כגון מתא מחסיא דמפקא מכרך ומפקא מכפר')],'Water-absent saleability branch; no water-present condition; Rav Hisda via Rafram bar Pappa')])
menstrual=[ev('4a:9','כי קאמר אפירסה אשתו נדה')]
split('kt.resume26.b3.c.notconsummated','kt.resume26.b3.p.notconsummated',[
 ('before_intercourse','Rava’s reported statement requires separate sleeping in the menstrual case before intercourse has occurred.',['Wife became menstruant','Intercourse has not yet occurred'],[ev('4a:8','ל"ש אלא שלא בעל')]+menstrual+[ev('4b:1','וכן מי שפירסה אשתו נדה ולא בעל הוא ישן בין האנשים ואשתו ישנה בין הנשים')],'Before-intercourse branch, menstruation only; reported by Rav Yosef son of Rava in Rava’s name'),
 ('after_intercourse','Rava’s reported statement permits his wife to sleep with him in the menstrual case after prior intercourse.',['Wife became menstruant','Intercourse has already occurred'],[ev('4a:8','אבל בעל אשתו ישנה עמו')]+menstrual,'After-intercourse branch, menstruation only; initial bereavement application was challenged before referent clarification')])
for oldc,oldp,ref,key in [('kt.open1.c.deadline','kt.open1.p.deadline','2a:2','deadline'),('kt.qual1.c.deadline_repeat','kt.qual1.p.deadline_repeat','2a:6','deadline_repeat')]:
 base=['Appointed time arrived','Marriage has not occurred'];e=ev(ref,'הגיע זמן ולא נישאו אוכלות משלו ואוכלות בתרומה')
 split(oldc,oldp,[(key+'_maintenance','The quoted deadline Mishnah grants maintenance from the betrothed man when the appointed time arrives without marriage.',base,[e],'Quoted maintenance entitlement; later impediment and Sunday qualifications remain separate'),(key+'_terumah','The quoted deadline Mishnah grants terumah consumption when the appointed time arrives without marriage, presupposing relevant priestly eligibility.',base+['Relevant priestly eligibility for terumah; implicit scope made explicit, not a new source quotation'],[e],'Quoted terumah entitlement; eligibility restricted and later applications remain disputed')])
split('kt.resume26.b2.c.evenings','kt.resume26.b2.p.evenings',[
 ('friday_prohibition','The quoted baraita prohibits initial intercourse on Sabbath eve in either referenced case.',['Initial intercourse','Sabbath eve','Either case referenced in the baraita'],[ev('4a:6','בין כך ובין כך לא יבעול לא בערב שבת')],'Quoted baraita stage only; reasons at4b:11/5a:5 and later anonymous permission7a:11 remain distinct; not certified as final prohibition'),
 ('saturday_prohibition','The quoted baraita prohibits initial intercourse on Saturday night in either referenced case.',['Initial intercourse','Saturday night','Either case referenced in the baraita'],[ev('4a:6','בין כך ובין כך לא יבעול לא בערב שבת ולא במוצ"ש')],'Quoted Saturday-night prohibition; accounting rationale replaced by preparation/slaughter concern at5a:4')])
# Exact endpoint decisions, rather than automatic one-to-many graph duplication.
edge_targets={
 'kt.resume26.b2.e.baraita_support':('target_id',prefix+'c.water_present'),
 'kt.resume26.b2.e.city':('target_id',prefix+'c.water_present'),
 'kt.resume26.b2.e.village':('target_id',prefix+'c.water_absent'),
 'kt.resume26.b2.e.water_restrict':('source_id',prefix+'c.water_present'),
 'kt.resume26.b3.e.menstrual_scope':('target_id',prefix+'c.before_intercourse'),
 'kt.resume26.b3.e.prior_objection':('target_id',prefix+'c.after_intercourse')}
for old,(key,target) in edge_targets.items():
 assert byid[old]==rb[old]
 e=clean(byid[old]);e.update(id=prefix+'e.'+old.rsplit('.',1)[1],supersedes=old);e['content'][key]=target;e['links']=[e['content']['source_id'],e['content']['target_id']]
 if old.endswith('prior_objection'):e['uncertainty']=['Historical objection to the initially unqualified application of the after-intercourse permission to bereavement; not an objection refuting the finally menstruation-qualified permission.']
 records.append(e);mapping[old]=[e['id']]
e=clean(byid['kt.resume26.b3.e.menstrual_scope']);e.update(id=prefix+'e.menstrual_scope_after');e['content']['target_id']=prefix+'c.after_intercourse';e['links']=[e['content']['source_id'],e['content']['target_id']];records.append(e)
# Ensure all active dependent records were consciously handled.
for x in state['records']:
 if x['release_state']=='valid' and x['id'] not in mapping:assert not set(x['links'])&set(mapping),x['id']
coverage=[];touched={(e['segment_id'],x['layer']) for x in records for e in x['evidence']}
touched|={(c['segment_id'],c['layer']) for c in state['coverage'] if set(c['record_ids'])&set(mapping)}
touched|={(sid,'reconciliation') for sid,layer in list(touched)}
for sid,layer in sorted(touched):
 old=next(c for c in state['coverage'] if c['segment_id']==sid and c['layer']==layer)
 c={k:v for k,v in old.items() if k!='proposal_execution'}
 ids=[rid for rid in old['record_ids'] if rid not in mapping]
 if layer!='reconciliation':ids+= [x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
 c.update(record_ids=list(dict.fromkeys(ids)),extraction_result='records_found' if ids else 'none_found_after_pass',rationale='Exact-version review correction KT-BRANCH/KT-ATOMIC: split mutually exclusive branch conditions and distinct entitlements/temporal prohibitions; preserve source occurrences, named transmission, prior historical objections and immutable predecessors. No added source coverage.')
 coverage.append(c)
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/ketubot_resume',epoch=3,source_sha256=j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/ketubot_resume',model_id=None),records=records,coverage=coverage,open_tails=state['open_tails'])
new=r.validate_apply(state,p,segs,j)
assert r.report(new,segs)['completed_by_layer']==r.report(state,segs)['completed_by_layer']
for key in ['water_absent','before_intercourse','after_intercourse']:
 for layer in ['c','p']:
  x=next(x for x in records if x['id']==prefix+layer+'.'+key)
  if key=='water_absent':assert 'Water has not been put on meat' in x['content']['conditions'] and not any('Water has been put' in a for a in x['content']['conditions'])
  if key=='before_intercourse':assert 'Intercourse has not yet occurred' in x['content']['conditions'] and 'Intercourse has already occurred' not in x['content']['conditions']
  if key=='after_intercourse':assert 'Intercourse has already occurred' in x['content']['conditions']
path=out/'review_correction001_proposal.json';r.immutable(path,r.encoded(p));receipt=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'review_correction001_receipt.json',r.encoded(receipt))
audit=dict(review_bindings=bindings,reviewed_snapshot='feaf61875f433691257d835a4681cfa805156825c0725a7d47dec13a4a84eea9',before_snapshot=current,after_snapshot=receipt['snapshot_sha256'],lineage=lineage,record_replacements=mapping,old_targets_unchanged_since_review=True,branch_regressions_pass=True,coverage_unchanged=True,review_status='Corrections authored; independent exact-version verification pending',notes=['No review-reader files altered.','Repeated deadline source2a:6 preserved separately.','Original composite/branch judgments preserved in original immutable proposals.','Context evidence from already completed source added without new coverage.'])
r.immutable(out/'review_correction001_lineage.json',r.encoded(audit));replay=r.replay(job);r.immutable(out/'review_correction001_replay.json',r.encoded(replay));print(receipt);print('replay_pass',replay['replay_pass'])
