"""Manual reading of refined speech and its narrative examples, 3a:10–3b:9."""
from author_opening_001 import *
records.clear()
core3=['3a:'+str(i) for i in range(10,15)]+['3b:'+str(i) for i in range(1,10)]
st=add('b3.language','structure',dict(title='Refined language, brevity and illustrative student/priest narratives',primary=True,boundary='open_right',legacy_ids=[]),[ev(x) for x in core3],origin='editorial_inference',uncertainty=['Further indirect-reporting narratives continue beyond this batch.'])
why=question('b3.why.q','3a:10','ותנא דידן מאי טעמא לא קתני לילי','Why does our tanna not use לילי?')
refined=claim('b3.refined','3a:10','לישנא מעליא הוא דנקט','The tanna chooses an elevated expression.',scope='Explanation of the opening Mishnah wording')
edge('b3.refined.answer',refined,why,'answer','3a:10','לישנא מעליא הוא דנקט')
jl=claim('b3.jl','3a:10',"וכדר' יהושע בן לוי דאמר ר' יהושע בן לוי לעולם אל יוציא אדם דבר מגונה מפיו",'Rabbi Yehoshua ben Levi teaches that one should never utter a degrading expression.',holder='רבי יהושע בן לוי',scope='Speech norm; qualified by subsequent brevity discussion')
eight=claim('b3.eight','3a:10','שהרי עקם הכתוב שמונה אותיות ולא הוציא דבר מגונה מפיו שנאמר (בראשית ז, ח) מן הבהמה הטהורה ומן הבהמה אשר איננה טהורה','The teaching cites Scripture’s eight extra letters in saying an animal is not pure rather than using the degrading term.',holder='רבי יהושע בן לוי',scope='Stated letter-count argument from Genesis 7:8; counts preserved as textual claims')
edge('b3.eight.support',eight,jl,'support','3a:10');edge('b3.jl.support',jl,refined,'support','3a:10')
pap=claim('b3.pappa','3a:11','רב פפא אמר תשע שנאמר (דברים כג, יא) כי יהיה בך איש אשר לא יהיה טהור מקרה לילה','Rav Pappa gives nine extra letters using Deuteronomy 23:11.',holder='רב פפא',scope='Alternative textual count/example; not independently recomputed')
rv=claim('b3.ravina','3a:11','רבינא אמר עשר וי"ו דטהור','Ravina gives ten, including the vav of טהור.',holder='רבינא',scope='Letter-count variant in the preceding example')
acha=claim('b3.acha','3a:11','רב אחא בר יעקב אמר שש עשרה שנאמר (שמואל א כ, כו) כי אמר מקרה הוא בלתי טהור הוא כי לא טהור','Rav Aha bar Yaakov gives sixteen, citing I Samuel 20:26.',holder='רב אחא בר יעקב',scope='Alternative scriptural circumlocution')
edge('b3.ravina.qualification',rv,pap,'qualification','3a:11','רבינא אמר עשר וי"ו דטהור')
school=claim('b3.ishmael','3a:12','תניא דבי רבי ישמעאל לעולם יספר אדם בלשון נקיה','The school of Rabbi Yishmael teaches that one should always speak with clean language.',holder='דבי רבי ישמעאל',scope='School teaching; not automatically the named master’s personal utterance')
ride=claim('b3.ride','3a:12','שהרי בזב קראו מרכב ובאשה קראו מושב','Its example contrasts מרכב for a zav with מושב for a woman.',scope='Scriptural terminology cited by the school teaching')
edge('b3.ride.support',ride,school,'support','3a:12','שהרי בזב קראו מרכב ובאשה קראו מושב')
q13=question('b3.verses.q','3a:13','מאי ואומר','Why are the further verses added?')
torahonly=claim('b3.torahonly','3a:13','וכי תימא הני מילי בדאורייתא אבל בדרבנן לא','One might limit the clean-language norm to Torah discourse and exclude rabbinic discourse.',mode='rejected',scope='Hypothetical restriction answered by added verse')
rabbinic=claim('b3.rabbinic','3a:13','תא שמע ואומר ותבחר לשון ערומים','The added verse ותבחר לשון ערומים is used to extend the norm to rabbinic discourse.',scope='Anonymous explanation of the added proof')
edge('b3.rabbinic.answer',rabbinic,torahonly,'answer','3a:13','תא שמע ואומר ותבחר לשון ערומים')
rabonly=claim('b3.rabonly','3a:13','וכי תימא הני מילי בדרבנן אבל במילי דעלמא לא','One might still exclude ordinary conversation from the norm.',mode='rejected',scope='Second hypothetical restriction')
ordinary=claim('b3.ordinary','3a:13','ואומר ודעת שפתי ברור מללו','The further verse ודעת שפתי ברור מללו extends the norm to ordinary speech.',scope='Anonymous explanation of the second added proof')
edge('b3.ordinary.answer',ordinary,rabonly,'answer','3a:13');edge('b3.verses.answer',rabbinic,q13,'answer','3a:13')
# Verse quotations remain source authorities, not invented personal speakers.
for key,quote,target in [('job15','ואומר (איוב טו, ה) ותבחר לשון ערומים',rabbinic),('job33','ואומר (איוב לג, ג) ודעת שפתי ברור מללו',ordinary)]:
    u=add('b3.'+key+'.u','utterances',dict(textual_voice='school teaching quoting Scripture',discourse_role='scriptural supporting quotation',composition='atomic'),[ev('3a:12',quote)])
    add('b3.'+key+'.a','attributions',dict(surface=quote,role='quoted_authority',candidates=[],scope='Book citation; no speaker identified by this sugya',transmission_chain=[]),[ev('3a:12',quote)],[u])
    edge('b3.'+key+'.quotation',u,target,'quotation','3a:12',quote)
