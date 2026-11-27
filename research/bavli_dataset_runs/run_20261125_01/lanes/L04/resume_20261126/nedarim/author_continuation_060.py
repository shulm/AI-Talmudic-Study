"""Manual reading of exchange/growth and conditional temporal Mishnah clauses."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r060.';a.OUTPUT='continuation_060.json'
c=a.c;e=a.edge
a.structure('growth',['57a:1','57a:2'],'Parallel fruit and wife-produced-item formulas with seed persistence condition')
a.structure('times',['57a:3','57b:1'],'Placement of time limits and conditional visits')
fruit=c('fruit','57a:1','קונם פירות האלו עלי קונם הן על פי קונם הן לפי אסור בחילופיהן ובגידוליהן','The formulas these fruits upon me, upon my mouth, or to my mouth prohibit their exchanges and growths.',composition='composite',scope='All three explicit formulations and both derivative categories')
taste=c('taste','57a:1','שאני אוכל ושאני טועם מותר בחילופיהן ובגידוליהן בדבר שזרעו כלה','The eating/tasting formulations permit exchanges and growths where the seed is consumed.',composition='composite',scope='Printed שאני wording retained, not silently normalized to שאיני; seed condition explicitly attached')
persist=c('persist','57a:1','אבל בדבר שאין זרעו כלה אפילו גידולי גידולין אסורין','Where the seed persists, even growths of growths are prohibited.',scope='Explicit exception to preceding permission')
work=c('work','57a:2','האומר לאשתו קונם מעשה ידיך עלי קונם הן על פי קונם הן לפי אסור בחילופיהן ובגידוליהן','A husband’s formulas prohibiting his wife’s handiwork upon him or his mouth likewise prohibit exchanges and growths.',composition='composite',scope='Separate parallel occurrence, all three printed formulas retained in evidence')
worktaste=c('worktaste','57a:2','שאני אוכל שאני טועם מותר בחילופיהן ובגידוליהן בדבר שזרעו כלה','The parallel eating/tasting formulas permit exchanges and growths where the seed is consumed.',composition='composite',scope='Wife-produced-item context and printed positive wording preserved')
workpersist=c('workpersist','57a:2','אבל דבר שאין זרעו כלה אפילו גידולי גידולין אסורין','Where the seed persists, the handiwork-context rule also prohibits growths of growths.',scope='Repeated exception retained as separate source occurrence')
untiluse=c('untiluse','57a:3','שאת עושה איני אוכל עד הפסח שאת עושה איני מתכסה עד הפסח עשתה לפני הפסח מותר לאכול ולהתכסות אחר הפסח','If the vow limits eating or wearing her work until Passover, items made beforehand may be eaten or worn afterward.',composition='composite',scope='Time limit modifies the prohibited use; two parallel use formulas and later permission')
untilmake=c('untilmake','57a:3','שאת עושה עד הפסח איני אוכל ושאת עושה עד הפסח איני מתכסה עשתה לפני הפסח אסור לאכול ולהתכסות אחר הפסח','If the vow targets what she makes until Passover, items made beforehand remain forbidden to eat or wear afterward.',composition='composite',scope='Time limit modifies production; contrast with prior word order')
visitbefore=c('visitbefore','57a:3','שאת נהנית לי עד הפסח אם הולכת את לבית אביך עד החג הלכה לפני הפסח אסורה בהנאתו עד הפסח','If benefit until Passover is conditioned on her visiting her father before the festival, a visit before Passover prohibits benefit until Passover.',mode='conditional',scope='Distinct benefit deadline and later visit-condition deadline retained')
visitafter=c('visitafter','57b:1','לאחר הפסח בבל יחל','A visit after Passover invokes the prohibition against profaning the vow.',scope='Continuation of prior condition, retroactive force regarding earlier benefit; source does not state a new post-Passover benefit ban',extra=[('57a:3','שאת נהנית לי עד הפסח אם הולכת את לבית אביך עד החג')])
reversevisit=c('reversevisit','57b:1','שאת נהנית לי עד החג אם הולכת את לבית אביך עד הפסח הלכה לפני הפסח אסורה בהנאתו עד החג','If benefit until the festival is conditioned on a visit before Passover, such an early visit prohibits benefit until the festival.',mode='conditional',scope='Reverse deadline arrangement, explicit continuing benefit prohibition')
late=c('late','57b:1','ומותרת לילך אחר הפסח','She may visit after Passover under the latter condition.',scope='Visit-condition deadline has expired; not a blanket release of a benefit prohibition already activated by an earlier visit')
e('time.distinction',untilmake,untiluse,'distinction','57a:3');e('late.qualification',late,reversevisit,'qualification','57b:1')
a.notes={
'57a:1':'Reread all three item formulas, eating/tasting wording, both derivative categories and consumed/persistent seed conditions.',
'57a:2':'Reread complete wife-handiwork parallel separately, without deduplicating source occurrence.',
'57a:3':'Reread both eating/wearing word-order pairs and their opposite post-Passover outcomes, then first conditional visit timeline.',
'57b:1':'Reread cross-folio post-Passover bal-yachel clause and reversed visit/benefit deadlines with explicit later-visit permission.'}
if __name__=='__main__':a.save()
