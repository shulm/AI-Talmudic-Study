from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.audibility_terumah.20261127e5.'
assert r.sha(r.encoded(state))=='880efa48e18d04fb6528a5aee07688a0735d27f5b462bc7b543368b879892451'
refs=['15a:'+str(i) for i in range(6,24)]
for k,rr,title in [('m',refs[:3],'Mishnah: audibility, articulation, order and error'),('reason',refs[3:5],'Derivations of audibility and language'),('terumah',refs[5:],'Terumah and silent blessing: alternative tannaitic assignments')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Anonymous Mishnah and Rabbi Yose','Rabbi Yose and Rabbi Yehuda','Anonymous Mishnah','Explanations of Rabbi Yose and first tanna','Rabbi Yose derivation','Terumot Mishnah citation','Anonymous attribution question','Rav Hisda assignment with cited Shema Mishnah','Anonymous explanation of Rav Hisda','Anonymous alternative attribution and grammatical proof','Anonymous rebuttal of grammatical proof','Challenge from blessing after meals begins','Challenge completed','Alternative proposal','Challenge from Rabbi Yehuda son of Rabbi Shimon ben Pazi','Challenge completed','First reconciliation: Rabbi Yehuda versus his teacher','Second reconciliation: Rabbi Yehuda follows teacher versus Rabbi Meir']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Rule or conditional dialectical assignment',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('6first','15a:6','The first tanna validates Shema read without making it audible to one’s ear.',['Anonymous first tanna'],cond=['Read Shema without hearing own recitation'],status='Retrospective validity; cited as Rabbi Yehuda in15a13')
claim('6yose','15a:6','Rabbi Yose says that reading does not fulfill the obligation.',['Rabbi Yose'],cond=['Read Shema without hearing own recitation'])
claim('7yose','15a:7','Rabbi Yose validates reading without precise articulation of letters.',['Rabbi Yose'],cond=['Did not articulate letters precisely'])
claim('7yehuda','15a:7','Rabbi Yehuda invalidates reading without precise articulation.',['Rabbi Yehuda'],cond=['Did not articulate letters precisely'])
claim('8reverse','15a:8','Reading in reverse order does not fulfill the obligation.',['Anonymous Mishnah'])
claim('8error','15a:8','One who read and erred returns to the place of error.',['Anonymous Mishnah'],cond=['Error while reading'])
q('q9','15a:9','What grounds Rabbi Yose’s audibility ruling?')
claim('9yose','15a:9','Rabbi Yose reads shema as making one’s ears hear what one’s mouth says.',['Rabbi Yose'])
claim('9first','15a:9','The first tanna reads shema as permitting any language one understands.',['Anonymous first tanna'])
claim('10','15a:10','Rabbi Yose derives both audibility and language from shema.',['Rabbi Yose'],status='Both derivations, not rejection of language permission')
claim('11','15a:11','The cited Mishnah says a deaf person who can speak but cannot hear should not separate terumah, but if done the terumah is effective.',['Anonymous Terumot Mishnah'],cond=['Can speak','Cannot hear'],status='Initial prohibition with retrospective validity')
q('q12','15a:12','Which tanna distinguishes initial prohibition from retrospective validity for this deaf person?')
claim('13','15a:13','Rav Hisda assigns this to Rabbi Yose, citing the Shema dispute with Rabbi Yehuda as the permitting first tanna.',['Rav Hisda'],status='Initial attribution proposal subsequently debated')
claim('14','15a:14','The explanation limits Rabbi Yose’s invalidity to biblical Shema; terumah’s issue is its rabbinic blessing and the terumah act does not depend on that blessing.',['Anonymous Gemara'],status='Rationale supporting Rav Hisda’s assignment')
q('q15','15a:15','Why Rabbi Yose rather than Rabbi Yehuda, who might validate Shema only retrospectively, as the wording one who reads suggests?')
claim('15','15a:15','The alternative tentatively reads Rabbi Yehuda as permitting only after the fact, using the Mishnah’s retrospective wording.',['Anonymous Gemara'],status='Proposed attribution alternative')
claim('16','15a:16','The reply says one who reads highlights Rabbi Yose’s strength in invalidating even after the fact; Rabbi Yehuda could permit initially too.',['Anonymous Gemara'],status='Rebuttal to grammatical proof, not final sole interpretation')
claim('17','15a:17','A baraita forbids reciting grace after meals in one’s heart but validates it if done.',['Anonymous baraita'],status='Ruling spans15a17–18')
q('q18','15a:18','Under the proposed positions, who authored that baraita: Rabbi Yose would invalidate even after the fact, Rabbi Yehuda would permit initially?')
claim('19','15a:19','A new proposal instead makes Rabbi Yehuda permit only retrospectively.',['Anonymous Gemara'],status='Conditional dialectical reassignment, challenged next')
claim('20','15a:20','Rabbi Yehuda son of Rabbi Shimon ben Pazi teaches that the deaf person who speaks but cannot hear may separate terumah initially.',['Rabbi Yehuda son of Rabbi Shimon ben Pazi'],status='Transmitted baraita posing attribution problem, not necessarily his own legal position')
q('q21','15a:21','Who fits initial permission if Rabbi Yehuda permits only retrospectively and Rabbi Yose invalidates even retrospectively?')
claim('22own','15a:22','One reconciliation retains Rabbi Yehuda’s own initial permission and distinguishes his own view from his teacher’s.',['Anonymous Gemara'],status='First accepted reconciliation alternative')
claim('22teacher','15a:22','Rabbi Yehuda in Rabbi Eleazar ben Azariah’s name says the Shema reader must make it audible to the ear, citing Shema Israel.',['Rabbi Eleazar ben Azariah'],status='Teacher’s view transmitted by Rabbi Yehuda')
claim('22meir','15a:22','Rabbi Meir replies from upon your heart that matters follow the heart’s intention.',['Rabbi Meir'],status='Alternative to teacher’s audibility demand')
claim('23','15a:23','A further reconciliation allows Rabbi Yehuda to agree with his teacher, assigning the permissive and restrictive traditions to Rabbi Meir and Rabbi Yehuda respectively.',['Anonymous Gemara'],status='Alternative retained attribution scheme; no exclusive final assignment imposed')
for k,ref,surface,name in [('6','15a:6',"ר' יוסי",'רבי יוסי'),('7y','15a:7',"ר' יוסי",'רבי יוסי'),('7j','15a:7','רבי יהודה','רבי יהודה'),('13','15a:13','רב חסדא','רב חסדא'),('13j','15a:13','רבי יהודה','רבי יהודה'),('22m','15a:22','רבי מאיר','רבי מאיר')]:att('a'+k,ref,surface,'speaker',[name],'Local named rule, source assignment or reply')
att('a20','15a:20',"ר' יהודה בריה דרבי שמעון בן פזי",'transmitter',['רבי יהודה בריה דרבי שמעון בן פזי'],'Baraita recital; not automatically holder of baraita position')
att('a22','15a:22',"רבי יהודה אומר משום ר' אלעזר בן עזריה",'transmitter',['רבי יהודה'],'Teacher attribution',chain=['רבי יהודה','רבי אלעזר בן עזריה'])
for k,ref,a,b,rel in [('6','15a:6','c6yose','c6first','distinction'),('7','15a:7','c7yehuda','c7yose','distinction'),('9','15a:9','c9yose','q9','answer'),('9s','15a:9','c9yose','c6yose','support'),('10','15a:10','c10','c9yose','qualification'),('13','15a:13','c13','q12','answer'),('14','15a:14','c14','c13','support'),('15','15a:15','q15','c13','objection'),('16','15a:16','c16','c15','objection'),('18','15a:18','q18','c16','objection'),('19','15a:19','c19','q18','answer'),('21','15a:21','q21','c19','objection'),('21s','15a:21','c20','q21','support'),('22','15a:22','c22own','q21','answer'),('22t','15a:22','c22teacher','c22own','support'),('22m','15a:22','c22meir','c22teacher','distinction'),('23','15a:23','c23','c22own','distinction')]:edge('e'+k,ref,a,b,rel)
# Complete evidence for the split grace-after-meals rule.
for x in rows:
 if x['id'] in [pre+'c17',pre+'p17']:x['evidence'].append(ev('15a:18','יצא'))
 if x['layer']=='claims':x['content']['scope']='Local audibility and terumah attribution dialectic. Keep initial versus retrospective permission, biblical act versus rabbinic blessing and alternative Rabbi Yehuda/teacher/Rabbi Meir assignments separate. Final practical synthesis occurs15b12–14.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read15a6–16a23 including repeated Megillah dialectic, dual practical ruling and corrected Rav Yosef report; reread core15a6–23 for both Mishnah disputes, language/audibility derivations, terumah act versus blessing, each provisional attribution, two counterexample baraitot and both surviving teacher/student reconciliations. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch28_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch28_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch28_receipt.json',r.encoded(out));print(r.encoded(out).decode())
