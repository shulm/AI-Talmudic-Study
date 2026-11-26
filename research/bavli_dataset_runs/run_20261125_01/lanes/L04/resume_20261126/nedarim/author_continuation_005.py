"""Manual Abaye/Rava unit, preserving Abaye's limited retraction."""
import author_continuation_002 as a
a.records=[];a.notes={};a.PREFIX='nd.r005.';a.OUTPUT='continuation_005.json'
c=a.c;q=a.q;e=a.edge
scope=['5b:'+str(i) for i in range(5,9)]+['6a:'+str(i) for i in range(1,9)]
a.structure('indicative',scope,'Abaye and Rava on nonindicative abbreviated expressions; limited retraction and competing tannaitic comparisons')
abaye=c('abaye','5b:5','ידים שאין מוכיחות אביי אמר  הוויין ידים','Abaye holds nonindicative abbreviated expressions effective.',holder='אביי',mode='challenged',conditions=['ידים שאין מוכיחות'],scope='Main position challenged below; the explicit retraction concerns his asserted compatibility with Rabbi Yehuda, not an unambiguous abandonment of this main view')
rava=c('rava','5b:5','ורבא אמר  לא הוויין ידים','Rava holds nonindicative abbreviated expressions ineffective.',holder='רבא',conditions=['ידים שאין מוכיחות'])
proof=c('proof','5b:5',"אמר רבא  רבי אידי אסברה לי  אמר קרא (במדבר ו ב) נזיר להזיר לי''י מקיש ידות נזירות לנזירות מה נזירות בהפלאה אף ידות נזירות בהפלאה",'Rava reports Rabbi Idi’s explanation: the verse compares abbreviated nazirite declarations to full naziriteship, requiring explicit articulation for both.',holder='רבא',scope='Rava is reporting voice, Rabbi Idi the explicitly named explanatory authority',composition='composite')
a.add('idi.attribution','attributions',dict(surface='רבי אידי',role='quoted_authority',candidates=['רבי אידי'],scope=proof,transmission_chain=['רבי אידי','רבא']),[a.ev('5b:5','רבי אידי אסברה לי')],[proof])
e('proof.support',proof,rava,'support','5b:5')
parallel=q('parallel','5b:6',"לימא בפלוגתא דר' יהודה ורבנן קמיפלגי",'Do Abaye and Rava dispute the same matter as Rabbi Yehuda and the sages?')
get=c('get','5b:6','דתנן  גופו של גט הרי את מותרת לכל אדם','The cited Mishnah states the divorce formula הרי את מותרת לכל אדם.',scope='Repeated quotation; distinct occurrence from5b:2')
yg=c('yg','5b:6',"ר' יהודה אומר  ודין דיהוי ליכי מינאי ספר תירוכין וגט פטורין ואיגרת שבוקין",'Rabbi Yehuda gives the fuller formula ודין דיהוי ליכי מינאי ספר תירוכין וגט פטורין ואיגרת שבוקין.',holder='רבי יהודה',scope='Exact repeated formulation, retaining the additional וגט פטורין printed here')
map=c('map','5b:6','אביי דאמר כרבנן ורבא דאמר כרבי יהודה','The initial suggestion aligns Abaye with the sages and Rava with Rabbi Yehuda.',mode='challenged',composition='composite',scope='Suggested alignment, challenged by both responses and partly reconsidered later')
e('get.support',get,map,'support','5b:6');e('yg.support',yg,map,'support','5b:6')
aboth=c('aboth','5b:7',"אמר לך אביי  אנא דאמרי אפי' לר' יהודה",'The response in Abaye’s voice initially claims compatibility even with Rabbi Yehuda.',holder='אביי',mode='retracted',scope='Dialectically supplied response אמר לך, withdrawn at6a:6; not independent historical speech certification')
cut=c('cut','5b:7','עד כאן לא קאמר רבי יהודה בעינן ידים מוכיחות אלא גבי גט דבעינן כריתות וליכא','That response limits Rabbi Yehuda’s indicative-wording requirement to divorce, where severance is required.',holder='אביי',mode='retracted',conditions=['divorce requires כריתות'],scope='Reason supporting Abaye’s subsequently withdrawn compatibility claim')
ageneral=q('ageneral','5b:7','אבל בעלמא מי שמעת ליה','Has Rabbi Yehuda been heard to require this in other contexts?')
e('aboth.answer',aboth,parallel,'answer','5b:7');e('cut.support',cut,aboth,'support','5b:7')
rboth=c('rboth','5b:8',"ורבא אמר  אנא דאמרי אפי' לרבנן",'Rava claims compatibility even with the sages.',holder='רבא',scope='Local response maintained again at6a:8')
wife=c('wife','5b:8',"ע''כ לא קאמרי רבנן דלא בעינן ידים מוכיחות אלא גבי גט",'Rava limits the sages’ leniency to divorce because a person does not divorce another man’s wife.',holder='רבא',conditions=['divorce context'],extra=[('6a:1','דאין אדם מגרש את אשת חבירו')],scope='Cross-page explanatory sentence; clarity supplied by the divorce setting')
rgeneral=q('rgeneral','6a:1','אבל בעלמא מי שמעת להו','Have the sages been heard to dispense with indicative expressions generally?')
e('rboth.answer',rboth,parallel,'answer','5b:8');e('wife.support',wife,rboth,'support','6a:1')
offerc=c('offerc','6a:2','מיתיבי  הרי הוא עלי הרי זה [עלי] אסור מפני שהוא יד לקרבן','The cited teaching prohibits הרי הוא עלי and הרי זה [עלי] as abbreviated offering declarations.',composition='composite',conditions=['quoted formulations including עלי'],scope='Exact bracketed reading retained; no emendation of source')
infer=c('infer','6a:2','טעמא דאמר עלי הוא דאסור אבל לא אמר עלי לא','The objection infers that omitting עלי leaves no prohibition.',mode='challenged',conditions=['עלי omitted'],scope='Initial inference challenged by the reply')
e('offerc.support',offerc,infer,'support','6a:2');e('infer.objection',infer,abaye,'objection','6a:2')
charity=c('charity','6a:3','אמר לך אביי  טעמא דאמר עלי הוא דאסור אבל אמר הרי הוא ולא אמר עלי הרי הוא דהפקר הרי הוא דצדקה קאמר','The first reply in Abaye’s voice reads bare הרי הוא as an ownerless-property or charity declaration rather than the prohibition of עלי.',holder='אביי',mode='rejected',conditions=['הרי הוא without עלי'],composition='composite',scope='Two possible senses in an attempted answer, not proof both dedications take effect')
textq=q('textq','6a:3','והא מפני שהוא יד לקרבן קתני','But does the teaching not explicitly call it an abbreviated offering declaration?')
e('charity.answer',charity,infer,'answer','6a:3');e('textq.objection',textq,charity,'objection','6a:3')
oneme=c('oneme','6a:4','אלא אימא  טעמא דאמר עלי הוא אסור וחבירו מותר','The replacement answer says עלי prohibits only the speaker, leaving the other person permitted.',conditions=['עלי stated'],scope='Anonymous reformulation of reply defending Abaye')
all=c('all','6a:4','אבל אמר הרי הוא שניהן אסורין דדלמא הרי הוא הקדש קאמר','Bare הרי הוא prohibits both because it may express consecration.',conditions=['הרי הוא without עלי'],scope='Replacement interpretation defending Abaye, with explicit uncertainty דדלמא')
e('oneme.correction',oneme,infer,'correction','6a:4');e('all.correction',all,charity,'correction','6a:4')
sin=c('sin','6a:5',"מיתיבי  הרי זו חטאת הרי זו אשם אע''פ שהוא חייב חטאת ואשם לא אמר כלום",'The next teaching says הרי זו חטאת or הרי זו אשם has no effect even if the speaker owes such an offering.',conditions=['formula without possessive suffix','even already obligated'],composition='composite',scope='Quoted paired sin/guilt-offering rule')
mine=c('mine','6a:5','הרי זו חטאתי הרי זו אשמי אם היה מחויב דבריו קיימין','The possessive formulations הרי זו חטאתי and הרי זו אשמי are effective if the speaker is obligated.',conditions=['possessive formulation','speaker obligated'],composition='composite',scope='Quoted positive paired rule')
e('sin.objection',sin,abaye,'objection','6a:5');e('mine.distinction',mine,sin,'distinction','6a:5')
assign=c('assign','6a:6',"אמר לך אביי  הא מני ר' יהודה היא",'The reply in Abaye’s voice assigns this teaching to Rabbi Yehuda.',holder='אביי',scope='Dialectical answer to sin/guilt-offering objection')
aq=q('aq','6a:6','והא אביי הוא דאמר  אנא דאמרי אפילו לרבי יהודה','But did Abaye not claim compatibility even with Rabbi Yehuda?')
retract=c('retract','6a:6','הדר ביה','The discussion states that Abaye withdrew his prior claim of compatibility with Rabbi Yehuda.',scope='Retraction targets immediately challenged compatibility assertion; no unsupported broader reversal of principal position')
e('assign.answer',assign,sin,'answer','6a:6');e('aq.objection',aq,aboth,'objection','6a:6');e('retract.correction',retract,aboth,'correction','6a:6');e('retract.answer',retract,aq,'answer','6a:6')
rq=q('rq','6a:7',None,'Should Rava then be identified only with Rabbi Yehuda?')
again=c('again','6a:8','אמר לך רבא  אנא דאמרי אפילו לרבנן','The reply in Rava’s voice maintains compatibility even with the sages.',holder='רבא',scope='Explicit repeated response, not deduplicated away')
special=c('special','6a:8','עד כאן לא קאמרי רבנן דלא בעינן ידים מוכיחות אלא גבי גט דאין אדם מגרש את אשת חבירו','The repeated rationale confines the sages’ divorce leniency to the fact that no one divorces another man’s wife.',holder='רבא',conditions=['divorce setting'],scope='Rava’s local argument about the sages')
general=c('general','6a:8','אבל בעלמא בעינן ידים מוכיחות','Outside that setting, the response requires indicative abbreviated expressions.',holder='רבא',scope='Rava’s account compatible with sages; no unqualified historical attribution to every sage')
e('again.answer',again,rq,'answer','6a:8');e('special.support',special,again,'support','6a:8');e('general.distinction',general,special,'distinction','6a:8')
a.notes={
'5b:5':'Reread distinct Abaye/Rava positions and Rava’s report from Rabbi Idi; attribution roles explicitly separated, no Rav/Rava conflation.',
'5b:6':'Reread repeated divorce wording with printed extra phrase and tentative two-way alignment.',
'5b:7':'Reread Abaye-voiced compatibility response against6a:6 retraction; scope is compatibility, not automatic reversal of whole position.',
'5b:8':'Reread Rava compatibility and cross-page divorce rationale.',
'6a:1':'Reread completion of rationale and question; no invented isolated source claim.',
'6a:2':'Reread bracketed עלי, offering rule and challenged negative inference.',
'6a:3':'Reread ownerless/charity attempted explanation and explicit offering-language objection.',
'6a:4':'Reread replacement personal/universal scope distinction and דדלמא uncertainty.',
'6a:5':'Reread nonpossessive/possessive sin and guilt formulations, including obligation condition in both.',
'6a:6':'Reread Rabbi Yehuda attribution, compatibility challenge and retraction, preserving initial claim.',
'6a:7':'Reread remaining Rava-alignment question as question only.',
'6a:8':'Reread repeated Rava answer, divorce-only rationale and general requirement; maintained asymmetry after Abaye retraction.'}
if __name__=='__main__':a.save()
