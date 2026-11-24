# Independent replication admission review

Reviewer: independent_AI (methods_review). Date: 2026-11-24. Decision: **NO ARCHIVAL CANDIDATE ADMITTED**. Exactly three candidates screened. This is a bounded metadata/methods screen, not proof that suitable data can never be obtained.

No participant response rows, candidate confirmation labels, or fitted results were opened. No model was fit. No MRI files were downloaded. No author was contacted. Cross-Psych remains outside admission; it was not treated as a fourth new candidate. The original SRO508 evidence remains exploratory.

## Admission rules

A candidate must support independent people, linked raw choices in two decision tasks, identifiable options and canonical item/session keys, permission for the exact release, actual position counterbalancing/randomization, a defensible static choice problem (or a separately justified sequential estimand), and feasible precision. All gates must pass before confirmation data are inspected. Unknown is not a pass. Position information in a schema alone is not proof that positions actually varied. Task order, colors, or post hoc option relabeling cannot repair fixed semantic position confounding.

| Gate | Bissett 2024 | Basel-Berlin Risk Study | AgeRisk |
|---|---|---|---|
| Distinct recruitment from SRO MTurk sample | Supported provenance; individual disjointness unverified | Supported provenance; individual disjointness unverified | Supported provenance; individual disjointness unverified |
| Within-person raw task linkage | Supported scanner schema | Supported partid schema | Supported Eprime/key schema |
| Full alternatives and canonical trial/session reconstruction | Partial; not validated on rows | Partial; definitions exist but no joined contract | Partial; discount and gamble definitions exist |
| Exact public release permission | Pass: OSF CC0 | Pass: OSF CC BY 4.0 | Pass: OSF CC BY 4.0 |
| Actual positions in qualifying two-task design | Fail for proposed scanner preference pair | Unresolved for qualifying static pair | Unresolved for discount; SafeSide alone insufficient for gamble implementation |
| Static source-to-other-task suitability | Fail for discount/CCT-hot pair | Unresolved; DFE sequential, LOT adaptive | Plausible lab discount/gamble pair, not yet position-qualified |
| Eligible confirmation N / precision | Unestablished, at most103 total | Unestablished, at most1507 total | Unestablished, at most200 total |
| Admission | No | No | No |

Recruitment provenance is evidence of a separate cohort, not a participant-level deduplication certificate. Task-level completeness and raw keys were deliberately not claimed to be empirically validated.

## 1. Bissett et al., Scientific Data 2024

The primary descriptor reports 103 completers recruited locally around Stanford and the Bay Area. The scanner battery includes discounting and CCT-hot. Task order was counterbalanced, but the paper restricts response-mapping counterbalancing to specified cognitive tasks; other tasks did not counterbalance mappings. The post-scan online battery was described as awaiting quality assurance and future matched-ID publication. Thus its availability cannot be assumed from its having been collected. [Descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271451/)

The public OSF root currently exposes raw/cleaned scanner behavior and reference files; sampled raw file metadata matches scanner tasks. Its codebook documents Subject, Trial_index, Trial_id, Exp_id, Exp_stage, key_press, and possible_responses. Trial_id describes a trial type and is not by itself a unique item key. Discountfix records Small_amount, Large_amount, Later_delay and Choice; CCT-hot records round, cards/clicks, loss outcomes and round reward. Those changing within-round states make the latter sequential. No response data were opened. [OSF release](https://osf.io/sjvnw/) / [codebook](https://osf.io/download/c2vj4/)

The release node is CC0; do not confuse this with article licensing. OpenNeuro v1.0.4 is the cited release; repository HEAD metadata was pinned to 769186fe1b185fae16437f380bfebd56edf7acd7 (2024-05-20). No OpenNeuro imaging was obtained. Failure of the proposed pair is substantive position/sequential mismatch, not simply small N. A newly published at-home release would require a fresh explicit admission amendment.

## 2. Basel-Berlin Risk Study (BBRS)

This is a separate laboratory cohort: 1507 young adults, with repeat sessions representing repeat people rather than extra independent participants. The article links the public repository and behavioral task definitions. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5627985/)

