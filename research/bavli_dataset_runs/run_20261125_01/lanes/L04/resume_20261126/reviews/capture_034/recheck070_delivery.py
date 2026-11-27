from recheck070 import *
def check():
 fr=read(LANE/'FROZEN_REPAIR121_070.json');cp=Path(fr['checkpoint_path']);assert sha(cp)==fr['checkpoint_sha256'];checkpoint=read(cp);export=Path(checkpoint['export_path']);assert sha(export/'manifest.json')==fr['export_manifest_sha256']
 for name,h in read(export/'manifest.json')['files'].items():assert sha(export/name)==h
 assert sha(LANE/'CONTINUATION069_FAILURE_LINEAGE.json')==fr['original069_failure_lineage_sha256']
 s=read(JOB/'snapshots'/f'{NEW}.json');b=read(JOB/'snapshots'/f'{BASE}.json');rows=read(O/'RECHECK070_RECORD_EVIDENCE.json');ids={r['id']:r for r in s['records'] if r['release_state']=='valid'};cov={(c['segment_id'],c['layer']):c for c in s['coverage']};bc={(c['segment_id'],c['layer']):c for c in b['coverage']}
 for r in rows:
  assert ids[r['id']]==r
  for sid in {e['segment_id'] for e in r['evidence']}:assert r['id'] in cov[(sid,r['layer'])]['record_ids']
 expected={
 'nd.fix121.repeated.answer':('answer','nd.r023.questions.c','nd.fix121.repeated.q'),
 'nd.fix121.invitation.objection':('objection','nd.r024.ob.q','nd.r024.m.c'),
 'nd.fix121.private.inference.objection':('objection','nd.r025.infer.c','nd.r025.common.c'),
 'nd.fix121.moses.objection':('objection','nd.r025.mosesq.q','nd.r025.common.c'),
 'nd.fix121.moses.support':('support','nd.r025.moses.c','nd.r025.mosesq.q'),
 'nd.fix121.context.private.objection':('objection','nd.r025.private.q','nd.r025.common.c'),
 'nd.fix121.context.court.support':('support','nd.r025.court.c','nd.r025.private.q')}
 for k,tup in expected.items():assert tuple(ids[k]['content'][v] for v in ['relation','source_id','target_id'])==tup
 assert ids['nd.fix121.premise.c']['content']['assertion_mode']=='hypothetical'
 assert ids['nd.r021.report.a.fix121']['content']['candidates']==['רבי אבא בר ממל']
 assert ids['nd.fix121.nesia.authority']['content']['role']=='quoted_authority'
 assert ids['nd.fix121.tarfon.transmitter']['content']['transmission_chain']==['רבי יהודה','רבי טרפון']
 assert ids['nd.r021.invitation.a.fix121']['content']['candidates']==['רב אשי']
 assert ids['nd.r021.invitation.p.fix121']['content']['holder_candidates']==[]
 assert ids['nd.r023.wouldnot.a.fix121']['content']['candidates']==['רבי ישמעאל בר רבי יוסי']
 if (O/'RECHECK070_DELIVERY.json').exists():
  for name,h in read(O/'RECHECK070_DELIVERY.json')['files'].items():assert sha(O/name)==h
 return dict(status='PASS',new_record_coverage_bidirectional=True,changed_coverage_cells=sum(cov[k]!=v for k,v in bc.items()),exact_D1_D4_nodes_and_endpoints=True,export_manifest_and_files_hashes=True,original069_failure_lineage_hash_unchanged=True,source_expansion_review=False)
if __name__=='__main__':
 result=check();print(json.dumps(result))
 if '--receipt' in sys.argv:
  p=O/'RECHECK070_SUPPLEMENTARY.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
