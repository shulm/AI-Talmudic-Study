from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.mourning_honor.20261127e5.'
assert r.sha(r.encoded(state))=='cf15b06626e8b06a442d290f5565b9a43c4d3583166896fa8d2e767793dc2b59'
refs=['16b:'+str(i) for i in range(5,18)]
for k,rr,title in [('m',refs[:3],'Mishnah: exceptional mourning and voluntary bridegroom Shema'),('bath',refs[3:4],'Delicate mourner and nighttime rabbinic restriction'),('servants',refs[4:8],'Mourning and eulogy for servants'),('titles',refs[8:12],'Ancestor and servant honorifics'),('prayer',refs[12:],'Shema and prayer in Psalm63')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rabban Gamliel narrative and student objection','Rabban Gamliel narrative and student objection','Anonymous Mishnah and Rabban Shimon ben Gamliel','Anonymous explanation with variant name wording','Mishnah lemma','Baraita','Rabbi Eliezer narrative and teaching','Baraita, Rabbi Yose and unnamed opponents','Baraita','Anonymous question and explanation','Baraita and Rabban Gamliel household exception','Anonymous objection and explanation','Rabbi Eleazar exposition']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Scoped rule, exception, narrative or exposition',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
q('q5','16b:5','Students ask why he bathed the first night after his wife’s death despite teaching that a mourner may not bathe.')
claim('5','16b:5','Rabban Gamliel answers that he is unusually delicate, unlike other people.',['Rabban Gamliel'],status='Personal exception explaining conduct, not repeal of mourner bathing restriction',unc=['Name supplied by continuous Mishnah narrative from16a8, not explicitly repeated in this segment.'])
q('q6','16b:6','Students ask why he accepted consolation for his servant Tavi despite teaching not to accept consolation for servants.')
claim('6','16b:6','Rabban Gamliel says Tavi differs from other servants because he was worthy.',['Rabban Gamliel'],status='Individual exception')
claim('7first','16b:7','The first tanna allows a bridegroom to recite Shema on the first night if he wishes.',['Anonymous Mishnah first tanna'],cond=['Bridegroom wishes to recite on first night'],unc=['Continuation17b9 offers Rabbi Yohanan’s reversal of the positions and Rav Shisha’s no-reversal reconciliation; retain this as printed Mishnah assignment rather than exclusive final attribution.'])
claim('7rsg','16b:7','Rabban Shimon ben Gamliel says not everyone who wishes to take the reputation may do so.',['Rabban Shimon ben Gamliel'],status='Printed restrictive response to voluntary recitation',unc=['Read17b7–10: Rabbi Yohanan proposes reversing the positions, while Rav Shisha preserves them with contextual distinctions.'])
q('q8','16b:8','What grounds Rabban Gamliel’s bathing exception?')
claim('8','16b:8','He treats nighttime acute mourning as rabbinic, deriving day from a bitter day, and the sages did not decree for an unusually delicate person.',['Anonymous Gemara explaining Rabban Gamliel'],cond=['Nighttime mourning','Unusually delicate'],unc=['Pinned Gemara name reads רבן (שמעון בן) גמליאל with parenthetical expansion. Preserve variant rather than silently resolving to the adjacent groom speaker.'])
claim('10','16b:10','The baraita disallows a consolation row, mourners’ blessing and mourners’ consolation for male and female servants.',['Anonymous baraita'])
claim('11story','16b:11','After Rabbi Eliezer’s maidservant died, students followed him through rooms to console him; he rebuked their failure to infer his refusal and repeated the mourning restriction.',['Rabbi Eliezer'],status='Narrative application of rule')
claim('11formula','16b:11','For a servant’s death one instead says may the Omnipresent replenish your loss, the formula said for loss of an ox or donkey.',['Rabbi Eliezer'],status='Reported ancient consolation distinction; source statement only')
claim('12first','16b:12','Another baraita forbids eulogizing male or female servants.',['Anonymous baraita'])
claim('12yose','16b:12','Rabbi Yose permits saying of a worthy servant: alas, a good and faithful man who benefited from his own labor.',['Rabbi Yose'],cond=['Worthy servant'])
q('q12','16b:12','Opponents ask Rabbi Yose what this leaves for the worthy.')
claim('13','16b:13','The baraita reserves fathers for three and mothers for four.',['Anonymous baraita'],status='Restricted collective ancestor honorifics')
q('q14','16b:14','Is the fathers restriction because tribal descent is unknown, and if so why allow mothers when Rachel/Leah descent is also unknown?')
claim('14','16b:14','The explanation rejects descent uncertainty and instead restricts these titles to those of the requisite importance.',['Anonymous Gemara'])
claim('15rule','16b:15','Another baraita says servants are not called Father so-and-so or Mother so-and-so.',['Anonymous baraita'])
claim('15house','16b:15','Those of Rabban Gamliel’s household were called those honorifics.',['Anonymous narrator'],status='Reported exception')
q('q16','16b:16','Does the narrative contradict the stated rule?')
claim('16','16b:16','Their importance explains the exception.',['Anonymous Gemara'])
claim('17shema','16b:17','Rabbi Eleazar reads thus I bless You in my life as Shema and in Your name I lift my hands as prayer.',['Rabbi Eleazar'])
claim('17reward','16b:17','One who does so is described as satisfied with fat and richness and inherits this world and the world to come, using the Psalm’s plural expressions of praise.',['Rabbi Eleazar'],status='Attributed exegetical reward teaching')
for k,ref,surface,name in [('7','16b:7','רבן שמעון בן גמליאל','רבן שמעון בן גמליאל'),('11','16b:11','רבי אליעזר','רבי אליעזר'),('12','16b:12',"ר' יוסי",'רבי יוסי'),('15','16b:15','ר"ג','רבן גמליאל'),('17','16b:17','ר אלעזר','רבי אלעזר')]:att('a'+k,ref,surface,'speaker',[name],'Printed attribution or narrated household')
att('a8','16b:8','רבן (שמעון בן) גמליאל','speaker',['רבן גמליאל','רבן שמעון בן גמליאל'],'Bathing explanation name variant',unc=['Parenthetical expansion preserved; immediate narrative concerns Rabban Gamliel.'])
for k,ref,a,b,rel in [('5','16b:5','c5','q5','answer'),('6','16b:6','c6','q6','answer'),('7','16b:7','c7rsg','c7first','distinction'),('8','16b:8','c8','q8','answer'),('8s','16b:8','c8','c5','support'),('11','16b:11','c11story','c10','support'),('11f','16b:11','c11formula','c10','qualification'),('12','16b:12','c12yose','c12first','qualification'),('12q','16b:12','q12','c12yose','objection'),('14','16b:14','c14','q14','answer'),('16','16b:16','c16','q16','answer'),('16q','16b:16','c16','c15house','support'),('17','16b:17','c17reward','c17shema','qualification')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local mourning and honorific distinctions and Psalm exposition. Preserve individual exceptions, textual name variant and later alternative treatment of the groom’s voluntary recitation.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read16b5–17b17 including17b7–10 reversal versus contextual preservation; reread core16b5–17 for all mourning exceptions, parenthetical name variant, three consolation restrictions and replacement formula, worthy-servant eulogy objection, rejected descent explanation and important-household exception. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch32_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch32_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch32_receipt.json',r.encoded(out));print(r.encoded(out).decode())
