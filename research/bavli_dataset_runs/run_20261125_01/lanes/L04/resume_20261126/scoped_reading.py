"""Serialization helper for explicitly authored readings, not an extractor.

Uses the common production schema/runner unchanged. All semantic decisions,
source windows, literal spans and relations must be supplied by the author.
"""
from author_remaining_openings_001 import Reading,r
class ScopedReading(Reading):
    def span(self,ref,quote):
        s=self.refs[ref];assert s['text'].count(quote)==1,(ref,quote)
        start=s['text'].index(quote)
        return dict(segment_id=s['id'],start_char=start,end_char=start+len(quote),quote=quote)
    def speech(self,key,ref,quote,candidates=(),role='speaker',composition='atomic',act='assertion',uncertainty=(),chain=(),naming_refs=()):
        u=self.add(key+'.u','utterances',dict(textual_voice=' / '.join(candidates) if candidates else 'anonymous discussion',discourse_role=act,composition=composition),[ref],uncertainty=uncertainty)
        self.rows[-1]['evidence']=[self.span(ref,quote)]
        aid=self.add(key+'.a','attributions',dict(surface=' / '.join(candidates),role=role if candidates else 'anonymous',candidates=list(candidates),scope=u,transmission_chain=list(chain)),[ref],[u],uncertainty)
        self.rows[-1]['evidence']=[self.span(ref,quote)]+[self.evidence(x) for x in dict.fromkeys(([ref] if candidates and quote!=self.refs[ref]['text'] else [])+list(naming_refs))]
        return u
    def claim(self,key,ref,quote,text,candidates=(),mode='asserted',conditions=(),scope='Local source assertion; not a later practical ruling',**kwargs):
        u=self.speech(key,ref,quote,candidates,act=mode,**kwargs)
        uncertainty=list(kwargs.get('uncertainty',()))
        if kwargs.get('composition')=='composite':uncertainty.append('Source list or paired formulation retained together; not certified as an atomic claim.')
        cid=self.add(key+'.c','claims',dict(proposition=text,conditions=list(conditions),scope=scope,assertion_mode=mode),[ref],[u],uncertainty)
        self.add(key+'.p','positions',dict(holder_candidates=list(candidates),claim_id=cid,question_id=None,conditions=list(conditions),local_status=mode+' in this source context'),[ref],[cid],uncertainty)
        return cid
    def question(self,key,ref,quote,text,candidates=(),**kwargs):
        u=self.speech(key,ref,quote,candidates,act='explicit question',**kwargs)
        return self.add(key+'.q','questions',dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='none'),[ref],[u],kwargs.get('uncertainty',()))
    def save_window(self,refs,filename,rationale,expected_parent):
        state=r.current(self.job);assert r.sha(r.encoded(state))==expected_parent
        active=[x for x in state['records'] if x['release_state']=='valid']+self.rows
        cov=[]
        for ref in refs:
            sid=self.refs[ref]['id']
            for layer in r.LAYERS:
                ids=[x['id'] for x in active if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
                cov.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale+' '+layer+' source pass: '+('supported records retained.' if ids else 'no additional independent object found.')))
        p=dict(schema_version=r.VERSION,tractate=self.title,owner='L04/'+self.slug+'_resume_20261126',epoch=3,source_sha256=self.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id=getattr(self,'agent_id','/root'),model_id=None),records=self.rows,coverage=cov,open_tails=state['open_tails'])
        out=self.job/'staging'/filename;r.immutable(out,r.encoded(p));print(out)
