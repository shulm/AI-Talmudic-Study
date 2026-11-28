from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.workers_groom.20261127e5.'
assert r.sha(r.encoded(state))=='12b00297ca4809a992797eca509c0c53cf00faa638b812ff50273c17afe0ecb6'
refs=['16a:'+str(i) for i in range(7,24)]+['16b:'+str(i) for i in range(1,5)]
for k,rr,title in [('m',refs[:2],'Mishnah: workers and bridegroom'),('workers',refs[2:13],'Workers’ attention, prayer and meal blessings'),('groom',refs[13:],'Commandment preoccupation and bridegroom exemption')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Anonymous Mishnah','Anonymous Mishnah and Rabban Gamliel narrative','Baraita','Rav Mari son of Shmuel’s daughter to Rava','Rava and Rav Mari dialogue citing Rav Sheshet','Anonymous objection from Beit Hillel','Anonymous first/second paragraph distinction','Baraita','Rav Sheshet proposed tannaitic distinction','Anonymous objection','Anonymous revised employment distinction','Supporting workers’ baraita','Wage/meal/employer qualification','Baraita of groom exemption','Rav Pappa derivation','Anonymous challenge','Anonymous possessive-word derivation','Anonymous widow challenge','Anonymous preoccupation distinction','Anonymous ordinary distress objection citing Rav','Anonymous commandment/optional distinction']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Scoped rule, narrative or dialectic',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('7','16a:7','Workers recite Shema atop a tree or a wall course, unlike prayer.',['Anonymous Mishnah'],cond=['Workers at elevated worksite'])
claim('8exempt','16a:8','A bridegroom is exempt from Shema on the first night until after Shabbat if the marital act has not occurred.',['Anonymous Mishnah'],cond=['Bridegroom','Has not performed marital act'],unc=['Timing wording preserved; no calendar scenario beyond the source supplied.'])
claim('8gamliel','16a:8','Rabban Gamliel recited on his wedding’s first night and answered the students’ exemption objection that he would not remove Heaven’s kingdom even for an hour.',['Rabban Gamliel'],status='Individual narrated conduct; not denial of taught exemption')
q('q8','16a:8','Students challenge Rabban Gamliel’s recitation given his teaching of bridegroom exemption.')
claim('9workers','16a:9','Workers recite Shema atop tree or wall course; for prayer they may remain atop olive or fig trees but descend from other trees.',['Anonymous baraita'],cond=['Worker'])
claim('9owner','16a:9','The employer descends for prayer in either case because his mind is not settled.',['Anonymous baraita'],cond=['Employer'])
q('q10','16a:10','Rav Mari asks Rava how workers’ elevated recitation fits the requirement of heart intention, derived by comparing Shema with hasket u-shema.')
claim('10intent','16a:10','The cited baraita requires intention, linking Shema to attentive listening in hasket u-shema.',['Anonymous baraita'],status='Requirement used to challenge inferred lack of attention')
claim('11','16a:11','After Rava’s silence and request for a teaching, the reply reports Rav Sheshet requiring workers to stop work while reciting.',['Rav Sheshet'],status='Condition answering attention objection',unc=['Pronoun dialogue follows Rav Mari supplying Rav Sheshet’s teaching to Rava; no ruling assigned to Rava’s silence.'])
q('q12','16a:12','But Beit Hillel permit continuing work while reciting?')
claim('12hillel','16a:12','Beit Hillel’s cited teaching permits work during recitation.',['Beit Hillel'],status='Scope qualified next')
claim('13','16a:13','The contradiction is resolved by distinguishing the first paragraph from the second.',['Anonymous Gemara'],status='Stop work for first paragraph; work during second in context')
claim('14','16a:14','Workers for an employer recite Shema with its before/after blessings, bless before and after eating bread, and pray eighteen blessings, but do not lead prayer or lift hands for priestly blessing.',['Anonymous baraita'],cond=['Workers for employer'],unc=['Full meal/prayer provisions receive wage-versus-meal and employer-present qualifications below.'])
q('q15','16a:15','Another baraita gives an abridgment of eighteen blessings instead; how do these fit?')
claim('15','16a:15','Rav Sheshet initially assigns full and abridged prayer to Rabban Gamliel and Rabbi Yehoshua respectively.',['Rav Sheshet'],status='Proposed reconciliation rejected as insufficient')
q('q16','16a:16','If Rabbi Yehoshua, why single out workers when his rule would cover everyone?')
claim('17','16a:17','The revised explanation assigns both to Rabban Gamliel and distinguishes those working for wages from those working for their meals.',['Anonymous Gemara'],status='Replacement reconciliation',unc=['Context assigns abridgment to wage workers and full prayer to meal workers; keep employment condition.'])
claim('18','16a:18','The supporting baraita has workers recite Shema and pray, omit the pre-meal blessing and say two afterward: first normally, second begins with land and includes Jerusalem.',['Anonymous baraita'],cond=['Wage workers as clarified19'])
claim('19','16a:19','That abridgment applies to wage workers; those working for meals, or with employer reclining with them, bless normally.',['Anonymous baraita'],cond=['Meal compensation or employer eats with them'])
claim('20engaged','16a:20','The baraita excludes one engaged in a commandment from when sitting in your house, and a bridegroom from walking on your way.',['Anonymous baraita'])
claim('20virgin','16a:20','From this it exempts one marrying a virgin and obligates one marrying a widow.',['Anonymous baraita'],cond=['Virgin versus widow marriage'])
q('q21','16a:21','How does the verse imply this?')
claim('21','16a:21','Rav Pappa argues that way signifies optional activity, and so does the compared case.',['Rav Pappa'],status='Initial derivation sharpened by23')
q('q22','16a:22','Could the traveler not be going for a commandment while still being required to recite?')
claim('23','16a:23','The possessive your going rather than going obligates one’s own journey but exempts a commandment journey.',['Anonymous Gemara'])
q('q1','16b:1','Then why distinguish marrying a virgin from marrying a widow?')
claim('2','16b:2','The first is preoccupied and the other is not.',['Anonymous Gemara'],status='Contextual distinction of these marriage cases')
q('q3','16b:3','If preoccupation alone exempts, would losing a ship at sea also exempt, despite Rav’s ruling obligating a mourner?')
claim('3rav','16b:3','Rav through Rabbi Abba bar Zavda obligates a mourner in all commandments except tefillin, called adornment in Ezekiel.',['Rav'],cond=['Mourner'],status='Counterexample to general preoccupation exemption')
claim('4','16b:4','Ordinary preoccupation differs from preoccupation for a commandment; the groom case is the latter.',['Anonymous Gemara'],status='Final qualification, not a universal distress exemption')
for k,ref,surface,name in [('8','16a:8','ר"ג','רבן גמליאל'),('10m','16a:10','רב מרי ברה דבת שמואל','רב מרי ברה דבת שמואל'),('10r','16a:10','רבא','רבא'),('11','16a:11','רב ששת','רב ששת'),('12','16a:12','בית הלל','בית הלל'),('15','16a:15','רב ששת','רב ששת'),('21','16a:21','רב פפא','רב פפא')]:att('a'+k,ref,surface,'speaker',[name],'Local named teaching, challenge or response')
att('a3','16b:3','רבי אבא בר זבדא','transmitter',['רבי אבא בר זבדא'],'Rav on mourner commandments',chain=['רבי אבא בר זבדא','רב'])
for k,ref,a,b,rel in [('8','16a:8','c8gamliel','q8','answer'),('9','16a:9','c9workers','c7','qualification'),('10','16a:10','q10','c7','objection'),('10s','16a:10','c10intent','q10','support'),('11','16a:11','c11','q10','answer'),('12','16a:12','q12','c11','objection'),('13','16a:13','c13','q12','answer'),('15','16a:15','c15','q15','answer'),('16','16a:16','q16','c15','objection'),('17','16a:17','c17','c15','correction'),('17a','16a:17','c17','q15','answer'),('18','16a:18','c18','c17','support'),('19','16a:19','c19','c18','qualification'),('21','16a:21','c21','q21','answer'),('22','16a:22','q22','c21','objection'),('23','16a:23','c23','q22','answer'),('1','16b:1','q1','c20virgin','objection'),('2','16b:2','c2','q1','answer'),('3','16b:3','q3','c2','objection'),('3s','16b:3','c3rav','q3','support'),('4','16b:4','c4','q3','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local worker and bridegroom cases. Distinguish worksite, paragraph, compensation and employer presence; retain rejected tannaitic assignment and commandment-specific preoccupation limit.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read16a7–16b25; reread core16a7–16b4 for tree species/employer distinction, first/second paragraph attention, rejected Gamliel/Yehoshua assignment, wage/meal and employer-present rules, groom narrative, possessive journey derivation, virgin/widow comparison and mourner counterexample with commandment-preoccupation resolution. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch31_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch31_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch31_receipt.json',r.encoded(out));print(r.encoded(out).decode())
