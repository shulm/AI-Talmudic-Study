from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.levites.20261126w3.'
assert r.sha(r.encoded(state))=='ed06be508e962eb6919b5cc0e4e6345d3ebbe23ffca9a98982ee47f8c10004ab'
refs=['3b:15']+['4a:'+str(n) for n in range(1,14)]+['4b:1']
add('s','structure',refs,dict(title='Priestly and Levitical exemptions: competing readings and category-wide derivation',primary=True,boundary='closed',legacy_ids=[]))
voices=[('3b:15','Mishnah','Exemption and a fortiori'),('4a:1','Anonymous Gemara','Who redeemed whom question'),('4a:2','Abaye','Animal-based interpretation'),('4a:3','Rava','Wording objection'),('4a:4','Rava continuation','Clean-animal consequence objection'),('4a:5','Rava','Personal-sanctity interpretation'),('4a:6','Anonymous Gemara','Unclean-animal derivation'),('4a:7','Rav Safra to Abaye','Sheep-ownership objection'),('4a:8','Rav Safra continuation','Age objection to both'),('4a:9','Rav Safra continuation citing Rav Adda bar Ahava','Levite-woman objection'),('4a:10','Anonymous reply reporting Mar son of Rav Yosef in Rava name','Womb principle'),('4a:11','Anonymous continuation','Aaron objection'),('4a:12','Anonymous reply','Category equivalence'),('4a:13','Anonymous question citing Rabbi Yehoshua ben Levi','Priestly inclusion'),('4b:1','Anonymous question and answer','Continuity across generations')]
for ref,v,role in voices:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
c('cmish','3b:15','The Mishnah exempts priests and Levites, reasoning that if they exempted Israel’s firstborn in the wilderness, they should exempt their own.',cond=['Scope clarified by ensuing Gemara; not all clean-animal firstborn exemption'])
q('q1',('4a:1','אינהו פטרי'),'Did the Levites themselves exempt the animals?')
c('c1people',('4a:1','אדם אדם פטר'),'The objection distinguishes people redeeming people.')
c('c1animals',('4a:1','בהמה בהמה פטרה'),'It distinguishes animals redeeming animals.')
c('c2','4a:2','Abaye interprets the exemption as their animals: if Levite animals released Israelite animals in the wilderness, all the more their own.',mode='hypothetical')
q('q3','4a:3','Rava objects that the Mishnah says they themselves exempted, not their animals.')
q('q4',('4a:4','ועוד אם איתא אפילו מבכור בהמה טהורה נפטרו'),'Would Abaye’s reading not also exempt clean-animal firstborn?')
c('c4limit',('4a:4','לא נפטרו מבכור בהמה טהורה אלא מפדיון הבן ופטר חמור'),'The cited Mishnah exempts only redemption of the son and firstborn donkey, not clean-animal firstborn.')
c('c5','4a:5','Rava instead reads the Mishnah as the priests and Levites themselves: their sanctity releasing Israelite sanctity in the wilderness supports releasing their own.')
q('q6',('4a:6','אשכחן אדם בהמה טמאה מנלן'),'People are established; what is the source for unclean animals?')
c('c6included',('4a:6','כל שישנו בבכור אדם ישנו בבכור בהמה טמאה'),'The paired verse makes one subject to human-firstborn redemption also subject to unclean-animal-firstborn redemption.')
c('c6excluded',('4a:6','וכל שאינו בבכור אדם אינו בבכור בהמה טמאה'),'One outside human-firstborn redemption is also outside unclean-animal-firstborn redemption.')
q('q7','4a:7','Rav Safra asks Abaye whether only a Levite who had a sheep that released an Israelite animal should be exempt, excluding one without a sheep.')
q('q8','4a:8','Under either Abaye or Rava, should only a month-old Levite who participated in the redemption be exempt, excluding one younger than a month?')
q('q9',('4a:9','לויה לא תיפקע'),'Should a Levite woman not be exempt under that reasoning?')
c('c9',('4a:9','אמר רב אדא בר אהבה לויה שילדה בנה פטור מחמש סלעים'),'Rav Adda bar Ahava says the son born to a Levite woman is exempt from five sela redemption.',cond=['Son born to a Levite woman'])
c('c10','4a:10','The reply invokes Mar son of Rav Yosef reporting Rava: scripture makes the matter depend on the first opening of the womb.')
q('q11',('4a:11','ואהרן שלא היה באותו מנין לא ליפקע'),'Should Aaron, who was not in that count, not be exempt?')
q('q11dots',('4a:11','למה נקוד על אהרן שבחומש הפקודים'),'Why is Aaron dotted in the census passage?')
c('c11',('4a:11','שלא היה באותו מנין'),'The baraita explains the dots by Aaron not being included in that count.')
c('c12','4a:12','The verse’s Levites category equates all Levites with each other.')
q('q13',('4a:13','כהנים מנלן'),'What is the source for priests?')
c('c13count',('4a:13','בעשרים וארבעה מקומות נקראו כהנים לוים'),'Rabbi Yehoshua ben Levi says priests are called Levites in twenty-four places.')
c('c13verse',('4a:13','וזה אחד מהן (יחזקאל מד, טו) והכהנים הלוים בני צדוק'),'The priests, the Levites, the sons of Zadok is cited as one such place.')
q('q4b1',('4b:1','ולדורות מנלן'),'What is the source that the exemption applies to later generations?')
c('c4b1',('4b:1','והיו לי הלוים והיו בהווייתן יהו'),'The verse “the Levites shall be Mine” is interpreted as their remaining in that status.')
for k,ref,surface,role,cands,scope,chain in [('a2','4a:2','אביי','speaker',['אביי'],'c2',[]),('a3','4a:3','רבא','speaker',['רבא'],'Objections to Abaye',[]),('a5','4a:5','רבא','speaker',['רבא'],'c5',[]),('a7','4a:7','רב ספרא','speaker',['רב ספרא'],'Objections starting with sheepownership',[]),('a9','4a:9','רב אדא בר אהבה','quoted_authority',['רב אדא בר אהבה'],'c9',[]),('a10m','4a:10','מר בריה דרב יוסף','transmitter',['מר בריה דרב יוסף'],'c10',['מר בריה דרב יוסף','רבא']),('a10r','4a:10','רבא','quoted_authority',['רבא'],'c10',['מר בריה דרב יוסף','רבא']),('a13','4a:13','רבי יהושע בן לוי','quoted_authority',['רבי יהושע בן לוי'],'Priests calledLevites',[])]:att(k,ref,surface,role,cands,pre+scope if scope.startswith('c') else scope,chain)
for k,ref,cl,h,status,question in [('pm','3b:15','cmish',['Anonymous Mishnah'],'Exemption scope clarified by Gemara',None),('p2','4a:2','c2',['אביי'],'Interpretation challenged by Rava','q1'),('p5','4a:5','c5',['רבא'],'Replacement interpretation','q1'),('p6i','4a:6','c6included',['Anonymous Gemara'],'Paired-verse derivation','q6'),('p6e','4a:6','c6excluded',['Anonymous Gemara'],'Paired-verse derivation','q6'),('p9','4a:9','c9',['רב אדא בר אהבה'],'Quoted exemption',None),('p10','4a:10','c10',['רבא'],'Reported womb principle answering woman case','q9'),('p12','4a:12','c12',['Anonymous Gemara'],'Category-wide answer','q11'),('p13','4a:13','c13count',['רבי יהושע בן לוי'],'Quoted lexical inclusion','q13'),('p4b1','4b:1','c4b1',['Anonymous Gemara'],'Continuity derivation','q4b1')]:
 cr=next(x for x in rows if x['id']==pre+cl);pos(k,ref,cl,h,status,question,cr['content']['conditions'])
