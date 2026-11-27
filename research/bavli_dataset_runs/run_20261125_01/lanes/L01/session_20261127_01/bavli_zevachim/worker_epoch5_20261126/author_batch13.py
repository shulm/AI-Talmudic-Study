import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b13.'
assert r.read(job/'CURRENT.json')['snapshot_sha256']=='4ea1a608b6faf5c89db99866737bbab7b3c56824537892fe96d885e688941636'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
# Each tuple is a manually read source proposition; serialization below does not infer semantics.
D=[
('1','14b:14','anonymous','Does carrying without walking count as carrying?','queried',['No walking'],'Open inquiry'),
('2','14b:15','anonymous','The seated/left-hand disqualification suggests comparable standing performance is valid.','hypothetical',['Standing analogous to seated; no walking inferred'],'Proof attempt'),
('3','14b:16','anonymous','The seated case may involve sliding and the standing case slight movement.','conditional',['Seated sliding; standing moving slightly'],'Rejects proof of no-walking validity'),
('4','14b:17','quoted source','An Israelite slaughters, a priest receives, and passes to his fellow and onward.','asserted',['Successive passing of blood'],'Proof text'),
('5','14b:18','anonymous','The participants may each move a little.','conditional',['Successive passing; slight movement'],'Defeats proof'),
('6','14b:18','anonymous','Many participants display the glory of the King.','asserted',['Purpose of successive passing; Proverbs14:28'],'Explains cited practice'),
('7','14b:19','quoted source','Blood received by a fit person and given to an unfit person is to be returned to the fit person.','asserted',['Fit reception then transfer to unfit person'],'Proof text'),
('8','14b:20','anonymous','Read the rule as the fit person returning and receiving it.','asserted',['Fit person walks back to receive'],'Alternative interpretation'),
('9','14b:21','Rabbi Yohanan','Carrying without walking does not count as carrying.','asserted',['Without walking'],'Ulla reports Rabbi Yohanan'),
('10','15a:1','anonymous','Can the deficient carrying be repaired?','queried',['Carrying without walking'],'New inquiry'),
('11','15a:2,15a:3','anonymous','Return from the unfit recipient appears to show repair is possible, even if the fit person returns to receive.','hypothetical',['Initial fit reception; transfer to unfit recipient'],'Attempted proof of repair'),
('12','15a:4','anonymous','The unfit recipient stands outside, not inside.','conditional',['Transfer outward does not supply required inward carrying'],'Defeats repair inference'),
('13','15a:5','Rabbi Yohanan','Carrying without walking is invalid.','rejected',['Without walking'],'Ulla report explicitly refuted at15a9'),
('14','15a:5','anonymous','This invalidity implies that repair is impossible.','rejected',['Inference from Ulla report of invalidity'],'Explicit refutation follows'),
('15','15a:6','Rav Nahman quoting source','Blood spilled from the vessel onto the floor and gathered is valid.','asserted',['Previously received in vessel; spilled then gathered'],'Objection addressed to Ulla'),
('16','15a:7','anonymous','The valid spill may have flowed outward.','hypothetical',['Outward rather than inward blood flow'],'Attempted limitation'),
('17','15a:8','anonymous','Why would outward flow exclude any inward flow?','queried',['Spill direction'],'Objection'),
('18','15a:8','anonymous','A slope can account for exclusively outward flow.','conditional',['Sloped floor'],'Alternative reply'),
('19','15a:8','anonymous','A depression can account for the spill configuration.','conditional',['Depression in floor'],'Alternative reply'),
('20','15a:8','anonymous','Thick blood can account for the spill configuration.','conditional',['Thick blood'],'Alternative reply'),
('21','15a:9','anonymous','It is implausible that the teacher intended only all these special configurations.','asserted',['Proposed restrictions on valid spill'],'Objection'),
('22','15a:9','anonymous','The later invalid-spill teaching should instead have distinguished outward from inward flow within this case; the report is refuted.','asserted',['Contrast with blood spilled directly onto floor'],'Second objection and explicit refutation'),
('23','15a:10','initial anonymous report','All agree that major carrying without walking is invalid.','rejected',['Major carrying; initial account'],'Corrected at15a14–15'),
('24','15a:10','initial anonymous report','Rabbi Shimon and the sages dispute minor carrying.','rejected',['Minor carrying; initial account'],'Corrected at15a14–15'),
('25','15a:11','western scholars','How can invalidating intent in bird sin-offering occur according to Rabbi Shimon?','queried',['Intent before emergence does nothing; after emergence act apparently done'],'Initial account of western laughter'),
('26','15a:11','western argument','Intent before blood emerges has no effect.','asserted',['Bird sin-offering; before emergence'],'Premise in objection'),
('27','15a:11','western argument','After emergence the commandment appears completed.','challenged',['Bird sin-offering; after emergence'],'Challenged by travel interval'),
('28','15a:12','anonymous','The intent may occur between blood leaving and reaching the altar.','conditional',['Flight interval before altar arrival'],'Answers apparent difficulty'),
('29','15a:13','Rabbi Yirmeya','What if the sprinkler hand is severed before blood reaches the altar airspace?','queried',['Sprinkling begun; hand severed before blood reaches altar'],'Question to Rabbi Zeira'),
('30','15a:13','Rabbi Zeira','That sprinkling is invalid, since sprinkling and placing are both required.','asserted',['Hand severed before blood reaches altar airspace'],'Reply includes bracketed invalidity/reason wording'),
('31','15a:14','Rav Pappa and Rav Huna son of Rav Yehoshua','The laughter concerns the claim of agreement about major carrying, where their dispute actually occurs.','asserted',['Report from school; reinterpretation of western laughter'],'Corrects initial report'),
('32','15a:15','corrected anonymous report','All agree minor carrying does not invalidate.','asserted',['Minor carrying'],'Corrected account; preserve source wording and local context'),
('33','15a:15','corrected anonymous report','Rabbi Shimon and the sages dispute major carrying.','asserted',['Major carrying'],'Corrected location of dispute'),
('34','15a:16','unassigned first view','The offering is valid because repair is possible.','asserted',['Nonpriest carried; priest returned blood and carried again'],'One of sons of Rabbi Hiyya/Rabbi Yannai, unresolved assignment'),
('35','15a:16','unassigned second view','The offering is invalid because repair is impossible.','asserted',['Nonpriest carried; priest returned blood and carried again'],'Other of sons of Rabbi Hiyya/Rabbi Yannai, unresolved assignment'),
('36','15a:17','Rav Shimi bar Ashi','For the earlier validating view the reversed case is invalid.','asserted',['Priest carried and returned blood; nonpriest carried again'],'Conditional report about unnamed view'),
('37','15a:17','Rav Shimi bar Ashi','For the earlier invalidating view the reversed case is valid.','challenged',['Priest carried and returned blood; nonpriest carried again'],'Opposed by Rava'),
('38','15a:18,15b:1','Rava','Even the earlier invalidating view invalidates the reversed case because the blood needs to be brought.','asserted',['Priest carried and returned blood; nonpriest carried again'],'Explicit opposition to Rav Shimi'),
('39','15b:2','Rav Yirmeya of Difti','Whether the blood now needs to be brought is disputed by Rabbi Eliezer and the sages.','challenged',['Repeated inward carrying after return outward'],'Reported by Rav Yirmeya to Rav Ashi; challenged below'),
('40','15b:3','Rabbi Eliezer','Intent during necessary carrying invalidates.','asserted',['Place where carrying is required'],'Quoted Mishnah'),
('41','15b:3','Rabbi Eliezer','Intent during unnecessary carrying does not invalidate.','asserted',['Place where carrying is unnecessary'],'Quoted Mishnah'),
('42','15b:4','Rava','All agree reception outside and bringing inside is necessary carrying.','asserted',['Reception outside; inward carrying'],'Reported explanation'),
('43','15b:4','Rava','All agree reception inside and bringing outside is unnecessary carrying.','asserted',['Reception inside; outward carrying'],'Reported explanation'),
('44','15b:5','proposed anonymous exposition','After bringing inside and returning outside one view regards bringing it back as necessary.','challenged',['Inward carrying then outward return'],'Unassigned view in proposed dispute; not resolved by name order'),
('45','15b:5','proposed anonymous exposition','The other view does not classify that return as carrying needed for service.','challenged',['Inward carrying then outward return'],'Proposed dispute challenged by baraita'),
('46','15b:6','Abaye quoting baraita','Bringing blood back inward after taking it outward is necessary carrying.','asserted',['Received inside; taken outside; then returned inside'],'Explicit objection to proposed dispute'),
('47','15b:7','anonymous respondent','If that is taught, it is taught.','asserted',['Abaye quoted baraita'],'Concession; respondent not named in segment')]
for k,rs,v,prop,mode,conds,status in D:
 refs=rs.split(',');rec('u'+k,'utterances',refs,dict(textual_voice=v,discourse_role='question' if mode=='queried' else 'argument_or_rule',composition='atomic'))
 rec('c'+k,'claims',refs,dict(proposition=prop,conditions=conds,scope='Nonwalking carrying, repair and necessary repeated carrying',assertion_mode=mode),['u'+k])
 if mode=='queried':rec('q'+k,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=conds,answer_set_status='partial'),['u'+k])
 if mode not in ['queried','hypothetical']:
  holder=[] if v in ['anonymous','quoted source','initial anonymous report','corrected anonymous report','western argument','proposed anonymous exposition','anonymous respondent'] else [v]
  unc=[]
  if k in ['34','35']:holder=['sons of Rabbi Hiyya','Rabbi Yannai'];unc=['View attribution remains unassigned; candidates are alternatives, not joint holders.']
  rec('p'+k,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+k,question_id=None,conditions=conds,local_status=status),['c'+k],unc)
