"""Manual23b8–24a6; next narrative and context read through24a14."""
import pathlib
helper=pathlib.Path(__file__).with_name('build_batch008.py').read_text(encoding='utf-8').split("A=c('yoreh.instruct'")[0]
helper=helper.replace('bf269222667a2403dbfb6b92cfedcbe3f842f578ba83fdb2dd2ebe4d6975292a','59c62a6064a816524290a464e500ca6e82b6b0fe2b540a8f9b385ee533dff776').replace('ta.resume008.','ta.resume050.').replace('/root/taanit_continuation_2','/root/taanit_continuation_5')
exec(compile(helper,__file__,'exec'))
A=c('hanan.children','23b:8','חנן הנחבא בר ברתיה דחוני המעגל הוה כי מצטריך עלמא למיטרא הוו משדרי רבנן ינוקי דבי רב לגביה ונקטי ליה בשיפולי גלימיה ואמרו ליה אבא אבא הב לן מיטרא','Hanan the Hidden, Honi’s daughter’s son, receives schoolchildren sent for rain; they grasp his cloak and call Father, give us rain.',voice='narrative',comp='composite')
B=c('hanan.prayer','23b:8','אמר לפני הקב"ה רבש"ע עשה בשביל אלו שאין מכירין בין אבא דיהיב מיטרא לאבא דלא יהיב מיטרא','Hanan asks God to act for children unable to distinguish the Father who gives rain from a father who does not.',who='Hanan the Hidden')
Bq=q('hanan.name.q','23b:8','ואמאי קרי ליה חנן הנחבא','Why is he called Hanan the Hidden?')
C=c('hanan.hiding','23b:8','מפני שהיה מחביא עצמו בבית הכסא','Because he hid himself in the privy.');e('hanan.name.answer','23b:8',ix['23b:8']['text'],C,Bq,'answer')
D=c('zerika.comparison','23b:9',ix['23b:9']['text'],'Rabbi Zerika tells Rav Safra to compare Israel’s forceful figures and Babylonia’s pious ones: Huna and Hisda gather for rain prayer in hope of divine favor.',who='Rabbi Zerika',comp='composite',unc=['Bracketed מה preserved.'])
E=c('yona.pretext','23b:10',"תקיפי דארעא דישראל כגון ר' יונה אבוה דרבי מני כי הוה מצטריך עלמא למיטרא הוה עייל לביתיה ואמר להו הבו לי גואלקי ואיזיל ואייתי לי בזוזא עיבורא",'The account cites Rabbi Yona, Mani’s father: when rain is needed he asks for his sack, saying he will buy grain for a zuz.',voice='comparison narrative',comp='composite')
F=c('yona.prayer','23b:10',"כי הוה נפיק לברא אזיל וקאי בדוכתא עמיקתא דכתיב (תהלים קל, א) ממעמקים קראתיך ה' וקאי בדוכתא צניעא ומכסי בשקא ובעי רחמי ואתי מיטרא",'Yona stands in a low, secluded place, invoking from the depths, covers himself in sackcloth, prays and rain comes.',voice='comparison narrative',comp='composite')
Fq=q('grain.bought.q','23b:10','כי הוה אתי לביתיה אמרי ליה אייתי מר עיבורא','At home he is asked whether he brought grain.',voice='unnamed household')
G=c('grain.reply','23b:10','אמר להו אמינא הואיל ואתא מיטרא השתא רווח עלמא','Yona says rain has now brought relief to the world.',who='Rabbi Yona');e('grain.answer','23b:10',ix['23b:10']['text'],G,Fq,'answer')
H=c('mani.grave','23b:11',ix['23b:11']['text'],'Harassed by the patriarch’s household, Mani appeals at his father’s grave; their horses’ legs become caught until they agree to stop harassing him.',voice='narrative',comp='composite')
I=c('mani.rich','23b:12','ותו רבי מני הוה שכיח קמיה דרבי יצחק בן אלישיב אמר ליה עתירי דבי חמי קא מצערו לי','Mani tells Yitzhak ben Elyashiv that his wealthy in-laws distress him.',who='Rabbi Mani')
J=c('make.poor','23b:12','אמר ליענו ואיענו','Yitzhak says let them become poor, and they do.',who='Rabbi Yitzhak ben Elyashiv',comp='composite')
K=c('poor.burden','23b:12','אמר קא דחקו לי','Mani reports that they now press him.',who='Rabbi Mani')
L=c('restore.wealth','23b:12','אמר ליעתרו ואיעתרו','Yitzhak says let them become rich, and they do.',who='Rabbi Yitzhak ben Elyashiv',comp='composite')
M=c('wife.displeasure','23b:13','אמר לא מיקבלי עלי אינשי ביתי','Mani says his wife is not pleasing to him.',who='Rabbi Mani')
Mq=q('wife.name.q','23b:13','א"ל מה שמה','Yitzhak asks her name.',who='Rabbi Yitzhak ben Elyashiv')
N=c('hannah.name','23b:13','חנה','Mani gives the name Hannah.',who='Rabbi Mani');e('wife.name.answer','23b:13','חנה',N,Mq,'answer')
O=c('hannah.beauty','23b:13','תתייפי חנה ונתייפת','Yitzhak says Hannah should become beautiful, and she does.',who='Rabbi Yitzhak ben Elyashiv',comp='composite')
R=c('hannah.pride','23b:13','אמר ליה קא מגנדרא עלי','Mani complains she now acts proudly toward him.',who='Rabbi Mani')
S=c('hannah.restored','23b:13','א"ל אי הכי תחזור חנה לשחרוריתה וחזרה חנה לשחרוריתה','Yitzhak says she should return to her prior appearance, and she does.',who='Rabbi Yitzhak ben Elyashiv',comp='composite',unc=['שחרוריתה retained in source; no racial category imposed.'])
T=c('students.wisdom','23b:14','הנהו תרי תלמידי דהוו קמיה דרבי יצחק בן אלישיב אמרו ליה ניבעי מר רחמי עלן דניחכים טובא','Two students ask Yitzhak to pray for their great wisdom.',voice='two students collective')
U=c('power.dismissed','23b:14','אמר להו עמי היתה ושלחתיה','He replies that it was with him and he sent it away.',who='Rabbi Yitzhak ben Elyashiv',unc=['Object of עמי היתה implicit; supernatural power not reified beyond context.'])
V=c('yosi.moves','23b:15',ix['23b:15']['text'],'Rabbi Yosi bar Avin leaves Yosi of Yokrat and comes to Rav Ashi.',voice='narrative')
W=c('fish.drying','24a:1','יומא חד שמעיה דקא גריס אמר שמואל השולה דג מן הים בשבת כיון שיבש בו כסלע חייב','He hears Ashi recite Shmuel’s rule: taking a fish from sea on Sabbath incurs liability when a sela-sized area dries.',who='Shmuel',chain=['Rav Ashi','Shmuel'],cond=['Sabbath','sela-sized drying'])
X=c('fins.qualification','24a:1','א"ל ולימא מר ובין סנפיריו','Yosi asks that between its fins be specified.',who='Rabbi Yosi bar Avin');e('fins.qualification.edge','24a:1',ix['24a:1']['text'],X,W,'qualification')
Xq=q('fins.author.q','24a:1','אמר ליה ולא סבר לה מר דההיא רבי יוסי בן רבי אבין אמרה','Ashi asks whether he knows that Yosi ben Rabbi Avin said that.',who='Rav Ashi')
Y=c('yosi.identity','24a:1','אמר ליה אנא ניהו','Yosi says he is that person.',who='Rabbi Yosi bar Avin');e('fins.author.answer','24a:1',ix['24a:1']['text'],Y,Xq,'answer')
Yq=q('former.teacher.q','24a:2',"א\"ל ולאו קמיה דר' יוסי דמן יוקרת הוה שכיח מר",'Ashi asks whether he had studied with Yosi of Yokrat.',who='Rav Ashi')
Z=c('former.teacher.yes','24a:2','א"ל (הין)','He says yes.',who='Rabbi Yosi bar Avin',unc=['Parenthetical הין retained.']);e('former.teacher.answer','24a:2',ix['24a:2']['text'],Z,Yq,'answer')
Zq=q('leave.why.q','24a:2','א"ל ומ"ט שבקיה מר ואתא הכא','Why did he leave and come here?',who='Rav Ashi')
AA=c('no.compassion','24a:2','אמר ליה גברא דעל בריה ועל ברתיה לא חס עלי דידי היכי חייס','Yosi reasons that someone without compassion for his own son/daughter would not have compassion for him.',who='Rabbi Yosi bar Avin');e('leave.why.answer','24a:2',ix['24a:2']['text'],AA,Zq,'answer')
AAq=q('son.story.q','24a:3','בריה מאי היא','What happened with his son?')
AB=c('workers.hungry','24a:3','יומא חד הוו אגרי ליה אגירי בדברא נגה להו ולא אייתי להו ריפתא אמרו ליה לבריה כפינן','Workers in the field lacked food because Yosi was late; they told his son they were hungry.',voice='narrative',comp='composite')
AC=c('fig.miracle','24a:3','הוו יתבי תותי תאינתא אמר תאנה תאנה הוציאי פירותיך ויאכלו פועלי אבא אפיקו ואכלו','Under a fig tree the son calls for fruit for his father’s workers; fruit emerges and they eat.',voice='narrative with son’s speech',comp='composite')
AD=c('father.delay','24a:4','אדהכי והכי אתא אבוה אמר להו לא תינקטו בדעתייכו דהאי דנגהנא אמצוה טרחנא ועד השתא הוא דסגאי','His father arrives and explains he was delayed attending a commandment.',who='Rabbi Yosi of Yokrat')
AE=c('workers.bless','24a:4','אמרו ליה רחמנא לישבעך כי היכי דאשבען ברך','The workers bless him as his son satisfied them.',voice='workers collective')
AEq=q('food.where.q','24a:4','אמר להו מהיכא','He asks where the food came from.',who='Rabbi Yosi of Yokrat')
AF=c('workers.report','24a:4','אמרו הכי והכי הוה מעשה','They report the incident.',voice='workers collective');e('food.where.answer','24a:4',ix['24a:4']['text'],AF,AEq,'answer')
AG=c('son.curse','24a:4','אמר לו בני אתה הטרחת את קונך להוציא תאנה פירותיה שלא בזמנה יאסף שלא בזמנו','Yosi tells his son that for troubling the Creator for untimely figs, he should be gathered before his time.',who='Rabbi Yosi of Yokrat',status='reported paternal imprecation, not normative ruling');e('son.story.answer','24a:4',ix['24a:4']['text'],AG,AAq,'answer')
AGq=q('daughter.story.q','24a:5','ברתיה מאי היא','What happened with his daughter?')
AH=c('daughter.observer','24a:5','הויא ליה ברתא בעלת יופי יומא חד חזיא לההוא גברא דהויא כריא בהוצא וקא חזי לה','His daughter was beautiful; he sees a man making an opening in the fence to look at her.',voice='narrative',comp='composite')
AHq=q('observer.q','24a:5','אמר לו מאי האי','Yosi asks what the man is doing.',who='Rabbi Yosi of Yokrat')
AI=c('observer.reply','24a:5','אמר ליה רבי אם ללוקחה לא זכיתי לראותה לא אזכה','The man asks whether, unable to marry her, he may not at least see her.',who='unnamed observer');e('observer.answer','24a:5',ix['24a:5']['text'],AI,AHq,'answer')
AJ=c('daughter.curse','24a:5','אמר לה בתי קא מצערת להו לברייתא שובי לעפריך ואל יכשלו ביך בני אדם','Yosi tells his daughter to return to dust so others will not stumble because of her.',who='Rabbi Yosi of Yokrat',status='reported imprecation, not normative ruling');e('daughter.story.answer','24a:5',ix['24a:5']['text'],AJ,AGq,'answer')
AK=c('donkey.payment','24a:6','הויא ליה ההוא חמרא כדהוו אגרי לה כל יומא לאורתא הוו משדרי לה אגרה אגבה ואתיא לבי מרה ואי טפו לה או בצרי לה לא אתיא','Yosi’s hired donkey returned with its fee only when the amount was exact, refusing excess or shortfall.',voice='narrative',comp='composite',cond=['exact fee'])
AL=c('forgotten.sandals','24a:6','יומא חד אינשו זוגא דסנדלי עלה ולא אזלה עד דשקלונהו מינה והדר אזלה','It refused to leave when sandals were forgotten on it until they were removed.',voice='narrative')
refs=list(ix);refs=refs[refs.index('23b:8'):refs.index('24a:6')+1]
for k,title,first,last in [('hanan','Hanan and hidden prayer comparison','23b:8','23b:10'),('mani','Mani, Yona’s grave and Yitzhak ben Elyashiv','23b:11','23b:14'),('yokrat','Yosi’s move, Sabbath fish rule and Yokrat family/donkey narratives','23b:15','24a:6')]:
 add('structure.'+k,'structure',first,dict(title=title,primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference');P['records'][-1]['evidence']=[ev(r) for r in refs[refs.index(first):refs.index(last)+1]]
notes={'23b:8':'Hanan lineage, children appeal, prayer and name question/reason retained.','23b:9':'Zerika/Safra comparison and Huna/Hisda joint prayer retained.','23b:10':'Yona grain pretext, secluded/deep prayer, verse, rain and household dialogue retained.','23b:11':'Mani harassment, grave appeal and horses/release condition retained.','23b:12':'Rich/poor/restored in-law sequence and distinct speakers retained.','23b:13':'Wife complaint, name question/answer, beauty/pride/reversal sequence retained.','23b:14':'Students wisdom request and implicit dismissed-power reply retained.','23b:15':'Yosi departure/arrival retained with continuation.','24a:1':'Shmuel fish threshold, fins addition and author identity exchange retained.','24a:2':'Former-teacher and departure questions plus compassion rationale retained.','24a:3':'Son-story question, hungry workers and fig miracle retained.','24a:4':'Father delay, blessing, source question/report and imprecation retained.','24a:5':'Daughter-story question, observer dialogue and paternal imprecation retained.','24a:6':'Exact-fee donkey and forgotten-sandals incident retained.'}
for z in P['records']:
 if z['layer']=='questions':z['uncertainty'].append('Partial means represented local source responses only; no exhaustive-choice eligibility.')
for ref in refs:
 for layer in runner.LAYERS:
  found=[r['id'] for r in P['records'] if r['layer']==layer and any(v['segment_id']==ix[ref]['id'] for v in r['evidence'])];rationale=('Source reread/omission reconciliation: ' if layer=='reconciliation' else '')+notes[ref]
  if not found:rationale+=' No distinct '+layer+' record warranted after pass.'
  P['coverage'].append(dict(segment_id=ix[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if found else 'none_found_after_pass',record_ids=found,rationale=rationale))
runner.validate_apply(runner.current(JOB),P,ss,j)
out=JOB/'staging_resume_20261126'/'batch050.json';runner.immutable(out,runner.encoded(P));print(json.dumps(dict(proposal=str(out),records=len(P['records']),segments=len(refs))))
