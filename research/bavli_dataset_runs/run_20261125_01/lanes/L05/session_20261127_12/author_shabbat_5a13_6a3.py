"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shabbat')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='46dd992408c44bbb867794fe78417950200f4407391bb5e3e6cd1961903e22ed';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shabbat','epoch':2}
assert I[79]['ref']=='Shabbat 5a:13' and I[98]['ref']=='Shabbat 6a:3'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='sha.s2712.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('handwater','structure',range(79,90),dict(title='Hand as resting place, moving catchers, rain and floating substances; two unresolved questions',primary=True,boundary='closed',legacy_ids=[]))
s2=add('intent','structure',range(90,93),dict(title='Loaded movement, rest versus adjusting load, original lifting intent and alternate reports',primary=True,boundary='closed',legacy_ids=[]))
s3=add('stoa','structure',range(93,99),dict(title='Shop-to-plaza transfer through stoa: Ben Azzai and sages, initial analogies still challenged in continuation',primary=True,boundary='open_right',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond,status='partial'):
 z[k]=add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status=status));return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
def report(k,ii,chain,targets):add(k,'attributions',ii,dict(surface=' אמר '.join(chain),role='transmitter',candidates=[chain[0]],scope='Explicit report chain; original authority distinct from intermediaries',transmission_chain=chain),targets)
C('handcatch',79,'One who throws an object and it lands in another’s hand is liable.','Rabbi Yohanan’s reported rule',holder='רבי יוחנן',cond=['Thrown object rests in another’s hand'])
Q('handnovel',79,'What does this teach—that a person’s hand counts as four by four?', ['Reported thrown-object ruling'])
C('handfour',79,'A person’s hand counts as four by four.','Premise invoked in novelty question')
Q('alreadyhand',79,'Did Rabbi Yohanan not already say this once?', ['Apparent repetition of hand-as-four-by-four teaching'])
C('selfimportance',79,'One might limit that rule to a case where he himself treated his own hand as significant.','Proposed limiting assumption rejected by new teaching',mode='rejected',cond=['He himself gives significance to his hand'])
C('noimportance',79,'The hand still counts even where he did not himself give his hand significance.','Novelty of received object in another’s hand; source pronouns retained',holder='רבי יוחנן',cond=['No such self-designation of hand significance'])
report('chain79',79,['רבי אבין','רבי אילעאי','רבי יוחנן'],[c['handcatch'],c['noimportance']])
C('stayscatch',80,'If the recipient remains in place and receives it, the thrower is liable.','Rabbi Yohanan’s rule; recipient’s movement distinguished',holder='רבי יוחנן',cond=['Receiver remains in original place'])
C('movescatch',80,'If the recipient moves from his place and receives it, the thrower is exempt.','Rabbi Yohanan’s rule',holder='רבי יוחנן',cond=['Receiver leaves original place before catching'])
report('chain80',80,['רבי אבין','רבי אילעאי','רבי יוחנן'],[c['stayscatch'],c['movescatch']])
C('aherimstay',80,'If he remains in his place and catches, there is liability.','Corroborating baraita attributed to Aherim',holder='אחרים',cond=['Recipient remains in place'])
C('aherimmove',80,'If he moves from his place and catches, there is exemption.','Corroborating baraita attributed to Aherim',holder='אחרים',cond=['Recipient changes place'])
Q('selfcatch',81,'What if one throws an object, moves from his place, and returns to catch it himself?', ['Same person throws and catches after movement'],status='unreviewed_alternatives')
add('yohananquestion','attributions',81,dict(surface='בעי רבי יוחנן',role='speaker',candidates=['רבי יוחנן'],scope='Asks unresolved self-throw-and-catch question',transmission_chain=[]),[z['selfcatch']])
Q('whatissue',82,'What is the issue in his question?', ['Rabbi Yohanan self-catching case'])
C('twoforces',82,'The issue is two forces in one person.','Rav Adda bar Ahava’s explanation of question',holder='רב אדא בר אהבה')
Q('oneortwo',82,'Are two forces in one person treated as one person, making him liable, or as two people, making him exempt?', ['One thrower moves and catches his own object'],status='unreviewed_alternatives')
C('oneforceoption',82,'If treated as one person, he would be liable.','Unresolved first alternative, not an adopted ruling',mode='unresolved',cond=['Two forces treated as one actor'])
C('twoforceoption',82,'If treated as two people, he would be exempt.','Unresolved second alternative',mode='unresolved',cond=['Two forces treated as two actors'])
C('selfteiku',82,'The question remains unresolved: תיקו.','Explicit outcome, no chosen side')
C('raininitial',83,'One who inserts his hand into another’s courtyard, receives rainwater, and takes it out is liable.','Initial Rabbi Yohanan report wording, amended from receiving to collecting and location clarified below',holder='רבי יוחנן',mode='challenged',cond=['Hand into another courtyard','Receives rainwater','Takes it out'])
report('chain83',83,['רבי אבין','רבי יוחנן'],[c['raininitial']])
Q('heavenfriend',83,'What difference is there between a friend loading his hand and heaven loading it?', ['Passive receipt of rainwater','He performs no lifting'])
add('zeiraspeaker','attributions',83,dict(surface='מתקיף לה רבי זירא',role='speaker',candidates=['רבי זירא'],scope='Objection to passive rain receipt as lifting',transmission_chain=[]),[z['heavenfriend']])
C('nolifting',83,'He did not perform a lifting.','Rabbi Zeira’s objection to passive-receipt wording',holder='רבי זירא')
C('collectinstead',83,'Do not read “received”; read “collected” instead.','Explicit wording correction requires active collection',mode='reconciled')
Q('fourplace',83,'But is lifting from a four-by-four place not required, and absent here?', ['Revised collected-water wording'])
C('wallcollection',84,'The case is collection from the wall.','Rabbi Hiyya son of Rav Huna’s proposed explanation, later replaced by pit-water case',holder='רבי חייא בריה דרב הונא',mode='rejected')
Q('wallnotrest',84,'Even on the wall, has the water not failed to come to rest?', ['Proposed wall collection'])
C('slopingwater',84,'The proposed answer uses a sloping wall, as in Rava’s explanation elsewhere.','Temporary analogy later rejected because water does not rest like scroll',mode='rejected')
Q('whereRava',84,'Where was Rava’s explanation stated?', ['Invoked sloping-wall analogy'])
C('thresholdscroll',85,'One reading a scroll on the threshold whose scroll rolls from his hand may roll it back to himself.','First case of quoted Mishnah retained',holder='Anonymous scroll Mishnah',cond=['Reading on threshold','Scroll rolls from hand'])
C('roofabove',85,'If reading on the roof, he may roll it back before it reaches ten handbreadths.','Quoted roof case, preserving threshold distinction',holder='Anonymous scroll Mishnah',cond=['Reading on roof','Rolled scroll not yet reached ten handbreadths'])
C('roofbelow',85,'Once it reaches ten handbreadths, he turns it onto the writing side (הופכו על הכתב).','Quoted הוראה הופכו על הכתב; exact original evidence retained',holder='Anonymous scroll Mishnah',cond=['Reading on roof','Scroll reaches ten handbreadths'])
Q('whyturn',85,'Why turn it onto the writing—has it not failed to come to rest?', ['Roof-scroll ten-handbreadth case'])
C('slopingscroll',86,'It is a sloping wall.','Rava’s explanation of the scroll case, not final water explanation',holder='רבא')
Q('waterrest',86,'Even if Rava says this for a scroll that can rest there, can water rest there?', ['Attempted analogy from scroll on sloping wall to water'])
C('scrollrestwaternot',86,'The scroll can rest on that surface, whereas the water analogy fails.','Distinction rejects water-wall explanation')
C('pitwater',87,'Instead the case is collection from a pit.','Rava’s replacement interpretation of the rainwater report',holder='רבא')
Q('pitobvious',87,'Is a pit case not obvious?', ['Water collected from pit'])
C('waternotrestassumption',87,'One might think water upon water is not considered resting.','Rejected limiting assumption explaining novelty',mode='rejected')
C('wateronwater',87,'Water upon water is considered resting.','Novelty of pit interpretation',holder='רבא')
C('waterrests',88,'Water upon water is its normal rest.','Repeated Rava rule supporting consistency, separate occurrence',holder='רבא')
C('nutnotrest',88,'A nut upon water is not at rest.','Rava’s contrasting rule',holder='רבא')
Q('nutvessel',88,'For a nut in a vessel floating on water, do we follow the nut, which rests, or the vessel, which moves and does not rest?', ['Nut in vessel','Vessel floating on water'],status='unreviewed_alternatives')
add('ravaquestion','attributions',88,dict(surface='בעי רבא',role='speaker',candidates=['רבא'],scope='Unresolved floating-vessel/nut question',transmission_chain=[]),[z['nutvessel']])
C('nutperspective',88,'Following the nut treats it as resting.','Unresolved alternative',mode='unresolved',cond=['Consider nut relative to vessel'])
C('vesselperspective',88,'Following the vessel treats it as not resting because it moves.','Unresolved alternative',mode='unresolved',cond=['Consider moving floating vessel'])
C('nutteiku',88,'The nut-in-floating-vessel question remains unresolved: תיקו.','Explicit unresolved outcome')
C('oilwine',89,'Oil floating on wine is a dispute between Rabbi Yohanan ben Nuri and the sages.','Connection/rest issue referred to purity Mishnah; no forced final Shabbat ruling')
C('oilonly',89,'If a tevul yom touches the oil floating on wine, only the oil is invalidated.','First/sages view in quoted Mishnah',holder='רבנן',cond=['Oil floating on wine','Tevul yom touches oil'])
C('bothconnected',89,'The oil and wine are connected to one another.','Rabbi Yohanan ben Nuri’s opposing purity position',holder='רבי יוחנן בן נורי',cond=['Oil floating on wine','Tevul yom touching oil'])
C('loadeduntilstop',90,'One loaded with foods and drinks who enters and exits all day is not liable until he stops.','Rabbi Yohanan’s reported necessary stopping condition, refined by rest purpose next; not immediate liability just for standing',holder='רבי יוחנן',cond=['Loaded with foods and drinks','Continuous entry and exit without qualifying rest'])
report('chain90',90,['רבי אבין','רבי אילעאי','רבי יוחנן'],[c['loadeduntilstop']])
C('restpurpose',91,'The stopping must be to rest.','Abaye qualifies stop requirement, distinguishing load adjustment',holder='אביי',cond=['Stop to rest, not merely adjust load'])
Q('restsource',91,'From where is the rest-purpose qualification known?', ['Abaye distinction'])
for k,within,reason,outcome in [('insideRest',True,'rest','exempt'),('insideAdjust',True,'adjust the load','liable'),('outsideRest',False,'rest','liable'),('outsideAdjust',False,'adjust the load','exempt')]:
 C(k,91,'If he stops '+('within' if within else 'beyond')+' four cubits to '+reason+', he is '+outcome+'.','Quoted comparison supporting Abaye; outcome of the carrying course, not liability for an intermediate sub-four-cubit stop alone',holder='Anonymous quoted rule',cond=[('Within' if within else 'Beyond')+' four cubits','Stops to '+reason])
