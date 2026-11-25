"""Preserve initial reading, add source-supported later resolution explicitly."""
import gittin_opening_proposal as a
a.records.clear()
r,j,JOB,add=a.r,a.j,a.JOB,a.add
s=add('s.number_resolution','structure',['5b:7','5b:8'],dict(title='מספר הנוכחים וייחוס מפורש לרבי יוחנן; הטעמים ממשיכים',primary=True,boundary='open_right',legacy_ids=[]),origin='editorial_inference')
u=add('u.number_resolution','utterances',['5b:7','5b:8'],dict(textual_voice='קול הדיון הסתמי המצטט הוראת רבי יוחנן לרבין בר רב חסדא',discourse_role='explicit_attribution_resolution',composition='composite'))
c1=add('c.number_yohanan','claims',['5b:8'],dict(proposition='המשך הסוגיה מזהה במפורש שרבי יוחנן אמר בפני שניים, על יסוד הוראתו לרבין בר רב חסדא.',conditions=['מספר הנוכחים בנתינת גט והצהרת השליח'],scope='תסתיים מפורש; זיהוי מאוחר של החלופה שבפתיחה',assertion_mode='asserted'),[u])
c2=add('c.number_hanina','claims',['5b:7','5b:8'],dict(proposition='רבי חנינא הוא האומר בפני שלושה, בהיסק מן הזוג לאחר הזיהוי המפורש של רבי יוחנן.',conditions=['זהות הזוג בשני האזכורים; רבי יוחנן זוהה כשניים'],scope='היסק מן החלופה שנותרה, לא לפי סדר השמות',assertion_mode='asserted'),[u,c1],origin='editorial_inference')
c3=add('c.ravin_instruction','claims',['5b:8'],dict(proposition='רבין בר רב חסדא הביא גט לפני רבי יוחנן, והוא הורה לו לתת בפני שניים ולומר בפני נכתב ובפני נחתם.',conditions=['הבאת גט במקרה המתואר'],scope='אירוע מסופר התומך בזיהוי השיטה',assertion_mode='asserted'),[u])
for suffix,cid,holder,role in [('yohanan',c1,'רבי יוחנן','position_holder'),('hanina',c2,'רבי חנינא','position_holder')]:
    aid=add('a.number_'+suffix,'attributions',['5b:7','5b:8'],dict(surface=holder,role=role,candidates=[holder],scope='רבין מביא ומקבל הוראה; רבי יוחנן נותן הוראה; אין לייחס לרבין את שיטת שניים.' if suffix=='ravin' else cid,transmission_chain=[]),[cid],origin='editorial_inference' if suffix in ['hanina','ravin'] else 'source_paraphrase')
    if suffix!='ravin':
        add('p.number_'+suffix,'positions',['5b:7','5b:8'],dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=['נתינה והצהרת שליח גט'],local_status='identified_in_continuation; AI provisional'),[cid,aid])
q=add('q.number_resolution','questions',['5b:7'],dict(formulation='בפני כמה נותנו לה?',question_origin='explicit',conditions=['מספר נוכחים בנתינת גט'],answer_set_status='unreviewed_alternatives'))
for suffix,src,tgt,rel,rr in [('answer',c1,q,'answer',['5b:7','5b:8']),('support',c3,c1,'support',['5b:8']),('initial',c1,'L02.git.open.c.a8','local_resolution',['3a:3','5b:7','5b:8']),('repeated',c1,'L02.git.open.c.b7','local_resolution',['3a:7','5b:8'])]:
    add('e.number_'+suffix,'edges',rr,dict(source_id=src,target_id=tgt,relation=rel,explicitness='source_explicit'),[src,tgt])
add('a.resh_lakish_quoted','attributions',['3a:6'],dict(surface='ר״ל',role='quoted_authority',candidates=['ריש לקיש'],scope='עדים החתומים על השטר כמי שנחקרה עדותם; מצוטט בידי הגמרא ולא מדבר כשליח במקרה',transmission_chain=[]),['L02.git.open.c.b4'])
c4=add('c.sages_restriction','claims',['2a:3'],dict(proposition='חכמים מנוסחים בשלילה מגבילה: אינו צריך אלא המביא ממדינת הים והמוליך.',conditions=['ההגבלה מנוסחת בתוך מחלוקת המשנה; פירושה נבדק בהמשך'],scope='שימור המילה אלא ולא רק חיוב שתי הקטגוריות',assertion_mode='asserted'),['L02.git.open.c.m4'])
add('e.sages_restriction','edges',['2a:3'],dict(source_id=c4,target_id='L02.git.open.c.m4',relation='qualification',explicitness='source_explicit'),[c4,'L02.git.open.c.m4'])

state=r.current(JOB)
allrecords=state['records']+a.records
coverage=[]
for f in ['5b:7','5b:8','3a:3','3a:7','3a:6','2a:3']:
    sid=a.byref[f]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in allrecords if x.get('release_state','valid')=='valid' and (x['layer']==layer or layer=='reconciliation') and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Targeted source-based follow-up after frozen independent reading git_opening_001. Original 5b:1–6a:19 read; preserve opening ambiguity as a historical stage and add explicit later resolution. Initial records remain immutable.'))
p={k:j[k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']}
p.update(owner='/root/L02_gittin',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=a.records,coverage=coverage,open_tails=state['open_tails']+[s])
r.immutable(JOB/'authored/L02_risk_followup_v1.json',r.encoded(p))
print(JOB/'authored/L02_risk_followup_v1.json')
