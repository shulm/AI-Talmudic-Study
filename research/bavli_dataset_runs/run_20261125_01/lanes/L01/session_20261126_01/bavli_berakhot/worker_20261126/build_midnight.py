from pathlib import Path
import sys
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE=Path(__file__).resolve().parent;JOB=HERE.parent;j,ss=r.load(JOB);state=r.current(JOB)
by={x['ref'].split(' ')[1]:x for x in ss.values()};rows=[];pre='bk.midnight.20261126.'
def ev(ref,quote=None):
 t=by[ref]['text'];quote=t if quote is None else quote;a=t.index(quote)
 return dict(segment_id=by[ref]['id'],start_char=a,end_char=a+len(quote),quote=quote)
def add(k,layer,refs,content,links=(),unc=(),origin='source_paraphrase'):
 rows.append(dict(id=pre+k,layer=layer,evidence=[ev(x) if isinstance(x,str) else ev(*x) for x in refs],content=content,links=[pre+x for x in links],uncertainty=list(unc),origin=origin));return pre+k
def c(k,ref,p,mode='asserted',cond=()):return add(k,'claims',[ref],dict(proposition=p,conditions=list(cond),scope='Reported local aggadic discussion; proposed readings distinguished from alternatives in continuation.',assertion_mode=mode))
def q(k,ref,p):return add(k,'questions',[ref],dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,ref,a,b,rel):return add(k,'edges',[ref],dict(source_id=pre+a,target_id=pre+b,relation=rel,explicitness='source_explicit'),[a,b])
def pos(k,ref,cl,holders,status,question=None,cond=(),unc=()):return add(k,'positions',[ref],dict(holder_candidates=holders,claim_id=pre+cl,question_id=pre+question if question else None,conditions=list(cond),local_status=status),[cl]+([question] if question else []),unc)
def att(k,ref,surface,role,candidates,scope,chain=(),unc=()):return add(k,'attributions',[(ref,surface)],dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=list(chain)),unc=unc)
refs=['3b:'+str(n) for n in range(27,33)]+['4a:'+str(n) for n in range(1,8)]
add('s','structure',refs,dict(title='David and Moses knowing midnight, with the harp and counsel narrative',primary=True,boundary='closed',legacy_ids=[]))
add('nested_counsel','structure',['3b:29','3b:30','3b:31','3b:32','4a:1','4a:2'],dict(title='Dawn livelihood request and sequence of counsel',primary=False,boundary='closed',legacy_ids=[]))
for ref,voice,role in [('3b:27','Anonymous Gemara','Challenge from Moses to David'),('3b:28','Anonymous Gemara','Hypothesis, rejection and inference'),('3b:29','Rav Aha bar Bizna reporting Rabbi Shimon Hasida; embedded David and sages dialogue','Harp answer and livelihood narrative'),('3b:30','Narrative continuation','Counsel sequence'),('3b:31','Rav Yosef','Scriptural evidence question and answer'),('3b:32','Expository continuation','Ahitophel identification'),('4a:1','Expository continuation','Benaiah and Abiathar identifications'),('4a:2','Expository continuation','Scriptural support and name explanation'),('4a:3','Rav Yitzhak bar Adda or Rav Yitzhak son of Rav Idi','Alternative attribution of scriptural support'),('4a:4','Rabbi Zeira','Alternative to the earlier ignorance inference'),('4a:5','Anonymous Gemara','Harp-purpose question and answer'),('4a:6','Anonymous Gemara representing Moses reasoning and citing an unnamed authority','Approximate-time question and caution answer'),('4a:7','Rav Ashi','Alternative temporal interpretation')]:
 add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'))
