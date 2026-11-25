# Send these instructions in this order

Prepared 2026-11-25. This is an execution launch pack for the full selected Bavli inventory: 37 tractates / 81,793 pinned source segments. It contains no new annotations or active agents.

## Launch order

1. Give [01_GLOBAL_COORDINATOR.md](01_GLOBAL_COORDINATOR.md) to **one lead only**, preferably on the source-owning machine. It prepares the executable common contract, portable source access, and actual assignment ledger.
2. Give [02_INDEPENDENT_REVIEW_LEAD.md](02_INDEPENDENT_REVIEW_LEAD.md) to a separate review lead. Its source-only preparation can overlap bootstrap; fresh blind readers must not inherit producer annotations.
3. After the common contract and the relevant source files are ready, launch **03–08 concurrently**, one lead for each lane. These six instructions are parallel assignments, not six sequential phases.
4. Give [09_INTEGRATION_RELEASE.md](09_INTEGRATION_RELEASE.md) to the coordinator/integrator as completed tractates arrive. Integrate continuously, then close the complete 37-tractate coverage audit.
5. At a session limit, use [10_RESUME_EXISTING_ROLE.md](10_RESUME_EXISTING_ROLE.md) with the saved checkpoint. Continue the same ownership and exact contract; do not start again.

The user does not need to manually launch every small window or every next tractate. Platform leads delegate the [37 prefilled worker files](WORKER_INDEX.md) and drain their own queues.

## Six disjoint queues

| Lead | Instruction | Tractates in initial processing order | Source segments |
| --- | --- | --- | ---: |
| L01 | [03_L01_PLATFORM_LEAD.md](03_L01_PLATFORM_LEAD.md) | Berakhot; Zevachim; Ketubot; Bekhorot; Sukkah; Chagigah | 13,657 |
| L02 | [04_L02_PLATFORM_LEAD.md](04_L02_PLATFORM_LEAD.md) | Bava Metzia; Sanhedrin; Gittin; Sotah; Keritot | 13,669 |
| L03 | [05_L03_PLATFORM_LEAD.md](05_L03_PLATFORM_LEAD.md) | Rosh Hashanah; Yevamot; Eruvin; Kiddushin; Nazir; Arakhin; Tamid | 13,635 |
| L04 | [06_L04_PLATFORM_LEAD.md](06_L04_PLATFORM_LEAD.md) | Taanit; Bava Batra; Pesachim; Avodah Zarah; Nedarim; Moed Katan; Makkot | 13,593 |
| L05 | [07_L05_PLATFORM_LEAD.md](07_L05_PLATFORM_LEAD.md) | Chullin; Shabbat; Yoma; Shevuot; Temurah; Horayot | 13,598 |
| L06 | [08_L06_PLATFORM_LEAD.md](08_L06_PLATFORM_LEAD.md) | Bava Kamma; Menachot; Niddah; Megillah; Beitzah; Meilah | 13,641 |

**Total: 37 unique tractates, 81,793 segments, no overlaps or omissions.** The largest/smallest lane counts differ by 76 source segments. Semantic difficulty and review effort may differ; this is an initial allocation, not a speed estimate.

## Match this to your platforms

- Six platforms: one lane lead per platform.
- Three platforms: run L01/L02, L03/L04, and L05/L06 as separate lead contexts, or let one lead explicitly own those two complete lanes.
- Two platforms: assign L01–L03 to one and L04–L06 to the other, retaining the same distinct lane/tractate ownership.
- More agents: each lane lead dispatches its individual whole-masechta files, and can add source-only reviewers or bounded internal helpers. Additional workers do not independently claim another lane.

The coordinator may rebalance unfinished jobs through a recorded checkpoint/epoch handoff without requesting routine new user permission. A reused/continuing run must reconcile actual existing owners before activating this planned map.

## Files and operating requirements

- [COMMON_EXECUTION_CONTRACT.md](COMMON_EXECUTION_CONTRACT.md) sets shared scope, source verification, writer isolation, required richness, review, and completion rules.
- [ASSIGNMENTS.json](ASSIGNMENTS.json) binds every job to one planned lane and the exact source hashes from the verified historical v2 queue.
- [RUN_CONTRACT_TEMPLATE.json](RUN_CONTRACT_TEMPLATE.json) is a template. A ready runtime contract must identify actual executable code, schemas, protocol, source access and passed checks.
- [WORKER_INDEX.md](WORKER_INDEX.md) links all 37 individual worker instructions.
- `VALIDATION_REPORT.json` and `PACKAGE_MANIFEST.json` describe checks and file hashes for this instruction pack, not new semantic review.

The original v2 production design remains under `research/bavli_dataset_program_v2/` in the repository. The portable ZIP includes a byte-identical `reference_v2/` copy for platforms that cannot read GitHub. Full source text is not included in this ZIP; the coordinator must supply verified source access separately.

Use existing authorized agent resources. The inherited allowance for new metered external model APIs remains zero; no new provider is required. Keep draft PRs unmerged. Do not use GitHub visibility as a license grant for every source or commit full source-corpus copies. Preserve the evidence/review policy and all prior data.

## Actual first action

**Send instruction 01 to the source-owning lead. Start instruction 02 alongside it. As soon as a real contract and source access are published, give instructions 03–08 to your platform leads concurrently.** Their goal is complete tractate data and review evidence; they must not end with another plan-only handoff.
