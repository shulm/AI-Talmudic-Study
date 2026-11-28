import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b9.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['13a:5'],'anonymous Mishnah','rule','Paschal and sin offerings are invalid when a specified service is performed not for its purpose.','asserted',['Paschal/sin offering; slaughter, receiving, carrying or sprinkling; wrong purpose'],'Mishnah baseline; carrying disputed below'),
('2',['13a:5'],'anonymous Mishnah','rule','Combining own-purpose then wrong-purpose intent invalidates these offerings.','asserted',['Paschal/sin offering; own-purpose then wrong-purpose intent'],'Order-specific mixed-intent outcome'),
('3',['13a:5'],'anonymous Mishnah','rule','Combining wrong-purpose then own-purpose intent also invalidates these offerings.','asserted',['Paschal/sin offering; wrong-purpose then own-purpose intent'],'Inverse mixed-intent outcome'),
('4',['13a:6'],'anonymous Mishnah','example','Paschal then peace-offering designation illustrates own-purpose then wrong-purpose.','asserted',['Paschal offering; two ordered designations'],'Example, not independent occurrence of a dispute'),
('5',['13a:6'],'anonymous Mishnah','example','Peace-offering then Paschal designation illustrates wrong-purpose then own-purpose.','asserted',['Paschal offering; reverse designation order'],'Inverse example'),
('6',['13a:7'],'anonymous Mishnah','enumeration','The four invalidating operations listed are slaughter, receiving, carrying and sprinkling.','asserted',['Wrong-purpose intent; four listed services'],'Mishnah enumeration'),
('7',['13a:8'],'רבי שמעון','rule','Rabbi Shimon validates in the carrying case.','asserted',['Wrong-purpose intent in carrying blood'],'Named exception to carrying invalidity'),
('8',['13a:8'],'רבי שמעון','reason','Slaughter, receiving and sprinkling cannot be omitted, whereas carrying can be avoided by slaughtering beside the altar and sprinkling.','asserted',['Possibility of avoiding carrying'],'Reason for carrying exception'),
('9',['13a:9'],'רבי אליעזר','rule','Intent invalidates where carrying is necessary.','asserted',['Carrying where required'],'Necessary carrying condition'),
('10',['13a:9'],'רבי אליעזר','rule','Intent does not invalidate where carrying is unnecessary.','asserted',['Carrying where unnecessary'],'Unnecessary carrying condition'),
('11',['13a:10'],'anonymous','question','Does intent in receiving blood invalidate?','queried',['Receiving blood'],'Question against Mishnah'),
('12',['13a:11'],'quoted baraita','derivation','והקריבו means receiving blood, since sprinkling is already explicitly expressed by וזרקו.','asserted',['Allocation of priestly service verbs'],'Quoted derivation'),
('13',['13a:11'],'quoted baraita','requirement','Receiving must be performed by a fit priest.','asserted',['Receiving blood'],'Separate personnel condition'),
('14',['13a:11'],'quoted baraita','requirement','Receiving must use a sacred vessel.','asserted',['Receiving blood'],'Separate implement condition'),
('15',['13a:12'],'רבי עקיבא','derivation','Rabbi Akiva derives fit priest and sacred vessel for receiving by the shared sons-of-Aaron wording.','asserted',['Receiving blood; verbal comparison'],'Derivation of two separately represented requirements'),
('16',['13a:13'],'רבי טרפון','report','Rabbi Tarfon says he heard a distinction between receiving and sprinkling but cannot explain it.','asserted',['Remembered received distinction'],'Report with emphatic oath retained literally in evidence'),
('17',['13a:14'],'רבי עקיבא','distinction','For receiving, intent was not treated like an act in the cited distinction.','asserted',['Receiving; intent kind and target clarified in13a16–13b4'],'Preliminary wording, not an unrestricted exemption'),
('18',['13a:14'],'רבי עקיבא','distinction','For sprinkling, intent was treated like an act in the cited distinction.','asserted',['Sprinkling; discussion of intent'],'Contrasting side'),
('19',['13a:14'],'רבי עקיבא','rule','Receiving blood outside does not incur karet.','asserted',['Receiving blood outside'],'Explicit liability category'),
('20',['13a:14'],'רבי עקיבא','rule','Sprinkling blood outside incurs karet.','asserted',['Sprinkling blood outside'],'Explicit contrasting liability'),
('21',['13a:14'],'רבי עקיבא','rule','If unfit persons received it, the source says there is no liability regarding it.','asserted',['Received by unfit persons; exact liability referent terse'],'Do not expand liability trigger beyond cited wording'),
('22',['13a:14'],'רבי עקיבא','rule','If unfit persons sprinkled it, the source says there is liability regarding it.','asserted',['Sprinkled by unfit persons; exact liability referent terse'],'Do not expand liability trigger beyond cited wording'),
('23',['13a:15'],'רבי טרפון','response','Rabbi Tarfon says Rabbi Akiva\'s interpretation agrees with his received teaching and praises its value.','asserted',['Response to explained distinction'],'Narrative approval; rhetoric not additional legal ruling'),
('24',['13a:16'],'רבא','initial_reconciliation','Rava distinguishes piggul intent from wrong-purpose intent.','asserted',['Mishnah versus cited receiving distinction'],'Initial distinction requires subsequent act/target refinement'),
('25',['13a:17'],'anonymous','support','The Mishnah says invalidated rather than made piggul, supporting the distinction.','asserted',['Wording נפסל rather than מתפגל'],'Textual support'),
('26',['13a:18'],'anonymous','objection','Does piggul intent not invalidate in receiving?','queried',['Receiving with piggul intent'],'Challenge to broad initial reading'),
('27',['13a:19'],'quoted baraita','rule','The verse includes slaughter and receiving, not only sprinkling, among operations where piggul intent can take effect.','asserted',['Operations leading to eating'],'Counterevidence to unrestricted receiving exemption'),
('28',['13a:20'],'anonymous quoted question','question','Should pouring remnants and burning portions also be included as the operations during which intent takes effect?','queried',['Potential additional operative services'],'Question on extent of operations'),
('29',['13a:21'],'quoted baraita','exclusion','Pouring remnants is excluded from the operative services because it does not prevent atonement.','asserted',['Intent entertained during pouring remnants'],'Exclusion as thought-bearing operation, not as intended consumption'),
('30',['13a:21'],'quoted baraita','exclusion','Burning portions is likewise excluded because it does not prevent atonement.','asserted',['Intent entertained during burning portions'],'Same operative-service distinction'),
('31',['13b:1'],'anonymous','reconciliation','Slaughter intending to receive the blood tomorrow does not create the relevant piggul.','asserted',['Thought during slaughter; intended receiving tomorrow'],'Receiving is not the intended eating/altar consumption'),
('32',['13b:1'],'anonymous','reconciliation','Receiving blood intending to pour remnants tomorrow is the contrasting effective-intent case.','asserted',['Thought during receiving; intended remnant pouring tomorrow'],'Receiving is a valid operative service; target distinguished'),
('33',['13b:2'],'anonymous scholar','objection','Do thoughts concerning pouring remnants or burning portions not invalidate?','queried',['Target versus operative-service ambiguity'],'Unnamed scholar challenges Rava'),
('34',['13b:3'],'quoted Mishnah','inclusion','The doubled eating expression includes human eating and altar eating, so intended remnant pouring and portion burning are included.','asserted',['Intended consumption targets; two eatings'],'Not a claim those are all valid thought-bearing operations'),
('35',['13b:4'],'anonymous','reconciliation','Sprinkling with intent to pour remnants tomorrow is an effective-intent case.','asserted',['Thought during sprinkling; intended pouring tomorrow'],'Operative service versus intended altar consumption'),
('36',['13b:4'],'anonymous','reconciliation','Pouring remnants with intent to burn portions tomorrow is the contrasting ineffective-intent case.','asserted',['Thought during pouring remnants; intended burning tomorrow'],'Pouring itself not indispensable operative service')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=['The source אין/חייבין עליו is preserved without resolving the unstated liability referent; demanding QA should not infer a specific act from this row alone.'] if key in ['21','22'] else []
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['8','15','23','24','34'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Four services, carrying dispute and receiving/piggul act-target distinctions',assertion_mode=mode),['u'+key],unc)
 if mode=='queried':rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key],unc)
 if mode=='asserted':rec('p'+key,'positions',refs,dict(holder_candidates=[] if voice.startswith('anonymous') else [voice],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if voice in ['רבי שמעון','רבי אליעזר','רבי עקיבא','רבי טרפון','רבא']:rec('a'+key,'attributions',refs,dict(surface=voice,role='speaker',candidates=[voice],scope='Local '+role,transmission_chain=[]),['c'+key])
for a,b,rel in [('4','2','support'),('5','3','support'),('8','7','support'),('17','11','support'),('23','16','local_resolution'),('24','11','answer'),('25','24','support'),('26','24','objection'),('27','26','support'),('29','28','answer'),('30','28','answer'),('31','26','answer'),('32','26','answer'),('33','29','objection'),('34','33','support'),('35','33','answer'),('36','33','answer')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['13a:'+str(i) for i in range(5,22)]+['13b:'+str(i) for i in range(1,5)]
rec('s1','structure',refs[:5],dict(title='Mishnah: wrong-purpose/mixed intent and carrying dispute',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[5:],dict(title='Receiving versus sprinkling: intent category, operative service and intended altar consumption',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Manual reread through13b4 final act/target reconciliation and13b5 new finger-dipping inquiry. Separate validity/discharge categories, physical outside liability, unfit-person uncertainty, mixed-intent orders, receiving as operation versus target, and remnant pouring as operation versus target.' if layer=='reconciliation' else 'Manual source pass; '+('supported rows listed.' if ids else 'No separate '+layer+' item after inspection; source discourse retained in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_13a5_13b4.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch9.json',r.encoded(res));print(res)
