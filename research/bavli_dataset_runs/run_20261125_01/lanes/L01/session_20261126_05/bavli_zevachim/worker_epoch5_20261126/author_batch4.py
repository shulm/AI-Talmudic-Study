import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_epoch5_20261126';j,ss=r.load(job);state=r.current(job);rows={x['ref'].split(' ')[1]:x for x in ss.values()};R=[];prefix='zv.epoch5.b4.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,c,links=[],unc=[],origin='source_paraphrase'):
 R.append(dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=c,origin=origin,uncertainty=unc,links=[prefix+x for x in links]));return key
D=[
('1',['10a:17'],'רבי אליעזר','derivation','Rabbi Eliezer invalidates a guilt offering not for its purpose by analogy to the sin offering: both come for sin.','asserted',['Guilt offering slaughtered not for its purpose'],'Initial analogy, challenged below'),
('2',['10a:18'],'רבי יהושע','objection','The sin offering differs because its blood is applied above.','challenged',['Sin versus guilt offering; blood location'],'Objection to initial analogy'),
('3',['10a:19'],'רבי אליעזר','counterexample','The Paschal offering has blood below and nevertheless is invalid when slaughtered not for its purpose.','asserted',['Paschal offering; wrong-purpose slaughter'],'Counterexample to blood-location distinction'),
('4',['10a:20'],'רבי יהושע','objection','The Paschal offering differs by having a fixed time.','challenged',['Paschal versus guilt offering'],'Distinguishing condition'),
('5',['10a:21'],'רבי אליעזר','counterexample','The sin offering counters the fixed-time distinction.','asserted',['Sin offering counterexample'],'Return to original example'),
('6',['10a:22','10b:1'],'רבי יהושע','objection','Rabbi Yehoshua says the argument returns in a circle.','challenged',['Alternating Paschal/sin counterexamples'],'Circular return objection'),
('7',['10b:2'],'רבי אליעזר','new_derivation','The sin offering has היא at slaughter and the Paschal offering has הוא at slaughter, marking validity only for their own purpose.','asserted',['New pronoun derivation; sin and Paschal slaughter'],'New proof, not a new outcome'),
('8',['10b:3'],'רבי אליעזר','analogy','The guilt offering too has הוא, so he infers validity for its own purpose and invalidity otherwise.','asserted',['Guilt-offering pronoun; inference from sin/Paschal'],'Contested analogy'),
('9',['10b:4'],'רבי יהושע','distinction','The guilt-offering הוא occurs only after burning the portions; the offering remains valid even if those portions were not burned.','asserted',['Guilt offering; omission of portion burning'],'Unlike pronouns at slaughter'),
('10',['10b:5'],'רבי אליעזר','replacement_proof','כחטאת כאשם compares guilt offering to sin offering, supporting invalidity not for its purpose.','asserted',['Guilt offering slaughtered not for its purpose'],'Scriptural juxtaposition offered'),
('11',['10b:6'],'anonymous','question','Why not turn the recurring examples into a common-factor argument?','queried',['Rabbi Yehoshua circularity objection'],'Question on unavailable combined proof'),
('12',['10b:7'],'anonymous','answer','The shared factor can be challenged because both have an aspect involving karet.','asserted',['Sin and Paschal offerings; common-factor inference'],'Reason common-factor proof fails'),
('13',['10b:8'],'anonymous','alternative_objection','Why not distinguish the sin offering by its blood entering the innermost area?','queried',['Alternative to above-altar blood objection'],'Proposed alternative distinction'),
('14',['10b:9'],'anonymous','answer','The discussion concerns outer sin offerings.','asserted',['Scope restricted to outer sin offerings'],'Rejects proposed inner-blood distinction'),
('15',['10b:10'],'anonymous','alternative_objection','Then distinguish that bringing its blood inside invalidates it.','queried',['Outer sin offering blood taken inward'],'Further alternative distinction'),
('16',['10b:11'],'anonymous','answer','Rabbi Eliezer holds that guilt offering too is invalidated in this respect.','asserted',['Guilt-offering blood taken inward; Rabbi Eliezer view'],'No distinguishing feature for Rabbi Eliezer'),
('17',['10b:12'],'anonymous','alternative_objection','Distinguish that sin offering atones for karet offenses.','queried',['Sin-offering atonement'],'Proposed distinguishing feature'),
('18',['10b:13'],'anonymous','answer','Use the sin offering for hearing testimony instead.','asserted',['Hearing-testimony sin offering as example'],'Avoids proposed karet distinction'),
('19',['10b:14'],'anonymous','alternative_objection','Distinguish that it requires four blood applications.','queried',['Sin offering; four applications'],'Proposed numerical distinction'),
('20',['10b:15'],'anonymous quoting רבי ישמעאל','answer','Rabbi Yishmael says all bloods require four applications.','asserted',['Rabbi Yishmael view; number of applications'],'Under this view not a distinguishing number'),
('21',['10b:16'],'anonymous','alternative_objection','Distinguish that its applications are on four horns.','queried',['Sin offering; horns rather than number alone'],'Refined alternative distinction'),
('22',['10b:17'],'anonymous','answer','Finger, horn and edge would also distinguish; the speaker selected one of several reasons.','asserted',['Available distinguishing features of sin-offering blood service'],'Nonexhaustive original objection'),
('23',['10b:18'],'anonymous','question','Why did Rabbi Eliezer not answer that guilt-offering blood too belongs above?','queried',['Counter to Rabbi Yehoshua blood-location objection'],'Inquiry into guilt blood location'),
('24',['10b:19'],'אביי','a_fortiori','A guilt offering cannot have blood above: a wholly burned burnt offering has blood below, all the more a guilt offering that is not wholly burned.','asserted',['Guilt compared with wholly consumed burnt offering'],'Initial blood-location proof'),
('25',['10b:20'],'anonymous','objection','The burnt offering differs in not atoning as described here.','challenged',['Burnt-offering premise'],'Objection to initial proof'),
('26',['10b:21'],'anonymous','counterexample','The bird sin offering provides a counterexample.','asserted',['Atoning offering with blood below'],'Response to lack-of-atonement distinction'),
('27',['10b:22'],'anonymous','objection','The bird sin offering is not a slaughtered animal offering.','challenged',['Bird versus animal sacrifice'],'Counterexample distinguished'),
('28',['10b:23'],'anonymous','common_factor','Burnt and bird sin offerings share most-holy status and blood below; infer the same blood location for most-holy guilt offering.','asserted',['Combined proof from burnt and bird sin offerings'],'Proposed common factor'),
('29',['10b:24'],'רבא מפרזקיא','objection','Both examples lack a fixed monetary valuation, unlike the guilt offering.','challenged',['Common factor compared with guilt-offering fixed amount'],'Rava of Parzakya addresses Rav Ashi'),
('30',['10b:25'],'anonymous','replacement_derivation','Rabbi Eliezer\'s reason instead uses המחטא אותה: this offering\'s blood is above, not another\'s.','asserted',['Sin-offering-exclusive upper blood location'],'Replacement for failed combined proof'),
('31',['10b:26'],'anonymous','objection','Then the sin-offering אותה could likewise imply only it is invalid not for its purpose while other sacrifices remain valid.','hypothetical',['Alternative exclusion from sin-offering intent verse'],'Challenge to guilt-offering invalidity'),
('32',['10b:27'],'anonymous','answer','That exclusion is not exhaustive, since the Paschal offering is also omitted from its literal wording.','asserted',['Wrong-purpose invalidity; Paschal exception'],'Reply concerning intent exclusion'),
('33',['10b:28'],'anonymous','objection','The blood-location exclusion likewise appears nonexhaustive because it leaves out the bird burnt offering.','challenged',['Bird burnt offering upper blood location'],'Challenge to exclusive blood inference'),
('34',['10b:29'],'anonymous','answer','Within slaughtered animal offerings it omits nothing.','asserted',['Restrict blood exclusion to animal slaughter category'],'Local restriction answers bird objection'),
('35',['10b:30'],'anonymous','alternative_answer','Alternatively the statement follows Rabbi Elazar son of Rabbi Shimon, who treats the two upper locations as separate.','asserted',['Alternative blood-location explanation'],'Alternative, not rejection of animal-category answer'),
('36',['10b:31'],'quoted baraita','rule','Lower blood applications are below the red line.','asserted',['Blood designated for lower applications'],'Quoted location rule'),
('37',['10b:31'],'quoted baraita','rule','Upper blood applications are above the red line.','asserted',['Blood designated for upper applications'],'Quoted location rule, subsequently qualified'),
('38',['10b:31'],'רבי אלעזר ברבי שמעון','qualification','The general above-red-line rule concerns the bird burnt offering.','asserted',['Rabbi Elazar son of Rabbi Shimon; bird burnt offering'],'Qualification of upper location'),
('39',['10b:31'],'רבי אלעזר ברבי שמעון','rule','An animal sin offering is performed only on the body of the horn itself.','asserted',['Animal sin offering; Rabbi Elazar son of Rabbi Shimon'],'Distinct upper location')]
for key,refs,voice,role,prop,mode,cond,status in D:
 unc=['Bracketed source text retained; no external text normalization.'] if key in ['15','21'] else []
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['7','9','22','24','28'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Rabbi Eliezer guilt-offering wrong-purpose invalidity and blood-location proofs',assertion_mode=mode),['u'+key],unc)
 if mode=='queried' or key in ['29','31','33']:rec('q'+key,'questions',refs,dict(formulation=prop,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key])
 if mode not in ['queried','hypothetical']:
  holder=[] if voice.startswith('anonymous') else [voice]
  if key=='16':holder=['רבי אליעזר']
  if key=='20':holder=['רבי ישמעאל']
  rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status=status),['c'+key],unc)
 if voice not in ['anonymous','quoted baraita'] and not voice.startswith('anonymous quoting'):rec('a'+key,'attributions',refs,dict(surface=voice,role='speaker',candidates=[voice],scope='Local '+role,transmission_chain=[]),['c'+key])
