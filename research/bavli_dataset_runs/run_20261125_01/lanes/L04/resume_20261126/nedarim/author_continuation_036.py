"""Priestly agency proof attempts and consent for offerings; rejected analogies retained."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r036.';a.OUTPUT='continuation_036.json'
c=a.c;q=b.q;e=a.edge
a.structure('agency',['35b:'+str(i) for i in range(1,9)]+['36a:'+str(i) for i in range(1,6)],'Priestly agency under benefit restriction: inconclusive offering proofs')
a.structure('consent',['36a:'+str(i) for i in range(6,13)],'Consent, impaired capacity and children’s Paschal participation')
a.structure('lemma',['36a:13'],'Return to teruma Mishnah lemma')
teruma=c('teruma','35b:1','ותורם את תרומתו ומעשרותיו לדעתו','The Mishnah allows separating teruma and tithes לדעתו.',scope='Whose awareness/consent is meant remains for36b discussion; exact term retained')
birds=c('birds','35b:1','ומקריב עליו קיני זבין קיני זבות קיני יולדות חטאות ואשמות','It permits offering bird pairs for zavim, zavot and women after childbirth, and sin/guilt offerings on his behalf.',composition='composite',scope='Printed list later limited to offerings completing ritual purification')
teach=c('teach','35b:1','ומלמדו מדרש הלכות ואגדות','It permits teaching him midrash, halakhot and aggadot.',composition='composite',scope='Benefit-restriction setting; fee rationale discussed later')
bible=c('bible','35b:1','אבל לא ילמדנו מקרא','It prohibits teaching him Scripture.',scope='Mishnah distinction, later explanation not yet resolved here')
children=c('children','35b:1','אבל מלמד הוא את בניו ואת בנותיו מקרא','It permits teaching Scripture to his sons and daughters.',composition='composite',scope='Children explicitly include both sexes')
agency=a.q('agency','35b:2','איבעיא להו הני כהני שלוחי דידן הוו או שלוחי דשמיא','Are priests agents of us or agents of Heaven?')
next(x for x in a.records if x['id']==agency)['uncertainty'].append('Both proof attempts are deflected in this continuation; no final agency resolution is supplied here.')
ours=c('ours','35b:2','אי אמרת דשלוחי דידן הוו הא מהני ליה ואסור','If priests are our agents, performing the service benefits the restricted person and is prohibited.',mode='conditional',conditions=['human agency model'])
heaven=c('heaven','35b:2','ואי אמרת שלוחי דשמיא שרי','If priests are Heaven’s agents, the service is permitted.',mode='conditional',conditions=['divine agency model'])
proof=c('proof','35b:3',None,'The first proof invokes the Mishnah’s permitted offerings, arguing that human agency would confer prohibited benefit.',mode='challenged',scope='Proposed inference to divine agency, deflected by special offering class')
special=c('special','35b:4','וליטעמיך ליתני מקריב עליו קרבנות אלא מחוסרי כפרה שאני','The reply distinguishes those lacking completion of purification; otherwise the Mishnah should have allowed offerings generally.',scope='Deflection of broad agency inference')
yohanan=c('yohanan','35b:4','דאמר רבי יוחנן הכל צריכין דעת חוץ ממחוסרי כפרה','Rabbi Yohanan requires awareness for all offerings except those completing purification.',holder='רבי יוחנן',scope='Class-specific consent exception')
minor=c('minor','35b:4','שהרי אדם מביא קרבן על בניו ועל בנותיו הקטנים שנאמר זאת תורת הזב (ויקרא טו, לב) בין גדול בין קטן','The support is a person’s offering for minor sons and daughters, deriving adult/minor inclusion from זאת תורת הזב.',composition='composite',scope='Source’s derivation supporting exception')
e('proof.support',proof,agency,'support','35b:3');e('special.correction',special,proof,'correction','35b:4');e('minor.support',minor,yohanan,'support','35b:4')
birthq=q('birthq','35b:5',"אלא מעתה לרבי יוחנן זאת תורת היולדת וגו' (ויקרא יג, יב) בין קטנה ובין גדולה קטנה בת לידה היא",'Would the analogous childbirth formula include a minor, and is a minor capable of childbirth?',conditions=['printed citation ויקרא יג, יב retained without correction'])
baraita=c('baraita','35b:5','והא תני רב ביבי קמיה דרב נחמן שלוש נשים משמשות במוך קטנה ומעוברת ומניקה קטנה שמא תתעבר ותמות','A baraita taught by Rav Bibi before Rav Nahman lists minor, pregnant and nursing women in a contraceptive context, and cites danger of pregnancy and death for a minor.',composition='composite',scope='Ancient source premise in textual argument, not contemporary medical advice; only the minor rationale is stated here')
capacity=c('capacity','35b:6',None,'The childbirth formula instead includes women with or without mental capacity, since a man may bring an offering for his wife lacking capacity.',composition='composite',scope='Answer redirects the adult/minor analogy to capacity categories')
yehuda=c('yehuda','35b:7',None,'The explanation invokes Rabbi Yehuda: a man brings a wealthy-person offering for his wife and all offerings she owes.',holder='רבי יהודה',composition='composite',scope='Specific support obligation, not an unrestricted exception for every offering without awareness')
document=c('document','35b:8',None,'The support is the written undertaking of responsibility for obligations she had from before.',scope='Quoted marital undertaking rationale')
e('capacity.answer',capacity,birthq,'answer','35b:6');e('yehuda.support',yehuda,capacity,'support','35b:7');e('document.support',document,yehuda,'support','35b:8')
shimi=c('shimi','36a:1',None,'Rav Shimi bar Abba objects from a teaching allowing a priest to sprinkle his sin-offering and guilt-offering blood.',scope='Second offering proof against human agency under benefit restriction')
leper=c('leper','36a:2',None,'The answer specifies a metzora’s sin/guilt offerings and derives adult/minor inclusion from זאת תהיה תורת המצורע.',composition='composite',scope='Again restricts proof to purification-completing offerings')
e('leper.correction',leper,shimi,'correction','36a:2')
piggul=c('piggul','36a:3','תנן (משנה גיטין ה, ד) הכהנים שפיגלו במקדש מזידין חייבין הא שוגגין פטורין','The quoted Mishnah makes priests liable for deliberately causing piggul, with inadvertent actors inferred exempt.',composition='composite',scope='Liability to compensate distinguished from ritual effectiveness')
effective=c('effective','36a:3','אלא שפיגולן פיגול','The discussion infers that their piggul nevertheless takes effect.',scope='Even where compensation liability is absent')
piggulq=q('piggulq','36a:4',None,'If priests are human agents, why does piggul take effect when the owner authorized proper service rather than wrongdoing?')
verse=c('verse','36a:5',None,'The reply makes piggul a special scriptural case from לא יחשב לו, applying regardless.',scope='Deflects agency proof through local verse, not general agency resolution')
e('verse.answer',verse,piggulq,'answer','36a:5');e('verse.unresolved',verse,agency,'unresolved_outcome','36a:5')
repeat=c('repeat','36a:6','גופא אמר רבי יוחנן הכל צריכין דעת חוץ ממחוסר כפרה שהרי אדם מביא קרבן על בניו ועל בנותיו הקטנים','The discussion repeats Rabbi Yohanan’s awareness rule and minor-child purification exception.',holder='רבי יוחנן',composition='composite',scope='Distinct return to cited rule')
fatq=q('fatq','36a:6','אלא מעתה יביא אדם חטאת חלב על חבירו שכן אדם מביא על אשתו שוטה כרבי יהודה  אלמה אמר רבי אלעזר הפריש חטאת חלב על חבירו לא עשה כלום?','Could one then bring a forbidden-fat sin offering for another by analogy with the incapacitated wife, despite Rabbi Elazar’s statement that such designation accomplishes nothing?')
incap=c('incap','36a:7',None,'If the wife ate while lacking capacity, she is not subject to an offering obligation.',conditions=['consumption while incapacitated'],scope='First branch showing wife analogy inapplicable')
later=c('later','36a:8',None,'If she ate while capable and later lost capacity, the cited Yohanan tradition says an offering designated before incapacity remains invalid even after recovery because once rejected it stays rejected.',holder='רבי יוחנן',composition='composite',scope='Yirmeya via Abbahu transmits rejection principle; second branch of failed wife analogy')
a.add('later.chain','attributions',dict(surface='אמר רבי ירמיה אמר רבי אבהו אמר רבי יוחנן',role='transmitter',candidates=['רבי ירמיה','רבי אבהו'],scope=later,transmission_chain=['רבי ירמיה','רבי אבהו','רבי יוחנן']),[a.ev('36a:8','אמר רבי ירמיה אמר רבי אבהו אמר רבי יוחנן')],[later])
e('incap.answer',incap,fatq,'answer','36a:7');e('later.answer',later,fatq,'answer','36a:8')
passoverq=q('passoverq','36a:9',None,'Could one similarly designate another’s Paschal offering by analogy with minor children, despite Rabbi Elazar’s no-effect ruling?')
zeira=c('zeira','36a:10',None,'Rabbi Zeira says household-lamb participation of minors is not a Torah-level requirement.',holder='רבי זירא',scope='Distinguishes children’s participation from another adult’s obligatory offering')
e('zeira.answer',zeira,passoverq,'answer','36a:10')
howq=q('howq','36a:11','וממאי','How is that established?')
race=c('race','36a:11','מדתנן (משנה פסחים ח, ג) האומר לבניו הריני שוחט את הפסח על מי שיעלה מכם ראשון לירושלים כיון שהכניס ראשון ראשו ורובו זכה בחלקו ומזכה את אחיו עמו','A cited Mishnah awards the first child entering Jerusalem head-and-majority a share, together with siblings, after the father’s first-arrival declaration.',composition='composite',scope='Source’s incentive arrangement, not winner’s exclusive entitlement')
meat=c('meat','36a:11','ואי אמרת שה לבית דאורייתא על בישרא קאי ומזכי להו','If household participation were Torah-required, this would allocate a share only when it is already meat.',mode='hypothetical',scope='Timing argument against treating the children’s allocation as mandatory Torah registration')
purposeq=q('purposeq','36a:12','אלא למה להו דאמר להון אבוהון','Why then did the father make the declaration?')
urge=c('urge','36a:12','כדי לזרזן במצות','It was to encourage their diligence in commandments.',scope='Stated purpose of first-arrival arrangement')
daughters=c('daughters','36a:12','תניא נמי הכי מעשה היה וקדמו בנות לבנים ונמצאו בנות זריזות ובנים שפלים','A corroborating story reports daughters arriving before sons, portraying daughters as diligent and sons as lagging in that incident.',composition='composite',scope='Particular source narrative, not an essential claim about sexes')
e('race.answer',race,howq,'answer','36a:11');e('meat.support',meat,zeira,'support','36a:11');e('urge.answer',urge,purposeq,'answer','36a:12');e('daughters.support',daughters,urge,'support','36a:12')
a.add('lemma.u','utterances',dict(textual_voice='anonymous textual citation',discourse_role='Mishnah lemma repeated',composition='atomic'),[a.ev('36a:13')])
a.add('lemma.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'lemma.u',transmission_chain=[]),[a.ev('36a:13')],[a.PREFIX+'lemma.u'])
a.notes={
'35b:1':'Reread teruma/tithes consent wording, all offering classes and adult/children teaching distinctions.',
'35b:2':'Reread priestly agency question and both conditional benefit outcomes; left overall question unresolved after deflected proofs.',
'35b:3':'Reread first Mishnah-based proof attempt.',
'35b:4':'Reread purification exception, Yohanan consent rule and both-sex minor derivation.',
'35b:5':'Reread childbirth/minor objection, printed anomalous reference unchanged and Bibi/Nahman baraita as ancient source premise.',
'35b:6':'Reread capacity-based childbirth interpretation and wife-offering example.',
'35b:7':'Reread Yehuda wealthy-wife/all-owed-offerings obligation.',
'35b:8':'Reread written undertaking quotation supporting obligation.',
'36a:1':'Reread Shimi bar Abba sin/guilt blood proof.',
'36a:2':'Reread metzora-specific deflection and adult/minor derivation.',
'36a:3':'Reread intentional/inadvertent compensation distinction and ritual-effect inference.',
'36a:4':'Reread agency counterfactual and proper-service authorization objection.',
'36a:5':'Reread special piggul verse deflection; no general agency resolution inferred.',
'36a:6':'Reread repeated Yohanan rule and forbidden-fat offering challenge citing Rabbi Elazar.',
'36a:7':'Reread consumption-while-incapacitated branch and absent offering obligation.',
'36a:8':'Reread later-incapacity/recovery branch and full Yirmeya/Abbahu/Yohanan chain.',
'36a:9':'Reread Paschal offering analogy and Elazar no-effect challenge.',
'36a:10':'Reread Zeira non-Torah-level minor-household participation distinction.',
'36a:11':'Reread evidentiary question, first-child/siblings allocation and already-meat timing argument.',
'36a:12':'Reread purpose question, diligence answer and particular daughters-before-sons narrative.',
'36a:13':'Reread teruma lemma as textual citation; no new legal claim invented.'}
if __name__=='__main__':a.save()
