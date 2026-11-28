import sys
from pathlib import Path
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1');import runner as r
job=Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_zevachim');out=job/'worker_20261126';j,ss=r.load(job);rows={v['ref'].split(' ')[1]:v for v in ss.values()};state=r.current(job);R=[];prefix='zv.20261126.b2.'
def ev(ref):
 s=rows[ref];return dict(segment_id=s['id'],start_char=0,end_char=len(s['text']),quote=s['text'])
def rec(key,layer,refs,content,links=[],unc=[],origin='source_paraphrase'):
 v=dict(id=prefix+key,layer=layer,evidence=[ev(x) for x in refs],content=content,origin=origin,uncertainty=unc,links=[prefix+x for x in links]);R.append(v);return key
# Manually authored semantic rows; multi-segment units preserve split syntax.
D=[
('8',['5b:8'],'רב הונא ורב נחמן','question','Rav Huna and Rav Nahman ask why the respondent did not answer Resh Lakish that the guilt offering too comes after death.','queried',['Resh Lakish\'s earlier guilt-offering objection'],'Why not answer that the guilt offering too comes after death?'),
('9',['5b:9'],'רב ששת','objection','The guilt offering comes only as its surplus; the sin offering\'s surplus likewise comes, so surplus alone does not establish the proposed distinction.','asserted',['After owner\'s death; surplus offering'],None),
('10',['5b:10'],'anonymous','reply','Although the sin offering\'s surplus comes, the restrictive הוא excludes the sin offering itself.','asserted',['Sin offering; proposed explanation for wrong-purpose invalidity'],None),
('11',['5b:11'],'anonymous','objection','The guilt offering too contains הוא, challenging the restriction to sin offerings.','challenged',['Guilt offering contains the same restrictive term'],'Does not the guilt offering also contain הוא?'),
('12',['5b:12'],'anonymous','reply','The guilt offering\'s הוא is written after burning its portions; even omission of burning those portions does not invalidate the offering itself.','asserted',['Guilt offering; omission of burning portions'],None),
('13',['5b:13'],'anonymous','question_and_answer','הוא instead serves Rav\'s law transmitted by Rav Huna: a guilt offering assigned to grazing and slaughtered without specification is valid.','conditional',['Guilt offering already assigned to grazing; slaughtered without specification'],'What then is the purpose of הוא?'),
('14',['5b:14'],'anonymous','qualification','The validity requires prior assignment to grazing; without it, no. הוא requires retention of its existing status.','asserted',['Guilt offering not yet assigned to grazing'],'Why is prior assignment necessary?'),
('15',['5b:15'],'רב נחמן ורב ששת','question','Rav Nahman and Rav Sheshet ask why Resh Lakish did not reply to Rabbi Elazar that posthumous offerings too should come and discharge.','queried',['Offerings after death'],'Why should posthumous offerings not also discharge?'),
('16',['5b:16'],'רב אדא בר מתנה','reply','The mother gave birth; her sons did not, so they do not have her childbirth obligation.','asserted',['Postpartum offering after the mother\'s death'],None),
('17',['5b:17'],'רב אסי','objection','The burnt offering might atone for several positive-commandment violations of the mother; if so, heirs too might obtain atonement.','hypothetical',['Burnt offering could atone for positive-commandment violations'],'Who establishes that the mother\'s additional positive-commandment violations would not be atoned?'),
('18',['5b:18'],'anonymous','objection','Does this imply heirs acquire the offering? Rabbi Yohanan says an inherited meal offering is brought for two sons without partnership; ownership by both would conflict with נפש.','challenged',['Father leaves meal offering to two sons and dies'],'Does the offering become the heirs\' property?'),
('19',['5b:19','6a:1'],'anonymous','counter_objection','If heirs do not acquire it, why does Rabbi Yohanan prohibit substitution for an inherited animal? Acquisition as partners would explain the prohibition; without acquisition they should be able to substitute.','hypothetical',['Father leaves animal offering to two sons and dies'],'If they do not acquire the offering, why can they not substitute?'),
('20',['6a:2'],'anonymous','reply','אם המר ימיר includes an heir but permits one heir to substitute, not two, independently answering the substitution objection.','asserted',['Inheritance; one versus two heirs'],None),
('21',['6a:3'],'רב יעקב מנהר פקוד','objection','Would the parallel inclusion of heirs in ואם גאל יגאל imply that one heir can redeem tithe but two cannot?','queried',['Parallel inference for redemption of inherited tithe'],'Would two heirs be barred from redeeming tithe?'),
('22',['6a:4'],'anonymous','distinction','Tithe differs because partnership is possible already in the fathers\' ownership.','asserted',['Tithe compared to substitution'],None),
('23',['6a:5'],'רב אסי','objection','If the heir acquires the offering, one heir\'s substitution is intelligible; without acquisition, how can even one substitute?','queried',['Single heir; interlocutor Rav Ashi'],'How can a single heir substitute without acquisition?'),
('24',['6a:6'],'anonymous citing רבי אבהו אמר ר׳ יוחנן','citation','Rabbi Abbahu reports Rabbi Yohanan: the consecrator adds the fifth, the person obtaining atonement makes substitution, and one who tithes his own produce for another retains the benefit of choosing the recipient.','asserted',['Distinct roles of consecrator, atonement beneficiary, and donor'],None),
('25',['6a:7'],'anonymous','distinction','The heirs do not receive primary fixed atonement but do receive incidental atonement.','asserted',['Inherited offering; distinction resolves acquisition/substitution challenge'],None)]
for key,refs,voice,role,prop,mode,cond,q in D:
 rec('u'+key,'utterances',refs,dict(textual_voice=voice,discourse_role=role,composition='composite' if key in ['13','18','19','24'] else 'atomic'))
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Posthumous offerings and heirs; local argument',assertion_mode=mode),['u'+key])
 if q:rec('q'+key,'questions',refs,dict(formulation=q,question_origin='explicit',conditions=cond,answer_set_status='partial'),['u'+key])
 if voice!='anonymous' and key!='24':rec('a'+key,'attributions',refs,dict(surface=voice,role='speaker',candidates=[voice],scope='u'+key,transmission_chain=[]),['u'+key])
 if mode in ['asserted','conditional']:
  holders=[] if voice=='anonymous' or key=='24' else [voice]
  if key=='13':holders=['רב']
  rec('p'+key,'positions',refs,dict(holder_candidates=holders,claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status='Local response or cited rule; objections retained separately'),['c'+key])
