from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.chapterend.20261126w3.'
assert r.sha(r.encoded(state))=='080a706cb53a11cce3db1bf8831f8b406f6797014a56b9cec0495580bf6fa99b'
refs=['12b:'+str(n) for n in range(16,28)]+['13a:'+str(n) for n in range(1,9)]
add('s1','structure',refs[:7],dict(title='Redemption animal loss, donkey death and restricted human-firstborn analogy',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[7:15],dict(title='Immediate redemption versus thirty days: successive resolutions and tannaitic distinction',primary=True,boundary='closed',legacy_ids=[]))
add('s3','structure',refs[15:19],dict(title='Priority of redemption and other paired commandments',primary=True,boundary='closed',legacy_ids=[]))
add('s4','structure',['13a:8'],dict(title='End of first chapter colophon',primary=True,boundary='closed',legacy_ids=[]))
c('c16e','12b:16','Rabbi Eliezer requires replacement liability if the designated donkey-redemption animal dies, like the five sela of human-firstborn redemption.',cond=['Redemption animal set aside','It dies before delivery'])
c('c16s','12b:16','The Sages impose no replacement liability, comparing second-tithe redemption.',cond=['Redemption animal set aside','It dies before delivery'])
c('c17testimony','12b:17','Rabbi Yehoshua and Rabbi Tzadok testified that if the donkey-redemption animal dies the priest has no claim.')
c('c17ebury','12b:17','If the firstborn donkey dies, Rabbi Eliezer requires its burial.')
c('c17elamb','12b:17','In that case Rabbi Eliezer permits benefit from the lamb.')
c('c17snobury','12b:17','The Sages do not require the donkey’s burial.')
c('c17slamb','12b:17','The Sages assign the lamb to the priest.')
q('q18','12b:18','What is Rabbi Eliezer’s reason for replacement liability?')
c('c18','12b:18','Rav Yosef derives it from the human-firstborn analogy in the redemption verse.')
q('q19','12b:19','Abaye asks whether that analogy should also permit benefit from the impure animal firstborn as for a human firstborn.')
c('c19burial','12b:19','The objection reads Rabbi Eliezer’s burial requirement as evidence of prohibited benefit.')
c('c20reply','12b:20','A proposed reply reads burial as analogous to human-firstborn burial rather than proof of prohibited benefit.',mode='challenged')
q('q20','12b:20','Would only a human firstborn require burial and not another human?')
c('c21','12b:21','A further baraita says Rabbi Eliezer concedes separation of a lamb for a doubtful firstborn donkey with the lamb retained by its owner.')
c('c22','12b:22','Rava restricts the analogy through the verse: comparison is for redemption, not other matters.')
c('c23valuations','12b:23','The cited Mishnah sets valuations at their specified times.')
c('c23human','12b:23','It sets human-firstborn redemption after thirty days.')
c('c23donkey','12b:23','It sets firstborn-donkey redemption immediately.')
q('q24','12b:24','How does immediate donkey redemption fit the source setting a thirty-day minimum for valuations, human-firstborn redemption, naziriteship and firstborn donkey?')
c('c25','12b:25','That source permits extension without an upper limit.')
c('c26','12b:26','Rav Nahman interprets immediate to mean that early donkey redemption is effective.')
q('q26','12b:26','Would that imply early redemption of one’s son is ineffective, contrary to Rav’s statement that it is redeemed?')
c('c26rav','12b:26','The cited Rav statement says a son redeemed within thirty days is redeemed.')
c('c27','12b:27','The answer recalls Rava’s clarification that everyone agrees immediate-effect redemption before thirty days does not redeem the son.',cond=['Before thirty days','Redemption intended to take effect now'])
c('c1','13a:1','Rav Sheshet explains the thirty-day statement as the period before the owner transgresses through delay.')
c('c2text','13a:2','Rami bar Hama cites a source: the mitzvah is throughout thirty days, after which one redeems or breaks the neck.')
c('c2initial','13a:2','He initially reads it as a mitzvah to leave the donkey until thirty days.',mode='challenged')
c('c2reply','13a:2','The reply reads it as a mitzvah to redeem throughout the thirty days.')
q('q3','13a:3','On that reading, why not say that after thirty days one redeems or transgresses?')
c('c3','13a:3','Rava resolves the sources by distinguishing Rabbi Eliezer, who makes the human-firstborn analogy, from the Sages, who do not.')
c('c4method','13a:4','If the owner refuses redemption, the Mishnah requires neck-breaking from behind.')
c('c4burial','13a:4','It requires burial.')
c('c4priority','13a:4','Redemption takes priority over neck-breaking.')
c('c4verse','13a:4','The Mishnah supports that priority from if you do not redeem, break its neck.')
c('c5priority','13a:5','Yiud takes priority over redemption of the Hebrew maidservant.')
c('c5verse','13a:5','The Mishnah supports that priority from the verse placing non-yiud before redemption.')
c('c6before','13a:6','Originally levirate marriage took priority over halitza when intention was for the mitzvah.',cond=['Intention for the mitzvah'])
c('c6now','13a:6','The Mishnah reports that now, when intention is not for the mitzvah, halitza takes priority.',cond=['Lack of mitzvah intention in the stated later situation'])
c('c7priority','13a:7','The owner’s redemption of his consecrated property takes priority over another person’s.')
c('c7verse','13a:7','The priority is supported by if it is not redeemed, it is sold at the valuation.')
for ref,v,role in [('12b:16','Mishnah Rabbi Eliezer and Sages','Replacement liability dispute'),('12b:17','Rabbi Yehoshua/RabbiTzadok testimony, RabbiEliezer and Sages','Loss and donkey-death outcomes'),('12b:18','Rav Yosef','Human-firstborn analogy'),('12b:19','Abaye','Benefit implication objection'),('12b:20','Anonymous exchange','Burial reinterpretation challenged'),('12b:21','Anonymous Gemara quoting baraita','Doubtful-donkey counterexample'),('12b:22','Rava','Analogy restricted to redemption'),('12b:23','Quoted Mishnah','Redemption timing'),('12b:24','Anonymous Gemara','Thirty-day contradiction'),('12b:25','Quoted source continuation','No upper limit'),('12b:26','Rav Nahman and anonymous challenge citing Rav','Effectiveness interpretation'),('12b:27','Anonymous answer citing Rava','Immediate-effect son redemption condition'),('13a:1','Rav Sheshet','Delay transgression interpretation'),('13a:2','Rami bar Hama and anonymous reply','Thirty-day mitzvah reading'),('13a:3','Anonymous objection and Rava','Tannaitic resolution'),('13a:4','Mishnah','Redemption priority'),('13a:5','Mishnah','Yiud priority'),('13a:6','Mishnah','Yibum/halitza priority changes by intention'),('13a:7','Mishnah','Owner redemption priority'),('13a:8','Chapter colophon','End marker, no halakhic proposition')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
for k,ref,surf,role,cands,scope in [('a16e','12b:16','רבי אליעזר','speaker',['רבי אליעזר'],'Replacement liability'),('a16s','12b:16','חכ"א','collective',['Sages'],'No replacement liability'),('a17y','12b:17','רבי יהושע','quoted_authority',['רבי יהושע'],'Joint testimony'),('a17t','12b:17','רבי צדוק','quoted_authority',['רבי צדוק'],'Joint testimony'),('a18','12b:18','רב יוסף','speaker',['רב יוסף'],'Redemption analogy'),('a19','12b:19','אביי','speaker',['אביי'],'Benefit objection'),('a22','12b:22','רבא','speaker',['רבא'],'Restriction to redemption'),('a26n','12b:26','אר"נ','speaker',['רב נחמן'],'Effectiveness reading'),('a26r','12b:26','רב אמר','quoted_authority',['רב'],'Early son redemption'),('a27','12b:27','רבא','quoted_authority',['רבא'],'Immediate-effect qualification'),('a1','13a:1','רב ששת','speaker',['רב ששת'],'Delay interpretation'),('a2','13a:2','רמי בר חמא','speaker',['רמי בר חמא'],'Thirty-day objection'),('a3','13a:3','רבא','speaker',['רבא'],'Final tannaitic distinction')]:att(k,ref,surf,role,cands,scope)
for k,ref,cl,h,st,qu in [('p16e','12b:16','c16e',['רבי אליעזר'],'Replacement liability',None),('p16s','12b:16','c16s',['Sages'],'No replacement liability',None),('p17t','12b:17','c17testimony',['רבי יהושע','רבי צדוק'],'Explicit joint testimony',None),('p17eb','12b:17','c17ebury',['רבי אליעזר'],'Donkey burial',None),('p17el','12b:17','c17elamb',['רבי אליעזר'],'Lamb benefit',None),('p17sb','12b:17','c17snobury',['Sages'],'No donkey burial',None),('p17sl','12b:17','c17slamb',['Sages'],'Lamb to priest',None),('p18','12b:18','c18',['רב יוסף'],'Analogy explanation','q18'),('p22','12b:22','c22',['רבא'],'Restricted analogy','q19'),('p26','12b:26','c26',['רב נחמן'],'Proposed timing resolution','q24'),('p27','12b:27','c27',['רבא'],'Condition on early son redemption','q26'),('p1','13a:1','c1',['רב ששת'],'Alternative timing resolution, later challenged','q24'),('p3','13a:3','c3',['רבא'],'Final tannaitic distinction','q24'),('p4','13a:4','c4priority',['Anonymous Mishnah'],'Priority',None),('p5','13a:5','c5priority',['Anonymous Mishnah'],'Priority',None),('p6b','13a:6','c6before',['Anonymous Mishnah'],'Original intention-dependent priority',None),('p6n','13a:6','c6now',['Anonymous Mishnah'],'Later intention-dependent priority',None),('p7','13a:7','c7priority',['Anonymous Mishnah'],'Priority',None)]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e16','12b:16','c16s','c16e','distinction'),('e18','12b:18','c18','q18','answer'),('e19','12b:19','q19','c18','objection'),('e19b','12b:19','c19burial','q19','support'),('e20','12b:20','c20reply','c19burial','objection'),('e20q','12b:20','q20','c20reply','objection'),('e21','12b:21','c21','c20reply','objection'),('e22','12b:22','c22','c18','qualification'),('e22a','12b:22','c22','q19','answer'),('e26','12b:26','c26','q24','answer'),('e26q','12b:26','q26','c26','objection'),('e27','12b:27','c27','c26rav','qualification'),('e27a','12b:27','c27','q26','answer'),('e1','13a:1','c1','q24','answer'),('e2i','13a:2','c2initial','c1','objection'),('e2r','13a:2','c2reply','c2initial','correction'),('e3q','13a:3','q3','c2reply','objection'),('e3','13a:3','c3','q24','local_resolution'),('e4','13a:4','c4verse','c4priority','support'),('e5','13a:5','c5verse','c5priority','support'),('e6','13a:6','c6now','c6before','qualification'),('e7','13a:7','c7verse','c7priority','support')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='First chapter final units. Redemption-lamb death versus donkey death distinct; human-firstborn analogy restricted by Rava. Timing resolutions preserve earlier hypotheses before tannaitic distinction. Mitzvah priorities reported with intention and temporal conditions; no contemporary ruling supplied.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read12b16–13a26 and omission reread12b16–13a8. Loss objects/beneficiaries separated, explicit joint testimony and analogy restriction retained, timing objections followed through Rava resolution, priorities scoped, chapter colophon has no invented legal claim. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch29_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch29_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch29_receipt.json',r.encoded(out));print(r.encoded(out).decode())
