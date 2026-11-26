"""Manual ethical and marital narratives; ancient causal assertions remain attributed reports."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r020.';a.OUTPUT='continuation_020b.json'
c=a.c;q=a.q;e=a.edge
a.structure('cautions',['20a:10','20a:11','20a:12'],'Cautions about habitual conduct, looking, and shame')
a.structure('marital',['20a:13','20a:14']+['20b:'+str(i) for i in range(1,13)],'Attributed marital teachings, rejected causal accounts, narratives, and qualifications')
a.structure('colophon',['20b:13'],'Printed ending of ואלו מותרין')
vows=c('vows','20a:10','תנא לעולם אל תהי רגיל בנדרים שסופך למעול בשבועות','The teaching warns that habitual vowing leads to violating oaths.',scope='Anonymous ethical warning, not a measured empirical prediction')
lay=c('lay','20a:10','ואל תהי רגיל אצל עם הארץ שסופך להאכילך טבלים','It warns against habitual association with an unlearned person because of untithed-food risk.',scope='Source’s stated social/ritual caution')
priest=c('priest','20a:10','אל תהי רגיל אצל כהן עם הארץ שסופך להאכילך תרומה','It separately warns about an unlearned priest providing terumah.',scope='Specific priest/terumah concern, not conflated with untithed produce')
talk=c('talk','20a:10','ואל תרבה שיחה עם האשה שסופך לבוא לידי ניאוף','The teaching warns against excessive conversation with a woman as leading to adultery.',scope='Historical source’s ethical warning, not annotator’s general claim about women')
look=c('look','20a:11','רבי אחא ברבי יאשיה אומר כל הצופה בנשים סופו בא לידי עבירה','Rabbi Aha ben Rabbi Yoshiyya warns that looking at women leads to transgression.',holder='רבי אחא ברבי יאשיה',scope='Attributed ethical statement')
heel=c('heel','20a:11','וכל המסתכל בעקבה של אשה הויין לו בנים שאינן מהוגנין','The report associates looking at a woman’s עקבה with unsuitable offspring.',holder='רבי אחא ברבי יאשיה',scope='Attributed ancient consequence claim; meaning of עקבה immediately glossed, no modern causal endorsement')
niddah=c('niddah','20a:11','אמר רב יוסף ובאשתו נדה','Rav Yosef specifies one’s wife while niddah.',holder='רב יוסף',conditions=['wife in niddah state'],scope='Qualification of preceding looking statement')
gloss=c('gloss','20a:11','אמר רבי שמעון בן לקיש עקבה דקתני במקום הטינופת שהוא מכוון כנגד העקב','Rabbi Shimon ben Lakish explains עקבה as the private region aligned opposite the heel.',holder='רבי שמעון בן לקיש',scope='Explicit euphemism gloss, not literal ankle-only reading')
e('niddah.qualification',niddah,heel,'qualification','20a:11');e('gloss.qualification',gloss,heel,'qualification','20a:11')
shame=c('shame','20a:12','תניא בעבור תהיה יראתו על פניכם זו בושה','The teaching interprets fear on one’s face as shame.',scope='Scriptural exposition')
fear=c('fear','20a:12','לבלתי תחטאו מלמד שהבושה מביאה לידי יראת חטא','It derives that shame leads to fear of sin.',scope='Source’s moral inference')
sign=c('sign','20a:12','מיכן אמרו סימן יפה באדם שהוא ביישן','It calls bashfulness a favorable sign in a person.',scope='Ethical evaluation')
others=c('others','20a:12','אחרים אומרים כל אדם המתבייש לא במהרה הוא חוטא','Others say a person who feels shame does not readily sin.',holder='אחרים',scope='Unresolved collective/textual authority label, no identification supplied')
ancestors=c('ancestors','20a:12','ומי שאין לו בושת פנים בידוע שלא עמדו אבותיו על הר סיני','The teaching rhetorically associates lack of shame with ancestors not standing at Sinai.',scope='Source’s moral-genealogical assertion, not an independently established genealogical test')
e('shame.support',shame,fear,'support','20a:12');e('fear.support',fear,sign,'support','20a:12')
reported=c('reported','20a:13','אמר רבי יוחנן בן דהבאי ארבעה דברים סחו לי מלאכי השרת','Rabbi Yohanan ben Dehavai reports four teachings from מלאכי השרת.',holder='רבי יוחנן בן דהבאי',scope='Reporting frame; Ameimar later interprets this designation as sages')
for key,quote,text in [
('lame','חיגרין מפני מה הויין מפני שהופכים את שולחנם','The report associates lameness in offspring with the marital act euphemistically described as turning the table.'),
('mute','אילמים מפני מה הויין מפני שמנשקים על אותו מקום','The report associates muteness in offspring with kissing the private region.'),
('deaf','חרשים מפני מה הויין מפני שמספרים  בשעת תשמיש','The report associates deafness in offspring with speaking during intercourse.'),
('blind','סומין מפני מה הויין מפני שמסתכלים באותו מקום','The report associates blindness in offspring with looking at the private region.')]:
    c(key,'20a:13',quote,text,holder='רבי יוחנן בן דהבאי',mode='challenged',scope='Ancient attributed causal assertion in question-and-answer form, not biomedical fact; sages reject the restrictive teaching at20b:4',composition='composite',uncertainty=['Not an independently supported medical claim. Preserve source attribution and subsequent rejection.'])
for key,quote,text in [('lameq','חיגרין מפני מה הויין','The report asks why lameness occurs.'),('muteq','אילמים מפני מה הויין','The report asks why muteness occurs.'),('deafq','חרשים מפני מה הויין','The report asks why deafness occurs.'),('blindq','סומין מפני מה הויין','The report asks why blindness occurs.')]:
    q(key,'20a:13',quote,text,voice='רבי יוחנן בן דהבאי')
beautyq=q('beautyq','20a:14','ורמינהו שאלו את אימא שלום מפני מה','Imma Shalom was asked why her children were exceptionally beautiful; the account is introduced as a challenge.',voice=None)
# The actual question crosses the page: preserve its ending as additional evidence.
for ident in ['nd.r020.beautyq.u','nd.r020.beautyq.a','nd.r020.beautyq.q']:
    next(x for x in a.records if x['id']==ident)['evidence'].append(a.ev('20b:1','בניך יפיפין ביותר'))
timing=c('timing','20b:1','אמרה להן אינו מספר עמי לא בתחלת הלילה ולא בסוף הלילה אלא בחצות הלילה','Imma Shalom reports that the intimacy described by מספר takes place at midnight, not the beginning or end of night.',holder='אימא שלום',conditions=['midnight'],scope='Her report about her partner, whose name is not supplied in this excerpt')
cover=c('cover','20b:1','וכשהוא מספר מגלה טפח ומכסה טפח ודומה עליו כמי שכפאו שד','She describes exposing and covering a handbreadth and an appearance like one compelled by a demon.',holder='אימא שלום',composition='composite',scope='Reported restrained behavior and simile, not a claim of actual supernatural compulsion')
why=q('why','20b:2','ואמרתי לו מה טעם','She reports asking him the reason.',voice='אימא שלום')
reason=c('reason','20b:2','ואמר לי כדי שלא אתן את עיני באשה אחרת ונמצאו בניו באין לידי ממזרות','His quoted reason is to avoid thinking of another woman and the stated consequence of offspring coming to ממזרות.',scope='Unnamed partner’s embedded explanation; no independent legal-status judgment of any child or identification of the partner')
dist=c('dist','20b:3',None,'The response distinguishes speech concerning intercourse from other matters.',scope='Resolution of apparent conflict concerning talking during intimacy')
e('reason.answer',reason,why,'answer','20b:2');e('dist.answer',dist,'nd.r020.deaf.c','answer','20b:3')
reject=c('reject','20b:4','אמר רבי יוחנן זו דברי יוחנן בן דהבאי אבל אמרו חכמים אין הלכה כיוחנן בן דהבאי','Rabbi Yohanan reports that the sages do not rule like Yohanan ben Dehavai.',holder='רבי יוחנן',scope='Explicit rejection; these two Yohanan names denote distinct textual speakers')
permission=c('permission','20b:4','אלא כל מה שאדם רוצה לעשות באשתו עושה','The sages’ quoted formulation permits marital conduct according to the man’s wishes.',scope='Historical source’s formulation in contrast to the preceding restrictions; not a present-day instruction or license for coercion')
food=c('food','20b:4','משל לבשר הבא מבית הטבח רצה לאוכלו במלח  אוכלו צלי אוכלו מבושל אוכלו שלוק אוכלו וכן דג הבא מבית הצייד','The explanation uses meat prepared with salt, roasted, cooked or boiled, and similarly fish, as an analogy.',composition='composite',scope='Source’s analogy and all listed preparations preserved, not an additional sexual-act taxonomy')
for key in ['lame','mute','deaf','blind']:e('reject.'+key,reject,'nd.r020.'+key+'.c','correction','20b:4')
e('food.analogy',food,permission,'analogy','20b:4')
ameimar=c('ameimar','20b:5','אמר אמימר מאן מלאכי השרת רבנן','Ameimar interprets מלאכי השרת here as the sages.',holder='אמימר',scope='Interpretation of report’s speaker designation, not literal angelic source certification')
ifangels=c('ifangels','20b:5','דאי תימא מלאכי השרת ממש אמאי אמר רבי יוחנן אין הלכה כיוחנן בן דהבאי הא אינהו בקיאי בצורת הולד טפי','He argues that if actual angels were meant, their greater knowledge of fetal formation would make the rejection puzzling.',holder='אמימר',mode='hypothetical',composition='composite',scope='Source-internal counterfactual argument, not scientific authority claim')
q('rejectq','20b:5','אמאי אמר רבי יוחנן אין הלכה כיוחנן בן דהבאי','Why would Rabbi Yohanan reject that view, under the literal-angel assumption?',conditions=['counterfactual literal angels'],voice='אמימר')
titleq=q('titleq','20b:5','ואמאי קרו להו מלאכי השרת','Why are the sages called מלאכי השרת here?')
marked=c('marked','20b:5','דמצייני כמלאכי השרת','The explanation is that they are distinguished like ministering angels.',scope='Source’s designation explanation, without adding unquoted clothing details')
e('ameimar.qualification',ameimar,reported,'qualification','20b:5');e('ifangels.support',ifangels,ameimar,'support','20b:5');e('marked.answer',marked,titleq,'answer','20b:5')
woman1=c('woman1','20b:6','ההיא דאתאי לקמיה דרבי אמרה לו רבי ערכתי לו שולחן והפכו','A woman came before Rabbi and reported “I set a table for him and he turned it.”',scope='First narrated consultation; source euphemism retained, no unexpressed consent or motive inferred')
rabbi=c('rabbi','20b:6','אמר לה בתי תורה התירתך ואני מה אעשה ליך','Rabbi responded that the Torah permitted her and asked what he could do for her.',holder='רבי',scope='Reported response to that woman; not present advice')
q('rabbiq','20b:6','ואני מה אעשה ליך','What can I do for you?',voice='רבי')
woman2=c('woman2','20b:6','ההיא דאתאי לקמיה דרב אמרה לו רבי ערכתי לו שולחן והפכו','A second woman presented the same table-turning report to Rav.',scope='Separate narrative occurrence; Rav not Rabbi')
rav=q('rav','20b:6','אמר מאי שנא מן ביניתא','Rav asked how this differs from fish.',voice='רב')
e('rabbi.answer',rabbi,woman1,'answer','20b:6');e('rav.answer',rav,woman2,'answer','20b:6')
cup=c('cup','20b:7','ולא תתורו אחרי לבבכם מכאן אמר רבי אל ישתה אדם בכוס זה ויתן עיניו בכוס אחר','Rabbi derives that a person should not drink from one cup while looking toward another.',holder='רבי',scope='Source’s marital metaphor under the cited verse')
two=c('two','20b:7','אמר רבינא לא נצרכא אלא דאפילו שתי נשיו','Ravina says this applies even to one’s two wives.',holder='רבינא',conditions=['both women are his wives'],scope='Qualification of the cup metaphor')
e('two.qualification',two,cup,'qualification','20b:7')
nine=c('nine','20b:8',None,'Rabbi Levi interprets the cited rebellious-offspring verse as בני תשע מדות, accompanied by the mnemonic בני אסנ״ת משגע״ח.',holder='רבי לוי',scope='Printed heading says nine; following list retained without count normalization',uncertainty=['The next segment prints ten labels, although this heading says nine; no reconciliation or omitted-label guess supplied.'])
labels=c('labels','20b:9',None,'The source lists בני אימה, בני אנוסה, בני שנואה, בני נידוי, בני תמורה, בני מריבה, בני שכרות, בני גרושת הלב, בני ערבוביא and בני חצופה.',composition='composite',scope='Ten printed labels retained as source categories; not applied to actual people',uncertainty=['Printed list has ten entries against preceding nine-category heading.'])
contraryq=q('contraryq','20b:10','איני','Is that so?')
desire=c('desire','20b:10','והאמר רבי שמואל בר נחמני אמר רבי יונתן כל אדם שאשתו תובעתו הויין לו בנים שאפילו בדורו של משה רבינו לא היו כמותם','Rabbi Yonatan, reported by Rabbi Shmuel bar Nahmani, praises the offspring of a wife who seeks intimacy, saying even Moses’ generation lacked their like.',holder='רבי יונתן',scope='Attributed praise challenging the חצופה category; not a biological prediction')
a.add('yonatan.chain','attributions',dict(surface='רבי שמואל בר נחמני אמר רבי יונתן',role='transmitter',candidates=['רבי שמואל בר נחמני'],scope=desire,transmission_chain=['רבי שמואל בר נחמני','רבי יונתן']),[a.ev('20b:10','רבי שמואל בר נחמני אמר רבי יונתן')],[desire])
moses=c('moses','20b:10','שנאמר הבו לכם אנשים חכמים ונבונים וכתיב ואקח את ראשי שבטיכם ולא כתיב נבונים','The argument compares a request for wise and understanding people with a later verse omitting נבונים.',scope='Explicit scriptural comparison, not an independent historical intelligence measurement',composition='composite')
issachar=c('issachar','20b:11',None,'It then cites Issachar as a strong donkey and Issachar’s descendants as understanding the times.',composition='composite',scope='Two supporting biblical citations')
appeal=c('appeal','20b:12',None,'The resolution distinguishes a woman who seeks intimacy through persuasion.',scope='Qualification reconciling praise with preceding category, not erasure of women’s voiced desires')
e('desire.objection',desire,labels,'objection','20b:10');e('moses.support',moses,desire,'support','20b:10');e('issachar.support',issachar,desire,'support','20b:11');e('appeal.qualification',appeal,desire,'qualification','20b:12')
a.speech('chapter',[a.ev('20b:13')],None,'printed chapter-ending formula','atomic')
a.notes={
'20a:10':'Reread four independent cautions and their stated consequences; not flattened into general moral summary.',
'20a:11':'Reread named looking warnings, Rav Yosef’s niddah qualification and Lakish’s explicit euphemism gloss.',
'20a:12':'Reread shame exposition, fear inference, favorable sign, Others’ teaching and rhetorical Sinai statement.',
'20a:13':'Reread report frame and all four question/answer causal pairings; attributed historical claims with later rejection, never biomedical facts.',
'20a:14':'Reread question to Imma Shalom together with20b:1 ending.',
'20b:1':'Reread her timing, exposure/covering and simile; no partner identity imported from memory.',
'20b:2':'Reread her reason question and partner’s embedded answer without assigning actual child status.',
'20b:3':'Reread subject-matter-of-speech distinction.',
'20b:4':'Reread Rabbi Yohanan’s explicit rejection of Yohanan ben Dehavai and full preparation analogy.',
'20b:5':'Reread Ameimar’s nonliteral authority explanation, conditional argument and designation rationale.',
'20b:6':'Reread both women’s consultations separately, Rabbi versus Rav responses, retaining source euphemism.',
'20b:7':'Reread cup metaphor and Ravina even-two-wives qualification.',
'20b:8':'Reread Rabbi Levi heading and mnemonic; count mismatch flagged.',
'20b:9':'Reread all ten printed labels, retaining mismatch rather than deleting one.',
'20b:10':'Reread challenge, Rabbi Shmuel bar Nahmani-to-Rabbi Yonatan transmission and Moses-verse comparison.',
'20b:11':'Reread both Issachar proof verses.',
'20b:12':'Reread persuasion qualification without inventing a further outcome.',
'20b:13':'Reread chapter-ending formula; no legal proposition, question or position fabricated.'}
if __name__=='__main__':a.save()
