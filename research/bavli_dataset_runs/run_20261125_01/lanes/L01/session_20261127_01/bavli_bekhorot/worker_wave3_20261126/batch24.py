from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.neckbreak.20261126w3.'
assert r.sha(r.encoded(state))=='91f4e31719051cc91b41d69a064348a902ba6465fd25e2de305900af1838e705'
refs=['10b:'+str(n) for n in range(9,28)]
add('s1','structure',refs[:16],dict(title='Post-neck-breaking benefit: baraita reinterpretations, failed proofs and explicit amoraic disagreement',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[16:],dict(title='Alternative betrothal report placements and one-shekel case',primary=True,boundary='closed',legacy_ids=[]))
for n,v,role in [(9,'Anonymous objection with baraita','Apparent post-neck-breaking dispute'),(10,'Anonymous answer','Reinterpretation as lifetime benefit'),(11,'Anonymous Gemara','Later clause seems to imply different initial scope'),(12,'Quoted baraita','Death methods and shearing/work dispute'),(13,'Anonymous answer','Both clauses lifetime, value/body distinction'),(14,'Anonymous explanation','Both clauses necessary'),(15,'Rav Nahman reporting Rabba bar Avuha','Post-neck-breaking concession'),(16,'Rav Nahman','Neck-breaking analogy proof'),(17,'Rav Nahman inference','Assigns baraita to RabbiShimon'),(18,'Rav Sheshet reporting Safra’s interpretation','RabbiYehuda alternative defeats inference'),(19,'Rav Nahman citing Levi','Priest-loss punishment proof'),(20,'Rav Nahman inference','Assigns loss rationale to RabbiShimon'),(21,'Anonymous answer','Both tannaitic assignments possible'),(22,'Anonymous explanation','RabbiYehuda surplus-value loss'),(23,'Anonymous explanation','RabbiShimon death depreciation'),(24,'Resh Lakish; Rabbi Yohanan or Rabbi Elazar','Explicit disagreement after neck-breaking'),(25,'Alternative report: Rav Nahman via Rabba bar Avuha','Betrothal Mishnah assigned to after neck-breaking'),(26,'Another version','Neither tanna seems to fit betrothal Mishnah'),(27,'Rabba bar Avuha reporting Rav','RabbiYehuda at exact-shekel value and RabbiYoseBarYehuda minimum')]:add('u'+str(n),'utterances',['10b:'+str(n)],dict(textual_voice=v,discourse_role=role,composition='composite'))
c('c9method','10b:9','The baraita requires one unwilling to redeem to break the donkey’s neck from behind with a cleaver.')
c('c9bury','10b:9','It requires burial.')
c('c9y','10b:9','Its Rabbi Yehuda clause prohibits benefit, initially read as after neck-breaking.',mode='challenged')
c('c9s','10b:9','Its Rabbi Shimon clause permits benefit, initially read as after neck-breaking.',mode='challenged')
c('c10','10b:10','The reply reads the benefit prohibition and permission as referring to the living donkey.')
q('q11','10b:11','If the later clause concerns the living donkey, should the earlier clause not concern after death?')
for k,method in [('reed','reed'),('sickle','sickle'),('axe','axe'),('saw','saw')]:c('c12'+k,'10b:12','The later baraita forbids killing it with a '+method+'.')
c('c12room','10b:12','It forbids shutting it in a room to cause its death.')
c('c12yshear','10b:12','Rabbi Yehuda forbids shearing it.')
c('c12ywork','10b:12','Rabbi Yehuda forbids working it.')
c('c12sshear','10b:12','Rabbi Shimon permits shearing it.')
c('c12swork','10b:12','Rabbi Shimon permits working it.')
c('c13first','10b:13','The answer makes the first clause lifetime benefit from its monetary value.')
c('c13last','10b:13','It makes the second clause lifetime benefit from its body.')
c('c14s','10b:14','Without the body-benefit clause one might limit Rabbi Shimon’s permission to monetary benefit.',mode='hypothetical')
c('c14y','10b:14','Without the monetary clause one might limit Rabbi Yehuda’s prohibition to bodily benefit.',mode='hypothetical')
c('c15','10b:15','Rav Nahman reports Rabba bar Avuha’s view that Rabbi Shimon concedes prohibition after neck-breaking.')
c('c16','10b:16','The cited baraita derives prohibition here from the shared neck-breaking term with the heifer.')
c('c17','10b:17','The proposed proof assigns the baraita to Rabbi Shimon because Rabbi Yehuda already prohibits benefit while alive.',mode='challenged')
c('c18assign','10b:18','Rav Sheshet reports Safra’s interpretation assigning the baraita to Rabbi Yehuda.')
c('c18hyp','10b:18','One might otherwise suppose neck-breaking substitutes for redemption and permits the donkey just as redemption does.',mode='hypothetical')
c('c18result','10b:18','The analogy rules out that supposed permission.')
c('c19','10b:19','Levi teaches that because the owner caused loss of the priest’s property, his own property is to be lost.')
c('c20','10b:20','Rav Nahman infers Rabbi Shimon must be intended because Rabbi Yehuda already treats the property as lost through prohibition.',mode='challenged')
c('c21','10b:21','The answer permits assigning Levi’s statement either to Rabbi Yehuda or to Rabbi Shimon.')
c('c22','10b:22','On the Rabbi Yehuda assignment, the owner loses the surplus between the donkey’s value and redemption cost.')
c('c23','10b:23','On the Rabbi Shimon assignment, the owner loses the depreciation caused by death.')
c('c24rl','10b:24','Resh Lakish likewise says Rabbi Shimon concedes prohibition after neck-breaking.')
c('c24other','10b:24','Rabbi Yohanan, or alternatively Rabbi Elazar, says the tannaitic dispute continues after neck-breaking.')
rows[-1]['uncertainty'].append('Explicit ואי תימא alternative attribution preserved; no single holder selected.')
c('c25m','10b:25','The cited Mishnah says betrothal with a firstborn donkey does not take effect.')
q('q25','10b:25','Does that Mishnah exclude Rabbi Shimon?')
c('c25answer','10b:25','This report version places Rav Nahman’s Rabba bar Avuha teaching here: the Mishnah is after neck-breaking and accords with all.')
c('c26s','10b:26','The other version argues Rabbi Shimon should allow betrothal with its whole value.',mode='hypothetical')
c('c26y','10b:26','It argues Rabbi Yehuda should allow betrothal with the surplus value.',mode='hypothetical')
q('q26','10b:26','How can the betrothal Mishnah fit either tanna?')
c('c27case','10b:27','Rabba bar Avuha in Rav’s name assigns it to Rabbi Yehuda when the donkey is worth only a shekel and the view follows Rabbi Yose bar Yehuda’s minimum.',cond=['Donkey worth one shekel','RabbiYehuda benefit prohibition','RabbiYoseBarYehuda minimum redemption one shekel'])
c('c27immediate','10b:27','The first baraita view derives immediate redemption from repeated redeem wording.')
c('c27any','10b:27','It derives redemption at any amount.')
c('c27min','10b:27','Rabbi Yose bar Yehuda says redemption cannot be less than a shekel.')
for k,ref,surf,role,cands,scope,chain in [('a9y','10b:9','רבי יהודה','quoted_authority',['רבי יהודה'],'Benefit prohibition',[]),('a9s','10b:9','רבי שמעון','quoted_authority',['רבי שמעון'],'Benefit permission',[]),('a15n','10b:15','רב נחמן','transmitter',['רב נחמן'],'Concession after neck-breaking',['רב נחמן','רבה בר אבוה']),('a15r','10b:15','רבה בר אבוה','quoted_authority',['רבה בר אבוה'],'Concession after neck-breaking',['רב נחמן','רבה בר אבוה']),('a16','10b:16','רב נחמן','speaker',['רב נחמן'],'First proof',[]),('a18s','10b:18','רב ששת','speaker',['רב ששת'],'Safra interpretation report',[]),('a18sp','10b:18','ספרא','quoted_authority',['ספרא'],'Baraita assigned to RabbiYehuda',['רב ששת','ספרא']),('a19n','10b:19','רב נחמן','speaker',['רב נחמן'],'Second proof',[]),('a19l','10b:19','לוי','quoted_authority',['לוי'],'Priest-loss explanation',[]),('a24r','10b:24','ריש לקיש','speaker',['ריש לקיש'],'Concession after neck-breaking',[]),('a24o','10b:24','ורבי יוחנן ואי תימא רבי אלעזר','speaker',['רבי יוחנן','רבי אלעזר'],'Continuing dispute, alternative named holder',[]),('a25n','10b:25','רב נחמן','transmitter',['רב נחמן'],'Alternative placement',['רב נחמן','רבה בר אבוה']),('a25r','10b:25','רבה בר אבוה','quoted_authority',['רבה בר אבוה'],'Alternative placement',['רב נחמן','רבה בר אבוה']),('a27r','10b:27','רבה בר אבוה','transmitter',['רבה בר אבוה'],'One-shekel case',['רבה בר אבוה','רב']),('a27rav','10b:27','אמר רב','quoted_authority',['רב'],'One-shekel case',['רבה בר אבוה','רב']),('a27y','10b:27','רבי יוסי בר יהודה','quoted_authority',['רבי יוסי בר יהודה'],'Minimum redemption',[])]:att(k,ref,surf,role,cands,scope,chain,['Explicit alternative attribution, not joint speakers.'] if k=='a24o' else [])
for k,ref,cl,h,st,qu in [('p9y','10b:9','c9y',['רבי יהודה'],'Initial scope reinterpreted as lifetime',None),('p9s','10b:9','c9s',['רבי שמעון'],'Initial scope reinterpreted as lifetime',None),('p13f','10b:13','c13first',['Anonymous Gemara'],'First clause scope','q11'),('p13l','10b:13','c13last',['Anonymous Gemara'],'Second clause scope','q11'),('p15','10b:15','c15',['רבה בר אבוה via רב נחמן'],'Concession view, explicitly disputed later',None),('p18','10b:18','c18assign',['ספרא as reported by רב ששת'],'Alternative defeats proof',None),('p22','10b:22','c22',['Anonymous Gemara'],'RabbiYehuda explanation',None),('p23','10b:23','c23',['Anonymous Gemara'],'RabbiShimon explanation',None),('p24r','10b:24','c24rl',['ריש לקיש'],'Concession view',None),('p24o','10b:24','c24other',['רבי יוחנן','רבי אלעזר'],'Alternative holder; continuing dispute',None),('p25','10b:25','c25answer',['רבה בר אבוה via רב נחמן'],'Alternative placement explanation','q25'),('p27','10b:27','c27case',['רב via רבה בר אבוה'],'Other-version case explanation','q26'),('p27m','10b:27','c27min',['רבי יוסי בר יהודה'],'Minimum one shekel',None)]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'],cr['uncertainty'])
for k,ref,a,b,rel in [('e10y','10b:10','c10','c9y','qualification'),('e10s','10b:10','c10','c9s','qualification'),('e11','10b:11','q11','c10','objection'),('e13f','10b:13','c13first','q11','answer'),('e13l','10b:13','c13last','q11','answer'),('e14s','10b:14','c14s','c13last','support'),('e14y','10b:14','c14y','c13first','support'),('e16','10b:16','c16','c15','support'),('e17','10b:17','c17','c15','support'),('e18','10b:18','c18assign','c17','objection'),('e18h','10b:18','c18hyp','c18result','support'),('e19','10b:19','c19','c15','support'),('e20','10b:20','c20','c15','support'),('e21','10b:21','c21','c20','objection'),('e22','10b:22','c22','c21','support'),('e23','10b:23','c23','c21','support'),('e24','10b:24','c24other','c24rl','distinction'),('e25','10b:25','c25answer','q25','answer'),('e26s','10b:26','c26s','q26','support'),('e26y','10b:26','c26y','q26','support'),('e27','10b:27','c27case','q26','answer'),('e27m','10b:27','c27min','c27case','support')]:edge(k,ref,a,b,rel)
add('eprior','edges',['10b:24'],dict(source_id=pre+'c24other',target_id='beh.foodintent.20261126w3.c19',relation='distinction',explicitness='source_explicit'));rows[-1]['links']=[pre+'c24other','beh.foodintent.20261126w3.c19']
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Post-neck-breaking benefit and betrothal report variants. Failed proofs do not erase their stated thesis; explicit ReshLakish versus Yohanan-or-Elazar disagreement retained. Monetary versus bodily benefit, lifetime versus after death, and one-shekel no-surplus condition remain separate.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read10b9–11a26 and omission reread10b9–27. Baraita scopes, two proof rebuttals, explicit amoraic disagreement with alternative holder, both report placements, distinct transmission chains and shekel condition preserved. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch24_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch24_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch24_receipt.json',r.encoded(out));print(r.encoded(out).decode())
