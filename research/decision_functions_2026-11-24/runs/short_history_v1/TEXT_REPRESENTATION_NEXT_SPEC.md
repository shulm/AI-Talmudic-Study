# Text representation: next specification (proposal only)

No encoder is selected, downloaded or run by this assignment. This document defines the admission and representation contract for a separately reviewed experiment; it is not execution authorization.

## What a text question must express

Represent a semantic case by an explicit structured tuple of task conditions and available answer meanings. In the controlled synthetic bridge, those conditions must encode the two question variables that drive the planted interaction, plus the known shared component. Express each case in neutral natural-language statements with a stable answer inventory and explicit alternative semantics. A separate, frozen renderer maps semantic tuples to text; human or independent semantic review must verify that a reader can recover the intended distinctions. Merely inserting arbitrary numerical features into unreviewed prose is not evidence of natural-language adequacy.

Do not include person IDs, latent personal vectors/phases, observed answers, query outcomes, oracle probabilities/logits, model predictions or train/test membership in question text. Stable opaque IDs belong only in manifests. Histories consist of the same observed question-answer pairs for all methods. Query text contains only conditions and alternatives. A model must not infer answers from filenames, template labels, answer ordering artifacts or renderer metadata.

## Grouping and controls

Assign every semantic case, its rotational/related variants, paraphrases and renderer lineage to a grouping graph before splitting. Keep semantic families and all paraphrases together. Hold out template families as a separate stress test; do not claim semantic generalization merely because a sentence template is reused with different numbers. Record exact text bytes, renderer revision and graph/split hashes. Separate source quotations from generated explanations; this bridge does not use provisional Talmudic annotations as labels.

Use a matched numerical-feature control with the identical people, semantic cases, observed support answers, query outcomes, shared-information budget and held-out groups. Run the same head/penalty/history policy at the same support count on both representations. Include B1 personal-frequency, B2 known/frozen shared predictor and B3 personal-offset controls, plus matched-other and uninformative controls. Keep shared parameters trained on training people/questions only. Fix whether shared logits are oracle-known or estimated before comparing representations; do not give one method extra labels or privileged shared information.

Distinguish head capability from representation adequacy: if the numerical control fails, text failure cannot isolate the representation. If the numerical control passes but the text version fails, report a representation-associated failure under this contract, without proving a unique mechanism. The short_history_v1 primary/secondary outcomes determine what is already qualified; a secondary success does not make primary k=16 qualified.

## Encoder and preprocessing admission

Before execution, separately select an encoder whose constituent terms and intended use are verified, with immutable model/tokenizer revision, exact local artifact hashes, dimension, pooling rule, sequence length, truncation policy, answer serialization and software environment. No unnamed latest model or unpinned remote default is admissible. Document any acquisition cost/resources and obtain authorization if outside that future assignment.

Freeze all preprocessing before evaluation. Learn centering, scaling, projection or other transforms on training questions only; store exact transform parameters. Do not use held-out texts to choose dimensionality or tune preprocessing. Keep effective representation dimension, feature norm and penalty normalization explicit; directly transplanting a two-dimensional penalty into a larger embedding does not establish comparable shrinkage. Any transformation/penalty candidates and selection budget require a new frozen design, separate from confirmation.

## Future decision rule and evidence

Before fitting, specify exact fresh realizations or admitted corpus revisions, support/grouping rules, primary representation comparison and a scientifically worthwhile effect distinct from numerical noise. Carry forward strict finite normalization,1e-12 clipping/replay tolerance, immutable records, batch checks and complete-run conjunctions. Keep primary and secondary policies distinct; choose no threshold or fallback after seeing held-out outcomes.

Report expected-oracle metrics only where an oracle exists, and realized NLL/accuracy/Brier in every condition. State accuracy tradeoffs explicitly. For a controlled synthetic bridge, paired person/group uncertainty must preserve semantic families and within-person history dependence; repeated paraphrases, schedules and initialization seeds are not new independent people. Report training/representation uncertainty separately from conditional resampling uncertainty. Freeze exact counts/resources and publish a pre-fit checkpoint before any optimizer.

## Human and scholarly boundaries

DICES and SRO pilot/follow-up outcomes are exposed. TID-8 CommitmentBank remains an archival candidate subject to constituent terms, immutable revision, identity/overlap checks and sufficient observed history coverage; no acquisition or substitution occurs here. PR10 and PR11 prepare distinct provisional Bavli tracks with their own edition/provenance and review boundaries. Neither makes AI-only positions validated human decisions. This proposal neither duplicates nor suspends their independently authorized work, and makes no scholarly training or corpus-expansion request.

Next review must resolve the semantic renderer, grouping graph, encoder admission and numerical normalization before a text experiment can be frozen. Stop at this specification.
