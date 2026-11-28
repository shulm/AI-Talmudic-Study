from pathlib import Path
import sys
sys.path.insert(0,r'C:/Users/David/.codex/worktrees/bavli-global-coordination/AI Talmudic Study/research/bavli_production_v1')
import runner as r
HERE=Path(__file__).resolve().parent; JOB=HERE.parent
j,ss=r.load(JOB); state=r.current(JOB)
by={x['ref'].split(' ')[1]:x for x in ss.values()}; rows=[]; pre='bk.david_evening.20261126.'
def ev(ref,quote=None):
 t=by[ref]['text']; quote=t if quote is None else quote; a=t.index(quote)
 return dict(segment_id=by[ref]['id'],start_char=a,end_char=a+len(quote),quote=quote)
def add(k,layer,refs,content,links=(),unc=(),origin='source_paraphrase'):
 rows.append(dict(id=pre+k,layer=layer,evidence=[ev(x) if isinstance(x,str) else ev(*x) for x in refs],content=content,links=[pre+x for x in links],uncertainty=list(unc),origin=origin));return pre+k
def c(k,refs,p,mode='asserted',cond=()): return add(k,'claims',refs,dict(proposition=p,conditions=list(cond),scope='Local discussion of David rising and the two uses of neshef; no historical chronology inferred.',assertion_mode=mode))
def q(k,refs,p):return add(k,'questions',refs,dict(formulation=p,question_origin='explicit',conditions=[],answer_set_status='partial'))
def edge(k,refs,a,b,rel):return add(k,'edges',refs,dict(source_id=pre+a,target_id=pre+b,relation=rel,explicitness='source_explicit'),[a,b])
def pos(k,ref,cl,holder,status,question=None):return add(k,'positions',[ref],dict(holder_candidates=[holder],claim_id=pre+cl,question_id=pre+question if question else None,conditions=[],local_status=status),[cl]+([question] if question else []))
def att(k,ref,surface,role,candidates,scope,chain=()):return add(k,'attributions',[(ref,surface)],dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=list(chain)))
add('s20','structure',['3b:20','3b:21','3b:22'],dict(title='Reconciling David rising at midnight with rising at evening',primary=True,boundary='closed',legacy_ids=[]))
add('s23','structure',['3b:23','3b:24','3b:25','3b:26'],dict(title='Neshef as evening and morning',primary=True,boundary='closed',legacy_ids=[]))
for n,voice,role in [(20,'Anonymous Gemara','Challenge and scriptural support'),(21,'Rav Oshaya reporting Rabbi Aha','Interpretive answer'),(22,'Rabbi Zeira and Rav Ashi','Two alternative temporal distinctions'),(23,'Anonymous Gemara','Challenge using another verse'),(24,'Anonymous Gemara','Provisional answer'),(25,'Anonymous Gemara','Objection to provisional answer'),(26,'Rava','Revised distinction')]:
 add('u'+str(n),'utterances',['3b:'+str(n)],dict(textual_voice=voice,discourse_role=role,composition='composite' if n in [20,22,23,26] else 'atomic'))
