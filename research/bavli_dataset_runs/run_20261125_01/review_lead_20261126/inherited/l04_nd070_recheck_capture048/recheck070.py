from validate_comparison import *
import copy,re
NEW='7d9b6947557eaf3b807e913f1acde3c82ca39e9124610980288d993b33f1fa3b';BASE='5168ca1425eb9ef707abb189482125b347fb49a65fc7e7effcec2309dbf96ce4';PROP='66ee6a75c0c45686cddf5babb7e4948347a49814136019e91cd4b0c42456d60e'
LANE=B/'bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/nedarim';JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_nedarim')
def verify():
 assert sha(LANE/'FROZEN_REPAIR121_070.json')=='8df3d4da95364f7f783d584e99562b15eb654a54a5f88739d5d3f88fc5711fce'
 fr=read(LANE/'FROZEN_REPAIR121_070.json');assert sha(LANE/fr['closure_receipt'])==fr['closure_sha256'];cl=read(LANE/fr['closure_receipt'])
 for h in [BASE,NEW]:assert sha(JOB/'snapshots'/f'{h}.json')==h
 assert sha(JOB/'proposals'/f'{PROP}.json')==PROP
 for n,h in read(O/'DELIVERY.json')['files'].items():assert sha(O/n)==h
 assert sha(R/'reading.json')=='63bd309b1650a8accb9a7f0bee4e4c58e0ea0521342676a7fef9ee5c8df96714'
 run=module(B/'bavli_production_v1/runner.py','runner_recheck');j,ss=run.load(JOB);base=read(JOB/'snapshots'/f'{BASE}.json');new=read(JOB/'snapshots'/f'{NEW}.json');old=read(P/'job/snapshots'/f'{H}.json');proposal=read(JOB/'proposals'/f'{PROP}.json')
 assert new['proposals']==base['proposals']+[PROP];assert base['proposals'][:len(old['proposals'])]==old['proposals']
 state=run.empty()
 for h in new['proposals']:
  p=JOB/'proposals'/f'{h}.json';assert sha(p)==h
  previous=state['proposals'];state=run.validate_apply(state,read(p),ss,j);state['proposals']=previous+[h]
 assert run.encoded(state)==run.encoded(new)
 bi={r['id']:r for r in base['records']};ni={r['id']:r for r in new['records']};oi={r['id']:r for r in old['records']};mapping=cl['supersession_mapping'];added=set(ni)-set(bi)
 assert len(added)==34 and len(mapping)==17 and len(added-set(mapping.values()))==17
 assert len(proposal['records'])==34 and {r['id'] for r in proposal['records']}==added
 for k,r in bi.items():
  target=copy.deepcopy(r)
  if k in mapping:target['release_state']='superseded'
  assert ni[k]==target,k
 for a,b in mapping.items():assert ni[b].get('supersedes')==[a] or ni[b].get('supersedes')==a,(a,ni[b].get('supersedes'))
 active={k:r for k,r in ni.items() if r['release_state']=='valid'}
 for k,r in active.items():
  for link in r['links']:assert link in active,(k,link)
  c=r['content']
  if r['layer']=='positions':
   assert active[c['claim_id']]['layer']=='claims'
   if c['question_id'] is not None:assert active[c['question_id']]['layer']=='questions'
  if r['layer']=='edges':
   assert c['source_id'] in active and c['target_id'] in active
   if c['relation']=='continuation':assert active[c['source_id']]['layer']==active[c['target_id']]['layer']=='structure'
  if r['layer']=='attributions' and c['scope'] in ni:assert c['scope'] in active
  raw=json.dumps(c,ensure_ascii=False)
  for oldid in mapping:assert not re.search(re.escape(oldid)+r'(?![\w.])',raw),(k,oldid)
 for c in new['coverage']:
  for k in c['record_ids']:
   assert k in active and active[k]['layer']==c['layer']
   assert any(e['segment_id']==c['segment_id'] for e in active[k]['evidence'])
 bc={(c['segment_id'],c['layer']):c for c in base['coverage']};nc={(c['segment_id'],c['layer']):c for c in new['coverage']};oc={(c['segment_id'],c['layer']):c for c in old['coverage']}
 assert set(bc)==set(nc)
 window_ids=set(bi)-set(oi);window_cells=set(bc)-set(oc)
 assert len(window_ids)==233 and len(window_cells)==176
 for k in window_ids:assert bi[k]==ni[k] and ni[k]['review_state']=='unreviewed' and ni[k]['ml_eligible']==False
 for k in window_cells:assert bc[k]==nc[k]
 for x in read(O/'answer_status_uncertainty.json'):
  for r in [x['question']]+x['answer_edges']+x['answers']:assert bi[r['id']]==ni[r['id']]==r
 for k in ['nd.r024.abaye.p','nd.r024.rava.p']:assert ni[k]==bi[k]==oi[k] and ni[k]['content']['question_id'] is None
 counts={l:sum(c['layer']==l and c['extraction_state']=='completed' for c in new['coverage']) for l in run.LAYERS};assert set(counts.values())=={1105}
 assert all(not r['ml_eligible'] for r in new['records']) and new['review_state']=='unreviewed' and new['ml_eligible']==False
 result=dict(status='PASS',at=datetime.datetime.now(datetime.timezone.utc).isoformat(),snapshot=NEW,base=BASE,proposal=PROP,accepted_proposals=len(new['proposals']),new_records=34,supersessions=17,additive_nodes=17,active_graph_content_scope_coverage_closed=True,completed_by_layer=counts,new_window_records_unchanged_unreviewed=233,new_window_cells_unchanged=176,U1_nine_cases_unchanged=True,U2_null_links_unchanged=True,original_comparison_files_unchanged=True,semantic_scope='D1-D4 only; source advance not reviewed',ml_eligible=False)
 return result,[ni[k] for k in sorted(added)],ss
if __name__=='__main__':
 result,records,ss=verify();print(json.dumps(result))
 if '--receipt' in sys.argv:
  for name,obj in [('RECHECK070_MECHANICAL.json',result),('RECHECK070_RECORD_EVIDENCE.json',records)]:
   p=O/name;assert not p.exists();p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
