"""Textual traditions and Moses/prophetic attributes: corrected proofs and agreeing Rav/Shmuel."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r039.';a.OUTPUT='continuation_039b.json'
c=a.c;q=b.q;e=a.edge
a.structure('text',['37b:'+str(i) for i in range(6,11)]+['38a:1','38a:2'],'Reading/writing traditions and Western verse division')
a.structure('moses',['38a:'+str(i) for i in range(3,17)],'Moses’ wealth, teaching gift, prophetic attributes and challenged proofs')
sinai=c('sinai','37b:6',None,'Rabbi Yitzhak describes scribal reading, scribal ornament, read-but-unwritten and written-but-unread traditions as law given to Moses at Sinai.',holder='רבי יצחק',composition='composite',scope='Source’s provenance assertion for four textual categories')
pronounce=c('pronounce','37b:7',None,'The examples of scribal reading are the pointed forms אָרֶץ, שָׁמַיִם and מִצְרַיִם.',composition='composite',scope='Exact vowels preserved; no additional phonetic reconstruction')
ornament=c('ornament','37b:8',None,'The scribal-ornament examples are אחר תעבורו, אחר תלכו, אחר תאסף, קדמו שרים אחר נוגנים and צדקתך כהררי אל with their printed references.',composition='composite',scope='Five explicitly supplied examples; no silent expansion of their textual mechanism')
for key,quote,text in [
('euphrates','פרת דבלכתו (שמואל ב ח, ג)','פרת in the cited בלכתו passage is listed as read but unwritten.'),
('man','איש דכאשר ישאל איש בדבר האלהים (שמואל ב טז, כג)','איש in the cited consultation passage is listed as read but unwritten.'),
('coming','באים דונבנתה (ירמיהו לא, לח)','באים in the cited ונבנתה passage is listed as read but unwritten.'),
('her','לה דפליטה (ירמיהו נ, כט)','לה in the cited פליטה passage is listed as read but unwritten.'),
('et','את דהגד הוגד (רות ב, יא)','את in the cited הגד הוגד passage is listed as read but unwritten.'),
('thresh','אלי דהגורן (רות ג, ה)','אלי in the threshing-floor passage is listed as read but unwritten.'),
('barley','אלי דהשעורים (רות ג, יז)','אלי in the barley passage is separately listed as read but unwritten.')]:c(key,'37b:9',quote,text,scope='Source’s explicit קריין ולא כתיבן inventory; original citation retained')
c('na','37b:10','נא דיסלח (מלכים ב ה, יח)','נא in the cited יסלח passage is listed as written but unread.',scope='First item of list continuing across page')
for key,quote,text in [
('this','זאת דהמצוה (דברים ו, א)','זאת in the cited commandment passage is listed as written but unread.'),
('tread','ידרוך דהדורך (ירמיהו נא, ג)','ידרוך in the cited הדורך passage is listed as written but unread.'),
('five','חמש דפאת נגב (יחזקאל מח, טז)','חמש in the south-side passage is listed as written but unread.'),
('if','אם דכי גואל (רות ג, ט)','אם in the cited כי גואל passage is listed as written but unread.')]:c(key,'38a:1',quote,text,scope='Source’s כתבן ולא קריין inventory; printed references preserved, not silently corrected')
west=c('west','38a:2',None,'Rav Aha bar Adda reports that in the West the cited הנה אנכי בא אליך בעב הענן passage is divided into three verses.',holder='רב אחא בר אדא',scope='Reported regional textual practice, not an instruction to alter the pinned edition')
wealth=c('wealth','38a:3',None,'Rabbi Hama son of Rabbi Hanina derives Moses’ wealth from leftover tablet stone, reading פסל לך as the remnants becoming his.',holder='רבי חמא ברבי חנינא',scope='Attributed homiletic account')
exclusive=c('exclusive','38a:4','אמר רבי יוסי ברבי חנינא לא ניתנה תורה אלא למשה ולזרעו שנאמר כתב לך (שמות לד, כז) פסל לך (שם, א) מה פסולתן שלך אף כתבן שלך','Rabbi Yosei son of Rabbi Hanina initially describes Torah as given to Moses and his descendants, by analogy between writing and tablet remnants.',holder='רבי יוסי ברבי חנינא',scope='Broad formulation subsequently narrowed to dialectical analysis')
generous=c('generous','38a:4',"משה נהג בה טובת עין ונתנה לישראל ועליו הכתוב אומר טוב עין הוא יבורך וגו' (משלי כב, ט)",'Moses is portrayed generously giving it to Israel, supported by the good-eye blessing verse.',holder='רבי יוסי ברבי חנינא',scope='Continuation of teaching, subject matter narrowed38a:6')
hasdaq=q('hasdaq','38a:5',"מתיב רב חסדא ואותי צוה ה' בעת ההיא ללמד אתכם (דברים ד, יד)",'Rav Hisda objects from God’s command to Moses to teach you.',voice='רב חסדא')
me=c('me','38a:5','ואותי צוה ואני לכם','The reply distinguishes the command to Moses from his teaching the people.',scope='First reply to broad Torah-gift objection')
secondq=q('secondq','38a:5',"ראה למדתי אתכם חוקים ומשפטים כאשר צוני ה' אלהי (דברים ד, ה)",'Does the statement that Moses taught as God commanded not show a command to teach the people?')
me2=c('me2','38a:5',('אותי צוה ואני לכם',1),'The reply again distinguishes the command to Moses and his teaching the people.',scope='Repeated reply retained as separate occurrence')
songq=q('songq','38a:6','ועתה כתבו לכם את השירה הזאת (דברים לא, יט)','What of the plural command to write this song?')
song=c('song','38a:6','השירה לחודה','The first reply restricts that command to the song alone.',mode='challenged',scope='Intermediate answer, followed by further witness-verse objection')
witnessq=q('witnessq','38a:6','למען תהיה לי השירה הזאת לעד בבני ישראל (שם)','What of the song being a witness among Israel?')
analysis=c('analysis','38a:6','אלא פילפולא בעלמא','The final answer narrows the special gift to dialectical analysis.',scope='Restriction on the earlier broad Torah-gift assertion')
e('me.answer',me,hasdaq,'answer','38a:5');e('me2.answer',me2,secondq,'answer','38a:5');e('song.answer',song,songq,'answer','38a:6');e('analysis.answer',analysis,witnessq,'answer','38a:6');e('analysis.qualification',analysis,exclusive,'qualification','38a:6');e('analysis.qualification2',analysis,generous,'qualification','38a:6')
attributes=c('attributes','38a:7','אמר רבי יוחנן אין הקב"ה משרה שכינתו אלא על גבור ועשיר וחכם ועניו וכולן ממשה','Rabbi Yohanan says divine presence rests on one strong, wealthy, wise and humble, deriving all four from Moses.',holder='רבי יוחנן',composition='composite',scope='Attributed theological criterion and exemplar')
tent=c('tent','38a:7',"גבור דכתיב ויפרוש את האהל על המשכן (שמות מ, יט) ואמר מר (בכורות מד א) משה רבינו פרסו וכתיב עשר אמות ארך הקרש וגו' (שמות כו, טז)",'The first strength proof cites Moses spreading the tent and boards ten cubits long.',mode='challenged',composition='composite',scope='Height-based inference challenged as not proving strength')
thin=q('thin','38a:7','אימא דאריך וקטין','Might he have been tall but thin?')
tablets=c('tablets','38a:8',None,'The replacement proof cites Moses breaking the tablets and a teaching giving their dimensions as six by six by three.',composition='composite',scope='Alternative strength evidence, dimensions as supplied without adding units')
e('tablets.answer',tablets,thin,'answer','38a:8');e('tablets.correction',tablets,tent,'correction','38a:8')
rich=c('rich','38a:9','עשיר פסל לך (שם, א) פסולתן שלך יהא','Wealth is supported by Moses receiving the tablet remnants.',scope='Second attribute proof')
gates=c('gates','38a:9','חכם רב ושמואל דאמרי תרוייהו חמשים שערי בינה נבראו בעולם וכולם ניתנו למשה חסר אחת שנאמר ותחסרהו מעט מאלהים (תהלים ח, ו)','Rav and Shmuel jointly teach that fifty gates of understanding were created and Moses received all but one, supporting wisdom.',composition='composite',scope='Explicit agreement דאמרי תרוייהו, not a Rav–Shmuel dispute')
a.add('gates.holders','attributions',dict(surface='רב ושמואל דאמרי תרוייהו',role='speaker',candidates=['רב','שמואל'],scope=gates,transmission_chain=[]),[a.ev('38a:9','רב ושמואל דאמרי תרוייהו')],[gates])
humble=c('humble','38a:9','עניו דכתיב והאיש משה עניו מאד (במדבר יב, ג)','Humility is supported by the verse describing Moses as exceedingly humble.',scope='Fourth attribute proof')
prophets=c('prophets','38a:10',"אמר ר' יוחנן כל הנביאים עשירים היו",'Rabbi Yohanan says all prophets were wealthy.',holder="ר' יוחנן",scope='Source’s general homiletic assertion, four exemplars cited next')
where=q('where','38a:10','מנלן','From where is the prophetic wealth assertion derived?')
exemplars=c('exemplars','38a:10','ממשה ומשמואל מעמוס ומיונה','The named exemplars are Moses, Samuel, Amos and Jonah.',composition='composite',scope='Samuel here is biblical prophet, not amora Shmuel')
moses=c('moses','38a:11','משה דכתיב לא חמור אחד מהם נשאתי (במדבר טז, טו) אי בלא אגרא לאפוקי מאן דשקל בלא אגרא אלא דאפילו באגרא','The first Moses argument interprets his not taking a donkey as not even renting one, since not stealing would be unremarkable.',mode='challenged',composition='composite',scope='Proposed wealth evidence, challenged as compatible with poverty')
poorq=q('poorq','38a:11','דילמא משום דעני הוה','Might his not renting be because he was poor?')
remnants=c('remnants','38a:11','אלא מן פסל לך פסולתן יהא שלך','The answer instead uses the tablet remnants.',scope='Replacement wealth proof')
e('remnants.answer',remnants,poorq,'answer','38a:11')
samuel=c('samuel','38a:12',"שמואל דכתיב הנני ענו בי נגד ה' ונגד משיחו את שור מי לקחתי וחמור מי לקחתי (שמואל א יב, ג) אי בחנם לאפוקי מאן דשקל בחנם אלא דאפילו בשכר",'The first Samuel argument similarly interprets not taking livestock as not even hiring it.',mode='challenged',composition='composite',scope='Biblical Samuel example, not amora statement')
poorq2=q('poorq2','38a:12','דלמא דעני הוה','Might Samuel likewise have been too poor to hire?')
home=c('home','38a:12','אלא מהכא ותשובתו הרמתה כי שם ביתו (שמואל א ז, יז) ואמר רבא (ברכות י ב) כל מקום שהלך ביתו עמו','The replacement cites Samuel’s home at Ramah and Rava’s interpretation that his household accompanied him wherever he went.',scope='Reported Rava interpretation supplies wealth proof')
e('home.answer',home,poorq2,'answer','38a:12')
greater=c('greater','38a:13',None,'Rava considers the testimony about Samuel stronger than Moses’: Samuel did not even hire willingly offered property, supported by לא עשקתנו ולא רצותנו.',holder='רבא',composition='composite',scope='Comparative exposition, distinct from proving wealth')
amos=c('amos','38a:14',None,'Amos’ wealth is derived from his cattle and sycamore work, with Rav Yosef’s translation describing possession of flocks and sycamores in the lowland.',composition='composite',scope='Translation explicitly attributed to Rav Yosef')
jonah=c('jonah','38a:15',"יונה דכתיב ויתן שכרה וירד בה (יונה א, ג) ואמר ר' יוחנן שנתן שכרה של ספינה כולה",'Rabbi Yohanan interprets Jonah as paying the whole ship’s fare.',holder="ר' יוחנן",scope='Jonah wealth proof')
fare=c('fare','38a:15',"אמר ר' רומנוס שכרה של ספינה הויא ד' אלפים דינרי דהבא",'Rabbi Romanus gives the ship’s fare as four thousand gold dinars.',holder="ר' רומנוס",scope='Attributed amount, not external historical verification')
gift=c('gift','38a:16',None,'Rabbi Yohanan says Moses initially learned and forgot Torah until it was given to him as a gift, citing ויתן אל משה.',holder="ר' יוחנן",scope='Separate pedagogic-theological narrative')
for key,claim,ref in [('remnants',remnants,'38a:11'),('home',home,'38a:12'),('amos',amos,'38a:14'),('jonah',jonah,'38a:15')]:e(key+'.where',claim,where,'answer',ref)
a.notes={
'37b:6':'Reread Yitzhak four-category Sinaitic provenance assertion.',
'37b:7':'Reread all three pointed reading examples preserving vowels.',
'37b:8':'Reread all five ornament examples and printed citations as composite inventory.',
'37b:9':'Reread all seven read-but-unwritten entries, separately retaining the two אלי occurrences.',
'37b:10':'Reread first written-but-unread entry continuing into next page.',
'38a:1':'Reread remaining four written-but-unread entries with source references unchanged.',
'38a:2':'Reread Aha bar Adda Western three-verse division report.',
'38a:3':'Reread Hama/Hanina tablet-remnant wealth derivation.',
'38a:4':'Reread Yosei/Hanina initially broad Torah-gift claim and generosity explanation, followed later narrowing.',
'38a:5':'Reread Hisda objection, first reply, second verse objection and repeated reply.',
'38a:6':'Reread song objection, intermediate restriction, witness objection and final pilpul-only qualification.',
'38a:7':'Reread Yohanan four attributes, tent/board strength proof and tall/thin challenge.',
'38a:8':'Reread replacement tablet-breaking proof and exact dimensions without invented units.',
'38a:9':'Reread wealth, agreed Rav/Shmuel49-of50 wisdom teaching and humility proof; no false dispute.',
'38a:10':'Reread all-prophets wealth assertion, derivation question and four exemplars.',
'38a:11':'Reread Moses donkey nonproof, poverty objection and replacement remnants proof.',
'38a:12':'Reread Samuel nonproof, poverty objection and Rava household-travel interpretation.',
'38a:13':'Reread Rava stronger Samuel testimony and voluntary-hiring distinction.',
'38a:14':'Reread Amos verse and attributed Yosef translation as wealth argument.',
'38a:15':'Reread Yohanan whole-ship fare and Romanus four-thousand gold-dinar amount.',
'38a:16':'Reread Yohanan learning/forgetting/gift narrative and verse.'}
if __name__=='__main__':a.save()
