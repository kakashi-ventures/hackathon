---
name: hack-rubric-check
description: >
  Scores a hackathon team's project against the five jury criteria of the 14 November event before the
  pitch deadline, names the weakest criterion and the one thing to do about it. Reads the team project
  and the economic model in Control8 (MCP server `hack`); writes nothing. Use when the team says
  "check our project against the jury rubric", "/hack-rubric-check", "rubric check", "how would the
  jury score us", "what is our weakest criterion", "are we ready for the jury", "what is missing for
  16:45", "come ci valuta la giuria".
metadata:
  author: kakashi-ventures
  version: "0.1.0"
  companion-of: 8hack
---

# Rubric check

A self-check against the jury's own rubric, run by the team's Claude. It is not the jury's score: the
jurors score on the day, each one on their own. What this skill gives the team is the criterion that
costs them most points while there is still time to move it.

The rubric, its weights and the deadlines are in the facts block at the end of this file. They are
generated from the code that runs the event, so use them as they are and never write a weight from
memory.

## 1. Read what the jury will read

The team project slug starts with `hack-` and is on the team's `/me`. Ask for it once if you do not
have it. Then, read only:

1. `get_project_context` with the slug: the pages, the artifacts and their genres. Note whether there is
   an artifact of genre `pitch`, when it was published, and whether its text has the GitHub repo link.
   If there is one, read it with `get_artifact`.
2. `get_economic_model` with the slug: the headline the jury card shows (annual revenue, CAC payback)
   and the coverage gaps.
3. `list_materials`: is there a pitch deck (`kind: 'pitch_deck'`)?
4. `get_document` for `8hack-start` and `8hack-check`, if they exist: the idea, the riskiest assumption,
   what the last checkpoint said works.

Then ask the team, in one message, what Control8 cannot see: does the core flow run end to end on the
demo machine, what is mocked, was the idea video uploaded, and which models and AI tools they used.

## 2. Score each criterion

Score 1 to 5, one line of reason each, with a marker on every fact: `[verified: what you read]`,
`[declared]` (the team said it) or `[unverified]`. Use the anchors; when the evidence sits between two,
take the lower.

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| Fit (memory, ontologies or AI brains) | The challenge is a label on a generic app | The project touches one of the challenge questions | The core flow answers one challenge question with a working mechanism (see `../8hack/references/event-2026-11-14.md`, The challenge) |
| Technical quality (what works on the day) | Slides or a static mock | The flow is clickable but the core is mocked | The core flow runs end to end with the real mechanism, and a check set prints a score |
| Problem and impact (a real problem for an industry) | Nobody named, no cost | A named segment and pain, the cost is a guess | One owner, one moment, a cost with a source or a real quote |
| Business case (as checked at the financial validation) | No economic model in Control8 | A model with a priced revenue line, volumes or acquisition missing | Revenue lines with price and volume, channels with cost per lead and conversion, a payback the team can defend |
| Demo clarity | Over time, demo at the end | On time, loose order | Something working on screen in the first 90 seconds, finishes on time |

The rows name the criteria as the jury sees them. If a name in the facts table differs, the facts
table wins.

## 3. Compute, do not estimate

Weighted mark = Σ (weight × score) / 100, with the weights of the facts table. Write the arithmetic
in one line so the team can check it.

The weakest criterion is the one with the most points to win back: the largest (5 − score) × weight.
On a tie, pick the one the team can still move before the pitch deadline. A criterion that cannot move
any more (the idea video after its deadline, for example) is reported, not chosen.

## 4. Before the pitch deadline

Check each hand-in against the facts block and mark it done, missing or late:

- A `pitch` artifact on the team project, published before the deadline. Only the most recent one
  before the deadline counts.
- The GitHub repo link, in the `pitch` artifact or on the project page («Add repo»).
- The economic model saved in Control8, with its headline. If it is missing or thin, hand over to the
  `hack-economic-model` skill.
- The models and AI tools the team used, named in the pitch. The rules ask for it (§7).
- The pitch deck in the materials, if the team has slides.

## 5. Output

```
RUBRIC CHECK · <team project> · T-<hh:mm> to the pitch deadline
| Criterion | Weight | Score | Why (marker) |
| …         | …      | …     | …            |
Weighted mark: <the arithmetic> = <n.n> / 5
Weakest: <criterion>, <points to win back> points to win back
Do now (<= 30 min): <one action, who does it>
Hand-in: pitch <done|missing|late> · repo <…> · economic model <…> · models and AI tools <…> · deck <…|none>
```

