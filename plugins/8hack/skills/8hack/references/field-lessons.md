# Field lessons

Lessons KVA learned the hard way on real projects, rewritten for a hackathon. Each one has a
**signature** (how to recognise it) and a **countermeasure** (what to do). Apply the countermeasure
when the signature matches; these are observations, not orders.

| Lesson | Signature in a hackathon | Countermeasure |
|---|---|---|
| **The model gets the direction and misses the level** | The demo shows a number the model produced (a score, a percentage, a forecast) as if it were measured | Treat model output as a hypothesis and an interpretation layer, never as a measurement. If a number matters, compare it with real data and show the comparison |
| **Harness failures disguise themselves as model failures** | A surprising result and nobody has looked at the raw input and output | Read a few raw runs before changing the prompt or switching models. Size the budget (tokens, timeouts) before interpreting results |
| **A number is not communicated before it exists** | A preliminary result goes on a slide | Separate measured from indicative in every sentence. If it was not measured today, say "we expect", or cut it |
| **Other people's numbers and your own need the same provenance check** | A market figure repeated by the team and never traced to its source | Before a number reaches the pitch, trace it to the primary source and date it, including numbers your own tools produced |
| **What is obvious to the builder is not obvious to the user** | Only the builder has clicked through the demo | Someone who did not build it clicks the whole flow before the freeze; watch where they hesitate |
| **Work that stays on the disk does not exist** | The remote repo does not reflect the day's work | Push at every milestone, incomplete work on a branch. Version the data the result depends on |
| **Adversarial review finds what the normal flow does not** | The only check is the person who wrote it | Ten minutes of red team before the freeze: one teammate (or 8hack in falsifier mode) attacks the demo and the claims |
| **"Re-read critically before closing" has a measured return** | A task closed the moment it compiles | Make the re-read a named step before the freeze and before the pitch |
| **Bugs that raise no exception are the most expensive** | Plausible-looking output, fewer results than expected, no errors | Compare outputs with expected answers (the check set), not with "it did not crash" |
| **An entity's identity is decided before it is coded** | Duplicates that appear "only in some cases"; two records the system calls the same and people do not | Write the identity key of each entity (for memory and ontology projects especially) before writing code |
| **The brief is raw input, not a specification** | The challenge text or a provided dataset is used as gospel | Check it for internal contradictions; find the operational source (often a spreadsheet, not the formal document) |
| **Security defects come from configuration, not code** | A key in a config file, a permissive setting in a template, a secret in the history of a public repo | `.env` in `.gitignore` from the first commit; a pre-commit secret scan if you have one; rotate any key that was ever pushed |
| **The cost of generation is designed before writing, not after** | Credits run out mid-afternoon; a video or audio asset budgeted after it was scripted | Split credits by phase (ideation, proof of concept) at kick-off; cache; use the cheapest model that passes the check set |
| **Practices that pay off immediately, with their cost declared** | A freeze or a rule adopted without saying what it costs, and dropped at the first annoyance | When you freeze features or adopt a rule, write what it costs you ("no new library after 16:00 means no charts") |
