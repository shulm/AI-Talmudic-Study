from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.chaptertwo.20261126w3.'
assert r.sha(r.encoded(state))=='faccf1bfa38c73399c5ce47b80b679d927f6e465b0b7f23f152ccd0b38293854'
refs=['13a:'+str(n) for n in range(9,13)]
add('s','structure',refs,dict(title='Pure-animal firstborn ownership cases and reason for chapter order',primary=True,boundary='closed',legacy_ids=[]))
for k,condition in [('buy','Israelite buys fetus of gentile’s cow'),('sell','Israelite sells fetus of his cow to gentile'),('partner','Israelite and gentile share ownership'),('receive','Israelite receives gentile’s animal under the described offspring-sharing arrangement'),('give','Israelite gives gentile his animal under that arrangement')]:
 c('c9'+k,'13a:9','The Mishnah exempts from firstborn liability in this case.',cond=[condition])
 pos('p9'+k,'13a:9','c9'+k,['Anonymous Mishnah'],'Exemption under stated ownership arrangement',cond=[condition])
c('c9prohibit','13a:9','The Mishnah says selling to the gentile is not permitted, while still stating the firstborn exemption as its consequence.')
c('c9verse','13a:9','The exemption derives from in Israel, excluding others.')
c('c10priests','13a:10','Priests are liable for pure-animal firstborn.')
c('c10levites','13a:10','Levites are liable for pure-animal firstborn.')
c('c10limited','13a:10','Their exemption is limited to human-firstborn redemption and firstborn donkey, not pure-animal firstborn.')
q('q11','13a:11','Why did the tractate teach donkey-fetus cases before cow-fetus cases, instead of putting bodily sanctity before monetary sanctity?')
c('c12dear','13a:12','One western answer says the donkey topic is especially beloved, as in Rabbi Hanina’s teaching.')
rows[-1]['uncertainty'].append('כדרבי חנינא cross-reference preserved; identity of the referenced teaching not expanded solely from proximity or memory.')
c('c12short','13a:12','The other western answer says the impure-animal material is short, so it is completed first.')
att('a12west','13a:12','אמרי במערבא','collective',['Unnamed western authorities'],'Two chapter-order explanations')
att('a12hanina','13a:12','רבי חנינא','quoted_authority',['רבי חנינא'],'Cross-reference in beloved-topic explanation',unc=['Referenced teaching not quoted here.'])
for k,cl,h,st in [('p10p','c10priests',['Anonymous Mishnah'],'Pure-animal liability'),('p10l','c10levites',['Anonymous Mishnah'],'Pure-animal liability')]:pos(k,'13a:10',cl,h,st)
pos('p12d','13a:12','c12dear',['Unnamed western authorities'],'First explanation','q11',unc=['Cross-reference not expanded.'])
pos('p12s','13a:12','c12short',['Unnamed western authorities'],'Alternative explanation','q11')
for k in ['buy','sell','partner','receive','give']:edge('e9'+k,'13a:9','c9verse','c9'+k,'support')
edge('e12d','13a:12','c12dear','q11','answer');edge('e12s','13a:12','c12short','q11','answer')
for ref,v,role in [('13a:9','Mishnah','Gentile ownership and arrangements'),('13a:10','Mishnah','Priest and Levite liability scope'),('13a:11','Anonymous Gemara','Chapter-order question'),('13a:12','Unnamed western authorities','Two explanations')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Chapter-two opening ownership exemptions and literary-order explanations. Rules are historical source statements, not contemporary legal advice. Transaction mechanics elaborated in following unit are not assumed here.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read13a9–14a9 and omission reread13a9–12. Five ownership conditions and prohibited-sale consequence separated, priest/Levite exemption scope limited, western alternative explanations and unexpanded cross-reference preserved. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch30_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch30_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch30_receipt.json',r.encoded(out));print(r.encoded(out).decode())