Q('intentnovel',92,'What does this teach—that the original lifting was not initially for this purpose?', ['Loaded-entry/exit rule','Lifting intention at initial stage'])
Q('alreadyintent',92,'Did Rabbi Yohanan not already say this once?', ['Apparent duplication of original-lifting-purpose rule'])
C('cornerchange',92,'One who moves objects from corner to corner, then changes his mind and takes them out, is exempt.','Rabbi Yohanan’s other reported formulation',holder='רבי יוחנן',cond=['Initially moves corner to corner','Subsequently decides to take outside'])
C('nopurpose',92,'The original lifting was not for that purpose.','Reason for exemption in changed-intention case',holder='רבי יוחנן')
report('chain92',92,['רב ספרא','רבי אמי','רבי יוחנן'],[c['cornerchange'],c['nopurpose']])
C('tworeporters',92,'Different amoraim transmitted the teaching in different wordings.','Resolution of apparent duplication; not two independent rulings or new contradiction')
C('shopliable',93,'One who takes an object from a shop to a plaza through a stoa is liable.','First tanna’s baraita ruling',holder='רבנן',cond=['From shop to plaza','Through stoa'])
C('shopbenazzai',93,'Ben Azzai exempts that transfer.','Walking-transfer position; later6a8 excludes throwing/handing from exemption',holder='בן עזאי',cond=['Carrying by walking from shop to plaza through stoa'])
C('walkingstanding',94,'Ben Azzai considers walking like standing.','Explanation for intermediate stoa interruption',holder='בן עזאי')
C('walkingnotstanding',94,'The sages consider walking unlike standing.','Conceded premise does not itself establish their liability analogy',holder='רבנן')
Q('analogywhere',94,'Where do we find a comparable case of liability, even granting walking is not standing?', ['Sages shop-through-stoa liability'])
C('publicanalogy',[95,96],'It is like carrying an object in a public domain: while carrying he is exempt, but when he places it down he is liable.','Rabbi Yohanan’s initial analogy reported through Rav Safra and Rabbi Ammi; challenged next',holder='רבי יוחנן',mode='rejected')
report('chain95',[95,96],['רב ספרא','רבי אמי','רבי יוחנן'],[c['publicanalogy']])
Q('firstcomparable',97,'Are those cases comparable?', ['Public-domain-carrying analogy for route through stoa'])
C('everywhereliable',97,'In the public-domain case, wherever he sets it down is a place of liability.','Distinguishing domain premise in objection')
C('stoaexempt',97,'If he sets it down in the stoa, it is a place of exemption.','Contrasting premise defeats first analogy',cond=['Sets down in stoa'])
C('fouranalogy',98,'Instead it is like carrying from the beginning to the end of four cubits: placing within four is exempt, but placing at the end of four is liable.','Second analogy; rejected in context6a4 as person-relative exemption versus stoa exemption for everyone',mode='rejected',cond=['Before end of four cubits versus completed four cubits'])
Q('publiccase',[95,96],'In public-domain carrying, is it not true that he is exempt while carrying but liable when he sets it down?', ['First proposed analogy','Carrying course fulfilling required transfer distance'])
Q('fourcase',98,'In a four-cubit carrying course, is it not true that setting down within four is exempt but setting down at its end is liable?', ['Second proposed analogy','Its comparability is rejected next at6a4'])
rels=[(79,'noimportance','handnovel','answer'),(79,'noimportance','alreadyhand','answer'),(79,'noimportance','selfimportance','correction'),(80,'aherimstay','stayscatch','support'),(80,'aherimmove','movescatch','support'),(82,'twoforces','whatissue','answer'),(82,'twoforces','selfcatch','qualification'),(82,'selfteiku','selfcatch','unresolved_outcome'),(82,'selfteiku','oneortwo','unresolved_outcome'),(83,'nolifting','raininitial','objection'),(83,'heavenfriend','raininitial','objection'),(83,'collectinstead','raininitial','correction'),(83,'fourplace','collectinstead','objection'),(84,'wallcollection','fourplace','answer'),(84,'slopingwater','wallnotrest','answer'),(86,'slopingscroll','whyturn','answer'),(86,'slopingscroll','whereRava','answer'),(86,'waterrest','slopingwater','objection'),(86,'scrollrestwaternot','slopingwater','objection'),(87,'pitwater','wallcollection','correction'),(87,'pitwater','fourplace','answer'),(87,'wateronwater','pitobvious','answer'),(87,'wateronwater','waternotrestassumption','correction'),(88,'waterrests','wateronwater','support'),(88,'nutnotrest','waterrests','distinction'),(88,'nutteiku','nutvessel','unresolved_outcome'),(89,'oilonly','oilwine','support'),(89,'bothconnected','oilwine','support'),(91,'restpurpose','loadeduntilstop','qualification'),(91,'insideRest','restsource','answer'),(91,'insideAdjust','restsource','answer'),(91,'outsideRest','restsource','answer'),(91,'outsideAdjust','restsource','answer'),(92,'nopurpose','cornerchange','support'),(92,'tworeporters','alreadyintent','answer'),(92,'nopurpose','intentnovel','answer'),(94,'walkingstanding','shopbenazzai','support'),(96,'publicanalogy','analogywhere','answer'),(97,'firstcomparable','publicanalogy','objection'),(97,'stoaexempt','publicanalogy','objection'),(97,'everywhereliable','publicanalogy','objection'),(98,'fouranalogy','publicanalogy','correction'),(98,'fouranalogy','analogywhere','answer')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={79:'Complete Avin–Ilai–Yohanan chain; throwing into other hand, two novelty/repetition questions and rejected self-designation limitation.',80:'Receiver stays versus changes place; liability concerns thrower. Aherim corroboration is distinct quoted occurrence.',81:'Yohanan self-throw/move/catch question, not merged with other-person catching; unresolved outcome next.',82:'What-issue question, Rav Adda bar Ahava two-forces explanation, both one-actor/two-actor alternatives and separate תיקו record.',83:'Avin–Yohanan report, Rabbi Zeira agency challenge, no lifting, explicit received-to-collected correction, four-by-four-place question.',84:'Hiyya son of Rav Huna wall answer, not-rested challenge, provisional slope reply and where-Rava question; wall answer later rejected.',85:'Full scroll threshold and roof cases before/after ten handbreadths, writing-side instruction and no-rest question.',86:'Rava sloping wall belongs to scroll; water-rest question rejects analogy.',87:'Rava pit correction, obviousness question and rejected water-on-water-not-resting assumption; positive novelty explicit.',88:'Water-on-water versus nut-on-water; nut-in-floating-vessel question with both viewpoints and distinct תיקו preserved.',89:'Oil/wine dispute via tevul-yom Mishnah; sages only-oil invalidation versus Yohanan ben Nuri connection, no unqualified final ruling forced.',90:'Loaded foods/drinks continuous movement no liability until qualifying stop; necessary condition not instantaneous liability just for stopping.',91:'Abaye rest-purpose restriction; all four within/beyond-four and rest/adjustment combinations preserved as carrying-course outcomes.',92:'Two novelty/repetition questions; Rav Safra–Ammi–Yohanan changed-intent report and cause; alternate transmitting amoraim resolve duplicate wording.',93:'Sages liability and Ben Azzai exemption on shop/plaza through stoa walking transfer;6a8 later exempts only walking carry-in/out, not throw/hand-over.',94:'Ben Azzai walking-as-standing versus sages opposite premise; further analogy question retained.',95:'Transmission-chain fragment joined to6a1; no stand-alone ruling inferred from names.',96:'Full public-domain analogy and embedded question; subsequent objection marks analogy rejected.',97:'Comparability question distinguishes any public-domain placement liability from stoa exemption.',98:'Second within/end-four analogy and embedded question, explicitly rejected by next6a4. Read6a4–8: person-relative versus universal exemption, replacement via public-domain sides, Pap(a)/Aha distinction with barriers, and Ben Azzai throwing/handing qualifications. No context coverage credit.'}
for i in range(79,99):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous argument and separately attributed named reports',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective Gemara discussion',role='anonymous',candidates=[],scope='Framing and inference only; named authorities and report chains are separate',transmission_chain=[]))
COV=[]
for i in range(79,99):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shabbat',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s3])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shabbat_5a13_6a3_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
