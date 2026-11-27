from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.moneytransfer.20261127w3.'
assert r.sha(r.encoded(state))=='0bfc69e75370e520b2e8bf51bcd482bda6945443d012a48adae126a25fbf202b'
refs=['13a:'+str(n) for n in range(13,27)]+['13b:1']
add('s','structure',refs,dict(title='Money transfer between Israelite and gentile: two directions, rejected personal-status analogies and Abaye’s derivations',primary=True,boundary='closed',legacy_ids=[]))
c('c13buy','13a:13','Rabbi Yitzhak bar Nahmani reports Resh Lakish in Rabbi Oshaya’s name: an Israelite who pays a gentile for the gentile’s animal acquires it under the stated law even without drawing it.',cond=['Israelite buyer','Gentile seller','Money paid','No drawing performed'])
c('c13liable','13a:13','The acquired animal is liable in firstborn status.',cond=['Same Israelite-from-gentile money acquisition'])
c('c13sell','13a:13','In the converse case a gentile who pays an Israelite acquires the animal even without drawing it.',cond=['Gentile buyer','Israelite seller','Money paid','No drawing performed'])
c('c13exempt','13a:13','The acquired animal is exempt from firstborn status.',cond=['Same gentile-from-Israelite money acquisition'])
c('c14','13a:14','The Gemara repeats the Israelite-buyer money-acquisition ruling as the first target of explanation.')
q('q15','13a:15','What does under their laws mean for Israelite acquisition from a gentile?')
c('c15hyp','13a:15','A proposed interpretation derives money acquisition of property from money acquisition of the person by an a-fortiori argument.',mode='hypothetical')
c('c16land','13a:16','The cited inheritance-possession analogy makes acquisition of a Canaanite slave analogous to landed property.')
c('c16money','13a:16','Money is one of the stated acquisition modes in that analogy.')
c('c16document','13a:16','A document is another stated acquisition mode.')
c('c16possession','13a:16','Possession is another stated acquisition mode.')
q('q17modes','13a:17','Would that argument not also allow property acquisition by document and possession?')
c('c17counter','13a:17','Israelite-to-Israelite transfer is a counterexample: personal acquisition can use money while property uses drawing.')
c('c18','13a:18','Abaye instead reads the Torah’s from your fellow as assigning drawing to acquisition from an Israelite and money to acquisition from a gentile.')
q('q19','13a:19','Could the exclusion instead mean that nothing is acquired from a gentile?')
c('c19','13a:19','The answer rejects total nonacquisition by the a-fortiori argument that if the person can be acquired, property can be acquired.')
q('q20both','13a:20','Could acquiring a gentile’s property require both money and drawing?')
c('c20both','13a:20','The answer rejects requiring two modes for property when personal acquisition needs one.')
q('q20either','13a:20','Could either money or drawing suffice?')
c('c21','13a:21','The analogy to your fellow requires a single acquisition mode rather than either of two alternatives.')
q('q22','13a:22','What does under their laws mean for a gentile buying an Israelite’s animal?')
c('c22hyp','13a:22','The proposed interpretation derives money purchase of property from the gentile’s money acquisition of the Israelite person.',mode='hypothetical')
c('c23counter','13a:23','Israelite-to-Israelite transfer again defeats that inference because personal and property acquisition modes differ.')
c('c23abaye','13a:23','Abaye instead reads sale to your fellow as requiring drawing for sale to an Israelite and money for sale to a gentile.')
q('q24','13a:24','Could the exclusion mean no acquisition by a gentile at all?')
c('c24','13a:24','The answer rejects that by the a-fortiori argument from acquiring the person to acquiring property.')
q('q25','13a:25','Could sale to a gentile require both money and drawing?')
c('c25','13a:25','The answer rejects two modes for property when acquisition of the person requires one.')
q('q26','13a:26','Could either money or drawing suffice for that sale?')
c('c26','13a:26','The response invokes analogy to your fellow.')
c('c1','13b:1','As acquisition by your fellow uses one mode, acquisition by the gentile uses one mode.')
for ref,v,role in [('13a:13','Rabbi Yitzhak bar Nahmani through Resh Lakish in Rabbi Oshaya name','Two-direction transfer rule'),('13a:14','Anonymous Gemara','Repeats first direction'),('13a:15','Anonymous Gemara','Initial personal-acquisition argument'),('13a:16','Anonymous exposition','Possession analogy'),('13a:17','Anonymous objections','Other modes and counterexample'),('13a:18','Abaye','From-your-fellow derivation'),('13a:19','Anonymous exchange','Total nonacquisition rejected'),('13a:20','Anonymous exchange','Both-modes and either-mode proposals'),('13a:21','Anonymous answer','Single-mode analogy'),('13a:22','Anonymous Gemara','Second-direction initial argument'),('13a:23','Anonymous objection and Abaye','Counterexample and to-your-fellow derivation'),('13a:24','Anonymous exchange','Total nonacquisition rejected'),('13a:25','Anonymous exchange','Both-modes proposal rejected'),('13a:26','Anonymous exchange','Either-mode proposal and answer begins'),('13b:1','Anonymous answer continuation','Single-mode analogy completed')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
chain=['רבי יצחק בר נחמני','ריש לקיש','רבי אושעיא']
att('a13i','13a:13',"ר' יצחק בר נחמני",'transmitter',[chain[0]],'Two-direction money acquisition',chain)
att('a13rl','13a:13','ריש לקיש','transmitter',[chain[1]],'Two-direction money acquisition',chain)
att('a13o','13a:13',"ר' אושעיא",'quoted_authority',[chain[2]],'Two-direction money acquisition',chain)
att('a18','13a:18','אביי','speaker',['אביי'],'First-direction derivation')
att('a23','13a:23','אביי','speaker',['אביי'],'Second-direction derivation')
for k,ref,cl,h,st,qu in [('p13buy','13a:13','c13buy',['רבי אושעיא via ריש לקיש and רבי יצחק בר נחמני'],'Reported acquisition',None),('p13liable','13a:13','c13liable',['רבי אושעיא via ריש לקיש and רבי יצחק בר נחמני'],'Firstborn consequence',None),('p13sell','13a:13','c13sell',['רבי אושעיא via ריש לקיש and רבי יצחק בר נחמני'],'Reported acquisition',None),('p13exempt','13a:13','c13exempt',['רבי אושעיא via ריש לקיש and רבי יצחק בר נחמני'],'Firstborn consequence',None),('p15','13a:15','c15hyp',['Anonymous Gemara'],'Rejected initial derivation','q15'),('p18','13a:18','c18',['אביי'],'Replacement derivation','q15'),('p22','13a:22','c22hyp',['Anonymous Gemara'],'Rejected initial derivation','q22'),('p23','13a:23','c23abaye',['אביי'],'Replacement derivation','q22')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e13b','13a:13','c13buy','c13liable','support'),('e13s','13a:13','c13sell','c13exempt','support'),('e15','13a:15','c15hyp','q15','answer'),('e16','13a:16','c16money','c15hyp','support'),('e17m','13a:17','q17modes','c15hyp','objection'),('e17c','13a:17','c17counter','c15hyp','objection'),('e18','13a:18','c18','q15','answer'),('e19','13a:19','c19','q19','answer'),('e20','13a:20','c20both','q20both','answer'),('e21','13a:21','c21','q20either','answer'),('e22','13a:22','c22hyp','q22','answer'),('e23c','13a:23','c23counter','c22hyp','objection'),('e23a','13a:23','c23abaye','q22','answer'),('e24','13a:24','c24','q24','answer'),('e25','13a:25','c25','q25','answer'),('e1','13b:1','c1','q26','answer')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Historical source argument concerning acquisition modes and firstborn ownership, not present legal advice or endorsement of personal enslavement. Both transfer directions and every rejected candidate derivation remain separate. Later Amemar alternative still to be recorded separately.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read13a13–14a9 and omission reread13a13–13b1. Both transaction directions, acquisition and firstborn consequences, three-member transmission chain, rejected personal-status argument and no/both/either-mode alternatives preserved. Page-break final answer included. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch31_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch31_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch31_receipt.json',r.encoded(out));print(r.encoded(out).decode())
