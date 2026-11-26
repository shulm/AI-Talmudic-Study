from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.offspring_rights.20261126w3.'
assert r.sha(r.encoded(state))=='be5427ca6f63168a478242b33693783689d8cb95183adad4a9977a92c0e48ef0'
refs=['2b:'+str(n) for n in range(9,23)]+['3a:1','3a:2']
add('s','structure',refs,dict(title='Sale of an animal for its offspring: competing rationales and failed proof readings',primary=True,boundary='closed',legacy_ids=[]))
voices={9:'Anonymous inquiry',10:'Anonymous hypothesis for Rabbi Yehuda',11:'Anonymous alternative for Rabbi Yehuda',12:'Anonymous hypothesis for Sages',13:'Anonymous alternative for Sages',14:'Anonymous objection citing Sages',15:'Anonymous reconstruction of Sages argument',16:'Continuation of reconstructed Sages argument',17:'Reconstructed Rabbi Yehuda reply',18:'Anonymous attempted proof',19:'Anonymous objection citing father of Shmuel',20:'Anonymous response and rationale',21:'Baraita quoting Rabbi Yehuda',22:'Baraita quoting Sages'}
for n in range(9,23):add('u'+str(n),'utterances',['2b:'+str(n)],dict(textual_voice=voices[n],discourse_role='Local inquiry and proof analysis',composition='composite'))
for n in [1,2]:add('u3a'+str(n),'utterances',['3a:'+str(n)],dict(textual_voice='Anonymous Gemara',discourse_role='Proposed referent rejected and confirming inference',composition='composite'))
q('q9','2b:9','What is the rule if one sells an animal for its offspring, under Rabbi Yehuda and under the Sages?')
c('c10','2b:10','One hypothesis limits Rabbi Yehuda’s permission to a broken animal unlikely to be confused with an ordinary animal, prohibiting the whole animal here.',mode='hypothetical',cond=['Selling a whole animal for its offspring','If likelihood of confusing the sale with an ordinary whole-animal sale is decisive'])
c('c11','2b:11','The alternative infers greater reason for permission here because the seller’s connection to the whole animal is not severed, unlike a broken-animal sale.',mode='hypothetical',cond=['Selling a whole animal for its offspring','Seller retains connection to the animal'])
c('c12','2b:12','One hypothesis limits the Sages’ prohibition to the broken-animal sale that severs the seller’s connection, permitting the whole animal here where it is retained.',mode='hypothetical',cond=['Selling a whole animal for its offspring','Seller retains connection to the animal'])
c('c13','2b:13','The alternative infers prohibition here all the more from the Sages’ prohibition of a broken animal: a whole animal is more liable to confusion.',mode='hypothetical',cond=['Selling a whole animal for its offspring','If confusion with an ordinary whole-animal sale is decisive'])
q('q14','2b:14','Is confusion really the Sages’ reason, when their objection to Rabbi Yehuda cites breeding the animal and its giving birth?')
c('c14','2b:14','The objection infers that the Sages’ reason concerns offspring rather than confusion.',mode='hypothetical')
c('c15own',('2b:15','טעמא דידן משום דאתיא לאיחלופי בבהמה'),'The answer reconstructs the Sages as maintaining confusion as their own reason.')
c('c15other',('2b:15','אלא את מ"ט שרית משום דאין יכולה להתרפאות כמאן דזבנה לשחיטה דמי'),'Their challenge instead addresses Rabbi Yehuda’s reasoning: an incurably broken animal is treated as sold for slaughter.')
c('c16','2b:16','The Sages object that breeding and birth would make the buyer retain the animal instead of slaughtering it.')
c('c17','2b:17','Rabbi Yehuda replies “when it gives birth,” explaining that it does not accept a male; the proposed breeding premise does not hold.')
c('c18','2b:18','An attempted proof infers permission of giving on contract from absence there of the phrase “although not permitted.”',mode='hypothetical')
q('q19',('2b:19','וליטעמיך המשתתף לו דלא קתני הכי נמי דרשאי'),'Would the same omission make partnership permitted?')
c('c19ban',('2b:19','אסור לאדם שיעשה שותפות עם העובד כוכבים'),'The father of Shmuel prohibits entering partnership with a non-Jew in the stated concern.')
c('c19risk',('2b:19','שמא יתחייב לו שבועה ונשבע לו בשם עבודת כוכבים שלו'),'The concern is that the partner may become obligated to swear and swear by his deity.',mode='hypothetical')
c('c19verse',('2b:19','והתורה אמרה לא ישמע על פיך'),'The argument cites the Torah’s ban on the name being heard through one’s mouth.')
c('c20extend',('2b:20','אלא תנא מכירה והוא הדין לשותפות ה"נ תנא מכירה והוא הדין לקבלנות'),'The prohibition phrase is given for sale and applies to partnership and contracting too, defeating the inference from omission.')
q('q20',('2b:20','ומאי שנא מכירה דנקט'),'Why does the text state the qualification specifically for sale?')
c('c20reason',('2b:20','דעיקר מכירה היא'),'The answer says that sale is the principal case.')
c('c21appraise',('2b:21','המקבל בהמה מן העובד כוכבים וילדה מעלין אותו בשוויו'),'The quoted Rabbi Yehuda rule appraises the offspring of an animal received from a non-Jew on contract.',cond=['Animal received from a non-Jew on contract','Animal gave birth'])
c('c21half',('2b:21','ונותן חצי דמיו לכהן'),'The rule gives half its value to a priest in that case.',cond=['Animal received from a non-Jew on contract','Animal gave birth'])
c('c21ban',('2b:21','והנותן בקבלה אע"פ שאינו רשאי'),'The converse giving-on-contract case is stated to be forbidden.',cond=['Giving to a non-Jew on contract','Referent debated in3a1'])
c('c21penalty',('2b:21','קונסין אותו עד עשרה בדמיו'),'That case has a penalty up to ten times its value.',cond=['Giving to a non-Jew on contract','Referent debated in3a1'])
c('c21whole',('2b:21','ונותן כל דמיו לכהן'),'The rule gives all its value to a priest.',cond=['Giving to a non-Jew on contract','Referent debated in3a1'])
c('c22','2b:22','The Sages exempt from firstborn status whenever a non-Jew has an interest in the animal.',cond=['Non-Jewish interest in the animal'])
q('q3a1',('3a:1','מאי לאו אבהמה'),'Does the quoted prohibition concern the animal, supporting the attempted proof?')
c('c3a1',('3a:1','לא אעובר'),'The answer rejects that proof reading and assigns it to the fetus.')
c('c3a2','3a:2','The phrase imposing a penalty up to ten times its value is taken to support the fetus reading.')
for k,ref,surface,role,cands,scope in [('a14','2b:14','אמרו לו','collective',['חכמים'],'Objection to Rabbi Yehuda in cited baraita'),('a15','2b:15','הכי קא"ל','anonymous',[],'Reconstruction of Sages argument'),('a17','2b:17','ואמר להו','quoted_authority',['רבי יהודה'],pre+'c17'),('a19','2b:19','אבוה דשמואל','quoted_authority',['אבוה דשמואל'],'Partnership prohibition; not Shmuel himself'),('a21','2b:21','רבי יהודה','quoted_authority',['רבי יהודה'],'Repeated penalty baraita'),('a22','2b:22','וחכמים','collective',['חכמים'],pre+'c22')]:att(k,ref,surface,role,cands,scope)
for k,ref,cl,h,status,question in [('p10','2b:10','c10',['Anonymous Gemara'],'Hypothetical Rabbi Yehuda inference','q9'),('p11','2b:11','c11',['Anonymous Gemara'],'Alternative Rabbi Yehuda inference','q9'),('p12','2b:12','c12',['Anonymous Gemara'],'Hypothetical Sages inference','q9'),('p13','2b:13','c13',['Anonymous Gemara'],'Alternative Sages inference','q9'),('p15','2b:15','c15own',['חכמים'],'Anonymous reconstruction of their own rationale','q14'),('p16','2b:16','c16',['חכמים'],'Reconstructed challenge to opponent’s reasoning',None),('p17','2b:17','c17',['רבי יהודה'],'Reported reply',None),('p19','2b:19','c19ban',['אבוה דשמואל'],'Quoted prohibition',None),('p22','2b:22','c22',['חכמים'],'Quoted exemption',None),('p3a1','3a:1','c3a1',['Anonymous Gemara'],'Rejection of attempted animal reading','q3a1')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for suffix in ['appraise','half','ban','penalty','whole']:
 cl='c21'+suffix;cr=next(x for x in rows if x['id']==pre+cl);pos('p21'+suffix,'2b:21',cl,['רבי יהודה'],'Quoted rule; referent interpreted in3a1',None,cr['content']['conditions'])
for k,ref,a,b,rel in [('e10','2b:10','c10','q9','answer'),('e11','2b:11','c11','q9','answer'),('e12','2b:12','c12','q9','answer'),('e13','2b:13','c13','q9','answer'),('e14','2b:14','q14','c13','objection'),('e14s','2b:14','c14','q14','support'),('e15','2b:15','c15own','q14','answer'),('e15d','2b:15','c15own','c15other','distinction'),('e16','2b:16','c16','c15other','objection'),('e17','2b:17','c17','c16','objection'),('e18','2b:18','c18','q9','answer'),('e19','2b:19','q19','c18','objection'),('e19b','2b:19','c19ban','q19','support'),('e19r','2b:19','c19risk','c19ban','support'),('e19v','2b:19','c19verse','c19ban','support'),('e20','2b:20','c20extend','c18','objection'),('e20a','2b:20','c20reason','q20','answer'),('e3a1','3a:1','c3a1','q3a1','answer'),('e3a2','3a:2','c3a2','c3a1','support'),('e22','2b:22','c22','c21half','distinction')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local inquiry about animal sold for offspring. Four hypothetical rationales remain proposals; proof referent is redirected to fetus in3a1. No unsupported final permission/prohibition for the whole-animals offspring-rights inquiry is supplied.'
 if x['id']==pre+'c17':x['uncertainty'].append('Compact ironic formulation לכשתלד preserved; explanation follows explicit דלא מקבלת זכר, without importing further biology.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source read2b9–3a19. Omission reread preserves four hypotheses, own/opponent rationale distinction, breeding reply, rejected omission proof, father-of-Shmuel identity, repeated baraita occurrence, Sages exemption and reversed proposed referent. Completed '+layer+' pass; no final rule invented.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch02_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch02_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch02_receipt.json',r.encoded(out));print(r.encoded(out).decode())
