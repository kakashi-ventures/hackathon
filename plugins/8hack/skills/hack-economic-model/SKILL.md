---
name: hack-economic-model
description: >
  Builds and updates a hackathon team's economic model in Control8 (MCP server `hack`): what the team
  sells, the price, the volumes, how customers arrive and what selling costs. The jury reads this model
  for Business case, at the financial validation. Use when the team says "draft our economic model",
  "update the economic model", "what do we charge", "our pricing", "CAC", "payback", "business case
  numbers", "modello economico", or when the rubric check says Business case is the weakest criterion.
metadata:
  author: kakashi-ventures
  version: "0.1.0"
  companion-of: 8hack
---

# Economic model

The jury card shows the headline of the team's saved model (annual revenue, CAC payback) next to the
Business case criterion, and the rules say that criterion is scored "as checked at the financial
validation". A model that is not saved in Control8 does not exist for the jury, however good the slide
is. This skill gets one saved, with every number traceable to where it came from.

It uses two tools and nothing else: `get_economic_model` to read, `update_economic_model` to write.

## 1. Read first

1. The team project slug starts with `hack-` and is on the team's `/me`. Ask once if you do not have it.
2. `get_project_context` with the slug, to know the idea (and `get_document` on `8hack-start` if it
   exists: the problem, the segment, the riskiest assumption).
3. `get_economic_model` with the slug. It returns the current model, the arithmetic Control8 derives
   from it, the coverage gaps and the **vocabulary**: the units, periods and acquisition channels a
   model may use. Use only those values. Never guess one.

If a model exists, you are updating it: keep what the team decided and change only what they ask.

## 2. Ask for the numbers, in one message

- What one unit is (a seat a month, a licence a year, a project fee, a call to the API) and who buys it.
- The price of one unit, and the currency.
- How many units are billed in a period, at what horizon ("month 12", "first year"). This is a flow,
  not a stock of customers.
- How customers arrive: the channels, the cost per lead, the share of leads that become customers, the
  leads expected in a period.
- Who sells, how many people, what they cost a month. The ad budget, if any.
- What it costs to serve one unit (hosting, model calls, support), if they know it.

For each number, ask where it comes from, and mark it: `[verified: source]`, `[declared]` (the team's
estimate) or `[unverified]`. A number the team does not have stays empty (`null`). Do not fill it with a
plausible value: an empty field is a gap the jury can see, an invented one is a claim they can break.

## 3. Write the document

`update_economic_model` takes the **whole** model and saves it as a new version (the previous one is
kept). Before calling it:

- **Money is integer cents.** €49 is `4900`. €1,500 is `150000`.
- **`volume` is the units billed in the period.** 500 monthly subscriptions is `volume: 500` with
  `period: "month"`; Control8 multiplies by 12 for the year. Writing 6000 there would count the year
  twelve times.
- `recurring` says whether the line repeats (a subscription) or is sold once (a setup fee).
- Keys are short and stable (`pro_seat`, `linkedin_outbound`), labels are what a person reads.
- `note` holds what the numbers cannot say: the horizon of the volumes, each number's marker and source,
  and the cost to serve one unit with the margin it leaves (the model has no field for unit cost).

Show the team the document and the yearly revenue it implies (Σ price × volume × periods in a year) and
save only after they say yes. If Control8 answers `invalid_input`, the message names the exact paths that
are wrong: fix those and send the whole document again. Nothing is saved by halves.

## 4. Read it back

Call `get_economic_model` again and report, in five lines: annual revenue, blended CAC, payback in
months, first-year return, and the coverage gaps still open. Then name the one number the Business case
rests on and its marker. If that number is `[declared]` or `[unverified]`, say how the team could check
it before the pitch deadline (16:45): a quote from a real buyer, a public price list, a competitor's page.

## 5. Checks before the jury

Do these as arithmetic, not as impressions:

- Every revenue line has a price, and every line meant to count has a volume.
- Every channel has a cost per lead and a conversion share, or the CAC cannot be computed.
- The volume does not need more customers than the segment the team counted (canvas Q7 in 8hack).
- The price and volume in the model are the ones in the `pitch` artifact. If they differ, one of them
  is wrong, and the jury will see both.

## 6. Rules

- Never write a number the team did not give or a source did not show.
- Never call the model "validated" in the pitch. Say which numbers were measured and which are estimates.
- One currency per model.
- The economic model is written only with `update_economic_model`. Do not put the numbers in a page or an
  artifact instead: the jury card reads the model.
