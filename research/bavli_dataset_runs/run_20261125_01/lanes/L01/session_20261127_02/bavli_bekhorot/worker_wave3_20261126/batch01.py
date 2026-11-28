from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.fetus_sale.20261126w3.'
assert r.sha(r.encoded(state))=='d33eec110117c488238f86530f882ddf97fb2c72b0662de4725ad6066d2999d8'
refs=['2a:'+str(n) for n in range(7,13)]+['2b:'+str(n) for n in range(1,9)]
add('s1','structure',refs[:9],dict(title='Rabbi Yehuda and sale of a fetus: inquiry, failed proofs and Rav Ashi proof',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[9:],dict(title='Alternative transmission attached to Mishnah sale restriction',primary=True,boundary='closed',legacy_ids=[]))
for ref,voice,role in [('2a:7','Quoted Mishnah','Rabbi Yehuda and Ben Beteira permissions'),('2a:8','Anonymous Gemara','Two-sided inquiry'),('2a:9','Anonymous Gemara citing Mishnah','Attempted proof'),('2a:10','Anonymous Gemara','Counterexample'),('2a:11','Anonymous Gemara','Rejection of silence inference'),('2a:12','Baraita quoting Rabbi Yehuda','Second proof text'),('2b:1','Anonymous Gemara','Proposed referent and rejection'),('2b:2','Anonymous Gemara','Grammatical objection, emendation, substantive objection and answer'),('2b:3','Rav Ashi','Concluding proof'),('2b:4','Alternative transmission','Mishnah compatibility challenge'),('2b:5','Anonymous Gemara','Compatibility answer'),('2b:6','Quoted baraita and anonymous discussion','Repeated proof and referent rejection'),('2b:7','Anonymous Gemara','Repeated grammatical and substantive objections and answer'),('2b:8','Rav Ashi in alternative transmission','Repeated concluding proof')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'))
c('c7y',('2a:7',"ר' יהודה מתיר בשבורה"),'Rabbi Yehuda permits sale of a broken animal to a non-Jew.',cond=['Broken animal in cited sale discussion'])
c('c7b',('2a:7','בן בתירא מתיר בסוס'),'Ben Beteira permits sale of a horse.',cond=['Horse in cited sale discussion'])
q('q8',('2a:8',"איבעיא להו עובר מה לי א"+'"'+"ר יהודה"),'What does Rabbi Yehuda say about sale of a fetus?')
c('c8permit',('2a:8',"טעמא דר' יהודה התם דשרי משום דשבורה עובר נמי שבור הוא"),'One proposed reason for permission is the broken condition, which could also characterize a fetus.',mode='hypothetical',cond=['If broken condition alone is the relevant reason'])
c('c8forbid',('2a:8','או דלמא שבורה לאו היינו אורחיה אבל עובר כיון דהיינו אורחיה לאו שבור הוא'),'The alternative distinguishes an abnormal broken animal from a fetus whose present state is normal.',mode='hypothetical',cond=['If abnormality of broken condition is decisive'])
c('c9','2a:9','The proof attempt infers agreement with the Mishnah sale prohibition from its not recording Rabbi Yehuda’s dissent.',mode='hypothetical')
q('q10','2a:10','Does the omission of dissent in partnership and receiving or giving on contract likewise mean Rabbi Yehuda does not dispute them?')
c('c11','2a:11','The answer says dissent exists despite not being recorded, rejecting the inference from silence here too.')
for tag,ref in [('first','2a:12'),('second','2b:6')]:
 c('c'+tag+'receive',(ref,'המקבל בהמה מן העובד כוכבים וילדה מעלין אותו בשוויו' if tag=='first' else 'המקבל בהמה מן העובד כוכבים וילדה מעלין אותו בשויו'),'Rabbi Yehuda says that when an animal received from a non-Jew gives birth, the offspring is appraised.',cond=['Animal received from a non-Jew on contract','Animal gave birth'])
 c('c'+tag+'half',(ref,'ונותן חצי דמיו לכהן'),'Rabbi Yehuda requires giving half its value to a priest in that received-animal case.',cond=['Animal received from a non-Jew on contract','Animal gave birth'])
 c('c'+tag+'forbidden',(ref,'והנותן לו בקבלה אף על פי שאינו רשאי' if tag=='first' else 'והנותן לו בקבלה אע"פ שאינו רשאי'),'The converse giving-on-contract case is described as not permitted.',cond=['Giving to a non-Jew on contract','Referent fetus versus animal debated in continuation'])
 c('c'+tag+'penalty',(ref,'קונסים אותו עד עשרה בדמיו' if tag=='first' else 'קונסין אותו עד עשרה בדמיו'),'That case receives a penalty up to ten times its value.',cond=['Giving to a non-Jew on contract','Referent debated in continuation'])
 c('c'+tag+'whole',(ref,'ונותן כל דמיו לכהן'),'The reported ruling further gives all its value to a priest.',cond=['Giving to a non-Jew on contract','Referent debated in continuation'])
for tag,ref in [('first','2b:1'),('second','2b:6')]:
 q('q'+tag+'fetus',(ref,'מאי לאו אעובר'),'Does the prohibition refer to the fetus?')
 c('c'+tag+'animal',(ref,'לא אבהמה'),'The answer rejects that proof by referring the prohibition to the animal.')
for tag,ref in [('first','2b:2'),('second','2b:7')]:
 q('q'+tag+'masc',(ref,'והא דמיו קתני'),'Does the masculine “its value” not contradict the proposed animal referent?')
 c('c'+tag+'fem',(ref,'תני דמיה'),'The reply instructs reading the feminine form “its value.”')
 q('q'+tag+'priest',(ref,'והא נותן כל דמיו לכהן קתני ואי בהמה כהן מאי עבידתיה'),'Why would all the animal’s value be given to a priest?')
 c('c'+tag+'pregnant',(ref,'כגון דיהיב ליה בהמה מעברתא לפטומה' if tag=='first' else 'כגון דיהיב בהמה מעברתא לפטומה'),'The case is explained as giving a pregnant animal for fattening.')
 c('c'+tag+'extension',(ref,'דמיגו דקנסינן ליה אבהמה קנסינן ליה אעובר'),'The penalty imposed on the animal extends to the fetus.')
for tag,ref in [('first','2b:3'),('second','2b:8')]:
 c('c'+tag+'noheal',(ref,'מפני שאינה יכולה להתרפאות'),'Rav Ashi cites Rabbi Yehuda’s permission as limited by inability to heal.',cond=['Broken animal unable to heal'])
 c('c'+tag+'heal',(ref,'הא יכולה להתרפאות אסר' if tag=='first' else 'הא יכולה להתרפאות אסור'),'The proof infers prohibition when the animal can heal.',cond=['Animal able to heal'])
 c('c'+tag+'fetusconclusion',(ref,'והא עובר נמי כיכול להתרפאות דמי שמע מינה' if tag=='first' else 'והאי נמי כיכול להתרפאות דמי שמע מינה'),'The fetus is treated as capable of healing, concluding the proof for prohibition of its sale.',cond=['Fetus in the sale inquiry'])
q('q4',('2b:4',"לימא מתני' דלא כרבי יהודה"),'In the alternative transmission, must the Mishnah be contrary to Rabbi Yehuda?')
c('c5','2b:5','The answer allows the Mishnah to accord with Rabbi Yehuda: a broken animal is abnormal whereas a fetus is in its normal state.')
for k,ref,surface,role,holders,scope in [('a7y','2a:7',"ר' יהודה",'quoted_authority',['רבי יהודה'],'c7y'),('a7b','2a:7','בן בתירא','quoted_authority',['בן בתירא'],'c7b'),('a12','2a:12',"ר' יהודה",'quoted_authority',['רבי יהודה'],'First quoted baraita'),('a3','2b:3','רב אשי','speaker',['רב אשי'],'First concluding proof'),('a3y','2b:3','רבי יהודה','quoted_authority',['רבי יהודה'],'cfirstnoheal'),('a4','2b:4','ואיכא דמתני לה','anonymous',[],'Alternative transmission'),('a6','2b:6','רבי יהודה','quoted_authority',['רבי יהודה'],'Second quoted baraita'),('a8','2b:8','רב אשי','speaker',['רב אשי'],'Second concluding proof'),('a8y','2b:8',"ר' יהודה",'quoted_authority',['רבי יהודה'],'csecondnoheal')]:att(k,ref,surface,role,holders,pre+scope if scope.startswith('c') else scope)
for k,ref,cl,h,status,question in [('p7y','2a:7','c7y',['רבי יהודה'],'Cited permission',None),('p7b','2a:7','c7b',['בן בתירא'],'Cited permission',None),('p8p','2a:8','c8permit',['Anonymous Gemara'],'Hypothetical rationale, not a settled Rabbi Yehuda ruling','q8'),('p8f','2a:8','c8forbid',['Anonymous Gemara'],'Alternative hypothesis','q8'),('p9','2a:9','c9',['Anonymous Gemara'],'Rejected proof attempt','q8'),('p5','2b:5','c5',['Anonymous Gemara'],'Compatibility answer in alternative transmission','q4')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for tag,ref,proofref in [('first','2a:12','2b:3'),('second','2b:6','2b:8')]:
 for suffix in ['receive','half','forbidden','penalty','whole']:
  cl='c'+tag+suffix;cr=next(x for x in rows if x['id']==pre+cl);pos('p'+tag+suffix,ref,cl,['רבי יהודה'],'Quoted rule; proof referent disputed in continuation',None,cr['content']['conditions'])
 for suffix in ['noheal','heal','fetusconclusion']:
  cl='c'+tag+suffix;cr=next(x for x in rows if x['id']==pre+cl);pos('p'+tag+suffix,proofref,cl,['רבי יהודה'],'Rav Ashi’s reported rationale or inference','q8' if tag=='first' else 'q4',cr['content']['conditions'])
for k,ref,a,b,rel in [('e8p','2a:8','c8permit','q8','answer'),('e8f','2a:8','c8forbid','q8','answer'),('e9','2a:9','c9','q8','answer'),('e10','2a:10','q10','c9','objection'),('e11','2a:11','c11','c9','objection'),('e11q','2a:11','c11','q10','answer'),('e5','2b:5','c5','q4','answer')]:edge(k,ref,a,b,rel)
for tag,ref,grammar,proofref in [('first','2b:1','2b:2','2b:3'),('second','2b:6','2b:7','2b:8')]:
 for k,a,b,rel,anchor in [('a','c'+tag+'animal','q'+tag+'fetus','answer',ref),('m','q'+tag+'masc','c'+tag+'animal','objection',grammar),('f','c'+tag+'fem','q'+tag+'masc','answer',grammar),('p','q'+tag+'priest','c'+tag+'animal','objection',grammar),('preg','c'+tag+'pregnant','q'+tag+'priest','answer',grammar),('ext','c'+tag+'extension','q'+tag+'priest','answer',grammar),('heal','c'+tag+'noheal','c'+tag+'heal','support',proofref),('concl','c'+tag+'heal','c'+tag+'fetusconclusion','support',proofref),('answer','c'+tag+'fetusconclusion','q8' if tag=='first' else 'q4','answer',proofref)]:edge('e'+tag+k,anchor,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local sale-of-fetus discussion. First inquiry and alternative Mishnah-attached transmission retained as separate occurrences; no unique-topic count inferred. Referent emendation and pregnant-fattening answer are attempted-proof analysis, not permission of the fetus concluded by Rav Ashi.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read2a7–3a19 continuation. Omission pass preserves rejected silence inference, distinct baraita duties/penalty, masculine/feminine correction, pregnant-fattening distinction and both RavAshi conclusions. Alternative transmission remains separate. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch01_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch01_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch01_receipt.json',r.encoded(out));print(r.encoded(out).decode())
