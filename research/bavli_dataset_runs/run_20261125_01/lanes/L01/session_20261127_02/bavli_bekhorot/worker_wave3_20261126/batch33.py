from pathlib import Path
helper=(Path(r'F:/Sefaria_QA/bavli_production_run_20261125_01/L01/bavli_berakhot/worker_wave2_20261126/batch01.py')).read_text(encoding='utf-8').split("refs=['4a:'")[0]
exec(compile(helper,'serialization_helpers','exec'))
pre='beh.blemishtiming.20261127w3.'
assert r.sha(r.encoded(state))=='3bfd713c1ec4034bd7f6d05a5f533ba39da88342f1bd8a4de801d96f34e58b85'
refs=['14a:'+str(n) for n in range(1,10)]+['14b:'+str(n) for n in range(1,4)]
add('s1','structure',refs[:4],dict(title='Permanent blemish before versus after consecration: distinct consequences',primary=True,boundary='closed',legacy_ids=[]))
add('s2','structure',refs[4:7],dict(title='Before-redemption inferences and limited shearing/work analogy',primary=True,boundary='closed',legacy_ids=[]))
add('s3','structure',refs[7:],dict(title='Offspring conceived before redemption and no stricter secondary sanctity',primary=True,boundary='closed',legacy_ids=[]))
prior=['Permanent blemish precedes consecration','Redeemed where stated'];later=['Consecration precedes permanent blemish, including earlier temporary blemish','Redeemed where stated']
items=[('firstborn','14a:1','They are liable in firstborn status after redemption.',prior),('gifts','14a:1','They are liable in priestly animal gifts after redemption.',prior),('shear','14a:1','They become ordinary animals permitting shearing after redemption.',prior),('work','14a:1','They become ordinary animals permitting work after redemption.',prior),('offspring','14a:1','Their offspring is permitted after redemption, with timing explained in the continuation.',prior),('milk','14a:1','Their milk is permitted after redemption.',prior),('outside','14a:2','One slaughtering them outside is exempt under the Mishnah formulation.',['Permanent blemish before consecration','Outside slaughter; later RabbiElazar alternative separately recorded']),('substitute','14a:2','They do not generate substitution sanctity.',['Permanent blemish before consecration']),('dead','14a:2','If they die they can be redeemed.',['Permanent blemish before consecration','Death before redemption','Subject to firstborn/tithe exception and later tannaitic analysis']),('laterfirst','14a:3','They are exempt from firstborn status after redemption.',later),('latergifts','14a:3','They are exempt from priestly animal gifts after redemption.',later),('latershear','14a:3','They do not become ordinary animals permitting shearing after redemption.',later),('laterwork','14a:3','They do not become ordinary animals permitting work after redemption.',later),('lateroffspring','14a:4','Their offspring is prohibited after redemption, with timing elaborated later.',later),('latermilk','14a:4','Their milk is prohibited after redemption.',later),('lateroutside','14a:4','One slaughtering them outside is liable.',['Consecration before permanent blemish','Outside slaughter; timing/qualification belongs to continuation']),('latersubstitute','14a:4','They generate substitution sanctity.',['Consecration before permanent blemish']),('laterdead','14a:4','If they die they must be buried.',['Consecration before permanent blemish','Death before redemption'])]
for k,ref,prop,conditions in items:
 c('c'+k,ref,'The Mishnah states: '+prop,cond=conditions);pos('p'+k,ref,'c'+k,['Anonymous Mishnah'],'Stated timing-dependent consequence',cond=conditions)
