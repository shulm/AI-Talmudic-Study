"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shabbat')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='416ad648fd0580e4cde06178b7a21deb50d8197eabd2c50444622a34cd38ab0d';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shabbat','epoch':2}
assert I[99]['ref']=='Shabbat 6a:4' and I[118]['ref']=='Shabbat 6b:7'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='sha.s19r01.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
import copy,importlib.util
D={r['id']:r for r in S['records']}
keys=['thresholdowner','thresholdpoor','nocrossowner','nocrosspoor','threeexempt','thresholdtwo','dooropen','doorclosed','thresholdindependent']
ids={'sha.s2719.'+k for k in keys}
while True:
 n=ids|{r['id'] for r in S['records'] if r['release_state']=='valid' and any(v in ids for v in r['links'])}
 if n==ids:break
 ids=n
mapping={rid:rid+'.s19r01' for rid in ids}
def remap(v):
 if isinstance(v,str):return mapping.get(v,v)
 if isinstance(v,list):return [remap(x) for x in v]
 if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
 return v
alternatives='Either Rav interpretation: alley threshold half roofed/half unroofed with roof toward inside; OR Rav Ashi interpretation: house threshold with two beams each under four, gap under three and door between; alternatives not cumulative'
contexts={k:list(range(161,166)) for k in keys[:4]};contexts['threeexempt']=list(range(161,168));contexts.update({k:list(range(168,173)) for k in ['thresholdtwo','dooropen','doorclosed']});contexts['thresholdindependent']=[173]
for rid in sorted(ids):
 r=remap({k:copy.deepcopy(v) for k,v in D[rid].items() if k not in ['review_state','release_state','ml_eligible','supersedes']});r['supersedes']=rid;k=rid.removeprefix('sha.s2719.').removesuffix('.a').removesuffix('.p')
 if k in contexts:
  extra=ev(contexts[k]);known={x['segment_id'] for x in r['evidence']};r['evidence'] += [x for x in extra if x['segment_id'] not in known]
 if r['layer']=='claims':
  if k in keys[:5]:r['content']['conditions']+=['Threshold is an exempt place lacking four by four, as resolved8b14'];r['content']['scope']+='; full8b10–14 rejects public/private/karmelit interpretations and retains no exchange restriction'
  if k=='threeexempt':r['content']['conditions']+=['Actual intermediate resting occurs here; unlike Rava continuous passage without rest'];r['content']['scope']+=';8b15–9a1 resolves apparent contradiction by resting versus nonresting'
  if k in ['thresholdtwo','dooropen','doorclosed']:r['content']['conditions']+=[alternatives];r['content']['scope']+='; conditional architectural alternatives explained9a2–6, not a general rule for all thresholds'
  if k=='thresholdindependent':r['content']['scope']+=';9a7 links this independent domain to Meir prohibition on shouldering onto a height-ten/width-four column within private domain, decree for a public-domain mound; identity is not unrestricted permission';r['content']['conditions']+=['Independent domain identity does not remove9a7 shouldering prohibition in the stated two-domains-within-one case']
 if r['layer']=='attributions' and k in contexts:r['content']['scope']+='; holder remains Others for baraita, contextual interpretations separately attributed to Rav or Rav Ashi, not merged'
 R.append(r)
bynew={r['id']:r for r in R}
for r in R:
 if r['layer']=='positions':
  claim=bynew[r['content']['claim_id']];r['content']['conditions']=claim['content']['conditions'];r['content']['local_status']+='; bound to explicit continuation qualifications in claim successor'
