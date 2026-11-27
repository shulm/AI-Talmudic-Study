from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.blessings_torah.20261126e5.'
assert r.sha(r.encoded(state))=='8bc159fa1bd4a69c2ea3766a7f59ca31ebbc4ee9ce0210de8ddb944cf9db2650'
refs=['11a:'+str(i) for i in range(24,28)]+['11b:'+str(i) for i in range(1,20)]
for k,rr,title in [('mishna',refs[:2],'Number and prescribed forms of Shema blessings'),('light',refs[2:11],'Light/dark wording and day/night mention'),('love',refs[11:13],'Ahavah Rabbah versus Ahavat Olam'),('study',refs[13:19],'When and for which study Torah blessings are required'),('formula',refs[19:],'Torah blessing formulas and combined instruction')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Mishnah','Mishnah','Anonymous question','Rabbi Yaakov reporting Rabbi Oshaya']+['Completion of reported blessing','Anonymous alternative wording','Anonymous first answer','Anonymous objection','Rava','Anonymous question','Abaye','Rav Yehuda reporting Shmuel; Rabbi Eleazar instructing Rabbi Pedat','Baraita and opposing sages','Rav Yehuda reporting Shmuel','Rav Huna','Rabbi Eleazar','Rabbi Yohanan','Rava','Rav Hiyya bar Ashi recounting Rav','Anonymous question; Rav Yehuda reporting Shmuel','Rabbi Yohanan','Rav Hamnuna','Anonymous conclusion']
assert len(voices)==len(refs)
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Mishnah or blessing discussion',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('24morning','11a:24','The Mishnah prescribes two blessings before morning Shema and one after.',['Anonymous Mishnah'])
claim('24evening','11a:24','For evening Shema it prescribes two before and two after, one long and one short.',['Anonymous Mishnah'],unc=['This line does not name the long/short blessings.'])
for k,text in [('long','Where a long form is prescribed one may not shorten it.'),('short','Where a short form is prescribed one may not lengthen it.'),('close','Where a concluding formula is prescribed one may not omit it.'),('noclose','Where no concluding formula is prescribed one may not add one.')]:claim('25'+k,'11a:25',text,['Anonymous Mishnah'])
q('q26','11a:26','What blessing is said?')
claim('1','11b:1','Rabbi Oshaya via Rabbi Yaakov gives forms light and creates darkness.',['Rabbi Oshaya'],unc=['Speaker prefix in11a27 completes at11b1.'])
claim('2','11b:2','The discussion proposes replacing darkness with brightness.',['Anonymous Gemara'],status='Proposed alternative wording')
claim('3','11b:3','The first answer says to use the scriptural wording.',['Anonymous Gemara'],status='Answer challenged by following example')
claim('4counter','11b:4','The discussion notes that creates evil is replaced in recitation by creates everything as refined language.',['Anonymous Gemara'])
claim('4proposal','11b:4','It therefore renews the proposal to use brightness as refined language here too.',['Anonymous Gemara'],status='Objection to scriptural-wording rationale')
claim('5','11b:5','Rava instead explains that one must mention the day’s attribute at night and night’s attribute by day.',['Rava'],status='Replacement rationale')
q('q6','11b:6','The morning darkness mention is clear; where is day mentioned at night?')
claim('7','11b:7','Abaye points to rolling light away before darkness and darkness before light.',['Abaye'])
q('q8','11b:8','What is the other blessing?')
claim('8shmuel','11b:8','Rav Yehuda reports Shmuel giving Ahavah Rabbah.',['Shmuel'])
claim('8eleazar','11b:8','Rabbi Eleazar likewise instructed his son Rabbi Pedat to say Ahavah Rabbah.',['Rabbi Eleazar'],status='Parallel instruction')
claim('9baraita','11b:9','A supporting baraita says not Ahavat Olam but Ahavah Rabbah.',['Unnamed baraita'])
claim('9sages','11b:9','The sages instead say Ahavat Olam, citing with everlasting love I loved you.',['Sages'])
claim('10before','11b:10','Shmuel via Rav Yehuda requires a blessing for one rising to study before reading Shema.',['Shmuel'],cond=['Study before Shema'])
claim('10after','11b:10','After Shema no further blessing is needed, since Ahavah Rabbah already exempted him.',['Shmuel'],cond=['Already read Shema with Ahavah Rabbah'])
claim('11script','11b:11','Rav Huna requires blessing for Scripture.',['Rav Huna'])
claim('11midrash','11b:11','Rav Huna does not require blessing for midrash.',['Rav Huna'])
claim('12midrash','11b:12','Rabbi Eleazar requires blessing for Scripture and midrash.',['Rabbi Eleazar'])
claim('12mishna','11b:12','He does not require it for Mishnah.',['Rabbi Eleazar'])
claim('13mishna','11b:13','Rabbi Yohanan also requires blessing for Mishnah.',['Rabbi Yohanan'])
claim('13talmud','11b:13','The bracketed text exempts Talmud in Rabbi Yohanan’s position.',['Rabbi Yohanan'],unc=['Source encloses אבל לתלמוד א"צ לברך in square brackets; retain textual status.'])
claim('14','11b:14','Rava also requires blessing for Talmud.',['Rava'],unc=['Printed לחזור ו is parenthetical; no extra repetition requirement asserted from it alone.'])
claim('15','11b:15','Rav Hiyya bar Ashi recounts that when studying their chapter in Sifra de-Vei Rav before Rav, Rav first washed his hands, blessed and taught them.',['Rav Hiyya bar Ashi'],status='Narrative evidence; Rav is the actor')
q('q16','11b:16','What blessing is said for study?')
claim('16','11b:16','Shmuel via Rav Yehuda gives the blessing sanctifying through commandments and commanding engagement in words of Torah.',['Shmuel'])
claim('17','11b:17','Rabbi Yohanan appends the prayer for Torah’s sweetness in the mouths of Israel and their descendants, ending who teaches Torah to His people Israel.',['Rabbi Yohanan'])
claim('18formula','11b:18','Rav Hamnuna gives who chose us from all peoples and gave us His Torah, ending giver of Torah.',['Rav Hamnuna'])
claim('18best','11b:18','He calls this the finest of the blessings.',['Rav Hamnuna'])
claim('19','11b:19','The conclusion directs saying all of them.',['Anonymous Gemara'],status='Explicit local combined instruction')
att('a27','11a:27',"ר' יעקב א"+'"'+"ר אושעיא",'transmitter',['רבי יעקב'],pre+'c1',chain=['רבי יעקב','רבי אושעיא'])
for k,ref,surface,name in [('5','11b:5','רבא','רבא'),('7','11b:7','אביי','אביי'),('8e','11b:8','רבי אלעזר','רבי אלעזר'),('8p','11b:8',"ר' פדת",'רבי פדת'),('11','11b:11','רב הונא','רב הונא'),('12','11b:12',"ר' אלעזר",'רבי אלעזר'),('13','11b:13',"ר' יוחנן",'רבי יוחנן'),('14','11b:14','רבא','רבא'),('15','11b:15','רב חייא בר אשי','רב חייא בר אשי'),('17','11b:17',"ר' יוחנן",'רבי יוחנן'),('18','11b:18','רב המנונא','רב המנונא')]:att('a'+k,ref,surface,'speaker',[name],'Local teaching or recipient as specified in claim')
for n in [8,10,16]:att('a'+str(n)+'chain','11b:'+str(n),'יהודה אמר שמואל','transmitter',['רב יהודה'],'Shmuel report',chain=['רב יהודה','שמואל'])
for k,ref,a,b,rel in [('1','11b:1','c1','q26','answer'),('3','11b:3','c3','c2','objection'),('4','11b:4','c4counter','c3','objection'),('5','11b:5','c5','c3','correction'),('7','11b:7','c7','q6','answer'),('8','11b:8','c8shmuel','q8','answer'),('8e','11b:8','c8eleazar','c8shmuel','support'),('9b','11b:9','c9baraita','c8shmuel','support'),('9s','11b:9','c9sages','c9baraita','distinction'),('12','11b:12','c12midrash','c11midrash','distinction'),('13','11b:13','c13mishna','c12mishna','distinction'),('14','11b:14','c14','c13talmud','distinction'),('15','11b:15','c15','c14','support'),('16','11b:16','c16','q16','answer'),('17','11b:17','c17','c16','qualification'),('18','11b:18','c18formula','q16','answer'),('19a','11b:19','c19','c16','qualification'),('19b','11b:19','c19','c17','qualification'),('19c','11b:19','c19','c18formula','qualification')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local blessing formulas and study categories; retain bracketed source readings, transmitter/actor distinctions, graded obligations and combined final direction.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read11a24–12b28; reread core11a24–11b19 for cross-folio authority, prescribed form constraints, rejected wording rationale, love-blessing alternatives, before/after Shema, all study categories with brackets/parentheses and three formulas followed by say all. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch18_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch18_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch18_receipt.json',r.encoded(out));print(r.encoded(out).decode())
