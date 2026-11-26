# Deterministic partial corpus assembly

See [the release entry point](../bavli_dataset_runs/run_20261125_01/releases/INTEGRATION_20261126_01.md) for scope, commands and limitations. `capture.py` freezes production state under each job lock. `assemble.py` verifies the frozen capture and separately bound policy, validates original sources and replays proposals, then emits deterministic read-only derivatives. It cannot promote producer state or grant task eligibility.
