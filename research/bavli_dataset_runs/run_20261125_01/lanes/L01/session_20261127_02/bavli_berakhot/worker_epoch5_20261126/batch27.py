from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.tefillin_sequence.20261127e5.'
assert r.sha(r.encoded(state))=='b8a833ebc8fcd8ec6bf406f2a88a7dc09e54557d73fe3506c446b060fb0c9077'
refs=['14b:'+str(i) for i in range(16,26)]+['15a:'+str(i) for i in range(1,6)]
for k,rr,title in [('rav',refs[:8],'Rav’s sequence and the messenger exception'),('full',refs[8:12],'Tefillin and full acceptance of Heaven’s kingdom'),('clean',refs[12:],'Hand cleansing alternatives and limits of searching for water')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rav narrative and baraita objection','Anonymous internal contradiction','Anonymous one/two distinction','Anonymous proposed Rav rationale','Anonymous scope objection','Rav Hiyya bar Ashi testimony and hypothetical defense','Anonymous alternative purpose of testimony','Anonymous final messenger explanation','Ulla and Rabbi Hiyya bar Abba/Rabbi Yohanan','Rabbi Yohanan begins teaching','Rabbi Yohanan continuation','Rabbi Hiyya bar Abba/Rabbi Yohanan and Rava','Ravina addresses Rava with western scholar report','Rava response and Rav Hisda precedent','Anonymous scope and distance qualification']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Narrated practice, challenge or scoped rule',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('16rav','14b:16','Rav washed his hands, recited Shema, put on tefillin and prayed.',['Anonymous narrator'],status='Individual occurrence; final explanation is messenger failure, not a general sequence ruling')
claim('16exempt','14b:16','The baraita exempts one digging a burial niche for the dead from Shema, prayer, tefillin and all Torah commandments.',['Anonymous baraita'],cond=['Engaged in digging burial niche for dead'],unc=['The continuation distinguishes one worker from two.'])
claim('16order','14b:16','The same baraita says when Shema time arrives one comes up, washes, puts on tefillin, recites Shema and prays.',['Anonymous baraita'],cond=['Shema time arrives'],unc=['The continuation places this clause with two workers.'])
q('q16','14b:16','How could Rav recite Shema before putting on tefillin, against the baraita sequence?')
q('q17','14b:17','The baraita itself first exempts and then obligates; how can both hold?')
claim('18','14b:18','The final clause concerns two workers, while the first concerns one.',['Anonymous Gemara'],status='Resolution of internal baraita contradiction')
claim('19','14b:19','A proposed explanation makes Rav follow Rabbi Yehoshua ben Korha: Heaven’s kingdom first, then commandments.',['Anonymous Gemara'],status='Proposed rationale rejected by following challenges')
q('q20','14b:20','Rabbi Yehoshua ben Korha orders one reading before another; did he ever put reading before action?')
q('q21','14b:21','Does Rav actually follow that proposed sequence, given Rav Hiyya bar Ashi’s contrary repeated observation?')
claim('21practice','14b:21','Rav Hiyya bar Ashi reports repeatedly seeing Rav wash, bless, teach the chapter, put on tefillin, then recite Shema.',['Rav Hiyya bar Ashi'],status='Repeated observation distinct from isolated14b16 occurrence')
claim('21early','14b:21','The discussion considers that the observed sequence might have occurred before Shema time.',['Anonymous Gemara'],status='Hypothetical defense, not established timing')
q('q21purpose','14b:21','If before Shema time, what does Rav Hiyya bar Ashi’s testimony teach?')
claim('22','14b:22','It teaches against the view that Mishnah needs no blessing: a blessing is required for Mishnah too.',['Anonymous Gemara'],status='Alternative instructional purpose of reported practice')
claim('23','14b:23','The remaining difficulty about Rav’s unusual order is answered that the messenger was at fault.',['Anonymous Gemara'],status='Final local explanation',unc=['Brief שלוחא הוא דעוית supplies messenger failure; exact operational details or motives are not stated.'])
claim('24ulla','14b:24','Ulla likens reciting Shema without tefillin to bearing false testimony concerning oneself.',['Ulla'],cond=['Recites Shema without tefillin'])
claim('24yoh','14b:24','Rabbi Yohanan through Rabbi Hiyya bar Abba likens it to offering an olah without meal offering and a sacrifice without libations.',['Rabbi Yohanan'],cond=['Recites Shema without tefillin'],status='Alternative analogy, not explicit disagreement over validity')
claim('1','15a:1','Rabbi Yohanan’s complete acceptance of Heaven’s kingdom consists of relieving oneself, washing hands, putting on tefillin, reciting Shema and praying.',['Rabbi Yohanan'],status='Completes introduction14b25')
claim('2altar','15a:2','Rabbi Yohanan through Rabbi Hiyya bar Abba says this sequence is credited as building an altar and offering a sacrifice, citing washing in cleanliness and surrounding God’s altar.',['Rabbi Yohanan'],cond=['Relieves oneself, washes, wears tefillin, recites Shema and prays'])
q('q2','15a:2','Rava asks whether the verse also suggests immersion, because it says erhatẓ rather than arhiẓ.')
claim('2immersion','15a:2','Rava proposes that the cleansing is reckoned like immersion from the verse’s wording.',['Rava'],status='Additional interpretive comparison; not an actual immersion requirement')
claim('3','15a:3','Ravina reports to Rava an unnamed western scholar’s teaching: without water to wash, one cleans hands with earth, a stone or a chip.',['Unnamed western scholar'],cond=['No water for handwashing'])
claim('4rava','15a:4','Rava approves: the verse says cleanliness, not water, so anything that cleans suffices.',['Rava'])
claim('4hisda','15a:4','Rav Hisda cursed one who searches for water at prayer time.',['Rav Hisda'],unc=['The next segment qualifies the scope to Shema and separately requires searching for prayer. Do not omit this tension.'])
claim('5scope','15a:5','The foregoing no-search statement applies to Shema; for prayer one searches.',['Anonymous Gemara'],status='Explicit qualification')
q('q5','15a:5','How far does one search?')
claim('5forward','15a:5','For prayer one goes forward up to a parasang.',['Anonymous Gemara'],cond=['Searching forward'])
claim('5back','15a:5','Behind oneself one does not return even a mil; the inference is that less than a mil one does return.',['Anonymous Gemara'],cond=['Searching behind oneself'],status='Distance distinction and explicit inference; less than one mil versus one mil')
for k,ref,surface,name in [('16','14b:16','רב','רב'),('21','14b:21','רב חייא בר אשי','רב חייא בר אשי'),('24u','14b:24','עולא','עולא'),('25','14b:25','רבי יוחנן','רבי יוחנן'),('2r','15a:2','רבא','רבא'),('3r','15a:3','רבינא','רבינא'),('3to','15a:3','רבא','רבא'),('4','15a:4','רב חסדא','רב חסדא')]:att('a'+k,ref,surface,'speaker',[name],'Named utterance, addressed respondent or narrated practice')
for k,ref,surface,chain in [('24','14b:24','ר חייא בר אבא',['רבי חייא בר אבא','רבי יוחנן']),('2','15a:2','ר חייא בר אבא',['רבי חייא בר אבא','רבי יוחנן'])]:att('a'+k,ref,surface,'transmitter',[chain[0]],'Explicit transmission',chain=chain)
for k,ref,a,b,rel in [('16','14b:16','q16','c16rav','objection'),('16s','14b:16','c16order','q16','support'),('17','14b:17','q17','c16exempt','objection'),('18','14b:18','c18','q17','answer'),('18q','14b:18','c18','c16order','qualification'),('19','14b:19','c19','q16','answer'),('20','14b:20','q20','c19','objection'),('21','14b:21','q21','c19','objection'),('21s','14b:21','c21practice','q21','support'),('21e','14b:21','c21early','q21','answer'),('22','14b:22','c22','q21purpose','answer'),('23','14b:23','c23','q16','answer'),('24','14b:24','c24yoh','c24ulla','distinction'),('2','15a:2','c2immersion','q2','answer'),('2q','15a:2','c2immersion','c2altar','qualification'),('4','15a:4','c4rava','c3','support'),('5','15a:5','c5scope','c4hisda','qualification'),('5f','15a:5','c5forward','q5','answer'),('5b','15a:5','c5back','q5','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['id'] in [pre+'e19',pre+'e21e']:x['uncertainty'].append('Provisional dialectical explanation, not final disposition; preserve subsequent objections and messenger resolution.')
 if x['layer']=='claims':x['content']['scope']='Local sequence, tefillin and cleansing arguments. Separate isolated narrative from repeated practice and final explanation; distinguish metaphors from validity rulings and hand-cleansing from immersion obligation.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read14b16–15a26; reread core14b16–15a5 for one/two burial workers, rejected kingdom-order rationale, Rav Hiyya testimony and hypothetical timing, messenger resolution, two tefillin analogies, full sequence, metaphorical immersion and forward/backward water-search distinctions. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch27_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch27_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch27_receipt.json',r.encoded(out));print(r.encoded(out).decode())