# Named transmission, direct addressee kept distinct from holder.
rec('a13','attributions',['5b:13'],dict(surface='רב הונא אמר רב',role='transmitter',candidates=['רב הונא'],scope='Guilt offering assigned to grazing',transmission_chain=['רב הונא','רב']),['c13'])
rec('a13h','attributions',['5b:13'],dict(surface='רב',role='position_holder',candidates=['רב'],scope='Validity after grazing assignment',transmission_chain=[]),['c13'])
rec('a15quote','attributions',['5b:15'],dict(surface='רבי אלעזר',role='quoted_authority',candidates=['רבי אלעזר'],scope='Earlier posthumous offering analogy',transmission_chain=[]),['u15'],['Earlier 5a:3 prints ר׳ אליעזר; preserve different surface without deciding identity.'])
rec('a24','attributions',['6a:6'],dict(surface='רבי אבהו אמר ר׳ יוחנן',role='transmitter',candidates=['רבי אבהו'],scope='Three separate ownership/benefit rules',transmission_chain=['רבי אבהו','רבי יוחנן']),['c24'])
rec('a24h','attributions',['6a:6'],dict(surface='ר׳ יוחנן',role='quoted_authority',candidates=['רבי יוחנן'],scope='Rules quoted to support objection',transmission_chain=[]),['c24'])
# Quoted component rulings separated from the surrounding objections.
extra=[('18q',['5b:18'],'An inherited meal offering is brought after the father dies leaving it to two sons, and is not treated as jointly owned.',['Meal offering; two sons; father died'],'רבי יוחנן'),('19q',['5b:19'],'An inherited animal offering is brought after the father dies leaving it to two sons, but they cannot make substitution.',['Animal offering; two sons; father died'],'רבי יוחנן'),('24a',['6a:6'],'The consecrator adds the fifth.',['Redemption by the consecrator'],'רבי יוחנן'),('24b',['6a:6'],'The atonement beneficiary makes substitution.',['Person for whom atonement occurs'],'רבי יוחנן'),('24c',['6a:6'],'One tithing his own produce for another retains the benefit of choosing the recipient.',['His own produce used to tithe for another'],'רבי יוחנן')]
for key,refs,prop,cond,holder in extra:
 rec('c'+key,'claims',refs,dict(proposition=prop,conditions=cond,scope='Explicit quoted rule',assertion_mode='asserted'))
 rec('p'+key,'positions',refs,dict(holder_candidates=[holder],claim_id=prefix+'c'+key,question_id=None,conditions=cond,local_status='Quoted dictum; application is debated'),['c'+key])
 if key in ['18q','19q']:rec('a'+key,'attributions',refs,dict(surface='רבי יוחנן',role='quoted_authority',candidates=[holder],scope=prop,transmission_chain=[]),['c'+key])
