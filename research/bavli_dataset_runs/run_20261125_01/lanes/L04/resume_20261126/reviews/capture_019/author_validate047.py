"""Source-only manual semantic inventory; deterministic author and validator. No APIs.
Run without arguments to validate in memory, --freeze for exclusive first write.
"""
import json, hashlib, pathlib, re, sys, collections, datetime
import jsonschema
ROOT=pathlib.Path(__file__).parent
JOB=pathlib.Path('C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/jobs/bavli_moed_katan_delegated047.json')
H=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(pathlib.Path(p).read_text(encoding='utf-8-sig'))
j=load(JOB)
assert H(JOB.read_bytes())=='199405c845c21087f234d1778116d9cc8f93093997360960f7ecf642e271f819'
bindings=[j['source'],*j['common_documents'],j['frozen_plan'],j['original_source_schema']]
for b in bindings: assert H(pathlib.Path(b['path']).read_bytes())==b['sha256']
plan=load(j['frozen_plan']['path']); ph=plan.copy();del ph['plan_sha256']
assert H(b'bavli-source-only-review-plan-v1\0'+json.dumps(ph,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode())==j['plan_sha256']==plan['plan_sha256']
source=load(j['source']['path']); schema=load(j['common_documents'][1]['path'])
texts={f'Moed Katan {i//2+1}{"a" if i%2==0 else "b"}:{n}':s for i,p in enumerate(source['text']) for n,s in enumerate(p,1)}
coords={f'Moed Katan {i//2+1}{"a" if i%2==0 else "b"}:{n}':[i,n-1] for i,p in enumerate(source['text']) for n,s in enumerate(p,1)}
for b in j['selected_blocks']:
 pb=next(v for v in plan['review_blocks'] if v['block_id']==b['block_id'])
 assert [v['ref'] for v in pb['spans']]==b['core_refs']
 assert b['block_id'] in plan['sampling']['probability_sample_block_ids']
 for v in pb['spans']:
  assert coords[v['ref']]==[v['page_index'],v['segment_index']]
  assert v['offsets_codepoints']==[0,len(texts[v['ref']])]
  assert H(texts[v['ref']].encode())==v['span_sha256_utf8']
records=[]; labels={}; notes={}; qids={}
def ref(r):return r if r.startswith('Moed Katan ') else 'Moed Katan '+r
def ev(r,quote=None):
 r=ref(r);t=texts[r];quote=t if quote is None else quote
 assert quote in t,(r,quote)
 start=t.index(quote);return {'segment_id':r,'start_char':start,'end_char':start+len(quote),'quote':quote}
def rec(layer,r,quote,content,key=None,links=(),unc=(),origin='source_paraphrase',extra=()):
 rid=f'mk047.{layer}.{len(records)+1:04d}'
 records.append(dict(id=rid,layer=layer,evidence=[ev(r,quote),*extra],content=content,origin=origin,uncertainty=list(unc),links=list(links)))
 if key: assert key not in labels;labels[key]=rid
 return rid
def u(r,quote,voice,role='statement',key=None,composition='atomic',unc=()):
 return rec('utterances',r,quote,dict(textual_voice=voice,discourse_role=role,composition=composition),key,unc=unc)
def a(r,quote,surface,role='speaker',candidates=None,chain=(),scope='',links=(),unc=()):
 return rec('attributions',r,quote,dict(surface=surface,role=role,candidates=candidates if candidates is not None else ([] if role=='anonymous' else [surface]),scope=scope or quote,transmission_chain=list(chain)),links=links,unc=unc)
def c(key,r,quote,prop,holder='anonymous',cond=(),mode='asserted',status=None,q=None,unc=(),extra=(),position=True):
 cid=rec('claims',r,quote,dict(proposition=prop,conditions=list(cond),scope=ref(r),assertion_mode=mode),key,unc=unc,extra=extra)
 if position:
  rec('positions',r,quote,dict(holder_candidates=[] if holder=='anonymous' else ([holder] if isinstance(holder,str) else holder),claim_id=cid,question_id=qids.get(q),conditions=list(cond),local_status=status or mode),links=[cid]+([qids[q]] if q else []),unc=unc,extra=extra)
 return cid
def q(key,r,quote,form,cond=(),status='partial',extra=()):
 rid=rec('questions',r,quote,dict(formulation=form,question_origin='explicit',conditions=list(cond),answer_set_status=status),key,extra=extra);qids[key]=rid;return rid
def edge(r,quote,fr,to,relation,explicit=True,unc=()):
 return rec('edges',r,quote,dict(source_id=labels[fr],target_id=labels[to],relation=relation,explicitness='source_explicit' if explicit else 'editorial_reconstruction'),links=[labels[fr],labels[to]],unc=unc)
def note(r,s):notes[ref(r)]=s
# Context needed to resolve the anonymous views in the first core.
u('13b:7',None,'Abaye; Rav Dimi','definitions',composition='composite')
c('split','13b:7','אמר אביי חילקא חדא לתרתי טרגיס חדא לתלת טיסני חדא לארבעה','Abaye defines hilqa, targis and tisni as grain split into two, three and four pieces respectively.','Abaye')
c('kunta','13b:7','כי אתא רב דימי אמר כונתא','Rav Dimi identifies the product as כונתא.','Rav Dimi',unc=['The source supplies the term כונתא; no botanical identification imposed.'])
a('13b:7','אמר אביי','אביי');a('13b:7','כי אתא רב דימי אמר','רב דימי')
# 13b:8–10. The grain arguments remain distinct; קשיא is not a retraction.
u('13b:8','מיתיבי חילקא טרגיס וטיסני טמאין בכל מקום','anonymous cited teaching','objection')
u('13b:8','בשלמא למ"ד חדא לתרתי לתלת ולארבעה משום הכי טמאין בכל מקום דאתכשור','anonymous dialectic','explanation')
u('13b:8','אלא למ"ד כונתא אמאי טמאין בכל מקום הא לא איתכשור','anonymous dialectic','objection')
c('impure','13b:8','חילקא טרגיס וטיסני טמאין בכל מקום','Hilqa, targis and tisni are impure everywhere.','anonymous cited teaching')
c('wet_split','13b:8','בשלמא למ"ד חדא לתרתי לתלת ולארבעה משום הכי טמאין בכל מקום דאתכשור','The split-grain account explains impurity because the products were rendered susceptible.',cond=['Abaye split-grain account'])
q('wetq','13b:8','אלא למ"ד כונתא אמאי טמאין בכל מקום הא לא איתכשור','Why impurity everywhere on the כונתא account, absent susceptibility?')
c('dry','13b:8','הא לא איתכשור','כונתא has not been rendered susceptible, an objection premise subsequently qualified.',mode='challenged',status='Objection premise answered by the peeled-product qualification.')
edge('13b:8','דאתכשור','wet_split','impure','support');edge('13b:8','אלא למ"ד כונתא','wetq','kunta','objection')
u('13b:9','כגון דמיקלפן דאי לאו דשרא להו במיא לא הוה מיקלפא','anonymous dialectic','answer')
u('13b:9','ואמאי קרי ליה חילקא דשקל חלקיהו','anonymous dialectic','question and answer',composition='composite')
c('peeled','13b:9','כגון דמיקלפן','The impurity teaching concerns peeled כונתא.',cond=['peeled product'],mode='reconciled',q='wetq')
c('soak','13b:9','דאי לאו דשרא להו במיא לא הוה מיקלפא','Peeling requires prior soaking in water.',cond=['product here is peeled'])
q('nameq','13b:9','ואמאי קרי ליה חילקא','Why is this called hilqa?')
c('name','13b:9','דשקל חלקיהו','The name hilqa is explained by removal of its portion.',q='nameq')
edge('13b:9','כגון דמיקלפן','peeled','wetq','answer');edge('13b:9','דאי לאו דשרא להו במיא לא הוה מיקלפא','soak','peeled','support');edge('13b:9','דשקל חלקיהו','name','nameq','answer')
u('13b:10','מיתיבי הנודר מן הדגן אסור אף בפול המצרי יבש ומותר בלח ומותר באורז בחילקא וטרגיס וטיסני','anonymous cited teaching','objection',composition='composite')
u('13b:10','בשלמא למ"ד חדא לתרתי חדא לתלת וחדא לארבעה שפיר דנפקו להו מתורת דגן','anonymous dialectic','explanation')
u('13b:10','אלא למ"ד כונתא דגן מעליא הוא קשיא','anonymous dialectic','unresolved objection')
c('drybean','13b:10','הנודר מן הדגן אסור אף בפול המצרי יבש','A vow against grain prohibits even dried Egyptian beans.','anonymous cited teaching',cond=['vow against דגן'])
c('wetbean','13b:10','ומותר בלח','Fresh Egyptian beans are permitted under that vow.','anonymous cited teaching',cond=['vow against דגן'])
for key,quote,food in [('rice','באורז','rice'),('hilqa','בחילקא','hilqa'),('targis','וטרגיס','targis'),('tisni','וטיסני','tisni')]:c(key,'13b:10',quote,f'{food} is permitted under a vow against grain.','anonymous cited teaching',cond=['vow against דגן'],extra=[ev('13b:10','ומותר באורז בחילקא וטרגיס וטיסני')])
c('notgrain','13b:10','דנפקו להו מתורת דגן','Split products have left the category of grain.',cond=['split-grain definition'])
c('stillgrain','13b:10','אלא למ"ד כונתא דגן מעליא הוא קשיא','כונתא is fully grain; its permission remains difficult for Rav Dimi’s definition.',mode='unresolved')
edge('13b:10','דנפקו להו מתורת דגן','notgrain','hilqa','support');edge('13b:10','קשיא','stillgrain','kunta','unresolved_outcome')
note('13b:10','Retained each vow item and the unresolved קשיא; no named authority retracts. Anonymous dialectic tests Rav Dimi; not a maintained anti-Rav-Dimi position of Abaye.')
# Market permissions and challenge, continued across source segments.
u('13b:11','רב הונא שרא להו להנהו כרופייתא למיזל לזבוני כי אורחייהו בשוקא','anonymous narrator','reported ruling')
u('13b:11','איתיביה רב כהנא חנות פתוחה לסטיו פותח ונועל כדרכו','Rav Kahana citing a teaching','objection')
a('13b:11','רב הונא שרא','רב הונא','position_holder');a('13b:11','איתיביה רב כהנא','רב כהנא','speaker',scope='Cites objection to Rav Huna; not original author of shop regulations.')
c('huna','13b:11','רב הונא שרא להו להנהו כרופייתא למיזל לזבוני כי אורחייהו בשוקא','Rav Huna permitted these vendors to sell normally in the market.','Rav Huna',cond=['festival intermediate days','vendors later distinguished as spice vendors'])
c('stoa','13b:11','חנות פתוחה לסטיו פותח ונועל כדרכו','A shop opening onto a stoa may open and close normally.','anonymous cited teaching',cond=['shop opens onto stoa'])
u('13b:12','פתוחה לרה"ר פותח אחת ונועל אחת וערב יום טוב האחרון של חג מוציא ומעטר את שוקי העיר בפירות בשביל כבוד י"ט האחרון','cited teaching continued','rules',composition='composite')
u('13b:12','מפני כבוד י"ט האחרון אין שלא מפני כבוד י"ט לא','anonymous dialectic within Rav Kahana objection','restrictive inference')
c('street','13b:12','פתוחה לרה"ר פותח אחת ונועל אחת','A shop opening to the public thoroughfare opens one and closes one.','anonymous cited teaching',cond=['shop opens to public thoroughfare'])
c('honor','13b:12','וערב יום טוב האחרון של חג מוציא ומעטר את שוקי העיר בפירות בשביל כבוד י"ט האחרון','On the eve of the last festival day one displays fruit in the city markets for its honor.','anonymous cited teaching',cond=['eve of final festival day'])
c('nohonor','13b:12','מפני כבוד י"ט האחרון אין שלא מפני כבוד י"ט לא','The special public display permission does not apply without the final festival day’s honor.',mode='challenged',status='Valid for fruit; distinguished from spice ruling.')
edge('13b:12','מפני כבוד י"ט האחרון אין שלא מפני כבוד י"ט לא','nohonor','huna','objection')
u('13b:13',None,'anonymous dialectic','distinction')
c('fruitspice','13b:13',None,'The teaching concerns fruit; Rav Huna’s permission concerns spices, resolving the apparent contradiction.',mode='reconciled',unc=['Assignment of הא to the two preceding cases is contextual, not an explicit noun-to-speaker labeling.'])
edge('13b:13',None,'fruitspice','nohonor','distinction');edge('13b:13',None,'fruitspice','huna','local_resolution')
note('13b:14','Chapter closing formula and markup only; no proposition, speaker, question, position or argumentative relation asserted.')
# Mishnah: each eligibility condition is inventoried separately.
u('13b:15',None,'anonymous Mishnah','permitted haircut classes',composition='composite')
for key,quote,prop,cond in [
 ('sea','הבא ממדינת הים','A person arriving from overseas may cut hair.','arrival from overseas'),
 ('captive','ומבית השביה','A person released from captivity may cut hair.','release from captivity'),
 ('prison','והיוצא מבית האסורין','A person leaving prison may cut hair.','release from prison'),
 ('released','והמנודה שהתירו לו חכמים','An excommunicated person whose ban the sages released may cut hair.','sages released ban'),
 ('vow','וכן מי שנשאל לחכם והותר','One who consulted a sage and was released from a vow may cut hair.','sage released vow'),
 ('nazir','והנזיר','The nazir may shave in the stated purification setting.','nazir purification'),
 ('leper','והמצורע מטומאתו לטהרתו','The metzora moving from impurity to purity may shave.','metzora purification')]:
 c(key,'13b:15',quote,prop,'anonymous Mishnah',cond=['intermediate festival days',cond],extra=[ev('13b:15','מגלחין במועד')],unc=['The final purification qualifier follows the combined nazir/metzora phrase.'] if key=='nazir' else ())
u('13b:16',None,'anonymous Mishnah','permitted laundry classes',composition='composite')
for key,quote,case in [('washsea','הבא ממדינת הים','arriving from overseas'),('washcapt','ומבית השביה','released from captivity'),('washprison','והיוצא מבית האסורין','released from prison')]:c(key,'13b:16',quote,f'One {case} may launder.','anonymous Mishnah',cond=['intermediate festival days',case],extra=[ev('13b:16','ואלו מכבסין במועד')])
u('14a:1',None,'anonymous Mishnah','laundry list continuation',composition='composite')
c('washban','14a:1','ומנודה שהתירו לו חכמים','One whose ban the sages released may launder.','anonymous Mishnah',cond=['festival intermediate days','sages released ban'],extra=[ev('13b:16','ואלו מכבסין במועד')])
c('washvow','14a:1','וכן מי שנשאל לחכם והותר','One released by a sage from a vow may launder.','anonymous Mishnah',cond=['festival intermediate days','sage released vow'],extra=[ev('13b:16','ואלו מכבסין במועד')])
# Travel: actual disagreement is identified through 14a:11 and reconciliation, not mere name order.
u('14a:11',None,'anonymous discussion citing Rabbi Yehuda','context')
c('yehudactx','14a:11',None,'Rabbi Yehuda prohibits haircut for the returning traveler because he left without permission.','Rabbi Yehuda',cond=['travel not authorized'])
u('14a:12',None,'Rava','classification',composition='composite');a('14a:12','אמר רבא','רבא',scope='Explains positions of Rabbi Yehuda and sages, not their original speaker.')
c('tour','14a:12','לשוט דברי הכל אסור','All prohibit haircut after a pleasure trip.',['Rabbi Yehuda','sages'],cond=['travel לשוט'])
c('food','14a:12','למזונות דברי הכל מותר','All permit haircut after travel for subsistence.',['Rabbi Yehuda','sages'],cond=['travel למזונות'])
c('profitdispute','14a:12','לא נחלקו אלא להרויחא','The disagreement concerns travel to increase profit.',cond=['travel להרויחא'])
c('profitno','14a:12','מר מדמי ליה כלשוט','Rabbi Yehuda analogizes profit travel to pleasure travel and prohibits haircut.','Rabbi Yehuda',cond=['travel להרויחא'],extra=[ev('14a:15','שאפילו חכמים לא נחלקו עליו אלא להרויחא אבל לשוט מודו ליה')])
c('profityes','14a:12','ומר מדמי ליה כלמזונות','The sages analogize profit travel to subsistence travel and permit haircut.','sages',cond=['travel להרויחא'],extra=[ev('14a:15','שאפילו רבי יהודה לא נחלק עליהם אלא להרויחא אבל למזונות מודה להו')])
edge('14a:12','מר מדמי ליה כלשוט','profitno','tour','analogy');edge('14a:12','ומר מדמי ליה כלמזונות','profityes','food','analogy')
u('14a:13','מיתיבי אמר ר\' נראין דברי ר\' יהודה כשיצא שלא ברשות ודברי חכמים כשיצא ברשות','anonymous objector quoting Rabbi','objection',composition='composite')
a('14a:13','אמר ר\'','ר\'','quoted_authority',candidates=['Rabbi'],scope='Rabbi comments on Rabbi Yehuda and sages; not identical to Rabbi Yehuda.')
c('rabbi1','14a:13','נראין דברי ר\' יהודה כשיצא שלא ברשות','Rabbi says Rabbi Yehuda’s words appear right for unauthorized departure.','Rabbi',cond=['unauthorized departure'],status='Wording reinterpreted as agreement by the sages in 14a:15.')
c('rabbi2','14a:13','ודברי חכמים כשיצא ברשות','Rabbi says the sages’ words appear right for authorized departure.','Rabbi',cond=['authorized departure'],status='Wording reinterpreted as agreement by Rabbi Yehuda in 14a:15.')
u('14a:13','מאי שלא ברשות אילימא לשוט והאמרת דברי הכל אסור ואלא למזונות והאמרת דברי הכל מותר אלא פשיטא להרויחא','anonymous dialectic','alternative testing',composition='composite')
q('unauthq','14a:13','מאי שלא ברשות','What does unauthorized departure mean in Rabbi’s formulation?')
c('not_tour','14a:13','אילימא לשוט והאמרת דברי הכל אסור','The initial reading rejects pleasure travel as the disputed unauthorized case because all prohibit.',cond=['initial reading of Rabbi as choosing between opponents'],mode='rejected',q='unauthq')
c('not_food','14a:13','ואלא למזונות והאמרת דברי הכל מותר','The initial reading rejects subsistence travel as unauthorized because all permit.',cond=['initial reading of Rabbi'],mode='rejected',q='unauthq')
c('initialprofit','14a:13','אלא פשיטא להרויחא','The objection initially identifies unauthorized departure with profit travel.',mode='hypothetical',q='unauthq',status='Superseded by reinterpretation in 14a:15.')
u('14a:14',None,'anonymous dialectic','tests second clause',composition='composite')
q('authq','14a:14','מאי ברשות','What is authorized departure in Rabbi’s second clause?')
c('authfood','14a:14','אילימא למזונות הא אמרת דברי הכל מותר','Subsistence does not fit the initial choosing-between-opponents reading because all permit.',cond=['initial reading of Rabbi'],mode='rejected',q='authq')
c('authprofit','14a:14','ואלא להרויחא והא אמרת נראין דברי רבי יהודה בהא','Profit travel cannot also be the preferred sages’ case under the initial interpretation, since that case was assigned to Rabbi Yehuda.',cond=['initial interpretation of first clause as profit'],mode='rejected',q='authq')
edge('14a:14','והא אמרת נראין דברי רבי יהודה בהא','authprofit','initialprofit','objection')
u('14a:15',None,'anonymous dialectic','reinterpretation',composition='composite')
c('resolve_tour','14a:15','נראין דברי ר\' יהודה לרבנן כשיצא שלא ברשות ומאי ניהו לשוט','Rabbi means the sages accept Rabbi Yehuda’s prohibition for pleasure travel.','sages',cond=['pleasure travel'],mode='reconciled',q='unauthq')
c('resolve_profit1','14a:15','שאפילו חכמים לא נחלקו עליו אלא להרויחא אבל לשוט מודו ליה','The sages disagree only about profit travel and concede on pleasure travel.','sages',cond=['distinguishes profit from pleasure'],mode='reconciled')
c('resolve_food','14a:15','ונראין דברי רבנן לר\' יהודה כשיצא ברשות ומאי ניהו למזונות','Rabbi means Rabbi Yehuda accepts the sages’ permission for subsistence travel.','Rabbi Yehuda',cond=['subsistence travel'],mode='reconciled',q='authq')
c('resolve_profit2','14a:15','שאפילו רבי יהודה לא נחלק עליהם אלא להרויחא אבל למזונות מודה להו','Rabbi Yehuda disagrees only about profit travel and concedes on subsistence.','Rabbi Yehuda',cond=['distinguishes profit from subsistence'],mode='reconciled')
edge('14a:15','הכי קאמר','resolve_tour','rabbi1','local_resolution');edge('14a:15','ונראין דברי רבנן לר\' יהודה','resolve_food','rabbi2','local_resolution');edge('14a:15','ומאי ניהו לשוט','resolve_tour','unauthq','answer');edge('14a:15','ומאי ניהו למזונות','resolve_food','authq','answer')
note('14a:15','Re-read both Rabbi clauses and every alternative. Final common-ground reading restores Rava; profit remains the only dispute. The discarded preference reading is preserved, not attributed as final law.')
# Two transmitted versions of Shmuel and a failed converse proof in each.
u('14a:16','אמר שמואל קטן הנולד במועד מותר לגלח במועד שאין לך בית האסורין גדול מזה','Shmuel','ruling and reason',composition='composite')
u('14a:16','במועד אין מעיקרא לא','anonymous dialectic','inference')
a('14a:16','אמר שמואל','שמואל')
c('childv1','14a:16','קטן הנולד במועד מותר לגלח במועד','A child born during the festival may have hair cut during it.','Shmuel',cond=['born during festival'],status='First transmitted formulation; distinct second version follows.')
c('womb','14a:16','שאין לך בית האסורין גדול מזה','The womb is treated as the greatest prison, explaining the newborn allowance.','Shmuel')
c('childbefore','14a:16','במועד אין מעיקרא לא','The anonymous inference excludes a child born before the festival.',cond=['born before festival'],mode='asserted',status='Inference from first version; challenged but not refuted by Pinhas proof; not merged with second version.')
edge('14a:16','שאין לך בית האסורין גדול מזה','womb','childv1','analogy')
u('14a:17','מתיב ר\' פנחס כל אלו שאמרו מותר לגלח במועד מותר לגלח בימי אבלו','Rabbi Pinhas quoting teaching','objection')
u('14a:17','הא אסור לגלח במועד אסור לגלח בימי אבלו','Pinhas objection / anonymous inferential continuation','converse inference',unc=['The source does not mark a new speaker before the inference.'])
a('14a:17','מתיב ר\' פנחס','ר\' פנחס',scope='Objector and citer; original teaching remains unnamed.')
c('mourningperm','14a:17','כל אלו שאמרו מותר לגלח במועד מותר לגלח בימי אבלו','All specified as permitted festival haircut are permitted haircut in mourning.','anonymous cited teaching',cond=['specified festival-permitted classes'])
c('converse','14a:17','הא אסור לגלח במועד אסור לגלח בימי אבלו','The objection infers that all festival-prohibited haircut cases are also mourning-prohibited.',mode='rejected',status='Rav Ashi denies that this converse was taught.')
u('14b:1',None,'Pinhas objection continued','conditional consequence')
c('childmourning','14b:1',None,'If children differ by birth timing in the festival rule, the inferred converse makes mourning apply to a child.',cond=['first-version distinction','converse inference'],mode='hypothetical')
edge('14b:1',None,'childmourning','childbefore','objection');edge('14b:1',None,'converse','childmourning','support')
u('14b:2',None,'cited baraita','counterevidence')
c('tearminor','14b:2','מקרעין לקטן מפני עגמת נפש','Garments are torn for a minor for grief, not stated as the minor’s own mourning obligation.','anonymous cited baraita',cond=['minor'],unc=['The exclusion of a minor’s mourning obligation is the argument’s implication, not a separate explicit sentence.'])
edge('14b:2',None,'tearminor','childmourning','objection')
u('14b:3',None,'Rav Ashi','rejects converse',composition='composite');a('14b:3','אמר רב אשי','רב אשי')
q('ashiq','14b:3','מי קתני הא אסורין','Does the teaching actually state the converse prohibition?',status='topic_inventory')
c('ashino','14b:3','מי קתני הא אסורין','The converse prohibition is not expressly taught.','Rav Ashi',q='ashiq')
c('ashimixed','14b:3','דלמא יש מהן אסור ויש מהן מותר','Perhaps some festival-prohibited cases are prohibited in mourning and others permitted.','Rav Ashi',mode='hypothetical',status='Alternative sufficient to defeat the proof; does not specify all members of either class.')
edge('14b:3','מי קתני הא אסורין','ashino','converse','objection');edge('14b:3','דלמא יש מהן אסור ויש מהן מותר','ashimixed','childmourning','answer')
u('14b:4',None,'Amemar OR Rav Shisha son of Rav Idi transmitting Shmuel','alternative version')
a('14b:4','אמימר ואי תימא רב שישא בריה דרב אידי','אמימר ואי תימא רב שישא בריה דרב אידי','transmitter',candidates=['Amemar','Rav Shisha son of Rav Idi'],chain=['Amemar OR Rav Shisha son of Rav Idi','Shmuel'],unc=['Alternative transmitters, not a serial chain through both.'])
a('14b:4','אמר שמואל','שמואל','quoted_authority',chain=['Amemar OR Rav Shisha son of Rav Idi','Shmuel'])
c('childv2','14b:4','קטן מותר לגלחו במועד לא שנא נולד במועד ולא שנא נולד מעיקרא','A child may have hair cut in the festival whether born during it or beforehand.','Shmuel',cond=['second transmitted version','either birth timing'],status='Alternative formulation; no instruction to replace first version.')
edge('14b:4','מתני הכי','childv2','childv1','continuation',unc=['Version relation; not chronological retraction.'])
# Context explicitly preserves why the second version also lacks a valid converse proof.
u('14b:5',None,'Rav Pinhas','attempted support',composition='composite')
c('v2proof','14b:5',None,'Pinhas attempts to support the second version from the same permission teaching and inferred converse.','Rav Pinhas',mode='challenged')
u('14b:6',None,'Pinhas support continued','conditional reductio')
c('v2minor','14b:6',None,'If a child were prohibited, the converse would entail mourning of a minor, contrary to the grief rationale.',mode='hypothetical')
u('14b:7',None,'Rav Ashi','rejects supporting inference')
c('v2reject','14b:7',None,'Rav Ashi again denies that the converse follows: some may be prohibited and some permitted.','Rav Ashi',mode='hypothetical')
edge('14b:5','אף אנן נמי תנינא','v2proof','childv2','support');edge('14b:7',None,'v2reject','v2proof','objection')
note('14b:4','Read through 14b:7: Pinhas switches from objection to attempted support across variants; Rav Ashi blocks both converse inferences. Neither version is forced as sole final Shmuel position.')
# Ritual mourning / ban / metzora inquiries, with cited scripture distinguished from voices.
u('15a:24','מצורע מהו בקריעה','anonymous dialectic','question');u('15a:24','ת"ש (ויקרא יג, מה) בגדיו יהיו פרומים שיהו מקורעין שמע מינה','anonymous citing scriptural exposition','answer')
q('tearq','15a:24','מצורע מהו בקריעה','Must a metzora rend garments?',status='topic_inventory')
c('lepertear','15a:24','בגדיו יהיו פרומים שיהו מקורעין שמע מינה','A metzora must have torn garments, derived from Leviticus 13:45.',q='tearq')
a('15a:24','(ויקרא יג, מה) בגדיו יהיו פרומים','Leviticus 13:45','quoted_authority',scope='Scriptural warrant, not a named amoraic speaker.')
edge('15a:24','שמע מינה','lepertear','tearq','answer')
u('15a:25','אבל חייב בכפיית המטה','anonymous dialectic','rule')
u('15a:25','דתני בר קפרא','anonymous narrator introducing Bar Kappara','citation opens into next segment')
c('bed','15a:25','אבל חייב בכפיית המטה','A mourner must overturn the bed.')
a('15a:25','דתני בר קפרא','בר קפרא','quoted_authority',scope='Teaches the rationale continued at 15b:1; not the first-person divine speaker.')
u('15b:1','דמות דיוקני נתתי בהן ובעונותיהם הפכתיה כפו מטותיהן עליה','divine first-person voice in Bar Kappara teaching','rationale',composition='composite')
c('image','15b:1','דמות דיוקני נתתי בהן','The teaching voices God as having placed His likeness in people.','divine voice in Bar Kappara teaching',extra=[ev('15a:25','דתני בר קפרא')])
c('overturn','15b:1','ובעונותיהם הפכתיה','Their sins led to the overturning of that likeness.','divine voice in Bar Kappara teaching',extra=[ev('15a:25','דתני בר קפרא')])
c('bedreason','15b:1','כפו מטותיהן עליה','The teaching commands overturning their beds on account of that overturning.','divine voice in Bar Kappara teaching',extra=[ev('15a:25','דתני בר קפרא')])
edge('15b:1','כפו מטותיהן עליה','bedreason','bed','support')
u('15b:1','מנודה ומצורע מה הן בכפיית המטה תיקו','anonymous dialectic','unresolved inquiry')
q('banbedq','15b:1','מנודה ומצורע מה הן בכפיית המטה','Must a person under niddui or a metzora overturn the bed?',status='none')
u('15b:2',None,'anonymous dialectic citing Amos','rule and analogy',composition='composite')
c('festivalwork','15b:2','מה חג אסור במלאכה','Festival labor is prohibited, serving as the analogy premise.')
c('mournerwork','15b:2','אף אבל אסור במלאכה','A mourner is prohibited from work, by analogy to festival.',extra=[ev('15b:2','אבל אסור בעשיית מלאכה')])
c('amos','15b:2','(עמוס ח, י) והפכתי חגיכם לאבל','Amos 8:10 connects festivals and mourning.','Amos 8:10')
edge('15b:2','מה חג אסור במלאכה אף אבל אסור במלאכה','mournerwork','festivalwork','analogy');edge('15b:2','דכתיב','amos','mournerwork','support')
q('banworkq','15b:3','מנודה מהו בעשיית מלאכה','May one under niddui work?')
u('15b:3','מנודה מהו בעשיית מלאכה','anonymous dialectic','question')
u('15b:3','אמר רב יוסף ת"ש כשאמרו אסור בעשיית מלאכה לא אמרו אלא ביום אבל בלילה מותר וכן אתה מוצא במנודה ובאבל','Rav Yosef citing teaching','attempted answer',composition='composite')
a('15b:3','אמר רב יוסף','רב יוסף','speaker',scope='Cites anonymous teaching; not the original authority for all clauses.')
c('daywork','15b:3','כשאמרו אסור בעשיית מלאכה לא אמרו אלא ביום','The quoted work prohibition is limited to daytime.','anonymous cited teaching',cond=['underlying subject of quoted teaching not explicitly named here','daytime'])
c('nightwork','15b:3','אבל בלילה מותר','The quoted rule permits work at night.','anonymous cited teaching',cond=['underlying subject of quoted teaching','night'])
c('alsobanwork','15b:3','וכן אתה מוצא במנודה ובאבל','The teaching adds that a corresponding rule occurs in niddui and mourning.','anonymous cited teaching',status='Which preceding restrictions are included is disputed in the dialectic.')
u('15b:3','מאי לאו אכולהו לא אשארא','anonymous dialectic','scope proposal and rejection',composition='composite')
q('workscopeq','15b:3','מאי לאו אכולהו','Does the comparison apply to all restrictions, including work?')
c('workall','15b:3','מאי לאו אכולהו','The inference applies the comparison to all restrictions including work.',mode='rejected',q='workscopeq')
c('workother','15b:3','לא אשארא','The response restricts the comparison to the other restrictions; this citation does not decide niddui work.',q='workscopeq',status='Blocks attempted proof; not itself a work prohibition.')
edge('15b:3','לא אשארא','workother','workall','objection');edge('15b:3','לא אשארא','workother','workscopeq','answer')
u('15b:4','ת"ש מנודה שונה ושונין לו נשכר ונשכרין לו שמע מינה','anonymous dialectic citing teaching','conclusive answer',composition='composite')
c('banstudy','15b:4','מנודה שונה','One under niddui studies.','anonymous cited teaching',cond=['niddui'])
c('teachban','15b:4','ושונין לו','Others teach one under niddui.','anonymous cited teaching',cond=['niddui'])
c('banhire','15b:4','נשכר','One under niddui may be hired.','anonymous cited teaching',cond=['niddui'],q='banworkq')
c('hireforban','15b:4','ונשכרין לו','Others may be hired by one under niddui.','anonymous cited teaching',cond=['niddui'],q='banworkq')
edge('15b:4','שמע מינה','banhire','banworkq','answer');edge('15b:4','שמע מינה','hireforban','banworkq','answer')
u('15b:4','מצורע מהו בעשיית מלאכה תיקו','anonymous dialectic','unresolved inquiry')
q('leperworkq','15b:4','מצורע מהו בעשיית מלאכה','May a metzora work?',status='none')
c('leperwork','15b:4','מצורע מהו בעשיית מלאכה תיקו','Metzora work remains unresolved.',mode='unresolved',q='leperworkq');edge('15b:4','תיקו','leperwork','leperworkq','unresolved_outcome')
u('15b:5',None,'anonymous dialectic citing Samuel','rule and derivation',composition='composite')
c('anoint','15b:5','ואל תסוכי שמן','The cited mourning instruction prohibits anointing with oil.','2 Samuel 14:2')
c('washinclude','15b:5','ורחיצה בכלל סיכה','Bathing is included in anointing for this derivation.')
c('mournerbath','15b:5','אבל אסור ברחיצה','A mourner is prohibited from bathing.')
edge('15b:5','דכתיב','anoint','mournerbath','support');edge('15b:5','ורחיצה בכלל סיכה','washinclude','mournerbath','support')
q('banbathq','15b:6','מנודה מהו ברחיצה','May one under niddui bathe?',status='none')
u('15b:6','מנודה מהו ברחיצה','anonymous dialectic','question')
u('15b:6','אמר רב יוסף ת"ש כשאמרו אסור ברחיצה לא אמרו אלא כל גופו אבל פניו ידיו ורגליו מותר וכן אתה מוצא במנודה ובאבל','Rav Yosef citing teaching','attempted answer',composition='composite')
a('15b:6','אמר רב יוסף','רב יוסף',scope='Citer of anonymous teaching; proposed applicability is rejected.')
c('wholebath','15b:6','כשאמרו אסור ברחיצה לא אמרו אלא כל גופו','The quoted bathing prohibition concerns the whole body.','anonymous cited teaching',cond=['underlying subject not specified here','whole body'])
c('partbath','15b:6','אבל פניו ידיו ורגליו מותר','Washing face, hands and feet is permitted under the quoted rule.','anonymous cited teaching',cond=['underlying subject of teaching','face, hands and feet'])
c('alsobath','15b:6','וכן אתה מוצא במנודה ובאבל','The teaching includes a comparison with niddui and mourning.','anonymous cited teaching',status='Scope of comparison subsequently restricted.')
u('15b:6','מאי לאו אכולהו לא אשארא','anonymous dialectic','scope inference rejected',composition='composite')
q('bathscopeq','15b:6','מאי לאו אכולהו','Does this comparison include bathing?')
c('bathall','15b:6','מאי לאו אכולהו','The attempted inference extends the comparison to bathing.',mode='rejected',q='bathscopeq')
c('bathother','15b:6','לא אשארא','The reply confines the comparison to other restrictions and leaves niddui bathing unanswered.',q='bathscopeq',status='Defeats proof; no final niddui bathing ruling.')
edge('15b:6','לא אשארא','bathother','bathall','objection');edge('15b:6','לא אשארא','bathother','bathscopeq','answer')
u('15b:6','מצורע מהו ברחיצה תיקו','anonymous dialectic','unresolved inquiry')
q('leperbathq','15b:6','מצורע מהו ברחיצה','May a metzora bathe?',status='none')
c('leperbath','15b:6','מצורע מהו ברחיצה תיקו','Metzora bathing is explicitly unresolved.',mode='unresolved',q='leperbathq');edge('15b:6','תיקו','leperbath','leperbathq','unresolved_outcome')
u('15b:7',None,'anonymous dialectic citing God’s exceptional instruction to Ezekiel','rule and inference',composition='composite')
c('ezekielshoe','15b:7','ונעליך תשים ברגליך','Ezekiel is instructed to put shoes on his feet.','God addressing Ezekiel',cond=['exceptional instruction to Ezekiel'])
c('mournershoe','15b:7','אבל אסור בנעילת הסנדל','Other mourners are prohibited from wearing sandals, inferred from Ezekiel’s exceptional instruction.')
edge('15b:7','מכלל דכולי עלמא אסור','ezekielshoe','mournershoe','support')
a('15b:7','דקאמר ליה רחמנא ליחזקאל','רחמנא','quoted_authority',candidates=['God'],scope='God speaks to Ezekiel; anonymous dialectic draws converse for other mourners.')
q('banshoeq','15b:8','מנודה מהו בנעילת הסנדל','May one under niddui wear sandals?',status='none')
u('15b:8','מנודה מהו בנעילת הסנדל','anonymous dialectic','question')
u('15b:8','אמר רב יוסף תא שמע כשאמרו אסור בנעילת הסנדל לא אמרו אלא בעיר אבל בדרך מותר הא כיצד יצא לדרך נועל נכנס לעיר חולץ וכן אתה מוצא במנודה ובאבל','Rav Yosef citing teaching','attempted answer',composition='composite')
a('15b:8','אמר רב יוסף','רב יוסף',scope='Citer, not original holder of teaching; blanket applicability rejected.')
c('cityshoe','15b:8','כשאמרו אסור בנעילת הסנדל לא אמרו אלא בעיר','The quoted sandal prohibition is confined to town.','anonymous cited teaching',cond=['underlying subject not named locally','in town'])
c('roadshoe','15b:8','אבל בדרך מותר','The quoted teaching permits sandals on the road.','anonymous cited teaching',cond=['underlying subject','on road'])
c('leavingshoe','15b:8','יצא לדרך נועל','When departing onto the road one puts on sandals.','anonymous cited teaching',cond=['departing onto road'])
c('enteringshoe','15b:8','נכנס לעיר חולץ','When entering town one removes sandals.','anonymous cited teaching',cond=['entering town'])
c('alsoshoe','15b:8','וכן אתה מוצא במנודה ובאבל','The teaching compares niddui and mourning.','anonymous cited teaching',status='Comparison scope narrowed; sandal applicability not established.')
u('15b:8','מאי לאו אכולהו לא אשארא','anonymous dialectic','scope inference rejected',composition='composite')
q('shoescopeq','15b:8','מאי לאו אכולהו','Does the comparison apply to all restrictions including sandals?')
c('shoeall','15b:8','מאי לאו אכולהו','The attempted inference includes sandals.',mode='rejected',q='shoescopeq')
c('shoeother','15b:8','לא אשארא','The response confines the comparison to other restrictions, leaving niddui sandals unanswered.',q='shoescopeq',status='No final niddui sandal ruling from this proof.')
edge('15b:8','לא אשארא','shoeother','shoeall','objection');edge('15b:8','לא אשארא','shoeother','shoescopeq','answer')
q('lepershoeq','15b:9','מצורע מהו בנעילת הסנדל','May a metzora wear sandals?',status='none')
c('lepershoe','15b:9',None,'Metzora sandal wearing remains unresolved.',mode='unresolved',q='lepershoeq')
edge('15b:9','תיקו','lepershoe','lepershoeq','unresolved_outcome')
# Final pre-freeze semantic/evidence audit additions: distinguish scriptural voice,
# retain the two separate unresolved populations, and make each omission pass concrete.
a('15b:1','דמות דיוקני נתתי בהן','divine first-person voice','quoted_authority',candidates=['God as voiced in Bar Kappara teaching'],chain=['Bar Kappara','embedded divine voice'],scope='First-person rationale, not a claim that Bar Kappara created people.')
a('15b:2','(עמוס ח, י) והפכתי חגיכם לאבל','Amos 8:10','quoted_authority',scope='Verse cited by anonymous dialectic as warrant for festival/mourning analogy.')
a('15b:5','(שמואל ב יד, ב) ואל תסוכי שמן','2 Samuel 14:2','quoted_authority',scope='Cited instruction to the woman of Tekoa; not a ruling spoken by an amora named Shmuel.')
c('banbedonly','15b:1','מנודה ומצורע מה הן בכפיית המטה תיקו','The bed-overturning obligation of one under niddui remains unresolved.',cond=['niddui'],mode='unresolved',q='banbedq')
c('leperbedonly','15b:1','מנודה ומצורע מה הן בכפיית המטה תיקו','The bed-overturning obligation of a metzora remains unresolved.',cond=['metzora'],mode='unresolved',q='banbedq')
edge('15b:1','תיקו','banbedonly','banbedq','unresolved_outcome');edge('15b:1','תיקו','leperbedonly','banbedq','unresolved_outcome')
for rr,nn in {
 '13b:8':'Checked quoted impurity rule, split-grain explanation, susceptibility premise and objection to כונתא against 13b:7 identities. Anonymous critic is not Abaye by default.',
 '13b:9':'Checked peeled-product restriction, required water soaking, etymological question and answer separately; this resolves first objection only.',
 '13b:11':'Checked narrator report of Rav Huna action, Rav Kahana as citer/objector, and stoa rule; read continuation for fruit/spice qualification.',
 '13b:12':'Checked public-road opening restriction, final festival eve exception, reason of honor, and restrictive inference; not unrestricted public trade.',
 '13b:13':'Checked fruit/spice distinction against both preceding cases; no assertion that Rav Huna retracts.',
 '13b:15':'Enumerated seven haircut classes with release/purification conditions; source chapter opening and anonymous Mishnah preserved. Nazir purification qualifier is explicitly flagged.',
 '13b:16':'Enumerated three laundry classes and read 14a:1–2 to retain continuing list; these are not separate haircut rules.',
 '14a:1':'Two laundry classes retain the governing predicate from 13b:16. Read 14a:2 list completion and 14a:3–10 rationale/context; these context items receive no sampled-core credit.',
 '14a:12':'Travel purpose distinguishes shared prohibitions/permissions from profit dispute. Rava reports categories, not original authorship; holders identified with 14a:11 and explicit 14a:15 continuation.',
 '14a:13':'Retained Rabbi quotation separately from anonymous unauthorized-travel alternative testing; rejected pleasure/subsistence suggestions and provisional profit identification preserved.',
 '14a:14':'Retained authorized-travel question and both failed candidates; circular consequence is objection under initial reading, not final interpretation.',
 '14a:16':'Separated Shmuel newborn permission, womb/prison rationale and anonymous exclusion of earlier birth; second transmitted version not merged.',
 '14a:17':'Pinhas cites a permission teaching and derives converse. Citer distinct from original unnamed authority; converse marked rejected by Rav Ashi, not a maintained rule.',
 '14b:1':'Conditional consequence depends jointly on birth distinction and inferred converse; no independently asserted child mourning duty.',
 '14b:2':'Baraita grief rationale retained; implication against minor mourning duty distinguished from exact text.',
 '14b:3':'Rav Ashi interrogates actual wording and supplies mixed-class possibility. No unsupported enumeration of prohibited/permitted cases.',
 '15a:24':'Explicit metzora rending query, Leviticus evidence, interpretive gloss and שמע מינה answer retained.',
 '15a:25':'Bed obligation and Bar Kappara attribution are distinct; following segment completes the teacher’s cited rationale.',
 '15b:1':'Three parts of embedded divine speech retained; Bar Kappara is teacher, not divine speaker. Bed query covers niddui and metzora; both unresolved, not prohibited by inference.',
 '15b:2':'Checked Amos quotation, festival premise and mourning conclusion with typed analogy/support; not a Rav/Shmuel dispute.',
 '15b:3':'Checked niddui-work query, Rav Yosef citation, daytime/night conditions, comparison, all-restrictions proposal and rejection. Subject of underlying cited rule not supplied locally; no invented holder.',
 '15b:4':'New proof explicitly permits study/being taught and hiring/being hired; work answer established by שמע מינה. Separate metzora work inquiry ends תיקו.',
 '15b:5':'Mourner bathing rule derives via cited anointing ban plus inclusion premise. Biblical Samuel reference is not amora Shmuel.',
 '15b:6':'Whole-body prohibition and face/hands/feet exception are quoted conditions. Applying them to niddui is a defeated proof; metzora query explicitly unresolved. No final negative answer fabricated.',
 '15b:7':'God’s exceptional shoe instruction to Ezekiel is separated from anonymous generalization to other mourners.',
 '15b:8':'Town/road conditions and departure/entry examples each retained. Rav Yosef cites, anonymous dialectic rejects universal comparison. Read 15b:9–18; next question concerns metzora, not a belated niddui sandal answer.'
}.items():note(rr,nn)
# Anonymous and collective attribution is explicitly inventoried even where no named authority appears.
for r in j['core_refs']:
 if r.endswith('13b:14'):continue
 us=[x for x in records if x['layer']=='utterances' and x['evidence'][0]['segment_id']==r]
 for x in us:
  if x['content']['textual_voice'].startswith(('anonymous','cited','Pinhas objection')):
   e=x['evidence'][0];a(r,e['quote'],x['content']['textual_voice'],'anonymous',scope=x['content']['discourse_role'],links=[x['id']])
# Primary structure is a complete literal partition at original segment granularity.
for r in j['core_refs']:
 short=r.replace('Moed Katan ','')
 title=('chapter closing formula' if short=='13b:14' else 'Mishnah eligibility list' if short in ['13b:15','13b:16','14a:1'] else 'source discourse segment: '+short)
 boundary='closed' if short in ['13b:13','13b:14','14a:15','14b:3','15a:24','15b:2','15b:5','15b:7'] else 'open_both'
 rec('structure',r,None,dict(title=title,primary=True,boundary=boundary,legacy_ids=[]),origin='literal')
layers=['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']
coverage=[]
for r in j['core_refs']:
 for layer in layers:
  ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==r for e in x['evidence'])]
  if layer=='reconciliation':
   rationale=notes.get(r,'Source-based omission pass checked every clause, conditions, speaker versus citer, anonymous argument, query alternatives, local status, and necessary continuation. Retained stated rulings separately from inference and rejected proofs; no current practical halacha inferred.')
   result='none_found_after_pass'
  elif ids:rationale='Source-anchored independent inventory; exact Unicode evidence retained.';result='records_found'
  else:
   result='not_applicable' if r.endswith('13b:14') else 'none_found_after_pass'
   rationale='Chapter closing formula only.' if r.endswith('13b:14') else {'questions':'No explicit question in this segment after source pass; no editorial query invented.','edges':'No additional supported local argument relation; list membership or standalone statement is not automatically an argumentative edge.','positions':'No maintained or locally tested proposition distinct from recorded material.','attributions':'No additional named speaker beyond inventoried anonymous material.','utterances':'No discourse utterance beyond paratext.'}.get(layer,'No record found after source pass.')
  coverage.append(dict(segment_id=r,layer=layer,extraction_state='completed',extraction_result=result,record_ids=ids,rationale=rationale))
