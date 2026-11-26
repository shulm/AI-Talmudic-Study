# Additive findings for the shared engineering/integration owner

The frozen production runner/schema/protocol were not changed. These findings do not grant task eligibility.

1. Attribution `content.scope` is free text and is not checked as a foreign key by the common validator. Dependent revisions can leave a superseded ID there while all validated `links` are correct. Nedarim/Moed Katan/Makkot exact-ID scopes were repaired with immutable `ptr003` revisions. Makkot later identified an ID followed by a semicolon/comment in its opening variant attribution; `pointer012` repairs that embedded reference. Historical packages preserve the old representation. The first package verifier checked only exact-ID scopes and therefore did not detect the semicolon form; its successful result was limited to that stated check. Proposed shared fix: define a structured scope-reference policy and validate it without treating arbitrary prose as an ID. Do not silently migrate the contract in this lane.

2. Several question records retain `answer_set_status: none` while argument edges provide answers. Reviewers have flagged the policy question: absence of an enumerated answer set may differ from absence of an answer. Until the engineering/semantic owners clarify the intended field, this is not promoted to a categorical data error or supervised answer-set eligibility. Exact reviewer observations remain in their comparisons.

3. Runner `semantic_records` counts all preserved versions, including superseded records. Lane package receipts separately report active and superseded counts. Intermediate progress messages that called the runner's total an active count are corrected by the exact receipts; source coverage is unaffected.

4. The schema has `distinction` but no `contrast` edge. The Moed Katan4a:17 review correction uses `distinction` to link the majority-condition disagreement explicitly, with a note that neither position is retracted or adjudicated. This uses the existing vocabulary and preserves the initial missing-relation finding.

5. Worker usage-limit interruptions occurred after source freezes/accepted proposals. Resumed readers preserve their first freeze and identify subsequent comparison as nonblind; no restarted blindness claim. Rejected proposal attempts remain external and do not enter accepted chains or coverage. No paid API was used to bypass the interruption.

6. Moed Katan marking010 initially used the unsupported assertion-mode value `reported` for two narrative claims. Common validation rejected the proposal without promotion. The preserved external attempt was replaced by marking010b using the existing `asserted` value while retaining narrative scope descriptions. No schema change or coverage from the rejected attempt occurred.

7. Moed Katan marking011 initially attempted a continuation edge between claims; common validation rejected it because continuation endpoints must be structures. Accepted011b uses two nonprimary narrative structures and their continuation edge while preserving the primary aggregate. Metadata012 aligns editorial origin and replaces stale question-coverage prose. All rejected attempts remain external, outside accepted chains.

8. Independent Pesachim PE-QA-001 requested a concrete correction where an explicit answer was already linked: review007 sets the question to partial with a nonexhaustive qualification and revises all dependent IDs. The broader answer-set policy question in item2 remains; this local correction does not introduce missing alternatives.
