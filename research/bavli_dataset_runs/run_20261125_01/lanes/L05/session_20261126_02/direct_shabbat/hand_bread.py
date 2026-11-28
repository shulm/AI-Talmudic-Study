import opening as x
import json
x.records.clear()
add=x.add; claim=x.claim; q=x.q; edge=x.edge; attr=x.attr
add('b_s1','structure',range(32,45),dict(title='Abaye: status of an extended hand and returning it; alternative reconciliations',primary=True,boundary='closed',legacy_ids=[]))
add('b_s2','structure',range(45,52),dict(title='Removing bread from an oven to avoid a more serious Sabbath liability',primary=True,boundary='closed',legacy_ids=[]))
roles={32:('Abaye','Domain classification assertion'),33:('Abaye','Question about a karmelit and rabbinic penalty'),34:('Anonymous discussion and two baraitot','Contradictory reports and proposed explanation'),35:('Anonymous discussion','First rejection and reconciliation'),36:('Anonymous discussion','Alternative reconciliation'),37:('Anonymous discussion','Objection proposing inverse penalties'),38:('Anonymous discussion quoting Rav Bibi bar Abaye','Attempted inference to oven question'),39:('Anonymous discussion','Acceptance of proposed inference'),40:('Anonymous discussion','Alternative withholding inference'),41:('Anonymous discussion','Alternative dispute over penalty for inadvertence'),42:('Anonymous discussion','Alternative reconciliation begins'),43:('Rava and Rav Nahman','Continuation and cited question-answer exchange'),44:('Rava and Rav Nahman','Question and rationale'),45:('Rav Bibi bar Abaye','Resumed question'),46:('Rav Aha bar Abaye','Objection to case formulation'),47:('Discussion continuing objection','Alternative and Mishnah-based refutation'),48:('Discussion continuing objection','Deliberate-case alternative and terminology objection'),49:('Rav Shila','Reinterpretation as removal by others'),50:('Rav Sheshet','Objection to intervention by others'),51:('Rav Ashi; Rav Aha son of Rava reporting Rav Bibi bar Abaye','Correction and alternate explicit version')}
for i,(voice,role) in roles.items():
 add('b_u'+str(i),'utterances',[i],dict(textual_voice=voice,discourse_role=role,composition='composite'))
 if i in range(34,43) or i in [47,48]:
  add('b_a'+str(i),'attributions',[i],dict(surface='Anonymous discussion',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
claim('b_c32a',32,'A person’s hand is not like the public domain.',scope='Abaye’s hand-domain classification, inferred from the poor person’s hand',holder='Abaye')
claim('b_c32b',32,'A person’s hand is not like the private domain.',scope='Abaye’s hand-domain classification, inferred from the householder’s hand',holder='Abaye')
attr('b_a32',32,'אביי',scope='Both asserted domain exclusions')
q('b_q33',33,'Does a person’s hand become like a karmelit; did the sages penalize returning it to him or not?')
attr('b_a33',33,'אביי',scope='Question; not an asserted karmelit classification')
claim('b_c34a',34,'One baraita forbids returning a hand full of fruit after it was extended outside.', ['Hand full of fruit extended outside'],scope='First anonymous baraita; its conditions are reconciled by alternatives below',holder='First anonymous baraita')
claim('b_c34b',34,'Another baraita permits returning a hand full of fruit after it was extended outside.', ['Hand full of fruit extended outside'],scope='Second anonymous baraita; keep distinct',holder='Second anonymous baraita')
claim('b_c34c',34,'Proposed explanation: the baraitot dispute whether the hand is like a karmelit.',mode='rejected',scope='Suggestion rejected at 3b:6, not an established named dispute')
q('b_q34',34,'Do the baraitot not differ over whether the hand is like a karmelit?')
claim('b_c35a',35,'First reconciliation: both baraitot treat the hand as like a karmelit.',mode='reconciled',scope='First alternative only')
claim('b_c35b',35,'The differing rulings concern below ten handbreadths versus above ten.',mode='reconciled',scope='First reconciliation; text gives cases in order without naming teachers')
claim('b_c36a',36,'Alternatively both concern below ten, and the hand is not like a karmelit.',mode='reconciled',scope='Second alternative, not cumulative with first')
claim('b_c36b',36,'The sages did not penalize extension before day’s end, but did penalize extension after dark.', ['Distinguish extension before Sabbath and after dark'],mode='reconciled',scope='Second alternative; challenged by following reversal')
claim('b_c37a',37,'It seems more reasonable to penalize the before-dark case, since dropping then would not incur a sin offering.', ['Extension before dark'],mode='challenged',scope='Objection to second alternative; proposes opposite penalty direction')
claim('b_c37b',37,'It seems more reasonable not to penalize the after-dark case, since dropping then could incur a sin offering.', ['Extension after dark'],mode='challenged',scope='Second half of reversal objection')
q('b_q38',38,'Did the sages permit a person who attached bread in an oven to remove it before he incurs a sin-offering liability?')
attr('b_a38',38,'רב ביבי בר אביי','quoted_authority',scope='Question quoted while discussing the hand; not resolved merely by naming')
claim('b_c38',38,'Not giving the proposed reversed answer would resolve Rav Bibi bar Abaye’s question.',mode='hypothetical',scope='Proposed inference only; alternative explanations later avoid it')
claim('b_c39',39,'One response accepts the inference: removal was not permitted, and that inference is no difficulty.',scope='First response; not the final sole ruling after alternative versions')
claim('b_c40a',40,'An alternative refuses to resolve the oven question from the hand baraitot.',scope='Alternative to acceptance at 3b:10')
claim('b_c40b',40,'Instead, the sages did not penalize inadvertent extension but did penalize deliberate extension.', ['Inadvertent versus deliberate act'],mode='reconciled',scope='Alternative reconciliation')
claim('b_c41a',41,'Another alternative places both baraitot in an inadvertent case.',mode='reconciled',scope='Alternative to inadvertent/deliberate distinction')
claim('b_c41b',41,'The baraitot then dispute whether to penalize an inadvertent act on account of deliberate acts: one penalizes, one does not.', ['Both inadvertent'],mode='reconciled',scope='Anonymous alternatives, not assigned to named authorities')
claim('b_c42',42,'A further alternative denies the penalty and begins distinguishing return to the same courtyard.',mode='reconciled',scope='Sentence continues at 4a:1')
claim('b_c43a',43,'The counterpart case is returning to another courtyard.',mode='reconciled',scope='Completes the same/other courtyard distinction')
q('b_q43a',43,'May one return a hand full of fruit that was extended outside to the same courtyard?', ['Hand full of fruit extended outside'])
q('b_q43b',43,'May one return it to another courtyard?', ['Same hand and fruit case'])
claim('b_c43b',43,'Returning to the same courtyard is permitted.', ['Hand full of fruit extended outside'],scope='Rav Nahman’s reply to Rava',holder='Rav Nahman')
claim('b_c43c',43,'Returning to another courtyard is forbidden.', ['Hand full of fruit extended outside'],scope='Rav Nahman’s reply to Rava',holder='Rav Nahman')
attr('b_a43a',43,'רבא',scope='Asks Rav Nahman both questions')
attr('b_a43b',43,'ר״נ',scope='Rav Nahman answers permission and prohibition; abbreviation retained')
q('b_q44',44,'What distinguishes returning to the same courtyard from another courtyard?')
claim('b_c44',44,'Returning to the original courtyard does not accomplish his intention, whereas returning to another courtyard accomplishes it.',scope='Rav Nahman’s explanation following the salt retort',holder='Rav Nahman')
attr('b_a44',44,'Anonymous pronominal continuation of Rav Nahman’s response',scope='Speaker inferred from uninterrupted question-answer context; source does not repeat name',unc=['Rav Nahman identification depends on preceding exchange.'])
q('b_q45',45,'Was removing bread from an oven permitted before the person incurs a sin offering?', ['Bread already attached inside oven'])
attr('b_a45',45,'רב ביבי בר אביי',scope='Question as initially transmitted; revised formulation follows')
q('b_q46',46,'What is the case? If he acted inadvertently and has not remembered, to whom was permission given?')
claim('b_c46',46,'An inadvertent actor who has not remembered cannot be the addressee of the proposed permission.',mode='challenged',scope='Rav Aha bar Abaye’s objection to question as framed')
attr('b_a46',46,'רב אחא בר אביי',scope='Objects to Ravina; Ravina is addressee, not author of this objection')
q('b_q47',47,'If he subsequently remembered, would he still incur a sin offering?')
claim('b_c47',47,'The cited Mishnah requires both the beginning and end of a sin-offering liable act to be inadvertent.',scope='Quoted Mishnah refuting remembered case',holder='Anonymous Mishnah')
claim('b_c48',48,'If the act was deliberate, the question should say before a stoning prohibition, not before a sin offering.',mode='challenged',scope='Terminology objection, corrected later by Rav Ashi')
claim('b_c49',49,'Rav Shila retains an inadvertent case and explains that permission is for others to remove the bread.',mode='rejected',scope='Proposed interpretation challenged by Rav Sheshet and replaced by Rav Ashi',holder='Rav Shila')
attr('b_a49',49,'רב שילא',scope='Proposed others-removal interpretation')
q('b_q50',50,'Do we tell a person to sin so that another person may benefit?')
attr('b_a50',50,'רב ששת',scope='Rhetorical objection to Rav Shila; do not infer unrestricted universal ruling beyond objection')
claim('b_c51a',51,'Rav Ashi places the case in deliberate action and corrects the wording to before a stoning prohibition.',scope='Correction of question’s wording',holder='Rav Ashi')
claim('b_c51b',51,'Rav Aha son of Rava transmits explicitly that Rav Bibi bar Abaye said removal was permitted before a stoning prohibition.', ['Bread attached in oven; removal before stoning prohibition'],scope='Alternative explicit version is an affirmative statement, not the original question',holder='Rav Bibi bar Abaye')
attr('b_a51a',51,'רב אשי',scope='Corrected deliberate-case question')
attr('b_a51b',51,'רב אחא בריה דרבא','transmitter',scope='Transmits explicit affirmative version',chain=['רב אחא בריה דרבא','רב ביבי בר אביי'])
attr('b_a51c',51,'רב ביבי בר אביי','quoted_authority',scope='Affirmative permission in explicit alternate version')
for k,ii,a,b,r in [
 ('01',[34],'b_c34c','b_q33','answer'),('02',[35],'b_c35a','b_c34c','correction'),('03',[35],'b_c35b','b_c34a','qualification'),('04',[36],'b_c36b','b_c34a','qualification'),('05',[37],'b_c37a','b_c36b','objection'),('06',[37],'b_c37b','b_c36b','objection'),('07',[39],'b_c39','b_q38','answer'),('08',[40],'b_c40a','b_c39','qualification'),('09',[40],'b_c40b','b_c34a','qualification'),('10',[41],'b_c41b','b_c34a','qualification'),('11',[43],'b_c43b','b_q43a','answer'),('12',[43],'b_c43c','b_q43b','answer'),('13',[44],'b_c44','b_q44','answer'),('14',[46],'b_q46','b_q45','objection'),('15',[47],'b_c47','b_q47','support'),('16',[48],'b_c48','b_q45','objection'),('17',[49],'b_c49','b_q46','answer'),('18',[50],'b_q50','b_c49','objection'),('19',[51],'b_c51a','b_q45','correction'),('20',[51],'b_c51b','b_q45','answer')]: edge('b_e'+k,ii,a,b,r)
notes={32:'Both negative domain classifications and their separate source bases preserved; no karmelit answer inferred.',33:'Two linked aspects of explicit question retained.',34:'Two anonymous baraitot, suggested dispute, and subsequent rejection distinguished.',35:'First alternative retained as alternative; height conditions preserved.',36:'Second alternative contradicts first classification; timing and penalty direction preserved.',37:'Both directions of reversal objection and distinct sin-offering risks preserved.',38:'Oven question and proposed inference kept distinct.',39:'Accepted inference retained even though next alternative avoids it.',40:'No-resolution alternative and inadvertent/deliberate conditions preserved.',41:'Anonymous penalty dispute preserved without named assignment.',42:'Sentence read across page to 4a:1; same-courtyard condition retained.',43:'Other-courtyard continuation, Rava/Rav Nahman roles, both questions and contrary answers retained.',44:'Intention distinction retained with speaker-context qualification; salt retort preserved in utterance evidence.',45:'Repeated occurrence of oven question retained; later explicit affirmative version not back-projected.',46:'No-memory case and speaker/addressee roles separated.',47:'Remembered case and beginning/end inadvertence requirement preserved.',48:'Deliberate case and sin-offering/stoning wording contrast retained.',49:'Others as permitted agents preserved; proposal later rejected.',50:'Rhetorical objection retained without universalizing beyond context.',51:'Rav Ashi correction separated from Rav Aha son of Rava transmission of affirmative Rav Bibi version; different individuals from Rav Aha bar Abaye.'}
coverage=[]
for i in range(32,52):
 for layer in x.layers:
  rs=[r['id'] for r in x.records if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==x.inv[i]['id'] for e in r['evidence'])]
  coverage.append(dict(segment_id=x.inv[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if rs else 'none_found_after_pass',record_ids=rs,rationale=('Source reread: ' if layer=='reconciliation' else 'Direct source '+layer+' pass: ')+notes[i]+(' No separate record found in this layer.' if not rs else '')))
p={k:x.meta[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']}
p.update(owner='L05/shabbat',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=x.records,coverage=coverage,open_tails=[])
b=(json.dumps(p,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode(); out=x.W/'hand_bread_3b3_4a9_v1.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(len(x.records),'records')
