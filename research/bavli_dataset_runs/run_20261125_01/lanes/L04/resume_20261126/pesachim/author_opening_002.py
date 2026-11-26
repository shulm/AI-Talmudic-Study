"""Manually read continuation 2b:5–3a:9; common-runner proposal only."""
from author_opening_001 import *
records.clear()
old=r.current(JOB)
newrefs=['2b:'+str(i) for i in range(5,16)]+['3a:'+str(i) for i in range(1,10)]
allrefs=core+newrefs
struct=add('b2.lexical','structure',dict(title='Meaning of אור: proposed day/night distinction resolved as local terminology for night',primary=True,boundary='closed',legacy_ids=[]),[ev(x) for x in allrefs],origin='editorial_inference')
records[-1]['supersedes']='pe.r001.lexical'
q='pe.r001.meaning.q';yh='pe.r001.yehuda.c';initial='pe.r001.initial.c'
workq=question('b2.work.q','2b:5','מאימתי ארבעה עשר אסור בעשיית מלאכה','From when is work prohibited on the fourteenth?',status='unreviewed_alternatives')
el=claim('b2.eliezer','2b:5',"ר' אליעזר בן יעקב אומר משעת האור",'Rabbi Eliezer ben Yaakov says from אור; the subsequent reply interprets this as dawn.',holder='רבי אליעזר בן יעקב',conditions=['work on the fourteenth'],scope='Quoted work prohibition, not the leaven-search timing')
ye=claim('b2.yehuda','2b:5','רבי יהודה אומר משעת הנץ החמה','Rabbi Yehuda says from sunrise.',holder='רבי יהודה',conditions=['work on the fourteenth'],scope='Quoted work prohibition')
edge('b2.el.answer',el,workq,'answer','2b:5');edge('b2.ye.answer',ye,workq,'answer','2b:5')
oq=question('b2.elchallenge.q','2b:6','וכי היכן מצינו יום שמקצתו אסור בעשיית מלאכה ומקצתו מותר בעשיית מלאכה','Where do we find a day partly prohibited and partly permitted for work?')
obj=claim('b2.elchallenge','2b:6','אמר ליה ר"א בן יעקב לרבי יהודה וכי היכן מצינו יום שמקצתו אסור בעשיית מלאכה ומקצתו מותר בעשיית מלאכה','Rabbi Eliezer ben Yaakov challenges a work prohibition that divides the daytime.',holder='רבי אליעזר בן יעקב',mode='challenged',scope='Objection to sunrise boundary')
edge('b2.elchallenge.edge',obj,ye,'objection','2b:6')
hametz=claim('b2.hametz','2b:6','אמר ליה הוא עצמו יוכיח שמקצתו מותר באכילת חמץ ומקצתו אסור באכילת חמץ','Rabbi Yehuda answers that the fourteenth itself is partly permitted and partly forbidden for eating leaven.',holder='רבי יהודה',conditions=['fourteenth of Nisan'],scope='Analogical answer; later distinction limits analogy')
edge('b2.hametz.answer',hametz,oq,'answer','2b:6');edge('b2.hametz.analogy',hametz,ye,'analogy','2b:6')
ni=claim('b2.nightinference','2b:7','מדקאמר רבי יהודה משעת הנץ החמה אלמא אור דקאמר ר"א בן יעקב אורתא הוא','The sunrise view is initially used to infer that the contrasting אור means night.',mode='rejected')
edge('b2.nightinference.support',ye,ni,'support','2b:7')
dawn=claim('b2.dawn','2b:7','לא מאי אור עמוד השחר','The response rejects that inference: אור in this source means dawn.',scope='Specific quoted work source, not the opening Mishnah')
edge('b2.dawn.answer',dawn,ni,'answer','2b:7')
question('b2.self.q','2b:8','נימא איהו לנפשיה הא איכא לילה דקא שרי ר"א בן יעקב','Why does his own permission at night not create the same divided period?')
selfobj=claim('b2.self','2b:8',None,'If אור means dawn, Rabbi Eliezer ben Yaakov himself allows night work, apparently weakening his objection to a divided day.',mode='challenged',conditions=['אור is interpreted as dawn'])
edge('b2.self.objection',selfobj,obj,'objection','2b:8')
daynight=claim('b2.daynight','2b:9','ה"ק בשלמא לדידי אשכחנא דקא פלגי רבנן בין יממא לליליא','The Gemara reconstructs his reply: rabbinic law can distinguish day from night.',holder='רבי אליעזר בן יעקב',scope='Anonymous reconstruction of the argument',uncertainty=['הכי קאמר reconstruction, not a separately transmitted utterance'])
fastel=claim('b2.fastel','2b:9',"(דתנן) גבי תענית צבור עד מתי אוכל ושותה עד שיעלה עמוד השחר דברי ר' אליעזר בן יעקב",'Rabbi Eliezer ben Yaakov allows eating and drinking before a communal fast until dawn.',holder='רבי אליעזר בן יעקב',conditions=['communal fast'],scope='Quoted fasting example')
fastrs=claim('b2.fastrs','2b:9',"ר' שמעון אומר עד קרות הגבר",'Rabbi Shimon says until cockcrow.',holder='רבי שמעון',conditions=['communal fast'],scope='Quoted fasting example')
question('b2.fast.q','2b:9','עד מתי אוכל ושותה','Until when may one eat and drink before the communal fast?',conditions=['communal fast'],status='unreviewed_alternatives')
question('b2.divided.q','2b:9','אלא לדידך היכא אשכחנא יממא גופיה דפלגי ביה רבנן','Where do the rabbis divide daytime itself, as your view would require?')
edge('b2.daynight.answer',daynight,selfobj,'answer','2b:9');edge('b2.fast.support',fastel,daynight,'support','2b:9')
reham=claim('b2.rehametz','2b:10','אמר ליה הוא עצמו יוכיח שמקצתו מותר באכילת חמץ ומקצתו אסור באכילת חמץ','Rabbi Yehuda repeats the counterexample of eating leaven on the fourteenth.',holder='רבי יהודה',scope='Repeated occurrence of the reply',conditions=['fourteenth of Nisan'])
question('b2.good.q','2b:10','שפיר קאמר ליה ר\' יהודה לר"א','Is Rabbi Yehuda not answering Rabbi Eliezer correctly?')
torah=claim('b2.torah','2b:10','הכי קאמר ליה רבי אליעזר אמינא לך אנא מלאכה דרבנן ואת אמרת לי חמץ דאורייתא דעד הכא אסר רחמנא ועד הכא שרא רחמנא','The reconstructed Rabbi Eliezer reply distinguishes rabbinic work law from the Torah boundary for leaven, which God set.',holder='רבי אליעזר בן יעקב',scope='Anonymous reconstructed reply distinguishing legal sources')
edge('b2.torah.distinction',torah,reham,'distinction','2b:10')
hours=claim('b2.hours','2b:11','ואידך שעות דרבנן','The other side invokes the rabbinically prohibited hours before the Torah leaven prohibition.',holder='רבי יהודה',scope='Contextual attribution of ואידך in this two-party exchange',uncertainty=['Name is resolved from the immediate alternating dialogue, not printed in this segment.'])
edge('b2.hours.objection',hours,torah,'objection','2b:11')
fence=claim('b2.fence','2b:12','ואידך הרחקה הוא דעבוד רבנן לדאורייתא','The reply treats those rabbinic hours as a protective distance from the Torah prohibition.',holder='רבי אליעזר בן יעקב',scope='Contextual attribution of second ואידך',uncertainty=['Name supplied by local dialogue continuation; no independent naming in this segment.'])
edge('b2.fence.answer',fence,hours,'answer','2b:12')
torch=claim('b2.torch','2b:13','מיתיבי אין משיאין משואות אלא על החדש שנראה בזמנו לקדשו','Torches are raised only for a new moon seen at its proper time for sanctification.',conditions=['new moon seen at its proper time'],scope='Quoted torch procedure')
tq=question('b2.torch.q','2b:13','ואימתי משיאין משואות','When are the torches raised?',status='partial')
tt=claim('b2.torchtime','2b:13','לאור עבורו','The quoted time is אור of its intercalation.',scope='Quoted torch timing; preserve source expression')
tp=claim('b2.torchproof','2b:13','אלמא אור אורתא הוא ש"מ','The discussion accepts the torch source as evidence that אור means night.')
edge('b2.torchtime.answer',tt,tq,'answer','2b:13');edge('b2.torchproof.support',tt,tp,'support','2b:13');edge('b2.torchproof.answer',tp,q,'answer','2b:13')
hands=claim('b2.hands','2b:14','מיתיבי היה עומד כל הלילה ומקריב על המזבח לאורה טעון קידוש ידים ורגלים דברי רבי','Rabbi says that one who stands all night offering on the altar needs hand-and-foot sanctification at אורה.',holder='רבי',conditions=['offered on the altar throughout the night'],scope='Quoted priestly service rule')
aurah=claim('b2.aurah','2b:14','אורה שאני','The reply distinguishes the form אורה from אור, so this source does not decide the same lexical question.')
edge('b2.aurah.distinction',aurah,hands,'distinction','2b:14')
intro=add('b2.marzutra.u','utterances',dict(textual_voice='מר זוטרא',discourse_role='introduces a textual objection continued in 3a:1–2',composition='atomic'),[ev('2b:15')])
add('b2.marzutra.a','attributions',dict(surface='מר זוטרא',role='speaker',candidates=['מר זוטרא'],scope=intro,transmission_chain=[]),[ev('2b:15')],[intro])
bs=claim('b2.birthbs','3a:1','המפלת אור לשמונים ואחד בית שמאי פוטרין מקרבן','Beit Shammai exempt from an offering when miscarriage occurs on אור of the eighty-first day.',holder='בית שמאי',conditions=['miscarriage on אור of day eighty-one'],scope='Quoted offering dispute; medical context not independently expanded')
bh=claim('b2.birthbh','3a:1','ובית הלל מחייבים','Beit Hillel require an offering in that case.',holder='בית הלל',conditions=['miscarriage on אור of day eighty-one'],scope='Quoted offering dispute')
edge('b2.birth.quotation',intro,bs,'quotation','2b:15')
bq=question('b2.birth.q','3a:2','מאי שנא אור שמנים ואחד מיום שמנים ואחד','Why distinguish אור of day eighty-one from its daytime?',status='none')
analogy=claim('b2.birthanalogy','3a:2','אמרו (להן) בית הלל לבית שמאי מאי שנא אור שמנים ואחד מיום שמנים ואחד אם שיוה לו לטומאה לא ישוה לו לקרבן','Beit Hillel argue that equal status for impurity should entail equal status for an offering.',holder='בית הלל',conditions=['equal status for impurity'],scope='Stated analogy; opposing response is not given here')
edge('b2.birthanalogy.support',analogy,bh,'support','3a:2');edge('b2.birthanalogy.objection',analogy,bs,'objection','3a:2')
bp=claim('b2.birthproof','3a:2','מדקאמר ב"ה לב"ש מאי שנא אור שמונים ואחד מיום שמונים ואחד שמע מינה אור אורתא הוא שמע מינה','The contrast between אור and daytime establishes that אור means night in this source.')
edge('b2.birthproof.support',analogy,bp,'support','3a:2');edge('b2.birthproof.answer',bp,q,'answer','3a:2')
eatq=question('b2.eat.q','3a:3','יכול יהא נאכל אור לשלישי','Could the offering be eaten on אור leading into the third day?')
oneday=claim('b2.oneday','3a:3','זבחים נאכלים ליום אחד ושלמים נאכלים לשני ימים','The quoted teaching contrasts sacrifices eaten for one day with peace offerings eaten for two days.',scope='Premises of the quoted sacrificial argument')
eatanalogy=claim('b2.eatanalogy','3a:3','מה להלן לילה אחר היום אף כאן לילה אחר היום','It proposes allowing the night following the final day by analogy to one-day offerings.',mode='rejected',conditions=['analogy to the night following one-day offerings'],scope='Tentative sacrificial extension')
edge('b2.eatanalogy.answer',eatanalogy,eatq,'answer','3a:3')
eatlimit=claim('b2.eatlimit','3a:4','ת"ל (ויקרא יט, ו) ביום זבחכם יאכל וממחרת והנותר עד יום בעוד יום הוא נאכל ואינו נאכל לאור שלישי','The verse is read to allow eating only while still day, excluding אור of the third day.',scope='Quoted verse exposition governing peace-offering consumption',conditions=['peace offerings after the second day'])
edge('b2.eatlimit.objection',eatlimit,eatanalogy,'objection','3a:4');edge('b2.eatlimit.answer',eatlimit,eatq,'answer','3a:4')
burnq=question('b2.burn.q','3a:5','יכול ישרף מיד','Could the leftover be burned immediately after the eating period?')
burnpremise=claim('b2.burnpremise','3a:5','זבחים נאכלין ליום ולילה אחד ושלמים נאכלין לשני ימים ולילה אחד','The argument contrasts a day-and-night eating period with the two days and one night of peace offerings.',scope='Premise for proposed immediate burning')
burnanalogy=claim('b2.burnanalogy','3a:5','מה להלן תיכף לאכילה שריפה אף כאן תיכף לאכילה שריפה','It proposes immediate burning after eating ends, by analogy to the other sacrifices.',mode='rejected',scope='Tentative analogy for burning time')
edge('b2.burnanalogy.answer',burnanalogy,burnq,'answer','3a:5')
burnlimit=claim('b2.burnlimit','3a:6','תלמוד לומר (ויקרא ז, יז) והנותר מבשר הזבח ביום השלישי באש ישרף ביום אתה (שורף) ואי אתה שורפו בלילה','The third-day verse limits burning to daytime and excludes nighttime.',scope='Quoted sacrificial burning rule',conditions=['leftover offering flesh on third day'])
edge('b2.burnlimit.objection',burnlimit,burnanalogy,'objection','3a:6');edge('b2.burnlimit.answer',burnlimit,burnq,'answer','3a:6')
sacproof=claim('b2.sacproof','3a:6','מדקאמר יהא נאכל אור לשלישי אלמא אור אורתא הוא שמע מינה','The proposed third-day אור eating period supplies accepted evidence that אור means night.')
edge('b2.sacproof.support',eatanalogy,sacproof,'support','3a:6');edge('b2.sacproof.answer',sacproof,q,'answer','3a:6')
for key,quote,prop,condition in [
('ykstart','אור של יום הכפורים מתפלל שבע ומתודה','On אור of Yom Kippur one prays seven blessings and confesses.','opening night of Yom Kippur'),
('ykmorning','שחרית מתפלל שבע ומתודה','At the morning prayer one prays seven blessings and confesses.','Yom Kippur morning'),
('ykmusaf','במוסף מתפלל שבע ומתודה','At Musaf one prays seven blessings and confesses.','Yom Kippur Musaf'),
('ykmincha','במנחה מתפלל שבע ומתודה','At Mincha one prays seven blessings and confesses.','Yom Kippur Mincha'),
('ykevening','בערבית מתפלל מעין שמונה עשר','At the following evening prayer one prays an abridgment of eighteen.','evening following Yom Kippur')]:
    claim('b2.'+key,'3a:7',quote,prop,conditions=[condition],scope='Quoted prayer schedule; no missing service inferred')
