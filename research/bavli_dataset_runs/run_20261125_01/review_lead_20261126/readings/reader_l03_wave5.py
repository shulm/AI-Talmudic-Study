import json, hashlib, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def setup(name):
 j=json.loads((ROOT/'jobs'/('bavli_'+name.lower()+'.json')).read_text(encoding='utf-8'))
 for x in j['common_documents']+[j['source'],j['original_source_schema'],j['frozen_plan']]:
  assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256']
 p=json.loads(Path(j['frozen_plan']['path']).read_text(encoding='utf-8'));s=json.loads(Path(j['source']['path']).read_text(encoding='utf-8'))
 q=dict(p);q.pop('plan_sha256'); assert hashlib.sha256(b'bavli-source-only-review-plan-v1\0'+json.dumps(q,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()==p['plan_sha256']
 texts={f'{name} {i//2+1}{"a" if i%2==0 else "b"}:{k}':t for i,a in enumerate(s['text']) for k,t in enumerate(a,1)}
 for b in p['review_blocks'][:3]:
  for a in b['spans']:
   t=texts[a['ref']];assert hashlib.sha256(t.encode()).hexdigest()==a['span_sha256_utf8'];assert a['offsets_codepoints']==[0,len(t)]
 return j,p,s,texts
def freeze(name,data,topics,context,relations,uncertainties):
 j,p,s,texts=setup(name); blocks=p['review_blocks'][:3];core=[a['ref'] for b in blocks for a in b['spans']]; records=[]
 def ev(ref):
  ref=name+' '+ref if not ref.startswith(name+' ') else ref;t=texts[ref];return {'ref':ref,'start_char':0,'end_char':len(t),'quote':t}
 for line in data.strip().splitlines():
  ref,holder,status,claims=line.split('|',3)
  for claim in claims.split(';;'):
   records.append({'id':f'{name.lower()}_b001_c{len(records)+1:03d}','evidence':[ev(ref)],'origin':'source_paraphrase','proposition':claim,'holder_or_voice':holder,'local_status':status,'conditions':'Conditions stated within proposition; no extension beyond local case.'})
 for t in topics:t['evidence']=[ev(r) for r in t.pop('refs')]
 contexts=[name+' '+r for r in context]; assert not set(contexts)&set(core)
 read={e['ref'] for r in records for e in r['evidence']};assert set(core)<=read
 artifact={'artifact_kind':'frozen_source_only_bounded_reading','tractate':name,'reader_id':'reader_l03_remaining_wave5','model_id':None,'blindness':{'producer_annotations_seen':False,'prior_readings_seen':False,'allowed_inputs':'Neutral job, pinned source/schema, frozen plan, common documents only'},'source':j['source'],'original_source_schema':j['original_source_schema'],'common_documents':j['common_documents'],'frozen_plan':j['frozen_plan'],'plan_sha256':p['plan_sha256'],'source_attribution':{k:s.get(k) for k in ['versionTitle','versionSource','license']},'selected_blocks':blocks,'core_refs':core,'context_expansion_refs':contexts,'denominators':{'union_blocks':len(blocks),'union_core_segments':len(core),'probability_blocks':sum('probability_sample' in b['roles'] for b in blocks),'probability_core_segments':sum(len(b['spans']) for b in blocks if 'probability_sample' in b['roles']),'endpoint_blocks':sum(any('check' in r for r in b['roles']) for b in blocks),'endpoint_core_segments':sum(len(b['spans']) for b in blocks if any('check' in r for r in b['roles'])),'overlap_blocks':sum('probability_sample' in b['roles'] and any('check' in r for r in b['roles']) for b in blocks),'context_segments':len(contexts)},'boundaries_questions_attribution_and_relations':topics,'atomic_claims':records,'relations':relations,'uncertainties':uncertainties,'reconciliation':'Reread all 30 selected segments against these findings; continuation and prior context distinguished. Source-only reading, not producer comparison, production layer completion, full admission, human certification, or ML qualification.','ml_eligible':False,'validation':{'all_input_hashes':True,'plan_internal_hash':True,'selected_span_hashes':True,'core_membership':True,'unique_ids':True,'exact_evidence_slices':True}}
 for r in records+topics:
  for e in r['evidence']:assert texts[e['ref']][e['start_char']:e['end_char']]==e['quote']
 out=ROOT/'readings'/(name.lower()+'_batch001.json');assert not out.exists();raw=(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n').encode();out.write_bytes(raw);h=hashlib.sha256(raw).hexdigest();out.with_suffix('.sha256').write_text(h+'  '+out.name+'\n'); print(out, h, 'claims',len(records),'contexts',len(contexts))
