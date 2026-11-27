# Inherited Berakhot continuation preservation audit

Audit date: 2026-11-25. This is an integrity and resumability audit, not a new semantic production run or expert certification.

## Preservation and ownership evidence

Original worktree: `F:/Sefaria_QA/worktrees/bavli-sugya-continuation-pr10`, branch `research/bavli-sugya-continuation-pr10`, HEAD `1b9741601cd27a8e1d8b25638af379d4d5117f00`, based on reviewed pilot `ef29310b50575ac2441ce59d0c68d58424f4b823`. HEAD author/committer is David Shulman; commit covers through 6a. Later dirty work includes blocks 003–005 through 9a and updated engine, data, ledgers, and reader. The status inventory is recorded in `snapshot_manifest.json`. Branch/commit authorship does not establish which live agent currently owns the tractate; coordinator must reconcile active owner/epoch before dispatch.

88 files, including all relevant dirty/untracked project files and AGENTS.md/AGENT_HANDOFF.md, were copied byte-for-byte to `F:/Sefaria_QA/bavli_inherited_snapshot_v1`. The snapshot excludes caches and full source corpus copies. Existing differing files would abort instead of being overwritten. Snapshot manifest SHA-256: `e08e8ed46e08eaa450ca3430b4bc9c962f5189c508033999b6ee5dafe6ef1ad8`. Original file hashes were checked again after testing and remain identical. No original-worktree writers or commits were run. All tests ran on a separate temporary copy of the snapshot.

## Independently executed mechanical checks

- All 37 original Wikisource tractate source-file hashes and pinned TOC hash match the inherited source manifest.
- All 450 core + 72 context records exactly match original source array strings, indices and their text hashes.
- All 12 packet/proposal/review hashes across four continuation blocks match the ledger. These are **canonical JSON hashes** (`json.dumps(value, ensure_ascii=False, sort_keys=True)` UTF-8), not raw file hashes. Raw file hashes are separately preserved in the snapshot manifest.
- `validate.py`: passes schema, source fidelity, references, evidence offsets, coverage and lineage checks.
- `verify_manifest.py`: passes published artifact hash checks.
- `test_reproduction.py`: all 21 expected outputs reproduced byte-for-byte from frozen pilot and four continuation block artifacts. This is deterministic replay, not semantic regeneration.
- `test_continuation.py`: all 7 invariants pass, including inherited tails, interrupted-write rollback, rejection of partial review overclaim, preservation of unaffected records/lineage, idempotency, conflicting proposal rejection, and changed-source rejection.
- `node exports/verify_reader.cjs`: passes. No Rav–Shmuel report changes were made.

Exact command outputs are in `verification.json`.

## Coverage and safe resume

Berakhot has 386/2749 processed segments (2a:1–9a:29), 71 primary sugyot. Last closed ref is 9a:28. Next core starts at **Berakhot 9b:1**, carrying inherited B71 (`sug_bb0081dd21382f865f03`) at 9a:29, which ends mid-sentence at `שלא יאמר`. Preserve its ID, evidence, and initial judgment. The source continuation starts `אותו צדיק`; inherited context already contains 9b. Do not restart from 6b or silently overwrite dirty later blocks.

B32 retains origin block 002 and was extended in block 003 to 6b:1; B63 retains origin block 004 and was extended in block 005 through 8b:7. Prior versions are archived in revisions_ledger.jsonl. Bava Metzia's independent partial pilot (64 segments, open M01/M05) remains separate.

Full corpus totals: 450 processed segments, 76 primary + 12 sub-sugyot, 309 selected statements, 52 questions, 94 positions, 250 open review items. 153 segments explicitly defer question/answer extraction. Zero complete tractates; semantic_completeness_pass=false; expansion_gate_pass=false; ml_eligible_records=0. Thus structural coverage must not be reported as completed semantic dataset coverage.

Frozen initial proposals and independent source review JSONs are retained. Recorded boundary disagreements at 6b:20|21, 7a:29|30, 8a:4|5 and 8b:14|15 remain explicit. Block 005 comparison records that the independent reviewer delivered its JSON before quota failure and the file was extracted verbatim from its conversation log. This audit verifies the frozen file and ledger hash, not that external conversation provenance claim or reviewer independence.

## Coordinator action and blockers

Adopt the preserved later state as the Berakhot inheritance baseline, subject to owner/epoch reconciliation, and port it via explicit schema migration into the production runner. The old engine's successful replay proves structural continuity; it does not satisfy full semantic production. Preserve original data and revisions separately when migrating. Any semantic completion pass must cover deferred layers and retain existing uncertainty. No new Berakhot job was started by this audit.

Remaining blockers to a claim of full production readiness: live owner confirmation, implemented/approved semantic schema migration, full-layer semantic proposals/review, and 2363 remaining Berakhot source segments plus deferred layers in already processed segments. Source access and inherited mechanical integrity are verified locally.
