# Yevamot production checkpoint 008 — partial, not delivered

Owner: `L03/yevamot`, tractate epoch **2**. Production agent `/root/yevamot`.

Eight accepted immutable proposals cover **158 / 3,869** original source segments in every required pass: structure, utterances, claims, attributions, questions, positions, edges, reconciliation. Source scope is **Yevamot 2a:1–8a:8**. **3,711 segments per layer remain**. There are 1,064 typed records. Independent review is **not completed**; no review agreement or ML qualification is claimed. All records retain `ml_eligible=false`.

The lead requested the durable session checkpoint after this bounded batch. No background worker is claimed. No shared code/schema/protocol, source corpus, global registry, or ownership file was changed by this producer. Nothing was committed, pushed, or merged.

## Exact artifacts

- `CHECKPOINT008.json`: hashes, source files, run contract, ownership, immutable proposal chain, layer counts, open tails and export manifest.
- `PROPOSALS_MANIFEST.json`: exact bytes of the eight producer proposals.
- `proposal001.json` through `proposal008.json`: initial semantic proposals retained unchanged.
- `replay008.json`: deterministic replay passed.
- `export008.json`: immutable export manifest content and counts.
- External source/job store: `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot`.
- External normalized package: `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot/exports/checkpoint008`.
- Snapshot: `9f023647b87afcf554aaaca7cbec483f0cfbc4183afe6a5dc30529f522f8be9c`.
- Export manifest SHA-256: `29ecdecb705d327fe25aed730d8850fbe4359c5ceef389ac6e37eac86ec59966`.

The export contains normalized typed tables, coverage, qualification and unresolved ledgers, per-structure source views and a hash manifest. Export hashes were independently recalculated after runner export. Contract, all frozen production-file hashes, original Yevamot file hash and original source-schema hash were verified again at checkpoint.

## Resume

1. Read project instructions and active run; verify the immutable run contract and the current job `OWNER.json`. Do not assume epoch 2 remains active after a lead handoff.
2. From the verified production checkout, run:

```powershell
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_yevamot
```

3. Expected current snapshot is the one above unless an explicitly documented successor exists. All next-unprocessed layer references are **Yevamot 8a:9**, original array index **[14,8]**. Do not renumber empty original positions.
4. Read an overlapping original-source window beginning at 8a:6 or earlier and extending beyond 8b:8. `window008.json` in the external job already contains original source through 8b:8, read as context only. No source from 8a:9 onward has completed production coverage.
5. Follow Rava's initial statement through corrections: 8a:9 initially says the verse prohibits the co-wife; 8a:19–8b:1 reports a correction in Rava's name; 8b:6 reports a further explanation via Rav Huna bar Tahlifa. Continue through the reversal proposed at 8b:7 and Rav Ashi's question at 8b:8; do not stop mid-dialogue or assign anonymous replies merely by name order.
6. Open structure fragments are `yev004.override`, `yev005.override`, `yev006.karet`, `yev007.karet`, `yev008.exception`, connected by explicit continuation edges. They preserve the unresolved larger discussion beginning 3b:16. The last accepted local reply is 8a:8. Use new IDs and explicit supersedes for corrections, replacing affected coverage/dependencies as runner requires. Never edit accepted proposal bytes.
7. Save the next immutable proposal under the assigned producer path; submit with current verified owner/epoch. Replay, export to a **new** directory, update a **new** checkpoint receipt. Build scripts are transparent materializers of manually read annotations, not retrieval/semantic heuristics; deterministic replay uses frozen proposals, not regeneration.

## Independent review and remaining work

The separate lead-managed reader must freeze source-first readings before comparison. No reviewer artifacts were supplied to this producer. Full tractate random, endpoint, risk and qualification cohorts remain required, as do every remaining source segment's eight passes. Use `UNRESOLVED_AND_ROUTING.md` for local uncertainties and candidate cross-tractate checks. Review must check omissions, not only existing rows.

Public proposal evidence is bounded source evidence, not a full corpus copy. Complete pinned source files and inventories remain external. Edition: Wikisource Talmud Bavli, Hebrew, source license metadata CC-BY-SA; no numeric license version inferred.
