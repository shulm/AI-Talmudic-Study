"""Direct source reading12b:22–13a:5: inherited penalties and exact hypotheticals."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r034');c=a.claim;e=a.e
refs=['12b:22','12b:23']+['13a:'+str(i) for i in range(1,6)]
def q(*args,**kwargs):
 v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial';a.rows[-1]['uncertainty'].append('Exact local source reply only, not exhaustive alternative inventory or certification.');return v
a.structure('inheritance',refs,'Whether a deliberate-work penalty passes to heirs; conditional analogies and distinct impurity case')
question=q('question','12b:22','בעי מיניה רבי ירמיה מרבי זירא כוון מלאכתו במועד ומת מהו שיקנסו בניו אחריו','Rabbi Yirmeya asks Rabbi Zeira whether a man’s sons are penalized after his death for work he deliberately scheduled for the festival.',candidates=['רבי ירמיה'])
a.speech('conditional','12b:23','אם תימצי לומר',act='conditional premise introducing cross-page comparison',uncertainty=['This is not an independent affirmative ruling; it introduces the following hypothetical.'])
ear=c('ear','13a:1','צרם אזן בכור קנסו בנו אחריו משום דאיסורא דאורייתא','If a penalty for mutilating the firstborn’s ear passes to the son, that could be because the offense is of Torah law.',mode='hypothetical',conditions=['conditional assumption introduced at12b:23'],scope='Conditional comparison; not an adjudicated ruling here')
slave=c('slave','13a:2','ואם תמצי לומר מכר עבדו לעובד כוכבים ומת קנסו בנו אחריו משום דכל יומא מפקע ליה ממצות','If a penalty for selling a slave to an idolater passes to the son after death, that could be because each day the slave is removed from commandments.',mode='hypothetical',conditions=['conditional assumption'],scope='Second hypothetical comparison, not an asserted inheritance rule',composition='composite')
which=q('which','13a:3','הכא מאי גברא קניס רבנן והא ליתיה או דלמא ממונא קניס רבנן והא איתיה','In the festival case, did the sages penalize the person, now absent, or the property, still present?',composition='composite')
cleared=c('cleared','13a:4','שדה שנתקווצה בשביעית תזרע למוצאי שביעית','A field cleared of thorns during the sabbatical year may be sown afterward.',scope='Quoted precedent; no unstated permissible method imported')
improved=c('improved','13a:4','נטייבה או נדיירה לא תזרע למוצאי שביעית','If improved or manured by penning, the field may not be sown afterward.',composition='composite',scope='Contrasting quoted precedent')
son=c('son','13a:4',"ואמר ר' יוסי בר חנינא נקטינן הטיבה ומת בנו זורעה",'Rabbi Yose bar Hanina says that if the man improved the field and died, his son may sow it.',candidates=['רבי יוסי בר חנינא'],role='quoted_authority',conditions=['father improved the field and died'])
person=c('person','13a:4','אלמא לדידיה קנסו רבנן לבריה לא קנסו רבנן','The inference is that the sages penalized him but not his son.',scope='Anonymous inference from the cited sabbatical-year precedent')
festival=c('festival','13a:4','ה"נ לדידיה קנסו רבנן לבריה לא קנסו רבנן','The same distinction is applied here: the penalty applies to him and not his son.',conditions=['festival work deliberately scheduled by deceased father'],scope='Reply in Rabbi Zeira’s exchange; anonymous logical application distinguished from quoted Yose bar Hanina')
e('son_person',son,person,'support','13a:4');e('person_analogy',person,festival,'analogy','13a:4');e('festival_answer',festival,question,'answer','13a:4');e('which_answer',festival,which,'answer','13a:4')
impure=c('impure','13a:5','אמר אביי נקטינן טימא טהרותיו ומת לא קנסו בנו אחריו','Abaye says that when a person rendered the pure items impure and died, his son is not penalized after him.',candidates=['אביי'],conditions=['person rendered pure items impure and died'],scope='Separate case; no invented ownership history beyond the printed formulation')
why=q('why','13a:5','מאי טעמא','What is the reason?')
unseen=c('unseen','13a:5','היזק שאינו ניכר לא שמיה היזק','Imperceptible damage is not legally called damage.',scope='Reason stated in this local argument, not an unqualified survey of all opinions')
penalty=c('penalty','13a:5','לדידיה קנסו רבנן לבריה לא קנסו רבנן','The sages penalized the offender but not his son.',scope='Explanation for the separate impurity case')
e('unseen_answer',unseen,why,'answer','13a:5');e('penalty_reason',penalty,impure,'support','13a:5')
a.save_window(refs,'resume_moed_katan_penalties034.json','Read12b:22–13a:5 and continuation13a–14a. Retain cross-page conditional marker, two hypothetical analogies rather than positive rulings, person/property question, field distinctions, named authority versus anonymous application, and Abaye’s distinct imperceptible-damage explanation.','475643d0aa2cf55b6476d5df11d6e5d245a516727547c348590f8ca8becf3ce9')