q('q27','3b:27','Did David know when midnight occurs, when even Moses appears not to know?')
q('q28','3b:28','What does “about midnight” mean; could God have said an approximate time?')
c('c28god',('3b:28','מי איכא ספיקא קמי שמיא'),'The discussion rejects uncertainty before Heaven.',mode='asserted')
c('c28moses',('3b:28','אלא דאמר ליה (למחר) בחצות (כי השתא) ואתא איהו ואמר כחצות אלמא מספקא ליה ודוד הוה ידע'),'The initial inference is that God said midnight but Moses said about midnight because Moses was uncertain; this is challenged by the later alternatives.',mode='challenged')
c('c29sign',('3b:29','דוד סימנא הוה ליה'),'The first answer says David had a sign for midnight.')
c('c29harp',('3b:29','כנור היה תלוי למעלה ממטתו של דוד וכיון שהגיע חצות לילה בא רוח צפונית ונושבת בו ומנגן מאליו'),'The transmitted account says a harp above David’s bed played by itself when the north wind blew at midnight.')
c('c29study',('3b:29','מיד היה עומד ועוסק בתורה עד שעלה עמוד השחר'),'In the harp account David immediately rose and studied Torah until dawn.',cond=['The harp sounded at midnight'])
c('c29need',('3b:29','כיון שעלה עמוד השחר נכנסו חכמי ישראל אצלו אמרו לו אדונינו המלך עמך ישראל צריכין פרנסה'),'At dawn the sages of Israel told David that his people needed sustenance.')
c('c29mutual',('3b:29','אמר להם לכו והתפרנסו זה מזה'),'David first instructed them to sustain one another.')
c('c29insufficient',('3b:29','אמרו לו אין הקומץ משביע את הארי ואין הבור מתמלא מחוליתו'),'The sages answered with two images of insufficiency: a handful does not satisfy a lion and a pit is not filled from its own excavated material.',cond=['Response to the proposal that the people sustain one another'])
c('c29raid',('3b:29','אמר להם לכו ופשטו ידיכם בגדוד'),'David then instructed them to go out in a raiding troop.',cond=['After the sages reject mutual provision as insufficient'])
c('c30','3b:30','The narrative then reports consulting Ahitophel, obtaining counsel from the Sanhedrin, and inquiring of the Urim and Thummim.',cond=['Following David’s instruction to go out in a troop'])
q('q31',('3b:31','מאי קרא'),'What verse supports the described sequence of counsel?')
c('c31','3b:31','Rav Yosef cites the verse ordering Ahitophel, Benaiah son of Jehoiada, Abiathar, and Joab the royal army commander as support.')
c('c32','3b:32','Ahitophel is identified as the counselor, supported by the verse comparing his counsel to inquiry of God.')
c('c41b',('4a:1','בניהו בן יהוידע זה סנהדרין'),'Benaiah son of Jehoiada is interpreted here as the Sanhedrin.')
c('c41a',('4a:1','ואביתר אלו אורים ותומים'),'Abiathar is interpreted here as the Urim and Thummim.')
c('c42verse',('4a:2','וכן הוא אומר (שמואל ב כ, כג) ובניהו בן יהוידע על הכרתי ועל הפלתי'),'The verse placing Benaiah over the Cherethites and Pelethites is supplied as further support.')
q('q42',('4a:2','ולמה נקרא שמם כרתי ופלתי'),'Why are they called Cherethites and Pelethites?')
c('c42c',('4a:2','כרתי שכורתים דבריהם'),'Cherethites is explained by their cutting or determining their words.')
c('c42p',('4a:2','פלתי שמופלאים בדבריהם'),'Pelethites is explained by their being distinguished in their words.')
c('c42joab',('4a:2','ואח"כ שר צבא למלך יואב'),'Only afterward does the verse name Joab as royal army commander, completing the counsel-before-command sequence.')
q('q43',('4a:3','מאי קרא'),'What verse supports the harp account?')
c('c43','4a:3','The verse “Awake, my glory; awake, lyre and harp; I will awaken the dawn” is cited in support of the harp account.')
c('c44','4a:4','Rabbi Zeira says that Moses did know midnight and David also knew.')
q('q45',('4a:5','וכיון דדוד הוה ידע כנור למה ליה'),'If David knew midnight, why did he need the harp?')
c('c45',('4a:5','לאתעורי משנתיה'),'The harp was needed to wake David from sleep.',cond=['Under the answer that David knew midnight'])
q('q46',('4a:6','וכיון דמשה הוה ידע למה ליה למימר כחצות'),'If Moses knew midnight, why say about midnight?')
c('c46fear',('4a:6','משה קסבר שמא יטעו אצטגניני פרעה ויאמרו משה בדאי הוא'),'Moses feared that Pharaoh’s astrologers might err and call him a liar.',cond=['Explaining approximate language despite knowledge of midnight'])
c('c46maxim',('4a:6','דאמר מר למד לשונך לומר איני יודע שמא תתבדה ותאחז'),'An unnamed authority counsels teaching one’s tongue to say “I do not know,” lest one be shown false and caught.')
c('c47','4a:7','Rav Ashi interprets Moses as speaking at midnight of the thirteenth leading into the fourteenth: God said that tomorrow, at midnight like the present moment, He would go out within Egypt.')
for k,ref,surface,role,candidates,scope,chain in [
 ('a29t','3b:29','רב אחא בר ביזנא','transmitter',['רב אחא בר ביזנא'],'Harp and ensuing narrative',['רב אחא בר ביזנא','רבי שמעון חסידא']),
 ('a29h','3b:29','רבי שמעון חסידא','quoted_authority',['רבי שמעון חסידא'],'Harp and ensuing narrative',['רב אחא בר ביזנא','רבי שמעון חסידא']),
 ('a29s','3b:29','חכמי ישראל','collective',['חכמי ישראל'],'Need and insufficiency statements',[]),
 ('a29d','3b:29','אדונינו המלך','speaker',['דוד'],'Embedded instructions replying to sages',[]),
 ('a31','3b:31','רב יוסף','speaker',['רב יוסף'],pre+'c31',[]),
 ('a44','4a:4','רבי זירא','speaker',['רבי זירא'],pre+'c44',[]),
 ('a46','4a:6','דאמר מר','anonymous',[] ,pre+'c46maxim',[]),
 ('a47','4a:7','רב אשי','speaker',['רב אשי'],pre+'c47',[])]:att(k,ref,surface,role,candidates,scope,chain)
