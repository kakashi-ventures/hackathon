---
name: hack-plain-voice
description: >
  Rewrites a hackathon team's 3-minute demo script and slides so they read and sound as written by a
  person, not generated: the problem before the system, a real person in the first sentence, no triads,
  no "not X but Y" slogans, no lists of noun-colon bullets. Keeps every fact at the level it has. Use
  when the team says "rewrite our 3-minute demo script in plain voice", "plain voice", "this sounds like
  AI", "make the pitch sound human", "tighten the demo script", "fix our slides", "sembra scritto
  dall'AI", "riscrivi lo script della demo".
metadata:
  author: kakashi-ventures
  version: "0.1.0"
  companion-of: 8hack
---

# Plain voice

A juror who has heard ten generated pitches in a row spots the eleventh in two sentences, and from
then on listens for tells instead of for the idea. This skill takes the team's script and slides and
removes what gives them away, with the problem first and the product after.

On 14 November the show-off slot is 5:00 with the questions: the demo script gets about 3 minutes.
The beats and their timing are in `../8hack/references/pitch-and-judging.md` §3 (the 3-minute column)
and §4 (demo script). Read them first, from the 8hack skill installed next to this one.

## 1. Get the text, then the specifics

The script or the slides come from one of these:

- pasted in the chat;
- the team's `pitch` artifact: `list_artifacts`, then `get_artifact`;
- the pitch deck in the team's materials: `list_materials`, then `get_material` for the download link.

Before rewriting, check you have at least one of each. If one is missing, ask for it. Do not fill the
gap with a general description of the problem: that is exactly the text that sounds generated.

- **A moment**: who did what, when, and what went wrong.
- **A cost**: minutes, euros, a document redone, a wrong answer sent to someone.
- **What the demo shows**: the one thing on screen the jury should remember.

## 2. Diagnose, then rewrite

Read the whole text once and write a short diagnosis, at most six lines: what to keep, what to fix in
place, what to rewrite, which facts are missing. Then rewrite only what the diagnosis flagged.

Structure comes first:

- Open on the person and the moment, in the user's words. The product name comes after, as the answer
  to that moment.
- Show something working early (pitch-and-judging §3). Narrate what the jury cannot see; do not narrate
  what is on the screen.
- One sentence of theory is enough. Cut the architecture tour.
- End on what the team would test next and the number that would stop them, not on a slogan.

Then sentences:

- People are the subjects. "The maintenance lead found the old procedure" beats "outdated knowledge
  causes errors".
- Verbs do the work: "we check" instead of "the verification of".
- One idea per sentence. Where a dash or a semicolon wants to go, start a new sentence.
- Specific over general: "€300 a month" over "a modest cost". If the specific is missing, ask.
- Spoken text: short sentences, no parentheses, numbers said the way a person says them.

## 3. Tells to remove

- Triads used for rhythm (three adjectives, three pillars). Keep three only if each one adds something.
- Contrast slogans: "it's not X, it's Y", "the question is no longer X". Keep one only if it corrects a
  real misunderstanding of the jury.
- Lists where every item is a bold noun, a colon and one sentence of the same length. Turn them into
  prose, or vary them.
- Announcing: "it's worth noting", "importantly", "at its core", "imagine a world where", "let's dive
  in". Say the thing.
- Restating: a closing line that repeats the section.
- Slides with a headline, a subtitle and a tagline each. One sentence per slide, large, or a screenshot.
- Other languages have their own tells ("si tratta di", "permette di", "non solo… ma anche", "a 360
  gradi", chains of "inoltre"). Write in the language the team will pitch in.

Do not overcorrect: no fake casual tone, no slang, no emoji. Keep the technical terms the jury uses.

## 4. Facts stay at their level

Keep apart what works, what is mocked, what is planned and what was measured, and write each at its own
level. "Prototype" does not become "product". "We talked to four maintenance leads" does not become "we
validated". A percentage needs its base, or it goes. Never add a number, a quote or a customer the
original does not have.

The rules ask each team to say which models and AI tools they used (§7). If the script does not say it,
add one plain sentence and ask the team to fill in the names.

## 5. Output

1. The diagnosis (six lines at most).
2. The rewritten script as numbered beats, each with its start time, what is on screen and what is said,
   and a word count per beat. At a speaking pace of about 130 words a minute, 3 minutes is about 390
   words: if the script is longer, cut a beat, never speak faster.
3. The slides, one line each: the sentence or the screenshot.
4. The facts you still need from the team.

Then read the result once more for the tells above and fix what is left.

Do not publish anything by yourself. If the team wants the new version in Control8, it becomes their
`pitch` artifact only when it is final and before the pitch deadline: the jury reads the most recent
`pitch` published before it.
