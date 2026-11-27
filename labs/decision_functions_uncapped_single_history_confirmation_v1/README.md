# Uncapped single-history confirmation v1

Authoritative assignment: ae74b9e5604b4905804d25b296097467f6794f14, PR31. Read the copied CONFIRMATION_PROTOCOL.md and DESIGN.json. No tuning stage is introduced.

Required computations run through `supervise.py --output-root <public-root> python .../cli.py <stage> --output-root <public-root>`. Stages: prepare, preflight, seal, execute, verify, report, recover-report. Preflight needs a fresh isolated `--private-root`; execution needs a distinct fresh scientific private root. Verification takes the saved private root and a fresh `--receipt`. Reporting/recovery takes an existing verification receipt. Supplemental fixed arithmetic tests have their own supervised entry point. No automatic resume exists.

Publish the sealed implementation commit and post/read back both issue2 and draft-PR comments and frozen files. PUBLICATION.json binds the exact commit and freeze hash. Execution refuses changed sources or an existing scientific root. Scientific and mock work use the same boundary.run and supervisor, with durable starts and protected terminal fields. Interruptions terminate and wait for children. Reporting resources and final terminal are written after the report child exits; supervisor/final metadata overhead and sampling gaps remain disclosed limitations.

The verifier never invokes a generator or optimizer. It reconstructs support schedules only, and independently expresses count partitions, scalar NLL, anchored contrasts and personal gradients. Complete IDs and before/after hashes are required. A passing exit code alone is insufficient. Private responses, vectors, traces and per-cell arrays remain outside Git. Reporting recovery cannot reconstruct missing scientific evidence. Historical results remain unchanged.