att('a43','4a:3','אמר רב יצחק בר אדא ואמרי לה אמר רב יצחק בריה דרב אידי','speaker',['רב יצחק בר אדא','רב יצחק בריה דרב אידי'],pre+'c43',unc=['Two explicit alternative attributions; no choice made between versions.'])
for k,ref,cl,holders,status,question,cond in [
 ('p28','3b:28','c28moses',['Anonymous Gemara'],'Initial inference, challenged by 4a alternatives','q27',[]),
 ('p29','3b:29','c29sign',['Anonymous Gemara'],'First answer','q27',[]),
 ('p29m','3b:29','c29mutual',['דוד'],'First embedded instruction',None,[]),
 ('p29i','3b:29','c29insufficient',['חכמי ישראל'],'Embedded objection',None,['Response to the proposal that the people sustain one another']),
 ('p29r','3b:29','c29raid',['דוד'],'Subsequent embedded instruction',None,['After the sages reject mutual provision as insufficient']),
 ('p31','3b:31','c31',['רב יוסף'],'Scriptural support','q31',[]),
 ('p43','4a:3','c43',['רב יצחק בר אדא','רב יצחק בריה דרב אידי'],'Explicit alternative speaker versions','q43',[]),
 ('p44','4a:4','c44',['רבי זירא'],'Alternative answer','q27',[]),
 ('p45','4a:5','c45',['Anonymous Gemara'],'Answer under Rabbi Zeira interpretation','q45',['Under the answer that David knew midnight']),
 ('p46','4a:6','c46fear',['משה'],'Anonymous account of Moses reasoning','q46',['Explaining approximate language despite knowledge of midnight']),
 ('p47','4a:7','c47',['רב אשי'],'Alternative explanation of approximate-time language','q46',[])]:pos(k,ref,cl,holders,status,question,cond,unc=['Explicit alternative attribution, not joint authorship.'] if k=='p43' else [])
for k,ref,a,b,rel in [
 ('e28','3b:28','c28god','q28','answer'),('e28m','3b:28','c28moses','q27','support'),
 ('e29','3b:29','c29sign','q27','answer'),('e29h','3b:29','c29harp','c29sign','support'),
 ('e29i','3b:29','c29insufficient','c29mutual','objection'),('e29r','3b:29','c29raid','c29insufficient','answer'),
 ('e31','3b:31','c31','q31','answer'),('e31s','3b:31','c31','c30','support'),
 ('e32','3b:32','c32','c31','support'),('e41b','4a:1','c41b','c31','support'),('e41a','4a:1','c41a','c31','support'),
 ('e42v','4a:2','c42verse','c41b','support'),('e42c','4a:2','c42c','q42','answer'),('e42p','4a:2','c42p','q42','answer'),('e42j','4a:2','c42joab','c30','support'),
 ('e43','4a:3','c43','q43','answer'),('e43s','4a:3','c43','c29harp','support'),
 ('e44','4a:4','c44','c28moses','objection'),('e44a','4a:4','c44','q27','answer'),
 ('e45','4a:5','c45','q45','answer'),('e46','4a:6','c46fear','q46','answer'),('e46s','4a:6','c46maxim','c46fear','support'),('e47','4a:7','c47','q46','answer')]:edge(k,ref,a,b,rel)
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  why='Original source read through 4a:12, with 3b:20–26 context. '+('Omission reread retained embedded counsel dialogue, name interpretations, initial Moses uncertainty inference and its alternatives, two speaker versions, fear condition, and counsel order. No additional core claim found in this pass.' if layer=='reconciliation' else 'Completed '+layer+' pass; all anchored findings saved.' if ids else 'Completed '+layer+' pass; no separate finding of this layer in the core segment.')
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=why))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_berakhot_correction',epoch=4,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'midnight_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'midnight_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'midnight_receipt.json',r.encoded(out));print(r.encoded(out).decode())
