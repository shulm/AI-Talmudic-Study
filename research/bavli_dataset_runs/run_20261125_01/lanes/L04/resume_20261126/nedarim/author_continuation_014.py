"""Manual chapter boundary, tangible objects, and comparison to forbidden things."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r014.';a.OUTPUT='continuation_014.json'
c=a.c;q=a.q;e=a.edge
a.structure('lamb',['13a:'+str(i) for i in range(8,13)],'Article/preposition variants and negative eating formulas')
a.structure('offering',['13a:13','13a:14','13a:15','13b:1','13b:2'],'Offering names and the distinction between הקרבן and הא קרבן')
a.structure('limbs',['13b:3','13b:4','13b:5'],'Vows concerning mouth, hands and feet as tangible objects')
a.structure('colophon',['13b:6'],'Printed ending of the first chapter')
a.structure('forbidden',['13b:7','13b:8','13b:9','13b:10']+['14a:'+str(i) for i in range(1,10)],'Comparisons to inherently forbidden objects and precautions against treating vows lightly')
a.speech('lemma',[a.ev('13a:8')],None,'quoted Mishnah lemma','atomic')
variants=c('variants','13a:9','תנא אימרא לאימרא כאימרא דירים לדירים כדירים עצים לעצים כעצים אישים לאישים כאישים מזבח למזבח כמזבח היכל להיכל כהיכל ירושלים לירושלים כירושלים','The teaching gives plain, ל-prefixed and כ-prefixed forms for אימרא, דירים, עצים, אישים, מזבח, היכל and ירושלים.',composition='composite',scope='Explicit seven groups of three printed forms, no silent vowel normalization')
eat=c('eat','13a:9','כולן שאוכל לך אסור','All the listed variants prohibit with שאוכל לך.',conditions=['listed form plus שאוכל לך'],scope='Grouped formulation rule')
noteat=c('noteat','13a:9','לא אוכל לך מותר','With לא אוכל לך the listed case is permitted.',conditions=['listed negative-eating formulation'],scope='Textual distinction clarified in13a:12')
who=q('who','13a:10','מאן שמעינן ליה דלא שני ליה אימרא לאימרא כאימרא','Who does not distinguish אימרא, לאימרא and כאימרא?')
meir=c('meir','13a:10','רבי מאיר היא','The discussion identifies Rabbi Meir.',scope='Attribution of grouped formula equivalence')
e('meir.answer',meir,who,'answer','13a:10')
challenge=c('challenge','13a:11','אימא סיפא וכולן לא אוכל לך מותר והתנן לקרבן לא אוכל לך רבי מאיר אוסר','The objection contrasts the baraita’s negative permission with Rabbi Meir’s prohibition of לקרבן לא אוכל לך.',composition='composite',scope='Explicit conflicting formulation comparison')
abba=c('abba','13a:11','ואמר רבי אבא נעשה כאומר לקרבן יהא לפיכך לא אוכל לך','Rabbi Abba explains it as: let it be an offering, therefore I will not eat.',holder='רבי אבא',scope='Repeated explanatory occurrence retained')
dist=c('dist','13a:12',None,'The reply distinguishes לא אימרא from לאימרא.',scope='Printed two-form distinction; no unprinted vocalization or broad generalization supplied')
e('challenge.objection',challenge,noteat,'objection','13a:11');e('abba.support',abba,challenge,'support','13a:11');e('dist.answer',dist,challenge,'answer','13a:12')
listc=c('list','13a:13','האומר קרבן עולה מנחה חטאת תודה שלמים שאני אוכל לך אסור','The Mishnah prohibits the eating formula with קרבן, עולה, מנחה, חטאת, תודה or שלמים.',composition='composite',conditions=['listed sacrificial term with שאני אוכל לך'],scope='Six-term Mishnah group')
yehuda=c('yehuda','13a:13','רבי יהודה מתיר','Rabbi Yehuda permits this group.',holder='רבי יהודה',conditions=['same listed formulations'])
pref=c('pref','13a:13','הקרבן כקרבן קרבן שאוכל לך אסור','הקרבן, כקרבן and קרבן with שאוכל לך prohibit.',composition='composite',scope='Mishnah’s second three-form group')
neg=c('neg','13a:13','לקרבן לא אוכל לך רבי מאיר אוסר','Rabbi Meir prohibits לקרבן לא אוכל לך.',holder='רבי מאיר',conditions=['exact negative formulation'])
attrib=c('attrib','13a:14',None,'The anonymous three-form rule is identified as Rabbi Meir’s view because he does not distinguish the corresponding אימרא forms.',composition='composite',scope='Anonymous explanation of Mishnah attribution')
e('attrib.qualification',attrib,pref,'qualification','13a:14')
contra=c('contra','13a:15',None,'A baraita says the sages agree with Rabbi Yehuda that הא קרבן, הא עולה, הא מנחה or הא חטאת with שאוכל לך permit, because this is an invocation by the life of the offering.',composition='composite',scope='Explicit four-form quotation and rationale challenging conflation with הקרבן; bracketed introduction preserved')
split=c('split','13b:1',None,'The answer distinguishes הא קרבן from הקרבן: the separated form expresses חיי קרבן.',composition='composite',scope='Exact orthographic distinction and source’s explanation')
e('contra.objection',contra,pref,'objection','13a:15');e('split.answer',split,contra,'answer','13b:1')
whyneg=q('whyneg','13b:2','והא לית ליה לרבי מאיר מכלל לאו אתה שומע הן','How can Rabbi Meir prohibit when he does not infer affirmation from negation?')
repeat=c('repeat','13b:2','אמר רבי אבא נעשה כאומר לקרבן יהא לפיכך לא אוכל לך','Rabbi Abba again explains: let it be an offering, therefore I will not eat.',holder='רבי אבא',scope='Repeated answer to explicit implication question')
e('repeat.answer',repeat,whyneg,'answer','13b:2')
mouth=c('mouth','13b:3','קונם פי מדבר עמך','The Mishnah includes קונם פי מדבר עמך in its prohibitory rule.',conditions=['mouth-speech wording'],scope='Mishnah object formulation, refined as tangible mouth below')
hands=c('hands','13b:3','ידי עושה עמך','The Mishnah includes ידי עושה עמך in the rule.',conditions=['hand-action wording'],scope='Continuation under קונם')
feet=c('feet','13b:3','רגלי מהלכת עמך אסור','The Mishnah prohibits the corresponding feet-walking formulation.',conditions=['feet-walking wording'],scope='Mishnah')
vowadv=c('vowadv','13b:4','חומר בנדרים שהנדרים חלין על המצווה כברשות מה שאין כן בשבועות','The contrasting teaching says vows take effect on commandments as on optional matters, unlike oaths.',composition='composite',scope='Quoted relative stringency; full conditions not expanded beyond citation')
oathadv=c('oathadv','13b:4','וחומר בשבועות שהשבועות חלות על דבר שיש בו ממש ושאין בו ממש מה שאין כן בנדרים','Oaths extend to tangible and intangible matters, unlike vows.',composition='composite',scope='Quoted rule generating objection to speech/action/walking formulations')
e('oathadv.objection',oathadv,mouth,'objection','13b:4','ורמינהו')
body=c('body','13b:5','אמר רב יהודה באומר ייאסר פי לדיבורי ידיי למעשיהם רגליי להילוכן','Rav Yehuda explains that the mouth, hands and feet themselves are prohibited for their speech, actions and walking.',holder='רב יהודה',composition='composite',scope='Three tangible-body-part formulations, not Rav himself')
precision=c('precision','13b:5','דייקא נמי דקתני פי מדבר עמך ולא קתני שאני מדבר עמך','The Mishnah’s “my mouth speaking” rather than “that I speak” supports this reading.',scope='Explicit source-wording proof')
e('body.answer',body,oathadv,'answer','13b:5');e('precision.support',precision,body,'support','13b:5')
a.speech('chapter',[a.ev('13b:6')],None,'printed chapter-ending formula','atomic')
ordinary=c('ordinary','13b:7','חולין שאוכל לך','The second chapter permits חולין שאוכל לך.',conditions=['plain חולין'],scope='Mishnah’s permitted-form list')
forbidden=c('forbidden','13b:7','כבשר חזיר כעבודה זרה כעורות לבובין כנבילות וטריפות כשקצים ורמשים','It lists comparisons to pork, idolatry, עורות לבובין, carcasses, torn animals, שקצים and רמשים as permitted.',composition='composite',scope='Exact categories of inherently forbidden comparison objects; unfamiliar terms retained')
gifts=c('gifts','13b:7','כחלת אהרן וכתרומתו מותר','Comparison to Aaron’s challah and terumah is permitted.',composition='composite',scope='Mishnah’s two gift categories')
mother=c('mother','13b:8',None,'For a husband saying to his wife הרי את עלי כאימא, an opening is sought elsewhere so he should not treat this lightly.',conditions=['wife compared to mother'],composition='composite',scope='Mishnah’s precautionary release procedure and explicit reason')
infer=c('infer','13b:9',None,'The initial inference contrasts plain חולין with לחולין, interpreting the latter as not unconsecrated but an offering.',mode='challenged',composition='composite',scope='Initial account of Mishnah wording')
tanna=q('tanna','13b:10','מני מתניתין','Whose view is this Mishnah?')
mexclude=c('mexclude','13b:10','אי רבי מאיר הא לית ליה מכלל','Rabbi Meir is problematic because he does not infer affirmation from negation.',extra=[('14a:1','לאו אתה שומע הן')],scope='Cross-page attribution premise')
duplicate=q('duplicate','14a:1','ואלא רבי יהודה היינו רישא','If Rabbi Yehuda, is this not already the earlier Mishnah?')
incidental=c('incidental','14a:2',None,'The answer says חולין is repeated incidentally alongside pork and idolatry comparisons.',scope='Explanation for apparently redundant opening item')
e('incidental.answer',incidental,duplicate,'answer','14a:2')
ravina=c('ravina','14a:3','רבינא אמר הכי קתני אלו מותרין כחולין כבשר חזיר כעבודת כוכבים','Ravina reads the list as: these comparisons, like unconsecrated, pork and idolatry, are permitted.',holder='רבינא',mode='challenged',composition='composite',scope='Alternative reconstruction, challenged next')
need=c('need','14a:3','ואי לא תנא חולין הוה אמינא בעי שאלה','Without חולין, one might require consultation for release.',mode='rejected',scope='Proposed purpose for wording')
possible=q('possible','14a:4','ומי איכא לאסוקי על דעתא הכי','Can that be supposed?')
tail=c('tail','14a:4','הא מדקתני סיפא האומר לאשתו הרי את עלי כאימא פותחין לו פתח ממקום אחר מכלל דרישא לא בעיא שאלה','The special wife/mother release clause already implies the opening list requires no release consultation.',scope='Explicit inference from separately qualified ending',composition='composite')
clear=c('clear','14a:4','אלא מחוורתא חולין ממילא נסבה','The conclusion returns to חולין being included incidentally.',scope='Local preferred explanation of redundant wording')
e('tail.objection',tail,need,'objection','14a:4');e('clear.correction',clear,ravina,'correction','14a:4')
sourceq=q('sourceq','14a:5','מנא הני מילי','What is the scriptural source for these rules?')
vowed=c('vowed','14a:5',"אמר קרא איש כי ידור נדר לה' עד שידור בדבר הנדור",'The verse requires a vow referring to something made forbidden through a vow.',scope='Derivation distinguishing דבר הנדור from inherently forbidden objects')
e('vowed.answer',vowed,sourceq,'answer','14a:5')
assurq=q('assurq','14a:6','אי הכי אפילו בדבר האסור נמי דהא כתיב לאסור איסר על נפשו','Should לאסור איסר also include comparison to inherently forbidden objects?')
allocate=c('allocate','14a:6',"לאסור איסר מבעי ליה לכדתניא איזהו איסר האמור בתורה וכו':",'The reply allocates לאסור איסר to the previously cited teaching about איסר.',scope='Explicit abbreviated cross-reference, not a fresh full quotation')
e('allocate.answer',allocate,assurq,'answer','14a:6')
bar=c('bar','14a:7','ורמינהו הרי את עלי כבשר אימא כבשר אחותי כערלה וככלאי הכרם לא אמר כלום','A baraita gives no effect to wife-comparisons with mother’s flesh, sister’s flesh, orlah and vineyard mixed species.',composition='composite',scope='Four-item objection to the Mishnah’s required release procedure')
abaye=c('abaye','14a:8','אמר אביי לא אמר כלום מדאורייתא וצריך שאלה מדרבנן','Abaye distinguishes no effect under Torah law from a rabbinic requirement of release consultation.',holder='אביי',composition='composite',scope='First reconciliation')
rava=c('rava','14a:8','רבא אמר הא בתלמידי חכמים הא בעם הארץ','Rava distinguishes scholars from unlearned people.',holder='רבא',scope='Second reconciliation; scholarly case needs no consultation, layperson precaution follows from adjacent support')
e('bar.objection',bar,mother,'objection','14a:7');e('abaye.answer',abaye,bar,'answer','14a:8');e('rava.answer',rava,bar,'answer','14a:8')
torah=c('torah','14a:9','והתניא הנודר בתורה לא אמר כלום','A cited teaching gives no effect to vowing by the Torah.',scope='Parallel rule offered as support for differentiated consultation')
yohanan=c('yohanan','14a:9','ואמר רבי יוחנן וצריך שאלה לחכם','Rabbi Yohanan nevertheless requires consulting a sage for release.',holder='רבי יוחנן',scope='Reported precaution concerning Torah vow')
nahman=c('nahman','14a:9','ואמר רב נחמן ותלמיד חכם אינו צריך שאלה','Rav Nahman says a scholar does not need that consultation.',holder='רב נחמן',conditions=['תלמיד חכם'],scope='Qualification of prior rule')
e('nahman.qualification',nahman,yohanan,'qualification','14a:9');e('nahman.support',nahman,rava,'support','14a:9')
a.notes={
'13a:8':'Reread source lemma as utterance without inventing a proposition.',
'13a:9':'Reread all seven three-form sets and positive/negative outcome distinction; grouped list expressly composite.',
'13a:10':'Reread identification question and Rabbi Meir answer.',
'13a:11':'Reread repeated negative challenge and Rabbi Abba explanation.',
'13a:12':'Reread exact לא אימרא/לאימרא distinction, no vowels fabricated.',
'13a:13':'Reread all six offering terms, Rabbi Yehuda permission, three-prefixed forms and Rabbi Meir negative prohibition.',
'13a:14':'Reread anonymous Rabbi Meir identification with its stated rationale.',
'13a:15':'Reread four separated הא forms and life-of-offering rationale, preserving bracketed source introduction.',
'13b:1':'Reread orthographic separation explanation.',
'13b:2':'Reread explicit implication objection and repeated Rabbi Abba answer.',
'13b:3':'Reread mouth/hands/feet formulations separately.',
'13b:4':'Reread both relative-stringency rules, including commandment scope and tangibility.',
'13b:5':'Reread Rav Yehuda tangible-body-part explanation and precise wording proof.',
'13b:6':'Reread chapter-ending printed formula and markup; structure/utterance only, no invented legal claim, question or position.',
'13b:7':'Reread entire permitted-object list, retaining unfamiliar labels and both Aaron gifts.',
'13b:8':'Reread wife/mother condition, alternative opening and explicit anti-frivolity purpose.',
'13b:9':'Reread tentative plain/prefixed חולין inference.',
'13b:10':'Reread tanna question and unfinished Rabbi Meir premise continuing14a:1.',
'14a:1':'Reread completion of implication premise and Rabbi Yehuda redundancy question.',
'14a:2':'Reread incidental-list answer.',
'14a:3':'Reread Ravina reconstruction and proposed consultation concern.',
'14a:4':'Reread impossibility challenge, ending-based inference and explicit מחוורתא conclusion.',
'14a:5':'Reread derivation question and דבר הנדור requirement.',
'14a:6':'Reread alternative איסר derivation and allocation to earlier quoted teaching.',
'14a:7':'Reread four-item baraita objection to mother-comparison release procedure.',
'14a:8':'Reread Abaye statutory-level distinction and Rava scholar/layperson distinction without conflating them.',
'14a:9':'Reread Torah-vow parallel, Rabbi Yohanan consultation rule and Rav Nahman scholar qualification.'}
if __name__=='__main__':a.save()
