# Kiddushin bounded production 001 — 2026-11-27

Exactly one delegated batch is complete: **Kiddushin 2a:1–2b:5**, ten original segments, all eight required passes, 100 typed records. Full tractate denominator is 2,406; **2,396 segments per layer remain**. No tractate completion or review certification is claimed.

Existing owner `/root/lead_l01_l03`, epoch **1**, remained unchanged. Actual executing agent was `/root/yevamot`, recorded truthfully in the proposal. The L03 lead explicitly delegated promotion under the existing owner. No handoff, duplicate initialization, paid API, shared code/schema edit, registry edit, commit, push, or merge occurred.

## Frozen initial reading and pins

`INITIAL_PROPOSAL.json` is the producer's frozen initial structured reading, generated after direct original-source reading. No central frozen Kiddushin reading or interpretation was accessed before freezing. Subsequent comparator output must name this exact version; preserve it if corrections are required.

- Initial proposal SHA-256: `1ba6786415d87e15834b70f181ead177deb8988224f993a2a4bafd9e33dac1c2`.
- Promoted snapshot: `485622fdbe5533eba01863f478943dfd0b7ad5ffa38f9832c18776dbd4f74e2d`.
- Receipt SHA-256: `08048d559df2e187fe07529ee17a5174f53723da31576c7b93e11ee0372d2d11`.
- Export manifest SHA-256: `84803a873f539ba77eb6f90d13203c0fdf7c7502a13ba841a198f3a0760de035`.
- Exact source/schema/contract/production pins and unchanged ownership are in `PINS.json` and `RECEIPT.json`.
- Replay passed; every exported artifact hash was recalculated against the immutable export manifest.

External job: `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin`.

External normalized package: `F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin/exports/bounded_001_20261127`.

The package contains typed core tables, coverage, qualification and uncertainty ledgers, per-structure views and exact manifest. All rows remain AI provisional, unreviewed, and `ml_eligible=false`.

## Scope and continuations

Core indices run from `[2,0]` through `[3,4]`. Original array coordinates are preserved; no empty page or position was collapsed. Context was read through **3a:1**, stored separately in the external `context_bounded001_20261127.json`; its eleven additional segments do not count as extraction coverage.

The opening Mishnah is closed. The broad wording discussion `kid001.gemara` remains **open_right**, since number/דרך questions begin at 2b:6 and continue beyond the batch. Two nested local units (acquisition terminology; choice of female grammatical subject) close within the core; this does not close the encompassing discussion.

Review priorities: both Beit Shammai and Beit Hillel monetary amount/equivalent alternatives; perutah's precise one-eighth ratio; separation of ordinary marriage from levirate acquisition/release; printed verse labels preserved without silent correction; אי נמי as alternative proof; Torah/rabbinic terminology versus legal validity; ואי בעית אימא as alternative subject explanation; coercion hypothetical versus explicit consent requirement. The source prints Deuteronomy 22:13 in the money derivation; the evidence preserves that exact label rather than normalizing it to another citation.

## Resume and correction

Every next-unprocessed layer starts at **Kiddushin 2b:6**, original index `[3,5]`. Verify current owner and run pins before any future promotion; a new delegation may change scope, but this batch itself authorizes no additional production.

```powershell
python -X utf8 research/bavli_production_v1/runner.py replay --job-dir F:/Sefaria_QA/bavli_production_run_20261125_01/L03/bavli_kiddushin
```

Corrections must use new IDs and explicit supersedes, retain this frozen initial proposal and comparator evidence, update affected dependent records/coverage, and export to a new immutable directory. Do not rerun `build_initial.py` to replace the initial proposal; it deliberately refuses an existing initial proposal/current checkpoint.

Edition is Wikisource Talmud Bavli, Hebrew; CC-BY-SA attribution is retained from source metadata, with no numeric license version inferred. Full corpus/source inventory remains outside Git.
