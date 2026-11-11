# GATE — scoring an idea in a hackathon

Two questions, scored separately because they fail separately:

- **Potential** — does this matter beyond today? (Would a user, a jury, an investor care?)
- **Readiness** — can this team show it working today, with what it has?

A high-potential idea the team cannot demo loses the day. A demo-able idea with no potential wins
nothing that lasts. The quadrant tells the team its next move, not its worth.

**The score orders the shortlist; only evidence moves the idea.** No score, however high, replaces a
riskiest assumption and a kill criterion. No low score kills without a written reason.

## 1. Potential (0–100) — five axes, 0–5 each

Use the anchors, not instinct. One line of reason per axis, with its evidence marker.

| Axis | Weight | Question | Anchors |
|---|---|---|---|
| **P1 · Pain mass** | 0.25 | How much recurring human work, money or risk does the target problem absorb today? | 0 = an occasional annoyance for a few people · 3 = a recurring task with dedicated people in one sector or country · 5 = structural headcount or large spend across thousands of organisations, or a safety or compliance cost |
| **P2 · Innovation void** | 0.15 | How little has this been innovated? | 0 = crowded with funded AI-native products doing exactly this · 3 = legacy digital tools, no AI-native leader · 5 = spreadsheets, email, PDFs, phone, paper |
| **P3 · Verifiable leverage** | 0.20 | How much of the job can AI do now with an output that can be checked deterministically? | 0 = the output is a signed human judgement nothing can check · 3 = partly automatable, mixed checks · 5 = the output is checked by a rule, a test, a reconciliation, a citation to its source |
| **P4 · Defensibility within reach** | 0.20 | What would stop a copy — and can this team build it? | 0 = nothing: a thin layer over a frontier model, copyable in a weekend · 3 = domain data, an ontology or a workflow integration that takes months to rebuild, and the team can reach it · 5 = a proprietary data loop, or a trust or regulatory barrier the team can cross and others cannot |
| **P5 · Unfair access** | 0.20 | What does the team know or have that a model does not? | 0 = no domain insight, no data, no user to talk to · 3 = one teammate with real experience of the problem, or one reachable user · 5 = the team has lived the problem, holds data, or has a buyer who will talk this week |

`Potential = 20 × (0.25·P1 + 0.15·P2 + 0.20·P3 + 0.20·P4 + 0.20·P5)`

P4 counts only barriers **this team can cross**. A barrier nobody in the team can cross (a licence you
will never get, data you cannot obtain) is not a moat: score P4 = 0 and raise `impassable_barrier`.

## 2. Readiness (0–100) — four axes, 0–5 each

| Axis | Weight | Question | Anchors |
|---|---|---|---|
| **R1 · Demo-ability** | 0.30 | Can one core flow work end to end in the build time left? | 0 = needs weeks of data or integration · 3 = the core flow is feasible with mocks at the edges · 5 = the core flow, with the real mechanism, fits in half the time left |
| **R2 · Data in hand** | 0.25 | Is the data the core flow needs available now? | 0 = depends on data you do not have and cannot get today · 3 = a public dataset or realistic synthetic data covers the core flow · 5 = real data, or a sanctioned sample, is in hand |
| **R3 · First evidence today** | 0.20 | Can the riskiest assumption meet a test today? | 0 = no way to test it today · 3 = proxy users in the room or mentors can stress it · 5 = a real target user is reachable today, or a deterministic test exists |
| **R4 · Challenge and team fit** | 0.25 | Does it answer the challenge, and does the team cover the work? | 0 = off-theme, or needs skills nobody has · 3 = on-theme; the team covers building and business with gaps · 5 = squarely on the challenge questions; builder, business owner and researcher roles covered |

`Readiness = 20 × (0.30·R1 + 0.25·R2 + 0.20·R3 + 0.25·R4)`

## 3. Floors — one zero can sink an idea

Applied before the quadrant; a floor overrides a high total.

| Floor | Effect | What to tell the team |
|---|---|---|
| `P3 < 2` → `floor_P3` | Verdict at most NARROW | The AI carries no checkable value: the demo will be a talk. Find the slice where the output can be checked. |
| `P5 < 2` → `median_idea` | Verdict at most NARROW | Every team with the same tools can build this. Find the angle the model does not know. |
| `P1 ≤ 1` → `toy` | Verdict at most TOY | Fine to learn from; hard to win with, and not a venture. |
| `R1 < 2` → `floor_R1` | Verdict at most NARROW | Not demo-able today. Cut to a wedge that is. |
| `R4 < 2` → `floor_R4` | Verdict DROP unless re-framed | Off the challenge, or beyond the team. Re-frame on the challenge or pick another variant. |
| `tarpit` (raised by judgement) | Verdict at most NARROW | Huge, systemic, unsolvable by one team. Pick one moment for one owner. |
| `vitamin` (raised by judgement) | Verdict at most TOY | Nobody is trying to solve it today. |
| `wrapper` (raised by judgement) | Note on P4 | Likely to ship as a native feature of a frontier assistant. |

