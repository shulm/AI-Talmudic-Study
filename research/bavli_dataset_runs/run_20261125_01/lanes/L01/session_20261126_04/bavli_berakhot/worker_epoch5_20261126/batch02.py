from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.prayer_presence.20261126e5.'
assert r.sha(r.encoded(state))=='1b80d479a386244c6c733f6c73ecf14a679fb94e5f6e30e86665d989544444ee'
refs=['5b:'+str(i) for i in range(21,28)]+['6a:'+str(i) for i in range(1,17)]
for k,rr,title in [('bed',refs[:4],'Abba Benjamin’s prayer and bed arrangement'),('wait',refs[4:8],'Waiting for a prayer companion and reward'),('demons',refs[8:13],'Reports about unseen damaging beings'),('synagogue',refs[13:14],'Synagogue prayer'),('presence',refs[14:],'Divine presence in prayer, judgment and Torah study')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Baraita of Abba Benjamin; anonymous discussion; Rav Yehuda reporting Rav, alternatively Rabbi Yehoshua ben Levi','Repeated Abba Benjamin clause','Rabbi Hama bar Hanina reporting Rabbi Yitzhak','Rav Nahman bar Yitzhak','Baraita of Abba Benjamin','Baraita continuation','Anonymous question','Rabbi Yose bar Hanina','Baraita of Abba Benjamin','Abaye','Rav Huna','Rava','Anonymous procedural report and narrative','Baraita of Abba Benjamin','Ravin bar Rav Adda reporting Rabbi Yitzhak','Continuation of reported teaching','Continuation of reported teaching','Continuation of reported teaching','Anonymous question and Rav Ashi','Continuation of reported teaching','Anonymous question and distinction','Anonymous question and rejected supposition','Anonymous question and distinction']
assert len(voices)==len(refs)
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Composite teaching, question or narrative',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('21prayer','5b:21','Abba Benjamin says he was concerned all his days for prayer to be before his bed.',['Abba Benjamin'],unc=['Literal לפני מטתי is reinterpreted in continuation; not final spatial instruction.'])
claim('21bed','5b:21','His second concern is that his bed be between north and south.',['Abba Benjamin'])
q('q21','5b:21','What does before my bed mean?')
claim('21literal','5b:21','The discussion considers literally in front of the bed.',['Anonymous Gemara'],status='Rejected proposed interpretation')
claim('21wall','5b:21','Rav Yehuda reporting Rav, alternatively Rabbi Yehoshua ben Levi, teaches that nothing should intervene between one praying and the wall, citing Hezekiah turning his face to the wall.',['Rav','Rabbi Yehoshua ben Levi'],status='Alternative attribution, unresolved',unc=['Do not present Rav and Rabbi Yehoshua ben Levi as joint speakers; the syntax reports an alternative.'])
claim('21near','5b:21','The answer replaces before my bed with adjacent to my bed.',['Anonymous Gemara'],status='Accepted reinterpretation',unc=['Temporal adjacency to rising is not spelled out in the raw wording סמוך למטתי; do not insert commentary as literal source.'])
claim('22','5b:22','The discussion repeats the north–south bed concern.',['Abba Benjamin'],status='Repeated lemma, not a new distinct teaching')
claim('23','5b:23','Rabbi Hama bar Hanina reports Rabbi Yitzhak that placing a bed north–south brings male children, citing Psalm17.',['Rabbi Yitzhak'],cond=['Bed placed between north and south'])
claim('24','5b:24','Rav Nahman bar Yitzhak adds that his wife does not miscarry, connecting filling the womb and completed days.',['Rav Nahman bar Yitzhak'],cond=['Same bed arrangement as preceding teaching'])
claim('25','5b:25','Abba Benjamin says when two enter to pray and the first finishes and leaves without waiting, his prayer is torn before him.',['Abba Benjamin'],cond=['Two entered to pray','One finishes first','Leaves without waiting'])
claim('26','5b:26','He additionally causes the Divine Presence to depart from Israel; tzur is interpreted as God.',['Abba Benjamin, continuation'],cond=['Leaving without waiting as in preceding teaching'])
q('q27','5b:27','What reward follows if he waits?')
claim('1','6a:1','Rabbi Yose bar Hanina says the one who waits merits the blessings of Isaiah48: peace like a river, righteousness like sea waves, and offspring like sand.',['Rabbi Yose bar Hanina'],cond=['Waits for prayer companion'])
claim('2','6a:2','Abba Benjamin says no creature could stand before the damaging beings if the eye were permitted to see them.',['Abba Benjamin'],cond=['Hypothetical permission for sight'])
claim('3','6a:3','Abaye says they are more numerous than humans and surround them like a ridge around a garden bed.',['Abaye'])
claim('4','6a:4','Rav Huna says each person has a thousand on the left and ten thousand on the right.',['Rav Huna'])
for k,quote,text in [('crowd','האי דוחקא דהוי בכלה מנייהו הוי','Rava attributes crowding at the kallah gathering to them.'),('knees','הני ברכי דשלהי מנייהו','He attributes weary knees to them.'),('garments','הני מאני דרבנן דבלו מחופיא דידהו','He attributes worn scholars’ garments to their rubbing.'),('feet','הני כרעי דמנקפן מנייהו','He attributes struck feet to them.')]:claim('5'+k,('6a:5',quote),text,['Rava'])
claim('6tracks','6a:6','An anonymous report describes sifting ashes around the bed to find rooster-like tracks in the morning as a way of knowing of the beings.',['Anonymous procedural report'],cond=['Desire to know of them'],status='Historical source prescription, not endorsed practical guidance')
claim('6sight','6a:6','A separate anonymous procedure for seeing them uses the burnt and ground placenta of a black firstborn female cat born of a black firstborn mother, placed in the eyes.',['Anonymous procedural report'],cond=['Desire to see them'],status='Historical source prescription, not endorsed practical guidance')
claim('6secure','6a:6','The report calls for an iron container and iron seal lest they steal the material, and sealing its opening to avoid harm.',['Anonymous procedural report'],status='Historical precaution within the report',unc=['The referent of פומיה is not expanded beyond its opening; no external interpretation supplied.'])
claim('6harm','6a:6','Rav Bibi bar Abaye did this, saw, and was harmed.',['Anonymous narrator'],status='Narrative outcome')
claim('6heal','6a:6','The sages prayed for mercy for him and he recovered.',['Anonymous narrator'],status='Narrative outcome')
claim('7','6a:7','Abba Benjamin says a person’s prayer is heard only in the synagogue, interpreting the place of song as the place of prayer.',['Abba Benjamin'])
for k,ref,text in [('8','6a:8','God is present in the synagogue, citing God stands in the divine congregation.'),('9','6a:9','The Divine Presence is with ten praying, citing the same verse.'),('10','6a:10','The Divine Presence is with three sitting in judgment, citing in the midst of judges He judges.'),('11','6a:11','The Divine Presence is with two sitting and engaging in Torah, citing those who fear God speaking one to another.'),('13','6a:13','The Divine Presence is even with one sitting and engaging in Torah, citing I shall come to you and bless you.')]:
 q('q'+k,ref,'What verse establishes that '+text.split(', citing')[0].lower()+'?');claim(k,ref,text,['Rabbi Yitzhak via Ravin bar Rav Adda'],unc=['The speaker attribution is inherited from 6a8; 6a12 is an intervening named teaching.'] if k=='13' else [])
q('q12','6a:12','What does and those who think of His name mean?')
claim('12','6a:12','Rav Ashi says Scripture credits one who intended to perform a mitzvah but was prevented as if it had been done.',['Rav Ashi'],cond=['Intended a mitzvah','Prevented and did not perform it'])
q('q14','6a:14','If the presence accompanies one, why state the case of two?')
claim('14','6a:14','The words of two are written in the book of remembrance; the words of one are not.',['Anonymous Gemara'],status='Distinction explaining separate cases')
q('q15','6a:15','If it accompanies two, why state the case of three?')
claim('15hyp','6a:15','One might think adjudication is merely peace-making and the Divine Presence does not come.',['Anonymous Gemara'],status='Rejected supposition')
claim('15answer','6a:15','The answer teaches that adjudication too is Torah.',['Anonymous Gemara'])
q('q16','6a:16','If it accompanies three, why state the case of ten?')
claim('16','6a:16','For ten, the Presence arrives before them; for three, only when they sit.',['Anonymous Gemara'],status='Distinction in timing')
att('a21ab','5b:21','אבא בנימין','speaker',['אבא בנימין'],'Two lifelong concerns')
att('a21chain','5b:21','רב יהודה אמר רב ואיתימא ריב"ל','quoted_authority',['רב','רבי יהושע בן לוי'],pre+'c21wall',chain=['רב יהודה','רב'],unc=['Chain describes first version only; Rabbi Yehoshua ben Levi is alternative.'])
att('a23','5b:23','חמא ברבי חנינא אמר רבי יצחק','transmitter',['רבי חמא ברבי חנינא'],'Bed arrangement assurance',chain=['רבי חמא ברבי חנינא','רבי יצחק'])
att('a24','5b:24','רב נחמן בר יצחק','speaker',['רב נחמן בר יצחק'],pre+'c24')
att('a25','5b:25','אבא בנימין','speaker',['אבא בנימין'],'Waiting teaching')
att('a1','6a:1',"ר' יוסי ברבי חנינא",'speaker',['רבי יוסי ברבי חנינא'],pre+'c1')
for k,ref,surface,name in [('2','6a:2','אבא בנימין','אבא בנימין'),('3','6a:3','אביי','אביי'),('4','6a:4','רב הונא','רב הונא'),('5','6a:5','רבא','רבא'),('7','6a:7','אבא בנימין','אבא בנימין'),('12','6a:12','רב אשי','רב אשי')]:att('a'+k,ref,surface,'speaker',[name],'Local teaching')
att('a6','6a:6','רב ביבי בר אביי','speaker',['רב ביבי בר אביי'],'Narrative actor, not attributed author of prescription')
att('a8trans','6a:8','רבין בר רב אדא','transmitter',['רבין בר רב אדא'],'Presence teaching chain',chain=['רבין בר רב אדא','רבי יצחק'])
att('a8auth','6a:8','ר יצחק','quoted_authority',['רבי יצחק'],'Presence teaching chain',chain=['רבין בר רב אדא','רבי יצחק'])
for k,ref,a,b,rel in [('21ob','5b:21','c21wall','c21literal','objection'),('21an','5b:21','c21near','q21','answer'),('23','5b:23','c23','c22','support'),('24','5b:24','c24','c23','qualification'),('26','5b:26','c26','c25','qualification'),('1','6a:1','c1','q27','answer'),('12','6a:12','c12','q12','answer'),('14','6a:14','c14','q14','answer'),('15','6a:15','c15answer','q15','answer'),('15h','6a:15','c15answer','c15hyp','objection'),('16','6a:16','c16','q16','answer')]:edge('e'+k,ref,a,b,rel)
for k in ['8','9','10','11','13']:edge('e'+k,'6a:'+k,'c'+k,'q'+k,'answer')
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local reported teachings; conditional cases and transmission inherited only within their stated unit. Narrative prescriptions describe the historical source rather than recommendations.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read 5b21–6b37 with core5b21–6a16. Reread for boundary at5b27/6a1, alternative attribution, distinction between knowing and seeing demons, report harm/recovery, interrupted presence chain and 1/2/3/10 distinctions. Completed '+layer+' pass; no further record where none listed.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch02_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch02_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch02_receipt.json',r.encoded(out));print(r.encoded(out).decode())
