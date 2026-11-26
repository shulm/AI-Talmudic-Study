# L02 resumable partial production checkpoint

Update 2026-11-26: Bava Metzia has a newer targeted correction, snapshot
`1de0ef2ed8f9cd4fc22791162f92e7d59d276dc09dd9c50336dd8fe0a3940a92`.
See `bm001_scope_correction_receipt.json` and run
`python -X utf8 research/bavli_dataset_runs/run_20261125_01/lanes/L02/verify_bm001_correction.py`.
BM001-SCOPE adds explicit provisional combined-clause scope to claims 17/44/54
and updates dependent records, while retaining sight-nonacquisition as an
asserted separate principle. Fourteen supersessions preserve original judgments;
coverage remains 47 segments per pass. The independent verdict remains
`REWORK_TARGETED` pending exact-version re-review. The session receipt and frozen
package below remain unchanged historical artifacts, not pointers to this newer
Bava Metzia snapshot. Other tractate checkpoints are unchanged.

**The requested five-tractate assignment is not complete. No tractate is delivered.**
The frozen checkpoint has 310/13,669 original segments with recorded passes in each
of structure, utterances, claims, attributions, questions, positions, edges and
source-based reconciliation. The remaining 13,359 segments still need those passes.
Input/runtime readiness is verified; there is no missing-source or unavailable-API
blocker. The unfinished work is substantive source reading, annotation and review,
not something the mechanical replay can supply. This packet is a session handoff,
not a claim that production continues after the chat ends.

| Tractate | Denominator | Each required pass | Next unprocessed source |
|---|---:|---:|---|
| Bava Metzia | 3,660 | 47 | 3a:14; separately resume interior continuation at 23a:3 |
| Sanhedrin | 4,171 | 18 | 2b:3 |
| Gittin | 2,992 | 91 | 5b:9 |
| Sotah | 1,635 | 76 | 3b:11 |
| Keritot | 1,211 | 78 | 3b:10 |

These are source-segment counts, not record counts or scholarly accuracy measures.
Completed zero-findings passes, actual records, provisional interpretations and
independent review have distinct fields in `SESSION_CHECKPOINT.json` and exports.

## Contract and ownership

The coordinator pointer was read at coordination head
`f6b691011b88f0b7f1f7dd5dc8fc29cc4100fcc1`, assignment revision 3.
Run: `run_20261125_01`.
Contract SHA-256: `6e6f3bb4c0095a47cb7e5b07b1e296e76dd7d67fdbea34995054354c914c5174`.
Actual production commit: `15bba19d80273232b4554dfe507ceb37e97843a2`.
Schema: `43638e2127e40eeb33124f5e884c980bcf8bd7a6a84ba37896b1c8f65cd7f7aa`.
Protocol: `ee727cd4cb9f19f893a2d4f2232c7df0e9e323647d7336c6eae3edbc86b1ceb2`.

The immutable contract Git blob, working production files and their production
commit blobs were checked. All five named-edition originals and source schemas
were individually hashed. The L02 ZIP verifier passed for all 13,669 segments.
The assignment file's documented LF/CRLF metadata distinction was checked using
the shared verifier; no source bytes were normalized. The v2 semantic/QA text
matches commit `5876cb9dfd40dbadecb4a79273e59631fe1f127a` modulo checkout line endings.

Revision 3 recorded the prior lead `/root/lead_l02_l04` inactive. The user's L02
appointment and the common contract authorize same-lane worker handoffs. Each
existing job was handed off through the shared locked runner from epoch 1 to 2:

- Bava Metzia and Keritot: `/root/bava_metzia`.
- Sanhedrin and Sotah: `/root/sanhedrin`.
- Gittin: `/root/L02_gittin` (parent acting as producer).

One producer promotes each tractate. The global ledger, shared code/schema,
other lanes, source corpora and historical pilot files were not changed.
Lane receipts record the newer local epochs for coordinator reconciliation.
At resume, inspect current `OWNER.json`, `CURRENT.json` and the coordinator pointer
again; these frozen receipts must not override later work or a live owner.

## Preserved substance and limits

Bava Metzia's original 21a–22b pilot remains recoverable in its legacy archive.
The true opening checkpoint was resumed, not treated as covered by that island.
New evidence explicitly joins 22b:16's משום with 23a:1's דמדרסא and links the
legacy sugya. That boundary work does not cover the omitted bulk of the prefix
or suffix. Read the per-job receipt for exact migration/archive hashes.