rq=question('b3.woman.q','3a:14','ובאשה לא כתיב בה מרכב','Is riding terminology never written of a woman?')
reb=claim('b3.rebekah','3a:14','והכתיב (בראשית כד, סא) ותקם רבקה ונערותיה ותרכבנה על הגמלים','Genesis describes Rebekah and her attendants as riding camels, challenging the generalization.',scope='Biblical counterexample; narrator is not Rebekah')
edge('b3.rebekah.objection',reb,ride,'objection','3a:14')
camel=claim('b3.camel','3a:14','התם משום ביעתותא דגמלים אורחא היא','The camel case is ordinary riding because of fear of camels.',conditions=['camel riding'],scope='Local explanation of the biblical wording')
edge('b3.camel.answer',camel,reb,'answer','3a:14','התם משום ביעתותא דגמלים אורחא היא')
moses=claim('b3.moses','3a:14','והכתיב (שמות ד, כ) ויקח משה את אשתו ואת בניו וירכיבם על החמור','Exodus describes Moses placing his wife and sons on a donkey, another wording challenge.',scope='Second biblical counterexample')
edge('b3.moses.objection',moses,ride,'objection','3a:14','והכתיב (שמות ד, כ) ויקח משה את אשתו ואת בניו וירכיבם על החמור')
sons=claim('b3.sons','3b:1','משום בניו אורחא הוא','The wording is ordinary because it includes his sons.',conditions=['the wife and sons are described together'],scope='Continuation of התם at end of 3a:14')
edge('b3.sons.answer',sons,moses,'answer','3b:1')
abigail=claim('b3.abigail','3b:2','והכתיב (שמואל א כה, כ) והיא רוכבת על החמור','I Samuel describes her riding a donkey, another counterexample.',scope='Biblical wording; identity not independently supplied beyond verse context')
edge('b3.abigail.objection',abigail,ride,'objection','3b:2','והכתיב (שמואל א כה, כ) והיא רוכבת על החמור')
fear1=claim('b3.fearnight','3b:2','התם משום ביעתותא דליליא אורחא הוא','One answer invokes fear at night.',conditions=['night fear'],scope='First alternative explanation')
fear2=claim('b3.feardavid','3b:2','ואיבעית אימא משום ביעתותא דליליא ליכא משום ביעתותא דדוד איכא','Another answer denies night fear and invokes fear of David.',conditions=['fear of David, without night fear'],scope='Alternative explanation, not cumulative requirement')
fear3=claim('b3.fearmountain','3b:2','ואיבעית אימא ביעתותא דדוד נמי ליכא משום ביעתותא דהר איכא','A further answer denies even fear of David and invokes fear of the mountain.',conditions=['mountain fear, without fear of David'],scope='Further alternative explanation')
for i,c in enumerate([fear1,fear2,fear3]): edge('b3.fear.answer'+str(i),c,abigail,'answer','3b:2')
uncleanq=question('b3.unclean.q','3b:3','ובאורייתא מי לא כתיב טמא','Does the Torah not also use the word טמא?')
equal=claim('b3.equal','3b:3','אלא כל היכא דכי הדדי נינהו משתעי בלשון נקיה','When the expressions are of equal length, one uses clean language.',conditions=['expressions have equal length'],scope='Qualification of the speech norm')
longer=claim('b3.longer','3b:3','כל היכא דנפישין מילי משתעי בלשון קצרה','When the clean expression is longer, one uses the shorter wording.',conditions=['clean expression adds words'],scope='Brevity qualification')
edge('b3.equal.answer',equal,uncleanq,'answer','3b:3');edge('b3.longer.distinction',longer,equal,'distinction','3b:3')
short=claim('b3.short','3b:3','כדאמר רב הונא אמר רב ואמרי לה אמר רב הונא אמר רב משום ר"מ לעולם ישנה אדם לתלמידו דרך קצרה','A person should always teach a student concisely; one version reports Rav Huna in Rav’s name, another Rav Huna in Rav’s name in Rabbi Meir’s name.',scope='Two transmission versions of concise teaching',uncertainty=['Holder is Rav in first version; Rabbi Meir in second. Do not collapse versions into a single chain.'])
# Replace the helper anonymous attribution and position with explicit unresolved-version fields before first promotion.
for row in records:
    if row['id']=='pe.r001.b3.short.a': row['content']=dict(surface='רב הונא אמר רב ... ואמרי לה ... משום ר"מ',role='quoted_authority',candidates=['רב','רבי מאיר'],scope='Alternative holders across two reported versions, not a joint position',transmission_chain=[])
    if row['id']=='pe.r001.b3.short.p': row['content']['holder_candidates']=['רב','רבי מאיר'];row['uncertainty']=['Alternative versions assign the authority differently.']
