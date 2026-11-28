import json
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
w=json.loads((job/'window002.json').read_text(encoding='utf-8'));seg=w['segments'];p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=[])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev002.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Local opening-Mishnah discussion',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' in local argument; not global halakhic ruling'),[c],u);return c
def q(k,inds,text,cond=[]):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
for k,inds,title in [('order',list(range(11)),'Why the fifteen relatives occur in this order'),('wording',list(range(11,16)),'Exemption wording, halitzah linkage and precedence'),('number',list(range(16,22)),'Two counts, Rav and Rav Assi, and absence of recursive co-wives')]:rec(k,'structure',inds,dict(title=title,primary=True,boundary='closed',legacy_ids=[]))
roles=['Question: why wife’s sister is not first','Hypothetical severity ordering and cited Rabbi Shimon','Two objections to severity ordering','Alternative explanation: daughter is derived','Challenge and distinction: basic prohibition versus yibbum application','Rava’s report from Rav Yitzhak bar Avdimi: הנה','Continuation of reported derivation: זמה','Challenge to position of wife’s sister and kinship reply','Objection to grouping and revised kinship ordering','Two generational associative-order explanations','Own kin, sister group, brother group, and daughter-in-law ordering','Question about exemption wording and rejected narrower inference','Alternative wording, counter-question and risk response','Final distinction: co-wife prohibited only within mitzvah context','Question why both acts and general linkage response','Two alternative formulations and Abba Shaul response','Two questions about restrictive enumeration','Proposed exclusions and challenge for Rav and Rav Assi','Conditional branch assuming mutual acceptance','Conditional branch assuming no mutual acceptance','Challenge: include their cases','Answer: absent co-wife-of-co-wife case']
for i,role in enumerate(roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous Gemara' if i not in [5,6] else 'Rava reporting Rav Yitzhak bar Avdimi',discourse_role=role,composition='composite' if i not in [3,6,16,20,21] else 'atomic'))
 rec('a'+str(i),'attributions',[i],dict(surface='anonymous discussion' if i not in [5,6] else 'רבא אמר לי רב יצחק בר אבדימי',role='anonymous' if i not in [5,6] else 'transmitter',candidates=[] if i not in [5,6] else ['Rava'],scope=role,transmission_chain=[] if i not in [5,6] else ['Rava','Rav Yitzhak bar Avdimi']))
rec('shimon','attributions',[(1,'ר"ש')],dict(surface='ר"ש',role='quoted_authority',candidates=['Rabbi Shimon'],scope='Severity of burning; identification of Mishnah with him is hypothetical only',transmission_chain=[]))
rec('yitzhak','attributions',[5,6],dict(surface='רב יצחק בר אבדימי',role='quoted_authority',candidates=['Rav Yitzhak bar Avdimi'],scope='הנה/זמה derivations reported by Rava',transmission_chain=['Rava','Rav Yitzhak bar Avdimi']))
rec('abba','attributions',[(15,'אבא שאול')],dict(surface='אבא שאול',role='quoted_authority',candidates=['Abba Shaul'],scope='Halitzah mitzvah precedence',transmission_chain=[]))
for name,can in [('רב','Rav'),('רב אסי','Rav Assi')]:rec('authority.'+can.replace(' ',''),'attributions',[17,18,19,20],dict(surface=name,role='quoted_authority',candidates=[can],scope='Unnamed rulings discussed as possible exclusions from the fifteen; agreement left conditional',transmission_chain=[]),u=['Ruling content is not stated in this source window; no reconstruction from later passages yet.'])
a=claim('derive_sister',[0],'The yibbum exclusions of all listed relatives are derived from wife’s sister.')
b=q('why_sister_first',[0],'Given this derivation, why is wife’s sister not listed first?');edge('derive_premise',[0],a,b,'support')
c=claim('severity',[1],'Perhaps the Mishnah orders cases by severity and follows Rabbi Shimon, for whom burning is more severe.','hypothetical');d=claim('shimon_burning',[1],'Burning is more severe.','asserted',holder='Rabbi Shimon')
edge('severity_answer',[1],c,b,'answer');edge('shimon_support',[1],d,c,'support')
e=q('mother_first',[(2,'אי הכי ליתני חמותו ברישא דעיקר שריפה בחמותו כתיבא')],'On severity ordering, why not mother-in-law first, since burning is written principally concerning her?',['Assume proposed severity order'])
f=q('daughterinlaw_next',[(2,'ועוד בתר חמותו ליתני כלתו דבתר שריפה סקילה חמורה')],'Why not daughter-in-law after mother-in-law, since stoning follows burning in severity?',['Assume proposed severity order'])
edge('objection1',[2],e,c,'objection');edge('objection2',[2],f,c,'objection')
g=claim('daughter_derivation',[3],'The daughter is placed first because a rule learned by exposition is especially valued by the tanna.');edge('newanswer',[3],g,b,'answer')
h=q('all_derived',[(4,'כולהו נמי מדרשא אתו')],'Are not all these rules learned by exposition?');edge('all_obj',[4],h,g,'objection')
j=claim('distinction',[4],'Although all yibbum applications are derived, the other basic prohibitions are explicit, while the daughter’s basic prohibition is derived.');edge('distinction_ans',[4],j,h,'answer');edge('distinction_sup',[4],j,g,'support')
k=claim('hena',[5],'A verbal analogy links הנה in Leviticus 18:10 and 18:17 in the daughter derivation.','asserted',holder='Rav Yitzhak bar Avdimi',u=['This brief quotation does not separately explicate every derivational step.'])
l=claim('zima',[6],'A verbal analogy links זמה in Leviticus 18:17 and 20:14 in the continuation of the daughter derivation.','asserted',holder='Rav Yitzhak bar Avdimi',u=['Penalty linkage inferred by context; no expanded derivation supplied in the quote.'])
edge('deriv1',[5],k,j,'support');edge('deriv2',[6],l,j,'support')
m=q('sister_last',[(7,'השתא דאמרת כל מלתא דאתיא מדרשא חביבא ליה ליתני לאחות אשה לבסוף')],'If derivational rules are preferred, why is wife’s sister not last?')
n=claim('sister_group',[(7,'איידי דאיירי באיסור אחוותא תנא אחות אשתו')],'Wife’s sister occurs there because the Mishnah is discussing sister prohibitions.');edge('sister_answer',[7],n,m,'answer')
o=q('group_last',[(8,'וליתנייא להאי בבא לבסוף')],'Why not place this entire group last?');edge('group_obj',[8],o,n,'objection')
pp=claim('kinship',[8],'The tanna arranges near relations together, starting with daughter and her two descendants as his own relatives.');edge('kinship_answer',[8],pp,o,'answer')
r=claim('wife_down',[9],'After three descending generations on his side, the tanna lists three descending generations on her side.')
s=claim('wife_up',[9],'After her descending generations, the tanna lists three ascending generations on her side.')
t=claim('sister_own',[10],'His sister and mother’s sister are listed as his own relatives, and wife’s sister is grouped with sister prohibitions.')
v=claim('brother_group',[10],'Although daughter-in-law should precede the wife of a noncontemporaneous brother under kinship ordering, brother prohibitions keep that brother’s wife in the brother group before daughter-in-law.',['The noncontemporaneous-brother prohibition is not due to kinship in the same sense used by this ordering rationale']) if False else claim('brother_group',[10],'Although daughter-in-law would precede the noncontemporaneous brother’s wife by kinship ordering, the brother-prohibition group accounts for the reverse order; the text says the latter is not prohibited on kinship grounds.');
for idx,cid in enumerate([r,s,t,v]):edge('kinship_detail'+str(idx),[9 if idx<2 else 10],cid,pp,'support')
wq=q('why_exempt',[(11,'ומאי איריא דתנא פוטרות ליתני אוסרות')],'Why say exempt rather than prohibit?')
x=claim('prohibit_inference',[11],'Had the Mishnah said prohibit, one could mistakenly understand yibbum alone to be prohibited while halitzah remains.','hypothetical')
edge('exempt_answer',[11],x,wq,'answer')
y=q('forbid_halitzah',[(12,'וליתני אסורה לחלוץ')],'Why not explicitly say halitzah is forbidden?')
z=q('what_harm',[(12,'מאי קעביד')],'What would she be doing wrong by halitzah?')
zz=claim('risk',[12],'Saying she performs halitzah may lead to yibbum.','conditional',cond=['If she is said to perform halitzah'])
edge('harm_challenge',[12],z,y,'objection');edge('harm_response',[12],zz,z,'answer')
aa=claim('mitzvah_scope',[13],'The co-wife prohibition exists only in a levirate-mitzvah situation; outside that situation the co-wife is permitted, so the Mishnah uses exemption language.');edge('scope_answer',[13],aa,wq,'answer')
bb=q('why_both',[(14,'ומאי איריא דתני מן החליצה ומן הייבום ליתני מן הייבום לחודיה')],'Why mention both halitzah and yibbum rather than yibbum alone?')
cc=claim('yibbum_only',[14],'Mentioning exemption from yibbum alone could leave the mistaken inference that halitzah is still performed.','hypothetical')
dd=claim('link_positive',[14],'Whoever is subject to yibbum is subject to halitzah.')
ee=claim('link_negative',[14],'Whoever is not subject to yibbum is not subject to halitzah.')
for idx,cid in enumerate([cc,dd,ee]):edge('both_answer'+str(idx),[14],cid,bb,'answer')
ff=q('reverse_order',[(15,'וליתני מן הייבום ומן החליצה')],'Why not list yibbum before halitzah?')
gg=q('halitzah_only',[(15,'א"נ מן החליצה לחודה')],'Alternatively why not mention exemption from halitzah alone?')
hh=claim('abba_precedence',[15],'The Mishnah follows Abba Shaul, who says the mitzvah of halitzah takes precedence over the mitzvah of yibbum.');ii=claim('abba_rule',[15],'The mitzvah of halitzah takes precedence over the mitzvah of yibbum.','asserted',holder='Abba Shaul')
edge('precedence_answer',[15],hh,ff,'answer');edge('precedence_answer2',[15],hh,gg,'answer');edge('abba_support',[15],ii,hh,'support')
jj=q('count_first',[16],'What does the opening count exclude?');kk=q('count_last',[16],'What does the final count exclude?')
ll=claim('counts',[17],'The counts exclude the rulings of Rav and Rav Assi.',u=['Precise rulings are not identified in this window; preserve as unresolved references.'])
edge('count_answer1',[17],ll,jj,'answer');edge('count_answer2',[17],ll,kk,'answer')
mm=q('rav_counts',[17],'For Rav and Rav Assi themselves, what do the counts exclude?')
nn=claim('agree_branch',[18],'If Rav and Rav Assi accept each other’s ruling, one count excludes the co-wife of one who refused and the other the co-wife of one who remarries his divorced wife.','conditional',cond=['Rav and Rav Assi accept each other’s rulings'])
oo=claim('disagree_branch',[19],'If they do not accept each other’s ruling, one count excludes the other’s case and the other excludes either the co-wife of one who refused or the co-wife of one who remarries his divorced wife.','conditional',cond=['Rav and Rav Assi do not accept each other’s rulings'],u=['Which alternative applies is left disjunctive; no assignment by name order.'])
edge('agree_answer',[18],nn,mm,'answer');edge('disagree_answer',[19],oo,mm,'answer')
qq=q('include_cases',[20],'According to Rav and Rav Assi, why not list their cases?')
rr=claim('no_recursive',[21],'Those cases are not included because they do not have the co-wife-of-co-wife situation.',u=['Antecedent is the challenged additional cases; their exact substantive content remains unexpanded here.']);edge('no_recursive_answer',[21],rr,qq,'answer')
for i in range(22):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale='Read with 2a:1–2b:8 and continuation through 3b:10. '+roles[i]+'. '
  if layer=='reconciliation':rationale+='Reread for omitted alternatives, conditional assumptions, attribution roles and local replacement answers; counts do not resolve whether Rav and Rav Assi agree.'
  elif not ids:rationale+='No separate '+layer+' record after source-based pass; question-only units were not forced into asserted claims.'
  else:rationale+='Completed '+layer+' pass on these explicit source units.'
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal002.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('records',len(p['records']))
