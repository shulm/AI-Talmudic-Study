"""Independent public arithmetic audit of PR27; no fitting or private-cache access.

This script does not import delivered analysis code or regenerate scientific data.
It checks saved public scalar/array relationships. It cannot independently
recreate predictions, oracle contrasts, gradients, or K from private artifacts.
"""
from __future__ import annotations

import collections
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(sys.argv[1]).resolve()
RUNS = ROOT / "research/decision_functions_2026-11-24/runs"
NEW = RUNS / "post_es_diagnostics_v1"
OLD = RUNS / "evidence_shrinkage_v1"
OUTPUT = Path(sys.argv[2]).resolve()
ARMS = ("B3", "M1", "FIXED_MIX", "ES", "ES_UNCAPPED")
WORLD = "EFGH"
HISTORY = (101, 211)
checks = collections.Counter()
failures = []
inputs = {}


def read(path):
    raw = path.read_bytes()
    inputs[str(path.relative_to(ROOT))] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def check(group, label, condition, observed=None):
    checks[group] += 1
    if not condition:
        failures.append({"group": group, "label": label, "observed": observed})


def near(group, label, observed, expected, atol=1e-12, rtol=1e-11):
    if isinstance(expected, (tuple, list)):
        check(group, label + ":length", len(observed) == len(expected), len(observed))
        for j, (a, b) in enumerate(zip(observed, expected)):
            near(group, f"{label}[{j}]", a, b, atol, rtol)
    else:
        check(group, label, math.isfinite(observed) and math.isfinite(expected)
              and math.isclose(observed, expected, rel_tol=rtol, abs_tol=atol),
              {"observed": observed, "expected": expected})


def mean(seq):
    seq = list(seq)
    return math.fsum(seq) / len(seq)


a = read(NEW / "ABLATION.json")
r = read(NEW / "RESIDUALS.json")
old = {w: read(OLD / f"{w}_scores.json") for w in WORLD}
evidence = {w: read(OLD / f"{w}_evidence.json") for w in WORLD}
rows = {x["id"]: x for x in a["rows"]}
aggs = {x["id"]: x for x in a["aggregates"]}
check("inventory", "rows", len(rows) == len(a["rows"]) == 16)
check("inventory", "aggregates", len(aggs) == len(a["aggregates"]) == 8)
check("inventory", "row_ids", set(rows) == {
    f"{w}_{h}_{s}" for w in WORLD for h in HISTORY for s in ("active", "inactive")})
check("inventory", "aggregate_ids", set(aggs) == {
    f"{w}_{s}" for w in WORLD for s in ("active", "inactive")})
check("inventory", "qualification_false", a["qualification"] is False)
check("inventory", "designation", a["designation"] == "POST_HOC_EXPOSED_DIAGNOSTIC")

