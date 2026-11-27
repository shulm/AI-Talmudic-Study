"""Reciprocal dealings and indirect assistance; contested ownerless-property mechanism."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r045.';a.OUTPUT='continuation_045b.json'
c=a.c;q=b.q;e=a.edge
a.structure('dealing',['42b:8','43a:1','43a:2'],'Borrowing, lending and trading restrictions in both directions')
a.structure('assistance',['43a:'+str(i) for i in range(3,9)]+['43b:'+str(i) for i in range(1,6)],'Intent in plowing vow, indirect provision and Rabbi Yosei’s ownerless-property restriction')
borrow=c('borrow','42b:8','המודר הנאה מחבירו לא ישאילנו ולא ישאל ממנו','The Mishnah prohibits lending an item to the restricted person and borrowing one from him.',composition='composite',scope='Two directions, explanation not assumed reciprocal until Gemara')
money=c('money','42b:8','לא ילונו ולא ילוה ממנו','It prohibits lending money to him or borrowing money from him.',composition='composite',scope='Separate monetary pair')
trade=c('trade','42b:8','ולא ימכור לו ולא יקח ממנו','It prohibits selling to him and buying from him.',composition='composite',scope='Separate trading pair')
which=q('which','43a:1',None,'How do all the listed directions confer the prohibited benefit, given that some benefit the other party?',conditions=['exact printed two-sided argument retained'])
mutual=c('mutual','43a:2','א"ר יוסי בר\' חנינא כגון שנדרו הנאה זה מזה','Rabbi Yosei son of Hanina construes reciprocal benefit vows.',holder="רבי יוסי בר' חנינא",conditions=['both parties prohibit benefit from each other'])
decree=c('decree','43a:2','אביי אמר גזירה לשאול משום להשאיל וכן בכולהו גזירה','Abaye explains decrees against one direction because of the opposite direction, extending this to all listed pairs.',holder='אביי',scope='Alternative explanation, not necessarily reciprocal vows')
e('mutual.answer',mutual,which,'answer','43a:2');e('decree.answer',decree,which,'answer','43a:2')
cow=c('cow','43a:3','אמר לו השאילני פרתך אמר לו אינה פנויה אמר קונם שדי שאני חורש בה לעולם','After a request for a cow is refused because it is unavailable, the speaker declares his field konam if he plows with it.',composition='composite',scope='Narrative trigger for intended scope of plowing declaration')
usual=c('usual','43a:3','אם היה דרכו לחרוש הוא אסור וכל אדם מותרים','If he customarily plows himself, he is prohibited while others are permitted.',composition='composite',conditions=['speaker ordinarily plows personally'],scope='Scope inferred from personal practice')
notusual=c('notusual','43a:3','ואם אין דרכו לחרוש הוא וכל אדם אסורין','If he does not ordinarily plow personally, he and others are prohibited.',composition='composite',conditions=['speaker does not ordinarily plow personally'])
shop=c('shop','43a:4',None,'When the restricted person lacks food, one may tell a shopkeeper of the predicament; the shopkeeper supplies him and subsequently collects from the speaker.',composition='composite',scope='Exact indirect-notice procedure, not express appointment as delivery agent')
workers=c('workers','43a:5',None,'For building a house, making a fence or harvesting a field, one may similarly notify workers, who work for the restricted person and then collect wages from the speaker.',composition='composite',scope='Three specified work needs and indirect remuneration')
gift=c('gift','43a:6','היו מהלכין בדרך ואין לו מה יאכל נותן לאחד לשום מתנה והלה מותר בה','On the road when the restricted person lacks food, one may give it as a gift to a third person, allowing the restricted person to benefit.',conditions=['third person present'],scope='Gift route distinct from ownerless route')
abandon=c('abandon','43a:6','אם אין עמהם אחר מניח על הסלע או על הגדר ואומר הרי הן מופקרים לכל מי שיחפוץ והלה נוטל ואוכל','Without a third person, one places the food on a rock or fence, declares it ownerless for anyone, and the other takes and eats.',composition='composite',conditions=['no third person','publicly unrestricted ownerless declaration'],scope='Anonymous Mishnah allowance')
yosei=c('yosei','43a:6',"ור' יוסי אוסר",'Rabbi Yosei prohibits the ownerless-food route.',holder="ר' יוסי",scope='Reason disputed by Yohanan and Rava')
e('yosei.objection',yosei,abandon,'objection','43a:6')
why=q('why','43a:7',"אמר ר' יוחנן מ\"ט דר' יוסי",'What is Rabbi Yosei’s reason, as explained by Rabbi Yohanan?',voice="ר' יוחנן")
ownership=c('ownership','43a:7','קסבר הפקר כמתנה מה מתנה עד דאתיא מרשות נותן לרשות מקבל אף הפקר עד דאתי לרשות זוכה','Rabbi Yohanan explains that ownerless property resembles a gift: it leaves the giver only when acquired by a recipient.',holder="ר' יוחנן",scope='Explanation of Yosei, challenged below; not a universally accepted definition of ownerlessness')
e('ownership.answer',ownership,why,'answer','43a:7')
before=c('before','43a:8','א"ר יוסי אימתי בזמן שנדרו קודם להפקירו','Rabbi Abba cites Rabbi Yosei limiting prohibition to a vow preceding the ownerless declaration.',holder='רבי יוסי',conditions=['vow before abandonment'],scope='Quoted timing qualification')
after=c('after','43b:1','אבל אם היה הפקירו קודם לנדרו הרי זה מותר','If abandonment preceded the vow, the citation permits benefit.',conditions=['abandonment before vow'],scope='Cross-page second branch of quoted qualification')
timingq=q('timingq','43b:1','ואי אמרת עד דאתי לרשות זוכה מה לי נדרו קודם להפקירו מה לי הפקירו קודם לנדרו','If ownership persists until acquisition, why should the order of vow and abandonment matter?')
intent=c('intent','43b:2',None,'The same questioner replies that a person making a vow does not intend property he has already declared ownerless.',scope='Intent-based answer preserves earlier ownership theory for this challenge')
e('intent.answer',intent,timingq,'answer','43b:2')
first=c('first','43b:3','מתיב רבא מקצתן לראשון וכולן לשני ראשון קנה','Rava objects from a teaching that assigning part to the first and all to the second results in the first acquiring.',scope='Compressed cited transaction; no unstated asset type or legal setting invented')
second=c('second','43b:4',None,'The second does not acquire.',scope='Cross-page completion of Rava’s quoted counterexample')
horon=c('horon','43b:5',None,'Rava instead explains Rabbi Yosei’s restriction as a decree because of the Beit Horon gift case.',holder='רבא',scope='Alternative rationale replaces ownership analogy in Rava’s explanation; full Beit Horon narrative not supplied here')
e('first.objection',first,ownership,'objection','43b:3');e('second.continuation',second,first,'distinction','43b:4');e('horon.answer',horon,why,'answer','43b:5');e('horon.correction',horon,ownership,'correction','43b:5')
a.notes={
'42b:8':'Reread all three reciprocal item-loan, money-loan and sale/purchase pairs.',
'43a:1':'Reread printed benefit-direction objections without silently normalizing wording.',
'43a:2':'Reread Yosei/Hanina reciprocal-vow and Abaye decree explanations as alternatives.',
'43a:3':'Reread cow refusal, field-vow formulation and both habitual-plowing scope branches.',
'43a:4':'Reread shopkeeper notification, provision and later reimbursement steps.',
'43a:5':'Reread three work needs and worker notification/work/payment sequence.',
'43a:6':'Reread third-party gift route, unrestricted abandonment route and Yosei objection.',
'43a:7':'Reread Yohanan question and ownerlessness-as-gift explanation, followed both challenges.',
'43a:8':'Reread Abba citation and vow-before-abandonment qualification across page.',
'43b:1':'Reread reverse-order permission and challenge to ownership-persistence theory.',
'43b:2':'Reread same-questioner intent answer; did not treat first challenge as definitive refutation.',
'43b:3':'Reread Rava compressed partial/all assignment counterexample, first acquires.',
'43b:4':'Reread second-does-not-acquire continuation without inventing omitted transaction setting.',
'43b:5':'Reread Rava Beit Horon decree alternative and maintained distinct rationale history.'}
if __name__=='__main__':a.save()
