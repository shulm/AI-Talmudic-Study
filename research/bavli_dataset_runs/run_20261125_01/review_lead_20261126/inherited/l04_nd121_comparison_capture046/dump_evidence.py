import sys
sys.dont_write_bytecode=True
from validate_comparison import *
ss=module(B/'bavli_production_v1/runner.py','r').load(P/'job')[1];s=read(P/'job/snapshots'/f'{H}.json');exp=read(R/'exposure.json');rd=read(R/'reading.json')
lines=[]
for ref in exp['fully_reviewed_core_refs']+exp['fully_reviewed_context_refs']:
 sid=next(k for k,v in ss.items() if v['ref']==ref);lines+=['\n## '+ref,ss[sid]['text']]
 for label,rows,key in [('READER',rd['records'],ref),('PRODUCER',s['records'],sid)]:
  lines.append(label)
  for r in rows:
   if r.get('release_state','valid')=='valid' and any(e['segment_id']==key for e in r['evidence']):
    lines.append(json.dumps({'id':r['id'],'layer':r['layer'],'content':r['content'],'evidence':r['evidence'],'uncertainty':r['uncertainty']},ensure_ascii=False))
p=O/'comparison_evidence.txt';assert not p.exists();p.write_text('\n'.join(lines),encoding='utf-8')
# compact separate claims view
for ref in exp['fully_reviewed_core_refs']+exp['fully_reviewed_context_refs']:
 sid=next(k for k,v in ss.items() if v['ref']==ref);print('\n##',ref,ss[sid]['text'])
 for label,rows,key in [('R',rd['records'],ref),('P',s['records'],sid)]:
  for r in rows:
   if r.get('release_state','valid')=='valid' and r['layer'] in ['claims','questions','edges'] and any(e['segment_id']==key for e in r['evidence']):print(label,r['id'],json.dumps(r['content'],ensure_ascii=False))