history_failures = []
for rid, row in rows.items():
    check("row", rid + ":designation", row["designation"] == a["designation"])
    check("row", rid + ":methods", set(row["methods"]) == set(ARMS))
    base = row["methods"]["B3"]
    es = row["methods"]["ES"]
    oldrows = {x["id"]: x for x in old[row["real"]]["rows"]}
    for arm, m in row["methods"].items():
        mid = rid + ":" + arm
        near("row", mid + ":gain", m["gain"], base["expected_nll"] - m["expected_nll"])
        near("row", mid + ":mean_excess", mean(m["per_person_excess"]), -m["gain"])
        check("row", mid + ":people", len(m["per_person_excess"]) == 24)
        near("row", mid + ":positive_excess", m["positive_part_excess"],
             mean(max(v, 0) for v in m["per_person_excess"]))
        near("row", mid + ":change_vs_ES", m["per_person_change_vs_ES"],
             [u - v for u, v in zip(m["per_person_excess"], es["per_person_excess"])])
        near("row", mid + ":mean_change", mean(m["per_person_change_vs_ES"]),
             m["expected_nll"] - es["expected_nll"])
        check("row", mid + ":cells", m["contrast_cells"] == 12 * 36 * 3)
        near("row", mid + ":numerator", m["contrast_numerator"],
             m["contrast_mse"] * m["contrast_cells"])
        check("row", mid + ":mse_enclosure", 0 <= m["contrast_mse_lower"]
              <= m["contrast_mse"] <= m["contrast_mse_upper"])
        near("row", mid + ":nll_enclosure", m["expected_nll_enclosure"],
             [m["expected_nll"] - m["expected_nll_error_bound"],
              m["expected_nll"] + m["expected_nll_error_bound"]])
        if row["stratum"] == "active":
            for suffix in ("", "_lower", "_upper"):
                near("row", mid + ":nrmse" + suffix, m["contrast_nrmse" + suffix],
                     math.sqrt(m["contrast_mse" + suffix] / m["contrast_denominator"]))
        else:
            check("row", mid + ":inactive_nrmse", all(
                m["contrast_nrmse" + suffix] is None for suffix in ("", "_lower", "_upper")))
            near("row", mid + ":inactive_denom", m["contrast_denominator"], 0)
            near("row", mid + ":inactive_rms", m["inactive_contrast_rms"], math.sqrt(m["contrast_mse"]))
        if arm != "ES_UNCAPPED":
            om = oldrows[f"{row['history']}_{row['stratum']}_{arm}"]
            for newkey, oldkey in [("expected_nll", "expected_nll"), ("sampled_nll", "nll"),
                                   ("accuracy", "accuracy"), ("brier", "brier")]:
                near("historical", mid + ":" + newkey, m[newkey], om["metrics"][oldkey])
            for key in ("gain", "oracle_loss", "contrast_mse", "per_person_excess", "positive_part_excess"):
                near("historical", mid + ":" + key, m[key], om[key])
            near("historical", mid + ":den", m["contrast_denominator"], om["contrast_den"])
        if row["stratum"] == "inactive" and arm == "ES_UNCAPPED":
            for key in ("expected_nll", "sampled_nll", "accuracy", "brier", "gain", "contrast_mse", "per_person_excess"):
                check("inactive", mid + ":exact_ES_" + key, m[key] == es[key])
    if row["stratum"] == "active" and row["methods"]["ES_UNCAPPED"]["contrast_nrmse"] > .5:
        history_failures.append({"id": rid, "nrmse": row["methods"]["ES_UNCAPPED"]["contrast_nrmse"],
                                 "lower": row["methods"]["ES_UNCAPPED"]["contrast_nrmse_lower"]})

for aid, agg in aggs.items():
    check("aggregate", aid + ":designation", agg["designation"] == a["designation"])
    check("aggregate", aid + ":methods", set(agg["methods"]) == set(ARMS))
    pair = [rows[f"{agg['real']}_{h}_{agg['stratum']}"] for h in HISTORY]
    for arm, m in agg["methods"].items():
        am = [x["methods"][arm] for x in pair]
        mid = aid + ":" + arm
        for key in ("expected_nll", "sampled_nll", "accuracy", "brier", "contrast_mse",
                    "contrast_denominator", "gain", "expected_nll_error_bound"):
            near("aggregate", mid + ":" + key, m[key], mean(x[key] for x in am))
        ex = [mean(x["per_person_excess"][i] for x in am) for i in range(24)]
        near("aggregate", mid + ":person_excess", m["per_person_excess"], ex)
        near("aggregate", mid + ":positive_excess", m["positive_part_excess"], mean(max(v, 0) for v in ex))
        if agg["stratum"] == "active":
            gap = mean(x["methods"]["B3"]["expected_nll"] - x["methods"]["B3"]["oracle_loss"] for x in pair)
            near("aggregate", mid + ":recovery", m["recovery"], m["gain"] / gap)
            for suffix in ("", "_lower", "_upper"):
                near("aggregate", mid + ":contrast" + suffix, m["contrast_nrmse" + suffix],
                     math.sqrt(mean(x["contrast_mse" + suffix] for x in am) / m["contrast_denominator"]))
        else:
            check("aggregate", mid + ":inactive_nrmse", m["contrast_nrmse"] is None)
    for source, target in zip(ARMS[1:], ARMS[2:]):
        delta = agg["ordered_contrast_changes"][source + "_to_" + target]
        near("aggregate", aid + ":delta_mse_" + source, delta["mse_change"],
             agg["methods"][target]["contrast_mse"] - agg["methods"][source]["contrast_mse"])
        if agg["stratum"] == "active":
            near("aggregate", aid + ":delta_nrmse_" + source, delta["nrmse_change"],
                 agg["methods"][target]["contrast_nrmse"] - agg["methods"][source]["contrast_nrmse"])