Gittin retains the initial differences between Rabbah and Rava, then links the
4b qualification that Rabbah also accepts Rava's concern. The 5b:8 identification
of Rabbi Yohanan with two attendees was added after an independent source alert;
it is not scored as first-pass independent agreement. Rabbi Hanina's three is
marked as inference from the identified pair, not name order. The later
attribution supplements do not erase the initial local reading.

Sotah preserves competing transmission versions and the corrected report at
2b:26. Keritot preserves the pinned anomalous wording ועל אשת אחי אמו in 2a:1
and flags the resulting textual/counting issue without repairing the original.
Other open questions and boundaries remain in each export's `unresolved.json`.

## Review and qualification

Reviewer `/root/source_review` started with a fresh context and source-only
instructions. Frozen seed-20261125 plans use the common ten-segment grid. Plans
are not completed reviews. Source-first readings precede comparisons; context
extensions, random cores, endpoints and risk scopes are distinguished.

The first opening comparison contains 15 independently recorded Bava Metzia
core claim units and 41 Gittin core claim units, all represented at the compared
versions. This narrow 56-unit result is not an exhaustive omission audit,
accuracy estimate, full review or human certification. The exact comparison
ledger records post-alert additions and version carry-forward. Later review
checkpoints, if present, state their own scope and do not expand this denominator
silently. The final review checkpoint has 13 frozen readings, 129 unique core
segments and 382 validated evidence spans. Mandatory endpoint readings are
complete, but only two probability blocks are complete and 167 selected blocks
remain. The later Sotah/Keritot opening comparison brings the independently
recorded core-claim denominator to 128. All are represented, sometimes inside
composites; this does not establish exhaustive atomic extraction. The reviewer's
initial Keritot quote-anchor error and source-only correction are both preserved.
Full probability cohorts, risk checking, remaining comparisons and qualification
are unfinished. Every production record remains ML-ineligible. See
`review/REVIEW_ARTIFACT_MANIFEST.json`, frozen readings/comparison ledgers and
`remaining_source_review_001.json` for exact hashes and unfinished references.

## Frozen data and deterministic verification

`SESSION_CHECKPOINT.json` records each exact snapshot, ordered accepted proposal
hashes, unaccepted attempts, all export file hashes, per-layer coverage and next
source. `frozen/<job>/snapshot.json` is the authoritative bounded checkpoint;
`frozen/<job>/proposals/` contains its immutable accepted inputs. It includes
original judgments and revisions. Rejected attempts are separately preserved.
The Gittin middle-window first attempt reused one question ID; the runner rejected
it before promotion. A new attempt corrected the namespace. No semantic output
was silently overwritten.

Run from this checkout with Python, `jsonschema`, and the exact original source
files available outside Git:

```powershell
python -X utf8 research/bavli_dataset_runs/verify_active_run.py
python -X utf8 research/bavli_source_access_v1/source_packages.py --lane L02 --package F:/Sefaria_QA/bavli_source_packages_v1/L02.zip
python -X utf8 research/bavli_dataset_runs/run_20261125_01/lanes/L02/verify_checkpoint.py --source-root F:/Sefaria-Export-master
```

The last command hashes frozen artifacts, loads the original named sources,
replays every accepted proposal through the unchanged shared validator in memory,
and compares exact snapshot bytes and coverage. It makes no model calls, changes
no owners and does not promote data. The authoring scripts are historical
serialization aids, **not** the replay route; scripts reading current state must
not be rerun as if they were frozen attempts.

External live jobs are under
`F:/Sefaria_QA/bavli_production_run_20261125_01/L02/<job_id>`.
Each current immutable export is under `exports/L02_session_<snapshot-prefix>`;
its exact path and hashes are in the checkpoint receipt. Exports contain typed
tables, per-sugya views, coverage, qualification and unresolved cases.
For a live job, use the common `runner.py replay`, then `packet` and new immutable
`submit` proposals under its verified owner/epoch. Same-lane reassignment must
use `handoff`; do not reset a job or skip a hole in its coverage matrix.

No new metered external model calls were used. Token/cost totals are unknown.
No full original source inventory or corpus copy is committed. Bounded source
evidence retains Wikisource/Sefaria provenance and the recorded CC-BY-SA label
without inventing a license version. Draft work must remain unmerged.
