from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.partialsigns.20261126w3.'
assert r.sha(r.encoded(state))=='e18210c51d8e3d60d0dc41f8ae704a71f170efba55404a862910e189322ed4f3'
refs=['6a:'+str(n) for n in range(10,20)]
add('s','structure',refs,dict(title='Partial maternal signs across pure and impure species: conditional inquiries and proof limits',primary=True,boundary='closed',legacy_ids=[]))
for n,role in [(10,'Initial partial-signs inquiry'),(11,'Known sheep/goat baseline'),(12,'Competing reasons in cow/donkey case'),(13,'Conditional donkey/horse inquiry'),(14,'Further conditional cow/horse inquiry'),(15,'Baraita proof and restriction'),(16,'Second baraita proof and restricted clause scope'),(17,'Redundancy objection'),(18,'Initial hypothetical distinguishing signs'),(19,'Horse-like donkey offspring exclusion despite similarity')]:add('u'+str(n),'utterances',['6a:'+str(n)],dict(textual_voice='Anonymous Gemara with cited baraitot',discourse_role=role,composition='composite'))
q('q10','6a:10','Does a cow’s donkey-kind offspring with some maternal signs have firstborn sanctity?')
c('c11','6a:11','For sheep/goat kind interchange, partial maternal signs incur firstborn liability; both species are pure and bear bodily sanctity.',cond=['Sheep or goat mother and goat or sheep kind offspring','Some maternal signs'])
c('c12no','6a:12','One possible answer denies sanctity in cow/donkey interchange because pure and impure kinds, and bodily and monetary sanctity, differ.',mode='hypothetical',cond=['Cow produces donkey-kind offspring with some maternal signs'])
c('c12yes','6a:12','The alternative would confer sanctity because both kinds can bear firstborn sanctity.',mode='hypothetical',cond=['Cow produces donkey-kind offspring with some maternal signs'])
q('q13','6a:13','Assuming cow/donkey sanctity, what of donkey offspring of horse-kind with partial maternal signs?')
rows[-1]['content']['conditions']=['Conditional on affirmative answer to cow/donkey inquiry','Partial maternal signs in continuing inquiry']
c('c13no','6a:13','One alternative excludes donkey/horse offspring because horse-kind cannot bear firstborn sanctity.',mode='hypothetical',cond=['Affirmative cow/donkey premise','Donkey produces horse-kind offspring with some maternal signs'])
c('c13yes','6a:13','The alternative would confer sanctity because the mother and offspring are both impure kinds.',mode='hypothetical',cond=['Affirmative cow/donkey premise','Donkey produces horse-kind offspring with some maternal signs'])
q('q14','6a:14','Assuming donkey/horse sanctity, what of a cow’s horse-kind offspring with partial maternal signs?')
rows[-1]['content']['conditions']=['Conditional on affirmative donkey/horse answer','Partial maternal signs in continuing inquiry']
c('c14no','6a:14','One alternative excludes cow/horse offspring because purity status and capacity for firstborn sanctity both differ.',mode='hypothetical',cond=['Affirmative donkey/horse premise','Cow produces horse-kind offspring with some maternal signs'])
c('c14yes','6a:14','The alternative would treat the maternal signs as sufficient.',mode='hypothetical',cond=['Affirmative donkey/horse premise','Cow produces horse-kind offspring with some maternal signs'])
c('c15rule','6a:15','The cited baraita exempts a pure animal’s impure-kind offspring but imposes firstborn liability if some maternal signs are present.',cond=['Pure mother','Impure-kind offspring','Partial signs determine exception scope'])
q('q15','6a:15','Does that baraita include a cow’s horse-kind offspring?')
c('c15limit','6a:15','The answer restricts the baraita’s partial-signs case to a cow producing donkey-kind offspring.',cond=['Cow produces donkey-kind offspring with some maternal signs'])
c('c16cow','6a:16','The second baraita exempts cow/donkey offspring in its initial clause.',cond=['Cow produces donkey-kind offspring','Subject to partial-signs exception'])
c('c16donkey','6a:16','The second baraita exempts donkey/horse offspring in its initial clause.',cond=['Donkey produces horse-kind offspring'])
c('c16sign','6a:16','Its next clause imposes liability when some maternal signs are present.')
q('q16','6a:16','Does the partial-signs liability clause apply to both preceding cases?')
c('c16limit','6a:16','The reply applies the liability clause only to cow/donkey offspring.',cond=['Cow produces donkey-kind offspring with some maternal signs'])
q('q17','6a:17','Why state the donkey/horse exemption, when even the more sanctifiable cow/donkey pair needs maternal signs?')
c('c18','6a:18','A possible distinction invokes horns and split versus unsplit hooves in the cow/donkey pair.',mode='hypothetical')
c('c19hyp','6a:19','One might regard donkey/horse offspring as merely a red donkey because both have no horns and unsplit hooves.',mode='hypothetical')
c('c19result','6a:19','The stated exemption is needed to reject treating donkey/horse offspring as merely a differently colored donkey.')
for k,ref,cl,qu,st in [('p12n','6a:12','c12no','q10','Unadopted inquiry branch'),('p12y','6a:12','c12yes','q10','Inquiry branch, later cow/donkey qualification supports liability'),('p13n','6a:13','c13no','q13','Conditional inquiry branch'),('p13y','6a:13','c13yes','q13','Conditional inquiry branch, not a ruling'),('p14n','6a:14','c14no','q14','Conditional inquiry branch'),('p14y','6a:14','c14yes','q14','Conditional inquiry branch, attempted proof restricted'),('p15','6a:15','c15limit','q15','Restricted proof scope'),('p16','6a:16','c16limit','q16','Restricted liability clause scope'),('p19','6a:19','c19result','q17','Local explanatory answer')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,['Anonymous Gemara'],st,qu,cr['content']['conditions'],['Conditional branches do not establish affirmative rulings for subsequent cases.'] if 'branch' in st else [])
for k,ref,a,b,rel in [('e12n','6a:12','c12no','q10','answer'),('e12y','6a:12','c12yes','q10','answer'),('e13n','6a:13','c13no','q13','answer'),('e13y','6a:13','c13yes','q13','answer'),('e14n','6a:14','c14no','q14','answer'),('e14y','6a:14','c14yes','q14','answer'),('e15','6a:15','c15limit','q15','answer'),('e15q','6a:15','c15limit','c15rule','qualification'),('e16','6a:16','c16limit','q16','answer'),('e16q','6a:16','c16limit','c16sign','qualification'),('e17','6a:17','q17','c16donkey','objection'),('e18','6a:18','c18','c19hyp','support'),('e19','6a:19','c19result','q17','answer'),('e19h','6a:19','c19result','c19hyp','objection')]:edge(k,ref,a,b,rel)
# Link the explicit continuation qualification back to preserved Mishnah claim and position.
for k,target in [('epriorclaim','beh.kinds.20261126w3.c7cow'),('epriorposition','beh.kinds.20261126w3.p7c')]:
 add(k,'edges',['6a:15','6a:16'],dict(source_id=pre+'c16limit',target_id=target,relation='qualification',explicitness='source_explicit'))
 rows[-1]['links']=[pre+'c16limit',target]
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Partial-maternal-sign inquiries. If-you-say premises remain conditional. Proof restrictions distinguish cow/donkey, donkey/horse and cow/horse; no universal affirmative outcome inferred.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source and omission reread6a10–22; later6b1–7a24 checked for continuation. Three conditional cases, alternatives, two proof restrictions and exemption rationale preserved. Earlier general cow exemption explicitly qualified by continuation. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch14_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch14_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch14_receipt.json',r.encoded(out));print(r.encoded(out).decode())
