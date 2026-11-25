# Quality, coordination, and reusable research releases

Protocol design version: `2.0.0-design`. This document specifies the production target. The queue and review-plan tools are implemented separately; the entire production protocol is not implemented by this package.

## 1. Separate the dimensions of progress

Use the following vocabulary in new qualification/coverage records. Preserve legacy fields unchanged and map them explicitly during migration.

| Dimension | Allowed values / meaning |
| --- | --- |
| `extraction_state` | `not_started`, `in_progress`, `completed` |
| `extraction_result` | `records_found`, `none_found_after_pass`, `abstained_ambiguous`, `not_applicable`; null if and only if extraction is not completed |
| `review_state` | `unreviewed`, `independent_ai_agreement`, `disputed`, `adjudicated_ai`, `human_reviewed` |
| `release_state` | `valid`, `quarantined`, `superseded` |
| Task eligibility | One versioned decision per task, record version, and required fields; boolean plus reason codes and policy hash |

A completed pass may abstain. `none_found_after_pass` is a recorded search/extraction outcome, not proof that no such content exists. `not_applicable` requires a reason; it stays in the source coverage denominator. Review and extraction are orthogonal. Human review records require an actual identified qualified review event for the claimed scope.

Administrative lifecycle states (`queued_unclaimed`, `assigned`, `running`, `checkpointed`, `awaiting_review`, `correction_required`, `delivered`, `blocked`) are separate from scientific qualification. A job cannot become completed merely because an agent exited successfully. Keep static job specifications separate from mutable runtime state.

## 2. Universal integrity gates

Every promoted output must pass:

1. Exact pinned source file hash, edition, original index mapping, and schema/tooling contract checks. Production never refreshes the approved source manifest automatically.
2. Exact direct-evidence equality against original strings; valid Unicode-codepoint half-open intervals; preserved markup/normalization mapping where relevant.
3. Complete source accounting, no duplicate primary ownership, and no context inflation. Preserve empty source positions and unusual starting pages explicitly. Do not shift array indices when skipping empty pages.
4. Valid IDs, versions, foreign keys, typed relations, and split/merge lineage. Anonymous and ambiguous attributions remain representable.
5. Per-layer extraction coverage linked to actual completed reading/proposal runs. A generic coverage marker without underlying execution evidence does not establish semantic completion.
6. Safe checkpoint promotion, replay from frozen artifacts, restart behavior, and stale-worker rejection. Regeneration using a new model call is not the replay guarantee.
7. Generated views/readers match authoritative records and the exact source/schema/review release. No second editable corpus inside a reader.
8. Recorded provenance and permitted distribution for the specific source/enrichment included in the artifact.

### Ownership precision

The pilot's exactly-one-primary-owner-per-segment rule is retained as legacy administrative accounting. Where a source segment contains a true semantic boundary, a production schema migration must support a nonoverlapping partition of canonical source intervals, with each interval assigned to a primary sugya. Nested units may overlap parents by design. Coverage must explicitly account for structural markup, delimiters, and whitespace under the declared text basis; do not silently discard characters to obtain 100%.

Do not set new interval-based data to the old strict schema version. Retain old IDs and compatibility maps. Any segment-level compatibility view must disclose coarse administrative ownership rather than assert that its whole segment belongs semantically to one discussion.

## 3. Independent review cohorts

### Probability sample

Use source coordinates, not worker-produced sugyot. The delivered planner uses fixed blocks of ten consecutive nonempty segments and a frozen seeded SHA-256 ranking. For B grid blocks, n = min(B, max(30, ceil(B/10))). Each block's probability-sample inclusion probability is n/B under the declared random-seed design. Choose/freeze the seed before examining annotation outcomes; do not hunt for a favorable seed.

These numbers allocate review effort. They do not establish a target accuracy or adequate statistical power. The reviewer reads sampled cores and enough original surrounding text to infer complete local meaning. Context expansions are reported separately. Report the unique sampled source segments/characters and independently found claims, questions, edges, and boundary opportunities.

### Mandatory source endpoints

Check opening and closing blocks even if not randomly selected. Track overlap with the random sample and deduplicate union coverage. Keep endpoint outcomes separately labeled; the combined set is not a simple random sample.

### Risk and task qualification

Review detected ambiguity, attribution/transmission risk, cross-window tails, competing versions, contradictions, and records proposed for demanding research views. Label source-derived flags separately from worker-derived flags. All detected critical cases must be resolved or quarantined. Review all candidate examples under the policy for their proposed high-value evaluation task.

The random source sample remains necessary because flagged rows cannot reveal every silent omission. Extra independent extraction is particularly useful for conditions, omitted claims, and attribution. Repeated endorsement of a producer's narrative is not equivalent to independent evidence reading.

## 4. Report measurements with the right denominators

| Measurement | Denominator |
| --- | --- |
| Direct quote fidelity | All saved direct-evidence spans |
| Source processing coverage | Unique canonical source scope / complete source scope |
| Layer extraction coverage | Source scope with documented completed pass / complete required scope |
| Attribution error/disagreement | Independently audited attributable claims |
| Omitted claims | Claims independently identified inside sampled source cores |
| Condition loss | Audited claims that contain relevant conditions |
| Alternative comparability | Audited proposed answer sets |
| Supported relation/direction | Audited argument edges |
| Boundary agreement | Independently defined boundary opportunities under a stated matching tolerance |
| Independent review coverage | Unique source cores actually independently read, plus separately reported expanded context |

