# Implemented commands and checkpoints

Run from this branch's repository root with existing Python,numpy,scipy,psutil. No new dependency install or paid tool is needed. All raw outputs must be outside the repository. Only the first two commands below belong to this planning assignment.

```powershell
python labs/decision_functions_null_control_v1/checks.py
python labs/decision_functions_null_control_v1/run.py contracts
```

After separate owner authorization, an authorization JSON must contain owner_authorized_execution:true and source_hashes equal to run.pins(). This records authorization; creating a file is not a substitute for obtaining it. Protocol must be PROTOCOL_FROZEN and exact hashes independently reviewed. Nothing in the present request authorizes scientific execution.

Set $studyRoot to a new private path and $studyAuth to the authorized JSON path. Commands are implemented:

```powershell
python labs/decision_functions_null_control_v1/run.py freeze --root $studyRoot --authorization $studyAuth
python labs/decision_functions_null_control_v1/run.py execute --root $studyRoot --authorization $studyAuth --phase dev --index 0
python labs/decision_functions_null_control_v1/run.py select --root $studyRoot --authorization $studyAuth
python labs/decision_functions_null_control_v1/run.py execute --root $studyRoot --authorization $studyAuth --phase confirmation --index 0
python labs/decision_functions_null_control_v1/run.py verify --root $studyRoot --authorization $studyAuth
```

The execute stage accepts each exact zero-based index in the frozen phase budget. Select refuses incomplete development. Confirmation refuses a missing/changed selection freeze or a declared stop. Do not dispatch these individually during routine execution: the implemented end-to-end command handles every index,selection,stop,confirmation and final replay:

```powershell
python labs/decision_functions_null_control_v1/run.py all --root $studyRoot --authorization $studyAuth
```

Resume skips complete world receipts; an attempted but incomplete world cannot be retried. Exclusive attempt files consume a world slot. Failed execution terminates the orchestrator and leaves incomplete evidence. There is no automatic merge or person-directed message.

Before owner-authorized execution, publish the exact reviewed pre-fit commit. Selection checkpoint is an immutable local hash binding before confirmation; publish its hash/decision with final evidence. Private arrays are never committed. Public final report should contain aggregate metrics,resource totals,freeze hashes and verification state; redact individual rows from publication.

Historical replay used the unchanged PR15 verify.py with --private-root pointing to its original cache and --output-root pointing to a fresh copy of its public evidence excluding verification.json. Do not run it against the original public results directory, because its receipt is create-once.
