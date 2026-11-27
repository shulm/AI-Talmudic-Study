import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b28.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='665564181580669b7731304da6dfaaea01aa69177674019cbee3bfa7ed44a8e3'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','21b:12','Rabbi Yosei son of Rabbi Hanina','A laver without enough water for four priests cannot be used for sanctification.','asserted',['Less than four-priest capacity'],'Derived from Moses Aaron and sons'),
('2','21b:13,22a:1','quoted source','All service vessels sanctify whether they contain a quarter-log or not.','asserted',['Service vessel; amount may be below quarter-log'],'Apparent objection to capacity rule'),
('3','22a:2','Rav Adda bar Aha','The case concerns boring within it.','asserted',['Small vessel case connected with the laver through a bored opening'],'Reconciliation; exact configuration not specified in this segment'),
('4','22a:3','anonymous','But Scripture says from it.','queried',['Potential restriction to laver'],'Objection to other service vessels'),
('5','22a:3','anonymous','They shall wash includes service vessels.','asserted',['Inclusive washing wording'],'Reply'),
('6','22a:4','anonymous','If so, why not ordinary vessels as well?','queried',['Scope of inclusive washing wording'],'Objection'),
('7','22a:4','Abaye','Ordinary vessels cannot be included by an a-fortiori inference from the base, which was anointed with the laver yet does not sanctify.','challenged',['Ordinary vessels not anointed; laver base anointed but not sanctifying'],'Inference challenged by function difference'),
('8','22a:5','anonymous','How is it known that the laver base does not sanctify?','queried',['Premise about base'],'Source inquiry'),
('9','22a:5','Rabbi Yehuda','The base is equated with the laver for copper, not for anything else.','asserted',['Exodus30:18; copper laver and copper base'],'Derivation excluding base from sanctifying'),
('10','22a:6','Mar Zutra son of Rav Mari','The base is not made to contain, unlike an ordinary vessel made to contain.','asserted',['Functional difference defeats comparison'],'Objection to Abaye inference addressed to Ravina'),
('11','22a:6','anonymous','Instead, from it excludes ordinary vessels.','asserted',['Restrictive mimennu wording'],'Replacement derivation'),
('12','22a:7','anonymous','Then why not exclude service vessels too?','queried',['Scope of restrictive wording'],'Objection'),
('13','22a:7','anonymous','Scripture includes them through they shall wash.','asserted',['Service vessels included by yirhatzu'],'Reply'),
('14','22a:8','anonymous','Why choose this allocation?','queried',['Include service vessels and exclude ordinary ones'],'Question on interpretive preference'),
('15','22a:8','anonymous','Service vessels require anointing like the laver.','asserted',['Service-vessel similarity to laver'],'Reason for inclusion'),
('16','22a:8','anonymous','Ordinary vessels do not require anointing like the laver.','asserted',['Ordinary-vessel difference from laver'],'Reason for exclusion')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Laver capacity and other vessel eligibility',assertion_mode=mode),['u'+k],['Exact bored-opening configuration not independently resolved; literal source retained.'] if k=='3' else [])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried':rec('p'+k,'positions',refs,dict(holder_candidates=[] if v in ['anonymous','quoted source'] else [v],claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,ref,surface,links in [('hanina','21b:12','Rabbi Yosei son of Rabbi Hanina',['c1']),('adda','22a:2','Rav Adda bar Aha',['c3']),('abaye','22a:4','Abaye',['c7']),('yehuda','22a:5','Rabbi Yehuda',['c9']),('zutra','22a:6','Mar Zutra son of Rav Mari',['c10'])]:rec('a'+k,'attributions',[ref],dict(surface=surface,role='speaker',candidates=[surface],scope='Explicit local speaker',transmission_chain=[]),links)
for a,b,rel in [('2','1','objection'),('3','2','qualification'),('4','3','objection'),('5','4','answer'),('6','5','objection'),('7','6','answer'),('9','8','answer'),('9','7','support'),('10','7','objection'),('11','6','answer'),('12','11','objection'),('13','12','answer'),('15','14','answer'),('16','14','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['21b:12','21b:13']+['22a:'+str(i) for i in range(1,9)]
rec('s1','structure',refs,dict(title='Four-priest laver capacity and inclusion of other service vessels',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through22a8 and new water-volume topic22a9 onward. Preserve laver versus other-vessel capacity, bored-opening uncertainty, challenged base analogy and replacement inclusive/restrictive wording argument.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_21b12_22a8.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch28.json',r.encoded(res));print(res)
