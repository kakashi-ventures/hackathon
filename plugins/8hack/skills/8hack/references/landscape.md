# SCAN — landscape analysis in twenty minutes

The scan answers four questions before the team commits its build time:

1. **Who already solves this, or something close?** (P2 Innovation void)
2. **What would stop a copy of us, and what stops a copy of them?** (P4 Defensibility)
3. **Which alternative does each USP beat?** (Q4)
4. **Is this about to become a native feature of a frontier assistant?** (wrapper risk)

Budget: 6 to 10 searches, 20 minutes, a fraction of the ideation credits. Stop when every question
above has an answer or an explicit gap.

## 1. Search plan

Run them as separate searches; a combined query returns shallow results for each part.

| # | Vector | Example query shape |
|---|---|---|
| 1 | The job, in the user's words | `<job> software`, `<job> tool small firms` |
| 2 | AI-native entrants | `AI <job> startup`, `<job> agent` |
| 3 | Incumbents in the vertical | `<vertical> <job> platform`, the names users mention |
| 4 | Open source doing the mechanism | `github <mechanism>` (e.g. temporal knowledge graph memory) |
| 5 | Money in the last 12 months | `<job> AI raises seed`, `<category> funding <year>` |
| 6 | Native-feature risk | the frontier assistants' docs and changelogs for the capability |
| 7 | Research and benchmarks for the mechanism | `<mechanism> benchmark`, `<mechanism> survey arXiv` |
| 8 | Regulation, if the domain has it | `<vertical> regulation <job> AI` |
| 9 | Bottom-up count of the segment | registries, directories, association member lists, job posts |
| 10 | What users complain about | reviews, forums, app-store reviews of the incumbents |

If web search is not available in the harness, ask the team to paste what they know and mark it all
`[declared]`; the scan then says so in its method line.

## 2. Evidence rules

- Every fact carries a marker: `[verified: <url or source>]` · `[declared]` · `[unverified]`.
- Count before you multiply: "1,400 firms with 5–20 staff in the region [verified: registry]" beats
  "1% of a €40B market". Top-down TAM never goes on a slide without its source and date.
- A vendor's own claims (accuracy, customers, ARR) are `[declared]` even when they are on the web.
- "No competitors found" is a warning: the problem may be fake, too hard or commercially weak. Say
  which searches came back empty.
- Same mechanism, different job is not a competitor; same job, different mechanism is. List both, label
  them.
- Date every fact that can change (prices, funding, features). The scan has an "as of" date.

## 3. The landscape card

Write it to `HACK.md` (section *Landscape*) or to `LANDSCAPE.md` if it is long.

```
LANDSCAPE · <idea> · as of <date>
Method: <searches run, what was unreachable, time spent>

Market (2–3 lines): <who has the problem, bottom-up count with source, why now>

Alternatives
| Name | What it does | Segment | Price | Size / traction | Why it does not solve OUR focus | Link | Marker |
|------|--------------|---------|-------|-----------------|----------------------------------|------|--------|
| …    | …            | …       | …     | …               | …                                | …    | …      |
| Status quo (spreadsheet, email, the senior colleague) | … | … | free | everywhere | … | — | [declared] |

Native-feature risk: <which frontier assistant capability overlaps, and how much> [marker]

Recent moves (last 12 months): <funding, launches, shutdowns> [markers]

Gaps: <what we could not verify, and how we would check it next>

So what: <one line each for P2, P4, the alternative each USP must beat>
Sources: <list>
```

Always include the **status quo** as an alternative: for most problems the real competitor is a
spreadsheet, an email thread and one senior person who remembers.

## 4. Reading the card into the gate

- **P2 Innovation void**: many funded AI-native products on the same job and segment → 0–1. Legacy
  tools only → 3. Status quo only → 4–5.
- **P4 Defensibility**: if the best alternative could add your feature in a sprint, your P4 is low
  unless you hold data, an ontology or access they do not.
- **Wrapper flag**: if a frontier assistant already does the core flow acceptably for this user, raise
  `wrapper` and look for the slice it cannot do (domain constraints, verification, integration, memory
  that must be governed).
- **USPs**: each USP names the alternative it beats from this card. A USP with no alternative to beat
  is either a real void (say so) or an unexamined claim.

## 5. Optional: one positioning picture

Two axes that matter to the segment (for example *checkable output* vs *effort to adopt*), the
alternatives placed on them, and the empty corner you claim. Use it in the pitch only if the empty
corner is real and the axes are what the user cares about, not what flatters the project.
