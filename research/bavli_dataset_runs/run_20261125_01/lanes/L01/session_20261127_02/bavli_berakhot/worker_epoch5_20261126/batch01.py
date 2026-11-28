from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.illness.20261126e5.'
assert r.sha(r.encoded(state))=='97f9f50aa253c5e3c9dd6760f9f21979358fb9e66f45098990bfdb12b683d00f'
refs=['5b:'+str(i) for i in range(4,21)]
for k,ns,title in [('cat',range(4,10),'Lesions and children: atonement versus sufferings of love'),('vis',range(10,17),'Illness visits, refusals of suffering and assistance'),('wine',range(17,21),'Rav Huna wine loss and restitution to tenant')]:add('s'+k,'structure',['5b:'+str(i) for i in ns],dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices={4:'Rabbi Yohanan',5:'Anonymous objection citing baraita',6:'Anonymous first answer',7:'Anonymous alternative answer',8:'Anonymous alternative answer',9:'Anonymous discussion citing Rabbi Yohanan',10:'Narrator; Rabbi Yohanan and Rabbi Hiyya bar Abba',11:'Narrator; Rabbi Hanina and Rabbi Yohanan',12:'Anonymous question',13:'Anonymous answer',14:'Narrator; Rabbi Yohanan addressing Rabbi Eliezer',15:'Rabbi Eliezer and Rabbi Yohanan; narrator',16:'Rabbi Yohanan and Rabbi Eliezer; narrator',17:'Narrator; Rav Huna and visitors with alternative identity',18:'Rav Huna and visitors',19:'Rav Huna',20:'Visitors, Rav Huna and alternative narrators'}
for n in range(4,21):add('u'+str(n),'utterances',['5b:'+str(n)],dict(textual_voice=voices[n],discourse_role='Question' if n==12 else 'Composite local discussion or narrative',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='5b:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('4',4,'Rabbi Yohanan excludes lesions and children from sufferings of love.',['רבי יוחנן'],unc=['Children is elliptical; 5b9 distinguishes never having children from children who died.'])
q('q5','5b:5','Are lesions not sufferings of love, given the baraita describing any of the four appearances as an altar of atonement?')
claim('5',5,'The cited baraita calls any of the four lesion appearances an altar of atonement.',['Unnamed baraita'])
claim('6',6,'The first answer allows atonement while denying classification as sufferings of love.',['Anonymous Gemara'],status='First resolution')
claim('7',7,'An alternative resolves the apparent conflict by distinguishing us and them.',['Anonymous Gemara'],status='Alternative resolution',unc=['The bare הא לן והא להו does not itself name regions or map each predicate. No commentary supplied.'])
claim('8',8,'Another alternative distinguishes private and public cases.',['Anonymous Gemara'],status='Alternative resolution',unc=['The source does not explicitly assign each predicate to the private/public side. Do not collapse alternative answers into cumulative conditions.'])
q('q9','5b:9','What exclusion concerning children is meant, given Yohanan’s statement about the bone of his tenth child?')
claim('9hyp',9,'The discussion considers the excluded case as having children who died.',['Anonymous Gemara'],status='Rejected candidate construal')
claim('9bone',9,'Rabbi Yohanan is quoted as referring to this bone of his tenth child.',['רבי יוחנן'])
claim('9answer',9,'The answer distinguishes never having children from having children who died.',['Anonymous Gemara'],status='Distinction resolving objection',unc=['Mapping exclusion to never having children is contextual inference; the literal הא/הא clauses are elliptical.'])
for n,patient,visitor in [(10,'Rabbi Hiyya bar Abba','Rabbi Yohanan'),(11,'Rabbi Yohanan','Rabbi Hanina'),(16,'Rabbi Eliezer','Rabbi Yohanan')]:
 q('q'+str(n),'5b:'+str(n),'The visitor asks whether sufferings are dear to '+patient+'.')
 claim(str(n)+'refuse',n,patient+' rejects both the sufferings and their reward.',[patient],status='Narrative personal response, not a universal denial of reward')
 claim(str(n)+'help',n,visitor+' asks for the patient’s hand; the patient gives it and the visitor raises him.',[visitor,patient],status='Narrative action')
q('q12','5b:12','Why does Rabbi Yohanan not raise himself?')
claim('13',13,'The answer says a prisoner cannot free himself from prison.',['Anonymous Gemara'])
claim('14scene',14,'Yohanan visits ill Rabbi Eliezer in a dark room, exposes his arm and light falls; he sees Eliezer crying.',['Anonymous narrator'],status='Narrative')
q('q14','5b:14','Why is Rabbi Eliezer crying?')
claim('14torah',14,'If tears concern insufficient Torah study, Yohanan cites that much and little are alike provided the heart is directed toward Heaven.',['רבי יוחנן'],cond=['Suggested reason: insufficient Torah study','Intention toward Heaven'],status='Conditional consolation, not identified cause of tears')
claim('14food',14,'If tears concern sustenance, Yohanan says not everyone merits two tables.',['רבי יוחנן'],cond=['Suggested reason: sustenance'],status='Conditional consolation')
claim('14children',14,'If tears concern children, Yohanan refers to the bone of his tenth child.',['רבי יוחנן'],cond=['Suggested reason: children'],status='Conditional consolation')
claim('15beauty',15,'Eliezer identifies his cause of crying as this beauty that will decay in dust.',['Rabbi Eliezer'])
claim('15agree',15,'Yohanan agrees that this warrants crying, and both cry.',['רבי יוחנן','Anonymous narrator'],status='Reply and narrative response')
claim('17loss',17,'Four hundred barrels of Rav Huna’s wine turn sour and sages visit.',['Anonymous narrator'],status='Narrative',unc=['Visitors reported as Rav Yehuda brother of Rav Sala the pious and sages, alternatively Rav Adda bar Ahava and sages.'])
claim('17examine',17,'The visitors tell Rav Huna to examine his deeds.',['Visitors: alternative identities unresolved'])
q('q17h','5b:17','Rav Huna asks whether they suspect him.')
q('q17v','5b:17','The visitors ask whether God is suspected of judgment without justice.')
claim('18request',18,'Rav Huna asks anyone who heard a matter against him to say it.',['רב הונא'])
claim('18charge',18,'The visitors report that he does not give vine branches to his tenant.',['Visitors: alternative identities unresolved'])
claim('19defense',19,'Rav Huna says the tenant leaves him nothing and steals it all.',['רב הונא'],status='Reported defense, not independently established fact')
claim('20reply',20,'The visitors apply the proverb that stealing after a thief tastes of theft.',['Visitors: alternative identities unresolved'],status='Reply rejecting retaliatory withholding')
claim('20accept',20,'Rav Huna accepts giving the tenant the branches.',['רב הונא'],status='Accepted corrective undertaking')
claim('20wine',20,'One version says the vinegar became wine again.',['One anonymous version'],status='Alternative narrative ending')
claim('20price',20,'Another version says vinegar rose in price and sold for the price of wine.',['Other anonymous version'],status='Alternative narrative ending')
att('a4','5b:4','ר יוחנן','speaker',['רבי יוחנן'],pre+'c4')
att('a5','5b:5','והתניא','anonymous',[],'Cited baraita on atonement')
att('a9','5b:9','ר יוחנן','quoted_authority',['רבי יוחנן'],pre+'c9bone')
for n,surfaces in [(10,['רבי חייא בר אבא',"ר' יוחנן"]),(11,["ר' יוחנן", "ר' חנינא"]),(14,['רבי אליעזר','רבי יוחנן']),(17,['רב הונא','רב יהודה אחוה דרב סלא חסידא','רב אדא בר אהבה'])]:
 for i,surface in enumerate(surfaces):att('a'+str(n)+'_'+str(i),'5b:'+str(n),surface,'speaker',[surface],'Narrative participant; dialogue roles recorded in claims',unc=['Alternative visitor report, not simultaneous visitors.'] if n==17 and i>0 else [])
for k,n,a,b,rel in [('5',5,'c5','c4','objection'),('6',6,'c6','q5','answer'),('7',7,'c7','q5','answer'),('8',8,'c8','q5','answer'),('9b',9,'c9bone','c9hyp','objection'),('9a',9,'c9answer','q9','answer'),('13',13,'c13','q12','answer'),('15',15,'c15beauty','q14','answer'),('15a',15,'c15agree','c15beauty','support'),('18',18,'c18charge','c18request','answer'),('19',19,'c19defense','c18charge','objection'),('20r',20,'c20reply','c19defense','objection'),('20a',20,'c20accept','c20reply','answer'),('20v',20,'c20wine','c20price','distinction')]:edge('e'+k,'5b:'+str(n),a,b,rel)
for n in [10,11,16]:edge('e'+str(n),'5b:'+str(n),'c'+str(n)+'refuse','q'+str(n),'answer')
for x in rows:
 if x['id']==pre+'e20v':x['uncertainty'].append('Mutually alternative reports; arrow follows textual order, not historical causal direction.')
 if x['id'] in [pre+'c14scene',pre+'c15beauty',pre+'c16refuse']:x['uncertainty'].append('Printed Rabbi Eliezer retained; not silently changed to Eleazar.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read 5a9 through5b27; reread 5b4–20 for omissions. Preserve alternative resolutions and narratives, atonement/category distinction, personal refusal rather than universal denial, conditional consolation, alternative visitors/endings. Completed '+layer+' pass; no further record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch01_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch01_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch01_receipt.json',r.encoded(out));print(r.encoded(out).decode())
