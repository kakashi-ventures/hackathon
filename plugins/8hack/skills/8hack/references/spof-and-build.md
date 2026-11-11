# SPOFs, build order, demo safety (canvas Q5, Q6, BUILD)

## 1. Team roles (assign in the first ten minutes)

| Role | Owns |
|---|---|
| **Builder** | Drives the coding agent; keeps the demo machine runnable at all times |
| **Business owner** | Problem, UVP, kill criterion, the pitch; owns the clock |
| **Researcher** | Landscape scan, interviews, the evidence log; keeps every claim marked |
| **Presenter** | Named at kick-off (often the business owner); collects pitch material all day |

Everyone prompts. In a team of two, the builder also keeps the verification log and the business owner
also researches. Choose the presenter for clarity, not seniority.

## 2. Single points of failure (Q5)

### Table

```
| # | Component | How it fails | Likelihood L/M/H | Impact on demo/thesis | Mitigation | Owner | By |
|---|-----------|--------------|------------------|-----------------------|------------|-------|----|
```

At least three demo SPOFs and two venture SPOFs. Re-read the table at each checkpoint.

### Catalogue — demo SPOFs (today)

| Component | Typical failure | Mitigation |
|---|---|---|
| External model API | Rate limit, outage, slow response on stage | Cache responses for the demo path; set timeouts; keep a second provider or a smaller model ready |
| Model credits | Burnt on long agent loops before the core works | Budget credits per phase; stop runaway loops; cache; use the cheapest model that passes the check set |
| Venue network | Wifi drops during the pitch | Local fixtures; the demo runs offline from the laptop; a recorded run saved locally |
| One laptop | Battery, crash, wrong display adapter | Second machine with the repo cloned and the demo tested; charger; adapter checked at lunch |
| One person who knows the deploy | They are presenting or away | Write `RUN.md` (three commands); a second person runs it once before the freeze |
| Live data or scraping | Source changes or blocks you | Snapshot the data you need into the repo early |
| Auth, sign-up, onboarding | Eats minutes on stage, breaks | Not built. Start the demo already logged in, with seeded data |
| Long model calls | 20 seconds of silence on stage | Pre-compute, stream, or cut the call from the live path |
| A fragile dependency | Version conflict at 16:00 | Pin versions; no new libraries after the last checkpoint |
| Secrets | A key committed to a public repo is abused | `.env` + `.gitignore`; rotate any key that was ever committed |

### Catalogue — venture SPOFs (beyond today)

| Component | Typical failure | What to write |
|---|---|---|
| **The riskiest assumption** | It is false | Always venture SPOF #1, with its kill criterion |
| One data source | Access withdrawn, licence changes, quality too low | Alternative sources; what the product does without it |
| One model or platform vendor | Price, policy, capability or availability changes | Models behind an interface you control; tested fallback |
| One regulatory gate | The use is regulated or needs certification | Name the rule; what part of the product sits outside it |
| One customer type | The only segment that cares is too small | Second segment hypothesis, untested |
| One key person | The domain insider leaves | What knowledge must be written down |

## 3. Build order (Q6)

Each item states **what it proves**, **done when** (a deterministic check, not a feeling) and a **time
box**. Default order for most ideas:

| # | Build | Proves | Done when | Time box |
|---|---|---|---|---|
| 1 | Walking skeleton: input → stubbed core → output, end to end, fake data | The flow exists and runs where you will demo | Someone outside the builder clicks through it | ~15% of the time |
| 2 | The riskiest piece, for real, on a small real or realistic dataset | The mechanism works at all | The skeleton calls it and returns real output | first half of the core phase |
| 3 | Check set: 10–20 cases with expected answers | The output is right, not just produced | The script runs and prints a score you report honestly | 30–45 min |
| 4 | The "now possible" moment | The contrast the jury will remember | It runs three times in a row without a hiccup | 30 min |
| 5 | Fallbacks: cached path, recorded run, offline page | The demo survives the room | The demo runs with wifi off | 30 min, before the freeze |

**Never in the build list**: login, settings, payments, admin, multi-tenant, a landing page beyond one
screen, a second user role, "nice to have" integrations. Everything not in the table goes to a **cut
list** in `HACK.md`, so the team can see what it chose not to do.

**For memory and ontology projects**, decide the identity of each entity (what makes two records the
same thing) before writing code. Duplicates that appear "only in some cases" come from an identity
decided too late, and they are expensive to undo.

## 4. Prototype brief for the coding agent

Paste it, filled in, as the first message to the coding agent or app builder. Plain language, one flow.

```
Build a small web app prototype. Disposable, for a live demo in <N> hours. Use the simplest stack
you can run immediately; no auth, no payments, no database unless in-memory or a local file.

User: <role, context, device>
Job to be done: <one sentence from the user's point of view>
The single core flow (3–6 numbered steps):
1. …
2. …
3. …
The core mechanism to make real (everything else may be mocked): <the riskiest piece>
Data: <real sample path, or realistic fake data: names, dates, amounts; local context where relevant>
What the user should feel at the end of the flow: <the moment that tests the riskiest assumption>
Check set: <path to the expected answers>; add a script that runs them and prints the score.
Out of scope: everything else. No settings, no login, no admin.
Style: readable on a projector, one accent colour, large text.
Secrets: read keys from environment variables; never write them into files.
When done: tell me how to run it in three commands, and list three things you were unsure about or
made up.
```

Read the "three things you were unsure about" before building on top. That list is where the agent
got it wrong.

## 5. Check set and deterministic verification

A check set is the cheapest proof that the output is right, not merely produced:

- 10–20 cases, each with the input and the expected answer, written by a human before running.
- Include the hard cases your challenge asks about. For memory: a rule that was superseded, two
  agents writing conflicting facts, a question whose answer must cite its source, a question the
  system should refuse to answer because it does not know.
- A script runs them and prints `passed / total`. Report the number as it is. "14/20, and here is
  what fails" is credible; "it works great" is not.
- When a result surprises you, read the raw input and output of a few runs before changing the
  prompt or blaming the model. Harness failures look like model failures.

## 6. Verification log (the AI-native method)

Juries increasingly ask what the agents did and how you checked it. Keep four lines per milestone in
`HACK.md`:

```
| When | What an agent produced | What a human checked, and how | What the agent got wrong, and how we caught it |
```

The pitch uses one row of this log. "The agent invented a field in the data model; the check set caught
it before lunch" is the strongest sentence about method you can say on stage.

## 7. Demo safety (from the last checkpoint on)

- **Feature freeze** at the last checkpoint: only the demo path gets work after it.
- Script the demo path click by click; pre-fill forms; seed the data; start logged in.
- Mock or pre-compute anything slow; set timeouts on every network call.
- Record a clean run before the final push; keep it on the laptop, not only in the cloud.
- Run the whole demo with wifi off once.
- Push to the remote. Tag the commit you demo.
- Close every app that could notify on screen; set the display to mirror; zoom the browser.

## 8. Re-planning when the clock slips

At each checkpoint, if the core is not working:

1. Cut scope, never pace: drop features from the flow, keep the flow whole.
2. Replace the riskiest piece's real version with a smaller real version (fewer documents, one rule,
   one entity type), not with a mock. A mocked core is a demo of a promise.
3. If the riskiest piece cannot work today, pivot the demo to what you learned: show the check set
   failing and why. Honesty about a failed test scores better than a fake success.
