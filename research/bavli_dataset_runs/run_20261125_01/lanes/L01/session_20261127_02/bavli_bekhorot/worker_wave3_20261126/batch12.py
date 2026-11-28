from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.kinds.20261126w3.'
assert r.sha(r.encoded(state))=='394c290fa60d500352b9d302b462bbdfb571b2f08045146ebe3dafaa733dd7ea'
refs=['5b:'+str(n) for n in range(7,17)]
add('sm','structure',refs[:2],dict(title='Differing-kind birth: firstborn status and permissibility of eating',primary=True,boundary='closed',legacy_ids=[]))
add('sg','structure',refs[2:],dict(title='Matching parent and offspring: two directions of derivation',primary=True,boundary='closed',legacy_ids=[]))
for n,v,role in [(7,'Mishnah','Exemptions and repeated donkey wording'),(8,'Mishnah','Eating rules and maternal principle'),(9,'Quoted Mishnah','Sheep/goat cases and partial signs'),(10,'Anonymous question and Rav Yehuda','Three species-specific derivations'),(11,'Expository continuation','Partial-signs exception'),(12,'Anonymous Gemara','Competing proof text objection'),(13,'Anonymous answer citing Rabbi Yose the Galilean','Different tannaitic derivation'),(14,'Tannaitic exposition continuation','Repeated partial-signs exception'),(15,'Anonymous Gemara','Basis of difference, Mishnah tanna'),(16,'Anonymous Gemara','Basis of difference, Rabbi Yose the Galilean')]:add('u'+str(n),'utterances',['5b:'+str(n)],dict(textual_voice=v,discourse_role=role,composition='composite'))
c('c7cow','5b:7','The Mishnah exempts from firstborn status a cow giving birth to a donkey-kind offspring.',cond=['Cow produces donkey-kind offspring'])
c('c7donkey','5b:7','The Mishnah exempts a donkey giving birth to a horse-kind offspring.',cond=['Donkey produces horse-kind offspring'])
c('c7repeat',('5b:7','פטר חמור שני פעמים'),'The proof notes firstborn donkey stated twice.')
c('c7parent',('5b:7','עד שיהא היולד חמור'),'The requirement includes the giving-birth parent being a donkey.')
c('c7child',('5b:7','והנולד חמור'),'It includes the offspring being a donkey.')
q('q8',('5b:8','ומה הם באכילה'),'What is their status for eating?')
c('c8pure',('5b:8','בהמה טהורה שילדה כמין בהמה טמאה מותר באכילה'),'An offspring resembling an impure animal but born from a pure animal is permitted to eat.',cond=['Pure mother','Offspring resembles impure kind'])
c('c8impure',('5b:8','וטמאה שילדה כמין בהמה טהורה אסור באכילה'),'An offspring resembling a pure animal but born from an impure animal is forbidden to eat.',cond=['Impure mother','Offspring resembles pure kind'])
c('c8fromimpure',('5b:8','שהיוצא מן הטמא טמא'),'What emerges from the impure is impure.')
c('c8frompure',('5b:8','והיוצא מן הטהור טהור'),'What emerges from the pure is pure.')
c('c9ewe',('5b:9','רחל שילדה מין עז'),'The cited Mishnah exempts a ewe giving birth to goat-kind offspring.',cond=['Ewe produces goat-kind offspring','No qualifying partial maternal signs'])
c('c9goat',('5b:9','ועז שילדה מין רחל פטור מן הבכורה'),'It exempts a goat giving birth to sheep-kind offspring.',cond=['Goat produces sheep-kind offspring','No qualifying partial maternal signs'])
c('c9sign',('5b:9','ואם יש בו מקצת סימנין חייב'),'Some corresponding maternal signs restore firstborn liability.',cond=['Differing-kind offspring has some corresponding signs'])
q('q10',('5b:10','מנא הני מילי'),'What is the source for these matching-kind requirements?')
for tag,ref in [('ravy','5b:10'),('yose','5b:13')]:
 for animal,prop in [('שור','ox'),('כשב','sheep'),('עז','goat')]:
  c('c'+tag+prop,ref,'The '+('Rav Yehuda' if tag=='ravy' else 'Rabbi Yose the Galilean')+' exposition requires both parent and offspring to be '+prop+' for that named firstborn category.',cond=['Category '+prop,'Subject to partial-signs exception in continuation'])
for tag,ref in [('ravy','5b:11'),('yose','5b:14')]:
 q('q'+tag+'sign',(ref,"יכול אפי' יש בו מקצת סימנין"),'Could exemption apply even when there are some corresponding signs?')
 c('c'+tag+'sign',(ref,'ת"ל אך חלק'),'The restrictive term akh distinguishes the partial-signs case from the exemption.',cond=['Some corresponding signs present'])