c('c2except','14a:2','Firstborn and animal-tithe animals are exceptions to the preceding prior-blemish regime.')
c('c5first','14a:5','The Gemara infers that before redemption the prior-blemish animals are exempt from firstborn status.')
c('c5gifts','14a:5','It infers they are then exempt from priestly animal gifts.')
c('c5principle','14a:5','It concludes monetary sanctity displaces firstborn and gift obligations.')
c('c6shear','14a:6','Before redemption, the Mishnah implies shearing is prohibited.')
c('c6work','14a:6','Before redemption, it implies work is prohibited.')
c('c6eliezer','14a:6','The passage proposes support for Rabbi Eliezer’s prohibition on shearing and work of Temple-maintenance consecrations.',mode='challenged')
c('c7altar','14a:7','The reply limits the present decree to monetary sanctity for the altar because it could be confused with bodily altar sanctity.')
c('c7maintenance','14a:7','It says that inference need not extend to Temple-maintenance consecrations.')
q('q8','14a:8','What offspring timing does the permission describe?')
c('c8after','14a:8','Conception and birth after redemption would be obvious because they are ordinary animals.')
c('c8before','14a:8','The case is conception before redemption and birth after redemption.')
c('c9','14a:9','The passage infers prohibition before redemption.')
q('q1','14b:1','May the offspring be redeemed while unblemished, or not?')
c('c2sell','14b:2','The cited baraita allows sale of offspring of animals consecrated to the altar while permanently blemished.')
c('c2noblemish','14b:2','Those offspring require no blemish to be sold.')
c('c2sanctity','14b:2','The explanation says the relevant sanctity does not take effect on the offspring.')
c('c2secondary','14b:2','The secondary offspring should not be more stringent than the primary animal.')
c('c3male','14b:3','The Gemara contrasts dedicating a male for its value: bodily sanctity does take effect on it.')
c('c3rava','14b:3','Rava states that a male dedicated for its value becomes bodily sacred.')
for ref,v,role in [('14a:1','Mishnah','Prior-blemish redeemed animal consequences'),('14a:2','Mishnah','Outside slaughter, substitution, death and exceptions'),('14a:3','Mishnah','Later-blemish redeemed animal consequences'),('14a:4','Mishnah','Offspring, milk, outside slaughter, substitution and death'),('14a:5','Anonymous Gemara','Before-redemption inference'),('14a:6','Anonymous Gemara citing Rabbi Eliezer','Proposed maintenance-sanctity support'),('14a:7','Anonymous reply','Altar confusion decree restricted'),('14a:8','Anonymous exchange','Offspring conception/birth timing'),('14a:9','Anonymous inference','Before-redemption prohibition'),('14b:1','Anonymous Gemara','Unblemished-offspring redemption inquiry'),('14b:2','Baraita','No stricter secondary sanctity'),('14b:3','Anonymous Gemara and Rava','Male-for-value bodily sanctity contrast')]:add('u'+ref.replace(':','_'),'utterances',[ref],dict(textual_voice=v,discourse_role=role,composition='composite'))
att('a6','14a:6','רבי אליעזר','quoted_authority',['רבי אליעזר'],'Temple-maintenance shearing/work prohibition')
att('a3','14b:3','רבא','speaker',['רבא'],'Male dedicated for value acquires bodily sanctity')
for k,ref,cl,h,st,qu in [('p5','14a:5','c5principle',['Anonymous Gemara'],'Inference before redemption',None),('p6','14a:6','c6eliezer',['Anonymous Gemara'],'Support attempt rejected',None),('p7','14a:7','c7altar',['Anonymous Gemara'],'Restricted decree',None),('p8','14a:8','c8before',['Anonymous Gemara'],'Timing explanation','q8'),('p2','14b:2','c2noblemish',['Anonymous baraita'],'No blemish required','q1'),('p3','14b:3','c3rava',['רבא'],'Bodily sanctity of male for value',None)]:pos(k,ref,cl,h,st,qu)
for k,ref,a,b,rel in [('e2','14a:2','c2except','cdead','qualification'),('e5f','14a:5','c5first','c5principle','support'),('e5g','14a:5','c5gifts','c5principle','support'),('e6s','14a:6','c6shear','c6eliezer','support'),('e6w','14a:6','c6work','c6eliezer','support'),('e7','14a:7','c7altar','c6eliezer','objection'),('e7m','14a:7','c7maintenance','c6eliezer','objection'),('e8','14a:8','c8before','q8','answer'),('e8q','14a:8','c8before','coffspring','qualification'),('e2a','14b:2','c2noblemish','q1','answer'),('e2s','14b:2','c2secondary','c2noblemish','support'),('e3','14b:3','c3male','c2secondary','distinction'),('e3r','14b:3','c3male','c3rava','support')]:edge(k,ref,a,b,rel)
for x in rows:
 if x['layer']=='claims':x['content']['scope']='Mishnah blemish-before/after-consecration regimes and first explanatory unit. Redemption, death, conception/birth and sacrifice timing kept explicit. Later alternate outside-slaughter version and tannaitic standing/valuation dispute read through15a20 and left for own records.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read14a1–15a20 and omission reread14a1–14b3. Each consequence separated by temporal regime; firstborn/tithe exception retained, inference not overextended to Temple maintenance, offspring question crosses page break and resolves by no stricter secondary sanctity. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/l01_bekhorot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch33_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch33_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch33_receipt.json',r.encoded(out));print(r.encoded(out).decode())
