import json,pathlib,hashlib,re
ROOT=pathlib.Path('research/bavli_dataset_runs/run_20261125_01/review_lead_20261126')
def sha(b): return hashlib.sha256(b).hexdigest()
def load(name):
 j=json.loads((ROOT/f'jobs/bavli_{name}.json').read_text(encoding='utf8'))
 for d in j['common_documents']+[j['source'],j['original_source_schema'],j['frozen_plan']]: assert sha(pathlib.Path(d['path']).read_bytes())==d['sha256']
 p=json.loads(pathlib.Path(j['frozen_plan']['path']).read_text(encoding='utf8')); s=json.loads(pathlib.Path(j['source']['path']).read_text(encoding='utf8'))
 pc=dict(p);pc.pop('plan_sha256');assert sha(b'bavli-source-only-review-plan-v1\0'+json.dumps(pc,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())==p['plan_sha256']
 source={f'{j["tractate"]} {i//2+1}{"a" if i%2==0 else "b"}:{n+1}':t for i,page in enumerate(s['text']) for n,t in enumerate(page)}
 for b,jb in zip(p['review_blocks'][:3],j['selected_blocks'][:3]):
  assert b['block_id']==jb['block_id'];assert [x['ref'] for x in b['spans']]==jb['core_refs']
  for x in b['spans']:
   t=s['text'][x['page_index']][x['segment_index']]; assert source[x['ref']]==t; assert sha(t.encode())==x['span_sha256_utf8']; assert x['offsets_codepoints']==[0,len(t)]
 return j,p,source

def freeze(name, rows, contexts, boundaries, notes):
 j,p,source=load(name);core=[r for b in j['selected_blocks'][:3] for r in b['core_refs']]; findings=[]
 for n,row in enumerate(rows.strip().splitlines(),1):
  refs,holder,chain,question,claim,conditions,status,relation=row.split('|'); refs=[j['tractate']+' '+x for x in refs.split(',')];ev=[]
  for ref in refs:
   raw=source[ref]; matches=list(re.finditer(r'<img[^>]*>',raw));last=0
   for m in matches:
    if last<m.start(): ev.append(dict(ref=ref,start_char=last,end_char=m.start(),quote=raw[last:m.start()]))
    last=m.end()
   if last<len(raw):ev.append(dict(ref=ref,start_char=last,end_char=len(raw),quote=raw[last:]))
  findings.append(dict(id=f'{name}.batch001.f{n:03}',evidence=ev,origin='source_paraphrase',holder_candidates=holder.split(';'),transmission_chain=[] if chain=='-' else chain.split('>'),comparable_question=question,atomic_claim=claim,operative_conditions=[] if conditions=='-' else conditions.split(';'),local_status=status,relation=relation,uncertainty=[]))
 readrefs=[j['tractate']+' '+r for r in contexts]; assert set(core)<=set(readrefs)
 counts=dict(unique_core_segments=len(core),probability_blocks=sum('probability_sample' in b['roles'] for b in j['selected_blocks'][:3]),probability_core_segments=sum(len(b['core_refs']) for b in j['selected_blocks'][:3] if 'probability_sample' in b['roles']),endpoint_blocks=sum(any('check' in r for r in b['roles']) for b in j['selected_blocks'][:3]),endpoint_core_segments=sum(len(b['core_refs']) for b in j['selected_blocks'][:3] if any('check' in r for r in b['roles'])),endpoint_overlap_blocks=sum('probability_sample' in b['roles'] and any('check' in r for r in b['roles']) for b in j['selected_blocks'][:3]),context_only_segments=len(set(readrefs)-set(core)))
 o=dict(artifact_kind='independent_source_only_bounded_reading',status='FROZEN_BOUNDED_READING_NOT_FULL_ADMISSION',tractate=j['tractate'],agent_id='/root/reader_l01_remaining_wave5',model_id=None,blind=True,producer_annotations_seen=False,source=j['source'],original_source_schema=j['original_source_schema'],frozen_plan=j['frozen_plan'],plan_sha256=p['plan_sha256'],common_documents=j['common_documents'],selected_blocks=j['selected_blocks'][:3],counts=counts,read_refs=readrefs,context_only_refs=[x for x in readrefs if x not in core],boundaries=boundaries,findings=findings,limitations=notes,ml_eligible=False,human_scholarly_certification=False,production_comparison_performed=False)
 ids=[f['id'] for f in findings];assert len(ids)==len(set(ids))
 for f in findings:
  for e in f['evidence']:assert source[e['ref']][e['start_char']:e['end_char']]==e['quote'];assert e['ref'] in readrefs
 assert set(core)<=set(e['ref'] for f in findings for e in f['evidence'])
 o['validation']={'source_schema_common_plan_hashes':'passed','canonical_plan_hash':'passed','first_three_core_membership_and_span_hashes':'passed','evidence_unicode_slices':'passed','finding_ids_unique':'passed','every_core_has_evidence':'passed','production_schema_conformance':'not claimed: review artifact, not production proposal'}
 path=ROOT/f'readings/{name}_batch001.json';data=(json.dumps(o,ensure_ascii=False,indent=2)+'\n').encode();path.parent.mkdir(exist_ok=True)
 with path.open('xb') as f:f.write(data)
 digest=sha(data)
 with pathlib.Path(str(path)+'.sha256').open('x') as f:f.write(digest+'  '+path.name+'\n')
 print(path,digest,len(findings),counts)
