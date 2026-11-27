from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.shema_language.20261127e5.'
assert r.sha(r.encoded(state))=='f945efff2852925bdf621f4936c8bd6e32fd23d801cd6844ccb12c94dad2cc08'
refs=['13a:'+str(i) for i in range(16,36)]
for k,rr,title in [('m',refs[:6],'Mishnah: intention, greetings, paragraph boundaries and order'),('intent',refs[6:9],'Inference of intention requirement and proofreading answer'),('language',refs[9:],'Shema language, audible reading, order and rejected generalizations')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Anonymous Mishnah','Rabbi Meir','Rabbi Yehuda','Anonymous Mishnah','Rabbi Yehuda','Rabbi Yehoshua ben Korha','Anonymous proposed inference','Anonymous reinterpretation and objection','Anonymous answer','Baraita: Rabbi and sages','Explanation of Rabbi','Explanation of sages','Objection and Rabbi’s derivation','Sages position alignment','Objection and sages’ derivation','Rabbi’s derivation and sages’ method','Proposed generalization about Rabbi','Anonymous rejection of inference','Proposed generalization about sages','Anonymous rejection of inference']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Mishnaic rule or dialectical analysis',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('16','13a:16','A person reading Torah when recitation time arrives fulfills the obligation if directing the heart.',['Anonymous Mishnah'],cond=['Reading Torah','Time of Shema arrives','Directs heart'],unc=['The Gemara13a23–24 reads this as intending to read in a proofreading case; do not automatically infer that all commandments require intention.'])
claim('17parts','13a:17','Rabbi Meir permits initiating a greeting between sections out of respect and responding.',['Rabbi Meir'],cond=['Between sections','Respect'],unc=['Mishnah leaves response motive unstated. Continuation13b27–14a2 rejects unrestricted response and explains even more so response under the same stated condition.'])
claim('17middle','13a:17','Rabbi Meir permits initiating in the middle out of fear and responding.',['Rabbi Meir'],cond=['Within a section','Fear'],unc=['Response scope is clarified by13b29–14a2; do not equate this to Rabbi Yehuda’s broader permission.'])
claim('18middle','13a:18','Rabbi Yehuda permits initiating in the middle out of fear and responding out of respect.',['Rabbi Yehuda'],cond=['Within a section'])
claim('18parts','13a:18','Rabbi Yehuda permits initiating between sections out of respect and returning greeting to anyone.',['Rabbi Yehuda'],cond=['Between sections'])
claim('19','13a:19','Section boundaries are first/second blessing, second/Shema, Shema/Ve-haya im shamoa, Ve-haya im shamoa/Vayomer and Vayomer/Emet ve-Yatziv.',['Anonymous Mishnah'])
claim('20','13a:20','Rabbi Yehuda forbids interruption between Vayomer and Emet ve-Yatziv.',['Rabbi Yehuda'],cond=['Boundary Vayomer/Emet ve-Yatziv'])
q('q21','13a:21','Why does Shema precede Ve-haya im shamoa?')
claim('21king','13a:21','Rabbi Yehoshua ben Korha explains that one first accepts the yoke of Heaven’s kingdom and then that of commandments.',['Rabbi Yehoshua ben Korha'])
claim('21day','13a:21','Ve-haya im shamoa precedes Vayomer because the former applies day and night and the latter only by day.',['Rabbi Yehoshua ben Korha'],unc=['This is the local rationale for paragraph order; do not infer that Exodus remembrance is excluded at night.'])
claim('22','13a:22','The discussion proposes deriving from the Mishnah that commandments require intention.',['Anonymous Gemara'],status='Proposed inference, not established conclusion')
claim('23','13a:23','It reinterprets directing the heart as intending to read.',['Anonymous Gemara'],status='Alternative explanation of Mishnah')
q('q23','13a:23','If intending to read, was he not already reading?')
claim('24','13a:24','The answer places the Mishnah in a case of reading to proofread.',['Anonymous Gemara'],status='Resolves objection to alternative explanation; blocks general inference')
claim('25rabbi','13a:25','Rabbi requires Shema as written.',['Rabbi'],status='Original-language position')
claim('25sages','13a:25','The sages permit Shema in any language.',['Sages'])
q('q26','13a:26','What is Rabbi’s reason?')
claim('26','13a:26','Rabbi derives from ve-hayu that they remain as they are.',['Rabbi'])
q('q27','13a:27','What is the sages’ reason?')
claim('27','13a:27','The sages read shema as in any language you understand.',['Sages'])
q('q28','13a:28','How does Rabbi account for shema?')
claim('28','13a:28','Rabbi needs shema to require hearing with one’s ears what one utters.',['Rabbi'])
claim('29','13a:29','The sages align with the view that one who did not make it audible to the ear fulfilled the obligation.',['Sages'],cond=['Did not hear own utterance'],unc=['This states retrospective validity, not an explicit instruction to omit audible recitation.'])
q('q30','13a:30','How do the sages account for ve-hayu?')
claim('30','13a:30','The sages use ve-hayu to prohibit reading in reverse order.',['Sages'])
q('q31','13a:31','From where does Rabbi derive not reading in reverse?')
claim('31rabbi','13a:31','Rabbi derives the order requirement from devarim/ha-devarim.',['Rabbi'])
claim('31sages','13a:31','The sages do not expound the devarim/ha-devarim difference.',['Sages'])
q('q32','13a:32','Does Rabbi therefore hold the whole Torah was said in any language, since otherwise ve-hayu would be unnecessary?')
claim('33','13a:33','Ve-hayu is necessary because shema is written; the proposed general conclusion about Rabbi does not follow.',['Anonymous Gemara'],status='Rebuttal to inference, not positive determination of whole-Torah language')
q('q34','13a:34','Do the sages therefore hold the whole Torah was said in the sacred language, since otherwise shema would be unnecessary?')
claim('35','13a:35','Shema is necessary because ve-hayu is written; the proposed general conclusion about the sages does not follow.',['Anonymous Gemara'],status='Rebuttal to inference, not positive determination of whole-Torah language')
for k,ref,surface,name in [('17','13a:17',"ר' מאיר",'רבי מאיר'),('18','13a:18',"ר' יהודה",'רבי יהודה'),('20','13a:20',"ר' יהודה",'רבי יהודה'),('21','13a:21',"ר' יהושע בן קרחה",'רבי יהושע בן קרחה'),('25r','13a:25','רבי','רבי'),('25s','13a:25','חכ"א','חכמים')]:att('a'+k,ref,surface,'speaker',[name],'Named rule or rationale')
for k,ref,a,b,rel in [('18m','13a:18','c18middle','c17middle','distinction'),('18p','13a:18','c18parts','c17parts','distinction'),('20','13a:20','c20','c19','qualification'),('21','13a:21','c21king','q21','answer'),('22','13a:22','c16','c22','support'),('23','13a:23','c23','c22','objection'),('23q','13a:23','q23','c23','objection'),('24','13a:24','c24','q23','answer'),('25','13a:25','c25sages','c25rabbi','distinction'),('26','13a:26','c26','q26','answer'),('26s','13a:26','c26','c25rabbi','support'),('27','13a:27','c27','q27','answer'),('27s','13a:27','c27','c25sages','support'),('28','13a:28','c28','q28','answer'),('29','13a:29','c29','c28','distinction'),('30','13a:30','c30','q30','answer'),('31','13a:31','c31rabbi','q31','answer'),('31d','13a:31','c31sages','c31rabbi','distinction'),('33','13a:33','c33','q32','answer'),('35','13a:35','c35','q34','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['id']==pre+'e22':x['uncertainty'].append('This support is the initial proposed inference only;13a23–24 defeats its necessity.')
 if x['layer']=='claims':x['content']['scope']='Local Mishnah and Gemara. Mishnaic greetings were checked against13b27–14a2; language discussion stops at rejected whole-Torah generalizations without assigning either unproved position.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read13a16–14a21 including greeting reinterpretation; reread core13a16–35 for named positions, paragraph order, intention/proofreading distinction, source of both language positions, audibility validity, reverse order and rejected global deductions. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch23_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch23_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch23_receipt.json',r.encoded(out));print(r.encoded(out).decode())
