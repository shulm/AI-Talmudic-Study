import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b26.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='0a7be04e1409e6207513a076ce013ed2f63f21dd4830d271d68491d76fce6491'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','20b:4','anonymous','Does leaving affect sanctification: even if overnight passage does not invalidate, departure might cause distraction, or return remains within his power?','queried',['Whole-body exit; conditional premise that overnight does not invalidate'],'Unresolved alternatives'),
('2','20b:5','quoted source','Sanctified hands and feet that became impure are immersed without new sanctification.','asserted',['Limbs impure after sanctification'],'Proof text; limbs not whole body'),
('3','20b:5','quoted source','If the sanctified limbs went out, they remain sanctified.','asserted',['Hands and feet outside'],'Proof text'),
('4','20b:6','anonymous','The question concerns the entire body leaving, not merely the hands.','asserted',['Whole-body departure versus hands leaving'],'Defeats proof from limbs'),
('5','20b:7','quoted source','One whose hands and feet are unwashed sanctifies from a service vessel inside.','asserted',['Initial sanctification; service vessel; inside'],'Required procedure'),
('6','20b:7','quoted source','Sanctifying from a service vessel outside yields invalid service.','asserted',['Service vessel; outside sanctification'],'Invalid procedure'),
('7','20b:7','quoted source','Sanctifying from an ordinary vessel inside yields invalid service.','asserted',['Ordinary vessel; inside sanctification'],'Invalid procedure'),
('8','20b:7','quoted source','Immersing in cave water yields invalid service.','asserted',['Cave-water immersion instead of prescribed sanctification'],'Invalid procedure'),
('9','20b:7','anonymous','The outside-sanctification case implies inside sanctification followed by exit would be valid.','hypothetical',['Inference about whole-body exit after inside sanctification'],'Proof attempt'),
('10','20b:8','anonymous','Outside sanctification may mean only hands put outside; the corresponding valid inference concerns only hands leaving.','asserted',['Hands outside, not whole body'],'Limits inference; parenthetical continuation retained'),
('11','20b:8','anonymous','The entire body leaving remains a question.','unresolved',['Whole-body exit'],'Explicit preservation of inquiry'),
('12','20b:9','Rav Zevid citing source','Leaving beyond the courtyard wall to remain requires immersion.','asserted',['Exit to remain; interpreted below as relieving oneself'],'Source offered to Rav Pappa'),
('13','20b:9','Rav Zevid citing source','Leaving briefly requires sanctification of hands and feet.','asserted',['Brief exit; interpreted below as urination'],'Distinct requirement'),
('14','20b:10','Rav Pappa reply','The cases concern leaving to defecate or urinate.','asserted',['Bodily functions, not mere exit'],'Restricts offered proof'),
('15','20b:11','anonymous','But those bodily-function rules are explicitly taught separately.','queried',['Redundancy of restricted reading'],'Objection'),
('16','20b:11','quoted source','Anyone who defecates requires immersion.','asserted',['Defecation'],'Explicit rule'),
('17','20b:11','quoted source','Anyone who urinates requires sanctification of hands and feet.','asserted',['Urination'],'Explicit rule'),
('18','20b:11','anonymous','The teacher first states the rule and then explains it.','asserted',['Initial exit formulation explained by bodily functions'],'Answers redundancy objection'),
('19','20b:12','Rabbi Hiyya bar Yosef','For the red cow, sanctify from a service vessel inside and then go out.','asserted',['Red-cow procedure; service vessel inside'],'Proof source'),
('20','20b:12','Rabbi Yohanan','For the red cow, sanctification may be outside.','asserted',['Red-cow procedure; outside location'],'Permissive alternative'),
('21','20b:12','Rabbi Yohanan','For the red cow, sanctification may use an ordinary vessel.','asserted',['Red-cow procedure; ordinary vessel'],'Distinct permission'),
('22','20b:12','Rabbi Yohanan','For the red cow, even an earthenware bowl may be used.','asserted',['Red-cow procedure; earthenware bowl'],'Explicit vessel example'),
('23','20b:13','Rav Pappa','Exit does not invalidate the red-cow procedure because all its acts are outside.','asserted',['Red cow exceptional outside procedure'],'Defeats transfer to ordinary service'),
('24','20b:13','anonymous','If so why is sanctification needed?','queried',['Red-cow exception'],'Question'),
('25','20b:13','anonymous','It must resemble inner service.','asserted',['Red-cow sanctification'],'Reply'),
('26','20b:14','anonymous','Does bodily impurity affect sanctification: even if exit does not invalidate a still-fit person, unfitness might cause distraction, or anticipated renewed fitness preserves attention?','queried',['Whole-body impurity; conditional exit premise'],'Unresolved alternatives'),
('27','20b:15','quoted source','Sanctified limbs made impure are immersed without new sanctification.','asserted',['Hands and feet alone impure'],'Repeated source occurrence preserved'),
('28','20b:16','anonymous','The question concerns the whole body becoming impure, not just hands.','asserted',['Whole-body impurity'],'Limits proof'),
('29','20b:16','anonymous','Would waiting for sunset itself cause distraction?','queried',['Whole-body impurity requiring sunset'],'Challenge to meaningful inquiry'),
('30','20b:16','anonymous','The case is impurity acquired close to sunset.','asserted',['Impurity shortly before sunset'],'Narrows unresolved inquiry'),
('31','20b:17','Rabbi Hiyya bar Yosef','For the red cow, sanctify from a service vessel inside and then go out.','asserted',['Red-cow sanctification; repeated proof occurrence'],'Same teaching, separate source occurrence'),
('32','20b:17','Rabbi Yohanan','Red-cow sanctification may be outside.','asserted',['Red cow; outside location'],'Repeated occurrence'),
('33','20b:17','Rabbi Yohanan','Red-cow sanctification may use an ordinary vessel.','asserted',['Red cow; ordinary vessel'],'Repeated occurrence'),
('34','20b:17','Rabbi Yohanan','Red-cow sanctification may even use an earthenware bowl.','asserted',['Red cow; earthenware bowl'],'Repeated occurrence'),
('35','21a:1','quoted Mishnah','They deliberately made the red-cow-burning priest impure and immersed him to reject the Sadducees requirement of sunset-completed purification.','asserted',['Red-cow priest; deliberate impurity then immersion'],'Practice contrasts Sadducean view'),
('36','21a:1','Sadducees quoted','The red cow must be performed by those whose purification was completed by sunset.','asserted',['Sadducean position; red cow'],'Quoted opposing view, not adopted law'),
('37','21a:1','anonymous','This seems to show impurity does not invalidate the sanctification.','hypothetical',['Inference from red-cow practice to whole-body inquiry'],'Proof attempt'),
('38','21a:2','anonymous','The red cow differs because a tevul yom does not disqualify it.','asserted',['Red cow exceptional eligibility after immersion before sunset'],'Defeats general proof'),
('39','21a:2','anonymous','If so why require sanctification?','queried',['Red-cow impurity exception'],'Question'),
('40','21a:2','anonymous','A resemblance to service is required.','asserted',['Red-cow sanctification'],'Reply with bracketed wording retained'),
('41','21a:3','anonymous','May one sanctify hands and feet inside the laver, or does from it exclude within it?','queried',['Immersion inside laver; Exodus30:19 wording'],'Unresolved alternatives'),
('42','21a:4','Rav Nahman bar Yitzhak','Invalid cave-water immersion seems to imply analogous immersion in laver water is valid.','hypothetical',['Inference from cave-water invalidity'],'Proof attempt'),
('43','21a:5','anonymous','The cave-water case is needed to reject an a-fortiori inference from whole-body immersion to hands and feet.','asserted',['Cave water valid for body immersion but not prescribed sanctification'],'Defeats inference about inside-laver immersion')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Unresolved exit, impurity and inside-laver sanctification inquiries',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='none' if k in ['1','26','41'] else 'partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v in ['anonymous','quoted source','quoted Mishnah'] else (['Rav Pappa'] if k=='14' else (['quoted baraita'] if k in ['12','13'] else [v]))
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,refs,surface,cands,links in [('zevid',['20b:9'],'Rav Zevid to Rav Pappa',['Rav Zevid'],['c12','c13']),('pappa',['20b:10','20b:13'],'Rav Pappa',['Rav Pappa'],['c14','c23']),('hiyya',['20b:12','20b:17'],'Rabbi Hiyya bar Yosef',['Rabbi Hiyya bar Yosef'],['c19','c31']),('yohanan',['20b:12','20b:17'],'Rabbi Yohanan',['Rabbi Yohanan'],['c20','c21','c22','c32','c33','c34']),('sadducees',['21a:1'],'Sadducees',['Sadducees'],['c36']),('nahman',['21a:4'],'Rav Nahman bar Yitzhak',['Rav Nahman bar Yitzhak'],['c42'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role='collective' if k=='sadducees' else 'speaker',candidates=cands,scope='Explicit local source attribution; repeated occurrences retained',transmission_chain=[]),links)
for a,b,rel in [('3','1','support'),('4','3','qualification'),('9','1','answer'),('10','9','objection'),('11','1','unresolved_outcome'),('12','1','support'),('13','1','support'),('14','12','qualification'),('14','13','qualification'),('15','14','objection'),('18','15','answer'),('19','1','support'),('23','19','qualification'),('25','24','answer'),('27','26','support'),('28','27','qualification'),('29','28','objection'),('30','29','answer'),('31','26','support'),('35','36','objection'),('35','37','support'),('37','26','answer'),('38','37','objection'),('40','39','answer'),('42','41','answer'),('43','42','objection')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['20b:'+str(i) for i in range(4,18)]+['21a:'+str(i) for i in range(1,6)]
for key,part,title in [('1',refs[:10],'Whole-body exit inquiry and limited proof cases'),('2',refs[10:16],'Whole-body impurity inquiry and exceptional red-cow procedure'),('3',refs[16:],'Immersion inside laver inquiry and failed cave-water inference')]:rec('s'+key,'structure',part,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through21a5 and new laver-water timing discussion21a6 onward. Preserve unresolved exit/impurity/inside-laver inquiries, limbs versus whole body, near-sunset condition, red-cow exceptions, Sadducean attribution and repeated source occurrences.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_20b4_21a5.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch26.json',r.encoded(res));print(res)
