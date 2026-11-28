import json,sys
from pathlib import Path
OUT=Path(__file__).parent;ROOT=OUT
while not (ROOT/'research/bavli_production_v1/runner.py').exists():ROOT=ROOT.parent
sys.path.insert(0,str(ROOT/'research/bavli_production_v1'));import runner
J=Path('F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot');job,segs=runner.load(J);s=list(segs.values());core=s[198:218];assert core[0]['ref']=='Yevamot 9a:14' and core[-1]['ref']=='Yevamot 9b:8'
by={x['ref'].removeprefix('Yevamot '):x for x in s}
data=[
('9a:14','Inference may distinguish collective/individual offerings after punishment/property distinction; תורה אחת rejects a difference. Preserve prior9a12–13 setup as context.'),
('9a:15','Rav Hilkiya of Hagronya challenges the need for תורה אחת: without it, what different offering could they bring? Named objector, not holder of rejected differential rule.'),
('9a:15','Bull candidate excluded as already public offering for other commandments; distinguish candidate from endorsed instruction.'),
('9a:16','Female lamb candidate corresponds to individual other-commandment offering.'),
('9a:16','Male goat candidate corresponds to ruler other-commandment offering.'),
('9a:16','Bull burnt offering plus male-goat sin offering corresponds to public idolatry offering.'),
('9a:16','Female-goat candidate is already individual idolatry offering; it supplies no differentiation.'),
('9a:17','Anonymous answer: one might invert the public instruction-error pair for this group; rejection hypothetical requires explicit polarity. Source says איפכא; do not confuse this with transmitter-name inversion.'),
('9a:18','Alternative need for verse: one could think an offering is required but there is no remedy/available offering. This is a rejected hypothetical, not final denial of atonement.'),
('9a:19','Levi asks Rabbi why fifteen rather than sixteen exemptions; preserve speaker and addressee.'),
('9a:19','Rabbi’s sharp reply is quoted speech, not annotator characterization of Levi.'),
('9a:20','Editorial reconstruction identifies proposed sixteenth as his mother who was raped by his father; not his father’s wife.'),
('9a:21','Initial explanation: mother raped by father is disputed by Rabbi Yehudah and sages.'),
('9a:21','Initial methodological answer says Mishnah does not deal with disputed cases. Later10a alternatives qualify this; not an unqualified final universal redaction principle.'),
('9a:22','Challenge from categories prohibition of mitzvah and holiness begins; sentence continues9a23.'),
('9a:23','Rabbi Aqiva/sages dispute and inclusion of those categories challenge the no-dispute principle; keep cross-segment linkage.'),
('9a:24','Reply restricts no-dispute principle to our chapter.'),
('9a:24','Beit Shammai permits co-wives to brothers; Beit Hillel prohibits. Separate substantive views from editorial challenge.'),
('9a:24','Their dispute is a counterexample to the chapter restriction.'),
('9a:25','Reply: Beit Shammai against Beit Hillel is not treated as authoritative Mishnah here; source methodological statement, not global deletion of Beit Shammai occurrences.'),
('9a:25','Next counterexample: wife of brother who was not in his lifetime; statement continues9b1.'),
('9b:1','Rabbi Shimon/sages dispute challenges no-dispute explanation.'),
('9b:1','Answer begins born, then underwent yibbum; complete9b2 before assigning chronology.'),
('9b:2','Rabbi Shimon does not dispute in born-then-yibbum case according to this reply. Do not reverse temporal order.'),
('9b:3','Rabbi Oshaya reportedly said Shimon disputed even the first case; this is objection to preceding reply.'),
('9b:4','Reply says Rabbi Oshaya was refuted. Preserve the report and its rejected status; do not simply retain competing live Shimon assignments.'),
('9b:5','Rav Yehudah reports Rav; Rabbi Hiyya teaches similarly. Two transmission routes, not a fabricated Rav→Hiyya chain.'),
('9b:5','Quoted all-cases schema: woman forbidden to this man permitted to the other, reciprocal case likewise, and her sister who is her co-yavam-wife undergoes halitzah or yibbum. Preserve two directions and two procedural options.'),
('9b:5','This all-cases schema introduces another challenge to refusal to include disputed cases; its subsequent interpreters narrow or broaden applicability.'),
('9b:6','Rav Yehudah applies schema from mother-in-law onward.'),
('9b:6','Rav Yehudah excludes first six cases; explicit why question.'),
('9b:7','Because his daughter begins explanation continued9b8; preserve original short segment and no fabricated standalone outcome.'),
('9b:8','Daughter configuration is available through rape/nonmarital relation, not marriage.'),
('9b:8','Rav Yehudah’s interpretation confines schema to marriage situations, not rape situations. Following Abaye and Rav Safra expand scope; not universal final exclusion.'),
('9b:9','CONTEXT Abaye includes daughter from rape because possible realization suffices; retains bracketed alternative wording rather than silently normalizing.'),
('9b:10','CONTEXT Abaye excludes brother-not-in-lifetime because realization requires Shimon rather than sages; he invokes no-dispute principle.'),
('9b:11','CONTEXT Rav Safra includes brother-not-in-lifetime using six brothers and Shimon; distinct third interpreter.'),
('10a:1','CONTEXT mnemonic death/birth/yibbum repeated twice belongs to Rav Safra construction, not arbitrary chronology for all cases.'),
('10a:2','CONTEXT asks whether Rabbi lacks these principles. Rav Adda Karhina before Rav Kahana reports Rava: Rabbi does hold them; mother-rape case fits one schema but not both.'),
('10a:3','CONTEXT Jacob with two sisters realizes sister/co-yavam relation but not forbidden-to-one/permitted-to-other reciprocity.'),
('10a:4','CONTEXT two unrelated women realizes reciprocal prohibition/permitted cases but not sister/co-yavam relationship. Separate opposite conditions.'),
('10a:5','CONTEXT Rav Ashi alternative: Rabbi does not hold these general rules and does discuss disputes. Explicit alternative to Rava; do not combine conclusions.'),
('10a:6','CONTEXT Rav Ashi reads Rabbi’s rebuke as failure to notice Mishnah follows Rabbi Yehudah forbidding father’s rape victim; printed bracketed clause retained.'),
('10a:7','CONTEXT cited six severe relations list: mother cannot simply mean father’s married wife, since father’s wife separately listed. Duplicate-category objection.'),
('10a:8','CONTEXT inference mother is father’s rape victim, married only to others not brothers; identified with Rabbi Yehudah. Basis for excluding sixteenth, distinct from initial no-disputes answer.'),
('10a:9','CONTEXT Ravina to Rav Ashi: could occur if brother transgressed and married her; answer excludes conditional-transgression cases.'),
('10a:10','CONTEXT Rav Ashi to Rav Kahana offers a construction without that conditional marriage: Jacob rapes daughter-in-law, son born, Reuben dies childless, she falls before her own son; her prohibition extends to co-wife. Preserve stated names/roles without genealogical shortcut.'),
('10a:11','CONTEXT reply limits treatment to permitted sister situation, not prohibited sister situation. Nevertheless Levi examined/added this in his teaching; do not falsely mark Levi’s proposal wholly absent afterward.'),
('10a:12','CONTEXT Levi says mother sometimes exempts co-wife and sometimes not; mother married to father then paternal brother does not exempt co-wife in specified case.'),
('10b:1','CONTEXT Levi says mother raped by father then married paternal brother and he dies exempts co-wife; separate from married-to-father case.'),
]
findings=[]
for n,(ref,text) in enumerate(data,1):
 x=by[ref];findings.append({'id':f'YV011-{n:03}','scope':'context' if text.startswith('CONTEXT ') else 'core','ref':x['ref'],'source_index':x['source_index'],'finding':text,'evidence':[{'segment_id':x['id'],'start_char':0,'end_char':len(x['text']),'quote':x['text']}]})
