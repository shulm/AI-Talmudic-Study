import json, hashlib, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
def digest(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
class Reading:
 def __init__(self,n,contexts):
  self.n=n; self.j=json.loads((ROOT/'jobs'/('bavli_'+n+'.json')).read_text(encoding='utf-8-sig')); j=self.j
  bindings=j['common_documents']+[j['source'],j['original_source_schema'],j['frozen_plan']]
  for d in bindings: assert digest(d['path'])==d['sha256']
  self.s=json.loads(pathlib.Path(j['source']['path']).read_text(encoding='utf-8-sig')); self.text={f'{j["tractate"]} {i//2+1}{"a" if i%2==0 else "b"}:{z+1}':t for i,a in enumerate(self.s['text']) for z,t in enumerate(a)}
  bs=j['selected_blocks'][:3]; core=[r for b in bs for r in b['core_refs']]
  self.d=dict(artifact_kind='frozen_source_only_bounded_reading',tractate=j['tractate'],core_refs=core,selected_blocks=bs,bindings=bindings,source_only_provenance=dict(agent_id='reader_l04_remaining_wave6',model_id=None,producer_annotations_seen=False,prior_readings_seen=False,source_edition={k:self.s[k] for k in ['versionTitle','versionSource','license']},coordinate_contract='Python Unicode codepoint half-open offsets in original unnormalized strings',source_only=True),findings=[],questions=[],answer_sets=[],relations=[],uncertainties=[],coverage={},next_coordinates=j['selected_blocks'][3],ml_eligible=False,full_admission=False)
  self.context=[]
  for lo,hi in contexts:
   refs=list(self.text);a=refs.index(j['tractate']+' '+lo);b=refs.index(j['tractate']+' '+hi);self.context+=refs[a:b+1]
  self.context=list(dict.fromkeys(self.context)); assert set(core)<=set(self.context)
 def ev(self,ref,quote=None):
  ref=self.j['tractate']+' '+ref; t=self.text[ref]; assert ref in self.context
  quote=t if quote is None else quote; start=t.index(quote)
  return dict(ref=ref,start_char=start,end_char=start+len(quote),quote=quote)
 def claim(self,ref,holder,proposition,quote=None,status='asserted',conditions=None,chain=None):
  id=f'{self.n}.c{len(self.d["findings"])+1:03}'
  self.d['findings'].append(dict(id=id,kind='atomic_claim',origin='source_paraphrase',proposition=proposition,holder_candidates=holder.split('|'),transmission_chain=chain or [],conditions=conditions or [],local_status=status,evidence=[self.ev(ref,quote)]));return id
 def question(self,ref,text,answers,quote=None,origin='explicit',status='locally_answered'):
  id=f'{self.n}.q{len(self.d["questions"])+1:03}'
  self.d['questions'].append(dict(id=id,formulation=text,origin=origin,evidence=[self.ev(ref,quote)]))
  self.d['answer_sets'].append(dict(id=id+'.answers',question_id=id,claim_ids=answers,status=status,comparability='Same local question; conditions and differing rationales preserved; no enduring scholar position inferred.'));return id
 def rel(self,source,target,kind,ref): self.d['relations'].append(dict(id=f'{self.n}.r{len(self.d["relations"])+1:03}',source_id=source,target_id=target,relation=kind,explicitness='source_explicit',evidence=[self.ev(ref)]))
 def freeze(self,notes):
  d=self.d;core=set(d['core_refs']);d['uncertainties']=notes
  d['coverage']=dict(status='bounded_source_reading_not_production_layer_completion',core_segments=len(core),probability_core_segments=len({r for b in d['selected_blocks'] if 'probability_sample' in b['roles'] for r in b['core_refs']}),endpoint_core_segments=len({r for b in d['selected_blocks'] if any('check' in x for x in b['roles']) for r in b['core_refs']}),context_only_refs=[r for r in self.context if r not in core],read_refs=self.context,segment_review=[dict(ref=r,status='source_read',finding_ids=[f['id'] for f in d['findings'] if any(e['ref']==r for e in f['evidence'])],rationale='Read original source and continuation; bounded semantic findings, not exhaustive production structure partition.') for r in d['core_refs']],reconciliation='Source reread against independently authored findings; no producer comparison.',excluded='No full tractate review, production comparison, human certification, or ML/task admission.')
  ids=[o['id'] for k in ['findings','questions','answer_sets','relations'] for o in d[k]];assert len(ids)==len(set(ids)); count=0
  def check(x):
   nonlocal count
   if isinstance(x,dict):
    if all(k in x for k in ['ref','start_char','end_char','quote']):assert self.text[x['ref']][x['start_char']:x['end_char']]==x['quote'];count+=1
    for k,v in x.items():
     if k in ['source_id','target_id','question_id']: assert v in ids
     if k=='claim_ids':assert all(i in ids for i in v)
     check(v)
   elif isinstance(x,list):
    for y in x:check(y)
  check(d)
  p=ROOT/'readings'/(self.n+'_batch001.json');assert not p.exists();p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');h=digest(p)
  with pathlib.Path(str(p)+'.sha256').open('x',encoding='utf-8') as f:f.write(h+'  '+p.name+'\n')
  report=dict(reading=p.name,sha256=h,status='PASS',source_and_common_and_plan_hashes='PASS',evidence_slices_checked=count,unique_ids=len(ids),core_membership='PASS',core_segments=len(core),semantic_certification=False)
  with pathlib.Path(str(p)+'.validation.json').open('x',encoding='utf-8') as f:json.dump(report,f,indent=2)
  print(json.dumps(report))
