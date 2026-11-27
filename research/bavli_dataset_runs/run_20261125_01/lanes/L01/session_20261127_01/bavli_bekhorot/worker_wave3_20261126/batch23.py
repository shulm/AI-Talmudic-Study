from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.foodintent.20261126w3.'
assert r.sha(r.encoded(state))=='24a3ca136da447c56b6805ee01376cf7d4593ab5ba1ef888ac109e1f2b0f7085'
refs=['9b:'+str(n) for n in range(19,24)]+['10a:'+str(n) for n in range(1,13)]+['10b:'+str(n) for n in range(1,9)]
add('s','structure',refs,dict(title='Neck-breaking and food impurity: designation, prior fitness and rejected prohibition-as-intention inference',primary=True,boundary='closed',legacy_ids=[]))
for ref,v,role in [('9b:19','Rabbah','RabbiShimon concedes after neck-breaking'),('9b:20','Anonymous Gemara','Neck-breaking analogy'),('9b:21','Rava citing baraita','Forbidden items food impurity proof'),('9b:22','Rabbi Shimon baraita','Exclusion and meat/milk exception'),('9b:23','Rabbi Asi reporting Rabbi Yohanan','Food defined by ability to feed others'),('10a:1','Anonymous Gemara','Meat/milk prior-fitness reason challenged'),('10a:2','Rabbi Shimon ben Yehuda reporting Rabbi Shimon','Eating versus benefit distinction'),('10a:3','Anonymous answer','Two cumulative reasons'),('10a:4','Anonymous Gemara','Donkey exception omission argument'),('10a:5','Anonymous answer','Lack of food designation'),('10a:6','Sages before Rav Sheshet','Prohibition-as-intention explanation'),('10a:7','Anonymous Gemara citing Mishnah','Pure bird carcass counterexample'),('10a:8','Anonymous answer','Assigns counterexample to Rabbi Shimon'),('10a:9','Anonymous Gemara and answer','Rural carcass/fat counterexample and same assignment'),('10a:10','Anonymous Gemara citing baraita','Market carcass/fat counterexample'),('10a:11','Anonymous Gemara with RabbiShimon continuation','First tanna cannot be RabbiShimon'),('10a:12','Rava','Rejects prohibition-as-intention and qualifies neck-breaking case'),('10b:1','Rava explanation continuation','Learning slaughter and Nimos/RabbiEliezer comparison'),('10b:2','Rabbi Yose reporting Nimos; Rabbi Eliezer','Crow slaughter blood dispute'),('10b:3','Anonymous Gemara','Proposed prohibition-as-intention contrast'),('10b:4','Anonymous exposition','First tanna requires intent for crow itself'),('10b:5','Anonymous exposition','RabbiEliezer proposed exemption'),('10b:6','Anonymous objection','Pure signs alternative'),('10b:7','Anonymous support quoting RabbiShimon','Significance of pure signs'),('10b:8','Anonymous Gemara','Learning versus casual slaughter scope')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
c('c19','9b:19','Rabbah says Rabbi Shimon concedes prohibition after neck-breaking.',cond=['Firstborn donkey after neck-breaking'])
c('c20','9b:20','The explanation derives it by the shared neck-breaking term from the broken-neck heifer.')
for key,item in [('orlah','orlah'),('vine','vineyard mixtures'),('ox','ox condemned to stoning'),('heifer','broken-neck heifer'),('birds','leper purification birds'),('donkey','firstborn donkey'),('milk','meat cooked with milk')]:
 c('c21'+key,'9b:21','The first tanna says '+item+' contracts food impurity.')
 c('c22'+key,'9b:22','Rabbi Shimon’s general exclusion says '+item+' does not contract food impurity'+('; immediately qualified by the explicit exception.' if key=='milk' else '.'))
c('c22except','9b:22','Rabbi Shimon concedes food impurity for meat with milk because it previously had a period of fitness.')
c('c23yes','9b:23','Rabbi Yohanan’s explanation through Rabbi Asi defines what may be fed to others as food.')
c('c23no','9b:23','What cannot be fed to others is not called food in this impurity derivation.')
q('q1','10a:1','Why need prior fitness for meat with milk if it may be fed to others?')
c('c2eat','10a:2','Rabbi Shimon ben Yehuda reports in Rabbi Shimon’s name that meat with milk is forbidden to eat.')
c('c2benefit','10a:2','That report permits benefit from meat with milk.')
c('c2analogy','10a:2','The report derives this distinction by the shared holiness language.')
c('c3other','10a:3','The answer gives ability to feed others as one ground for food impurity.')
c('c3prior','10a:3','It adds prior fitness for the person himself as a second ground.')
q('q4','10a:4','If Rabbi Shimon permits the donkey after neck-breaking, why not list it with meat/milk as an impurity exception?')
c('c5intent','10a:5','The reply says the exception would indeed apply if he had designated it as food.')
c('c5case','10a:5','The case under discussion lacks such designation.')
q('q6','10a:6','Why then do the Sages impose food impurity?')
c('c6','10a:6','The Sages before Rav Sheshet propose that its prohibition itself supplies food designation.',mode='challenged')
c('c7intent','10a:7','The cited Mishnah requires food designation for a pure bird carcass.')
c('c7wet','10a:7','It does not require liquid preparation for that carcass.')
q('q8','10a:8','If prohibition supplies designation, why is designation required?')
c('c8','10a:8','The reply assigns that Mishnah to Rabbi Shimon.')
for key,subj in [('impure','Impure animal carcass everywhere'),('bird','Pure bird carcass in villages'),('fat','Fat in villages')]:
 c('c9'+key+'i','10a:9',subj+' requires food designation in the cited baraita.')
 c('c9'+key+'w','10a:9',subj+' does not require liquid preparation in that baraita.')
c('c9assign','10a:9','The reply again assigns the requirement to Rabbi Shimon.')
for key,subj in [('pure','Pure animal carcass everywhere'),('bird','Pure bird carcass in markets'),('fat','Fat in markets')]:
 c('c10'+key+'i','10a:10',subj+' does not require food designation in the new baraita.')
 c('c10'+key+'w','10a:10',subj+' does not require liquid preparation in that baraita.')
c('c10infer','10a:10','The passage infers that impure animal carcass does require food designation under its first tanna.')
c('c11not','10a:11','Because the continuation explicitly gives Rabbi Shimon’s distinct view, the first tanna cannot simply be assigned to him.')
for key,animal in [('camel','camel'),('hare','hare'),('hyrax','hyrax'),('pig','pig')]:
 c('c11'+key+'i','10a:11','Rabbi Shimon says '+animal+' too needs no food designation.')
 c('c11'+key+'w','10a:11','He says '+animal+' too needs no liquid preparation.')
c('c11signs','10a:11','Rabbi Shimon explains this by their having signs of purity.')
c('c12all','10a:12','Rava states that all agree prohibition does not itself supply food designation.')
c('c12broken','10a:12','He concedes the proposed impurity outcome in an actual neck-breaking case.')
c('c1case','10b:1','The present case is instead slaughter performed to learn the technique.')
c('c1compare','10b:1','The attempted explanation compares Nimos and Rabbi Eliezer’s dispute.')
c('c2nimos','10b:2','Nimos reports that blood of a crow slaughtered to learn the technique prepares food for impurity.',cond=['Crow slaughtered to learn'])
c('c2eliezer','10b:2','Rabbi Eliezer says slaughter blood always prepares food for impurity.')
q('q3','10b:3','How does Rabbi Eliezer differ from the first tanna?')
c('c3hyp','10b:3','The proposed difference is whether prohibition itself supplies food designation.',mode='challenged')
c('c4other','10b:4','Under the proposal, the first tanna’s blood prepares other food.')
c('c4self','10b:4','The crow itself still requires food designation under that tanna.')
c('c5','10b:5','Under the proposal, Rabbi Eliezer dispenses with food designation for the crow itself.',mode='challenged')
c('c6alt','10b:6','The objection offers another explanation: a crow is different because it has signs of purity.')
c('c7support','10b:7','Rabbi Shimon’s earlier pure-signs explanation supports the relevance of that distinction.')
q('q8scope','10b:8','If pure signs explain Rabbi Eliezer, why specify learning rather than casual slaughter?')
c('c8scope','10b:8','The answer accepts the broader scope for Rabbi Eliezer and says the learning wording is needed for Nimos.')
for k,ref,surf,role,cands,scope,chain in [('a19','9b:19','רבה','speaker',['רבה'],'Post-neck-breaking concession',[]),('a21','9b:21','רבא','speaker',['רבא'],'Food impurity proof',[]),('a22','9b:22','רבי שמעון','quoted_authority',['רבי שמעון'],'Food impurity exclusion',[]),('a23asi','9b:23','רבי אסי','transmitter',['רבי אסי'],'Food definition',['רבי אסי','רבי יוחנן']),('a23y','9b:23','ר יוחנן','quoted_authority',['רבי יוחנן'],'Food definition',['רבי אסי','רבי יוחנן']),('a2trans','10a:2','רבי שמעון בן יהודה','transmitter',['רבי שמעון בן יהודה'],'Meat/milk distinction',['רבי שמעון בן יהודה','רבי שמעון']),('a2h','10a:2',"ר' שמעון",'quoted_authority',['רבי שמעון'],'Meat/milk distinction',['רבי שמעון בן יהודה','רבי שמעון']),('a6','10a:6','רבנן','collective',['Sages before Rav Sheshet'],'Initial prohibition-as-intention explanation',[]),('a12','10a:12','רבא','speaker',['רבא'],'Rejection of explanation',[]),('ab2y','10b:2',"ר' יוסי",'transmitter',['רבי יוסי'],'Nimos teaching',['רבי יוסי','נימוס']),('ab2n','10b:2','נימוס','quoted_authority',['נימוס'],'Crow slaughter blood',['רבי יוסי','נימוס']),('ab2e','10b:2',"ר' אליעזר",'speaker',['רבי אליעזר'],'Always prepares food',[])]:att(k,ref,surf,role,cands,scope,chain)
for k,ref,cl,h,st,qu in [('p19','9b:19','c19',['רבה'],'Reported concession, later dispute retained',None),('p22','9b:22','c22except',['רבי שמעון'],'Explicit meat/milk exception',None),('p2e','10a:2','c2eat',['רבי שמעון via רבי שמעון בן יהודה'],'Eating prohibition',None),('p2b','10a:2','c2benefit',['רבי שמעון via רבי שמעון בן יהודה'],'Benefit permission',None),('p5','10a:5','c5case',['Anonymous Gemara'],'Case restriction','q4'),('p6','10a:6','c6',['Sages before Rav Sheshet'],'Initial explanation rejected by Rava','q6'),('p12','10a:12','c12all',['רבא'],'Corrected shared principle','q6'),('pb2n','10b:2','c2nimos',['נימוס via רבי יוסי'],'Reported rule',None),('pb2e','10b:2','c2eliezer',['רבי אליעזר'],'Reported rule',None),('pb3','10b:3','c3hyp',['Anonymous Gemara'],'Attempted distinction challenged','q3'),('pb6','10b:6','c6alt',['Anonymous Gemara'],'Alternative explanation defeats proof',None),('pb8','10b:8','c8scope',['Anonymous Gemara'],'Scope reply','q8scope')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e20','9b:20','c20','c19','support'),('e22','9b:22','c22except','c22milk','qualification'),('e1','10a:1','q1','c22except','objection'),('e2','10a:2','c2benefit','q1','support'),('e3o','10a:3','c3other','q1','answer'),('e3p','10a:3','c3prior','q1','answer'),('e4','10a:4','q4','c19','support'),('e5','10a:5','c5case','q4','answer'),('e6','10a:6','c6','q6','answer'),('e8q','10a:8','q8','c6','objection'),('e8','10a:8','c8','q8','answer'),('e9','10a:9','c9assign','c6','support'),('e11','10a:11','c11not','c6','objection'),('e12','10a:12','c12all','c6','correction'),('eb1','10b:1','c1case','c12broken','qualification'),('eb3','10b:3','c3hyp','q3','answer'),('eb6','10b:6','c6alt','c3hyp','objection'),('eb7','10b:7','c7support','c6alt','support'),('eb8','10b:8','c8scope','q8scope','answer')]:edge(k,ref,a,b,rel)
add('eprior','edges',['9b:19'],dict(source_id=pre+'c19',target_id='beh.benefit.20261126w3.c4s',relation='qualification',explicitness='source_explicit'));rows[-1]['links']=[pre+'c19','beh.benefit.20261126w3.c4s']
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local food-impurity proof sequence. Rabbah at9b19 and Rava at9b21/10a12 retained as printed distinct names. Intent and liquid preparation are distinct predicates. Prohibition-as-intention explanations are challenged/corrected; later10b24 dispute prevents treating post-neck-breaking agreement as universal.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read9b19–10b33 and omission reread9b19–10b8. Seven food categories and purity/preparation predicates separated. Prior-fitness/benefit reasons, successive counterexamples, Rava correction, Nimos report chain and pure-signs alternative preserved. Later named dispute read before unrestricted inference. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch23_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch23_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch23_receipt.json',r.encoded(out));print(r.encoded(out).decode())
