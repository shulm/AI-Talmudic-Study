# Pre-fit engineering record

All entries below preceded scientific optimizer calls and the public pre-fit checkpoint.

- Zero-fit unit/preflight checks passed: objective/gradient equivalence, finite differences, support permutation invariance, uninformative identity, grouping/pairs/support geometry, donor aggregation, independent bootstrap and failure paths.
- First full zero-fit integration attempt failed closed on a Windows path-serialization mismatch: private parameter manifest keys used backslashes while the exact contract used forward slashes. Fixed manifest serialization to POSIX relative paths. The command receipt remains in commands/ with exit 1.
- Second full integration attempt passed using zero-parameter stubs and only legacy generator seeds 20261125/2718 in temporary directories. No C/D scientific labels were scored, no optimizer ran, and no scientific slots were consumed. It validated a complete predictive failure as VERIFIED_COMPLETE with qualification=false. Temporary mock record totals were 196; they are not real optimizer attempts and are not mixed into the experiment ledger.
- Exact expected saved-evidence comparisons: 17,038. Both complete-run and predictive qualification checks require all declared prerequisites. No early-stop path is allowed by this protocol.

All test process resource receipts, including the unsuccessful test, count in cumulative sampled usage. This is not a scientific retry.

Additional pre-fit hardening: required protocol-derived archive shapes and the exact private parameter-file set. One import-only attempt caught a syntax typo in that shape contract; it performed no pipeline or optimizer work. Fixed before the final successful full zero-fit integration and final unit check. Both unsuccessful command receipts remain in the resource ledger. Duplicate row/ID sets are explicitly rejected.
