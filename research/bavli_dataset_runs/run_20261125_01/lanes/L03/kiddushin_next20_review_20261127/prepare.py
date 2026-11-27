import json,hashlib,sys
from pathlib import Path
root=Path.cwd();sys.path.insert(0,str(root/'research/bavli_production_v1'));import runner
out=Path(__file__).resolve().parent;job=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin');j,src=runner.load(job);s=list(src.values());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert runner.sha(runner.encoded(runner.current(job)))=='485622fdbe5533eba01863f478943dfd0b7ad5ffa38f9832c18776dbd4f74e2d'
# Manual source-first findings; no new producer proposal exists at this preparation.
notes={
10:['Explicit why שלוש rather than שלושה question.','Female grammatical דרך supported by Exodus quotation; linguistic derivation, not halakhic outcome.'],
11:['Male seven ways in zav examination raises counterexample.','Deuteronomy quotation supports masculine דרך.','Both verse-to-verse and Mishnah-to-Mishnah contradictions explicitly asked.'],
12:['Torah context explains feminine grammar, with Psalms feminine תורה evidence.','War context explains masculine grammar by the text’s assertion that war is normally a man’s way, not a woman’s. Keep source cultural assertion separate from endorsement.'],
13:['Mishnah about woman uses feminine grammar.','Male zav examination explains masculine grammar.','Female discharge conveys impurity even under compulsion; this supplies the contrast, not a blanket assertion that women are never examined for anything.'],
14:['Why not דברים with masculine numeral is an explicit alternative-wording question.','Intercourse is called דרך, with Proverbs citation.'],
15:['Question challenges money/document terminology when only intercourse is called דרך.','Initial reply says it follows intercourse.'],
16:['Objection asks why two follow one.','Reply says the other methods also serve intercourse; preserve local rationale without importing intention requirements.'],
17:['Alternative answer identifies the formulation with Rabbi Shimon.','Quoted Rabbi Shimon asks why Torah says man takes woman, not woman taken to man.','His answer says man characteristically pursues woman, not reverse.','Lost-object analogy: owner pursues lost item. Keep analogy distinct from actual ownership law.'],
18:['Zav wording challenged again: why דרכים rather than דברים?','Excess eating is said to bring discharge.','Excess drinking is said to bring discharge.'],
19:['Etrog equal to tree in three ways cited and challenged.','Initial response depends on ending: like vegetable in one way.','Question challenges ending too: why not דבר?'],
20:['Vegetables grow on all water sources.','Vegetable tithe-year follows picking.','Etrog likewise grows on all water and its tithe-year follows picking.','This vegetable analogy answers initial etrog wording stage, not final universal terminology principle.'],
21:['Koi citation distinguishes four relation types: like wild animal, like domesticated animal, like both, like neither.','Question asks why these are ways rather than things.','Further question from wording comparing women’s divorce documents and slaves’ release documents. Do not invent the unquoted particular shared rule.'],
22:['Final אלא principle: where there are differentiated aspects use דרכים, where none use דברים. Do not force פלוגתא here into a named interpersonal dispute.','Support: printed ר״א says etrog equals tree in every דבר. Preserve abbreviation rather than guessing identity from order.','Final wording principle revises earlier blanket explanations; earlier local analogies remain initial reasoning, not erased.'],
23:['Two explicit exclusion questions: opening count and closing count.'],
24:['Opening count excludes chuppah on first answer.','Rav Huna holds chuppah acquires by a fortiori argument.','Follow-up asks what count excludes under Rav Huna; no false unanimous rejection of chuppah.'],
25:['Answer excludes halipin.','Hypothetical: field taking analogy might permit halipin as for Ephron field.','Conclusion rejects that hypothetical; initial derivation preserved.'],
26:['Question asks why not actually permit halipin.','Halipin can operate below perutah value.','Woman-below-perutah clause is unfinished at folio boundary; join3b1 without index shift.'],
27:['Cross-folio completion: woman does not allow acquisition of herself for less than perutah.','Keep local halipin-exclusion rationale distinct from all possible future less-than-perutah cases.'],
28:['Closing count excludes halitzah.','Hypothetical a fortiori from yevamah: she lacks get release yet has halitzah; married woman has get, so perhaps halitzah too.','Rejected inference retained; yevamah versus wife subjects kept distinct.'],
29:['Question repeats why halitzah should not work.','ספר כריתות answer restricts the severing instrument: document severs, no other thing.','Scope is proposed alternative act of release in this argument; do not negate husband-death release already taught in opening Mishnah.']}
findings=[]
for i,items in notes.items():
 for text in items:findings.append(dict(id='kid_next20_'+str(len(findings)+1).zfill(3),ref=s[i]['ref'],source_index=s[i]['source_index'],finding=text,evidence=[dict(segment_id=s[i]['id'],start_char=0,end_char=len(s[i]['text']),quote=s[i]['text'])]))
packet=dict(status='FROZEN_SOURCE_FIRST_BEFORE_NEW_PRODUCER',reader='/root',method='Purposive contiguous source reading, no new random cohort. Root saw earlier first-batch producer script and review summary but did not produce Kiddushin; no new-batch labels exist or were viewed.',source_sha256=j['source_sha256'],schema_sha256=j['schema_sha256'],protocol_sha256=j['protocol_sha256'],base_snapshot='485622fdbe5533eba01863f478943dfd0b7ad5ffa38f9832c18776dbd4f74e2d',core_segments=20,core_start=s[10]['ref'],core_end=s[29]['ref'],core_indices=[s[10]['source_index'],s[29]['source_index']],context_read='Earlier opening2a1–2b5 known; following3b4–4a6 source read only. New topic starts3b4; no core coverage inflated.',findings=findings,qualification=False)
f=out/'SOURCE_READING.json';assert not f.exists();f.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(out/'SOURCE_MANIFEST.json').write_text(json.dumps({'SOURCE_READING.json':sha(f),'prepare.py':sha(Path(__file__))},indent=2)+'\n',encoding='utf-8');print(json.dumps({'findings':len(findings),'source_reading_sha256':sha(f)}))