for w in WORLD:
    pos = aggs[w + "_active"]["methods"]["ES_UNCAPPED"]
    neg = aggs[w + "_inactive"]["methods"]["ES_UNCAPPED"]
    expected = {"gain": pos["gain"] >= .05, "recovery": pos["recovery"] >= .5,
                "contrast": pos["contrast_nrmse"] <= .5, "inactive": -neg["gain"] <= .01,
                "numerical_enclosure_informative": pos["contrast_nrmse_upper"] < .5 or pos["contrast_nrmse_lower"] > .5}
    check("reference", w, a["reference_only"][w] == expected)

changes = underflows = 0
for w in WORLD:
    ev = evidence[w]["rows"]
    check("evidence", w + ":n", len(ev) == 96)
    for er in ev:
        near("evidence", w + ":mean_seed_e_" + er["id"], math.exp(er["log_e"]),
             mean(math.exp(v) for v in er["seed_log_e"].values()))
        check("evidence", w + ":supports_" + er["id"], sum(er["counts"]) == 16)
    for h in HISTORY:
        for s in ("active", "inactive"):
            picked = [x for x in ev if x["history"] == h and x["active"] == (s == "active")]
            check("evidence", f"{w}_{h}_{s}:n", len(picked) == 24)
            hs = [.009 * math.expm1(x["log_e"]) if x["log_e"] > 0 else 0 for x in picked]
            weights = [-math.expm1(-v) for v in hs]
            caps = sum(v > math.log(10) for v in hs)
            under = sum(math.exp(-v) == 0 for v in hs)
            row = rows[f"{w}_{h}_{s}"]
            near("evidence", row["id"] + ":weight", row["uncapped_mean_weight"], mean(weights))
            check("evidence", row["id"] + ":caps", row["changed_weights"] == caps)
            check("evidence", row["id"] + ":underflows", row["baseline_underflow"] == under)
            if s == "inactive":
                check("evidence", row["id"] + ":inactive_unchanged_rule", caps == 0)
            changes += caps
            underflows += under
check("evidence", "total_changes", changes == a["active_weight_changes"] == 153)
check("evidence", "total_underflows", underflows == a["baseline_coefficient_underflow_rows"] == 12)

res = {x["id"]: x for x in r["rows"]}
expected_res = set()
heads = ("B3", "M1_11", "M1_29", "M1_47")
for w in WORLD:
    for h in HISTORY:
        for head in heads:
            expected_res.update(f"{w}_support_{h}_{head}_48/p{p}" for p in range(48))
    for batch in (1, 7):
        for head in heads:
            expected_res.update(f"{w}_numerical_101_{head}_{batch}/p{p}" for p in range(batch))
