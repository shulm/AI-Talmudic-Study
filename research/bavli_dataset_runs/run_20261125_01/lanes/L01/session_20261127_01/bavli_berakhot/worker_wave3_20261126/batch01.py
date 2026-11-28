from pathlib import Path
helper=(Path(__file__).parent.parent/'worker_wave2_20261126/batch01.py').read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='bk.psalm_angels.20261126w3.'
refs=['4b:'+str(n) for n in range(16,27)]
assert r.sha(r.encoded(state))=='beb7c66617f160761349b7790b2b3df88ff9f95fb955e6e4d431d3819f3d22cb'
add('s16','structure',refs[:7],dict(title='Psalm145 merit, its two features, and absent nun',primary=True,boundary='closed',legacy_ids=[]))
add('s23','structure',refs[7:],dict(title='Michael and Gabriel flight expressions and identification',primary=True,boundary='closed',legacy_ids=[]))
for n,voice,role in [(16,'Rabbi Eleazar reporting Rabbi Avina','Saying'),(17,'Anonymous Gemara','Reason question'),(18,'Anonymous Gemara','First proposed explanation and objection'),(19,'Anonymous Gemara','Second proposed explanation and objection'),(20,'Anonymous Gemara','Combined explanation'),(21,'Rabbi Yohanan','Question and explanation'),(22,'Western interpreters and Rav Nahman bar Yitzhak','Alternative reading and consolation'),(23,'Rabbi Eleazar bar Avina','Comparison of scriptural flight expressions'),(24,'Anonymous Gemara','Identification question'),(25,'Rabbi Yohanan','Shared-word derivation'),(26,'Unnamed tanna','Flight counts and epidemic exception')]:
 add('u'+str(n),'utterances',['4b:'+str(n)],dict(textual_voice=voice,discourse_role=role,composition='composite'))
c('c16', '4b:16','Rabbi Eleazar reports Rabbi Avina: one who recites Tehillah leDavid three times every day is assured a share in the world to come.',cond=['Reciting Tehillah leDavid three times every day'])
q('q17','4b:17','What is the reason for this merit of Tehillah leDavid?')
c('c18hyp',('4b:18','אילימא משום דאתיא באל"ף בי"ת'),'The discussion proposes its alphabetical arrangement as the reason.',mode='hypothetical')
c('c18counter',('4b:18','נימא (תהלים קיט, א) אשרי תמימי דרך דאתיא בתמניא אפין'),'The discussion counters that Psalm119, with eightfold alphabetical arrangement, would then be preferable.',mode='challenged',cond=['If alphabetical arrangement alone explains the merit'])
c('c19hyp',('4b:19','אלא משום דאית ביה (תהלים קמה, טז) פותח את ידך'),'The discussion proposes the verse about opening Your hand as the reason.',mode='hypothetical')
c('c19counter',('4b:19','נימא הלל הגדול דכתיב ביה (תהלים קלו, כה) נותן לחם לכל בשר'),'The discussion counters that the Great Hallel also contains giving food to all flesh.',cond=['If the sustenance theme alone explains the merit'])
c('c20','4b:20','The answer combines the alphabetical arrangement and the sustenance verse.')
q('q21',('4b:21','מפני מה לא נאמר נו"ן באשרי'),'Why is there no nun verse in Ashrei?')
c('c21',('4b:21','מפני שיש בה מפלתן של שונאי ישראל'),'Rabbi Yohanan explains the omission by the fall of the enemies of Israel associated with nun.',cond=['The source euphemism is preserved; no literal hostile group is identified'])
c('c21verse',('4b:21','נפלה לא תוסיף קום בתולת ישראל'),'Amos is quoted as the fallen virgin Israel not rising again, supporting the explanation of the missing nun.')
c('c22west',('4b:22','במערבא מתרצי לה הכי נפלה ולא תוסיף לנפול עוד קום בתולת ישראל'),'The Western interpretation rereads the verse: fallen, she will not fall again; arise, virgin Israel.')
c('c22support',('4b:22',"אמר רב נחמן בר יצחק אפילו הכי חזר דוד וסמכן ברוח הקדש שנא' (תהלים קמה, יד) סומך ה' לכל הנופלים"),'Rav Nahman bar Yitzhak says that even so David returned to support them through holy inspiration with the verse that the Lord supports all who fall.')
c('c23','4b:23','Rabbi Eleazar bar Avina says what is stated about Michael is greater than what is stated about Gabriel, contrasting vayaf with muaf biyaf.')
q('q24','4b:24','How is the one seraph in the cited verse identified as Michael?')
c('c25','4b:25','Rabbi Yohanan identifies Michael by linking the word one in the seraph verse and in the verse naming Michael one of the chief princes.')
for suffix,quote,prop,cond in [('m','מיכאל באחת','The tanna gives Michael one flight.',[]),('g','גבריאל בשתים','The tanna gives Gabriel two flights.',[]),('e','אליהו בארבע','The tanna gives Elijah four flights.',[]),('d','ומלאך המות בשמנה','The tanna gives the angel of death eight flights.',['Ordinary case contrasted with epidemic exception']),('plague','ובשעת המגפה באחת','The tanna gives the angel of death one flight during an epidemic.',['During an epidemic'])]:
 c('c26'+suffix,('4b:26',quote),prop,cond=cond)
