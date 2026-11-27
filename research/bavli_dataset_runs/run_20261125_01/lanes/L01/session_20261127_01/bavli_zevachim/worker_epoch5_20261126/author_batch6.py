import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b6.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['11a:20'],'רבי יוחנן','interpretation','Rabbi Yohanan says Yosef ben Honi and Rabbi Eliezer said the same thing.','asserted',['Scope of their wrong-purpose sacrifice positions'],'Named interpretive alignment; Rabbah differs below'),
('2',['11a:21'],'רבה','interpretation','Rabbah says they disagree concerning other offerings slaughtered as a sin offering.','asserted',['Other offerings designated as sin offering'],'Alternative interpretation, not a Rabbah/Rava confusion'),
('3',['11a:22'],'רבי אליעזר','quoted_rule','Rabbi Eliezer invalidates an over-year Paschal slaughtered at its appointed time for its own purpose.','asserted',['Over-year Paschal; at appointed time; own purpose'],'Quoted rule'),
('4',['11a:22'],'רבי יהושע','quoted_rule','Rabbi Yehoshua validates that over-year Paschal case.','asserted',['Over-year Paschal; at appointed time; own purpose'],'Quoted contrasting rule'),
('5',['11a:22'],'רבי אליעזר','quoted_rule','Rabbi Eliezer invalidates other offerings slaughtered as Paschal at its appointed time.','asserted',['Other offering; Paschal designation; appointed time'],'Quoted rule'),
('6',['11a:22'],'רבי יהושע','quoted_rule','Rabbi Yehoshua validates other offerings slaughtered as Paschal at its appointed time.','asserted',['Other offering; Paschal designation; appointed time'],'Quoted contrasting rule'),
('7',['11a:23'],'רבי יהושע','a_fortiori','Other offerings are valid as Paschal outside its time when Paschal itself is not valid as such; all the more they should be valid as Paschal at its time when it is valid as such.','asserted',['Other offerings designated as Paschal; outside versus appointed time'],'Proposed proof for permissive outcome'),
('8',['11a:24'],'רבי אליעזר','reductio','Reversing the comparison would wrongly validate Paschal at its time as other offerings, since outside its time it is valid as others despite not being valid as itself.','hypothetical',['Counter-inference would validate wrong-purpose Paschal on fourteenth'],'Reductio, not Rabbi Eliezer actual permission'),
('9',['11a:25'],'רבי אליעזר continued','distinction','Outside-time validity of other offerings as Paschal coincides with Paschal validity as others; at its time Paschal is invalid as others, so the comparison fails.','challenged',['Reciprocal validity differs by time'],'Distinguishes Rabbi Yehoshua premise'),
('10',['11a:26'],'רבי יהושע','objection','Rabbi Yehoshua objects that this weakens Paschal and strengthens peace offerings.','challenged',['Relative standing in reciprocal designation argument'],'Explicit response'),
('11',['11a:27'],'רבי אליעזר','premise','Surplus Paschal becomes peace offering, but surplus peace offering does not become Paschal.','asserted',['Direction of surplus conversion'],'Asymmetric premise for replacement proof'),
('12',['11a:28'],'רבי אליעזר','replacement_proof','If Paschal, whose surplus becomes peace offering, is invalid at its time as peace offering, peace offering whose surplus never becomes Paschal should all the more be invalid as Paschal at its time.','asserted',['Peace offering designated as Paschal at Paschal time'],'Replacement a-fortiori proof'),
('13',['11b:1'],'רבי יהושע','counterpremise','Surplus sin offering becomes burnt offering, but surplus burnt offering does not become sin offering.','asserted',['Direction of surplus sin/burnt conversion'],'Parallel counterexample premise'),
('14',['11b:2'],'רבי יהושע','counterargument','The same reasoning would invalidate a burnt offering slaughtered as a sin offering, since a sin offering is invalid as burnt despite surplus conversion in that direction.','hypothetical',['Burnt offering designated as sin offering'],'Counterargument to Rabbi Eliezer, not a new independent ruling'),
('15',['11b:3'],'רבי אליעזר','distinction','Sin offering is valid for its own purpose all year, unlike Paschal only at its time; its outside-time invalidity supports invalidating others as Paschal.','asserted',['Distinguish year-round sin validity from time-limited Paschal validity'],'Response to counterexample; does not simply accept inferred burnt invalidity'),
('16',['11b:5'],'רבי יוחנן או רבי ינאי reported','derivation','The verse about what Israel will raise is read to preserve sanctity under a higher designation and invalidate under a lower designation, explaining Shimon brother of Azariah.','asserted',['Higher versus lower designated sanctity'],'Two alternative named report chains preserved'),
('17',['11b:6'],'anonymous','objection','The verse is needed for Shmuel\'s teaching that eating tevel incurs death, because it speaks of produce awaiting separation.','challenged',['Alternative use of אשר ירימו'],'Challenge to exclusive use of verse'),
('18',['11b:7'],'anonymous','answer','The future form ירימו rather than הורמו supports both derivations.','asserted',['Word-form difference in same verse'],'Allows both source uses'),
('19',['11b:8'],'רבי זירא','inquiry','Does Shimon mean valid without discharge, disagreeing in one respect, or valid with discharge, disagreeing in two?','unresolved',['Shimon brother of Azariah\'s validation under higher designation'],'Inquiry; later inference is challenged, no final binary resolution asserted'),
('20',['11b:9'],'אביי או רבי זריקא','proof_attempt','The firstborn/tithe-as-peace valid and inverse invalid examples are offered to test discharge.','asserted',['Proof from final Mishnah examples'],'Alternative attribution Abaye or Rabbi Zerika preserved'),
('21',['11b:10'],'anonymous continuation of proof','inference','Firstborn has no owner-discharge obligation; infer valid without discharge in the latter examples and then in the earlier general rule.','challenged',['Inference from firstborn example to general higher-designation rule'],'Proof inference challenged next, not settled interpretation'),
('22',['11b:11'],'anonymous','objection','The two portions may each have their own meaning; the proposed transfer is not necessary.','asserted',['Different Mishnah portions need not share discharge sense'],'Rejects proof, does not select the opposite answer'),
('23',['11b:12'],'anonymous','question','If only higher/lower status is taught, is that not already stated in the most-holy/lesser-holy examples?','queried',['Purpose of firstborn/tithe examples'],'Apparent redundancy question'),
('24',['11b:13'],'anonymous','answer','One might think higher/lower distinction applies only across most-holy and lesser-holy, not within lesser-holy offerings.','hypothetical',['Differences within lesser-holy class'],'Explains need for additional example'),
('25',['11b:14'],'anonymous','objection','Another Mishnah already gives peace offerings precedence over firstborn because of four applications, laying on hands, libations, and breast/thigh waving.','challenged',['Relative rank among lesser-holy offerings'],'Existing evidence makes rank known'),
('26',['11b:15'],'anonymous','answer','This is the primary teaching; the other passage includes it incidentally.','asserted',['Relationship between present and cited teaching'],'Local response to redundancy')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=['Names retained as explicit alternative transmission; no forced single speaker.'] if key in ['16','20'] else []
 if key=='1':unc=['Source here reads יוסף בן חוני; opening Mishnah has יוסי בן חוני. Surface preserved without external identity harmonization.']
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['7','8','12','14','19','25'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Yosef ben Honi/Eliezer alignment and Shimon higher/lower sanctity inquiry',assertion_mode=mode),['u'+key],unc)
 if key in ['17','19','23','25']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='unreviewed_alternatives' if key=='19' else 'partial'),['u'+key],unc)
 if mode not in ['queried','unresolved']:
  holder=[] if voice.startswith('anonymous') else [voice.replace(' continued','')]
  if key=='16':holder=['רבי יוחנן','רבי ינאי']
  if key=='20':holder=['אביי','רבי זריקא']
  rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if not voice.startswith('anonymous') and key not in ['16','20']:rec('a'+key,'attributions',refs,dict(surface=voice,role='speaker',candidates=[voice.replace(' continued','')],scope='Local '+role,transmission_chain=[]),['c'+key],unc)