hc=claim('b2.hanina','3a:7',"ר' חנינא בן גמליאל אומר משום אבותיו מתפלל שמונה עשר שלימות",'Rabbi Hanina ben Gamliel reports in his ancestors’ name that one prays the full eighteen.',holder='אבותיו של רבי חנינא בן גמליאל',chain=['רבי חנינא בן גמליאל','אבותיו'],conditions=['evening following Yom Kippur'],scope='Transmitted alternative to abridged eighteen',uncertainty=['The ancestors are collective and unnamed in this passage.'])
add('b2.hanina.transmitter','attributions',dict(surface="ר' חנינא בן גמליאל אומר משום אבותיו",role='transmitter',candidates=['רבי חנינא בן גמליאל'],scope=hc,transmission_chain=['רבי חנינא בן גמליאל','אבותיו']),[ev('3a:7',"ר' חנינא בן גמליאל אומר משום אבותיו מתפלל שמונה עשר שלימות")],[hc])
hav=claim('b2.havdalah','3a:7','מפני שצריך לומר הבדלה בחונן הדעת','The full prayer is justified by the need to say havdalah in the knowledge blessing.',scope='Rationale in the transmitted prayer alternative',conditions=['evening following Yom Kippur'])
edge('b2.havdalah.support',hav,hc,'support','3a:7','מפני שצריך לומר הבדלה בחונן הדעת')
ykproof=claim('b2.ykproof','3a:7','אלמא אור אורתא הוא שמע מינה','The prayer schedule establishes that אור means night.')
edge('b2.ykproof.support','pe.r001.b2.ykstart.c',ykproof,'support','3a:7');edge('b2.ykproof.answer',ykproof,q,'answer','3a:7')
school=claim('b2.school','3a:8','תא שמע דתני דבי שמואל לילי ארבעה עשר בודקין את החמץ לאור הנר','The school of Shmuel teaches explicitly that leaven is searched by candlelight on the night of the fourteenth.',holder='דבי שמואל',conditions=['night of the fourteenth'],scope='School teaching, not automatically a personal statement of Shmuel')
schoolproof=claim('b2.schoolproof','3a:8','אלמא אור אורתא הוא','The explicit לילי wording establishes the night meaning of אור.')
edge('b2.schoolproof.support',school,schoolproof,'support','3a:8');edge('b2.schoolproof.answer',schoolproof,q,'answer','3a:8')
agreement=claim('b2.agreement','3a:9','אלא בין רב הונא ובין רב יהודה דכולי עלמא אור אורתא הוא ולא פליגי','Both Rav Huna and Rav Yehuda mean night; they do not disagree.',mode='reconciled',scope='Explicit resolution of initial lexical supposition')
local=claim('b2.local','3a:9','מר כי אתריה ומר כי אתריה באתריה דרב הונא קרו נגהי ובאתריה דרב יהודה קרו לילי','Each uses local terminology: Rav Huna’s locale says נגהי and Rav Yehuda’s says לילי.',scope='Explanation of lexical variation')
edge('b2.agreement.resolution',agreement,q,'local_resolution','3a:9');edge('b2.agreement.correction',agreement,initial,'correction','3a:9');edge('b2.local.support',local,agreement,'support','3a:9')

