import opening as x
import json
x.records.clear()
add=x.add;cl=x.cl;q=x.q;at=x.at;edge=x.edge
add('d_s','structure',range(56,64),dict(title='Lashes for cursing another by the divine name: derivation and rejected alternatives',primary=True,boundary='closed',legacy_ids=[]))
roles={56:'Question and transmitted scriptural derivation',57:'Proposed truthful-oath inclusion and objection',58:'Refined truthful-oath suggestion and rejection',59:'Competing use for oath verse and second verse answer',60:'Application to cursing and alternative vain-name suggestion',61:'Clarification of proposed severity distinction',62:'Negative-warning requirement and objection to vain-name interpretation',63:'Proposed warning and positive-command distinction'}
for i,r in roles.items():
 add('d_u'+str(i),'utterances',[i],dict(textual_voice='Anonymous discussion with named reports where stated',discourse_role=r,composition='composite'))
 at('d_an'+str(i),i,'Anonymous discussion','anonymous',r,cand=[])
q('d_q56',56,'From where are lashes for cursing another with the divine name derived?')
cl('d_c56a',56,'The passage אם לא תשמר is followed by והפלא ה׳ את מכותך.',scope='First scriptural link in Rabbi Oshaya’s transmitted derivation')
cl('d_c56b',56,'The meaning of הפלאה is identified as lashes from והפילו השופט והכהו לפניו.',scope='Second scriptural link; reported by Rabbi Elazar in Rabbi Oshaya’s name',holder='Rabbi Oshaya')
at('d_a56t',56,'רבי אלעזר','transmitter','Reports Rabbi Oshaya’s derivation',chain=['רבי אלעזר','רבי אושעיא'])
at('d_a56h',56,'רבי אושעיא','quoted_authority','Derives the lashes punishment')
q('d_q57',57,'Could the derivation impose lashes even for a truthful oath?')
cl('d_c57',57,'The explicit verse שבועת ה׳ תהיה בין שניהם provides a truthful-oath case against that suggestion.',scope='Initial rejection of truthful-oath lashes')
q('d_q58',58,'Could that oath merely appease the other party while the swearer nevertheless receives lashes?')
cl('d_c58',58,'The suggestion cannot stand because Scripture says ובשמו תשבע.',scope='Rejection of lashes for the truthful-oath case, challenged by alternative verse use next')
cl('d_c59a',59,'That verse is proposed as needed for Rav’s teaching about swearing to fulfill commandments.',mode='hypothetical',scope='Objection to using first ובשמו תשבע for truthful-oath permission')
q('d_q59',59,'From where do we know that one may swear to fulfill commandments?')
cl('d_c59b',59,'Rav derives swearing to fulfill commandments from נשבעתי ואקיימה לשמור משפטי צדקך.',scope='Rav reported by Rav Giddel',holder='Rav')
cl('d_c59c',59,'Another verse also states ובו תדבק ובשמו תשבע.',scope='Additional verse answers competing-use objection')
at('d_a59t',59,'רב גידל','transmitter','Reports Rav',chain=['רב גידל','רב'])
at('d_a59h',59,'רב','quoted_authority','Oaths to fulfill commandments; not Rav Giddel’s independent view')
q('d_q60a',60,'For what then does the punishment passage come?')
cl('d_c60a',60,'It applies to cursing another with the divine name.',scope='Answer locating lashes derivation')
q('d_q60b',60,'Could it apply instead to uttering the divine name in vain?')
q('d_q60c',60,'Is cursing another with the divine name any less than uttering the name in vain?')
cl('d_c61a',61,'The clarified suggestion would treat lashes as sufficient for vain utterance of the divine name.',mode='hypothetical',scope='Proposed alternative reading, not accepted ruling')
cl('d_c61b',61,'The clarified suggestion would treat lashes as insufficient for cursing another with the name, because it combines vain utterance and distressing the other person.',mode='hypothetical',scope='Rejected severity distinction; no particular additional punishment is specified')
cl('d_c62a',62,'The curse interpretation has a negative warning in לא תקלל חרש.',scope='Answer rejecting the proposed alternative punishment allocation')
q('d_q62',62,'If the passage instead concerns vain utterance of the divine name, where is its negative warning?')
q('d_q63',63,'Why could את ה׳ אלהיך תירא ואותו תעבוד not provide that warning?')
cl('d_c63',63,'That verse is a positive-command warning, not the needed negative warning.',scope='Final rejection of proposed source for vain-name lashes')
for k,ii,a,b,r in [('01',[56],'d_c56b','d_q56','answer'),('02',[57],'d_c57','d_q57','answer'),('03',[58],'d_c58','d_q58','answer'),('04',[59],'d_c59a','d_c58','objection'),('05',[59],'d_c59b','d_q59','answer'),('06',[59],'d_c59c','d_c59a','objection'),('07',[60],'d_c60a','d_q60a','answer'),('08',[60],'d_q60c','d_q60b','objection'),('09',[61],'d_c61b','d_q60c','qualification'),('10',[62],'d_c62a','d_c61b','objection'),('11',[63],'d_c63','d_q63','answer')]:edge('d_e'+k,ii,a,b,r)
notes={56:'Question, transmitted authority and both scriptural links retained.',57:'Truthful-oath extension retained as question, not actual lashes ruling.',58:'Appeasement-versus-lashes suggestion and explicit rejection both retained.',59:'Rav Giddel/Rav roles separated; mitzvah-oath proof and second verse retained.',60:'Three questions and application to cursing kept distinct.',61:'Clarified hypothetical severity distinction retained without inventing an additional punishment.',62:'Negative warning is key; source question not suppressed.',63:'Positive-command status answers proposed warning; read next segment 4a:3, which starts terumah/first-fruits exception.'}
coverage=[]
for i in range(56,64):
 for l in x.layers:
  rr=[r['id'] for r in x.records if (l=='reconciliation' or r['layer']==l) and any(e['segment_id']==x.inv[i]['id'] for e in r['evidence'])]
  coverage.append(dict(segment_id=x.inv[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if rr else 'none_found_after_pass',record_ids=rr,rationale=('Source reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record found in this layer.' if not rr else '')))
p={k:x.meta[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};p.update(owner='L05/temurah',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=x.records,coverage=coverage,open_tails=[])
out=x.W/'curse_name_3b15_4a2_v1.json';blob=(json.dumps(p,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
if out.exists():assert out.read_bytes()==blob
else:out.write_bytes(blob)
print(len(x.records),'records')