att('a16e','4b:16','רבי אלעזר','transmitter',['רבי אלעזר'],pre+'c16',chain=['רבי אלעזר','רבי אבינא'])
att('a16a','4b:16','ר אבינא','quoted_authority',['רבי אבינא'],pre+'c16',chain=['רבי אלעזר','רבי אבינא'])
att('a21','4b:21','רבי יוחנן','speaker',['רבי יוחנן'],pre+'c21')
att('a22w','4b:22','במערבא','collective',['Western interpreters'],pre+'c22west')
att('a22n','4b:22','רב נחמן בר יצחק','speaker',['רב נחמן בר יצחק'],pre+'c22support')
att('a23','4b:23','ר אלעזר בר אבינא','speaker',['רבי אלעזר בר אבינא'],pre+'c23',unc=['Source here says bar Avina;4b16 says Rabbi Eleazar reporting Rabbi Avina. Preserve distinct textual roles rather than harmonizing.'])
att('a25','4b:25',"ר' יוחנן",'speaker',['רבי יוחנן'],pre+'c25')
att('a26','4b:26','תנא','anonymous',[],'Flight-count report')
for k,ref,cl,h,status,question,cond in [
 ('p16','4b:16','c16',['רבי אבינא'],'Reported assurance',None,['Reciting Tehillah leDavid three times every day']),
 ('p18','4b:18','c18hyp',['Anonymous Gemara'],'Proposed sole explanation; challenged by Psalm119 counterexample','q17',[]),
 ('p19','4b:19','c19hyp',['Anonymous Gemara'],'Proposed sole explanation; challenged by Great Hallel counterexample','q17',[]),
 ('p20','4b:20','c20',['Anonymous Gemara'],'Combined answer','q17',[]),
 ('p21','4b:21','c21',['רבי יוחנן'],'Explanation of omission','q21',['The source euphemism is preserved; no literal hostile group is identified']),
 ('p22w','4b:22','c22west',['Western interpreters'],'Alternative construal of verse',None,[]),
 ('p22n','4b:22','c22support',['רב נחמן בר יצחק'],'Consolatory support despite preceding discussion',None,[]),
 ('p23','4b:23','c23',['רבי אלעזר בר אבינא'],'Reported comparison',None,[]),
 ('p25','4b:25','c25',['רבי יוחנן'],'Shared-word identification','q24',[])]:pos(k,ref,cl,h,status,question,cond)
for k,ref,a,b,rel in [('e18','4b:18','c18hyp','q17','answer'),('e18c','4b:18','c18counter','c18hyp','objection'),('e19','4b:19','c19hyp','q17','answer'),('e19c','4b:19','c19counter','c19hyp','objection'),('e20','4b:20','c20','q17','answer'),('e21','4b:21','c21','q21','answer'),('e21s','4b:21','c21verse','c21','support'),('e22','4b:22','c22west','c21verse','qualification'),('e22s','4b:22','c22support','c21','qualification'),('e25','4b:25','c25','q24','answer'),('e25s','4b:25','c25','c23','support'),('e26','4b:26','c26plague','c26d','qualification')]:edge(k,ref,a,b,rel)
# Replace inherited helper's domain-specific scope; all propositions above are manually source-read.
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local aggadic exposition of Psalm145 or angelic flight; descriptive source claim, not independently certified theology.'
# Counterproposal is asserted as an objection, not itself rejected.
next(x for x in rows if x['id']==pre+'c18counter')['content']['assertion_mode']='asserted'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read source4b16-26 with4b27-5a context. Omission reread retains three-times condition, both rejected single reasons, combined answer, Western rereading, distinct reporting/patronymic forms, five flight statements and epidemic exception. '+('No further distinct reconciliation record required.' if layer=='reconciliation' else 'Completed source-based '+layer+' pass.')))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_berakhot_correction',epoch=4,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch01_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch01_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch01_receipt.json',r.encoded(out));print(r.encoded(out).decode())
