# Review of evidence_shrinkage_v1 and next assignment

Reviewed on 2026-11-26.

**Retain PR #20 as INCOMPLETE / NUMERICALLY_UNRESOLVED, qualification false.** Its available predictions also fail the declared ES contrast criterion in every realization and history. The numerical stop and scientific recovery failure are distinct.

- [Review, evidence and limits](REVIEW.md)
- [Mathematical diagnosis and method note](METHOD_NOTE.md)
- [Executable next-agent assignment: H0–H4](NEXT_AGENT_PROMPT.md)
- [Fixed numerical engineering suite](ENGINEERING_SPEC.md)
- [Machine-readable next design](next_post_es_design.json)
- [Public review receipt](public_review_receipt.json)
- [Portable public-arithmetic check](check_public.py)
- [Portable deterministic equation check](check_math.py)

Pinned inputs:

| Input | Revision |
|---|---|
| PR #19 assignment | 724be8c49808e1e1b8643d81c73267f7577439c8 |
| PR #20 scientific pre-fit | 38dfff076b90d7c08387a06bd25f3cc75f15f6ae |
| PR #20 final delivery | f18255c5fad37f704881ff1f9ad50cd113497236 |
| PR #18 original planning package | 49d7157e3998a20f646e9200c3e223bbbb58541f |
| PR #18 current engineering-repair head | cdcafb41726820265bd4e1dea5272702f2663aae |

The next assignment, post_es_diagnostics_v1, authorizes a new diagnostic directory, read-only analysis of saved artifacts, one fixed uncapped-mixture ablation, and numerical implementation tested on deterministic engineering cases. It authorizes **zero new scientific fits, zero historical refits, and no fresh scientific realization**. Its engineering suite contains 384 explicitly counted personal solves. It ends with a decision and a proposal for the next independent experiment.

This review performed no optimization and had no access to the original private cache. It independently checked public arithmetic, exact inventories, hashes, chronology and deterministic mathematical identities. It does not claim to replay the original private arrays.

PR #18 remains a separate planning-only assignment. The corpus production/review track, including PRs #14, #16, #17 and #21–#24 observed during this review, remains separate. No merge is authorized.

To reproduce the review checks from a checkout containing the pinned source, supply that checkout as the first argument and a fresh output directory as the second:

~~~sh
python research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26/check_public.py REPOSITORY_ROOT FRESH_PUBLIC_OUTPUT
python research/decision_functions_2026-11-24/reviews/evidence_shrinkage_v1_2026-11-26/check_math.py REPOSITORY_ROOT FRESH_MATH_OUTPUT
~~~

The mathematical check requires NumPy/SciPy already used by the laboratory. Neither check runs a scientific fixture or optimizer.