notes2={
'2b:5':'Read both named work-time views and explicit question; dawn gloss comes from 2b:7, not name order.',
'2b:6':'Retained Rabbi Eliezer ben Yaakov objection and Rabbi Yehuda chametz analogy; neither is the amora Rav Yehuda.',
'2b:7':'Night inference rejected; dawn answer limited to this work source, not forced on the opening Mishnah.',
'2b:8':'Retained self-objection against the night/day distinction with its dawn premise.',
'2b:9':'Retained reconstructed day/night response and both fast thresholds; no erasure of Rabbi Shimon alternative.',
'2b:10':'Retained repeated reply and rabbinic/Torah distinction; later practical ruling not inferred.',
'2b:11':'Resolved first other-side response only from immediate alternating dialogue; uncertainty explicitly stored.',
'2b:12':'Resolved second response locally; protective-distance answer retained, not a new rule for work.',
'2b:13':'Retained torch precondition, timing question, timing answer and night inference.',
'2b:14':'Retained Rabbi service rule and lexical distinction אורה; no silent collapse into אור.',
'2b:15':'Standalone introductory utterance and named attribution; semantic content continues 3a:1–2, so no invented independent proposition.',
'3a:1':'Retained both school positions and miscarriage timing condition; no missing response fabricated.',
'3a:2':'Retained impurity/offering analogy, explicit question and lexical inference; no Beit Shammai answer given here.',
'3a:3':'Retained consumption-period premise, tentative nighttime extension and explicit question.',
'3a:4':'Retained scriptural restriction rejecting nighttime extension.',
'3a:5':'Retained burning question, distinct consumption premise and tentative analogy.',
'3a:6':'Retained daytime-only burning restriction and separate accepted lexical inference.',
'3a:7':'Retained five scheduled prayer occasions, transmitted full-prayer alternative, ancestors chain, havdalah rationale and night inference.',
'3a:8':'Retained school teaching without assigning it directly to Shmuel; lexical inference explicit.',
'3a:9':'Retained no-dispute resolution and two local lexical usages, correcting initial assumption.'}
coverage=[]
for ref,note in notes2.items():
    sid=refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Source-based '+layer+' pass; '+('records listed.' if ids else 'no additional independent object after reading.')))
for ref in core:
    coverage.append(dict(segment_id=refs[ref]['id'],layer='structure',extraction_state='completed',extraction_result='records_found',record_ids=[struct],rationale='Previous lexical structure extended through the explicit 3a:9 no-dispute resolution; original partition preserved in superseded version.'))
p=dict(schema_version=r.VERSION,tractate='Pesachim',owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=JOB/'staging'/'opening_002.json';r.immutable(out,r.encoded(p));print(out)