Report confirmed errors, unresolved source ambiguity, reviewer disagreement, and corrected cases separately. Preserve original readings and initial error counts; do not calculate post-correction perfection while deleting the first-pass findings. If uncertainty intervals are computed, respect clustered windows/discussions and the sampling design. Thousands of claims from a few discussions are not thousands of independent samples.

No blanket semantic accuracy threshold is justified by the current evidence. The release rule is zero unresolved integrity-critical errors **inside released scope**, clear exclusions, and adequate declared review for the intended task. A systematic semantic defect blocks its affected layer until repaired and checked on a fresh relevant sample.

## 5. Local versus shared blockers

| Finding | Scope of pause |
| --- | --- |
| One unsupported forced/wrong attribution | Affected record versions and dependent task examples |
| One unresolved boundary | Boundary and dependent records; stable interior units continue |
| Repeated rule/prompt failure | Affected pass and all records generated under that rule/prompt |
| Source hash or edition mismatch | Every job depending on that snapshot |
| Destructive checkpoint or duplicate-ID defect | All dependent promotions |
| Missing optional commentary/metadata | That optional enrichment layer |
| Missing paid API access | That execution route; permitted existing agents can continue |

Supported unresolved alternatives may remain valid, disputed corpus records with restricted eligibility; uncertainty alone is not corruption. A blocker includes evidence, dependency scope, repair owner, and the check that can clear it. Do not repeatedly call a failed semantic generation until it produces the desired answer. Preserve uncertainty and use evidence-based adjudication.

## 6. Coordination and immutable review

One dispatcher owns assignments. One producer promotes each tractate. Reviewers write separate artifacts. One integrator owns global registries/releases. Record leases/epochs and use an atomic assignment authority; stale workers cannot promote. Save independent proposals before comparison. An integrator may build a release candidate in its own branch from accepted artifacts; this does not authorize merging PRs into their base branches.

Freeze common-contract hashes before each production wave. A shared schema/prompt change triggers an impact report and targeted reprocessing; unchanged unrelated data need not be regenerated. Exact-commit review is supplemented by artifact hashes so unrelated documentation changes do not masquerade as annotation changes.

## 7. Research export qualification and leakage

Use distinct, versioned views for source retrieval, segmentation, extraction training, attribution evaluation, argument evaluation, QA, and scholar-position comparison. Every exported row records underlying source/record versions, eligibility policy, review tier, and excluded-risk flags. A provisional extraction training view must advertise its annotation origin/noise and cannot double as an independently verified test set.

Maintain occurrence IDs and a typed family graph. Confirmed repeated reports, direct parallels, cross-edition counterparts, and derivative examples can require shared split groups. Similar topics alone do not automatically define a single family. Candidate links are uncertainty, not confirmed equivalence. Preserve each textual occurrence even when it shares a family.

Before a supervised benchmark is frozen:

- Define the prediction question and the information available at prediction time.
- Group required families and record unresolved-link exclusions.
- Split groups before generating paraphrases, questions, summaries, or other derivatives.
- Remove targets and outcome-bearing summaries, titles, aliases, rationales, continuation text, and retrieved parallels from input views as required by the task.
- Freeze source/record versions, family graph, input recipe, label policy, and train/dev/test manifests.
- Version any later cross-family discovery and identify affected evaluations; never silently preserve a false independence claim.

A tractate split alone does not establish independence. Family controls address project-level leakage; they cannot certify that a public classical text was unseen during a foundation model's pretraining. Report that evaluation limitation. Textual order does not provide historical decision chronology; any history-conditioned view must state how histories were constructed.

## 8. Public artifacts and licensing

The repository is already public, but reuse permissions remain artifact-specific. Keep exact source metadata, source attribution, edition and license labels, and any unresolved version detail. PR #10 records CC-BY-SA without a numeric version; do not silently rewrite its historical metadata. Preserve relevant share-alike requirements for text-containing derivatives. Keep code, source text, Sefaria link metadata, commentaries, and original annotation licensing separately identified. Do not declare the entire repository MIT/CC0 by convenience.

Follow the repository instruction against committing full corpus copies. Publish source manifests, source acquisition/reconstruction instructions, reviewed annotation tables, release indexes, and permitted bounded evidence. A public standalone full-text bundle or reader requires an appropriate distribution location and complete applicable rights metadata; its preparation is separate from deciding that GitHub may be public. Missing rights for one optional edition does not block source-reference metadata or unrelated licensed layers.

Official source guidance is linked in `SOURCES.md`. Sefaria's links dataset has its own CC-BY terms; importing a link does not grant rights to the linked commentary text or certify the link's semantic meaning.

## 9. Release labels and final matrix

Use the four verdicts in `INDEPENDENT_REVIEW_PROMPT.md`. Every release gives a matrix for source integrity, structural coverage, semantic coverage by layer, review coverage by cohort, unresolved cases, and task eligibility. A completed extraction pass may be provisionally released with supported unresolved interpretations preserved and invalid records quarantined. Unresolved claims cannot enter a task that requires their resolution, and quarantined claims cannot enter a qualified benchmark.

Retain a durable raw/provisional layer, an AI-reviewed layer with exact scope, and any later human-reviewed subset. Avoid the label "gold" for AI agreement. Release per tractate as useful work completes, then assemble corpus snapshots with declared edition/schema compatibility. The current package contributes production instructions and preparatory tools, not a new data release.
