"""Additive exact-version repairs for BB037-P001 and BB037-P002 only."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from scoped_reading import ScopedReading,r
a=ScopedReading('bava_batra','Bava Batra','bb.r036')
state=r.current(a.job);assert r.sha(r.encoded(state))=='45510ebd6b2486c0695e120808be45afa55e373ebad4eacae6d6fd2171842a9d'
assert r.read(a.job/'OWNER.json')==dict(owner='L04/bava_batra_resume_20261126',epoch=3)
quote='אמר מר היה סתום ובקש לפותחו אין בני מבוי מעכבין עליו'
u=a.speech('reopen_lemma','11b:12',quote,act='anonymous quotation of preceding baraita lemma')
cid=a.add('reopen_lemma.c','claims',dict(proposition='The anonymous discussion repeats the baraita lemma: residents cannot prevent reopening a previously closed entrance.',conditions=['previously closed entrance being reopened'],scope='Distinct repeated occurrence at11b:12 of Rabbi’s baraita clause at11b:10; Rava immediately limits it to retained doorposts.',assertion_mode='conditional'),['11b:12'],[u])
a.rows[-1]['evidence']=[a.span('11b:12',quote)]
a.add('reopen_lemma.quoted_authority','attributions',dict(surface='דברי רבי / אמר מר',role='quoted_authority',candidates=['רבי'],scope=cid,transmission_chain=[]),['11b:12','11b:10'],[cid],['Rabbi is the quoted baraita authority established at11b:10; the citing voice at11b:12 remains anonymous.'])
a.rows[-1]['evidence']=[a.span('11b:12',quote),a.evidence('11b:10')]
a.add('reopen_lemma.p','positions',dict(holder_candidates=['רבי'],claim_id=cid,question_id=None,conditions=['reopening prior entrance','Rava limits permission to doorposts not removed'],local_status='Quoted baraita rule repeated and immediately qualified; no new independent doctrine'),['11b:12'],[cid])
a.rows[-1]['evidence']=[a.span('11b:12',quote)]
a.e('reopen_quotation',cid,'bb.r032.reopen.c','quotation','11b:12')
a.rows[-1]['evidence']=[a.span('11b:12',quote)]
a.e('reopen_retained_qualification','bb.r032.retained.c',cid,'qualification','11b:12')
a.rows[-1]['evidence']=[a.span('11b:12','אמר רבא לא שנו אלא שלא פרץ את פצימיו')]
a.e('four_cubit_distinction','bb.r032.nopost.c','bb.r032.closed.c','distinction','12a:1')
active=[x for x in state['records'] if x['release_state']=='valid']+a.rows
coverage=[]
for ref in ['11b:10','11b:12','12a:1']:
 for layer in r.LAYERS:
  sid=a.refs[ref]['id'];ids=[x['id'] for x in active if x['layer']==layer and any(ev['segment_id']==sid for ev in x['evidence'])]
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='BB037 targeted source reread11b:10–12a:4. P001 adds distinct repeated lemma with anonymous quoting voice, Rabbi quoted authority, quotation relation and Rava qualification; P002 adds retained/lost four-cubit distinction. Existing source occurrences and all prior objects preserved. '+layer+' pass reconciled; no new source coverage or independent acceptance.'))
p=dict(schema_version=r.VERSION,tractate=a.title,owner='L04/bava_batra_resume_20261126',epoch=3,source_sha256=a.meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root/bava_batra_continuation_2',model_id=None),records=a.rows,coverage=coverage,open_tails=state['open_tails'])
r.validate_apply(state,p,a.source,a.meta)
out=a.job/'staging'/'next_release_20261127_bb037_repair036.json';r.immutable(out,r.encoded(p));print(out)
