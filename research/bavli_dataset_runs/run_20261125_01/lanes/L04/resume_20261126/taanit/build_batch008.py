"""Manually authored from pinned original 6a:2–6b:6; not a semantic extractor."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[7]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=pathlib.Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_taanit')
j,ss=runner.load(JOB)
assert runner.read(JOB/'CURRENT.json')['snapshot_sha256']=='bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a'
assert runner.read(JOB/'OWNER.json')==dict(owner='L04/taanit_resume_20261126',epoch=3)
ix={s['ref'].replace('Taanit ',''):s for s in ss.values()}
P={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
P.update(owner='L04/taanit_resume_20261126',epoch=3,execution=dict(route='interactive_agent',agent_id='/root/taanit_continuation_2',model_id=None),records=[],coverage=[],open_tails=[])
def ev(r,t=None):
 s=ix[r];t=s['text'] if t is None else t;a=s['text'].index(t);return dict(segment_id=s['id'],start_char=a,end_char=a+len(t),quote=t)
def add(k,l,r,c,t=None,links=None,unc=None,origin='source_paraphrase'):
 rid='ta.resume008.'+k;P['records'].append(dict(id=rid,layer=l,evidence=[ev(r,t)],content=c,origin=origin,links=links or [],uncertainty=unc or []));return rid
def attr(k,r,target,who,t,chain=None,role=None):
 ch=chain or [];a=add(k+'.a','attributions',r,dict(surface=who or 'anonymous',role=role or ('speaker' if who else 'anonymous'),candidates=[who] if who else [],scope=target,transmission_chain=ch),t,[target])
 for n,person in enumerate(ch[:-1]):add(k+'.tx'+str(n),'attributions',r,dict(surface=person,role='transmitter',candidates=[person],scope=target,transmission_chain=ch),t,[target])
 return a
def c(k,r,t,p,who=None,cond=None,mode='asserted',status=None,chain=None,voice=None,comp='atomic',unc=None):
 cond=cond or [];cid=add(k,'claims',r,dict(proposition=p,conditions=cond,scope='Taanit '+r+' local discussion',assertion_mode=mode),t,unc=unc)
 add(k+'.u','utterances',r,dict(textual_voice=voice or who or 'anonymous discussion',discourse_role=mode,composition=comp),t,[cid],unc)
 attr(k,r,cid,who,t,chain)
 add(k+'.p','positions',r,dict(holder_candidates=[who] if who else [],claim_id=cid,question_id=None,conditions=cond,local_status=status or mode+' locally; no later halakhic adjudication inferred'),t,[cid],unc)
 return cid
def q(k,r,t,p,who=None,voice=None):
 x=add(k,'questions',r,dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'),t)
 add(k+'.u','utterances',r,dict(textual_voice=voice or who or 'anonymous discussion',discourse_role='question',composition='atomic'),t,[x]);attr(k,r,x,who,t);return x
def e(k,r,t,a,b,rel='support'):
 return add(k,'edges',r,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),t,[a,b])
A=c('yoreh.instruct','6a:2','יורה שמורה את הבריות להטיח גגותיהן ולהכניס את פירותיהן ולעשות כל צרכיהן','Yoreh instructs people to plaster roofs, bring in produce and attend to their needs.',voice='anonymous baraita',comp='composite')
B=c('yoreh.soak','6a:2','דבר אחר שמרוה את הארץ ומשקה עד תהום','Alternatively, yoreh saturates the earth and waters down to the deep.',voice='anonymous baraita',comp='composite')
V=c('psalm.soak','6a:2','שנאמר (תהלים סה, יא) תלמיה רוה נחת גדודיה ברביבים תמוגגנה צמחה תברך','Psalm 65:11 describes watering furrows, settling ridges, softening with showers and blessing growth.',voice='biblical quotation',comp='composite');e('soak.proof','6a:2','שנאמר (תהלים סה, יא) תלמיה רוה נחת גדודיה ברביבים תמוגגנה צמחה תברך',V,B)
C=c('yoreh.gentle','6a:2','דבר אחר יורה שיורד בנחת ואינו יורד בזעף','Another explanation is that yoreh falls gently, without fury.',voice='anonymous baraita')
D=q('yoreh.damage.q','6a:3','או אינו יורה אלא שמשיר את הפירות ומשטיף את הזרעים ומשטיף את האילנות','Could yoreh instead mean shedding fruit and washing away seeds and trees?',voice='baraita rhetorical question')
E=c('yoreh.blessing','6a:3','ת"ל מלקוש מה מלקוש לברכה אף יורה לברכה','The baraita analogizes yoreh to malkosh: both are for blessing.',voice='anonymous baraita');e('yoreh.answer','6a:3','ת"ל מלקוש מה מלקוש לברכה אף יורה לברכה',E,D,'answer')
F=q('malkosh.damage.q','6a:3','או אינו מלקוש אלא שמפיל את הבתים ומשבר את האילנות ומעלה את הסקאין','Could malkosh instead mean collapsing houses, breaking trees and raising the סקאין?',voice='baraita rhetorical question')
G=c('malkosh.blessing','6a:3','ת"ל יורה מה יורה לברכה אף מלקוש לברכה','The baraita analogizes malkosh to yoreh: both are for blessing.',voice='anonymous baraita');e('malkosh.answer','6a:3','ת"ל יורה מה יורה לברכה אף מלקוש לברכה',G,F,'answer')
H=q('yoreh.basis.q','6a:4','ויורה גופיה מנלן','What establishes that yoreh itself is a blessing?')
I=c('joel.blessing','6a:4',"דכתיב (יואל ב, כג) ובני ציון גילו ושמחו בה' אלהיכם כי נתן לכם את המורה לצדקה ויורד לכם גשם מורה ומלקוש בראשון:",'Joel’s exhortation to rejoice in the rain given for righteousness supports yoreh’s beneficial character.',voice='anonymous explanation quoting Scripture',comp='composite');e('yoreh.basis.answer','6a:4',ix['6a:4']['text'],I,H,'answer');e('yoreh.basis.support','6a:4',ix['6a:4']['text'],I,E)
J=c('months.first','6a:5','ת"ר יורה במרחשון ומלקוש בניסן','A baraita places yoreh in Marheshvan and malkosh in Nisan.',voice='anonymous baraita',comp='composite')
K=q('months.alternative.q','6a:5','אתה אומר יורה במרחשון ומלקוש בניסן או אינו אלא יורה בתשרי ומלקוש באייר','Why Marheshvan/Nisan rather than Tishri/Iyyar?',voice='baraita rhetorical question')
L=c('months.timely','6a:5','ת"ל בעתו','The word בעתו is offered to support the stated season.',voice='anonymous baraita');e('months.answer','6a:5','ת"ל בעתו',L,K,'answer');e('months.support','6a:5',ix['6a:5']['text'],L,J)
M=c('malkosh.hardness','6a:6','אמר רב נהילאי בר אידי אמר שמואל דבר שמל קשיותיהן של ישראל','Shmuel explains malkosh as removing Israel’s hardness.',who='Shmuel',chain=['Rav Nehilai bar Idi','Shmuel'])
N=c('malkosh.filling','6a:6',"דבי ר' ישמעאל תנא דבר שממלא תבואה בקשיה",'The school of Rabbi Yishmael teaches that malkosh fills grain in its stalks.',voice='school of Rabbi Yishmael')
O=c('malkosh.ears','6a:6','במתניתא תנא דבר שיורד על המלילות ועל הקשין','Another baraita describes rain falling on ears and stalks.',voice='anonymous baraita',comp='composite')
# School is a collective voice, not an identified personal position of Rabbi Yishmael.
next(r for r in P['records'] if r['id']==N+'.a')['content'].update(surface="דבי ר' ישמעאל",role='collective',candidates=[])
P1=c('months.second','6a:7','ת"ר יורה במרחשון ומלקוש בניסן','A further baraita again places yoreh in Marheshvan and malkosh in Nisan.',voice='anonymous baraita',comp='composite')
Pq=q('kislev.q','6a:7','אתה אומר יורה במרחשון או אינו אלא בחדש כסליו','Could yoreh instead be in Kislev?',voice='baraita rhetorical question')
P2=c('timeliness.analogy','6a:7','ת"ל (דברים יא, יד) בעתו יורה ומלקוש מה מלקוש בעתו אף יורה בעתו','The baraita reads בעתו to compare timely yoreh with timely malkosh.',voice='anonymous baraita');e('kislev.answer','6a:7','ת"ל (דברים יא, יד) בעתו יורה ומלקוש מה מלקוש בעתו אף יורה בעתו',P2,Pq,'answer');e('timeliness.support','6a:7',ix['6a:7']['text'],P2,P1)
P3=c('postnisan','6a:7','(כיון שיצא ניסן וירדו גשמים אינו סימן ברכה)','Rain after Nisan has ended is not a sign of blessing.',cond=['Nisan has ended'],voice='parenthetical source teaching',unc=['Parenthetical status preserved; no named authority assigned.'])
Q=c('meir.months','6a:8','יורה במרחשון ומלקוש בניסן דברי ר"מ','Rabbi Meir places yoreh in Marheshvan and malkosh in Nisan.',who='Rabbi Meir',comp='composite')
R=c('sages.kislev','6a:8','וחכמים אומרים יורה בכסליו','The Sages place yoreh in Kislev.',voice='Sages collective')
next(r for r in P['records'] if r['id']==R+'.a')['content'].update(surface='חכמים',role='collective',candidates=[])
Rq=q('sages.identity.q','6a:9','מאן חכמים','Who are the Sages in the preceding teaching?')
R2=c('sages.yosi','6a:9',"אמר רב חסדא ר' יוסי היא",'Rav Hisda identifies the Sages as Rabbi Yosi.',who='Rav Hisda');e('sages.answer','6a:9',"אמר רב חסדא ר' יוסי היא",R2,Rq,'answer');e('sages.identity','6a:9',"אמר רב חסדא ר' יוסי היא",R2,R,'qualification')
S=c('meir.dates','6a:9','דתניא איזו היא רביעה ראשונה הבכירה בשלשה במרחשון בינונית בשבעה בו אפילה בשבעה עשר בו דברי ר"מ','Rabbi Meir gives the early, intermediate and late rainfall dates as 3, 7 and 17 Marheshvan.',who='Rabbi Meir',comp='composite',unc=['Source calls these timings of רביעה ראשונה; later discussion uses first/second/third rainfall terminology. Preserve wording rather than silently harmonizing.'])
T=c('yehuda.dates','6a:9',"ר' יהודה אומר בשבעה ובי\"ז ובעשרים ושלשה",'Rabbi Yehuda gives 7, 17 and 23 Marheshvan.',who='Rabbi Yehuda',comp='composite')
U=c('yosi.dates','6a:10',"ר' יוסי אומר בי\"ז ובעשרים ושלשה ובראש חדש כסליו",'Rabbi Yosi gives 17 and 23 Marheshvan and the new moon of Kislev.',who='Rabbi Yosi',comp='composite');e('yosi.identification.support','6a:10',ix['6a:10']['text'],U,R2)
U2=c('yosi.fast','6a:10',"וכן היה ר' יוסי אומר אין היחידים מתענין עד שיגיע ראש חדש כסליו",'Rabbi Yosi says individuals do not fast until the new moon of Kislev arrives.',who='Rabbi Yosi',cond=['new moon of Kislev has arrived'])
W=c('hisda.yosi','6a:11',"אמר רב חסדא הלכה כר' יוסי",'In the first report Rav Hisda rules like Rabbi Yosi.',who='Rav Hisda',status='explicit halakhic ruling in first transmission; alternative report follows')
W2=c('ask.third','6a:11','בשלשה במרחשון שואלין את הגשמים','In the teaching used by Amemar’s alternative report, rain is requested from 3 Marheshvan.',voice='anonymous teaching quoted in alternative transmission',cond=['3 Marheshvan'])
W3=c('gamliel.seventh','6a:11','רבן גמליאל אומר בשבעה בו','Rabban Gamliel says from 7 Marheshvan.',who='Rabban Gamliel',cond=['7 Marheshvan'])
W4=c('hisda.gamliel','6a:11','אמר רב חסדא הלכה כרבן גמליאל','In Amemar’s version Rav Hisda rules like Rabban Gamliel regarding the request for rain.',who='Rav Hisda',chain=['Amemar','Rav Hisda'],status='explicit ruling in alternative report, not an asserted retraction of first report')
e('hisda.variant','6a:11',ix['6a:11']['text'],W4,W,'qualification')
X=c('seven.days','6a:12','ר"ש בן גמליאל אומר גשמים שירדו שבעה ימים זה אחר זה אתה מונה בהן רביעה ראשונה ושניה ושלישית','Rabban Shimon ben Gamliel says seven consecutive days of rain can count as first, second and third rainfall.',who='Rabban Shimon ben Gamliel',cond=['rain on seven consecutive days'])
Xq=q('seven.days.q','6a:12','כמאן אזלא הא דתניא','Whose timetable accords with the seven-consecutive-days teaching?')
X2=c('seven.yosi','6a:12',"כמאן כר' יוסי",'The discussion aligns the teaching with Rabbi Yosi.');e('seven.answer','6a:12',"כמאן כר' יוסי",X2,Xq,'answer')
X3=c('hisda.yosi.repeat','6a:12',"אמר רב חסדא הלכה כר' יוסי",'Rav Hisda is again reported to rule like Rabbi Yosi in this context.',who='Rav Hisda',status='explicit local halakhic ruling; separate occurrence retained')
Y=c('rainfall.uses','6a:13','בשלמא רביעה ראשונה לשאול שלישית להתענות','The discussion accepts requesting rain as the first rainfall’s significance and fasting as the third’s.',comp='composite')
Yq=q('second.use.q','6a:13','שניה למאי','What is the second rainfall significant for?')
Z=c('zeira.vows','6a:13',"אמר ר' זירא לנדרים",'Rabbi Zeira answers: for vows.',who='Rabbi Zeira');e('vows.answer','6a:13',"אמר ר' זירא לנדרים",Z,Yq,'answer')
Z2=c('vows.rule','6b:1',ix['6b:1']['text'],'For a vow phrased until the rains or from when rains fall, the cited Mishnah sets the second rainfall as the threshold.',voice='quoted Mishnah',cond=['vow referring to the rains'],unc=['Compact quoted syntax preserved; no extension to other vow formulations.']);e('vows.support','6b:1',ix['6b:1']['text'],Z2,Z)
A2=c('zevid.olives','6b:2','רב זביד אמר לזיתים','Rav Zevid answers: for olives.',who='Rav Zevid');e('olives.answer','6b:2','רב זביד אמר לזיתים',A2,Yq,'answer')
A3=c('gifts.leket','6b:2','דתנן מאימתי כל אדם מותרין בלקט בשכחה ובפאה משילכו הנמושות','The cited Mishnah permits everyone leket, shikhha and peah after the נמושות have passed.',voice='quoted Mishnah',cond=['נמושות have passed'],comp='composite')
A4=c('gifts.grapes','6b:2','בפרט ובעוללות משילכו עניים בכרם ויבואו','For peret and olelot, the threshold is after poor people have gone through the vineyard and returned.',voice='quoted Mishnah',cond=['poor have gone through vineyard and returned'],comp='composite')
A5=c('gifts.olives','6b:2','בזיתים משתרד רביעה שניה','For olives, the threshold is the second rainfall.',voice='quoted Mishnah',cond=['second rainfall']);e('olives.support','6b:2',ix['6b:2']['text'],A5,A2)
Bq=q('nemushot.q','6b:3','מאי נמושות','What are נמושות?')
B1=c('nemushot.yohanan','6b:3',"אמר ר' יוחנן סבי דאזלי אתיגרא",'Rabbi Yohanan identifies them as elderly people walking with support.',who='Rabbi Yohanan');e('nemushot.answer1','6b:3',"אמר ר' יוחנן סבי דאזלי אתיגרא",B1,Bq,'answer')
B2=c('nemushot.lakish','6b:3','ר"ל אמר לקוטי בתר לקוטי','Resh Lakish identifies them as gleaners following gleaners.',who='Resh Lakish');e('nemushot.answer2','6b:3','ר"ל אמר לקוטי בתר לקוטי',B2,Bq,'answer')
C1=c('papa.paths','6b:4','רב פפא אמר כדי להלך בשבילי הרשות','Rav Pappa answers: for walking on permissively accessible paths.',who='Rav Pappa');e('paths.answer','6b:4','רב פפא אמר כדי להלך בשבילי הרשות',C1,Yq,'answer')
C2=c('paths.rule','6b:4','דאמר מר מהלכין כל אדם בשבילי הרשות עד שתרד רביעה שניה','The cited teaching permits everyone to walk on those paths until the second rainfall.',voice='anonymous quoted teaching',cond=['before second rainfall']);e('paths.support','6b:4',ix['6b:4']['text'],C2,C1)
D1=c('nahman.burn','6b:5','רב נחמן בר יצחק אמר לבער פירות שביעית','Rav Nahman bar Yitzhak answers: for removal of seventh-year produce.',who='Rav Nahman bar Yitzhak');e('seventh.answer','6b:5','רב נחמן בר יצחק אמר לבער פירות שביעית',D1,Yq,'answer')
D2=c('straw.rule','6b:5','דתנן עד מתי נהנין ושורפין בתבן ובקש של שביעית עד שתרד רביעה שניה','The quoted Mishnah permits benefiting from and burning seventh-year straw and stubble until the second rainfall.',voice='quoted Mishnah',cond=['seventh-year straw and stubble','before second rainfall'],comp='composite');e('seventh.support','6b:5',ix['6b:5']['text'],D2,D1)
Dq=q('seventh.reason.q','6b:6','מאי טעמא','What is the reason for the seventh-year threshold?')
D3=c('animal.verse','6b:6','דכתיב (ויקרא כה, ז) ולבהמתך ולחיה אשר בארצך','The explanation cites Leviticus 25:7 joining domestic animals and wild animals in the land.',voice='biblical quotation')
D4=c('animal.available','6b:6','כל זמן שחיה אוכלת בשדה האכל לבהמתך בבית','While wild animals eat in the field, feed your domestic animals at home.',cond=['wild animals still eat in the field'])
D5=c('animal.exhausted','6b:6','כלה לחיה מן השדה כלה לבהמתך מן הבית','Once food is exhausted for wild animals in the field, remove it for domestic animals from home.',cond=['food exhausted for wild animals in the field'])
e('animal.interpretation1','6b:6',ix['6b:6']['text'],D3,D4);e('animal.interpretation2','6b:6',ix['6b:6']['text'],D3,D5);e('seventh.reason.answer','6b:6',ix['6b:6']['text'],D5,Dq,'answer');e('seventh.reason.support','6b:6',ix['6b:6']['text'],D5,D2)
# Explicit questions nested within cited teachings remain questions as well as rules.
Sq=q('dates.definition.q','6a:9','איזו היא רביעה ראשונה','What is the first rainfall?',voice='quoted baraita')
e('dates.definition.answer','6a:9',ix['6a:9']['text'],S,Sq,'answer')
Aq=q('gifts.threshold.q','6b:2','מאימתי כל אדם מותרין בלקט בשכחה ובפאה','From when may everyone take leket, shikhha and peah?',voice='quoted Mishnah')
e('gifts.threshold.answer','6b:2',ix['6b:2']['text'],A3,Aq,'answer')
Dq2=q('straw.until.q','6b:5','עד מתי נהנין ושורפין בתבן ובקש של שביעית','Until when may seventh-year straw and stubble be used and burned?',voice='quoted Mishnah')
e('straw.until.answer','6b:5',ix['6b:5']['text'],D2,Dq2,'answer')
# Include the explicit Amemar framing in transmission evidence, not just the final ruling.
for r in P['records']:
 if r['layer']=='attributions' and r['content']['scope']==W4:r['evidence']=[ev('6a:11')]
# A verse is quoted text, never a named holder in the person projections.
for cid in [V,D3]:
 next(r for r in P['records'] if r['id']==cid+'.a')['content'].update(surface='scriptural quotation',role='quoted_authority',candidates=[])
refs=list(ix);refs=refs[refs.index('6a:2'):refs.index('6b:6')+1]
for k,title,first,last in [('rainterms','Yoreh and malkosh: names, blessing and seasons','6a:2','6a:8'),('dates','Rainfall dates, alternative Hisda report and seven consecutive days','6a:9','6a:12'),('secondrain','Practical thresholds of second rainfall and seventh-year removal','6a:13','6b:6')]:
 rid=add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'6a:2':'Three interpretations, practical preparations and psalm proof retained.','6a:3':'Both damaging alternatives are rhetorical questions, with reciprocal blessing replies.','6a:4':'Question about original blessing premise and Joel proof retained.','6a:5':'Stated months, rejected alternative-month question and בעתו proof retained.','6a:6':'Three word explanations and Nehilai–Shmuel transmission distinguished; school not equated with individual.','6a:7':'Repeated seasonal baraita, Kislev alternative, timing analogy and parenthetical post-Nisan restriction retained.','6a:8':'Meir versus collective Sages retained; continuation identifies Sages.','6a:9':'Hisda identification, all Meir/Yehuda dates and source rainfall terminology retained.','6a:10':'All Yosi dates and individual-fast restriction retained.','6a:11':'First Hisda ruling and Amemar alternative version kept distinct, including rain-request alternatives.','6a:12':'Seven-consecutive-days rule, identification question, Yosi answer and repeated ruling retained.','6a:13':'First/third practical uses, second-rain question and Zeira answer retained across folio.','6b:1':'Vow threshold retained with compact syntax uncertainty.','6b:2':'Zevid answer and all three quoted agricultural-gift categories retained.','6b:3':'Definition question and both named definitions retained.','6b:4':'Pappa answer and quoted path-access time limit retained.','6b:5':'Nahman bar Yitzhak answer and quoted straw/stubble use/burning limit retained.','6b:6':'Reason question, verse and both positive/exhausted-food conditions retained; next rain-name topic read for boundary.'}
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])]
  rationale=('Source reread and omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after this pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch008.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs)),indent=2))
