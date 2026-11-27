"""Direct source annotations for the explicitly bounded range: 21 original segments."""
import json,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent;J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L05/bavli_shevuot')
M=json.loads((J/'JOB.json').read_bytes());I=json.loads((J/'source_inventory.json').read_bytes())
old='d1b09a32eb74e36f033ec52491cfb4279ef68933f33b8a3030c34956a8d72250';S=json.loads((J/'snapshots'/f'{old}.json').read_bytes());R=[]
assert json.loads((J/'OWNER.json').read_bytes())=={'owner':'L05/shevuot','epoch':2}
assert I[29]['ref']=='Shevuot 3a:10' and I[48]['ref']=='Shevuot 4a:3'
assert json.loads((J/'CURRENT.json').read_bytes())['snapshot_sha256']==old
def ev(ii):return [dict(segment_id=I[i]['id'],start_char=0,end_char=len(I[i]['text']),quote=I[i]['text']) for i in ii]
def add(k,l,ii,c,links=(),unc=(),origin='source_paraphrase'):
 if isinstance(ii,int):ii=[ii]
 rid='she.s2707.'+k;R.append(dict(id=rid,layer=l,evidence=ev(ii),content=c,origin=origin,uncertainty=list(unc),links=list(links)));return rid
def cl(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):
 cid=add(k,'claims',ii,dict(proposition=p,conditions=list(cond),scope=scope,assertion_mode=mode),unc=unc)
 if holder:
  add(k+'.a','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope=scope,transmission_chain=[]),[cid],unc=unc)
  add(k+'.p','positions',ii,dict(holder_candidates=[holder],claim_id=cid,question_id=None,conditions=list(cond),local_status=mode+'; '+scope),[cid],unc=unc)
 return cid
def q(k,ii,p,cond):return add('q.'+k,'questions',ii,dict(formulation=p,question_origin='explicit',conditions=cond,answer_set_status='partial'))
def e(k,ii,a,b,rel):return add('e.'+k,'edges',ii,dict(source_id=a,target_id=b,relation=rel,explicitness='source_explicit'),[a,b])
s1=add('identity','structure',range(29,49),dict(title='Initial Mishnah-author proposals and lashes-only explanation; Rabbi Yohanan’s anonymous-Mishnah sources and unresolved preference challenge',primary=True,boundary='open_right',legacy_ids=[]))
e('continuation',29,'she.s2706.classes',s1,'continuation')
c={};z={}
def C(k,ii,p,scope,cond=(),holder=None,mode='asserted',unc=()):c[k]=cl(k,ii,p,scope,cond,holder,mode,unc);return c[k]
def Q(k,ii,p,cond):z[k]=q(k,ii,p,cond);return z[k]
def E(k,ii,a,b,rel):return e(k,ii,c.get(a,z.get(a,a)),c.get(b,z.get(b,b)),rel)
Q('who',29,'Whose view is the Mishnah?', ['Opening two-that-are-four classifications'])
C('neither',29,'Initially the Mishnah appears to fit neither Rabbi Yishmael nor Rabbi Akiva.','Opening difficulty, not final attribution',mode='challenged')
C('yishmaelfuture',29,'Rabbi Yishmael imposes oath liability only for the future.','Quoted limit; subsequent3b2 distinguishes sacrificial liability from lashes',holder='רבי ישמעאל',cond=['Sacrificial liability, clarified below','Future-directed oath'])
C('akivaimpurity',29,'Rabbi Akiva imposes liability for unawareness of impurity.','Quoted impurity-position limit',holder='רבי עקיבא',cond=['העלם טומאה'])
C('akivatemple',29,'Rabbi Akiva does not impose liability for unawareness of the Temple.','Negative limb of quoted impurity position',holder='רבי עקיבא',cond=['העלם מקדש'])
C('initialyishmael',30,'One proposed answer identifies the Mishnah with Rabbi Yishmael, with some listed cases liable and others exempt.','First alternative; exemption interpretation rejected next',mode='rejected')
C('initialakiva',30,'Alternatively the Mishnah is identified with Rabbi Akiva, with some listed cases liable and others exempt.','Second alternative; exemption interpretation rejected next',mode='rejected')
Q('exempt',[31,32],'Exempt? Does the Mishnah not present these like the appearances of lesions, where all are liable?', ['Proposed liable/exempt mixture','Split question לפטור / הא דומיא across folio'])
C('lesionsliable',32,'All the appearances in the comparison are liable.','Premise against interpreting expanded categories as exemptions')
C('allliable',32,'The parallel formulation likewise requires all the listed categories here to be liable.','Objection to both exemption answers, not yet identification of liability type')
C('yishmaellashes',33,'A renewed answer identifies the Mishnah with Rabbi Yishmael and reads it in terms of lashes.','Interim explanation developed here but abandoned by4a10–11; not final Mishnah attribution',mode='rejected')
C('pastnocorban',33,'Rabbi Yishmael’s refusal to impose past-directed oath liability concerns a sacrifice.','Scope qualification of earlier future-only report',holder='רבי ישמעאל',cond=['Past-directed oath','Sacrifice'])
C('pastlashes',33,'Rabbi Yishmael does impose lashes for past-directed oaths.','Distinction used in interim reading; not a claim that all Mishnah lists finally concern lashes',holder='רבי ישמעאל',cond=['False past-directed oath','Lashes'])
C('rava',34,'The Torah explicitly included a false oath by comparison with a vain oath.','Rava’s derivation supporting past-directed lashes',holder='רבא')
C('vainpast',34,'A vain oath concerns the past in the stated comparison.','Rava’s source premise',holder='רבא')
C('falsepast',34,'A false oath likewise includes the past.','Rava’s consequence of analogy',holder='רבא')
C('pastaccepted',35,'The “I ate” and “I did not eat” cases are explained by Rava’s statement.','Acknowledged support for past-oath lashes in current argument',cond=['False past-directed oath'])
C('notateaction',35,'Swearing “I will not eat” and then eating violates a prohibition with an action.','Acknowledged action-based lashes case',cond=['Oath not to eat','Then eats'])
Q('eatnoaction',35,'Why impose lashes when one swore to eat but did not eat, since the prohibition has no action?', ['Oath to eat','Failure to eat','Interim all-cases lashes reading'])
C('eatnoaction',35,'Swearing to eat and failing to eat is a prohibition without an action.','Premise of objection; question asks how lashes could follow',cond=['Oath to eat','Does not eat'])
C('yishmaelnoaction',36,'The proposed answer assumes Rabbi Yishmael holds that a prohibition without an action receives lashes.','Local reconstruction within interim Mishnah attribution; later author revision does not by itself settle all independent views of Yishmael',holder='רבי ישמעאל',mode='hypothetical',cond=['Prohibition without action'])
Q('yohanancontradiction',[37,38,39],'If so, how can Rabbi Yohanan’s statements be reconciled?', ['He rules according to anonymous Mishnah','This interim reading implies no-action lashes','His express oath ruling denies lashes'])
C('yohanananonymous',38,'The halakhah follows an anonymous Mishnah.','Rabbi Yohanan’s reported rule invoked in contradiction',holder='רבי יוחנן')
C('yohananno',39,'One who swears to eat this loaf today and lets the day pass without eating it does not receive lashes.','Rabbi Yohanan’s express ruling',holder='רבי יוחנן',cond=['Specified loaf','Today','Day passes without eating'])
C('lakishno',39,'One who swears to eat this loaf today and lets the day pass without eating it does not receive lashes.','Resh Lakish agrees on outcome, gives different reason',holder='ריש לקיש',cond=['Specified loaf','Today','Day passes without eating'])
C('yohananreason',39,'The failure to eat is a prohibition without an action.','Rabbi Yohanan’s reason',holder='רבי יוחנן',cond=['Oath to eat specified loaf today','Day passes without eating'])
C('yohanangeneral',39,'One does not receive lashes for a prohibition without an action.','Rabbi Yohanan’s general principle in this report',holder='רבי יוחנן',cond=['Prohibition without action'])
C('lakishwarning',39,'The warning in this case is uncertain.','Resh Lakish’s distinct reason',holder='ריש לקיש',cond=['Oath to eat specified loaf today','Day passes without eating'])
C('lakishgeneral',39,'An uncertain warning does not count as a warning.','Resh Lakish’s principle',holder='ריש לקיש',cond=['התראת ספק'])
C('anotheranonymous',40,'Rabbi Yohanan found another anonymous Mishnah.','Answer to contradiction; which Mishnah is then investigated')
Q('whichanonymous',41,'Which anonymous Mishnah did he find?', ['Answer invoking another anonymous Mishnah'])
C('firstcandidate',41,'The first candidate is the anonymous teaching about leaving over a pure offering or breaking a bone in an impure one.','Candidate tested and found insufficient as evidence of no-action principle',mode='challenged')
C('leaverno',41,'One who leaves over from a pure offering does not receive forty lashes.','Quoted anonymous teaching; rationale disputed next',holder='Anonymous quoted Mishnah',cond=['Leaves over from pure offering'])
C('breakerno',41,'One who breaks a bone in an impure offering does not receive forty lashes.','Quoted anonymous teaching',holder='Anonymous quoted Mishnah',cond=['Breaks bone in impure offering'])
C('breakproof',42,'ועצם לא תשברו בו applies to a valid offering, not a disqualified one.','Accepted reason for no lashes for breaking in impure offering',cond=['Contrast valid and disqualified offering'])
Q('leaverreason',42,'Why does the one who leaves over from a pure offering not receive lashes?', ['Quoted anonymous no-lashes teaching'])
Q('leavernoaction',42,'Is it not because this is a prohibition without an action, for which there are no lashes?', ['Proposed rationale for leftover case'])
C('leaverinference',42,'The proposed inference explains leftover exemption by the no-action principle.','Inference from anonymous teaching challenged as not uniquely established',mode='challenged')
Q('whichyaakov',43,'How do we know this is Rabbi Yaakov’s no-action explanation rather than Rabbi Yehuda’s positive-command-after-prohibition explanation?', ['Anonymous leftover Mishnah','Competing possible authors and grounds'])
C('yaakovcandidate',43,'The anonymous teaching could reflect Rabbi Yaakov’s no-action principle.','Candidate whose unique identification is challenged',mode='hypothetical')
C('yehudacandidate',43,'It could instead reflect Rabbi Yehuda, because the verse supplies a positive command after the prohibition.','Alternative blocks unique no-action inference; not final unique attribution',mode='hypothetical')
C('otherwise',43,'On the proposed Rabbi Yehuda explanation, without that positive-command provision lashes would follow.','Conditional inference in objection, not unconditional lashes ruling',mode='hypothetical',cond=['No subsequent positive command provided'])
C('yehudapositive',44,'The verse provides a positive command after a prohibition to say that no lashes are imposed.','Rabbi Yehuda’s baraita explanation using לא תותירו and באש תשרפו',holder='רבי יהודה',cond=['Leftover offering prohibited','Subsequent command to burn remainder'])
C('yaakovreject',44,'Rabbi Yaakov rejects that rationale: לא מן השם הוא זה.','Explicit disagreement about the ground of exemption',holder='רבי יעקב')
C('yaakovnoaction',44,'The exemption is because leaving over is a prohibition without an action.','Rabbi Yaakov’s alternative reason',holder='רבי יעקב',cond=['Leftover offering'])
C('yaakovgeneral',44,'A prohibition without an action receives no lashes.','Rabbi Yaakov’s principle',holder='רבי יעקב',cond=['Prohibition without action'])
C('secondcandidate',[45,46],'Instead he found the anonymous Mishnah about two oaths not to eat this loaf followed by eating it.','Replacement candidate for Rabbi Yohanan’s anonymous authority; full folio continuation')
C('oneonly',[45,46],'If one swears not to eat this loaf, swears not to eat it, and then eats it, only one liability is incurred.','Repeated oath case; preserves both oath formulations',holder='Anonymous second Mishnah',cond=['שבועה שלא אוכל ככר זו','שבועה שלא אוכלנה','Then eats it'])
C('deliberatelashes',[45,46],'For deliberate violation of this oath of utterance, lashes are imposed.','Quoted characterization of the repeated-prohibitory-oath case',holder='Anonymous second Mishnah',cond=['Deliberate violation'])
C('inadvertentoffering',[45,46],'For inadvertent violation of this oath of utterance, a variable-value offering is incurred.','Quoted characterization; distinct from deliberate lashes',holder='Anonymous second Mishnah',cond=['Inadvertent violation'])
C('zohi',47,'זו היא specifies this case as one receiving lashes for deliberate violation.','Restrictive reading of the second anonymous Mishnah')
C('affirmativenolashes',47,'One who swears to eat and does not eat does not receive lashes.','Exclusion inferred from זו היא, supporting Rabbi Yohanan',cond=['Oath to eat','Does not eat'])
Q('prefer',48,'Since both teachings are anonymous, why follow this anonymous Mishnah rather than the other?', ['Rabbi Yohanan selects no-action-exemption anonymous source','Other anonymous Mishnah read as requiring lashes'])
Q('firstanonymous',41,'Could it be the anonymous Mishnah that exempts the one leaving over from a pure offering and the one breaking a bone in an impure offering?', ['Proposed source for Rabbi Yohanan','Candidate later insufficient because rationale is not unique'])
for k,holder,ii in [('initialyishmael','רבי ישמעאל',30),('initialakiva','רבי עקיבא',30),('yishmaellashes','רבי ישמעאל',33),('yaakovcandidate','רבי יעקב',43),('yehudacandidate','רבי יהודה',43)]:
 add(k+'.candidate','attributions',ii,dict(surface=holder,role='position_holder',candidates=[holder],scope='Proposed author identification only; local alternative/rejected status retained in linked claim, not uniquely accepted final attribution',transmission_chain=[]),[c[k]])
rels=[(29,'yishmaelfuture','neither','support'),(29,'akivatemple','neither','support'),(30,'initialyishmael','who','answer'),(30,'initialakiva','who','answer'),(32,'lesionsliable','allliable','analogy'),(32,'exempt','initialyishmael','objection'),(32,'exempt','initialakiva','objection'),(33,'yishmaellashes','who','answer'),(33,'pastnocorban','yishmaelfuture','qualification'),(33,'pastlashes','yishmaellashes','support'),(34,'vainpast','falsepast','analogy'),(34,'rava','pastlashes','support'),(35,'falsepast','pastaccepted','support'),(35,'eatnoaction','yishmaellashes','objection'),(36,'yishmaelnoaction','eatnoaction','answer'),(39,'yohanananonymous','yohanancontradiction','support'),(39,'yohananno','yohanancontradiction','support'),(39,'yohananreason','yohananno','support'),(39,'yohanangeneral','yohananno','support'),(39,'lakishwarning','lakishno','support'),(39,'lakishgeneral','lakishno','support'),(40,'anotheranonymous','yohanancontradiction','answer'),(41,'firstcandidate','whichanonymous','answer'),(42,'breakproof','breakerno','support'),(42,'leaverinference','leaverreason','answer'),(43,'whichyaakov','leaverinference','objection'),(43,'yehudacandidate','leaverinference','objection'),(44,'yehudapositive','yehudacandidate','support'),(44,'yaakovgeneral','yaakovcandidate','support'),(44,'yaakovreject','yehudapositive','objection'),(44,'yaakovnoaction','leaverno','support'),(44,'yehudapositive','leaverno','support'),(46,'secondcandidate','whichanonymous','answer'),(46,'secondcandidate','firstcandidate','correction'),(47,'zohi','affirmativenolashes','support'),(47,'affirmativenolashes','yohananno','support'),(48,'prefer','anotheranonymous','objection')]
for n,(ii,a,b,r) in enumerate(rels):
 if a=='eatnoaction' and r=='objection':e(str(n),ii,z['eatnoaction'],c[b],r)
 elif b=='eatnoaction' and r=='answer':e(str(n),ii,c[a],z['eatnoaction'],r)
 else:E(str(n),ii,a,b,r)
notes={29:'Author question and apparently neither answer; Yishmael future-only with sacrifice scope clarified3b2, Akiva impurity yes/Temple no distinguished.',30:'Both optional named-author answers preserved with some liable/some exempt, rejected by following analogy.',31:'One-word לפטור is the start of a challenge whose complete evidence continues3b1; not a free-standing exemption ruling.',32:'All-liable lesion analogy challenges both proposed mixtures; no premature choice of liability type.',33:'Interim Yishmael lashes reading separated from actual sacrifice/lashes distinction. Full continuation4a10–5a5 read: this whole-Mishnah reading is superseded; no final author certification.',34:'Rava himself is named authority; vain/false comparison and past scope retained, no invented transmitter.',35:'Past formulas explained by Rava, negative-future breach has action, affirmative-future omission question explicitly captured.',36:'No-action lashes view attributed as local assumed Yishmael explanation, not final author resolution.',37:'Contradiction question spans Rabbi Yohanan anonymous-rule and express oath-case report; full evidence3b6–8.',38:'Rabbi Yohanan rule distinguished from the two amoraim’s later outcome and different reasons.',39:'Full loaf/today/day-expiry conditions, shared no-lashes outcome, distinct no-action and doubtful-warning rationales retained.',40:'Another anonymous Mishnah proposed to resolve contradiction; candidate investigated next.',41:'Which-Mishnah and first-candidate questions recorded; leftover-pure versus bone-breaking-impure separate exemptions.',42:'Valid/not-disqualified verse accepted for breaker; leftover rationale question and no-action suggested explanation retained as challenged.',43:'Rabbi Yaakov versus Rabbi Yehuda is an unresolved candidate contrast here; positive-command exception and counterfactual otherwise-lashes not unconditional rulings.',44:'Both named baraita grounds, Rabbi Yaakov explicit rejection of Yehuda reason, full two-part verse evidence preserved.',45:'Replacement anonymous source retains repeated two oath formulas and eating, reads full4a1 sentence.',46:'Only-one liability, deliberate lashes and inadvertent variable offering distinguished with full previous segment evidence.',47:'Restrictive זו היא inference excludes affirmative oath nonperformance from lashes; not all-oath liability equivalence.',48:'Final core question why prefer one anonymous teaching; remains open. Context4a4–5 supplies Rabbi’s revision chronology with prior Mishnah preserved, and4a10–5a5 revises larger author analysis; not extracted or credited in this batch.'}
for i in range(29,49):
 add('u'+str(i),'utterances',i,dict(textual_voice='Anonymous Gemara framing and quoted named/anonymous authorities as separately recorded',discourse_role=notes[i],composition='composite'))
 add('anon'+str(i),'attributions',i,dict(surface='Anonymous Gemara connective discussion',role='anonymous',candidates=[],scope='Framing and inferences only, not substitution for explicitly named positions',transmission_chain=[]))
COV=[]
for i in range(29,49):
 for l in ['structure','utterances','claims','attributions','questions','positions','edges','reconciliation']:
  ids=[r['id'] for r in R if (l=='reconciliation' or r['layer']==l) and any(v['segment_id']==I[i]['id'] for v in r['evidence'])]
  COV.append(dict(segment_id=I[i]['id'],layer=l,extraction_state='completed',extraction_result='records_found' if ids else 'none_found_after_pass',record_ids=ids,rationale=('Source-first omission reread: ' if l=='reconciliation' else 'Direct '+l+' pass: ')+notes[i]+(' No separate record in this layer found.' if not ids else '')))
P={k:M[k] for k in ['schema_version','tractate','source_sha256','protocol_sha256','schema_sha256']};P.update(owner='L05/shevuot',epoch=2,execution=dict(route='interactive_agent',agent_id='/root/shabbat',model_id=None),records=R,coverage=COV,open_tails=S['open_tails']+[s1])
b=(json.dumps(P,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode();out=H/'shevuot_3a10_4a3_final_proposal.json'
if out.exists():assert out.read_bytes()==b
else:out.write_bytes(b)
print(json.dumps(dict(records=len(R),new_segments=20,sha256=hashlib.sha256(b).hexdigest())))
