import sys,json,copy
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah');BASE='57051426b858b389c7e8f9df0a31dfa57c1314b24064e1ec6d14a62245672c8d';REVIEW=OUT.parent.parent/'rh_next20_016_review_20261127/comparison'
job,segs=runner.load(J);runner.authorize(J,'L03/rosh_hashanah',3);state=runner.current(J);assert runner.sha(runner.encoded(state))==BASE
old={r['id']:r for r in state['records']};S={s['ref']:s for s in segs.values()}
p={k:job[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/rosh_hashanah',epoch=3,execution={'route':'interactive_agent','agent_id':'/root/rosh_hashanah','model_id':None},records=[],coverage=[],open_tails=state['open_tails'])
a='rh.e3.b016.u8';b='rh.e3.b016.fix1.u8';r=copy.deepcopy(old[a]);r['id']=b;r['supersedes']=a
for k in ['review_state','release_state','ml_eligible']:r.pop(k,None)
r['content']['textual_voice']='Anonymous alignment framing, followed by quoted Rabbi Yehoshua'
r['content']['discourse_role']='Explicit ואזדו לטעמייהו framing: the two authorities follow their earlier creation-month positions; then Yehoshua flood date, seasonal course and changed cosmos account. This is stated discourse alignment, not an independently reconstructed calendrical proof.'
r['links']=['rh.e3.b015.el_creation','rh.e3.b015.ye_creation','rh.e3.b016.el_flood_date','rh.e3.b016.ye_flood_date']
for ref in ['Rosh Hashanah 10b:10','Rosh Hashanah 11a:2']:
 s=S[ref];r['evidence'].append(dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text']))
p['records']=[r]
for c in state['coverage']:
 if a in c['record_ids']:
  c=copy.deepcopy(c);c.pop('proposal_execution',None);c['record_ids']=[b if x==a else x for x in c['record_ids']];c['rationale']+=' Independent RH016_01 correction: explicit alignment framing now represented with earlier chronology links.';p['coverage'].append(c)
assert len(p['coverage'])==1;runner.validate_apply(state,p,segs,job);runner.immutable(OUT/'PROPOSAL.json',runner.encoded(p))
runner.immutable(OUT/'PROMOTION.json',runner.encoded(runner.submit(J,OUT/'PROPOSAL.json','L03/rosh_hashanah',3)))
replay=runner.replay(J);assert replay['completed_by_layer']=={k:282 for k in runner.LAYERS};runner.immutable(OUT/'REPLAY.json',runner.encoded(replay))
ep=J/'exports/correction_016_20261127';runner.immutable(OUT/'EXPORT.json',runner.encoded(runner.export(J,ep)))
response={'status':'TARGETED_CORRECTION_PENDING_INDEPENDENT_RECHECK','base_snapshot_sha256':BASE,'snapshot_sha256':replay['snapshot_sha256'],'proposal_sha256':runner.sha((OUT/'PROPOSAL.json').read_bytes()),'comparison_sha256':runner.sha((REVIEW/'VERDICT.json').read_bytes()),'finding_sha256':runner.sha((REVIEW/'FINDING.json').read_bytes()),'finding_id':'RH016_01','disposition':'One immutable utterance revision explicitly records alignment framing and links both earlier creation views and both flood date claims; no causal proof edge invented.','revised_id':b,'superseded_id':a,'new_rows':1,'superseded_rows':1,'coverage_cells_refreshed':1,'completed_by_layer':replay['completed_by_layer'],'independent_review_seen':True,'independent_acceptance_pending':True,'source_sha256':job['source_sha256'],'export_path':str(ep),'export_manifest_sha256':runner.sha((ep/'manifest.json').read_bytes()),'next_ref':'Rosh Hashanah12b:1','next_source_index':[23,0],'open_tails':state['open_tails'],'remaining_per_layer':743,'ml_eligible':False,'all_demanding_tasks':False,'tractate_delivered':False,'resume':'Independent exact recheck of this correction; next production under coordinator instructions at12b1, reusing prior context outcomes and extending vegetables primary immutably.','committed':False}
runner.immutable(OUT/'RESPONSE.json',runner.encoded(response));runner.immutable(OUT/'RESUME.md',('Exact snapshot '+response['snapshot_sha256']+'; proposal '+response['proposal_sha256']+'.\n\n282/1025 all eight passes unchanged,743 remain. Next12b1[23,0],ownerL03/rosh_hashanah epoch3. One utterance and onecoveragecell repaired; independent recheck pending. Production continuation follows coordinator instructions, reuses rh.e3.b016 context outcomes and extends vegetables primary. Initial proposal and reviewer finding retained.\n').encode())
m={f.name:runner.sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'snapshot':response['snapshot_sha256'],'proposal':response['proposal_sha256'],'response':m['RESPONSE.json'],'manifest':runner.sha((OUT/'MANIFEST.json').read_bytes())}))
