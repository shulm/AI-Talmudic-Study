# Bavli rolling integration — partial release 20261126_01

**Partial research assembly, not a completed corpus or full release candidate.** All 37 tractates remain incomplete. The frozen capture covers **2,450 / 81,793 segments per required extraction pass**, leaving **79,343 per pass**. It includes **19,128 provisional records**, preserves **20,060 record versions**, and excludes **one exact unsupported attribution**. Full-tractate admissions and task-qualified records both remain zero.

## Contract and exact artifacts

The authoritative run remains `run_20261125_01` on `dataset/bavli-coordination-v1`, ledger revision 5 at `d7637a9`. No second active-run pointer was created. Production code is `15bba19d80273232b4554dfe507ceb37e97843a2`.

| Artifact | SHA-256 |
|---|---|
| Run contract | `6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174` |
| Production schema | `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa` |
| Annotation protocol | `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2` |
| Source manifest | `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c` |
| [Input manifest](../integration_20261126_01/INPUT_MANIFEST.json) | `ebe2f6ff56cd789a3e6df016d6ec404e153313e654d43e69554c5ab6c4e7087c` |
| [Policy manifest](../integration_20261126_01/POLICY_MANIFEST.json) | `dab9cbceaca6a8b032af672e7560b98f3618cf9448ce83596094ae53fae6aa8c` |
| [Output manifest](assembled_20261126_01/OUTPUT_MANIFEST.json) | `451bb168a0020b70c8708222d88e98448baa832276ba1d613602aa679afa416c` |

`capture.py` locked each job, validated approved source/schema/protocol and historical ownership, replayed every accepted proposal, and saved exact immutable inputs. This is a set of per-job versions, not a simultaneous wall-clock snapshot. Later live production must not be silently substituted. The coordinator reconciled within-lane epochs without changing producer state or transferring jobs across lanes.

## Outputs

- [Normalized core tables](assembled_20261126_01/tables/) retain job/native-ID composite keys, exact spans, conditions, attribution candidates, transmission roles, questions, scoped positions and directed relations.
- [Coverage matrix](assembled_20261126_01/coverage_matrix.json) lists each required pass and every missing interval. [Remaining work](REMAINING_INTEGRATION_20261126_01.md) lists all 37 jobs and next coordinates.
- [Review matrix](assembled_20261126_01/review_matrix.json) and [review context](assembled_20261126_01/REVIEW_CONTEXT.json) distinguish reading, comparison, probability, endpoint and risk cohorts. Preserved checkpoint003 reports 180 directly dispatched reading cores, 92 directly compared cores and a 694-core combined declared-reading union with inherited-provenance limits. These are not 694 semantically certified passages or full review of this later production capture.
- [Per-sugya index](assembled_20261126_01/per_sugya/INDEX.json) links contextual views. Segment overlap is not semantic attachment or unique ownership.
- [Read-only Hebrew evidence reader](assembled_20261126_01/reader.html) displays bounded quotations separately from annotation content. Download/open locally if GitHub does not render HTML.
- `history/records.jsonl` and `history/supersession.jsonl` preserve original judgments and revisions. `unresolved_ledger.jsonl`, `exclusion_ledger.jsonl` and `qualification_ledger.jsonl` retain uncertainty, exclusions and restrictions.
- `entity_mentions.jsonl` preserves every occurrence, surface, role and identity candidate. No people were merged by spelling; no global equivalence families were inferred without evidence. Raw link proposals remain typed. Similar topics are not independent-decision families.

Chullin `ch01_a_ashi_addressee` is excluded by exact record hash because an addressee was typed as quoted authority. Its original evidence stays in history. Transitive dependency exclusion is implemented; this capture has no additional dependent exclusions. Superseded Taanit/Chullin/Rosh Hashanah defects are not automatically attributed to replacements. Replacement review remains separate. The saved nonblind integration audit is advisory evidence, not human certification or a completed independent integration audit.

## Validation and reconstruction

[Validation receipt](ASSEMBLY_VALIDATION_20261126_01.json) records verification of 350 generated files, unique keys, foreign-key closure, quarantine exclusion and byte-identical reconstruction in a second external directory. Four tests cover exact-version/dependency exclusion, non-prefix gaps, ID/path safety and tampered inputs. Every job passed original-source checks and proposal replay in both builds. These checks do not prove scholarly completeness.

Run from repository root with Python 3.11+ and `jsonschema`:

```powershell
python -X utf8 research/bavli_dataset_runs/verify_active_run.py
python -X utf8 -m unittest discover -s research/bavli_integration_release_v1 -p test_assemble.py -v
python -X utf8 research/bavli_integration_release_v1/assemble.py --input research/bavli_dataset_runs/run_20261125_01/integration_20261126_01 --output F:/Sefaria_QA/bavli_release_rebuild_NEW --source-root F:/Sefaria-Export-master
```

Use a new external output path or an already-identical output. Never edit generated aggregates. [Source access instructions](../../../bavli_source_access_v1/README.md) provide packages and verification commands. Complete source copies stay outside Git. `SOURCE_LICENSES.json` retains source-specific attribution/license metadata; public repository publication does not invent a license for third-party sources.

`SUPERVISED_EXPORT_POLICY.json` blocks supervised exports until task population, labels, input recipe, cutoff, family grouping and exact-version qualification are frozen. It requires grouping source overlap and derivatives, and checking titles, rationales, summaries, continuations, aliases and retrieval for answer leakage. Unknown pretraining exposure stays separate. Optional enrichment and future adapters do not block core delivery.

## Capacity and unfinished work

All six lane leads were explicitly asked to continue actual production and resolve exact review findings. Subsequent snapshots exist beyond this capture; preserve them for the next release. Three integration subagents hit service usage limits after saving artifacts. The coordinator inspected/completed assembly code and performed mechanical validation directly. Full incoming-export package audit was unfinished; no unchecked incoming export files were reused. Six bounded lane metadata receipts are preserved in `integration_20261126_01/lane_deliveries/`; assembly inputs are independently replay-verified proposal chains.

Review capacity also hit usage limits and later partly resumed. Capacity changes do not establish completed review. Required production and full review remain unfinished for all 37 jobs. Resume from the current lane owners and latest valid checkpoints; never reset later production to this capture. Keep draft PRs unmerged and do not assume unattended background execution.
