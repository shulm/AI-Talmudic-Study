from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.remembrance.20261127e5.'
assert r.sha(r.encoded(state))=='89ee1340d3057f6871c2de616df572cf0fc37155ed1057eea516fdac6b66d897'
refs=['12b:'+str(i) for i in range(14,29)]+['13a:'+str(i) for i in range(1,16)]
for k,rr,title in [('balak',refs[:5],'Unadopted Balak passage and public burden'),('tzitzit',refs[5:9],'Reasons for inclusion of tzitzit passage'),('exodus',refs[9:18],'Night and messianic remembrance; primary and secondary redemption'),('names',refs[18:29],'Abram, Sarai and Jacob naming distinctions'),('close',refs[29:],'Chapter closing formula')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rabbi Abbahu ben Zutarti reporting Rav Yehuda bar Zevida','Anonymous question and rejected explanation','Rabbi Yose bar Avin','Anonymous challenge','Anonymous received rule','Anonymous question','Rabbi Yehuda bar Haviva','Anonymous explanation and question','Baraita','Mishnah and Rabbi Eleazar ben Azariah','Ben Zoma interpretation','Sages interpretation','Ben Zoma to sages','Sages reply','Analogy citation','Analogy explanation and Isaiah interpretation','Rav Yosef baraita','Anonymous parable','Chronicles citation','Anonymous interpretation','Citation about Sarai','Anonymous interpretation','Bar Kappara and Rabbi Eliezer','Anonymous objection','Anonymous answer','Anonymous objection','Anonymous answer','Rabbi Yose bar Avin or Rabbi Yose bar Zevida','Unidentified respondent','Chapter closing formula']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Rule, argument, parable or editorial closure',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('14','12b:14','Rav Yehuda bar Zevida via Rabbi Abbahu ben Zutarti reports that they sought to establish the Balak passage in Shema but did not because of public burden.',['Rav Yehuda bar Zevida'],status='Reported unadopted proposal and reason')
q('q14','12b:14','Why was the Balak passage not instituted?')
q('q15','12b:15','What motivates Balak: if Exodus mention, why not the interest or weights passages that also mention it?')
claim('15','12b:15','Exodus mention alone does not explain selecting Balak, since interest and weights passages also contain it.',['Anonymous Gemara'],status='Rejected proposed explanation')
claim('16','12b:16','Rabbi Yose bar Avin instead grounds the proposal in the verse he crouched and lay like a lion and lioness, who shall raise him.',['Rabbi Yose bar Avin'])
q('q17','12b:17','Why not recite only that verse?')
claim('18','12b:18','The received rule permits dividing a passage where Moses divided it and forbids division where he did not.',['Anonymous received tradition'],cond=['Passage division corresponds to Mosaic division'])
q('q19','12b:19','Why was the tzitzit passage established?')
claim('20','12b:20','Rabbi Yehuda bar Haviva explains its inclusion by tzitzit, Exodus, yoke of commandments, sectarian belief, sinful thought and idolatrous thought.',['Rabbi Yehuda bar Haviva'],unc=['Pinned text says חמשה דברים but the printed enumeration has six named items. Preserve mismatch; do not emend or merge categories without evidence.'])
claim('21','12b:21','The discussion identifies direct wording for tzitzit, Exodus and the yoke of commandments.',['Anonymous Gemara'])
q('q21','12b:21','Where are sectarian belief, sinful thought and idolatrous thought found?')
claim('22heart','12b:22','The baraita reads after your hearts as sectarian belief, citing the fool saying in his heart there is no God.',['Anonymous baraita'])
claim('22eyes','12b:22','It reads after your eyes as sinful thought, citing Samson’s she is right in my eyes.',['Anonymous baraita'])
claim('22stray','12b:22','It reads you stray as idolatrous thought, citing straying after the Baalim.',['Anonymous baraita'])
claim('23rule','12b:23','The Mishnah states that Exodus is mentioned at night.',['Anonymous Mishnah'])
claim('23age','12b:23','Rabbi Eleazar ben Azariah says he is like seventy years old and had not achieved the saying of Exodus at night until Ben Zoma expounded it.',['Rabbi Eleazar ben Azariah'],unc=['Preserve כבן and ולא זכיתי; no literal age or biographical explanation supplied here.'])
claim('24','12b:24','Ben Zoma reads days of your life as days and all days of your life as including nights.',['Ben Zoma'])
claim('25','12b:25','The sages read days of your life as this world and all as including the messianic days.',['Sages'],status='Alternative interpretation; source here does not expressly give sages a separate night ruling')
q('q26','12b:26','Ben Zoma challenges whether Exodus is mentioned in messianic days, since Jeremiah describes replacing the Exodus oath with the ingathering oath.')
claim('26','12b:26','Ben Zoma cites Jeremiah’s future oath to challenge messianic Exodus remembrance.',['Ben Zoma'],status='Objection to sages')
claim('27','12b:27','The sages answer that Exodus is not uprooted; redemption from subjugation to kingdoms becomes primary and Exodus secondary.',['Sages'])
claim('28','12b:28','The Jacob-to-Israel renaming verse is introduced as a parallel to primary and secondary status.',['Anonymous Gemara'],status='Analogy completed at13a1')
claim('1names','13a:1','Jacob is not uprooted: Israel is primary and Jacob secondary.',['Anonymous Gemara'])
claim('1old','13a:1','Do not remember former things is interpreted as subjugation to kingdoms, and do not consider ancient things as Exodus.',['Anonymous Gemara'])
claim('2','13a:2','Rav Yosef teaches that the new thing in Isaiah is the war of Gog and Magog.',['Rav Yosef'])
claim('3','13a:3','A parable successively replaces recollection of rescue from wolf, lion and snake; later troubles make Israel forget earlier ones.',['Anonymous Gemara'],status='Illustrative parable; not a new legal abolition of Exodus remembrance')
claim('5','13a:5','Abram becoming Abraham is read as first father to Aram and finally father to the whole world.',['Anonymous Gemara'])
claim('7','13a:7','Sarai becoming Sarah is read as first ruler to her nation and finally to the whole world.',['Anonymous Gemara'])
claim('8kap','13a:8','Bar Kappara teaches that calling Abraham Abram violates a positive command, your name shall be Abraham.',['Bar Kappara'],cond=['Calling Abraham Abram'])
claim('8eliezer','13a:8','Rabbi Eliezer says it violates a prohibition, your name shall no longer be called Abram.',['Rabbi Eliezer'],cond=['Calling Abraham Abram'],unc=['The text contrasts legal formulations; it does not explicitly say whether Rabbi Eliezer excludes the positive-command characterization.'])
q('q9','13a:9','Should calling Sarah Sarai similarly violate a command?')
claim('10','13a:10','The answer limits the Sarai instruction to God’s address to Abraham: you shall not call her Sarai.',['Anonymous Gemara'])
q('q11','13a:11','Should calling Jacob Jacob similarly violate a command?')
claim('12','13a:12','Jacob differs because Scripture returned to the name in God’s Jacob, Jacob at night.',['Anonymous Gemara'])
q('q13','13a:13','Rabbi Yose bar Avin, alternatively Rabbi Yose bar Zevida, objects from Nehemiah’s God who chose Abram.')
claim('14answer','13a:14','The respondent says the prophet is recounting God’s praise by describing what occurred originally.',['Unidentified respondent'],status='Reply permitting historical recounting in this proof context',unc=['אמר ליה has no named respondent here; do not assign by proximity.'])
att('a14','12b:14',"ר' אבהו בן זוטרתי",'transmitter',["רבי אבהו בן זוטרתי"],'Balak institution report',chain=['רבי אבהו בן זוטרתי','רב יהודה בר זבידא'])
for k,ref,surface,name in [('16','12b:16',"ר' יוסי בר אבין",'רבי יוסי בר אבין'),('20','12b:20','ר יהודה בר חביבא','רבי יהודה בר חביבא'),('23','12b:23','ר אלעזר בן עזריה','רבי אלעזר בן עזריה'),('23b','12b:23','בן זומא','בן זומא'),('25','12b:25','חכ"א','חכמים'),('26','12b:26','בן זומא','בן זומא'),('2','13a:2','רב יוסף','רב יוסף'),('8b','13a:8','בר קפרא','בר קפרא'),('8e','13a:8','רבי אליעזר','רבי אליעזר')]:att('a'+k,ref,surface,'speaker',[name],'Local named teaching or interpretation')
att('a13','13a:13','רבי יוסי בר אבין ואיתימא רבי יוסי בר זבידא','speaker',['רבי יוסי בר אבין','רבי יוסי בר זבידא'],'Alternative objection attribution',unc=['Two reported versions, not joint speakers and not a resolved identity.'])
for k,ref,a,b,rel in [('14','12b:14','c14','q14','answer'),('16','12b:16','c16','q15','answer'),('16r','12b:16','c16','c15','correction'),('18','12b:18','c18','q17','answer'),('20','12b:20','c20','q19','answer'),('21','12b:21','c21','c20','support'),('22h','12b:22','c22heart','q21','answer'),('22e','12b:22','c22eyes','q21','answer'),('22s','12b:22','c22stray','q21','answer'),('24','12b:24','c24','c23rule','support'),('25','12b:25','c25','c24','distinction'),('26','12b:26','c26','c25','objection'),('27','12b:27','c27','q26','answer'),('28','12b:28','c28','c27','support'),('1','13a:1','c1names','c28','support'),('2','13a:2','c2','c1old','qualification'),('3','13a:3','c3','c1old','support'),('8','13a:8','c8eliezer','c8kap','distinction'),('9','13a:9','q9','c8kap','objection'),('10','13a:10','c10','q9','answer'),('11','13a:11','q11','c8kap','objection'),('12','13a:12','c12','q11','answer'),('13','13a:13','q13','c8kap','objection'),('14a','13a:14','c14answer','q13','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local passage-inclusion arguments, Exodus remembrance and naming exposition. Preserve alternatives, rhetorical objections and contextual distinctions; no modern practical ruling.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read12b14–13a35; reread core12b14–13a15 for rejected Balak rationale, indivisible passage rule, five/six wording mismatch, all tzitzit categories, night and messianic interpretations, primary/secondary names, later-trouble parable, positive/negative naming formulations, both attribution versions and all three objections with replies. Chapter closure is editorial, with no invented semantic claim. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch22_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch22_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch22_receipt.json',r.encoded(out));print(r.encoded(out).decode())
