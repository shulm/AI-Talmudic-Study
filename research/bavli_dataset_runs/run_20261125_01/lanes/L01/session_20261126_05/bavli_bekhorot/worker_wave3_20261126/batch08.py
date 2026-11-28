from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.sheep_redemption.20261126w3.'
assert r.sha(r.encoded(state))=='9640aaaf881518d73f7af2cb357c2db3630ba24306721a6a7f824def9a6e3cf0'
refs=['4b:'+str(n) for n in range(2,11)]
add('s2','structure',refs[:4],dict(title='Sheep redemption in the wilderness and later generations',primary=True,boundary='closed',legacy_ids=[]))
add('s6','structure',refs[4:],dict(title='One Levite sheep redeeming multiple Israelite firstborn donkeys',primary=True,boundary='closed',legacy_ids=[]))
for n,voice,role in [(2,'Anonymous inquiry and Rav Hisda','Medium-of-redemption derivation'),(3,'Rav Hisda argument continuation','Money/sheep analogy'),(4,'Anonymous Gemara','Analogy objection'),(5,'Anonymous Gemara','Replacement paired-verse derivation'),(6,'Rabbi Hanina and Abaye','Multiple-donkey rule and census support'),(7,'Anonymous Gemara','Numerical objection and answer'),(8,'Anonymous Gemara','Alternative numerical objection and verse answer'),(9,'Anonymous Gemara','Collective-noun objection and wording answer'),(10,'Rava and anonymous explanation','Mishnah support and rationale relation')]:add('u'+str(n),'utterances',['4b:'+str(n)],dict(textual_voice=voice,discourse_role=role,composition='composite'))
q('q2',('4b:2','וממאי דבשה'),'How is it known that the wilderness animal redemption used a sheep?')
c('c2money',('4b:2','נאמר כסף לדורות'),'Rav Hisda notes that money is specified for later generations.')
c('c2sheep',('4b:2','ונאמר שה לדורות'),'He notes that a sheep is specified for later generations.')
c('c3money',('4b:3','מה כסף האמור לדורות בו פדו לדורות בו פדו לאותה שעה'),'His analogy says the money used in later generations was also used at that time.')
c('c3sheep',('4b:3','אף שה האמור לדורות בו פדו לדורות בו פדו באותה שעה'),'It infers the same continuity for sheep redemption.',mode='hypothetical')
q('q4','4b:4','Is money different because it also redeems consecrated property and second tithe?')
c('c5','4b:5','The replacement proof pairs human and unclean-animal firstborn in the verse: as the human redemption medium does not differ between that time and later generations, neither does sheep redemption of unclean animals.')
c('c6rule',('4b:6','שה אחד של בן לוי פטר כמה פטרי חמורים מישראל'),'Rabbi Hanina says one Levite sheep released multiple Israelite firstborn donkeys.',cond=['Wilderness redemption'])
c('c6count',('4b:6','שהרי מנה הכתוב עודפים באדם ולא מנה עודפין בבהמה'),'Abaye supports this from scripture counting surplus people but not surplus animals.')
q('q7',('4b:7','ממאי דילמא לא הוי נפישי להו בהמות טובא'),'Perhaps there simply were not many animals?')
c('c7',('4b:7','לא ס"ד דכתיב (במדבר לב, א) ומקנה רב היה לבני ראובן ולבני גד'),'The answer rejects that by the verse about abundant livestock among Reuben and Gad.')
q('q8',('4b:8','דילמא אפילו הכי פשוטים דלוים הוו קיימי לבהדי בכורי ישראל'),'Perhaps nevertheless the Levites’ ordinary animals numerically matched Israel’s firstborn?')
c('c8',('4b:8','בהמה אחת תחת בהמות הרבה'),'The answer reads the singular Levite animal against plural Israelite animals as one animal in place of many.')
q('q9',('4b:9','ואימא (יונה ד, יא) בהמה רבה'),'Could animal be collective as in the phrase much livestock?')
c('c9','4b:9','The reply uses the unmatched singular/plural wording: either both singular or both plural would suffice otherwise; the mismatch implies one redeeming many.')
c('c10mish',('4b:10','אף אנן נמי תנינא ופודה בו פעמים הרבה'),'Rava cites the Mishnah permitting repeated redemption with it as support.')
c('c10relation',('4b:10',"ור' חנינא טעמא דמתני' מפרש"),'The continuation explains that Rabbi Hanina supplies the Mishnah’s reason.')
c('c10reason',('4b:10','משום דשה אחד של בן לוי פוטר כמה פטרי חמורים של ישראל'),'The repeated-use rule is explained by one Levite sheep having released multiple Israelite firstborn donkeys.')
for k,ref,surface,role,cands,scope in [('a2','4b:2','רב חסדא','speaker',['רב חסדא'],'Initial analogy'),('a6h','4b:6',"ר' חנינא",'speaker',['רבי חנינא'],'c6rule'),('a6a','4b:6','אביי','speaker',['אביי'],'c6count'),('a10','4b:10','רבא','speaker',['רבא'],'c10mish')]:att(k,ref,surface,role,cands,pre+scope if scope.startswith('c') else scope)
for k,ref,cl,h,status,question in [('p3','4b:3','c3sheep',['רב חסדא'],'Initial analogy challenged by money distinction','q2'),('p5','4b:5','c5',['Anonymous Gemara'],'Replacement derivation','q2'),('p6h','4b:6','c6rule',['רבי חנינא'],'Reported wilderness rule',None),('p6a','4b:6','c6count',['אביי'],'Census support challenged by numerical alternatives',None),('p8','4b:8','c8',['Anonymous Gemara'],'Verse answer','q8'),('p9','4b:9','c9',['Anonymous Gemara'],'Wording answer','q9'),('p10','4b:10','c10mish',['רבא'],'Mishnah comparison',None)]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for k,ref,a,b,rel in [('e2m','4b:2','c2money','c3sheep','support'),('e2s','4b:2','c2sheep','c3sheep','support'),('e3m','4b:3','c3money','c3sheep','analogy'),('e3a','4b:3','c3sheep','q2','answer'),('e4','4b:4','q4','c3sheep','objection'),('e5','4b:5','c5','q2','answer'),('e6','4b:6','c6count','c6rule','support'),('e7q','4b:7','q7','c6count','objection'),('e7a','4b:7','c7','q7','answer'),('e8q','4b:8','q8','c6count','objection'),('e8a','4b:8','c8','q8','answer'),('e9q','4b:9','q9','c8','objection'),('e9a','4b:9','c9','q9','answer'),('e10s','4b:10','c10mish','c6rule','support'),('e10r','4b:10','c10relation','c10mish','qualification'),('e10reason','4b:10','c10reason','c10mish','support')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local historical redemption derivation and repeated-use rationale. Initial money analogy is challenged; numerical alternatives are proof-analysis possibilities, not established counts.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read4b2-24 surroundingtext. Omission reread retains replacementderivation, surplus-count versus ratio alternatives, collective-noun challenge, singular/plural answer and Mishnah/rationale direction. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch08_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch08_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch08_receipt.json',r.encoded(out));print(r.encoded(out).decode())
