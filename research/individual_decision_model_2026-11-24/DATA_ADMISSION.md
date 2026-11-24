# Data admission — 24 November 2026

**Admitted: Self-Regulation Ontology, Complete_02-16-2019 at repository revision `4e6e837fb5aaca87ed5914fd9be251156f43eec9`.** One primary direction: Kirby delay choices → Holt–Laury lottery choices. No secondary pair or budget 16. Selection precedes all predictive model comparisons.

## Cross-Psych-101: inspected first, not admitted

Pinned Hugging Face revision `532794c51e046a0ddaf560e7972789688d46bf63` contains 29,118 train and 7,295 test transcript rows. Direct participant-column counting gives 481 train and 120 test people, no overlap, **601 total**. The [authoritative paper](https://aclanthology.org/2026.emnlp-main.2235.pdf) distinguishes the experimental 601 from a public 591 after ten opt-outs; its public valid-decision headline is 261,551. This release therefore cannot be reconciled with the paper's public-participant count. Public accessibility does not resolve the opt-out discrepancy. Neither the raw README nor release metadata declares a license.

Train rows contain entire source histories, entire target transcripts, outcomes and session totals. They lack explicit session and original trial IDs. There are 17,475 distinct `(participant, source task, transcript hash)` values in 29,118 training rows; neither count is a count of independent decisions. Identical transcripts could be repetitions of one session or distinct identical sessions. Hash deduplication alone cannot recover that identity. Some tasks have sequential outcomes; their full transcripts are inappropriate static learner inputs. Raw task implementation provenance was not located through the inspected release/paper links. Test messages were not read; only participant metadata was accessed.

Admission checklist: participant linkage is present, split IDs disjoint; permission and opt-out reconciliation fail; canonical original decision identity and chronology remain unresolved. These are structural reasons for the specified fallback, not model-performance reasons. `cross_psych_audit.json` preserves machine counts. No Cross-Psych responses enter training or evaluation; its downloaded files remain local and uncommitted.

## Fallback evidence and task choice

The [SRO repository README](https://github.com/IanEisenberg/Self_Regulation_Ontology/blob/4e6e837fb5aaca87ed5914fd9be251156f43eec9/README.md) explicitly licenses repository data CC-BY-4.0. Credit: Ian Eisenberg and collaborators, Self-Regulation Ontology; associated [Nature Communications paper](https://www.nature.com/articles/s41467-019-10301-1). We use individual raw choice records, not dependent-variable summaries, questionnaire traits, or inferred labels.

Inspected raw columns and original task definitions:

- [Kirby code](https://github.com/expfactory/expfactory-experiments/blob/49b8123f18b26d94dfc010bb8a6ec7458b265e2e/kirby/experiment.js): 27 hard-coded amount/delay pairs, fixed timeline, one prior practice item, no response-adaptive next item and no between-item reward feedback. `80` means larger/later and `81` smaller/sooner; the parser cross-checks the named choice and actual stimulus. The random bonus is selected at task end. Source choice semantics are **later versus sooner**, not right versus left.
- [Holt–Laury definition](https://github.com/expfactory/expfactory-surveys/blob/7fee0ece12aa60497436990c6a7c5ca7349eb42a/holt_laury_survey/survey.tsv): ten fixed gamble pairs displayed on the same page, no adaptive selection or feedback. Raw options contain the monetary alternatives and their stable IDs. Response 1 is safe, response 2 risky; response text is cross-checked. Target meaning is **risky versus safe**. Within-page click chronology is unavailable. All ten items form one dependent schedule family, not ten independent experimental families.

These inspected code revisions postdate collection; stimulus/options correspondence is checked in every retained raw row. This supports the static representation, but does not prove the precise deployment commit. No historical deployment SHA is asserted. Sessions use worker ID, task, and finish time; original file row IDs remain separate. In particular, a row's embedded `s000` need not equal its `worker_id`; linkage uses the latter, not a substring guess.

The third inspected candidate, Columbia Card Task cold, is **not admitted**. Its raw records contain round outcomes and would require an additional feedback/definition audit. The chosen delay-to-risk pair tests whether sparse intertemporal behavior helps predict another monetary tradeoff, without claiming a single psychological construct or causal transfer.

## Coverage and pre-model eligibility

Raw selected-task files have 522 linked people; Kirby has 14,094 test choices plus 522 excluded practice choices. Holt–Laury has 5,206 observed choices: 508 complete ten-item schedules and 14 nine-item schedules. For a fixed common-probe retrieval comparator and identical targets, the declared cohort requires 27 source choices and a complete ten-item target schedule. Thus 508 people are eligible and 14 are excluded for incomplete schedule coverage, independently of response values. No response-consistency or predictability exclusions are applied. The existing Complete release's upstream selection is inherited, not reproduced; inference is conditional on that release.

The new deterministic person split has 304 training, 102 validation and 102 test people. This is not an official SRO benchmark. The first raw rows for `s001` were read to establish semantics; that participant is permanently development-only (the deterministic split already puts them in training). All later person-level content inspection for design is limited to development records. Full-data mechanical mapping, availability, schema and duplicate checks do not tune predictors.

The primary support budget is eight, with nested 0/2/4 curves. All people have the same input-only hash-selected Kirby items. Their original order is retained in canonical evidence; this is offline selection of static recorded decisions, not a simulated sequential questionnaire. Source task finish times need not precede target completion: the claim is retrospective static choice prediction from a permitted source history, not forecasting a future decision or reproducing a live experiment.

## Admission limitations

Choice events and IDs are distinct; behavioral independence is not assumed. Same-page target responses may influence one another. Models see only the current target scenario, no other target choices. Participant clustering accounts for repeated decisions, but the result remains conditional on these two tasks and one target schedule family. This does not establish transfer to a task absent from training, general psychology, or scholarly positions.

Both tasks confound one substantive alternative with fixed display position: later is right/second and riskier is second. Semantic encoding prevents treating arbitrary A/B labels as a trait in code, but cannot remove this experimental confound. Any positive signal may include stable second-option response tendencies; the source-summary comparator is essential. A counterbalanced replication would be needed to distinguish those mechanisms.

The extractor and mechanical validator necessarily process raw choices, including held-out rows, only for mapping and integrity assertions. No test-person response is printed or used for design/model selection. Development loaders read physically separate train/validation outcome files; only the final scorer opens the test outcome file. This is an enforced program boundary, not a claim that the agent or OS cannot access local raw files.

Raw data, canonical participant records, detailed splits, memberships and probability predictions stay in ignored `local_data/`. Public reports contain aggregates and artifact hashes. No new participant-level release is made.
