import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_20261126';j,ss=r.load(job);rows={v['ref'].split(' ')[1]:v for v in ss.values()};state=r.current(job);R=[];prefix='zv.20261126.b3.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,content,links=[],unc=[],origin='source_paraphrase'):
 v=dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=content,origin=origin,uncertainty=unc,links=[prefix+x for x in links]);R.append(v);return key
# Static, manually authored source readings. Conditions are supplied explicitly.
D=[
('1',['6a:8'],'anonymous','inquiry','Do wrong-purpose offerings atone for what they originally came to atone, or not?','queried',['Offerings brought not for their designated purpose'],'Do they atone for their original purpose?'),
('2',['6a:9'],'רב ששת בריה דרב אידי','answer','It is reasonable that they do not atone, since if they atoned the second offering would have no purpose.','asserted',['First offering slaughtered not for its designated purpose'],None),
('3',['6a:10'],'anonymous','objection','If they do not atone, why is the first offering brought?','queried',['Assume first offering does not atone'],'Why is the first offering brought without atonement?'),
('4',['6a:11'],'רב אשי','clarification','Rav Ashi explains the earlier challenge: if the first did not atone it can derive its offering-status from the intended offering, and the second atones; if it did atone, the second has no purpose.','asserted',['First offering not for intended purpose; subsequent second offering'],None),
('5',['6a:12'],'anonymous','inquiry','Does a burnt offering atone for positive-commandment violations occurring after its designation?','queried',['Positive-commandment violation after designation of the offering'],'Does it atone for violations after designation?'),
('6',['6a:13'],'anonymous','alternative','Perhaps it is like a sin offering: only violations before designation are atoned, not those afterward.','hypothetical',['Analogy to sin offering; violation after designation'],None),
('7',['6a:14'],'anonymous','alternative','Perhaps it differs from a sin offering, which requires one offering per sin: since the burnt offering atones for multiple positive-commandment violations, it might atone for those after designation too.','hypothetical',['Burnt offering can atone for multiple positive-commandment violations'],None),
('8',['6a:15'],'anonymous citing baraita','proof_attempt','The laying-on-of-hands verse is interpreted: blood, not laying on hands, effects atonement; treating laying on hands as a nonessential remainder of the commandment is reckoned as not atoning, yet atoning.','asserted',['Offering made without the required laying on hands'],None),
('9',['6a:16'],'anonymous','interpretation','Does this not mean it atoned for prior positive-commandment violations but not the omitted laying on hands, a violation after designation?','hypothetical',['Omission of laying on hands; proposed interpretation'],'Does the baraita distinguish prior violations from the later omission of laying on hands?'),
('10',['6a:17'],'רבא','rejection','Laying on hands remains possible until slaughter; its violation becomes fixed only after slaughter, and the inquiry did not ask about violations after slaughter.','asserted',['Omission becomes final after slaughter'],None),
('11',['6a:18','6b:1'],'רב הונא בר יהודה','alternative_interpretation','Rav Huna bar Yehuda suggests to Rava: the person is atoned for, yet not fully atoned before Heaven.','asserted',['Baraita saying atoned and not atoned'],None),
('12',['6b:2'],'quoted Mishnah','support','For the remaining oil applied to the head, Rabbi Akiva says application atones and nonapplication does not; Rabbi Yohanan ben Nuri calls it a remainder of the commandment and says atonement occurs either way, yet is reckoned as not atoning.','asserted',['Leper purification; remaining oil applied or omitted'],None),
('13',['6b:3'],'anonymous','interpretation','The phrase as if not atoned cannot demand another offering, since the Mishnah says atonement occurs either way; it means atoned for the person but not before Heaven, and the same can explain the earlier baraita.','asserted',['Rabbi Yohanan ben Nuri\'s formulation; no additional offering required'],None),
('14',['6b:4'],'anonymous','alternative_interpretation','There too it can mean atonement for thumb applications but not head applications, rather than the proposed person/Heaven distinction.','asserted',['Alternative explanation of oil-application Mishnah'],None),
('15',['6b:5'],'ר׳ שמעון quoted','question','For what do the Shavuot lambs come?','queried',['Initial wording later corrected to goats'],'For what do the Shavuot lambs come?'),
('16',['6b:6'],'anonymous','text_correction','The Shavuot lambs are peace offerings; the question is corrected to ask about the Shavuot goats.','asserted',['Correction from lambs to goats'],'For what do the Shavuot goats come?'),
('17',['6b:7'],'ר׳ שמעון quoted continuation','answer','The goats come for impurity of the sanctuary and its consecrated things.','asserted',['Shavuot goats'],None),
('18',['6b:8'],'ר׳ שמעון quoted continuation','explanation','After the first goat\'s blood is sprinkled, the second comes for impurity occurring between the two; Israel would merit offerings at every time, but Scripture spared them.','asserted',['Second Shavuot goat; impurity between the sprinklings'],None),
('19',['6b:9'],'anonymous','proof_attempt','This appears to be atonement for a violation after designation.','asserted',['Shavuot goats; assumption both already designated'],None),
('20',['6b:10'],'anonymous','distinction','If both were designated together the inference would hold; the case can instead be successive designation.','asserted',['Successively designated goats; contrasted with simultaneous designation'],None),
('21',['6b:11'],'anonymous','objection','Can one force the scriptural provision to concern only successive designation?','queried',['Restriction to successive designation'],'Why restrict the verse to successively designated goats?'),
('22',['6b:12'],'רב פפא','distinction','Communal offerings differ because the court makes a condition about them; Rav Yehuda reports Shmuel that the knife determines communal offerings\' designation.','asserted',['Communal offerings; court condition determines allocation at slaughter'],None),
('23',['6b:13','7a:1'],'רב יוסף בריה דרב שמואל','objection','Does Rabbi Shimon accept the court\'s condition? A transmission from Rabbi Yohanan says unneeded communal daily offerings cannot be redeemed unblemished according to Rabbi Shimon, whereas the sages permit it.','challenged',['Unneeded communal daily offerings; unblemished animals'],'Does Rabbi Shimon accept a court condition?'),
('24',['7a:2'],'anonymous','additional_objection','Rabbi Yirmeya asked Rabbi Zeira about two Shavuot goats whose blood was received in two cups: after the first sprinkling, the second comes for impurity between them.','asserted',['Both goats slaughtered; blood received in two cups'],'What does the second goat atone for after the first sprinkling?'),
('25',['7a:3'],'anonymous','inference','His uncertainty concerns violations after slaughter; atonement for violations after designation seemed not to be in doubt.','asserted',['Inference from Rabbi Yirmeya\'s inquiry'],None),
('26',['7a:4'],'anonymous','qualification','Perhaps that inquiry was conditional on accepting atonement after designation; it therefore need not settle the present question.','hypothetical',['If-you-say conditional reading of the later inquiry'],None)]
for key,refs,voice,role,prop,mode,cond,q in D:
 unc=[]
 if key in ['2','4']:unc=['6a:9 names רב ששת בריה דרב אידי, while 6a:11 says רב שישא בריה דרב אידי; do not normalize the textual difference.']
 if key=='12':unc=['בן נורי is bracketed in the source; preserved as source reading, not external identity verification.']
 if key=='24':unc=['Parenthetical tail in 7a:2 is retained in evidence; inference follows the explicit main question and 7a:3–4.']
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['4','8','12','18','22','23','24'] else 'atomic'),unc=unc)
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Local atonement inquiry; alternatives and later qualification preserved',assertion_mode=mode),['u'+key],unc)
 if q:rec('q'+key,'questions',refs,dict(formulation=q,question_origin='explicit',conditions=cond,answer_set_status='unreviewed_alternatives' if key=='5' else 'partial'),['u'+key],unc)
 if voice not in ['anonymous','quoted Mishnah','anonymous citing baraita']:
  rolea='quoted_authority' if 'quoted' in voice else 'speaker'
  rec('a'+key,'attributions',refs,dict(surface=voice,role=rolea,candidates=[voice],scope='u'+key,transmission_chain=[]),['u'+key],unc)
 if mode in ['asserted','hypothetical']:
  holder=[] if voice.startswith('anonymous') or voice=='quoted Mishnah' else [voice]
  # The inquiry's proposed alternatives are genuine alternatives, not named positions.
  qid=prefix+'q5' if key in ['6','7'] else None
  rec('p'+key,'positions',refs,dict(holder_candidates=holder,claim_id=prefix+'c'+key,question_id=qid,conditions=cond,local_status='Proposed alternative, not settled' if mode=='hypothetical' else 'Local statement; objections and qualifications retained'),['c'+key]+(['q5'] if qid else []),unc)
