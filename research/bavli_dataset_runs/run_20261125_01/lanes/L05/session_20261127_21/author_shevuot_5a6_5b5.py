"""Direct source annotations for the explicitly bounded range: 20 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shevuot')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='0315c06d454f7a05a4be1535e7e6d17a357cac91fa000e933562c4d770b00593';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shevuot','epoch':2}
assert I[77]['ref']=='Shevuot 5a:6' and I[96]['ref']=='Shevuot 5b:5'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='she.s2721.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('knowledge','structure',range(77,85),dict(title='Two awarenesses with concealment: Akiva and Rabbi derivations, rejected grammar and school knowledge',primary=True,boundary='closed',legacy_ids=[]))
s2=add('shabbatcount','structure',range(85,97),dict(title='Two-that-are-four Shabbat count, rejected avot explanation, liability categories and terminology alternatives',primary=True,boundary='closed',legacy_ids=[]))
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('awarenesssource',77,'From where is liability only with knowledge initially and at the end, and concealment between them?', ['Impurity liability case','Two-awareness condition'])
C('akivacondition',77,'Liability requires initial knowledge, final knowledge and concealment between.','Rabbi Akiva baraita formulation; three elements conjunctive',cond=['Initial knowledge','Concealment between','Final knowledge'],holder='רבי עקיבא')
C('akivadouble',77,'The two occurrences of ונעלם provide the derivation.','Rabbi Akiva textual basis',holder='רבי עקיבא')
C('rabbinoneed',78,'Rabbi says that derivation is not needed.','Opposes need for Akiva double-ונעלם use, not denial of two-awareness requirement',holder='רבי')
C('concealedknowledge',78,'ונעלם implies that he knew.','Rabbi first awareness derivation; precise type explained below by Abaye',holder='רבי')
C('finalknowledge',78,'והוא ידע supplies the other awareness; there are thus two awarenesses.','Rabbi second textual component',holder='רבי')
Q('extraunelam',78,'If so, what does the additional ונעלם teach?', ['Rabbi already derived two awarenesses'])
C('concealimpurity',78,'It establishes liability for concealment of impurity.','First covered concealment according to Rabbi',cond=['Concealment of impurity'],holder='רבי')
C('concealtemple',78,'It also establishes liability for concealment of the Temple.','Second branch, not simultaneous concealment requirement',cond=['Concealment of Temple'],holder='רבי')
Q('grammar',79,'How does ונעלם imply prior knowledge?', ['Rabbi stated derivation'])
C('ravawording',79,'Because it does not say והיא עלומה ממנו.','Rava initial grammatical explanation, challenged by Abaye then replaced',holder='רבא',mode='challenged')
Q('sotahknowledge',80,'If so, does ונעלם מעיני אישה imply the husband knew previously?', ['Rava grammatical rule applied to suspected-adultery passage'])
Q('waterstest',80,'If he knew, would the waters test her?', ['Husband had prior knowledge','Challenge to proposed inference'])
C('innocenthusband',81,'When the husband is free of sin, the waters test his wife.','Quoted baraita condition from ונקה האיש מעון',cond=['Husband free of sin'])
C('guiltyhusband',81,'When the husband is not free of sin, the waters do not test his wife.','Negative complementary condition',cond=['Husband not free of sin'])
add('abayeobject','attributions',[80,81],dict(surface='א״ל אביי אלא מעתה',role='speaker',candidates=['אביי'],scope='Sotah objection to Rava explanation with quoted baraita support',transmission_chain=[]),[z['sotahknowledge'],z['waterstest']])
Q('torahknowledge',82,'Does ונעלמה מעיני כל חי imply someone had known Torah’s full worth, despite לא ידע אנוש ערכה?', ['Further application of proposed grammatical inference to Job passage'])
C('unknownworth',82,'לא ידע אנוש ערכה states that a human did not know its worth.','Quoted Job28:13 countertext, not denial that anyone learns any Torah')
C('schoolknowledge',83,'Rabbi considers knowledge acquired in one’s teacher’s school to count as knowledge.','Abaye replacement explanation; not mere repetition of rejected Rava grammar',holder='רבי')
add('abayeinterpret','attributions',83,dict(surface='אלא אמר אביי קסבר רבי',role='speaker',candidates=['אביי'],scope='Abaye attributes school-knowledge stance to Rabbi; interpreter and holder distinct',transmission_chain=[]),[c['schoolknowledge']])
Q('noschool',84,'For the case with no initial knowledge but final knowledge, can there be someone lacking school knowledge?', ['Rav Pappa asks Abaye','School knowledge counted as initial awareness'])
C('captivechild',84,'Yes: a child captured among non-Jews provides such a case.','Abaye example of absent school knowledge, retains final-awareness clause being explained',cond=['Child captured among non-Jews','Lacks school knowledge'],holder='אביי')
add('pappaquestion','attributions',84,dict(surface='א״ל רב פפא לאביי',role='speaker',candidates=['רב פפא'],scope='Questions existence of no-initial-knowledge case',transmission_chain=[]),[z['noschool']])
C('heretwofour',85,'Here the Mishnah says Shabbat transfers are two that are four.','Shevuot wording')
C('theretwosides',85,'There it says two that are four inside, and two that are four outside.','Quoted Shabbat Mishnah wording, separate side counts')
Q('countdifference',85,'Why does this Mishnah state only two that are four, whereas the Shabbat Mishnah gives inside and outside counts?', ['Different formulations of same Shabbat topic'])
C('initialthere',86,'The initial explanation says that where Shabbat is the primary subject, both primary and derivative labors are taught.','Initial anonymous proposal, fails count objection below',mode='challenged')
C('initialhere',86,'Here, where Shabbat is not the main subject, primary labors are taught but derivatives are not.','Negative derivative inclusion in initial explanation',mode='challenged')
Q('whichprimary',87,'What are the primary labors here?', ['Initial avot-only explanation'])
C('primaryout',87,'Taking out would be the primary labors meant.','Intermediate identification in objection, not final count solution')
Q('onlytwo',87,'But taking-out cases are only two?', ['Claim that four cases here are primary taking out'])
C('liabilityexemptionproposal',88,'One might propose that some are liable and some exempt.','Attempted rescue of initial count, rejected by parallel to lesion appearances',mode='hypothetical')
Q('lesionparallel',88,'But is the count not taught parallel to lesion appearances, all of which entail liability?', ['Proposed mix of liable/exempt cases in this Mishnah'])
C('lesionsall',88,'All the lesion-appearance cases in that comparison entail liability.','Comparison premise, not an assertion all dermatological conditions incur liability')
C('hereall',88,'So all the counted cases here must likewise entail liability.','Count restriction rejects mixed exemption rescue')
C('pappathere',89,'Where Shabbat is the main subject, both liable and exempt cases are taught.','Rav Pappa replacement account of expanded Shabbat Mishnah',holder='רב פפא')
C('pappahere',89,'Here liable cases are taught, but exempt cases are not.','Rav Pappa account of compact Shevuot count',holder='רב פפא')
Q('whichliable',90,'What are the liable cases—taking out?', ['Rav Pappa liable-only explanation'])
Q('liableonlytwo',90,'But taking-out cases are only two?', ['Liable-only count still needs four'])
C('twoout',90,'There are two taking-out cases.','First half of final four-case account')
C('twoin',90,'There are also two bringing-in cases.','Second half, not derivative exclusion of initial explanation')
Q('outword',91,'But the Mishnah says יציאות?', ['Final count includes bringing in'])
C('ashiterminology',[91,92],'The tanna also calls bringing in taking out.','Rav Ashi terminology answer, demonstrated by next quotation',holder='רב אשי')
Q('termproof',[91,92],'From what can this terminology be shown?', ['Rav Ashi bringing-in-as-taking-out explanation'])
C('domaintransfer',92,'The quoted Mishnah says one who takes from domain to domain is liable.','Quoted general wording')
Q('includesin',92,'Does it not include bringing in, while calling it taking out?', ['From-domain-to-domain wording'])
Q('maybeoutonly',93,'Perhaps it means only private-to-public taking out?', ['Proposed restriction of the prooftext'])
Q('whyunspecified',93,'If so, why not state private to public; why say from domain to domain?', ['Alternative restrictive reading'])
C('includesreverse',93,'The general formulation includes even public to private.','Reply rejects taking-out-only reading')
Q('termreason',94,'Why is this called taking out?', ['Bringing in included by wording'])
C('alluproot',94,'The tanna calls every removal of an object from its place taking out.','General semantic explanation in Mishnah terminology, not claim every such movement is liable')
C('ravinasupport',95,'Our Mishnah also supports it: after the inside/outside taking-out counts it explains bringing in.','Ravina additional proof with שמע מינה',holder='רבינא')
C('ravadomains',96,'Rava says the Mishnah is counting domains.','Alternative account to operation-terminology explanation',holder='רבא')
C('twodomains',96,'The Shabbat domains being counted are two.','Rava reading of רשויות שבת שתים; no invented new detail of four cases beyond line',holder='רבא')
rels=[(77,'akivadouble','awarenesssource','answer'),(77,'akivadouble','akivacondition','support'),(78,'rabbinoneed','akivadouble','objection'),(78,'concealedknowledge','akivacondition','support'),(78,'finalknowledge','akivacondition','support'),(78,'concealimpurity','extraunelam','answer'),(78,'concealtemple','extraunelam','answer'),(79,'ravawording','grammar','answer'),(80,'sotahknowledge','ravawording','objection'),([80,81],'guiltyhusband','waterstest','support'),(82,'torahknowledge','ravawording','objection'),(82,'unknownworth','torahknowledge','support'),(83,'schoolknowledge','ravawording','correction'),(83,'schoolknowledge','grammar','answer'),(84,'captivechild','noschool','answer'),(86,'initialthere','countdifference','answer'),(86,'initialhere','countdifference','answer'),(87,'primaryout','whichprimary','answer'),(87,'onlytwo','initialhere','objection'),(88,'lesionparallel','liabilityexemptionproposal','objection'),(88,'lesionsall','hereall','analogy'),(89,'pappathere','initialthere','correction'),(89,'pappahere','initialhere','correction'),(89,'pappahere','countdifference','answer'),(90,'twoout','whichliable','answer'),(90,'twoin','liableonlytwo','answer'),(91,'outword','twoin','objection'),([91,92],'ashiterminology','outword','answer'),(92,'domaintransfer','termproof','support'),(92,'includesin','ashiterminology','support'),(93,'maybeoutonly','domaintransfer','objection'),(93,'whyunspecified','maybeoutonly','objection'),(93,'includesreverse','maybeoutonly','answer'),(94,'alluproot','termreason','answer'),(94,'alluproot','ashiterminology','support'),(95,'ravinasupport','ashiterminology','support'),(96,'ravadomains','outword','answer'),(96,'twodomains','ravadomains','support')]
for n,(ii,a,b,r) in enumerate(rels):E(str(n),ii,a,b,r)
notes={77:'Actual מנין question, Akiva conjunctive initial/final knowledge plus intervening concealment and doubleונעלם derivation. Separate renewed occurrence, not replacing prior compiler-role correction.',78:'Rabbi says no need for Akiva derivation; two versecomponents derive knowledge, explicit additionalונעלם question, concealment of impurity OR Temple branches. Not absence of knowledge requirement.',79:'How-does-it-imply question; Rava grammar explanation provisional and challenged, never final personal Rabbi teaching.',80:'Abaye sotah prior-awareness implication and would-waters-test questions separately conditional; not a final husband-liability ruling from hypothetical.',81:'Baraita clean-husband waterstest and notclean no-test branches explicit, supports preceding question.',82:'Second grammatical objection Torah hiddenness versus nohuman-knows-worth, not denial allTorahknowledge.',83:'Abaye replaces explanation with Rabbi schoolknowledgecounts; interpreter and position-holder distinct.',84:'Pappa existence question noinitial-but-finalknowledge versus schoolknowledge; Abaye yes capturedchildamongnonJews example preserves condition.',85:'This versus ShabbatMishnah count formulations and explicit why-difference question.',86:'Initial main-topic avot/toladot versus hereavotonly theory provisional, rejectednext.',87:'Whichavot question, takingout identification and onlytwo count objection.',88:'Mixed-liable/exempt rescue hypothetical, explicit lesion-parallel challenge, allcasesliable restriction.',89:'RavPappa corrects to there liable+exempt versus here liableonly; does not simply revive rejected derivatives explanation.',90:'Whichliable question and onlytwo objection separately represented; twoout+twoin final fouraccount.',91:'Butיציאות wording objection, Ashi terms bringingin takingout; ממאי proofquestion spans5b1.',92:'Domain-to-domain Mishnah and explicit includes-bringing-in question; full priorAshi sentence retained.',93:'Maybeprivate-to-public objection, why-not-specific wording counterquestion, public-to-private inclusion answer.',94:'Why-term question, alluprooting calledtakingout semantic answer not blanket liabilityforallmovement.',95:'Ravina inside/outsidecount plus explanationofbringingin proof, שמע מינה; quotedproof not inventing new four detailedcases.',96:'Rava domainscount alternative and two-domainreading; not merged with Ashi explanation.5b6–6b2 nextlesions unit read for boundary, not source qualification of this Shabbatcount. No unrelated later lesions proofs imported as accepted count revisions.'}
for i in range(77,97):
 add('u'+str(i),'utterances',i,dict(textual_voice='Baraita, named interpretations and anonymous count arguments separated',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous connective framing',role='anonymous',candidates=[],scope='Framing only, not compiler endorsement of all quoted authorities',transmission_chain=[]))
COV=[]
for i in range(77,97):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No distinct record found in this layer.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shevuot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails'])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shevuot_5a6_5b5_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
