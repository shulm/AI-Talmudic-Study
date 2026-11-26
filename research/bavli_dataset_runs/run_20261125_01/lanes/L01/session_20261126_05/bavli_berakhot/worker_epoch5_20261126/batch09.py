from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.reading_conduct.20261126e5.'
assert r.sha(r.encoded(state))=='5a87d3375f68d838fa132ea02e4805eaad9ad1689ff3fbbf5885779b8f8bb6f6'
refs=['8a:'+str(i) for i in range(21,31)]+['8b:'+str(i) for i in range(1,17)]
for k,rr,title in [('labor',refs[:1],'Enjoying one’s labor and fear of Heaven'),('teacher',refs[1:4],'Residence near teacher and deference'),('scroll',refs[4:9],'Leaving Torah reading and unresolved between-verses case'),('portion',refs[9:15],'Weekly double reading and translation at communal time'),('elders',refs[15:17],'Veins at slaughter and scholar forgetting involuntarily'),('sons',refs[17:22],'Rava’s advice and alternative interpretations'),('medes',refs[22:24],'Median customs and field consultation'),('persians',refs[24:],'Persian modesty and separate prophetic exposition')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rabbi Hiyya bar Ammi reporting Ulla','Rabbi Hiyya bar Ammi reporting Ulla','Anonymous baraita objection','Anonymous distinction','Rav Huna bar Yehuda reporting Rabbi Menahem reporting Rabbi Ammi','Narrator about Rabbi Abbahu','Rav Pappa','Anonymous unresolved conclusion','Rav Sheshet and narrator','Rav Huna bar Yehuda reporting Rabbi Ammi','Continuation','Rav Bibi bar Abaye and Hiyya bar Rav of Difti','Expository question and derivation','Rav Bibi and unnamed elder','Rabbi Yehoshua ben Levi addressing sons','Continuation citing Rabbi Yehuda','Continuation','Rava addressing sons; two anonymous rationales','Rava’s advice and three interpretations','Narrative about Rav Pappa; Sages’ conclusion','Repeated advice supporting Rabbi Yehoshua ben Levi','Abaye','Baraita of Rabbi Akiva','Rav Adda bar Ahava','Baraita of Rabban Gamliel','Rav Yosef']
assert len(voices)==len(refs)
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Teaching, narrative or discussion',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('21','8a:21','Ulla via Rabbi Hiyya bar Ammi ranks enjoying one’s labor above fear of Heaven: the former receives fortunate in this world and good in the next, while the latter verse lacks good for you.',['Ulla'])
claim('22','8a:22','Ulla via Rabbi Hiyya bar Ammi says to live in one’s teacher’s place; Solomon did not marry Pharaoh’s daughter while Shimei ben Gera lived.',['Ulla'],unc=['Qualified by the following deference distinction.'])
claim('23','8a:23','A baraita says not to live there.',['Unnamed baraita'],status='Opposing cited directive')
claim('24','8a:24','The answer distinguishes one who submits to him from one who does not.',['Anonymous Gemara'],status='Reconciliation by condition',unc=['Literal הא דכייף ליה הא דלא כייף ליה leaves terse pronouns; no added identification of individual persons.'])
claim('25','8a:25','Rav Huna bar Yehuda reports Rabbi Menahem reporting Rabbi Ammi: leaving the Torah scroll and going out is the case of those who forsake God perishing.',['Rabbi Ammi'])
claim('26','8a:26','Rabbi Abbahu went out between one reader and the next.',['Anonymous narrator'],status='Narrated conduct, distinct from leaving during reading')
q('q27','8a:27','Rav Pappa asks whether leaving between verses is permitted.')
claim('28','8a:28','The between-verses question is left unresolved.',['Anonymous Gemara'],status='Explicit תיקו',unc=['No permission or prohibition inferred.'])
claim('29','8a:29','Rav Sheshet turned his face and studied, saying we in ours and they in theirs.',['Rav Sheshet','Narrator'],status='Separate narrated study conduct',unc=['Not an answer resolving Rav Pappa’s leaving-between-verses question.'])
claim('30','8a:30','Rav Huna bar Yehuda reports Rabbi Ammi requiring completing portions with the congregation: twice Scripture and once translation.',['Rabbi Ammi'])
claim('1include','8b:1','This includes even Atarot and Divon.',['Continuation of reported teaching'],unc=['The source itself does not state the linguistic reason these names require emphasis.'])
claim('1reward','8b:1','One completing portions with the congregation has days and years lengthened.',['Continuation of reported teaching'],cond=['Completes portions with congregation'])
claim('2plan','8b:2','Rav Bibi bar Abaye planned to complete the whole year’s portions on the eve of Yom Kippur.',['Anonymous narrator'],status='Initial plan challenged by cited teaching')
q('q3','8b:3','Does one fast on the ninth rather than the tenth?')
claim('3','8b:3','The verse about affliction on the ninth credits one who eats and drinks on the ninth as if fasting on both ninth and tenth.',['Hiyya bar Rav of Difti’s teaching continued'],cond=['Eating and drinking on ninth'])
claim('4plan','8b:4','Rav Bibi then planned to complete the portions in advance.',['Anonymous narrator'],status='Revised plan challenged by elder')
claim('4rule','8b:4','An elder cites the teaching not to do it earlier or later.',['Unnamed elder quoting teaching'],status='Timing constraint')
claim('5','8b:5','Rabbi Yehoshua ben Levi tells his sons to complete portions with the congregation, twice Scripture and once translation.',['Rabbi Yehoshua ben Levi'])
claim('6','8b:6','He tells them to be careful regarding the veins in accordance with Rabbi Yehuda, whose Mishnah requires slaughtering the veins.',['Rabbi Yehoshua ben Levi','Rabbi Yehuda as quoted legal authority'])
claim('7','8b:7','He tells them to respect an elder who forgot learning involuntarily, since both the tablets and broken tablets lay in the ark.',['Rabbi Yehoshua ben Levi'],cond=['Forgetting due to circumstances beyond control'])
claim('8rule','8b:8','Rava tells his sons not to cut meat over the hand.',['Rava'])
claim('8danger','8b:8','One version explains this because of danger.',['One anonymous version'])
claim('8meal','8b:8','Another version explains this because of spoiling the meal.',['Other anonymous version'])
claim('9bed','8b:9','Rava tells his sons not to sit on an Aramean woman’s bed.',['Rava'],status='Advice with three alternative interpretations')
claim('9passing','8b:9','He also tells them not to pass behind synagogue while the congregation prays.',['Rava'],cond=['Congregation is praying'])
claim('9shema','8b:9','One interpretation of the bed advice is not to sleep without Shema.',['One anonymous interpretation'])
claim('9convert','8b:9','Another interpretation is not to marry a female convert.',['Another anonymous interpretation'],status='Reported interpretation of Rava’s advice to sons, not universal legal ruling')
claim('9literal','8b:9','Another interpretation takes the Aramean woman literally.',['Another anonymous interpretation'])
claim('10event','8b:10','An Aramean woman offered Rav Pappa a bed to sit on; he refused until she lifted it, revealing a dead infant.',['Anonymous narrator'],status='Narrative',unc=['No motive or planned accusation is explicitly supplied; do not invent one.'])
claim('10rule','8b:10','The Sages derive a prohibition on sitting on an Aramean woman’s bed from this incident.',['Sages as reported in source'],status='Reported source ruling')
claim('11','8b:11','The repeated advice supports Rabbi Yehoshua ben Levi’s prohibition on passing behind synagogue while the congregation prays.',['Rabbi Yehoshua ben Levi'],cond=['Congregation is praying'])
claim('12door','8b:12','Abaye limits the prohibition to when no other entrance exists; another entrance removes the objection.',['Abaye'],cond=['Other entrance exists'],status='Exception')
claim('12synagogue','8b:12','Another synagogue removes the objection.',['Abaye'],cond=['Other synagogue exists'],status='Exception')
claim('12load','8b:12','Carrying a load removes the objection.',['Abaye'],cond=['Carries load'],status='One of independently sufficient final exceptions')
claim('12run','8b:12','Running removes the objection.',['Abaye'],cond=['Runs'],status='One of independently sufficient final exceptions')
claim('12tefillin','8b:12','Wearing tefillin removes the objection.',['Abaye'],cond=['Wears tefillin'],status='One of independently sufficient final exceptions')
for k,text in [('meat','Rabbi Akiva appreciates Medes cutting meat only on a table.'),('kiss','He appreciates their kissing only the back of the hand.'),('field','He appreciates their consulting only in the field.')]:claim('13'+k,'8b:13',text,['Rabbi Akiva'])
q('q14','8b:14','Rav Adda bar Ahava asks the verse for field consultation.')
claim('14','8b:14','He cites Jacob calling Rachel and Leah to the field by his flock.',['Rav Adda bar Ahava'])
for k,text in [('eating','Rabban Gamliel appreciates Persian modesty while eating.'),('privy','He appreciates their modesty in the privy.'),('other','He appreciates their modesty in another matter.')]:claim('15'+k,'8b:15',text,['Rabban Gamliel'],unc=['Another matter is the source euphemism; not replaced by a literal source quotation.'] if k=='other' else [])
claim('16','8b:16','Rav Yosef interprets My consecrated ones as Persians designated and prepared for Gehinnom.',['Rav Yosef'],status='Separate prophetic exposition, not explicit retraction of the prior three custom praises')
for ref,chain,surface in [('8a:21',['רבי חייא בר אמי','עולא'],'חייא בר אמי'),('8a:22',['רבי חייא בר אמי','עולא'],'חייא בר אמי'),('8a:25',['רב הונא בר יהודה','רבי מנחם','רבי אמי'],'רב הונא בר יהודה'),('8a:30',['רב הונא בר יהודה','רבי אמי'],'רב הונא בר יהודה')]:att('a'+ref.replace(':','_'),ref,surface,'transmitter',[chain[0]],'Reported teaching',chain=chain)
for k,ref,surface,name in [('26','8a:26','רבי אבהו','רבי אבהו'),('27','8a:27','רב פפא','רב פפא'),('29','8a:29','רב ששת','רב ששת'),('2b','8b:2','רב ביבי בר אביי','רב ביבי בר אביי'),('2h','8b:2','חייא בר רב מדפתי','חייא בר רב מדפתי'),('5','8b:5',"ר' יהושע בן לוי",'רבי יהושע בן לוי'),('6','8b:6','רבי יהודה','רבי יהודה'),('8','8b:8','רבא','רבא'),('10','8b:10','רב פפא','רב פפא'),('11','8b:11','רבי יהושע בן לוי','רבי יהושע בן לוי'),('12','8b:12','אביי','אביי'),('13','8b:13','ר"ע','רבי עקיבא'),('14','8b:14','רב אדא בר אהבה','רב אדא בר אהבה'),('15','8b:15','רבן גמליאל','רבן גמליאל'),('16','8b:16','רב יוסף','רב יוסף')]:att('a'+k,ref,surface,'speaker',[name],'Local teaching or narrative actor')
for k,ref,a,b,rel in [('23','8a:23','c23','c22','objection'),('24','8a:24','c24','c23','answer'),('26','8a:26','c26','c25','qualification'),('28','8a:28','c28','q27','answer'),('1i','8b:1','c1include','c30','qualification'),('3','8b:3','c3','q3','answer'),('3p','8b:3','c3','c2plan','objection'),('4','8b:4','c4rule','c4plan','objection'),('5','8b:5','c5','c4rule','support'),('8d','8b:8','c8danger','c8rule','support'),('8m','8b:8','c8meal','c8rule','support'),('9s','8b:9','c9shema','c9bed','answer'),('9c','8b:9','c9convert','c9bed','answer'),('9l','8b:9','c9literal','c9bed','answer'),('10','8b:10','c10event','c10rule','support'),('10l','8b:10','c10rule','c9literal','support'),('11','8b:11','c9passing','c11','support'),('14','8b:14','c14','q14','answer'),('14s','8b:14','c14','c13field','support')]:edge('e'+k,ref,a,b,rel)
for k in ['door','synagogue','load','run','tefillin']:edge('e12'+k,'8b:12','c12'+k,'c11','qualification')
for x in rows:
 if x['id']==pre+'c28':x['content']['assertion_mode']='unresolved'
 if x['layer']=='claims':x['content']['scope']='Local source teachings and reported conduct. Explicit unresolved question stays unresolved; alternative interpretations are not collapsed into one universal rule.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read8a21–8b23; reread core8a21–8b16 for teacher distinction, explicit teiku, nonresolution by separate Rav Sheshet conduct, portion timing and reward, ninth-day eating, involuntary forgetting, two/three alternative explanations, all Abaye exceptions and separate custom evaluations. Core ends before new Shema discussion8b17. Completed '+layer+' pass; no additional record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch09_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch09_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch09_receipt.json',r.encoded(out));print(r.encoded(out).decode())
