"""Manual divine-name vow release and narrative openings; self-release wording qualified."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r023.';a.OUTPUT='continuation_023.json'
c=a.c;q=a.q;e=a.edge
a.structure('name',['22b:4','22b:5','22b:6','22b:7'],'Divine-name release restriction, quoted echo and final local permission')
a.structure('openings',['22b:'+str(i) for i in range(8,12)]+['23a:'+str(i) for i in range(1,8)],'Narrative counterfactual openings and whether later events are unforeseen')
asi=c('asi','22b:4','אמר רבי אסי אין נזקקין לאלהי ישראל','Rabbi Asi refuses release assistance for vows in the name אלהי ישראל.',holder='רבי אסי',scope='Reported restrictive position, contrary local ruling appears22b:7')
mistake=c('mistake','22b:4','חוץ מקונם אשתי נהנית לי שגנבה את כיסי ושהכתה את בני ונודע שלא גנבה ושלא הכתו','The exception is a wife-benefit vow based on alleged theft of his purse or striking his son, when those allegations prove false.',conditions=['stated factual grounds later disproved'],composition='composite',scope='Explicit mistake exception; no allegation treated as true')
e('mistake.qualification',mistake,asi,'qualification','22b:4')
ask=q('ask','22b:5','אמר לה במאי נדרת','Rav Asi asks the woman by what she vowed.',voice='רב אסי')
answer=c('answer','22b:5',('באלהי ישראל',0),'She identifies אלהי ישראל.',scope='Woman’s reported answer, not Rav Asi’s oath')
substitute=c('substitute','22b:5','אמר לה אי נדרת במוהי שהיא כינוי בעלמא מזדקיקנא לך','Rav Asi says he would assist had she used במוהי, a substitute expression.',holder='רב אסי',mode='hypothetical',conditions=['counterfactual substitute wording'],scope='Printed רב אסי label retained distinct from preceding רבי אסי spelling')
refuse=c('refuse','22b:5','השתא דלא נדרת במוהי אלא באלהי ישראל לא מזדקיקנא לך','Given her actual אלהי ישראל wording, he refuses assistance.',holder='רב אסי',conditions=['actual divine-name expression'],scope='Narrative application of restrictive view')
e('answer.answer',answer,ask,'answer','22b:5')
visit=c('visit','22b:6','רב כהנא איקלע לבי רב יוסף אמר ליה לטעום מר מידי','Rav Kahana visits Rav Yosef, who invites him to taste something.',composition='composite',scope='Narrative setting and invitation')
decline=c('decline','22b:6','אמר ליה לא מרי כולא לא טעימנא ליה','Rav Kahana declines using לא מרי כולא לא טעימנא ליה.',holder='רב כהנא',scope='Reported oath-like refusal, exact expression retained')
echo=c('echo','22b:6','אמר ליה לא מרי כולא לא טעימת ליה','Rav Yosef repeats the expression in his response.',holder='רב יוסף',scope='Apparent oath formulation, explained as quotation below')
why=q('why','22b:6','הניחא לרב כהנא דאמר לא מרי כולא אלא לרב יוסף אמאי אמר לא מרי כולא','Why does Rav Yosef also say לא מרי כולא?')
quote=c('quote','22b:6','הכי הוא דקאמר ליה לא מרי כולא הוא דקאמרת הלכך לא טעימת ליה','The answer explains that Rav Yosef quotes Rav Kahana’s wording and states the resulting refusal to taste.',scope='Quoted echo rather than an independent oath by Rav Yosef')
e('quote.answer',quote,why,'answer','22b:6');e('quote.qualification',quote,echo,'qualification','22b:6')
regret=c('regret','22b:7','אמר רבא אמר רב נחמן הלכתא פותחין בחרטה','Rav Nahman, reported by Rava, rules that release may be opened through regret.',holder='רב נחמן',scope='Explicit local הלכתא, differing from earlier Rav Asi inference')
name=c('name','22b:7','ונזקקין לאלהי ישראל','The same ruling allows assistance for אלהי ישראל vows.',holder='רב נחמן',conditions=['divine-name vow'],scope='Second operative local clause')
for key,claim in [('chain',regret),('chain2',name)]:a.add(key,'attributions',dict(surface='אמר רבא אמר רב נחמן',role='transmitter',candidates=['רבא'],scope=claim,transmission_chain=['רבא','רב נחמן']),[a.ev('22b:7','אמר רבא אמר רב נחמן')],[claim])
e('name.correction',name,asi,'correction','22b:7')
praise=c('praise','22b:8','משתבח ליה רבא לרב נחמן ברב סחורה דאדם גדול הוא','Rava praises Rav Sehora as a great man to Rav Nahman.',scope='Narrated assessment by Rava, not independent biographical ranking')
request=c('request','22b:8','אמר לו כשיבא לידך הביאהו לידי','Rav Nahman requests that Rav Sehora be brought to him.',holder='רב נחמן',scope='Narrative request')
petition=c('petition','22b:8','הוה ליה נדרא למישרא אתא לקמיה דרב נחמן','Rav Sehora comes before Rav Nahman needing release of a vow.',scope='Narrative occasion')
counterq=q('counterq','22b:9','אמר ליה נדרת אדעתא דהכי','Rav Nahman asks whether he vowed with this consideration in mind.',voice='רב נחמן')
affirm=c('affirm','22b:9','אמר ליה אין אדעתא דהכי אין כמה זימנין','Rav Sehora repeatedly answers affirmatively to proposed circumstances.',composition='composite',scope='Repeated unsuccessful counterfactual openings, circumstances themselves not supplied')
angry=c('angry','22b:9','איקפד רב נחמן אמר ליה זיל לקילעך','Rav Nahman becomes angry and tells him זיל לקילעך.',composition='composite',scope='Narrated reaction and dismissal; no additional motive invented')
e('affirm.answer',affirm,counterq,'answer','22b:9')
find=c('find','22b:10','נפק רב סחורה ופתח פיתחא לנפשיה','Rav Sehora leaves and finds an opening for himself.',scope='Narrative describes his discovery of a rationale')
rabbi=c('rabbi','22b:10','רבי אומר איזו היא דרך ישרה שיבור לו האדם כל שהיא תפארת לעושיה ותפארת לו מן האדם','He cites Rabbi’s principle that the chosen path should bring credit to its doer and from other people.',holder='רבי',scope='Embedded ethical quotation with question-and-answer form',composition='composite')
regret2=c('regret2','22b:10','והשתא דאיקפד רב נחמן אדעתא דהכי לא נדרי','Rav Sehora says he would not have vowed had he anticipated Rav Nahman’s anger.',conditions=['counterfactual anticipated anger'],scope='His explicitly stated new opening')
self=c('self','22b:10','ושרא לנפשיה','The account concludes ושרא לנפשיה.',scope='Printed release wording retained; this excerpt does not name a distinct releasing authority',uncertainty=['Do not infer a general rule permitting a person to annul his own vow from this compressed narrative wording.'])
e('rabbi.support',rabbi,regret2,'support','22b:10')
shimon=c('shimon','22b:11','רבי שמעון ברבי הוה ליה נדרא למישרא אתא לקמייהו דרבנן','Rabbi Shimon son of Rabbi comes before the sages to release a vow.',scope='Separate narrative person, not Shimon bar Yohai')
againq=q('againq','22b:11','אמרי ליה נדרת אדעתא דהכי','The sages ask whether he vowed with a proposed circumstance in mind.')
yes=c('yes','22b:11','אמר אין אדעתא דהכי אין כמה זימנין','He repeatedly answers yes.',scope='Repeated unsuccessful proposed openings')
sun=c('sun','23a:1',None,'The sages suffer moving between sun and shade.',scope='Narrated inconvenience during consultation')
alternate=c('alternate','23a:2',None,'An alternate version repeats the affirmative answers and the sages’ discomfort between sun and shade.',composition='composite',scope='Explicit לישנא אחרינא retained as a separate textual occurrence')
batnit=q('batnit','23a:3','אמר ליה בטנית בריה דאבא שאול בן בטנית מי נדרת אדעתא דמצערי רבנן מטולא לשימשא ומשימשא לטולא','Batnit son of Abba Shaul ben Batnit asks whether he would have vowed knowing the sages’ discomfort.',voice='בטנית בריה דאבא שאול בן בטנית')
free=c('free','23a:3','אמר לא ושריוה','He says no, and they release him.',scope='Narrative plural releasing authority explicitly stated')
e('yes.answer',yes,againq,'answer','22b:11');e('free.answer',free,batnit,'answer','23a:3')
yishmael=c('yishmael','23a:4','רבי ישמעאל בר רבי יוסי הוה ליה נדרא למישרא אתא לקמייהו דרבנן','Rabbi Yishmael son of Rabbi Yosei comes to the sages for vow release.',scope='Third consultation narrative')
questions=c('questions','23a:4','אמרו ליה נדרת אדעתא דהכי אמר להו אין נדרתא אדעתא דהכי אמר להו אין כמה זימנין','He repeatedly answers yes to their proposed counterfactual circumstances.',composition='composite',scope='Reported repeated dialogue, circumstances not invented')
launderer=c('launderer','23a:4','כיוון דחזא ההוא קצרא דמצטערי רבנן מחייה באוכלא דקצרי','A launderer, seeing the sages’ distress, strikes him with a laundering implement.',scope='Narrated violent reaction; source states observed distress, not permission to strike')
wouldnot=c('wouldnot','23a:4','אמר אדעתא דמחי לי קצרא לא נדרי','He says he would not have vowed anticipating the launderer’s blow.',conditions=['counterfactual blow'],scope='Petitioner’s stated opening')
free2=c('free2','23a:4','ושריה לנפשיה','The account concludes ושריה לנפשיה.',scope='Compressed release wording, not a general legal authorization of self-annulment',uncertainty=['A distinct releasing authority is not supplied in this clause; do not resolve mechanism from the phrase alone.'])
novelq=q('novelq','23a:5','אמר ליה רב אחא מדיפתי לרבינא האי נולד הוא דלא מסיק אדעתיה דמחי ליה קצרא ותנינא אין פותחין לו בנולד','Rav Aha of Difti asks Ravina whether this is an unforeseen event, which cannot supply a release opening.',voice='רב אחא מדיפתי')
common=c('common','23a:5','אמר ליה האי לאו נולד הוא דשכיחי אפיקורי דמצערי רבנן','Ravina answers that it is not an unforeseen novelty because disrespectful people who distress sages are common.',holder='רבינא',scope='Source’s foreseeability rationale for this event')
e('novelq.objection',novelq,wouldnot,'objection','23a:5');e('common.answer',common,novelq,'answer','23a:5')
daughter=c('daughter','23a:6','דביתהו דאביי הוה לה ההיא ברתא הוא אמר לקריבאי היא אמרה לקריבה','Abaye’s wife had a daughter; he proposed his relative and she proposed hers.',composition='composite',scope='Marriage-arrangement disagreement; no assertion that Abaye was the daughter’s father')
condition=c('condition','23a:6','אמר לה תיתסרא הנאתי עלך אי עברת אדעתאי ומינסבת לה לקריבך','Abaye conditionally prohibited his benefit to his wife if she arranged the marriage with her relative against his wishes.',holder='אביי',conditions=['wife arranges daughter’s marriage with her relative against his wishes'],scope='Narrated conditional declaration, not a recommendation')
did=c('did','23a:6','אזלת ועברת על דעתיה ואינסבא לקריבה אתא לקמיה דרב יוסף','She did arrange that marriage, and he came before Rav Yosef.',composition='composite',scope='Narrative condition fulfillment and consultation')
anticipated=q('anticipated','23a:6','אמר ליה אילו הוה ידעת דעברת על דעתך ומנסבא לה לקריבה מי אדרתה','Rav Yosef asks whether he would have imposed the vow knowing she would act against his wishes.',voice='רב יוסף')
abayeNo=c('abayeNo','23a:6','אמר לא ושרייה רב יוסף','Abaye says no, and Rav Yosef releases him.',scope='Explicit named release authority')
e('abayeNo.answer',abayeNo,anticipated,'answer','23a:6')
allowedq=q('allowedq','23a:7','ומי שרי כי האי גוונא','Is this kind of release permissible?')
pilgrim=c('pilgrim','23a:7','אין והתניא מעשה באדם אחד שהדיר את אשתו מלעלות לרגל ועברה על דעתו ועלתה לרגל ובא לפני רבי יוסי','The answer cites a man who vowed to prevent his wife’s pilgrimage; she went despite his wishes, and he came to Rabbi Yosei.',composition='composite',scope='Supporting parallel narrative, not the same couple')
pilgrimq=q('pilgrimq','23a:7','אמר לו ואילו היית יודע שעוברת על דעתך ועולה לרגל כלום הידרתה','Rabbi Yosei asks whether he would have vowed knowing she would go anyway.',voice='רבי יוסי')
pilgrimNo=c('pilgrimNo','23a:7','אמר לו לא והתירו רבי יוסי','He says no, and Rabbi Yosei releases him.',scope='Explicit outcome of supporting narrative')
e('pilgrim.answer',pilgrim,allowedq,'answer','23a:7');e('pilgrimNo.answer',pilgrimNo,pilgrimq,'answer','23a:7');e('pilgrimNo.analogy',pilgrimNo,abayeNo,'analogy','23a:7')
a.notes={
'22b:4':'Reread divine-name restriction and both disproved factual grounds in its exception.',
'22b:5':'Reread woman’s oath-word answer and substitute/actual expression contrast; רבי/רב Asi spellings not silently harmonized.',
'22b:6':'Reread invitation, Kahana refusal, Yosef echo, question and quotation explanation.',
'22b:7':'Reread Rava-to-Rav Nahman transmission and both explicit final permissions.',
'22b:8':'Reread Rava praise, Nahman request and Sehora consultation.',
'22b:9':'Reread repeated affirmations and anger/dismissal without inventing unstated proposed circumstances.',
'22b:10':'Reread Rabbi quotation, self-found opening and compressed self-release phrase with mechanism uncertainty.',
'22b:11':'Reread Shimon son of Rabbi consultation and repeated yes answers.',
'23a:1':'Reread sages’ sun/shade distress as narrative event.',
'23a:2':'Reread explicit alternate version, retained rather than deduplicated.',
'23a:3':'Reread Batnit lineage, discomfort-based question and plural release outcome.',
'23a:4':'Reread Yishmael narrative, repeated questions, launderer’s blow, counterfactual and ambiguous compressed release wording.',
'23a:5':'Reread Rav Aha/Ravina novel-event objection and common-event answer.',
'23a:6':'Reread daughter/relative disagreement, conditional benefit vow, condition fulfillment and named Rav Yosef release.',
'23a:7':'Reread legality question and full parallel pilgrimage narrative with Rabbi Yosei response.'}
if __name__=='__main__':a.save()
