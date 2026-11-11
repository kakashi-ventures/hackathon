---
name: hack-venture-gates
description: >
  Checks a hackathon team's idea against KVA's venture gates, in order: problem, customer, alternatives,
  solution, edge, today, evidence. Names the weakest gate and the smallest move that would pass it. It
  is the method KVA uses for its own ventures (8gate), compressed for a one-day event. Use when the team
  asks "which gate is our idea weakest on?", "venture gates", "is this a venture or a feature", "could
  this be a company", "check our idea against the gates", "su quale gate siamo deboli".
metadata:
  author: kakashi-ventures
  version: "0.1.0"
  companion-of: 8hack
---

# Venture gates

A venture idea fails in a predictable order. If nobody has the problem, the customer does not matter.
If there is no customer, the solution does not matter. So the gates are checked in order, and the
weakest gate is the first one that does not hold, even when a later one looks strong.

This skill reuses the 8hack scoring, which is KVA's 8gate method compressed for a hackathon. Read these
files from the 8hack skill installed next to this one before scoring:

- `../8hack/references/scoring.md`: the nine axes (P1–P5, R1–R4), their anchors and the floors.
- `../8hack/references/landscape.md`: the landscape card and the native-feature check.
- `../8hack/references/audience-uvp-usp.md`: segment, persona, UVP.

If those paths do not open, 8hack is not installed: install it with the same command that installed
this skill.

## 1. Read the idea

The team project slug starts with `hack-` and is on the team's `/me`. Then:

1. `get_project_context` with the slug.
2. `get_document` on `8hack-start` and `8hack-check`, if they exist: problem, team, plan, riskiest
   assumption, kill criterion.
3. `HACK.md` at the root of the team's repo, if you can read it: the canvas.

If you do not have the problem, how people handle it today and who suffers and who pays, ask for those
three in one message before checking any gate (8hack intake, items 1 to 3).

## 2. The gates, in order

| # | Gate | The question | It holds when | Score with |
|---|---|---|---|---|
| 1 | Problem | Who loses what, at which moment, and how do they cope today? | A named owner, a kind of loss with a rough number, the moment, the workaround; not a vitamin, not a tarpit | P1, 8hack canvas Q1 |
| 2 | Customer | Who has it first, and who pays? | One early-adopter segment, buyer and user named, a bottom-up count with its source, ten of them reachable next week | audience-uvp-usp §1 |
| 3 | Alternatives | What do they use instead, and could a frontier assistant already do it? | A landscape card with the status quo and the native-feature check, every fact marked | P2, landscape card |
| 4 | Solution | What changes for the user, and can the output be checked? | A UVP in the 8hack format, an output a rule or a test can check | P3 (floor below 2), canvas Q3 |
| 5 | Edge | What does this team know or hold that a model does not, and what would stop a copy? | Unfair access the team really has; a barrier the team can cross | P5 (floor below 2), P4 |
| 6 | Today | Can the core flow run end to end today, on the challenge? | Demo-able in the time left, with data in hand, on one of the challenge questions | R1, R2, R4 (floors below 2) |
| 7 | Evidence | What would prove it wrong, and how is it tested today? | Riskiest assumption, cheapest test today and a numeric kill criterion, all written | R3, scoring §5 |

Score the nine axes against the anchors in `scoring.md`, one line of reason each, with a marker on
every fact: `[verified: source]`, `[declared]`, `[unverified]`. Compute Potential and Readiness with the
8hack script, never in prose:

```bash
python3 ../8hack/scripts/score.py '{"P1":3,"P2":4,"P3":4,"P4":3,"P5":3,"R1":4,"R2":3,"R3":3,"R4":5}'
```

Then give each gate one status:

- **holds**: the question has an answer backed by at least one `[verified]` fact, and no floor of its
  axes is hit;
- **weak**: there is an answer, but only `[declared]` or `[unverified]`;
- **fails**: no answer, or a floor is hit.

The weakest gate is the first one that **fails**. If none fails, it is the first one that is **weak**.

## 3. Output

```
VENTURE GATES · <idea> · T-<hh:mm>
1 Problem       <holds|weak|fails>  <one line, marker>
2 Customer      …
3 Alternatives  …
4 Solution      …
5 Edge          …
6 Today         …
7 Evidence      …
Potential <n>/100 · Readiness <n>/100 · flags <…>   (from score.py)
Weakest gate: <n name>. What would pass it: <the evidence, concretely>
Do now (<= 30 min): <one move, who does it>
```

If the team wants to keep it, write the table into the Gate section of `HACK.md`. Nothing is written to
Control8: the organisers read `8hack-start` and `8hack-check`, which 8hack keeps.

## 4. Rules

- Kill ideas, never people. Every "fails" names the evidence that would turn it into "holds".
- A synthetic persona or a model's opinion is not evidence. It can sharpen a question, never pass a gate.
- The gates order the work; they do not decide for the team. If the team overrides a verdict, write the
  override and its reason in `HACK.md` and carry on.
- The scores here are a self-assessment of the idea, not the jury's rubric. For the jury's criteria use
  the `hack-rubric-check` skill.
