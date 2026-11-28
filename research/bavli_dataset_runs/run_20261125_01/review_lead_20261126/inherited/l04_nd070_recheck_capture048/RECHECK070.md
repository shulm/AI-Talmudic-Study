# Additive original-comparator recheck: correction070

**D1–D4 CLOSED for the bounded findings against exact correction snapshot `7d9b6947557eaf3b807e913f1acde3c82ca39e9124610980288d993b33f1fa3b`.** Mechanical replay and graph/coverage closure PASS. This does not grant broad semantic acceptance, source expansion review, human certification, or ML eligibility.

This recheck is additive to `COMPARISON.md`; the original comparison of historical1083 snapshot `b6421aabe6cab3ce7d705b4e1dd71fa6f1dab74a7a6122db508b95ce954e8b74` remains unchanged and valid as a description of that version. The repair's base is1105 snapshot `5168ca1425eb9ef707abb189482125b347fb49a65fc7e7effcec2309dbf96ce4`, and its proposal is `66ee6a75c0c45686cddf5babb7e4948347a49814136019e91cd4b0c42456d60e`. No CURRENT lookup selected the rechecked version.

## Verification and chronology

Read the frozen repair receipt and closure/checkpoint metadata, then independently replayed the exact accepted prefix before inspecting the new semantic records. The direct replay validated all72 accepted proposals and reconstructed the exact named snapshot. `RECHECK070_MECHANICAL.json` records completion at2026-11-27T13:21:20.257075Z. This invocation completed without an execution failure.

The delta is exactly34 new nodes:17 successors with explicit supersession mappings and17 additive nodes. Every pre-existing record is unchanged except the17 mapped predecessors' release states. All active links, typed claim/question/edge endpoints, exact attribution scopes and embedded references to the superseded IDs close on active records. Coverage references also close; all new nodes are represented in every corresponding evidence-reference/layer cell. Exactly28 existing coverage cells change, and no coverage keys are added by the repair. All eight completed-layer counts remain1105.

The233 records and176 cells introduced by window069 are byte-for-byte unchanged relative to the base. All233 records retain unreviewed state and false eligibility. The original069 failure-lineage hash is unchanged. This is preservation checking, not semantic reading of those22 additional references. The export manifest and every listed export file hash match the frozen repair receipt.

Original comparison artifacts and reader SHA pins remain unchanged. The earlier optional initial dump failure (`KeyError: release_state` after a successful original replay receipt), its additive recovery, and the source-only adapter limitations remain disclosed in `COMPARISON.md`. The repair closure receipt's phrase historical1062 is an acknowledged inherited wording error: the original comparison was historical1083. The frozen repair receipt explicitly records this correction; no old receipt is overwritten.

## Source-grounded disposition

**D1, core23a:4 — CLOSED.** `nd.fix121.repeated.q` now represents `נדרת אדעתא דהכי` and the second printed `נדרתא אדעתא דהכי`; the utterance/attribution names the sages from `אתא לקמייהו דרבנן אמרו ליה`. `nd.fix121.repeated.answer` connects the existing repeated-yes claim `nd.r023.questions.c` to the new question, supported by `אמרו ליה ... אמר להו אין ... כמה זימנין`. Unknown individual circumstances remain unspecified. The question has partial answer-set status without claiming exhaustive alternatives. Questions coverage now includes it.

The new repeated `.u/.a/.q` evidence arrays each contain10 entries but only4 distinct exact spans. These are duplicate evidence entries, not ten separate occurrences or ten new semantic facts. This redundancy does not reopen D1; downstream counts must count distinct spans/records appropriately. No cleanup mutation is made or required by this bounded recheck.

**D2, core25a:8 — CLOSED.** `nd.fix121.premise.u/.c/.a/.p` retain the previously missing first101 characters: `מאי אמר להו משה לישראל לאו הכי קאמר להו דלמא עבידתון מילי ואמריתון על דעתינו משום הכי אמר להו על דעתי`. The claim is hypothetical, anonymous, and explicitly an interpretation of the cited speech rather than a fresh certified historical speech by Moses. Its qualification edge targets `nd.r025.moses.c`. The existing subsequent private-idol-name hypothesis and lexical rebuttal are preserved separately. This resolves the omitted premise without flattening the proposed inference into a final ruling.

**D3, bounded core attribution cases — CLOSED.**