# Mnemonic belongs to structure and utterance, not a fabricated claim.
rec('u7','utterances',['5b:7'],dict(textual_voice='anonymous textual mnemonic',discourse_role='mnemonic',composition='atomic'),origin='literal')
for a,b,rel in [('9','8','objection'),('10','9','answer'),('11','10','objection'),('12','11','answer'),('13','12','qualification'),('14','13','qualification'),('16','15','answer'),('17','16','objection'),('18','17','objection'),('18q','18','support'),('19','18','objection'),('19q','19','support'),('20','19','answer'),('21','20','objection'),('22','21','answer'),('23','20','objection'),('24b','23','support'),('25','23','answer')]:
 refs=next(x[1] for x in (D+extra) if x[0]==a)
 rec('e'+a+'_'+b,'edges',refs,dict(source_id=prefix+'c'+a,target_id=prefix+'c'+b,relation=rel,explicitness='source_explicit'),['c'+a,'c'+b])
refs=['5b:'+str(i) for i in range(7,20)]+['6a:'+str(i) for i in range(1,8)]
for k,title,part in [('s0','Mnemonic for ensuing discussions',refs[:1]),('s1','Posthumous guilt-offering surplus and the term הוא',refs[1:8]),('s2','Heirs: acquisition, substitution, primary and incidental atonement',refs[8:])]:rec(k,'structure',part,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
C=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in R if x['layer']==layer and any(e['segment_id']==rows[ref]['id'] for e in x['evidence'])]
  why='Reread original through 6a:7 closure; verified split 5b:19–6a:1, anonymous replies, Rav versus Rav Asi, named transmission, two-heir conditions and retrospective 5a discussion. Next independent inquiry starts 6a:8.' if layer=='reconciliation' else 'Manual source pass: '+('source-supported records listed.' if ids else ('Mnemonic has no semantic '+layer+' assertion.' if ref=='5b:7' else 'No separate '+layer+' item found; voice, conditional/rejected status and argument recorded in appropriate layers.'))
  C.append(dict(segment_id=rows[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/zevachim_resume',epoch=3,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root/zevachim_resume',model_id=None),records=R,coverage=C,open_tails=[])
r.validate_apply(state,p,ss,j);path=out/'proposal_5b7_6a7.json';r.immutable(path,r.encoded(p));res=r.submit(job,path,p['owner'],p['epoch']);r.immutable(out/'receipt_batch2.json',r.encoded(res));print(res)
