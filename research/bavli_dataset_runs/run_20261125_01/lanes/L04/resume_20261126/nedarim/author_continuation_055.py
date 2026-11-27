"""Manual reading of derivative names, local supplies and singular/plural foods."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r055.';a.OUTPUT='continuation_055.json'
c=a.c;e=a.edge;q=b.q
a.structure('names',['53a:'+str(i) for i in range(1,9)],'Named derivatives, secondary names and regional oil usage')
a.structure('vegetables',['53a:9','53b:1','53b:2'],'Sabbatical vegetable supply and imported soil')
a.structure('formulas',['53b:'+str(i) for i in range(3,10)],'Cabbage, pulse and singular/plural wheat formulas; chapter end')
dates=c('dates','53a:1','הנודר מן התמרים מותר בדבש תמרים מסתוניות מותר בחומץ סתוניות','Vows against dates or late-season grapes permit date honey or their vinegar respectively.',composition='composite',scope='Two source/derivative pairs; סתוניות label preserved in evidence')
betera=c('betera','53a:1','רבי יהודה בן בתירא אומר כל ששם תולדתו קרויה עליו ונודר הימנו אסור ביוצא הימנו','Rabbi Yehuda ben Beteira prohibits derivatives whose name retains the source item’s name under a vow against the source.',holder='רבי יהודה בן בתירא',scope='Explicit general named-derivative rule')
sages=c('sages','53a:1','וחכמים מתירים','The sages permit the derivatives.',holder='חכמים',scope='Position contrasted with Yehuda ben Beteira; relation to opening tanna questioned next')
same=q('same','53a:2',None,'How do these sages differ from the first tanna?')
distinction=c('distinction','53a:3','איכא בינייהו הדא דתניא כלל זה אר"ש בן אלעזר','The reply distinguishes them through Rabbi Shimon ben Elazar’s following rule.',scope='Text introduces a differentiating rule without explicitly mapping each side to it in this clause')
edible=c('edible','53a:3','כל שדרכו לאכול ודרך היוצא ממנו לאכול כגון תמרים ודבש תמרים נדר בו אסור ביוצא ממנו נודר מיוצא ממנו אסור בו','Rabbi Shimon ben Elazar says that where both source and derivative are ordinarily eaten, such as dates and date honey, a vow against either prohibits the other.',holder='רבי שמעון בן אלעזר',composition='composite',scope='Both edibility conditions, example and reciprocal outcomes explicitly represented')
inedible=c('inedible','53a:4','כל שאין דרכו לאכול ודרך היוצא ממנו לאכול נודר בו אין אסור אלא ביוצא ממנו שלא נתכוון זה אלא ליוצא ממנו','Where the source is not ordinarily eaten but its derivative is, a vow naming the source prohibits only its derivative because that alone was intended.',holder='רבי שמעון בן אלעזר',composition='composite',scope='Continued baraita: two consumption conditions, exclusive outcome and stated intention rationale')
e('sages.objection',sages,betera,'objection','53a:1');e('distinction.answer',distinction,same,'answer','53a:3')
apple=c('apple','53a:5','הנודר מן היין מותר ביין תפוחים','A wine vow permits apple wine.',scope='Secondary named variety excluded from unqualified category')
sesame=c('sesame','53a:5','מן השמן מותר בשמן שומשמין','An oil vow permits sesame oil.',scope='Mishnah rule later qualified by locality')
honey=c('honey','53a:5','מן הדבש מותר בדבש תמרים','A honey vow permits date honey.',scope='Secondary named variety')
vinegar=c('vinegar','53a:6','החומץ מותר בחומץ סתוניות','A vinegar vow permits late-season-grape vinegar.',scope='Formula begins with מן at preceding segment end; exact continuation preserved')
leek=c('leek','53a:6','מן הכרישין מותר בקפלוטות','A vow against כרישין permits קפלוטות.',scope='Distinct vegetable labels retained without imposing modern species identities')
wild=c('wild','53a:6','מן הירק מותר בירקות השדה שהוא שם לוויי','A vegetable vow permits field vegetables because that is a qualified name.',scope='Explicit secondary-name rationale')
israel=c('israel','53a:7','תניא הנודר מן השמן בארץ ישראל מותר בשמן שומשמין ואסור בשמן זית','The baraita says an oil vow in the land of Israel permits sesame oil and prohibits olive oil.',composition='composite',scope='Source-era regional usage, not a present-day geographic rule')
babylon=c('babylon','53a:7','ובבבל אסור בשמן שומשמין ומותר בשמן זית','In Babylonia it prohibits sesame oil and permits olive oil.',composition='composite',scope='Opposite regional usage under same generic formula')
mixed=c('mixed','53a:7','מקום שמסתפקין מזה ומזה אסור בזה ובזה','Where both oils are supplied, both are prohibited.',composition='composite',scope='Local supply determines ambiguity')
obvious=q('obvious','53a:8','פשיטא','Why is the mixed-supply rule not obvious?')
majority=c('majority','53a:8','לא צריכא דרובא מן חד מסתפקין','The answer applies it even where most use one kind.',scope='Majority-supply qualification')
follow=c('follow','53a:8','מהו דתימא איזיל בתר רובא','One might have thought to follow the majority.',mode='rejected',scope='Explicit rejected proposed rule in this ambiguous vow case')
strict=c('strict','53a:8','קא משמע לן ספק איסורא לחומרא','The teaching treats the prohibition doubt stringently.',scope='Local stated reason for including both despite majority')
e('majority.answer',majority,obvious,'answer','53a:8');e('strict.correction',strict,follow,'correction','53a:8');e('majority.qualification',majority,mixed,'qualification','53a:8')
ordinary=c('ordinary','53a:9','הנודר מן הירק בשאר שני שבוע אסור בירקות הגינה ומותר בירקות השדה','In ordinary years of the seven-year cycle a vegetable vow prohibits garden vegetables and permits field vegetables.',composition='composite',scope='Two outcomes under ordinary-year condition')
seventh=c('seventh','53a:9','ובשביעית אסור בירקות השדה ומותר בירקות הגינה','In the sabbatical year it prohibits field vegetables and permits garden vegetables.',composition='composite',scope='Reversed outcomes subsequently limited by import practice')
imported=c('imported','53b:1',None,'Rabbi Abbahu reports Rabbi Hanina ben Gamliel that the sabbatical distinction applies only where vegetables are not imported; where they are imported, garden vegetables are prohibited too.',holder='רבי חנינא בן גמליאל',composition='composite',scope='Cross-folio report and both import conditions; object garden vegetables inferred from preceding permission',extra=[('53a:9','אמר רבי אבהו משום רבי חנינא בן גמליאל')])
e('imported.qualification',imported,seventh,'qualification','53b:1')
noimport=c('noimport','53b:2','כתנאי אין מביאין ירק מן חוצה לארץ לארץ','The anonymous tanna prohibits importing vegetables from outside into the land of Israel.',scope='Tannaitic dispute introduced to explain differing supply practices')
yesimport=c('yesimport','53b:2','רבי חנניה בן גמליאל אומר מביאין ירק מחוצה לארץ לארץ','Rabbi Hananya ben Gamliel permits importing vegetables.',holder='רבי חנניה בן גמליאל',scope='Printed חנניה retained distinct from preceding חנינא surface; no unsupported identity resolution')
why=q('why','53b:2','מ"ט דמאן דאמר אין מביאין','What is the reason for the view prohibiting import?')
soil=c('soil','53b:2','אמר רבי ירמיה משום גוש','Rabbi Yirmeya explains: because of the attached clod of earth.',holder='רבי ירמיה',scope='Source’s compressed soil rationale without adding an unquoted full legal regime')
e('yesimport.objection',yesimport,noimport,'objection','53b:2');e('soil.answer',soil,why,'answer','53b:2')
cabbage=c('cabbage','53b:3',None,'A cabbage vow prohibits איספרגוס, while an איספרגוס vow permits cabbage.',composition='composite',scope='Asymmetric two-direction relation; named preparation retained')
pulse=c('pulse','53b:4','מן הגריסין אסור במקפה ורבי יוסי מתיר','A גריסין vow prohibits מקפה according to the anonymous view, while Rabbi Yosei permits it.',composition='composite',scope='Explicit two-holder contrast on pulse preparation')
reverse=c('reverse','53b:4','מן המקפה מותר בגריסין','A מקפה vow permits גריסין.',scope='Reverse direction separately stated')
garlic=c('garlic','53b:4',"מן המקפה אסור בשום ור' יוסי מתיר",'A מקפה vow prohibits garlic according to the anonymous view, while Rabbi Yosei permits it.',composition='composite',scope='Second explicit Yosei disagreement, not merged with first')
garlicrev=c('garlicrev','53b:4','מן השום מותר במקפה','A garlic vow permits מקפה.',scope='Reverse garlic direction')
lentil=c('lentil','53b:5',"מן העדשים אסור באשישים ר' יוסי מתיר",'A lentil vow prohibits אשישים according to the anonymous view, while Rabbi Yosei permits them.',composition='composite',scope='Repeated dispute occurrence retained separately from52b1')
lentilrev=c('lentilrev','53b:5','מן האשישים מותר בעדשים','An אשישים vow permits lentils.',scope='Reverse direction')
wheat=c('wheat','53b:6','חטה חטין שאני טועם אסור בהן בין קמח בין הפת','The combined חטה חטין tasting formula prohibits both flour and bread.',composition='composite',scope='Both explicit processed wheat products')
groats=c('groats','53b:6','גריס גריסין שאני טועם אסור בהן בין חיין בין מבושלין','The combined גריס גריסין tasting formula prohibits both raw and cooked groats.',composition='composite',scope='Both preparation states')
yehuda=c('yehuda','53b:6','רבי יהודה אומר קונם גריס או חטה שאני טועם מותר לכוס חיים','Rabbi Yehuda permits chewing raw grains under singular גריס or חטה tasting vows.',holder='רבי יהודה',composition='composite',scope='Two singular formulas share raw-consumption permission')
ws=c('ws','53b:7','תניא ר\' שמעון בן גמליאל אומר חטה שאני טועם אסור לאפות ומותר לכוס','Rabbi Shimon ben Gamliel says singular חטה prohibits baked consumption and permits chewing raw.',holder="ר' שמעון בן גמליאל",composition='composite',scope='Singular wheat form and opposed preparation outcomes')
wp=c('wp','53b:7','חטים שאני טועם אסור לכוס ומותר לאפות','Plural חטים prohibits chewing raw and permits baked consumption.',holder="ר' שמעון בן גמליאל",composition='composite',scope='Plural wheat form reverses outcomes')
wb=c('wb','53b:7','חטה חטין שאני טועם אסור בין לכוס בין לאפות','Combined חטה חטין prohibits both raw and baked consumption.',holder="ר' שמעון בן גמליאל",composition='composite',scope='Combined wheat forms')
gs=c('gs','53b:8','גריס שאני טועם אסור לבשל ומותר לכוס','Singular גריס prohibits cooked consumption and permits chewing raw.',holder="ר' שמעון בן גמליאל",composition='composite',scope='Continued baraita, singular groat form')
gp=c('gp','53b:8','גריסין שאני טועם אסור לכוס ומותר לבשל','Plural גריסין prohibits chewing raw and permits cooked consumption.',holder="ר' שמעון בן גמליאל",composition='composite',scope='Continued baraita, plural groat form')
gb=c('gb','53b:8','גריס גריסין שאני טועם אסור בין לבשל בין לכוס','Combined גריס גריסין prohibits both cooked and raw consumption.',holder="ר' שמעון בן גמליאל",composition='composite',scope='Continued baraita, combined groat forms')
a.add('chapter.u','utterances',dict(textual_voice='anonymous textual marker',discourse_role='chapter conclusion',composition='atomic'),[a.ev('53b:9')])
a.add('chapter.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'chapter.u',transmission_chain=[]),[a.ev('53b:9')],[a.PREFIX+'chapter.u'])
a.notes={
'53a:1':'Reread date/grape derivative permissions, Yehuda ben Beteira naming rule and sages opposition.',
'53a:2':'Reread bracketed sages/first-tanna identity question.',
'53a:3':'Reread differentiating baraita and both edible reciprocal cases; no unstated named-side mapping.',
'53a:4':'Reread inedible-source condition, derivative-only prohibition and explicit intent rationale.',
'53a:5':'Reread wine/apple, oil/sesame, honey/date-honey exclusions and continuing vinegar formula.',
'53a:6':'Reread vinegar, leek and field-vegetable exclusions with secondary-name rationale.',
'53a:7':'Reread Israel/Babylonia opposite oil outcomes and both-supply rule.',
'53a:8':'Reread obviousness question, majority condition, rejected majority-following and doubt stringency.',
'53a:9':'Reread ordinary/seventh-year reversals and Abbahu transmission continuing next folio.',
'53b:1':'Reread full no-import/import qualification of garden-vegetable permission.',
'53b:2':'Reread import tannaitic dispute, printed Hananya name, reason question and Yirmeya soil answer.',
'53b:3':'Reread asymmetric cabbage/ispargus directions.',
'53b:4':'Reread both Yosei disputes and both reverse permissions for groats, mikpa and garlic.',
'53b:5':'Reread repeated lentil/ashishim dispute and reverse permission.',
'53b:6':'Reread combined wheat/groat formulas and Yehuda singular raw-consumption permission.',
'53b:7':'Reread Shimon ben Gamliel three wheat formulas and all raw/baked outcomes.',
'53b:8':'Reread same baraita three groat formulas and all raw/cooked outcomes.',
'53b:9':'Reread chapter-end marker only; no legal claim invented.'}
if __name__=='__main__':a.save()