out={'status':'FROZEN_SOURCE_ONLY_BEFORE_NEW_LABELS','reader':'/root/rosh_hashanah','source_sha256':job['source_sha256'],'schema_sha256':job['schema_sha256'],'protocol_sha256':job['protocol_sha256'],'scope':{'core_segments':20,'first':core[0]['ref'],'last':core[-1]['ref'],'inventory_indices':[198,217],'original_indices':[core[0]['source_index'],core[-1]['source_index']],'context_read':'9a9–13;9b9–10b1; additionally10b2–11a6 inspected for transition but not exhaustive context annotation'},'exposure':'Never produced Yevamot. Earlier opening Yevamot correction-review assignment and its pins/findings context present in inherited history; no fresh-agent claim. No current next20 production labels viewed. Purposive contiguous source review, not random cohort.','source_evidence':[{'ref':x['ref'],'source_index':x['source_index'],'text':x['text']} for x in s[193:234]],'findings':findings,'layer_checks':{'structure':'Sacrifice distinction finishes9a18; Levi question opens9a19 and requires10a alternatives/Levi followup; raw short9b7 retained.','utterances':'Cross-segment9a22–23,9a25–9b2,9b7–8 preserved.','claims':'Candidate offerings not asserted final instructions; separate exceptions and scope.','attributions':'Hilkiya, Levi→Rabbi, RavYehudah→Rav versus Hiyya parallel, Oshaya rejected report; later Abaye/Safra/Rava/Ashi distinct.','questions':'Necessity/what offering,15vs16, repeated counterexamples and scope why retained.','positions':'Initial no-dispute explanation later alternatives; no forced merger.','edges':'Replies/objections, Oshaya refutation, Rava versus Ashi alternatives; no named-order assignment.','reconciliation':'All20 cores checked against full relevant continuation;50 findings are purposive audit prompts, not exhaustive atomic gold records.'},'ml_eligible':False,'eligible_records':0,'fresh_blind_cohort_credit':0,'random_cohort_credit':0,'producer_labels_seen':False,'qualification':False}
assert len(findings)==50
runner.immutable(OUT/'SOURCE_READING.json',runner.encoded(out));m={f.name:runner.sha(f.read_bytes()) for f in OUT.iterdir() if f.is_file() and f.name!='MANIFEST.json'};runner.immutable(OUT/'MANIFEST.json',runner.encoded(m));print(json.dumps({'reading':m['SOURCE_READING.json'],'manifest':runner.sha((OUT/'MANIFEST.json').read_bytes()),'core_findings':sum(f['scope']=='core' for f in findings),'context_findings':sum(f['scope']=='context' for f in findings)}))
