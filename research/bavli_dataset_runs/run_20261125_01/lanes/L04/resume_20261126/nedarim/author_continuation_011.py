"""Manual negative wording and competing reported positions of Rabbi Yehuda."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r011.';a.OUTPUT='continuation_011.json'
c=a.c;q=a.q;e=a.edge
a.structure('mishnah',['10b:12','10b:13'],'Prohibitory expressions and comparisons to sacrificial objects')
a.structure('tanna',['11a:'+str(i) for i in range(1,7)],'Attributing the Mishnah and preserving divergent reports of Rabbi Yehuda')
a.structure('negative',['11b:'+str(i) for i in range(1,7)],'Negative formulations, implication, and two explanations of a baraita')
listc=c('list','10b:12','האומר לחולין שאוכל לך לא כשר ולא דכי טהור וטמא נותר ופיגול אסור','The Mishnah lists לחולין שאוכל לך, לא כשר, לא דכי, טהור וטמא, נותר ופיגול and states prohibition.',composition='composite',scope='Printed list retained exactly; do not silently regularize טהור or supply missing negations; following discussion explains לחולין')
objects=c('objects','10b:13','כאימרא כדירים כעצים כאשים כמזבח כהיכל כירושלים','The Mishnah lists comparisons כאימרא, כדירים, כעצים, כאשים, כמזבח, כהיכל and כירושלים.',composition='composite',scope='Seven listed sacrificial comparisons, with effect in next clause')
effect=c('effect','10b:13','נדר באחד מכל משמשי המזבח אף על פי שלא הזכיר קרבן הרי זה נדר בקרבן','A vow by reference to an altar-associated object takes effect as an offering vow even without saying קרבן.',conditions=['reference to an item in the stated altar-service category'],scope='Mishnah formulation rule')
jer=c('jer','10b:13','רבי יהודה אומר האומר ירושלים לא אמר כלום','Rabbi Yehuda says that saying ירושלים has no effect.',holder='רבי יהודה',conditions=['ירושלים without כ'],scope='Printed Mishnah report; divergent report below explicitly preserved')
initial=c('initial','11a:1','סברוה מאי לחולין לא לחולין ליהוי אלא קרבן','The initial reading interprets לחולין as “not unconsecrated, but an offering.”',mode='hypothetical',scope='Explicit סברוה interpretation used in ensuing attribution argument')
who=q('who','11a:2','מני מתניתין','Whose view is the Mishnah?')
meir=c('meir','11a:2','אי רבי מאיר לית ליה מכלל לאו אתה שומע הן','Rabbi Meir does not infer the positive from the negative, creating an attribution difficulty.',scope='Anonymous stated premise about Rabbi Meir')
condition=c('condition','11a:2','דתנן רבי מאיר אומר כל תנאי שאינו כתנאי בני גד ובני ראובן אינו תנאי','The cited Mishnah has Rabbi Meir require a condition to follow the form of the children of Gad and Reuben.',holder='רבי מאיר',scope='Cited conditional-form rule, used here for implication principle')
e('condition.support',condition,meir,'support','11a:2')
assign=c('assign','11a:3','אלא רבי יהודה היא','The discussion instead proposes Rabbi Yehuda as the Mishnah’s author.',mode='challenged',scope='Tentative attribution, objection immediately follows')
tail=c('tail','11a:3','אימא סיפא רבי יהודה אומר האומר ירושלים לא אמר כלום','The objection cites the ending separately naming Rabbi Yehuda on ירושלים.',scope='Repeated occurrence of Mishnah’s named ending')
infer=c('infer','11a:3','מדסיפא רבי יהודה רישא לאו רבי יהודה היא','The objection infers that the opening must differ from Rabbi Yehuda because the ending names him separately.',mode='rejected',scope='Attribution inference explicitly rejected next')
e('assign.answer',assign,who,'answer','11a:3');e('tail.support',tail,infer,'support','11a:3');e('infer.objection',infer,assign,'objection','11a:3')
all=c('all','11a:4',None,'The reply attributes the entire Mishnah to Rabbi Yehuda and reads the ending as a supporting “for Rabbi Yehuda says.”',composition='composite',scope='Explicit proposed reading שרבי יהודה, not silent emendation')
e('all.correction',all,infer,'correction','11a:4')
kyq=q('kyq','11a:5','וכי אמר כירושלים לרבי יהודה מי מיתסר','Does Rabbi Yehuda prohibit when one says כירושלים?')
other=c('other','11a:5','והתניא רבי יהודה אומר האומר כירושלים לא אמר כלום עד שידור בדבר הקרב בירושלים','Another teaching reports Rabbi Yehuda giving כירושלים no effect unless the vow refers to something offered in Jerusalem.',holder='רבי יהודה',conditions=['must vow by something offered in Jerusalem'],scope='Distinct reported position, not harmonized with the printed Mishnah by deleting כ')
two=c('two','11a:6',None,'The reply maintains Rabbi Yehuda attribution and identifies two tannaitic reports of his view.',scope='Explicit divergent reports, no historical final choice inferred',composition='composite')
e('other.support',other,kyq,'support','11a:5');e('kyq.objection',kyq,all,'objection','11a:5');e('two.answer',two,kyq,'answer','11a:6')
plain=c('plain','11b:1','תניא חולין החולין כחולין בין שאוכל לך ובין שלא אוכל לך מותר','The baraita permits חולין, החולין and כחולין with either שאוכל לך or שלא אוכל לך.',composition='composite',conditions=['one of three listed forms','either positive or negative eating phrase'],scope='Explicit three-by-two formulation group')
positive=c('positive','11b:1','לחולין שאוכל לך אסור','לחולין שאוכל לך prohibits.',conditions=['exact listed positive eating formula'],scope='Baraita')
negative=c('negative','11b:1','לחולין לא אוכל לך מותר','לחולין לא אוכל לך is permitted.',conditions=['exact listed negative eating formula'],scope='Baraita, apparently challenged below')
headq=q('headq','11b:2','רישא מני','Whose view is the beginning of this baraita?')
head=c('head','11b:2','רבי מאיר היא דלית ליה מכלל לאו אתה שומע הין','It is initially assigned to Rabbi Meir, who does not infer affirmation from negation.',mode='challenged',scope='Initial attribution, refined below')
e('head.answer',head,headq,'answer','11b:2')
tailagain=c('tailagain','11b:3','אימא סיפא לחולין לא אוכל לך מותר','The objection repeats the final permission for לחולין לא אוכל לך.',scope='Repeated baraita clause')
offerc=c('offerc','11b:3','והתנן לקרבן לא אוכל לך רבי מאיר אוסר','A cited Mishnah has Rabbi Meir prohibit לקרבן לא אוכל לך.',holder='רבי מאיר',conditions=['לקרבן לא אוכל לך'],scope='Quoted apparent counterexample')
contradict=q('contradict','11b:3','וקשיא לן הא לית ליה מכלל לאו אתה שומע הין','How does this fit his rejection of positive implication from a negative?')
abba=c('abba','11b:4','ואמר רבי אבא נעשה כאומר לקרבן יהא לפיכך לא אוכל לך','Rabbi Abba explains that it is as though he said: let it be an offering, therefore I will not eat of yours.',holder='רבי אבא',scope='Reported explanation of Rabbi Meir’s offering formulation')
analogy=c('analogy','11b:4','הכא נמי הכי קאמר ליה לא חולין ליהוי לפיכך לא אוכל לך','By the same reasoning the present wording should mean: let it not be unconsecrated, therefore I will not eat.',mode='challenged',scope='Anonymous extension challenging the baraita’s permission')
e('abba.answer',abba,contradict,'answer','11b:4');e('abba.analogy',abba,analogy,'analogy','11b:4');e('analogy.objection',analogy,negative,'objection','11b:4')
partial=c('partial','11b:5',None,'The first answer makes the baraita’s tanna agree with Rabbi Meir about not inferring affirmation from negation, but disagree about the offering formula.',composition='composite',scope='Two-point partial agreement, not a complete Rabbi Meir attribution')
e('partial.answer',partial,analogy,'answer','11b:5');e('partial.qualification',partial,head,'qualification','11b:5')
ashi=c('ashi','11b:6',None,'Rav Ashi distinguishes לחולין from explicit לא חולין, the latter meaning not unconsecrated but like an offering.',holder='רב אשי',composition='composite',conditions=['distinguish exact wording לחולין / לא חולין'],scope='Alternative wording-based resolution; no phonetic vowels added to the pinned consonantal text')
e('ashi.answer',ashi,analogy,'answer','11b:6')
a.notes={
'10b:12':'Reread every printed Mishnah label, preserving unusual טהור wording without emendation; expressly composite list.',
'10b:13':'Reread seven comparisons, altar-service rule and named bare-Jerusalem exception.',
'11a:1':'Reread סברוה interpretation as initial reading, not final universally accepted etymology.',
'11a:2':'Reread tanna question, implication premise and Gad/Reuben condition quotation.',
'11a:3':'Reread Rabbi Yehuda proposal, repeated ending and rejected inference of different author.',
'11a:4':'Reread whole-Mishnah attribution and explicit שרבי יהודה reading.',
'11a:5':'Reread כירושלים objection and separate Rabbi Yehuda report requiring offered object.',
'11a:6':'Reread two-tannaim reporting resolution; conflicting reports remain distinct.',
'11b:1':'Reread six plain variants as grouped composite, positive לחולין prohibition and negative permission separately.',
'11b:2':'Reread initial Rabbi Meir attribution and reason.',
'11b:3':'Reread baraita ending, distinct offering counterexample and explicit consistency question.',
'11b:4':'Reread Rabbi Abba explanation and anonymous analogical extension; not conflated voices.',
'11b:5':'Reread selective agreement/disagreement answer as explicit two-point composite.',
'11b:6':'Reread Rav Ashi alternative distinguishing printed forms; no unverified vowel reconstruction.'}
if __name__=='__main__':a.save()
