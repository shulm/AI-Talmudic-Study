# L04 exact-version partial production checkpoint

Checkpoint 001 contains actual semantic annotations and preserved review evidence for **460 of 13,593 source segments**. **Zero of seven tractates are delivered.** Required extraction and independent review remain incomplete; all machine-learning and human-certification eligibility remains false. This is a resumable draft, not acceptance of the lane assignment.

The authoritative selection of package versions is [LANE_CHECKPOINT_001.json](LANE_CHECKPOINT_001.json). Later production may advance beyond these immutable packages.

| Tractate | Covered in each of eight layers | Denominator | Next source |
|---|---:|---:|---|
| Taanit | 118 | 895 | 6a:2 |
| Bava Batra | 142 | 3,804 | 7a:5 |
| Pesachim | 71 | 3,519 | 4b:8 |
| Avodah Zarah | 60 | 2,131 | 4a:4 |
| Nedarim | 22 | 1,509 | 3a:5 |
| Moed Katan | 17 | 1,026 | 2b:3 |
| Makkot | 30 | 709 | 3a:8 |

Coverage means the producer recorded a source pass for structure, utterances, claims, attribution/transmission, questions, positions, edges, and reconciliation. It does not establish exhaustive recall or scholarly correctness. Reconciliation can correctly have zero records while retaining a source-reread rationale. Tables preserve superseded records; consumers must filter `release_state == "valid"` for the current graph. Per-sugya exports use segment-overlap context, not certified semantic containment.

## Exact inputs and ownership

The active coordinator pointer and nine implementation file hashes were verified against production commit `15bba19d80273232b4554dfe507ceb37e97843a2`; the immutable run contract SHA-256 is `6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174`. Schema SHA-256 is `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa`; protocol SHA-256 is `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2`. See [readiness evidence](READ_ONLY_READINESS_AUDIT.json).

Each package includes the exact source hash, edition metadata, source-manifest references, owner, snapshot, and accepted proposal chain. Original edition: Wikisource Talmud Bavli, Hebrew, from the pinned Sefaria export. The source metadata declares CC-BY-SA and retains source/version credits; no unverified license version is asserted. Original corpora and full source inventories remain external.

All seven external jobs use owner `L04/<slug>_resume_20261126`, epoch 3. [Dispatch receipt 001](DISPATCH_RECEIPT_001.json) and [receipt 002](DISPATCH_RECEIPT_002.json) preserve the within-lane handoffs; the global ledger was not edited. Only one producer promotes each tractate. Read the external OWNER and CURRENT files before further dispatch; this document is not a lease for a second writer.

## Review and qualification

[Frozen review capture](reviews/capture_001/MANIFEST.json) preserves source readings, comparisons, correction checks, and their exact versions. Probability samples, endpoint samples, and continuation context are separately recorded. An independent reading of source not yet produced is pending comparison, not an omission failure. A correction check is not a fresh random sample and is not full-tractate acceptance.

Taanit review corrected rejected-position statuses and biblical speaker/holder projections. Moed Katan review corrected Rav Huna's replaced identification and added the explicit replacement edge. Makkot review separated Ulla's initial question from anonymous clarification. Broad opening utterances in Nedarim, Moed Katan, and Makkot were qualified as composite; selected named speeches were narrowed. A subsequent mechanical repair updated attribution scopes to successor IDs, with independent equivalence checking. Initial findings and superseded versions remain preserved.

Avodah Zarah's opening ten source segments were compared against the 60-segment checkpoint: all 21 independently identified claims were represented. Its 70 independently read core segments include 60 probability-sample segments mostly beyond produced scope; this does not mean 70 produced segments passed comparison. The review checkpoint lists the remaining blocks. Other comparison files similarly identify their exact scope and version; do not project acceptance onto later additions.

The production runner deliberately leaves qualification unreviewed and does not implement automatic review acceptance. Remaining work includes full source coverage, completion of frozen probability/endpoint and risk reviews, resolving or qualifying disagreements, and task-specific qualification. Composite utterance boundaries and bundled claims are not eligible as certified atomic examples. Avodah Zarah also retains explicitly linked open structural continuations.

## Reproduce and resume

Use Python with `jsonschema`, the pinned common runner in this repository, and the exact original source tree. From repository root:

On Windows, Git operations on the hash-addressed package paths may require `git -c core.longpaths=true ...`. The lane's `.gitattributes` preserves exact artifact bytes, including inherited line endings, because the manifests hash those bytes.

```powershell
python -X utf8 research/bavli_dataset_runs/run_20261125_01/lanes/L04/resume_20261126/verify_packages.py --source-root F:/Sefaria-Export-master
```

This verifies package hashes, named-edition source/schema hashes, every accepted proposal by deterministic replay, active attribution scope references, and every exported byte/file. It reads the originals without changing them. Engineering checks do not certify scholarly accuracy. Each `PACKAGE.json` binds the job snapshot, proposal chain, exports, qualification, unresolved cases, per-layer coverage, and next source.

Resume the authoritative external jobs under `F:/Sefaria_QA/bavli_production_run_20261125_01/L04/bavli_<slug>`, after verifying current authority and comparing CURRENT with this checkpoint. Keep the common runner unchanged. Read the next source and its continuation, author explicit evidence-backed proposals, submit with the recorded owner/epoch, and replay/export. Do not rerun state-dependent authoring scripts against a changed CURRENT to reproduce historical work; use the immutable accepted proposals instead. Further corrections require supersession and dependent graph/coverage revisions, including exact-ID attribution scopes.

The repository stores bounded annotations and review evidence. Full source-package transfer, if needed on another machine, must follow the coordinator's authorized L04 package descriptor. Available telemetry records zero new metered API calls; token and cost totals are unknown. No merge is authorized or performed.
