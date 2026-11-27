"""Explicit reading of mixed-crop inspections, funding and successive enactments."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scoped_reading import ScopedReading
a=ScopedReading('moed_katan','Moed Katan','mk.r014');c=a.claim;e=a.e
def q(*args,**kwargs):
    v=a.question(*args,**kwargs);a.rows[-1]['content']['answer_set_status']='partial'
    a.rows[-1]['uncertainty'].append('Only represented source-supported replies for this question; not an exhaustive or task-qualified inventory.')
    return v
refs=['6a:'+str(i) for i in range(9,17)]+['6b:'+str(i) for i in range(1,5)]
a.structure('inspections',refs,'Mixed crops: inspection times, public funding, measure and successive enforcement enactments')
lemma=c('lemma','6a:9','ויוצאין אף על הכלאים','The Mishnah includes going out to inspect mixed crops among festival public works.',scope='Repeated Mishnah lemma')
when=q('when','6a:10','ואכלאים בחולו של מועד נפקינן','Are mixed-crop inspections made during the intermediate festival days?')
adar=c('adar','6a:10','באחד באדר משמיעין על השקלים ועל הכלאים','The cited calendar announces the shekels and mixed crops on the first of Adar.',conditions=['first of Adar'],composition='composite')
purim=c('purim','6a:11','בחמשה עשר בו קורין את המגילה בכרכים','The cited calendar places the Megillah reading in walled cities on the fifteenth of Adar.',conditions=['fifteenth of Adar','walled cities'])
works=c('works','6a:11','ויוצאין לקווץ את הדרכים ולתקן הרחובות ולמוד המקואות ועושין כל צורכי רבים ומציינין את הקברות','The calendar lists road clearing, street repair, measuring immersion pools, public needs and grave marking on that date.',conditions=['fifteenth of Adar'],composition='composite',scope='Quoted public-work list retained, not only the mixed-crop clause')
inspection=c('inspection','6a:11','ויוצאין על הכלאים','The calendar also places mixed-crop inspection on that date.',conditions=['fifteenth of Adar'])
e('when_challenge',when,lemma,'objection','6a:10');e('inspection_support',inspection,when,'support','6a:11')
unc=['The two explanations are assigned by חד אמר/וחד אמר to Rabbi Elazar and Rabbi Yose bar Hanina without identifying which speaker holds which. No name-order assignment.']
pair=['רבי אלעזר','רבי יוסי בר חנינא']
early=c('early','6a:12','חד אמר כאן בבכיר כאן באפיל','One explanation distinguishes early from late crops.',candidates=pair,role='position_holder',conditions=['early versus late crops'],uncertainty=unc,scope='Alternative reconciliation of the two inspection dates; terse source categories retained')
types=c('types','6a:12','וחד אמר כאן בזרעים כאן בירקות','The other explanation distinguishes seeds from vegetables.',candidates=pair,role='position_holder',conditions=['seeds versus vegetables'],uncertainty=unc,scope='Alternative reconciliation of inspection dates; not mechanically assigned by name order')
e('early_answer',early,when,'answer','6a:12');e('types_answer',types,when,'answer','6a:12')
visible=c('visible','6a:13','א"ר אסי א"ר יוחנן לא שנו אלא שאין ניצן ניכר אבל ניצן ניכר יוצאין עליהן','Rav Asi reports Rabbi Yohanan limiting the stated timing to when growth is not recognizable; when it is recognizable, inspectors go out.',candidates=['רבי יוחנן'],role='quoted_authority',chain=['רב אסי','רבי יוחנן'],conditions=['growth recognizable or not recognizable'],composition='composite')
e('visible_qualifies',visible,lemma,'qualification','6a:13')
wageq=q('wage_q','6a:14','מאי שנא בחולו של מועד דנפקינן','Why specifically go out during the intermediate festival days?')
wage=c('wage','6a:14','אמר רבי יעקב אמר רבי יוחנן משום שכר פעולה דמוזלי גבן','Rabbi Yaakov reports Rabbi Yohanan that labor is cheaper for the public then.',candidates=['רבי יוחנן'],role='quoted_authority',chain=['רבי יעקב','רבי יוחנן'],conditions=['cheaper labor during intermediate festival days'])
e('wage_answer',wage,wageq,'answer','6a:14')
fund=c('fund','6a:15','אמר רב זביד ואיתימא רב משרשיא שמע מינה כי יהבינן להו שכר מתרומת הלשכה יהבינן להו','Rav Zevid, alternatively Rav Mesharshiya, infers that inspectors’ wages are paid from the chamber contribution.',candidates=['רב זביד','רב משרשיא'],uncertainty=['ואיתימא preserves alternative attribution versions; not two separate endorsers.'])
reason=c('fund_reason','6a:15','דאי סלקא דעתך מדידהו יהבינן להו מאי נפקא לן מינייהו כל כמה דבעו ליתן להו','If owners paid themselves, the argument says there would be no public concern over the amount they wished to pay.',candidates=['רב זביד','רב משרשיא'],mode='hypothetical',conditions=['hypothetical owner-paid wages'],uncertainty=['Alternative source attribution to Rav Zevid or Rav Mesharshiya retained.'],scope='Counterfactual argument for public funding; not a permission to set public wages arbitrarily')
rq=q('fund_q','6a:15','מאי נפקא לן מינייהו','What concern would the public have over owner-paid wages?',candidates=['רב זביד','רב משרשיא'],uncertainty=['Rhetorical question within the alternatively attributed funding argument.'])
e('wage_fund',wage,fund,'support','6a:15');e('fund_reason_support',reason,fund,'support','6a:15');e('fund_q_reply',reason,rq,'answer','6a:15')
amountq=q('amount_q','6a:16','ועד כמה','What quantity of mixed seed requires intervention?')
head=a.speech('measure_head','6a:16','אמר רב שמואל בר יצחק כאותה ששנינו כל סאה שיש בה',candidates=['רב שמואל בר יצחק'],composition='composite',act='introduction to quoted measure continued on next page',uncertainty=['Incomplete measure continues at6b:1; not treated as a complete independent rule.'])
measure=c('measure','6b:1','רובע זרע ממין אחר ימעט','Rav Shmuel bar Yitzhak cites the rule: a seah containing a quarter-kav of seed of another kind must have that admixture reduced.',candidates=['רב שמואל בר יצחק'],role='quoted_authority',naming_refs=['6a:16'],conditions=['one seah containing a quarter-kav of another seed kind'],scope='Quoted measure spanning6a:16–6b:1')
for row in a.rows:
    if row['id'].startswith('mk.r014.measure.') and row['layer']!='attributions':row['evidence'].append(a.evidence('6a:16'))
e('measure_answer',measure,amountq,'answer','6b:1')
challenge=q('enactment_q','6b:2','והתניא התקינו שיהו מפקירין כל השדה כולה','Does not a baraita say that the entire field is declared ownerless?')
confisc=c('confiscate','6b:2','התקינו שיהו מפקירין כל השדה כולה','An enactment provides that the entire field is declared ownerless.',scope='Quoted enforcement enactment')
period=c('period','6b:2','לא קשיא כאן קודם תקנה כאן לאחר תקנה','The discussion reconciles the measure with the whole-field rule by distinguishing before and after the enactment.',conditions=['before versus after enactment'])
e('enactment_challenge',challenge,measure,'objection','6b:2');e('period_answer',period,challenge,'answer','6b:2')
first=c('first','6b:3','דתניא בראשונה היו עוקרין ומשליכין לפני בהמתן','Initially inspectors uprooted the plants and threw them before the owners’ animals.',scope='Historical enforcement account')
benefit1=c('benefit_weeding','6b:3','והיו בעלי בתים שמחין שתי שמחות אחת שמנכשין להם שדותיהן','Owners welcomed the weeding of their fields as one benefit.',scope='Narrative report of owners’ response, not endorsement')
benefit2=c('benefit_feed','6b:3','ואחת שמשליכין לפני בהמתם','Owners also welcomed the plants being thrown before their animals.',scope='Second benefit in the historical narrative')
road=c('road','6b:4','התקינו שיהו עוקרין ומשליכין על הדרכים','An intermediate enactment required uprooting and throwing the plants onto roads.',scope='Historical enforcement revision')
still=c('still','6b:4','ועדיין היו שמחין שמחה גדולה שמנכשין שדותיהן','Owners still welcomed the benefit of having their fields weeded.',scope='Narrative response explaining the next revision')
last=c('last','6b:4','התקינו שיהו מפקירין כל השדה כולה','The later enactment declared the entire field ownerless.',scope='Final stage in the quoted enforcement history; parallel occurrence of6b:2')
e('road_corrects',road,first,'correction','6b:4');e('last_corrects',last,road,'correction','6b:4');e('still_support',still,last,'support','6b:4')
a.rows[-1]['content']['explicitness']='editorial_reconstruction';a.rows[-1]['origin']='editorial_inference';a.rows[-1]['uncertainty']=['Causal explanation inferred from the narrated sequence; no explicit causal connective.']
a.save_window(refs,'resume_moed_katan_mixtures014.json','Read inspection and successive-enactment account with continuation through6b:16; preserve unassigned paired speakers and alternative attribution, public-work list, narrative motives and cross-page measure. Source-supported partial answer inventories are nonexhaustive.','d16f0a518bcd7b7f24385fee06d10ecee2d465eda1aeb8bdad395e42766f8af0')
