# Target audience, UVP and USPs (canvas Q3, Q4, Q7)

Work in this order: **audience → UVP → USPs**. A UVP written before the segment is chosen ends up
promising everything to everyone.

## 1. Target audience (Q7)

### Segment

One segment, two at most. Pick it on the adoption curve:

| Kind | Who | Why it matters today |
|---|---|---|
| **Early adopter** | Has the pain, knows it, already hacks a workaround, has budget or authority | Your first users and your best interviews. Pick this one. |
| Early majority | Has the pain, waits for proof and references | Your market later; do not design for them today |
| Late | Changes only when forced | Ignore for the hackathon |

For each segment: a label, the adopter kind, a **bottom-up size** with its source, and why this
segment first.

### Persona (one or two per segment)

Five questions, answered from real conversations where possible:

| Field | Question |
|---|---|
| **Who** | Role, context, the tools they use every day |
| **Job** | What they need to get done, in their words |
| **Trigger** | The moment that makes them look for a solution |
| **Where** | Where you find ten of them next week (community, association, event, channel) |
| **Objection** | What makes them say no: liability, habit, data, price, their boss |

Plus up to three **pains** (what hurts today) and three **gains** (what would make their week
better). Pains and gains are what the USPs connect.

### Buyer and user

Name both when they differ: the maintenance technician uses it, the plant manager pays; the
researcher uses it, the department or the funder pays. Solving for the user while the buyer is
someone else is the most common trap in B2B ideas. Name the payer before the prototype.

### Evidence in a hackathon

- Synthetic personas: use them to stress-test the interview script and to find blind spots. They are
  not evidence and never go on a slide as quotes.
- Proxy users in the room (other participants, mentors): good for the user's side of the story, weak
  on willingness to pay. Say who they are standing in for.
- One real person in the segment, reached by phone or message during the day, beats ten proxies.

Interview rules (the Mom Test): talk about their life, not your idea; ask about specific past
behaviour, not opinions about the future; talk less. Never ask "would you use…?" or "would you
pay…?". Ask "tell me about the last time…", "what did you do about it?", "what did it cost you?".

After each conversation, in two minutes: three verbatim quotes; the riskiest assumption confirmed,
refuted or unclear; one surprise.

## 2. UVP — the one promise (Q3)

### Format

`For [segment] who [moment and pain], [product] [outcome] — unlike [current alternative] — because
[mechanism].`

- **Segment and moment** come from Q7 and Q2.
- **Outcome** is what changes for the user, in their words: a job done, a risk removed, an hour saved.
- **Current alternative** comes from the landscape card, usually the status quo.
- **Mechanism** is why it works; it is the only place where technology appears.

### Tests

1. **Jargon test**: read everything before "because" aloud to someone outside the team. If it means
   nothing without the mechanism, it is a mechanism pitch; rewrite the outcome.
2. **Uniqueness test**: could the best alternative say the same sentence truthfully? If yes, the
   UVP is not unique; sharpen the segment or the outcome.
3. **Falsifiability test**: name the observable behaviour that would show the promise matters, and the
   number below which you stop believing it.

### Making it testable

```
UVP: For … who …, … — unlike … — because …
Hypothesis: We believe [segment] will [observable behaviour] because [reason].
Test today: [who, how, minutes]
Kill criterion (written now): if [metric] < [number] by [time], we [narrow the segment | change the
outcome | drop the idea].
Result: [pending | passed | killed] — [what we observed]
```

Behaviour beats stated intent. Good observable behaviours for a hackathon day: a real user describes
the pain unprompted in the last month; asks to see it again; sends you a real example to try; names
someone else who has the problem. Polite enthusiasm is not a result.

## 3. USPs — the proofs behind the promise (Q4)

Three to five, each tied to the UVP and to one pain of the persona.

| Field | Content |
|---|---|
| **Pain** | The specific pain, from Q7 |
| **Resolves** | How the product removes it |
| **Gain** | What the user gets, in their words |
| **Proof** | What the demo shows, or the evidence; if neither exists today, the USP is `[unverified]` |
| **vs** | The alternative from the landscape card that this beats |
| **Angle** | outcome · mechanism · proof · objection · alternative (how the pitch will frame it) |

Angles, in plain terms: **outcome** leads with the result; **mechanism** explains why it works;
**proof** shows a number or a quote; **objection** answers the reason they would say no; **alternative**
contrasts with what they use now.

Rules:
- Every USP has a proof or is marked `[unverified]`. Unverified USPs stay off the pitch, or appear as
  "what we would test next".
- A USP every competitor can claim ("AI-powered", "intuitive", "secure", "fast") is deleted.
- At least one USP answers the persona's main objection.
- The strongest USP becomes the "now possible" moment of the demo.

## 4. Worked example (illustrative)

- **Segment**: maintenance leads in machine shops with 20–100 staff (early adopters: they already keep
  a shared folder of procedures and a WhatsApp group for changes) `[declared]`.
- **Persona**: *Who* maintenance lead, three technicians, a CMMS nobody updates · *Job* make sure the
  night shift follows the current procedure · *Trigger* a near miss after an outdated procedure was
  used · *Where* regional manufacturing association, maintenance forums · *Objection* "my people will
  not type questions into a chatbot".
- **UVP**: For maintenance leads who discover that an outdated procedure was used on the night shift,
  the agent always answers with the procedure in force and who changed it — unlike the shared folder
  and the WhatsApp group — because every procedure is a versioned object that supersedes the old one.
- **USP 1**: pain *old versions still circulate* → resolves *supersession closes the old version* →
  gain *nobody follows a retired procedure* · proof *demo: change a step, ask again, old answer gone* ·
  vs *shared folder* · angle *proof*.
- **USP 2**: pain *"who decided this?"* → resolves *every answer cites author and date* → gain *audits
  take minutes* · proof *citation in the demo* · vs *WhatsApp group* · angle *outcome*.
- **USP 3**: objection *technicians will not type* → resolves *ask by voice from the machine, or scan a
  QR code on the machine* · proof `[unverified]` → next test, not on the pitch.
