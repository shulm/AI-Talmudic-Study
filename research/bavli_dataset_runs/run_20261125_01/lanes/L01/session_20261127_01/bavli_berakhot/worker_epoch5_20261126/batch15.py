from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.hezekiah.20261126e5.'
assert r.sha(r.encoded(state))=='b6c5e4bcf54e92a13fff89fdbced964cd8dd574172cba74a6d072e8a1b12703b'
refs=['10a:'+str(i) for i in range(26,33)]+['10b:'+str(i) for i in range(1,14)]
for k,rr,title in [('visit',refs[:8],'Hezekiah and Isaiah: visit, procreation and mercy'),('wall',refs[8:12],'Hezekiah’s wall and good deed'),('acts',refs[12:17],'Six actions and intercalation correction'),('merit',refs[17:],'Invoking one’s own or others’ merit')]:add('s'+k,'structure',rr,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
voices=['Rav Hamnuna representing Hezekiah and Isaiah','Narrative divine arrangement and Isaiah message','Hezekiah and Isaiah','Isaiah','Hezekiah and Isaiah','Hezekiah quoting ancestral tradition','Rabbi Yohanan and Rabbi (Eliezer) jointly','Rabbi Hanan','Narrative continuation','Anonymous question; Resh Lakish','Rabbi Levi representing Hezekiah','Anonymous question; Rav Yehuda reporting Rav; Rabbi Levi','Baraita introduction','Baraita approved actions','Baraita unapproved actions','Anonymous objection','Anonymous correction citing Shmuel','Rabbi Yohanan reporting Rabbi Yose ben Zimra','Moses example','Hezekiah example; Rabbi Yehoshua ben Levi']
assert len(voices)==len(refs)
for ref,voice in zip(refs,voices):add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=voice,discourse_role='Narrative or interpretation',composition='composite'))
def claim(k,ref,text,holders,cond=(),status='Reported locally',unc=()):
 c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
