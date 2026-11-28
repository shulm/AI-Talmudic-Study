import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b22.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='ac5373d071cf710cf8cf67b2335824f9f60c7c5afa806410443644731849528e'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','19b:2','anonymous','What is the source for disqualification of one lacking atonement?','queried',['Required atonement offering not yet brought'],'New source inquiry'),
('2','19b:2','Rav Huna','The priest shall atone for her and she shall be pure implies she remains impure beforehand.','asserted',['Leviticus12:8; missing atonement'],'Source for status'),
('3','19b:3','anonymous','Unwashed hands and feet are learned through shared statute wording from missing garments.','asserted',['Hands and feet not washed; hukkah analogy'],'Source for invalidity'),
('4','19b:4','quoted baraita','A high priest who omitted immersion between garments or services nevertheless has valid service.','asserted',['High priest; intervening immersion omitted'],'Distinguished from morning washing'),
('5','19b:4','quoted baraita','A high priest who omitted sanctification between garments or services nevertheless has valid service.','asserted',['High priest; intervening hand/foot sanctification omitted'],'Distinct omitted act'),
('6','19b:4','quoted baraita','A high priest who omitted morning sanctification of hands and feet has invalid service.','asserted',['High priest; morning sanctification omitted'],'Indispensable morning act'),
('7','19b:4','quoted baraita','An ordinary priest who omitted morning sanctification of hands and feet has invalid service.','asserted',['Ordinary priest; morning sanctification omitted'],'Same requirement for ordinary priest'),
('8','19b:5','Rav Assi','Since five immersions and ten sanctifications are biblical and statute is written, why do they not invalidate when omitted?','queried',['High-priest required immersions and sanctifications'],'Question to Rabbi Yohanan; Rav Assi is not Rav'),
('9','19b:6','Rabbi Yohanan','And he shall put them on makes dressing indispensable while other acts do not invalidate.','asserted',['Leviticus16:4; intervening acts versus dressing'],'Initial derivation; morning distinction still needs qualification'),
('10','19b:7','anonymous dialogue continuation','If so, morning sanctification too should not invalidate.','queried',['Overbroad inference from dressing verse'],'Critical follow-up after pleased reaction and rebuke'),
('11','19b:8','Hezekiah','What is indispensable for his descendants is indispensable for him.','asserted',['High priest compared with ordinary descendants; Exodus30:21'],'Morning sanctification included'),
('12','19b:8','Hezekiah','What is not indispensable for his descendants is not indispensable for him.','asserted',['High-priest-specific intervening requirements'],'Limits effect of dressing verse'),
('13','19b:9','Rabbi Yonatan','What is indispensable for his sons is indispensable for him.','asserted',['Moses Aaron and sons washing; Exodus40:31'],'Alternative derivation of shared requirement'),
('14','19b:9','Rabbi Yonatan','What is not indispensable for his sons is not indispensable for him.','asserted',['High-priest-specific intervening acts'],'Alternative negative derivation'),
('15','19b:10','anonymous','Why does Rabbi Yonatan not use Hezekiah verse?','queried',['Competing textual sources'],'Question'),
('16','19b:10','Rabbi Yonatan reconstructed reply','That verse is written for succeeding generations.','asserted',['Exodus30:21; generations'],'Alternative use of verse'),
('17','19b:11','anonymous','Why does the other authority not use the Moses Aaron and sons verse?','queried',['Hezekiah alternative textual use'],'Question'),
('18','19b:11','Rabbi Yosei son of Rabbi Hanina','A laver holding insufficient water to sanctify four priests may not be used for sanctification.','asserted',['Laver capacity less than four priests'],'Derived from Moses Aaron and sons; alternate use for Hezekiah'),
('19','19b:12','first washing baraita view','Place the right hand over the right foot for sanctification.','asserted',['Method of washing right limbs'],'First method'),
('20','19b:12','first washing baraita view','Place the left hand over the left foot for sanctification.','asserted',['Method of washing left limbs'],'First method'),
('21','19b:12','Rabbi Yosei son of Rabbi Yehuda','Place the two hands one over the other above the two feet one over the other and sanctify.','asserted',['All limbs stacked together'],'Alternative method'),
('22','19b:12','other sages','That proposal is excessive and cannot be done.','asserted',['Objection to stacked-limbs method'],'Practical objection'),
('23','19b:13','anonymous','Their objection is well made.','asserted',['Practical difficulty of stacked limbs'],'Supports practical objection'),
('24','19b:13','Rav Yosef','Another person assists him.','asserted',['Stacked-limbs method with support from another'],'Reply'),
('25','19b:14','anonymous','What is the difference between the views?','queried',['Washing methods after assistance explanation'],'Question on dispute'),
('26','19b:14','Abaye','They differ about standing with external support.','asserted',['Supported standing during sanctification'],'Identifies underlying dispute'),
('27','19b:15','Rav Sama son of Rav Ashi','Why not sit and sanctify?','queried',['Seated sanctification'],'Question to Ravina'),
('28','19b:15','anonymous reply','Scripture says to serve, and service is performed standing.','asserted',['Exodus30:20; sanctification associated with service'],'Excludes seated method')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Missing atonement, morning and intervening sanctification, washing method',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode!='queried':
  holder=[] if v.startswith(('anonymous','quoted','first')) else (['Rabbi Yonatan'] if k=='16' else [v])
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=prefix+'qmethod' if k in ['19','20','21'] else None,conditions=conds,local_status=status),['c'+k])
rec('ureaction','utterances',['19b:7'],dict(textual_voice='dialogue narration',discourse_role='pleased_reaction_and_rebuke',composition='composite'),unc=['Narrative pronouns not assigned beyond locally secure speaker context.'])
rec('qmethod','questions',['19b:12'],dict(formulation='How should hands and feet be positioned for sanctification?',question_origin='editorial_reconstruction',conditions=['Priestly sanctification'],answer_set_status='partial'),origin='editorial_inference')
for k,refs,surface,cands,links in [('huna',['19b:2'],'Rav Huna',['Rav Huna'],['c2']),('assi',['19b:5'],'Rav Assi to Rabbi Yohanan',['Rav Assi'],['c8']),('yohanan',['19b:6'],'He replied',['Rabbi Yohanan'],['c9']),('hezekiah',['19b:8'],'Hezekiah',['Hezekiah'],['c11','c12']),('yonatan',['19b:9','19b:10'],'Rabbi Yonatan',['Rabbi Yonatan'],['c13','c14','c16']),('hanina',['19b:11'],'Rabbi Yosei son of Rabbi Hanina',['Rabbi Yosei son of Rabbi Hanina'],['c18']),('yehuda',['19b:12'],'Rabbi Yosei son of Rabbi Yehuda',['Rabbi Yosei son of Rabbi Yehuda'],['c21']),('yosef',['19b:13'],'Rav Yosef',['Rav Yosef'],['c24']),('abaye',['19b:14'],'Abaye',['Abaye'],['c26']),('sama',['19b:15'],'Rav Sama son of Rav Ashi to Ravina',['Rav Sama son of Rav Ashi'],['c27'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role='speaker',candidates=cands,scope='Explicit local speaker; similar names kept distinct',transmission_chain=[]),links)
for a,b,rel in [('2','1','answer'),('8','4','objection'),('8','5','objection'),('9','8','answer'),('10','9','objection'),('11','10','answer'),('12','9','qualification'),('13','10','answer'),('14','9','qualification'),('16','15','answer'),('18','17','answer'),('22','21','objection'),('23','22','support'),('24','23','answer'),('26','25','answer'),('28','27','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
for k in ['19','20','21']:rec('emethod'+k,'edges',['19b:12'],dict(source_id=prefix+'c'+k,target_id=prefix+'qmethod',relation='answer',explicitness='editorial_reconstruction'),['c'+k,'qmethod'],origin='editorial_inference')
refs=['19b:'+str(i) for i in range(2,16)]
for key,part,title in [('1',refs[:2],'Sources for missing atonement and unwashed service'),('2',refs[2:10],'Morning versus intervening high-priest sanctification'),('3',refs[10:],'Washing posture and supported standing dispute')]:rec('s'+key,'structure',part,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through19b15 and new overnight dispute19b16 onward. Preserve morning/intervening distinction, individual omitted acts, two derivation authorities, four-priest laver capacity, standing-method dispute and names distinct from Rav.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_19b2_19b15.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch22.json',r.encoded(res));print(res)