proposal=dict(schema_version='2.0.0-production',tractate='Moed Katan',owner='/root/mk_source_review047',epoch=1,source_sha256=j['source']['sha256'],protocol_sha256=j['common_documents'][0]['sha256'],schema_sha256=j['common_documents'][1]['sha256'],execution=dict(route='interactive_agent',agent_id='/root/mk_source_review047',model_id=None),records=records,coverage=coverage,open_tails=['No unique final Shmuel version selected; both transmitted formulations and Rav Ashi counter-inferences preserved.','13b:10 קשיא remains local unresolved objection to כונתא.','Niddui bathing and sandals are not resolved by rejected comparison proofs; metzora bed/work/bath/sandals explicitly תיקו.'])
# Reading log includes all displayed original segments, not just the selected supporting excerpts.
readrefs=[r for r in texts if 25<=coords[r][0]<=29]
context=[r for r in readrefs if r not in j['core_refs']]
annotated_context=sorted({e['segment_id'] for x in records for e in x['evidence']} - set(j['core_refs']),key=lambda r:coords[r])
out=dict(artifact_kind='frozen_independent_source_only_reading',job_id=j['job_id'],agent_id='/root/mk_source_review047',freshfork='none',model_id=None,model_observation='Unknown; no model identity supplied by runtime.',blindness=dict(source_only=True,producer_annotations_seen=False,prior_readings_seen=False,annotated_handoff_seen=False,paid_api_calls=0,comparison_performed=False),job_sha256=H(JOB.read_bytes()),bindings=bindings,plan_sha256=j['plan_sha256'],core_refs=j['core_refs'],selected_blocks=j['selected_blocks'],context_read_refs=context,context_semantically_annotated_refs=annotated_context,source_coordinate_map={r:dict(page_index=coords[r][0],segment_index=coords[r][1],unicode_length=len(texts[r]),sha256_utf8=H(texts[r].encode())) for r in j['core_refs']+context},source_attribution={k:source[k] for k in ['title','versionTitle','versionSource','license']},sample_accounting=dict(core_count=len(j['core_refs']),context_read_count=len(context),context_annotated_count=len(annotated_context),context_counts_as_core=False,cohort='original_probability_sample'),semantic_audit=dict(completed_before_initial_freeze=True,checks=['All 30 originals reread against claims and conditions.','Mishnah haircut/laundry classes independently enumerated; cross-page predicate retained.','Rabbi versus Rabbi Yehuda distinguished; anonymous rejected interpretations not final positions.','Both Shmuel formulations and alternative transmitter maintained; supporting and opposing converse arguments both defeated.','Bar Kappara teacher distinct from embedded divine voice.','Rav Yosef citer distinct from original teaching and anonymous scope rejection.','No inference from unresolved or missing answer to a negative scholar position.','Chapter ending excluded from semantic propositions.'],limitations=['AI provisional source reading, not human certification.','Structure ownership uses source segments; semantic utterances may be finer.','Context is read for core interpretation, not claimed as full eight-layer context coverage.']),release=dict(additive_next_release_only=True,current_release015_changed=False,full_admission=False,ml_eligible=False,task_eligibility_granted=False),proposal=proposal)
jsonschema.Draft202012Validator(schema).validate(proposal)
ids={x['id'] for x in records};assert len(ids)==len(records)
for x in records:
 for e in x['evidence']:assert texts[e['segment_id']][e['start_char']:e['end_char']]==e['quote']
 assert set(x['links'])<=ids
 if x['layer']=='positions':assert x['content']['claim_id'] in ids and (x['content']['question_id'] is None or x['content']['question_id'] in ids)
 if x['layer']=='edges':assert {x['content']['source_id'],x['content']['target_id']}<=ids
