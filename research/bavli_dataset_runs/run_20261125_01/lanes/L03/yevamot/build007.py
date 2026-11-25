import json
from pathlib import Path
job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');out=Path(__file__).parent
w=json.loads((job/'window007.json').read_text(encoding='utf-8'));seg=w['segments'];p={k:w['job'][k] for k in ['schema_version','tractate','source_sha256','schema_sha256','protocol_sha256']};p.update(owner='L03/yevamot',epoch=2,execution={'route':'interactive_agent','agent_id':'/root/yevamot','model_id':None},records=[],coverage=[],open_tails=['yev004.override','yev005.override','yev006.karet','yev007.karet'])
def ev(i,q=None):
 s=seg[i];t=s['text'];a=0 if q is None else t.index(q);b=len(t) if q is None else a+len(q);return dict(segment_id=s['id'],start_char=a,end_char=b,quote=t[a:b])
def rec(k,l,inds,c,links=[],u=[],origin='source_paraphrase'):
 rid='yev007.'+k;p['records'].append(dict(id=rid,layer=l,evidence=[ev(i) if isinstance(i,int) else ev(*i) for i in inds],content=c,links=links,uncertainty=u,origin=origin));return rid
def claim(k,inds,prop,mode='asserted',cond=[],holder='anonymous Gemara',u=[]):
 c=rec(k,'claims',inds,dict(proposition=prop,conditions=cond,scope='Judicial burning and Sabbath: proposed source for needing explicit exclusion',assertion_mode=mode),u=u)
 rec(k+'.p','positions',inds,dict(holder_candidates=[holder],claim_id=c,question_id=None,conditions=cond,local_status=mode+' in argument; retrospective hypothetical stages remain distinct'),[c],u);return c
