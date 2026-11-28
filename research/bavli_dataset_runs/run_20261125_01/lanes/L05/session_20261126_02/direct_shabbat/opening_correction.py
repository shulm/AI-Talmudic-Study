import json,copy
from pathlib import Path
W=Path('F:/Sefaria_QA/bavli_l05_workspace_20261126/direct_shabbat')
p=json.loads((W/'opening_2a1_3b2_v1.json').read_text(encoding='utf-8'))
old={r['id']:r for r in p['records']}; new=[]
for key in ['a28b','a31']:
 r=copy.deepcopy(old['sha_open_'+key]); r['supersedes']=r['id']; r['id']+='_v2'
 if key=='a28b':
  r['content'].update(surface='ר׳ חייא בר גמדא',candidates=['Rabbi Hiyya bar Gamda'],transmission_chain=['Rabbi Hiyya bar Gamda','Unnamed group'])
  r['uncertainty']=['Source abbreviation א״ר identifies the report; v1 expanded the title as Rav incorrectly. Identity kept as Rabbi Hiyya bar Gamda.']
 else: r['content']['candidates']=[]
 new.append(r)
# Additional direct answer links for each Mishnah case, rather than treating u2 as the entire answer.
for i in [3,4,5]:
 r=dict(id='sha_open_e1_'+str(i),layer='edges',evidence=old['sha_open_u'+str(i)]['evidence'],content=dict(source_id='sha_open_u'+str(i),target_id='sha_open_q1',relation='answer',explicitness='source_explicit'),origin='source_paraphrase',uncertainty=[],links=['sha_open_u'+str(i),'sha_open_q1'])
 new.append(r)
replacement={r['supersedes']:r['id'] for r in new if r.get('supersedes')}
coverage=[]
affected={e['segment_id'] for r in new for e in r['evidence']}
for c0 in p['coverage']:
 if c0['segment_id'] not in affected or c0['layer'] not in ['attributions','edges','reconciliation']:continue
 c=copy.deepcopy(c0); c['record_ids']=[replacement.get(x,x) for x in c['record_ids']]
 for r in new:
  if r.get('supersedes'):continue
  if c['layer'] in ['edges','reconciliation'] and any(e['segment_id']==c['segment_id'] for e in r['evidence']): c['record_ids'].append(r['id'])
 c['rationale']+=' Producer second-check correction: title expansion corrected; anonymous baraita has no named candidate; case-answer links expanded. Initial proposal preserved.'
 coverage.append(c)
p.update(records=new,coverage=coverage)
out=W/'opening_correction_v2.json'; b=(json.dumps(p,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
