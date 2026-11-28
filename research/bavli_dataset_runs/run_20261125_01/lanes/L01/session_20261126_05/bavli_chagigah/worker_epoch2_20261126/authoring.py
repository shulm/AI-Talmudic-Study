"""Mechanical serialization of manually source-read annotations; no semantic inference."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[7]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_chagigah')
j,ss=runner.load(JOB); rows=list(ss.values())
class Batch:
 def __init__(self,n,lo,hi):
  self.n=n;self.lo=lo;self.hi=hi;self.records=[];self.ids={}
 def ev(self,i,q=None):
  t=rows[i]['text'];a=0 if q is None else t.index(q);q=t if q is None else q
  return dict(segment_id=rows[i]['id'],start_char=a,end_char=a+len(q),quote=q)
 def add(self,key,layer,ix,content,q=None,links=(),unc=(),origin='source_paraphrase'):
  rid='chg.e2.'+key;assert rid not in self.ids.values();self.ids[key]=rid
  ev=[self.ev(i) for i in ix] if isinstance(ix,list) else [self.ev(ix,q)]
  self.records.append(dict(id=rid,layer=layer,evidence=ev,content=content,origin=origin,uncertainty=list(unc),links=[self.ids.get(x,x) for x in links]));return rid
 def structure(self,key,lo,hi,title,boundary='closed'):
  return self.add(key,'structure',list(range(lo,hi+1)),dict(title=title,primary=True,boundary=boundary,legacy_ids=[]))
 def claim(self,key,i,q,p,holder='סתם התלמוד',conditions=(),mode='asserted',status='source assertion; not independently reviewed',chain=(),unc=()):
  c=self.add(key,'claims',i,dict(proposition=p,conditions=list(conditions),scope=rows[i]['ref'],assertion_mode=mode),q,unc=unc)
  self.add(key+'.u','utterances',i,dict(textual_voice=holder,discourse_role=mode,composition='atomic'),q,links=[key],unc=unc)
  candidates=[] if holder in ['סתם התלמוד','תנא קמא','ברייתא','מספר הברייתא'] else holder.split('|')
  self.add(key+'.a','attributions',i,dict(surface=holder,role='anonymous' if not candidates else 'position_holder',candidates=candidates,scope=p,transmission_chain=list(chain)),q,links=[key],unc=unc)
  self.add(key+'.p','positions',i,dict(holder_candidates=candidates,claim_id=c,question_id=None,conditions=list(conditions),local_status=status),q,links=[key],unc=unc)
  if chain:
   self.add(key+'.t','attributions',i,dict(surface=' ← '.join(chain),role='transmitter',candidates=list(chain[:-1]),scope=p,transmission_chain=list(chain)),q,links=[key],unc=unc)
  return c
 def question(self,key,i,q,p,conditions=()):
  return self.add(key,'questions',i,dict(formulation=p,question_origin='explicit',conditions=list(conditions),answer_set_status='partial'),q)
 def edge(self,key,i,a,b,relation,q=None):
  return self.add(key,'edges',i,dict(source_id=self.ids.get(a,a),target_id=self.ids.get(b,b),relation=relation,explicitness='source_explicit'),q,links=[a,b])
 def save(self,notes):
  cov=[]
  for i in range(self.lo,self.hi+1):
   sid=rows[i]['id']
   for layer in runner.LAYERS:
    rr=[r['id'] for r in self.records if (r['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in r['evidence'])]
    cov.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if rr else 'none_found_after_pass',record_ids=rr,rationale=notes if layer=='reconciliation' else 'Manual original-source pass: '+layer+'; '+('supported records retained' if rr else 'no distinct supported item in this segment; contextual continuations checked')))
  old=runner.current(JOB)
  tails=old['open_tails']+[r['id'] for r in self.records if r['layer']=='structure' and r['content']['boundary']!='closed']
  p=dict(schema_version=j['schema_version'],tractate=j['tractate'],owner='/root/chagigah_production',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/chagigah_production',model_id=None),records=self.records,coverage=cov,open_tails=tails)
  path=Path(__file__).parent/f'batch_{self.n:03}.json';runner.immutable(path,runner.encoded(p));return path
