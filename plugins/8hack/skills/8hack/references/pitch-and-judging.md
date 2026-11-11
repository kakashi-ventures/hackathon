# PITCH and MENTOR — how the room is won, and how it is judged

## 1. What juries reward, and what they penalise

Consistent across judges' accounts of many events (sources at the end):

| Rewarded | Penalised |
|---|---|
| A clearly stated problem the room can feel | Skipping the problem because the tech "speaks for itself" |
| One flow that works end to end | Five half-built features; scope creep |
| Something working on screen early (about 90 seconds in) | The demo at the very end, or missing |
| Honesty about what works, what is mocked, what is next | Talking about features that do not exist |
| A memorable "now possible" moment, built from the product working | Decoration that shows nothing |
| Naming the model and how its output was checked | "Our AI" with no word on evaluation |
| Clear language a non-expert follows | Jargon, dense slides |
| Finishing on time | Running long and losing the ending |

Juries differ: some weigh technical depth, some business viability, some UX. Read the official rubric
and score yourselves against it at the last checkpoint. On 14 November it is in SKILL.md §2a.

## 2. Proxy rubric (only where no rubric is published)

The 14 November jury scores with the official rubric in SKILL.md §2a: score yourselves on that one.
This proxy is for events that do not publish a rubric. 1 to 5 per criterion.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| **Problem and customer** | Generic market, no owner | A named segment and pain, some vagueness | One sentence: specific owner, job, moment |
| **Evidence** | Synthetic or none; assumptions unchanged | Some real input, weak link to the assumption | Real quotes or real data; the riskiest assumption confirmed, refuted or changed, and the team says which |
| **Working prototype** | Slides or a static mock | Clickable, but the core is mocked | The core flow works end to end and exercises the riskiest assumption |
| **Depth on the challenge** | The challenge is a label | Touches the challenge's questions | Answers one of the challenge's questions with a working mechanism and a check set |
| **AI-native method** | Cannot say what was delegated or checked | Delegation clear, verification vague | What agents did, what humans checked, what an agent got wrong and how it was caught |
| **Pitch** | Over time, demo late | On time, loose structure | On time, demo early, honest about unknowns, ends on the next test and its number |

## 3. Pitch outline

Default four minutes; compress to three by halving the method and the ask. Hard stop. On 14 November
the slot is 5:00 with the questions (SKILL.md §2a): use the 3-minute column.

| 4 min | 3 min | Beat | What to say |
|---|---|---|---|
| 0:00–0:30 | 0:00–0:25 | **Problem and owner** | "For [owner] who [moment], [the pain, with a real number or quote]." One sentence, then the moment. |
| 0:30–1:30 | 0:25–1:20 | **Demo, early** | The core flow, narrated as the user's experience. Land the "now possible" moment. |
| 1:30–2:15 | 1:20–1:55 | **Evidence** | Two real quotes or one real number. Which assumption was confirmed, refuted or changed. How many real people. |
| 2:15–2:50 | 1:55–2:25 | **Why it is hard to copy** | The differentiator in the stack, what is built, what is the plan (`moat.md` §5). |
| 2:50–3:30 | 2:25–2:45 | **Method** | Model and why; how outputs were checked (the check set score); one thing an agent got wrong and how it was caught. |
| 3:30–4:00 | 2:45–3:00 | **Next test** | The experiment for next week, its threshold, the kill criterion. What you would need: an intro, a week, a dataset. |

Do not: open with the stack; show sign-up or settings; read slides; quote synthetic users; say "we
validated"; run over.

Slides, if any: one idea each, large text (30 pt and up), high contrast, screenshots over paragraphs.
One title slide and one closing slide with the next test are often enough; the demo is the pitch.

## 4. Demo script

Write it as a numbered list of clicks and sentences. For each step: what the presenter clicks, what
appears, the one sentence said. Mark the "now possible" moment. Mark where the backup video takes over
if the live demo fails, and the sentence to say when switching ("here is the same run, recorded at
<hh:mm>").

Narrate what the judges cannot see: the check set behind the answer, the supersession that just
happened, the citation. Do not narrate what they can see.

## 5. Q&A sheet (prepare answers in one line each)

- Who exactly is the user, and who pays?
- What is real and what is mocked in what we just saw?
- Which model, why that one, and how did you check its output?
- What did the agent get wrong today?
- Who else does this, and why would the user switch?
- What is hard to copy?
- What happens if [the riskiest assumption] is false?
- What would you build or test next week?
- What is the number that would make you stop?

## 6. Rehearsal

- Rehearse out loud, timed, at least twice; once in front of someone who has not seen the project.
- Cut content, never pace. If it runs long, a beat goes, not words per minute.
- Memorise four or five transition phrases, not the script.
- The presenter runs the demo at least once without the builder touching the laptop.

## 7. MENTOR mode — for mentors and judges using 8hack on a team

### At a checkpoint (5 minutes per team)

1. Ask for the six-line status (SKILL.md §5.6).
2. Score the official rubric (SKILL.md §2a; the proxy one of §2 only at events without one), 1–5,
   one line of reason each.
3. Look for the two failures that sink teams: no kill criterion, and a core that is still mocked at
   the second checkpoint.
4. Give feedback with the protocol below. Agree on one cut with the team.

### Feedback protocol (2 minutes)

1. One strength, in one sentence.
2. One question the team did not answer.
3. One thing to test next, with a number.

The score starts the conversation; it is not a verdict on the people.

## Sources

Public practice consulted on 28/10/2026:
- [How to win a hackathon: notes from the judging table — JetBrains (June 2026)](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)
- [10 tips to help you rock your next hackathon demo — AngelHack](https://angelhack.com/blog/10-tips-to-help-you-rock-your-next-hackathon-demo/)
- [Land your hackathon pitch — Xero Developer](https://devblog.xero.com/land-your-hackathon-pitch-a-playbook-for-winning-the-room-8b327de726ca)
- [Builder's guide, ch. 15: how judging works — BuilderBase](https://intercom.help/builderbase/en/articles/14836129-builder-s-guide-ch-15-how-judging-works)
- [Judging guide — Devfolio](https://guide.devfolio.co/docs/guide/judging)

KVA's AI-native venture-building sprint (rubric, pitch outline, feedback protocol) is the base of §2,
§3 and §7.
