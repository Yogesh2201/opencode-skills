---
name: md-full-overview
description: Build a complete company/stock overview as a portable Markdown file (tables, ASCII bars, one-line takeaway) using only its bundled references (examples/example.md — byte copy of the TDPS Markdown member — plus assets/ for section skeleton, forecast/valuation model and verify checklist, data/ for schema + a proven company JSON). Use when the user asks for a "md full overview", "md-full-overview", a Markdown company overview, or a forecast-style stock report in MD. Generates <Stock>-<YYYY-MM-DD>.md in MD-Full-Overview/, then offers a new stock analysis.
---

# MD Full Overview — Markdown-only company report

Builds a complete company/stock overview as **one portable plain-Markdown `.md` file**
(demo-01 style — no color layer, no `<style>`, no spans), then loops
into the next question. Reference files live in **this skill's own folders** — all
copied verbatim from `full-overview-2-0` (MD path only). That skill is **never
modified** by this workflow. This skill is Markdown-only; there is no HTML handoff.

| Folder | File | Purpose | Copied from |
|---|---|---|---|
| `examples/` | `demo-01.md` | **Canonical reference — strict section order + table columns** | Verbatim copy of `demo/demo-01.md` |
| `examples/` | `example.md` | Legacy TDPS render — do NOT use for structure | `full-overview-2-0/examples/example.md` |
| `templates/` | `markdown.template.md` | Verbatim copy of `example.md` (static starting point) | `full-overview-2-0/templates/markdown.template.md` |
| `assets/` | `section-skeleton.md` | Fixed section order, ids, nav labels, verbatim copy blocks | `full-overview-2-0/assets/section-skeleton.md` |
| `assets/` | `tokens.md` | Structure rules (MD rule: plain markdown — headings/tables/quotes carry hierarchy, no color) | `full-overview-2-0/assets/tokens.md` (MD section only) |
| `assets/` | `forecast-model.md` | Section 04 + 06 numbers (anchor, outcomes, assumptions, year path) | `full-overview-2-0/assets/forecast-model.md` |
| `assets/` | `verify-checklist.md` | Build + verification steps, reply format | `full-overview-2-0/assets/verify-checklist.md` |
| `data/` | `schema.json` | JSON Schema for `data/<company>.json` (LLM generates only this, ~600 tokens) | `full-overview-2-0/data/schema.json` |
| `data/` | `zen.json` | Proven company data file — filings-traced, peer pot, AlphaSpread valuation, forecast | `full-overview-2-0/data/zen.json` |

Do **not** use `Full-overview/`, `IRCTC_*`, `demo-02.md`, or any other HTML/MD as a template.
`examples/demo-01.md` **alone** supplies structure, section order and table columns; company data changes per request.

---

## Step 1 — Research the company (before any reading or writing)

Gather filings-traced figures for `data/<company>.json` per `data/schema.json`
(see `data/zen.json` as the filled reference):

- `meta` — company, NSE/BSE symbols, HQ, kicker line, render date.
- `price` — current (latest close), MCap, shares outstanding, TTM P/E, P/B.
  Sources: `screener.in/company/<TICKER>/consolidated`, exchange quotes, BSE filings.
- `bank_kpis` — 5-yr sales + PAT + OPM history (feeds the Section 2 five-year table),
  Screener compounded growth boxes (sales / profit / price CAGR: 10Y, 5Y, 3Y, TTM),
  order book, cash/debt, debtor/inventory/WC days,
  ROCE/ROE, promoter holding, dividend, capex note, cashflow note.
  Sources: AR FY25, quarterly BSE filings, investor presentations, concall transcripts.
- `peers_sfb` — one listed peer-group pot (3–4 peers): FY revenues, HQ geography,
  share = revenue ÷ pot, one-line overlap each. Never a TAM claim.
- `products` — 6 capability families + 3 extras + value spectrum line.
- `revenue_mix` — where money comes from + geographical footprint: segment/product split
  (or best proxy + one-line disclosure note if undisclosed), domestic/export + regional split,
  delivery footprint (offices, locations, headcount).
  Sources: AR segment notes, investor presentation, concalls.
