"""Food-benefit tools and unanswered indirect-benefit questions."""
import author_continuation_024 as b
a=b.a;a.records=[];a.notes={};a.PREFIX='nd.r033.';a.OUTPUT='continuation_033.json'
c=a.c;q=b.q;e=a.edge
a.structure('tools',['32b:'+str(i) for i in range(10,14)]+['33a:'+str(i) for i in range(1,8)],'Food-benefit restrictions, indirect means and customary rental')
diff=c('diff','32b:10','בין המודר הנאה מחבירו למודר הימנו מאכל אלא דריסת הרגל וכלים שאין עושין בהם אוכל נפש','The Mishnah distinguishes general-benefit and food-benefit vows through passage on property and utensils not used to prepare food.',composition='composite',scope='Restricted comparison within these two vow categories')
food=c('food','32b:11','המודר מאכל מחבירו לא ישאילנו נפה וכברה וריחיים ותנור','Under a food-benefit restriction one may not lend a sieve, coarse sieve, mill or oven.',composition='composite',scope='Explicit food-preparation list')
clothes=c('clothes','32b:11','אבל משאיל לו חלוק וטבעת וטלית ונזמים','One may lend a tunic, ring, cloak and earrings.',composition='composite',scope='Context qualified by later indirect-purpose question and local rental practice')
who=q('who','32b:12','מאן תנא','Which tanna teaches the restriction?')
el=c('el','32b:12','אמר רב אדא בר אהבה רבי אליעזר היא דתניא רבי אליעזר אומר אפילו ויתור אסור במודר הנאה','Rav Adda bar Ahava identifies Rabbi Eliezer, whose teaching forbids even a freely conceded benefit under a general-benefit vow.',holder='רבי אליעזר',scope='Position holder distinguished from identifying reporter')
a.add('el.chain','attributions',dict(surface='אמר רב אדא בר אהבה',role='transmitter',candidates=['רב אדא בר אהבה'],scope=el,transmission_chain=['רב אדא בר אהבה','רבי אליעזר']),[a.ev('32b:12','אמר רב אדא בר אהבה')],[el])
e('el.answer',el,who,'answer','32b:12')
a.add('lemma.u','utterances',dict(textual_voice='anonymous textual citation',discourse_role='Mishnah lemma repeated',composition='atomic'),[a.ev('32b:13')])
a.add('lemma.a','attributions',dict(surface='',role='anonymous',candidates=[],scope=a.PREFIX+'lemma.u',transmission_chain=[]),[a.ev('32b:13')],[a.PREFIX+'lemma.u'])
foodq=q('foodq','33a:1','והא מן מאכל נדר','Did he not vow only against food itself?')
lakish=c('lakish','33a:1','אמר רבי שמעון בן לקיש באומר הנאת מאכלך עלי','Rabbi Shimon ben Lakish specifies a declaration prohibiting benefit from your food.',holder='רבי שמעון בן לקיש',scope='First formulation, narrowed/replaced next segment')
e('lakish.answer',lakish,foodq,'answer','33a:1')
wheatq=q('wheatq','33a:2','אימא שלא ילעוס חיטין ויתן על מכתו','Might that wording instead prohibit chewing wheat and putting it on a wound?')
rava=c('rava','33a:2','אמר רבא באומר הנאה המביאה לידי מאכלך עלי','Rava specifies benefit that leads to your food.',holder='רבא',scope='Formulation encompasses means of obtaining food')
e('rava.answer',rava,wheatq,'answer','33a:2');e('rava.correction',rava,lakish,'correction','33a:2')
pappa=c('pappa','33a:3','אמר רב פפא שק להביא פירות וחמור להביא עליו פירות ואפילו צנא בעלמא הנאה המביאה לידי מאכל הוא','Rav Pappa includes a sack, donkey and even a simple basket for bringing produce as benefit leading to food.',holder='רב פפא',composition='composite',scope='Three explicitly named transport means')
ride=a.q('ride','33a:3','בעי רב פפא סוס לרכוב עליו וטבעת ליראות בה מהו','Rav Pappa asks about a horse for riding and a ring for appearing with.',voice='רב פפא')
path=a.q('path','33a:3','מיפסק ומיזל בארעיה מאי','What about crossing through the other’s land?',voice='רב פפא')
for ident in [ride,path]:next(x for x in a.records if x['id']==ident)['uncertainty'].append('The proposed proof below is deflected; no definitive resolution appears before the next Mishnah.')
proof=c('proof','33a:4','תא שמע אבל משאיל לו חלוק וטלית נזמים וטבעות','The permitted tunic, cloak, earrings and rings are cited as a possible proof.',scope='Quoted Mishnah evidence in indirect-benefit inquiry')
appearance=c('appearance','33a:4','היכי דמי אילימא שלא ליראות בהן צריכא למימר אלא לאו אפילו ליראות בהן וקתני משאילו','The argument assumes the permission must include appearing with them, because otherwise it would be obvious.',mode='rejected',composition='composite',scope='Proposed resolution through appearance use, deflected next segment')
deflect=c('deflect','33a:5',None,'The reply limits the permission to use not for appearing with them; its wording parallels the earlier prohibition clause.',scope='Deflects proposed proof without settling all indirect-benefit questions')
e('appearance.support',appearance,ride,'support','33a:4');e('deflect.correction',deflect,appearance,'correction','33a:5');e('deflect.unresolved',deflect,ride,'unresolved_outcome','33a:5');e('deflect.unresolved2',deflect,path,'unresolved_outcome','33a:5')
rental=c('rental','33a:6','וכל דבר שאין עושין בו אוכל נפש מקום שמשכירין כיוצא בהן אסור','Even non-food-preparation items are prohibited where equivalent items are customarily rented.',conditions=['local rental practice'],scope='Mishnah’s qualification of nonfood-tool allowance')
free=c('free','33a:7','מכלל דרישא אף על פי שאין משכירין','The discussion infers that the earlier food-preparation prohibition applies even where lending is free.',scope='Inference from rental qualification')
who2=q('who2','33a:7','מאן תנא','Who teaches this freely conceded-benefit restriction?')
el2=c('el2','33a:7','אמר רב אדא בר אהבה רבי אליעזר היא','Rav Adda bar Ahava again identifies Rabbi Eliezer.',scope='Repeated authorial identification, separate source occurrence')
e('el2.answer',el2,who2,'answer','33a:7');e('rental.qualification',rental,clothes,'qualification','33a:6')
a.notes={
'32b:10':'Reread general/food benefit distinction and both listed exceptions.',
'32b:11':'Reread all four food-preparation tools and all four permitted items.',
'32b:12':'Reread authorship question, Adda identification and Eliezer freely-conceded-benefit principle.',
'32b:13':'Reread abbreviated Mishnah lemma as citation marker, no new legal proposition invented.',
'33a:1':'Reread food-only objection and Shimon ben Lakish formulation.',
'33a:2':'Reread wheat/wound counterreading and Rava benefit-leading-to-food formulation.',
'33a:3':'Reread sack/donkey/basket rule and horse/ring/path questions, with final uncertainty preserved.',
'33a:4':'Reread cited garment/jewelry allowance and rejected appearance-purpose inference.',
'33a:5':'Reread nonappearance deflection and parallelism rationale, no manufactured final resolution.',
'33a:6':'Reread customary-rental qualification for nonfood items.',
'33a:7':'Reread free-lending implication and repeated Adda/Eliezer attribution.'}
if __name__=='__main__':a.save()
