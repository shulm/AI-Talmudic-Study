# Scholar human-review preparation

Start with [the 30-family index](INDEX.md), [the six pending-family summaries](PENDING_FAMILIES.md), and [the blank review forms](human_review_forms.json). This packet prepares knowledgeable-human source review and family adjudication; **no human review has occurred**. It preserves the PR5 result: 32 attempted occurrences, 30 provisional families, 24 provisionally usable focal cases, six families without a usable focal case. The 24 include 17 outcome disputes and seven interpretive alternatives, not a homogeneous set of observed psychological choices.

The source is the exact completed delivery commit `6ca2dedc547144d7279696bd5322c1e39c7f03d3`. The preparation helper verifies every consumed source file's Git blob against that commit and records its local SHA256. It neither edits nor regenerates previous evidence, reviews, indexes, corpora, or confirmation material. The source-only cards contain exact unvocalized quotations already preserved in PR5, plus clearly marked AI questions; the linked original context contains raw Hebrew text, array indices, source hashes and version information. These selected excerpts do not replace reading complete enough surrounding discussion.

For each family, ask two knowledgeable readers to record initial judgments separately in their own copies of the blank form, before opening `annotations/`. Record whether each reader actually saw prior AI annotations. Preserve submitted first decisions; enter subsequent comparison and resolution separately. This is a proposed review workflow, not a claim that reviewers were recruited, contacted, or signed off. Identity, expertise, date, attribution, eligibility and signature fields are all blank/null. Unknown attribution must remain unknown.

The `annotations/` cards expose the original first AI review, its recorded context extension, the independent second AI review, current neutral inputs, source qualifications, and disagreements. RS10 and RS21 remain scope disagreements; RS32's first-reader repair is not initial agreement; RS14's corrected conditions remain explicit. The two historical family merges are retained: RS09/RS10 (deathbed gift continuation/version) and RS11/RS13 (answer-bearing cross-context). Do not count the second occurrence as another independent family. Mechanical cross-inventory context overlaps are supplied as candidates, not established parallel questions.

Review in this order:

1. Establish the question, necessary conditions, distinct alternatives, exact speakers and transmission status from the source. Read continuations for inversion, identification, reconciliation, retraction and rejection. Rav, Rav Asi and Rav Yehuda are not interchangeable.
2. Preserve an initial eligibility and assignment judgment before consulting the prior AI readings. Explain missing context or unresolved versions instead of forcing a binary label.
3. Compare semantic parallels, continuations and answer-bearing overlap across cases and inventories. Propose a merge/separation with exact supporting references. Shared topic alone is insufficient; uncertain relationships must block a purported disjoint split.
4. Check the Hebrew neutral view for missing conditions and direct attribution cues. Distinguish interpretable source recognition from explicit field leakage; masking names does not prove absence of memorization.
5. Reconcile documented differences only from evidence. If unresolved, preserve both readings and leave the family pending. No agreement percentage establishes expert truth.

The [broader sampling plan](BROADER_SAMPLING_PLAN.md) proposes collection of agreements and single-scholar statements independently of dispute discovery. It authorizes no model fitting or confirmation scoring and treats silence as missing, never a negative position.

Reproduce from the repository root with Python 3.12.4 (standard library only):

```powershell
python -X utf8 research/individual_decision_followup_pr5/scholar_review/build_packet.py
python -X utf8 research/individual_decision_followup_pr5/scholar_review/verify_packet.py
```

`build_packet.py` regenerates **blank preparation forms**. Once humans submit reviews, save those separately with immutable initial snapshots; do not place completed forms at the generated `human_review_forms.json` path. All current forms are unfilled preparation templates. `family_packets.json` is the machine-readable crosswalk of the 30 cards, original attempt IDs, exact excerpt spans, candidate overlaps and prior disagreements. No new download, fitting or paid call was used.
