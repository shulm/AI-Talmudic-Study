import json
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
w=json.loads((job/'window008.json').read_text(encoding='utf-8'));seg=w['segments'];p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=['yev004.override','yev005.override','yev006.karet','yev007.karet','yev008.exception'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev008.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Need for עליה through brother’s-wife exception, expanded permission and forbidden-relations analogy',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=holder if isinstance(holder,list) else [holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' within local sequence'),[c],u);return c
def q(k,inds,text,cond=[]):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('exception','structure',list(range(24)),dict(title='Brother’s wife as exception: hermeneutic categories, leper precedent and chronology, alternative scriptural analogy',primary=True,boundary='open_both',legacy_ids=[]))
rec('continuation','edges',[0],dict(source_id='yev007.karet',target_id='yev008.exception',relation='continuation',explicitness='source_explicit'),['yev007.karet','yev008.exception'])
roles=['New proposed exception-teaches-general-class explanation','Baraita introduces example of exception teaching general class','Peace-offering analogy restricts impurity rule to altar sancta','Proposed brother’s-wife permission generalized to all relatives','Objection: prohibition/prohibition unlike prohibition/permission','Alternative category: new-law exception requires explicit return','Leper guilt-offering verse and question on comparison to sin-offering','Novel thumb/toe ritual could displace ordinary altar requirements','Explicit comparison restores blood and fats altar requirements','Counterfactual absence of return and local conclusion only brother’s wife permitted','Simple analogy from brother’s wife proposed','One prohibition versus two; once permitted broader permission proposed','Evidence question; leper on Passover eve after seminal emission and immersion admitted','Karet-positive priority rationale; Rabbi Yohanan denies Torah positive prohibition','New courtyard interpreted as new tevul-yom exclusion from Levite camp','Ulla’s once-permitted explanation and analogy challenge','Chronology: deceased brother’s marriage first proposed sufficient','Reverse marriage order objection','Even deceased marriage first insufficient unless death precedes survivor’s marriage','Ulla’s night-of-eighth-day exclusion provides control case','עליה needed for interval-of-eligibility chronology','Alternative heqesh; Rabbi Yonah or Rav Huna son of Rav Yehoshua','Rav Aha of Difti asks Ravina why compare to wife’s sister rather than brother’s wife','Two anonymous alternatives: stringent analogy or matching two prohibitions']
for i,role in enumerate(roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous framing and embedded authorities',discourse_role=role,composition='composite'))
 rec('a'+str(i),'attributions',[i],dict(surface='anonymous discussion' if i not in [1,2,6,7,8,12] else 'anonymous cited baraita',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
attrs=[('sages',[12,13],'אמרו חכמים','collective',['sages'],'Permission for the specified leper to enter',[]),('yohanan',[13,14],"ר' יוחנן",'speaker',['Rabbi Yohanan'],'No Torah positive prohibition; new courtyard interpretation',[]),('ulla',[15],'עולא','speaker',['Ulla'],'Permission for leprosy extends to seminal impurity',[]),('variant',[21],'רבי יונה ואיתימא רב הונא בריה דרב יהושע','quoted_authority',['Rabbi Yonah','Rav Huna son of Rav Yehoshua'],'Alternative attribution of forbidden-relations comparison',[]),('aha',[22],'רב אחא מדפתי','speaker',['Rav Aha of Difti'],'Question directed to Ravina',[])]
for k,inds,surface,role,candidates,scope,chain in attrs:rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=chain),u=['Alternative attribution preserved; no unique holder chosen.'] if k=='variant' else (['Rabbi Yohanan’s name in 7b:7 is parenthesized in source.'] if k=='yohanan' else []))
a=claim('exception_general',[0],'Brother’s wife might be treated as an exception that teaches the entire class, permitting all forbidden relatives in yibbum.','hypothetical')
b=q('example_general',[1],'What is an example of an item leaving a general category to teach the whole?')
c=claim('peace_altar',[2],'Peace offerings were included in sacred objects but singled out to teach that the impurity rule concerns altar sancta.',holder='anonymous hermeneutic baraita')
d=claim('maintenance_excluded',[2],'Temple-maintenance sancta are excluded from this impurity rule.',holder='anonymous hermeneutic baraita');edge('example_answer',[2],c,b,'answer');edge('example_exclusion',[2],d,c,'qualification')
e=claim('wife_analogy',[3],'By the proposed analogous reading, brother’s wife was singled out from forbidden relatives to permit all of them in yibbum.','hypothetical');edge('wife_general_support',[3],e,a,'support');edge('peace_pattern',[2,3],c,e,'analogy')
f=claim('unlike',[4],'The peace-offering general and special cases are both prohibitions; here the general case is prohibited while the special case is permitted.');edge('unlike_obj',[4],f,e,'objection')
g=claim('new_rule',[5],'An item singled out for a novel rule cannot be restored to its general category without an explicit scriptural return.',holder='anonymous quoted hermeneutic baraita')
h=claim('new_classification',[5],'Brother’s wife instead resembles an exception adjudicated under a novel rule.');edge('classify_correct',[5],h,a,'correction')
j=q('guilt_comparison',[6],'Why say that the guilt offering is like the sin offering?')
k=claim('leper_novel',[7],'The leper’s guilt offering has a novel ritual involving right thumb and right big toe.',holder='anonymous guilt-offering baraita')
l=claim('no_altar_hyp',[7],'The novel ritual could suggest no requirement for blood application and fats on the altar.','hypothetical',holder='anonymous guilt-offering baraita')
m=claim('altar_restore',[8],'The explicit sin-offering comparison requires blood application and fats on the altar for the guilt offering as for the sin offering.',holder='anonymous guilt-offering baraita')
edge('comparison_answer',[8],m,j,'answer');edge('altar_correct',[8],m,l,'correction');edge('new_rule_example',[6,7,8],m,g,'support')
n=claim('counterfactual_return',[9],'Without explicit restoration, the text describes the departure according to what was or was not singled out.','hypothetical',u=['Compressed למאי דנפק נפק ולמאי דלא נפק לא נפק kept without forcing an expanded legal model.'])
o=claim('only_brothers_wife',[9],'Here only brother’s wife, which was permitted, would be permitted; the other relatives would not.');edge('no_generalization',[9],o,e,'correction')
pp=claim('simple_analogy',[10],'One might infer by simple analogy that wife’s sister undergoes yibbum just as brother’s wife does.','hypothetical')
r=claim('one_two',[11],'Ordinary brother’s wife involves one prohibition while wife’s sister in yibbum involves two.');edge('one_two_obj',[11],r,pp,'objection')
s=claim('once_permitted',[11],'One might nevertheless argue that once permission has been granted it extends to the additional prohibition.','hypothetical');edge('permission_answer',[11],s,r,'answer')
t=q('permission_source',[12],'Where do we find once-permitted extension?')
v=claim('leper_entry',[12],'A leper whose eighth day is Passover eve, who has a seminal emission that day and immerses, may enter although another tevul yom may not.',cond=['Eighth day on Passover eve','Seminal emission that day','Immersion performed'],holder='sages in baraita')
wq=claim('priority',[13],'A positive command carrying karet should override a positive command without karet.',holder='sages/baraita continuation')
x=claim('no_torah_positive',[13],'Under Torah law there is not even a positive prohibition in this entry restriction.',holder='Rabbi Yohanan')
y=q('new_court',[14],'What is the new courtyard in II Chronicles 20:5?')
z=claim('court_decree',[14],'New rules were instituted there: a tevul yom was barred from the Levite camp.',holder='Rabbi Yohanan',u=['Name printed parenthetically in this segment; prior unparenthesized attribution retained.'])
aa=claim('ulla_permission',[15],'Because entry was permitted for his leprosy, it is permitted for his seminal impurity.',holder='Ulla')
edge('leper_example',[12],v,t,'answer');edge('priority_support',[13],wq,v,'support');edge('yohanan_qual',[13],x,wq,'qualification');edge('court_answer',[14],z,y,'answer');edge('decree_support',[14],z,x,'support');edge('ulla_reason',[15],aa,v,'support');edge('once_support',[15],aa,s,'support')
bb=q('ulla_analogy',[15],'Is the proposed yibbum case comparable to Ulla’s case?')
cc=claim('dead_first',[16],'The once-permitted analogy initially seems possible when the deceased brother married before the survivor married.','hypothetical',cond=['Deceased brother’s marriage precedes survivor’s marriage'])
dd=claim('survivor_first',[17],'If the survivor married first, the wife’s-sister prohibition came first, defeating that chronology.','conditional',cond=['Survivor’s marriage precedes deceased brother’s marriage'])
ee=claim('interim_eligibility',[18],'Even with the deceased brother’s marriage first, the analogy works only if he died before the survivor married, leaving an intervening period of eligibility.','conditional',cond=['Deceased married and died before survivor married'])
ff=claim('no_interval',[18],'If the deceased married but remained alive until after the survivor’s marriage, she was never eligible in the interval.','conditional',cond=['Deceased brother alive at survivor’s marriage'])
gg=claim('night_case',[19],'Ulla would agree that a seminal emission on the night of the eighth day prevents insertion of hands for the thumb ritual, since no offering-eligible time had yet arrived.','conditional',cond=['Seminal emission on night preceding eighth day'],holder='Ulla as explicitly invoked by anonymous question')
edge('chronology_answer',[16],cc,bb,'answer');edge('earlier_sister',[17],dd,cc,'qualification');edge('interval_required',[18],ee,cc,'qualification');edge('never_eligible',[18],ff,cc,'objection');edge('night_support',[19],gg,ee,'support')
hh=claim('aleha_interval',[20],'עליה is needed for the case where the deceased brother married and died before the survivor married.','conditional',cond=['Intervening eligibility before wife’s-sister prohibition'])
edge('interval_resolution',[20],hh,bb,'local_resolution')
ii=claim('heqesh_all',[21],'Leviticus 18:29 compares all forbidden relatives to brother’s wife, so without עליה one could infer permission for all in yibbum.','hypothetical',holder=['Rabbi Yonah','Rav Huna son of Rav Yehoshua'],u=['ואיתימא gives two alternatives, not joint endorsement.'])
jj=claim('aleha_blocks',[21],'עליה blocks that proposed general permission.')
edge('heqesh_correction',[21],jj,ii,'correction')
kk=q('which_model',[22],'Why compare all forbidden relatives to wife’s sister rather than brother’s wife, when either comparison is available?')
ll=claim('stringent',[23],'When the comparison could be lenient or stringent, the stringent comparison is chosen.','asserted',cond=['First anonymous alternative reply'])
mm=claim('two_from_two',[23],'Other yibbum relatives involve two prohibitions like wife’s sister; two are learned from two rather than from brother’s wife’s single prohibition.','asserted',cond=['Second anonymous alternative reply'])
edge('model_answer1',[23],ll,kk,'answer');edge('model_answer2',[23],mm,kk,'answer')
for i in range(24):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=roles[i]+'. Read full chronological refinement and alternative analogy through 8a:8, with Rava continuation through 8b:8. '
  rationale+=('Reread for distinctions between rule/example/application, two marriage orders, actual interval of eligibility, parenthesized attribution, and ואיתימא alternatives; no unique attribution forced.' if layer=='reconciliation' else ('Actual '+layer+' pass found no separate item.' if not ids else 'Completed '+layer+' pass with evidence.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal008.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('records',len(p['records']))
