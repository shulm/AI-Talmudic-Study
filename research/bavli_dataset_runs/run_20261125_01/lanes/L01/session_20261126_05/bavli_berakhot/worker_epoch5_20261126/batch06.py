from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.moses.20261126e5.'
assert r.sha(r.encoded(state))=='d28b005f8ea9fc6449f7c8bd869f9835fac6b91e444330583be651c3fe2e4224'
refs=['7a:'+str(i) for i in range(22,37)]
for k,ns,title in [('rebuke',range(22,23),'Inward chastening and lashes'),('requests',range(23,30),'Moses’s requests, theodicy and corrected explanation'),('vision',range(30,34),'Hiding the face, rewards and divine tefillin knot'),('promise',range(34,37),'Good promises remain despite conditions')]:add('s'+k,'structure',['7a:'+str(i) for i in ns],dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={22:'Rabbi Yohanan reporting Rabbi Yose; Resh Lakish',23:'Rabbi Yohanan reporting Rabbi Yose',24:'Continuation',25:'Continuation with Moses/God represented dialogue',26:'Anonymous objection',27:'Anonymous recalled resolution',28:'Anonymous corrected interpretation of divine reply',29:'Rabbi Meir in explicit dispute',30:'Tanna reporting Rabbi Yehoshua ben Korha',31:'Rabbi Shmuel bar Nahmani reporting Rabbi Yonatan',32:'Continuation of reported reward exposition',33:'Rav Hana bar Bizna reporting Rabbi Shimon Hasida',34:'Rabbi Yohanan reporting Rabbi Yose',35:'Anonymous derivation and narrative exposition',36:'Rav Yosef and lexical analogy'}
for n in range(22,37):add('u'+str(n),'utterances',['7a:'+str(n)],dict(textual_voice=voices[n],discourse_role='Teaching, objection or exposition',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='7a:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('22y',22,'Rabbi Yohanan reports Rabbi Yose that one inward chastening is better than many lashes, citing the decision to return to the first husband.',['Rabbi Yose'])
claim('22l',22,'Resh Lakish says it is better than a hundred lashes, citing rebuke entering the understanding person more than striking a fool a hundred times.',['Resh Lakish'],unc=['Different comparative formulations need not mean denial of the other’s lower bound.'])
claim('23all',23,'Rabbi Yohanan reports Rabbi Yose that Moses requested three things and all were granted.',['Rabbi Yose'],status='Reported position opposed by Rabbi Meir in7a29')
claim('23israel',23,'Moses requested that the Divine Presence rest on Israel and was granted it.',['Rabbi Yose via Rabbi Yohanan'])
claim('24',24,'He requested that the Divine Presence not rest on idolaters and was granted it.',['Rabbi Yose via Rabbi Yohanan'])
claim('25ways',25,'He requested to know God’s ways and was granted it.',['Rabbi Yose via Rabbi Yohanan'],status='Third request contested by Rabbi Meir')
q('q25','7a:25','Moses asks why some righteous people prosper and others suffer, while some wicked people prosper and others suffer.')
for k,text in [('good','The initial reply assigns righteous prosperity to a righteous child of a righteous parent.'),('bad','The initial reply assigns righteous suffering to a righteous child of a wicked parent.'),('wickedgood','The initial reply assigns wicked prosperity to a wicked child of a righteous parent.'),('wickedbad','The initial reply assigns wicked suffering to a wicked child of a wicked parent.')]:claim('25'+k,25,text,['God as represented in initial exposition'],status='Initial interpretation replaced at7a28')
q('q26','7a:26','Can a righteous person’s suffering be explained by a wicked parent, given the reconciled verses about visiting fathers’ sins and children not dying for fathers?')
claim('27hold',27,'The prior reconciliation applies visiting parental sin when children hold their ancestors’ deeds.',['Anonymous Gemara'],cond=['Children retain ancestors’ conduct'])
claim('27not',27,'The verse against children dying for fathers applies when they do not hold their ancestors’ deeds.',['Anonymous Gemara'],cond=['Children do not retain ancestors’ conduct'])
for k,text in [('righteousgood','The corrected reply identifies the prosperous righteous person as wholly righteous.'),('righteousbad','The corrected reply identifies the suffering righteous person as not wholly righteous.'),('wickedgood','The corrected reply identifies the prosperous wicked person as not wholly wicked.'),('wickedbad','The corrected reply identifies the suffering wicked person as wholly wicked.')]:claim('28'+k,28,text,['God as represented in corrected exposition'],status='Replacement interpretation of the reply')
claim('29count',29,'Rabbi Meir says two requests were granted and one was not.',['Rabbi Meir'],status='Explicit opposition to the three-granted report',unc=['The third request about divine ways is the locally disputed one.'])
claim('29grace',29,'I shall favor whom I favor and show mercy to whom I show mercy are read as applying even to someone unworthy.',['Rabbi Meir'])
claim('30',30,'Rabbi Yehoshua ben Korha’s reported interpretation has God tell Moses: when I wanted you did not; now that you want I do not.',['Rabbi Yehoshua ben Korha'],status='Critical interpretation of Moses’s earlier refusal')
claim('31',31,'Rabbi Shmuel bar Nahmani reports Rabbi Yonatan that Moses merited three things for three actions.',['Rabbi Yonatan'],status='Explicit alternative to critical interpretation')
claim('32face',32,'For hiding his face Moses merited a radiant countenance.',['Rabbi Yonatan via Rabbi Shmuel bar Nahmani'])
claim('32fear',32,'For being afraid he merited others being afraid to approach him.',['Rabbi Yonatan via Rabbi Shmuel bar Nahmani'])
claim('32look',32,'For refraining from looking he merited beholding the form of God.',['Rabbi Yonatan via Rabbi Shmuel bar Nahmani'],unc=['Refraining is supplied from the cited Moses hiding/afraid-to-look narrative; literal local citation is מהביט.'])
claim('33',33,'Rav Hana bar Bizna reports Rabbi Shimon Hasida that seeing God’s back means God showed Moses the knot of tefillin.',['Rabbi Shimon Hasida'])
claim('34',34,'Rabbi Yohanan reports Rabbi Yose that God never retracts a favorable statement even if conditional.',['Rabbi Yose'],cond=['Favorable divine statement','Even conditional'])
q('q35','7a:35','From where is this learned?')
claim('35promise',35,'The example is God’s promise to make Moses a mighty nation in connection with destroying Israel.',['Anonymous exposition'])
claim('35cancel',35,'Moses prayed concerning the matter and it was annulled, yet the promise was fulfilled in his descendants.',['Anonymous exposition'],unc=['Cancellation concerns the destructive plan, not erasure of the favorable promise.'])
claim('35descendants',35,'The genealogy of Moses through Eliezer and Rehabiah, whose descendants multiplied greatly, is cited as fulfillment.',['Anonymous exposition'])
claim('36number',36,'Rav Yosef teaches that they exceeded six hundred thousand.',['Rav Yosef'])
claim('36proof',36,'The explanation connects the multiplication wording for Rehabiah’s descendants with Israel’s multiplication.',['Expository lexical analogy'])
for n in [22,23,34]:att('a'+str(n),'7a:'+str(n),"יוחנן משום ר' יוסי" if n!=22 else 'יוחנן משום רבי יוסי','transmitter',['רבי יוחנן'],'Teaching of Rabbi Yose',chain=['רבי יוחנן','רבי יוסי'])
att('a22l','7a:22','ריש לקיש','speaker',['ריש לקיש'],pre+'c22l')
att('a29','7a:29',"ר' מאיר",'speaker',['רבי מאיר'],'Two requests granted')
att('a30','7a:30',"ר' יהושע בן קרחה",'quoted_authority',['רבי יהושע בן קרחה'],pre+'c30')
att('a31','7a:31',"ר' שמואל בר נחמני א"+'"'+"ר יונתן",'transmitter',['רבי שמואל בר נחמני'],'Three rewards',chain=['רבי שמואל בר נחמני','רבי יונתן'])
att('a33','7a:33','רב חנא בר ביזנא','transmitter',['רב חנא בר ביזנא'],pre+'c33',chain=['רב חנא בר ביזנא','רבי שמעון חסידא'])
att('a36','7a:36','רב יוסף','speaker',['רב יוסף'],pre+'c36number')
for k,n,a,b,rel in [('22',22,'c22y','c22l','distinction'),('26',26,'q26','c25bad','objection'),('27h',27,'c27hold','q26','support'),('27n',27,'c27not','q26','support'),('29',29,'c29count','c23all','objection'),('29s',29,'c29grace','c29count','support'),('31',31,'c31','c30','distinction'),('32f',32,'c32face','c31','support'),('32fear',32,'c32fear','c31','support'),('32l',32,'c32look','c31','support'),('35',35,'c35descendants','q35','answer'),('35p',35,'c35promise','c34','support'),('35c',35,'c35cancel','c34','support'),('36',36,'c36number','c35descendants','support'),('36p',36,'c36proof','c36number','support')]:edge('e'+k,'7a:'+str(n),a,b,rel)
for old,new in [('good','righteousgood'),('bad','righteousbad'),('wickedgood','wickedgood'),('wickedbad','wickedbad')]:
 edge('e28'+new,'7a:28','c28'+new,'c25'+old,'correction');edge('e28answer'+new,'7a:28','c28'+new,'q25','answer')
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local reported interpretations of divine ways and Moses; initial explanations remain preserved as replaced, not final assertions. No contemporary judgment of sufferers is inferred.'
 if x['id']==pre+'e31':x['uncertainty'].append('Explicit ופליגא marks opposed appraisal. Arrow follows textual presentation, not historical interaction.')
 if x['id']==pre+'e22':x['uncertainty'].append('Difference in formulations, not proof of mutually exclusive numeric bounds.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read7a22–7b28; reread core7a22–36 for three requests, four initial cases explicitly replaced by four corrected cases, parental conduct qualification, Meir dispute, opposed appraisal of hiding face, three rewards, conditional promise and genealogy. Completed '+layer+' pass; no additional record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch06_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch06_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch06_receipt.json',r.encoded(out));print(r.encoded(out).decode())
