"""Manual jubilee dispute and explicit Rav correction of Meir/Yosei attribution."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r064.';a.OUTPUT='continuation_064.json'
c=a.c;e=a.edge;q=b.q
a.structure('jubilee',['61a:'+str(i) for i in range(3,8)],'Fiftieth-year counting dispute with reciprocal scriptural challenges')
a.structure('reverse',['61a:8']+['61b:'+str(i) for i in range(1,5)],'Ambiguity attribution contradiction and explicit named reversal')
jubileeq=q('jubileeq','61a:3',None,'For a wine vow lasting a jubilee, is the fiftieth year counted with the preceding or following fifty-year period?')
dispute=c('dispute','61a:4','ת"ש דתניא פלוגתא דרבי יהודה ורבנן','The answer presents this as the dispute between Rabbi Yehuda and the sages.',scope='Question resolved by identifying competing authorities, not selecting a final halakhic winner')
sages=c('sages','61a:4','(ויקרא כה, י) וקדשתם את שנת החמשים שנה שנת החמשים אתה מונה ואי אתה מונה שנת חמשים ואחת מכאן אמרו יובל אינו עולה למנין שבוע','The sages derive that jubilee does not count toward the seven-year cycle from sanctifying the fiftieth year and not counting a fifty-first.',holder='רבנן',composition='composite',scope='Quoted counting derivation and conclusion; fiftieth year belongs to completed jubilee period')
yehuda=c('yehuda','61a:4','רבי יהודה אומר יובל עולה למנין שבוע','Rabbi Yehuda counts jubilee toward the seven-year cycle.',holder='רבי יהודה',scope='Fiftieth year also begins the following count')
sixq=q('sixq','61a:5',None,'The sages object to Yehuda that the verse promises six sowing years, whereas his count leaves only five.')
fourq=q('fourq','61a:6',None,'Yehuda counters that the sages’ count makes the promised three-year crop support cover four years.',voice='רבי יהודה')
other=c('other','61a:7','אלא איכא לאוקמה בשאר שני שבוע דילי נמי איכא לאוקמה בשאר שני שבוע','Yehuda concludes that just as their verse can concern other sabbatical cycles, so can his six-year verse.',holder='רבי יהודה',composition='composite',scope='Reciprocal qualification avoids both objections; no retraction of counting dispute')
e('dispute.answer',dispute,jubileeq,'answer','61a:4');e('yehuda.objection',yehuda,sages,'objection','61a:4');e('other.answer',other,sixq,'answer','61a:7');e('other.answerfour',other,fourq,'answer','61a:7')
avoid=c('avoid','61a:8','למימרא דרבי מאיר סבר לא מעייל איניש נפשיה','The initial deduction from the printed Passover Mishnah makes Rabbi Meir hold that people do not place themselves in doubt.',holder='רבי מאיר',mode='rejected',scope='Cross-folio sentence and provisional attribution, reversed below',extra=[('61b:1',('לספיקא',0))])
enter=c('enter','61b:1','ורבי יוסי סבר מעייל איניש נפשיה לספיקא','The corresponding initial deduction makes Rabbi Yosei hold that people do enter ambiguity.',holder='רבי יוסי',mode='rejected',scope='Provisional assignment contradicted by daughters Mishnah and reversed below')
contradict=q('contradict','61b:2','ורמינהי','How can those ambiguity positions fit the daughters-betrothal dispute?')
daughters=c('daughters','61b:2','מי שיש לו שתי כיתי בנות משתי נשים ואמר קדשתי את בתי הגדולה ואיני יודע אם גדולה שבגדולות אם גדולה שבקטנות ואם קטנה שבגדולות שהיא גדולה מן הגדולה שבקטנות','A father with two sets of daughters from two wives says he betrothed his elder daughter but cannot identify whether he meant the eldest of the older set, eldest of the younger set, or youngest of the older set who exceeds the younger set’s eldest.',composition='composite',scope='All three explicit candidate descriptions retained; no named daughter invented')
meir=c('meir','61b:2','כולן אסורות דברי ר"מ חוץ מן הקטנה שבקטנות','Rabbi Meir prohibits all candidate daughters except the youngest of the younger set.',holder='רבי מאיר',scope='Marriage-status uncertainty in quoted Mishnah, showing broader ambiguity than provisional Passover attribution')
yosei=c('yosei','61b:3',None,'Rabbi Yosei permits all except the eldest of the older set.',holder='רבי יוסי',scope='Quoted Mishnah narrows the ambiguous elder designation')
reverse=c('reverse','61b:4','אמר רבי חנינא בר אבדימי אמר רב מוחלפת השיטה','Rabbi Hanina bar Avdimi reports Rav that the positions are reversed.',holder='רב',scope='Explicit attribution correction of Passover positions, supported by following fixed-time baraita; Rav himself, not transmitter')
fixedMeir=c('fixedMeir','61b:4','והתניא זה הכלל כל שזמנו קבוע ואמר עד לפני ר"מ אומר עד שיצא','The supporting baraita assigns Rabbi Meir the departure endpoint for עד לפני with a fixed-time event.',holder='רבי מאיר',scope='Corrected final named assignment, distinct from rejected printed60a7')
fixedYosei=c('fixedYosei','61b:4','ורבי יוסי אומר עד שיגיע','The baraita assigns Rabbi Yosei the arrival endpoint.',holder='רבי יוסי',scope='Corrected final named assignment for same fixed-time formula')
e('meir.objection',meir,avoid,'objection','61b:2');e('yosei.objection',yosei,enter,'objection','61b:3');e('reverse.answer',reverse,contradict,'answer','61b:4');e('reverse.correctavoid',reverse,avoid,'correction','61b:4');e('reverse.correctenter',reverse,enter,'correction','61b:4');e('fixedMeir.correction',fixedMeir,'nd.r063.meir.c','correction','61b:4');e('fixedYosei.correction',fixedYosei,'nd.r063.yosei.c','correction','61b:4');e('fixedMeir.support',fixedMeir,reverse,'support','61b:4');e('fixedYosei.support',fixedYosei,reverse,'support','61b:4')
a.notes={
'61a:3':'Reread jubilee vow question and both fiftieth-year allocation alternatives.',
'61a:4':'Reread explicit Yehuda/sages dispute identification, sages fiftieth/not-fifty-first derivation and opposite cycle-counting positions.',
'61a:5':'Reread sages six-versus-five-sowing-years challenge to Yehuda.',
'61a:6':'Reread Yehuda three-versus-four-sustenance-years counterchallenge.',
'61a:7':'Reread reciprocal other-cycle qualification; no final winner inferred.',
'61a:8':'Reread initial Meir no-ambiguity deduction continuing next folio; marked rejected after Rav reversal.',
'61b:1':'Reread completion of Meir claim and opposite provisional Yosei ambiguity claim.',
'61b:2':'Reread contradiction, both daughter sets, all three explicit candidate relations and Meir exception.',
'61b:3':'Reread Yosei opposite broad permission with eldest-of-older-set exception.',
'61b:4':'Reread Hanina bar Avdimi transmission of Rav’s מוחלפת השיטה and supporting fixed-event baraita assigning Meir departure/Yosei arrival; correction edges point to original rejected records.'}
if __name__=='__main__':a.save()
