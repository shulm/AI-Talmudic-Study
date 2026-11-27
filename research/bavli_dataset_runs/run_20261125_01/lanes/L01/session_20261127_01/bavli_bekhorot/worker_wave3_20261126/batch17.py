from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.products.20261126w3.'
assert r.sha(r.encoded(state))=='8f6a318713028a854ef547071889b099e9d37b2c744542aaf4761b4f67ce72ab'
refs=['7a:'+str(n) for n in range(22,25)]+['7b:'+str(n) for n in range(1,15)]
add('s1','structure',refs[:12],dict(title='Donkey urine, two question versions and competing honey exceptions',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[12:13],dict(title='Substance from yahmur: rejected organ identification and semen explanation',primary=True,boundary='closed',legacy_ids=[]))
add('s3','structure',refs[13:],dict(title='Membrane in front of newborn face and impurity analogy',primary=True,boundary='closed',legacy_ids=[]))
for ref,v,role in [('7a:22','Unnamed questioners to Rav Sheshet','Donkey urine inquiry'),('7a:23','Anonymous Gemara','First version: cloudiness and physiological alternatives'),('7a:24','Rav Sheshet','Maternal-origin maxim response'),('7b:1','Rav Sheshet response continuation','Impure-origin application'),('7b:2','Alternative anonymous version','Human consumption and reported jaundice benefit premise'),('7b:3','Rav Sheshet','Repeated response in alternate version'),('7b:4','Anonymous Gemara citing baraita','Honey objection based on intake rather than bodily extraction'),('7b:5','Anonymous Gemara','Alignment with Rabbi Yaakov'),('7b:6','Rabbi Yaakov baraita','Initial verse formulation'),('7b:7','Anonymous correction of formulation','Bee honey permitted by verse'),('7b:8','Baraita','Named honey varieties excluded'),('7b:9','Anonymous Gemara citing baraita','Permissive other-honey ruling excludes Rabbi Yaakov'),('7b:10','Anonymous Gemara and baraita','Food-intention distinction'),('7b:11','Sages then Rav Safra','Organ hypothesis versus semen identification'),('7b:12','Rav Huna','Face membrane permitted as mere waste'),('7b:13','Rav Hisda','Supporting human membrane baraita and initial reading'),('7b:14','Anonymous reply and explicit baraita','Rejected reinterpretation and acceptance')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
q('q22','7a:22','What is the eating status of donkey urine?')
q('q23','7a:23','Why is the question not asked about horses and camels?')
c('c23horse','7a:23','In the first version, horse and camel urine is unclouded and unlike milk; the account treats it as water entering and leaving.')
c('c23cloud','7a:23','Donkey urine is described as cloudy and milk-like, generating the question.')
c('c23extract','7a:23','One branch treats it as extracted from the animal’s body and prohibited.',mode='hypothetical')
c('c23water','7a:23','The other treats it as water entering and leaving, clouded by bodily heat.',mode='hypothetical')
c('c24','7a:24','Rav Sheshet answers by citing the maxim that what emerges from the impure is impure and what emerges from the pure is pure.')
c('c1','7b:1','His answer applies impure origin to this product, prohibiting it.')
c('c2horse','7b:2','The alternative version says horse and camel urine is not in question because people do not drink it.')
c('c2donkey','7b:2','It makes donkey urine the question because people drink it and it is reported beneficial for jaundice; this is a source premise, not medical advice.')
c('c3','7b:3','Rav Sheshet again applies the impure-origin maxim to prohibit the product.')
c('c4permit','7b:4','The cited baraita permits bee honey.')
c('c4reason','7b:4','It explains that bees bring honey into their bodies rather than extract it from their bodies.')
c('c5','7b:5','The answer aligns Rav Sheshet with Rabbi Yaakov, for whom the Torah specifically permits honey.')
c('c6','7b:6','Rabbi Yaakov’s baraita initially contrasts what may be eaten with an impure winged creeping creature.')
q('q7','7b:7','Is the prohibition on the impure winged creature not already explicit?')
c('c7','7b:7','The corrected formulation prohibits the creature but permits what it produces, identified as bee honey.')
q('q8','7b:8','Should honey of gazin and hornets be included too?')
c('c8no','7b:8','The baraita excludes honey of gazin and hornets from this permission.')
c('c8bee','7b:8','Bee honey is included because its ordinary honey name has no qualifying modifier.')
c('c8other','7b:8','Honey of gazin and hornets is excluded because it has a qualifying modifier.')
q('q9','7b:9','Whose view is the baraita declaring honey of gazin and hornets pure and permitted to eat?')
c('c9pure','7b:9','The other baraita states that honey of gazin and hornets is pure.')
c('c9eat','7b:9','That baraita permits eating honey of gazin and hornets.')
c('c9not','7b:9','The passage identifies that baraita as not following Rabbi Yaakov.')
c('c10thought','7b:10','From the term pure, the passage infers that this honey requires designation as food.')
c('c10bee','7b:10','The cited comparison says bee honey in its hive contracts food impurity without such designation.')
c('c11initial','7b:11','The Sages initially identify hallei of yahmur as testicles and regard them as forbidden.',mode='challenged')
c('c11safra','7b:11','Rav Safra instead identifies the substance as deer semen deposited after pursuit of a hind whose narrow womb prevents mating and subsequent pursuit of a yahmur; preserve the source’s account without asserting modern zoology.')
rows[-1]['uncertainty'].append('Terms חלי and יחמורתא retained; precise zoological identification and physiology not independently established.')
c('c12permit','7b:12','Rav Huna permits the membrane coming in front of a donkey’s face.')
c('c12reason','7b:12','He treats it as mere waste.')
c('c13pure','7b:13','Rav Hisda cites a baraita declaring the corresponding human face membrane pure whether living or dead.')
c('c13read','7b:13','The initial reading covers both child and mother alive or both child and mother dead.')
c('c14narrow','7b:14','The reply narrows the cases to a live child with dead mother or dead child with live mother.',mode='challenged')
c('c14explicit','7b:14','An explicit baraita states both alive and both dead, defeating that narrowed reading.')
c('c14accept','7b:14','The response accepts the explicit baraita: if taught, it is taught.')
for k,ref,surf,role,cands,scope in [('a22','7a:22','רב ששת','quoted_authority',['רב ששת'],'Question recipient and explicit answering authority in continuation'),('a24','7a:24','רב ששת','speaker',['רב ששת'],'First-version answer'),('a3','7b:3','רב ששת','speaker',['רב ששת'],'Second-version answer'),('a5','7b:5',"ר' יעקב",'position_holder',['רבי יעקב'],'Explicit alignment'),('a6','7b:6',"ר' יעקב",'quoted_authority',['רבי יעקב'],'Honey baraita'),('a11r','7b:11','רבנן','collective',['Sages'],'Initial identification'),('a11s','7b:11','רב ספרא','speaker',['רב ספרא'],'Alternative identification'),('a12','7b:12','רב הונא','speaker',['רב הונא'],'Membrane permission'),('a13','7b:13','רב חסדא','speaker',['רב חסדא'],'Supporting baraita')]:att(k,ref,surf,role,cands,scope)
for k,ref,cl,h,st,qu in [('p1','7b:1','c1',['רב ששת'],'First-version prohibition','q22'),('p3','7b:3','c3',['רב ששת'],'Alternative-version prohibition','q22'),('p4','7b:4','c4permit',['Anonymous baraita'],'Honey permission with physical rationale',None),('p7','7b:7','c7',['רבי יעקב'],'Specific scriptural honey permission','q7'),('p8','7b:8','c8no',['רבי יעקב'],'Other-honey exclusion','q8'),('p9','7b:9','c9eat',['Anonymous baraita; not Rabbi Yaakov'],'Contrasting permission',None),('p11i','7b:11','c11initial',['Sages'],'Initial identification challenged',None),('p11s','7b:11','c11safra',['רב ספרא'],'Replacement identification',None),('p12','7b:12','c12permit',['רב הונא'],'Permission',None),('p13','7b:13','c13read',['רב חסדא'],'Initial support reading later confirmed',None),('p14','7b:14','c14narrow',['Anonymous Gemara'],'Rejected narrowed reading',None)]:pos(k,ref,cl,h,st,qu)
for k,ref,a,b,rel in [('e23','7a:23','c23horse','q23','answer'),('e23c','7a:23','c23cloud','q22','support'),('e23x','7a:23','c23extract','q22','answer'),('e23w','7a:23','c23water','q22','answer'),('e1','7b:1','c24','c1','support'),('e1a','7b:1','c1','q22','answer'),('e3','7b:3','c3','q22','answer'),('e4','7b:4','c4reason','c4permit','support'),('e4o','7b:4','c4permit','c3','objection'),('e5','7b:5','c5','c4permit','answer'),('e7q','7b:7','q7','c6','objection'),('e7','7b:7','c7','q7','answer'),('e7c','7b:7','c7','c6','correction'),('e8','7b:8','c8no','q8','answer'),('e8b','7b:8','c8bee','c7','support'),('e8o','7b:8','c8other','c8no','support'),('e9','7b:9','c9not','q9','answer'),('e9d','7b:9','c9eat','c8no','distinction'),('e10','7b:10','c9pure','c10thought','support'),('e10b','7b:10','c10bee','c10thought','distinction'),('e11','7b:11','c11safra','c11initial','correction'),('e12','7b:12','c12reason','c12permit','support'),('e13','7b:13','c13pure','c12reason','support'),('e14n','7b:14','c14narrow','c13read','objection'),('e14e','7b:14','c14explicit','c14narrow','objection'),('e14a','7b:14','c14accept','c14explicit','local_resolution')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local product-origin rulings, two urine-question versions, competing honey explanations and membrane analogy. Medical and physiological premises remain reported source claims; modern identification not certified.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read7a22–8a17 and omission reread7a22–7b14. Alternate reasons retained independently, honey tannaitic disagreement explicit, food purity/eating separate, initial identification and narrowed membrane reading corrected by continuation. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch17_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch17_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch17_receipt.json',r.encoded(out));print(r.encoded(out).decode())