rec('uchapter','utterances',['15b:8'],dict(textual_voice='editorial chapter marker',discourse_role='chapter_closure',composition='atomic'),origin='literal')
for k,refs,surface,cands,chain,links in [
('ulla1',['14b:21'],'Ulla said Rabbi Yohanan',['Ulla'],['Ulla','Rabbi Yohanan'],['c9']),('ulla2',['15a:5'],'Ulla said Rabbi Yohanan',['Ulla'],['Ulla','Rabbi Yohanan'],['c13']),('nahman',['15a:6'],'Rav Nahman objected to Ulla',['Rav Nahman'],[],['c15']),('west',['15a:11'],'They laughed in the West',['western scholars'],[],['c25']),('yirmeya',['15a:13'],'Rabbi Yirmeya asked Rabbi Zeira',['Rabbi Yirmeya'],[],['c29']),('zeira',['15a:13'],'and he said to him',['Rabbi Zeira'],[],['c30']),('school',['15a:14'],'Rav Pappa and Rav Huna son of Rav Yehoshua',['Rav Pappa','Rav Huna son of Rav Yehoshua'],[],['c31']),('unnamed',['15a:16'],'one said and one said',['sons of Rabbi Hiyya','Rabbi Yannai'],[],['c34','c35']),('shimi',['15a:17'],'Rav Shimi bar Ashi',['Rav Shimi bar Ashi'],[],['c36','c37']),('rava',['15a:18','15b:1'],'Rava',['Rava'],[],['c38']),('difti',['15b:2'],'Rav Yirmeya said to Rav Ashi: thus said Rav Yirmeya of Difti',['Rav Yirmeya'],['Rav Yirmeya','Rav Yirmeya of Difti'],['c39']),('eliezer',['15b:3'],'Rabbi Eliezer',['Rabbi Eliezer'],[],['c40','c41']),('rava2',['15b:4'],'Rava',['Rava'],[],['c42','c43']),('abaye',['15b:6'],'Abaye objected',['Abaye'],[],['c46'])]:
 rec('a'+k,'attributions',refs,dict(surface=surface,role='transmitter' if chain else 'speaker',candidates=cands,scope='Local explicit report; alternatives unassigned for one-said passage',transmission_chain=chain),links,['Bracketed wording retained in quoted source.'] if k=='zeira' else (['No named assignment of the opposing views.'] if k=='unnamed' else []))
