"""Circumcision terminology and attributed aggadic alternatives; no medical/generalized inference."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r031.';a.OUTPUT='continuation_031.json'
c=a.c;q=b.q;e=a.edge
a.structure('labels',['31b:6','31b:7'],'Circumcised/uncircumcised designations in vow interpretation')
a.structure('praise',['31b:'+str(i) for i in range(8,15)]+['32a:'+str(i) for i in range(1,8)],'Attributed praises, Moses interpretations and cosmic-covenant disagreement')
uncirc=c('uncirc','31b:6','קונם שאני נהנה לערלים מותר בערלי ישראל ואסור במולי נוכרים','The Mishnah’s vow against ערלים permits uncircumcised Israel and prohibits circumcised non-Jews.',composition='composite',scope='Source’s conventional religious designation, distinct from bodily status')
circ=c('circ','31b:7','שאני נהנה למולים אסור בערלי ישראל ומותר במולי נוכרים','The vow against מולים prohibits uncircumcised Israel and permits circumcised non-Jews.',composition='composite',scope='Reverse conventional designation in this Mishnah')
name=c('name','31b:7','שאין הערלה קרויה אלא לשם נוכרים','The Mishnah explains its lexical classification by associating the term ערלה with non-Jews.',scope='Source’s religious rhetoric and terminology, not assistant characterization')
jer=c('jer','31b:7','שנאמר כי כל הגוים ערלים וכל בית ישראל ערלי לב (ירמיהו ט, כה)','The first support is Jeremiah’s contrast between bodily and heart-related uncircumcision.',scope='Explicit biblical quotation')
phil=c('phil','31b:7','ואומר והיה הפלשתי הערל הזה (שמואל א יז, לו)','The second support quotes the description of the Philistine.',scope='First Samuel quotation used for lexical evidence')
daughters=c('daughters','31b:7','ואומר פן תשמחנה בנות פלשתים פן תעלוזנה בנות הערלים (שמואל ב א, כ)','The third support quotes Philistine daughters and daughters of the uncircumcised in parallel.',scope='Second Samuel quotation used for lexical evidence')
for key,claim in [('jer',jer),('phil',phil),('daughters',daughters)]:e(key+'.support',claim,name,'support','31b:7')
azarya=c('azarya','31b:8','רבי אלעזר בן עזריה אומר מאוסה היא הערלה שנתגנו בה רשעים שנאמר כי כל הגוים ערלים (ירמיהו ט, כה)','Rabbi Elazar ben Azarya calls uncircumcision repugnant because Scripture uses it to disparage the wicked, citing Jeremiah.',holder='רבי אלעזר בן עזריה',scope='Attributed evaluative religious teaching, not an independent judgment about people')
ishmael=c('ishmael','31b:8','רבי ישמעאל אומר גדולה מילה שנכרתו עליה שלוש עשרה בריתות','Rabbi Yishmael praises circumcision through thirteen covenants associated with it.',holder='רבי ישמעאל',scope='Source’s covenant-count assertion, not independently enumerated here')
yosei=c('yosei','31b:9',None,'Rabbi Yosei praises circumcision for overriding the stringent Sabbath.',holder='רבי יוסי',scope='Attributed praise; full timing/eligibility conditions not supplied in this excerpt')
karha=c('karha','31b:10',None,'Rabbi Yehoshua ben Korha praises circumcision because Moses was not granted even an hour’s delay regarding it.',holder='רבי יהושע בן קרחה',scope='Aggadic reading developed and challenged below')
nehemiah=c('nehemiah','31b:11','רבי נחמיה אומר גדולה מילה שדוחה את הנגעים','Rabbi Nehemiah praises circumcision for overriding the skin-affliction restriction.',holder='רבי נחמיה',scope='Source’s legal-religious comparison; not contemporary medical guidance')
rabbi=c('rabbi','31b:11','רבי אומר גדולה מילה שכל המצוות שעשה אברהם אבינו לא נקרא שלם עד שמל שנאמר התהלך לפני והיה תמים (בראשית יז, א)','Rabbi says Abraham was not called complete despite his commandments until circumcision, citing התהלך לפני והיה תמים.',holder='רבי',scope='Attributed scriptural interpretation')
world=c('world','31b:12',None,'An alternative teaching says the world would not have been created without circumcision, interpreting the covenant verse in Jeremiah.',scope='Explicit דבר אחר; speaker not newly named, cosmic assertion remains source-attributed')
moses=c('moses','31b:13',None,'A baraita in Rabbi Yehoshua ben Korha’s name says Moses’ merits did not protect him when he delayed circumcision, citing the encounter threatening his life.',holder='רבי יהושע בן קרחה',scope='Distinct quoted occurrence, subsequently opposed by Rabbi')
deny=c('deny','31b:14','אמר רבי חס ושלום שמשה רבינו נתרשל מן המילה','Rabbi rejects describing Moses as negligent in circumcision.',holder='רבי',scope='Explicit interpretive objection to negligence characterization')
travel=c('travel','31b:14',"אלא כך אמר אמול ואצא סכנה היא שנאמר ויהי ביום השלישי בהיותם כואבים וגו' (בראשית לד, כה)",'Rabbi attributes to Moses concern that circumcision followed by travel would endanger the child, citing the third-day pain verse.',holder='רבי',scope='Rabbi’s reconstructed reasoning, not directly recorded speech by Moses or current medical advice')
delay=c('delay','31b:14','אמול ואשהא שלשה ימים הקב"ה אמר לי לך שוב מצרים (שמות ד, יט)','The other branch is circumcising and waiting three days, constrained by the divine command to return to Egypt.',holder='רבי',scope='Second branch of Rabbi’s reconstructed dilemma')
punish=q('punish','31b:14','אלא מפני מה נענש משה','Then why was Moses punished?',voice='רבי')
lodging=c('lodging','32a:1',None,'The answer faults attending first to lodging, citing ויהי בדרך במלון.',holder='רבי',scope='Continuation of Rabbi’s account, distinct from broad negligence charge')
e('deny.objection',deny,moses,'objection','31b:14');e('lodging.answer',lodging,punish,'answer','32a:1')
child=c('child','32a:2','רבן שמעון בן גמליאל אומר לא למשה רבינו ביקש שטן להרוג אלא לאותו תינוק','Rabban Shimon ben Gamliel says Satan sought to kill the infant rather than Moses.',holder='רבן שמעון בן גמליאל',scope='Alternative identification of threatened person, not harmonized with prior account')
groom=c('groom','32a:2','שנאמר כי חתן דמים אתה לי (שמות ד כה) צא וראה מי קרוי חתן הוי אומר זה התינוק','He identifies the infant as the one called חתן, supporting this from חתן דמים.',holder='רבן שמעון בן גמליאל',scope='Embedded rhetorical question and explicit answer in derivation',composition='composite')
e('groom.support',groom,child,'support','32a:2');e('child.distinction',child,moses,'distinction','32a:2')
angels=c('angels','32a:3','דרש רבי יהודה בר ביזנא בשעה שנתרשל משה רבינו מן המילה באו אף וחימה ובלעוהו ולא שיירו ממנו אלא רגליו','Rabbi Yehuda bar Bizna expounds that Af and Hema swallowed Moses, leaving only his legs, when he delayed circumcision.',holder='רבי יהודה בר ביזנא',composition='composite',scope='Aggadic narrative, not independently verified event')
zipporah=c('zipporah','32a:3','מיד ותקח צפורה צור ותכרת את ערלת בנה (שמות ד, כה) מיד וירף ממנו (שמות ד, כו)','The exposition links Zipporah’s circumcising her son immediately with the release from the attack.',holder='רבי יהודה בר ביזנא',composition='composite',scope='Sequence of cited verses within exposition')
kill=c('kill','32a:4','באותה שעה ביקש משה רבינו להורגן שנאמר הרף מאף ועזוב חמה (תהלים לז, ח)','The account says Moses sought to kill Af and Hema and reads the Psalm accordingly.',scope='Aggadic interpretation, intended action rather than completed killing')
killed=c('killed','32a:4','ויש אומרים לחימה הֲרָגוֹ שנאמר חמה אין לי (ישעיהו כז, ד)','An explicitly unnamed alternative says he killed Hema, citing חמה אין לי.',scope='יש אומרים variant retained; not attributed to a named sage')
fear=q('fear','32a:4','והכתיב כי יגרתי מפני האף והחמה (דברים ט, יט)','How does that fit Moses’ later fear of Af and Hema?')
two=c('two','32a:4','תרי חימה הוו','One answer posits two figures called Hema.',scope='First aggadic reconciliation')
troop=c('troop','32a:4','ואיבעית אימא גונדא דחימה','Alternatively, the feared entity is Hema’s troop.',scope='Explicit alternative reconciliation')
e('two.answer',two,fear,'answer','32a:4');e('troop.answer',troop,fear,'answer','32a:4')
complete=c('complete','32a:5',None,'A baraita repeats Rabbi’s teaching that Abraham’s completeness is associated with circumcision despite his many commandments, adjoining the covenant verse.',holder='רבי',composition='composite',scope='Separate occurrence with two explicit verses')
equal=c('equal','32a:6',"דבר אחר גדולה מילה ששקולה כנגד כל המצוות שבתורה שנאמר כי על פי הדברים האלה וגו' (שמות לד, כז)",'Another explanation calls circumcision equal to all Torah commandments, citing כי על פי הדברים האלה.',scope='Alternative homiletic valuation; does not cancel other obligations')
cosmos=c('cosmos','32a:6',"דבר אחר גדולה מילה שאילמלא מילה לא נתקיימו שמים וארץ שנאמר אם לא בריתי יומם ולילה וגו' (ירמיהו לג, כה)",'Another explanation says heaven and earth would not endure without circumcision, interpreting Jeremiah’s covenant verse.',scope='Attributed alternative cosmic teaching')
torah=c('torah','32a:7',None,'The discussion explicitly contrasts Rabbi Eliezer, who interprets the same covenant verse as Torah sustaining heaven and earth.',holder='רבי אליעזר',scope='Explicit ופליגא marks different interpretation of covenant referent')
e('torah.objection',torah,cosmos,'objection','32a:7')
a.notes={
'31b:6':'Reread uncircumcised designation rule, separating conventional category from actual bodily state.',
'31b:7':'Reread reverse rule, lexical explanation and all three biblical supports separately.',
'31b:8':'Reread Elazar ben Azarya’s attributed evaluation and Yishmael covenant count.',
'31b:9':'Reread Yosei Sabbath comparison without importing unstated practical conditions.',
'31b:10':'Reread Yehoshua ben Korha Moses-delay praise and followed all competing explanations.',
'31b:11':'Reread Nehemiah afflictions comparison and Rabbi Abraham-completeness interpretation.',
'31b:12':'Reread alternative world-creation interpretation and exact covenant quotation.',
'31b:13':'Reread baraita negligence interpretation and supporting Exodus verse.',
'31b:14':'Reread Rabbi explicit rejection, travel/delay dilemma and punishment question spanning page.',
'32a:1':'Reread lodging-first answer as Rabbi continuation.',
'32a:2':'Reread Shimon ben Gamliel infant-not-Moses alternative and חתן derivation.',
'32a:3':'Reread Yehuda bar Bizna swallowing narrative and Zipporah/release verse sequence.',
'32a:4':'Reread intended killing, unnamed completed-Hema variant, fear contradiction and both reconciliations.',
'32a:5':'Reread repeated Rabbi completeness baraita with both verses, retained distinct occurrence.',
'32a:6':'Reread two דבר אחר valuations and their respective prooftexts.',
'32a:7':'Reread explicit disagreement with Rabbi Eliezer’s Torah interpretation; no conflation of covenant referents.'}
if __name__=='__main__':a.save()