q('q20',['3b:20'],'Did David rise at midnight, given the verse indicating rising at evening?')
q('q20n',[('3b:20','וממאי דהאי נשף אורתא הוא')],'How do we know neshef here means evening?')
c('c20',[('3b:20','מאורתא הוה קאי דכתיב (תהלים קיט)קדמתי בנשף ואשועה')],'The questioner infers that David rose at evening from “I preceded at neshef and cried out.”',mode='challenged')
c('c20n',[('3b:20','דכתיב (משלי ז)בנשף בערב יום באישון לילה ואפילה')],'The verse in Proverbs is used to establish an evening sense of neshef.')
c('c21',['3b:21'],'Rav Oshaya reports Rabbi Aha interpreting David: midnight never passed over him in sleep.')
c('c22z',[('3b:22','רבי זירא אמר עד חצות לילה היה מתנמנם כסוס מכאן ואילך היה מתגבר כארי')],'Rabbi Zeira distinguishes David dozing like a horse before midnight from becoming vigorous like a lion afterward.')
c('c22a',[('3b:22','רב אשי אמר עד חצות לילה היה עוסק בדברי תורה מכאן ואילך בשירות ותשבחות.')],'Rav Ashi distinguishes David studying Torah before midnight from songs and praises afterward.')
att('a21t','3b:21','רב אושעיא','transmitter',['רב אושעיא'],pre+'c21',['רב אושעיא','רבי אחא'])
att('a21h','3b:21','רבי אחא','quoted_authority',['רבי אחא'],pre+'c21',['רב אושעיא','רבי אחא'])
att('a22z','3b:22','רבי זירא','speaker',['רבי זירא'],pre+'c22z')
att('a22a','3b:22','רב אשי','speaker',['רב אשי'],pre+'c22a')
pos('p21','3b:21','c21','רבי אחא','Interpretive reconciliation transmitted by Rav Oshaya','q20')
pos('p22z','3b:22','c22z','רבי זירא','Alternative temporal distinction','q20')
pos('p22a','3b:22','c22a','רב אשי','Alternative activity distinction','q20')
edge('e20n',['3b:20'],'c20n','q20n','answer')
edge('e20',['3b:20'],'c20','q20','support')
edge('e21',['3b:21'],'c21','q20','answer')
edge('e22z',['3b:22'],'c22z','q20','answer')
edge('e22a',['3b:22'],'c22a','q20','answer')
q('q23',['3b:23'],'Does neshef mean evening, when the verse about David striking his enemies seems to mean from morning until night?')
c('c23',['3b:23'],'The challenge proposes a morning sense of neshef in the verse about David striking from neshef until evening of the following day.',mode='hypothetical')
c('c24',['3b:24'],'The provisional answer reads the interval as evening to evening.',mode='rejected')
q('q25',['3b:25'],'If the interval is evening to evening, why does the verse not use neshef twice or evening twice?')
c('c26m',[('3b:26','נשף ליליא ואתי יממא')],'Rava distinguishes the departure of night and arrival of day as one neshef.')
c('c26e',[('3b:26','נשף יממא ואתי ליליא')],'Rava distinguishes the departure of day and arrival of night as the other neshef.')
att('a26','3b:26','רבא','speaker',['רבא'],'Two-neshef distinction')
pos('p24','3b:24','c24','Anonymous Gemara','Provisional answer displaced by אלא אמר רבא','q23')
pos('p26m','3b:26','c26m','רבא','Final local distinction; morning usage','q23')
pos('p26e','3b:26','c26e','רבא','Final local distinction; evening usage','q23')
edge('e23',['3b:23'],'c23','c20n','qualification')
edge('e24',['3b:24'],'c24','q23','answer')
edge('e25',['3b:25'],'q25','c24','objection')
edge('e26m',['3b:26'],'c26m','q23','answer')
edge('e26e',['3b:26'],'c26e','q23','answer')
edge('e26r',['3b:26'],'c26m','c24','correction')
coverage=[]
for ref in ['3b:'+str(n) for n in range(20,27)]:
 sid=by[ref]['id']
 for layer in r.LAYERS:
  linked=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
  rationale='Read original source and continuation through 4a:7. '+('Re-read for omissions: retained alternative reconciliations, transmitter/holder distinction, provisional evening-to-evening answer and its rejection, both senses of neshef. No further claims found in this core pass.' if layer=='reconciliation' else 'Completed '+layer+' pass over the stated core; source evidence and local dialectical status preserved.' if linked else 'Completed '+layer+' pass: no distinct '+layer+' record found in this source segment beyond the represented surrounding discourse.')
  coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if linked else 'none_found_after_pass',record_ids=linked,rationale=rationale))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_berakhot_correction',epoch=4,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=coverage,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j); r.immutable(HERE/'david_evening_proposal.json',r.encoded(p))
out=r.submit(JOB,HERE/'david_evening_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'david_evening_receipt.json',r.encoded(out));print(r.encoded(out).decode())
