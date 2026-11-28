import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b24.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='1fad6fac33a1e1641c78fc904d5c16c674d49ce5b5d6c5baaa89db652e62d7fb'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','20a:2','Ilfa reported by Rabbi Yohanan','For the view that overnight passage does not expire hand/foot sanctification, does it invalidate laver water?','queried',['No expiration of sanctification view; laver water overnight'],'Unresolved alternatives in initial report'),
('2','20a:2','inquiry alternative','Since the water is for sanctification that does not expire overnight, perhaps the water likewise does not expire.','hypothetical',['Functional comparison with hand/foot sanctification'],'Unadopted alternative'),
('3','20a:2','inquiry alternative','Since the water is sanctified in a service vessel, perhaps it becomes invalid overnight.','hypothetical',['Laver as service vessel'],'Unadopted alternative'),
('4','20a:3','Ilfa reported through Rabbi Yohanan','The dispute about sanctification is also the dispute about the water.','challenged',['Overnight water validity; purported later resolution'],'Ravin chain report challenged by Yitzhak bar Bisna'),
('5','20a:4','Rabbi Yitzhak bar Bisna','Master, do you say this? The received report differs.','queried',['Challenge to purported resolution'],'Addresses report recipient without assigning unnamed master'),
('6','20a:4','Rabbi Yohanan via Rabbi Assi','A laver not submerged before evening may be used for night service sanctification.','asserted',['Laver not submerged before evening; night service'],'Corrective report; bracketed attribution in name of Ilfa'),
('7','20a:4','Rabbi Yohanan via Rabbi Assi','One does not sanctify from it the next day.','unresolved',['Same laver; next day'],'Ambiguous: no need or water invalidity, not categorical invalidity'),
('8','20a:5','reporting interlocutor','Does not sanctify next day mean sanctification is unnecessary or that water expired overnight?','queried',['Ambiguous corrective report'],'It was not resolved for us; contests claim of settled resolution'),
('9','20a:5','reporting interlocutor','The ambiguity was not resolved for us, yet you resolve it.','asserted',['Status of reported inquiry'],'Explicit challenge to resolution report'),
('10','20a:6','quoted source','Ben Katin made twelve spouts for the laver.','asserted',['Laver equipment'],'Historical source detail'),
('11','20a:6','quoted source','He also made a mechanism to prevent its water becoming invalid overnight.','asserted',['Laver mechanism preserving water'],'Proof source'),
('12','20a:6','anonymous','Is this not Rabbi Elazar son of Rabbi Shimon teaching?','hypothetical',['Attribution of mechanism teaching'],'Attempted proof that even no-expiration view invalidates water'),
('13','20a:6','anonymous','No; it may be Rabbi teaching.','conditional',['Mechanism teaching assigned to Rabbi'],'Defeats proof'),
('14','20a:7','anonymous','Since the beginning is Rabbi Elazar son of Rabbi Shimon, the ending should be his too.','hypothetical',['Shared authorship of opening and ending'],'Attribution argument challenged'),
('15','20a:8','quoted source','The high-priest bull stood between porch and altar with head south and face west; the priest stood east facing west.','asserted',['Bull arrangement in quoted procedure'],'Spatial source offered for attribution inference'),
('16','20a:8','anonymous','Who includes between porch and altar as north? Rabbi Elazar son of Rabbi Shimon.','challenged',['Authorship inference from bull location'],'Rabbi also includes it, as continuation explains'),
('17','20a:9','Rabbi Yosei son of Rabbi Yehuda','North runs from the northern altar wall to the northern courtyard wall opposite the whole altar.','asserted',['Definition of north slaughter area'],'Base northern zone'),
('18','20a:9','Rabbi Elazar son of Rabbi Shimon','North additionally includes between porch and altar.','asserted',['Expanded northern zone'],'Addition to base zone'),
('19','20a:9','Rabbi','North additionally includes the priests walking area.','asserted',['Further expanded northern zone; priests area'],'Additional area'),
('20','20a:9','Rabbi','North additionally includes the Israelites walking area.','asserted',['Further expanded northern zone; Israelites area'],'Distinct additional area'),
('21','20a:9','all authorities','The area from the knife chambers inward is invalid.','asserted',['From halifot inward'],'Shared exclusion'),
('22','20a:10','anonymous','Rabbi adds to Rabbi Yosei son of Rabbi Yehuda and surely also includes Rabbi Elazar son of Rabbi Shimon addition.','asserted',['Nested north-area opinions'],'Refutes exclusive attribution from between-porch-and-altar location'),
('23','20a:11','anonymous','If it were Rabbi, why not place the bull in the priests or Israelites walking areas?','queried',['Procedure location despite broader Rabbi valid zone'],'Reformulated attribution argument'),
('24','20a:12','anonymous','Even for Rabbi Elazar son of Rabbi Shimon, why not put it in the basic northern altar-to-wall zone?','queried',['Alternative placement within his valid zone'],'Counterquestion'),
('25','20a:12','anonymous','The location is chosen because of the high priest weakness, equally under either view.','asserted',['Convenience for high priest; chosen bull location'],'Defeats exclusive attribution; water inquiry remains unproved')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'report_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Laver water overnight inquiry and disputed attribution of proof text',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='none' if k in ['1','8'] else 'partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v in ['anonymous','quoted source','reporting interlocutor'] else (['Ilfa'] if k=='4' else (['Rabbi Yohanan'] if k in ['6','7'] else [v]))
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k])
for k,refs,surface,cand,chain,links in [('dimi',['20a:2'],'Rav Dimi said Rabbi Yohanan: Ilfa asked',['Rav Dimi'],['Rav Dimi','Rabbi Yohanan','Ilfa'],['c1']),('ravin',['20a:3'],'Ravin said Rabbi Yirmeya said Rabbi Ami said Rabbi Yohanan: Ilfa resolved',['Ravin'],['Ravin','Rabbi Yirmeya','Rabbi Ami','Rabbi Yohanan','Ilfa'],['c4']),('itzhak',['20a:4','20a:5'],'Rabbi Yitzhak bar Bisna',['Rabbi Yitzhak bar Bisna'],[],['c5','c8','c9']),('assi',['20a:4'],'Rabbi Assi said Rabbi Yohanan [in name of Ilfa]',['Rabbi Assi'],['Rabbi Assi','Rabbi Yohanan'],['c6','c7']),('ilfa',['20a:4'],'[in name of Ilfa]',['Ilfa'],[],['c6','c7']),('yosei',['20a:9'],'Rabbi Yosei son of Rabbi Yehuda',['Rabbi Yosei son of Rabbi Yehuda'],[],['c17']),('elazar',['20a:9'],'Rabbi Elazar son of Rabbi Shimon',['Rabbi Elazar son of Rabbi Shimon'],[],['c18']),('rabbi',['20a:9'],'Rabbi',['Rabbi'],[],['c19','c20'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role='transmitter' if chain else 'speaker',candidates=cand,scope='Exact local report chain or named authority; bracketed Ilfa preserved separately',transmission_chain=chain),links,['Bracketed attribution in source.'] if k=='ilfa' else [])
for a,b,rel in [('2','1','unresolved_outcome'),('3','1','unresolved_outcome'),('4','1','answer'),('5','4','objection'),('6','5','answer'),('8','7','qualification'),('9','4','objection'),('11','1','support'),('12','11','qualification'),('13','12','objection'),('14','13','objection'),('15','14','support'),('16','14','support'),('18','16','support'),('22','16','objection'),('23','22','objection'),('24','23','objection'),('25','23','answer'),('25','24','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['20a:'+str(i) for i in range(2,13)]
rec('s1','structure',refs,dict(title='Unresolved laver-water overnight inquiry; contested resolution report and attribution proof',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through20a12 and new ash-removal sanctification20a13 onward. Preserve competing report chains, bracketed Ilfa attribution, no-need versus invalid-water ambiguity, failed authorship inference and separate north-zone additions.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_20a2_20a12.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch24.json',r.encoded(res));print(res)
