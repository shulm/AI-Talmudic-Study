import json,hashlib
from pathlib import Path
OUT=Path(__file__).parent;sha=lambda b:hashlib.sha256(b).hexdigest()
S=Path('F:/Sefaria-Export-master/json/Talmud/Bavli/Seder Nashim/Nazir/Hebrew/Wikisource Talmud Bavli.json');assert sha(S.read_bytes())=='29a2a4347221c24b248de9b131523cb8354dcbf78d7975167c12ab7c13d43bef'
t=json.loads(S.read_text(encoding='utf-8'))['text'];core=[f'Nazir 2a:{n}' for n in range(11,15)]+[f'Nazir 2b:{n}' for n in range(1,11)]+[f'Nazir 3a:{n}' for n in range(1,7)]
ev=[]
for i,js in [(2,range(7,14)),(3,range(10)),(4,range(10))]:
 for j in js:
  ref=f'Nazir {i//2+1}{"a" if i%2==0 else "b"}:{j+1}';ev.append({'ref':ref,'source_index':[i,j],'text':t[i][j],'role':'core' if ref in core else 'context'})
notes=[
 ('2a:11','Anonymous citation','Animal-going-out Mishnah starts with permitted going out after announcing both permission/prohibition.','counterexample','Against universal last-mentioned-first, not contradicting factual lighting example.'),
 ('2a:12','Anonymous citation','Inheritance Mishnah lists inheritance-and-bequest, inheritance-only, bequest-only and neither.','citation','Four categories recoverable; producer may retain composite utterance but separate asserted classification as needed.'),
 ('2a:12','Anonymous citation','It explains those both inheriting and bequeathing first.','counterexample','Second example against universal ordering principle; preserve distinct occurrence.'),
 ('2a:13','Anonymous','Both exposition orders occur.','correction','Universal last-first rule rejected; neither all first-first nor all last-first established.'),
 ('2a:14','Anonymous','Where prohibition attaches to person himself, prohibited side explained first.','local rationale','Lighting/insulation/woman-going-out examples; not universal irrespective of subject.'),
 ('2a:14','Anonymous','For animal-mediated prohibition, permitted side explained first.','local rationale','Separate reason for animal case.'),
 ('2b:1','Anonymous','Inheritance discussion explains principal inheritance first.','local rationale','Continuation of ordering examples, not isolated inheritance ruling.'),
 ('2b:2','Anonymous','Then why not explain kinuyim first here?','renewed question','Repeated question occurrence distinct from2a8.'),
 ('2b:2','Anonymous','Yadot explained first because derived by exposition and dear to tanna.','local answer','Do not infer universal last-first principle remains final.'),
 ('2b:3','Anonymous','Why not begin with yadot?','question','Opening order versus explanatory order distinguished.'),
 ('2b:3','Anonymous','Opening begins with primary offering formulation.','answer','Exact עיקר קרבן retained; avoid unsupported generalized theory.'),
 ('2b:3','Anonymous','Explanation begins with yadot.','answer','Two purposes, not competing anonymous held views.'),
 ('2b:4','Quoted Mishnah','Saying aha establishes naziriteship.','repeated occurrence','Not new unique topic; continuation necessary.'),
 ('2b:4','Anonymous','Could aha mean I will fast?','alternative objection','Not an asserted fasting vow.'),
 ('2b:4','Shmuel','Aha case has a nazir passing before speaker.','qualification','Distinct Shmuel utterance, linked to quoted aha.'),
 ('2b:5','Anonymous','Does this imply Shmuel holds non-demonstrative handles ineffective?','proposed inference question','Do not attribute unqualified general doctrine by limakasavar alone.'),
 ('2b:5','Anonymous reply','With nazir passing, no other interpretation is in doubt.','scope clarification','Specific case is demonstrative.'),
 ('2b:5','Anonymous reply','Without passing nazir, it may mean I will fast.','ambiguity','No automatic nazirite designation in absence of disambiguating context.'),
 ('2b:6','Anonymous','Could intent be to discharge another nazir’s offering obligations?','objection','Passing nazir condition not sufficient on its own for intended personal status.'),
 ('2b:6','Anonymous answer','He intends in his heart the nazirite undertaking.','qualification','Meaning inferred from question/answer; no silent vow generalization.'),
 ('2b:7','Anonymous','If so what is novel?','question','Novelty of abbreviated spoken expression with intent.'),
 ('2b:7','Anonymous','One might require mouth and heart to match fully; teaches abbreviated declaration suffices here.','rejected hypothesis and answer','Do not generalize to no speech or no intention needed.'),
 ('2b:8','Quoted Mishnah','Aha naeh establishes naziriteship.','repeated occurrence','Later hair condition required.'),
 ('2b:8','Anonymous objection / baraita','May mean beautifying mitzvot, as זה אלי ואנוהו interpreted.','alternative reading','Not naziriteship uniquely from beauty word alone.'),
 ('2b:8','Cited baraita','Beautification exemplified by beautiful sukkah, lulav, tzitzit, Torah scroll and fine silk wrapping.','five examples','Retain distinct items in production, not opaque general summary if claiming full claims pass.'),
 ('2b:9','Shmuel','He holds his hair while making beauty declaration.','qualification','Answers mitzvah-beautification ambiguity.'),
 ('2b:10','Anonymous','How can naziriteship be called beautiful if a matter of transgression?','objection','Do not treat premise as universally maintained final conclusion.'),
 ('3a:1','Anonymous explanation invoking Rabbi Elazar HaKappar','Even the nazir-as-sinner teaching is applied here to impure nazir.','distinction','Not a universal attribution of all following rationale to Rabbi Elazar directly.'),
 ('3a:1','Anonymous','Impurity nullifies preceding days, with cited verse.','premise','Explains why renewed obligation may tempt transgression.'),
 ('3a:1','Anonymous','Concern is that impure nazir may transgress naziriteship because days must restart.','conditional rationale','Fear, not asserted individual conduct.'),
 ('3a:1','Anonymous','Pure nazir not called sinner in this local explanation.','answer','Resolves beauty objection; no outside halakhic finality.'),
 ('3a:2','Quoted Mishnah','I am like this establishes nazirite status.','repeated lemma','Do not merge occurrence with original2a2.'),
 ('3a:2','Anonymous objection','Holding hair alone does not supply this referent.','objection','Hair alone not sufficient for this formula.'),
 ('3a:2','Shmuel','A nazir passes before him for like-this declaration.','qualification','Do not indiscriminately copy hair-holding condition from other formulas.'),
 ('3a:3','Anonymous question / maid in Rabbi’s household','Mesalsel is glossed as tending hair from maid’s speech to a man.','lexical evidence','Maid is source speaker, not Rabbi personally.'),
 ('3a:4','Anonymous','Could mesalsel refer to Torah, using סלסלה ותרוממך?','alternative objection','Source citation distinct from actual hair interpretation.'),
 ('3a:4','Shmuel','Here too he holds his hair.','qualification','Answers Torah alternative for mesalsel.'),
 ('3a:5','Anonymous cited Mishnah / Rabbi Yehudah','The lime measure for kilkul is cited for hair terminology.','lexical premise','Rabbi Yehudah gives quantity sufficient to lime kilkul; not Shmuel opponent.'),
 ('3a:5','Rav','Kilkul glossed as temple hair (בת צידעא).','lexical explanation','Rav distinct from Rabbi Yehudah and from Shmuel; no Rav–Shmuel dispute.'),
 ('3a:6','Anonymous','Could mekalkel mean sustaining poor, via Joseph supporting family verse?','alternative objection','Not claimed speaker donated money.'),
 ('3a:6','Shmuel','Here too he holds his hair.','qualification','Answers sustenance alternative; separate occurrence from3a4.')]