q('q26','10a:26','Rav Hamnuna asks who is like the wise one and knows resolution of a matter.')
claim('26god','10a:26','He interprets it as God knowing how to make compromise between Hezekiah and Isaiah.',['Rav Hamnuna'])
claim('26king','10a:26','Hezekiah expects Isaiah to come to him, using Elijah going to Ahab as precedent.',['Hezekiah as represented by Rav Hamnuna'])
claim('26prophet','10a:26','Isaiah expects Hezekiah to come to him, using Jehoram going to Elisha as precedent.',['Isaiah as represented by Rav Hamnuna'])
claim('27plan','10a:27','God brings illness upon Hezekiah and tells Isaiah to visit the sick man.',['Narrative exposition'])
claim('27death','10a:27','Isaiah’s you shall die and not live is interpreted as death in this world and no life in the world to come.',['Exposition of Isaiah’s message'])
q('q28','10a:28','Hezekiah asks why the consequence is so severe.')
claim('28reason','10a:28','Isaiah answers that Hezekiah did not engage in procreation.',['Isaiah in represented dialogue'])
claim('28defense','10a:28','Hezekiah says he saw by holy spirit that his children would be unworthy.',['Hezekiah in represented dialogue'],status='Defense subsequently challenged')
claim('29','10a:29','Isaiah tells him not to concern himself with divine secrets: do what commanded and let God do what He pleases.',['Isaiah in represented dialogue'])
claim('30proposal','10a:30','Hezekiah asks for Isaiah’s daughter, hoping their combined merit could produce worthy children.',['Hezekiah in represented dialogue'],status='Proposal, not assertion that marriage already occurred')
claim('30decree','10a:30','Isaiah says the decree has already been issued.',['Isaiah in represented dialogue'])
claim('30dismiss','10a:30','Hezekiah tells the son of Amoz to finish the prophecy and leave.',['Hezekiah in represented dialogue'])
claim('31','10a:31','Hezekiah cites ancestral tradition not to refrain from mercy even when a sharp sword rests on one’s neck.',['Hezekiah citing ancestral tradition'],cond=['Even imminent lethal danger'])
claim('32','10a:32','Rabbi Yohanan and Rabbi (Eliezer) jointly teach the same refusal to give up mercy, citing though He slay me I hope in Him.',['Rabbi Yohanan','Rabbi (Eliezer) as printed'],unc=['Parenthetical אליעזר retained rather than silently harmonized to אלעזר.'])
claim('1','10b:1','Rabbi Hanan says even if a master of dreams says one will die tomorrow, one must not refrain from mercy.',['Rabbi Hanan'],cond=['Prediction of death tomorrow by a dream figure'])
claim('2','10b:2','Hezekiah immediately turns his face to the wall and prays.',['Narrator'],status='Narrative response')
q('q3','10b:3','What is the wall?')
claim('3','10b:3','Resh Lakish interprets it as the walls of his heart, citing the heart’s walls.',['Resh Lakish'])
claim('4','10b:4','Rabbi Levi interprets prayer concerning the wall: if the Shunammite’s single small wall merited reviving her son, his ancestor’s covering the whole sanctuary in silver and gold should do so all the more.',['Rabbi Levi representing Hezekiah'],status='A fortiori plea in narrative')
q('q5','10b:5','What is the good in Your eyes that I did?')
claim('5rav','10b:5','Rav through Rav Yehuda identifies it as adjoining redemption to prayer.',['Rav'])
claim('5levi','10b:5','Rabbi Levi identifies it as concealing the book of remedies.',['Rabbi Levi'])
claim('6','10b:6','The baraita lists six actions of Hezekiah: three approved and three not approved.',['Unnamed baraita'])
for k,text in [('book','Concealing the book of remedies was approved.'),('serpent','Crushing the bronze serpent was approved.'),('father','Dragging his father’s bones on a rope bed was approved.')]:claim('7'+k,'10b:7',text,['Baraita’s approving authorities, unnamed'],status='Reported approval')
for k,text in [('water','Blocking Gihon’s water was not approved.'),('doors','Cutting sanctuary doors and sending them to Assyria’s king was not approved.'),('month','Intercalating Nisan in Nisan was not approved.')]:claim('8'+k,'10b:8',text,['Baraita’s disapproving authorities, unnamed'],status='Reported disapproval',unc=['The calendar wording is reinterpreted at10b10.'] if k=='month' else [])
q('q9','10b:9','Did Hezekiah not know this month is the first month, Nisan and no other Nisan?')
claim('10rule','10b:10','Shmuel says not to intercalate the year on day thirty of Adar because it is fit to be established as Nisan.',['Shmuel'],cond=['Thirtieth day of Adar'])
claim('10error','10b:10','The answer says Hezekiah erred in that rule, thinking potential fitness was not taken into account.',['Anonymous Gemara representing Hezekiah’s reasoning'],status='Correction of literal Nisan-in-Nisan interpretation')
claim('11self','10b:11','Rabbi Yohanan reports Rabbi Yose ben Zimra that one invoking his own merit has the outcome attributed to others’ merit.',['Rabbi Yose ben Zimra'],cond=['Invokes own merit'])
claim('11others','10b:11','One invoking others’ merit has it attributed to his own.',['Rabbi Yose ben Zimra'],cond=['Invokes others’ merit'])
claim('12','10b:12','Moses invoked the patriarchs’ merit, but the salvation was attributed to Moses standing in the breach.',['Expository example'])
claim('13','10b:13','Hezekiah invoked his own conduct, but protection was attributed to God’s sake and David’s merit.',['Expository example'])
claim('13bitter','10b:13','Rabbi Yehoshua ben Levi reads bitter peace as bitterness even when God sent Hezekiah peace.',['Rabbi Yehoshua ben Levi'])
for k,ref,surface,name in [('26','10a:26','רב המנונא','רב המנונא'),('32y','10a:32','רבי יוחנן','רבי יוחנן'),('32e','10a:32','רבי (אליעזר)','רבי (אליעזר)'),('1','10b:1','ר חנן','רבי חנן'),('3','10b:3','רשב"ל','רבי שמעון בן לקיש'),('4','10b:4',"ר' לוי",'רבי לוי'),('5l','10b:5',"ר' לוי",'רבי לוי'),('10','10b:10','שמואל','שמואל'),('13','10b:13','ריב"ל','רבי יהושע בן לוי')]:att('a'+k,ref,surface,'speaker',[name],'Local teaching')
att('a5','10b:5','ר יהודה אמר רב','transmitter',['רבי יהודה as printed'],pre+'c5rav',chain=['רב יהודה','רב'],unc=['Preserve source abbreviation; holder is Rav, not transmitter.'])
att('a11','10b:11',"ר יוחנן משום ר' יוסי בן זמרא",'transmitter',['רבי יוחנן'],'Merit teaching',chain=['רבי יוחנן','רבי יוסי בן זמרא'])
for k,ref,a,b,rel in [('26','10a:26','c26god','q26','answer'),('26d','10a:26','c26king','c26prophet','distinction'),('27','10a:27','c27plan','c26god','support'),('28','10a:28','c28reason','q28','answer'),('28d','10a:28','c28defense','c28reason','objection'),('29','10a:29','c29','c28defense','objection'),('30','10a:30','c30decree','c30proposal','objection'),('31','10a:31','c31','c30decree','objection'),('32','10a:32','c32','c31','support'),('1','10b:1','c1','c31','support'),('3','10b:3','c3','q3','answer'),('4','10b:4','c4','q3','answer'),('5r','10b:5','c5rav','q5','answer'),('5l','10b:5','c5levi','q5','answer'),('9','10b:9','q9','c8month','objection'),('10','10b:10','c10error','q9','answer'),('10c','10b:10','c10error','c8month','correction'),('10s','10b:10','c10rule','c10error','support'),('12','10b:12','c12','c11others','support'),('13','10b:13','c13','c11self','support'),('13b','10b:13','c13bitter','c13','support')]:edge('e'+k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Local Hezekiah narrative and reported approvals; preserve proposals versus outcomes, opposed speakers, corrected calendar interpretation and merit attribution.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read10a26–10b41; reread core10a26–10b13 for rival visit precedents, procreation defense/rebuttal, mercy despite decree, wall alternatives, six separately evaluated acts, thirtieth-Adar correction, and reciprocal merit examples. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch15_proposal.json',r.encoded(p));print(r.encoded(dict(staged_only=True,proposal_sha256=r.sha(r.encoded(p)),records=len(rows),core_segments=len(refs),base_snapshot_sha256=r.sha(r.encoded(state)))).decode())
