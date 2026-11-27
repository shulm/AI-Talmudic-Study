"""Manual reading of derivative foods, local names and the unresolved tasting formula."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r054.';a.OUTPUT='continuation_054.json'
c=a.c;e=a.edge;q=b.q
a.structure('derivatives',['51b:9','52a:1','52a:2','52a:3']+['52b:'+str(i) for i in range(1,6)],'Milk, meat and wine derivatives; particular-item prohibition')
a.structure('inquiry',['52b:'+str(i) for i in range(6,15)],'Rami bar Hama inquiry narrowed after successive deflected proofs')
milk=c('milk','51b:9','הנודר מן החלב מותר בקום','A milk vow permits whey.',scope='Anonymous Mishnah position')
yosei=c('yosei','51b:9',"ור' יוסי אוסר",'Rabbi Yosei prohibits whey under a milk vow.',holder="ר' יוסי",scope='Explicit disagreement with preceding permission')
whey=c('whey','51b:9','מן הקום מותר בחלב','A whey vow permits milk.',scope='Reverse direction separately stated')
cheese=c('cheese','51b:9','אבא שאול אומר הנודר מן הגבינה אסור בה בין מלוחה וטפלה','Abba Shaul includes both salted and unsalted cheese under a cheese vow.',holder='אבא שאול',composition='composite',scope='Both explicit preparation categories')
meat=c('meat','52a:1','מותר ברוטב ובקיפה','A meat vow permits broth and קיפה.',composition='composite',scope='Subject continues from previous segment; residue term retained',extra=[('51b:9','הנודר מן הבשר')])
yehuda=c('yehuda','52a:1',"ור' יהודה אוסר",'Rabbi Yehuda prohibits broth and קיפה under the meat vow.',holder="ר' יהודה",composition='composite',scope='Contrary ruling on both preceding derivatives')
e('yosei.objection',yosei,milk,'objection','51b:9');e('yehuda.objection',yehuda,meat,'objection','52a:1')
tarfon=c('tarfon','52a:2','אמר רבי יהודה מעשה ואסר עלינו רבי טרפון בביצים שנתבשלו עמו','Rabbi Yehuda reports that Rabbi Tarfon prohibited eggs cooked with the meat.',holder='רבי טרפון',scope='Tarfon ruling as explicitly reported by Yehuda, not an independent narrator ruling')
specific=c('specific','52a:2','אמרו לו כן הדבר אימתי בזמן שיאמר בשר זה עלי','The respondents agree only when the vow says this meat is upon me.',scope='Anonymous respondents narrow the narrative ruling to a designated item')
taste=c('taste','52a:2','שהנודר מן הדבר ונתערב באחר אם יש בו בנותן טעם אסור','Their rationale is that a vowed item mixed into another prohibits the mixture if it imparts flavor.',scope='Particular-item mixture principle in this response')
e('specific.qualification',specific,tarfon,'qualification','52a:2');e('taste.support',taste,specific,'support','52a:2')
wine=c('wine','52a:3','הנודר מן היין מותר בתבשיל שיש בו טעם יין','A general wine vow permits a dish flavored with wine.',scope='General category vow')
thiswine=c('thiswine','52a:3','אמר קונם יין זה שאני טועם ונפל לתבשיל אם יש בו בנותן טעם הרי זה אסור','A vow against tasting this wine prohibits a dish into which it falls if it imparts flavor.',mode='conditional',scope='Designated wine and actual flavor contribution both explicit')
lentilq=q('lentilq','52b:1',None,'How does the milk/whey dispute fit the lentil-preparation dispute?')
lentil=c('lentil','52b:1',"מן העדשים אסור באשישים ור' יוסי מתיר",'For a lentil vow the anonymous rule prohibits אשישים while Rabbi Yosei permits them.',composition='composite',scope='Quoted counterexample reverses the relative stringent/lenient positions')
local=c('local','52b:2','לא קשיא מר כי אתריה ומר כי אתריה','The reply explains the different rulings through local usage.',scope='No general derivatives-dispute inferred across contexts')
names=c('names','52b:2','באתרא דרבנן קרו לחלבא חלבא ולקומא קומא באתריה דרבי יוסי לקומא נמי קרו ליה קומא דחלבא','The sages’ locality names milk and whey separately; Yosei’s locality also calls whey whey of milk.',composition='composite',scope='Two explicitly described regional naming practices, not modern geographic claims')
e('local.answer',local,lentilq,'answer','52b:2');e('names.support',names,local,'support','52b:2')
barMilk=c('barMilk','52b:3','תניא הנודר מן החלב מותר בקום מן הקום מותר בחלב','A baraita permits whey under a milk vow and milk under a whey vow.',composition='composite',scope='Repeated reciprocal pair retained as separate occurrence')
barCheese=c('barCheese','52b:3','מן החלב מותר בגבינה מן הגבינה מותר בחלב','The baraita permits cheese under a milk vow and milk under a cheese vow.',composition='composite',scope='Second reciprocal pair')
barBroth=c('barBroth','52b:3','מן הרוטב מותר בקיפה מן הקיפה מותר ברוטב','The baraita permits קיפה under a broth vow and broth under a קיפה vow.',composition='composite',scope='Third reciprocal pair')
barMeat=c('barMeat','52b:3','אם אמר בשר זה עלי אסור בו וברוטבו ובקיפו','The formula this meat upon me prohibits the meat, its broth and its קיפה.',composition='composite',scope='Specific-item rule and three explicit objects')
barWine=c('barWine','52b:4',None,'The baraita repeats the distinction between general wine-vow permission for a flavored dish and prohibition where this wine is vowed and contributes wine flavor.',composition='composite',scope='Full repeated two-case occurrence; printed שאיני versus earlier שאני preserved')
grape=c('grape','52b:5','הנודר מן הענבים מותר ביין מן הזיתים מותר בשמן','A grape vow permits wine, and an olive vow permits oil.',composition='composite',scope='Two ordinary category/derivative permissions')
these=c('these','52b:5','אמר קונם זיתים וענבים אלו שאיני טועם אסור בהן וביוצא מהן','The formula these olives and grapes that I will not taste prohibits them and what emerges from them.',composition='composite',scope='Both designation and tasting phrase occur; ensuing inquiry tests which is operative')
initial=q('initial','52b:6','בעי רמי בר חמא אלו דוקא או שאיני טועם דוקא','Rami bar Hama asks whether these or that I will not taste is the operative wording.',voice='רמי בר חמא')
redundant=q('redundant','52b:7','אי ס"ד אלו דוקא שאיני טועם למ"ל','If these is operative, why include that I will not taste?')
teaching=c('teaching','52b:7','הא קמ"ל דאע"ג דאמר שאיני טועם אי דאמר אלו מיתסר ואי לא לא','The tentative reply says the wording could teach that even with a tasting phrase prohibition depends on saying these.',mode='hypothetical',scope='Possible explanation of redundancy, not final resolution of the tasting inquiry')
e('teaching.answer',teaching,redundant,'answer','52b:7')
exchange=c('exchange','52b:8','אמר רבא ת"ש קונם פירות האלו עלי קונם הן לפי אסור בחילופיהן ובגידוליהן','Rava adduces the teaching that these fruits upon me or they are forbidden to my mouth prohibits exchanges and growths.',holder='רבא',composition='composite',scope='Quoted proof text and both explicit derivative categories')
infer=c('infer','52b:8','הא ביוצא מהן מותר','The proposed inference permits what emerges from them.',mode='rejected',scope='Inference from omission explicitly denied next')
deny=c('deny','52b:9','ה"ה דאפי\' ביוצא מהן אסור והא עדיפא ליה לאשמועינן דחילופיהן כגידוליהן דמי','The reply says emerged products are also prohibited; the teaching prefers to establish that exchanges are like growths.',composition='composite',scope='Denies omission inference and states pedagogic reason')
e('deny.correction',deny,infer,'correction','52b:9')
eat=c('eat','52b:10','ת"ש שאיני אוכל ושאיני טועם מותר בחילופיהן ובגידוליהן','A further proof cites that I will not eat or taste, permitting exchanges and growths.',composition='composite',scope='Quoted contrasting formulas and two outcomes')
inf2=c('inf2','52b:10','הא היוצא מהן אסור','It proposes that emerged products are therefore prohibited.',mode='rejected',scope='Inference from omission deflected in same segment')
parallel=c('parallel','52b:10','איידי דלא נסיב ברישא יוצא מהן לא נסיב נמי בסיפא יוצא מהן','The reply explains that the latter clause omits emerged products to parallel the first clause’s wording.',scope='Deflects inference without deciding tasting formula')
e('parallel.correction',parallel,inf2,'correction','52b:10')
proof=c('proof','52b:11',None,'The next proof repeats Yehuda’s report of Tarfon’s eggs ruling and the respondents’ limitation to this meat and flavor contribution.',composition='composite',scope='Full quoted proof occurrence; does not silently substitute the earlier עלינו for printed עלי')
narrow=c('narrow','52b:12','באלו לא קא מיבעיא לן דדוקא הוא','The discussion clarifies that these is certainly operative and was not in doubt.',scope='Explicit narrowing of initial two-way formulation')
remaining=a.q('remaining','52b:12','כי מיבעיא לן בשאיני טועם דוקא או לאו דוקא','The remaining question is whether that I will not taste is itself operative to prohibit emerged products.')
e('narrow.qualification',narrow,initial,'qualification','52b:12')
fish=c('fish','52b:13',None,'The final proof cites the דג דגים tasting formula, prohibiting large/small and raw/cooked fish but permitting טרית טרופה and brine.',composition='composite',scope='Full repeated fish-proof occurrence; proposed evidence against tasting-alone prohibition')
prior=c('prior','52b:14','אמר רבא וכבר יצא מהן','Rava limits the permitted liquid to what had already emerged from the fish.',holder='רבא',scope='Temporal deflection of the fish proof; no answer supplied for products emerging after the vow')
e('prior.qualification',prior,fish,'qualification','52b:14')
for row in a.records:
    if row['id']==remaining:row['uncertainty'].append('The final fish proof is deflected by Rava’s already-emerged qualification; no explicit final determination of tasting-alone wording appears before the next Mishnah.')
a.notes={
'51b:9':'Reread milk/whey Yosei dispute, reverse permission, Abba Shaul cheese conditions and cross-folio meat subject.',
'52a:1':'Reread broth/kifa permissions and Yehuda contrary ruling attached to prior meat subject.',
'52a:2':'Reread Yehuda report of Tarfon, respondents designated-meat limitation and flavor principle.',
'52a:3':'Reread general wine versus designated wine/flavor conditions.',
'52b:1':'Reread reversed lentil/ashishim dispute as objection rather than assumed universal positions.',
'52b:2':'Reread local-usage reconciliation and both precise milk/whey naming practices.',
'52b:3':'Reread all three reciprocal derivative pairs and designated meat inclusion of broth/kifa.',
'52b:4':'Reread complete repeated wine distinction with printed negative tasting phrase.',
'52b:5':'Reread grape/wine and olive/oil permissions plus combined designation/tasting prohibition.',
'52b:6':'Reread Rami bar Hama initial either-wording inquiry; later narrowed explicitly.',
'52b:7':'Reread redundancy question and only tentative these-required explanation.',
'52b:8':'Reread Rava exchange/growth proof and rejected emerged-products omission inference.',
'52b:9':'Reread prohibition reply and pedagogic exchange-equals-growth explanation.',
'52b:10':'Reread eating/tasting proof, proposed opposite omission inference and parallel-wording deflection.',
'52b:11':'Reread full repeated Tarfon narrative proof, including singular עלי variation.',
'52b:12':'Reread definitive these clarification and surviving tasting-only inquiry.',
'52b:13':'Reread full fish proof and all explicit size/preparation/exclusion cases.',
'52b:14':'Reread Rava already-emerged temporal deflection; later Mishnah starts without final tasting resolution.'}
if __name__=='__main__':a.save()
