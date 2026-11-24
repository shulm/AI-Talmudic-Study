This is the separate P0–P1 source-feasibility track, not a scholar simulator or an evaluation dataset. Read ../SCHOLAR_AUDIT.md first.

From the repository root with Python 3.12+ and the original local Sefaria export mounted at the recorded paths:

```powershell
python -X utf8 research/individual_decision_model_2026-11-24/scholar/prepare.py
python -X utf8 research/individual_decision_model_2026-11-24/scholar/annotate.py
python -X utf8 research/individual_decision_model_2026-11-24/scholar/verify.py
```

Only standard-library modules are required. Scripts read the four committed indexes and original corpus without invoking historical builders. All writes are confined to this directory. `prepare.py` reproduces the frozen sampling and extracted evidence; `annotate.py` materializes hand-authored AI readings and Hebrew paraphrases; `verify.py` checks provenance and separation. Reproduction does not independently reproduce scholarly judgment.

`evidence_context.jsonl` preserves exact raw corpus excerpts and normalized reading text with original array indices and hashes. This is a bounded excerpt collection, not full tractate copies. Most attempts extract three complete amudim; RS17 extracts five and RS32 four to cover additional necessary boundaries. Extracted does not mean every unrelated segment was read. `evidence_records.jsonl` marks focal spans, qualifications, and attribution. `prediction_inputs.jsonl` contains only neutral input fields, with content-hashed alternatives sorted independently of scholar identity. No labels or source references are permitted there. Case IDs link via SHA256(attempt_id)[:16]; the evaluator may perform this join but a predictor must not receive the evidence files.

`initial_reviews_round1.jsonl` is the first saved AI review. `initial_reviews.jsonl` includes the same reader's subsequent RS32 boundary repair after reading Eruvin 41b:6–8. Neither is overwritten by reproduction. `second_review.jsonl` preserves a separately initiated, source-first AI review of all 32 attempts, frozen before comparing initial judgments. `INDEPENDENT_REVIEW.md` documents its scope. Current evidence is `ai_independent_double`, never human-reviewed. `review_disagreements.jsonl` records RS10/RS21 scope differences, RS32's initial missing boundary, and the source-adjudicated RS14 neutral-condition repair. Original neutral views are retained in `prediction_inputs_pre_second_review.jsonl`; use only current `prediction_inputs.jsonl` for future experiments. Both version-scope uncertainties and anonymous assignments remain unresolved.

Agreement denominators distinguish the original 30 attempts (eligibility 28/30; jointly named assignment 22/22), all 32 versus preserved round1 (29/32; 23/23), and all 32 after RS32's first-reader extension (30/32; 24/24). These are conditional AI agreement counts, not correctness rates, independent people, or evidence that family grouping is complete. The outcome remains PROVISIONAL_PENDING_REVIEW.

`pilot_selection.json` retains the full sorted candidate pools, seed and draw algorithm. Thirty original context-components were drawn before reading labels. Explicit answer-bearing overlaps merge RS09/RS10 and RS11/RS13. The next shuffled civil and festival candidates were appended as RS31 and RS32, leaving 32 attempts and 30 provisional families; failures are never silently replaced. No usable focal family repeats. Index-context components and subsequent manual merges are conservative leakage groups, not certified unique topics. Before any split, finish semantic parallel/version grouping across inventories.
