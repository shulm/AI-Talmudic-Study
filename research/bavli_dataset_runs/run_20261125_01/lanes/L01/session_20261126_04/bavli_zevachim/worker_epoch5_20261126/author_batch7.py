import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b7.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['11b:16'],'רבי יהושע','mishnah_rule','Rabbi Yehoshua validates Paschal slaughtered in the morning of the fourteenth not for its purpose, as if slaughtered on the thirteenth.','asserted',['Fourteenth morning; Paschal; wrong-purpose slaughter'],'Mishnah position'),
('2',['11b:16'],'בן בתירא','mishnah_rule','Ben Beteira invalidates that morning wrong-purpose Paschal, as if slaughtered in the afternoon.','asserted',['Fourteenth morning; Paschal; wrong-purpose slaughter'],'Mishnah position; explanation debated'),
('3',['11b:17'],'שמעון בן עזאי','received_rule','Ben Azzai reports from seventy-two elders that edible sacrifices slaughtered not for their purpose are valid apart from Paschal and sin offerings.','asserted',['Edible sacrifices; wrong-purpose slaughter; Paschal/sin exceptions'],'Received teaching; edible restriction matters'),
('4',['11b:17'],'שמעון בן עזאי','received_rule','Those valid wrong-purpose sacrifices do not discharge their owners\' obligation.','asserted',['Edible sacrifices; wrong-purpose slaughter; stated exceptions'],'Separate non-discharge outcome'),
('5',['11b:17'],'anonymous Mishnah','qualification','Ben Azzai\'s added exception is the burnt offering.','asserted',['Difference between received rule and preceding anonymous view'],'Mishnah interpretation of addition'),
('6',['11b:17'],'חכמים','disagreement','The sages did not agree with Ben Azzai\'s addition.','asserted',['Burnt-offering addition'],'Disagreement retained, reasons discussed later'),
('7',['11b:18'],'רבי אלעזר אמר רבי אושעיא','initial_interpretation','Rabbi Elazar reports Rabbi Oshaya: Ben Beteira validates Paschal slaughtered morning of fourteenth for its purpose, because the whole day is its time.','rejected',['Fourteenth morning; own-purpose Paschal'],'Initial interpretation displaced at12a9'),
('8',['11b:19'],'anonymous','question','Why then does Ben Beteira say as if?','queried',['Whole-day-time interpretation'],'Wording objection'),
('9',['11b:20'],'anonymous','answer','He mirrors Rabbi Yehoshua\'s as-if wording.','asserted',['Initial whole-day interpretation'],'Local wording defense, not final adopted interpretation'),
('10',['11b:21'],'anonymous','objection','Why debate wrong-purpose slaughter rather than own-purpose slaughter?','queried',['Initial whole-day interpretation'],'Choice-of-case objection'),
('11',['11b:22'],'anonymous','answer','Had they debated own-purpose, one might think Rabbi Yehoshua concedes wrong-purpose invalidity because part of the day is fit; the stated case prevents that inference.','hypothetical',['Hypothetical alternate presentation'],'Defense of initial interpretation'),
('12',['11b:23'],'anonymous','objection','The verse says between the evenings.','challenged',['Paschal time phrase'],'Textual objection to whole-day reading'),
('13',['11b:24'],'עולא בריה דרב עילאי','answer','The phrase is read as between two evenings.','asserted',['Initial whole-day-time reading'],'Proposed interpretation subsequently pressured'),
('14',['11b:25'],'anonymous','objection','Would the daily offering\'s between-evenings phrase also permit the whole day?','queried',['Parallel daily-offering time phrase'],'Parallel-text challenge'),
('15',['11b:26'],'anonymous','answer','The specified morning lamb implies that between evenings there means its literal afternoon sense.','asserted',['Daily offering; one lamb specified in morning'],'Distinguishes daily offering'),
('16',['11b:27'],'anonymous','objection','Perhaps one is in the morning and the other may be offered all day.','hypothetical',['Alternative reading of daily-offering pair'],'Counter-reading'),
('17',['11b:28'],'anonymous','answer','One in the morning excludes two in the morning.','asserted',['Daily offering; one morning lamb'],'Answer to counter-reading'),
('18',['11b:29'],'anonymous','objection','Would the lamps\' between-evenings phrase likewise permit the whole day?','queried',['Lamp time phrase'],'Parallel-text challenge'),
('19',['11b:30'],'quoted baraita','answer','The lamp receives enough oil to burn from evening until morning.','asserted',['Lamp oil measure; evening to morning'],'First explanation of evening-until-morning'),
('20',['11b:30'],'quoted baraita','alternative_answer','Alternatively, no service is valid from evening until morning except this one.','asserted',['Alternative exposition of evening-until-morning'],'Alternative exposition kept distinct'),
('21',['11b:31'],'anonymous','objection','Would incense with between-evenings wording be valid all day?','queried',['Incense time phrase'],'Parallel-text challenge'),
('22',['11b:32','12a:1'],'anonymous','answer','Incense is compared to lamps.','asserted',['Incense time compared with lamps'],'Answer to incense challenge'),
('23',['12a:2'],'anonymous','objection','Paschal itself also says in the evening.','challenged',['Paschal evening phrase'],'Additional textual objection'),
('24',['12a:3'],'quoted baraita','answer','An offering specified both evening and between-evenings is delayed after one specified only between-evenings.','asserted',['Paschal versus daily offering ordering'],'Ordering interpretation of additional phrase'),
('25',['12a:4'],'anonymous','objection','Can morning count as its time while afternoon imposes delay behind another service?','queried',['Whole-day validity alongside afternoon priority'],'Apparent inconsistency'),
('26',['12a:5'],'anonymous citing רבי יוחנן','answer','Rabbi Yohanan rules to pray minha and then musaf, supplying an analogous later priority despite earlier availability.','asserted',['Minha and musaf both due; prayer analogy'],'Analogy, not identical sacrifice rule'),
('27',['12a:6'],'anonymous','objection','Then what do the between-evenings phrases for incense and lamps add?','queried',['Initial reading leaves parallel phrases redundant'],'Unanswered pressure on initial interpretation'),
('28',['12a:7'],'רבי quoted','objection','Rabbi answers on Ben Beteira\'s behalf that the thirteenth has no fit portion but the fourteenth has a fit portion.','asserted',['Fourteenth partly fit compared with thirteenth'],'Quoted answer inconsistent with whole-day premise'),
('29',['12a:8'],'anonymous','objection','If the whole-day interpretation were right, the entire day would be fit.','challenged',['Contrast with Rabbi\'s partly-fit language'],'Rejects initial whole-day interpretation'),
('30',['12a:9'],'רבי יוחנן','replacement','Ben Beteira invalidates fourteenth-morning Paschal for its own purpose as well.','asserted',['Fourteenth morning; Paschal; own-purpose slaughter'],'Replacement interpretation; part of day fit'),
('31',['12a:9'],'רבי יוחנן','replacement','Ben Beteira invalidates fourteenth-morning Paschal not for its own purpose as well.','asserted',['Fourteenth morning; Paschal; wrong-purpose slaughter'],'Replacement interpretation; part of day fit'),
('32',['12a:10'],'רבי אבהו','objection','Then how can Ben Beteira have a fit Paschal? Designation today seems initially rejected; designation yesterday seems fit and then rejected.','queried',['Designation today or yesterday under morning invalidity'],'Problem of rejection'),
('33',['12a:11'],'רבי אבהו','answer','The case can be designation after midday.','asserted',['Paschal consecration after midday'],'Construction answering rejection problem'),
('34',['12a:12'],'אביי','alternative_answer','Even morning designation works: missing the required time within the same day does not count as premature for this purpose.','asserted',['Morning designation; fitness later same day'],'Alternative answer'),
('35',['12a:13'],'רב פפא','alternative_answer','Even designation at night works: night does not count as missing time; the school of Rabbi Yishmael allows entering the tithe pen on the eighth night.','asserted',['Night designation; eighth-night analogy'],'Alternative answer, not denial of day offering requirement'),
('36',['12a:14'],'רבי אפטוריקי','textual_question','Seven days under its mother appears to allow the next night, whereas from the eighth day onward appears to disallow the night.','queried',['Apparent timing conflict in verses'],'Textual contradiction'),
('37',['12a:15'],'anonymous resolution','distinction','Night is fit for consecration.','asserted',['Night preceding eighth day; sanctification rather than offering'],'First side of distinction'),
('38',['12a:15'],'anonymous resolution','distinction','Day is required for acceptance of the offering.','asserted',['Eighth day; actual sacrificial acceptance'],'Second side of distinction'),
('39',['12a:16'],'רבי זירא','question','Does Rabbi Yohanan consequently hold that living animals can be rejected?','queried',['Implication of timing interpretation'],'Question to Rabbi Abbahu'),
('40',['12a:17'],'רבי יוחנן quoted','case_rule','For an animal shared by two partners, one consecrates his half, then buys and consecrates the other half: it is holy.','asserted',['Partial ownership consecrated before acquisition of remaining half'],'Sanctity outcome'),
('41',['12a:17'],'רבי יוחנן quoted','case_rule','That animal cannot be offered.','asserted',['Partial ownership consecrated before acquisition/consecration of remaining half'],'Non-offerability distinct from sanctity'),
('42',['12a:18'],'רבי יוחנן quoted continuation','case_rule','That animal effects substitution.','asserted',['Rejected consecrated animal from shared-ownership case'],'Substitution effect'),
('43',['12a:18'],'רבי יוחנן quoted continuation','case_rule','Its substitute is like it.','asserted',['Substitute of that rejected animal'],'Corresponding status, not ordinary offerable substitute'),
('44',['12a:19'],'anonymous','inference','Living animals can be rejected.','asserted',['Inference from shared-ownership case'],'First stated inference'),
('45',['12a:19'],'anonymous','inference','Initial rejection counts as rejection.','asserted',['Initially unofferable shared-ownership consecration'],'Second stated inference'),
('46',['12a:19','12b:1'],'anonymous','inference','There is rejection in monetary sanctity.','asserted',['Stated third inference from shared-ownership case'],'Third stated inference'),
('47',['12b:2'],'עולא אמר רבי יוחנן','rule','One who ate forbidden fat, designated an offering, changed religion and returned leaves that offering rejected.','asserted',['Sin; offering designation; apostasy; return'],'Reported permanent rejection'),
('48',['12b:3'],'רבי ירמיה אמר רבי אבהו אמר רבי יוחנן','rule','One who ate forbidden fat, designated an offering, lost sanity and recovered leaves that offering rejected.','asserted',['Sin; offering designation; loss and recovery of sanity'],'Separate reported permanent rejection'),
('49',['12b:4'],'anonymous','necessity','Apostasy alone might establish rejection only for deliberately rejecting oneself; involuntary insanity might be like sleep.','hypothetical',['Only apostasy rule known'],'Counterfactual, not accepted exemption'),
('50',['12b:5'],'anonymous','necessity','Insanity alone might establish rejection because recovery is not controlled, whereas voluntary return from apostasy might differ; both reports are needed.','hypothetical',['Only insanity rule known'],'Counterfactual, not accepted exemption'),
('51',['12b:6'],'רבי ירמיה','inquiry','If after sin and designation the court permits forbidden fat and later retracts, is the offering rejected?','queried',['Forbidden-fat sin; designation; temporary court permission and retraction'],'Inquiry about temporary public ruling'),
('52',['12b:7'],'anonymous elder','answer','Rabbi Yohanan began the rejection teaching from this case: elsewhere the person was rejected, but here the offering itself was also rejected.','asserted',['Temporary court permission case contrasted with personal disability'],'Elder reports rejection applies; no invented elder identity')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=[]
 if key=='3':unc=['Source reads רבי אליעזר in the installation narrative; preserve surface rather than silently changing to another name.']
 if key=='33':unc=['Designation after midday is inferred from immediate designation question; terse source תהא לאחר חצות preserved.']
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['11','24','32','35','36','49','50','52'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Fourteenth-morning Paschal, interpretations of time and rejection',assertion_mode=mode),['u'+key],unc)
 if mode=='queried':rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key],unc)
 if mode not in ['queried','hypothetical']:
  holder=[] if voice.startswith('anonymous') else [voice]
  if key in ['7']:holder=['בן בתירא']
  if key in ['30','31']:holder=['בן בתירא']
  if key in ['40','41','42','43','47','48']:holder=['רבי יוחנן']
  rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if voice in ['רבי יהושע','בן בתירא','שמעון בן עזאי','חכמים','עולא בריה דרב עילאי','רבי יוחנן','רבי אבהו','אביי','רב פפא','רבי אפטוריקי','רבי זירא','רבי ירמיה']:rec('a'+key,'attributions',refs,dict(surface=voice,role='collective' if voice=='חכמים' else 'speaker',candidates=[voice],scope='Local '+role,transmission_chain=[]),['c'+key])
