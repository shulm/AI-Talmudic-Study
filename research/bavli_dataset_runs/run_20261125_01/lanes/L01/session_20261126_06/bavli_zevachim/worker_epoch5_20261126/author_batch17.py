import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b17.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='8eb098f3dc8e9c9373ea80f7a529acc74ddc74e94a58a815bee73d65862ccbce'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','17b:6','anonymous','What is the source for disqualification when priestly garments are missing?','queried',['Missing priestly garments'],'New derivation inquiry'),
('2','17b:6','Rabbi Yohanan; alternate report Rabbi Elazar son of Rabbi Shimon','While their garments are on them their priesthood is on them.','asserted',['Priestly garments worn; Exodus29:9'],'Reported by Rabbi Abbahu; alternative ultimate attribution preserved'),
('3','17b:6','Rabbi Yohanan; alternate report Rabbi Elazar son of Rabbi Shimon','Without their garments they lack priesthood for the service.','asserted',['Priestly garments missing; Exodus29:9'],'Reported derivation of missing-garment invalidity'),
('4','17b:7','anonymous','Is missing-garment invalidity not already derived through the intoxicated-service teaching?','queried',['Alternative source for same invalidity'],'Challenge to need for first verse'),
('5','17b:7','quoted baraita','Intoxicated service profanes, derived from the prohibition of wine and distinguishing holy from ordinary.','asserted',['Priest who drank wine; service'],'Baraita derivation examined'),
('6','17b:7,18a:1','quoted baraita','Missing-garment service is linked by the shared statute wording.','asserted',['Missing priestly garments; hukkah comparison'],'Initial formulation from wine case'),
('7','17b:7,18a:1','quoted baraita','Service without washing hands and feet is linked by the shared statute wording.','asserted',['Hands and feet unwashed; hukkah comparison'],'Distinct disqualification'),
('8','18a:2','anonymous','The wine comparison alone might limit invalidity to service for which a nonpriest is liable to death.','hypothetical',['Initial proposed limit on missing-garment derivation'],'Reason additional source needed'),
('9','18a:2','anonymous','The priesthood-with-garments source includes service for which a nonpriest is not liable to death.','asserted',['Missing garments; service without nonpriest death liability'],'Broadens service scope'),
('10','18a:3','anonymous','Having established the broad missing-garment rule, how is the broad intoxicated-service rule established?','queried',['Service without nonpriest death liability'],'Scope inquiry'),
('11','18a:3','anonymous','The shared statute wording derives intoxicated-service invalidity from missing garments.','asserted',['Broad service scope; hukkah comparison'],'Reverse direction after independent garments source'),
('12','18a:4','anonymous','But the teacher cites distinguishing holy from ordinary.','queried',['Apparent inconsistency in derivation source'],'Objection'),
('13','18a:4','anonymous','That citation is before the verbal analogy has been established.','asserted',['Stage of derivation before hukkah comparison'],'Reply'),
('14','18a:5','anonymous','But the teacher appears to derive missing garments from intoxication.','queried',['Apparent direction of derivation'],'Second objection'),
('15','18a:5','anonymous','The teaching means the shared statute wording establishes no distinction among missing garments, intoxication and unwashed hands/feet.','asserted',['Equivalent service scope across three disqualifications'],'Reformulated baraita reading'),
('16','18a:6','anonymous','What then is the distinguishing clause needed for?','queried',['Leviticus10:10 after verbal analogy'],'Residual verse purpose'),
('17','18a:6','Rav practice','Rav did not appoint a public interpreter from one festival day to the next because of intoxication.','asserted',['Public teaching while affected by festival wine'],'Practice illustrating distinguishing clause; Rav himself, not Rav Yehuda'),
('18','18a:7','anonymous','Is missing-garment invalidity not already derived from Aaron the priest acting in his priesthood?','queried',['Alternative Exodus/Leviticus garment source'],'Redundancy challenge'),
('19','18a:7','quoted derivation','A high priest serving in ordinary-priest garments has invalid service.','asserted',['High priest; ordinary-priest garment set'],'Leviticus1:7 priest in his priesthood'),
('20','18a:8','anonymous','The other source is needed to include service that does not prevent atonement.','asserted',['Missing garments; non-atonement-essential service'],'Prevents limiting garment invalidity to atonement-essential service'),
('21','18a:9','anonymous','Is garment invalidity not already derived from the priests arranging the pieces in their priesthood?','queried',['Leviticus1:8 alternate source'],'Further redundancy challenge'),
('22','18a:9','quoted derivation','An ordinary priest serving in high-priest garments has invalid service.','asserted',['Ordinary priest; high-priest garment set'],'Excess-garment case'),
('23','18a:10','anonymous','A source stating deficient garments alone would not establish excess garments; the additional source teaches excess too.','asserted',['Excess garments distinct from missing garments'],'Concluding necessity of both sources')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'derivation',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Missing and excess garments; intoxication and unwashed service derivations',assertion_mode=mode),['u'+k],['Alternative ultimate attribution: Rabbi Yohanan or Rabbi Elazar son of Rabbi Shimon.'] if k in ['2','3'] else [])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v in ['anonymous','quoted baraita','quoted derivation'] else (['Rabbi Yohanan','Rabbi Elazar son of Rabbi Shimon'] if k in ['2','3'] else ['Rav'])
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k],['Alternative reports, not joint attribution.'] if k in ['2','3'] else [])
rec('aabbahu','attributions',['17b:6'],dict(surface='Rabbi Abbahu said Rabbi Yohanan',role='transmitter',candidates=['Rabbi Abbahu'],scope='Primary report chain',transmission_chain=['Rabbi Abbahu','Rabbi Yohanan']),['c2','c3'])
rec('aalternate','attributions',['17b:6'],dict(surface='and some reach it in the name of Rabbi Elazar son of Rabbi Shimon',role='quoted_authority',candidates=['Rabbi Elazar son of Rabbi Shimon'],scope='Alternative ultimate report attribution',transmission_chain=[]),['c2','c3'],['Alternative version; do not append as a definite extra transmitter in the primary chain.'])
rec('arav','attributions',['18a:6'],dict(surface='Rav',role='speaker',candidates=['Rav'],scope='Named practice about intoxication and public interpreter',transmission_chain=[]),['c17'])
for a,b,rel in [('3','1','answer'),('2','3','support'),('4','3','objection'),('5','4','support'),('6','4','support'),('7','6','analogy'),('8','4','answer'),('9','8','qualification'),('11','10','answer'),('12','11','objection'),('13','12','answer'),('14','11','objection'),('15','14','answer'),('17','16','answer'),('18','3','objection'),('19','18','support'),('20','18','answer'),('21','20','objection'),('22','21','support'),('23','21','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['17b:6','17b:7']+['18a:'+str(i) for i in range(1,11)]
rec('s1','structure',refs,dict(title='Priestly garments and related disqualifications: derivation scope and alternative report',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through18a10 and ensuing garment baraita18a11–18b12. Preserve alternate Rabbi Elazar son of Rabbi Shimon attribution, service-scope limits, reversed derivation direction and deficient/excess distinction.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_17b6_18a10.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch17.json',r.encoded(res));print(res)