assert len(coverage)==240 and len(set(j['core_refs']))==30
for r in j['core_refs']:
 owned=[e for x in records if x['layer']=='structure' and x['content']['primary'] for e in x['evidence'] if e['segment_id']==r]
 assert [(e['start_char'],e['end_char']) for e in owned]==[(0,len(texts[r]))]
 assert {v['layer'] for v in coverage if v['segment_id']==r}==set(layers)
for v in coverage:assert set(v['record_ids'])<=ids and v['rationale']
counts=dict(collections.Counter(x['layer'] for x in records))
payload=(json.dumps(out,ensure_ascii=False,indent=2)+'\n').encode();digest=H(payload)
receipt=dict(validation='PASS',job_id=j['job_id'],artifact_sha256=digest,helper_sha256=H(pathlib.Path(__file__).read_bytes()),checks=['job and every pinned original/common/plan hash','canonical domain-separated plan hash','all three block memberships and source spans','production schema applied to proposal payload','every Unicode quote and interval','record ids and link referential integrity','30 exact cores and 240 core-layer rows','complete nonoverlapping primary ownership','explicit zero-result and reconciliation rationales'],record_counts=counts,record_total=len(records),core_count=30,context_read_count=len(context),context_annotated_count=len(annotated_context),semantic_certification=False)
if '--freeze' in sys.argv:
 target=ROOT/'moed_katan_delegated047.json'
 with target.open('xb') as f:f.write(payload)
 with (ROOT/'moed_katan_delegated047.json.sha256').open('x',encoding='utf8') as f:f.write(digest+'  '+target.name+'\n')
 with (ROOT/'validation_receipt047.json').open('x',encoding='utf8') as f:json.dump(receipt,f,ensure_ascii=False,indent=2);f.write('\n')
 with (ROOT/'author_validate047.py.sha256').open('x',encoding='utf8') as f:f.write(receipt['helper_sha256']+'  author_validate047.py\n')
elif (ROOT/'moed_katan_delegated047.json').exists():assert (ROOT/'moed_katan_delegated047.json').read_bytes()==payload
print(json.dumps(receipt,ensure_ascii=False,indent=2))
