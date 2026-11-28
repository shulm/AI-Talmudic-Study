from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.standingvaluation.20261127w3.'
assert r.sha(r.encoded(state))=='57d542a155575761e748fa7f3e56d101e297f4bf90f732191cc92368c7d3d8de'
refs=['14b:'+str(n) for n in range(15,20)]+['15a:'+str(n) for n in range(1,5)]
add('s','structure',refs,dict(title='Dead-animal redemption: standing and valuation, school of Levi and two readings of Rav',primary=True,boundary='closed',legacy_ids=[]))
c('c15assign','14b:15','Rav Yehuda reports Rav assigning the Mishnah’s dead-animal redemption rule to Rabbi Shimon.')
c('c15altar','14b:15','Rabbi Shimon includes altar consecrations in standing and valuation.')
c('c15maintenance','14b:15','He excludes Temple-maintenance consecrations from standing and valuation.')
c('c16maintenance','14b:16','The cited Mishnah permits redeeming dead Temple-maintenance consecrations according to Rabbi Shimon.')
c('c16blemish','14b:16','Rabbi Shimon concedes redemption of an animal blemished from the outset.')
c('c16verse','14b:16','The restrictive it wording excludes an originally blemished animal from standing and valuation.')
c('c17bury','14b:17','The contrasting Sages statement requires burial when they die.')
c('c17identify','14b:17','The Gemara identifies those Sages as the school of Levi.')
c('c17all','14b:17','The school of Levi includes everything in standing and valuation.')
c('c17blemish','14b:17','That inclusion extends even to an animal blemished from the outset.')
c('c18wild','14b:18','The school of Levi’s formulation explicitly includes a wild animal.')
c('c18bird','14b:18','It explicitly includes a bird.')
q('q18','14b:18','How does the school of Levi explain the restrictive it wording?')
c('c18unresolved','14b:18','The passage leaves that difficulty for the school of Levi unresolved.',mode='unresolved')
q('q19','14b:19','What then do the Sages who dispute Rabbi Shimon say about dead-animal redemption?')
c('c19','14b:19','The answer allows that those Sages too permit redemption if the originally blemished animals die.')
q('q1','15a:1','Should Rav then have said this is Rabbi Shimon and those disputing him?')
c('c2rav','15a:2','One answer aligns Rav with Rabbi Shimon ben Lakish’s account of the Sages.')
c('c2maintenance','15a:2','In that account the Sages include Temple-maintenance consecrations in standing and valuation.')
c('c2altar','15a:2','They exclude altar consecrations from standing and valuation.')
c('c2mishnah','15a:2','The Mishnah cannot follow those Sages because its latter clause requires burial if the later-blemished animals die.')
q('q3','15a:3','How is it known that the burial clause rests on standing and valuation rather than the rule against redeeming sacred animals to feed dogs?')
c('c3answer','15a:3','If the dog-feeding rule were the basis, the Mishnah could have stated burial when they become treifa.')
c('c4rav','15a:4','The alternative answer aligns Rav with Rabbi Yohanan.')
c('c4reading','15a:4','It changes the reported wording to Rabbi Shimon and those disputing him.')
for ref,v,role in [('14b:15','Rav Yehuda reporting Rav','RabbiShimon attribution and category contrast'),('14b:16','Quoted Mishnah and anonymous explanation','Dead maintenance animals and original-blemish exception'),('14b:17','Anonymous Gemara and school of Levi','Burial view and broad inclusion'),('14b:18','School of Levi wording and anonymous objection','Wild/bird inclusion with unresolved verse'),('14b:19','Anonymous exchange','Other Sages permit original-blemish redemption'),('15a:1','Anonymous Gemara','Challenge to narrow Rav attribution'),('15a:2','Anonymous answer citing Rabbi Shimon ben Lakish','First account of Rav'),('15a:3','Anonymous exchange','Alternative burial basis rejected'),('15a:4','Anonymous alternative answer citing Rabbi Yohanan','Second account and expanded report wording')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
att('a15y','14b:15','רב יהודה','transmitter',['רב יהודה'],'Mishnah attribution',['רב יהודה','רב'])
att('a15r','14b:15','אמר רב','quoted_authority',['רב'],'Mishnah attribution',['רב יהודה','רב'])
att('a15s','14b:15','רבי שמעון','position_holder',['רבי שמעון'],'Standing/valuation categories')
att('a17','14b:17','תנא דבי לוי','collective',['School of לוי'],'All categories included')
att('a2','15a:2','רבי שמעון בן לקיש','quoted_authority',['ריש לקיש'],'Sages standing/valuation categories')
att('a4','15a:4','רבי יוחנן','quoted_authority',['רבי יוחנן'],'Alternative alignment of Rav')
for k,ref,cl,h,st,qu in [('p15a','14b:15','c15altar',['רבי שמעון'],'Altar included',None),('p15m','14b:15','c15maintenance',['רבי שמעון'],'Maintenance excluded',None),('p16','14b:16','c16blemish',['רבי שמעון'],'Originally blemished exception',None),('p17','14b:17','c17blemish',['School of לוי'],'Originally blemished included',None),('p18','14b:18','c18unresolved',['Anonymous Gemara'],'Explicit difficulty','q18'),('p19','14b:19','c19',['Sages disputing רבי שמעון'],'Originally blemished redemption','q19'),('p2','15a:2','c2rav',['Anonymous Gemara'],'First report alignment','q1'),('p2m','15a:2','c2maintenance',['Sages according to ריש לקיש'],'Maintenance included',None),('p2a','15a:2','c2altar',['Sages according to ריש לקיש'],'Altar excluded',None),('p4','15a:4','c4reading',['Anonymous Gemara'],'Alternative report wording','q1')]:pos(k,ref,cl,h,st,qu)
for k,ref,a,b,rel in [('e16m','14b:16','c16maintenance','c15maintenance','support'),('e16v','14b:16','c16verse','c16blemish','support'),('e17','14b:17','c17identify','c17bury','qualification'),('e17d','14b:17','c17blemish','c16blemish','distinction'),('e18','14b:18','c18unresolved','q18','unresolved_outcome'),('e19','14b:19','c19','q19','answer'),('e1','15a:1','q1','c15assign','objection'),('e2','15a:2','c2rav','q1','answer'),('e2m','15a:2','c2mishnah','c2rav','support'),('e3q','15a:3','q3','c2mishnah','objection'),('e3','15a:3','c3answer','q3','answer'),('e4','15a:4','c4reading','q1','answer'),('e4r','15a:4','c4rav','c4reading','support')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Standing/valuation taxonomy preserves RabbiShimon, school-of-Levi and other-Sages distinctions. Two alternative accounts of Rav remain separate; RabbiShimonBenLakish is not RabbiShimon. School-of-Levi verse difficulty explicitly unresolved.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read14b15–15a20 and omission reread14b15–15a4. Altar/maintenance and original-blemish cases separated, school-of-Levi unresolved wording retained, cross-page objection resolved by two alternative report accounts rather than silent replacement. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch35_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch35_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch35_receipt.json',r.encoded(out));print(r.encoded(out).decode())
