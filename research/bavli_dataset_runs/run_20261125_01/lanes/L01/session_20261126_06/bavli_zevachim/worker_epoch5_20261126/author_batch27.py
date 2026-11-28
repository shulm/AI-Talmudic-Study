import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b27.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='9abee83dabb3b6e070e50900f3eaaf2338f245d010ffb0d3a50297b18029767b'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1','21a:6','Rabbi Hiyya bar Yosef','Laver water becomes invalid for permitting rites as those rites become invalid.','asserted',['Water intended for matirin service'],'Rite-specific expiry formulation'),
('2','21a:6','Rabbi Hiyya bar Yosef','Laver water becomes invalid for limbs as limbs become invalid.','asserted',['Water intended for limb service'],'Distinct service category'),
('3','21a:7','Rav Hisda','Even for permitting rites, the water becomes invalid only at dawn, like limbs.','asserted',['Laver water; includes matirin; dawn'],'Opposes earlier category differentiation'),
('4','21a:7','Rabbi Yohanan','Once the laver has been submerged, it is not raised again.','asserted',['Submerged laver'],'Literal report qualified by following day/night and re-submersion discussion'),
('5','21a:8','anonymous','Does that mean it is unfit even for night service?','queried',['Possible interpretation of no raising'],'Challenged by Ilfa report'),
('6','21a:8','Rabbi Yohanan in name of Ilfa','A laver not submerged before evening can be used to sanctify for night service.','asserted',['Not submerged before evening; night service'],'Rabbi Assi transmission'),
('7','21a:8','Rabbi Yohanan in name of Ilfa','The next day one does not sanctify from it.','unresolved',['Same laver next day; meaning examined below'],'Do not flatten ambiguity of no-need vs invalidity'),
('8','21a:9','anonymous','The prohibition on raising concerns day service; for night service the water is fit.','asserted',['Day/night distinction in Yohanan report'],'Answers night-service difficulty'),
('9','21a:10','anonymous','If so, is this not Rabbi Hiyya bar Yosef view?','queried',['Comparison of Yohanan and Hiyya'],'Bracketed if-so retained'),
('10','21b:1','anonymous','They differ about a decree of submersion.','asserted',['First distinction between Yohanan and Hiyya'],'Preserve source terminology without merging later mitzvah distinction'),
('11','21b:2','Rabbi Yohanan quoted','One who sanctified for ash removal need not sanctify the next day because he sanctified at service start.','asserted',['Ash-removal sanctification'],'Repeated source occurrence used as objection'),
('12','21b:3','anonymous','Under Rava the ash-removal statement follows Rabbi Elazar son of Rabbi Shimon while this statement follows Rabbi.','asserted',['Rava attribution account'],'Reconciles two Yohanan reports'),
('13','21b:4','anonymous','Under Abaye both follow Rabbi: why is the laver submerged in one case but not the other?','queried',['Abaye attribution account'],'Apparent contradiction'),
('14','21b:5','anonymous','He raises it and then submerges it again.','asserted',['Laver raised for use then resubmerged'],'Reply'),
('15','21b:6','anonymous','If so, how is next day he does not sanctify understood; why is sanctification unnecessary?','queried',['Next-day report; bracketed no-need wording'],'Preserve bracketed textual qualification'),
('16','21b:7','anonymous','This implies fitness for permitting rites; is it not Rav Hisda view?','queried',['Yohanan water fitness for matirin'],'Comparison following resubmersion interpretation'),
('17','21b:8','anonymous','They differ about the requirement of submersion.','asserted',['Second distinction between Yohanan and Hisda'],'Source says mitzvat shiqua, distinct from earlier decree formulation'),
('18','21b:9','quoted source','They did not see or hear him until hearing the wooden mechanism made by Ben Katin, then said the time for sanctification had arrived.','asserted',['Audible laver mechanism; priests timing cue'],'Source proof'),
('19','21b:9','anonymous','Does that not mean raising it, implying it had been submerged?','hypothetical',['Inference from mechanism sound'],'Proof attempt'),
('20','21b:10','anonymous','No; it is the act of submerging it.','asserted',['Mechanism sound interpreted as lowering'],'Alternative reading'),
('21','21b:10','anonymous','If submerging it, would its sound be heard?','queried',['Audibility of lowering mechanism'],'Objection'),
('22','21b:10','anonymous','It is submerged using the wheel.','asserted',['Wheel-assisted lowering'],'First explanation of audible sound'),
('23','21b:11','alternative version','It is submerged with its fitting so the sound will be heard and they will come.','asserted',['Alternative version of audible submersion mechanism'],'Source term humrata retained in evidence; exact hardware not resolved'),
('24','21b:11','anonymous','But Gevini the crier was present.','queried',['Existing vocal signal'],'Objection to needing mechanical signal'),
('25','21b:11','anonymous','They made two signals, so whoever heard either would come.','asserted',['Mechanical signal plus Gevini crier'],'Resolution')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'rule_or_argument',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Laver water expiration, submersion and audible signals',assertion_mode=mode),['u'+k],['Bracketed wording retained; local reading does not settle broader report ambiguity.'] if k=='15' else (['Precise mechanism component denoted humrata not resolved.'] if k=='23' else []))
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v in ['anonymous','quoted source','alternative version'] else (['Rabbi Yohanan'] if v.startswith('Rabbi Yohanan') else [v])
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=prefix+'qexpiry' if k in ['1','2','3'] else None,conditions=conds,local_status=status),['c'+k])
rec('qexpiry','questions',['21a:6','21a:7'],dict(formulation='When does laver water expire for each service category?',question_origin='editorial_reconstruction',conditions=['Laver water; matirin versus limbs'],answer_set_status='partial'),origin='editorial_inference')
for k,refs,surface,cand,chain,links in [('hiyya',['21a:6'],'Rabbi Hiyya bar Yosef',['Rabbi Hiyya bar Yosef'],[],['c1','c2']),('hisda',['21a:7'],'Rav Hisda',['Rav Hisda'],[],['c3']),('yohanan',['21a:7','21b:2'],'Rabbi Yohanan',['Rabbi Yohanan'],[],['c4','c11']),('assi',['21a:8'],'Rabbi Assi said Rabbi Yohanan in name of Ilfa',['Rabbi Assi'],['Rabbi Assi','Rabbi Yohanan','Ilfa'],['c6','c7'])]:rec('a'+k,'attributions',refs,dict(surface=surface,role='transmitter' if chain else 'speaker',candidates=cand,scope='Local rule or explicit reporting chain',transmission_chain=chain),links)
for a,b,rel in [('5','4','objection'),('6','5','objection'),('8','5','answer'),('8','4','qualification'),('9','8','objection'),('10','9','answer'),('11','4','objection'),('12','11','answer'),('13','12','objection'),('14','13','answer'),('15','14','objection'),('16','8','objection'),('17','16','answer'),('19','18','qualification'),('20','19','objection'),('21','20','objection'),('22','21','answer'),('23','21','answer'),('24','23','objection'),('25','24','answer')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
for k in ['1','2','3']:
 refs=next(x[1].split(',') for x in D if x[0]==k);rec('edispute'+k,'edges',refs,dict(source_id=prefix+'c'+k,target_id=prefix+'qexpiry',relation='answer',explicitness='editorial_reconstruction'),['c'+k,'qexpiry'],origin='editorial_inference')
refs=['21a:'+str(i) for i in range(6,11)]+['21b:'+str(i) for i in range(1,12)]
rec('s1','structure',refs,dict(title='Laver expiration and submersion: competing interpretations and two timing signals',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through21b11 and four-priest-capacity topic21b12 onward. Preserve service-specific expiry, day/night qualifications, Rava/Abaye accounts, decree versus requirement terminology, bracketed ambiguity and alternative mechanism explanation.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' finding in this segment.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_21a6_21b11.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch27.json',r.encoded(res));print(res)