# Atomic rules inside quoted composite passages, with exact scope and holders.
E=[
('8a',['6a:15'],'Blood effects atonement, not laying on hands.',['Sacrificial atonement'],'quoted baraita'),
('12a',['6b:2'],'If the remaining oil is applied, atonement occurs; if omitted, it does not.',['Remaining oil application to head'],'רבי עקיבא'),
('12b',['6b:2'],'Atonement occurs whether the remaining oil is applied or not, but omission is reckoned as nonatonement.',['Remaining oil application to head; omission is a remainder-of-commandment issue'],'רבי יוחנן [בן נורי]'),
('22a',['6b:12'],'The knife determines what communal offerings are designated as.',['Communal offerings; slaughter'],'שמואל'),
('23a',['6b:13','7a:1'],'Unneeded communal daily offerings cannot be redeemed while unblemished according to Rabbi Shimon.',['Daily offerings no longer needed by community; unblemished'],'רבי שמעון'),
('23b',['6b:13','7a:1'],'Unneeded communal daily offerings can be redeemed while unblemished according to the sages.',['Daily offerings no longer needed by community; unblemished'],'חכמים')]
for key,refs,prop,cond,holder in E:
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Quoted rule in local proof discussion',assertion_mode='asserted'))
 rec('p'+key,'positions',refs,dict(holder_candidates=[holder],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status='Quoted position, not independently adjudicated'),['c'+key])
 rec('a'+key,'attributions',refs,dict(surface=holder,role='quoted_authority',candidates=[holder],scope=prop,transmission_chain=[]),['c'+key])
