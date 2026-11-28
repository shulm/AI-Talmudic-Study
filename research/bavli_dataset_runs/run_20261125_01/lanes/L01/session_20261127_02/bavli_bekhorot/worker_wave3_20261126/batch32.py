from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.scraptransfer.20261127w3.'
assert r.sha(r.encoded(state))=='16a3c142c4d6577dbbbb931ccdacd357545d45955b45804a0c2b7715c2cac433'
refs=['13b:'+str(n) for n in range(2,15)]
add('s1','structure',refs[:5],dict(title='Amemar’s drawing-acquisition rule and possible underlying scriptural positions',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[5:],dict(title='Idol found in scrap purchase: acquisition, mistaken purchase and alternative readings',primary=True,boundary='closed',legacy_ids=[]))
c('c2amemar','13b:2','Amemar says drawing acquires in a transaction with a gentile.')
c('c2yohanan','13b:2','Rabbi Yohanan’s position says money acquires by Torah law.')
c('c2fit','13b:2','If Amemar follows Rabbi Yohanan, your fellow distinguishes money for the Israelite transaction from drawing for the gentile transaction.',cond=['Amemar follows RabbiYohanan'])
c('c3rl','13b:3','Resh Lakish holds drawing is specified by Torah law.')
q('q3','13b:3','If Amemar follows Resh Lakish and both transactions use drawing, what does your fellow exclude?')
c('c4first','13b:4','The proposed answer uses your fellow to limit return of overcharge to the Israelite counterparty.')
q('q4','13b:4','Is that exclusion not already derived from do not wrong each his brother?')
c('c5two','13b:5','The answer assigns one exclusion to a gentile and one to sacred property.')
c('c5need','13b:5','Without both one might exclude only the gentile while retaining overcharge liability for sacred property.',mode='hypothetical')
q('q6','13b:6','For a view permitting theft from a gentile, why would a verse be needed to permit overcharge?')
c('c6','13b:6','Under that hypothetical underlying view, Amemar must follow Rabbi Yohanan’s money-acquisition position.')
c('c7before','13b:7','The cited baraita says a buyer who drew scrap from a gentile and discovered an idol before paying should return it.',cond=['Idol discovered in scrap','Drawing before payment'])
c('c7after','13b:7','If he drew after payment, he must cast the benefit into the Dead Sea.',cond=['Idol discovered in scrap','Payment then drawing'])
q('q8','13b:8','If money acquires, why does the latter clause need drawing?')
c('c8law','13b:8','The proposed answer makes the case one accepting adjudication under Israelite law.')
q('q8money','13b:8','Then why is payment mentioned?')
c('c8reading','13b:8','The answer reads it as even if paid, acquisition needs drawing; without drawing it does not occur.')
q('q9','13b:9','On that reading why does the initial clause permit return after drawing?')
c('c9abaye','13b:9','Abaye says the initial clause involves mistaken purchase.')
q('q9rava','13b:9','Rava asks whether the latter clause is not also mistaken purchase.')
c('c10both','13b:10','Rava treats both clauses as mistaken purchase.')
c('c10before','13b:10','Before payment the idol does not appear to have been in Israelite ownership.')
c('c10after','13b:10','After payment it appears to have been in Israelite ownership.')
c('c11before','13b:11','Abaye replies that before payment the buyer did not know and the purchase is mistaken.')
c('c11after','13b:11','After paying, the buyer should inspect before drawing, so the latter case is not treated as mistaken purchase.')
c('c12first','13b:12','Rav Ashi infers from the first clause that drawing does not acquire.')
c('c12last','13b:12','He likewise reads the latter clause as drawing not acquiring.')
c('c12word','13b:12','He explains the latter mention of drawing as wording parallel to the initial clause.')
c('c13last','13b:13','Ravina instead infers from the latter clause that drawing acquires.')
c('c13first','13b:13','He interprets the first clause as neither paid nor drawn.')
c('c13return','13b:13','Return there means withdrawal from the verbal agreement.')
c('c14general','13b:14','The explanation recognizes lack of good faith in withdrawing from words.')
c('c14israel','13b:14','It applies that concern to Israelite-to-Israelite dealings, described as parties keeping their word.')
c('c14gentile','13b:14','It does not apply that concern here to Israelite purchase from a gentile, based on the passage’s stated characterization of the other party’s reliability.')
for ref,v,role in [('13b:2','Anonymous Gemara citing Amemar and Rabbi Yohanan','Drawing rule under money-acquisition premise'),('13b:3','Anonymous Gemara citing Resh Lakish','Alternative underlying premise question'),('13b:4','Anonymous exchange','Overcharge exclusion and redundancy'),('13b:5','Anonymous answer','Gentile/sacred-property distinction'),('13b:6','Anonymous conditional argument','Theft-permission premise forces RabbiYohanan alignment'),('13b:7','Baraita','Scrap purchase with idol'),('13b:8','Anonymous exchange','Accepted law and even-if-paid reading'),('13b:9','Abaye and Rava','Mistaken-purchase exchange'),('13b:10','Rava','Both mistaken, appearance distinction'),('13b:11','Abaye reply','Knowledge and duty to inspect distinction'),('13b:12','Rav Ashi','Drawing does not acquire reading'),('13b:13','Ravina','Drawing acquires and verbal return reading'),('13b:14','Anonymous exposition','Good-faith principle and stated scope')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
for k,ref,surf,role,cands,scope in [('a2a','13b:2','אמימר','quoted_authority',['אמימר'],'Drawing acquisition'),('a2y','13b:2',"ר' יוחנן",'position_holder',['רבי יוחנן'],'Torah money acquisition'),('a3','13b:3','ר"ל','position_holder',['ריש לקיש'],'Torah drawing acquisition'),('a9a','13b:9','אביי','speaker',['אביי'],'Initial clause mistaken purchase'),('a9r','13b:9','רבא','speaker',['רבא'],'Challenge to Abaye'),('a10','13b:10','רבא','speaker',['רבא'],'Both mistaken purchases'),('a11','13b:11','אביי','position_holder',['אביי'],'Reply based on inspection'),('a12','13b:12','רב אשי','speaker',['רב אשי'],'Drawing nonacquisition reading'),('a13','13b:13','רבינא','speaker',['רבינא'],'Drawing acquisition reading')]:att(k,ref,surf,role,cands,scope)
for k,ref,cl,h,st,qu in [('p2a','13b:2','c2amemar',['אמימר'],'Reported rule',None),('p2f','13b:2','c2fit',['Anonymous Gemara'],'Conditional alignment',None),('p4','13b:4','c4first',['Anonymous Gemara'],'Proposed exclusion','q3'),('p5','13b:5','c5two',['Anonymous Gemara'],'Two exclusions','q4'),('p6','13b:6','c6',['Anonymous Gemara'],'Conditional forced alignment','q6'),('p7b','13b:7','c7before',['Anonymous baraita'],'Return, subject to subsequent readings',None),('p7a','13b:7','c7after',['Anonymous baraita'],'Destroy benefit, subject to subsequent readings',None),('p8','13b:8','c8reading',['Anonymous Gemara'],'Proposed reading','q8money'),('p9','13b:9','c9abaye',['אביי'],'Initial-clause explanation','q9'),('p10','13b:10','c10both',['רבא'],'Competing explanation','q9rava'),('p11','13b:11','c11after',['אביי'],'Latter-clause distinction','q9rava'),('p12','13b:12','c12first',['רב אשי'],'Alternative nonacquisition reading',None),('p13','13b:13','c13last',['רבינא'],'Alternative acquisition reading',None),('p13r','13b:13','c13return',['רבינא'],'Verbal withdrawal reading',None)]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e4','13b:4','c4first','q3','answer'),('e4q','13b:4','q4','c4first','objection'),('e5','13b:5','c5two','q4','answer'),('e5n','13b:5','c5need','c5two','support'),('e6','13b:6','c6','q6','answer'),('e8','13b:8','c8law','q8','answer'),('e8m','13b:8','c8reading','q8money','answer'),('e9','13b:9','c9abaye','q9','answer'),('e9r','13b:9','q9rava','c9abaye','objection'),('e10','13b:10','c10both','q9rava','answer'),('e10a','13b:10','c10after','c7after','support'),('e10b','13b:10','c10before','c7before','support'),('e11a','13b:11','c11after','c10both','objection'),('e11b','13b:11','c11before','c9abaye','support'),('e12','13b:12','c12word','c12last','support'),('e13','13b:13','c13last','c12first','distinction'),('e13f','13b:13','c13first','c7before','qualification'),('e13r','13b:13','c13return','c13first','qualification'),('e14i','13b:14','c14israel','c14general','qualification'),('e14g','13b:14','c14gentile','c14general','qualification')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Historical source discussion only. Competing acquisition and mistaken-purchase readings not merged into one ruling. Conditional discussion of theft/overcharge and generalized reliability characterizations are attributed source premises, not endorsed contemporary factual or legal claims.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read13b2–14a9 and omission reread13b2–14. Amemar conditional alignments, overcharge verses, payment/drawing sequence, Abaye/Rava explanations and RavAshi/Ravina alternative readings retained independently. No final universal acquisition ruling inferred. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch32_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch32_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch32_receipt.json',r.encoded(out));print(r.encoded(out).decode())