check("residual", "inventory", set(res) == expected_res and len(r["rows"]) == 1664)
for rid, row in res.items():
    dim = 3 if row["model"] == "B3" else 5
    d = [.6] * 3 + [.06] * (dim - 3)
    check("residual", rid + ":gradient_dimension", len(row["gradient"]) == dim)
    calc_r = math.sqrt(math.fsum(g * g / penalty for g, penalty in zip(row["gradient"], d)))
    near("residual", rid + ":R", row["R"], calc_r, atol=1e-18)
    near("residual", rid + ":R_used", row["R_used"], row["R"] + row["R_allowance"], atol=1e-18)
    check("residual", rid + ":reported_gradient_agreement", row["gradient_comparison"] <= 1e-12 * max(1, *map(abs, row["gradient"])))
    allowance = 1e-12 * max(1, *map(abs, row["gradient"])) * math.sqrt(math.fsum(1/v for v in d))
    near("residual", rid + ":R_allowance", row["R_allowance"], allowance, atol=1e-20)
    check("residual", rid + ":K_dimension", len(row["K"]) == 36)
    near("residual", rid + ":prob_bound", row["probability_bound"], [.5 * k * row["R_used"] for k in row["K"]], atol=1e-18)
    near("residual", rid + ":log_bound", row["log_probability_bound"], [math.sqrt(2) * k * row["R_used"] for k in row["K"]], atol=1e-18)
    if row["model"] == "B3":
        near("residual", rid + ":B3_K", row["K"], [1/math.sqrt(.6)] * 36)

expected_batches = {f"{w}_{head}_{batch}_p{p}" for w in WORLD for head in heads for batch in (1, 7) for p in range(batch)}
check("batch", "inventory", {x["id"] for x in r["batch_comparisons"]} == expected_batches and len(r["batch_comparisons"]) == 128)
for row in r["batch_comparisons"]:
    rid = row["id"]
    p = row["person"] - 144
    full = res[f"{row['real']}_support_101_{row['model']}_48/p{p}"]
    small = res[f"{row['real']}_numerical_101_{row['model']}_{row['batch']}/p{p}"]
    near("batch", rid + ":sum_bound", row["per_query_bound"], [x + y for x, y in zip(full["probability_bound"], small["probability_bound"])], atol=1e-18)
    near("batch", rid + ":max_diff", row["probability_difference_max"], max(row["per_query_difference"]), atol=1e-18)
    near("batch", rid + ":max_bound", row["summed_probability_bound_max"], max(row["per_query_bound"]), atol=1e-18)
    covered = all(d <= b + 1e-12 for d, b in zip(row["per_query_difference"], row["per_query_bound"]))
    check("batch", rid + ":covered", row["covered"] is True and covered)

receipt = {
    "status": "PASS" if not failures else "FAIL",
    "source_commit": "16ef28b105ff6c28ee3f822b1409f076fa895318",
    "checks": dict(checks),
    "total_checks": sum(checks.values()),
    "failures": failures,
    "public_input_sha256": inputs,
    "uncapped_history_failures": history_failures,
    "uncapped_aggregate_contrast": {w: aggs[w + "_active"]["methods"]["ES_UNCAPPED"]["contrast_nrmse"] for w in WORLD},
    "original_ES_aggregate_contrast_lower": {w: aggs[w + "_active"]["methods"]["ES"]["contrast_nrmse_lower"] for w in WORLD},
    "max_published_personal_R": max(x["R"] for x in r["rows"]),
    "max_published_batch_difference": max(x["probability_difference_max"] for x in r["batch_comparisons"]),
    "scope": "Public scalar arithmetic and published residual relationships only; no model fit, no original fixture generation, no private-cache access. Saved gradients, interaction K, probabilities and per-cell contrast bounds cannot be independently recreated without private artifacts. Bounds are analytic expressions evaluated in float64, not directed-rounding certificates. Check count is arithmetic assertions, not independent studies or verifier groups.",
}
OUTPUT.write_text(json.dumps(receipt, indent=2, allow_nan=False) + "\n")
print(json.dumps({k: v for k, v in receipt.items() if k != "public_input_sha256"}, indent=2))
if failures:
    raise SystemExit(1)