for key,refs,surface,chain,links in [('22t',['6b:12'],'רב יהודה אמר שמואל',['רב יהודה','שמואל'],['c22a']),('23t',['6b:13'],'רב אידי בר אבין אמר רב עמרם אמר רבי יצחק אמר רבי יוחנן',['רב אידי בר אבין','רב עמרם','רבי יצחק','רבי יוחנן'],['c23a','c23b']),('24t',['7a:2'],'בעא מיניה ר׳ ירמיה מר׳ זירא',['רבי ירמיה','רבי זירא'],['q24'])]:
 rec('a'+key,'attributions',refs,dict(surface=surface,role='transmitter' if key!='24t' else 'speaker',candidates=[chain[0]],scope='Reporting chain' if key!='24t' else 'Questioner first, addressee second; not a report chain',transmission_chain=chain if key!='24t' else []),links)
for a,b,rel in [('2','1','answer'),('3','2','objection'),('4','3','answer'),('6','5','answer'),('7','5','answer'),('8','5','support'),('9','8','qualification'),('10','9','objection'),('11','9','distinction'),('12','11','support'),('13','12','qualification'),('14','13','objection'),('16','15','correction'),('17','16','answer'),('18','17','qualification'),('19','5','support'),('20','19','objection'),('21','20','objection'),('22','21','answer'),('23','22','objection'),('24','20','objection'),('25','24','qualification'),('26','25','qualification')]:
 refs=next(x[1] for x in D if x[0]==a)
 rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['6a:'+str(i) for i in range(8,19)]+['6b:'+str(i) for i in range(1,14)]+['7a:'+str(i) for i in range(1,5)]
rec('s1','structure',refs[:4],dict(title='Whether wrong-purpose offerings atone for their original purpose',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
rec('s2','structure',refs[4:],dict(title='Post-designation violations: proof attempts, distinctions and unresolved conditional inquiry',primary=True,boundary='closed',legacy_ids=[]),unc=['Local discussion closes with a possible conditional reading, not a final binary ruling.'],origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Re-read complete continuation through 7a:4 and next topic 7a:5–6; preserve 6a:18–6b:1 and 6b:13–7a:1 syntax, alternative designation dates, corrected lamb/goat wording, transmissions and conditional ending without forcing resolution.' if layer=='reconciliation' else 'Manual source pass: '+('listed supported records.' if ids else 'No separate '+layer+' item after inspection; anonymous or quoted continuity preserved in utterances.')
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=3,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_6a8_7a4.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch3.json',r.encoded(res));print(res)
