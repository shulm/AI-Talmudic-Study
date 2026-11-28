from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.gestation.20261126w3.'
assert r.sha(r.encoded(state))=='8940d752565f9c7a563a9706a23be60fcdf965a62552eeddda716908c0d9c5e2'
refs=['8a:'+str(n) for n in range(12,18)]+['8b:'+str(n) for n in range(1,4)]
add('s','structure',refs,dict(title='Reported gestation periods and plant counterparts; snake curse ratio derivation',primary=True,boundary='closed',legacy_ids=[]))
for ref,v,role in [('8a:12','Baraita','First gestation and plant correspondences'),('8a:13','Baraita','Further gestation and plant correspondences'),('8a:14','Baraita and some say','Efeh, carob and snake accounts'),('8a:15','Rav Yehuda in Rav name, alternatively Rabbi Yehoshua ben Hanania','Verse and curse comparison question'),('8a:16','Expository answer','Sevenfold donkey/cat analogy'),('8a:17','Anonymous objection','Proposed nine-year alternative'),('8b:1','Anonymous answer','Verse order excludes reversed comparison'),('8b:2','Anonymous objection','Proposed fifteen-month alternative'),('8b:3','Anonymous answers','All-beasts wording and severity of curse')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
items=[('hen','8a:12','Hen','21 days','luz'),('dog','8a:12','Dog','50 days','fig'),('cat','8a:12','Cat','52 days','mulberry'),('pig','8a:12','Pig','60 days','apple'),('fox','8a:12','Fox and all creeping kinds','6 months','grain'),('smallpure','8a:13','Small pure livestock','5 months','vine'),('largeimpure','8a:13','Large impure livestock','12 months','date palm'),('largepure','8a:13','Large pure livestock','9 months','olive'),('wolf','8a:13','Wolf','3 years','benot shuah'),('lion','8a:13','Lion','3 years','benot shuah'),('bear','8a:13','Bear','3 years','benot shuah'),('leopard','8a:13','Leopard','3 years','benot shuah'),('bardelas','8a:13','Bardelas','3 years','benot shuah'),('elephant','8a:13','Elephant','3 years','benot shuah'),('monkey','8a:13','Monkey','3 years','benot shuah'),('kippof','8a:13','Kippof','3 years','benot shuah'),('efeh','8a:14','Efeh','70 years','carob')]
for k,ref,animal,duration,tree in items:
 c('c'+k,ref,'The baraita reports a gestation period of '+duration+' for '+animal+'.')
 c('t'+k,ref,'It gives '+tree+' as the plant counterpart to '+animal+'.')
 pos('p'+k,ref,'c'+k,['Anonymous baraita'],'Reported period, not modern biological certification')
c('c14carob70','8a:14','The source gives seventy years from carob planting to completion of its fruit.')
c('c14carob3','8a:14','It gives the carob fruit’s development period as three years.')
c('c14snake','8a:14','The source gives the snake a seven-year gestation period.')
c('c14none','8a:14','The first voice says no corresponding plant was found for that wicked one, the snake.')
c('c14some','8a:14','Some say the corresponding plant is mukhsasim.')
rows[-1]['uncertainty'].append('מוכססים retained without imposing a modern botanical identification.')
q('q15','8a:15','What supports the snake’s seven-year period?')
q('q15verse','8a:15','If the snake is cursed more than domestic animals, does the curse beyond wild animals not follow all the more?')
c('c16ratio','8a:16','The exposition compares domestic-animal to wild-animal gestation by a sevenfold ratio, donkey versus cat.')
c('c16snake','8a:16','It applies a further sevenfold ratio from domestic animal to snake and obtains seven years.')
q('q17','8a:17','Why not compare lion to donkey at a threefold ratio and apply another threefold ratio, giving nine years?')
c('c1','8b:1','The answer invokes the verse’s domestic-before-wild wording: the snake exceeds the domestic animal that already exceeds the wild animal.')
q('q2','8b:2','Why not compare goat to cat at a threefold ratio and apply another threefold ratio, giving fifteen months?')
c('c3all','8b:3','One answer invokes all the domestic animals in the verse.')
c('c3curse','8b:3','The other answer says to impose the curse with its severity rather than the lighter alternative.')
att('a15y','8a:15','רב יהודה','transmitter',['רב יהודה'],'Seven-year source derivation',['רב יהודה','רב'])
att('a15rav','8a:15','אמר רב','quoted_authority',['רב'],'Seven-year source derivation',['רב יהודה','רב'])
att('a15alt','8a:15',"ר' יהושע בן חנניא",'quoted_authority',['רבי יהושע בן חנניא'],'Alternative transmitted attribution',[],['ומטו בה marks an alternate attribution; not a combined chain through Rav.'])
att('a14some','8a:14','ויש אומרים','anonymous',[],'Alternative plant correspondence')
for k,ref,cl,h,st,qu in [('p14n','8a:14','c14none',['Anonymous first voice'],'No counterpart found',None),('p14s','8a:14','c14some',['Some say'],'Alternative counterpart',None),('p16','8a:16','c16snake',['רב via רב יהודה','Alternatively רבי יהושע בן חנניא'],'Derivation with alternate attribution','q15'),('p1','8b:1','c1',['Anonymous Gemara'],'Answer to nine-year alternative','q17'),('p3a','8b:3','c3all',['Anonymous Gemara'],'First answer','q2'),('p3c','8b:3','c3curse',['Anonymous Gemara'],'Alternative answer','q2')]:pos(k,ref,cl,h,st,qu,unc=['Alternative transmitted authorities are not joint authorship.'] if k=='p16' else [])
for k,ref,a,b,rel in [('e14','8a:14','c14some','c14none','distinction'),('e16r','8a:16','c16ratio','q15verse','answer'),('e16s','8a:16','c16ratio','c16snake','support'),('e16a','8a:16','c16snake','q15','answer'),('e17','8a:17','q17','c16snake','objection'),('e1','8b:1','c1','q17','answer'),('e2','8b:2','q2','c16snake','objection'),('e3a','8b:3','c3all','q2','answer'),('e3c','8b:3','c3curse','q2','answer')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Reported baraita gestation/botanical correspondences and scriptural ratio argument. Preserve printed numbers without converting calendars or endorsing contemporary biological truth. Alternate botanical and attribution accounts retained.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read8a12–8b21 and omission reread8a12–8b3. Each listed animal/period and plant correspondence separated; RavYehuda-to-Rav chain distinct from alternate attribution; both numerical objections and two final answers retained. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch19_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch19_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch19_receipt.json',r.encoded(out));print(r.encoded(out).decode())
