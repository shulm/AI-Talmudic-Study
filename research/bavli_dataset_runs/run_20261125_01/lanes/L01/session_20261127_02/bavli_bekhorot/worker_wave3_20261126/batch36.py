from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.deergazelle.20261127w3.'
assert r.sha(r.encoded(state))=='b3179521aa43132294b4c0dba987dbdae5bae4ef489d41889ebb85e0f6221693'
refs=['15a:'+str(n) for n in range(5,21)]+['15b:1']
add('s1','structure',refs[:15],dict(title='Deer/gazelle analogy: firstborn, gifts, forbidden fat and parent-offspring slaughter',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[15:],dict(title='Residual restrictions and alternative reading on redemption to feed dogs',primary=True,boundary='closed',legacy_ids=[]))
q('q5','15a:5','What is the source for the later-blemish regime’s firstborn exemption?')
c('c5','15a:5','The baraita compares disqualified sacred animals to gazelle to exempt them from firstborn status.')
c('c6initial','15a:6','An initial distinction would exempt firstborn status while retaining priestly animal gifts.',mode='hypothetical')
c('c6deer','15a:6','The deer comparison also exempts disqualified sacred animals from priestly gifts.')
c('c7hyp','15a:7','A proposed extension would permit their forbidden fat like that of deer and gazelle.',mode='hypothetical')
c('c7akh','15a:7','The restrictive akh blocks that extension in the baraita’s initial formulation.')
q('q8','15a:8','Why would one distinguish firstborn exemption from gift exemption?')
c('c8first','15a:8','Firstborn status is not uniform for all persons or animals in the way invoked by the argument.')
c('c8gifts','15a:8','Priestly gifts are characterized as generally applicable, motivating the proposed distinction before the deer text excludes them.')
q('q9','15a:9','Rav Pappa asks Abaye whether the deer/gazelle analogy should also remove the same-day parent-and-offspring slaughter prohibition.')
c('c10','15a:10','Abaye replies that the prohibition applies whether the animals are analogized to ordinary domestic animals or to sacred animals.')
q('q11','15a:11','Why would that same either-category answer not preserve the forbidden-fat rule as well?')
c('c12','15a:12','The challenge proposes using akh to retain the parent-offspring slaughter prohibition as it was used to retain forbidden fat.')
c('c13akh','15a:13','Rava assigns akh to the parent-offspring slaughter prohibition.')
c('c13fat','15a:13','He derives the forbidden-fat rule instead from do not eat its blood.')
q('q14','15a:14','Could its blood mean literal blood, since even deer and gazelle blood is forbidden?')
c('c14','15a:14','The exposition therefore reads its blood as referring here to its forbidden fat.')
q('q15','15a:15','Why not write forbidden fat directly?')
c('c15both','15a:15','A direct fat formulation could leave a role for both the deer/gazelle analogy and the explicit prohibition.',mode='hypothetical')
c('c16','15a:16','The proposed role of the analogy would remove karet because the karet text speaks of domestic-animal fat.',mode='hypothetical')
c('c17negative','15a:17','The proposed role of the explicit fat text would be only a negative prohibition.',mode='hypothetical')
c('c17karet','15a:17','Using blood language instead preserves karet for the fat as for the blood.')
q('q18','15a:18','But the tanna explicitly said akh excludes permission of fat.')
c('c19without','15a:19','The answer reads the tanna counterfactually: without the blood text, akh would be used for fat.')
c('c19with','15a:19','With the blood text present, akh is available for the parent-offspring slaughter rule.')
q('q20','15a:20','What is the source that redeemed later-blemished animals do not become fully ordinary?')
c('c20shear','15a:20','The slaughter wording excludes shearing.')
c('c20milk','15a:20','The flesh wording excludes milk.')
c('c20dogs','15a:20','The eat wording excludes feeding them to one’s dogs.')
c('c20redeem','15a:20','From this the baraita derives that sacred animals are not redeemed for feeding dogs.')
c('c1time','15b:1','An alternative formulation reads slaughter and eat as allowing consumption only from slaughter onward.')
c('c1dogs','15b:1','That alternative permits redemption of sacred animals to feed dogs.')
for ref,v,role in [('15a:5','Anonymous Gemara citing baraita','Gazelle firstborn exemption'),('15a:6','Baraita','Deer gift exemption'),('15a:7','Baraita','Fat permission rejected by akh'),('15a:8','Anonymous Gemara','Why distinguish firstborn and gifts'),('15a:9','Rav Pappa to Abaye','Parent-offspring prohibition question'),('15a:10','Abaye reply','Ordinary/sacred categories'),('15a:11','Dialogue challenge','Fat parallel'),('15a:12','Dialogue challenge continuation','Akh allocation'),('15a:13','Rava','Revised verse allocation'),('15a:14','Anonymous Gemara','Blood interpreted as fat'),('15a:15','Anonymous Gemara','Why indirect wording'),('15a:16','Anonymous explanation','Possible removal of karet'),('15a:17','Anonymous explanation','Negative prohibition versus karet'),('15a:18','Anonymous objection','Baraita wording challenge'),('15a:19','Anonymous answer','Counterfactual reading'),('15a:20','Baraita','Shearing, milk and dog-feeding exclusions'),('15b:1','Alternative version','Eating after slaughter and dog-feeding permission')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
att('a9p','15a:9','רב פפא','speaker',['רב פפא'],'Question to Abaye')
att('a9a','15a:9','לאביי','quoted_authority',['אביי'],'Explicit question recipient, reply at15a10 follows')
att('a13','15a:13','רבא','speaker',['רבא'],'Akh/blood allocation')
for k,ref,cl,h,st,qu in [('p5','15a:5','c5',['Anonymous baraita'],'Firstborn exemption','q5'),('p6','15a:6','c6deer',['Anonymous baraita'],'Gift exemption',None),('p7','15a:7','c7akh',['Anonymous baraita'],'Initial wording later explained counterfactually',None),('p10','15a:10','c10',['אביי'],'Reply challenged','q9'),('p13a','15a:13','c13akh',['רבא'],'Parent-offspring rule source','q9'),('p13f','15a:13','c13fat',['רבא'],'Fat prohibition source',None),('p17','15a:17','c17karet',['Anonymous Gemara'],'Karet retained','q15'),('p19','15a:19','c19with',['Anonymous Gemara'],'Final allocation','q18'),('p20','15a:20','c20redeem',['Anonymous baraita'],'No redemption for dogs','q20'),('p1','15b:1','c1dogs',['Alternative anonymous report'],'Redemption for dogs permitted',None)]:pos(k,ref,cl,h,st,qu)
for k,ref,a,b,rel in [('e5','15a:5','c5','q5','answer'),('e6','15a:6','c6deer','c6initial','objection'),('e7','15a:7','c7akh','c7hyp','objection'),('e8f','15a:8','c8first','q8','answer'),('e8g','15a:8','c8gifts','q8','answer'),('e10','15a:10','c10','q9','answer'),('e11','15a:11','q11','c10','objection'),('e12','15a:12','c12','q11','support'),('e13','15a:13','c13akh','q9','answer'),('e14','15a:14','c14','q14','answer'),('e14s','15a:14','c14','c13fat','support'),('e17','15a:17','c17karet','q15','answer'),('e18','15a:18','q18','c13akh','objection'),('e19a','15a:19','c19without','q18','answer'),('e19b','15a:19','c19with','q18','answer'),('e20s','15a:20','c20shear','q20','answer'),('e20m','15a:20','c20milk','q20','answer'),('e20d','15a:20','c20dogs','c20redeem','support'),('e1','15b:1','c1dogs','c20redeem','distinction')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Deer/gazelle analogy and residual restrictions. חלב in15a7–19 is forbidden fat; milk is the separate flesh/not-milk exclusion at15a20. Karet versus negative prohibition and alternate dog-feeding report retained without harmonization.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read15a5–16a15 and omission reread15a5–15b1. Fat/milk distinct by context, parent-offspring prohibition challenge and revised verse allocation retained, baraita counterfactual interpretation explicit, alternate dog-feeding permission preserved. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch36_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch36_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch36_receipt.json',r.encoded(out));print(r.encoded(out).decode())
