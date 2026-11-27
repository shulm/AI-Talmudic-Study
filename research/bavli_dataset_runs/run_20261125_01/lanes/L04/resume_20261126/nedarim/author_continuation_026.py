"""Mistaken vows and partial release: explicit Rabbah/Rava constructions."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r026.';a.OUTPUT='continuation_026.json'
c=a.c;q=b.q;e=a.edge
a.structure('mistake',['25b:1','25b:2','25b:3'],'Mistaken vows and oaths; family among fig-eaters')
a.structure('release',['25b:4','25b:5']+['26a:'+str(i) for i in range(1,8)]+['26b:'+str(i) for i in range(1,9)]+['27a:'+str(i) for i in range(1,5)],'Partial release under Rabbah and Rava: wording, dependent vows and counterexamples')
past=c('past','25b:1','נדרי שגגות אם אכלתי ואם שתיתי ונזכר שאכל ושתה','Mistaken vows include conditions about past eating or drinking followed by remembering that he did eat or drink.',composition='composite',scope='Two parallel Mishnah examples, no invented object of prohibition')
future=c('future','25b:1','שאני אוכל ושאני שותה ושכח ואכל ושתה','The Mishnah also includes future eating or drinking declarations followed by forgetful eating or drinking.',composition='composite',scope='Mistake/forgetfulness category')
wife=c('wife','25b:1','אמר קונם אשתי נהנית לי שגנבה את כיסי ושהכתה את בני ונודע שלא הכתו ונודע שלא גנבה','It includes a wife-benefit prohibition founded on alleged theft or striking the son when both grounds prove false.',composition='composite',conditions=['stated grounds disproved'],scope='Allegations not reported as actual wrongdoing')
figs=c('figs','25b:2','ראה אותן אוכלין תאנים ואמר הרי עליכם קרבן ונמצאו אביו ואחיו והיו עמהן אחרים','The case concerns people eating figs prohibited by the speaker, among whom he then discovers his father and brothers alongside others.',composition='composite',scope='Unexpected inclusion of family in collective declaration')
bs=c('bs','25b:2','בית שמאי אומרים הן מותרים ומה שעמהם אסורים','Beit Shammai permit the family and prohibit the other participants.',holder='בית שמאי',composition='composite',scope='Mishnah’s stated differentiated outcome')
bh=c('bh','25b:2','ובית הלל אומרים אלו ואלו מותרין','Beit Hillel permit both groups.',holder='בית הלל',scope='Precise hypothetical wording is disputed below')
e('bh.objection',bh,bs,'objection','25b:2')
both=c('both','25b:3','תנא כשם שנדרי שגגות מותרין כך שבועות שגגות מותרות','The teaching permits mistaken oaths as it permits mistaken vows.',scope='Explicit extension across categories')
oathq=q('oathq','25b:3','היכי דמי שבועות שגגות','What is an example of mistaken oaths?')
kahana=c('kahana','25b:3','כגון רב כהנא ורב אסי הדין אמר שבועתא דהכי אמר רב והדין אמר שבועתא דהכי אמר רב','Rav Kahana and Rav Asi each swear that Rav spoke as he recalls.',composition='composite',scope='Alternative remembered reports of Rav; neither substantive view nor assignment by order is supplied')
good=c('good','25b:3','דכל חד וחד אדעתא דנפשיה שפיר קמישתבע','Each swears correctly according to his own understanding.',scope='Reason for mistaken-oath permission, not proof that both reports match Rav’s exact words')
e('kahana.answer',kahana,oathq,'answer','25b:3');e('good.support',good,both,'support','25b:3')
days=c('days','25b:4','תנן התם פותחין בשבתות ובימים טובים','A cited Mishnah allows openings based on Sabbaths and festivals.',scope='Release discussion, not automatic dissolution of every vow on those days')
early=c('early','25b:4','בראשונה היו אומרים אותן הימים מותרים ושאר כל הימים אסורים','Originally the allowance was limited to those days while other days remained prohibited.',mode='rejected',composition='composite',scope='Earlier rule subsequently changed by Rabbi Akiva’s teaching')
akiva=c('akiva','25b:4','עד שבא רבי עקיבא ולימד נדר שהותר מקצתו הותר כולו','Rabbi Akiva taught that a vow partly released is wholly released.',holder='רבי עקיבא',scope='Scope and wording examined in ensuing dispute')
e('akiva.correction',akiva,early,'correction','25b:4')
rabbahAll=c('rabbahAll','25b:5','אמר רבה דכולי עלמא כל היכא דאמר אילו הייתי יודע שאבא ביניכם הייתי אומר כולכם אסורין חוץ מאבא דכולהון אסורין ואביו מותר','Rabbah says all agree that had he known his father was present and said all are prohibited except father, the others remain prohibited and father is permitted.',holder='רבה',composition='composite',conditions=['counterfactual retains collective all except father'],scope='Rabbah, distinct from Rava in next segment')
rabbahSplit=c('rabbahSplit','25b:5','לא נחלקו אלא באומר אילו הייתי יודע שאבא ביניכם הייתי אומר פלוני ופלוני אסורין ואבא מותר','Rabbah places the dispute where the counterfactual individually names prohibited people and exempts father.',holder='רבה',conditions=['counterfactual changes collective expression to individuals'])
ravaSplit=c('ravaSplit','26a:1','ורבא אמר דכולי עלמא כל היכא דאמר אילו הייתי יודע שאבא ביניכם הייתי אומר פלוני ופלוני אסורין ואבא מותר כולם מותרין','Rava says all agree to permit everyone where the counterfactual individually names people and exempts father.',holder='רבא',conditions=['counterfactual names individuals'])
ravaAll=c('ravaAll','26a:1','לא נחלקו אלא באומר אילו הייתי יודע שאבא ביניכם הייתי אומר כולכם אסורין חוץ מאבא','Rava locates the dispute in the counterfactual all except father formulation.',holder='רבא',conditions=['counterfactual retains collective expression'])
e('rava.distinction',ravaAll,rabbahAll,'distinction','26a:1');e('rava.distinction2',ravaSplit,rabbahSplit,'distinction','26a:1')
first=c('first','26a:2',None,'Beit Shammai follow Rabbi Meir’s principle to seize the initial wording.',holder='בית שמאי',scope='Explanation within Rava’s collective-wording dispute; embedded principle attributed to Rabbi Meir')
end=c('end','26a:3',None,'Beit Hillel follow Rabbi Yosei’s principle that a person is held by the conclusion of his words.',holder='בית הלל',scope='Explanation within Rava’s account; embedded principle attributed to Rabbi Yosei')
for key,ref,name,claim in [('meir','26a:2','רבי מאיר',first),('yosei','26a:3','רבי יוסי',end)]:a.add(key,'attributions',dict(surface=name,role='speaker',candidates=[name],scope=claim,transmission_chain=[]),[a.ev(ref)],[claim])
collect=c('collect','26a:4','קונם שאיני נהנה לכולכם הותר אחד מהן הותרו כולם','Rav Pappa cites to Rava a teaching illustrating Rabbi Akiva: a collective benefit vow is wholly released when one participant is released.',scope='Quoted rule inside Rav Pappa’s objection')
chainFirst=c('chainFirst','26a:4','שאיני נהנה לא לזה ולזה הותר הראשון הותרו כולם','The same citation says that in a not-this-one-and-this-one formulation, releasing the first releases all.',scope='Dependency mechanism supplied26b:3, not assumed ordinary independent list')
chainLast=c('chainLast','26a:4','הותר האחרון האחרון מותר וכולן אסורין','Releasing the last permits only the last while the others remain prohibited.',scope='Quoted final-member rule')
rp=q('rp','26a:4','איתיביה רב פפא לרבא כיצד אמר רבי עקיבא נדר שהותר מקצתו הותר כולו','Rav Pappa challenges Rava using the teaching explaining Rabbi Akiva’s partial-release principle.',voice='רב פפא',conditions=['specific contradiction completed26b:1'])
rr1=c('rr1','26a:5',None,'For Rabbah the first clause can be placed in a counterfactual this-one-and-this-one formulation.',mode='hypothetical',scope='Proposed construction in objection, subsequently challenged')
rr2=c('rr2','26a:6',None,'For Rabbah the final clause is proposed as a collective all-of-you formulation.',mode='challenged',scope='Proposal later questioned for lacking first/last order')
ra1=c('ra1','26a:7',None,'For Rava the first clause can be placed in an all-of-you formulation.',mode='hypothetical',scope='Concession within Rav Pappa’s objection')
contradict=q('contradict','26b:1',None,'If the final clause is an individual formulation and Rabbi Akiva’s view, why do the sages disagree when Rava said all agree to permit?')
counter=q('counter','26b:2','אמר ליה רבא ולרבה לרבי עקיבא מי ניחא סיפא במאי מוקים לה דאמר לכולכם הי דין הוא ראשון והי דין הוא אחרון','Rava responds that Rabbah also faces a difficulty: what are first and last in a collective all-of-you formulation?',voice='רבא')
resolve=c('resolve','26b:3','אלא רישא דאמר לכולכם','The resolution places the first clause in an all-of-you formulation.',scope='Final construction of quoted teaching')
dependent=c('dependent','26b:3','וסיפא כגון שתלאן זה בזה ואמר פלוני כפלוני ופלוני כפלוני','The final clause concerns people made dependent one on another, saying one person is like the prior person.',scope='Ordered dependent vows rather than independent enumerated prohibitions')
middle=c('middle','26b:4',None,'A corroborating teaching permits the middle member and those below when the middle is released, while those above remain prohibited.',composition='composite',scope='Evidence for ordered dependency')
for key,question in [('rp',rp),('contradict',contradict),('counter',counter)]:e(key+'.answer',dependent,question,'answer','26b:3')
e('middle.support',middle,dependent,'support','26b:4');e('dependent.correction',dependent,rr2,'correction','26b:3')
onion=c('onion','26b:5','קונם בצל שאני טועם שהבצל רע ללב אמרו לו והלא הכופרי יפה ללב','Rav Adda bar Ahava cites a vow against onions on the stated belief that they harm the heart, challenged by the claimed benefit of the kufri variety.',composition='composite',scope='Ancient claim quoted within vow reasoning, not modern medical guidance')
permit=c('permit','26b:5','הותר בכופרי ולא בכופרי בלבד הותר אלא בכל הבצלים','Release for kufri extends to all onions in the cited case.',scope='Partial-release counterexample, wording subsequently specified')
meir=c('meir','26b:5','מעשה היה והתירו רבי מאיר בכל הבצלים','An actual incident is reported where Rabbi Meir permitted all the onions.',holder='רבי מאיר',scope='Source-reported precedent')
onionq=q('onionq','26b:6',None,'Is the case not a counterfactual saying all onions are prohibited and kufri permitted?',conditions=['challenge to Rava using Rabbi Meir’s reported ruling'])
individual=c('individual','26b:7','לא באומר אילו הייתי יודע שהכופרי יפה ללב הייתי אומר בצל פלוני ופלוני אסורין וכופרי מותר','The reply specifies instead a counterfactual individually naming onion varieties and permitting kufri.',scope='Deflection of assumed collective wording')
agree=c('agree','26b:7','ורבי מאיר אליבא דרבי עקיבא ואליבא דרבנן','Rabbi Meir’s ruling fits both Rabbi Akiva and the sages under this formulation.',scope='Local agreement in specified case, not global agreement on partial release')
e('individual.answer',individual,onionq,'answer','26b:7')
basket=c('basket','26b:8','רבי נתן אומר יש נדר שמקצתו מותר ומקצתו אסור כיצד נדר מן הכלכלה','Ravina cites Rabbi Natan’s case of a basket vow that is partly permitted and partly prohibited.',holder='רבי נתן',scope='Opening of cross-page citation; detailed fruit case follows')
fruit=c('fruit','27a:1','והיו בה בנות שוח ואמר אילו הייתי יודע שבנות שוח בתוכה לא הייתי נודר הכלכלה אסורה בנות שוח מותרות','If the basket contains benot shuah and he says he would not have vowed had he known, the basket remains prohibited while those fruits are permitted.',composition='composite',scope='Earlier cited outcome before Rabbi Akiva’s intervention')
akiva2=c('akiva2','27a:1','עד שבא רבי עקיבא ולימד נדר שהותר מקצתו הותר כולו','The citation says Rabbi Akiva taught that partial release releases the whole vow.',holder='רבי עקיבא',scope='Repeated teaching in distinct basket occurrence')
basketq=q('basketq','27a:1','מאי לאו דאמר אילו הייתי יודע שבנות שוח בתוכה הייתי אומר תאנים שחורות ולבנות אסורות בנות שוח מותרות ורבי עקיבא היא ופליגי רבנן','Does the case not individually specify black and white figs as prohibited, with benot shuah permitted, while sages disagree with Rabbi Akiva?')
basketAll=c('basketAll','27a:2',None,'The reply specifies a collective counterfactual: the whole basket prohibited except benot shuah.',scope='Deflects assumption of individual formulation')
e('akiva2.correction',akiva2,fruit,'correction','27a:1');e('basketAll.answer',basketAll,basketq,'answer','27a:2')
who=q('who','27a:3','מאן תנא להא דתנו רבנן','Who teaches the following baraita?')
five=c('five','27a:3','נדר מחמשה בני אדם כאחד הותר לאחד מהם  הותרו כולן','A vow concerning five people together is wholly released when one is released.',scope='First clause of authorship question')
exceptc=c('except','27a:3','חוץ מאחד מהן הוא מותר והן אסורין','In the except-one formulation, that one is permitted while the others are prohibited.',scope='Second clause of baraita, interpreted under two models')
rabbahMap=c('rabbahMap','27a:4','אי לרבה רישא רבי עקיבא וסיפא דברי הכל','Under Rabbah the first clause is Rabbi Akiva and the latter is unanimous.',composition='composite',conditions=['Rabbah’s model'])
ravaMap=c('ravaMap','27a:4','אי לרבא סיפא רבנן ורישא דברי הכל','Under Rava the latter clause is the sages and the first is unanimous.',composition='composite',conditions=['Rava’s model'])
e('rabbahMap.answer',rabbahMap,who,'answer','27a:4');e('ravaMap.answer',ravaMap,who,'answer','27a:4')
a.notes={
'25b:1':'Reread past memory, future forgetfulness and disproved wife-vow grounds, preserving paired examples.',
'25b:2':'Reread fig-eaters, unexpected family, others and Beit Shammai/Beit Hillel outcomes.',
'25b:3':'Reread oath parallel and Kahana/Asi reports of Rav; did not invent reported content or assign opinions by order.',
'25b:4':'Reread day-based openings, earlier limited rule and Rabbi Akiva correction.',
'25b:5':'Reread Rabbah collective consensus and individually named dispute; distinguished רבה from רבא.',
'26a:1':'Reread Rava’s inverse allocation and both conditional wordings.',
'26a:2':'Reread Beit Shammai alignment with Rabbi Meir’s initial-wording principle.',
'26a:3':'Reread Beit Hillel alignment with Rabbi Yosei’s final-wording principle.',
'26a:4':'Reread Rav Pappa challenge, collective release and both first/last clauses; followed resolution26b:3.',
'26a:5':'Reread first proposed Rabbah construction as objection-stage interpretation.',
'26a:6':'Reread second proposed Rabbah construction, later challenged for orderlessness.',
'26a:7':'Reread concession concerning Rava first clause and continuing objection.',
'26b:1':'Reread completed objection against Rava’s unanimous individual-case allowance.',
'26b:2':'Reread Rava counterquestion about first/last under collective wording.',
'26b:3':'Reread final first-clause construction and explicit ordered dependency resolution.',
'26b:4':'Reread middle-member corroboration with above/below distinction.',
'26b:5':'Reread Rav Adda source, heart-related statements as attributed ancient premises, and Rabbi Meir incident.',
'26b:6':'Reread proposed collective wording as challenge, not source’s final reconstruction.',
'26b:7':'Reread individual-variety deflection and local compatibility with both tannaitic sides.',
'26b:8':'Reread Ravina challenge introduction and Rabbi Natan citation continuing27a:1.',
'27a:1':'Reread basket/benot shuah outcome, Rabbi Akiva change and proposed black/white individual formulation.',
'27a:2':'Reread collective-basket deflection.',
'27a:3':'Reread authorship question and both five-person baraita clauses.',
'27a:4':'Reread conditional Rabbah and Rava mappings; neither silently promoted to sole final model.'}
if __name__=='__main__':a.save()