rec('a16a','attributions',['11b:5'],dict(surface='רב אשי מתני משמיה דרבי יוחנן',role='transmitter',candidates=['רב אשי'],scope='First report version of Shimon rationale',transmission_chain=['רב אשי','רבי יוחנן']),['c16'])
rec('a16b','attributions',['11b:5'],dict(surface='רב אחא בריה דרבא מתני משמיה דרבי ינאי',role='transmitter',candidates=['רב אחא בריה דרבא'],scope='Alternative report version',transmission_chain=['רב אחא בריה דרבא','רבי ינאי']),['c16'])
rec('a17','attributions',['11b:6'],dict(surface='שמואל',role='quoted_authority',candidates=['שמואל'],scope='Tevel prohibition teaching',transmission_chain=[]),['c17'])
rec('a20','attributions',['11b:9'],dict(surface='אמר אביי ואיתימא רבי זריקא',role='speaker',candidates=['אביי','רבי זריקא'],scope='Alternative attribution of proof attempt',transmission_chain=[]),['c20'],['Do not assign one speaker or report joint authorship.'])
for a,b,rel in [('7','6','support'),('8','7','objection'),('9','7','objection'),('10','9','objection'),('11','12','support'),('12','5','support'),('13','14','support'),('14','12','objection'),('15','14','answer'),('17','16','objection'),('18','17','answer'),('20','19','support'),('21','19','answer'),('22','21','objection'),('24','23','answer'),('25','24','objection'),('26','25','answer')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
rec('uHeading','utterances',['11b:4'],dict(textual_voice='Mishnah lemma',discourse_role='topic heading',composition='atomic'),origin='literal')
refs=['11a:'+str(i) for i in range(20,29)]+['11b:'+str(i) for i in range(1,16)]
rec('s1','structure',refs[:12],dict(title='Yohanan versus Rabbah on Yosef ben Honi/Eliezer alignment; Paschal reciprocal-designation debate',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[12:],dict(title='Shimon higher/lower sanctity source and unresolved discharge inquiry',primary=True,boundary='closed',legacy_ids=[]),unc=['Proof for no-discharge is rejected; no final binary resolution inferred before next Mishnah.'],origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Reread through11b15 closure and11b16 new Mishnah. Preserve reciprocal comparisons as proposed/reductio not rulings, source name variants, alternative report chains and unresolved discharge inquiry after rejected proof.' if layer=='reconciliation' else 'Manual source pass; '+('supported records listed.' if ids else 'No separate '+layer+' item after inspection; lemma or discourse preserved in utterances.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_11a20_11b15.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch6.json',r.encoded(res));print(res)
