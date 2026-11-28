from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.privatealtar.20261127w3.'
assert r.sha(r.encoded(state))=='4f8aeb300249eacc7075c887631bade8dcff2f80cf1f99012cf3b2b3e9bf83e3'
refs=['14b:'+str(n) for n in range(4,15)]
add('s1','structure',refs[:10],dict(title='Rabbi Elazar’s alternative outside-slaughter reading and private-altar blemish prohibition',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[10:],dict(title='Original fitness determines substitution sanctity',primary=True,boundary='closed',legacy_ids=[]))
c('c4','14b:4','Rabbi Elazar transmits liable instead of exempt and places the case at an individual altar.')
c('c5rule','14b:5','Rabbi Elazar says slaughtering a blemished animal on an individual altar during the permitted-altar period violates a prohibition.',cond=['Blemished animal','Individual altar','Period when such altars are permitted'])
c('c5verse','14b:5','He uses the do not sacrifice an ox or seh verse for the individual altar because another verse already prohibits blemished offerings at the great altar.')
c('c6alt','14b:6','An alternative assigns the otherwise unneeded verse to firstborn animals.',mode='hypothetical')
c('c6reason','14b:6','One might allow offering a blemished firstborn because it is consecrated despite the blemish.',mode='hypothetical')
c('c7','14b:7','The answer rejects that use because the firstborn’s lame-or-blind prohibition is explicit.')
c('c8alt','14b:8','Another alternative assigns the verse to animal tithe.',mode='hypothetical')
c('c8reason','14b:8','One might allow offering blemished animal tithe because it becomes sacred without distinguishing good and bad.',mode='hypothetical')
c('c9','14b:9','The answer derives animal-tithe blemish exclusion from firstborn through the shared passing term.')
c('c10alt','14b:10','A further alternative assigns the verse to substituted sacred animals.',mode='hypothetical')
c('c10reason','14b:10','One might offer a blemished substitute because substitution sanctity attaches even with a blemish.',mode='hypothetical')
c('c11','14b:11','The answer compares the substitute to the original through it and its substitute: neither may be offered blemished.')
c('c12alt','14b:12','Rabbi Zeira proposes assigning the verse to offspring of sacred animals.',mode='hypothetical')
c('c12reason','14b:12','One might offer blemished offspring because it acquires sanctity through its mother despite the blemish.',mode='hypothetical')
c('c13tannai','14b:13','Rava replies that the school of Rabbi Yishmael already settled this through its exposition.')
c('c13substitutes','14b:13','That exposition identifies your sacred things as substitutes.')
c('c13offspring','14b:13','It identifies that you will have as offspring.')
c('c13vow','14b:13','The vows wording compares both categories to a vow offering, excluding blemished animals as with a vow.')
q('q14','14b:14','Why do animals blemished before consecration not generate substitution sanctity?')
c('c14question','14b:14','The exposition asks why good-for-bad exchange needs stating if bad-for-good exchange is already prohibited.')
c('c14good','14b:14','It reads original fitness as the basis for generating substitution sanctity.')
c('c14bad','14b:14','An animal originally unfit does not generate substitution sanctity.')
for ref,v,role in [('14b:4','Rabbi Elazar','Alternate Mishnah wording and setting'),('14b:5','Rabbi Elazar','Individual-altar prohibition derivation'),('14b:6','Anonymous objection','Firstborn alternative'),('14b:7','Anonymous answer','Explicit firstborn verse'),('14b:8','Anonymous objection','Animal-tithe alternative'),('14b:9','Anonymous answer','Firstborn-to-tithe analogy'),('14b:10','Anonymous objection','Substitute alternative'),('14b:11','Anonymous answer','Substitute-to-original analogy'),('14b:12','Rabbi Zeira','Sacred-offspring alternative'),('14b:13','Rava citing school of Rabbi Yishmael','Vow analogy for substitutes and offspring'),('14b:14','Anonymous Gemara','Originally fit/unfit substitution distinction')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
att('a4','14b:4','רבי אלעזר','speaker',['רבי אלעזר'],'Alternative reading liable')
att('a5','14b:5','רבי אלעזר','speaker',['רבי אלעזר'],'Private altar prohibition')
att('a12','14b:12',"ר' זירא",'speaker',['רבי זירא'],'Offspring alternative')
att('a13r','14b:13','רבא','speaker',['רבא'],'School exposition response')
att('a13school','14b:13','תנא דבי רבי ישמעאל','collective',['School of רבי ישמעאל'],'Vow analogy for offspring and substitutes')
for k,ref,cl,h,st,qu in [('p4','14b:4','c4',['רבי אלעזר'],'Alternative wording, not silent replacement',None),('p5','14b:5','c5rule',['רבי אלעזר'],'Individual-altar prohibition',None),('p6','14b:6','c6alt',['Anonymous Gemara'],'Rejected alternative use',None),('p8','14b:8','c8alt',['Anonymous Gemara'],'Rejected alternative use',None),('p10','14b:10','c10alt',['Anonymous Gemara'],'Rejected alternative use',None),('p12','14b:12','c12alt',['רבי זירא'],'Alternative answered by prior teaching',None),('p13','14b:13','c13vow',['School of רבי ישמעאל via רבא'],'Exclusion already derived',None),('p14g','14b:14','c14good',['Anonymous Gemara'],'Originally fit generates substitution','q14'),('p14b','14b:14','c14bad',['Anonymous Gemara'],'Originally unfit does not','q14')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,st,qu,cr['content']['conditions'])
for k,ref,a,b,rel in [('e5','14b:5','c5verse','c5rule','support'),('e6','14b:6','c6alt','c5verse','objection'),('e6r','14b:6','c6reason','c6alt','support'),('e7','14b:7','c7','c6alt','objection'),('e8','14b:8','c8alt','c5verse','objection'),('e8r','14b:8','c8reason','c8alt','support'),('e9','14b:9','c9','c8alt','objection'),('e10','14b:10','c10alt','c5verse','objection'),('e10r','14b:10','c10reason','c10alt','support'),('e11','14b:11','c11','c10alt','objection'),('e12','14b:12','c12alt','c5verse','objection'),('e12r','14b:12','c12reason','c12alt','support'),('e13','14b:13','c13vow','c12alt','objection'),('e14g','14b:14','c14good','q14','answer'),('e14b','14b:14','c14bad','q14','answer')]:edge(k,ref,a,b,rel)
add('eprior','edges',['14b:4'],dict(source_id=pre+'c4',target_id='beh.blemishtiming.20261127w3.coutside',relation='distinction',explicitness='source_explicit'));rows[-1]['links']=[pre+'c4','beh.blemishtiming.20261127w3.coutside']
for x in rows:
 if x['layer']=='claims':x['content']['scope']='RabbiElazar alternative Mishnah wording with private-altar setting. Four proposed alternative verse uses rejected through explicit sources; original Mishnah exemption preserved alongside variant. Substitution depends on original fitness, not merely present condition.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read14b4–15a20 and omission reread14b4–14. Alternate wording and setting, firstborn/tithe/substitute/offspring alternative uses and rebuttals, school attribution, and originally-fit distinction retained. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch34_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch34_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch34_receipt.json',r.encoded(out));print(r.encoded(out).decode())
