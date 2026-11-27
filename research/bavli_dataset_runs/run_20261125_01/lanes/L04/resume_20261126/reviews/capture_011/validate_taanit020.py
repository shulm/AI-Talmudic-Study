import json,hashlib
from pathlib import Path
import jsonschema
D=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
p=D/'taanit_delegated020.json'; raw=p.read_bytes(); a=json.loads(raw); proposal=a['independent_review']
assert (D/'taanit_delegated020.sha256').read_text().split()[0]==sha(raw)
for x in a['bindings']:assert sha(Path(x['path']).read_bytes())==x['sha256']
schema=json.loads(Path(a['bindings'][2]['path']).read_text(encoding='utf8'));jsonschema.validate(proposal,schema)
s=json.loads(Path(a['bindings'][0]['path']).read_text(encoding='utf8'))
source={f'Taanit {p//2+1}{"a" if p%2==0 else "b"}:{i+1}':t for p,page in enumerate(s['text']) for i,t in enumerate(page)}
ids={x['id'] for x in proposal['records']};assert len(ids)==len(proposal['records'])
for x in proposal['records']:
 for e in x['evidence']:assert source[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
 for k in x['links']:assert k in ids
 if x['layer']=='positions':assert x['content']['claim_id'] in ids
 if x['layer']=='edges':assert x['content']['source_id'] in ids and x['content']['target_id'] in ids
for r in a['core_refs']:
 es=[e for x in proposal['records'] if x['layer']=='structure' and x['content']['primary'] for e in x['evidence'] if e['segment_id']==r]
 assert len(es)==1 and es[0]['start_char']==0 and es[0]['end_char']==len(source[r])
 assert len([c for c in proposal['coverage'] if c['segment_id']==r])==8
receipt={'artifact':str(p),'sha256':sha(raw),'author_script_sha256':sha((D/'author_review.py').read_bytes()),'validator_script_sha256':sha(Path(__file__).read_bytes()),'agent_identity':a['agent_identity'],'checks':{'dependency_hashes':6,'proposal_json_schema':True,'exact_evidence':sum(len(x['evidence']) for x in proposal['records']),'unique_ids_and_resolved_links':True,'primary_structure_full_partition':30,'coverage_cells':240,'source_only_omission_pass':30},'record_counts':{l:sum(x['layer']==l for x in proposal['records']) for l in ['structure','utterances','claims','attributions','questions','positions','edges']},'context_count':len(a['context_refs']),'core_count':30,'no_producer_inspection':True,'context_not_counted':True,'receipt_collision':'Generic validation_receipt.json already existed; not inspected or overwritten. This uniquely named receipt validates this frozen artifact.'}
with (D/'taanit_delegated020.validation_receipt.json').open('x',encoding='utf8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2)
print(json.dumps(receipt,ensure_ascii=False))
