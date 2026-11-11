# The technology moat (canvas Q8)

A moat is what makes the product hard to copy **after** someone has seen the demo. In a hackathon
the moat is almost always a plan, not a fact. Saying so is a strength; pretending otherwise is the
fastest way to lose a technical judge.

## 1. Commodity or differentiator

For each technology in the stack, decide which it is.

| | Commodity (buy, do not compete) | Differentiator (build, the moat may live here) |
|---|---|---|
| Examples | Frontier models, hosting, auth, payments, vector search, transcription, UI kits | Your domain ontology, your data loop, your evaluation set, your verification logic, your integration into the user's workflow |
| Rule | Use the best available and keep it swappable behind an interface you control | Spend the hackathon's scarce build time here |

The demo should spend its seconds on the differentiator. Nobody gives points for the login screen or
the model you called.

## 2. The moat table

```
| Technology | Commodity / differentiator | State today (in the demo) | Target state (hard to copy) | Measured by | Horizon |
|------------|----------------------------|---------------------------|-----------------------------|-------------|---------|
```

- **State today**: what the demo actually does, honestly ("12 procedures, hand-written ontology of 3
  classes").
- **Target state**: what would have to be true to be hard to copy ("the ontology updates from 500
  procedure changes a month, with a human approving each supersession").
- **Measured by**: a benchmark, your check set, a public evaluation, a usage metric.
- **Horizon**: this week, three months, a year.

## 3. Five moat tests

1. **The copy test.** A strong team with the same frontier model and a free weekend copies the demo.
   What can they not copy? If the answer is "nothing", the moat is a plan: write the plan.
2. **The next-release test.** If the next frontier assistant release shipped your core flow as a
   feature, what would still be yours? (Usually: the data, the domain constraints, the workflow
   integration, the governance.)
3. **The compounding test.** Does the product get better with every use? Corrections that improve the
   memory, decisions that enrich the ontology, usage that sharpens the check set. No compounding, no
   moat.
4. **The access test.** Does the moat depend on something only this team can reach (data, a buyer, a
   regulation, a domain)? If nobody in the team can reach it, it is not a moat for this team.
5. **The verification test.** Can you prove the output is right in a way a competitor cannot easily
   reproduce? Deterministic checks on a domain are slow to build and hard to fake.

**Not moats**: a prompt, the choice of model, a UI, a fine-tune on public data, being first at a
hackathon, "our AI is smarter".

## 4. Technology map for AI brains, memory and ontologies

Use this when the challenge is about industrial AI brains, shared memory or custom ontologies. The
concepts are stable; the product names are examples as of mid-2026 and must be checked in SCAN before
they are cited.

### Memory

| Capability | Why it is hard | What "achieved" looks like |
|---|---|---|
| **Supersession** — knowing a rule is no longer in force | Overwriting loses history; appending keeps contradictions | Facts carry validity windows; the old fact is closed, not deleted; queries answer "in force now" and "in force on date X" |
| **Provenance** — who said it, from which source, when | Most stacks keep the text and lose the origin | Every answer cites its source and author; a fact without a source is flagged |
| **Multi-writer consistency** — many agents and people writing to one memory | Conflicting writes, races, silent overrides | Conflicts are detected and queued for a decision, not resolved by the last write |
| **Decision records** — why a decision was made | The why lives in meetings and chats, not in systems | Decisions are objects with their reasons, alternatives and evidence |
| **Abstention** — saying "I do not know" | Retrieval always returns something | The system refuses when evidence is missing, and says what is missing |
| **Forgetting and retention** | Memory grows until it is noise; some data must expire | Explicit retention rules; stale facts decay or are reviewed |
| **Evaluation** | Memory quality is invisible until it fails | A check set with supersessions, conflicts and abstentions, run on every change; public long-memory benchmarks exist (for example LongMemEval) |

Example open-source and commercial building blocks to check in SCAN: self-editing agent memory
(Letta), vector-plus-graph memory layers (Mem0), temporal knowledge graphs with validity windows
(Graphiti / Zep), document-to-graph pipelines with ontology validation (Cognee). Using one of them is
a commodity choice; what you build on top for one domain is where the moat can be.

### Ontologies

| Capability | Why it is hard | What "achieved" looks like |
|---|---|---|
| **Bootstrapping** — classes, relations and axioms from unstructured text | Extraction is noisy; the schema drifts | A model proposes, a domain expert approves; the ontology is versioned |
| **Entity identity** — when two records are the same thing | Duplicates appear only in some cases | Identity keys decided and written down before coding |
| **Evolution** — updating when the organisation changes how it works | Changes break queries and past answers | Versioned schema with migrations; answers say which version they used |
| **Reasoning, not only search** | Retrieval finds text; it does not infer | Rules and constraints derive missing relations; the agent's path follows relations and shows the inference |
| **Validation** | Bad data enters silently | Shape constraints (for example SHACL-style rules over RDF/OWL, or equivalent checks in a property graph) reject invalid facts |
| **Alignment with the domain's standards** | Every company reinvents its vocabulary | Mapping to the vertical's existing standards and codes |

### The agent layer on top

- Tools grounded in the ontology (the agent queries relations, not just text chunks).
- Answers with citations to facts and to their versions.
- A verification step before an answer is shown (a rule, a constraint check, a source match).
- Human approval where the output changes the memory or the ontology.

## 5. Saying it on stage

One sentence for the moat, then one for the plan:

> "Today the demo runs on 12 procedures and a three-class ontology we wrote by hand. The moat is the
> correction loop: every supersession a maintenance lead approves makes the next answer more reliable,
> and that history is something a copy starts without."

Mark which half is built and which half is the plan.
