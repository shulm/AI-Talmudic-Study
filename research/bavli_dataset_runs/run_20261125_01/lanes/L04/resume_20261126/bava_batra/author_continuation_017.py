"""Explicit reading of window reconstruction, divided inheritance and orphan receipt cases."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r017')
parent='95c61e5e4d60466f3ebb56f5fd491908d64e0f3320e901e9d7220beed5d46940'
assert r.sha(r.encoded(r.current(a.job)))==parent
c=a.claim;q=a.question;e=a.e
a.structure('rebuild',['7a:5','7a:6','7a:7'],'Neighbor light obstruction and rejected proposals to reconstruct the house')
a.structure('brothers',['7a:'+str(i) for i in range(8,15)]+['7b:1','7b:2'],'Divided inheritance, light access, valuation and preserved easements')
a.structure('receipt',['7b:3','7b:4','7b:5'],'Orphan debt document met by a receipt: preservation, collection and credibility')
c('wall_event','7a:5','ההוא גברא דהוה בני אשיתא אחורי כווי דחבריה','A man was building a wall behind his neighbor’s windows.',mode='narrative')
dark=c('dark','7a:5','קא מאפלת עלי','The window owner objects that the wall blocks his light.',scope='Litigant objection in this narrated case')
raise_=c('raise','7a:5','סכרנא לך הכא ועבידנא לך כווי לעיל מאשיתאי','The builder offers to close the existing windows and make new ones above his wall.',mode='proposal',composition='composite')
weak=c('weak','7a:5','קא מרעת ליה לאשיתאי','The window owner objects that this would weaken his wall.')
partial=c('partial','7a:5','סתרנא לך לאשיתך עד דוכתא דכווי ובנינא לה ועבידנא לך כווי בבנינא לעיל מאשיתאי','The builder offers to demolish to window level and rebuild with higher windows.',mode='proposal',composition='composite')
oldnew=c('oldnew','7a:5','אשיתא מתתאה עתיקא ומלעיל חדתא לא קיימא','The owner objects that a wall old below and new above will not stand.',conditions=['old lower wall and new upper wall'])
wholewall=c('wholewall','7a:6','סתרנא לה עד לארעא ובנינא לה ועבידנא לך כווי בגוה','The builder offers to demolish the entire wall and rebuild it with windows.',mode='proposal',composition='composite')
onewall=c('onewall','7a:6','חדא אשיתא חדתא בכוליה ביתא עתיקא לא קיימא','The owner objects that one new wall in an entirely old house will not stand.',conditions=['one new wall among old house walls'])
wholehouse=c('wholehouse','7a:6','סתרנא לה לכוליה ביתא ובנינא לך כווי בבנינא','The builder offers to demolish the whole house and rebuild it with windows.',mode='proposal',composition='composite')
homeless=c('homeless','7a:6','לית לי דוכתא למידר בה','The owner objects that he has nowhere to live during reconstruction.')
rent=c('rent','7a:6','אגירנא לך דוכתא','The builder offers to rent alternative accommodation.',mode='proposal')
effort=c('effort','7a:6','לא טרחנא','The owner refuses the trouble of moving.')
hama=c('hama','7a:6','אמר רב חמא בדין קא מעכב','Rav Hama rules that the owner legally prevents the proposed reconstruction.',candidates=['רב חמא'],scope='This narrated light-obstruction and reconstruction case')
for key,source,target,ref,rel in [('raise_reply',raise_,dark,'7a:5','answer'),('weak_obj',weak,raise_,'7a:5','objection'),('partial_reply',partial,weak,'7a:5','answer'),('oldnew_obj',oldnew,partial,'7a:5','objection'),('wholewall_reply',wholewall,oldnew,'7a:6','answer'),('onewall_obj',onewall,wholewall,'7a:6','objection'),('wholehouse_reply',wholehouse,onewall,'7a:6','answer'),('homeless_obj',homeless,wholehouse,'7a:6','objection'),('rent_reply',rent,homeless,'7a:6','answer'),('effort_obj',effort,rent,'7a:6','objection'),('hama_support',hama,effort,'7a:6','support')]:e(key,source,target,rel,ref)
repeat=q('repeat','7a:7','היינו הך והא תו למה לי','This resembles the previous case; why repeat it?')
store=c('store','7a:7','הא קמ"ל דאע"ג דלא משתמש אלא תיבנא ובי ציבי בעלמא','The additional case teaches that the owner may object even if he uses the building only for straw and wood.',conditions=['building used only for straw or wood storage'])
e('store_answer',store,repeat,'answer','7a:7');e('store_qualification',store,hama,'qualification','7a:7')
c('division_event','7a:8','הנהו בי תרי אחי דפלגי בהדי הדדי חד מטייה אספלידא וחד מטייה תרביצא','Two brothers divided their property: one received the אספלידא and the other the תרביצא.',mode='narrative',composition='composite',uncertainty=['Source property terms retained; no unverified architectural details imposed.'])
c('division_wall','7a:8','אזל ההוא דמטייה תרביצא וקא בני אשיתא אפומא דאספלידא','The recipient of the תרביצא built a wall at the opening of the אספלידא.',mode='narrative')
divdark=c('division_dark','7a:8','קא מאפלת עלי','The other brother objects that the new wall blocks his light.',scope='Second narrated case, divided inherited property')
own=c('own','7a:8','בדידי קא בנינא','The builder replies that he builds on his own property.')
divhama=c('division_hama','7a:8','אמר רב חמא בדין קאמר ליה','Rav Hama upholds the builder’s response.',candidates=['רב חמא'],scope='Divided inherited property case; not the earlier neighbor-window case')
e('own_answer',own,divdark,'answer','7a:8');e('divhama_support',divhama,own,'support','7a:8')
vineq=q('vineyard_q','7a:9','מאי שנא מהא דתניא','Ravina asks Rav Ashi how this differs from the vineyard/field division teaching.',candidates=['רבינא'])
vine=c('vineyard','7a:9',"שני אחין שחלקו אחד מהן נטל שדה כרם ואחד מהן נטל שדה לבן יש לו לבעל הכרם ד' אמות בשדה לבן שעל מנת כן חלקו",'When brothers divide a vineyard and a grain field, the vineyard recipient has four cubits in the grain field because they divided on that basis.',conditions=['one brother receives vineyard','other receives grain field'],scope='Quoted baraita in Ravina’s challenge')
e('vine_support',vine,vineq,'support','7a:9');e('vine_objection',vineq,divhama,'objection','7a:9')
valuation=c('valuation','7a:10','התם דעלו להדדי אבל הכא מאי דלא עלו להדדי','Rav Ashi initially distinguishes a division with mutual valuation there from one without it here.',candidates=['רב אשי'],naming_refs=['7a:9'],mode='challenged',composition='composite')
fools=q('fools','7a:10','וכי בשופטני עסקינן דהאי שקיל אספלידא והאי שקיל תרביצא ולא עלו להדדי','Could brothers receiving such different properties really have divided without valuation?')
materials=c('materials','7a:10','נהי דעלו להדדי דמי ליבני כשורי והודרי דמי אוירא לא עלו להדדי','The reply concedes valuation of bricks, beams and construction materials but excludes valuation of the air/light space.',candidates=['רב אשי'],naming_refs=['7a:9'],conditions=['valuation of construction materials','no valuation of air/light space'],composition='composite',scope='Refinement of Rav Ashi’s distinction, not denial of every valuation')
e('valuation_answer',valuation,vineq,'answer','7a:10');e('fools_objection',fools,valuation,'objection','7a:10');e('materials_answer',materials,fools,'answer','7a:10');e('materials_refine',materials,valuation,'qualification','7a:10')
nameq=q('name_q','7a:11','ולימא ליה מעיקרא אספלידא פלגת לי השתא משוית לי אידרונא','Can the brother object that he received an אספלידא but now it is made an אידרונא?')
name=c('name','7a:11','אמר רב שימי בר אשי שמא בעלמא פלג ליה','Rav Shimi bar Ashi answers that the division conveyed the property by its name.',candidates=['רב שימי בר אשי'])
e('name_answer',name,nameq,'answer','7a:11')
for key,quote,statement,cond in [('kor','האומר בית כור עפר אני מוכר לך אע"פ שאינו אלא לתך הגיעו שלא מכר לו אלא שמא והוא דמיתקרי בית כור','A sale called בית כור is fulfilled even with only a לתך when that is the property’s name.','property actually called בית כור'),('orchard','פרדס אני מוכר לך אע"פ שאין בו רמונים הגיעו שלא מכר לו אלא שמא והוא דמיתקרי פרדס','A sale called פרדס is fulfilled despite absence of pomegranates when that is its name.','property actually called פרדס'),('vines','כרם אני מוכר לך אע"פ שאין בו גפנים הגיעו שלא מכר לו אלא שמא והוא דמיתקרי כרמא','A sale called כרם is fulfilled despite absence of vines when that is its name.','property actually called כרם')]:
    x=c(key,'7a:12',quote,statement,conditions=[cond],scope='Quoted sale teaching used as analogy to division');e(key+'_analogy',x,name,'analogy','7a:12')
different=q('sale_difference','7a:13','מי דמי','Is a sale by name analogous to this division?')
sale=c('sale_name','7a:13','התם מצי אמר ליה מוכר ללוקח שמא זביני לך','In the sale the seller can say he sold by the name.',scope='Premise distinguishing sale from inheritance division')
father=c('father_use','7a:13','הכא מצי א"ל אדעתא דהכי פלגי דדאירנא ביה כי היכי דדרו אבהתן','In division the brother can argue that he divided intending to live there as their father had.',scope='Reconstructed litigant argument challenging the sale analogy')
e('sale_distinction',sale,name,'distinction','7a:13');e('father_objection',father,name,'objection','7a:13');e('different_objection',different,name,'objection','7a:13')
a.speech('continued_intro','7a:14','אמרו ליה',act='speech introduction continued on next page',uncertainty=['Named speakers and recipient appear in7b:1; this is not an independent anonymous claim.'])
neh=c('nehardea','7b:1','מר ינוקא ומר קשישא בריה דרב חסדא לרב אשי נהרדעי לטעמייהו','Mar Yenuka and Mar Kashisha, printed with בריה דרב חסדא, tell Rav Ashi that the Nehardeans follow their own position.',candidates=['מר ינוקא','מר קשישא בריה דרב חסדא'],naming_refs=['7a:14'],uncertainty=['Printed singular patronymic retained; no normalized genealogical assignment beyond source wording.'])
path=c('no_path','7b:1','דאמר ר"נ אמר שמואל האחין שחלקו אין להן לא דרך זה על זה','Rav Nahman transmits Shmuel: brothers who divide have no right of passage over one another’s property.',candidates=['שמואל'],chain=['רב נחמן','שמואל'],conditions=['brothers divided property'])
rights=[]
for key,quote,text in [('window','ולא חלונות זה על זה','window rights'),('ladder','ולא סולמות זה על זה','ladder rights'),('water','ולא אמת המים זה על זה','water-channel rights')]:
    rights.append(c('no_'+key,'7b:2',quote,'The transmitted Shmuel teaching denies '+text+' over the other brother’s property.',candidates=['שמואל'],chain=['רב נחמן','שמואל'],naming_refs=['7b:1'],conditions=['brothers divided property']))
fixed=c('fixed','7b:2','והזהרו בהן שהלכות קבועות הן','The transmitted teaching warns to preserve these rules because they are established halakhot.',candidates=['שמואל'],chain=['רב נחמן','שמואל'],naming_refs=['7b:1'])
rava=c('rava_rights','7b:2','ורבא אמר יש להן','Rava says the divided brothers do retain the listed rights.',candidates=['רבא'],conditions=['brothers divided property'],composition='composite',scope='Contrary position covering the preceding listed rights; no final resolution asserted')
for i,x in enumerate([path]+rights):e('rava_contrast'+str(i),rava,x,'distinction','7b:2');e('neh_support'+str(i),x,neh,'support','7b:2')
e('neh_answer',neh,father,'answer','7b:1')
c('orphan_event','7b:3','ההוא שטרא דיתמי דנפיק עליה תברא','A receipt was produced against a debt document belonging to orphans.',mode='narrative')
no_collect=c('no_collect','7b:3','אמר רב חמא אגבויי לא מגבינן ליה','Rav Hama says not to collect on this document.',candidates=['רב חמא'],conditions=['orphan debt document confronted by a receipt'])
preserve=c('preserve','7b:3','ומיקרע לא קרעינן ליה','Rav Hama says not to tear up the document.',candidates=['רב חמא'],conditions=['orphan debt document confronted by a receipt'])
receipt=c('receipt_reason','7b:3','דנפק תברא עליה','Collection is withheld because a receipt has been produced.',candidates=['רב חמא'])
grow=c('grow','7b:3','דכי גדלי יתמי דילמא מייתו ראיה ומרעי ליה','The document is preserved because when grown the orphans may produce evidence undermining the receipt.',candidates=['רב חמא'],conditions=['possible later evidence against receipt'])
e('receipt_support',receipt,no_collect,'support','7b:3');e('grow_support',grow,preserve,'support','7b:3')
law=q('law_q','7b:4','אמר ליה רב אחא בריה דרבא לרבינא הלכתא מאי','Rav Aha son of Rava asks Ravina what the halakha is.',candidates=['רב אחא בריה דרבא'])
rule=c('rule','7b:4','בכולהו הלכתא כרב חמא לבר מתברא','Ravina rules like Rav Hama in the preceding cases except the receipt case.',candidates=['רבינא'],scope='Local preceding Rav Hama cases; exception explicitly preserved')
witness=c('witness','7b:4','דסהדי בשקרי לא מחזקינן','Ravina reasons that witnesses are not presumed to be liars.',candidates=['רבינא'])
e('rule_answer',rule,law,'answer','7b:4');e('witness_support',witness,rule,'support','7b:4');e('rule_contrast',rule,preserve,'distinction','7b:4')
mar=c('mar','7b:5','מר זוטרא בריה דרב מרי אמר בהא נמי הלכתא כרב חמא','Mar Zutra son of Rav Mari rules like Rav Hama also in the receipt case.',candidates=['מר זוטרא בריה דרב מרי'])
timing=c('timing','7b:5','דאם איתא דתברא מעליא הוא איבעי ליה לאפוקי בחיי אבוהון','Mar Zutra reasons that a valid receipt should have been produced during their father’s lifetime.',candidates=['מר זוטרא בריה דרב מרי'],conditions=['receipt claimed valid'])
forged=c('forged','7b:5','ומדלא אפקיה שמע מינה זיופי זייפיה','Mar Zutra infers forgery from failure to produce it during the father’s lifetime.',candidates=['מר זוטרא בריה דרב מרי'],scope='Mar Zutra’s competing evidentiary inference; not independently verified historical forgery')
e('mar_contrast',mar,rule,'distinction','7b:5');e('timing_support',timing,forged,'support','7b:5');e('forged_support',forged,mar,'support','7b:5')
refs=['7a:'+str(i) for i in range(5,15)]+['7b:'+str(i) for i in range(1,6)]
for row in a.rows:
    if row['layer']=='claims':
        if row['content']['assertion_mode']=='narrative':row['content']['assertion_mode']='asserted'
        if row['content']['assertion_mode']=='proposal':row['content']['assertion_mode']='hypothetical'
    if row['layer']=='questions' and row['id'] in {'bb.r017.repeat.q','bb.r017.vineyard_q.q','bb.r017.fools.q','bb.r017.name_q.q','bb.r017.law_q.q'}:row['content']['answer_set_status']='partial'
a.save_window(refs,'continuation017b.json','Reread complete cases through7b:5 and context7b:6–16. Preserve every rebuilding offer/refusal, narrative litigants, valuation refinement, name-sale distinctions, cross-page speech, contrary property-right positions and receipt credibility dispute; no forced winner. Source-based omission pass over all eight layers.',parent)