out={'artifact_kind':'frozen_purposive_contiguous_source_reading','reviewer':'/root/rosh_hashanah','source':{'path':str(S),'sha256':sha(S.read_bytes())},'scope':{'core_refs':core,'core_segments':20,'context_refs':[e['ref'] for e in ev if e['role']=='context'],'sampling':'Purposive contiguous next20; not random review'},'exposure':{'new_production_seen':False,'prior_source_and_label_exposure':'All these source cores previously read as opening-batch context. Comparator reviewed initial10core labels and correction, including limited context qualifiers in this passage. This is not blind to all semantic interpretations; no new fresh blind-cohort claim. New bounded002 labels unseen.'},'evidence':ev,'findings':[{'id':f'NA2-{i:02d}','ref':'Nazir '+r,'holder':h,'proposition':p,'status':st,'qualification':q} for i,(r,h,p,st,q) in enumerate(notes,1)],'qualification':{'ml_eligible':False,'all_demanding_tasks':False},'status':'FROZEN_BEFORE_NEXT_BATCH_LABELS'}
b=json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();p=OUT/'SOURCE_READING.json'
if p.exists():assert p.read_bytes()==b
else:p.write_bytes(b)
print(json.dumps({'source_reading_sha256':sha(b),'core_segments':20,'findings':len(notes)}))
