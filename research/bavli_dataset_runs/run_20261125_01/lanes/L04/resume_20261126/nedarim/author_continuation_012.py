"""Manual comparison-to-sacrifice discussion; proposed proofs remain challenged."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r012.';a.OUTPUT='continuation_012b.json'
c=a.c;q=a.q;e=a.edge
scope=['11b:7','11b:8','11b:9']+['12a:'+str(i) for i in range(1,9)]+['12b:'+str(i) for i in range(1,10)]+['13a:'+str(i) for i in range(1,8)]
a.structure('original',scope,'Whether an unspecified comparison follows sacrificial meat’s original or permitted state; successive inconclusive proofs')
main=q('main','11b:7','בעי רמי בר חמא הרי עלי כבשר זבחי שלמים לאחר זריקת דמים מהו','Rami bar Hama asks about comparison to peace-offering meat after the blood is sprinkled.',voice='רמי בר חמא')
explicit=c('explicit','11b:8','אי דקאמר בהדין לישנא בהיתרא קא מתפיס','If he explicitly uses that wording, he attaches to something permitted.',conditions=['expressly says after blood sprinkling'],scope='Case excluded from unresolved question')
case=c('case','11b:8','אלא כגון דמחית בשר זבחי שלמים ומחית דהיתרא גביה ואמר זה כזה','The actual case places peace-offering meat beside permitted meat and says זה כזה.',conditions=['sacrificial meat now after blood sprinkling','unspecified זה כזה'],scope='Question’s precise case')
which=q('which','11b:8','מאי בעיקרו קא מתפיס או בהיתרא קא מתפיס','Does the comparison attach to its original sacrificial state or its present permitted state?',conditions=['actual זה כזה case'])
proof=c('proof','11b:9','אמר רבא תא שמע נותר ופיגול','Rava offers the Mishnah’s נותר ופיגול as proof.',holder='רבא',mode='challenged',scope='Proposed proof, not a settled resolution')
after=c('after','12a:1',None,'The proposed proof treats leftover and invalidated meat as post-sprinkling cases.',mode='challenged',scope='Premise of Rava’s offered inference, narrowed by response')
e('proof.answer',proof,main,'answer','11b:9');e('after.support',after,proof,'support','12a:1')
olah=c('olah','12a:2','אמר ליה רב הונא בריה דרב נתן בנותר של עולה','Rav Huna son of Rav Natan restricts the cited case to leftover burnt-offering meat.',holder='רב הונא בריה דרב נתן',conditions=['leftover meat of עולה'],scope='Deflection of proposed proof, since burnt-offering meat remains prohibited')
why=q('why','12a:2','אמר ליה אם כן ליתני בבשר עולה','If so, why not teach ordinary burnt-offering meat?')
e('olah.objection',olah,proof,'objection','12a:2')
simple=c('simple','12a:3','לא מיבעיא קאמר לא מיבעיא בשר עולה דאסור דהא בקרבן קא מתפיס','Ordinary burnt-offering meat is plainly prohibitory because the comparison is to an offering.',conditions=['ordinary עולה meat'],scope='First part of graded-novelty answer')
novel=c('novel','12a:3','נותר ופיגול דעולה איצטריכא','Leftover and invalidated burnt-offering meat supply the needed novelty.',conditions=['נותר ופיגול of עולה'],composition='composite',scope='Novelty stated, rationale follows')
hypothesis=c('hypothesis','12a:4','סלקא דעתך אמינא כאיסור נותר כאיסור פיגול והוה ליה כמתפיס בדבר האסור ולא מיתסר','One might view the comparison as to the forbidden status of נותר or פיגול, which would not prohibit as a vow.',mode='rejected',composition='composite',scope='Excluded assumption distinguishes דבר האסור from sacrificial vow status')
exclude=c('exclude','12a:4','קא משמע לן','The teaching excludes that assumption and gives the comparison prohibitory effect.',conditions=['the burnt-offering cases in the response'],scope='Local outcome, not resolution of the original peace-offering question')
e('simple.answer',simple,why,'answer','12a:3');e('hypothesis.support',hypothesis,novel,'support','12a:4');e('exclude.correction',exclude,hypothesis,'correction','12a:4')
issar=q('issar','12a:5','מיתיבי איזהו איסר האמור בתורה','What is the איסר referred to in the Torah?')
days=c('days','12a:5','אמר הריני שלא אוכל בשר ושלא אשתה יין כיום שמת בו אביו כיום שמת בו רבו כיום שנהרג בו גדליה בן אחיקם כיום שראיתי ירושלים בחורבנה','The teaching gives refraining from meat and wine like the day of one’s father’s death, teacher’s death, Gedaliah’s death, or seeing Jerusalem in ruin.',composition='composite',scope='Explicit two-restraint/four-day formula list, no literal claim that all dates coincide')
shmuel=c('shmuel','12a:5','ואמר שמואל והוא שנדור באותו היום','Shmuel qualifies that the relevant day must have been subject to a vow.',holder='שמואל',conditions=['prior vowed day'],scope='Initial reported wording, refined at12a:7')
e('days.answer',days,issar,'answer','12a:5');e('shmuel.qualification',shmuel,days,'qualification','12a:5')
daycase=q('daycase','12a:6','היכי דמי לאו כגון דקאי בחד בשבא דמית ביה אבוה','Is the case not standing on a Sunday corresponding to the father’s day of death?')
intervening=c('intervening','12a:6','ואף על גב דאיכא טובא חד בשבא דהיתרא וקתני אסור','The proposed proof allows intervening permitted Sundays yet reads the comparison as prohibited.',mode='challenged',conditions=['intervening permitted matching weekdays'],scope='Proposed reading, not established fact of the baraita')
original=c('original','12a:6','שמע מינה בעיקר הוא מתפיס','The proposal infers that a comparison attaches to the original state.',mode='challenged',scope='Inference defeated by the continuing-vow qualification next')
e('intervening.support',intervening,original,'support','12a:6');e('original.answer',original,main,'answer','12a:6')
continuous=c('continuous','12a:7',None,'The corrected Shmuel report requires that he has remained under the vow from that day onward.',holder='שמואל',conditions=['continuous vowed status from the original day'],scope='Report qualification prevents the proposed intervening-permission proof')
e('continuous.correction',continuous,shmuel,'correction','12a:7');e('continuous.objection',continuous,original,'objection','12a:7')
teruma=c('teruma','12a:8','אמר רבינא תא שמע כחלת אהרן וכתרומתו מותר','Ravina cites the rule permitting comparison to Aaron’s challah or terumah.',holder='רבינא',composition='composite',scope='Citation introducing a proposed proof; not claiming Ravina originated the rule')
thanks=c('thanks','12a:8','הא כתרומת לחמי תודה אסור','He infers that comparison to the separated thanksgiving breads would prohibit.',mode='challenged',scope='Proposed contrast with ordinary terumah')
tpost=c('tpost','12b:1',None,'The proposed proof takes thanksgiving-bread terumah to be after blood sprinkling.',mode='challenged',scope='Premise reconsidered at12b:4–7')
e('teruma.support',teruma,thanks,'support','12a:8');e('tpost.support',tpost,thanks,'support','12b:1');e('thanks.answer',thanks,main,'answer','12a:8')
chamber=c('chamber','12b:2',None,'The reply instead makes the prohibited contrast the chamber contribution, תרומת הלשכה.',scope='Alternative inference from the cited ordinary-terumah rule')
e('chamber.correction',chamber,thanks,'correction','12b:2')
whyordinary=q('whyordinary','12b:3','אבל תרומת לחמי תודה מאי מותר ליתני לחמי תודה וכל שכן תרומתו','If thanksgiving-bread terumah is permitted, why not teach thanksgiving breads, with ordinary terumah all the more permitted?')
included=c('included','12b:3','הא קא משמע לן תרומת לחמי תודה תרומתו היא','The reply treats thanksgiving-bread terumah as included in the cited term תרומתו.',scope='Answer under the first deflection of Ravina proof')
e('included.answer',included,whyordinary,'answer','12b:3')
dough=c('dough','12b:4',None,'Alternatively thanksgiving-bread terumah can be separated at kneading, before the blood is sprinkled.',conditions=['separation during kneading'],scope='Second deflection; no present-permitted-state proof remains')
e('dough.objection',dough,tpost,'objection','12b:4')
four=c('four','12b:5','וכי הא דאמר רב טובי בר קיסנא אמר שמואל לחמי תודה שאפאן בארבע חלות יצא','Shmuel, reported by Rav Tovi bar Kisna, says four baked thanksgiving loaves suffice after the fact.',holder='שמואל',conditions=['thanksgiving breads baked as four loaves'],scope='Example supporting separation at kneading')
a.add('tovi','attributions',dict(surface='רב טובי בר קיסנא אמר שמואל',role='transmitter',candidates=['רב טובי בר קיסנא'],scope=four,transmission_chain=['רב טובי בר קיסנא','שמואל']),[a.ev('12b:5','רב טובי בר קיסנא אמר שמואל')],[four])
fortyq=q('fortyq','12b:5','והכתיב ארבעים','But is the requirement not forty?')
ideal=c('ideal','12b:5','למצווה','Forty is the preferred fulfillment of the commandment.',scope='Answer distinguishes ideal count from after-the-fact validity')
e('ideal.answer',ideal,fortyq,'answer','12b:5')
separateq=q('separateq','12b:6','והא בעי למשקל תרומה','But must he not separate terumah?')
one=c('one','12b:6','וכי תימא דשקיל חדא ריפתא על כולה','One proposed solution would take one loaf for all the kinds.',mode='rejected',scope='Rejected candidate for how four loaves suffice')
each=c('each','12b:6','והתנן אחד מכל קרבן שלא יטול מקרבן על חבירו','The cited rule requires one from each offering and forbids taking one offering’s contribution for another.',scope='Objection to taking a single loaf for all types',composition='composite')
piece=c('piece','12b:6','וכי תימא דשקיל פרוסה מכל חד וחד','Another proposed solution would take a piece from each loaf.',mode='rejected',scope='Second rejected candidate')
whole=c('whole','12b:6','והתנן אחד שלא יטול פרוסה','The cited rule reads אחד as excluding a piece.',scope='Objection requiring a whole unit')
e('each.objection',each,one,'objection','12b:6');e('whole.objection',whole,piece,'objection','12b:6')
separate=c('separate','12b:7',None,'The answer separates during kneading: one from leavened dough, one from the loaves, one from wafers and one from the boiled-dough kind.',composition='composite',scope='Explicit four-type separation procedure, preceding four main baked loaves')
e('separate.answer',separate,separateq,'answer','12b:7');e('separate.support',separate,dough,'support','12b:7')
parallel=q('parallel','12b:8','לימא כתנאי','Is the original-state question a tannaitic dispute?')
yaakov=c('yaakov','12b:8','הרי עלי כבכור רבי יעקב אוסר','Rabbi Yaakov prohibits הרי עלי כבכור.',holder='רבי יעקב',conditions=['comparison to firstborn offering'],scope='Quoted named view, rationale developed below')
yehuda=c('yehuda','12b:8','ורבי יהודה מתיר','Rabbi Yehuda permits that comparison.',holder='רבי יהודה',conditions=['same כבכור formula'],scope='Quoted named contrasting view')
before=q('before','12b:9','היכי דמי אי נימא לפני זריקת דמים מאי טעמא דמאן דשרי','If this is before blood sprinkling, why would anyone permit it?')
afterq=q('afterq','12b:9','ואי לאחר זריקת דמים מאי טעמא דמאן דאסר','If explicitly after sprinkling, why would anyone prohibit it?')
proposed=c('proposed','12b:9','אלא לאו','The proposed reading places firstborn meat next to the other meat and interprets זה כזה, making the original-state question tannaitically disputed.',extra=[('13a:1',None)],mode='rejected',composition='composite',scope='Cross-page proposed mapping rejected by next answer')
e('proposed.answer',proposed,parallel,'answer','13a:1')
bothbefore=c('bothbefore','13a:2','לא דכולי עלמא לפני זריקת דמים','The reply places both tannaitic positions before sprinkling.',scope='Alternative explanation avoids resolving original-state question')
whypermit=q('whypermit','13a:2','ומאי טעמא דמאן דשרי','What is the permissive tanna’s reason?')
neder=c('neder','13a:2','אמר קרא כי ידור עד שידור בדבר הנדור לאפוקי בכור דדבר האסור הוא','The permissive rationale requires comparison to something made sacred by a vow and excludes firstborn sanctity as דבר האסור.',scope='Anonymous reconstruction of permissive tanna’s argument')
e('bothbefore.correction',bothbefore,proposed,'correction','13a:2');e('neder.answer',neder,whypermit,'answer','13a:2');e('neder.support',neder,yehuda,'support','13a:2')
include=c('include','13a:3',None,'The prohibiting tanna reads לה׳ as including דבר האסור.',scope='Anonymous reconstruction of restrictive rationale')
e('include.support',include,yaakov,'support','13a:3')
whatq=q('whatq','13a:4',"ומאן שרי לה' מאי עביד ליה",'How does the permissive tanna use לה׳?')
sin=c('sin','13a:4','מיבעי ליה למתפיס בחטאת ואשם','He uses it for comparison to sin and guilt offerings.',composition='composite',scope='Alternative use of the same scriptural term')
e('sin.answer',sin,whatq,'answer','13a:4')
selectq=q('selectq','13a:5','ומה ראית לרבות חטאת ואשם ולהוציא את הבכור','Why include sin and guilt offerings but exclude the firstborn?')
choice=c('choice','13a:5','מרבה אני חטאת ואשם שהוא מתפיס בנדר ומוציא אני את הבכור שהוא קדוש ממעי אמו','The answer distinguishes sin and guilt offerings, designated through a vow, from firstborn sanctity present from the womb.',composition='composite',scope='Explicit comparison, not an external assertion that all offering obligations are voluntary')
e('choice.answer',choice,selectq,'answer','13a:5')
firstborn=c('firstborn','13a:6','ומאן דאסר בכור נמי מתפיסו בנדר הוא','The restrictive response says the firstborn too has vow-like designation.',scope='Argument of prohibiting side, challenged next')
rabbi=c('rabbi','13a:6','דתניא משום רבי אמרו מניין לנולד בכור בתוך ביתו שמצווה להקדישו שנאמר הזכר תקדיש','A teaching in Rabbi’s name requires consecrating a firstborn born in one’s house, citing הזכר תקדיש.',holder='רבי',conditions=['firstborn born in one’s house'],scope='Quoted authority; report is משום רבי, no named transmitter invented')
e('rabbi.support',rabbi,firstborn,'support','13a:6');e('firstborn.objection',firstborn,choice,'objection','13a:6')
automatic=q('automatic','13a:7',None,'The permissive side asks: would the firstborn not be sacred even if he did not consecrate it?')
e('automatic.objection',automatic,firstborn,'objection','13a:7')
a.notes={
'11b:7':'Reread Rami bar Hama question in original wording; precise case refined next.',
'11b:8':'Reread excluded explicit-after case, juxtaposed-meat case and both interpretation branches.',
'11b:9':'Reread Rava proof proposal with12a:1 premise; no final resolution assumed.',
'12a:1':'Reread post-sprinkling premise in proof context, then response.',
'12a:2':'Reread Rav Huna son of Rav Natan restriction and anonymous why-not-meat question.',
'12a:3':'Reread obvious ordinary burnt-offering case and paired novelty.',
'12a:4':'Reread excluded דבר האסור interpretation and local teaching, not original-question resolution.',
'12a:5':'Reread two abstentions and all four commemorative days plus Shmuel’s initial qualification.',
'12a:6':'Reread proposed Sunday case, intervening permissions and challenged original-state inference.',
'12a:7':'Reread corrected continuous-vow report, undermining prior proof.',
'12a:8':'Reread Ravina’s ordinary-terumah citation and challenged thanksgiving contrast.',
'12b:1':'Reread post-sprinkling premise and both subsequent deflections.',
'12b:2':'Reread chamber-contribution alternative.',
'12b:3':'Reread redundancy question and inclusion of thanksgiving-bread terumah in generic term.',
'12b:4':'Reread alternative kneading-stage separation, before sprinkling.',
'12b:5':'Reread Rav Tovi/Shmuel chain, four-loaf validity, forty challenge and ideal-count distinction.',
'12b:6':'Reread both rejected separation solutions and independent whole/from-each restrictions.',
'12b:7':'Reread all four dough types in successful separation explanation.',
'12b:8':'Reread comparison question and Rabbi Yaakov/Rabbi Yehuda positions without assigning original-state views.',
'12b:9':'Reread before/after questions and cross-page attempted mapping.',
'13a:1':'Reread proposed זה כזה tannaitic alignment as rejected next.',
'13a:2':'Reread before-sprinkling reset, permissive rationale and דבר הנדור distinction.',
'13a:3':'Reread restrictive use of לה׳.',
'13a:4':'Reread term-allocation question and sin/guilt-offering answer.',
'13a:5':'Reread selective-inclusion question and vow-designation/womb-sanctity distinction.',
'13a:6':'Reread restrictive firstborn-designation argument and teaching משום רבי.',
'13a:7':'Reread automatic-sanctity objection; no final ruling fabricated for original question.'}
for ident in [main,which]:
    next(x for x in a.records if x['id']==ident)['uncertainty']=['The inspected continuation through13a:7 deflects the proposed proofs; no final answer to the original-state/present-state question is asserted.']
if __name__=='__main__':a.save()
