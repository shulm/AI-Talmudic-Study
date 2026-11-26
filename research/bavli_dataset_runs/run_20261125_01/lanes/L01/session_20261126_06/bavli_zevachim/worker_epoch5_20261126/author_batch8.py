import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b8.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['12b:8'],'anonymous','question_answer','The singular elder wording with seventy-two teaches that all stood in one position.','asserted',['Seventy-two elders in Ben Azzai report'],'Explanation of unusual singular wording'),
('2',['12b:10'],'רב הונא','initial_derivation','Rav Huna initially explains Ben Azzai from עולה הוא: own-purpose burnt offering valid, wrong-purpose invalid.','rejected',['Burnt-offering pronoun derivation'],'Initial derivation replaced below'),
('3',['12b:11'],'anonymous','objection','Guilt offering too has הוא.','challenged',['Parallel guilt-offering wording'],'Objection to burnt-offering-exclusive proof'),
('4',['12b:12'],'anonymous','answer','The guilt-offering pronoun occurs after burning the portions.','asserted',['Guilt-offering pronoun location'],'Initial distinction'),
('5',['12b:13'],'anonymous','objection','The burnt-offering pronoun too occurs after burning the portions.','challenged',['Burnt-offering pronoun location'],'Undermines proposed distinction'),
('6',['12b:14'],'anonymous','answer','Two הוא occurrences appear for the burnt offering.','asserted',['Proposed surplus-word explanation'],'Initial defense'),
('7',['12b:15'],'anonymous','objection','There are also two הוא occurrences for the guilt offering.','challenged',['Parallel guilt-offering wording'],'Undermines surplus-word defense'),
('8',['12b:16'],'anonymous','replacement_derivation','Ben Azzai can be derived by a fortiori: sin offering not wholly burned is invalid not for its purpose, all the more a wholly burned burnt offering.','asserted',['Wrong-purpose burnt offering; comparison with sin offering'],'Reconstructed proof; alternate learned-tradition account follows'),
('9',['12b:17'],'anonymous','objection','Sin offering differs because it atones.','challenged',['Sin-offering premise'],'Distinguishing feature'),
('10',['12b:18'],'anonymous','counterexample','Paschal offering supplies a counterexample.','asserted',['Wrong-purpose Paschal offering'],'Response to atonement distinction'),
('11',['12b:19'],'anonymous','objection','Paschal differs because its time is fixed.','challenged',['Paschal premise'],'Distinguishing feature'),
('12',['12b:20'],'anonymous','common_factor','Sin and Paschal offerings jointly establish sacred status and invalidity not for their purpose; infer the burnt offering likewise.','asserted',['Combined sin/Paschal proof for burnt offering'],'Proposed common-factor inference'),
('13',['12b:21'],'anonymous','objection','Both examples have an aspect involving karet.','challenged',['Sin/Paschal common factor'],'Potential distinguishing severity'),
('14',['12b:22','13a:1'],'anonymous','answer','Ben Azzai does not object on the basis of an aspect of karet.','asserted',['First explanation of Ben Azzai proof'],'First resolution only; alternative follows'),
('15',['13a:2'],'anonymous','objection','Then why not also derive the guilt offering?','queried',['Extend combined proof to guilt offering'],'Scope challenge'),
('16',['13a:3'],'anonymous','answer','For guilt offering one can object that both examples occur publicly as well as individually.','asserted',['Sin/Paschal examples versus guilt offering; public/private availability'],'Distinguishing feature prevents extension'),
('17',['13a:4'],'anonymous','alternative_answer','Alternatively, Ben Azzai does accept the karet objection and received his rule by tradition.','asserted',['Alternative account of Ben Azzai source'],'Alternative, not forced harmonization with first resolution'),
('18',['13a:4'],'anonymous','alternative_explanation','On that alternative, Rav Huna\'s a-fortiori presentation was only to sharpen his students.','asserted',['Alternative tradition account'],'Pedagogic explanation local to this alternative')]
for key,refs,voice,role,prop,mode,cond,status in D:
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['1','8','12','17'] else 'atomic'))
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Ben Azzai burnt-offering exception and alternative source accounts',assertion_mode=mode),['u'+key])
 if key in ['1','2','3','5','7','9','11','13','15']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key])
 if mode!='queried':rec('p'+key,'positions',refs,dict(holder_candidates=['רב הונא'] if key=='2' else [],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key])
rec('a2','attributions',['12b:10'],dict(surface='רב הונא',role='speaker',candidates=['רב הונא'],scope='Initial explanation of Ben Azzai',transmission_chain=[]),['c2'])
rec('aBen','attributions',['12b:16','12b:22','13a:4'],dict(surface='בן עזאי',role='quoted_authority',candidates=['בן עזאי'],scope='Anonymous explanations of Ben Azzai position; alternate foundations retained',transmission_chain=[]),['c8','c14','c17'])
rec('uLemma','utterances',['12b:9'],dict(textual_voice='Mishnah lemma',discourse_role='topic heading',composition='atomic'),origin='literal')
for a,b,rel in [('3','2','objection'),('4','3','answer'),('5','4','objection'),('6','5','answer'),('7','6','objection'),('8','2','correction'),('9','8','objection'),('10','9','answer'),('11','10','objection'),('12','11','answer'),('13','12','objection'),('14','13','answer'),('15','14','objection'),('16','15','answer'),('17','13','answer'),('18','17','qualification')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['12b:'+str(i) for i in range(8,23)]+['13a:'+str(i) for i in range(1,5)]
rec('s1','structure',refs,dict(title='Ben Azzai: elders wording, failed pronoun derivation, common factor or received tradition',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual reread through13a4 alternative resolution and13a5 new Mishnah. Preserve first versus alternative karet treatment, pedagogic account, failed pronoun defenses, and separate source occurrence of elder explanation.' if layer=='reconciliation' else 'Manual source pass; '+('supported records listed.' if ids else 'No separate '+layer+' finding; lemma or anonymous discourse retained in utterances.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_12b8_13a4.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch8.json',r.encoded(res));print(res)
