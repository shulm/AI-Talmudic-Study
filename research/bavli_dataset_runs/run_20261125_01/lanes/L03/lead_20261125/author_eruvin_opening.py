"""Frozen manual reading of Eruvin 2a:1-5; serialization is not extraction."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / 'research/bavli_production_v1'))
import runner

JOB = Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_eruvin')
j, segments = runner.load(JOB)
byref = {r['ref'].removeprefix('Eruvin '): r for r in segments.values()}
records = []

def ev(ref, quote=None):
    row = byref[ref]
    text = row['text']
    quote = text if quote is None else quote
    start = text.index(quote)
    return dict(segment_id=row['id'], start_char=start, end_char=start+len(quote), quote=quote)

def add(key, layer, refs, content, links=(), origin='source_paraphrase', uncertainty=()):
    rid = 'er.opening.001.' + key
    records.append(dict(id=rid, layer=layer, evidence=[ev(ref) for ref in refs],
                        content=content, origin=origin, uncertainty=list(uncertainty),
                        links=list(links)))
    return rid

def claim(key, ref, proposition, conditions=(), mode='asserted', scope='Opening mishnah and its wording discussion'):
    return add(key, 'claims', [ref], dict(proposition=proposition, conditions=list(conditions), scope=scope, assertion_mode=mode))

def position(key, ref, holder, cid, conditions=(), status='stated in this local text'):
    return add(key, 'positions', [ref], dict(holder_candidates=[holder], claim_id=cid, question_id=None, conditions=list(conditions), local_status=status), [cid])

def edge(key, ref, source, target, relation):
    return add(key, 'edges', [ref], dict(source_id=source,target_id=target,relation=relation,explicitness='source_explicit'),[source,target])

add('mishnah', 'structure', ['2a:1','2a:2'], dict(title='מבוי: גובה, רוחב וצורת הפתח במשנה',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('wording', 'structure', ['2a:3','2a:4','2a:5'], dict(title='מדוע נשנתה תקנת מבוי לעומת פסלות סוכה',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('2a:1','anonymous mishnah and Rabbi Yehuda','contrasting height rulings'),('2a:2','anonymous mishnah','width rule and doorway-form exception'),('2a:3','anonymous Gemara quoting a mishnah','comparison and explicit wording question'),('2a:4','anonymous Gemara','first answer'),('2a:5','anonymous Gemara','alternative answer')]:
    add('u.'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite' if ref!='2a:4' else 'atomic'),origin='editorial_inference')
c1=claim('height.reduce','2a:1','A mavoi higher than twenty cubits must be reduced.', ['height exceeds twenty cubits'])
c2=claim('height.yehuda','2a:1','Rabbi Yehuda says reduction is unnecessary.', ['mavoi height exceeds twenty cubits'])
c3=claim('width.reduce','2a:2','A mavoi wider than ten cubits must be reduced.', ['width exceeds ten cubits'])
c4=claim('width.form','2a:2','A doorway form exempts a mavoi wider than ten cubits from reduction.', ['doorway form exists','width exceeds ten cubits'])
c5=claim('sukkah.invalid','2a:3','The quoted mishnah invalidates a sukkah higher than twenty cubits.', ['sukkah height exceeds twenty cubits'])
c6=claim('sukkah.yehuda','2a:3','The quoted Rabbi Yehuda validates that sukkah.', ['sukkah height exceeds twenty cubits'])
c7=claim('wording.observation','2a:3','The sukkah mishnah states invalidity while the mavoi mishnah states a remedy.')
q=add('q.wording','questions',['2a:3'],dict(formulation='Why does the sukkah mishnah say invalid while the mavoi mishnah states the remedy?',question_origin='explicit',conditions=['comparison of the two opening formulations'],answer_set_status='unreviewed_alternatives'),[c7])
c8=claim('answer.legal.level','2a:4','The first answer explains invalidity language by sukkah being Torah law and remedy language by mavoi being rabbinic.',scope='First anonymous explanation of wording; alternative follows')
c9=claim('alternative.torah','2a:5','The alternative allows remedy language even for Torah law.',scope='Alternative answer; does not deny the legal-level distinction itself')
c10=claim('alternative.many','2a:5','The sukkah has numerous relevant rules, so its mishnah states invalidity concisely.',scope='Alternative explanation of the mishnah wording')
c11=claim('alternative.few','2a:5','The mavoi has fewer relevant rules, so its mishnah states the remedy.',scope='Alternative explanation of the mishnah wording')
for key,ref,surface,role,candidates,scope in [
 ('a.mishnah','2a:1','מתני׳','anonymous',[],'Anonymous height ruling; do not resolve a named author'),
 ('a.yehuda','2a:1',"ר' יהודה אומר",'position_holder',['רבי יהודה'],'Height reduction exception'),
 ('a.width','2a:2','והרחב מעשר אמות ימעט','anonymous',[],'Anonymous width rule and its doorway-form exception'),
 ('a.quoted.mishnah','2a:3','תנן התם','anonymous',[],'Quoted anonymous sukkah ruling'),
 ('a.quoted.yehuda','2a:3','ורבי יהודה מכשיר','quoted_authority',['רבי יהודה'],'Quoted sukkah validation'),
 ('a.question','2a:3','מאי שנא','anonymous',[],'Wording comparison'),
 ('a.first.answer','2a:4','סוכה דאורייתא','anonymous',[],'First explanation; no named speaker'),
 ('a.alternative','2a:5','ואיבעית אימא','anonymous',[],'Alternative explanation, not an identified scholar')]:
    add(key,'attributions',[ref],dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=[]))
for key,ref,holder,cid,cond in [
 ('p.height','2a:1','anonymous mishnah',c1,['height exceeds twenty cubits']),
 ('p.height.yehuda','2a:1','רבי יהודה',c2,['height exceeds twenty cubits']),
 ('p.width','2a:2','anonymous mishnah',c3,['width exceeds ten cubits']),
 ('p.width.form','2a:2','anonymous mishnah',c4,['doorway form exists','width exceeds ten cubits']),
 ('p.sukkah','2a:3','anonymous quoted mishnah',c5,['sukkah height exceeds twenty cubits']),
 ('p.sukkah.yehuda','2a:3','רבי יהודה',c6,['sukkah height exceeds twenty cubits']),
 ('p.answer','2a:4','anonymous Gemara',c8,[]),
 ('p.alternative.torah','2a:5','anonymous Gemara',c9,[]),
 ('p.alternative.many','2a:5','anonymous Gemara',c10,[]),
 ('p.alternative.few','2a:5','anonymous Gemara',c11,[])]:
    position(key,ref,holder,cid,cond)
edge('e.width.exception','2a:2',c4,c3,'qualification')
edge('e.answer.first','2a:4',c8,q,'answer')
edge('e.answer.alternative.many','2a:5',c10,q,'answer')
edge('e.answer.alternative.few','2a:5',c11,q,'answer')
# Source reread: retain both anonymous explanations and all four opening rulings.
# No unsupported objection edge is inferred solely from opposite rulings.
coverage=[]
for ref in ['2a:1','2a:2','2a:3','2a:4','2a:5']:
    sid=byref[ref]['id']
    for layer in runner.LAYERS:
        ids=[r['id'] for r in records if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==sid for e in r['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Manual source reading and omission reread of 2a:1-5; surrounding argument inspected through 3b:13. Both explanations, quoted rulings, conditions and anonymous voices retained; no relation inferred from opposition alone.' if ids else 'Source pass found no explicit '+layer+' object in this segment; no missing object fabricated.'))
p=dict(schema_version=runner.VERSION,tractate=j['tractate'],owner='L03/eruvin',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
out=Path(__file__).with_name('eruvin_opening_001.json')
runner.immutable(out,runner.encoded(p))
print(runner.submit(JOB,out,'L03/eruvin',2))
print(runner.replay(JOB))