- `vision` — verbatim management quote + 4 funded pillars (target + why + tag).
- **`valuation` — AlphaSpread live** from `https://www.alphaspread.com/security/nse/<ticker>/dcf-valuation/base-case`
  + `/relative-valuation` + `/summary`: DCF Value, Multiples-Based Value, Intrinsic Value,
  Buy Zone (20% MOS), 4-row multiples + 4 tiles + methodology. DCF params are
  template-dependent — banks/SFBs use the Bank template (e.g. 7yr, Discount 10%, Exit 1.8x P/S);
  hospitals/industrials use the Net Income template (e.g. 15yr, Discount ~10–11.5%, Exit P/E or P/S).
- `trends` — 5 trends + 3 management messages + 5 red flags (2 HIGH · 3 MEDIUM) + bottom-line six lenses.
- `forecast` — anchor (price/MCap/shares/TTM sales/EPS/P-E/OPM/guidance), 3 scenarios
  (Bear/Base/Bull price + CAGR + MCap), assumptions (sales CAGR, FY31 sales, PAT margin,
  exit P/E, FY31 EPS), 6-column year path (price + MCap), logic lines.
- `takeaway` — one-line takeaway.
- `ir` — reports-library URL (annual/integrated reports + results briefings page) plus
  the next 4–5 dated events: upcoming results, dividend ex/record dates, AGM.
  Sources: company IR calendar page, exchange notices; past pattern dates labelled as pattern.

Ask the user for source figures if filings data is missing. **~800 tokens of JSON, not 20K.**

## Step 2 — Read the reference, then write the file

1. Read `examples/demo-01.md` **fully** — it is the ONLY structural reference.
   Reproduce its section order and table columns exactly, in this strict order:
2. Also open `assets/forecast-model.md` (section 07 + 09
   number discipline), `assets/verify-checklist.md` and `assets/tokens.md` (MD rule) before writing.
3. Write `MD-Full-Overview/<YYYY-MM>/<Stock>-<YYYY-MM-DD>.md` directly
   (month folder + stock name + date only, e.g. `MD-Full-Overview/2026-09/Zensar-2026-09-27.md` — no `_forecast` infix;
   no build script — Markdown is hand-rendered from the JSON + reference):

```
Title `# <Co> (NSE: <NSE> · BSE: <BSE>)` → bold kicker line
  (`<HQ> · <one-line business>`) → bold price line
  (`Price: ₹<P> (<D Mon YYYY> close · <±Z%>) · Market cap: ₹<M> Cr · Report date: <D Mon YYYY>`)
  → `>` filings-only blockquote (no `<style>`, no color anywhere)
## TL;DR (5 bullets: what it is / where it stands / balance sheet / problem is price / takeaway)
## Key Numbers — table Metric | Value | Context
  (Revenue TTM · Operating margin · Net profit TTM · Returns · Order book · Net cash · Valuation · Dividend)
## 1. What the Company Does (para + How it makes money + Why it's different + three numbered things +
  ### Where the money comes from + geographical footprint — one-line disclosure/proxy note +
  table Revenue stream | Share | Note + table Region | Share / Presence | Note + one-line footprint)
## 2. Order Book & Execution — table Snapshot | Amount | Detail + pipeline bullets + YoY tables + five-year history table (Revenue + PAT with 3-yr/5-yr change)
## 3. Products — table Product line | What it is | Recent proof points
## 4. Competitors — pot intro + table Company | HQ | FY Revenue | Share | Profile vs + In-short line
## 5. Financial Health — table Metric | TTM | % of Market Cap | Comment
  (Market cap · Revenue · Operating profit · Net profit · Free cash flow · Net cash + Strengths | Concerns table)
## 6. Strategy & Management Vision (verbatim quote + table Priority | Target | Why it matters +
  transformation chart — fenced code Old → plan → New)
