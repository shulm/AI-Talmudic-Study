import pathlib,json,hashlib
r=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/review_20261126_resume/source_only')
h=lambda x:hashlib.sha256(x).hexdigest()
results=[]
for f in sorted(r.glob('*_batch0*.json')):
 d=json.loads(f.read_text(encoding='utf-8')); src=pathlib.Path(d['source_path']); assert h(src.read_bytes())==d['source_sha256']; s=json.loads(src.read_text(encoding='utf-8'))['text']; count=0
 def walk(o):
  global count
  if isinstance(o,dict):
   if 'quote' in o:
    assert s[o['page_index']][o['segment_index']][o['start_char']:o['end_char']]==o['quote']; assert h(o['quote'].encode())==o['quote_sha256']; count+=1
   for v in o.values(): walk(v)
  elif isinstance(o,list):
   for v in o:walk(v)
 walk(d)
 assert f.with_suffix('.sha256').read_text().split()[0]==h(f.read_bytes())
 for block in d['selected_blocks']:
  for span in block['spans']:
   t=s[span['page_index']][span['segment_index']]; a,b=span['offsets_codepoints']; assert h(t[a:b].encode())==span['span_sha256_utf8']
 results.append(dict(file=f.name,sha256=h(f.read_bytes()),exact_evidence_occurrences_checked=count,scope=d['scope'],denominators=d['measurement_denominators']))
record=dict(status='PASS_EXACT_SOURCE_AND_QUOTE_CHECKS_ONLY',artifacts=results,limits='No production comparison or semantic acceptance; full-segment evidence can contain multiple clauses. No blanket eligibility. Scripts are frozen construction provenance, not production runners.',next_work={'bavli_taanit':'Frozen block_000015, then adjacent000016/000017, with full source continuation.','bavli_bava_batra':'Dedicated core review000002/000003; context previously read is not promoted automatically.'})
b=(json.dumps(record,ensure_ascii=False,indent=2)+'\n').encode(); (r/'validation_receipt_01.json').open('xb').write(b); (r/'validation_receipt_01.sha256').open('x').write(h(b)+'  validation_receipt_01.json\n'); print(h(b)); print([(x['file'],x['exact_evidence_occurrences_checked']) for x in results])