## 4. Quadrant — what to do next

Thresholds: **Potential ≥ 65** = worth it · **Readiness ≥ 60** = showable today.

| | **Readiness ≥ 60** | **Readiness < 60** |
|---|---|---|
| **Potential ≥ 65** | **BUILD IT** — write the kill criterion, start the walking skeleton now. | **NARROW** — keep the problem, cut to the slice you can show today. Name the missing ingredient (data, a skill, access). |
| **Potential < 65** | **TOY** — buildable, but hard to win or continue. Find the off-distribution angle or gate the next variant. | **DROP** — go to the next variant; write why in one line. |

**Bands, not decimals.** Scores are ordinal. Differences under 10 points are not signal: the team
decides on those, not the second digit.

## 5. Always produced, whatever the verdict

- **Riskiest assumption**: the one that, if false, makes everything else irrelevant. One sentence that
  could be proven false today.
- **Cheapest test today**: who, how, how many minutes.
- **Kill criterion, ex-ante, numeric**: "if fewer than 3 of 5 maintenance technicians we reach say a
  procedure changed under them in the last month, we drop the supersession angle". Not "if it does not
  work".

A verdict without these three is invalid by construction: it is the antidote to cheerleading.

## 6. Eight kill questions (ask the two that bite)

1. What would prove this is a feature of a frontier assistant, not a product?
2. What would prove nobody is trying to solve this today (a vitamin)?
3. What would prove existing tools already solve it well enough?
4. What would prove the user does not care this month?
5. What would prove we cannot show it working end to end today?
6. What would prove the value needs us in the room to explain it?
7. What would prove it does not get better with use or data?
8. What would prove the problem is badly framed (the real owner, buyer or moment is elsewhere)?

## 7. Comparing a shortlist in ten minutes per idea

1. Same intake fields for each idea (SKILL.md §4).
2. Score all nine axes, one line each, markers on every number.
3. Run `scripts/score.py` on all three; apply floors.
4. Put the three verdict blocks side by side. Pick on quadrant first, then on R1 (demo-ability), then
   on P5 (unfair access). Under 10 points apart: the team chooses.

`scripts/score.py` is a self-assessment of the idea, not the jury's rubric (that is in SKILL.md §2a).
Usage:

```bash
python3 scripts/score.py '{"P1":3,"P2":4,"P3":4,"P4":3,"P5":3,"R1":4,"R2":3,"R3":3,"R4":5}'
python3 scripts/score.py ideas.json        # a list of {"name": ..., "axes": {...}, "flags": [...]}
python3 scripts/score.py --self-test
```

## 8. Calibration example (illustrative, not a market claim)

Two ideas for a challenge about AI brains, memory and ontologies for industry.

**A · "The current procedure"** — for maintenance technicians in mid-size machine shops: when a
procedure changes, the agent answers with the version in force and cites who changed it and when.

| Axis | Score | Why |
|---|---|---|
| P1 | 3 | Recurring work with dedicated maintenance teams in one sector `[declared]` |
| P2 | 4 | Binders, PDFs and memory of senior staff `[declared]` |
| P3 | 4 | Answers check against the version in force; supersession is testable |
| P4 | 3 | Domain ontology plus a correction loop; months to rebuild |
| P5 | 3 | One teammate worked in maintenance `[declared]` |
| R1 | 4 | One flow: ask → current procedure with citation → change it → ask again |
| R2 | 3 | Realistic synthetic procedure set with two supersessions |
| R3 | 3 | Mentors and the teammate can stress it today |
| R4 | 5 | Squarely on "how does a memory tell a rule was superseded?" |

Potential 67 · Readiness 76 → **BUILD IT**.

**B · "Chat with your company documents"** — P1 3, P2 0 (crowded), P3 3, P4 0 (a wrapper), P5 1.
Potential 31, flags `median_idea`, `wrapper` → **TOY** at best. The fix is not a better prompt: it is a
different slice (one owner, one moment, one checkable output) or a different team edge.

Do not copy these numbers: score your own idea against the anchors.
