"""Ownerless-field retraction, tannaitic constructions and witness counts; chapter close."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r046.';a.OUTPUT='continuation_046.json'
c=a.c;q=b.q;e=a.edge
a.structure('retract',['43b:6']+['44a:'+str(i) for i in range(1,6)]+['44b:'+str(i) for i in range(1,6)]+['45a:1','45a:2'],'Retraction from ownerlessness and public-witness conditions')
a.structure('end',['45a:3'],'End of no-difference benefit-vow chapter')
three=c('three','43b:6',None,'A baraita permits retracting an ownerless-field declaration for three days, but not thereafter.',composition='composite',conditions=['unqualified field abandonment'],scope='Rabbinic/Torah-level explanation debated below')
term=c('term','44a:1','אמר תהא שדה זו מופקרת ליום אחד לשבת אחת לחדש אחד לשנה אחת לשבוע אחת','The latter case declares the field ownerless for a day, week, month, year or seven-year period.',composition='composite',scope='Explicit five-duration inventory')
before=c('before','44a:1','עד שלא זכה בה בין הוא בין אחר יכול לחזור בו','Before either the original owner or another acquires, he may retract.',conditions=['fixed-term abandonment','no acquisition yet'])
after=c('after','44a:1','משזכה בה בין הוא בין אחר אין יכול לחזור בו','After acquisition by himself or another, he may not retract.',conditions=['fixed-term abandonment','acquisition has occurred'])
mixed=c('mixed','44a:1',"רישא רבנן סיפא ר' יוסי",'The initial interpretation assigns the first clause to the sages and the latter to Rabbi Yosei.',mode='challenged',composition='composite',scope='Mixed-authorship reading challenged by two uniform alternatives')
ulla=c('ulla','44a:2','אמר עולא סיפא נמי רבנן היא','Ulla assigns the latter clause too to the sages.',holder='עולא',scope='Uniform-sages construction')
why=q('why','44a:2',"אי הכי אמאי עד שלא זכה בה בין הוא בין אחר יכול לחזו' בו",'Why then does retraction remain possible until acquisition?')
rare=c('rare','44a:2','שאני שנה ושבוע דלא שכיחי','Year and seven-year declarations differ because they are uncommon.',scope='Reason for distinctive fixed-term treatment')
e('ulla.correction',ulla,mixed,'correction','44a:2');e('rare.answer',rare,why,'answer','44a:2')
lakish=c('lakish','44a:3',"ר\"ל אמר מדסיפא ר' יוסי רישא נמי ר' יוסי",'Reish Lakish assigns the first clause too to Rabbi Yosei.',holder='ר"ל',scope='Alternative uniform-Yosei construction')
forget=c('forget','44a:3','ורישא היינו טעמא דלא לישתכח תורת הפקר','The first clause’s nonretractability is explained as preserving the institution of ownerlessness.',scope='Rationale within Reish Lakish’s construction')
dayq=q('dayq','44a:4','אי הכי אפילו מיום הראשון נמי ליהוי הפקר','Why not make it irretractably ownerless from the first day?')
fraud=c('fraud','44a:4','אמר רבה מפני הרמאין דמפקירין והדרין בהון','Rabbah explains the three-day provision as addressing deceivers who abandon and then retract.',holder='רבה',scope='רבה distinguished from רבא; anti-evasion rationale')
e('lakish.distinction',lakish,ulla,'distinction','44a:3');e('fraud.answer',fraud,dayq,'answer','44a:4')
torah=c('torah','44a:5',None,'The discussion notes that under this construction it is not ownerless at Torah level.',scope='Premise of ensuing tithe-status objection within Reish Lakish/Yosei analysis, not universal conclusion')
titheq=q('titheq','44b:1',None,'Might this cause tithing from obligated produce for exempt produce, or the reverse?')
same=c('same','44b:2',None,'The answer is to instruct him to tithe from that produce itself.',scope='Avoids mixing conflicting obligation statuses')
e('same.answer',same,titheq,'answer','44b:2')
vine=c('vine','44b:3',None,'A counterexample makes one who abandons his vineyard and harvests it next morning liable for פרט, עוללות, forgotten produce and field-corner gifts, but exempt from tithes.',composition='composite',scope='Four poor-gift obligations distinguished from tithe exemption')
fit=c('fit','44b:4','בשלמא לעולא דרבנן קתני לה ודאורייתא קתני לה','The vineyard rule is said to fit Ulla’s sages-based account at Torah level.',scope='Concession before challenge to Reish Lakish')
lakishq=q('lakishq','44b:4','אלא לריש לקיש אמאי פטור מן המעשר','Why is it tithe-exempt under Reish Lakish’s account?')
sages=c('sages','44b:5',None,'Reish Lakish can answer that his earlier construction concerned Rabbi Yosei, while this vineyard teaching follows the sages.',scope='Different tannaitic attribution, not abandoning his previous reading')
e('sages.answer',sages,lakishq,'answer','44b:5')
twoThree=c('twoThree','45a:1','איבעית אימא הא דאפקריה באנפי תרין והא דאפקריה באפי תלתא','An alternative distinguishes declarations before two and before three people.',composition='composite',scope='Explicit alternative resolution of ownerlessness/tithe contrast')
yohanan=c('yohanan','45a:1',"דאמר ר' יוחנן משום רבי שמעון בן יהוצדק כל המפקיר בפני שלשה הוי הפקר בפני שנים לא הוי הפקר",'Rabbi Shimon ben Yehotzadak, through Rabbi Yohanan, makes a declaration before three effective and before two ineffective.',holder='רבי שמעון בן יהוצדק',composition='composite',conditions=['number present'],scope='Reported witness-count rule supporting alternative distinction')
a.add('yohanan.chain','attributions',dict(surface="אמר ר' יוחנן משום רבי שמעון בן יהוצדק",role='transmitter',candidates=["ר' יוחנן"],scope=yohanan,transmission_chain=["ר' יוחנן",'רבי שמעון בן יהוצדק']),[a.ev('45a:1',"אמר ר' יוחנן משום רבי שמעון בן יהוצדק")],[yohanan])
levi=c('levi','45a:2',"ור' יהושע בן לוי אמר דבר תורה אפילו באחד הוי הפקר",'Rabbi Yehoshua ben Levi says that Torah law allows effective abandonment even before one.',holder="ר' יהושע בן לוי",conditions=['Torah-law level'],scope='Distinguishes Torah validity from three-person enactment')
witnessq=q('witnessq','45a:2','ומה טעם אמרו בשלשה','Why did the sages specify three?')
witness=c('witness','45a:2','כדי שיהא אחד זוכה ושנים מעידין','So one can acquire and two can testify.',scope='Functional division of acquirer and witnesses')
e('twoThree.answer',twoThree,lakishq,'answer','45a:1');e('yohanan.support',yohanan,twoThree,'support','45a:1');e('levi.distinction',levi,yohanan,'distinction','45a:2');e('witness.answer',witness,witnessq,'answer','45a:2')
a.add('chapter.u','utterances',dict(textual_voice='anonymous textual marker',discourse_role='chapter conclusion',composition='atomic'),[a.ev('45a:3')])
a.add('chapter.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'chapter.u',transmission_chain=[]),[a.ev('45a:3')],[a.PREFIX+'chapter.u'])
a.notes={
'43b:6':'Reread unqualified field three-day retraction and later nonretraction rule.',
'44a:1':'Reread all five fixed terms, before/after acquisition by either person and proposed mixed attribution.',
'44a:2':'Reread Ulla all-sages construction, retraction objection and uncommon-term answer.',
'44a:3':'Reread Reish Lakish all-Yosei alternative and preserving-ownerlessness rationale.',
'44a:4':'Reread first-day objection and Rabbah anti-deceiver explanation, not Rava.',
'44a:5':'Reread Torah-level nonownerlessness premise within this construction.',
'44b:1':'Reread both directions of obligated/exempt tithe concern.',
'44b:2':'Reread same-produce tithing answer.',
'44b:3':'Reread next-morning vineyard case, all four poor-gift liabilities and tithe exemption.',
'44b:4':'Reread fit with Ulla and challenge to Reish Lakish.',
'44b:5':'Reread different-tanna response preserving prior Yosei construction.',
'45a:1':'Reread alternative two/three distinction and complete Yohanan/Shimon ben Yehotzadak chain.',
'45a:2':'Reread Yehoshua ben Levi Torah-one versus enacted-three distinction and acquirer/two-witness rationale.',
'45a:3':'Reread chapter ending and markup, retained textual utterance without invented legal claim.'}
if __name__=='__main__':a.save()
