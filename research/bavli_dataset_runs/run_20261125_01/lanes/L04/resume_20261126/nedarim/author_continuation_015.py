"""Manual Torah-reference formulas and conditional sleep/benefit prohibitions."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r015.';a.OUTPUT='continuation_015.json'
c=a.c;q=a.q;e=a.edge
a.structure('torah',['14b:'+str(i) for i in range(1,6)],'Vowing by Torah scroll or its contents; three explanations of wording')
a.structure('sleep',['14b:6','14b:7']+['15a:'+str(i) for i in range(1,13)]+['15b:'+str(i) for i in range(1,10)],'Conditional sleep vows, precautions against later fulfillment, and successive objections')
a.structure('marital',['15b:10','15b:11','15b:12'],'Marital-benefit formula and the distinction between imposing a prohibition on another and accepting one personally')
bare=c('bare','14b:1','תניא הנודר בתורה לא אמר כלום','The teaching gives no effect to vowing by the Torah itself.',scope='Baraita, contextual distinctions below')
written=c('written','14b:1',('במה שכתוב בה דבריו קיימין',0),'Vowing by what is written in it is effective.',scope='Baraita’s second clause')
both=c('both','14b:1','בה ובמה שכתוב בה דבריו קיימין','Vowing by it and by what is written in it is effective.',composition='composite',scope='Baraita’s combined formula')
redundant=q('redundant','14b:2',None,'After the written-content formula is effective, need the combined formula be stated?')
ground=c('ground','14b:3','אמר רב נחמן לא קשיא הא דמחתא אורייתא אארעא הא דנקיט לה בידיה','Rav Nahman distinguishes a Torah lying on the ground from one held in the speaker’s hand.',holder='רב נחמן',composition='composite',scope='First explanation of context-sensitive reference')
parchment=c('parchment','14b:3','מחתא על ארעא דעתיה אגווילי','When it lies on the ground, the reference is taken to concern its parchment.',holder='רב נחמן',conditions=['scroll on ground'],scope='Source’s stated interpretation of referent, not inferred private psychology')
names=c('names','14b:3','נקט לה בידיה דעתיה על האזכרות שבה','When held in hand, the reference concerns the divine names in it.',holder='רב נחמן',conditions=['holding scroll'])
e('ground.answer',ground,redundant,'answer','14b:3')
alternative=c('alternative','14b:4',None,'Alternatively the scroll lies on the ground, yet explicit reference to what is written works; the clauses proceed from the less obvious to the obvious.',composition='composite',scope='Second explanation, separate from hand/ground assignment')
third=c('third','14b:5',None,'A further explanation places even the middle clause in the held-scroll case; holding it makes bare בה equivalent to reference to its contents.',composition='composite',conditions=['scroll held in hand'],scope='Third explanation, not combined with prior alternatives into one factual scene')
e('alternative.answer',alternative,redundant,'answer','14b:4');e('third.answer',third,redundant,'answer','14b:5')
sleepm=c('sleepm','14b:6','קונם שאני ישן שאני מדבר שאני מהלך','The Mishnah lists sleep, speech and walking קונם formulations under its בל יחל rule.',composition='composite',scope='Three intangible-action formulas, interpretation discussed next')
maritalm=c('maritalm','14b:6','האומר לאשה קונם שאני משמשך הרי זה בלא יחל דברו:','The Mishnah places a man’s קונם שאני משמשך formula under בל יחל.',conditions=['declaration to a woman'],scope='Object/obligation scope clarified15b:10–12')
rav=c('rav','14b:7','אמר רב יהודה אמר רב אל יישן היום שמא יישן למחר','Rav, reported by Rav Yehuda, forbids sleeping today when today’s sleep is vowed prohibited if he sleeps tomorrow, lest he sleep tomorrow.',holder='רב',conditions=['קונם עיני בשינה היום אם אישן למחר'],scope='Conditional vow: present prohibition, future triggering act')
a.add('rav.transmit','attributions',dict(surface='אמר רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope=rav,transmission_chain=['רב יהודה','רב']),[a.ev('14b:7','אמר רב יהודה אמר רב')],[rav])
nahman=c('nahman','14b:7','ורב נחמן אמר יישן היום ולא חיישינן שמא יישן למחר','Rav Nahman permits sleeping today and does not fear tomorrow’s triggering sleep.',holder='רב נחמן',conditions=['same today-prohibited-if-tomorrow formula'])
reverse=c('reverse','14b:7','ומודה רב יהודה באומר קונם עיני בשינה למחר אם אישן היום שישן היום','Rav Yehuda agrees that one may sleep today if the vow instead prohibits tomorrow’s sleep conditional on sleeping today.',holder='רב יהודה',conditions=['קונם עיני בשינה למחר אם אישן היום'],scope='Source names Rav Yehuda in the concession; not silently rewritten as Rav')
care=c('care','15a:1',None,'The distinction is that a person may neglect a condition but takes care about the prohibited act itself.',scope='Anonymous rationale for reverse-condition concession')
e('care.support',care,reverse,'support','15a:1')
caseq=q('caseq','15a:2','היכי דמי אילימא כדקתני שאני ישן מי הוי נדרא','How can the Mishnah’s literal “that I sleep” create a vow?')
tangible=c('tangible','15a:2','והתנן חומר בשבועות שהשבועות חלות על דבר שיש בו ממש ועל דבר שאין בו ממש מה שאין כן בנדרים','The objection cites that oaths cover tangible and intangible matters, unlike vows.',composition='composite',scope='Repeated comparison rule')
intangible=c('intangible','15a:2','ושינה דבר שאין בו ממש הוא','Sleep is intangible.',scope='Premise of objection')
eyes=c('eyes','15a:2','אלא דאמר קונם עיני בשינה','The first explanation supplies the tangible formula קונם עיני בשינה.',scope='Reconstructed Mishnah case, not replacement of source words')
e('eyes.answer',eyes,caseq,'answer','15a:2')
unlimited=q('unlimited','15a:3','ואי דלא יהיב שיעורא מי שבקינן ליה עד דעבר איסור בל יחל','If no time limit is specified, would he be left until violating בל יחל?')
three=c('three','15a:3','והאמר רבי יוחנן שבועה שלא אישן שלשה ימים מלקין אותו וישן לאלתר','Rabbi Yohanan says one who swears not to sleep three days is given lashes and sleeps immediately.',holder='רבי יוחנן',conditions=['oath not to sleep three days'],composition='composite',scope='Cited rule against impossible sleep abstention, not health advice')
e('three.support',three,unlimited,'support','15a:3')
tomorrow=c('tomorrow','15a:4','אלא דאמר קונם עיני בשינה למחר אם אישן היום','The discussion tentatively proposes tomorrow’s sleep prohibited if he sleeps today.',mode='rejected',conditions=['tomorrow prohibited, today condition'],scope='Candidate Mishnah case rejected by carefulness premise')
careq=q('careq','15a:4','הא אמרת כל באיסוריה מזדהר','But have you not said that he guards against the prohibited act?')
e('careq.objection',careq,tomorrow,'objection','15a:4')
today=c('today','15a:5','אלא פשיטא דאמר קונם עיני בשינה היום אם אישן למחר','The objection therefore places the Mishnah in today’s prohibition conditional on tomorrow’s sleep.',conditions=['today prohibited, tomorrow condition'],scope='Proposed case used to challenge Rav Yehuda’s report')
violateq=q('violateq','15a:5','ואי לא ניים היום כי ניים למחר מאי בל יחל דברו איכא','If he did not sleep today, how would sleeping tomorrow violate בל יחל?')
slept=c('slept','15a:5','אלא לאו בדניים אלמא איתיה דניים ותיובתא דרב יהודה','The objection infers that sleeping today is allowed, contradicting Rav Yehuda.',mode='rejected',scope='Mistaken permission inference from a described violation')
if_slept=c('if_slept','15a:6',None,'The answer reads the Mishnah as “if he slept,” without permitting it.',scope='After-the-fact case, not permission')
e('slept.objection',slept,rav,'objection','15a:5');e('if_slept.correction',if_slept,slept,'correction','15a:6')
ravina=c('ravina','15a:7',None,'Ravina retains the literal Mishnah wording and interprets its בל יחל as rabbinic.',holder='רבינא',scope='Alternative explanation of intangible-action vows')
e('ravina.answer',ravina,caseq,'answer','15a:7')
rabbinicq=q('rabbinicq','15a:8','ומי איכא בל יחל מדרבנן','Is there a rabbinic form of בל יחל?')
custom=c('custom','15a:8','אִין והתניא דברים המותרין ואחרים נהגו בהן איסור אי אתה רשאי להתירן בפניהם שנאמר לא יחל דברו','Yes: a teaching forbids permitting before others things they customarily treat as prohibited, citing לא יחל דברו.',conditions=['intrinsically permitted things','others adopted prohibitory practice','in their presence'],scope='Cited proof for rabbinic usage')
e('custom.answer',custom,rabbinicq,'answer','15a:8');e('custom.support',custom,ravina,'support','15a:8')
passover=c('passover','15a:9',None,'A cited Mishnah prohibits the wife’s benefit until Passover if she goes to her father’s house before the festival; going before Passover forbids benefit until Passover.',conditions=['benefit until Passover','visit condition until החג','visit before Passover'],composition='composite',scope='First conditional-benefit example; deadlines preserved distinctly')
notgone=c('notgone','15a:10',None,'The objection infers that without a visit before Passover she is not prohibited.',mode='rejected',scope='Inference challenged by Rabbi Abba')
abba=c('abba','15a:11',None,'Rabbi Abba distinguishes prohibition with lashes after she visits from prohibition alone before she visits.',holder='רבי אבא',conditions=['same first conditional-benefit vow'],composition='composite',scope='Corrects inference of initial permission')
e('notgone.objection',notgone,rav,'objection','15a:10');e('abba.correction',abba,notgone,'correction','15a:11')
afterp=c('afterp','15a:12','אימא סיפא אחר הפסח בבל יחל דברו','The later clause states בל יחל after Passover.',scope='Quoted continuation used for second objection')
benefitq=q('benefitq','15a:12','ואי דלא איתהני לפני הפסח מי איכא בל יחל','Without benefit before Passover, how can there be בל יחל?')
permitted=c('permitted','15a:12','אלא פשיטא דאיתהני אלמא מיתהני','The objection infers prior permitted benefit and thereby a contradiction to Rav Yehuda.',extra=[('15b:1',None)],mode='rejected',scope='Cross-page inference, corrected next')
e('permitted.objection',permitted,rav,'objection','15b:1')
ifbenefit=c('ifbenefit','15b:2',None,'The answer reads the clause as “if she benefited,” then בל יחל applies.',scope='Described transgression does not establish permission')
e('ifbenefit.correction',ifbenefit,permitted,'correction','15b:2')
festival=c('festival','15b:3',None,'A second Mishnah prohibits benefit until the festival if she visits her father by Passover; visiting before Passover prohibits benefit until the festival, while visiting after Passover is allowed.',conditions=['benefit deadline החג','visit-condition deadline Passover'],composition='composite',scope='Second example reverses deadline order; not conflated with first')
nogone2=c('nogone2','15b:4',None,'The objection again infers that if she did not go she is not prohibited.',mode='rejected',scope='Second separate occurrence of permission inference')
rava=c('rava','15b:5',None,'Rava says she is prohibited even without going; after going there is prohibition and lashes, before going prohibition alone.',holder='רבא',conditions=['second deadline arrangement'],composition='composite',scope='Second correction, distinct named responder')
e('nogone2.objection',nogone2,rav,'objection','15b:4');e('rava.correction',rava,nogone2,'correction','15b:5')
loaf=c('loaf','15b:6',None,'A baraita makes today’s loaf prohibited if he goes to a place tomorrow; if he ate it, he is prohibited from going.',conditions=['loaf today conditional on going tomorrow','loaf was eaten'],composition='composite',scope='Cited conditional case; אכל is past action, not permission')
past=c('past','15b:7',None,'The reply stresses that the baraita says אכל, not אוכל: after eating, he must not go.',scope='Explicit grammatical distinction blocks permission inference')
e('past.qualification',past,loaf,'qualification','15b:7')
went=c('went','15b:8','הלך הרי זה בבל יחל דברו','If he went, the baraita states violation of בל יחל.',conditions=['ate the conditioned loaf then went'],scope='Second baraita clause')
walkq=q('walkq','15b:8','מהלך לא וקשיא לרב יהודה','Does the wording imply he may not go initially, contrary to Rav Yehuda?')
symmetry=c('symmetry','15b:9',None,'The reply in Rav Yehuda’s voice permits teaching מהלך; הלך is chosen to parallel the opening אכל, where אוכל could not be taught.',holder='רב יהודה',scope='Dialectical response to wording objection; second act is allowed when earlier prohibited consumption did not occur',composition='composite')
e('symmetry.answer',symmetry,walkq,'answer','15b:9')
dutyq=q('dutyq','15b:10','והא משתעבד לה מדאורייתא דכתיב שארה כסותה ועונתה לא יגרע','How can the marital formula work when he is obligated to her under the Torah’s conjugal-duty provision?')
selfbenefit=c('selfbenefit','15b:11','באומר הנאת תשמישך עלי','The answer construes the formula as prohibiting to himself the benefit of intercourse with her.',conditions=['הנאת תשמישך עלי'],scope='Self-directed benefit prohibition rather than cancellation of his obligation to her')
unwelcome=c('unwelcome','15b:11','והא לא קא ניחא ליה בתשמיש','The discussion treats the intercourse as unwelcome to him under that prohibition.',scope='Source’s stated explanation, not an inferred motive beyond this legal formulation')
e('selfbenefit.answer',selfbenefit,dutyq,'answer','15b:11')
kahana1=c('kahana1','15b:12','דאמר רב כהנא תשמישי עליך כופין אותה ומשמשתו דשעבודי משעבדת ליה','Rav Kahana’s cited rule says that for her תשמישי עליך formula she is compelled to fulfill the marital obligation because she is obligated to him.',holder='רב כהנא',conditions=['her תשמישי עליך formula'],scope='Historical source rule reported faithfully, not contemporary advice or endorsement')
kahana2=c('kahana2','15b:12','הנאת תשמישך עלי אסור שאין מאכילין לו לאדם דבר האסור לו:','For הנאת תשמישך עלי, Rav Kahana’s cited rule prohibits the benefit, because a person is not given what is forbidden to them.',holder='רב כהנא',conditions=['self-directed benefit prohibition'],scope='Contrasting formulation in quoted rule')
e('kahana2.support',kahana2,selfbenefit,'support','15b:12');e('kahana1.distinction',kahana1,kahana2,'distinction','15b:12')
a.notes={
'14b:1':'Reread three Torah-reference clauses separately.',
'14b:2':'Reread redundancy question about combined wording.',
'14b:3':'Reread Rav Nahman’s two physical settings and their specified referents.',
'14b:4':'Reread second explanation and nonascending novelty order.',
'14b:5':'Reread third explanation of held-scroll bare reference; alternatives remain distinct.',
'14b:6':'Reread three action formulas and marital formula; later object/obligation interpretations retained.',
'14b:7':'Reread exact two-day condition directions, Rav Yehuda-to-Rav transmission, Rav Nahman disagreement and Rav Yehuda concession.',
'15a:1':'Reread condition/prohibited-act care distinction.',
'15a:2':'Reread intangible-action question, oath comparison, sleep premise and tangible-eyes reconstruction.',
'15a:3':'Reread unlimited-duration objection and Rabbi Yohanan three-day rule.',
'15a:4':'Reread rejected reverse-day case and carefulness objection.',
'15a:5':'Reread today-prohibited case, violation question and rejected permission inference.',
'15a:6':'Reread conditional after-the-fact answer דאי ניים.',
'15a:7':'Reread Ravina’s literal/rabbinic alternative.',
'15a:8':'Reread rabbinic question and permitted-things/custom/in-presence proof with all conditions.',
'15a:9':'Reread first benefit/visit deadline arrangement.',
'15a:10':'Reread mistaken no-visit permission inference.',
'15a:11':'Reread Rabbi Abba prohibition-versus-lashes distinction.',
'15a:12':'Reread after-Passover clause, benefit question and inference continuing15b:1.',
'15b:1':'Reread completion of Rav Yehuda objection, tied to prior inference.',
'15b:2':'Reread after-the-fact benefit answer.',
'15b:3':'Reread reversed benefit/visit deadlines and permission to visit after Passover.',
'15b:4':'Reread second no-visit inference as separate occurrence.',
'15b:5':'Reread Rava’s two-status answer, not confused with earlier Rabbi Abba.',
'15b:6':'Reread loaf-today/travel-tomorrow condition and past eating.',
'15b:7':'Reread אכל versus אוכל distinction.',
'15b:8':'Reread went/violation clause and initial-travel objection.',
'15b:9':'Reread Rav Yehuda-voiced reply and grammatical symmetry rationale.',
'15b:10':'Reread marital-duty objection and cited verse.',
'15b:11':'Reread self-directed benefit formula and source explanation.',
'15b:12':'Reread both Rav Kahana formulas, obligation and forbidden-benefit rationales without contemporary normative assertion.'}
if __name__=='__main__':a.save()