for a,b,rel in [('2','1','answer'),('3','2','objection'),('4','1','support'),('5','4','qualification'),('6','5','support'),('7','1','support'),('8','7','qualification'),('9','1','answer'),('11','10','answer'),('12','11','objection'),('14','13','support'),('14','10','answer'),('15','13','objection'),('16','15','qualification'),('17','16','objection'),('18','17','answer'),('19','17','answer'),('20','17','answer'),('21','16','objection'),('22','13','objection'),('22','14','objection'),('25','24','objection'),('26','25','support'),('27','25','support'),('28','25','answer'),('30','29','answer'),('30','28','support'),('31','23','correction'),('31','24','correction'),('32','24','correction'),('33','23','correction'),('34','10','answer'),('35','10','answer'),('38','37','objection'),('39','38','objection'),('40','39','support'),('41','39','support'),('44','39','support'),('45','39','support'),('46','45','objection'),('46','39','objection'),('47','46','local_resolution')]:
 refs=next(x[1].split(',') for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['14b:'+str(i) for i in range(14,22)]+['15a:'+str(i) for i in range(1,19)]+['15b:'+str(i) for i in range(1,9)]
rec('s1','structure',refs,dict(title='Nonwalking carrying and repair; corrected major/minor account; repeated carrying and chapter closure',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual omission reread through chapter closure15b8 and next Mishnah15b9–10; preserve explicit refutation15a9, corrected major/minor account, bracketed Zeira reply, unassigned one-said views, repeated-carry conditions and final concession.' if layer=='reconciliation' else 'Manual source pass; '+('supported records listed.' if ids else 'No separate '+layer+' finding; chapter marker remains structural discourse where applicable.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_14b14_15b8.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch13.json',r.encoded(res));print(res)
