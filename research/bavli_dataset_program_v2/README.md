# Bavli research dataset — parallel production program v2

Prepared 2026-11-25 for `shulm/AI-Talmudic-Study`.

**Status: reviewed production design, executable queue builder and source-only review-plan builder. This package is not a completed corpus, a running agent service, or an annotation-model executor.**

## Start here

Give **`MASTER_AGENT_PROMPT.md` to one lead agent** that can access the repository, the pinned source export, and your available worker agents. The lead owns the full queue and launches whole-masechta assignments. You do not need to issue a new prompt for every daf or every completed tractate.

The production unit is one whole masechta. Several units run concurrently. Each active unit has one accountable producer and a separate reviewer assignment. Shared tooling has one owner. A single integrator assembles release manifests from immutable tractate artifacts.

The first production wave is **Berakhot, Bava Metzia, Rosh Hashanah, and Taanit**, subject to actual simultaneous capacity. These are a proposed operating order, not a claim that any of them has started. Berakhot and Bava Metzia inherit pilot material; the latter pilot is in the middle of its tractate, so the beginning must also be processed.

## Package contents

| File | Purpose |
| --- | --- |
| `MASTER_AGENT_PROMPT.md` | One lead-agent assignment covering setup, parallel production, rolling review, and continuation |
| `TRACTATE_WORKER_PROMPT.md` | Reusable whole-masechta production contract |
| `INDEPENDENT_REVIEW_PROMPT.md` | Source-first independent reading, comparison, and exact-artifact verdict |
| `SCHEMA_AND_RESEARCH_VIEWS.md` | Rich reusable core, additive qualifications, schema migration, derived research views |
| `QA_AND_RELEASE.md` | Coverage, review denominators, scoped blockers, leakage, and release policy |
| `REVIEW_OF_PREVIOUS_HANDOFF.md` | What to preserve and what to change in the supplied handoff |
| `ENGINEERING_NEXT.md` | Concrete next implementation work against the inspected pilot code |
| `jobs.json` | Source-derived inventory queue; queued jobs are not running jobs |
| `RUN_STATE_TEMPLATE.json` | Runtime ownership/checkpoint template; contains no active assignments |
| `tools/build_jobs.py` | Deterministically rebuild the queue from the pinned manifests |
| `tools/make_review_plan.py` | Build a source-only probability sample after verifying an exact source file |
| `tools/test_*.py` | Focused integrity tests for the two delivered tools |
| `SOURCES.md` | Inspection scope, pinned repository evidence, and official source-license guidance |
| `VALIDATION_REPORT.json` | Checks actually performed on this package |

## Verified starting point

The production base inspected on 2026-11-25 is draft PR #10, branch `codex/bavli-sugya-corpus-v1`, commit `ef29310b50575ac2441ce59d0c68d58424f4b823`. Its named source is **Wikisource Talmud Bavli**. The source inventory contains **37 tractates and 81,793 source segments**; in this snapshot the nonempty denominator is also 81,793. The byte-exact `source_manifest.json` SHA-256 is `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c`.

The existing semantic pilot contains 215 segments: Berakhot 151/2,749 and Bava Metzia 64/3,660. The recorded output has 29 primary sugyot, 6 sub-sugyot, 231 discourse units, 52 questions, 94 provisional positions, and 39 open review entries. **No entire masechta is complete.** Those are the pinned pilot's reported/manifest counts, not new annotation output from this package.

PR #11 is a separate draft at `9a9dfad93675b984b8223ba065732599a973f074`, using a different named edition and incompatible identifiers. Use its methodology only as a separately identified reference. Do not mix its source strings, offsets, or semantic records into PR #10.

## Proposed capacity allocation

For an external pool of twelve simultaneous agent slots, start with one coordinator/integrator, one shared tooling owner, four whole-masechta producers, four independent reviewers, one adjudicator, and one cross-tractate enrichment worker. When fewer slots are available, combine compatible operational roles and time-share reviewers; preserve independent reading contexts. When more slots are available, add production/review pairs or independent extraction of high-value layers.

This is a resource allocation, not a speed guarantee. Measure reviewed semantic coverage per elapsed hour and use the review backlog to decide where to add capacity. An agent specification does not mean an agent has been launched.

## Run the tools

The queue builder is deliberately pinned to the historical PR #10 manifest bytes. It recreates static specifications, not current runtime progress. Later accepted continuations belong in the separate runtime ledger; a changed source baseline requires an explicitly updated queue/tool version. The writer accepts an identical existing artifact and refuses to replace different bytes.

From the repository root after checking out a branch containing this package and the PR #10 base:

```bash
python research/bavli_dataset_program_v2/tools/build_jobs.py --manifest research/bavli_sugya_corpus_v1/source_manifest.json --progress research/bavli_sugya_corpus_v1/progress_manifest.json --output research/bavli_dataset_program_v2/jobs.json
python -m unittest discover -s research/bavli_dataset_program_v2/tools -p 'test_*.py'
```

Review-plan invocation, after resolving the source path from the selected job:

```bash
python research/bavli_dataset_program_v2/tools/make_review_plan.py --source "/absolute/path/to/the/pinned/Berakhot/Hebrew/Wikisource Talmud Bavli.json" --tractate Berakhot --expected-sha256 dd24d48aef18159564471380f7ba200302cc9889b22380aef724d2fb086a9d38 --seed 20261125 --output "/absolute/path/to/private_review/berakhot_plan.json"
```

The plan contains source coordinates and hashes, not annotations. A fresh reviewer must still read the pinned source and freeze its independent readings. Store review plans outside the producer's input path until the corresponding first-pass proposals are frozen.

## Completion means several separately reported things

Report source coverage, structural coverage, each semantic layer's extraction coverage, independent review coverage, and each downstream task's eligible-record count separately. A finished source pass does not imply a finished argument graph; an AI-reviewed sample does not certify an entire tractate; a valid retrieval record need not be eligible for scholar-choice prediction.

Publish useful provisional tractate packages as they pass their declared gates. Continue with the next queued tractate while supported unresolved interpretations remain visible with restricted task eligibility. Quarantine unsupported resolutions or corrupted records, and preserve all initial proposals.

## Authority and limits

The user's current instruction authorizes substantial dataset preparation using available agents and permits a public repository. The repository is already public. Routine internal batching, worker assignment, ordinary corrections, and advancement through the queue do not require repeated user approval.

This instruction does not supply a new metered vendor API budget. The example inherited budget remains USD 0 for **new external paid calls**, while already available agent resources may be used. Keep unavailable usage measurements null rather than inventing them. Dataset preparation does not require model training.

Preserve source corpora, historical pilot files, existing studies, and current visibility. Work in isolated branches and open draft PRs; do not merge without an owner instruction. Follow the repository's prohibition on committing full source-corpus copies. Public text-containing artifacts require their own recorded source terms and attribution. See `SOURCES.md` and `QA_AND_RELEASE.md`.

## What this package has not done

It has not produced a new whole-masechta annotation, performed a new blind scholarly reading, launched a persistent production service, called a paid model API, trained a model, or revalidated the complete original source corpus. The full pinned source export is needed on the execution machine. The next lead's concrete deliverable is completed tractate data with review evidence, not another plan-only handoff.
