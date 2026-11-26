"""Abraham aggadah, alternative interpretations, allegory and chapter close."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r032.';a.OUTPUT='continuation_032.json'
c=a.c;q=b.q;e=a.edge
a.structure('abraham',['32a:'+str(i) for i in range(8,20)]+['32b:1','32b:2'],'Abraham, completeness, astrology and distinct interpretations')
a.structure('allegory',['32b:3','32b:4','32b:5'],'Body-city and ten-rulers allegories')
a.structure('priest',['32b:6','32b:7','32b:8'],'Shem, blessing order and priesthood interpretation')
a.structure('end',['32b:9'],'End of four-vows chapter')
tremble=c('tremble','32a:8','אמר רב יהודה אמר רב בשעה שאמר לו הקב"ה לאברהם אבינו התהלך לפני והיה תמים (בראשית יז, א) אחזתו רעדה אמר שמא יש בי דבר מגונה','Rav, transmitted by Rav Yehuda, depicts Abraham trembling at the command to be complete and fearing a fault in himself.',holder='רב',composition='composite',scope='Attributed narrative reconstruction of Abraham’s reaction')
calm=c('calm','32a:8','כיוון שאמר לו ואתנה בריתי ביני ובינך (בראשית יז, ב) נתקררה דעתו','Abraham is reassured by the covenant declaration.',holder='רב',scope='Continuation of Rav’s narrative')
for key,claim in [('tremble',tremble),('calm',calm)]:a.add(key+'.chain','attributions',dict(surface='אמר רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope=claim,transmission_chain=['רב יהודה','רב']),[a.ev('32a:8','אמר רב יהודה אמר רב')],[claim])
star=c('star','32a:9','אמר לפניו רבונו של עולם הסתכלתי במזל שלי ואין לי אלא בן אחד','The exposition attributes to Abraham an astrological expectation of only one son.',scope='Narrative speech attributed to Abraham; exact בן אחד preserved rather than harmonized to other versions')
leave=c('leave','32a:9','אמר לו צא מאיצטגנינות שלך אין מזל לישראל','The divine reply tells him to leave his astrology and states אין מזל לישראל.',scope='Source’s theological reply, not empirical endorsement of astrology')
e('leave.correction',leave,star,'correction','32a:9')
yitzhak=c('yitzhak','32a:10',None,'Rabbi Yitzhak says God acts with completeness toward one who makes himself complete, citing Psalms.',holder='רבי יצחק',scope='Attributed ethical-theological maxim')
hoshaya=c('hoshaya','32a:11',None,'Rabbi Hoshaya says the time favors one who makes himself complete, connecting Abraham’s completeness and fatherhood-of-nations verses.',holder='רבי הושעיא',scope='Separate attributed maxim and two-verse derivation')
omen=c('omen','32a:12','אמר רבי כל המנחש לו נחש שנאמר כי לא נחש ביעקב (במדבר כג, כג)','Rabbi says one who practices divination is subject to divination-related consequence, initially citing כי לא נחש ביעקב.',holder='רבי',scope='Exact לו/לא wordplay generates correction; no practical divination guidance')
spelling=q('spelling','32a:12','והא בלמ"ד אל"ף כתיב','But is the verse not spelled לא with aleph, rather than לו?')
measure=c('measure','32a:12','אלא משום מידה כנגד מידה','The basis is instead measure for measure.',scope='Corrects the proposed spelling-based derivation without retracting the maxim')
e('measure.answer',measure,spelling,'answer','32a:12');e('measure.correction',measure,omen,'correction','32a:12')
ahava=c('ahava','32a:13',None,'Ahava son of Rabbi Zeira teaches that one who does not practice divination enters a domain even ministering angels cannot enter, citing the verse against divination in Jacob and Israel.',holder='אהבה בריה דרבי זירא',scope='Attributed homiletic reward claim')
why=q('why','32a:14','מפני מה נענש אברהם אבינו ונשתעבדו בניו למצרים מאתיים ועשר שנים','Why, in this exposition, was Abraham punished with his descendants’ 210-year Egyptian servitude?',voice='רבי אלעזר')
labor=c('labor','32a:14','מפני שעשה אנגרייא בתלמידי חכמים שנאמר וירק את חניכיו ילידי ביתו (בראשית יד, יד)','Rabbi Elazar attributes it to conscripting Torah scholars, citing Abraham’s retainers.',holder='רבי אלעזר',scope='First homiletic explanation, reported by Rabbi Abbahu')
a.add('labor.chain','attributions',dict(surface='אמר רבי אבהו אמר רבי אלעזר',role='transmitter',candidates=['רבי אבהו'],scope=labor,transmission_chain=['רבי אבהו','רבי אלעזר']),[a.ev('32a:14','אמר רבי אבהו אמר רבי אלעזר')],[labor])
shmuel=c('shmuel','32a:15','ושמואל אמר מפני שהפריז על מדותיו של הקב"ה שנאמר במה אדע כי אירשנה (בראשית טו, ח)','Shmuel attributes it to Abraham’s excess in questioning God’s ways, citing במה אדע כי אירשנה.',holder='שמואל',scope='Second homiletic explanation; Rav is not the opposing speaker in this question')
yohanan=c('yohanan','32a:15','ורבי יוחנן אמר שהפריש בני אדם מלהכנס תחת כנפי השכינה שנאמר תן לי הנפש והרכוש קח לך (בראשית יד, כא)','Rabbi Yohanan attributes it to preventing people from entering under the divine presence, citing the demand to return persons.',holder='רבי יוחנן',scope='Third homiletic explanation')
for key,claim,ref in [('labor',labor,'32a:14'),('shmuel',shmuel,'32a:15'),('yohanan',yohanan,'32a:15')]:e(key+'.answer',claim,why,'answer',ref)
torah=c('torah','32a:16','רב אמר שהוריקן בתורה','Rav interprets וירק through Torah: שהוריקן בתורה.',holder='רב',scope='Interpretation of retainers verse; precise הוריקן wording retained without choosing an unstated lexical gloss')
gold=c('gold','32a:16','ושמואל אמר שהוריקן בזהב','Shmuel interprets the same phrase through gold: שהוריקן בזהב.',holder='שמואל',scope='Actual Rav/Shmuel contrast in this verse, distinct from previous three-way servitude explanations')
e('gold.distinction',gold,torah,'distinction','32a:16')
equiv=c('equiv','32a:17','אמר רבי אמי בר אבא אליעזר כנגד כולם','Rabbi Ami bar Abba explains Eliezer as equivalent to all 318.',holder='רבי אמי בר אבא',scope='First interpretation of the verse’s number')
gem=c('gem','32a:17','איכא דאמרי אליעזר הוא דחושבניה הכי הוי','An alternative says it was Eliezer himself, whose name has the numerical value 318.',scope='Explicit איכא דאמרי, not conflated with equivalence interpretation')
e('gem.distinction',gem,equiv,'distinction','32a:17')
age=c('age','32a:18','ואמר רבי אמי בר אבא בן שלוש שנים הכיר אברהם את בוראו','Rabbi Ami bar Abba says Abraham recognized his Creator at age three.',holder='רבי אמי בר אבא',scope='Attributed chronology derived homiletically')
heel=c('heel','32a:18','שנאמר עקב אשר שמע אברהם בקולי (בראשית כו, ה) חושבניה מאה ושבעין ותרין','The support reads עקב numerically as 172.',scope='Source’s gematria, used in the age derivation')
e('heel.support',heel,age,'support','32a:18')
satan=c('satan','32a:19',None,'Rami bar Abba gives השטן the numerical value 364.',extra=[('32b:1','השטן בחושבניה תלת מאה ושיתין וארבעה')],holder='רמי בר אבא',scope='Cross-page sentence; printed רמי differs from preceding רבי אמי, not silently harmonized')
limbs=c('limbs','32b:1','ואמר רמי בר אבא כתיב אברם, וכתיב אברהם בתחילה המליכו הקב"ה על מאתיים וארבעים ושלושה איברים ולבסוף המליכו על מאתיים וארבעים ושמונה איברים','Rami bar Abba relates Abram/Abraham to dominion first over 243 and then 248 limbs.',holder='רמי בר אבא',composition='composite',scope='Homiletic numerical anthropology, not an anatomical count asserted independently')
five=c('five','32b:2',None,'The five added are two eyes, two ears and the sexual organ.',composition='composite',scope='Source’s explicit enumeration explaining the five-unit difference')
e('five.qualification',five,limbs,'qualification','32b:2')
allegq=q('allegq','32b:3',"ואמר רמי בר אבא מאי דכתיב עיר קטנה ואנשים וגו' (קהלת ט, יד)",'How does Rami bar Abba interpret the small-city verse?',voice='רמי בר אבא')
city=c('city','32b:3','עיר קטנה זה הגוף ואנשים בה מעט אלו איברים','The small city represents the body and its few inhabitants the limbs.',holder='רמי בר אבא',composition='composite',scope='Explicit allegorical mapping, not literal urban account')
king=c('king','32b:3','ובא אליה מלך גדול וסבב אותה זה יצר הרע ובנה עליה מצודים וחרמים אלו עוונות','The great besieging king represents the evil inclination; his traps represent sins.',holder='רמי בר אבא',composition='composite',scope='Continuation of city allegory')
wise=c('wise','32b:4','ומצא בה איש מסכן וחכם זה יצר טוב','The poor wise man represents the good inclination.',holder='רמי בר אבא',scope='Continuation of same exposition')
save=c('save','32b:4','ומלט הוא את העיר בחכמתו זו תשובה ומעשים טובים','Saving the city by wisdom represents repentance and good deeds.',holder='רמי בר אבא',scope='Ethical allegory')
forget=c('forget','32b:4','ואדם לא זכר את האיש המסכן ההוא דבשעת יצר הרע לית דמדכר ליה ליצר טוב','Forgetting the poor man represents failing to recall the good inclination while under the evil inclination.',holder='רמי בר אבא',scope='Allegorical explanation of concluding verse')
for key,claim,ref in [('city',city,'32b:3'),('king',king,'32b:3'),('wise',wise,'32b:4'),('save',save,'32b:4'),('forget',forget,'32b:4')]:e(key+'.answer',claim,allegq,'answer',ref)
wisdom=c('wisdom','32b:5','החכמה תעוז לחכם זו תשובה ומעשים טובים','Wisdom strengthening the wise is interpreted as repentance and good deeds.',scope='Adjacent Ecclesiastes exposition')
ten=c('ten','32b:5','מעשרה שליטים שתי עיניים ושתי אזניים ושתי ידיים ושתי רגליים וראש הגוייה ופה','The ten rulers are two eyes, two ears, two hands, two feet, the sexual organ and mouth.',composition='composite',scope='Exact allegorical ten-member inventory')
shem=c('shem','32b:6','אמר רבי זכריה משום רבי ישמעאל ביקש הקב"ה להוציא כהונה משֵם שנאמר והוא כהן לאל עליון (בראשית יד, יח)','Rabbi Yishmael, transmitted by Rabbi Zekharya, teaches that God intended priesthood to descend from Shem, citing his priesthood.',holder='רבי ישמעאל',scope='Source’s identification and homiletic genealogy')
order=c('order','32b:6','כיוון שהקדים ברכת אברהם לברכת המקום הוציאה מאברהם','Because Shem blessed Abraham before God, priesthood instead descended from Abraham.',holder='רבי ישמעאל',scope='Exposition’s causal claim')
for key,claim in [('shem',shem),('order',order)]:a.add(key+'.chain','attributions',dict(surface='אמר רבי זכריה משום רבי ישמעאל',role='transmitter',candidates=['רבי זכריה'],scope=claim,transmission_chain=['רבי זכריה','רבי ישמעאל']),[a.ev('32b:6','אמר רבי זכריה משום רבי ישמעאל')],[claim])
bless=c('bless','32b:7','שנאמר ויברכהו ויאמר ברוך אברם לאל עליון קונה שמים וארץ וברוך אל עליון (בראשית יד יט-כ)','The exposition quotes the order of blessings: Abram, then God.',scope='Source evidence for the alleged prioritization')
ob=c('ob','32b:7','אמר לו אברהם וכי מקדימין ברכת עבד לברכת קונו','Abraham is portrayed objecting to blessing a servant before his master.',scope='Embedded rhetorical question in attributed narrative')
transfer=c('transfer','32b:7','מיד נתנה לאברהם שנאמר נאם ה\' לאדני שב לימיני עד אשית אויביך הדום לרגליך (תהלים קי, א)','The account says priesthood was immediately given to Abraham and supports it from Psalm110.',scope='Homiletic identification within narrative')
speech=c('speech','32b:7',"ובתריה כתיב נשבע ה' ולא ינחם אתה כהן לעולם על דברתי מלכי צדק (תהלים קי, ד) על דיבורו של מלכי צדק",'The phrase על דברתי מלכי צדק is read as on account of Melchizedek’s speech.',scope='Wordplay explaining priesthood transfer')
desc=c('desc','32b:8',None,'The concluding reading limits והוא כהן to him personally, excluding his descendants from that priesthood.',scope='Local homiletic conclusion about Shem’s line')
e('bless.support',bless,order,'support','32b:7');e('speech.support',speech,order,'support','32b:7')
a.add('chapter.u','utterances',dict(textual_voice='anonymous textual marker',discourse_role='chapter conclusion',composition='atomic'),[a.ev('32b:9')])
a.add('chapter.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'chapter.u',transmission_chain=[]),[a.ev('32b:9')],[a.PREFIX+'chapter.u'])
a.notes={
'32a:8':'Reread Yehuda-to-Rav chain, Abraham trembling/self-question and covenant reassurance separately.',
'32a:9':'Reread exact one-son astrological expectation and divine rejection; did not harmonize with other versions.',
'32a:10':'Reread Yitzhak ethical maxim and Psalm support.',
'32a:11':'Reread Hoshaya maxim and both Genesis verses.',
'32a:12':'Reread Rabbi maxim, לא/לו spelling objection and corrected measure-for-measure basis.',
'32a:13':'Reread Ahava lineage, no-divination reward and exact verse.',
'32a:14':'Reread Abbahu-to-Elazar chain, 210-year reason question and conscription answer.',
'32a:15':'Reread Shmuel and Yohanan alternative explanations with distinct verses; not mislabeled Rav/Shmuel dispute.',
'32a:16':'Reread actual Rav/Shmuel Torah/gold contrast on וירק; retained exact ambiguous הוריקן wording.',
'32a:17':'Reread Ami bar Abba equivalence and explicit alternative numerical Eliezer interpretation.',
'32a:18':'Reread age-three assertion and עקב172 derivation.',
'32a:19':'Reread dangling Rami bar Abba attribution attached across page to Satan364; preserved name variant.',
'32b:1':'Reread cross-page364 completion and separate Abram/Abraham243/248 exposition.',
'32b:2':'Reread all five named added members.',
'32b:3':'Reread interpretive question and each city/body, inhabitants/limbs, king/inclination, traps/sins mapping.',
'32b:4':'Reread wise-man/good-inclination, saving/repentance-and-deeds and forgetting mapping.',
'32b:5':'Reread wisdom ethical mapping and exact ten-member ruler enumeration.',
'32b:6':'Reread Zekharya/Yishmael chain, intended Shem priesthood and blessing-order transfer.',
'32b:7':'Reread blessing verse, Abraham objection, immediate transfer and both Psalm supports/wordplay.',
'32b:8':'Reread personal-priesthood versus descendants conclusion.',
'32b:9':'Reread chapter-ending marker and markup; retained textual utterance and structure, no legal claim invented.'}
if __name__=='__main__':a.save()
