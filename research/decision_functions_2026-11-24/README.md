# General decision functions from text

**Status: PLAN_READY / EXPERIMENTS_NOT_STARTED.** Prepared 2026-11-24.

The objective is to predict a decision-maker's answer to a new textual problem from their observed question–answer history:

$$\widehat P(a\mid q,C(q),H_s).$$

Talmudic scholarship is a later application of this general method. The immediate experiment uses an existing general human-judgment corpus.

## Start here

1. Read [RESEARCH_PLAN.md](RESEARCH_PLAN.md) for the mathematical model, staged research program, and pilot protocol.
2. Execute [NEXT_AGENT_PROMPT.md](NEXT_AGENT_PROMPT.md) for the first bounded assignment.
3. Consult [LITERATURE_AND_DATASETS.md](LITERATURE_AND_DATASETS.md) for primary sources, dataset mappings, and evidence limitations.
4. Use [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md) for all agent coordination and return reports.
5. Fill and freeze [protocol_template.json](protocol_template.json) before the final evaluation. It is an unexecuted template, not a run record.
6. Consult [SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json) for the inspected repository baseline and [REVIEW_NOTES.md](REVIEW_NOTES.md) for planning checks.

**Coordination issue:** https://github.com/shulm/AI-Talmudic-Study/issues/2

## Scope of the next assignment

Audit DICES350, implement a small reproducible laboratory, compare frozen-embedding baselines and a low-rank personal interaction model, then perform one declared held-out evaluation after pushing a frozen protocol. Continue through these steps autonomously when the data and correctness checks permit. A negative or inconclusive result is a completed assignment.

The endpoint is a reviewable pilot with actual evidence. Corpus-wide sugya extraction, larger neural models, a second human-domain experiment, and free-form answer generation belong to later phases.

## Relationship to earlier work

[Draft PR #1](https://github.com/shulm/AI-Talmudic-Study/pull/1) proposed recovering scholar–position assignments. Preserve it as a historical proposal. This continuation supersedes that modeling objective: the learner receives a person's observed decisions and predicts that person's answer. Predicting the speaker of an already supplied answer is not the primary task.

Existing source-index research remains a separate useful track. Its source-location counts are not counts of independent, verified training examples. No source reports, index builders, quotations, or attribution decisions are changed by this planning package.

The repository was observed to be **public** at preparation time; its current AGENTS.md records that visibility as the user's decision. Keep raw third-party data, individual histories, model weights, and caches outside Git. Commit acquisition recipes, source hashes, code, protocol, and suitably compact derived reports.
