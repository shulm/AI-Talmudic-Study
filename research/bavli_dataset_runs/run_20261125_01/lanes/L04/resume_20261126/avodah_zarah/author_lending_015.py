"""Three distinct Abaye/Rava explanations and the necessity of every case."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('avodah_zarah','Avodah Zarah','az.r015');a.agent_id='/root/avodah_continuation_2'
c=a.claim;q=a.question;e=a.e
parent='bb06c7afac53719485cdbc3d3c82732f762c6918e381430a03d01f0f76fbe7a4'
a.structure('lending',['6b:'+str(i) for i in range(7,13)],'Borrowing, lending and repayment: Abaye/Rava and necessity of the separate cases')
# These are individually read and authored cases, not semantic extraction rules.
answered=[]
for key,ref,lemma,premise,question,abaye,rava,label in [
 ('objects','6b:7','להשאילן ולשאול מהן כו\'','בשלמא להשאילן דקא מרווח להו','אבל לשאול מהן מעוטי קא ממעט להו','אמר אביי גזרה לשאול מהן אטו להשאילן','רבא אמר כולה משום דאזיל ומודה הוא','lending and borrowing objects'),
 ('money','6b:8','להלוותם וללוות מהן','בשלמא להלוותם משום דקא מרווח להו','אלא ללוות מהן אמאי','אמר אביי גזרה ללוות מהן אטו להלוותם','רבא אמר כולה משום דאזיל ומודה הוא','lending and borrowing money'),
 ('repay','6b:9','לפורען ולפרוע מהן כו\'','בשלמא לפורען משום דקא מרווח להו','אלא לפרוע מהן מעוטי ממעט להו','אמר אביי גזירה לפרוע מהן אטו לפורען','רבא אמר כולה משום דאזיל ומודה הוא','paying debts to them and collecting debts from them')]:
  c(key+'_lemma',ref,lemma,'The discussion quotes the Mishnah’s prohibition on '+label+'.',scope='Distinct quoted Mishnah clause')
  pc=c(key+'_premise',ref,premise,'The discussion accepts that giving the relevant benefit to them explains prohibition in the first direction.',scope='Premise in the '+label+' discussion; not imported as final resolution of6a:14')
  qc=q(key+'_q',ref,question,'Why is the reverse direction prohibited in the case of '+label+'?')
  ac=c(key+'_abaye',ref,abaye,'Abaye explains the reverse-direction prohibition as a decree on account of the first-direction prohibition.',candidates=['אביי'],scope='Separate source occurrence for '+label)
  rc=c(key+'_rava',ref,rava,'Rava explains both directions by the recipient going and thanking his deity.',candidates=['רבא'],scope='Separate source occurrence for '+label+'; not silently assigned to Rabbah')
  e(key+'_abaye_answer',ac,qc,'answer',ref);e(key+'_rava_answer',rc,qc,'answer',ref);answered.append(qc)
commerce=c('commerce','6b:10','דאי תנא לשאת ולתת עמהן משום דקא מרווח להו ואזיל ומודה','If only business dealings were taught, one could explain them by benefit leading to thanks.',mode='hypothetical',conditions=['only business dealings taught'],scope='First stage of necessity argument')
borrowallow=c('borrowallow','6b:10','אבל לשאול מהן דמעוטי קא ממעט להו שפיר דמי','One might then permit borrowing their objects because it diminishes what they hold.',mode='rejected',conditions=['hypothetical omission of borrowing-objects clause'],scope='Rejected inference, not local permission')
honor=c('honor','6b:11','ואי תנא לשאול מהן משום דחשיבא ליה מילתא ואזיל ומודה','If borrowing objects were specified, its prohibition could be explained by the importance the lender attaches to the request and subsequent thanks.',mode='hypothetical',conditions=['borrowing objects'],scope='Second stage of necessity argument')
fear=c('fear','6b:11','אבל ללוות מהן צערא בעלמא אית ליה אמר תוב לא הדרי זוזי','One might distinguish borrowing money because the lender worries that the money will not return.',mode='rejected',conditions=['hypothetical omission of borrowing-money clause'],scope='Hypothetical lender thought in rejected distinction, not an actual narrative person',composition='composite')
recover=c('recover','6b:12','ואי תנא ללוות מהן משום דקאמר בעל כרחיה מיפרענא והשתא מיהא אזיל ומודה','If borrowing money were specified, the lender could expect enforced recovery and give thanks now.',mode='hypothetical',conditions=['borrowing money'],scope='Third stage, reconstructed lender reasoning; not an event report',composition='composite')
loss=c('loss','6b:12','אבל ליפרע מהן דתו לא הדרי זוזי אימא צערא אית ליה ולא אזיל ומודה','One might then exclude collecting from them because the money will not return and the debtor would feel distress rather than give thanks.',mode='rejected',conditions=['hypothetical omission of collecting-debt clause'],scope='Rejected reason to permit collecting, not denial of the Mishnah’s prohibition',composition='composite')
need=c('need','6b:12','צריכא','The separate clauses are therefore all needed.',scope='Conclusion of the three-segment necessity argument')
e('commerce_support',commerce,need,'support','6b:10');e('borrowallow_support',borrowallow,need,'support','6b:10');e('honor_support',honor,need,'support','6b:11');e('fear_support',fear,need,'support','6b:11');e('recover_support',recover,need,'support','6b:12');e('loss_support',loss,need,'support','6b:12')
for row in a.rows:
 if row['id'] in answered:
  row['content']['answer_set_status']='partial';row['uncertainty'].append('Both source-present named explanations retained; no certification of exhaustive alternatives.')
a.save_window(['6b:'+str(i) for i in range(7,13)],'lending015.json','Original6b:7–12 reread with continuation through7a:11. All three Abaye/Rava occurrences preserved separately, objects/money/repayment directions retained, reconstructed lender motives confined to necessity argument, hypothetical permissions marked rejected, all eight passes recorded. Previous structural tails unchanged.',parent)
