# Planning review and verification

Date: 2026-11-24. Scope: documentation and the unexecuted protocol template.

## Evidence inspected

- Current GitHub repository metadata, root instructions, README, handoff, open PR list and Git tree.
- Baseline commit and source-file identities recorded in `SOURCE_SNAPSHOT.json`.
- Primary papers and official dataset/model documentation cited in the source register.
- The prior attribution proposal in draft PR #1, to distinguish its objective from this continuation.

The repository was observed as public, with current instructions recording that as the user's decision. Its source acquisition now covers four scholar-pair indexes. This planning review did not re-audit their contents or turn occurrence counts into training examples.

## Independent AI review

Two separate AI review passes examined protocol/evaluation and source/data definitions. No human scholarly review is claimed. Material corrections incorporated:

1. The primary task predicts a person's decision from a problem and history; old speaker-attribution thresholds do not carry over.
2. The first full pilot uses DICES350 and its actual three-class human target, with chatbot `response` kept distinct from the human answer.
3. A text-plus-personal-intercept baseline distinguishes label tendency from question-dependent effects.
4. Support histories and budgets match across methods; held-out people drive the few-shot comparison.
5. Macro-person uncertainty preserves within-person normalization under sparse intersections; repeated support draws are not independent people.
6. The primary 16-support endpoint cannot silently disappear if a secondary budget is unavailable.
7. MultiPref remains audit-only in the first assignment; its future candidate-choice model needs a complete separate contract.
8. Personal class intercepts apply to fixed label inventories; changing answer menus require feature-based scoring.
9. The scope includes a freeze checkpoint and one final evaluation without an unnecessary owner-approval pause.
10. Negative primary results, lack of history effects and true implementation invalidity have distinct meanings.

## Verification for the planning package

The publishing agent checks JSON syntax and required template fields, consistency of primary endpoint/seeds/model grids, relative document links against new files and the baseline tree, absence of unresolved coordination placeholders, additive root navigation, and remote content/blob identities after upload. It also verifies that pre-existing source and code blobs are unchanged outside the two navigation documents.

These are documentation and preservation checks. No dataset acquisition, synthetic fixture execution, embedding generation, fit, bootstrap, test evaluation, or scientific performance measurement has been executed by this planning task. The proposed resource limits are not measured requirements.

Publication commit and live PR/issue links are recorded externally in the coordination issue; a commit cannot contain its own hash.