c={k:mapping['sha.s2719.'+k] for k in keys};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('thresholdkind',161,'What kind of threshold is this?', ['Baraita permits exchange with householder and poor person'])
Q('publichypothesis',162,'If public domain, is taking from the householder not removal from private to public?', ['Hypothetical public-domain threshold'])
Q('privatehypothesis',163,'If private domain, is taking from the poor person not bringing public into private?', ['Hypothetical private-domain threshold'])
Q('karmelithypothesis',164,'If karmelit, how is taking and giving permitted initially, since a prohibition still exists?', ['Hypothetical karmelit threshold'])
C('exemptplace',165,'The threshold is an exempt place, such as one without four by four.','Final resolution of rejected three classifications',cond=['Lacks four by four'])
C('shoulderprivate',165,'Residents of private domain may shoulder onto a place lacking four by four handbreadths.','Rabbi Yohanan reported by Rav Dimi',cond=['Place lacks four by four handbreadths'],holder='רבי יוחנן')
C('shoulderpublic',165,'Residents of public domain may likewise shoulder onto it.','Same teaching, opposite side',cond=['Place lacks four by four handbreadths'],holder='רבי יוחנן')
C('noexchange',165,'They must not exchange through it.','Qualification on both permissions',cond=['Exempt place between domains'],holder='רבי יוחנן')
add('dimireport','attributions',165,dict(surface='כי אתא רב דימי אמר רבי יוחנן',role='transmitter',candidates=['רב דימי'],scope='Reports Yohanan exempt-place permission with no exchange',transmission_chain=['רב דימי','רבי יוחנן']),[c['shoulderprivate'],c['shoulderpublic'],c['noexchange']])
Q('ravacontradiction',[166,167],'Should the all-three exemption refute Rava’s liability ruling?', ['Apparent contrast with continuous transfer through above this exempt place'])
C('ravacontinuous',[166,167],'One carrying an object from the beginning to the end of four cubits in public domain is liable even if it passes above that place.','Rava rule; next contrast states it did not rest',cond=['Four-cubit public-domain transfer','Passes above exempt place','No resting there'],holder='רבא')
C('therenorest',167,'There it did not rest.','First distinction limb, Rava continuous transfer')
C('hererest',167,'Here it rested.','Second distinction limb, baraita relay exemption')
Q('nolehi',169,'Does this apply even without a sidepost, despite Rav’s requirement of another sidepost within the doorway?', ['Others open-door classification','No additional sidepost'])
C('ravlehi',169,'The interior of the doorway needs another sidepost to permit it.','Rav reported by Rav Hama bar Gurya',cond=['Interior of doorway'],holder='רב')
Q('smallstilllehi',170,'If one proposes it lacks four by four, does Rav not require another sidepost even then?', ['Proposed small-threshold answer','Interior doorway lacks four by four'])
C('smallneedslehi',170,'Even when the doorway interior lacks four by four, another sidepost is required.','Rav rule blocks simple smallness answer',cond=['Doorway interior lacks four by four'],holder='רב')
add('hamareport','attributions',[169,170],dict(surface='אמר רב חמא בר גוריא אמר רב',role='transmitter',candidates=['רב חמא בר גוריא'],scope='Reports Rav extra-sidepost rule, distinct from Yehuda report of Rav solution',transmission_chain=['רב חמא בר גוריא','רב']),[c['ravlehi'],c['smallneedslehi']])
C('ravalley',171,'The case is an alley threshold half roofed and half unroofed, with the roof toward the inside.','Rav interpretation reported by Yehuda; alternative to Ashi house construction',holder='רב')
C('ravalleyopen',171,'In that alley case, an open door makes it like the inside.','Rav conditional branch',cond=['Half-roofed alley threshold','Roof inward','Door open'],holder='רב')
C('ravalleyclosed',171,'In that alley case, a shut door makes it like the outside.','Rav opposite branch',cond=['Half-roofed alley threshold','Roof inward','Door shut'],holder='רב')
add('yehudareport','attributions',171,dict(surface='אמר רב יהודה אמר רב',role='transmitter',candidates=['רב יהודה'],scope='Reports Rav alley construction; not Rav Yehuda independent original stance',transmission_chain=['רב יהודה','רב']),[c['ravalley'],c['ravalleyopen'],c['ravalleyclosed']])
C('ashihouse',172,'Rav Ashi interprets a house threshold roofed by two beams, each under four, with a gap under three and a door between.','Alternative construction, not simultaneous conditions added to Rav alley',holder='רב אשי')
C('ashiopen',172,'In that house construction, an open door makes it like the inside.','Ashi branch',cond=['Two beams each under four','Gap under three','Door between','Door open'],holder='רב אשי')
C('ashiclosed',172,'In that house construction, a shut door makes it like the outside.','Ashi opposite branch',cond=['Two beams each under four','Gap under three','Door between','Door shut'],holder='רב אשי')
C('meirshoulder',173,'Where there are two domains which are one, such as a column in private domain ten high and four wide, one may not shoulder onto it.','Rabbi Meir reported by Yitzhak bar Avdimi; distinct from denying private-domain identity',cond=['Column within private domain','Height ten','Width four'],holder='רבי מאיר')
C('publicmound',173,'This is a decree because of a mound in public domain.','Reason for within-private-domain column restriction',holder='רבי מאיר')
add('yitzhakreport','attributions',173,dict(surface='רב יצחק בר אבדימי אומר היה רבי מאיר',role='transmitter',candidates=['רב יצחק בר אבדימי'],scope='Reports Meir shouldering restriction and decree',transmission_chain=['רב יצחק בר אבדימי','רבי מאיר']),[c['meirshoulder'],c['publicmound']])
rels=[(162,'publichypothesis','thresholdkind','objection'),(163,'privatehypothesis','thresholdkind','objection'),(164,'karmelithypothesis','thresholdkind','objection'),(165,'exemptplace','thresholdkind','answer'),([109,165],'exemptplace','thresholdowner','qualification'),([109,165],'exemptplace','thresholdpoor','qualification'),([109,165],'noexchange','nocrossowner','support'),([109,165],'noexchange','nocrosspoor','support'),([166,167],'ravacontinuous','ravacontradiction','support'),(167,'therenorest','ravacontradiction','answer'),(167,'hererest','ravacontradiction','answer'),([109,166,167],'hererest','threeexempt','qualification'),(169,'ravlehi','nolehi','support'),(170,'smallneedslehi','smallstilllehi','support'),(171,'ravalley','nolehi','answer'),(171,'ravalley','smallstilllehi','answer'),(172,'ashihouse','nolehi','answer'),(172,'ashihouse','smallstilllehi','answer'),([110,171],'ravalley','thresholdtwo','qualification'),([110,172],'ashihouse','thresholdtwo','qualification'),([110,171],'ravalleyopen','dooropen','qualification'),([110,171],'ravalleyclosed','doorclosed','qualification'),([110,172],'ashiopen','dooropen','qualification'),([110,172],'ashiclosed','doorclosed','qualification'),([110,173],'meirshoulder','thresholdindependent','qualification'),(173,'publicmound','meirshoulder','support'),([110,173],'thresholdindependent','meirshoulder','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
# Original covered coordinates only; context remains evidence without extraction coverage.
COV=[]
for pc in S['coverage']:
 if any(v in ids for v in pc['record_ids']) or pc['segment_id'] in [I[109]['id'],I[110]['id']]:
  cv=remap({k:copy.deepcopy(v) for k,v in pc.items() if k!='proposal_execution'})
  for r in R:
   if (cv['layer']=='reconciliation' or r['layer']==cv['layer']) and any(e['segment_id']==cv['segment_id'] for e in r['evidence']) and r['id'] not in cv['record_ids']:cv['record_ids'].append(r['id'])
  if cv['record_ids']:cv['extraction_result']='records_found'
  cv['rationale']+=' S19-R01 full8b10–9a7 continuation integrated with conditions, resting distinction, separate Rav/Ashi constructions and Meir shouldering decree. Context-only evidence adds no core coverage.';COV.append(cv)
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shabbat',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails'])
W=H.parents[5];runner=Path('F:/Sefaria_QA/worktrees/bavli-l05-production-20261126/research/bavli_production_v1/runner.py');spec=importlib.util.spec_from_file_location('runner',runner);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);mod.validate_apply(S,P,{v['id']:v for v in I},M)
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shabbat_S19_R01_threshold_correction.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),coverage_updates=len(COV),superseded=len(ids),sha256=hashlib.sha256(b).hexdigest())))