## 7. Valuation (summary + Multiples table Metric | Co | Benchmark | Read +
  Intrinsic table Method | Value/Share | vs price +
  earnings-yield cross-check tile + 4-row 5-column table + How-to-read bullets)
## 8. Risks — table # | Risk | Severity | Evidence (2 HIGH · 3 MEDIUM)
## 9. Five-Year Scenarios (method + compounded growth boxes + assumptions/outcomes Bear | Base | Bull +
  scenario meanings + price-path table + insights)
## 10. What to Watch Each Quarter — table Signal | Healthy sign | Warning sign +
  ### Upcoming IR calendar — table Date | Event | Detail
## Bottom Line — table Lens | Take + one-line quote
### Sources + disclaimer (SEBI educational-only line + reports-library link)
```

Never reproduce `Editor's Notes` (demo-only correction log, not part of the template).

### Markdown build rules (match `examples/demo-01.md` — plain markdown, no color layer)

- Title + bold kicker + bold price line + `>` filings-only blockquote (exactly as in `examples/demo-01.md`).
- Tables with these exact columns — never rename, reorder or merge columns:
  Key Numbers `Metric | Value | Context` · Order book `Snapshot | Amount | Detail` ·
  Products `Product line | What it is | Recent proof points` ·
  Revenue-mix `Revenue stream | Share | Note` · Footprint `Region | Share / Presence | Note` ·
  Competitors `Company | HQ | FY Revenue | Share | Profile vs` ·
  Financial Health `Metric | TTM | % of Market Cap | Comment` + `✅ Strengths | ⚠️ Concerns` ·
  Vision `Priority | Target | Why it matters` ·
  Multiples `Metric | <Co> | Benchmark | Read/Verdict` ·
  Intrinsic `Method | Value/Share | vs <price>` ·
  Earnings-yield `Metric | Current Market Levels | At 3.7% Yield | At Forward P/E | At 5-yr Avg P/E`
  (4 rows: Earnings Yield / Implied P/E / **Market Capitalisation** / **Share Price** —
  the MCap and Share Price rows are fully bold; diffs vs current in brackets per cell) ·
  Risks `# | Risk | Severity | Evidence` ·
  Five-year history `| | FY×5 | 3-yr avg (CAGR) | 5-yr avg (CAGR)` ·
  Growth boxes `| | 10 Years | 5 Years | 3 Years | TTM / 1 Year` ·
  Scenarios assumptions table with `Bear | Base | Bull` columns + price-path rows ·
  What to Watch `Signal | Healthy sign | Warning sign` · Bottom Line `Lens | Take`.
- Section headings `## TL;DR` … `## 1. What the Company Does` … `## 10. What to Watch Each Quarter`,
  then `## Bottom Line`, then `### Sources` and the disclaimer. Inside `## 1`, the fixed
  subsection is always `### Where the money comes from + geographical footprint`.
- Emoji preserved as written in the reference; ₹ / × / → / − as literal UTF-8.
- Plain markdown only — never add a `<style>` block, spans, pills, or band divs.
  Hero figures use plain `**bold**`; `Read` / `Severity` cells use emoji as in demo-01
  (`🔴` expensive/high, `🟡` elevated/medium, `🟢` at-plan/best-in-set); the Section 5
  quality-watch is a plain `>` quote; Section 7 keeps the valuation bar (fenced code) and
  the `>` reading paragraph; Section 8 keeps the flags summary (fenced code);
  Bottom Line closes with a `> **One line:**` quote; the footer is `### Sources` +
  the SEBI disclaimer. Column headers stay demo-01 exact, except the Earnings-yield
  table which uses the 5-column form specified below.

### Revenue-mix + footprint (fixed subsection of Section 1)

- Render only from `revenue_mix` in `data/<company>.json`. If the company discloses no
  split, say so in one line and use the best proxy (order book, inflow, installed base),
  labelled as proxy — never invent a split.
- Two tables with the exact columns above, then a one-line footprint (HQ + offices +
  delivery locations + headcount). Same currency convention (₹ Cr / $ billion).
