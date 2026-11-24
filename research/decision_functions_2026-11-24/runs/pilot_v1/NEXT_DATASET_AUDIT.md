# Documentation-only replication audit

No MultiPref or TID-8 data files were downloaded or trained in this assignment. Counts below are documented, not measured corpus counts.

## MultiPref

Read the [official card at 12910233a0238a997ebe425656e9dfed7b0ff031](https://huggingface.co/datasets/allenai/multipref/blob/12910233a0238a997ebe425656e9dfed7b0ff031/README.md). The `default` release keeps comparison and prompt IDs, candidate completions and evaluator-linked ordinary/expert annotations. Preferences include five strengths with a central tie; reasons, confidence and timing must remain evaluator-only. Expert assignment is routed by subject expertise, so the next audit must measure overlap and history coverage rather than assume dense exchangeable assignment. The card specifies ODC-BY.

A future protocol must group prompts/comparisons, score the actual candidate texts, preserve ties/strength or explicitly declare a three-way reduction, and require swapped candidates to swap the full probability vector appropriately. DICES personal class offsets and raw-label neighbor votes cannot be recycled as arbitrary A/B preferences. Measure per-person support feasibility first. Do not use the aggregated `human_overall_binarized` configuration for this objective.

## TID-8 CommitmentBank

Read the [official card at e12b715be7582af64efc596f8402d916fb64f1e3](https://huggingface.co/datasets/MichiganNLP/TID-8/blob/e12b715be7582af64efc596f8402d916fb64f1e3/README.md). Its `commitmentbank-ann` and `commitmentbank-atr` schemas map answer_label indices **0,1,2,3,4,5,6 to judgment values 0,1,2,3,-3,-1,-2**, respectively. Indices are therefore not ordinal scores. `weak_labels` must be excluded. `question`, `uid`, and `annotator_id` provide candidate input/join fields, subject to an actual identity and duplicate audit. Existing annotation/annotator splits do not establish the required independent item-group and person split with support histories.

The card's top-level license is unknown and constituent licensing remains unresolved here. Before acquisition/redistribution for P4, verify original CommitmentBank terms and ID scope. No claim of a measured k=16 cohort is made. A separate frozen ordinal or categorical protocol is required.
