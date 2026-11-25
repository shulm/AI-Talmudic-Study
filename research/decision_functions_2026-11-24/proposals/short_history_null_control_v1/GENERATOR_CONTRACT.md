# Fresh generator and learner contract

Implementation: labs/decision_functions_null_control_v1/engine.py fixture. Initial geometry follows PR15's rotational generator at the pinned base, with fresh PCG64 generator and label seeds from SEEDS.json. No fresh seeds were materialized in planning.

Each world has96 people in48 adjacent pairs; train people0:48,unused48:72,heldout72:96. There are64 semantic families with3 rotational cases each,192 cases,2 features,3 classes. Draw64 angles uniformly on[0,2pi/3); each family adds0,2pi/3,4pi/3. Permute64 groups; first40 are training,next12 unused,last12 query. Support pool is first32 training groups (96 cases). All policies share these exact identities.

Draw48 phases uniformly on[0,2pi), duplicate each with phase+pi, and set u=(cos,sin). Draw48 three-class Normal(0,.12) offsets, repeat in pairs, center each row. V_c=2.5 times the rotation matrix at2pi*c/3; shared base_c=.25*cos(angle-2pi*c/3). Original geometry, shared objective scaling and fitted V units stay unchanged; there is no unit-norm or post-fit basis rescaling. Shared fitting is separate per world/regime/seed and reused across all adaptation policies and schedules within that regime.

The fixed regime order is population,offset,strong,weak,nontransfer,mixed. Labels use independent streams from SeedSequence(label_seed).spawn(6), sample via uniform inverse CDF. This differs prospectively from the historical stream order; historical data are never regenerated. All probabilities and responses are saved privately.

| Regime | logits |
|---|---|
| population | shared base only |
| offset | shared base + paired offset |
| strong | shared base + offset + u V z |
| weak | shared base + offset + .2 u V z (interaction scale .5) |
| nontransfer | strong except heldout query phases independently redrawn |
| mixed | shared base + offset + member*u V z |

For mixed, randomly permute pair indices separately within train,unused,heldout blocks and mark exactly half interaction-active, using the world's geometry RNG after offsets. Pair membership is never supplied to inference. Next draw12 fresh heldout phases for nontransfer, preserve paired opposite phases, and replace only heldout query interaction. Shared training and support remain strong. The learner sees the same z/base and history, with no shift flag or context indicator. The target change is invisible; detecting it is not a primary requirement. It diagnoses the cost of an unidentifiable shift. Comparators have identical permitted inputs.

Learning receives only training people/labels/features for V and heldout support labels/features for b,u. Evaluator alone consumes query labels/oracle. The full source arrays saved for provenance are not arguments to head.fit/adapt. This is a logical boundary, not OS isolation. Replay validates train/support/query joins and whole-group disjointness.

Support schedules retain PR15's SHA256 format short_history_v1|<realization>|<101 or211>|group|<group_id>, with phase replacing group for phase hash. Realization is dev000…dev011 or confirmation000…confirmation095. Sort by digest then integer ID; phase=full unsigned digest mod3; concatenate cyclic triplets, take first16. This admits a partial training group, never a family crossing train/query. Raw Gram eigenvalues [.46875,.53125], absolute tolerance1e-12.

Each B1 uses own history counts plus4 times training-label frequency; B2=softmax(known shared base). B3 at each required offset penalty is fitted once per schedule. M1 uses the same history and shared V with each adaptation penalty pair; average three initialization probabilities within history. Blends use probabilities, not logits; losses average the two histories afterward.

Matched donor is heldout local row xor1. It is a deliberately paired opposite-phase donor, not a random-person population estimand. Compute recipient loss of the saved donor prediction minus own loss. One donor is used, so no multi-donor mixture claim is made. No extra fitting is needed. Every world/schedule/person harm distribution is retained.

Weak results are descriptive only: report gain/common-B3 oracle-gap when gap>1e-8, otherwise undefined; report contrast NRMSE only when oracle contrast square mean>1e-8, otherwise unscaled contrast RMS. There is no .05 weak gate or post-hoc scaled eligibility rule. Nontransfer and mixed receive the same descriptive metrics and no new primary gates.

