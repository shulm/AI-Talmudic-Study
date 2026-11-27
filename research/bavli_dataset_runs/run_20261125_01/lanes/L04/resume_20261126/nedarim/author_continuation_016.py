"""Manual oath syntax and commandment restrictions, including alternative Rav/Shmuel reports."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r016.';a.OUTPUT='continuation_016b.json'
c=a.c;q=a.q;e=a.edge
a.structure('offering',['15b:13','16a:1','16a:2','16a:3'],'Oaths concerning intangible actions and nonprohibitory offering forms')
a.structure('oathword',['16a:'+str(i) for i in range(4,11)],'Positive and negative eating-oath language in context')
a.structure('command',['16a:11']+['16b:'+str(i) for i in range(1,8)]+['17a:1','17a:2'],'Vows and oaths concerning commandments; alternative transmission and two scriptural exemptions')
actions=c('actions','15b:13','שבועה שאיני ישן שאיני מדבר שאיני מהלך אסור','Oaths not to sleep, speak or walk prohibit those acts.',composition='composite',scope='Mishnah’s three intangible-action cases')
forms=c('forms','15b:13','קרבן לא אוכל לך הא קרבן שאוכל לך לא קרבן לא אוכל לך מותר:','The Mishnah permits the three printed formulas קרבן לא אוכל לך, הא קרבן שאוכל לך and לא קרבן לא אוכל לך.',composition='composite',scope='Exact list, followed by orthographic distinction in Gemara')
who=q('who','16a:1','מני מתניתין','Whose view is the Mishnah?')
meir=c('meir','16a:1','רבי מאיר היא דאי רבי יהודה לא שני ליה קרבן ולא שני ליה הקרבן','The answer attributes it to Rabbi Meir, contrasting Rabbi Yehuda’s treatment of קרבן and הקרבן.',composition='composite',scope='Anonymous attribution and explanatory contrast')
e('meir.answer',meir,who,'answer','16a:1')
contradiction=c('contradiction','16a:2','אימא סיפא לקרבן לא אוכל לך מותר והתנן לקרבן לא אוכל לך רבי מאיר אוסר','The objection compares the ending’s permission with a quoted Rabbi Meir prohibition for לקרבן לא אוכל לך.',composition='composite',scope='Repeated formula-contrast argument')
abba=c('abba','16a:2','ואמר רבי אבא נעשה כאומר לקרבן יהא לפיכך לא אוכל לך','Rabbi Abba’s cited explanation reads the prohibition as “let it be an offering, therefore I will not eat.”',holder='רבי אבא',scope='Repeated explanatory report')
split=c('split','16a:3',None,'The reply distinguishes לקרבן from לא לקרבן, the latter denying offering status.',scope='Printed negative-prefix distinction')
e('contradiction.objection',contradiction,meir,'objection','16a:2');e('abba.support',abba,contradiction,'support','16a:2');e('split.answer',split,contradiction,'answer','16a:3')
oathforms=c('oathforms','16a:4','שבועה לא אוכל לך הא שבועה שאוכל לך לא שבועה לא אוכל לך אסור:','The Mishnah prohibits its three listed oath formulas: שבועה לא אוכל לך, הא שבועה שאוכל לך and לא שבועה לא אוכל לך.',composition='composite',scope='Exact printed list; meaning of שאוכל examined next')
negative=c('negative','16a:5','מכלל דהא שבועה שאוכל לך דלא אכילנא משמע','The initial inference takes the Mishnah’s שאוכל לך as a negative eating commitment.',scope='Inference generating lexical conflict, qualified by explanations')
four=c('four','16a:5','ורמינהו שבועות שתים שהן ארבע שאוכל ושלא אוכל שאכלתי ושלא אכלתי','The conflicting teaching gives four oath types: future eat/not eat and past ate/did not eat.',composition='composite',scope='Quoted four-way distinction')
positive=c('positive','16a:5','מדקאמר שלא אוכל שאכלתי ושלא אכלתי מכלל דשאוכל לך דאכילנא משמע','From that contrast the discussion infers that שאוכל לך means that he will eat.',scope='Opposing lexical inference')
e('four.support',four,positive,'support','16a:5');e('positive.objection',positive,negative,'objection','16a:5')
two=c('two','16a:6','אמר אביי שאוכל שתי לשונות משמע','Abaye says שאוכל can have two meanings.',holder='אביי',scope='Contextual explanation')
yes=c('yes','16a:6','היו מסרבין בו לאכול ואמר אכילנא אכילנא ותו שבועה שאוכל דאכילנא משמע','If urged to eat he repeatedly agrees and then swears שאוכל, it means he will eat.',holder='אביי',conditions=['urged to eat','prior repeated agreement'],scope='First contextual branch')
no=c('no','16a:6','אבל אמר לא אכילנא לא אכילנא ותו אמר שבועה שאוכל דלא אכילנא קאמר','If he repeatedly refuses and then swears שאוכל, it means he will not eat.',holder='אביי',conditions=['prior repeated refusal'],scope='Second contextual branch')
e('two.answer',two,positive,'answer','16a:6')
ashi=c('ashi','16a:7','רב אשי אמר שאוכל דשבועה שאי אוכל קאמר','Rav Ashi reads the Mishnah’s oath wording as שאי אוכל.',holder='רב אשי',scope='Alternative pronunciation/wording explanation, exact source form retained')
obvious=q('obvious','16a:7','אם כן פשיטא מאי למימרא','If so, what novelty remains?')
slip=c('slip','16a:7','מהו דתימא מיקם לישנא היא דאיתקיל ליה','One might have treated this as a slip of the tongue.',mode='rejected',scope='Excluded interpretation of the pronounced form')
exclude=c('exclude','16a:7','קא משמע לן','The teaching excludes that dismissal of the wording.',scope='Local novelty under Rav Ashi’s reading')
e('ashi.answer',ashi,positive,'answer','16a:7');e('slip.answer',slip,obvious,'answer','16a:7');e('exclude.correction',exclude,slip,'correction','16a:7')
abayewhy=c('abayewhy','16a:8',None,'Abaye does not use Rav Ashi’s explanation because the text does not teach שאי אוכל.',scope='Anonymous reason for maintaining distinct explanations')
e('abayewhy.objection',abayewhy,ashi,'objection','16a:8')
ashiwhy=c('ashiwhy','16a:9','ורב אשי נאדי מן טעם דאביי קסבר שלא אוכל נמי משמע שתי לשונות','Rav Ashi avoids Abaye’s explanation because שלא אוכל too could be contextually ambiguous.',scope='Anonymous account of Rav Ashi’s objection')
example=c('example','16a:9','היו מסרבין בו לאכול ואמר לא אכילנא לא אכילנא ואמר נמי שבועה בין שאוכל בין שלא אוכל הדין אכילנא משמע דאמר','The discussion gives repeated refusal followed by oath wording as an example in which a positive eating sense could be proposed even for negative wording.',composition='composite',scope='Compressed dialectical example preserved without inventing a fully settled parsing of its repeated phrases',uncertainty=['The exact referent of the printed בין שאוכל בין שלא אוכל wording needs further philological review; only the explicit ambiguity argument is asserted.'])
other=c('other','16a:10','ואיכא לתרוצה נמי לישנא שבועה שלא אוכל שבועה דלא אכילנא קאמר','The text also permits construing שבועה שלא אוכל as a negative eating oath.',scope='Opposite possible parsing in the ambiguity discussion')
fixed=c('fixed','16a:10','אלא תנא פסקה שאוכל דאכילנא משמע ושלא אוכל לא אוכל משמע:','The tanna instead states fixed senses: שאוכל means eating and שלא אוכל means not eating.',composition='composite',scope='Conclusion explaining Rav Ashi’s resistance to contextual ambiguity as the teaching’s explanation')
e('example.support',example,ashiwhy,'support','16a:9');e('fixed.support',fixed,ashiwhy,'support','16a:10')
vows=c('vows','16a:11','כיצד אמר קונם סוכה שאני עושה לולב שאני נוטל תפילין שאני מניח בנדרים אסור','The Mishnah makes the listed sukkah, lulav and tefillin קונם vows prohibitory.',composition='composite',conditions=['the stated commandment-object formulas'],scope='Three Mishnah cases, object/action form refined below')
oaths=c('oaths','16a:11','בשבועות מותר שאין נשבעין לעבור על המצות:','The corresponding oaths do not prohibit performance, because an oath cannot require violation of commandments.',scope='Mishnah’s vow/oath distinction, not an exemption from the commandments')
stringency=q('stringency','16b:1',None,'Does the wording “stringency” imply a vow exists, whereas the preceding clause said permitted?')
refer=c('refer','16b:2',None,'The phrase refers back to the earlier oath-not-to-sleep/speak/walk clause: this is the oath’s stringency over vows.',composition='composite',scope='Backward structural reference resolving apparent mismatch')
e('refer.answer',refer,stringency,'answer','16b:2')
versions=c('versions','16b:3','רב כהנא מתני אמר רב גידל אמר רב ורב טביומי מתני אמר רב גידל אמר שמואל','Rav Kahana transmits Rav Giddel in Rav’s name; Rav Tavyomi transmits Rav Giddel in Shmuel’s name.',composition='composite',scope='Explicit alternative versions of one teaching, not a Rav–Shmuel disagreement')
sourceq=q('sourceq','16b:3','מניין שאין נשבעין לעבור על המצות','What is the source that oaths cannot override commandments?')
derive=c('derive','16b:3','תלמוד לומר לא יחל דברו דברו לא יחל אבל מיחל הוא לחפצי שמים','The derivation limits לא יחל to his own word, allowing its breach for heavenly requirements.',scope='One derivation with alternative reported authority, Rav or Shmuel',uncertainty=['Two explicit transmission versions name Rav and Shmuel respectively; no choice or substantive dispute inferred.'])
for key,quote,chain in [('kahana','רב כהנא מתני אמר רב גידל אמר רב',['רב כהנא','רב גידל','רב']),('tavyomi','ורב טביומי מתני אמר רב גידל אמר שמואל',['רב טביומי','רב גידל','שמואל'])]:
    a.add(key,'attributions',dict(surface=quote,role='transmitter',candidates=chain[:-1],scope=derive,transmission_chain=chain),[a.ev('16b:3',quote)],[derive],uncertainty=['Alternative reported chain, not cumulative chain.'])
a.add('authority','attributions',dict(surface='רב כהנא מתני אמר רב גידל אמר רב ורב טביומי מתני אמר רב גידל אמר שמואל',role='quoted_authority',candidates=['רב','שמואל'],scope=derive,transmission_chain=[]),[a.ev('16b:3','רב כהנא מתני אמר רב גידל אמר רב ורב טביומי מתני אמר רב גידל אמר שמואל')],[derive],uncertainty=['Source supplies two versions; authority not resolved to one name.'])
e('derive.answer',derive,sourceq,'answer','16b:3')
same=q('same','16b:4',None,'Why distinguish vows and oaths when both appear with לה׳ and לא יחל דברו?')
abaye=c('abaye','16b:5',None,'Abaye distinguishes prohibiting the benefit of a sukkah to oneself from swearing not to benefit from a sukkah.',holder='אביי',mode='rejected',composition='composite',scope='Initial object/person formula explanation challenged by Rava')
pleasure=q('pleasure','16b:6','אמר רבא וכי מצות ליהנות ניתנו','Were commandments given for enjoyment?',voice='רבא')
rava=c('rava','16b:6','אלא אמר רבא הא דאמר ישיבת סוכה עלי והא דאמר שבועה שלא אשב בסוכה','Rava instead distinguishes prohibiting sukkah sitting to oneself from swearing not to sit in a sukkah.',holder='רבא',composition='composite',scope='Replacement formula explanation, preserving action rather than enjoyment')
e('abaye.answer',abaye,same,'answer','16b:5');e('pleasure.objection',pleasure,abaye,'objection','16b:6');e('rava.correction',rava,abaye,'correction','16b:6');e('rava.answer',rava,same,'answer','16b:6')
otherq=q('otherq','16b:7','ושאין נשבעין לעבור על המצות מהכא נפקא ליה מהתם נפקא ליה','Is the oath/commandment rule not derived from another verse?')
liableq=q('liableq','16b:7','דתניא יכול נשבע לבטל את המצוה ולא ביטל יכול יהא חייב','Might someone who swore to cancel a commandment but did not cancel it be liable?')
optional=c('optional','17a:1',None,'The teaching derives from להרע או להיטיב that the oath categories are optional acts, excluding cancellation of a commandment which is not optional.',composition='composite',scope='Quoted alternative derivation')
bothverses=c('bothverses','17a:2',None,'One verse exempts from the oath offering and the other from the oath prohibition.',composition='composite',scope='Different liabilities explain the need for both verses')
e('optional.answer',optional,liableq,'answer','17a:1');e('bothverses.answer',bothverses,otherq,'answer','17a:2')
a.notes={
'15b:13':'Reread three intangible oath cases and three permitted offering formulas.',
'16a:1':'Reread tanna question, Rabbi Meir answer and Rabbi Yehuda contrast.',
'16a:2':'Reread apparently conflicting negative formula and repeated Rabbi Abba explanation.',
'16a:3':'Reread explicit לקרבן/לא לקרבן distinction.',
'16a:4':'Reread all three oath formulas exactly.',
'16a:5':'Reread negative inference, four oath types and opposing positive inference.',
'16a:6':'Reread Abaye’s two contextual branches with prior agreement/refusal preserved.',
'16a:7':'Reread Rav Ashi wording proposal, novelty question and rejected tongue-slip reading.',
'16a:8':'Reread why Abaye rejects Rav Ashi’s wording reconstruction.',
'16a:9':'Reread Rav Ashi’s ambiguity objection and compressed example; precise parsing uncertainty explicitly retained.',
'16a:10':'Reread alternative negative parsing and tanna’s fixed positive/negative categorization.',
'16a:11':'Reread sukkah/lulav/tefillin vows, corresponding oath exception and commandment rationale.',
'16b:1':'Reread stringency/existence contradiction.',
'16b:2':'Reread backward reference resolving it, including all three action examples.',
'16b:3':'Reread both explicit transmission versions; Rav/Shmuel alternative authority not misclassified as dispute; derivation preserved.',
'16b:4':'Reread parallel biblical wording question.',
'16b:5':'Reread Abaye benefit wording as superseded explanation.',
'16b:6':'Reread Rava enjoyment objection and sitting-based replacement.',
'16b:7':'Reread redundant-source question and baraita liability question continuing17a:1.',
'17a:1':'Reread optional-act derivation and exclusion of commandment cancellation.',
'17a:2':'Reread distinct offering/prohibition exemptions; no single-verse redundancy asserted.'}
if __name__=='__main__':a.save()