- The subsection answers *"who pays, from where"* — it must agree with Section 3
  (Products) and Section 4 (Competitors HQ geography), never contradict them.

### Five-year history (always in Section 2)

- After the demo-01 YoY tables (latest quarter + latest year), render one extra table
  `**Five-year history (FYxx–FYxx, consolidated):**` with columns
  `| | FY | FY | FY | FY | FY | 3-yr avg (FYxx→FYxx) | 5-yr avg (FYxx→FYxx) |`
  and three rows — Revenue · Operating margin · PAT — from the `bank_kpis`
  5-yr sales + PAT + OPM history.
- The avg cells are **per-year averages, not point-to-point totals**: Revenue and PAT use
  CAGR — `(end ÷ start)^(1÷n) − 1` where `n` = elapsed years (**intervals, not data
  points**: FY23→FY26 is `n = 3` over 4 points; FY21→FY26 is `n = 5` over 6 points
  counting the named base year). Label cells e.g. `+13.8% p.a. (CAGR)`.
- The margin avg is a per-year pp move (`(end − start) ÷ n`, e.g. `−1.3 pp p.a.`),
  or "Turn from X% (FYxx)" off a trough.
- PAT avg is a **CAGR %** whenever all years are profits; fall back to an **absolute
  ₹ Cr move** (e.g. `+₹1,161 Cr (loss to profit)`) whenever a base year is a loss —
  % change off negative earnings misleads, so never use it there.
  Name the FY-base figures in brackets in the 5-yr cells (e.g. `(off FY21 ₹3,647 Cr)`).
- Sanity-check the 3-yr CAGRs against Screener's compounded growth boxes (3 Years
  sales/profit) — they must match within rounding.

### Compounded growth boxes (always in Section 9)

- Right after the `**Method:**` line and before `### Assumptions & Outcomes`, render the
  **compounded growth boxes** as one plain table
  (`| | 10 Years | 5 Years | 3 Years | TTM / 1 Year |`, rows: Sales growth · Profit growth ·
  Stock price CAGR) copied from the Screener company page header — they ground the scenario
  CAGRs, so title the table accordingly (e.g. `**, grounding the CAGRs above:**`).
  Mark pre-listing cells `—` with a one-line note (e.g. `10-yr figures n/a — listed May 2022`).
  Attribute the table as Screener machine figures with the as-of date.

### Earnings-yield cross-check (always in Section 04)

- *Yield = PAT ÷ MCap · implied P/E = 1 ÷ yield · benchmark 3.7% ↔ 27.027×.*
- Recompute per company from **live price, MCap, TTM PAT and shares** — never reuse
  another company's worked numbers. If reported TTM PAT is polluted by exceptionals /
  one-time gains, add a one-line continuing-earnings footnote (yield, implied P/E, implied price).
- Additionally pull two multiple lenses from AlphaSpread `/relative-valuation`: the
  **forward P/E** (nearest forward-year P/E) and the **5-year average P/E**. Apply both
  to the same TTM PAT-implied EPS (price = EPS × multiple; MCap = price × shares).
- Render as **one extra tile row** (`🧮 Earnings yield → ≈ ₹X`) in the tiles table **plus**
  a 4-row 5-column comparison table
  (`Metric | Current Market Levels | At 3.7% Yield | At Forward <N>× | At 5-yr Avg <M>×`:
  Earnings Yield / Implied P/E / **Market Capitalisation** / **Share Price** — the MCap
  and Share Price rows are fully bold, diffs vs current in brackets in every valuation
   cell) with a `🧮 Reading` quote covering all three lenses.
   Store the inputs in `data/<company>.json` under `ey` per `data/schema.json`.

### Transformation chart + IR calendar (always include)

- **Section 6 — transformation chart.** After the pillars table, render one fenced-code
  ASCII chart showing the strategic shift: old mix → the named plan → new mix →
  the mechanism → the targets. Adapt labels per company; keep the shape:
