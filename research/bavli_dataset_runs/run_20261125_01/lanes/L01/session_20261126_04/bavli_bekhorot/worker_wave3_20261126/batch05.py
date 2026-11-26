from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.blemishes.20261126w3.'
assert r.sha(r.encoded(state))=='f61255b91c29e2b74062031db3dae389cd23890d62180c54c03849a382e50bef'
refs=['3a:19']+['3b:'+str(n) for n in range(1,10)]
add('s','structure',refs,dict(title='Rabbi Yohanan report, minor share and change of species as permanent blemish',primary=True,boundary='closed',legacy_ids=[]))
for ref,voice,role in [('3a:19','Rabbi Eleazar asking Rabbi Asi','School report introduced'),('3b:1','Rabbi Asi reporting Rabbi Yohanan','Two reported teachings'),('3b:2','Anonymous Gemara','Import of first teaching'),('3b:3','Anonymous Gemara','Novelty challenge'),('3b:4','Anonymous Gemara','Possible distinction and counterexample'),('3b:5','Tannaitic gloss and anonymous argument','Eye dimensions and inference'),('3b:6','Anonymous Gemara','Alternative unevenness explanation and proof'),('3b:7','Anonymous Gemara','Human/animal distinction'),('3b:8','Anonymous Gemara','Reasoning for unevenness'),('3b:9','Anonymous Gemara','Reinstated change explanation with qualification')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'))
q('q19',('3a:19','מאי אמור רבנן בי מדרשא'),'Rabbi Eleazar asks Rabbi Asi what the Sages said in the study hall.')
c('c1minor',('3b:1',"הכי אמר רבי יוחנן אפי' מום קל"),'Rabbi Asi reports Rabbi Yohanan that even a minor blemish suffices in the preceding partnership-threshold issue.',cond=['Non-Jewish share corresponding to a minor blemish'])
next(x for x in rows if x['id']==pre+'c1minor')['evidence'].append(ev('3a:19'))
c('c1different',('3b:1','רחל שילדה מין עז ועז שילדה מין רחל פטורה מן הבכורה'),'The cited Mishnah exempts a ewe producing a goat-kind offspring or a goat producing a sheep-kind offspring.',cond=['Offspring differs in kind as specified'])
c('c1signs',('3b:1','ואם יש בו מקצת סימנין חייב'),'If the offspring has some corresponding signs, the cited Mishnah imposes firstborn status.',cond=['Offspring has some corresponding signs of the mother’s kind'])
c('c1permanent',('3b:1','מום קבוע הוי לשחוט עליו'),'The report treats that change as a permanent blemish permitting slaughter on its basis.',cond=['Differing-kind offspring with some corresponding signs, hence firstborn status'])
c('c2','3b:2','The minor-blemish report supports Rav Huna’s threshold and excludes those of Rav Hisda and Rava.')
q('q3',('3b:3','אלא מום קבוע מאי קא משמע לן'),'What is new in saying that this is a permanent blemish?')
c('c3pig',('3b:3','ופיו דומה כשל חזיר הרי זה מום'),'The objection cites a mouth resembling a pig’s as an already-taught blemish.')
c('c4dist',('3b:4','וכי תימא התם נשתנה בדבר שאין במינו קדוש בבכורה הכא נשתנה בדבר שבמינו קדוש בבכורה'),'A possible distinction contrasts change toward a kind not subject to firstborn sanctity with change toward a kind subject to it.',mode='hypothetical')
c('c4eyes',('3b:4','עינו אחת גדולה ואחת קטנה'),'The counterexample cites one large eye and one small eye.')
c('c5large',('3b:5','גדולה גדולה כשל עגל'),'The tannaitic gloss explains large as like a calf’s eye.')
c('c5small',('3b:5','וקטנה קטנה כשל אווז'),'The gloss explains small as like a goose’s eye.')
c('c5inference',('3b:5','אלא גדולה כשל עגל יש במינו קדוש בבכורה אלא לאו משום דאמרינן כיון דאישתני הוה ליה מומא'),'Since a calf’s kind is subject to firstborn sanctity, the argument infers that change itself makes the blemish.',mode='hypothetical')
c('c6uneven',('3b:6','לא משום דהוה ליה שרוע'),'The reply instead explains the case by unevenness or disproportion.',mode='hypothetical')
c('c6human',('3b:6','יתר עליהן אדם עיניו שתיהן גדולות שתיהן קטנות'),'The support cites both eyes large or both small as additional human defects.')
c('c7human',('3b:7','גבי אדם הוא דכתיב (ויקרא כב, ד) איש איש מזרע אהרן דבעינן איש שוה בזרעו של אהרן'),'For a human priest the verse is interpreted as requiring ordinary proportion among Aaron’s descendants.')
c('c7animal',('3b:7','אבל בהמה שתיהן גדולות שתיהן קטנות נמי לא הוי מומא'),'For an animal, both eyes large or both small are not a blemish.')
q('q8',('3b:8','אחת גדולה ואחת קטנה מאי טעמא'),'Why then are one large and one small eye a blemish?')
c('c8change',('3b:8','אי משום שינוי אפילו שתיהן גדולות שתיהן קטנות נמי'),'The argument objects that if mere change were decisive, both large or both small should also be a blemish.',mode='hypothetical')
c('c8uneven',('3b:8','אלא לאו משום דהוה ליה שרוע'),'The argument accordingly infers unevenness as the basis.',mode='hypothetical')
c('c9change',('3b:9','לא לעולם אימא לך משום שינוי שינוי הוי מומא'),'The reply reinstates change as a sufficient explanation of the blemish.')
c('c9robust',('3b:9','התם אי מחמת בריותא יתירא תרווייהו בעי למיברא'),'It qualifies the symmetric case: unusual robustness should enlarge both eyes.')
c('c9weak',('3b:9','אי מחמת כחישותא יתירא תרווייהו בעי מיכחש'),'Likewise unusual weakness should make both eyes smaller.')
for k,ref,surface,role,cands,scope,chain in [('a19e','3a:19',"ר' אלעזר",'speaker',['רבי אלעזר'],'q19',[]),('a19a','3a:19','רבי אסי','transmitter',['רבי אסי'],'Report continuing3b1',['רבי אסי','רבי יוחנן']),('a1y','3b:1','רבי יוחנן','quoted_authority',['רבי יוחנן'],'Minor share and permanent blemish',['רבי אסי','רבי יוחנן']),('a5','3b:5','ותנא','anonymous',[],'Eye-dimension gloss',[])]:att(k,ref,surface,role,cands,pre+scope if scope.startswith('q') else scope,chain)
for k,ref,cl,h,status,question in [('p1m','3b:1','c1minor',['רבי יוחנן'],'Report through Rabbi Asi','q19'),('p1p','3b:1','c1permanent',['רבי יוחנן'],'Second reported teaching; novelty debated','q19'),('p4','3b:4','c4dist',['Anonymous Gemara'],'Possible distinction challenged by eye example','q3'),('p6','3b:6','c6uneven',['Anonymous Gemara'],'Alternative explanation, later countered',None),('p8','3b:8','c8uneven',['Anonymous Gemara'],'Proposed inference countered in3b9','q8'),('p9','3b:9','c9change',['Anonymous Gemara'],'Reinstated possible explanation','q8')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for k,ref,a,b,rel in [('e1','3b:1','c1minor','q19','answer'),('e1p','3b:1','c1permanent','q19','answer'),('e1s','3b:1','c1signs','c1different','qualification'),('e2','3b:2','c2','c1minor','support'),('e3','3b:3','c3pig','q3','support'),('e4','3b:4','c4dist','q3','answer'),('e4o','3b:4','c4eyes','c4dist','objection'),('e5l','3b:5','c5large','c4eyes','qualification'),('e5s','3b:5','c5small','c4eyes','qualification'),('e5i','3b:5','c5inference','c4dist','objection'),('e6','3b:6','c6uneven','c5inference','objection'),('e6h','3b:6','c6human','c6uneven','support'),('e7h','3b:7','c7human','c6human','support'),('e7a','3b:7','c7animal','c6human','distinction'),('e8','3b:8','c8change','c8uneven','support'),('e8a','3b:8','c8uneven','q8','answer'),('e9','3b:9','c9change','c8uneven','objection'),('e9r','3b:9','c9robust','c9change','support'),('e9w','3b:9','c9weak','c9change','support')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local RabbiYohanan report and novelty debate. Alternative causes of eye blemish are argument stages; final counterreply preserves a change-based reading rather than licensing a blanket medical inference.'
 if x['id']==pre+'c1permanent':x['uncertainty'].append('Antecedent supplied by immediately cited differing-kind/some-signs case; retained as contextual scope.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read3a19–4a13 continuation. Omission reread preserves crossfolio RabbiAsi→RabbiYohanan report, two teachings, citedMishnah conditions, calf/goose distinction, human/animal symmetry and final rebuttal. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch05_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch05_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch05_receipt.json',r.encoded(out));print(r.encoded(out).decode())
