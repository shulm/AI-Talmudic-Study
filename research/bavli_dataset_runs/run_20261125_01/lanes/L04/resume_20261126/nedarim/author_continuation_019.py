"""Manual explanation of ambiguous vow referents and remedial restrictions."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r019.';a.OUTPUT='continuation_019.json'
c=a.c;q=a.q;e=a.edge
a.structure('reinterpret',['20a:'+str(i) for i in range(1,10)],'Claimed alternative referents, scholar/layperson distinction, and discipline before release')
sea=c('sea','20a:1','נדר בחרם ואמר לא נדרתי אלא בחרמו של ים','The Mishnah considers a חרם declaration later explained as the sea’s net.',scope='Claimed alternative referent, not an independently verified intention')
kings=c('kings','20a:1','בקרבן ואמר לא נדרתי אלא בקרבנות של מלכים','A קרבן declaration may be explained as royal gifts.',scope='Second claimed non-sacrificial referent')
bone=c('bone','20a:2','הרי עצמי קרבן ואמר לא נדרתי אלא בעצם שהנחתי לי להיות נודר בו:','The speaker explains הרי עצמי קרבן as referring to a bone set aside for this wording.',scope='Claimed bone/self wordplay, not emendation of the original formula')
wife=c('wife','20a:2','קונם אשתי נהנית לי ואמר לא נדרתי אלא באשתי הראשונה שגירשתי','He explains a wife-benefit קונם as referring to his first wife whom he divorced.',conditions=['claimed referent is divorced first wife'],scope='Claimed restricted referent')
meir=c('meir','20a:3',None,'Rabbi Meir states אין נשאלין להם, then prescribes punishment and stringency if they seek release.',holder='רבי מאיר',composition='composite',scope='Printed wording retained; apparent inconsistency resolved in Gemara rather than silently paraphrased away')
sages=c('sages','20a:4',None,'The sages seek an opening from elsewhere and instruct them not to treat vows lightly.',holder='חכמים',composition='composite',scope='Remedial procedure and stated educational purpose')
conflict=q('conflict','20a:5',None,'How can the Mishnah first say אין נשאלין and then prescribe treatment if they seek release?')
scholar=c('scholar','20a:6','אמר רב יהודה הכי קתני וכולן אין צריכין שאלה במה דברים אמורים בתלמיד חכם','Rav Yehuda reads the opening as no release consultation being needed for a scholar.',holder='רב יהודה',conditions=['תלמיד חכם'],scope='Explicit reconstruction אין צריכין שאלה')
lay=c('lay','20a:6','אבל בעם הארץ שבא לישאל עונשין אותו ומחמירין עליו','For a layperson who seeks release, punishment and stringency are imposed.',holder='רב יהודה',conditions=['עם הארץ comes for release'],scope='Second branch of explanation')
e('scholar.answer',scholar,conflict,'answer','20a:6');e('lay.qualification',lay,meir,'qualification','20a:6')
strict=c('strict','20a:7','בשלמא מחמירין דלא פתחינן ליה בחרטה','Stringency is understood as not opening release on mere regret.',scope='Anonymous explanation of מחמירין')
punishq=q('punishq','20a:7','אלא עונשין היכי דמי','What does punishing mean here?')
yehuda=c('yehuda','20a:8','כדתניא מי שנזר ועבר על נזירותו אין נזקקין לו עד שינהוג בו איסור כימים שנהג בהן היתר דברי רבי יהודה','Rabbi Yehuda says a nazirite who violated his undertaking is not assisted until observing prohibition for as many days as he treated it as permitted.',holder='רבי יהודה',conditions=['nazirite violated undertaking','period of permitted conduct'],scope='Cited disciplinary rule illustrating punishment')
yosei=c('yosei','20a:8','אמר רבי יוסי במה דברים אמורים בנזירות מועטת אבל בנזירות מרובה דיו שלושים יום','Rabbi Yosei limits this to short naziriteship; for lengthy naziriteship, thirty days suffice.',holder='רבי יוסי',conditions=['short versus lengthy naziriteship'],composition='composite',scope='Explicit limitation on remedial duration')
e('yehuda.answer',yehuda,punishq,'answer','20a:8');e('yosei.qualification',yosei,yehuda,'qualification','20a:8')
yosef=c('yosef','20a:9','אמר רב יוסף הואיל ואמרי רבנן אין נזקקים לו בי דינא דמזדקקי לא עביד שפיר','Rav Yosef says a court that nevertheless assists him acts improperly.',holder='רב יוסף',conditions=['court assists despite stated waiting restriction'])
aha=c('aha','20a:9','רב אחא בר יעקב אומר משמתינן ליה:','Rav Aha bar Yaakov prescribes excommunication for the transgressing adjudicator.',holder='רב אחא בר יעקב',scope='Sanction against one who disregards the stated judicial restriction; no personal historical identity assigned')
a.notes={
'20a:1':'Reread both claimed reinterpretations, sea-net and royal gifts, preserving claimed-intent status.',
'20a:2':'Reread bone/self play and divorced-first-wife qualification separately.',
'20a:3':'Reread Rabbi Meir’s apparently inconsistent wording and preserve subsequent need for explanation.',
'20a:4':'Reread sages’ alternative opening and teaching purpose.',
'20a:5':'Reread explicit internal contradiction question.',
'20a:6':'Reread Rav Yehuda reconstruction and scholar/layperson conditions.',
'20a:7':'Reread no-mere-regret explanation and separate punishment question.',
'20a:8':'Reread Rabbi Yehuda matched-day restriction and Rabbi Yosei thirty-day limit for long cases.',
'20a:9':'Reread Rav Yosef improper-court judgment and Rav Aha bar Yaakov stronger sanction.'}
if __name__=='__main__':a.save()