```
                    OLD <CO>
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    <old biz 1>    <old biz 2>     <old biz 3>
        │              │              │
        └──────────────┴──────────────┘
                       │
                 <old constraint>
                       ↓
                   <old outcome>


                ↓ <PLAN NAME> ↓


                    NEW <CO>
                       │
       ┌───────────────┼────────────────┐
       │               │                │
  <new pillar 1>  <new pillar 2>   <new pillar 3>
       │               │                │
 <proof point>    <proof point>     <proof point>
       │               │                │
       └───────────────┼────────────────┘
                       │
                    <enabler>
                       │
                       ↓
                <target metric 1>
                       │
                       ↓
                <target metric 2>
                       2030
```
- **Section 10 — IR calendar.** After the What-to-Watch table, render a fixed
  subsection `### Upcoming IR calendar — key dates` with table
  `Date | Event | Detail` (4–5 rows: next results with time/timezone, dividend
  ex-date + record date, full-year results, AGM with term number). Confirm each
  date from the IR calendar / exchange notice; label pattern-derived dates as
  pattern (e.g. "Pattern: 27 Mar 2026").
- **Sources — reports link.** Add a `Reports library` bullet with the company's
  IR library URL (annual/integrated reports + briefings) and, where one exists,
  the IR calendar URL. Store both under `ir` in `data/<company>.json`.

## Content rules

- **Filings-only + AlphaSpread**: every figure traced (AR, BSE filings, `screener.in`,
  peer 10-K/AR/NOR) **and** valuation pulled live from AlphaSpread (DCF + Multiples-Based
  → Intrinsic as primary, local forward/EV cross-check secondary). Peer % = share of one
  listed peer-group pot, never a TAM claim.
- **Currency convention (never mix): Indian stocks → ₹ Cr (crore) for every money
  figure** (MCap, revenue, PAT, cash, order book, EY table, forecast paths).
  **US stocks → $ billion for every money figure.** Peer pots follow the same unit.
- Forecast discipline is **Revenue → PAT margin → EPS → P/E → Price → MCap**.
  Keep scenarios internally consistent (year path = anchor × (1 + price CAGR)^t;
  MCap path = price path × shares, flat unless dilution is disclosed).
- Always mark section 06 **illustrative, not a price target**, and keep the SEBI disclaimer:
  *Educational only, not investment advice… Consult a SEBI-registered advisor.*
- If the user names a different company, keep the structure and replace only the data.
- Verify before delivering: zero build markers (`PART_`), no `<style>` / `<span` / `pill` / `band` markup anywhere (prose words like "pillar" are fine — the check is for pill/band div markup),
  all `##` sections present in demo-01 order (TL;DR, Key Numbers, 1 What it does **+ revenue-mix/footprint subsection**,
  2 Order book **+ five-year history table**, 3 Products, 4 Competitors, 5 Financial Health **+ quality-watch quote**, 6 Vision **+ transformation chart**,
  7 Valuation **including the earnings-yield tile row + 5-column table (MCap/Price rows bold) + valuation bar**, 8 Risks **+ flags summary**,
  9 Scenarios + price path **+ growth boxes**, 10 What to watch **+ IR calendar subsection**, Bottom line **+ one-line quote**, Sources + disclaimer **+ reports-library link**),
  every table uses the exact column headers listed above,
  no overflow wide tables beyond ~120 chars where avoidable.

## Output

Save the file in `MD-Full-Overview/<YYYY-MM>/`:

| Output | File name |
|---|---|
| Markdown | `<Stock>-<YYYY-MM-DD>.md` |

Reply with the path + one line on what was built, then **always** go to Step 3.

**Token budget:** ~28K input (example) + ~20K output per report on first build for a
new company; the saved `data/<company>.json` makes refreshes cheap.

## Step 3 — Follow-up question (always last)

After delivering, ask via the question tool (two options only — no HTML handoff;
this skill is Markdown-only):

1. **New stock analysis** — start a fresh Markdown overview for a different company (back to Step 1)
2. **Done** — nothing further for now

If they pick new analysis → restart at Step 1.