for k,ref,a,b,rel in [('e1p','4a:1','c1people','q1','support'),('e1a','4a:1','c1animals','q1','support'),('e2','4a:2','c2','q1','answer'),('e3','4a:3','q3','c2','objection'),('e4','4a:4','q4','c2','objection'),('e4s','4a:4','c4limit','q4','support'),('e5','4a:5','c5','q1','answer'),('e6i','4a:6','c6included','q6','answer'),('e6e','4a:6','c6excluded','q6','answer'),('e7','4a:7','q7','c2','objection'),('e8a','4a:8','q8','c2','objection'),('e8r','4a:8','q8','c5','objection'),('e9','4a:9','c9','q9','support'),('e10','4a:10','c10','q9','answer'),('e11','4a:11','c11','q11','support'),('e11d','4a:11','c11','q11dots','answer'),('e12','4a:12','c12','q11','answer'),('e12s','4a:12','c12','q7','answer'),('e12age','4a:12','c12','q8','answer'),('e13','4a:13','c13count','q13','answer'),('e13v','4a:13','c13verse','c13count','support'),('e4b1','4b:1','c4b1','q4b1','answer')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local scope of priest/Levite exemption. Abaye’s animal-based interpretation is challenged; Rava’s personal-sanctity reading plus paired-verse/category derivations retained. Clean-animal firstborn remains outside exemption.'
 if x['id'] in [pre+'e12s',pre+'e12age']:
  x['origin']='editorial_inference';x['content']['explicitness']='editorial_reconstruction';x['uncertainty'].append('Category-wide answer follows Aaron objection; application to preceding sheep/age objections is reconstructed from the shared inclusion rationale.')
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read3b15–4b24 continuation. Omission reread retains wording/cleananimal objections, alternative interpretations, womblineage, sheep/age/woman/Aaron scope questions, priests-as-Levites and latergenerations. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch07_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch07_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch07_receipt.json',r.encoded(out));print(r.encoded(out).decode())