for key,refs,surface,chain,links in [('7',['11b:18'],'רבי אלעזר אמר רבי אושעיא',['רבי אלעזר','רבי אושעיא'],['c7']),('47',['12b:2'],'עולא אמר רבי יוחנן',['עולא','רבי יוחנן'],['c47']),('48',['12b:3'],'רבי ירמיה אמר רבי אבהו אמר רבי יוחנן',['רבי ירמיה','רבי אבהו','רבי יוחנן'],['c48'])]:rec('achain'+key,'attributions',refs,dict(surface=surface,role='transmitter',candidates=[chain[0]],scope='Exact named reporting chain',transmission_chain=chain),links)
rec('aelders','attributions',['11b:17'],dict(surface='מפי שבעים ושנים זקן',role='quoted_authority',candidates=['seventy-two elders'],scope='Ben Azzai received teaching',transmission_chain=['שמעון בן עזאי','seventy-two elders']),['c3','c4'])
rec('a52','attributions',['12b:7'],dict(surface='ההוא סבא',role='anonymous',candidates=[],scope='Elder reporting Rabbi Yohanan teaching; identity not supplied',transmission_chain=[]),['c52'])
for a,b,rel in [('6','5','objection'),('8','7','objection'),('9','8','answer'),('10','7','objection'),('11','10','answer'),('12','7','objection'),('13','12','answer'),('14','13','objection'),('15','14','answer'),('16','15','objection'),('17','16','answer'),('18','13','objection'),('19','18','answer'),('20','18','answer'),('21','13','objection'),('22','21','answer'),('23','7','objection'),('24','23','answer'),('25','24','objection'),('26','25','answer'),('27','7','objection'),('28','7','objection'),('29','28','qualification'),('30','7','correction'),('31','2','qualification'),('32','30','objection'),('33','32','answer'),('34','32','answer'),('35','32','answer'),('37','36','answer'),('38','36','answer'),('37','35','support'),('41','39','answer'),('44','41','local_resolution'),('45','41','local_resolution'),('46','41','local_resolution'),('49','47','qualification'),('50','48','qualification'),('52','51','answer')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['11b:'+str(i) for i in range(16,33)]+['12a:'+str(i) for i in range(1,20)]+['12b:'+str(i) for i in range(1,8)]
rec('s1','structure',refs[:2],dict(title='Mishnah: fourteenth morning and Ben Azzai received exception',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[2:26],dict(title='Ben Beteira timing interpretation: whole-day reading challenged and replaced',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s3','structure',refs[26:],dict(title='Designation timing and rejection: living animal, shared ownership and personal/court changes',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Reread11b16–12b7 through elder answer and12b8 next lemma. Keep initial whole-day report rejected, two morning outcomes, day/night sanctification versus offering, three separate rejection inferences, parallel personal disability cases and court case conditions. Exact names/transmissions retained.' if layer=='reconciliation' else 'Manual source pass; '+('supported records listed.' if ids else 'No separate '+layer+' item after inspection; anonymous or quoted discourse retained.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_11b16_12b7.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch7.json',r.encoded(res));print(res)