q('q12','5b:12','Does the Mishnah tanna not use the repeated firstborn-donkey wording for the cow case instead?')
c('c13align',('5b:13','הוא דאמר כרבי יוסי הגלילי'),'The answer aligns Rav Yehuda’s exposition with Rabbi Yose the Galilean.')
q('q15',('5b:15','במאי קמיפלגי'),'What is the difference between the derivation approaches?')
c('c15',('5b:15','תנא דידן סבר גלי רחמנא בקדושת דמים וה"ה בקדושת הגוף'),'The Mishnah tanna learns the rule from monetary sanctity and extends it to bodily sanctity.')
c('c16','5b:16','Rabbi Yose learns the rule from bodily sanctity and derives monetary sanctity from it.')
att('a10','5b:10','רב יהודה','speaker',['רב יהודה'],'Matching-kind exposition')
att('a13','5b:13','רבי יוסי הגלילי','quoted_authority',['רבי יוסי הגלילי'],'Alternative tannaitic derivation')
att('a15','5b:15','תנא דידן','anonymous',[],'Mishnah tanna derivation')
att('a16','5b:16',"ר' יוסי",'position_holder',['רבי יוסי הגלילי'],'Bodily-to-monetary derivation',unc=['Short form רבי יוסי resolved by explicit immediate RabbiYoseGalilean context, not generic name matching.'])
for k,ref,cl,h,status,question in [('p7c','5b:7','c7cow',['Anonymous Mishnah'],'Stated exemption',None),('p7d','5b:7','c7donkey',['Anonymous Mishnah'],'Stated exemption',None),('p8p','5b:8','c8pure',['Anonymous Mishnah'],'Maternal-status rule','q8'),('p8i','5b:8','c8impure',['Anonymous Mishnah'],'Maternal-status rule','q8'),('p9e','5b:9','c9ewe',['Cited anonymous Mishnah'],'Exemption qualified by signs',None),('p9g','5b:9','c9goat',['Cited anonymous Mishnah'],'Exemption qualified by signs',None),('p9s','5b:9','c9sign',['Cited anonymous Mishnah'],'Exception',None),('p15','5b:15','c15',['Mishnah tanna'],'First derivation direction','q15'),('p16','5b:16','c16',['רבי יוסי הגלילי'],'Other derivation direction','q15')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for tag,ref,h in [('ravy','5b:10',['רב יהודה']),('yose','5b:13',['רבי יוסי הגלילי'])]:
 for animal in ['ox','sheep','goat']:
  cl='c'+tag+animal;cr=next(x for x in rows if x['id']==pre+cl);pos('p'+tag+animal,ref,cl,h,'Species-specific exposition','q10',cr['content']['conditions'])
for tag,ref,h in [('ravy','5b:11',['רב יהודה']),('yose','5b:14',['רבי יוסי הגלילי'])]:pos('p'+tag+'sign',ref,'c'+tag+'sign',h,'Partial-signs qualification','q'+tag+'sign',['Some corresponding signs present'])
for k,ref,a,b,rel in [('e7p','5b:7','c7repeat','c7parent','support'),('e7c','5b:7','c7repeat','c7child','support'),('e8p','5b:8','c8pure','q8','answer'),('e8i','5b:8','c8impure','q8','answer'),('e8ps','5b:8','c8frompure','c8pure','support'),('e8is','5b:8','c8fromimpure','c8impure','support'),('e9e','5b:9','c9sign','c9ewe','qualification'),('e9g','5b:9','c9sign','c9goat','qualification'),('e12','5b:12','q12','cravyox','objection'),('e13','5b:13','c13align','q12','answer'),('e15','5b:15','c15','q15','answer'),('e16','5b:16','c16','q15','answer'),('e16d','5b:16','c15','c16','distinction')]:edge(k,ref,a,b,rel)
for tag,ref in [('ravy','5b:10'),('yose','5b:13')]:
 for animal in ['ox','sheep','goat']:edge('e'+tag+animal,ref,'c'+tag+animal,'q10','answer')
for tag,ref in [('ravy','5b:11'),('yose','5b:14')]:edge('e'+tag+'sign',ref,'c'+tag+'sign','q'+tag+'sign','answer')
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local firstborn-kind derivations and eating-status Mishnah. Firstborn liability and eating permissibility remain separate predicates; source parallel derivations retained. Partial-signs continuation read through6a19 before any blanket exemption claim.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read5b7–6a22. Omission reread distinguishes firstborn/eating rules, mother/offspring conditions, three species and two derivation occurrences, partial-signs exceptions and monetary/bodily direction contrast. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch12_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch12_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch12_receipt.json',r.encoded(out));print(r.encoded(out).decode())
