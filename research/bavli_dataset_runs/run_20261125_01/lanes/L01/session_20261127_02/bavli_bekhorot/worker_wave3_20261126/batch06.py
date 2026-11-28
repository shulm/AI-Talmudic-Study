from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.mari.20261126w3.'
assert r.sha(r.encoded(state))=='941f3c694b3a757b74be0fcf9bb9defef017b9220d1c20d184f9e6416a5fad9d'
refs=['3b:'+str(n) for n in range(10,15)]
add('s10','structure',refs[:1],dict(title='Rava response to a convert receiving animals to fatten',primary=True,boundary='closed',legacy_ids=[]))
add('s11','structure',refs[1:],dict(title='Rav Mari ear-transfer practice and alternative explanations of herd loss',primary=True,boundary='closed',legacy_ids=[]))
for n,voice,role in [(10,'Narrator and Rava','Applied response'),(11,'Narrator','Practice and herd loss'),(12,'Anonymous Gemara','Motive and loss questions'),(13,'Anonymous Gemara quoting Rav Yehuda','Objection and sanctity distinction'),(14,'Anonymous alternative','Risk of imitation explanation')]:add('u'+str(n),'utterances',['3b:'+str(n)],dict(textual_voice=voice,discourse_role=role,composition='composite'))
c('c10case',('3b:10','ההיא גיורתא דהוו מסרין לה אחי חיותא לפטומה אתאי לקמיה דרבא'),'A convert whose brothers entrusted animals to her for fattening came before Rava.')
c('c10rava',('3b:10','לית דחש לה להא דרבי יהודה דאמר שותפות עובד כוכבים חייבת בבכורה'),'Rava told her that Rabbi Yehuda’s view imposing firstborn status in non-Jewish partnership is not followed in this case.',cond=['The entrusted-animal case presented to Rava'])
c('c11ear',('3b:11','הוה מקנה לאודנייהו לעובד כוכבים'),'Rav Mari bar Rahel would transfer ownership of the animals’ ears to a non-Jew.')
c('c11shear',('3b:11','ואסר להו בגיזה ועבודה'),'He nevertheless prohibited shearing and work with them.')
c('c11priest',('3b:11','ויהיב להו לכהנים'),'He gave them to priests.')
c('c11loss',('3b:11','וכלאי חיותא דרב מרי בר רחל'),'The narrative reports that Rav Mari bar Rahel’s livestock died out.')
q('q12why',('3b:12','וכי מאחר דאסר להו בגיזה ועבודה ויהיב להו לכהנים אמאי מקנה להו לאודנייהו לעובד כוכבים'),'If he prohibited shearing/work and gave them to priests, why transfer the ears?')
c('c12motive',('3b:12','דלמא אתי בהו לידי תקלה'),'The answer gives concern about coming to a prohibited mishap with them.',mode='hypothetical')
q('q12loss',('3b:12','אי הכי מאי טעמא כלו חיותא דרב מרי'),'If so, why did Rav Mari’s livestock die out?')
c('c12loss',('3b:12','משום דמפקע להו מקדושתייהו'),'The first explanation attributes the loss to removing their sanctity.')
q('q13',('3b:13','והאמר רב יהודה מותר לאדם להטיל מום בבכור קודם שיצא לאויר העולם'),'How does that explanation accord with Rav Yehuda’s permission to blemish a firstborn before birth?')
c('c13permit',('3b:13','מותר לאדם להטיל מום בבכור קודם שיצא לאויר העולם'),'Rav Yehuda permits imposing a blemish on a firstborn before it comes into the world.',cond=['Before birth'])
c('c13altar',('3b:13','התם מקדושת מזבח קא מפקע ליה'),'The answer says the prenatal blemish removes altar sanctity.')
c('c13priest',('3b:13','מקדושת כהן לא מפקע ליה'),'It does not remove the priest’s entitlement.')
c('c13ear',('3b:13','הכא אפי\' מקדושת כהן קא מפקע ליה'),'Here the ownership transfer removes even the priest’s entitlement.')
c('c14skill',('3b:14','רב מרי בר רחל ידע לאקנויי קנין גמור'),'The alternative explanation recognizes that Rav Mari knew how to effect a complete transfer.')
c('c14imitate',('3b:14','וחזי ליה איניש אחרינא ואזיל ועביד וסבר רב מרי מילתא הוא דעבד ואתי בה לידי תקלה'),'It instead identifies the risk that another person would imitate the practice, regard it as mere words, and incur a mishap.',mode='hypothetical',cond=['Observer imitates without effecting the same complete acquisition'])
for k,ref,surface,role,cands,scope in [('a10','3b:10','רבא','speaker',['רבא'],'c10rava'),('a10y','3b:10','רבי יהודה','quoted_authority',['רבי יהודה'],'Position described but not followed in Rava response'),('a11','3b:11','רב מרי בר רחל','position_holder',['רב מרי בר רחל'],'Reported practice, not a transmission'),('a13','3b:13','רב יהודה','quoted_authority',['רב יהודה'],'c13permit')]:att(k,ref,surface,role,cands,pre+scope if scope.startswith('c') else scope)
for k,ref,cl,h,status,question in [('p10','3b:10','c10rava',['רבא'],'Applied response',None),('p11e','3b:11','c11ear',['רב מרי בר רחל'],'Reported conduct with loss and criticism in continuation',None),('p11s','3b:11','c11shear',['רב מרי בר רחל'],'Reported restriction',None),('p11p','3b:11','c11priest',['רב מרי בר רחל'],'Reported conduct',None),('p12m','3b:12','c12motive',['Anonymous Gemara'],'Proposed motive','q12why'),('p12l','3b:12','c12loss',['Anonymous Gemara'],'First explanation; alternative follows','q12loss'),('p13','3b:13','c13permit',['רב יהודה'],'Quoted permission under prenatal condition',None),('p14','3b:14','c14imitate',['Anonymous Gemara'],'Alternative explanation; no selection made','q12loss')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for k,ref,a,b,rel in [('e12m','3b:12','c12motive','q12why','answer'),('e12l','3b:12','c12loss','q12loss','answer'),('e13q','3b:13','q13','c12loss','objection'),('e13s','3b:13','c13permit','q13','support'),('e13a','3b:13','c13altar','q13','answer'),('e13p','3b:13','c13priest','q13','answer'),('e13e','3b:13','c13ear','q13','answer'),('e13d','3b:13','c13priest','c13ear','distinction'),('e14','3b:14','c14imitate','q12loss','answer'),('e14s','3b:14','c14skill','c14imitate','distinction')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local practice narratives and anonymous explanations. Alternative explanations of herd loss remain alternatives; narrative causal explanations are reported, not independently established facts.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source read3b10–4a13. Omission reread distinguishes RabbiYehuda tannaitic partnership view from RavYehuda prenatal permission, narrative conduct from permission, altar/priest sanctity, and two herd-loss explanations. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch06_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch06_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch06_receipt.json',r.encoded(out));print(r.encoded(out).decode())
