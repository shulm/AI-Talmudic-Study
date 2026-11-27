# Bavli rolling partial release — 20261127_02, review015

**Partial required work remains.** This frozen assembly records **10,519 / 81,793 source segments per each of eight required passes**, leaving **71,274 per pass**. It includes **84,263 provisional records**, preserves **85,429 record versions**, and excludes **21 records** (14 exact direct exclusions and seven dependent records). **0/37 tractates are fully admitted; supervised eligibility is zero.** Completed-pass counts describe recorded production, not certified scholarly completeness.

## Authoritative contract and exact versions

The run remains `run_20261125_01`, governed by the coordinator's existing [active-run pointer](../../ACTIVE_RUN.json) and [run contract](../RUN_CONTRACT.json). Production commit: `15bba19d80273232b4554dfe507ceb37e97843a2`. Coordinator ledger revision6 was published at `f8e7dc1718340be82d68613e6eb5d028e1ed2c59`; the immutable capture retains ledger5 and verifies all later within-lane ownership histories. No producer owner, epoch or cross-lane assignment was changed.

| Artifact | SHA-256 |
|---|---|
| Run contract | `6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174` |
| Schema | `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa` |
| Protocol | `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2` |
| Source manifest | `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c` |
| [Input manifest](../integration_20261127_02_review015/INPUT_MANIFEST.json) | `df1922be89b1869d3b9070496a113fbeaa3e65cc5faa5ebc3e36d00e3c6a606b` |
| [Current policy](../integration_20261127_02_review015/POLICY_MANIFEST.json) | `aaed2943b574ef52a86c348763d54cba96378737b5ee7a6a8d2863ac2aae5e45` |
| [Output manifest](assembled_20261127_02_review015/OUTPUT_MANIFEST.json) | `39bc9644b33c8bc8460d6d4ed30418f2064efd2e865fe5f15ee17ab9c02ca658` |
| Review delivery015 | `f35186b4e6a6bc63ee41cbd36029bb2f026d4fb928b67147073bde793ee78459` |

All six lanes have verified local source access at `F:/Sefaria-Export-master`; their source packages and hashes are documented in [source access instructions](../../../bavli_source_access_v1/README.md). Remote transfers are not established. Full source copies remain outside Git. All six lanes may continue under their existing delegated ownership when actual execution/review capacity is available; this release does not reset later checkpoints.

| Lane | Captured segments per pass | Source denominator |
|---|---:|---:|
| L01 | 3,641 | 13,657 |
| L02 | 413 | 13,669 |
| L03 | 471 | 13,635 |
| L04 | 3,265 | 13,593 |
| L05 | 422 | 13,598 |
| L06 | 2,307 | 13,641 |

## Outputs and qualifications

[Normalized tables](assembled_20261127_02_review015/tables/), the [1,582 per-sugya exports](assembled_20261127_02_review015/per_sugya/INDEX.json), and the [Hebrew evidence reader](assembled_20261127_02_review015/reader.html) retain source occurrences and separate evidence from annotation. Per-sugya membership is contextual source overlap, not an inferred semantic edge or unique ownership. Download the HTML to view it locally.

The [coverage matrix](assembled_20261127_02_review015/coverage_matrix.json) records every missing interval by pass. [Exact remaining jobs and resume instructions](REMAINING_INTEGRATION_20261127_02.md) cover all 37 tractates. Histories, supersession, uncertainty, exclusions and qualification ledgers remain separate. Surface mentions, identity candidates and transmission roles are preserved; no name-based entity merges or unverified parallel families were created.

The [review context](assembled_20261127_02_review015/REVIEW_CONTEXT.json) preserves probability, endpoint, supplemental and inherited provenance. Root direct reading remains 1,477 cores; the declared reading union is 2,118. Root-led historical comparison covers 880 coordinates; 90 separately attributed external comparisons bring that union to 970. These are historical exact-version scopes, not approval of this later production capture. All full-review flags remain false. Mandatory reviewer corrections and initial judgments remain available.

[Correction requests](CORRECTION_REQUESTS_20261127_02_REVIEW015.json) name exact records, hashes and source references. Chullin's addressee-role defect, Chagigah condition/status defects, and the reviewed Taanit/Nedarim/Makkot defects are excluded with dependency closure. Supported statements and uncertainty remain. Missing edges, questions, occurrences and speaker annotations stay visible as required rework. The [initial audit](../integration_20261127_02_review015/exclusion_audit.json) and [review015 impact](../integration_20261127_02_review015/review015_impact.json) preserve the withdrawn Nedarim P04 and mandatory Makkot context/chronology addendum.

The original policy014 capture is preserved as historical input. Its local generated assembly is superseded for current use by review015. Later Tamid work and L04 corrective rechecks belong to the next version; they do not silently alter this capture or lift its exclusions.

No supervised dataset is exported. Family grouping, overlapping evidence, derivatives, input cutoffs and leakage through summaries, titles, rationales, continuations and retrieval must be frozen and checked before task eligibility. Unknown pretraining exposure remains separate. Optional enrichment and future adapters do not block core delivery.

## Verification and reconstruction

All 37 jobs passed source/schema/protocol checks, ownership-history validation and deterministic proposal replay. Two independent final builds reproduced all 1,606 output files byte-for-byte; all 1,605 manifest entries passed hash/size checks. See [build evidence](ASSEMBLY_BUILD_VALIDATION_20261127_02_REVIEW015.json) and [export audit](ASSEMBLY_EXPORT_AUDIT_20261127_02_REVIEW015.json). These checks do not establish scholarly completeness or human certification.

From repository root, with Python and `jsonschema`, reconstruct into a new external directory:

```powershell
python -X utf8 research/bavli_dataset_runs/verify_active_run.py
python -X utf8 research/bavli_integration_release_v1/assemble.py --input research/bavli_dataset_runs/run_20261125_01/integration_20261127_02_review015 --output F:/Sefaria_QA/bavli_release_review015_REBUILD_NEW --source-root F:/Sefaria-Export-master
```

Compare the resulting output manifest with the hash above. Existing outputs must already match exactly; never edit generated aggregates or overwrite live producer checkpoints. Source licenses/edition metadata are retained in `SOURCE_LICENSES.json` and the source-access documentation.

## Publication and remaining work

This rolling snapshot belongs to [draft PR30](https://github.com/shulm/AI-Talmudic-Study/pull/30), branch `codex/bavli-integration-release-20261126`. Keep it unmerged. It is not a final complete release candidate.

Required production and independent review remain unfinished across all 37 jobs. Several lane/review agents reported usage-limit interruptions; exact checkpoint/resume artifacts are retained. Available lanes received bounded continuation requests, including untouched-job production and source-only review. A dispatch is not completion, and no unattended completion is promised. Resume current owners, resolve exact correction requests, complete missing passes and review cohorts, and publish a new immutable version.
