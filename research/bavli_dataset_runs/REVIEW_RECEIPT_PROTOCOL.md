# Exact-version integration review receipts

`integrate_run.py` is coordinator integration tooling, separate from the frozen
producer implementation. Its file hash is recorded in each release index.
Adding this integration gate does not change proposal/schema/protocol hashes or
invalidate unrelated worker epochs. Six focused tests exercise its missing
receipt, missing sampled scope, missing risk coverage, corrupt evidence, complete
receipt, and exact missing-range behavior.

The producer runner's conservative `tractate_delivered=false` is not the final
integration decision. Integration requires all eight extraction passes over the
entire pinned tractate, no unresolved structural tail or quarantined records, and
a separately admitted full independent-review receipt. Every current partial
snapshot reports unfulfilled gates honestly.

For a full tractate review, the coordinator admits
`<run>/review/<job_id>/<snapshot_sha256>.json` with:

- `snapshot_sha256`, `source_sha256`, `plan_file_sha256` binding the exact production
  version, source and frozen source-coordinate plan.
- `review_kind: independent_ai_source_first` and `initial_readings`, each containing
  a run-relative `path` and file-byte `sha256`.
- `comparison: {path, sha256}` and `verdict: ACCEPT_PROVISIONAL_TRACTATE`.

Each initial-reading artifact declares its source hash, actual execution identity
and route, `frozen_before_comparison: true`, `producer_labels_exposed: false`,
`core_refs`, separate context, and substantive `findings`. Every finding has an
`interpretation` and exact original `evidence` entries (`ref`, `start_char`,
`end_char`, `quote`). Integration checks evidence slices against the pinned source.
The union of actually read cores must include every probability/endpoint reference
in the frozen plan. Generated plans are not readings.

The comparison binds the same snapshot and ordered `initial_reading_hashes`,
declares `omission_pass_performed: true`, lists `reviewed_risk_record_ids`, and
reports `unresolved_integrity_critical_count`. Every active uncertainty/open-boundary
record requires risk review. Actual independent execution and honest source-first
provenance remain methodological obligations; a schema cannot prove that an agent
read a passage. No receipt confers human certification or ML eligibility.

The targeted bootstrap and opening-block readings in this run are deliberately
not written into the full-tractate receipt namespace. Their individual scopes,
disagreements and corrections remain available for later source-based review.

`QUARANTINE.json` excludes exact record hashes and their graph dependents from an
integrated release. Initial producer rows and proposals remain intact. A scope
note cannot cure a known incorrect typed role. Exports from a raw producer job
must be interpreted together with this overlay; they are not independently
qualified release tables.