- At21a:2, `nd.r021.report.u.fix121/.a.fix121` name Rabbi Abba bar Mamal as speaker. `nd.r021.nesia.chain.fix121` preserves Abba bar Mamal→Rabbi Ami→Rabbi Yehuda Nesia; `nd.fix121.nesia.authority` separately identifies Nesia as quoted authority, and the position holder is Nesia. This matches `אמר ליה רבי אבא בר ממל לרבי אמי אמרת לן משמיה דרבי יהודה נשיאה` while keeping the tanna Yehuda distinct.
- `nd.fix121.tarfon.transmitter` now encodes Rabbi Yehuda→Rabbi Tarfon from `רבי יהודה היא דאמר משום רבי טרפון`; `nd.r021.tarfon.a.fix121` uses quoted-authority role for Tarfon. The principle's substantive claim remains unchanged.
- At21a:4–5, `nd.r021.invitation.u.fix121/.a.fix121` identify Rav Ashi from Ravina's addressed question and the following `אמר ליה תנינא`. Its claim/scope and position explicitly distinguish Rav Ashi as citing speaker from the unidentified original author of the teaching. Empty original-holder candidates here are appropriate and do not reopen the typed-speaker defect.
- At23a:4, `nd.r023.wouldnot.u.fix121/.a.fix121/.p.fix121` identify Rabbi Yishmael bar Rabbi Yosi for `אמר אדעתא דמחי לי קצרא לא נדרי`. The counterfactual-blow condition remains. The separate difficult `ושריה לנפשיה` wording is not converted into a general self-annulment permission.

The successor graph also redirects Rava's objection and Tarfon's support to the new report claim, and the novel-event objection to the new Yishmael claim. Existing attributions and position claim references no longer target the superseded nodes.

**D4 core — CLOSED, four explicit relations.**

- `nd.fix121.invitation.objection`:23a:9 `וכיוון דאמר ... לא שמע ליה ולא אתי בהדיה`, `nd.r024.ob.q`→`nd.r024.m.c`, objection.
- `nd.fix121.private.inference.objection`:25a:3 `ומדקאמר על דעתינו מכלל ...`, `nd.r025.infer.c`→`nd.r025.common.c`, objection.
- `nd.fix121.moses.objection`:25a:7 `ואכתי לא עביד דמישתבע אדעתא דנפשיה`, `nd.r025.mosesq.q`→`nd.r025.common.c`, renewed objection.
- `nd.fix121.moses.support`:the following `והתניא וכן מצינו במשה רבינו ...`, `nd.r025.moses.c`→`nd.r025.mosesq.q`, support.

**D4 fully reviewed context25a:2 — CLOSED separately, two relations.** `nd.fix121.context.private.objection` connects `nd.r025.private.q`→`nd.r025.common.c` on `ועל דעתא דנפשיה לא עביד איניש דמשתבע`; `nd.fix121.context.court.support` connects `nd.r025.court.c`→`nd.r025.private.q` on `והתניא כשהן משביעין אותו ... על דעתינו ועל דעת בית דין`. These remain context findings and do not enlarge the30 sampled cores.

## Preserved limitations

U1's nine answer-status cases, including their exact question, answer-edge and answer records, remain unchanged. The enum's field-meaning uncertainty is not silently resolved. U2's two null comparable-question position links remain unchanged. Neither is upgraded to a confirmed schema violation. The other reader findings, including its context22b:11 typed-question omission, the23a:7 answer-explicitness observation, status-vocabulary ambiguity, prudent25a:4 speaker uncertainty, and reasonable grouping differences remain as originally reported.

The30-core/15-context/38-incidental separation remains in force. This recheck does not review unrelated active records, the later22-reference window, all1105 extracted references, or a full tractate. Human-readable source-only IDs and descriptive open tails still require a production adapter; a mechanical PASS does not establish adapter compatibility. No source, production, eligibility, original reader, or initial comparison artifact was mutated.

## Reproduce

Run `python -B -X utf8 recheck070.py` for pins, full exact-prefix replay, immutable delta, active graph/content/scope closure, coverage counts, window preservation and U1/U2 preservation. Run `python -B -X utf8 recheck070_delivery.py` for new-node coverage incidence, exact repaired endpoints, export hashes, failure-lineage preservation and delivery hashes. Omit `--receipt` on rerun: existing receipts are immutable. `RECHECK070_RECORD_EVIDENCE.json` preserves all34 exact repair nodes with source quotes and IDs. These checks reproduce mechanics and record assertions; the bounded scholarly judgments above remain AI provisional.