for key,chain,quote in [('v1',['רב הונא','רב'],'כדאמר רב הונא אמר רב'),('v2',['רב הונא','רב','רבי מאיר'],'ואמרי לה אמר רב הונא אמר רב משום ר"מ')]:
    add('b3.short.'+key,'attributions',dict(surface=quote,role='transmitter',candidates=['רב הונא'],scope=short+'; '+key,transmission_chain=chain),[ev('3b:3',quote)],[short],uncertainty=['Alternative transmission version, not cumulative chain.'])
edge('b3.short.support',short,longer,'support','3b:3')
eqquestion=question('b3.equal.q','3b:4','וכל היכא דכי הדדי נינהו משתעי בלשון כבוד','Is respectful speech always used for equal-length expressions?')
rideequal=claim('b3.rideequal','3b:4','והא רוכבת ויושבת דכי הדדי נינהו וקאמר רוכבת','The objection treats רוכבת and יושבת as equal-length words despite the use of riding.',mode='rejected',scope='Orthographic objection')
defective=claim('b3.defective','3b:4','רכבת כתיב','The answer observes that רכבת is written defectively, making it shorter.',scope='Source’s orthographic answer')
edge('b3.rideequal.objection',rideequal,equal,'objection','3b:4');edge('b3.defective.answer',defective,rideequal,'answer','3b:4')
students=claim('b3.students','3b:5','הנהו תרי תלמידי דהוו יתבי קמיה דרב','Two students sat before Rav.',scope='Narrative frame, not a decision')
pig=claim('b3.pig','3b:5','חד אמר שויתינן האי שמעתא כדבר אחר מסנקן','One student compared the teaching’s exhaustion of them to an exhausted דבר אחר.',holder='unnamed student using דבר אחר',scope='Reported student metaphor',uncertainty=['Preserve euphemistic source wording; no named identity.'])
goat=claim('b3.goat','3b:5','וחד אמר שויתינן האי שמעתא כגדי מסנקן','The other compared it to an exhausted kid.',holder='unnamed student using גדי',scope='Reported student metaphor')
silence=claim('b3.silence','3b:5','ולא אישתעי רב בהדי דהאיך','Rav did not converse with that student, contextually the one using the degrading metaphor.',scope='Narrative consequence; referent inferred from contrast',uncertainty=['דהאיך is a pronoun, not an explicit name.'])
question('b3.grapesclean.q','3b:6','מפני מה בוצרין בטהרה ואין מוסקין בטהרה','Why harvest grapes in purity but not harvest olives in purity?')
question('b3.grapesunclean.q','3b:6','מפני מה בוצרין בטהרה ומוסקין בטומאה','Why harvest grapes in purity and olives in impurity?')
frame=claim('b3.frames','3b:6','הנהו תרי תלמידי דהוו יתבי קמיה דהלל וחד מינייהו רבן יוחנן בן זכאי ואמרי לה קמיה דרבי וחד מינייהו רבי יוחנן','One version places two students before Hillel, one being Rabban Yohanan ben Zakkai; another places them before Rabbi, one being Rabbi Yohanan.',scope='Alternative narrative versions',uncertainty=['Do not assign either named student to חד אמר by order.'])
clean=claim('b3.cleanquestion','3b:6','חד אמר מפני מה בוצרין בטהרה ואין מוסקין בטהרה','One student phrased the contrast using not-in-purity.',holder='unnamed questioner with negative-purity formulation',mode='queried',scope='Narrated question formulation, not a resolved legal explanation')
unclean=claim('b3.uncleanquestion','3b:6','וחד אמר מפני מה בוצרין בטהרה ומוסקין בטומאה','The other phrased it using in-impurity.',holder='unnamed questioner with impurity formulation',mode='queried',scope='Narrated alternative question wording')
prediction=claim('b3.prediction','3b:6','אמר מובטח אני בזה שמורה הוראה בישראל','The teacher expressed confidence that this student would issue rulings in Israel.',scope='Teacher prediction; teacher varies by narrative version',uncertainty=['Context favors cleaner wording; no fixed student-name assignment supplied.'])
fulfil=claim('b3.fulfil','3b:6','ולא היה ימים מועטים עד שהורה הוראה בישראל','The narrator says that shortly afterward he issued rulings in Israel.',scope='Narrative fulfilment, not independent historical validation')
priests=claim('b3.priests','3b:7','הנהו תלתא כהני','Three priests are introduced.',scope='Narrative frame')
for key,quote,prop in [('bean','חד אמר להו הגיעני כפול','One priest described his share as bean-sized.'),('olive','וחד אמר הגיעני כזית','Another described his share as olive-sized.'),('tail','וחד אמר הגיעני כזנב הלטאה','Another described his share as a lizard tail.')]:
    claim('b3.'+key,'3b:7',quote,prop,holder='unnamed priest: '+key,scope='Narrated metaphor for allotted share')