The version2 codebook documents partid and session keys, missing-task indicators, and raw decision tables. DFE has gamble_rev and color_rev, but participants sample outcomes before deciding: these cannot be flattened to context-free static choices. Adaptive LOT records Presentation_XZ, complete X/Z payoff/probability fields, Stage/Substage and previous-choice-sensitive transitions. Initial nonadaptive LOT stages might be usable after exact task reconstruction; that possibility is not established by this screen. DFD lacks an explicit presentation-reversal field in the inspected schema. MPL records choice0left1right and a separate problems table, but the inspected schema does not establish randomized semantic positions. Consequently no pair has passed both position and static-context gates. [Repository](https://osf.io/rce7g/) / [codebook](https://osf.io/download/7ren6/)

The Frey subproject metadata exposes analysis directories (preparation, distributions, correlations, latent variables, retest, regressions), not a verified task runtime. The article's supplementary task-method link was located, but browser retrieval did not return inspectable supplementary text in this screen. This remains an evidence gap, not a claim that the original implementation definitely fixed all positions. The OSF project is CC BY 4.0; the article's different license is not substituted for the data license. A project description invites coordination to avoid overlapping research; no contact was made and no mandatory contact condition was inferred.

## 3. AgeRisk / Tisdall et al., Data in Brief 2023

The descriptor reports a community sample of 200, with laboratory discounting and mixed gambles. The lab delay task has 80 decisions; mixed gambles has 210 trials across seven gamble types. These are plausibly static preference tasks. Scanner discounting uses specified fingers for smaller-sooner and larger-later; this is not evidence of semantic key counterbalancing. [Descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC10751829/)

Codebooks support Eprime IDs linked through participants_key, trial order, full SS/LL amounts/delays, and full safe/risky payoff probabilities. Mixed gambles explicitly records SafeSide and selected side; discounting's inspected schema has no corresponding presentation-position variable. SafeSide makes the target promising, but does not itself prove an actual randomized schedule. The inspected mixed-gamble R file generates payoff stimuli/images, not runtime display assignment; its sample/runif calls therefore do not verify option-position randomization. Delay materials inspected at first and last metadata pages contain stimulus images; runtime randomization code was not established. No images or response rows were downloaded. [Release](https://osf.io/sh34n/) / [delay codebook](https://osf.io/download/rzy7g/) / [gamble codebook](https://osf.io/download/nm85v/) / [stimulus code](https://osf.io/download/e5jfd/)

The data project is CC BY 4.0. Dividing the seven gamble conditions into artificial source/target tasks would change the intended cross-task claim, so this screen does not use that workaround. Missing presentation evidence for laboratory discounting is sufficient to withhold admission.

## Precision and stopping decision

Headline sample sizes are ceilings, not verified complete-pair or confirmation counts. No eligible participant intersection was computed from responses. None currently has a locked confirmation partition or an outcome-independent, justified participant-level variance bound for the intended own-versus-matched-donor contrast. Thus precision is unestablished for all three; this is not a claim that BBRS is inherently underpowered. For planning only, a normal paired-mean interval has approximate half-width 1.96*sigma/sqrt(n), where n is independent confirmation participants, not trials, donors, seeds, or retests. Any sigma borrowed from the original exploratory study requires sensitivity ranges and cannot establish transport to a new task. A valid next protocol must specify precision before confirmation access.

Stop the archival screen at three candidates and proceed to a collection specification / preregistered replication protocol. No confirmation dataset has been admitted or scored. Keep independent persons, actual randomized semantic positions in both tasks, raw option values, recorded assignment schedule, stable trial/session IDs, and participant-level inference as prerequisites. Sequential/adaptive alternatives require a new explicit state-aware design, not implicit substitution into the static pipeline.

## Transfer accounting and reproducibility

Measured direct HTTP response bodies: **462145 bytes** (metadata, four codebooks, one stimulus-generation script), including 10918 bytes reconstructed from the initial recorded byte counts. No raw participant data or MRI payloads. Browser search/page transport sizes are not exposed; they are not falsely counted as zero. Two browser attempts to inspect the BBRS supplementary PDF did not return inspectable content; its advertised size was 2.6 MB. Even counting both advertised payloads conservatively gives less than6 MB plus browser HTML/search overhead, well below the shared2 GiB cap. This is a local subagent account; parent must aggregate any other transfers.

`admission_http_log.json` contains exact measured bodies and SHA256 where retained. `admission_sources.json` pins the relevant metadata/codebook versions. `screen_metadata.py` only reads bounded OSF/GitHub metadata and does not follow download links. It is a screening utility, not a candidate validator. Candidate admission cannot be inferred from utility success.
