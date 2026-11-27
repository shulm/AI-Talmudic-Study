import json,pathlib,hashlib
D=pathlib.Path(__file__).parent;J=pathlib.Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_arakhin');job=json.loads((J/'JOB.json').read_text());owner=json.loads((J/'OWNER.json').read_text());assert owner=={'epoch':1,'owner':'/root/lead_l01_l03'};assert not (J/'CURRENT.json').exists()
raw=pathlib.Path(r'F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Kodashim/Arakhin/Hebrew/Wikisource Talmud Bavli.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==job['source_sha256'];inv=json.loads((J/'source_inventory.json').read_text(encoding='utf8'));segments={int(r['ref'].split(':')[-1]):r for r in inv if r['ref'].startswith('Arakhin 2a:')}
rows=[];prefix='ar.e1.b001.'
def ev(n,quote=None):
 s=segments[n];q=s['text'] if quote is None else quote;a=s['text'].index(q);return dict(segment_id=s['id'],start_char=a,end_char=a+len(q),quote=q)
def add(id,layer,ns,content,links=[],unc=[]):
 es=[ev(n) if isinstance(n,int) else ev(*n) for n in ns];r=dict(id=prefix+id,layer=layer,evidence=es,content=content,origin='source_paraphrase',uncertainty=unc,links=[prefix+x for x in links]);rows.append(r);return id
for id,ns,title in [('s1',range(1,4),'Mishnah: actors and subjects of fixed valuations and monetary-value vows'),('s2',range(4,8),'Inclusiveness of fixed valuations: near-adult declarant and persons with no market value'),('s3',range(8,11),'Inclusiveness of monetary-value vow subjects: infant below one month')]:add(id,'structure',ns,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['anonymous Mishnah']*3+['anonymous Gemara']*7
roles=['Four capacities across listed groups','Tumtum/androgynos capacities and exclusion','Lack of daat distinguishes actors from subjects','Question and near-adult inclusion','Question and disfigured/skin-diseased inclusion','Rejected monetary-value analogy','Scriptural rebuttal','Nodrin question redirected to nidrin','Explicitly listed candidates challenged','More candidate objections and final infant inclusion']
for n,(voice,role) in enumerate(zip(voices,roles),1):add(f'u{n}','utterances',[n],dict(textual_voice=voice,discourse_role=role,composition='composite'))
def claim(id,ns,text,mode='asserted',conditions=[],status='asserted locally',holder=None,unc=[]):
 add(id,'claims',ns,dict(proposition=text,conditions=conditions,scope='Arakhin opening: fixed Torah valuation (erekh) distinguished from monetary-value vow (damim); source categories retained',assertion_mode=mode),unc=unc)
 voice=holder or ('anonymous Mishnah' if ns[0]<=3 else 'anonymous Gemara')
 add(id+'.pos','positions',ns,dict(holder_candidates=[voice],claim_id=prefix+id,question_id=None,conditions=conditions,local_status=status),[id],unc)
def q(id,ns,text):add(id,'questions',ns,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(id,ns,a,b,rel):add(id,'edges',ns,dict(source_id=prefix+a,target_id=prefix+b,relation=rel,explicitness='source_explicit'),[a,b])
cohort='Priests, Levites, Israelites, women and slaves'
for id,text in [('c1',cohort+' may declare a fixed statutory valuation (מעריכין).'),('c2',cohort+' may be subjects of a fixed statutory valuation (נערכין).'),('c3',cohort+' may make monetary-value vows (נודרין).'),('c4',cohort+' may be subjects of monetary-value vows (נידרין).')]:claim(id,[1],text)
for id,text in [('c5','Tumtum and androgynos may make monetary-value vows.'),('c6','Tumtum and androgynos may be subjects of monetary-value vows.'),('c7','Tumtum and androgynos may declare fixed valuations.'),('c8','Tumtum and androgynos are not subjects of fixed valuations.'),('c9','A subject of fixed valuation must be definitely male or definitely female.')]:claim(id,[2],text)
edge('e1',[2],'c9','c8','support')
for id,text in [('c10','Heresh, shoteh and minor may be subjects of monetary-value vows.'),('c11','Heresh, shoteh and minor may be subjects of fixed valuations.'),('c12','Heresh, shoteh and minor do not make monetary-value vows.'),('c13','Heresh, shoteh and minor do not declare fixed valuations.'),('c14','The stated reason for exclusion as declarants is that they lack daat.')]:claim(id,[3],text,unc=['Technical source categories preserved; no medical or modern legal identity equivalence inferred.'])
edge('e2',[3],'c14','c12','support');edge('e3',[3],'c14','c13','support')
q('q1',[4],'What does הכל מעריכין include?');claim('c15',[4],'The inclusive wording admits a מופלא סמוך לאיש as a fixed-valuation declarant.',conditions=['מופלא סמוך לאיש'],status='Specific inclusion qualifying the general minor exclusion; no unstated exact age added');edge('e4',[4],'c15','q1','answer');edge('e5',[3,4],'c15','c13','qualification')
q('q2',[5],'What does נערכין include?');claim('c16',[5],'The inclusive wording admits a disfigured person (מנוול) and one afflicted with boils (מוכה שחין) as subjects of fixed valuation.');edge('e6',[5],'c16','q2','answer')
claim('c17',[6],'The proposed reading of נדר בערכך would make monetary-value eligibility a prerequisite for fixed-valuation eligibility.',mode='rejected',status='סד"א hypothesis displaced by קמ"ל in2a:7')
claim('c18',[6],'Under that proposed reading, one having no monetary value would have no fixed valuation.',mode='rejected',status='Rejected negative implication, not maintained ruling',conditions=['Person has no monetary value'])
claim('c19',[7],'נפשות is interpreted inclusively: any person, rebutting the proposed restriction to monetary-value eligibility.',status='Local response to rejected hypothesis; retains Mishnah explicit exclusions')
edge('e7',[6,7],'c19','c17','correction');edge('e8',[6,7],'c19','c18','correction');edge('e9',[5,6,7],'c19','c16','support')
q('q3',[8],'What additional case does נודרין include?');claim('c20',[8],'The discussion replies that נידרין was needed; the formulation נודרין is not assigned a separate additional subject here.');edge('e10',[8],'c20','q3','answer')
q('q4',[9],'What additional case does נידרין include?')
claim('c21',[9],'Tumtum and androgynos cannot serve as a previously unmentioned inclusion because they are explicitly taught.');claim('c22',[9],'Heresh, shoteh and minor likewise are explicitly taught, so do not supply a previously unmentioned case.')
claim('c23',[10],'A child below one month is also explicitly taught, creating the same apparent redundancy.');claim('c24',[10],'An עובד כוכבים is also explicitly taught, creating the same apparent redundancy.',unc=['Preserve printed עובד כוכבים; no broader identity substitution.'])
claim('c25',[10],'The final answer nevertheless identifies the subject below one month as the inclusion in נידרין.',conditions=['Age below one month'],status='Local conclusion about monetary-value vow subjects, not fixed-valuation subjects')
claim('c26',[10],'תני והדר מפרש explains the apparent redundancy: first states the general inclusion, then explains it explicitly.')
edge('e11',[10],'c25','q4','answer');edge('e12',[10],'c26','c23','answer');edge('e13',[10],'c26','c25','support')
# No named teacher or transmission occurs in the10core segments; anonymous role rows preserve this fact.
add('a1','attributions',range(1,4),dict(surface='מתני׳',role='anonymous',candidates=[],scope='Anonymous Mishnah, no named teacher in opening',transmission_chain=[]))
add('a2','attributions',range(4,11),dict(surface='גמ׳',role='anonymous',candidates=[],scope='Anonymous explanations, challenges and responses; no named transmitter in core',transmission_chain=[]))
coverage=[]
for n in range(1,11):
 sid=segments[n]['id']
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in rows if r['layer']==layer and any(e['segment_id']==sid for e in r['evidence'])]
  rationale='Original source reread; actor/subject and erekh/damim distinctions, minor exception, rejected premise, listed candidates and final infant answer checked. Context2a:11–2b:3 begins separate heir discussion; no core continuation omitted.' if layer=='reconciliation' else ('Evidence-bearing rows for this original segment.' if ids else 'Read this segment: no separate explicit question or argument relation requiring a record in this layer; do not invent one.')
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
p=dict(schema_version='2.0.0-production',tractate='Arakhin',owner=owner['owner'],epoch=owner['epoch'],source_sha256=job['source_sha256'],protocol_sha256=job['protocol_sha256'],schema_sha256=job['schema_sha256'],execution=dict(route='interactive_agent',agent_id='/root/blind_review',model_id=None),records=rows,coverage=coverage,open_tails=[])
with (D/'proposal.json').open('x',encoding='utf8') as f:json.dump(p,f,ensure_ascii=False,indent=2)
print('records',len(rows),'proposal_sha256',hashlib.sha256((D/'proposal.json').read_bytes()).hexdigest())