blemish=claim('b3.blemish','3b:7','בדקו אחריו ומצאו בו שמץ פסול','They investigated him and found a trace of disqualification.',mode='challenged',scope='Initial narrative wording; two responses follow',uncertainty=['3b:9 either corrects the wording to arrogance or preserves it under an exception.'])
noinvest=claim('b3.noinvest','3b:8','והא (תניא) אין בודקין מן המזבח ולמעלה','The objection cites the rule against further pedigree investigation beyond established altar service.',scope='Quoted rule challenging the narrative investigation')
edge('b3.noinvest.objection',noinvest,blemish,'objection','3b:8')
arrogance=claim('b3.arrogance','3b:9','לא תימא שמץ פסול אלא אימא שחץ פסול','One answer changes the reading from a trace of disqualification to disqualifying arrogance.',scope='Explicit correction of initial narrative wording')
exception=claim('b3.exception','3b:9','ואי בעית אימא שאני התם דאיהו דארע נפשיה','Alternatively, that case differs because he cast suspicion on himself.',scope='Alternative answer preserving the possibility of investigation')
edge('b3.arrogance.correction',arrogance,blemish,'correction','3b:9','לא תימא שמץ פסול אלא אימא שחץ פסול');edge('b3.exception.answer',exception,noinvest,'answer','3b:9','ואי בעית אימא שאני התם דאיהו דארע נפשיה')
notes3={
'3a:10':'Read wording question, elevated-language reply, named norm and eight-letter proof.',
'3a:11':'Read all three additional named counts; preserve counts as source claims without manufacturing agreement or recomputation.',
'3a:12':'Read school norm, zav/woman contrast and both added verse quotations; book citations are not person holders.',
'3a:13':'Read explicit why-and-another question and both staged restrictions/answers.',
'3a:14':'Read woman-wording question, Rebekah and Moses counterexamples, camel reply and open התם continuing 3b:1.',
'3b:1':'Read completion of the preceding answer: sons explain plural riding wording.',
'3b:2':'Read third counterexample and all three alternative fears, without merging mutually alternative premises.',
'3b:3':'Read equal-length/brevity qualification and both Rav Huna transmission versions; authority alternatives retained.',
'3b:4':'Read equal-length challenge and defective-spelling reply.',
'3b:5':'Read complete Rav/two-student narrative, both metaphors and pronoun-limited consequence.',
'3b:6':'Read both teacher/student identity versions, both questions, prediction and reported fulfilment; no assignment by חד אמר order.',
'3b:7':'Read three anonymous priest metaphors and initial investigated-disqualification report in light of 3b:8–9.',
'3b:8':'Read quoted no-investigation objection against initial narrative.',
'3b:9':'Read both explicit word correction and alternative self-suspicion exception; preserve initial uncertainty.'}
coverage=[]
for ref,note in notes3.items():
    sid=refs[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=note+' Source-based '+layer+' pass; '+('records listed.' if ids else 'no additional independent object after reading.')))
p=dict(schema_version=r.VERSION,tractate='Pesachim',owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[st])
out=JOB/'staging'/'language_003.json';r.immutable(out,r.encoded(p));print(out)
