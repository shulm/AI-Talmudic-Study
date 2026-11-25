# Engineering next steps: verified pilot limitations

Inspection target: PR #10 commit `ef29310b50575ac2441ce59d0c68d58424f4b823`, files under `research/bavli_sugya_corpus_v1/`. This is a source-code inspection, not successful execution of a full-tractate pipeline.

1. **Parameterize source extraction and preserve the approved source pin.** `pipeline.py` defines `PILOTS` for Berakhot and Bava Metzia; `extract()` skips every other tractate and uses those fixed page ranges. Its CLI provides `build` and `show`, with no full-tractate production command. `build()` calls `inventory()` and recomputes the expected hashes from its current inputs. Production must instead verify original bytes against the approved manifest; creating a new source inventory must be a separate explicit operation. Preserve source identifiers and separate core ownership from reading context when generalizing extraction.
2. **Add isolated staging and recoverable promotion.** `write()` and `jsonl()` directly replace files at shared `HERE` locations. `inventory()` replaces the common manifest, and `extract()` replaces common segment/window tables. The inspected module does not implement leases, checkpoints, atomic validated promotion, or rollback. Give each tractate isolated output paths before parallel production writes begin.
3. **Implement and record actual semantic execution.** The inspected `pipeline.py` handles source inventory/extraction and display; its docstring explicitly says semantic decisions are separately authored. The file does not provide an annotation runner. A queue file or API readiness check cannot establish that annotation has happened.
4. **Generalize validation with explicit scope.** `validate.py` constructs expected coverage from `p.PILOTS`, reports pilot metrics, and hardcodes zero completed tractates in generated progress. It also returns `semantic_completeness_pass=False`, `expansion_gate_pass=False`, and a literal `source_files_checked=37`. Preserve the useful quote/hash/referential checks, but make the intended source coverage and measured counts explicit inputs.
5. **Version the schema.** `schema_v1.json` calls itself a pilot contract and constrains segment scope to `pilot` or `context_only`. Add a documented migration and preserve old IDs and evidence; do not relabel old pilot records as completed production.
6. **Keep semantic coverage distinct from selected statements.** The validator requires a pending review record for a segment without a selected statement. That is useful omission tracking, but does not certify that every atomic claim, question, condition, or argument has been extracted. Add per-layer extraction-pass records and task-specific eligibility gates.

## What is implemented in this package

`tools/build_jobs.py` is a deterministic metadata-to-job-specification utility. Its CLI accepts only the exact two historical manifest byte hashes pinned to the inspected commit. It validates their consistency, records the hashes, and preserves historical pilot metadata separately. The pure builder used by synthetic tests marks its inputs unverified and leaves `base_commit` null; only the verified CLI path binds that commit. Original full-text bytes are not checked by either path.

`runtime_initialization_template` contains suggested starting fields for a future scheduler. Those static defaults are not a dynamic progress ledger, and rerunning this utility cannot reset runtime state. A byte-identical existing specification succeeds without rewriting it; a differing existing file is refused. Publication uses a flushed, fsynced same-directory temporary file and an atomic non-overwriting hard link. The utility does not launch agents, call models, schedule work, implement annotation checkpoints, or certify the proposed protocol. Protocol version `2.0.0-design` makes that distinction explicit.

Run from this package directory, providing the actual pinned repository inputs:

```bash
python tools/build_jobs.py --manifest /path/to/source_manifest.json --progress /path/to/progress_manifest.json --output jobs.json
python -m unittest discover -s tools -p 'test_build_jobs.py'
```

Berakhot's 151-segment pilot is a prefix with an open tail beginning at `5a:24`. Bava Metzia's 64-segment pilot is an interior range (`21a–22b`); its job starts at the actual first source reference and requires both the omitted prefix and suffix. Neither historical count becomes new-run progress.
