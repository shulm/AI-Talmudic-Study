# Frozen source-only review preparation

This is infrastructure preparation, **not completed independent semantic review**.
All 37 original sources and their original source schemas passed byte SHA-256
checks against `jobs.json`. The exact active-run contract, production protocol,
output schema, source manifest and contract-listed tooling hashes passed.
Every existing review plan was reproduced byte-for-byte using the existing
`make_review_plan.py`, seed **20261125**, block size 10, with no reroll.
Producer annotations were not inspected by this preparation process.

| Cohort | Blocks | Nonempty source core segments |
| --- | ---: | ---: |
| Probability sample | 1,205 | 12,006 |
| Mandatory endpoints, including overlap | 74 | 563 |
| Endpoint overlap with probability sample | 18 | 136 |
| Additional endpoints | 56 | 427 |
| Unique probability/endpoint union | 1,261 | 12,433 |

All 12,433 selected source cores remain pending semantic reading at this
immutable checkpoint. The full source inventory contains 81,793 nonempty
segments in 37 tractates. These counts describe source segments, not sugyot,
claims, accuracy rates, or extraction completion. No risk cohort has yet been
selected or reviewed here. Context expansions are not counted as sampled cores.

Start with `RESUME_CHECKPOINT.json`, then verify the hash-bound
`verification_results.json`, `inventory.json` and `pending_queue.json`.
The queue follows the original jobs' queue priority, then source block order.
All selected block IDs, roles and exact core references appear in the queue and
per-job descriptors. Original frozen plans are copied unchanged under
`frozen_plans/`. Their byte hashes and domain-separated plan hashes remain
distinct and are both recorded.

Dispatch only `jobs/<job_id>.json` and its source-only dependencies to a fresh
reader context. The descriptor identifies the original source absolute path and
hash, frozen plan absolute path and hash, selected cohorts, and the three common
documents under `source_only_common/`. It includes no producer examples or
annotations. Readers must expand original context to complete discussions and
freeze substantive exact-source findings before viewing corresponding producer
output. The receipt protocol's provenance requirements still apply; these files
are not review receipts.

Revalidate in place with:

```powershell
python -B -X utf8 'C:/Users/David/Documents/ChatGPT/AI Talmudic Study/research/bavli_dataset_runs/run_20261125_01/review_lead_20261126/verify_prepare.py'
```

The script reads the authoritative coordination checkout and original corpus.
It writes only within this directory, refuses to replace differing existing
bytes, and disables imported Python bytecode writes. It reproduces the complete
preparation deterministically. Subsequent readers must preserve this initial
queue and use a separate append-only progress ledger for actual frozen reading
hashes, context expansions, comparisons, disagreements and adjudications.
No full-tractate acceptance, human certification, or ML eligibility is claimed.
