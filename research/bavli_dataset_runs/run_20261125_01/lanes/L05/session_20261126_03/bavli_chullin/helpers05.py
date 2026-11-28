import json, pathlib, hashlib
W=pathlib.Path('F:/Sefaria_QA/worktrees/bavli-l05-production-20261126'); J=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_chullin'); O=pathlib.Path('F:/Sefaria_QA/bavli_l05_workspace_20261126/proposals/bavli_chullin');O.mkdir(parents=True,exist_ok=True)
inv=json.loads((J/'source_inventory.json').read_text(encoding='utf8'));meta=json.loads((J/'JOB.json').read_text()); rows=[]
def ev(n,q=None):
 s=inv[n];q=s['text'] if q is None else q;start=s['text'].index(q);return dict(segment_id=s['id'],start_char=start,end_char=start+len(q),quote=q)
def rec(id,layer,e,content,links=[],unc=[],origin='source_paraphrase'):
 rid='ch05_'+id;rows.append(dict(id=rid,layer=layer,evidence=e,content=content,origin=origin,uncertainty=unc,links=links));return rid
def unit(id,n,q,prop,holder='anonymous discussion',mode='asserted',conditions=[],role='explanation',unc=[]):
 e=[ev(n,q)];u=rec(id+'_u','utterances',e,dict(textual_voice=holder,discourse_role=role,composition='composite' if conditions else 'atomic'),origin='literal');c=rec(id+'_c','claims',e,dict(proposition=prop,conditions=conditions,scope='Rav Ashi and two Ravina versions; comparative explanations of the opening Mishnah, not a final halakhic ruling',assertion_mode=mode),[u],unc);rec(id+'_a','attributions',e,dict(surface=holder,role='anonymous' if holder=='anonymous discussion' else 'position_holder',candidates=[] if holder=='anonymous discussion' else [holder],scope=prop,transmission_chain=[]),[c],unc);rec(id+'_p','positions',e,dict(holder_candidates=[] if holder=='anonymous discussion' else [holder],claim_id=c,question_id=None,conditions=conditions,local_status=mode+'; AI provisional; wider dispute retained'),[c],unc);return c
def question(id,n,q,form,cond=[]):
 e=[ev(n,q)];u=rec(id+'_u','utterances',e,dict(textual_voice='anonymous discussion',discourse_role='question/objection',composition='atomic'),origin='literal');r=rec(id,'questions',e,dict(formulation=form,question_origin='explicit',conditions=cond,answer_set_status='partial'),[u]);rec(id+'_a','attributions',e,dict(surface='anonymous discussion',role='anonymous',candidates=[],scope=form,transmission_chain=[]),[r]);return r
def edge(id,n,source,target,kind,q=None):return rec(id,'edges',[ev(n,q)],dict(source_id=source,target_id=target,relation=kind,explicitness='source_explicit'),[source,target])

O=W/'research/bavli_dataset_runs/run_20261125_01/lanes/L05/session_20261126_03/bavli_chullin'
