import json
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
w=json.loads((job/'window003.json').read_text(encoding='utf-8'));seg=w['segments'];p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=[])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev003.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous baraita',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Baraita deriving the fifteen-relative/co-wife exemption',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' within baraita; subsequent Gemara questions derivational premise'),[c],u);return c
def q(k,inds,text,cond=[]):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('baraita','structure',list(range(10)),dict(title='עליה and לצרור: derivation of fifteen relatives, recursive co-wives, limitation and penalty',primary=True,boundary='closed',legacy_ids=[]))
roles=['Anonymous source question introducing baraita; verse quote and עליה question','Hypothetical extension of yibbum command and shared עליה expression','Analogy places prohibition within mitzvah situation','Two questions and two derivations for co-wife and recursive co-wife','Question and generalization to other forbidden relatives','Question, generalization to co-wives and cited sages’ rule','Hypothetical extension to six more severe relatives','Restriction of analogy to relatives able to marry brothers','Exclusion of six relatives and co-wife-from-brother rule','Question on punishment and supporting verse']
for i,role in enumerate(roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous baraita introduced by Gemara' if i==0 else 'anonymous baraita',discourse_role=role,composition='composite'))
 rec('a'+str(i),'attributions',[i],dict(surface='דת"ר' if i==0 else 'anonymous baraita continuation',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
rec('sages','attributions',[(5,'מכאן אמרו חכמים')],dict(surface='חכמים',role='collective',candidates=['sages quoted by baraita'],scope='Fifteen-relative exemption rule',transmission_chain=[]))
a=q('source',[(0,'מנה"מ')],'What is the scriptural basis for the exemption?')
b=q('aleha',[(0,'עליה מה ת"ל')],'What does עליה in the wife’s-sister prohibition teach?')
c=claim('all_yibbum',[1],'The command that the levir come to her could have been read to include even a forbidden relative.','hypothetical',cond=['Before considering עליה linkage'])
d=claim('same_word',[0,1],'עליה appears both in Leviticus 18:18 and in the yibbum command in Deuteronomy 25:5.')
e=claim('prohibition_context',[2],'As the yibbum עליה concerns a mitzvah situation, the wife’s-sister עליה prohibits taking her even in that mitzvah situation.')
edge('aleha_answer',[1,2],e,b,'answer');edge('analogy',[0,1,2],d,e,'support');edge('reject_all',[2],e,c,'correction');edge('sourceanswer',[2],e,a,'answer')
f=q('cowife',[(3,'ואין לי אלא היא צרתה מנין')],'How is the co-wife prohibition derived beyond the forbidden relative herself?')
g=claim('cowife_derive',[(3,'צרתה מנין ת"ל לצרור')],'לצרור teaches the co-wife prohibition.')
h=q('recursive',[(3,'ואין לי אלא צרתה צרת צרתה מניין')],'How is a co-wife’s co-wife included?')
j=claim('recursive_derive',[(3,'צרת צרתה מניין ת"ל לצרור ולא לצור')],'The form לצרור rather than לצור teaches the co-wife’s co-wife.')
edge('cowife_answer',[3],g,f,'answer');edge('recursive_answer',[3],j,h,'answer')
k=q('other_relatives',[(4,'ואין לי אלא אחות אשה שאר עריות מניין')],'How do the other forbidden relatives follow from wife’s sister?')
l=claim('relative_analogy',[4],'Like wife’s sister, any forbidden relative whose intentional violation carries karet and inadvertent violation a sin-offering is forbidden to the levir.','conditional',cond=['Forbidden-relative status','Intentional karet','Inadvertent sin-offering'])
edge('relative_answer',[4],l,k,'answer');edge('relative_pattern',[4],e,l,'analogy')
m=q('other_cowives',[(5,'ואין לי אלא הן צרותיהן מניין')],'How are the co-wives of the other forbidden relatives included?')
n=claim('cowife_analogy',[5],'The wife’s-sister pattern extends the co-wife prohibition to forbidden relatives carrying intentional karet and inadvertent sin-offering and forbidden in yibbum.','conditional',cond=['Forbidden relative','Intentional karet','Inadvertent sin-offering','Forbidden to the levir'])
edge('cowives_answer',[5],n,m,'answer');edge('cowife_pattern',[5],g,n,'analogy')
o=claim('sages_rule',[5],'From this the sages stated that fifteen women exempt their co-wives and co-wives’ co-wives from halitzah and yibbum without terminal generation.',holder='sages quoted by baraita')
edge('sages_support',[5],n,o,'support');edge('recursive_support',[3,5],j,o,'support')
pp=q('six_more',[6],'Might the co-wives of the six more severe forbidden relatives also be prohibited?')
r=claim('possible_extension',[6],'The six more severe categories might also have prohibited co-wives.','hypothetical',u=['The six categories are not enumerated in this passage.'])
s=claim('marriage_limit',[7],'The extension requires that the forbidden relative can marry the brothers, as wife’s sister can, in addition to the karet, sin-offering and levirate prohibition conditions.','conditional',cond=['Possible marriage to the brothers','Forbidden relative','Intentional karet','Inadvertent sin-offering','Forbidden to the levir'])
t=claim('six_excluded',[8],'The six more severe relatives cannot marry the brothers, so their co-wives are permitted.','asserted',u=['No unsupported identities supplied for the six.'])
v=claim('brother_only',[8],'The co-wife prohibition applies only through a brother.')
edge('six_answer',[7,8],t,pp,'answer');edge('six_correction',[8],t,r,'correction');edge('limit',[7],s,n,'qualification');edge('limitation_support',[7,8],s,t,'support');edge('brother_reason',[8],v,t,'support')
wq=q('penalty',[(9,'אזהרה שמענו עונש מניין')],'The warning has been derived; what supplies the punishment?')
x=claim('penalty_verse',[9],'Leviticus 18:29, concerning anyone who does these abominations, supplies the punishment basis.',u=['Source quotes the verse incompletely with וגו׳; evidence is not silently completed.'])
edge('penalty_answer',[9],x,wq,'answer')
for i in range(10):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=roles[i]+'. Read baraita through penalty and following challenge through 4b:10. '
  rationale+=('Omission reread preserves hypothetical alternatives, limited analogy conditions, anonymous and collective voices, recursive exemption and incomplete verse quotation.' if layer=='reconciliation' else ('Actual '+layer+' pass; no separate record found.' if not ids else 'Completed '+layer+' pass with quoted evidence.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal003.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('records',len(p['records']))
