"""Serialization helpers only; semantic selections are explicit in author scripts."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
sys.path.insert(0,str(ROOT/'bavli_production_v1'))
import runner as r
class Author:
 def __init__(self,batch):
  self.batch=batch;self.job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_makkot');self.j,self.ss=r.load(self.job);self.refs={s['ref'].split(' ',1)[1]:s for s in self.ss.values()};self.rows=[];self.notes={}
 def ev(self,ref,quote=None):
  s=self.refs[ref];t=s['text'];quote=t if quote is None else quote;assert t.count(quote)==1,(ref,quote);a=t.index(quote);return dict(segment_id=s['id'],start_char=a,end_char=a+len(quote),quote=quote)
 def add(self,key,layer,content,ev,links=(),origin='source_paraphrase',uncertainty=()):
  rid='ma.'+self.batch+'.'+key;self.rows.append(dict(id=rid,layer=layer,content=content,evidence=ev,links=list(links),origin=origin,uncertainty=list(uncertainty)));return rid
 def unit(self,key,ref,quote,voice='anonymous discussion',role='assertion',composition='atomic',chain=()):
  ev=[self.ev(ref,quote)];u=self.add(key+'.u','utterances',dict(textual_voice=voice,discourse_role=role,composition=composition),ev)
  self.add(key+'.a','attributions',dict(surface=voice if voice!='anonymous discussion' else '',role='anonymous' if voice=='anonymous discussion' else 'speaker',candidates=[] if voice=='anonymous discussion' else [voice],scope=u,transmission_chain=list(chain)),ev,[u]);return u,ev
 def c(self,key,ref,quote,text,voice='anonymous discussion',mode='asserted',conditions=(),scope='Local argument; no later practical ruling implied',composition='atomic',chain=(),holder=None):
  u,ev=self.unit(key,ref,quote,voice,mode,composition,chain);c=self.add(key+'.c','claims',dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),ev,[u]);self.add(key+'.p','positions',dict(holder_candidates=[holder or voice] if (holder or voice)!='anonymous discussion' else [],claim_id=c,question_id=None,conditions=list(conditions),local_status=mode+' within stated local scope'),ev,[c]);return c
 def q(self,key,ref,quote,text,voice='anonymous discussion',conditions=(),composition='atomic'):
  u,ev=self.unit(key,ref,quote,voice,'question',composition);return self.add(key+'.q','questions',dict(formulation=text,question_origin='explicit',conditions=list(conditions),answer_set_status='partial'),ev,[u])
 def edge(self,key,a,b,relation,ref,quote):return self.add(key,'edges',dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),[self.ev(ref,quote)],[a,b])
 def structure(self,key,refs,title,boundary='closed'):
  return self.add(key,'structure',dict(title=title,primary=True,boundary=boundary,legacy_ids=[]),[self.ev(ref) for ref in refs],origin='editorial_inference')
 def save(self):
  state=r.current(self.job);cov=[]
  for ref,note in self.notes.items():
   sid=self.refs[ref]['id']
   for layer in r.LAYERS:
    ids=[x['id'] for x in self.rows if (x['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in x['evidence'])]
    cov.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Separate '+layer+' reread completed; '+('anchored results retained.' if ids else 'no independent object on this layer in this segment.')))
  tails=state['open_tails']+[x['id'] for x in self.rows if x['layer']=='structure' and x['content']['boundary']!='closed']
  p=dict(schema_version=r.VERSION,tractate='Makkot',owner='L04/makkot_resume_20261126',epoch=3,source_sha256=self.j['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/makkot_continuation',model_id=None),records=self.rows,coverage=cov,open_tails=tails)
  r.validate_apply(state,p,self.ss,self.j)
  out=self.job/'staging'/('continuation_'+self.batch+'.json');r.immutable(out,r.encoded(p));print(out);print(r.submit(self.job,out,p['owner'],3))
