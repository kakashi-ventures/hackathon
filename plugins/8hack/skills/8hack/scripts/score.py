#!/usr/bin/env python3
"""8hack GATE scorer: Potential, Readiness, floors and quadrant from axis scores.

The model proposes the axis scores; this script does the arithmetic, so a model never computes
its own total in favour of its own conclusion. Rubric: references/scoring.md.

This is a self-assessment of the idea, not the jury's rubric: the jury scores with the official
rubric in SKILL.md §2a.

Usage:
  python3 score.py '{"P1":3,"P2":4,"P3":4,"P4":3,"P5":3,"R1":4,"R2":3,"R3":3,"R4":5}'
  python3 score.py ideas.json   # a list of {"name": str, "axes": {...}, "flags": [...]}
  python3 score.py --self-test

Judgement flags you may pass in "flags": tarpit, vitamin, wrapper, impassable_barrier.
"""
import json
import sys

POTENTIAL = {"P1": 0.25, "P2": 0.15, "P3": 0.20, "P4": 0.20, "P5": 0.20}
READINESS = {"R1": 0.30, "R2": 0.25, "R3": 0.20, "R4": 0.25}
POTENTIAL_OK = 65
READINESS_OK = 60
JUDGEMENT_FLAGS = {"tarpit", "vitamin", "wrapper", "impassable_barrier"}

# Verdicts ordered from most to least permissive; a cap can only move a verdict down this list.
ORDER = ["BUILD IT", "NARROW", "TOY", "DROP"]


def _weighted(axes, weights):
    missing = [k for k in weights if k not in axes]
    if missing:
        raise ValueError(f"missing axes: {', '.join(missing)}")
    for k in weights:
        v = axes[k]
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 5:
            raise ValueError(f"{k} must be an integer 0-5, got {v!r}")
    return round(20 * sum(weights[k] * axes[k] for k in weights))


def _cap(verdict, cap):
    return verdict if ORDER.index(verdict) >= ORDER.index(cap) else cap


def score(axes, flags=()):
    unknown = set(flags) - JUDGEMENT_FLAGS
    if unknown:
        raise ValueError(f"unknown flags: {', '.join(sorted(unknown))}")
    if "impassable_barrier" in flags and axes.get("P4") != 0:
        raise ValueError("impassable_barrier means P4 = 0 (a barrier the team cannot cross is not a moat)")

    potential = _weighted(axes, POTENTIAL)
    readiness = _weighted(axes, READINESS)

    if potential >= POTENTIAL_OK:
        verdict = "BUILD IT" if readiness >= READINESS_OK else "NARROW"
    else:
        verdict = "TOY" if readiness >= READINESS_OK else "DROP"

    raised = list(flags)
    caps = []
    if axes["P3"] < 2:
        raised.append("floor_P3"); caps.append("NARROW")
    if axes["P5"] < 2:
        raised.append("median_idea"); caps.append("NARROW")
    if axes["P1"] <= 1:
        raised.append("toy"); caps.append("TOY")
    if axes["R1"] < 2:
        raised.append("floor_R1"); caps.append("NARROW")
    if axes["R4"] < 2:
        raised.append("floor_R4"); caps.append("DROP")
    if "tarpit" in flags:
        caps.append("NARROW")
    if "vitamin" in flags:
        caps.append("TOY")
    for c in caps:
        verdict = _cap(verdict, c)

    # A capped NARROW on a low-potential idea stays where the quadrant put it (TOY/DROP):
    # caps lower a verdict, they never raise one.
    return {
        "potential": potential,
        "readiness": readiness,
        "verdict": verdict,
        "flags": raised or ["ok"],
        "bands": f"P{potential // 10 * 10}s R{readiness // 10 * 10}s",
    }


def _line(name, axes, result):
    p = " · ".join(f"{k}={axes[k]}" for k in POTENTIAL)
    r = " · ".join(f"{k}={axes[k]}" for k in READINESS)
    head = f"{name}: " if name else ""
    return (f"{head}Potential {result['potential']}/100 [{p}]   Readiness {result['readiness']}/100 [{r}]\n"
            f"  Flags: {', '.join(result['flags'])}   Verdict: {result['verdict']}")


def _self_test():
    ok = True

    def check(label, cond):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + label)
        ok = ok and cond

    a = score({"P1": 3, "P2": 4, "P3": 4, "P4": 3, "P5": 3, "R1": 4, "R2": 3, "R3": 3, "R4": 5})
    check("calibration A is 67/76 BUILD IT", (a["potential"], a["readiness"], a["verdict"]) == (67, 76, "BUILD IT"))
    b = score({"P1": 3, "P2": 0, "P3": 3, "P4": 0, "P5": 1, "R1": 5, "R2": 4, "R3": 3, "R4": 3}, ["wrapper"])
    check("calibration B is 31 and TOY with median_idea", b["potential"] == 31 and b["verdict"] == "TOY" and "median_idea" in b["flags"])
    c = score({"P1": 5, "P2": 5, "P3": 1, "P4": 5, "P5": 5, "R1": 5, "R2": 5, "R3": 5, "R4": 5})
    check("floor P3 caps a perfect idea at NARROW", c["verdict"] == "NARROW" and "floor_P3" in c["flags"])
    d = score({"P1": 5, "P2": 5, "P3": 5, "P4": 5, "P5": 5, "R1": 5, "R2": 5, "R3": 5, "R4": 1})
    check("off-challenge drops even a perfect idea", d["verdict"] == "DROP")
    e = score({"P1": 1, "P2": 5, "P3": 5, "P4": 5, "P5": 5, "R1": 5, "R2": 5, "R3": 5, "R4": 5})
    check("pain mass 1 caps at TOY", e["verdict"] == "TOY" and "toy" in e["flags"])
    f = score({"P1": 4, "P2": 4, "P3": 4, "P4": 4, "P5": 4, "R1": 4, "R2": 4, "R3": 4, "R4": 4}, ["tarpit"])
    check("tarpit caps BUILD IT at NARROW", f["verdict"] == "NARROW")
    g = score({"P1": 2, "P2": 2, "P3": 2, "P4": 2, "P5": 2, "R1": 1, "R2": 1, "R3": 1, "R4": 2})
    check("a cap never raises DROP", g["verdict"] == "DROP")
    full = {**{k: 3 for k in POTENTIAL}, **{k: 3 for k in READINESS}}
    for bad, label in (({**full, "P1": 6}, "out of range rejected"), ({"P1": 3}, "missing axes rejected"),
                       ({**full, "R2": 2.5}, "non-integer rejected")):
        try:
            score(bad)
            check(label, False)
        except ValueError:
            check(label, True)
    try:
        score(full, ["impassable_barrier"])
        check("impassable_barrier requires P4 = 0", False)
    except ValueError:
        check("impassable_barrier requires P4 = 0", True)
    return 0 if ok else 1


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    if argv[1] == "--self-test":
        return _self_test()
    arg = argv[1]
    try:
        data = json.loads(arg)
    except json.JSONDecodeError:
        with open(arg, encoding="utf-8") as fh:
            data = json.load(fh)
    items = data if isinstance(data, list) else [{"name": "", "axes": data, "flags": []}]
    for item in items:
        axes = item.get("axes", item)
        flags = item.get("flags", [])
        try:
            print(_line(item.get("name", ""), axes, score(axes, flags)))
        except ValueError as err:
            print(f"{item.get('name', 'idea')}: not scored — {err}")
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
