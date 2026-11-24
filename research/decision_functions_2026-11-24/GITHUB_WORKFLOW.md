# GitHub communication and review workflow

## Canonical channel

Use **https://github.com/shulm/AI-Talmudic-Study/issues/2** for the continuation. It links the plan PR, its exact starting commit, execution PRs, protocol freezes, completed reports, and subsequent review instructions.

The repository is the durable record. Do not rely on a chat transcript, an agent's memory, or an uncommitted local notebook to transmit a scientific decision. GitHub does not automatically start an arbitrary external AI agent when an issue is created; the owner or execution environment must launch the agent with the prompt.

## Branch and PR rules

- Planning branch: `research/general-decision-functions-plan-20261124`.
- Suggested execution branch: `research/decision-functions-pilot-v1`; use a distinct suffix if it already belongs to active work.
- If the planning PR is unmerged, branch from its issue-linked commit and target the planning branch in a stacked draft PR. If merged, branch from current main and target main.
- Inspect current head and uncommitted changes before writes. Use an isolated checkout/worktree when another task is active.
- Commit only files belonging to the assigned task. Keep raw data, weights, individual support histories, large arrays and caches outside Git. Publish retrieval recipes, hashes, code, aggregate outcomes and small review documents.
- Do not force-push over another agent's changes, merge PRs, change visibility, or close historical work as an incidental action.

## Checkpoints

Append concise comments at meaningful milestones:

| Checkpoint | Required evidence |
|---|---|
| `STARTED` | Agent/run identifier, branch, base SHA, scope, environment |
| `AUDIT_COMPLETE` | Data revision/hash, real dimensions, target mapping, exclusions and access limits |
| `DEV_COMPLETE` | Code SHA, executed model grid, selected models, validation checks and resources |
| `PROTOCOL_FROZEN` | Exact freeze SHA, manifest hashes, selected configurations, declared final evaluation list |
| `TEST_COMPLETE` | Evaluation run ID, preserved probability-artifact hashes, primary/secondary results and controls |
| `READY_FOR_REVIEW` | Final commit, draft PR, report/handoff links, outcome, precise next recommendation |

Post `BLOCKED` when an actual capability, data structure, or resource limit prevents completion, with the exact failing action and all completed feasible work. A negative scientific finding is not a blocked state.

Read the latest issue comments before changing shared plans. Avoid overlapping execution when another agent has claimed the same run. A comment is coordination information, not an atomic lock or an access-control mechanism.

## Standard final comment

Use this structure, replacing every placeholder with an observed value or explicit `not run`:

```text
Status: <execution outcome>
Run: <run ID>
Branch / final commit: <branch> / <SHA>
Draft PR: <URL>
Protocol freeze: <SHA and URL>
Source / encoder: <immutable revisions and hashes>
Data: <people, item groups, observations, exclusions>
Executed: <commands and declared comparisons>
Primary result: <baseline, M1, paired delta and interval at k=16>
History and bias controls: <results, or not run>
Resources: <measured downloads, runtime, memory, fits and adaptations>
Reports: <AGENT_REPORT.md, TEST_RESULTS.md, NEXT_HANDOFF.md URLs>
Limitations: <specific remaining limits>
Recommended next task: <one concrete experiment or correction>
```

## Review exchange

The coordinating/reviewing agent reads the issue and execution PR, inspects the exact commit, and posts findings with severity and specific file/evidence references. The executor responds to each finding with a correction commit or an evidence-based explanation. Preserve the original result and record any invalidation or test exposure.

The next assignment should cite the reviewed commit and be posted in the issue or a linked versioned prompt. A fresh study gets a new protocol version and a declared relationship to previously exposed tests. Do not silently recycle a completed test while calling it new confirmation.

The coordinator reviews updates when invoked; this document does not claim a background watcher or scheduled monitoring service is running.
