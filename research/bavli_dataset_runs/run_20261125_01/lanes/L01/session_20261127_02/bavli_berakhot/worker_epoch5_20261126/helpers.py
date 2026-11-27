from pathlib import Path
import sys
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/l01-production-20261125/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE=Path(__file__).resolve().parent;JOB=HERE.parent;j,ss=r.load(JOB);state=r.current(JOB)
by={x['ref'].split(' ')[1]:x for x in ss.values()};rows=[];pre='bk.piety.20261126w2.'
def ev(ref,quote=None):
 t=by[ref]['text'];quote=t if quote is None else quote;a=t.index(quote)
 return dict(segment_id=by[ref]['id'],start_char=a,end_char=a+len(quote),quote=quote)
def add(k,layer,refs,content,links=(),unc=(),origin='source_paraphrase'):
 rows.append(dict(id=pre+k,layer=layer,evidence=[ev(x) if isinstance(x,str) else ev(*x) for x in refs],content=content,links=[pre+x for x in links],uncertainty=list(unc),origin=origin));return pre+k
def c(k,ref,p,mode='asserted',cond=()):return add(k,'claims',[ref],dict(proposition=p,conditions=list(cond),scope='Local source account; preserve alternatives, distinguish reported behavior from universal legal claims.',assertion_mode=mode))
def q(k,ref,p):return add(k,'questions',[ref],dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,ref,a,b,rel):return add(k,'edges',[ref],dict(source_id=pre+a,target_id=pre+b,relation=rel,explicitness='source_explicit'),[a,b])
def pos(k,ref,cl,holders,status,question=None,cond=(),unc=()):return add(k,'positions',[ref],dict(holder_candidates=holders,claim_id=pre+cl,question_id=pre+question if question else None,conditions=list(cond),local_status=status),[cl]+([question] if question else []),unc)
def att(k,ref,surface,role,candidates,scope,chain=(),unc=()):return add(k,'attributions',[(ref,surface)],dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=list(chain)),unc=unc)
