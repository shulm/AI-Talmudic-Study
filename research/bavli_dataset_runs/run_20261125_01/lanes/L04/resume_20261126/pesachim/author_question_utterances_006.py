"""Source-reread correction: explicit questions also need utterance objects.

The question text/interpretations already exist; this explicit list repairs the
missing utterance-layer representation without claiming new source coverage.
"""
from author_opening_001 import *
records.clear();state=r.current(JOB);byid={x['id']:x for x in state['records']}
anonymous=['b2.burn.q','b2.eat.q','b2.good.q','b2.torch.q','b2.work.q','b3.equal.q','b3.unclean.q','b3.verses.q','b3.why.q','b3.woman.q','b4.alternative.q','b5.burden.q','b5.difference.q','b5.here.q','b5.howknow.q','b5.mistake.q','b5.morning.q','b5.pres.q','b5.rent.q','b5.six.q','b5.speech.q','b5.whytrust.q','meaning.q','nonshining.q','sam23.q','vow.q','wordorder.q']
specific={'b2.divided.q':('רבי אליעזר בן יעקב','speaker','Anonymous reconstruction introduced by הכי קאמר; not a separately transmitted quotation.'),'b4.death.q':('unnamed questioners of the messenger','collective','Narrative אמרו ליה does not name these questioners.'),'b4.suspicion.q':('unnamed Jerusalem interlocutors','collective','Narrative plural questioners.'),'b4.tail.q':('רבי יהודה בן בתירא','speaker','Explicit preceding אמר ליה רבי יהודה בן בתירא.'),'b4.wheat.q':('unnamed questioners of Yohanan Hakkukaah','collective','Narrative plural questioners.'),'b4.who.q':('unnamed Jerusalem interlocutors','collective','Narrative plural questioners.')}
for key in anonymous+list(specific):
    q=byid['pe.r001.'+key];assert q['layer']=='questions'
    voice,role,note=specific.get(key,('anonymous question in the discussion','anonymous','No named speaker is supplied for this question.'))
    u=add('b6.'+key+'.u','utterances',dict(textual_voice=voice,discourse_role='explicit question',composition='atomic'),q['evidence'],[q['id']],uncertainty=[note] if key=='b2.divided.q' else [])
    add('b6.'+key+'.a','attributions',dict(surface=q['evidence'][0]['quote'],role=role,candidates=[voice] if role=='speaker' else [],scope=u+'; '+note,transmission_chain=[]),q['evidence'],[u])
coverage=[];touched={e['segment_id'] for x in records for e in x['evidence']}
for sid in touched:
    for layer in ['utterances','attributions']:
        ids=[x['id'] for x in state['records']+records if x['layer']==layer and x.get('release_state','valid')=='valid' and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found',record_ids=ids,rationale='Direct reread of explicit question spans: questions previously existed but lacked dedicated utterance/voice objects. This correction adds those objects and preserves previous claims/questions.'))
    coverage.append(dict(segment_id=sid,layer='reconciliation',extraction_state='completed',extraction_result='none_found_after_pass',record_ids=[],rationale='Question-layer-to-utterance omission audit reread original spans and narrative speaker context. Added all explicitly listed missing question utterances; no new proposition or source coverage invented.'))
p=dict(schema_version=r.VERSION,tractate='Pesachim',owner='L04/pesachim_resume_20261126',epoch=3,source_sha256=meta['source_sha256'],**r.hashes(),execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=sorted(coverage,key=lambda x:(x['segment_id'],x['layer'])),open_tails=state['open_tails'])
out=JOB/'staging'/'question_utterances_006.json';r.immutable(out,r.encoded(p));print(out)
