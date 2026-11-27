from pathlib import Path
import sys,json
sys.path.insert(0,str(Path.cwd()/'research/bavli_production_v1'))
import runner
D=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L06/bavli_meilah')
class Batch:
 def __init__(self,name,start,end):
  self.name=name;self.start=start;self.end=end;self.J,self.ss=runner.load(D);self.S=list(self.ss.values());self.R=[];self.C={};self.Q={}
 def add(self,k,l,ii,c,links=None,u=None):
  rid='l06.mei.'+self.name+'.'+k;self.R.append(dict(id=rid,layer=l,evidence=[dict(segment_id=self.S[i]['id'],start_char=0,end_char=len(self.S[i]['text']),quote=self.S[i]['text']) for i in ii],content=c,links=links or [],uncertainty=u or [],origin='source_paraphrase'));return rid
 def structure(self,k,ii,title,boundary='closed'):
  return self.add('s.'+k,'structure',ii,dict(title=title,primary=True,boundary=boundary,legacy_ids=[]))
 def claim(self,k,ii,text,conditions=None,holders=None,mode='asserted',uncertainty=None):
  c=self.add('c.'+k,'claims',ii,dict(proposition=text,conditions=conditions or [],scope=self.name,assertion_mode=mode),u=uncertainty);self.C[k]=c;self.add('p.'+k,'positions',ii,dict(holder_candidates=holders or [],claim_id=c,question_id=None,conditions=conditions or [],local_status=mode),[c],uncertainty);return c
 def question(self,k,ii,text):
  self.Q[k]=self.add('q.'+k,'questions',ii,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'));return self.Q[k]
 def attribution(self,k,ii,surface,people,scope,role='speaker',chain=None):
  return self.add('a.'+k,'attributions',ii,dict(surface=surface,role=role,candidates=people,scope=scope,transmission_chain=chain or []))
 def edge(self,k,a,b,ii,relation):
  return self.add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=relation,explicitness='source_explicit'),[a,b])
 def finish(self,rationale):
  for i in range(self.start,self.end):
   self.add('u'+str(i),'utterances',[i],dict(textual_voice='quoted teaching and anonymous or named discussion',discourse_role='rule, question, argument, qualification or continuation',composition='composite'))
   self.attribution('anon'+str(i),[i],'anonymous framing',[],'framing only; named teachings separately scoped','anonymous')
  cv=[]
  for i in range(self.start,self.end):
   for l in runner.LAYERS:
    ids=[r['id'] for r in self.R if (r['layer']==l or l=='reconciliation') and any(e['segment_id']==self.S[i]['id'] for e in r['evidence'])];cv.append(dict(segment_id=self.S[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
  J=self.J;p=dict(schema_version=J['schema_version'],tractate=J['tractate'],owner='/root/l06_meilah',epoch=2,source_sha256=J['source_sha256'],schema_sha256=J['schema_sha256'],protocol_sha256=J['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=self.R,coverage=cv,open_tails=runner.current(D)['open_tails']+[r['id'] for r in self.R if r['layer']=='structure' and r['content']['boundary']!='closed'])
  f=D/'authored_20261126'/(self.name+'_v1.json');assert not f.exists();f.write_bytes(runner.encoded(p));runner.validate_apply(runner.current(D),p,self.ss,J);result=runner.submit(D,f,'/root/l06_meilah',2);assert runner.replay(D)['replay_pass'];print(result['snapshot_sha256'],result['proposal_sha256'],self.end)
