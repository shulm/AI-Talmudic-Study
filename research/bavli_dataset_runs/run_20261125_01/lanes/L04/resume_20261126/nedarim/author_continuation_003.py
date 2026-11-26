"""Manual continuation: local violation and delay explanations, not general halakha."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r003.';a.OUTPUT='continuation_003.json'
c=a.c;q=a.q;e=a.edge
a.structure('violation',['3b:5','3b:6'],'How violation of a nazirite undertaking adds בל יחל')
a.structure('delay',['3b:7','3b:8']+['4a:'+str(i) for i in range(1,13)]+['4b:1','4b:2','4b:3'],'Explanations of delaying naziriteship and its obligations')
a.structure('annul',['4b:4','4b:5'],'Why nazirite annulment requires the explicit comparison with vows')
repeat=c('repeat','3b:5','אמר מר  ומה נדרים עובר (במדבר ל ג) בבל יחל ובל תאחר','The discussion repeats the vow premise concerning בל יחל and בל תאחר.',composition='composite',scope='Repeated baraita premise, not a second unique-topic count')
vow=c('vow','3b:5','כגון דאמר ככר זו אוכל ולא אכלה עובר משום בל יחל דברו','The discussion illustrates בל יחל of vows by one who says he will eat this loaf and does not eat it.',conditions=['stated undertaking to eat this loaf','not fulfilled'],scope='Source’s example as printed; no external correction of its classification')
qv=q('qv','3b:6','אלא בל יחל דנזירות היכי משכחת לה','How does בל יחל arise for naziriteship?')
immediate=c('immediate','3b:6','כיון דאמר הריני נזיר הוה ליה נזיר','Saying הריני נזיר makes the person a nazirite.',scope='Premise of the local violation question')
eat=c('eat','3b:6','אכל קם ליה בבל יאכל','Eating the prohibited nazirite food already incurs its eating prohibition.',conditions=['nazirite','prohibited eating'],scope='Premise asking what בל יחל adds')
drink=c('drink','3b:6','שתה קם ליה בבל ישתה','Drinking already incurs the nazirite drinking prohibition.',conditions=['nazirite','prohibited drinking'],scope='Premise asking what בל יחל adds')
two=c('two','3b:6','אמר רבא  לעבור עליו בשנים','Rava explains that the nazirite incurs two prohibitions.',holder='רבא',scope='בל יחל in addition to the respective nazirite prohibition, not two physical acts')
e('two.answer',two,qv,'answer','3b:6','אמר רבא  לעבור עליו בשנים')
delayq=q('delayq','3b:7','בל תאחר דנזירות היכי משכחת לה','How can delay of naziriteship arise?')
now=c('now','3b:7','כיון דאמר הריני נזיר הוה ליה נזיר  אכל קם ליה בבל יאכל','A direct nazirite declaration takes effect immediately, and prohibited eating violates the eating prohibition.',composition='composite',scope='Paired premises of delay question; no delay of onset in this direct declaration')
want=c('want','3b:7','באומר לכשארצה אהא נזיר','The discussion tentatively proposes a declaration to become a nazirite whenever he wishes.',mode='rejected',conditions=['לכשארצה אהא נזיר'],scope='Proposed case for delay, immediately rejected')
nodelay=c('nodelay','3b:7','ואי אמר כשארצה ליכא בל תאחר','A declaration conditioned on whenever he wishes supplies no בל תאחר.',conditions=['כשארצה'])
e('want.answer',want,delayq,'answer','3b:7');e('nodelay.correction',nodelay,want,'correction','3b:7','ואי אמר כשארצה ליכא בל תאחר')
death=c('death','3b:8','אמר רבא  כגון דאמר לא איפטר מן העולם עד שאהא נזיר דמן ההיא שעתא הוה ליה נזיר','Rava gives a commitment not to depart the world before becoming a nazirite, which requires immediate naziriteship.',holder='רבא',conditions=['לא איפטר מן העולם עד שאהא נזיר'],scope='Source’s immediate-obligation explanation of delay; exact legal mechanism not expanded')
get=c('get','3b:8','מידי דהוה האומר לאשתו הרי זו גיטיך שעה אחת קודם מיתתי אסורה לאכול בתרומה מיד','The comparison is a wife given a divorce effective one hour before the husband’s death, who immediately may not eat terumah.',conditions=['divorce effective one hour before his death'],scope='Analogy within Rava response, no independent speaker assigned')
risk=c('risk','3b:8','אלמא אמרינן  כל שעתא ושעתא דילמא מיית הכא נמי לאלתר הוי נזיר דאמרינן  דילמא השתא מיית','Because death may occur at any moment, the nazirite commitment likewise requires immediate action.',conditions=['commitment to naziriteship before death'],scope='Explicit risk-of-death rationale, not a claim of historical motive')
e('death.answer',death,delayq,'answer','3b:8');e('get.analogy',get,death,'analogy','3b:8');e('risk.support',risk,death,'support','3b:8')
cemetery=c('cemetery','4a:1',None,'Rav Aha bar Yaakov offers a nazirite vow made while the person is in a cemetery.',holder='רב אחא בר יעקב',conditions=['vow in cemetery'],mode='challenged',scope='Alternative explanation of בל תאחר, refined in4a:3')
e('cemetery.answer',cemetery,delayq,'answer','4a:1')
cq=q('cq','4a:2',"הניחא למ''ד לא חיילא עליה נזירות מאלתר אלא למ''ד מאלתר חיילא עליה מי איכא בל תאחר",'If naziriteship takes effect immediately in the cemetery, how can there be delay?',conditions=['view that naziriteship takes effect immediately'])
notnow=c('notnow','4a:2',"הניחא למ''ד לא חיילא עליה נזירות מאלתר",'The proposed cemetery case initially fits a view that naziriteship does not take effect immediately.',mode='challenged',scope='Initial conditional analysis challenged by Mar bar Rav Ashi’s report, not a resolved school attribution')
mar=c('mar','4a:2','ועוד האמר מר בר רב אשי  חיילא נזירות עליה מאלתר וכי פליגי לענין מלקות פליגי','Mar bar Rav Ashi says naziriteship takes effect immediately and the disagreement concerns lashes.',holder='מר בר רב אשי',composition='composite',scope='Quoted correction of the supposed disagreement over onset')
e('cq.objection',cq,cemetery,'objection','4a:2');e('mar.support',mar,cq,'support','4a:2')
e('mar.correction',mar,notnow,'correction','4a:2')
pure=c('pure','4a:3',"אפ''ה קם ליה בבל תאחר משום דקא מאחר נזירות דטהרה",'Even with immediate onset, the cemetery case delays naziriteship in purity and incurs בל תאחר.',conditions=['nazirite in cemetery','delaying naziriteship in purity'])
ashi=c('ashi','4a:3',"א''ר אשי  הואיל וכן נזיר שטימא עצמו במזיד עובר משום בל תאחר דנזירות טהרה",'Rav Ashi accordingly says a nazirite who deliberately defiles himself violates delay of naziriteship in purity.',holder='רב אשי',conditions=['nazirite','deliberate self-defilement'])
e('pure.answer',pure,cq,'answer','4a:3');e('pure.qualification',pure,cemetery,'qualification','4a:3');e('pure.support',pure,ashi,'support','4a:3')
hair=c('hair','4a:4',None,'Rav Aha son of Rav Ika explains the delay as delay of the nazirite’s shaving.',holder='רב אחא בריה דרב איקא',conditions=['delayed nazirite shaving'])
e('hair.answer',hair,delayq,'answer','4a:4')
even=c('even','4a:5',None,'The shaving explanation works both if shaving is indispensable and if it is not: at least the shaving commandment is unfulfilled.',conditions=['shaving delayed'],composition='composite',scope='Anonymous explanation of both conditional schools and remaining commandment')
e('even.support',even,hair,'support','4a:5')
offer=c('offer','4a:6',None,'Mar Zutra son of Rav Mari explains the delay as delay of the nazirite’s offerings.',holder='מר זוטרא בריה דרב מרי',conditions=['delayed nazirite offerings'])
e('offer.answer',offer,delayq,'answer','4a:6')
oq=q('oq','4a:7','ומן הכא נפקא ליה  מהתם נפקא ליה','Why derive offering-delay here when it is derived elsewhere?')
elsewhere=c('elsewhere','4a:7','(דברים כג:כב) כי דרוש ידרשנו אלו חטאות ואשמות','The other derivation interprets כי דרוש ידרשנו as including sin and guilt offerings.',scope='Cited derivation as a redundancy objection')
e('oq.objection',oq,offer,'objection','4a:7');e('elsewhere.support',elsewhere,oq,'support','4a:7')
novel=c('novel','4a:8',None,'One might have exempted the nazirite case because the Torah treats it exceptionally.',mode='hypothetical',scope='Reason a special derivation is needed; nature of novelty examined next')
e('novel.answer',novel,oq,'answer','4a:8')
what=q('what','4a:9','מאי חידוש','What is the exceptional feature?')
novel1=c('novel1','4a:9','אילימא דלא מתפיס ליה לחטאת נזיר בנדר','The first proposed feature is that a nazirite sin offering cannot be undertaken by a vow.',mode='challenged',scope='Proposed rationale rejected in this formulation but reconsidered with distinction at4b:2')
fat=c('fat','4a:9','הרי חטאת חלב שאין מתפיסה בנדר ועובר בבל תאחר','A sin offering for forbidden fat also cannot be undertaken by vow yet is subject to delay.',scope='Counterexample to the first novelty rationale')
e('novel1.answer',novel1,what,'answer','4a:9');e('fat.objection',fat,novel1,'objection','4a:9')
seed=c('seed','4a:10',None,'The next proposal is that even undertaking naziriteship only from a grape seed makes one a nazirite for all restrictions; one might therefore exempt delay, but the comparison teaches otherwise.',mode='rejected',composition='composite',scope='Explicit composite of proposed exceptional feature, proposed exemption and its exclusion; rationale rejected at4a:11')
e('seed.answer',seed,what,'answer','4a:10')
sq=q('sq','4a:11',"הניחא למ''ד  כי נזיר מן חרצן הוי נזיר לכל אלא לר''ש דאמר  אין נזיר עד שיזיר מכולן מאי איכא למימר",'How can that novelty explain the derivation for Rabbi Shimon, who requires undertaking all restrictions?')
shimon=c('shimon','4a:11',"לר''ש דאמר  אין נזיר עד שיזיר מכולן",'Rabbi Shimon requires undertaking all nazirite restrictions before one is a nazirite.',holder='ר״ש',conditions=['undertaking all restrictions'],scope='Quoted position; textual abbreviation retained without additional identity adjudication')
strict=c('strict','4a:11','ועוד  האי חידוש לחומרא הוא','The proposed grape-seed novelty is stringent, undermining its use to infer an exemption.',scope='Second independent objection to proposed rationale')
e('sq.objection',sq,seed,'objection','4a:11');e('strict.objection',strict,seed,'objection','4a:11')
one=c('one','4a:12',None,'The replacement novelty is that shaving after one of the three offerings suffices; this could have suggested exemption from delay, which the derivation excludes.',mode='hypothetical',composition='composite',extra=[('4b:1',None)],scope='Composite question-reformulation, premise and excluded exemption; continuous cross-page sentence')
again=q('again','4a:12','אלא מאי חידושיה','What, then, is its exceptional feature?')
e('one.answer',one,what,'answer','4b:1')
e('one.again',one,again,'answer','4b:1')
alternate=c('alternate','4b:2','ואיבעית אימא  מאי חדושיה משום דלא מתפיסו בנדר','Alternatively the inability to undertake the nazirite sin offering by vow can serve as the exceptional feature.',scope='Alternative reinstatement with the distinction that follows')
atonement=c('atonement','4b:2','והא דקא קשיא לך חטאת חלב חטאת חלב קאתיא לכפרה חטאת נזיר למאי אתיא','The response distinguishes the fat sin offering as coming for atonement and asks what the nazirite sin offering comes for.',composition='composite',scope='Explicit contrast in offered answer, no general external theology of sacrifices supplied')
nwhy=q('nwhy','4b:2','חטאת נזיר למאי אתיא','What does the nazirite sin offering come for?')
e('alternate.answer',alternate,what,'answer','4b:2');e('atonement.answer',atonement,fat,'answer','4b:2')
birthq=q('birthq','4b:3','והרי חטאת יולדת דלא אתיא לכפרה ועבר עלה משום בל תאחר','What of a childbirth sin offering, which does not come for atonement yet is subject to delay?')
permit=c('permit','4b:3',"ההיא קא שריא לה למיכל בקדשי'",'That offering permits the woman to eat sacred food.',scope='Answer distinguishing childbirth offering')
e('birthq.objection',birthq,atonement,'objection','4b:3');e('permit.answer',permit,birthq,'answer','4b:3')
annul=c('annul','4b:4','אמר מר  ומה נדרים האב מיפר נדרי בתו ובעל מיפר נדרי אשתו אף נזירות האב מיפר נזירות בתו ובעל מיפר נזירות אשתו','The discussion repeats the baraita comparing paternal and spousal annulment of vows with naziriteship.',composition='composite',scope='Repeated occurrence of four explicitly paired annulment clauses, already individually represented at3a:7')
aq=q('aq','4b:4','למה לי היקשא  תיתי במה מצינו מנדרים','Why require a scriptural comparison rather than ordinary analogy from vows?')
unlimited=c('unlimited','4b:5','דילמא גבי נדרים הוא דמיפר משום דלא אית ליה קיצותא','One might restrict annulment to vows because they lack a fixed duration.',mode='hypothetical',scope='Excluded distinction explaining necessity of comparison')
thirty=c('thirty','4b:5',"אבל גבי נזירות דאית ליה קיצותא דסתם נזירות ל' יום",'Unspecified naziriteship has a fixed duration of thirty days.',conditions=['unspecified naziriteship'],scope='Premise of the proposed vow/nazirite distinction')
exclude=c('exclude','4b:5',"אימא לא קמ''ל",'The comparison excludes the proposed denial of annulment for naziriteship.',scope='Conclusion of the duration-based hypothetical; ordinary analogy alone would not settle it')
e('unlimited.answer',unlimited,aq,'answer','4b:5');e('exclude.correction',exclude,unlimited,'correction','4b:5')
a.notes={
'3b:5':'Reread repeated baraita and loaf example as printed; no commentary substitution.',
'3b:6':'Reread direct onset, eating and drinking premises, explicit question and Rava’s dual-prohibition answer.',
'3b:7':'Reread delay question, immediate-onset premise, proposed desire-conditioned declaration and its rejection.',
'3b:8':'Reread Rava’s commitment, divorce/terumah analogy and repeated mortality rationale; retained exact conditional scope.',
'4a:1':'Reread cemetery proposal against continuation4a:2–3; not treated as settled delayed-onset claim.',
'4a:2':'Reread conditional onset objection and Mar bar Rav Ashi correction locating disagreement in lashes.',
'4a:3':'Reread pure-naziriteship answer and Rav Ashi’s deliberate-defilement extension.',
'4a:4':'Reread Rav Aha son of Rav Ika shaving explanation; kept distinct from Rav Aha bar Yaakov.',
'4a:5':'Reread both schools on indispensability and common remaining commandment; explicit composite.',
'4a:6':'Reread Mar Zutra son of Rav Mari offering explanation.',
'4a:7':'Reread redundant-derivation objection and cited sin/guilt-offering inclusion.',
'4a:8':'Reread exceptional-law response with full subsequent analysis; no settled unnamed exception fabricated.',
'4a:9':'Reread question, initial nonvow feature and fat-offering counterexample; later reconsideration4b:2 preserved.',
'4a:10':'Reread grape-seed feature, hypothetical exemption and exclusion as explicit composite; later objections retained.',
'4a:11':'Reread Rabbi Shimon condition and separate stringency objection; abbreviation remains textual label.',
'4a:12':'Reread sentence jointly with4b:1; one cross-page claim rather than false isolated unit.',
'4b:1':'Reread one-of-three-offerings premise and excluded exemption in continuous4a:12 sentence.',
'4b:2':'Reread alternative restoration of nonvow feature and atonement contrast; no invented ultimate doctrinal ruling.',
'4b:3':'Reread childbirth objection and permission-to-eat answer.',
'4b:4':'Reread repeated annulment baraita and ordinary-analogy question; repetition retained.',
'4b:5':'Reread indefinite-vow versus thirty-day-nazirite hypothetical and its exclusion; no absolute annulment rule without scope.'}
if __name__=='__main__':a.save()
