# Planning check history

All entries concern zero-fit engineering. No failed check caused a scientific retry.

1. The first11-test analytic suite had two failures because its fabricated positive example had gain .3 and oracle gap .7, below the declared .50 recovery requirement. The implementation correctly rejected it. The mock positive gain was corrected to .4; the failed receipt remains ZERO_FIT_CHECKS_INITIAL_FAILED.json. The subsequent11-test run passed.
2. The first full mocked integration stopped at source-freeze verification because the primary writer edited run.py while the test was running. The guard correctly detected changed source hashes. The temporary mocked run was discarded; no scientific artifacts existed.
3. The next mocked integration exposed a genuine JSON round-trip defect: common_losses used float dictionary keys in memory and string keys after serialization. Exact selection replay rejected the mismatch. The implementation now emits string keys from the outset.
4. Final integration tests use a reduced two-world mock budget to exercise both stop and selected-confirmation branches. Production12-development and24–96-confirmation counts are checked separately by the analytic suite. Mock selection scores and fit/objective replacements cannot be interpreted as numerical research results.

Historical saved-array replay and public arithmetic audit succeeded separately. Their receipts identify exactly what was executed; the original execution's resource totals remain reported historical evidence.
