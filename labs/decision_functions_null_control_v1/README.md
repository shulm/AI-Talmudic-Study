# Null-control study laboratory

Proposal and commands: `research/decision_functions_2026-11-24/proposals/short_history_null_control_v1/`.

`design.py` defines the finite candidate set, seed banks, exact stage contracts, selection and inference. `engine.py` implements the new generator, component fits and saved-evidence replay. `run.py` manages pre-fit/selection checkpoints, exclusive attempts, resource stops and the end-to-end workflow. `checks.py` uses analytic examples; `integration_checks.py` substitutes mock fit/objective/score functions and reduced world counts. Neither test produces research evidence. `audit_history.py` checks the public historical results and compacts the completed original-array replay receipt.

No scientific execution is authorized by the planning assignment. Use the implemented authorization/hash guards only after the owner separately authorizes the exact reviewed design. Never commit generated arrays or parameters.
