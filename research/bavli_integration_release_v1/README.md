# Deterministic partial corpus assembly

See [the current partial release](../bavli_dataset_runs/run_20261125_01/releases/INTEGRATION_20261127_02_REVIEW015.md) for exact versions, commands and limitations. Prior releases remain immutable. `capture.py` freezes producer state under per-job locks; `assemble.py` verifies source, schema, ownership and replay before generating deterministic derivatives. It cannot promote producer state or grant task eligibility.
