"""Debt payment and lost property: both unassigned Ami/Asi versions and final difficulty."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r034.';a.OUTPUT='continuation_034.json'
c=a.c;q=b.q;e=a.edge
a.structure('debt',['33a:8','33a:9','33a:10']+['33b:'+str(i) for i in range(1,6)],'Paying obligations under benefit restriction: Hanan and alternative construction')
a.structure('lost',['33b:6','33b:7']+['34a:'+str(i) for i in range(1,8)],'Returning property: two anonymous Ami/Asi transmissions and fee challenges')
shekel=c('shekel','33a:8','המודר הנאה מחבירו שוקל לו את שקלו','The Mishnah permits paying the restricted person’s shekel obligation.',scope='Benefit-vow allowance examined below')
pay=c('pay','33a:8','ופורע את חובו','It permits paying his debt.',scope='Precise debt arrangement disputed below')
returnc=c('return','33a:8','ומחזיר לו את אבידתו','It permits returning his lost property.',scope='Direction of benefit restriction debated in two versions')
fee=c('fee','33a:8','מקום שנוטלין עליה שכר תיפול הנאה להקדש','Where a fee is taken for return, the benefit is assigned to consecration.',conditions=['customary return fee'],scope='Application tested against both lost-property versions')
lion=c('lion','33a:9',None,'The discussion infers that merely driving away a lion is allowed.',scope='Metaphor for removing a threatened loss rather than supplying direct benefit')
who=q('who','33a:10','מאן תנא','Which tanna permits this?')
hoshaya=c('hoshaya','33a:10','אמר רב הושעיא זו','Rav Hoshaya identifies the teaching as Hanan’s.',extra=[('33b:1',None)],holder='רב הושעיא',scope='Cross-page authorial identification')
rava=c('rava','33b:2',None,'Rava permits a construction agreeing with everyone, where the loan was given on condition not to demand repayment.',holder='רבא',conditions=['debt given על מנת שלא לפרוע'],scope='Exact unusual condition retained; not an ordinary immediately collectible debt')
e('hoshaya.answer',hoshaya,who,'answer','33b:1');e('rava.answer',rava,who,'answer','33b:2')
hananq=q('hananq','33b:3','מאי חנן','What teaching of Hanan is meant?')
wife=c('wife','33b:3','דתנן מי שהלך למדינת הים ועמד אחד ופירנס את אשתו','The cited case is one who goes overseas while another supports his wife.',scope='Voluntary support by a third party')
hanan=c('hanan','33b:3','חנן אמר איבד את מעותיו','Hanan says the supporter has lost his money.',holder='חנן',scope='No reimbursement entitlement under this cited case')
priests=c('priests','33b:4','נחלקו עליו בני כהנים גדולים ואמרו ישבע כמה הוציא ויטול','The sons of high priests disagree and allow recovery upon swearing to the amount spent.',holder='בני כהנים גדולים',conditions=['oath to expenditure amount'])
dosa=c('dosa','33b:4','אמר רבי דוסא בן הרכינס כדבריהם','Rabbi Dosa ben Harkinas agrees with the sons of high priests.',holder='רבי דוסא בן הרכינס',scope='Explicit endorsement of reimbursement view')
zakai=c('zakai','33b:4','אמר רבן יוחנן בן זכאי יפה אמר חנן הניח מעותיו על קרן הצבי','Rabban Yohanan ben Zakkai endorses Hanan, describing the money as placed on a deer’s horn.',holder='רבן יוחנן בן זכאי',scope='Metaphor for unrecoverable voluntary expenditure')
e('hanan.answer',hanan,hananq,'answer','33b:3');e('priests.objection',priests,hanan,'objection','33b:4');e('dosa.support',dosa,priests,'support','33b:4');e('zakai.support',zakai,hanan,'support','33b:4')
universal=c('universal','33b:5','רבא לא אמר כרב הושעיא דקא מוקים לה למתניתין כדברי הכל','Rava does not adopt Hoshaya’s attribution because he can make the Mishnah agree with all.',scope='Anonymous explanation of Rava’s methodological preference')
decree=c('decree','33b:5','רב הושעיא לא אמר כרבא גזירה שלא ליפרע משום ליפרע','Hoshaya does not adopt Rava’s construction because of a decree from a noncollection case to a collection case.',scope='Source’s explanation of Hoshaya’s rejection; printed שלא ליפרע/ליפרע distinction retained')
e('decree.objection',decree,rava,'objection','33b:5')
names=c('names','33b:6','פליגי בה רבי אמי ורבי אסי חד אמר','Rabbi Ami and Rabbi Asi dispute the return rule, but the first view is not identified by name.',scope='חד אמר assignment left unresolved; alternative version34a:4 also leaves names unassigned',uncertainty=['No attribution by order of names.'])
first=c('first','33b:6','לא שנו אלא בשנכסי מחזיר אסורין על בעל אבידה דכי מהדר ליה מידעם דנפשיה קא מהדר ליה','In the first version one view permits return only when the finder’s property is forbidden to the owner, because the finder returns the owner’s own property.',conditions=['finder property prohibited to owner'],scope='First unnamed Ami/Asi view, first transmission')
reverse=c('reverse','33b:6','אבל נכסי בעל אבידה אסורין על מחזיר לא קא מהדר ליה דקא מהני ליה פרוטה דרב יוסף','That view prohibits return in the opposite restriction direction because the finder receives the benefit called Rav Yosef’s peruta.',conditions=['owner property prohibited to finder'],scope='Same unnamed view; exact technical benefit retained without unquoted expansion')
second=c('second','33b:7',None,'The other view permits return even when the owner’s property is forbidden to the finder, because Rav Yosef’s peruta benefit is uncommon.',conditions=['owner property prohibited to finder'],scope='Second unnamed view, first transmission')
e('second.objection',second,reverse,'objection','33b:7')
fits=c('fits','34a:1',None,'The fee-to-consecration clause is presented as fitting the view permitting return even when the owner’s property is forbidden to the finder.',scope='Concession preceding challenge to narrower view')
feeq=q('feeq','34a:2',None,'For the view prohibiting return when the owner’s property is forbidden to the finder, why would the benefit go to consecration?')
one=c('one','34a:3',None,'The answer says the clause is taught about one case.',scope='Compressed אחדא קתני answer preserved; does not explicitly enumerate both restriction directions')
e('one.answer',one,feeq,'answer','34a:3')
alt=c('alt','34a:4','איכא דמתני לה בהאי לישנא פליגי בה רבי אמי ורבי אסי חד אמר','An explicitly alternate transmission again reports an unnamed first view in the Ami/Asi dispute.',scope='Not conflated with first transmission or assigned by name order')
altFirst=c('altFirst','34a:4','לא שנו אלא בשנכסי בעל אבידה אסורין על מחזיר ומשום פרוטה דרב יוסף לא שכיח','In the alternate version one view permits only when the owner’s property is forbidden to the finder, treating Rav Yosef’s peruta benefit as uncommon.',conditions=['owner property prohibited to finder'],scope='First unnamed view, alternate transmission')
altNo=c('altNo','34a:4','אבל נכסי מחזיר אסורים על בעל אבדה לא מהדר ליה משום דקא מהני ליה','That alternate first view prohibits return when the finder’s property is forbidden to the owner, because return benefits the owner.',conditions=['finder property prohibited to owner'],scope='Reversed restrictive branch, distinct from33b:6')
altYes=c('altYes','34a:5',None,'The alternate second view permits even that direction because the finder returns the owner’s own property.',conditions=['finder property prohibited to owner'],scope='Second unnamed view, alternate transmission')
e('altYes.objection',altYes,altNo,'objection','34a:5')
altFits=c('altFits','34a:6',None,'The alternate fee discussion treats the clause as fitting permission when the finder’s property is prohibited to the owner.',scope='Concession specific to second transmission')
hard=a.q('hard','34a:7','אלא למאן דאמר בשנכסי מחזיר אסורין ולא מהדר היכי מתרץ מקום','How does the alternate restrictive view explain the customary-fee clause?')
next(x for x in a.records if x['id']==hard)['uncertainty'].append('The text ends קשיא; this version’s fee challenge is not resolved here.')
difficulty=c('difficulty','34a:7','קשיא','The source leaves the challenge as a difficulty.',mode='unresolved',scope='Explicit local outcome, not a named-speaker identification or definitive refutation')
e('difficulty.unresolved',difficulty,hard,'unresolved_outcome','34a:7')
a.notes={
'33a:8':'Reread separate shekel, debt, lost-property permissions and customary-fee consecration clause.',
'33a:9':'Reread removal-of-lion metaphor as inferred benefit classification.',
'33a:10':'Reread author question and Hoshaya introduction spanning next page.',
'33b:1':'Reread Hanan identification completing preceding statement.',
'33b:2':'Reread Rava all-views construction and precise שלא לפרוע condition.',
'33b:3':'Reread Hanan-source question, overseas-wife-support case and loss-of-money position.',
'33b:4':'Reread priestly sons disagreement, Dosa endorsement and Yohanan ben Zakkai endorsement of Hanan.',
'33b:5':'Reread each amora’s reason for not adopting the other’s approach.',
'33b:6':'Reread first Ami/Asi version, both restriction directions and Rav Yosef peruta rationale; no name-order assignment.',
'33b:7':'Reread second unnamed permissive view and infrequency rationale.',
'34a:1':'Reread fee-clause fit under broader first-version allowance.',
'34a:2':'Reread first-version fee challenge to narrower return permission.',
'34a:3':'Reread compressed one-case answer without inventing unstated expanded wording.',
'34a:4':'Reread explicit alternative version, reversed restrictive direction and its own rationale.',
'34a:5':'Reread alternate second view own-property-return answer.',
'34a:6':'Reread fee-clause concession in alternate version.',
'34a:7':'Reread alternate restrictive-view challenge and explicit קשיא, retained unresolved.'}
if __name__=='__main__':a.save()
