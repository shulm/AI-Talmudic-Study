import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b16.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='9640eec7451e88a388e827376670831ab34a4a2e2cf6773f9ce8cbf569b6c41e'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','16b:13','Rava','The onen disqualification applies to an individual offering.','asserted',['Individual offering; ordinary priest onen'],'First half of Rava distinction'),
('2','16b:13','Rava','An onen effects acceptance for a communal offering.','rejected',['Communal offering; ordinary priest onen'],'A-fortiori claim undermined by reciprocal inferences;17a1 leaves cases in place'),
('3','16b:14','Rava argument','Impurity is not permitted for a high priest individual offering.','asserted',['Impure high priest; individual offering'],'Premise'),
('4','16b:14','Rava argument','Impurity is permitted for an ordinary priest communal offering.','asserted',['Impure ordinary priest; communal offering'],'Premise'),
('5','16b:14','Rava argument','Mourning is permitted for a high priest individual offering.','asserted',['Onen high priest; individual offering'],'Premise'),
('6','16b:14','Rava argument','If impurity with the stricter high-priest rule is permitted communally, mourning with the high-priest exception should be permitted communally.','rejected',['A-fortiori from impurity to mourning'],'Support for Rava challenged by reciprocal proofs'),
('7','16b:15','Rava bar Ahilai','The same reasoning could prohibit an onen high priest individual offering, from impurity and the ordinary priest communal restrictions.','hypothetical',['Reverse a-fortiori; onen high priest individual offering'],'Counter-inference, not adopted ruling'),
('8','16b:16','continuing objection','One could instead permit an impure high priest individual offering by comparison with mourning.','hypothetical',['Reverse a-fortiori; impure high priest individual offering'],'Counter-inference, not adopted ruling'),
('9','16b:17','continuing objection','One could instead prohibit an impure ordinary priest communal offering by comparison with mourning.','hypothetical',['Reverse a-fortiori; impure ordinary priest communal offering'],'Counter-inference, not adopted ruling'),
('10','17a:1','anonymous','Because objections run in both directions, each case remains in its existing place.','asserted',['Reciprocal inconsistent a-fortiori derivations'],'Concluding rejection of altering the established cases'),
('11','17a:2','anonymous','What is the source for invalidity of service by one immersed today before sunset?','queried',['Tevul yom service'],'New derivation'),
('12','17a:2,17a:3','Rabbi Simai','Be holy and do not profane is assigned to a tevul yom, since the impure case is already derived from separation.','asserted',['Leviticus21:6; Leviticus22:2 already covers impure'],'Derivation by surplus wording'),
('13','17a:4','anonymous','Why not apply the verse to one making a forbidden bald patch?','queried',['Forbidden bald patch; alternative verse application'],'Objection'),
('14','17a:4','anonymous','Why not apply the verse to one destroying the beard corner?','queried',['Forbidden destruction of beard corner'],'Distinct alternative verse application'),
('15','17a:5','anonymous','How is the death liability for a tevul yom serving derived?','queried',['Tevul yom service; death liability'],'Question introducing shared profanation wording'),
('16','17a:5','anonymous','Profanation is learned from profanation in terumah.','asserted',['Shared hillul wording; service and terumah'],'Derivation of service liability'),
('17','17a:5','anonymous','A person disqualified for terumah profanes service.','asserted',['Disqualified for terumah'],'Distinguishes tevul yom'),
('18','17a:5','anonymous','A person not disqualified for terumah does not profane service by this derivation.','asserted',['Not disqualified for terumah; proposed baldness/beard cases'],'Answers alternative applications'),
('19','17a:6','Rabbah','Why separately state impure, tevul yom and one lacking atonement?','queried',['Three service-disqualified statuses'],'Redundancy inquiry'),
('20','17a:7','anonymous','The impure case alone cannot establish the others because it transmits impurity.','asserted',['Single-source derivation from impure'],'Need for separate wording'),
('21','17a:7','anonymous','One lacking atonement cannot be learned from a tevul yom because the latter is disqualified for terumah.','asserted',['Single-source derivation from tevul yom'],'Need for separate wording'),
('22','17a:7','anonymous','A tevul yom cannot be learned from one lacking atonement because the latter still lacks an act.','asserted',['Single-source derivation from lacking atonement'],'Need for separate wording'),
('23','17a:8','anonymous','If no case follows from one other, derive one from the other two.','queried',['Two-source derivation among three statuses'],'Further redundancy inquiry'),
('24','17a:9','anonymous','Omitting the lacking-atonement case fails because both other cases are disqualified for terumah.','asserted',['Impure and tevul yom as proof pair'],'Objection to first pair'),
('25','17a:10','anonymous','Why not omit the tevul-yom case and derive it from the other two?','queried',['Impure and lacking atonement as proof pair'],'Second pair proposed'),
('26','17a:10','anonymous','Their lacking an act does not settle the objection because their impurity has nevertheless diminished.','challenged',['Proposed pair; purported diminished impurity'],'Premise corrected by ensuing explanation'),
('27','17b:1','anonymous explanation','The position treats a zav lacking atonement as a zav.','asserted',['Zav lacking atonement; explanation of need for separate tevul-yom verse'],'Answers diminished-impurity premise'),
('28','17b:2','anonymous','Is whether a zav lacking atonement is like a zav a tannaitic dispute?','queried',['Proposed reading of red-cow burning baraita'],'Rejected explanation follows'),
('29','17b:2','anonymous baraita','Red-cow burning by an onen is valid.','asserted',['Red cow; onen burner'],'First authority'),
('30','17b:2','anonymous baraita','Red-cow burning by one lacking atonement is valid.','asserted',['Red cow; burner lacking atonement'],'Disputed outcome'),
('31','17b:2','Yosef the Babylonian','Red-cow burning by an onen is valid.','asserted',['Red cow; onen burner'],'Agreement with first authority'),
('32','17b:2','Yosef the Babylonian','Red-cow burning by one lacking atonement is invalid.','asserted',['Red cow; burner lacking atonement'],'Disputed outcome'),
('33','17b:2','proposed anonymous explanation','One side regards a zav lacking atonement as a zav.','rejected',['Proposed basis of baraita dispute'],'Named allocation not made by order'),
('34','17b:2','proposed anonymous explanation','The other side does not regard a zav lacking atonement as a zav.','rejected',['Proposed basis of baraita dispute'],'Rejected at17b3'),
('35','17b:3','anonymous','All agree a zav lacking atonement is like a zav.','asserted',['Alternative explanation of baraita'],'Rejects proposed dispute basis'),
('36','17b:3','anonymous','The pure person shall sprinkle implies a person with some impurity and teaches that a tevul yom is valid for the red cow.','asserted',['Numbers19:19; tevul yom'],'Shared scriptural exception'),
('37','17b:4','anonymous first interpretation','One side extends the verse exception to impurity throughout the Torah.','asserted',['Breadth of red-cow exception'],'Unassigned named speaker; explains permissive breadth'),
('38','17b:4','anonymous second interpretation','The other side limits it to impurity in this passage.','asserted',['Corpse impurity context of red-cow passage'],'Unassigned named speaker; restrictive breadth'),
('39','17b:5','restrictive interpretation','An onen is permitted by an a-fortiori inference from a corpse-impurity tevul yom.','asserted',['Red cow; lighter onen status'],'Restricted reading nevertheless permits lighter cases'),
('40','17b:5','restrictive interpretation','A tevul yom from creeping-animal impurity is permitted by that a-fortiori inference.','asserted',['Red cow; lighter external creeping-animal impurity'],'Distinct lighter case'),
('41','17b:5','restrictive interpretation','A zav lacking atonement is not permitted because bodily-origin impurity is more severe.','asserted',['Red cow; bodily-origin zav impurity; missing atonement'],'Restricted reading excludes more severe case')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'argument_or_rule',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Onen communal exception rejected; tevul-yom and lacking-atonement derivations',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v.startswith(('anonymous','proposed','restrictive','continuing')) else (['Rava'] if v=='Rava argument' else [v])
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=prefix+'qredcow' if k in ['30','32'] else None,conditions=conds,local_status=status),['c'+k])
rec('umnemonic','utterances',['16b:18'],dict(textual_voice='editorial mnemonic',discourse_role='mnemonic',composition='atomic'),origin='literal')
rec('qredcow','questions',['17b:2'],dict(formulation='Is red-cow burning by one lacking atonement valid?',question_origin='editorial_reconstruction',conditions=['Red cow; missing atonement'],answer_set_status='partial'),origin='editorial_inference')
for k,refs,surface,cands,links in [('rava',['16b:13'],'Rava',['Rava'],['c1','c2']),('ahilai',['16b:15'],'Rava bar Ahilai',['Rava bar Ahilai'],['c7']),('simai',['17a:2'],'Rabbi Simai',['Rabbi Simai'],['c12']),('rabbah',['17a:6'],'Rabbah',['Rabbah'],['c19']),('yosef',['17b:2'],'Yosef the Babylonian',['Yosef the Babylonian'],['c31','c32'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role='speaker',candidates=cands,scope='Named source speaker; Rava and Rava bar Ahilai distinguished',transmission_chain=[]),links)
for a,b,rel in [('6','2','support'),('3','6','support'),('4','6','support'),('5','6','support'),('7','6','objection'),('8','6','objection'),('9','6','objection'),('10','2','correction'),('10','7','local_resolution'),('10','8','local_resolution'),('10','9','local_resolution'),('12','11','answer'),('13','12','objection'),('14','12','objection'),('16','15','answer'),('17','12','support'),('18','13','answer'),('18','14','answer'),('20','19','answer'),('21','19','answer'),('22','19','answer'),('23','19','objection'),('24','23','answer'),('25','24','objection'),('26','25','support'),('27','26','correction'),('28','27','objection'),('33','28','answer'),('34','28','answer'),('35','33','correction'),('35','34','correction'),('36','35','support'),('37','36','qualification'),('38','36','qualification'),('39','38','support'),('40','38','support'),('41','38','support')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
for k in ['30','32']:rec('eredcow'+k,'edges',['17b:2'],dict(source_id=prefix+'c'+k,target_id=prefix+'qredcow',relation='answer',explicitness='editorial_reconstruction'),['c'+k,'qredcow'],origin='editorial_inference')
refs=['16b:'+str(i) for i in range(13,19)]+['17a:'+str(i) for i in range(1,11)]+['17b:'+str(i) for i in range(1,6)]
rec('s1','structure',refs[:7],dict(title='Reciprocal a-fortiori arguments defeat proposed communal onen exception',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[7:],dict(title='Tevul-yom source and three-status derivation; red-cow exception interpretations',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through17b5 and new missing-garments inquiry17b6. Preserve reciprocal arguments as hypothetical, Rava correction, mnemonic, separate red-cow outcomes and rejected proposed tannaitic basis; no name-order allocation.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding; mnemonic has no legal assertion.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_16b13_17b5.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch16.json',r.encoded(res));print(res)
