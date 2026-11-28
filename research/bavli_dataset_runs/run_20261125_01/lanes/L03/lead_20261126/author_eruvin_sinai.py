"""Manual source reading: Eruvin 4a:10–4b:17; no automatic semantic extraction."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
j,ss=runner.load(JOB)
assert runner.sha(runner.encoded(runner.current(JOB)))=='34f1e84481eca5a2e7e6180ea23ab306ee9b68b99118f960f6fb1ca47d3e3fe0'
byref={r['ref'].removeprefix('Eruvin '):r for r in ss.values()}
refs=['4a:'+str(n) for n in range(10,15)]+['4b:'+str(n) for n in range(1,18)]
records=[];cs={};qs={}
def add(key,layer,rr,content,links=(),origin='source_paraphrase',uncertainty=()):
 rid='er.sinai.001.'+layer+'.'+key
 records.append(dict(id=rid,layer=layer,evidence=[dict(segment_id=byref[r]['id'],start_char=0,end_char=len(byref[r]['text']),quote=byref[r]['text']) for r in rr],content=content,links=list(links),origin=origin,uncertainty=list(uncertainty)))
 return rid
add('unit','structure',refs,dict(title='שיעורין חציצין ומחיצין: תחומי ההלכה למשה מסיני',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
spec=[
('rav.measures','4a:10','Measures are halakha to Moses at Sinai.','asserted',[],'רב'),
('rav.barriers','4a:10','Interposition rules are halakha to Moses at Sinai.','asserted',[],'רב'),
('rav.partitions','4a:10','Partition rules are halakha to Moses at Sinai.','asserted',[],'רב'),
('hanan','4a:11','Rav Hanan says the whole land-of-seven-species verse was stated for measures.','asserted',[],'רב חנן'),
('house.carried','4a:12','One entering a leprous house with clothes on the shoulders and sandals and rings in the hands becomes impure immediately, together with those carried objects.','conditional',['entry into a leprous house','objects carried, not worn'],None),
('house.person','4a:12','A person entering the leprous house while wearing the clothes, sandals and rings becomes impure immediately.','conditional',['entry into a leprous house','objects worn'],None),
('house.worn','4a:12','The worn objects remain pure until the person stays long enough to eat a peras.','conditional',['objects worn on entry','duration less than eating a peras'],None),
('wheat.standard','4a:12','The peras-duration standard uses wheat bread, not barley bread, eaten reclining with accompaniment.','asserted',['leprous-house duration standard'],None),
('bone.contact','4a:13','A barley-sized bone imparts impurity by contact.','conditional',['bone the size of a barley grain'],None),
('bone.carry','4a:13','A barley-sized bone imparts impurity by carrying.','conditional',['bone the size of a barley grain'],None),
('bone.tent','4a:13','A barley-sized bone does not impart impurity by tent.','conditional',['bone the size of a barley grain'],None),
('vine','4a:14','The vine is associated with a quarter-log wine measure for a nazir.','asserted',[],None),
('fig','4b:1','The fig is associated with a dried-fig measure for Shabbat carrying.','asserted',[],None),
('pomegranate','4b:2','Householders’ utensils have a pomegranate-size measure.','asserted',['householders’ utensils'],None),
('olive.all','4b:3','An initial exposition calls the land one whose measures are all olive-sized.','hypothetical',[],None),
('olive.most','4b:3','The corrected exposition says most measures are olive-sized.','asserted',[],None),
('date','4b:4','Honey is associated with the large-date measure for Yom Kippur.','asserted',[],None),
('measures.halakha','4b:5','The measures are received halakha; the Sages attached them to verses as supporting allusions.','asserted',[],None),
('barrier.verse','4b:6','The washing verse requires no object to intervene between flesh and water.','asserted',[],None),
('mikveh','4b:6','The water in the washing verse is mikveh water.','asserted',[],None),
('body.water','4b:6','All his flesh requires water in which the whole body can enter.','asserted',[],None),
('volume.dimensions','4b:6','The bodily immersion volume is a cubit by a cubit, three cubits high.','asserted',[],None),
('volume.seah','4b:6','The Sages estimated that mikveh volume as forty seah.','asserted',[],'חכמים'),
('hair.proposal','4b:7','The initial answer locates the needed received law in hair.','hypothetical',[],None),
('hair.one','4b:7','Rabbah bar Rav Huna says a single tied hair interposes.','asserted',['one tied hair'],'רבה בר רב הונא'),
('hair.three','4b:7','Three tied hairs do not interpose in Rabbah bar Rav Huna’s statement.','asserted',['three tied hairs'],'רבה בר רב הונא'),
('hair.two','4b:7','Rabbah bar Rav Huna says he does not know the status of two tied hairs.','asserted',['two tied hairs'],'רבה בר רב הונא'),
('hair.verse','4b:8','A baraita derives the hair attached to the flesh from the washing verse.','asserted',[],None),
('barrier.scope','4b:9','The received law addresses majority/minority and whether one objects to the interposition.','asserted',[],None),
('yitzhak.major','4b:10','Rabbi Yitzhak says a majority interposition to which one objects interposes by Torah law.','conditional',['majority','one objects'],'רבי יצחק'),
('yitzhak.not.care','4b:10','An interposition to which one does not object does not interpose by Torah law.','conditional',['one does not object'],'רבי יצחק'),
('decree.major','4b:10','A decree covers a majority interposition without objection on account of majority with objection.','conditional',['majority','one does not object'],'רבי יצחק'),
('decree.minor','4b:10','A decree covers a minority interposition with objection on account of majority with objection.','conditional',['minority','one objects'],'רבי יצחק'),
('no.double','4b:12','The cited restricted cases are themselves decrees; the response declines to add a decree upon a decree.','asserted',['suggested extension to minority without objection'],None),
('ark','4b:14','The ark’s nine handbreadths and the cover’s one handbreadth total ten.','asserted',[],None),
('yehuda.building','4b:15','Rabbi Yehuda says the building cubit has six handbreadths.','asserted',[],'רבי יהודה'),
('yehuda.vessels','4b:15','Rabbi Yehuda says the utensils cubit has five handbreadths.','asserted',[],'רבי יהודה'),
('yehuda.need','4b:15','The answer locates the need for the received partition rule in Rabbi Yehuda’s differing cubits.','asserted',['Rabbi Yehuda’s cubit account'],None),
('meir','4b:16','Rabbi Meir says all cubits were of the middle measure.','asserted',[],'רבי מאיר'),
('gud','4b:17','For Rabbi Meir the received law supplies gud.','asserted',['Rabbi Meir’s cubit account'],None),
('lavud','4b:17','For Rabbi Meir the received law supplies lavud.','asserted',['Rabbi Meir’s cubit account'],None),
('bent.wall','4b:17','For Rabbi Meir the received law supplies bent-wall treatment.','asserted',['Rabbi Meir’s cubit account'],None)]
for key,ref,text,mode,conditions,holder in spec:
 unc=['Source gives no determination for two hairs; preserve explicit uncertainty.'] if key=='hair.two' else []
 cs[key]=add(key,'claims',[ref],dict(proposition=text,conditions=conditions,scope='Local discussion of the scope of received laws; initial replies are not final unrestricted rulings.',assertion_mode=mode),uncertainty=unc)
 if holder:add(key,'positions',[ref],dict(holder_candidates=[holder],claim_id=cs[key],question_id=None,conditions=conditions,local_status='Source-attributed report; hair.two is expressly undetermined' if key=='hair.two' else 'Attributed local statement'),[cs[key]],uncertainty=unc)
for key,rr,text in [
('measures',['4a:11'],'Are measures not scriptural, as the seven-species verse and Rav Hanan indicate?'),
('olive',['4b:3'],'Can every measure be olive-sized given the measures just listed?'),
('written',['4b:5'],'Are the measures themselves actually written in the verses?'),
('barrier',['4b:6'],'Are interposition rules not scriptural from the washing verse?'),
('volume',['4b:6'],'How much water accommodates the whole body?'),
('hair',['4b:8'],'Is hair not also scripturally included in the washing requirement?'),
('minority',['4b:11'],'Why not decree against minority without objection on account of minority with objection or majority without objection?'),
('partition',['4b:13','4b:14'],'Are partitions not scriptural through the ark-and-cover ten-handbreadth measure?'),
('meir',['4b:16'],'What need remains for the received partition law according to Rabbi Meir’s uniform cubits?')]:
 qs[key]=add(key,'questions',rr,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='unreviewed_alternatives'))
for ref in refs:
 voice={'4a:10':'Rabbi Hiyya bar Ashi reporting Rav','4a:11':'anonymous objection quoting Rav Hanan','4b:7':'anonymous reply quoting Rabbah bar Rav Huna','4b:10':'Rabbi Yitzhak’s quoted formulation'}.get(ref,'anonymous Gemara with cited source where present')
 add(ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='received-law scope discussion: claims and questions separately represented',composition='composite'),origin='editorial_inference')
 if ref!='4a:10' and ref!='4b:10':add('anon.'+ref.replace(':','_'),'attributions',[ref],dict(surface='anonymous framing',role='anonymous',candidates=[],scope='Anonymous framing only; quoted authorities separately retained',transmission_chain=[]))
for key,ref,surface,role,names,scope,chain in [
('hiya','4a:10',"אמר ר' חייא בר אשי אמר רב",'transmitter',['רבי חייא בר אשי'],'Reports three received-law categories',['רבי חייא בר אשי','רב']),
('rav','4a:10','אמר רב','quoted_authority',['רב'],'Authority for three received-law categories',['רבי חייא בר אשי','רב']),
('hanan','4a:11','ואמר רב חנן','quoted_authority',['רב חנן'],'Seven-species verse interpreted for measures',[]),
('sages','4b:6','ושיערו חכמים','collective',['חכמים'],'Forty-seah estimate',[]),
('rabbah','4b:7','דאמר רבה בר רב הונא','quoted_authority',['רבה בר רב הונא'],'One/three hairs and uncertainty for two',[]),
('yitzhak','4b:10',"דאמר ר' יצחק",'quoted_authority',['רבי יצחק'],'Majority and objection distinctions',[]),
('yehuda','4b:15',"לר' יהודה דאמר",'quoted_authority',['רבי יהודה'],'Building and utensil cubits',[]),
('meir','4b:16','ולר"מ דאמר','quoted_authority',['רבי מאיר'],'All cubits middle measure',[])]:
 add(key,'attributions',[ref],dict(surface=surface,role=role,candidates=names,scope=scope,transmission_chain=chain))
for key,ref,src,tgt,rel in [
('hanan.challenge','4a:11','hanan','rav.measures','objection'),
('olive.correct','4b:3','olive.most','olive.all','correction'),
('barrier.challenge','4b:6','barrier.verse','rav.barriers','objection'),
('hair.challenge','4b:8','hair.verse','hair.proposal','objection'),
('major.scope','4b:10','yitzhak.major','barrier.scope','support'),
('partition.challenge','4b:14','ark','rav.partitions','objection'),
('yehuda.basis','4b:15','yehuda.vessels','yehuda.need','support')]:
 add(key,'edges',[ref],dict(source_id=cs[src],target_id=cs[tgt],relation=rel,explicitness='source_explicit'),[cs[src],cs[tgt]])
for key,ref,src,tgt in [
('measure.reply','4b:5','measures.halakha','measures'),('olive.reply','4b:3','olive.most','olive'),
('volume.reply','4b:6','volume.dimensions','volume'),('hair.proposed','4b:7','hair.proposal','barrier'),
('hair.reply','4b:9','barrier.scope','hair'),('minority.reply','4b:12','no.double','minority'),
('partition.reply','4b:15','yehuda.need','partition'),('meir.gud','4b:17','gud','meir'),('meir.lavud','4b:17','lavud','meir'),('meir.bent','4b:17','bent.wall','meir')]:
 add(key,'edges',[ref],dict(source_id=cs[src],target_id=qs[tgt],relation='answer',explicitness='source_explicit'),[cs[src],qs[tgt]])
coverage=[]
for ref in refs:
 seg=byref[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in records if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg for e in r['evidence'])]
  coverage.append(dict(segment_id=seg,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source-based omission reread: seven-species sequence, carried/worn distinction, majority/minority decrees, explicit two-hair uncertainty, rejected hair-only reply, and Rabbi Yehuda/Meir scope retained; subsequent 4b:18 begins a new mavoi-height case.' if ids else 'Read source and continuation; no separate '+layer+' record in this segment.'))
p=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=Path(__file__).with_name('eruvin_sinai_002.json');runner.immutable(out,runner.encoded(p));print(runner.submit(JOB,out,'L03/eruvin',2));print(runner.replay(JOB))
