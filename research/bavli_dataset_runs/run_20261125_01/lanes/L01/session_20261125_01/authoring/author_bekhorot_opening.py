"""Six original segments manually annotated; later discussion read as context only."""
from pathlib import Path
helpers=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L01/author_ketubot_opening.py').read_text(encoding='utf-8').split('# Primary ownership')[0]
exec(helpers.replace('bavli_ketubot','bavli_bekhorot').replace('kt.open1.','bek.open1.'))
add('s.mishnah','structure',['2a:1'],dict(title='Gentile ownership and firstborn-donkey exemption',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
add('s.necessity','structure',[f'2a:{i}' for i in range(2,7)],dict(title='Why each ownership and husbandry case is listed',primary=True,boundary='closed',legacy_ids=[]),origin='editorial_inference')
for ref,voice,role in [('2a:1','unnamed Mishnah','five ownership/husbandry cases, sale restriction, and scriptural exclusion'),('2a:2','anonymous Gemara','question about redundancy'),('2a:3','anonymous Gemara','need for purchase and sale cases'),('2a:4','anonymous Gemara citing Rabbi Yehuda','partnership contrast'),('2a:5','anonymous Gemara','receiving case paired with giving case'),('2a:6','anonymous Gemara','giving-case necessity and rejected fine')]:
    add('u.'+ref,'utterances',[ref],dict(textual_voice=voice,discourse_role=role,composition='composite'))
facts=[
('purchase',['2a:1'],'Purchasing the fetus of a gentile’s donkey is exempt from the firstborn obligation.',['purchase of fetus of gentile-owned donkey'],'asserted','unnamed Mishnah'),
('sale',['2a:1'],'Selling the fetus to a gentile is exempt from the firstborn obligation.',['sale of fetus to gentile'],'asserted','unnamed Mishnah'),
('sale_prohibited',['2a:1'],'The stated sale to a gentile is not permitted.',['sale described in Mishnah'],'asserted','unnamed Mishnah'),
('partnership',['2a:1'],'Partnership with a gentile is exempt from the firstborn obligation.',['gentile partnership'],'asserted','unnamed Mishnah'),
('receiving',['2a:1'],'Receiving the animal from a gentile under the stated husbandry arrangement is exempt from the firstborn obligation.',['המקבל הימנו'],'asserted','unnamed Mishnah'),
('giving',['2a:1'],'Giving the animal to a gentile under the stated husbandry arrangement is exempt from the firstborn obligation.',['הנותן לו בקבלה'],'asserted','unnamed Mishnah'),
('israel',['2a:1'],'The Mishnah derives the exclusion from בישראל: within Israel, not others.',['scope of firstborn obligation'],'asserted','unnamed Mishnah'),
('purchase_reason',['2a:3'],'If only purchase were taught, one could attribute its exemption to bringing the animal toward sanctity.',['hypothetical purchase-only teaching'],'hypothetical','anonymous argument'),
('sale_fine',['2a:3'],'One might instead impose a fine for sale because it removes the animal from sanctity.',['sale removes from sanctity'],'rejected','anonymous proposed inference'),
('sale_no_fine',['2a:3'],'The sale case teaches that the proposed fine does not override the exemption.',['sale case'],'asserted','anonymous explanation'),
('yehuda',['2a:4'],'Rabbi Yehuda holds that gentile partnership is subject to the firstborn obligation.',['gentile partnership'],'asserted','רבי יהודה as quoted'),
('partnership_contrast',['2a:4'],'The Mishnah expressly exempts partnership to exclude Rabbi Yehuda’s position.',['gentile partnership'],'asserted','anonymous explanation'),
('paired',['2a:5'],'Receiving under the arrangement is listed because the teaching also wishes to list giving under it.',['paired receiving/giving clauses'],'asserted','anonymous explanation'),
('giving_fine',['2a:6'],'One might impose a fine in the giving arrangement because the underlying animal is Israelite-owned and confusion with another animal might follow.',['underlying animal belongs to Israelite','giving under husbandry arrangement'],'rejected','anonymous proposed inference'),
('giving_no_fine',['2a:6'],'The giving clause teaches exemption despite the proposed fine and confusion rationale.',['giving arrangement described'],'asserted','anonymous explanation')]
for key,refs,text,conditions,mode,holder in facts:
    claim('c.'+key,refs,text,conditions,mode,scope='Firstborn-donkey opening; transactional scope as stated in original')
    position('p.'+key,refs,holder,'c.'+key,conditions,'hypothetical argument rejected by קמשמע לן' if mode=='rejected' else ('candidate explanatory argument' if mode=='hypothetical' else 'local assertion; not later practical adjudication'))
question('q.all',['2a:2'],'Why are all these cases needed?',status='partial')
question('q.partnership',['2a:4'],'Why explicitly teach partnership?',status='partial')
question('q.receiving',['2a:5'],'Why explicitly teach receiving?',status='partial')
question('q.giving',['2a:6'],'Why explicitly teach giving?',status='partial')
attr('a.mishnah',['2a:1'],'unnamed Mishnah','anonymous','opening clauses',candidates=[])
attr('a.yehuda',[('2a:4','דרבי יהודה דאמר שותפות עובד כוכבים חייבת בבכורה')],'רבי יהודה','quoted_authority','gentile partnership firstborn obligation')
relations=[('israel',['2a:1'],'c.israel','c.purchase','support'),('israel_sale',['2a:1'],'c.israel','c.sale','support'),('israel_partner',['2a:1'],'c.israel','c.partnership','support'),('israel_receive',['2a:1'],'c.israel','c.receiving','support'),('israel_give',['2a:1'],'c.israel','c.giving','support'),('purchase',['2a:3'],'c.purchase_reason','q.all','answer'),('sale_fine',['2a:3'],'c.sale_fine','c.sale','objection'),('sale_answer',['2a:3'],'c.sale_no_fine','c.sale_fine','answer'),('partner',['2a:4'],'c.partnership_contrast','q.partnership','answer'),('partner_difference',['2a:4'],'c.partnership','c.yehuda','objection'),('receiving',['2a:5'],'c.paired','q.receiving','answer'),('giving_fine',['2a:6'],'c.giving_fine','c.giving','objection'),('giving_answer',['2a:6'],'c.giving_no_fine','c.giving_fine','answer'),('giving_need',['2a:6'],'c.giving_no_fine','q.giving','answer')]
for key,refs,src,target,rel in relations: edge('e.'+key,refs,src,target,rel)
coverage=[]
for ref in [f'2a:{i}' for i in range(1,7)]:
    sid=byref[ref]['id']
    for layer in r.LAYERS:
        ids=[x['id'] for x in records if x['layer']==layer and any(e['segment_id']==sid for e in x['evidence'])]
        coverage.append(dict(segment_id=sid,layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=f'Original Bekhorot {ref} read with continuation through2b:22. '+('Omission pass retained all five Mishnah cases, sale restriction, Israel exclusion, purchase/sale distinction, Rabbi Yehuda disagreement, paired clauses and rejected fines; no additional item found in this scope.' if layer=='reconciliation' else f'{layer} pass performed; actual findings listed, no further independent object when empty.')))
p=dict(schema_version=r.VERSION,tractate='Bekhorot',owner='/root/l01_bekhorot',epoch=2,source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],execution=dict(route='interactive_agent',agent_id='/root',model_id=None),records=records,coverage=coverage,open_tails=[])
r.validate_apply(r.current(job),p,rows,j)
out=base/'bekhorot_proposals/opening_001.json'; r.immutable(out,r.encoded(p))
print(json.dumps(dict(path=str(out),sha256=r.sha(out.read_bytes()),records=len(records),segments=6)))
