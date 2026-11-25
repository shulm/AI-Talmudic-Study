"""Manual reading 2a:6-2b:1; future source was inspected through 3b:13."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'))
import runner
JOB=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
j,ss=runner.load(JOB); byref={r['ref'].removeprefix('Eruvin '):r for r in ss.values()}
records=[]
def add(key,layer,refs,content,links=(),uncertainty=(),origin='source_paraphrase'):
    rid='er.derivation.002.'+layer+'.'+key
    evidence=[dict(segment_id=byref[r]['id'],start_char=0,end_char=len(byref[r]['text']),quote=byref[r]['text']) for r in refs]
    records.append(dict(id=rid,layer=layer,evidence=evidence,content=content,links=list(links),uncertainty=list(uncertainty),origin=origin));return rid
def c(key,ref,p,mode='asserted',conditions=(),scope='Temple-opening derivation and terminology',uncertainty=()):
    return add(key,'claims',[ref],dict(proposition=p,conditions=list(conditions),scope=scope,assertion_mode=mode),uncertainty=uncertainty)
def q(key,ref,p,conditions=()):
    return add(key,'questions',[ref],dict(formulation=p,question_origin='explicit',conditions=list(conditions),answer_set_status='unreviewed_alternatives'))
def a(key,ref,surface,role,people,scope,chain=()):
    return add(key,'attributions',[ref],dict(surface=surface,role=role,candidates=people,scope=scope,transmission_chain=list(chain)))
def p(key,ref,holder,claim,status='Textual position in the present report; not a final practical ruling'):
    return add(key,'positions',[ref],dict(holder_candidates=[holder],claim_id=claim,question_id=None,conditions=[],local_status=status),[claim])
def e(key,refs,src,tgt,rel):
    return add(key,'edges',refs,dict(source_id=src,target_id=tgt,relation=rel,explicitness='source_explicit'),[src,tgt])
refs=['2a:'+str(i) for i in range(6,15)]+['2b:1']
structure=add('structure','structure',refs,dict(title='לימוד מפתחי היכל ואולם ומונחי מקדש ומשכן',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference',uncertainty=['Continuation beginning 2b:2 through 3a:11 has been read but not yet promoted; objections and Rav Hisda/Rav Nahman bar Yitzhak alternatives must remain attached.'])
voices={
'2a:6':('Rav reported by Rav Yehuda','Reported explanations of the two height positions'),
'2a:7':('Anonymous Gemara quoting a mishnah','Temple dimensions offered as support'),
'2a:8':('Anonymous exposition of the Rabbis','Shared verse and distinct-sanctity rationale'),
'2a:9':('Anonymous exposition of Rabbi Yehuda','Unified-sanctity rationale in first account'),
'2a:10':('Anonymous alternative exposition','Separate sanctity with a different doorway verse'),
'2a:11':('Anonymous exposition of the Rabbis','Response to the alternative verse interpretation'),
'2a:12':('Anonymous questioner','Tabernacle versus Temple objection'),
'2a:13':('Anonymous Gemara with Rav Yehuda reporting Shmuel','Terminological answer and sacrificial precedent'),
'2a:14':('Anonymous Gemara','Proof, question, and proposed proof'),
'2b:1':('Anonymous Gemara','Rejection of proposed proof and replacement proof')}
for ref,(voice,role) in voices.items():
    add('u.'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'),origin='editorial_inference')
c1=c('rav.rabbis','2a:6','Rav, as reported by Rav Yehuda, derives the Rabbis’ limit from the opening of the Heikhal.',scope='Rav’s reported explanation, contested later at 2b:11 and 3a:8',uncertainty=['Later explanations must not be silently attributed to Rav.'])
c2=c('rav.yehuda','2a:6','Rav, as reported by Rav Yehuda, derives Rabbi Yehuda’s view from the opening of the Ulam.',scope='Rav’s reported explanation, challenged by higher permitted heights at 2b:9-11',uncertainty=['Rav Hisda later contests this explanation; this is not a source-attested retraction by Rav.'])
c3=c('dimensions.heikhal','2a:7','The quoted mishnah gives the Heikhal opening a height of twenty cubits and width of ten.')
c4=c('dimensions.ulam','2a:7','The quoted mishnah gives the Ulam opening a height of forty cubits and width of twenty.')
c5=c('shared.verse','2a:8','Both positions are initially explained as deriving from the same verse, ושחטו פתח אהל מועד.')
c6=c('rabbis.sanctity','2a:8','In this exposition the Rabbis distinguish the sanctity of Heikhal and Ulam.')
c7=c('rabbis.verse','2a:8','For the Rabbis, פתח אהל מועד refers to the Heikhal.',conditions=['Heikhal and Ulam have separate sanctity'])
c8=c('yehuda.sanctity','2a:9','The first exposition of Rabbi Yehuda treats Heikhal and Ulam as one sanctity.',scope='First anonymous explanation of Rabbi Yehuda; an alternative follows')
c9=c('yehuda.verse','2a:9','In that first exposition, פתח אהל מועד refers to both Heikhal and Ulam.',conditions=['Heikhal and Ulam have one sanctity'])
c10=c('alternative.sanctity','2a:10','An alternative explanation grants that Rabbi Yehuda too separates the sanctities of Ulam and Heikhal.',mode='hypothetical',scope='Alternative explanation, not a retraction by Rabbi Yehuda')
c11=c('alternative.verse','2a:10','The alternative bases Rabbi Yehuda’s reasoning on אל פתח אולם הבית.',scope='Alternative anonymous explanation of Rabbi Yehuda')
c12=c('rabbis.counterfactual','2a:11','The Rabbis would accept the proposed reading if the wording were אל פתח אולם.',mode='hypothetical',conditions=['Counterfactual wording omitting הבית'])
c13=c('rabbis.house','2a:11','The Rabbis interpret the actual wording אל פתח אולם הבית as the house opening into the Ulam.')
q1=q('q.tabernacle','2a:12','How can this opening verse be applied to the Temple when it was written about the Tabernacle?')
c14=c('terms.interchange','2a:13','The response observes that the Tabernacle is called מקדש and the Temple is called משכן.')
c15=c('shmuel.invalid','2a:13','Shmuel, reported by Rav Yehuda, invalidates peace-offerings slaughtered before the Heikhal doors are opened.',conditions=['peace-offerings','slaughter before opening the Heikhal doors'])
c16=c('shmuel.derivation','2a:13','The quoted derivation reads ושחטו פתח אהל מועד as requiring open doors rather than closed doors.',scope='Derivation within the reported Shmuel statement')
q2=q('q.shmuel.parallel','2a:13','Would not the same Tabernacle-context objection undermine the quoted Temple-door ruling?',conditions=['If the Temple could not be called by Tabernacle terminology'])
c17=c('temple.called.tabernacle','2a:14','ונתתי (את) משכני בתוככם is adduced as evidence that the Temple is called משכן.')
q3=q('q.reverse.term','2a:14','Where is the Tabernacle called מקדש?')
c18=c('proposed.kohath','2a:14','The text provisionally proposes הקהתים נושאי המקדש as the proof that the Tabernacle is called מקדש.',mode='rejected',scope='Proposed proof explicitly rejected in next segment 2b:1')
c19=c('kohath.ark','2b:1','The proposed Kohathite verse concerns the Ark, so it does not establish the proposed naming proof.')
c20=c('replacement.proof','2b:1','ועשו לי מקדש ושכנתי בתוכם is instead adduced to establish that the Tabernacle is called מקדש.')
for key,ref,surface,role,people,scope,chain in [
 ('ravyehuda.rav','2a:6','אמר רב יהודה אמר רב','transmitter',['רב יהודה'],'Rav’s explanation of the Rabbis and Rabbi Yehuda',['רב יהודה','רב']),
 ('rav','2a:6','אמר רב','quoted_authority',['רב'],'Origin authority of reported derivations',['רב יהודה','רב']),
 ('rabbis.report','2a:6','חכמים','collective',['חכמים'],'Holders whose derivation Rav reports',[]),
 ('yehuda.report','2a:6','ורבי יהודה','position_holder',['רבי יהודה'],'Holder whose derivation Rav reports',[]),
 ('dimensions','2a:7','דתנן','anonymous',[],'Quoted mishnah gives dimensions',[]),
 ('rabbis.sanctity','2a:8','דרבנן סברי','collective',['רבנן'],'Distinct sanctities and Heikhal reading',[]),
 ('yehuda.first','2a:9','ורבי יהודה סבר','position_holder',['רבי יהודה'],'First exposition, not his direct quotation',[]),
 ('yehuda.alternative','2a:10',"לר' יהודה",'position_holder',['רבי יהודה'],'Alternative exposition only',[]),
 ('rabbis.reply','2a:11','ורבנן','collective',['רבנן'],'Interpretation of הבית',[]),
 ('objection','2a:12','והא כי כתיב','anonymous',[],'Tabernacle-context objection',[]),
 ('ravyehuda.shmuel','2a:13','רב יהודה אמר שמואל','transmitter',['רב יהודה'],'Temple-door ruling',['רב יהודה','שמואל']),
 ('shmuel','2a:13','אמר שמואל','quoted_authority',['שמואל'],'Peace-offering ruling',['רב יהודה','שמואל']),
 ('terms','2a:13','אשכחן','anonymous',[],'Terminological reconciliation',[]),
 ('proofs','2a:14','בשלמא','anonymous',[],'Proof search',[]),
 ('replacement','2b:1','ההוא בארון כתיב','anonymous',[],'Rejects candidate proof and gives another',[])]:
    a(key,ref,surface,role,people,scope,chain)
for key,ref,holder,cid,status in [
 ('rav.rabbis','2a:6','רב',c1,'Reported explanation; challenged later, no recorded self-retraction'),
 ('rav.yehuda','2a:6','רב',c2,'Reported explanation; challenged later, no recorded self-retraction'),
 ('rabbis.sanctity','2a:8','רבנן',c6,'Position as exposited by anonymous argument'),
 ('rabbis.verse','2a:8','רבנן',c7,'Verse interpretation in first account'),
 ('yehuda.sanctity','2a:9','רבי יהודה',c8,'First account only; alternative at 2a:10'),
 ('yehuda.verse','2a:9','רבי יהודה',c9,'First account only'),
 ('yehuda.alt.sanctity','2a:10','רבי יהודה',c10,'Alternative account; unresolved historical attribution'),
 ('yehuda.alt.verse','2a:10','רבי יהודה',c11,'Alternative account'),
 ('rabbis.house','2a:11','רבנן',c13,'Response to alternative explanation'),
 ('shmuel','2a:13','שמואל',c15,'Reported invalidity under explicitly stated condition'),
 ('shmuel.derivation','2a:13','שמואל',c16,'Derivation inside reported statement')]:
    rid=p(key,ref,holder,cid,status)
    # Retain claim conditions in the holder relation too.
    records[-1]['content']['conditions']=next(r['content']['conditions'] for r in records if r['id']==cid)
e('dimensions.heikhal',['2a:7'],c3,c1,'support');e('dimensions.ulam',['2a:7'],c4,c2,'support')
e('sanctity.rabbis',['2a:8'],c6,c7,'support');e('sanctity.yehuda',['2a:9'],c8,c9,'support')
e('rabbis.reply',['2a:11'],c13,c11,'objection')
e('terms.answer',['2a:13'],c14,q1,'answer')
e('shmuel.derivation',['2a:13'],c16,c15,'support')
e('shmuel.parallel',['2a:13'],c15,c14,'support')
e('shmuel.question',['2a:13'],q2,c15,'objection')
e('terms.parallel.answer',['2a:13'],c14,q2,'answer')
e('first.term.proof',['2a:14'],c17,c14,'support')
e('candidate.proof',['2a:14'],c18,q3,'answer')
e('reject.candidate',['2b:1'],c19,c18,'objection')
e('replacement.answer',['2b:1'],c20,q3,'answer')
coverage=[]
for ref in refs:
    sid=byref[ref]['id']
    for layer in runner.LAYERS:
        ids=[r['id'] for r in records if (layer=='reconciliation' or layer==r['layer']) and any(x['segment_id']==sid for x in r['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Source reread retained both explanations of Rabbi Yehuda, Rav/Rav Yehuda and Shmuel/Rav Yehuda transmission, conditions, rejected proof and replacement. Continuation through 3b:13 inspected; open structure awaits explicit continuation promotion.' if ids else 'Manual pass found no '+layer+' object needing a separate record in this segment.'))
proposal=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[structure])
out=Path(__file__).with_name('eruvin_derivation_002.json');runner.immutable(out,runner.encoded(proposal))
print(runner.submit(JOB,out,'L03/eruvin',2));print(runner.replay(JOB))
