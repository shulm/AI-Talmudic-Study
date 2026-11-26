import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b15.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='3200660de8f16e0f249eb4796febac0f964e51a646f0ac0cc751acaa8291af72'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','16a:14','anonymous','What is the source for invalidity of an onen serving?','queried',['Onen service'],'New derivation inquiry'),
('2','16a:14','anonymous','The high priest not leaving and not profaning implies another priest who remains and serves profanes.','asserted',['Leviticus21:12; ordinary priest in mourning'],'First derivation contested by Rabbi Elazar'),
('3','16a:15','Rabbi Elazar','Aaron says he offered; had his sons offered, burning would have been proper.','asserted',['Leviticus10:19; onen sons offering'],'Alternative derivation of onen invalidity'),
('4','16a:16','anonymous','Why does Rabbi Elazar not use the high-priest verse?','queried',['Alternative derivation source'],'Question on preference'),
('5','16a:16','Rabbi Elazar reconstructed reply','Does the verse explicitly say that another who does not leave profanes?','challenged',['Inference from high priest exception'],'Rejects first derivation inference; reconstructed response'),
('6','16a:17','anonymous','Why does the other authority not derive from Aaron statement?','queried',['Alternative derivation source'],'Question on anonymous authority preference'),
('7','16a:17','anonymous authority','That offering was burned because of impurity.','asserted',['Reason for burning in Leviticus10 episode'],'Alternative to mourning explanation'),
('8','16a:18,16b:1','school of Rabbi Ishmael','If a blemished priest who may eat profanes by serving, an onen who may not eat certainly profanes.','asserted',['Onen compared with blemished priest'],'Initial a-fortiori derivation'),
('9','16b:2','anonymous','Blemish is stricter because it disqualifies offerings as well as offerers.','asserted',['Blemished animal and priest'],'Objection'),
('10','16b:3','anonymous','A nonpriest supplies the proof counterexample.','asserted',['Nonpriest proof partner'],'Reply'),
('11','16b:3','anonymous','A nonpriest is stricter because his status has no remedy.','asserted',['Nonpriest status'],'Objection'),
('12','16b:4','anonymous','Blemish supplies the counterexample; together the warning and profanation of these cases extend to an onen.','asserted',['Common-factor proof: blemished priest and nonpriest'],'Combined derivation'),
('13','16b:5','anonymous','Where is an onen warned independently of a verse already stating profanation?','queried',['Need warning premise for common-factor proof'],'High-priest verse would itself state profanation'),
('14','16b:5','anonymous','The warning is derived from Aaron statement, assuming the offering was burned because of mourning.','asserted',['Leviticus10:19; mourning as reason for burning'],'Conditional interpretive premise retained'),
('15','16b:6','anonymous','The combined proof cases are stricter because no exception to their prohibition was permitted.','asserted',['Blemished priest and nonpriest; contrast onen high priest'],'Objection to common factor'),
('16','16b:7','anonymous','An impure priest supplies a proof counterexample.','asserted',['Impurity has an exception'],'Reply'),
('17','16b:8','anonymous','Impurity is stricter because it transmits impurity.','asserted',['Impure proof partner'],'Objection'),
('18','16b:8','anonymous','The earlier cases counter that distinction, yielding a combined common-factor proof from warned persons.','asserted',['Blemish, nonpriest and impurity proof cases'],'Reply'),
('19','16b:9','anonymous','Could the combined cases be challenged because none is permitted to a high priest offering an individual sacrifice?','queried',['Specific high-priest individual-offering exception'],'Further objection'),
('20','16b:9','anonymous','The category of impurity has nevertheless been permitted.','asserted',['General impurity exception suffices despite different context'],'Reply to specific-context objection'),
('21','16b:10','Rav Mesharshiya','A seated priest may eat yet profanes service, so an onen who may not eat certainly profanes.','asserted',['Seated priest compared with onen'],'Alternative a-fortiori proof'),
('22','16b:11','anonymous','Seated posture is stricter because it disqualifies testimony.','asserted',['Seated witness'],'Objection'),
('23','16b:11','anonymous','Use a seated Torah scholar as the comparison.','asserted',['Scholar may testify seated'],'Reply'),
('24','16b:12','anonymous','Could the category of sitting be challenged for its testimony restriction?','queried',['Category-level objection'],'Further objection'),
('25','16b:12','anonymous','The category of sitting is not a valid objection.','asserted',['Category-level comparison'],'First reply'),
('26','16b:12','anonymous','Even accepting that objection, derive from a seated person plus one earlier case.','conditional',['Assume category objection accepted'],'Alternative combined proof')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'derivation',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Derivations for onen service invalidity',assertion_mode=mode),['u'+k])
 if mode=='queried' or k=='5':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried':
  holder=[] if v.startswith('anonymous') else (['Rabbi Elazar'] if k=='5' else [v])
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,refs,surface,cands,role,links in [('elazar',['16a:15','16a:16'],'Rabbi Elazar',['Rabbi Elazar'],'speaker',['c3','c5']),('ishmael',['16a:18','16b:1'],'school of Rabbi Ishmael',['school of Rabbi Ishmael'],'collective',['c8']),('mesh',['16b:10'],'Rav Mesharshiya',['Rav Mesharshiya'],'speaker',['c21'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role=role,candidates=cands,scope='Named local derivation attribution',transmission_chain=[]),links)
for a,b,rel in [('2','1','answer'),('3','1','answer'),('5','4','answer'),('5','2','objection'),('7','6','answer'),('7','3','objection'),('8','1','answer'),('9','8','objection'),('10','9','answer'),('11','10','objection'),('12','11','answer'),('13','12','objection'),('14','13','answer'),('15','12','objection'),('16','15','answer'),('17','16','objection'),('18','17','answer'),('19','18','objection'),('20','19','answer'),('21','1','answer'),('22','21','objection'),('23','22','answer'),('24','23','objection'),('25','24','answer'),('26','24','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['16a:'+str(i) for i in range(14,19)]+['16b:'+str(i) for i in range(1,13)]
rec('s1','structure',refs,dict(title='Onen invalidity: competing scriptural readings and combined derivations',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through16b12; next16b13 introduces Rava communal-offering qualification. Preserve anonymous first authority, reconstructed Elazar response, competing burning reasons and all conditional proof alternatives.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_16a14_16b12.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch15.json',r.encoded(res));print(res)
