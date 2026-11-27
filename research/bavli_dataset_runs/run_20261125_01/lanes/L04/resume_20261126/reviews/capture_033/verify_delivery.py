from validate_comparison import *
def check():
 s=read(P/'job/snapshots'/f'{H}.json');active=[r for r in s['records'] if r.get('release_state','valid')=='valid'];ids={r['id']:r for r in active};rd=read(R/'reading.json');ri={r['id']:r for r in rd['records']};ad=read(O/'scope_and_adapter.json');matrix=read(O/'layer_comparison.json');cm=read(O/'claim_correspondence.json');edges=read(O/'relation_inventory.json')
 assert len(matrix)==360 and len({(x['ref'],x['layer']) for x in matrix})==360
 assert sum(x['cohort']=='core' for x in matrix)==240
 assert len(ad['core_refs'])==30 and len(ad['fully_reviewed_context_refs'])==15 and len(ad['incidental_display_only_refs'])==38
 assert len(cm)==91 and {x['reader']['id'] for x in cm}=={r['id'] for r in rd['records'] if r['layer']=='claims'}
 for x in cm:
  assert x['reader']==ri[x['reader']['id']]
  for p in x['producer_records']:assert p==ids[p['id']]
 assert len(edges)==54
 for x in edges:
  assert x['reader_edge']==ri[x['reader_edge']['id']]
  for p in x['producer_endpoint_candidates']:assert p==ids[p['id']]
 # Bounded source/record omissions, not heuristic semantic similarity.
 sid=ad['adapter']['Nedarim 23a:4'];assert not any(r['layer']=='questions' and any(e['segment_id']==sid for e in r['evidence']) for r in active)
 sid=ad['adapter']['Nedarim 25a:8'];early=[e for r in active if r['layer'] in ['claims','utterances'] for e in r['evidence'] if e['segment_id']==sid and e['start_char']<102];assert not early
 assert not any(r['layer']=='questions' and any(e['segment_id']=='Nedarim 22b:11' for e in r['evidence']) for r in rd['records'])
 missing=[('nd.r024.ob.q','nd.r024.m.c'),('nd.r025.infer.c','nd.r025.common.c'),('nd.r025.mosesq.q','nd.r025.common.c'),('nd.r025.moses.c','nd.r025.mosesq.q'),('nd.r025.private.q','nd.r025.common.c'),('nd.r025.court.c','nd.r025.private.q')]
 for a,b in missing:assert not any(r['layer']=='edges' and r['content']['source_id']==a and r['content']['target_id']==b for r in active)
 u=read(O/'answer_status_uncertainty.json');assert len(u)==9
 for x in u:
  assert x['question']==ids[x['question']['id']] and x['question']['content']['answer_set_status']=='none'
  for e in x['answer_edges']:assert e==ids[e['id']] and e['content']['target_id']==x['question']['id']
 if (O/'DELIVERY.json').exists():
  for n,h in read(O/'DELIVERY.json')['files'].items():assert sha(O/n)==h,n
 return dict(status='PASS',core_layer_cells=240,context_layer_cells=120,reader_claims_preserved=91,reader_relations_preserved=54,field_uncertainties=9,semantic_certification=False)
if __name__=='__main__':
 result=check();print(json.dumps(result))
 if '--receipt' in sys.argv:
  p=O/'delivery_validation.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