Then stop. If the team asks how to fix the weakest criterion, the 8hack references cover each one:
`../8hack/references/pitch-and-judging.md` for the demo and the pitch,
`../8hack/references/spof-and-build.md` for what works on the day, `../8hack/references/moat.md` and
`../8hack/references/event-2026-11-14.md` for fit.

## 6. Rules

- Read only. This skill writes nothing to Control8.
- Never raise a score because the team is confident. A `[declared]` fact can support a 3, not a 5.
- Never tell the team what the jury will decide. Say what the jury will read and what is missing.
- If 8hack is not installed next to this skill, the `../8hack/` paths will not open: install it with the
  same command that installed this one.

## 7. The event facts

<!-- 8hack:facts:start -->
_Generated by `pnpm skills:hack-sync` from the code that runs the event (Control8). Do not edit between the markers: change the code and run the sync. Times are Rome time. If the organisers say otherwise on the day, they win._

**Before the day.** Sign in and connect your agent to Control8 (MCP server `hack`) by Friday 13 November, 22:00.

**Schedule of 14 November** (`code` = enforced by Control8, `runbook` = the organisers' plan for the day):

| Time | What | Source |
|---|---|---|
| 09:30–10:20 | Welcome and check-in | runbook |
| 10:00 | Rules | runbook |
| 10:05 | Team matching | runbook |
| 10:15 | Talks: Venture Building, Memory and AI | runbook |
| 10:30 | Teams are final; hacking starts | runbook |
| 10:30–12:30 | Mentor calls open (call from /me) | code |
| 12:15 | Video upload closes | code |
| 12:15 | Teams stop choosing or changing their track | code |
| 12:30 | Projection of the videos, then voting until the close | runbook |
| 13:00–13:30 | Lunch | runbook |
| 13:30 | Phase II: the teams chosen by the organisers continue | runbook |
| 14:00–16:30 | Mentor calls open (call from /me) | code |
| 16:00 | Draw of the show-off order | runbook |
| 16:30 | Financial validation | runbook |
| 16:45 | Pitch delivery deadline | code |
| 17:05–18:15 | Show-off: one 5:00 slot per team, demo and questions | runbook |
| 18:30 | Announcement | runbook |

**Video.** Upload it on `/hackathon/live`, not via MCP, by 12:15: one MP4 file (`video/mp4`), at most 50 seconds and 25 MB, about the idea only — no team name, no member's name, voice or face. Before 12:15 a new upload replaces the previous one; after 12:15 no video is added or replaced, for anyone.

**Public vote.** The videos are projected one by one as «Video N». Afterwards every participant can rewatch every video except their own team's and give each one a score from 1 to 5, one per video, until an organiser closes the vote; jurors and staff watch.

**Pitch delivery.** By 16:45 publish an artifact of genre `pitch` on your team's project. The jury reads the most recent `pitch` your team published before 16:45; one published later does not count: if it is your only one, the jury sees no delivery. The jury card also shows your economic model's headline (annual revenue, CAC payback), saved with `update_economic_model`.

**Materials.** Any file your team wants the jury and the organisers to see (PDF, slides, images, data, archives; not executables; up to 100 MB each) goes in your team's materials, from the project page or from your agent: `request_material_upload` gives a signed URL, you PUT the file there (`curl -X PUT -H 'Content-Type: <mime>' --data-binary @file '<upload_url>'`), then `register_material` with the same path, kind and file name. `list_materials` lists them, `get_material` gives a download link. The **pitch deck** has its own canvas (`kind: 'pitch_deck'`): the latest one is the current one, earlier ones stay as versions; your team can replace it until 16:45, then it is read-only. Only your team, the jury and the organisers can read your materials.

**Track and repo.** Until 12:15 your team chooses, changes or drops its track (no track = free project) on its project page or on `/me`; after that an organiser changes it. Put your GitHub repo link in your `pitch` artifact, or add it with «Add repo» on your team's project page: the jury opens it from there. Keep the repo private until 16:45, with the jury invited (Control8 warns the organisers about a public one).

**Your track in your agent.** `get_project_context` on your team project returns your track under `track`: the brief, the reading list and the market research. Read it before you choose the idea.

**Jury rubric.** Each juror scores each criterion 1 to 5; a team's mark is the weighted mean across jurors. Ties are broken on Fit; a tie on that too stays a declared tie.

| Criterion | Weight |
|---|---|
| Fit | 25 |
| Technical quality | 25 |
| Problem and impact | 25 |
| Business case | 20 |
| Demo clarity | 5 |

**Model credit.** $25 per team at the start, in dollars. In phase II the organisers raise the credit of the teams they choose. Every member of your team reads the key on their own `/me` («Show the key»): keep it in `.env`, never in the repo.
<!-- 8hack:facts:end -->