def q(k,inds,text,cond=[]):return rec(k,'questions',inds,dict(formulation=text,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def edge(k,inds,a,b,rel):return rec(k,'edges',inds,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
rec('karet','structure',list(range(20)),dict(title='Judicial burning on Sabbath: purpose of מושבות, disputed burning category, a-fortiori derivation and retrospective override reading',primary=True,boundary='open_both',legacy_ids=[]))
rec('continuation','edges',[0],dict(source_id='yev006.karet',target_id='yev007.karet',relation='continuation',explicitness='source_explicit'),['yev006.karet','yev007.karet'])
roles=['Judicial-burning source proposed; school asks verse purpose','Question challenged because Rabbi Yose and Rabbi Natan supply purposes','Baraita: Rabbi Yose ordinary prohibition versus Rabbi Natan separate-liability function','Rava clarifies the question concerns מושבות','Personal Sabbath obligation applies everywhere; why מושבות?','Unnamed student quotes Rabbi Yishmael: competing readings of execution and Sabbath commands','Renewed alternative and comparison of מושבות verses','Court context carried over; burning forbidden in court too','Rabbi Natan attribution and absent-verse override proposed','Rabbi Yose attribution proposed; ordinary-burning limitation raised','Judicial burning includes cooking a wick','Rav Sheshet equates wick cooking with cooking dyes','Rav Shimi bar Ashi replaces override explanation with a-fortiori explanation','A-fortiori: execution displaces service, service displaces Sabbath','או אינו explained through unattended corpse counterexample and counter-derivation','Corpse/service basis from ולאחותו; no-burning verse defeats conclusion','Retrospective question about או אינו under initial override assumption','Retrospective first stage: court execution excepted by positive-command override','Retrospective hesitation about karet and rejoinder about relative severity','Retrospective little/great severity argument defeated by no-burning verse']
for i,role in enumerate(roles):
 rec('u'+str(i),'utterances',[i],dict(textual_voice='anonymous framing and attributed quotations',discourse_role=role,composition='composite'))
 if i not in [2,3,5,6,7,11,12,13,14,15]:rec('a'+str(i),'attributions',[i],dict(surface='anonymous analysis',role='anonymous',candidates=[],scope=role,transmission_chain=[]))
attrs=[('school',[0],'תנא דבי רבי ישמעאל','collective',['school of Rabbi Yishmael'],'Question about judicial-burning verse',[]),('yose',[1,2],'רבי יוסי','quoted_authority',['Rabbi Yose'],'Burning singled out as ordinary prohibition',[]),('natan',[1,2],'רבי נתן','quoted_authority',['Rabbi Natan'],'Burning singled out for dividing Sabbath labors',[]),('rava',[3],'רבא','speaker',['Rava'],'Question concerns מושבות',[]),('student',[5,6,7],'תלמיד אחד','transmitter',[],'Competing execution/Sabbath readings and court analogy',['unnamed student','Rabbi Yishmael']),('yishmael',[5,6,7],'רבי ישמעאל','quoted_authority',['Rabbi Yishmael'],'Judicial execution barred on Sabbath',[]),('sheshet',[11],'רב ששת','quoted_authority',['Rav Sheshet'],'Wick cooking and dye cooking',[]),('shimi',[12,13,14,15],'רב שימי בר אשי','speaker',['Rav Shimi bar Ashi'],'A-fortiori reconstruction of the baraita',[])]
for k,inds,surface,role,candidates,scope,chain in attrs:rec(k,'attributions',inds,dict(surface=surface,role=role,candidates=candidates,scope=scope,transmission_chain=chain),u=['Student identity remains unnamed.'] if k=='student' else [])
a=claim('burning_source',[0],'Burning might supply the proposed precedent for a specific exclusion.','hypothetical')
b=q('verse_purpose',[0],'What does לא תבערו אש בכל מושבותיכם teach?')
c=q('already_explained',[1],'Why ask this, given Rabbi Yose’s and Rabbi Natan’s respective explanations?')
d=claim('yose_rule',[1,2],'Burning was singled out to be an ordinary negative prohibition.',holder='Rabbi Yose')
e=claim('natan_rule',[1,2],'Burning was singled out to divide liability for Sabbath labors.',holder='Rabbi Natan')
edge('yose_premise',[1,2],d,c,'support');edge('natan_premise',[1,2],e,c,'support')
f=claim('moshavot_focus',[3],'The tanna’s difficulty concerns the word מושבות, not the entire burning prohibition.',holder='Rava');edge('focus_answer',[3],f,c,'answer')
g=q('why_moshavot',[3,4],'Why specify dwellings for Sabbath, which is a personal obligation?')
h=claim('body_obligation',[4],'Sabbath is a personal obligation, and personal obligations apply both in the Land and outside it.');edge('location_premise',[4],h,g,'support')
j=claim('execution_includes',[5],'The execution command might apply on weekdays and Sabbath, with the Sabbath death-penalty verse restricted to other labors.','hypothetical',holder='Rabbi Yishmael as reported by unnamed student')
k=claim('execution_excludes',[5],'Alternatively the Sabbath prohibition includes judicial execution, and the execution command applies on weekdays alone.','hypothetical',holder='Rabbi Yishmael as reported by unnamed student')
l=q('execution_alternative',[5,6],'Should judicial execution be permitted on Sabbath or excluded from it?')
m=claim('court_analogy',[6,7],'מושבות in the burning verse is compared with מושבות in the judicial-statutes verse, so the burning prohibition applies to the court.',holder='Rabbi Yishmael as reported by unnamed student')
edge('court_answer',[6,7],m,l,'answer');edge('dwellings_answer',[6,7],m,g,'answer');edge('burning_correction',[7],m,j,'correction')
n=claim('natan_identification',[8],'The baraita is proposed to follow Rabbi Natan, implying that without the special verse judicial execution would override the Sabbath prohibition.','hypothetical',cond=['Proposed identification with Rabbi Natan'])
o=claim('yose_identification',[9],'The alternative response identifies the baraita with Rabbi Yose.','hypothetical',cond=['Local proposed attribution, not independently established'])
edge('attribution_correction',[9],o,n,'correction')
pp=claim('ordinary_only',[9],'Even for Rabbi Yose, ordinary-prohibition status concerns burning alone.')
r=claim('wick_cooking',[10],'Judicial burning involves cooking the wick.')
s=claim('cooking_equal',[11],'Cooking a wick is no different from cooking dyes for the relevant cooking classification.',holder='Rav Sheshet')
edge('yose_obj',[9,10],r,o,'objection');edge('limit_yose',[9],pp,o,'qualification');edge('cooking_support',[11],s,r,'support')
t=claim('shimi_reconstruction',[12],'This tanna’s contemplated Sabbath override arises from an a-fortiori argument, not the general positive-command override principle.',holder='Rav Shimi bar Ashi')
edge('override_replaced',[12],t,n,'correction')
v=claim('service_sabbath',[13],'Temple service overrides Sabbath within the argument’s premise.',holder='Rav Shimi bar Ashi')
wq=claim('execution_service',[13],'Judicial execution displaces Temple service, as מעם מזבחי תקחנו למות indicates.',holder='Rav Shimi bar Ashi')
x=claim('execution_kal',[12,13],'If execution displaces service and service displaces Sabbath, execution should all the more displace Sabbath.','hypothetical',holder='Rav Shimi bar Ashi')
edge('kal_premise1',[13],v,x,'support');edge('kal_premise2',[13],wq,x,'support');edge('shimi_explication',[13],x,t,'support')
y=q('or_not',[14],'What does the baraita’s או אינו mean on this a-fortiori interpretation?')
z=claim('corpse_counter',[14],'Burial of an unattended corpse displaces service yet does not displace Sabbath, providing a counterexample to the proposed argument.','asserted',holder='Rav Shimi bar Ashi')
aa=claim('corpse_kal',[14,15],'One might then infer that unattended-corpse burial itself overrides Sabbath, since it displaces the service that overrides Sabbath.','hypothetical',holder='Rav Shimi bar Ashi')
bb=claim('sister_proof',[15],'ולאחותו supplies the basis that unattended-corpse burial takes precedence over service.',holder='Rav Shimi bar Ashi',u=['The brief citation is preserved without silently supplying its full baraita.'])
cc=claim('no_burning',[15],'לא תבערו defeats the proposed Sabbath-override conclusion.',holder='Rav Shimi bar Ashi')
edge('corpse_objection',[14],z,x,'objection');edge('or_not_answer',[14],z,y,'answer');edge('corpse_rejoinder',[14,15],aa,z,'objection');edge('corpse_proof',[15],bb,aa,'support');edge('verse_defeat',[15],cc,aa,'correction')
dd=q('original_or_not',[16],'Under the original positive-command override assumption, what did או אינו mean?')
ee=claim('original_first',[17],'On the original interpretation, judicial execution initially excepts itself from Sabbath because a positive command overrides a negative command.','hypothetical',cond=['Retrospective account of abandoned reading'])
ff=claim('original_doubt',[18],'The reconstructed speaker then doubts whether the ordinary override principle extends to a prohibition with karet.','hypothetical',cond=['Retrospective account'])
gg=claim('original_rejoinder',[18,19],'The reconstructed reply argues that even an ordinary prohibition is more severe than the positive command yet is overridden, so lesser and greater severity might not matter.','hypothetical',cond=['Retrospective rejoinder, defeated by verse'])
hh=claim('original_verse',[19],'לא תבערו explicitly blocks the reconstructed override conclusion.')
edge('original_answer',[17],ee,dd,'answer');edge('original_doubt_edge',[18],ff,ee,'objection');edge('original_rejoinder_edge',[18,19],gg,ff,'answer');edge('original_defeat',[19],hh,gg,'correction')
for i in range(20):
 for layer in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in p['records'] if (layer=='reconciliation' or r['layer']==layer) and any(e['segment_id']==seg[i]['id'] for e in r['evidence'])]
  rationale=roles[i]+'. Read with prior failed sources and continuation through 8a:1. '
  rationale+=('Omission reread keeps anonymous student distinct from Rabbi Yishmael, Rabbi Yose/Natan attribution proposals tentative, and retrospective rejected argument separate from accepted baraita ruling.' if layer=='reconciliation' else ('Actual '+layer+' pass found no separate item.' if not ids else 'Completed '+layer+' pass with exact source.'))
  p['coverage'].append(dict(segment_id=seg[i]['id'],layer=layer,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=rationale))
(out/'proposal007.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('records',len(p['records']))
