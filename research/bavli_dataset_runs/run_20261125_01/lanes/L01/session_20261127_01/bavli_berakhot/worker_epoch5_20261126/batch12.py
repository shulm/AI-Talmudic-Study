from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.exodus_wealth.20261126e5.'
assert r.sha(r.encoded(state))=='5539cbf3e3f1dd25c562f4d1bc41d7961cd26cfc6feba1c655bfce0909fb27b5'
refs=['9a:29']+['9b:'+str(i) for i in range(1,9)]
for k,rr,title in [('wealth',refs[:6],'Requested Egyptian wealth, reluctance and emptying'),('name',refs[6:8],'Divine name and future servitude'),('elijah',refs[8:],'Elijah’s doubled plea')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['School of Rabbi Yannai representing divine request','Continuation of request','Israel’s response and prisoner parable','Rabbi Ammi; alternative referents','Anonymous reasons for alternative referents','Rabbi Ammi; Resh Lakish','Divine speech represented by exposition','Moses/God dialogue','Rabbi Abbahu representing Elijah’s prayer']
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Scriptural exposition',composition='composite'))
def claim(k,rr,text,holders,cond=(),status='Reported locally',unc=()):
 evidence=rr if isinstance(rr,list) else [rr];add('c'+k,'claims',evidence,dict(proposition=text,conditions=list(cond),scope='Local aggadic exposition; preserve represented divine/human voices and alternative referents.',assertion_mode='asserted'),unc=unc);add('p'+k,'positions',evidence,dict(holder_candidates=holders,claim_id=pre+'c'+k,question_id=None,conditions=list(cond),local_status=status),['c'+k],unc=unc)
claim('29word','9a:29','The school of Rabbi Yannai interprets na as a request.',['School of Rabbi Yannai'])
claim('29request','9a:29','God asks Moses to ask Israel to request silver and gold vessels from Egypt.',['God represented by school of Rabbi Yannai'])
claim('1reason',['9a:29','9b:1'],'The purpose is that the righteous ancestor not say the servitude promise was fulfilled but the great-wealth promise was not.',['School of Rabbi Yannai'],unc=['Sentence crosses the folio boundary; righteous ancestor refers contextually to Abraham.'])
claim('2reply','9b:2','Israel responds that it is enough simply to leave.',['Israel as represented in exposition'])
claim('2parable','9b:2','A prisoner offered release tomorrow with much money asks to be released today and wants nothing.',['Anonymous parable'],status='Illustrative analogy')
claim('3','9b:3','Rabbi Ammi reads vayashilum as lending against their will.',['Rabbi Ammi'],unc=['Their has two explicit alternative referents.'])
claim('3egypt','9b:3','One version takes against their will as the Egyptians’ will.',['One anonymous version'])
claim('3israel','9b:3','Another takes it as Israel’s will.',['Other anonymous version'])
claim('4egypt','9b:4','The Egyptians interpretation cites the verse about the house-dweller dividing spoil.',['Anonymous explanation'])
claim('4israel','9b:4','The Israel interpretation explains reluctance by the burden of carrying.',['Anonymous explanation'])
claim('5grain','9b:5','Rabbi Ammi compares emptied Egypt to a trap without grain.',['Rabbi Ammi'])
claim('5fish','9b:5','Resh Lakish compares it to a depth without fish.',['Resh Lakish'],unc=['Alternative imagery; no forced binary practical dispute.'])
claim('6','9b:6','God tells Moses to say He was with Israel in this servitude and will be with them in servitude under kingdoms.',['God represented in exposition'])
claim('7moses','9b:7','Moses replies that the trouble is enough in its own time.',['Moses represented in exposition'])
claim('7god','9b:7','God then tells him to say Ehyeh has sent me to you.',['God represented in exposition'],status='Modified message after Moses’s response')
q('q8','9b:8','Rabbi Abbahu asks why Elijah says answer me twice.')
claim('8fire','9b:8','The first plea asks that heavenly fire consume everything on the altar.',['Rabbi Abbahu representing Elijah'])
claim('8thought','9b:8','The second asks that their minds be diverted so they do not call it sorcery, citing turning their heart backward.',['Rabbi Abbahu representing Elijah'])
att('a29','9a:29',"דבי ר' ינאי",'collective',['School of Rabbi Yannai'],'Exodus request interpretation')
for k,ref,surface,name in [('3','9b:3','ר אמי','רבי אמי'),('5a','9b:5','ר אמי','רבי אמי'),('5l','9b:5','ר"ל','ריש לקיש'),('8','9b:8','ר אבהו','רבי אבהו')]:att('a'+k,ref,surface,'speaker',[name],'Local interpretation')
for k,ref,a,b,rel in [('1','9b:1','c1reason','c29request','support'),('2','9b:2','c2parable','c2reply','support'),('3','9b:3','c3egypt','c3israel','distinction'),('4e','9b:4','c4egypt','c3egypt','support'),('4i','9b:4','c4israel','c3israel','support'),('5','9b:5','c5grain','c5fish','distinction'),('7m','9b:7','c7moses','c6','objection'),('7g','9b:7','c7god','c7moses','answer'),('8f','9b:8','c8fire','q8','answer'),('8t','9b:8','c8thought','q8','answer')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['id'] in [pre+'e3',pre+'e5']:x['uncertainty'].append('Alternatives in textual order, not a claim about historical rebuttal direction.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read9a29–10a32; reread core9a29–9b8 for cross-folio request sentence, prisoner parable, both forced-lending referents and reasons, two emptying images, changed divine message, and two Elijah pleas. Completed '+layer+' pass; no further finding where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch12_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch12_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch12_receipt.json',r.encoded(out));print(r.encoded(out).decode())
