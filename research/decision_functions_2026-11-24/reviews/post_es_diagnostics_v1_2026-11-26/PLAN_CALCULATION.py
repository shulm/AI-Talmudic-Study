#!/usr/bin/env python3
"""Deterministic design arithmetic only: no data, worlds, fitting, or simulation.

Run explicitly, for example:
    python PLAN_CALCULATION.py --output PLAN_CALCULATION.json

The script selects exact binomial critical values using rational arithmetic,
checks SciPy's floating-point tails, and calculates Clopper-Pearson bounds.
Only the requested output JSON is written. No project modules are imported.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path
import platform

import scipy
from scipy.stats import beta, binom


ALPHA = Fraction(1, 20)
NULL_RELIABILITY = Fraction(4, 5)
PLANNING_RELIABILITY = Fraction(9, 10)
TARGET_POWER = Fraction(4, 5)
PRIMARY_N = 82
COMPARISON_NS = (16, 24, 32, 48, 82, 96)
AGREEMENT_TOLERANCE = 5e-14


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def exact_tails(n: int, probability: Fraction) -> list[Fraction]:
    """Return P[Binomial(n,p) >= k], k=0,...,n+1, exactly."""
    a, b = probability.numerator, probability.denominator
    denominator = b**n
    accumulated = 0
    tails = [Fraction(0)] * (n + 2)
    for k in range(n, -1, -1):
        accumulated += comb(n, k) * a**k * (b - a)**(n - k)
        tails[k] = Fraction(accumulated, denominator)
    require(tails[0] == 1, "Exact binomial probabilities do not sum to one")
    return tails


def fraction_record(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def design(n: int) -> tuple[dict, Fraction, Fraction]:
    null_tails = exact_tails(n, NULL_RELIABILITY)
    alternative_tails = exact_tails(n, PLANNING_RELIABILITY)
    critical = next((k for k in range(n + 1) if null_tails[k] <= ALPHA), None)
    if critical is None:
        return {
            "worlds": n,
            "critical_successes": None,
            "nonempty_rejection_region": False,
            "size_at_null": 0.0,
            "power_at_planning_alternative": 0.0,
            "one_sided_95pct_cp_lower_at_critical": None,
            "meets_target_power_exactly": False,
            "scipy_tail_max_absolute_difference": 0.0,
        }, Fraction(0), Fraction(0)

    size = null_tails[critical]
    power = alternative_tails[critical]
    scipy_size = float(binom.sf(critical - 1, n, float(NULL_RELIABILITY)))
    scipy_power = float(binom.sf(critical - 1, n, float(PLANNING_RELIABILITY)))
    agreement = max(abs(float(size) - scipy_size), abs(float(power) - scipy_power))
    require(agreement <= AGREEMENT_TOLERANCE, "Exact/SciPy tail mismatch")
    require(critical == 0 or null_tails[critical - 1] > ALPHA,
            "Critical value is not the smallest permitted value")
    lower = float(beta.ppf(float(ALPHA), critical, n - critical + 1))
    inversion_error = abs(float(binom.sf(critical - 1, n, lower)) - float(ALPHA))
    require(inversion_error <= 1e-12, "Clopper-Pearson inversion mismatch")
    return {
        "worlds": n,
        "critical_successes": critical,
        "nonempty_rejection_region": True,
        "size_at_null": float(size),
        "power_at_planning_alternative": float(power),
        "one_sided_95pct_cp_lower_at_critical": lower,
        "meets_target_power_exactly": power >= TARGET_POWER,
        "scipy_tail_max_absolute_difference": agreement,
        "cp_inversion_absolute_error": inversion_error,
    }, size, power


def calculate() -> dict:
    search = [design(n)[0] for n in range(1, PRIMARY_N + 1)]
    eligible = [row["worlds"] for row in search if row["meets_target_power_exactly"]]
    require(eligible and min(eligible) == PRIMARY_N,
            "The proposed n is not the minimum reaching the target power")
    primary, exact_size, exact_power = design(PRIMARY_N)
    require(primary["critical_successes"] == 72, "Unexpected primary cutoff")
    require(primary["one_sided_95pct_cp_lower_at_critical"] >= .8,
            "Primary confidence bound does not clear the target")
    primary.update({
        "exact_size_fraction": fraction_record(exact_size),
        "exact_power_fraction": fraction_record(exact_power),
        "decision": "Qualify the primary reliability claim only if S >= 72 of 82, with all separately declared completeness and numerical gates satisfied.",
    })
    comparisons = [design(n)[0] for n in COMPARISON_NS]
    all_rows = search + comparisons
    shared = PRIMARY_N * 3
    personal = PRIMARY_N * 2 * 4 * 48
    require((shared, personal) == (246, 31488), "Optimization inventory mismatch")
    return {
        "schema_version": 1,
        "status": "DETERMINISTIC_PLANNING_ONLY",
        "scope": {
            "worlds_generated": 0,
            "shared_fits_executed": 0,
            "personal_solves_executed": 0,
            "scientific_data_loaded": False,
            "random_sampling_used": False,
            "project_modules_imported": False,
            "new_scientific_evidence": False,
            "description": "Exact design arithmetic and deterministic special-function evaluation; not a scientific run or authorization to execute one.",
        },
        "environment": {
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "scipy_version": scipy.__version__,
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "parameters": {
            "one_sided_alpha": float(ALPHA),
            "null_reliability_upper_boundary": float(NULL_RELIABILITY),
            "planning_alternative_reliability": float(PLANNING_RELIABILITY),
            "target_power": float(TARGET_POWER),
            "primary_unit": "One independent world with its predeclared primary balanced 16-case history H1",
            "event": "All four frozen active-gain, recovery, contrast, and inactive-degradation gates are jointly satisfied in H1",
            "histories_nested_within_world": True,
            "iid_requirement": "A common predeclared law for generator, labels, masks, and outcome-blind balanced support schedules across worlds",
            "power_alternative_is_planning_assumption_not_estimate": True,
        },
        "primary_design": primary,
        "minimum_search": {
            "inclusive_range": [1, PRIMARY_N],
            "candidate_count": len(search),
            "selection_rule": "For each n choose the smallest integer k with exact P_0.8(S>=k)<=0.05, then require exact P_0.9(S>=k)>=0.80",
            "smallest_eligible_n": min(eligible),
            "every_smaller_n_fails_target_power": all(not row["meets_target_power_exactly"] for row in search[:-1]),
            "rows": search,
        },
        "comparison_designs": comparisons,
        "optimization_inventory": {
            "status": "PROPOSED_NOT_EXECUTED",
            "worlds": PRIMARY_N,
            "shared_starts_per_world": 3,
            "shared_start_ids": [11, 29, 47],
            "histories_per_world": 2,
            "heldout_people_per_history": 48,
            "personal_heads_per_history": ["B3", "M1_11", "M1_29", "M1_47"],
            "shared_fits_per_world": 3,
            "personal_solves_per_world": 384,
            "total_shared_fits": shared,
            "total_b3_personal_solves": PRIMARY_N * 2 * 48,
            "total_m1_personal_solves": PRIMARY_N * 2 * 3 * 48,
            "total_personal_solves": personal,
            "additional_optimization_for_derived_controls": 0,
            "scientific_retries": 0,
        },
        "numerical_validation": {
            "critical_values_selected_with_exact_rational_arithmetic": True,
            "minimum_sample_size_selected_with_exact_rational_arithmetic": True,
            "maximum_scipy_tail_absolute_difference": max(row["scipy_tail_max_absolute_difference"] for row in all_rows),
            "tail_agreement_tolerance": AGREEMENT_TOLERANCE,
            "maximum_cp_inversion_absolute_error": max(row.get("cp_inversion_absolute_error", 0.0) for row in all_rows),
            "cp_bounds_are_float64_special_function_results": True,
            "monte_carlo_error": "None: no simulation or resampling",
        },
        "confidence_bound": {
            "kind": "One-sided 95% Clopper-Pearson lower bound",
            "formula_for_positive_S": "Beta^{-1}(0.05; S, n-S+1)",
            "value_at_S_zero": 0.0,
            "not_a_two_sided_95pct_lower_bound": True,
        },
        "sources": [
            "https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbino.htm",
            "https://doi.org/10.6028/NIST.TN.2119",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="Explicit JSON output path; existing content is replaced")
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n",
                           encoding="utf-8")
    print(json.dumps({"output": str(args.output), "status": result["status"],
                      "worlds": PRIMARY_N, "critical_successes": 72,
                      "minimum_n_verified": True}))


if __name__ == "__main__":
    main()
