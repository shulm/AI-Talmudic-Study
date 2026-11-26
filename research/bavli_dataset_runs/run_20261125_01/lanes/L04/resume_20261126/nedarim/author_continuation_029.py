"""Vow terminology: anonymous variant assignments and context-bound group designations."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r029.';a.OUTPUT='continuation_029.json'
c=a.c;q=b.q;e=a.edge
a.structure('sea',['30a:4','30a:5','30b:1','30b:2'],'Sea travelers and land dwellers: two unassigned placements')
a.structure('sun',['30b:3','30b:4'],'Those seen by the sun')
a.structure('heads',['30b:5','30b:6','30b:7'],'Black-headed designation and local clothing rationale')
a.structure('born',['30b:'+str(i) for i in range(8,14)],'Born and to-be-born: reconstructed formulation and ordinary usage')
a.structure('groups',['31a:'+str(i) for i in range(1,9)],'Religious practice and ancestry labels within vow interpretation')
sea=c('sea','30a:4','הנודר מיורדי הים מותר ביושבי היבשה','A vow against sea travelers permits land dwellers.',scope='Mishnah’s directional category rule')
land=c('land','30a:4','מיושבי היבשה אסור מיורדי הים שיורדי הים בכלל יושבי היבשה','A vow against land dwellers includes sea travelers because they fall within land dwellers.',scope='Reverse direction includes wider category')
limit=c('limit','30a:4','לא כאלו שהולכין מעכו ליפו אלא במי שדרכו לפרש','The qualification contrasts Acre-to-Jaffa travelers with those accustomed to sailing out.',scope='Attachment to first or final clause disputed below; not preassigned')
reports=c('reports','30a:5','רב פפא ורב אחא בריה דרב איקא חד מתני ארישא וחד מתני אסיפא','Rav Pappa and Rav Aha son of Rav Ika transmit different placements, one on the first clause and one on the final clause.',composition='composite',scope='חד/חד left unassigned; continuation never identifies which named scholar holds which placement',uncertainty=['Do not assign placements by order of names.'])
first=c('first','30a:5','מאן דתני ארישא מתני הכי הנודר מיורדי הים מותר ביושבי יבשה הא ביורדי הים אסור ולא כאלו','On the first-clause reading, sea travelers are prohibited, excluding short Acre-to-Jaffa travelers as land dwellers but including habitual seafarers.',extra=[('30b:1',None)],composition='composite',scope='First unnamed transmission; clause spans page boundary')
last=c('last','30b:2',None,'On the final-clause reading, a vow against land dwellers includes not only short Acre-to-Jaffa travelers but habitual seafarers, who ultimately return to land.',composition='composite',scope='Second unnamed transmission, not assigned to either named reporter')
e('first.qualification',first,limit,'qualification','30b:1');e('last.qualification',last,limit,'qualification','30b:2')
blind=c('blind','30b:3','הנודר מרואי החמה אסור אף בסומין שלא נתכוון זה אלא למי שהחמה רואה אותן','A vow against those who see the sun includes blind people because the expression is read as those whom the sun sees.',scope='Source’s vow-language interpretation, not literal visual capacity')
sunq=q('sunq','30b:4','מאי טעמא','Why interpret the phrase this way?')
see=c('see','30b:4','מדלא קאמר מן הרואין','He did not simply say those who see.',scope='Linguistic rationale for inclusion of blind people')
fish=c('fish','30b:4','לאפוקי דגים ועוברים','Fish and fetuses are excluded.',composition='composite',scope='Source’s sunlight-exposure category, not a biological generalization')
e('see.answer',see,sunq,'answer','30b:4')
bald=c('bald','30b:5','הנודר משחורי הראש אסור בקרחין ובעלי שיבות','A vow against black-headed people includes bald and gray-haired men.',composition='composite',scope='Conventional designation rather than actual hair color')
exclude=c('exclude','30b:5','ומותר בנשים ובקטנים שאין נקראין שחורי הראש אלא אנשים','The same vow permits women and children, because the designation here names adult men.',composition='composite',scope='Mishnah’s historical language classification')
hairq=q('hairq','30b:6','מאי טעמא','Why are bald and gray-haired men included?')
hair=c('hair','30b:6','מדלא קאמר מבעלי שיער','The speaker did not say those who have hair.',scope='Lexical distinction')
e('hair.answer',hair,hairq,'answer','30b:6')
coverq=q('coverq','30b:7','מאי טעמא','Why does the designation exclude women and children?')
men=c('men','30b:7','אנשים זימנין דמיכסו רישייהו וזימנין דמגלו רישייהו','The explanation says men sometimes cover and sometimes uncover their heads.',scope='Source’s contextual customary premise, not a universal modern demographic claim')
women=c('women','30b:7','אבל נשים לעולם מיכסו וקטנים לעולם מיגלו','The explanation contrasts women as covered and children as uncovered.',composition='composite',scope='Historical categorical rationale asserted by this source')
e('men.answer',men,coverq,'answer','30b:7');e('women.answer',women,coverq,'answer','30b:7')
already=c('already','30b:8','הנודר מן הילודים מותר בנולדים','A vow against הילודים permits הנולדים.',scope='Exact lexical contrast retained; semantic interpretation follows')
future=c('future','30b:8','מן הנולדים אסור מן הילודים','A vow against הנולדים prohibits הילודים under the initial anonymous ruling.',scope='Mishnah’s reverse direction')
meir=c('meir','30b:8','רבי מאיר מתיר אף בילודים','Rabbi Meir’s printed clause permits even הילודים.',holder='רבי מאיר',scope='Compressed wording explicitly reconstructed30b:10')
sages=c('sages','30b:8','וחכמים אומרים לא נתכוון זה אלא במי שדרכו להיוולד','The sages interpret the intention as those whose way is to be born.',holder='חכמים',scope='Exclusion explained30b:13')
meirq=q('meirq','30b:9',None,'If Rabbi Meir also permits הנולדים, from whom would the vow prohibit benefit?')
reconstruct=c('reconstruct','30b:10','רבי מאיר אומר אף הנודר מן הנולדים מותר בילודים כי היכי דנודר מן הילודים מותר בנולדים','The reconstructed Rabbi Meir view permits הילודים to one vowing against הנולדים, just as the reverse vow permits הנולדים.',holder='רבי מאיר',composition='composite',scope='Explicit חסורי מיחסרא reconstruction, not permission for both classes under the same vow')
e('reconstruct.answer',reconstruct,meirq,'answer','30b:10');e('reconstruct.correction',reconstruct,meir,'correction','30b:10')
pastq=q('pastq','30b:11','אמר ליה רב פפא לאביי למימרא דנולדים דמתיילדן משמע אלא מעתה שני בניך הנולדים לך בארץ מצרים הכי נמי דאיתיילדן הוא','Rav Pappa asks Abaye whether נולדים means future births, given the verse about the two sons already born in Egypt.',voice='רב פפא')
josiahq=q('josiahq','30b:12','ואלא מאי דיילידו משמע אלא מעתה דכתיב הנה בן נולד לבית דוד יאשיהו שמו הכי נמי דהוה והא עדיין מנשה לא בא','Conversely, if it means already born, how can the future prophecy about Josiah use נולד when Manasseh had not yet come?')
both=c('both','30b:12','אלא משמע הכי ומשמע הכי ובנדרים הלך אחר לשון בני אדם','The conclusion permits both temporal meanings in Scripture and follows ordinary human usage for vows.',composition='composite',scope='Distinguishes scriptural range from operative vow usage')
e('both.answer',both,pastq,'answer','30b:12');e('both.answer2',both,josiahq,'answer','30b:12')
whichq=q('whichq','30b:13','לאפוקי מאי','What does the sages’ born-in-the-usual-way formulation exclude?')
eggs=c('eggs','30b:13','לאפוקי דגים ועופות','It excludes fish and birds.',composition='composite',scope='Source’s classification of mode of birth, distinct from sunlight exclusion')
e('eggs.answer',eggs,whichq,'answer','30b:13');e('eggs.qualification',eggs,sages,'qualification','30b:13')
sabbath=c('sabbath','31a:1','הנודר משובתי שַבָּת אסור בישראל ואסור בכותים','A vow against Sabbath-resters prohibits Israel and Kutim in this Mishnah.',composition='composite',scope='Source’s vow-language group classification')
garlic=c('garlic','31a:1','מאוכלי שום אסור בישראל ואסור בכותים','A vow against garlic-eaters likewise includes Israel and Kutim.',composition='composite',scope='Specific customary designation, not every incidental garlic consumer')
pilgrims=c('pilgrims','31a:1','מעולי ירושלים אסור בישראל ומותר בכותים','A vow against Jerusalem pilgrims includes Israel and permits Kutim.',composition='composite',scope='Difference in practice explained below')
whatq=q('whatq','31a:2','מאי שובתי שבת','What does Sabbath-resters mean?')
any=c('any','31a:2','אילימא ממקיימי שבת מאי איריא בכותים אפילו נוכרים נמי','If it merely means people observing Sabbath, the question objects that non-Jews who do so would also be included.',mode='challenged',scope='Rejected purely behavioral interpretation')
commanded=c('commanded','31a:2','אלא ממצווים על השבת','The proposed answer defines those commanded concerning Sabbath.',mode='challenged',scope='Incomplete answer challenged by pilgrimage clause')
e('commanded.answer',commanded,whatq,'answer','31a:2')
pilgrimq=q('pilgrimq','31a:3',None,'Why does the pilgrimage clause permit Kutim if being commanded alone determines membership?')
abaye=c('abaye','31a:4','אמר אביי מצווה ועושה קתני','Abaye says the teaching requires both being commanded and practicing.',holder='אביי',scope='Combined criterion resolves previous incomplete definition')
firstgroups=c('firstgroups','31a:4','בתרתי בבי קמייתא ישראל וכותים מצווין ועושין נוכרים ההוא דעבדי עושין ואינם מצווין','In the first two clauses Israel and Kutim are described as commanded and practicing, whereas non-Jews who practice are not commanded.',holder='אביי',composition='composite',scope='Source’s legal classification within Sabbath/garlic usages')
lastgroups=c('lastgroups','31a:4','בעולי ירושלים ישראל מצווין ועושין כותים מצווין ואינם עושין','For Jerusalem pilgrimage, Israel are described as commanded and practicing, while Kutim are commanded but do not practice.',holder='אביי',composition='composite',scope='Source’s reason for distinct third-clause outcome')
e('abaye.answer',abaye,pilgrimq,'answer','31a:4');e('abaye.qualification',abaye,commanded,'qualification','31a:4')
noah=c('noah','31a:5','קונם שאיני נהנה לבני נוח מותר בישראל ואסור בנוכרים','A benefit vow against descendants of Noah permits Israel and prohibits non-Jews.',composition='composite',scope='Conventional vow designation, not denial of genealogy')
noahq=q('noahq','31a:6','וישראל מי נפיק מכלל בני נח','Are Israel not also descendants of Noah?')
abraham=c('abraham','31a:6','כיוון דאיקדש אברהם איתקרו על שמיה','The answer says that after Abraham was consecrated, they were called by his name.',scope='Naming explanation for vow category')
e('abraham.answer',abraham,noahq,'answer','31a:6')
seed=c('seed','31a:7','שאיני נהנה לזרע אברהם אסור בישראל ומותר בנוכרים','A benefit vow against Abraham’s seed prohibits Israel and permits non-Jews.',composition='composite',scope='Mishnah’s scripturally delimited vow designation')
ishmaelq=q('ishmaelq','31a:8','והאיכא ישמעאל','What about Ishmael?')
isaac=c('isaac','31a:8','כי ביצחק יקרא לך זרע (בראשית כא, יב) כתיב','The answer cites the verse defining Abraham’s seed through Isaac.',scope='Quoted scriptural delimitation')
esauq=q('esauq','31a:8','והאיכא עשו','What about Esau?')
notall=c('notall','31a:8','ביצחק ולא כל יצחק','The reply reads through Isaac as not all of Isaac’s descendants.',scope='Derivation delimiting this vow label, not a biological assertion')
e('isaac.answer',isaac,ishmaelq,'answer','31a:8');e('notall.answer',notall,esauq,'answer','31a:8')
a.notes={
'30a:4':'Reread directional land/sea rules and unsettled placement of short-route qualification.',
'30a:5':'Reread named reporters and חד/חד without identification; retained cross-page first reading.',
'30b:1':'Reread first reading completion excluding short route and including habitual seafarers.',
'30b:2':'Reread second reading with eventual return to land rationale; no order-based assignment.',
'30b:3':'Reread blind inclusion and those-seen-by-sun explanation.',
'30b:4':'Reread wording rationale and fish/fetus exclusions.',
'30b:5':'Reread bald/gray inclusion and women/children exclusion as historical lexical classification.',
'30b:6':'Reread hair-possession versus conventional label rationale.',
'30b:7':'Reread question and source’s contrasting head-covering customs without universalizing.',
'30b:8':'Reread both lexical vow directions, compressed Meir clause and sages criterion.',
'30b:9':'Reread objection to implausible all-permitted interpretation.',
'30b:10':'Reread full חסורי מיחסרא reconstruction; retained corrected Meir reciprocity.',
'30b:11':'Reread Rav Pappa-to-Abaye past-birth scriptural counterexample.',
'30b:12':'Reread future Josiah counterexample and final ordinary-usage principle.',
'30b:13':'Reread sages exclusion question and fish/bird answer.',
'31a:1':'Reread all three group-designation outcomes separately.',
'31a:2':'Reread behavior-only objection and initially incomplete command-only explanation.',
'31a:3':'Reread pilgrimage counterexample to command-only definition.',
'31a:4':'Reread Abaye combined criterion and all groups across first two and final clauses.',
'31a:5':'Reread Noah-descendant vow rule as naming convention, not genealogy denial.',
'31a:6':'Reread genealogical objection and Abraham-name explanation.',
'31a:7':'Reread Abraham-seed vow outcome.',
'31a:8':'Reread Ishmael and Esau questions with separate scriptural delimiting answers.'}
if __name__=='__main__':a.save()
