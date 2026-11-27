from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.temple_blessing.20261126e5.'
assert r.sha(r.encoded(state))=='bad44eb1c96b46c0d34f9bcfb4a991c65dbb18167931cce8d2a4e74b0dcbb499'
refs=['11b:'+str(i) for i in range(20,24)]+['12a:'+str(i) for i in range(1,10)]
for k,rr,title in [('one',refs[:7],'Temple one blessing: explicit answer versus uncertain inference'),('decalogue',refs[7:12],'Ten Commandments outside Temple and rejected reinstatement'),('watch',refs[12:],'Sabbath priestly-watch blessing')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Cited Mishnah of Temple service','Narrative questions and Rav Yehuda reporting Shmuel','Rabbi Zerika/Rabbi Ammi/Resh Lakish chain; Rav Yitzhak bar Yosef correction','Anonymous conditional inference','Anonymous counterpossibility','Anonymous question','Anonymous alternative interpretation','Repeated Mishnah lemma','Rav Yehuda reporting Shmuel','Supporting baraita of Rabbi Nathan','Rabbah bar bar Hana and Rav Hisda','Amemar and Rav Ashi','Mishnah lemma; question; Rabbi Helbo']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Ritual account or report analysis',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('20one','11b:20','The supervisor orders one blessing, and they bless and recite Ten Commandments and the three Shema sections.',['Cited Mishnah'])
claim('20three','11b:20','They bless the people with Emet ve-Yatziv, Avodah and the priestly blessing.',['Cited Mishnah'])
claim('20sabbath','11b:20','On Sabbath an additional blessing is made for the outgoing watch.',['Cited Mishnah'])
q('q21','11b:21','What was the one blessing?')
claim('21unknown','11b:21','Rabbi Abba and Rabbi Yose bar Abba could not answer when asked; Rav Matna also did not have the answer.',['Narrator'],status='Reported absence of knowledge, not a competing formula')
claim('21answer','11b:21','Rav Yehuda reports Shmuel identifying it as Ahavah Rabbah.',['Shmuel'],status='Explicit transmitted identification')
claim('22light','11b:22','Rabbi Zerika through Rabbi Ammi reports Resh Lakish identifying it as Yotzer Or.',['Resh Lakish'],status='Initial reported identification subsequently marked inferred')
claim('22inference','11b:22','Rav Yitzhak bar Yosef says Rabbi Zerika’s report was inferred, not explicit.',['Rav Yitzhak bar Yosef'],status='Provenance correction')
claim('22independent','11b:22','The explicit report attributed to Resh Lakish is that blessings do not impede one another.',['Resh Lakish'])
claim('23','11b:23','If they said Yotzer Or and omitted Ahavah Rabbah, independence of blessings is readily inferred.',['Anonymous Gemara'],status='Conditional reasoning, not independently established ritual fact')
claim('1','12a:1','If they said Ahavah Rabbah, perhaps Yotzer Or was only delayed until its time arrived, so omission is not established.',['Anonymous Gemara'],status='Counterpossibility undermining inference')
q('q2','12a:2','What difference does it make that the report was inferred?')
claim('3formula','12a:3','If inferred, they may in fact have said Ahavah Rabbah and later Yotzer Or at its proper time.',['Anonymous Gemara'],status='Live alternative, not resolved identification')
claim('3order','12a:3','Blessings not impeding one another can then refer to their order.',['Anonymous Gemara'],status='Alternative interpretation of explicit Resh Lakish statement')
claim('4','12a:4','The discussion repeats the Temple reading and blessing sequence.',['Repeated Mishnah lemma'],status='Repeated source occurrence')
claim('5','12a:5','Shmuel via Rav Yehuda says they sought the same reading outside the Temple but abolished it because of sectarian complaint.',['Shmuel'])
claim('6','12a:6','Rabbi Nathan’s baraita gives the same outside-Temple attempt and abolition reason.',['Rabbi Nathan'])
claim('7plan','12a:7','Rabbah bar bar Hana intended to institute the reading in Sura.',['Narrator'],status='Proposed reinstatement, not completed enactment')
claim('7reply','12a:7','Rav Hisda told him it had already been abolished because of sectarian complaint.',['Rav Hisda'])
claim('8plan','12a:8','Amemar intended to institute it in Nehardea.',['Narrator'],status='Proposed reinstatement')
claim('8reply','12a:8','Rav Ashi told him it had already been abolished for the same reason.',['Rav Ashi'])
q('q9','12a:9','What is the extra Sabbath blessing for the departing watch?')
claim('9','12a:9','Rabbi Helbo says the outgoing watch addresses the incoming: may He who placed His name in this house place love, brotherhood, peace and fellowship among you.',['Rabbi Helbo'],unc=['The lemma says blessing for the outgoing watch, while the explanation explicitly has outgoing addressing incoming; both wordings preserved without silent inversion.'])
att('a21a','11b:21','רבי אבא','speaker',['רבי אבא'],'Narrative participant unable to answer')
att('a21y','11b:21',"ר' יוסי בר אבא",'speaker',['רבי יוסי בר אבא'],'Narrative participant unable to answer')
att('a21m','11b:21','רב מתנה','speaker',['רב מתנה'],'Consulted authority unable to answer')
att('a21s','11b:21','רב יהודה','transmitter',['רב יהודה'],pre+'c21answer',chain=['רב יהודה','שמואל'])
att('a22','11b:22','רבי זריקא אמר רבי אמי','transmitter',['רבי זריקא'],'Resh Lakish report',chain=['רבי זריקא','רבי אמי','רבי שמעון בן לקיש'])
att('a22i','11b:22','רב יצחק בר יוסף','speaker',['רב יצחק בר יוסף'],pre+'c22inference')
att('a5','12a:5','ר יהודה אמר שמואל','transmitter',['רב יהודה'],pre+'c5',chain=['רב יהודה','שמואל'])
for k,ref,surface,name in [('6','12a:6',"ר' נתן",'רבי נתן'),('7b','12a:7','רבה בב"ח','רבה בר בר חנה'),('7h','12a:7','רב חסדא','רב חסדא'),('8a','12a:8','אמימר','אמימר'),('8r','12a:8','רב אשי','רב אשי'),('9','12a:9','ר חלבו','רבי חלבו')]:att('a'+k,ref,surface,'speaker',[name],'Local account or response')
for k,ref,a,b,rel in [('21','11b:21','c21answer','q21','answer'),('22','11b:22','c22light','q21','answer'),('22i','11b:22','c22inference','c22light','correction'),('23','11b:23','c23','c22light','support'),('1','12a:1','c1','c23','objection'),('3f','12a:3','c3formula','q2','answer'),('3o','12a:3','c3order','c22independent','qualification'),('6','12a:6','c6','c5','support'),('7','12a:7','c7reply','c7plan','objection'),('8','12a:8','c8reply','c8plan','objection'),('9','12a:9','c9','q9','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Temple ritual and transmitted-report analysis. Yotzer identification is an uncertain inference, not a forced established disagreement with Shmuel; later alternative reading of independence as order is retained.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read11b20–12b28; reread core11b20–12a9 for unknown answers, explicit Shmuel report, inferred Resh Lakish identification and alternative order interpretation, two aborted local institutions, and exact outgoing/incoming watch wording. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch19_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch19_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch19_receipt.json',r.encoded(out));print(r.encoded(out).decode())
