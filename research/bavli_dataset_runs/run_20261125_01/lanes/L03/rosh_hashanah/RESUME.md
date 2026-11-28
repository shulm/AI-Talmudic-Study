# Rosh Hashanah epoch 3 checkpoint — PARTIAL

The lane lead requested a durable checkpoint because its execution context was limited. This is not whole-tractate delivery and does not claim background continuation.

- Owner: `L03/rosh_hashanah`; epoch `3`.
- Job: `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah`.
- Snapshot: `73e6ef36b8a8df4f14fc006202501b4bfbeee0589919f8ad4c8330c7f3103592`.
- Eight required passes: **144/1025** original segments each. **881 remain per pass**.
- Completed prefix ends at **Rosh Hashanah 7a:2**; next for every pass **7a:3**.
- Runner reports 939 semantic records. Historical proposals and superseded records remain preserved.
- Independent full-tractate review: unfinished; no eligibility or delivery certification. Legacy `ml_eligible=false` retained.
- Export: `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/rh_export_epoch3_009`.
- Exact proposal chain, export manifest hash, and file hashes: `CHECKPOINT.json`.

## Resume

Read repository instructions, `AGENT_HANDOFF.md`, active contract, and this tractate’s prepared assignment. Recheck current owner and epoch before promotion; this checkpoint does not override a later handoff.

```powershell
python -X utf8 research/bavli_dataset_runs/verify_active_run.py
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah
python -X utf8 research/bavli_production_v1/runner.py packet --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_rosh_hashanah --start-ref 'Rosh Hashanah 7a:1' --end-ref 'Rosh Hashanah 8a:10' --output F:/Sefaria_QA/bavli_production_run_20261125_01/L03/rh_packet_010.json
```

The packet range is a reading window, not an annotation boundary. Existing context was read through 7b:12 but **only through 7a:2 was annotated**. Next topic begins at 7a:3: Nisan for months, intercalation cessation, new shekel appropriation, and house rentals. Its continuation must be read before semantic completion. Preserve indices and empty positions. No current primary structure is open: the previous firstborn-clock reconciliation closes at 7a:2. Future proposals need new IDs, not regenerated or duplicate accepted records.

Builders `build_batch_005.py` through `build_batch_009.py` encode explicit source-read judgments; they are serialization conveniences, not semantic extraction algorithms. Later builders reuse only the first builder’s helper definitions. Their packet inputs remain external at `.../L03/rh_packet_next.json` and `rh_packet_006.json` through `rh_packet_009.json`. **Deterministic replay uses frozen accepted proposals and does not require these builders or a model call.**

Batch 005’s initial proposal failed because prose was supplied in `open_tails`, which must contain active open-structure IDs. `proposal_005_rejected_open_tail.json` preserves that rejected attempt; the accepted replacement has an empty list because the unit closes. Batch 008 serialization caught a nonexistent copied citation string in 6a:2 before writing a proposal; it was corrected against exact source. No source files changed.

## Review and unresolved scope

The independent source-first reader is coordinated by L03. Producer outputs must not be supplied to a fresh blind reader before its source reading is frozen. No comparison or reviewer agreement is claimed here. All five new producer batches need exact-version discrepancy comparison. Retain correction proposals with explicit supersedes and updated coverage.

Specific preserved risk cases and potential authority-catalogue proposals for the designated owner (no registry writes):

- 3a:8 retains `ר״א` unexpanded rather than selecting an unsupported identity.
- 3a:3 retains two versions of Sihon/Arad name interpretation; 3b:10 reports the source’s Cyrus/Darius/Artaxerxes identification without external historical endorsement.
- 4a:6 preserves Rav Yosef / Rabbi Yitzhak alternative attribution, and separately records Rabbah bar Lima reporting Rav. Do not confuse Rabbah with Rava or a transmitter with the holder.
- 4a:9 preserves ordinary queen meaning versus received occurrence-specific dog interpretation. 4a:11’s return to prior answers is not assigned a unique unstated antecedent.
- 5a:3 preserves the actual `רבי שמעון (בן אלעזר)` reading. Any catalogue normalization requires an explicit owner-reviewed proposal, not silent harmonization.
- 6a:4 retains Rabbi Yohanan / Rabbi Elazar variant and treats quoted aggadic causation as source-reported, not externally verified fact.
- 6a:8 does not assign the two duplicate sources to cases by their order.
- 6b:16 records Abaye’s reply as conditional on Rabbi Zeira’s premise, not necessarily Abaye’s own theory.
- 6b:17–7a:2 is explicitly `לא פליגי`: Abaye and Rav Aha bar Jacob concern different firstborn cases, further qualified by known full gestation. Do not index it as an unresolved dispute.
- No cross-tractate equivalence was asserted. Possible thematic parallels (festival make-up periods, coercion, vowed/offered charity, firstborn year) should be routed to integration owners with exact evidence after their own source verification.

All source quotation spans, schema, links, ownership, primary character partition and replay were validated by the production runner. This is integrity validation, not independent scholarly certification. The Rav–Shmuel report was not modified.
