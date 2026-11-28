from pathlib import Path
import sys
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE=Path(__file__).resolve().parent;JOB=HERE.parent;j,ss=r.load(JOB);state=r.current(JOB)
by={x['ref'].split(' ')[1]:x for x in ss.values()};rows=[];pre='bk.piety.20261126w2.'
def ev(ref,quote=None):
 t=by[ref]['text'];quote=t if quote is None else quote;a=t.index(quote)
 return dict(segment_id=by[ref]['id'],start_char=a,end_char=a+len(quote),quote=quote)
def add(k,layer,refs,content,links=(),unc=(),origin='source_paraphrase'):
 rows.append(dict(id=pre+k,layer=layer,evidence=[ev(x) if isinstance(x,str) else ev(*x) for x in refs],content=content,links=[pre+x for x in links],uncertainty=list(unc),origin=origin));return pre+k
def c(k,ref,p,mode='asserted',cond=()):return add(k,'claims',[ref],dict(proposition=p,conditions=list(cond),scope='Local aggadic interpretations of David piety and the possibility of sin affecting a promise; no named assignment of anonymous alternatives.',assertion_mode=mode))
def q(k,ref,p):return add(k,'questions',[ref],dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,ref,a,b,rel):return add(k,'edges',[ref],dict(source_id=pre+a,target_id=pre+b,relation=rel,explicitness='source_explicit'),[a,b])
def pos(k,ref,cl,holders,status,question=None,cond=(),unc=()):return add(k,'positions',[ref],dict(holder_candidates=holders,claim_id=pre+cl,question_id=pre+question if question else None,conditions=list(cond),local_status=status),[cl]+([question] if question else []),unc)
def att(k,ref,surface,role,candidates,scope,chain=(),unc=()):return add(k,'attributions',[(ref,surface)],dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=list(chain)),unc=unc)
refs=['4a:'+str(n) for n in range(8,19)]
add('s8','structure',refs[:6],dict(title='Two unnamed assignments of David piety and his willingness to accept correction',primary=True,boundary='closed',legacy_ids=[]))
add('s14','structure',refs[6:],dict(title='Piety, uncertainty of reward, and sin affecting a promise',primary=True,boundary='closed',legacy_ids=[]))
for ref,voice,role in [('4a:8','One of Levi and Rabbi Yitzhak, unnamed','First interpretation of David claim'),('4a:9','The other of Levi and Rabbi Yitzhak, unnamed','Second interpretation and embedded self-account'),('4a:10','Rabbi Yehoshua son of Rav Idi','Scriptural support'),('4a:11','Unnamed tanna','Name interpretation and merit consequence'),('4a:12','Rabbi Yohanan','Name interpretation'),('4a:13','Anonymous citing Solomon','Scriptural support'),('4a:14','Anonymous question with tannaitic report in Rabbi Yose name','Apparent contradiction to David piety'),('4a:15','Anonymous answer','Fear of sin explanation'),('4a:16','Rabbi Yaakov bar Idi','Parallel promise-fear contradiction and answer'),('4a:17','Quoted baraita','Verse introducing historical comparison'),('4a:18','Quoted baraita and Sages','Two entries and lost miracle interpretation')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'))
c('c8',('4a:8','שכל מלכי מזרח ומערב ישנים עד שלש שעות ואני (תהלים קיט, סב) חצות לילה אקום להודות לך'),'One interpretation has David distinguish kings sleeping until three hours from his rising at midnight to give thanks.')
c('c9work',('4a:9','שכל מלכי מזרח ומערב יושבים אגודות אגודות בכבודם ואני ידי מלוכלכות בדם ובשפיר ובשליא כדי לטהר אשה לבעלה'),'The other interpretation has David contrast kings sitting in honor with his handling blood, fetal sacs and placenta to determine a woman’s permissibility to her husband.')
c('c9consult',('4a:9','ולא עוד אלא כל מה שאני עושה אני נמלך במפיבשת רבי'),'David further represents himself as consulting his teacher Mephibosheth about everything he does.')
c('c9unashamed',('4a:9','ואומר לו מפיבשת רבי יפה דנתי  יפה חייבתי  יפה זכיתי יפה טהרתי יפה טמאתי ולא בושתי'),'David asks whether he judged, imposed liability, acquitted, declared pure and declared impure correctly, without embarrassment.')
q('q10',('4a:10','מאי קרא'),'What verse supports David speaking without shame?')
c('c10','4a:10','Rabbi Yehoshua son of Rav Idi cites speaking of God’s testimonies before kings without shame.')
c('c11name',('4a:11','תנא לא מפיבשת שמו אלא איש בשת שמו'),'The tanna says the name was Ish Bosheth rather than Mephibosheth.')
q('q11',('4a:11','ולמה נקרא שמו מפיבשת'),'Why was he called Mephibosheth?')
c('c11shame',('4a:11','שהיה מבייש פני דוד בהלכה'),'The tanna explains the name by his putting David to shame in halakhah.')
c('c11merit',('4a:11','לפיכך זכה דוד ויצא ממנו כלאב'),'The passage makes David’s having Chileab descend from him a consequence of this conduct.')
c('c12name',('4a:12','וא"ר יוחנן לא כלאב שמו אלא דניאל שמו'),'Rabbi Yohanan says the name was Daniel rather than Chileab.')
q('q12',('4a:12','ולמה נקרא שמו כלאב'),'Why was he called Chileab?')
c('c12shame',('4a:12','שהיה מכלים פני מפיבשת בהלכה'),'The name Chileab is explained by his putting Mephibosheth to shame in halakhah.')
c('c13','4a:13','The passage applies Solomon’s verses about a wise son rejoicing his father’s heart and answering a taunter to this case.')
q('q14',('4a:14','ודוד מי קרי לנפשיה חסיד'),'Did David call himself pious, given the cited uncertainty about his share among the righteous?')
q('q14dots',('4a:14','למה נקוד על לולא'),'Why are there dots on the word lule?')
c('c14reward',('4a:14','מובטח אני בך שאתה משלם שכר טוב לצדיקים לעתיד לבוא'),'The tannaitic report in Rabbi Yose’s name represents David as confident that God gives good reward to the righteous in the future.')
c('c14share',('4a:14','אבל איני יודע אם יש לי חלק ביניהם אם לאו'),'That report represents David as not knowing whether he has a share among them.',mode='unresolved')
c('c15','4a:15','The answer explains David’s uncertainty as fear that sin might cause an adverse result.',cond=['Explaining uncertainty despite his claim of piety'])
q('q16','4a:16','How can God’s promise to guard Jacob be reconciled with Jacob being greatly afraid?')
c('c16','4a:16','Rabbi Yaakov bar Idi reconciles Jacob’s fear with the promise of protection by fear that sin might affect it.',cond=['The promise of protection is juxtaposed with Jacob being greatly afraid'])
c('c17','4a:17','The baraita cites the two clauses “until Your people pass” and “until the people You acquired pass.”')
c('c18first',('4a:18','עד יעבור עמך ה\' זו ביאה ראשונה'),'The first clause is interpreted as the first entry.')
c('c18second',('4a:18','עד יעבור עם זו קנית זו ביאה שנייה'),'The second clause is interpreted as the second entry.')
c('c18miracle',('4a:18','מכאן אמרו חכמים ראוים היו ישראל ליעשות להם נס בימי עזרא כדרך שנעשה להם בימי יהושע בן נון'),'The Sages infer that Israel deserved a miracle in Ezra’s days like that in Joshua son of Nun’s days.')
c('c18sin',('4a:18','אלא שגרם החטא'),'Sin is given as the reason that the comparable miracle did not occur.')
att('a8','4a:8',"לוי ור' יצחק חד אמר",'speaker',['לוי','רבי יצחק'],'First interpretation',unc=['Anonymous חד אמר; continuation does not assign by name.'])
att('a9','4a:9','ואידך','speaker',['לוי','רבי יצחק'],'Other interpretation',unc=['Other member of the pair; no name-order assignment.'])
att('a8d','4a:8','כך אמר דוד','quoted_authority',['דוד'],'Embedded piety speech in first interpretation')
att('a9d','4a:9','כך אמר דוד','quoted_authority',['דוד'],'Embedded piety speech in second interpretation')
att('a10','4a:10','רב אידי','transmitter',[],'Name occurs as patronymic inside רבי יהושע בריה דרב אידי, not an asserted transmission',unc=['This patronymic is not a transmission attribution.'])
# Remove the draft patronymic attribution: no record for a person merely named as father.
rows.pop()
att('a10holder','4a:10','רב יהושע' if 'רב יהושע' in by['4a:10']['text'] else 'ר יהושע בריה דרב אידי','speaker',['רבי יהושע בריה דרב אידי'],pre+'c10')
att('a11','4a:11','תנא','anonymous',[],'Tannaitic name/merit account')
att('a12','4a:12','ר יוחנן','speaker',['רבי יוחנן'],'Daniel/Chileab interpretation')
att('a14','4a:14','ותנא משמיה דרבי יוסי','transmitter',['Unnamed tanna'],'David uncertainty interpretation',['Unnamed tanna','רבי יוסי'])
att('a14h','4a:14','רבי יוסי','quoted_authority',['רבי יוסי'],'David uncertainty interpretation',['Unnamed tanna','רבי יוסי'])
att('a16','4a:16',"ר' יעקב בר אידי",'speaker',['רבי יעקב בר אידי'],pre+'c16')
att('a18','4a:18','חכמים','collective',['חכמים'],'Inference of miracle eligibility and sin')
for k,ref,cl,holders,status,question,cond in [
 ('p8','4a:8','c8',['לוי','רבי יצחק'],'One unnamed member of pair; not joint authorship',None,[]),
 ('p9','4a:9','c9work',['לוי','רבי יצחק'],'Other unnamed member of pair; not joint authorship',None,[]),
 ('p11','4a:11','c11shame',['Unnamed tanna'],'Name explanation','q11',[]),
 ('p12','4a:12','c12shame',['רבי יוחנן'],'Name explanation','q12',[]),
 ('p14','4a:14','c14share',['דוד'],'Reported uncertainty through Rabbi Yose; no resolved share','q14dots',[]),
 ('p15','4a:15','c15',['Anonymous Gemara'],'Reconciliation','q14',['Explaining uncertainty despite his claim of piety']),
 ('p16','4a:16','c16',['רבי יעקב בר אידי'],'Parallel reconciliation','q16',['The promise of protection is juxtaposed with Jacob being greatly afraid']),
 ('p18','4a:18','c18miracle',['חכמים'],'Reported historical inference',None,[])]:pos(k,ref,cl,holders,status,question,cond,['Name assignment unresolved.'] if k in ['p8','p9'] else [])
for k,ref,a,b,rel in [
 ('e10','4a:10','c10','q10','answer'),('e10s','4a:10','c10','c9unashamed','support'),('e11','4a:11','c11shame','q11','answer'),('e11m','4a:11','c11merit','c9unashamed','support'),('e12','4a:12','c12shame','q12','answer'),('e13','4a:13','c13','c12shame','support'),('e14','4a:14','c14share','q14','support'),('e14d','4a:14','c14share','q14dots','answer'),('e15','4a:15','c15','q14','answer'),('e16','4a:16','c16','q16','answer'),('e16p','4a:16','c16','c15','analogy'),('e18a','4a:18','c18first','c18miracle','support'),('e18b','4a:18','c18second','c18miracle','support'),('e18s','4a:18','c18sin','c18miracle','qualification'),('e18p','4a:18','c18sin','c16','analogy')]:edge(k,ref,a,b,rel)
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  why='Original source read through4a19 with preceding midnight context. '+('Omission reread preserves both unnamed explanations, teacher consultation and five retrospective questions, names and merit consequence, dotted-word interpretation, uncertainty and both historical parallels. No later assignment of Levi/Rabbi Yitzhak found.' if layer=='reconciliation' else 'Completed '+layer+' pass, preserving anchored findings.' if ids else 'Completed '+layer+' pass; no separate finding in this segment.')
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_berakhot_correction',epoch=4,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch01_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch01_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch01_receipt.json',r.encoded(out));print(r.encoded(out).decode())
