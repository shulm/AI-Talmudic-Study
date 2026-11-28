"""Manually authored cubit-measure dispute, Eruvin 3b:6-4a:9."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6];sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin');j,ss=runner.load(JOB)
byref={r['ref'].removeprefix('Eruvin '):r for r in ss.values()};records=[];cs={};qs={}
def add(key,layer,refs,content,links=(),origin='source_paraphrase',uncertainty=()):
 rid='er.cubits.001.'+layer+'.'+key
 records.append(dict(id=rid,layer=layer,evidence=[dict(segment_id=byref[r]['id'],start_char=0,end_char=len(byref[r]['text']),quote=byref[r]['text']) for r in refs],content=content,links=list(links),origin=origin,uncertainty=list(uncertainty)));return rid
refs=['3b:'+str(i) for i in range(6,23)]+['4a:'+str(i) for i in range(1,10)]
add('structure','structure',refs,dict(title='מסורות אביי ורבא בשם רב נחמן על מידות האמה',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
# key, ref, proposition, assertion mode, conditions, holder (if text attributes it)
spec=[
('abaye.five','3b:6','Abaye reports Rav Nahman: sukkah and mavoi cubits have five handbreadths.','asserted',[],'רב נחמן'),
('abaye.six','3b:6','In Abaye’s report, kilayim cubits have six handbreadths.','asserted',[],'רב נחמן'),
('mavoi.apply','3b:7','The five-handbreadth mavoi measure applies to height and a breach.','asserted',[],None),
('mavoi.leniency','3b:8','A four-cubit mavoi length requirement would become more lenient with five-handbreadth cubits.','challenged',['four-cubit length requirement'],None),
('mavoi.four.hand','3b:9','One answer adopts the view measuring required mavoi length in four handbreadths.','asserted',[],None),
('mavoi.most','3b:10','Alternatively the four-cubit length remains, but the five-handbreadth statement refers to most cubits.','asserted',[],None),
('sukkah.apply','3b:11','The five-handbreadth sukkah measure applies to height and bent-wall allowance.','asserted',[],None),
('sukkah.rabbi','3b:12','Rabbi invalidates a sukkah smaller than four cubits by four cubits.','asserted',['area smaller than four by four cubits'],'רבי'),
('sukkah.leniency','3b:12','The objection notes the smaller cubit would make Rabbi’s minimum area requirement lenient.','challenged',['Rabbi’s four-cubit minimum'],None),
('sukkah.rabbis','3b:13','One answer follows the Rabbis, who allow a sukkah accommodating only head, most of the body, and table.','asserted',[],'רבנן'),
('sukkah.most','3b:14','Alternatively Rabbi’s view can stand because the statement concerns most cubits.','asserted',[],None),
('kilayim.apply','3b:15','The six-handbreadth measure applies to the vineyard’s central clearing and its perimeter strip.','asserted',[],None),
('clearing.bsh','3b:16','Beit Shammai give the central clearing measure as twenty-four cubits.','asserted',[],'בית שמאי'),
('clearing.bh','3b:16','Beit Hillel give the central clearing measure as sixteen cubits.','asserted',[],'בית הלל'),
('perimeter.bsh','3b:16','Beit Shammai give the perimeter-strip measure as sixteen cubits.','asserted',[],'בית שמאי'),
('perimeter.bh','3b:16','Beit Hillel give the perimeter-strip measure as twelve cubits.','asserted',[],'בית הלל'),
('clearing.definition','3b:17','A vineyard central clearing is a vineyard whose middle has been destroyed.','asserted',[],None),
('clearing.prohibit','3b:17','If the clearing lacks sixteen cubits one must not plant seed there.','conditional',['clearing less than sixteen cubits'],None),
('clearing.allow','3b:17','With sixteen cubits, reserve the cultivation space and sow the remainder.','conditional',['clearing has sixteen cubits','cultivation space reserved'],None),
('perimeter.definition','3b:18','The perimeter strip is the space between the vineyard and its fence.','asserted',[],None),
('perimeter.prohibit','3b:18','With less than twelve cubits in that strip one must not plant seed there.','conditional',['strip less than twelve cubits'],None),
('perimeter.allow','3b:18','With twelve cubits, reserve cultivation space and sow the rest.','conditional',['strip has twelve cubits','cultivation space reserved'],None),
('dense.shimon','3b:19','Rabbi Shimon does not classify planting spaced less than four cubits as a vineyard.','asserted',['spacing less than four cubits'],'רבי שמעון'),
('dense.rabbis','3b:19','The Sages classify it as a vineyard and regard intermediate vines as absent.','asserted',['spacing less than four cubits'],'חכמים'),
('dense.leniency','3b:19','The objection notes that using larger cubits for the four-cubit dense-planting threshold could be lenient.','challenged',['Rabbi Shimon’s classification'],None),
('dense.answer','3b:20','One answer follows the Rabbis who still classify dense planting as a vineyard.','asserted',[],None),
('dense.most','3b:20','Alternatively Rabbi Shimon can stand and the statement concerns most cubits.','asserted',[],None),
('rava.six','3b:21','Rava reports Rav Nahman that all these cubits have six handbreadths, with some expansive and some tight.','asserted',[],'רב נחמן'),
('baraita.all','3b:22','The objection begins citing a baraita that all cubits specified by the Sages have six handbreadths.','asserted',[],None),
('baraita.qualification','4a:1','The baraita continues that these measures should not be exact; this fits Rava’s expansive/tight distinction but challenges Abaye.','asserted',[],None),
('abaye.reread','4a:2','The reply formulated for Abaye reads the baraita as referring specifically to kilayim cubits.','hypothetical',[],'אביי'),
('rashbag','4a:3','Rabban Shimon ben Gamliel specifies that all cubits stated by the Sages in kilayim have six handbreadths and must not be compressed.','asserted',[],'רבן שמעון בן גמליאל'),
('first.tanna','4a:3','The objection infers from Rabban Shimon ben Gamliel’s explicit kilayim wording that the first tanna referred to all cubits.','asserted',[],None),
('abaye.rashbag','4a:4','The anonymous defense formulated for Abaye adopts Rabban Shimon ben Gamliel as a supporting tanna.','hypothetical',[],'אביי'),
('abaye.dispute','4a:5','For Abaye the accounts necessarily reflect a tannaitic dispute.','asserted',[],None),
('rava.rashbag','4a:6','The reply formulated for Rava says Rabban Shimon ben Gamliel teaches that kilayim cubits must not be compressed.','hypothetical',[],'רבא'),
('excluded.five','4a:7','The question proposes that specifying six excludes sukkah and mavoi cubits.','queried',[],None),
('altar.exclusion','4a:8','The answer instead excludes the altar’s foundation cubit and ledge cubit.','asserted',[],None),
('altar.verse','4a:9','The verse is expounded: חיק האמה denotes the foundation; אמה רחב the ledge; גבולה אל שפתה סביב the horns; גב המזבח the golden altar.','asserted',[],None)]
for key,ref,text,mode,conditions,holder in spec:
 scope='Abaye/Rava reports and alternative anonymous replies; do not identify the two reports as a chronological retraction'
 cs[key]=add(key,'claims',[ref],dict(proposition=text,conditions=conditions,scope=scope,assertion_mode=mode))
 if holder:
  add(key,'positions',[ref],dict(holder_candidates=[holder],claim_id=cs[key],question_id=None,conditions=conditions,local_status='Hypothetical defense on named authority’s behalf' if mode=='hypothetical' else 'Source-attributed position in specified report'),[cs[key]])
for key,rr,text in [
('mavoi.application',['3b:7'],'For which mavoi laws is the five-handbreadth measure used?'),
('mavoi.counter',['3b:8'],'Would a four-cubit minimum length not make the shorter cubit lenient?'),
('sukkah.application',['3b:11'],'For which sukkah laws is the five-handbreadth measure used?'),
('sukkah.counter',['3b:12'],'Would Rabbi’s four-cubit minimum size not become lenient?'),
('kilayim.application',['3b:15'],'For which kilayim rules is the six-handbreadth measure used?'),
('clearing.definition',['3b:17'],'What is the central vineyard clearing?'),
('perimeter.definition',['3b:18'],'What is the vineyard perimeter strip?'),
('dense.counter',['3b:19'],'Would the dense-planting four-cubit measure not be lenient?'),
('baraita.challenge',['3b:22','4a:1'],'How can Abaye fit a baraita saying all cubits have six handbreadths?'),
('first.tanna',['4a:3'],'Does Rabban Shimon ben Gamliel’s specific clause not show the first tanna meant all cubits?'),
('rava.tannaim',['4a:5'],'Must Rava too treat this as a tannaitic dispute?'),
('exclusion',['4a:7'],'Why specify six handbreadths: does this not exclude sukkah and mavoi?')]:
 qs[key]=add(key,'questions',rr,dict(formulation=text,question_origin='explicit',conditions=[],answer_set_status='unreviewed_alternatives'))
for ref in refs:
 voice='anonymous Gemara with quoted sources'
 if ref=='3b:6':voice='Abaye reporting Rav Nahman'
 if ref=='3b:21':voice='Rava reporting Rav Nahman'
 add(ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='measure rule, definition, objection, or local response as specified by attached claims/questions',composition='composite'),origin='editorial_inference')
 if ref not in ['3b:6','3b:21']:
  add('anon.'+ref.replace(':','_'),'attributions',[ref],dict(surface='anonymous framing',role='anonymous',candidates=[],scope='Local source framing or anonymous definition; no named historical author assigned',transmission_chain=[]))
for key,ref,surface,role,names,scope,chain in [
('abaye','3b:6','אמר אביי משמיה דרב נחמן','transmitter',['אביי'],'Five/six cubit report',['אביי','רב נחמן']),
('nahman.abaye','3b:6','משמיה דרב נחמן','quoted_authority',['רב נחמן'],'Authority in Abaye’s report',['אביי','רב נחמן']),
('rabbi','3b:12','רבי אומר','quoted_authority',['רבי'],'Four by four minimum',[]),
('rabbis.sukkah','3b:13','כרבנן דאמרי','collective',['רבנן'],'Head, body, table minimum',[]),
('bsh','3b:16','ב"ש אומרים','collective',['בית שמאי'],'24 clearing and 16 perimeter',[]),
('bh','3b:16','ב"ה אומרים','collective',['בית הלל'],'16 clearing and 12 perimeter',[]),
('shimon','3b:19','רבי שמעון אומר','quoted_authority',['רבי שמעון'],'Dense planting not vineyard',[]),
('dense.rabbis','3b:19','וחכמים אומרים','collective',['חכמים'],'Dense planting is vineyard',[]),
('rava','3b:21','ורבא משמיה דר"נ אמר','transmitter',['רבא'],'Six with expansive/tight distinctions',['רבא','רב נחמן']),
('nahman.rava','3b:21','משמיה דר"נ','quoted_authority',['רב נחמן'],'Authority in Rava’s report',['רבא','רב נחמן']),
('abaye.reply1','4a:2','אמר לך אביי','quoted_authority',['אביי'],'Anonymous hypothetical defense',[]),
('rashbag','4a:3','רשב"ג אומר','quoted_authority',['רבן שמעון בן גמליאל'],'Kilayim six cubits noncompressed',[]),
('abaye.reply2','4a:4','אמר לך אביי','quoted_authority',['אביי'],'Anonymous hypothetical reliance on Rashbag',[]),
('rava.reply','4a:6','אמר לך רבא','quoted_authority',['רבא'],'Anonymous hypothetical reading of Rashbag',[])]:
 add(key,'attributions',[ref],dict(surface=surface,role=role,candidates=names,scope=scope,transmission_chain=chain))
for key,ref,src,tgt in [
('mavoi.apply','3b:7','mavoi.apply','mavoi.application'),('mavoi.four','3b:9','mavoi.four.hand','mavoi.counter'),('mavoi.most','3b:10','mavoi.most','mavoi.counter'),
('sukkah.apply','3b:11','sukkah.apply','sukkah.application'),('sukkah.rabbis','3b:13','sukkah.rabbis','sukkah.counter'),('sukkah.most','3b:14','sukkah.most','sukkah.counter'),
('kilayim.apply','3b:15','kilayim.apply','kilayim.application'),('clearing.definition','3b:17','clearing.definition','clearing.definition'),('perimeter.definition','3b:18','perimeter.definition','perimeter.definition'),
('dense.rabbis','3b:20','dense.answer','dense.counter'),('dense.most','3b:20','dense.most','dense.counter'),('abaye.reread','4a:2','abaye.reread','baraita.challenge'),
('abaye.rashbag','4a:4','abaye.rashbag','first.tanna'),('rava.reply','4a:6','rava.rashbag','rava.tannaim'),('altar.exclusion','4a:8','altar.exclusion','exclusion')]:
 add(key,'edges',[ref],dict(source_id=cs[src],target_id=qs[tgt],relation='answer',explicitness='source_explicit'),[cs[src],qs[tgt]])
for key,ref,src,tgt,rel in [
('first.tanna.objection','4a:3','first.tanna','abaye.reread','objection'),('altar.support','4a:9','altar.verse','altar.exclusion','support'),('rashbag.support','4a:4','rashbag','abaye.rashbag','support')]:
 add(key,'edges',[ref],dict(source_id=cs[src],target_id=cs[tgt],relation=rel,explicitness='source_explicit'),[cs[src],cs[tgt]])
coverage=[]
for ref in refs:
 seg=byref[ref]['id']
 for layer in runner.LAYERS:
  ids=[r['id'] for r in records if (layer=='reconciliation' or r['layer']==layer) and any(x['segment_id']==seg for x in r['evidence'])]
  coverage.append(dict(segment_id=seg,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Manual source and omission reread retained numeric thresholds, cultivation reservations, alternative majority-of-measures replies, named transmission and hypothetical defenses. Page boundary 3b:22/4a:1 retained as continuation.' if ids else 'Actual pass found no separate '+layer+' record in this source segment.'))
p=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=Path(__file__).with_name('eruvin_cubits_001.json');runner.immutable(out,runner.encoded(p));print(runner.submit(JOB,out,'L03/eruvin',2));print(runner.replay(JOB))
