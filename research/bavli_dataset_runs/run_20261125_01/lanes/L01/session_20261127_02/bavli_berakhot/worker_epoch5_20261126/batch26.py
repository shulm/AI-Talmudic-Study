from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.emet_tzitzit.20261127e5.'
assert r.sha(r.encoded(state))=='fb119fee2d3ecc7b56e036b69c74c5466372cc922563cd062e5e6043f88dc342'
refs=['14a:20','14a:21']+['14b:'+str(i) for i in range(1,16)]
for k,rr,title in [('truth',refs[:5],'No interruption before Emet and repeating Emet'),('night',refs[5:12],'Western evening passage and when beginning requires completion'),('order',refs[12:],'Paragraph order: study, teaching and practice')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Mishnah lemma','Rabbi Abbahu reporting Rabbi Yohanan','Continuation proof citation','Anonymous question','Rabbi Abbahu/Rabbi Yohanan, Rabbah and narrative','Rav Yosef praising Rav Shmuel bar Yehuda’s western report','Abaye’s objection citing two Rav traditions','Rav Pappa’s explanation','Abaye’s practical inference','Hiyya son of Rav','Anonymous challenge','Anonymous alternative thanksgiving wording','Mishnah lemma','Rabbi Shimon ben Yohai baraita','Anonymous objection','Anonymous corrected formulation','Anonymous harmonization with Rabbi Yehoshua ben Korha']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Ruling, reported custom or corrected argument',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('21law','14a:21','Rabbi Yohanan through Rabbi Abbahu rules like Rabbi Yehuda: no interruption between eloheikhem and Emet ve-Yatziv.',['Rabbi Yohanan'])
q('q21','14a:21','What is Rabbi Yehuda’s reason?')
claim('1','14b:1','The proof is Jeremiah’s the Lord God is truth.',['Rabbi Yohanan through Rabbi Abbahu'],status='Citation completing14a21 explanation')
q('q2','14b:2','Does one repeat Emet or not?')
claim('3y','14b:3','Rabbi Yohanan through Rabbi Abbahu says to repeat Emet.',['Rabbi Yohanan'])
claim('3r','14b:3','Rabbah says not to repeat Emet.',['Rabbah'])
claim('3story','14b:3','Hearing a reader before him say Emet twice, Rabbah comments that every Emet has seized this person.',['Rabbah'],status='Narrated expression consistent with his no-repeat ruling',unc=['Figurative כל אמת אמת תפסיה wording preserved without inventing a medical claim.'])
claim('4','14b:4','Rav Shmuel bar Yehuda reports western evening recitation as Speak to the children of Israel and say to them, I am the Lord your God, truth; Rav Yosef praises this teaching.',['Western practitioners reported by Rav Shmuel bar Yehuda'],status='Regional evening practice report, not universal consensus')
q('q5','14b:5','Abaye challenges the praised report using Rav’s requirement to complete once begun and Rav’s treating and say to them as a beginning.')
claim('5kahana','14b:5','Rav via Rav Kahana says not to begin, but if begun to finish.',['Rav'],cond=['Evening tzitzit passage in context','If begun'],status='Transmitted rule cited as objection')
claim('5yitzhak','14b:5','Rav via Rav Shmuel bar Yitzhak says Speak to the children of Israel is not a beginning, while and say to them is a beginning.',['Rav'],status='Explicit threshold in Rav’s report')
claim('6','14b:6','Rav Pappa explains that in the west even and say to them is not a beginning until they shall make themselves tzitzit.',['Rav Pappa explaining western view'])
claim('7','14b:7','Abaye concludes that we begin because they begin in the west, and once begun we finish in accordance with Rav’s rule.',['Abaye'],cond=['Our evening recitation practice'],status='Local practical inference combining beginning custom and completion rule')
claim('8yes','14b:8','Hiyya son of Rav requires Emet if one said I am the Lord your God.',['Hiyya son of Rav'],cond=['Said I am the Lord your God'])
claim('8no','14b:8','If that phrase was not said, Hiyya son of Rav does not require Emet.',['Hiyya son of Rav'],cond=['Did not say I am the Lord your God'])
q('q9','14b:9','But Exodus still needs to be mentioned?')
claim('10','14b:10','The answer provides thanksgiving for bringing us from Egypt, redeeming us from slavery, performing wonders at sea and our song, as an alternative Exodus mention.',['Anonymous Gemara'],status='Alternative wording resolving remembrance requirement')
claim('12','14b:12','Rabbi Shimon ben Yohai’s initial order rationale contrasts Shema with Ve-haya im shamoa as learning versus teaching, then Ve-haya im shamoa with Vayomer as learning versus doing.',['Rabbi Shimon ben Yohai'],status='Printed compressed formulation corrected next',unc=['The second contrast literally prints ללמוד, though the objection13 treats it as ללמד; preserve both rather than silently normalize.'])
q('q13','14b:13','Does Shema not also contain teaching and doing, and Ve-haya im shamoa also doing, as their verses show?')
claim('14','14b:14','The corrected rationale is Shema contains learning, teaching and doing; Ve-haya im shamoa teaching and doing; Vayomer doing alone.',['Rabbi Shimon ben Yohai'],status='Gemara’s corrected formulation')
q('q15','14b:15','Why is Rabbi Yehoshua ben Korha’s reason not sufficient?')
claim('15','14b:15','The explanation offers one reason and another: first accept Heaven’s kingdom then commandments, and additionally these other learning, teaching and doing features.',['Anonymous Gemara'],status='Complementary reasons, not contradiction between sages')
for k,ref,surface,name in [('3r','14b:3','רבה','רבה'),('4y','14b:4','רב יוסף','רב יוסף'),('5','14b:5','אביי','אביי'),('6','14b:6','רב פפא','רב פפא'),('7','14b:7','אביי','אביי'),('8','14b:8','חייא בר רב','חייא בר רב'),('12','14b:12','ר"ש בן יוחי','רבי שמעון בן יוחי')]:att('a'+k,ref,surface,'speaker',[name],'Local named teaching or objection')
for k,ref,surface,chain in [('21','14a:21','ר אבהו',['רבי אבהו','רבי יוחנן']),('3','14b:3','ר אבהו',['רבי אבהו','רבי יוחנן']),('4','14b:4','רב שמואל בר יהודה',['רב שמואל בר יהודה','אמרי במערבא']),('5k','14b:5','רב כהנא',['רב כהנא','רב']),('5s','14b:5','רב שמואל בר יצחק',['רב שמואל בר יצחק','רב']),('7chain','14b:7','רב כהנא',['רב כהנא','רב'])]:att('a'+k,ref,surface,'transmitter',[chain[0]],'Explicit transmission distinct from current discussant',chain=chain)
for k,ref,a,b,rel in [('1','14b:1','c1','q21','answer'),('1s','14b:1','c1','c21law','support'),('3y','14b:3','c3y','q2','answer'),('3r','14b:3','c3r','q2','answer'),('3d','14b:3','c3r','c3y','distinction'),('3s','14b:3','c3story','c3r','support'),('5','14b:5','q5','c4','objection'),('5k','14b:5','c5kahana','q5','support'),('5s','14b:5','c5yitzhak','q5','support'),('6','14b:6','c6','q5','answer'),('6d','14b:6','c6','c5yitzhak','distinction'),('7','14b:7','c5kahana','c7','support'),('9','14b:9','q9','c8no','objection'),('10','14b:10','c10','q9','answer'),('13','14b:13','q13','c12','objection'),('14a','14b:14','c14','q13','answer'),('14c','14b:14','c14','c12','correction'),('15','14b:15','c15','q15','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local Emet, evening passage and paragraph-order discussion. Distinguish regional report, Rav’s threshold, Abaye’s inference and corrected baraita wording; no unsupported consensus.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read14a20–15a26; reread core14a20–14b15 for cross-page truth proof, Emet repeat dispute and narrative, regional opening threshold versus two Rav transmissions, Abaye’s combined practice, alternative Exodus wording and corrected learning/teaching/doing rationale with complementary order reasons. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch26_proposal.json',r.encoded(p));print('STAGED',r.sha(r.encoded(p)),len(rows))
