from pathlib import Path
exec(compile((Path(__file__).parent/'helpers.py').read_text(encoding='utf8'),'helpers','exec'))
pre='bk.blessing_intent.20261126e5.'
assert r.sha(r.encoded(state))=='437890edf65f47c28802a5e19961c3981bae0a463daeaa249be16a4c267f37e9'
refs=['12a:'+str(i) for i in range(10,23)]
add('s','structure',refs,dict(title='Mistaken blessing intention versus ending; rejected proofs and unresolved beer case',primary=True,boundary='closed',legacy_ids=[]))
for n in range(10,23):add('u'+str(n),'utterances',['12a:'+str(n)],dict(textual_voice='Anonymous discussion with quoted authorities' if n in [17,18] else 'Anonymous discussion or quoted baraita',discourse_role='Question, proposed proof or distinction',composition='composite'))
def claim(k,n,text,holders,cond=(),status='Reported locally',unc=()):
 ref='12a:'+str(n);c('c'+k,ref,text,cond=cond);pos('p'+k,ref,'c'+k,holders,status,cond=cond,unc=unc)
 if unc:rows[-2]['uncertainty'].extend(unc)
claim('10wine',10,'Holding wine but thinking it beer, opening with beer in mind and ending for wine fulfills the obligation.',['Anonymous Gemara'],cond=['Actual drink wine','Initially thinks beer','Ends with wine blessing'],status='Stated obvious case')
claim('10reason',10,'Even saying shehakol over it would fulfill, because the Mishnah validates shehakol for all foods.',['Anonymous Gemara citing Mishnah'])
q('q11','12a:11','What if holding beer but thinking it wine, opening with wine in mind and ending for beer?')
q('q12','12a:12','Do we follow the essential beginning of the blessing or the concluding formula?')
claim('13bad',13,'The cited baraita invalidates a morning blessing beginning forms light but ending brings evenings.',['Cited baraita'],cond=['Morning','Starts Yotzer Or','Ends Maariv Aravim'])
claim('13good',13,'In morning it validates beginning brings evenings but ending forms light.',['Cited baraita'],cond=['Morning','Starts Maariv Aravim','Ends Yotzer Or'])
claim('14bad',14,'In evening it invalidates beginning brings evenings but ending forms light.',['Cited baraita'],cond=['Evening','Starts Maariv Aravim','Ends Yotzer Or'])
claim('14good',14,'In evening it validates beginning forms light but ending brings evenings.',['Cited baraita'],cond=['Evening','Starts Yotzer Or','Ends Maariv Aravim'])
claim('15',15,'The baraita summarizes: everything follows the concluding formula.',['Cited baraita'],status='General rule whose application to the beer case is challenged')
claim('16',16,'The discussion distinguishes that case because the ending says Blessed, Creator of the lights.',['Anonymous Gemara'],status='Rejects direct proof from long blessing')
claim('17rav',17,'Rav requires mention of the divine name for a blessing to count.',['Rav'])
claim('17yohanan',17,'Rabbi Yohanan requires mention of kingship for a blessing to count.',['Rabbi Yohanan'])
q('q17','12a:17','The distinguished ending works under Rav’s name requirement, but how under Yohanan’s kingship requirement?')
claim('18reason',18,'Rabbah bar Ulla’s explanation requires mentioning day by night and night by day.',['Rabbah bar Ulla'],unc=['This occurrence explicitly names Rabbah bar Ulla; do not silently substitute Rava from11b5.'])
claim('18scope',18,'Therefore the initial blessing and kingship declaration address both attributes.',['Anonymous Gemara'],status='Answer preserving distinction from beer case')
q('q19','12a:19','Does the concluding general rule everything follows the ending include the beer case?')
claim('20food',20,'The answer says it includes bread and dates instead.',['Anonymous Gemara'])
claim('20hyp',20,'The case of eating bread but thinking dates, opening for dates and ending for bread would itself be the unresolved question.',['Anonymous Gemara'],status='Rejected construction of proposed additional case')
claim('21',21,'The actual included case is eating dates while thinking bread, starting for bread and ending for dates; it is valid even if the ending had been for bread.',['Anonymous Gemara'],cond=['Actual food dates','Initially thinks bread'],status='Accepted narrower inclusion',unc=['The printed יצא after the dates ending is bracketed.'])
claim('22',22,'Dates too provide nourishment, explaining why the bread ending can work.',['Anonymous Gemara'])
for k,ref,surface,name in [('17r','12a:17','רב','רב'),('17y','12a:17',"ר' יוחנן",'רבי יוחנן'),('18','12a:18','רבה בר עולא','רבה בר עולא')]:att('a'+k,ref,surface,'quoted_authority',[name],'Named rule used by anonymous discussion')
for k,n,a,b,rel in [('10',10,'c10reason','c10wine','support'),('13g',13,'c13good','q12','support'),('13b',13,'c13bad','q12','support'),('14g',14,'c14good','q12','support'),('14b',14,'c14bad','q12','support'),('15',15,'c15','q12','support'),('16',16,'c16','c15','qualification'),('17',17,'q17','c16','objection'),('18',18,'c18scope','q17','answer'),('18r',18,'c18reason','c18scope','support'),('20',20,'c20food','q19','answer'),('21',21,'c21','c20hyp','correction'),('22',22,'c22','c21','support')]:edge('e'+k,'12a:'+str(n),a,b,rel)
for x in rows:
 if x['id'] in [pre+'q11',pre+'q12']:x['content']['answer_set_status']='partial';x['uncertainty'].append('No final resolution of the original beer/wine-intention case in this continuation; both attempted proofs are distinguished. No explicit תיקו is printed.')
 if x['id'] in [pre+'e13g',pre+'e13b',pre+'e14g',pre+'e14b',pre+'e15']:x['uncertainty'].append('Proposed support, subsequently distinguished; not a final answer to the original beverage question.')
 if x['layer']=='claims':x['content']['scope']='Exact actual-object/intended-object/ending combinations. Do not promote rejected proof attempts into a resolved rule for the original beer case.'
cov=[]
for ref in refs:
 for layer in r.LAYERS:
  ids=[x['id'] for x in rows if x['layer']==layer and any(e['segment_id']==by[ref]['id'] for e in x['evidence'])]
  cov.append(dict(segment_id=by[ref]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale='Read12a10–12b28; reread core12a10–22 for actual versus intended drink, four day/night endings, name/kingship distinction, initial declaration scope, rejected bread case and accepted dates case. Original beverage question remains without final resolution; no explicit teiku invented. Completed '+layer+' pass.'))
p=dict(schema_version=r.VERSION,tractate=j['tractate'],owner='/root/blind_reader_wave3',epoch=5,execution=dict(route='interactive_agent',agent_id='/root/blind_reader_wave3',model_id=None),records=rows,coverage=cov,open_tails=state['open_tails'],**{k:j[k] for k in ['source_sha256','schema_sha256','protocol_sha256']})
r.validate_apply(state,p,ss,j);r.immutable(HERE/'batch20_proposal.json',r.encoded(p));out=r.submit(JOB,HERE/'batch20_proposal.json',p['owner'],p['epoch']);r.immutable(HERE/'batch20_receipt.json',r.encoded(out));print(r.encoded(out).decode())
