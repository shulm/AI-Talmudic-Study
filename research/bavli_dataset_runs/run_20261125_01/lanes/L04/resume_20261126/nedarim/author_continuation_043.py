"""Deprivation, memory restoration and attributed ancient illness teachings."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r043.';a.OUTPUT='continuation_043.json'
c=a.c;q=b.q;e=a.edge
a.structure('deprivation',['40b:3','41a:1','41a:2'],'Exile equipment and interpretations of lacking everything')
a.structure('illness',['41a:'+str(i) for i in range(3,12)]+['41b:1','41b:2','41b:3'],'Illness narratives, recovery of learning and historical therapeutic claims')
a.structure('healing',['41b:4'],'Personal versus animal healing under benefit vow')
equipment=c('equipment','40b:3',None,'Rav, through Rabbi Ami, interprets exile equipment as a lamp, bowl and mat.',extra=[('41a:1','ושטיח')],holder='רב',composition='composite',scope='Cross-page list; mat belongs to preceding verse interpretation')
a.add('equipment.chain','attributions',dict(surface="אמר ר' אמי אמר רב",role='transmitter',candidates=["ר' אמי"],scope=equipment,transmission_chain=["ר' אמי",'רב']),[a.ev('40b:3',"אמר ר' אמי אמר רב")],[equipment])
lamp=c('lamp','41a:1',"בחוסר כל (דברים כח, מח) אמר ר' אמי אמר רב בלא נר ובלא שלחן",'Rav, through Rabbi Ami, interprets lacking everything as lacking lamp and table.',holder='רב',composition='composite',scope='New verse interpretation, distinct from exile equipment list')
wife=c('wife','41a:1','רב חסדא אמר בלא אשה','Rav Hisda interprets it as lacking a wife.',holder='רב חסדא',scope='Alternative homiletic reading, not an objective definition of a person’s worth')
servant=c('servant','41a:1','רב ששת אמר בלא שמש','Rav Sheshet interprets it as lacking an attendant.',holder='רב ששת',scope='Separate alternative')
knowledge=c('knowledge','41a:1','רב נחמן אמר בלא דעה','Rav Nahman interprets it as lacking knowledge.',holder='רב נחמן',scope='Separate alternative')
salt=c('salt','41a:1','תנא בלא מלח ובלא רבב','An unnamed teaching interprets it as lacking salt and fat.',composition='composite',scope='Anonymous alternative, not assigned to preceding named speaker')
abaye=c('abaye','41a:2','אמר אביי נקטינן אין עני אלא בדעה','Abaye states that the essential poverty is in knowledge.',holder='אביי',scope='Attributed aphorism, not denial of material deprivation')
west=c('west','41a:2','במערבא אמרי דדא ביה כולא ביה דלא דא ביה מה ביה דא קני מה חסר דא לא קני מה קני','A Western saying treats possessing knowledge as possessing all, and asks what one gains without it.',composition='composite',scope='Parallel rhetorical aphorism with questions, not new unresolved legal questions')
forgive=c('forgive','41a:3',"אמר ר' אלכסנדרי אמר ר' חייא בר אבא אין החולה עומד מחליו עד שמוחלין לו על כל עונותיו שנאמר (תהלים קג, ג) הסולח לכל עוניכי הרופא לכל תחלואיכי",'Rabbi Hiyya bar Abba, via Rabbi Alexandri, links recovery to forgiveness of sins through Psalm103.',holder="ר' חייא בר אבא",scope='Attributed theological interpretation, not a diagnosis of illness or moral blame')
youth=c('youth','41a:3','רב המנונא אמר חוזר לימי עלומיו שנאמר (איוב לג, כה) רוטפש בשרו מנוער ישוב לימי עלומיו','Rav Hamnuna describes recovery as a return to youth, citing Job.',holder='רב המנונא',scope='Attributed recovery image')
forget=c('forget','41a:3','כל משכבו הפכת בחליו (תהלים מא, ד) אמר רב יוסף לומר דמשכח למודו','Rav Yosef interprets turning the sickbed as forgetting one’s learning.',holder='רב יוסף',scope='Homiletic association followed by memory-loss narratives')
yosef=c('yosef','41a:4','רב יוסף חלש איעקר ליה למודיה אהדריה אביי קמיה','Rav Yosef becomes ill and loses his learning; Abaye restores it before him.',composition='composite',scope='Source-reported memory recovery through pupil')
remind=c('remind','41a:4','היינו דבכל דוכתא אמרינן אמר רב יוסף לא שמיע לי הדא שמעתא אמר ליה אביי את אמריתה ניהלן ומהא מתניתא אמריתה ניהלן','The text explains recurring exchanges where Abaye reminds Rav Yosef that he taught the teaching and its baraita basis.',composition='composite',scope='Narrative explanation of reported dialogue elsewhere, no automatic external identification')
thirteen=c('thirteen','41a:5','כי הוה גמיר רבי תלת עשרי אפי הילכתא אגמריה לרבי חייא שבעה מנהון','Rabbi knows thirteen forms of a teaching and teaches Rabbi Hiyya seven.',composition='composite',scope='Specific counts in narrative')
seven=c('seven','41a:5',"לסוף חלש רבי אהדר ר' חייא קמיה הנהו שבעה אפי דאגמריה שיתא אזדו",'After Rabbi’s illness, Rabbi Hiyya restores seven forms but six remain lost.',composition='composite',scope='First restoration stage')
launderer=c('launderer','41a:5',"הוה ההוא קצרא הוה שמיע ליה לרבי כדהוה גריס להו אזל ר' חייא וגמר יתהון קמי קצרא ואתא ואהדר יתהון קמי רבי",'A launderer had heard Rabbi’s recitation; Rabbi Hiyya learns the remaining forms from him and restores them to Rabbi.',composition='composite',scope='Second restoration stage, preserving lay participant’s role')
praise=c('praise','41a:5','כד הוה חזי ליה רבי לההוא קצרא אמר ליה רבי אתה עשית אותי ואת חייא','Rabbi addresses the launderer honorifically and says he made both himself and Hiyya.',scope='First wording of acknowledgment')
alternate=c('alternate','41a:5','איכא דאמרי הכי קאמר ליה אתה עשית את חייא וחייא עשה אותי','An alternate wording credits the launderer with making Hiyya, who then made Rabbi.',scope='Explicit alternate version, not deduplicated')
miracle=c('miracle','41a:6',None,'Rabbi Hiyya bar Abba, via Rabbi Alexandri, compares a patient’s recovery to a greater miracle than the fiery-furnace rescue because illness is described as heavenly fire.',holder="ר' חייא בר אבא",composition='composite',scope='Attributed theological comparison, not a literal medical mechanism')
end=c('end','41a:7',"ואמר ר' אלכסנדרי אמר ר' חייא בר אבא ואמרי לה אמר ר' יהושע בן לוי כיון שהגיע קיצו של אדם הכל מושלים בו שנאמר (בראשית ד, יד) והיה כל מוצאי יהרגני",'When a person’s appointed end arrives, everything can master him, supported by Cain’s fear of being killed by anyone.',scope='Attributed alternatively to Hiyya bar Abba via Alexandri or Yehoshua ben Levi; not resolved by order')
a.add('end.variant','attributions',dict(surface="אמר ר' חייא בר אבא ואמרי לה אמר ר' יהושע בן לוי",role='speaker',candidates=["ר' חייא בר אבא","ר' יהושע בן לוי"],scope=end,transmission_chain=[]),[a.ev('41a:7',"אמר ר' חייא בר אבא ואמרי לה אמר ר' יהושע בן לוי")],[end],uncertainty=['Alternative attribution explicitly preserved.'])
rav=c('rav','41a:7','רב אמר מן הדין קרא (תהלים קיט, צא) למשפטיך עמדו היום כי הכל עבדיך','Rav supports the same idea from all being God’s servants in Psalm119.',holder='רב',scope='Alternative prooftext, not necessarily disagreement with preceding proposition')
e('rav.support',rav,end,'support','41a:7')
rider=c('rider','41a:8',None,'Rabbah bar Shila hears of a tall man thrown by a small mount at a bridge and killed, and applies the Psalm verse.',composition='composite',scope='Reported narrative exemplifying vulnerability; exact mount description retained in evidence')
scorpion=c('scorpion','41a:9',None,'Shmuel observes the narrated river-crossing creature episode ending in a fatal sting and applies the same Psalm.',holder='שמואל',composition='composite',scope='Parenthetical קרוקיתא דעקרבא and אקרוקתא preserved; no zoological normalization imposed')
visit=c('visit','41a:10','אמר שמואל אין מבקרין את החולה אלא למי שחלצתו חמה','Shmuel limits visiting to the fever case expressed as חלצתו חמה.',holder='שמואל',scope='Ancient visitation instruction, term preserved rather than assuming fever ended')
excludeq=q('excludeq','41a:10','לאפוקי מאי','Which illnesses does that exclude?')
excluded=c('excluded','41a:10',"לאפוקי הא דתניא ר' יוסי בן פרטא אומר משום ר' אליעזר אין מבקרין לא חולי מעיים ולא חולי העין ולא מחושי הראש",'A baraita attributed to Rabbi Eliezer via Rabbi Yosei ben Parta excludes intestinal, eye and head complaints from visits.',holder="ר' אליעזר",composition='composite',scope='Source-specific list, not modern medical advice')
embarrass=c('embarrass','41a:10','בשלמא חולי מעיים משום כיסופא','Embarrassment is offered as the reason for the intestinal case.',scope='Social rationale within source')
eyeq=q('eyeq','41a:10','אלא חולי העין ומחושי הראש מאי טעמא','Why exclude eye and head complaints?')
speech=c('speech','41a:11','משום דרב יהודה דאמר רב יהודה דיבורא קשיא לעינא ומעלי לאישתא','Rav Yehuda’s statement says speech harms the eye and benefits fever.',holder='רב יהודה',scope='Attributed ancient therapeutic premise, not independently endorsed')
e('excluded.answer',excluded,excludeq,'answer','41a:10');e('speech.answer',speech,eyeq,'answer','41a:11')
fever=c('fever','41a:11','אמר רבא האי אישתא אי לאו דפרוונקא דמלאכא דמותא מעלי','Rava says fever would be beneficial were it not a messenger of death, comparing it to periodic protection and an antidote.',extra=[('41b:1','כחיזרא לדיקלי חד לתלתין יומין וכי תירייקי לגופא')],holder='רבא',mode='conditional',composition='composite',scope='Cross-page qualified ancient comparison, not recommendation to induce fever')
reject=c('reject','41b:1','רב נחמן בר יצחק אמר לא היא ולא תירייקה','Rav Nahman bar Yitzhak rejects both fever and its antidote-like benefit.',holder='רב נחמן בר יצחק',scope='Explicit dissent from favorable fever comparison')
e('reject.objection',reject,fever,'objection','41b:1')
porridge=c('porridge','41b:2','אמר רבה בר יונתן אמר רב יחיאל ערסן יפה לחולה לרפואתו','Rav Yehiel, through Rabbah bar Yonatan, says arsan is beneficial for a patient’s recovery.',holder='רב יחיאל',scope='Attributed ancient food remedy, not treatment recommendation')
whatq=q('whatq','41b:2','מאי ערסן','What is arsan?')
yonatan=c('yonatan','41b:2',"אמר ר' יונתן חושלא דשערי עתיקתא דריש נפיא",'Rabbi Yonatan identifies it with coarse old barley from the first sifting.',holder="ר' יונתן",scope='First food identification; exact technical terms in evidence')
cook=c('cook','41b:2','אמר אביי בעיין בישולא כעין בישרא דתורא','Abaye says it requires cooking comparable to ox meat.',holder='אביי',scope='First cooking instruction, within ancient account')
yosefFood=c('yosefFood','41b:2','רב יוסף אמר סמידי דשערי עתיקתא דריש נפיא','Rav Yosef identifies it with fine old-barley meal from the first sifting.',holder='רב יוסף',scope='Alternative identification')
cook2=c('cook2','41b:2','אמר אביי בעיין בישולא כבשרא דתורא','Abaye again specifies cooking comparable to ox meat.',holder='אביי',scope='Repeated instruction in second identification retained')
e('yonatan.answer',yonatan,whatq,'answer','41b:2');e('yosefFood.answer',yosefFood,whatq,'answer','41b:2')
burdam=c('burdam','41b:3','א"ר יוחנן בורדם אין מבקרים ואין מזכירין שמו','Rabbi Yohanan says not to visit or mention בורדם.',holder='רבי יוחנן',composition='composite',scope='Historical illness label retained, not diagnostically equated to a modern disease')
whyq=q('whyq','41b:3','מ"ט','Why?')
spring=c('spring','41b:3','א"ר אלעזר מפני שהוא כמעיין הנובע','Rabbi Elazar says it is like a flowing spring.',holder='רבי אלעזר',scope='Source’s descriptive rationale')
name=c('name','41b:3','וא"ר אלעזר למה נקרא שמו בורדם שהוא כמעיין הנובע','Rabbi Elazar also explains the name through the same flowing-spring description.',holder='רבי אלעזר',scope='Separate etymological statement, not merged with reason question')
e('spring.answer',spring,whyq,'answer','41b:3')
healQ=q('healQ','41b:4','היכי קתני','How is personal versus property healing to be read?')
fee=c('fee','41b:4','אילימא דרפואת נפש בחנם רפואת ממון בשכר ליתני הכי מרפאהו בחנם אבל לא בשכר','The free-versus-paid interpretation is rejected because the Mishnah could simply have said so.',mode='rejected',scope='Rejected fee-based reconstruction')
body=c('body','41b:4','אלא רפואת נפש גופו רפואת ממון בהמתו','The distinction is treatment of his body versus his animal.',composition='composite',scope='Final identification of Mishnah’s two categories')
advice=c('advice','41b:4','א"ר זוטרא בר טוביה אמר רב אבל אומר לו סם פלוני יפה לה סם פלוני רע לה','Rav, through Zutra bar Toviyya, nevertheless permits stating which remedy is good or bad for the animal.',holder='רב',composition='composite',scope='Advice exception to direct animal treatment under benefit vow; no actual remedy prescribed here')
e('body.answer',body,healQ,'answer','41b:4');e('advice.qualification',advice,body,'qualification','41b:4')
for key,ref,claim in [('forgive','41a:3',forgive),('miracle','41a:6',miracle)]:a.add(key+'.chain','attributions',dict(surface="אמר ר' אלכסנדרי אמר ר' חייא בר אבא",role='transmitter',candidates=["ר' אלכסנדרי"],scope=claim,transmission_chain=["ר' אלכסנדרי","ר' חייא בר אבא"]),[a.ev(ref,"אמר ר' אלכסנדרי אמר ר' חייא בר אבא")],[claim])
a.notes={
'40b:3':'Reread Ami/Rav exile-equipment teaching and cross-page mat completion.',
'41a:1':'Reread mat completion separately from five alternative deprivation readings, preserving anonymous salt/fat view.',
'41a:2':'Reread Abaye and Western knowledge aphorisms as attributed rhetoric.',
'41a:3':'Reread Alexandri/Hiyya forgiveness, Hamnuna youth and Yosef memory interpretations separately.',
'41a:4':'Reread Yosef illness, Abaye restoration and recurring reminder dialogue.',
'41a:5':'Reread13/7/6 counts, launderer role, Hiyya recovery work and both praise versions.',
'41a:6':'Reread attributed furnace/illness miracle comparison.',
'41a:7':'Reread alternative Hiyya/Yehoshua ben Levi attribution and Rav’s different supporting verse.',
'41a:8':'Reread Rabbah bar Shila reported fatal mount/bridge incident and verse application.',
'41a:9':'Reread Shmuel creature/river/sting narrative with parenthetical species wording preserved.',
'41a:10':'Reread Shmuel fever visitation rule, three exclusions, embarrassment rationale and eye/head question.',
'41a:11':'Reread Yehuda speech premise and Rava qualified fever comparison spanning page.',
'41b:1':'Reread fever comparison completion and Nahman bar Yitzhak explicit rejection.',
'41b:2':'Reread Yehiel/ Yonatan food-remedy report, two arsan identifications and both Abaye cooking instructions.',
'41b:3':'Reread Yohanan burdam rule, Elazar reason and separate name explanation without modern diagnosis.',
'41b:4':'Reread rejected fee interpretation, body/animal resolution and Rav advice exception.'}
if __name__=='__main__':a.save()