for key,refs,authority in [('16',['10b:11'],'רבי אליעזר'),('20',['10b:15'],'רבי ישמעאל'),('35',['10b:30'],'רבי אלעזר ברבי שמעון')]:rec('aquote'+key,'attributions',refs,dict(surface=authority,role='quoted_authority',candidates=[authority],scope='Explicitly cited position',transmission_chain=[]),['c'+key])
for a,b,rel in [('2','1','objection'),('3','2','answer'),('4','3','objection'),('5','4','answer'),('6','5','objection'),('7','1','support'),('8','7','analogy'),('9','8','objection'),('10','1','support'),('12','11','answer'),('14','13','answer'),('16','15','answer'),('18','17','answer'),('20','19','answer'),('22','21','answer'),('24','23','answer'),('25','24','objection'),('26','25','answer'),('27','26','objection'),('28','27','answer'),('29','28','objection'),('30','23','answer'),('31','30','objection'),('32','31','answer'),('33','30','objection'),('34','33','answer'),('35','33','answer'),('38','37','qualification'),('39','35','support')]:
 refs=next(x[1] for x in D if x[0]==a);rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['10a:'+str(i) for i in range(17,23)]+['10b:'+str(i) for i in range(1,32)]
rec('s1','structure',refs[:11],dict(title='Eliezer–Yehoshua exchange: guilt-offering invalidity and replacement proofs',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[11:],dict(title='Alternative distinguishing features and guilt-offering blood-location derivation',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Source reread10a17–10b31 with10b32–11a11 context separating next inquiry. Preserve multiple revised proofs, karet/valuation/bird distinctions, anonymous alternative answers, Eliezer versus Elazar son of Shimon, and split cross-page speaker at10a22–10b1.' if layer=='reconciliation' else 'Manual source pass; '+('supported records listed.' if ids else 'No separate '+layer+' item after inspection; discourse preserved in other layers.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=5,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_10a17_10b31.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch4.json',r.encoded(res));print(res)
