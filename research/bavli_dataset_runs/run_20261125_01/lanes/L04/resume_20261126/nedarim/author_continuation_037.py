"""Teruma from another’s produce: consent proof deflection and recipient-selection benefit."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r037.';a.OUTPUT='continuation_037.json'
c=a.c;q=b.q;e=a.edge
a.structure('teruma',['36b:'+str(i) for i in range(1,9)],'Consent and benefit of selecting recipient when separating one’s own produce for another')
consent=a.q('consent','36b:1','איבעיא להו התורם משלו על של חבירו צריך דעתו או לא','Does separating one’s own produce as teruma for another’s produce require that other’s consent?')
next(x for x in a.records if x['id']==consent)['uncertainty'].append('The Mishnah-based proof is deflected; the local continuation does not explicitly settle this consent question.')
benefit=c('benefit','36b:1','מי אמרינן כיון דזכות הוא לו לא צריך דעת','One branch dispenses with consent because the separation benefits the owner.',mode='hypothetical',scope='First question alternative')
mitzva=c('mitzva','36b:1','או דלמא מצוה דיליה היא וניחא ליה למיעבדיה','The other branch considers the owner’s wish to perform his own commandment.',mode='hypothetical',scope='Second question alternative')
cited=c('cited','36b:2','תא שמע תורם את תרומותיו ואת מעשרותיו לדעתו','The Mishnah’s permission to separate לדעתו is proposed as evidence.',scope='Consent pronoun remains to be parsed')
ownpile=c('ownpile','36b:2','במאי עסקינן אילימא מן בעל הכרי על של בעל הכרי ולדעתו דמאן אילימא לדעתו דיליה מאן שוויה שליח','The first construction uses the owner’s produce for his own pile; if consent is only the separator’s, the question asks who made him agent.',mode='challenged',composition='composite',scope='Rejected construction within proof argument')
owner=c('owner','36b:3','אלא לדעתו דבעל הכרי הא קמהני ליה דקעביד שליחותיה','If the consent is the owner’s, serving as his agent would confer prohibited benefit.',mode='challenged',scope='Second construction within proof')
donor=c('donor','36b:3','אלא משלו על של הכרי ולדעתו דמאן אילימא לדעתו דבעל הכרי הא קמהני ליה','The argument shifts to the separator’s own produce but again objects if owner consent makes it beneficial agency.',mode='challenged',composition='composite',scope='Third construction within attempted proof')
no=c('no','36b:3','אלא לאו לדעתיה דנפשיה ומשלו תורם על של חבירו ואי אמרת צריך דעת הא קמהני ליה אלא לאו אין צריך דעת','The proposed inference is own-produce separation on the separator’s initiative, apparently proving owner consent unnecessary.',mode='challenged',composition='composite',scope='Inference deflected next segment, not accepted answer')
open=c('open','36b:4',None,'The reply returns to owner-produce separation, using Rava’s formulation that whoever wishes to separate may come and do so.',scope='General invitation distinguishes this from personally appointed agency; proof does not settle own-produce consent')
e('no.support',no,consent,'support','36b:3');e('open.correction',open,no,'correction','36b:4');e('open.unresolved',open,consent,'unresolved_outcome','36b:4')
whose=q('whose','36b:5','בעא מיניה רבי ירמיה מרבי זירא התורם משלו על של חבירו טובת הנאה של מי','Rabbi Yirmeya asks Rabbi Zeira who holds the benefit of choosing the recipient when one separates his own produce for another.',voice='רבי ירמיה')
fruit=c('fruit','36b:5','מי אמרינן אי לאו פירי דהאיך מי מתקנא כריא דההוא','One branch emphasizes that the separator’s produce makes the other pile fit.',mode='hypothetical',scope='Argument favoring separator’s benefit')
pile=c('pile','36b:5','או דלמא אי לאו כריא דההוא לא הויין פירי דהדין תרומה','The other emphasizes that without the owner’s pile the separator’s produce would not become teruma.',mode='hypothetical',scope='Argument favoring pile owner’s benefit')
verse=c('verse','36b:6',None,'Rabbi Zeira answers by citing את כל תבואת זרעך ונתת.',holder='רבי זירא',scope='Compressed verse-only answer; no extra owner designation supplied in the quote',uncertainty=['The next objection assumes an owner-benefit reading; do not silently insert an unstated prose ruling into this verse-only answer.'])
e('verse.answer',verse,whose,'answer','36b:6')
challenge=q('challenge','36b:7','איתיביה תורם את תרומותיו ואת מעשרותיו לדעתו ואי אמרת טובת הנאה דבעל הכרי הא קא מהני ליה','If the benefit belongs to the pile owner, would the Mishnah’s permitted separation not confer prohibited benefit?')
inference=c('inference','36b:7','אלא שמע מינה טובת הנאה דיליה','The attempted proof infers that the benefit belongs to the separator.',mode='challenged',scope='This proof route is deflected, though separate explicit Yohanan evidence follows')
deflect=c('deflect','36b:7','אמרי לא משל בעל הכרי על של בעל הכרי ולדעתו דבעל הכרי באומר כל הרוצה לתרום יבא ויתרום','The reply again uses owner produce, owner consent and a general whoever-wishes invitation.',composition='composite',scope='Deflection of Mishnah-based recipient-benefit inference')
e('deflect.answer',deflect,challenge,'answer','36b:7');e('deflect.correction',deflect,inference,'correction','36b:7')
fifth=c('fifth','36b:8','תא שמע דאמר רבי אבהו אמר רבי יוחנן המקדיש מוסיף חומש','Rabbi Yohanan, through Rabbi Abbahu, assigns the added fifth to the consecrator.',holder='רבי יוחנן',scope='First clause of cited three-role teaching')
exchange=c('exchange','36b:8','ומתכפר עושה תמורה','He assigns substitution power to the person receiving atonement.',holder='רבי יוחנן',scope='Second distinct role, not conflated with consecrator')
right=c('right','36b:8','והתורם משלו על שאינו שלו טובת הנאה שלו','He assigns recipient-selection benefit to the person separating his own produce for another’s.',holder='רבי יוחנן',scope='Explicit evidence answering recipient-benefit question; does not itself settle prior consent question')
for key,claim in [('fifth',fifth),('exchange',exchange),('right',right)]:a.add(key+'.chain','attributions',dict(surface='אמר רבי אבהו אמר רבי יוחנן',role='transmitter',candidates=['רבי אבהו'],scope=claim,transmission_chain=['רבי אבהו','רבי יוחנן']),[a.ev('36b:8','אמר רבי אבהו אמר רבי יוחנן')],[claim])
e('right.answer',right,whose,'answer','36b:8')
a.notes={
'36b:1':'Reread consent question and both benefit-versus-personal-commandment alternatives; final consent outcome not invented.',
'36b:2':'Reread Mishnah proof introduction and owner-produce/separator-awareness agency difficulty.',
'36b:3':'Reread owner-consent agency objection, own-produce alternative and proposed no-consent inference.',
'36b:4':'Reread Rava general-invitation construction deflecting inference.',
'36b:5':'Reread Yirmeya-to-Zeira recipient-benefit question and both causal arguments.',
'36b:6':'Reread verse-only Zeira response without expanding unstated prose ruling.',
'36b:7':'Reread owner-benefit objection, proposed separator-benefit proof and repeated general-invitation deflection.',
'36b:8':'Reread Abbahu-to-Yohanan chain and all three separate role assignments; explicit separator-benefit answer.'}
if __name__=='__main__':a.save()
