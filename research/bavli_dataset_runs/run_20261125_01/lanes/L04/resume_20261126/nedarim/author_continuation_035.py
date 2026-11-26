"""Loaf transfer and misuse liability: direct/third-party gift and tannaitic disagreement."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r035.';a.OUTPUT='continuation_035.json'
c=a.c;q=b.q;e=a.edge
a.structure('loaf',['34b:1','34b:2','34b:3','35a:1','35a:2','35a:3'],'Consecrated loaf valuation and ownership-limited vow after gift')
a.structure('misuse',['35a:'+str(i) for i in range(4,9)],'Misuse of konam property, redemption and recipient liability')
eat=c('eat','34b:1','אמר רבא היתה לפניו ככר של הפקר ואמר ככר זו הקדש נטלה לאוכלה מעל לפי כולה','Rava says that after consecrating an ownerless loaf, taking it to eat incurs misuse liability for its full value.',holder='רבא',conditions=['ownerless loaf declared consecrated','taken for eating'])
heirs=c('heirs','34b:1','להורישה לבניו מעל לפי טובת הנאה שבה','Taking it to bequeath to his sons incurs liability according to its benefit value.',holder='רבא',conditions=['taking for inheritance purpose'],scope='Contrasting valuation branch, no numerical value invented')
giftq=q('giftq','34b:2','בעא מיניה רב חייא בר אבין מרבא ככרי עליך ונתנה לו במתנה מהו','Rav Hiyya bar Avin asks Rava what happens if one prohibits my loaf to another and then gives it to him.',voice='רב חייא בר אבין')
owned=c('owned','34b:2','ככרי אמר לו כי איתיה ברשותיה הוא דאסור','One proposed reading makes my loaf prohibit it only while it belongs to the speaker.',mode='hypothetical',scope='First explicit branch of question, not accepted conclusion')
personal=c('personal','34b:2','או דלמא עליך אמר ליה עילויה שויתיה הקדש','The alternative reading makes upon you impose consecration-like status relative to the recipient.',mode='hypothetical',scope='Second explicit branch of question')
still=c('still','34b:3','אמר ליה פשיטא דאף על גב דיהבה ליה במתנה אסור','Rava answers that it remains prohibited even after a gift.',holder='רבא',conditions=['direct gift after my-loaf-upon-you declaration'])
e('still.answer',still,giftq,'answer','34b:3');e('still.correction',still,owned,'correction','34b:3')
excludeq=q('excludeq','34b:3','אלא ככרי עליך לאפוקי מאי לאו לאפוקי דאי גנבה מיניה מיגנב','What then does my loaf exclude: perhaps stealing it from the speaker?')
invite=c('invite','34b:3','אמר ליה לא לאפוקי דאי אזמניה עלה','The reply instead identifies the invitation case as what is excluded.',scope='Exact אזמניה עלה retained; no inferred permission for theft')
e('invite.answer',invite,excludeq,'answer','34b:3')
cow=c('cow','35a:1','איתיביה אמר לו השאילני פרתך אמר לו קונם פרה שאני קנוי לך נכסי עליך אם יש לי פרה אלא זו','The objection cites a request to borrow a cow and the printed conditional cow/property declaration.',composition='composite',scope='Exact unusual שאני קנוי wording retained; no silent grammatical reconstruction')
axe=c('axe','35a:1','השאילני קרדומך אמר לו קונם קרדום שיש לי שאני קנוי נכסי עלי אם יש לי קרדום אלא זה','The parallel axe request is followed by the printed axe/property declaration.',composition='composite',scope='Exact עלי and שאני קנוי retained, not harmonized to cow clause')
alive=c('alive','35a:1','ונמצא שיש לו בחייו אסור','When he is found to possess another, the prohibition applies during his life.',conditions=['additional item discovered'],scope='Cited case before death/gift exceptions')
deathgift=c('deathgift','35a:1','מת או שנִתְּנה לו במתנה הרי זה מותר','The citation permits after death or when given as a gift.',composition='composite',scope='Gift clause challenges direct-gift prohibition until intermediary distinction')
indirect=c('indirect','35a:2',None,'Rav Aha son of Rav Ika explains that the gift came through another person.',holder='רב אחא בריה דרב איקא',conditions=['third-party transfer'],scope='Distinct from direct gift in Rava’s ruling')
grammar=c('grammar','35a:3',None,'Rav Ashi supports the distinction from the passive שניתנה לו rather than active שנתָנָהּ לו.',holder='רב אשי',scope='Explicit grammatical evidence, original vocalization retained')
e('deathgift.objection',deathgift,still,'objection','35a:1');e('indirect.qualification',indirect,deathgift,'qualification','35a:2');e('grammar.support',grammar,indirect,'support','35a:3')
misuseq=q('misuseq','35a:4',None,'Rava asks Rav Nahman whether misuse liability applies to konam prohibitions.',voice='רבא')
nahman=c('nahman','35a:5',None,'Rav Nahman derives misuse liability from the Mishnah assigning a fee benefit to consecration: konam resembles consecrated property for this purpose.',holder='רב נחמן',scope='Analogy subsequently located in tannaitic disagreement')
e('nahman.answer',nahman,misuseq,'answer','35a:5')
general=c('general','35a:6','קונם ככר זו הקדש ואכלה בין הוא ובין חבירו מעל לפיכך יש לה פדיון','Rabbi Meir’s first case imposes misuse on either declarant or another who eats a generally consecrated konam loaf; therefore it has redemption.',holder='רבי מאיר',composition='composite',conditions=['general loaf consecration'],scope='Rabbi Meir attribution supplied at end of same segment')
own=c('own','35a:6','ככר זו עלי להקדש ואכלה הוא מעל חבירו לא מעל לפיכך אין לה פדיון דברי רבי מאיר','For a loaf consecrated only upon himself, Rabbi Meir imposes misuse on him but not his fellow and denies redemption.',holder='רבי מאיר',composition='composite',conditions=['personal upon-me declaration'])
sages=c('sages','35a:7',None,'The sages deny misuse liability in either case because konamot do not carry misuse liability.',holder='חכמים',scope='Explicit tannaitic opposition, not erased by Rav Nahman’s preceding answer')
e('sages.objection',sages,general,'objection','35a:7');e('sages.objection2',sages,own,'objection','35a:7');e('sages.qualification',sages,nahman,'qualification','35a:7')
who=q('who','35a:8','אמר ליה רב אחא בריה דרב אוויא לרב אשי  ככרי עליך ונתנה לו במתנה מי מעל','Rav Aha son of Rav Avya asks Rav Ashi who commits misuse when a prohibited my-loaf is given to its recipient.',voice='רב אחא בריה דרב אוויא')
giver=c('giver','35a:8','למעול נותן הא לא אסירא עליה','The giver seemingly cannot be liable because the loaf is not prohibited to him.',mode='hypothetical',scope='First elimination branch in question')
recipient=c('recipient','35a:8','למעול מקבל יכול דאמר היתירא בעיתי איסורא לא בעיתי','The recipient could object that he wanted a permitted gift, not a prohibited one.',mode='hypothetical',scope='Second difficulty, answered by expenditure analogy')
spend=c('spend','35a:8','אמר ליה מקבל מעל לכשיוציא','Rav Ashi answers that the recipient commits misuse when he expends it.',holder='רב אשי',conditions=['recipient expends the item'],scope='Time of liability, not simply receipt')
mistake=c('mistake','35a:8','שכל המוציא מעות הקדש לחולין כסבור של חולין הוא מועל אף זה מועל','The analogy is spending consecrated money as ordinary money while mistakenly believing it ordinary; such a spender commits misuse.',scope='Reason rejecting recipient’s mistaken-permission defense')
e('spend.answer',spend,who,'answer','35a:8');e('mistake.support',mistake,spend,'support','35a:8')
a.notes={
'34b:1':'Reread ownerless loaf declaration and separate eating/full-value versus inheritance/benefit-value branches.',
'34b:2':'Reread Hiyya bar Avin-to-Rava question and ownership/personal-prohibition alternatives.',
'34b:3':'Reread direct-gift prohibition, stolen-loaf exclusion suggestion and invitation-case reply.',
'35a:1':'Reread both cow/axe dialogues exactly despite unusual printed wording, additional possession and death/gift exceptions.',
'35a:2':'Reread Aha son of Ika third-party-gift distinction.',
'35a:3':'Reread Ashi passive/active grammatical support with vocalization preserved.',
'35a:4':'Reread Rava-to-Nahman misuse-in-konamot question.',
'35a:5':'Reread fee-consecration analogy answer and followed tannaitic disagreement.',
'35a:6':'Reread both Meir general/personal cases, both actors’ liability and redemption consequences.',
'35a:7':'Reread sages blanket no-misuse disagreement for both stated cases.',
'35a:8':'Reread Aha son of Avya-to-Ashi question, both actor difficulties, expenditure-time answer and mistaken-sacred-money analogy.'}
if __name__=='__main__':a.save()
