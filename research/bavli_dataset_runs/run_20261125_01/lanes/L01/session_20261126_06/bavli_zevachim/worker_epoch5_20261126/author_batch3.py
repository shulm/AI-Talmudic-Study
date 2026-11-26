import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b3.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['9b:25'],'רבי יוחנן','disputed_rule','Slaughter for its purpose with intent to sprinkle its blood for another purpose is invalid according to Rabbi Yohanan.','asserted',['Slaughter for own purpose; planned sprinkling for another purpose'],'Named disputed outcome'),
('2',['9b:25'],'ריש לקיש','disputed_rule','The same slaughter with intent for wrong-purpose sprinkling is valid according to Resh Lakish.','asserted',['Slaughter for own purpose; planned sprinkling for another purpose'],'Named disputed outcome'),
('3',['9b:26'],'רבי יוחנן','reason','Intent in one service concerning another service counts, learned from piggul intent.','asserted',['One service with intent concerning a subsequent service'],'Rabbi Yohanan reason'),
('4',['9b:27'],'ריש לקיש','reason','Intent does not transfer across services; the piggul-intent analogy is not accepted.','asserted',['One service with intent concerning a subsequent service'],'Resh Lakish reason'),
('5',['9b:28','10a:1'],'רבי יוחנן quoted parallel','parallel_rule','Slaughtering an animal intending its blood sprinkling and fat burning for idolatry makes the animal forbidden according to Rabbi Yohanan.','asserted',['Slaughter with intended subsequent blood/fat services for idolatry'],'Parallel non-Temple case'),
('6',['10a:1'],'רבי יוחנן quoted parallel','parallel_reason','Intent counts across services and the outside case is learned from the inside sacrificial case.','asserted',['Idolatry outside case learned from Temple intent rules'],'Rabbi Yohanan parallel reasoning'),
('7',['10a:2'],'ריש לקיש quoted parallel','parallel_rule','The animal is permitted according to Resh Lakish in this intended subsequent idolatrous-service case.','asserted',['Slaughter with planned blood/fat services for idolatry'],'Parallel outcome'),
('8',['10a:2'],'ריש לקיש quoted parallel','parallel_reason','Intent does not count across services, and outside is not learned from inside.','asserted',['Idolatry outside case versus Temple case'],'Resh Lakish parallel reasoning'),
('9',['10a:3'],'anonymous','necessity','If only the outside case were taught, Resh Lakish might have agreed to an inference within the Temple rules.','hypothetical',['Only the idolatry case known'],'Counterfactual explaining why both disputes are reported'),
('10',['10a:4'],'anonymous','necessity','If only the Temple case were taught, Rabbi Yohanan might have agreed with Resh Lakish outside; both reports are needed.','hypothetical',['Only the Temple case known'],'Counterfactual, not actual concession'),
('11',['10a:5'],'רב דימי','report','Rav Dimi reports Rav Yirmeya\'s argument supporting Rabbi Yohanan and Rabbi Ila\'s supporting Resh Lakish.','asserted',['Rav Dimi arrival report'],'Transmission attribution distinct from argument holders'),
('12',['10a:6'],'רב ירמיה','a_fortiori','If direct slaughter beyond time is valid but slaughter intending late sprinkling is invalid, then wrong-purpose slaughter, itself invalid, should certainly invalidate when intended for later sprinkling.','asserted',['A fortiori from beyond-time intent to wrong-purpose intent'],'Initial proof for Rabbi Yohanan; challenged next'),
('13',['10a:7'],'רבא בר אהילאי','objection','Beyond-time intent has karet, a distinguishing severity.','challenged',['Beyond-time premise in Rav Yirmeya proof'],'Objection to first a fortiori'),
('14',['10a:8'],'רבא בר אהילאי','reconstruction','Replace beyond-time with beyond-place: direct declaration about slaughter is valid, but intent for later out-of-place sprinkling invalidates; infer wrong-purpose later sprinkling.','asserted',['Beyond-place comparison rather than beyond-time'],'Reconstructed proof, challenged next'),
('15',['10a:9'],'רב אשי','objection','Beyond-place intent applies to all sacrifices, whereas wrong-purpose invalidity applies only to Paschal and sin offerings.','challenged',['Comparison of broad beyond-place invalidity with limited wrong-purpose invalidity'],'Objection to reconstructed proof'),
('16',['10a:10'],'רב אשי','reconstruction','Use change of owner instead: slaughter stated for another is valid but slaughter intending sprinkling for another is invalid; infer invalidity for later wrong-purpose sprinkling where wrong-purpose slaughter itself invalidates.','asserted',['Change-of-owner a fortiori; service distinction'],'Rav Ashi revised proof'),
('17',['10a:11'],'רבי אילא','proof','An explicit sprinkling requirement would be unnecessary if inferred by a combined a fortiori from slaughter and receiving; its separate mention teaches that intent does not transfer across services.','asserted',['Derivation supporting Resh Lakish; separate sprinkling verse'],'Proposed inference for Resh Lakish'),
('18',['10a:12'],'רב פפא','objection','Perhaps the separate verse instead teaches that intent does transfer across services.','hypothetical',['Alternative purpose of explicit sprinkling requirement'],'Objection to Rabbi Ila inference'),
('19',['10a:13'],'anonymous','answer','If so, the verse could be omitted and the result learned from Rav Ashi\'s a fortiori.','asserted',['Assume verse teaches cross-service intent'],'Reply defending redundancy argument'),
('20',['10a:14'],'anonymous other side','objection','The other side distinguishes the compared services as requiring north and existing in inner sin offerings.','challenged',['Response attributed only as the other side; no forced named mapping'],'Distinction against combined inference'),
('21',['10a:15'],'anonymous other side','answer','The response says the present discussion is in any event about peace offerings.','asserted',['Peace-offering context'],'Local reply; unnamed side retained'),
('22',['10a:16'],'רב נחמן','disputed_rule','Rav Nahman invalidates slaughter for its purpose with intent for wrong-purpose sprinkling.','asserted',['Slaughter for own purpose with planned wrong-purpose sprinkling'],'Reported position retained'),
('23',['10a:16'],'רבה','initial_rule','Rabbah initially validates that case.','retracted',['Slaughter for own purpose with planned wrong-purpose sprinkling'],'Explicitly retracted in same segment'),
('24',['10a:16'],'רבה','retraction','Rabbah returns to Rav Nahman\'s position because of Rav Ashi\'s a fortiori.','asserted',['Same cross-service intent case'],'Explicit local retraction, not erased initial judgment')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=['Bracketed or parenthetical wording preserved; comparison paraphrase follows the local main argument.'] if key in ['14','16'] else []
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['12','14','16','17'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Intent from one sacrificial service to a subsequent service',assertion_mode=mode),['u'+key],unc)
 if key in ['13','15','18','20']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key])
 holder=[] if voice.startswith('anonymous') else [voice.replace(' quoted parallel','')]
 rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if holder:rec('a'+key,'attributions',refs,dict(surface=voice,role='quoted_authority' if 'parallel' in voice else 'speaker',candidates=holder,scope='Local '+role,transmission_chain=[]),['c'+key])
rec('aDimi','attributions',['10a:5'],dict(surface='כי אתא רב דימי אמר',role='transmitter',candidates=['רב דימי'],scope='Reports two supporting arguments; does not become their holder',transmission_chain=[]),['c11','c12','c17'])
for a,b,rel in [('3','1','support'),('4','2','support'),('6','5','support'),('8','7','support'),('5','1','analogy'),('7','2','analogy'),('12','1','support'),('13','12','objection'),('14','12','correction'),('15','14','objection'),('16','14','correction'),('17','2','support'),('18','17','objection'),('19','18','answer'),('20','19','objection'),('21','20','answer'),('24','23','retraction'),('16','24','support')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['9b:'+str(i) for i in range(25,29)]+['10a:'+str(i) for i in range(1,17)]
rec('s1','structure',refs,dict(title='Cross-service intent: Yohanan and Resh Lakish, revised proofs and Rabbah retraction',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Reread9b25–10a16 through explicit Rabbah retraction and new10a17 topic. Preserve quoted parallels, Rav Dimi transmission, three reconstructed a-fortiori arguments, unnamed sides, service/type conditions and initial retracted position.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' record identified; source discourse retained in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_9b25_10a16.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch3.json',r.encoded(res));print(res)
