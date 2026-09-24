---
name: stock
description: Author a single-name equity research report (the 7-section ALL-CAPS styled .md) and its demo.html-style HTML twin, following this spec. Use when the user wants an equity report on a ticker, a "stock analysis", or a Stock/<YYYY-MM>/ report rendered to HTML. Unified author+render skill replacing the older Equity-research + stock-html-report pair.
---

# Stock — Skill Specification (`stock`)

> **Scope:** Author **and** render a single-name equity research report from a ticker (plus any supplied financials / market data). The pipeline produces **two sibling artifacts** in one invocation:
>
> 1. the **authored** 7-section ALL-CAPS, narratively-framed, styled `.md` in `Stock/<YYYY-MM>/`, and
> 2. its **rendered** standalone browser-openable `.html` twin — the rich demo.html-style page with sticky topbar, meta-grid, KPI strip, section cards, verdict box, and one hero — in `Stock/<YYYY-MM>_html/`.
>
> **Invocation:**
> - `/stock <TICKER>` → authors the `.md` **and** the `.html` twin.
> - natural-language: *"research MSFT"*, *"give me an equity report on ITC"*, *"ITC as html"*, *"make the ITC report into a demo-style HTML"*.
> - If the user only wants to **re-render an existing** `Stock/<YYYY-MM>/<TICKER>_*.md` into HTML (no new analysis), run the render half only (see §Procedure step 5).
>
> This single skill replaces the older split of `Equity-research` (author) + `stock-html-report` (render). It *writes* the report **and** *renders* it — never invent new CSS tokens, never new analysis for the HTML.

---

## When to use

- The user asks for "an equity research report", "research on <TICKER>", "stock analysis", or references the 7-section shape — and wants an HTML deliverable too.
- The user names a ticker and wants a full bottom-up writeup: overview → strengths → financials → valuation → DCF → red flags → verdict, plus a polished shareable HTML.
- The user has an existing `Stock/` `.md` and asks for the "demo.html style" / "rich HTML" / "make it look like the AAPL/ITC page".

**Not for:**
- A quick price/headline lookup with no 7-section structure.
- Anything that isn't single-name, long-only, bottom-up equity analysis.
- A dark-bg "YK Neon" minimalist twin — that variant is deprecated; this skill emits only the rich demo.html-style page (light palette). All twins now share one design.
- Financial advice. The disclaimer is mandatory on every file.

---

## Output shape

**Two files, written in one invocation:**

```text
Stock/<YYYY-MM>/<TICKER>_<Month>_<Day>_<Year>.md        ← authored report (PRIMARY)
Stock/<YYYY-MM>_html/<TICKER>_<Mon>_<Day>_<Year>.html   ← rendered twin (ALWAYS, unless user said .md-only)
```

- Filename uses the **full month** in the `.md` (`ITC_September_10_2026.md`), the `Mon` abbreviation is accepted for the HTML twin to match existing folders (`ITC_Sep_10_2026.html`). Prefer full month everywhere; if a `Stock/<YYYY-MM>_html/` file already exists for that ticker with the `Sep` abbreviation, match it.
- The `.md` is the **source of truth**. The `.html` is a *rendering* of the same analysis — never new numbers.

---

## The `.md` anatomy (authored)

**Format note:** the `.md` is *markdown with embedded HTML* — the heading blockquote, tables, and the styled elements (`<div class="quote">`, `<div class="quote warning">`, `<span class="hero">`) are written as real HTML so the `<style>` block can target the classes. Blockquotes may appear as either markdown `>` (e.g. the `> ⚠️ **BALANCE-SHEET WARNING**` line, the `> ✅ Strengths:` line) or as HTML `<div class="quote">` (e.g. the §7 Research Summary) — both are valid and the renderer must handle both. **Every number is wrapped in backticks** so it renders in the designated accent color.

Prepend this `<style>` block verbatim, then the 7 sections:

```text
1. <style> block      (YK light-bg palette — purple hero, blue workhorse, red numbers)
2. H1                 # <emoji> EQUITY RESEARCH REPORT: <COMPANY>
3. Header blockquote  6 bold-label rows: TICKER · REPORT DATE · LIVE PRICE · MARKET CAP · SECTOR · VALUATION STATUS
4. Section 1          ## 1. COMPANY OVERVIEW       (2-3 framed bullets → segments table → Strategic Position quote)
5. Section 2          ## 2. KEY COMPETITIVE STRENGTHS (2-3 framed bullets → strengths table)
6. Section 3          ## 3. FINANCIAL SNAPSHOT & QUALITY READ (2-3 bullets → snapshot table → BALANCE-SHEET WARNING quote)
7. Section 4          ## 4. VALUATION MULTIPLES    (2-3 bullets → 6-row multiples table)
8. Section 5          ## 5. DCF & INTRINSIC VALUATION (DCF table → 📌 METHODOLOGY NOTE → 📈 Valuation Bar → ⚙️ DCF Parameters)
9. Section 6          ## 6. RED FLAGS — <TICKER>  (3 framing paras → flags table → Red Flag Dashboard strip)
10. Section 7         ## 7. BOTTOM LINE & INVESTMENT VERDICT (Research Summary quote → Strengths/Concerns → hero verdict)
11. Disclaimer        *italicized educational-use footer*
```

### Header

```markdown
# 🚀 EQUITY RESEARCH REPORT: <COMPANY>

> **TICKER:** `EXCHANGE: TICKER`
> **REPORT DATE:** `<Month> <Day>, <Year>`
> **LIVE PRICE:** `₹XXX` (… close — last trading session)
> **MARKET CAP:** `₹XXX Cr` (`~$X.XB`)
> **SECTOR:** <one-line sector + moat characterization>
> **VALUATION STATUS:** <🟢/🟡/🔴> **<Verdict word>** — <one sentence thesis in dispute>
```

- **Title emoji:** 🚀 is the default. One ticker-relevant substitution allowed (IRCTC → 🚂, ITC → 🚬, Apple → 🍎, Microsoft → 🪟). Keep to one.
- **Backticked numbers everywhere** — they render red (`#B91C1C`) via the `<style>` block.
- **VALUATION STATUS** must state a verdict word: `MODESTLY UNDERVALUED` / `FAIRLY VALUED` / `FAIRLY VALUED to MODESTLY OVERVALUED` / `OVERVALUED`, prefixed by the matching emoji.

### Section 1 — COMPANY OVERVIEW
- **Lead paragraph:** plain-language *what the business is* + the dominant investment debate in one line.
- **Framing bullets (2-3, italicized, BEFORE the table):** mental model, threats to test, why the framing matters. No bullets inside the table.
- **Segments table:** `| Vertical | Nature | TTM indicative Revenue* | Share of Mix |`. Footnote `*` if segments are indicative (Indian PSUs / thin-disclosure names: they are).
- **Strategic Position blockquote:** `> **Strategic Position:**` one sentence — revenue scale, margin, ROCE/ROE, market cap, debate framed as a question.

### Section 2 — KEY COMPETITIVE STRENGTHS
- **Framing bullets (2-3):** the question on this name, the tests to run the moat against, ranking rationale.
- **Strengths table:** `| Strength | Details |` with emoji per row. Rank most-durable first. Typically 5 rows; up to 6 if a clearly distinct strength exists.

### Section 3 — FINANCIAL SNAPSHOT & QUALITY READ
- **Framing bullets (2-3):** the headline is elite / the story is hidden in one row / why the gap exists.
- **Snapshot table:** `| Metric | TTM Value | % of Market Cap | Analyst Interpretation |` with 5 rows — Market Cap, Revenue (TTM), Net Profit (TTM), Free Cash Flow (TTM), Debt-to-Equity. Embed the *derived* yield/earnings-yield multiples in the interpretation cell (e.g. `**6.2% Earnings Yield**` = `16.5x` P/E).
- **BALANCE-SHEET WARNING quote:** `> ⚠️ **BALANCE-SHEET WARNING**` — 3 short lines: growth is/isn't the problem, the specific deterioration, the BUT (bull/bear framing). Always present, even if balanced.

### Section 4 — VALUATION MULTIPLES
- **Framing bullets (2-3):** read as a system not one-at-a-time, what outcome is priced, what is NOT priced in.
- **Multiples table (exactly 6 rows):** `| Metric | Value | Benchmark | Valuation Read |` — Trailing P/E, Forward P/E, EV/EBITDA, Price-to-Book, Price-to-Sales (or P/FCF), PEG. Last column gets the 🟢/🟡/🔴 emoji + a phrase.
- **Footnote blockquote** with `*` marking historical/sector benchmarks as *approximate, contextual only*.

### Section 5 — DCF & INTRINSIC VALUATION
- **DCF table (4–5 rows):** `| Valuation Approach | Intrinsic Value / Share | vs Live Price (`<price>`) |`. Rows:
  - `DCF (Base Case, WACC x%, g y%)` → base intrinsic
  - `Forward P/E (Nx × FY??E EPS)` → peer cross-check (optional second peer row)
  - `EV/EBITDA (Nx × FY??E EBITDA)` → peer cross-check (optional second peer row)
  - `Blended Intrinsic Value` → equal-weighted blend (green/amber pill)
  - `Buy Zone (20% Safety Margin)` → `0.80 × Blended`, 🎯 pill
  - Last column: 🟢 undervalued / 🟡 fairly / 🔴 overvalued with `%`.
- **📌 METHODOLOGY NOTE blockquote:** state the DCF is *independently modelled*, not a vendor figure; name data sources; state blend weighting.
- **📈 Valuation Bar** (fenced ``` block, Persistent Systems style — 5 columns):

  ```text
    WS LOW       CURRENT          BUY ZN    IV         DCF
    ₹XXX         ₹XXX             ₹XXX      ₹XXX       ₹XXX
    |-------------|-----------------|---------|----------|-----------|
    Low target   Live price       Entry     Blended    Base Case
  ```
  Then 4-5 bullet metadata lines (Blended, Buy Zone, DCF base, shares out, calc date).
- **⚙️ DCF Parameters** (### sub-heading, bullet list) — fully disclosed: WACC, Rf, ERP, Beta, Cost of Equity, After-tax Cost of Debt, Weights, Base FCF, Forecast FCF growth fade, Terminal Growth, Net Cash Adjustment (mind sign: `+` net cash, `−` net debt), Shares Outstanding.

### Section 6 — RED FLAGS
- **Three framing paragraphs:** (1) red flags = demand margin of safety, (2) why these flags justify the discount, (3) the severity-scoring legend (🔴 High / 🟡 Medium / 🟢 Low definition).
- **Flags table:** `| # | Red Flag | Severity | Evidence |` — **5 rows typical**, 6 acceptable for names with an extra material flag (e.g. `SPCX`, `OLAELEC`); severity emoji, evidence backticked. The renderer's flag-grid accommodates 5 or 6 tiles.
- **Red Flag Dashboard** (fenced ``` strip, `### Red Flag Dashboard`): two label rows + severity row + HIGH/MEDIUM row, e.g.

  ```text
  DE-RATE    FEE-CAP    OPM        PROMO     P/B
  NARRAT    REGULAT   COMPRESS   OVERHANG   EXTREME
    🔴         🔴         🟡         🟡        🟡
    HIGH      HIGH     MEDIUM     MEDIUM    MEDIUM
  ```

### Section 7 — BOTTOM LINE & INVESTMENT VERDICT
- **Research Summary** — `<div class="quote">` containing `**RESEARCH SUMMARY**` + 2 paragraphs: where it trades (yields vs mcap), the *mirror-image* framing vs prior reports, the one-line thesis tension.
- **Strengths/Concerns blockquote:** `> ✅ **Strengths:** … · …` then `> ❌ **Concerns:** …` then `> **The blended DCF model calculates fair value at `₹XXX`** — indicating the stock is **<X> by Y%**.` then `> **Disciplined Margin-of-Safety Buy Zone: `₹XXX`** — the stock currently trades Z% above it (**patience required**).`
- **Hero verdict** — exactly one `<span class="hero">🎯 The verdict hinges on one question: …</span>`. One sentence, framed as a binary question, no hedge. This is the single purple moment on the page.

### Disclaimer
Italicized, educational-only, with data-source caveats (filings/exchange/consensus), DCF-independence statement, `*`-benchmark note, and "consult a SEBI/RIA" line.

---

## The standard `.md` `<style>` block (verbatim)

Prepend this to every `.md` — defines the YK light-bg palette: purple hero, blue workhorse, **red `#B91C1C` backticked numbers**.

```html
<style>
  /* Color hierarchy — YK palette (light-bg variants) */
  /* Purple = hero (one moment per page). Blue = workhorse structure. Dark = body. */
  h1, h2, h3 { color: #0B5FC0; border-bottom: 1px solid rgba(11,95,192,0.25); padding-bottom: 6px; }
  h1 { color: #692D9A; border-bottom: 2px solid rgba(105,45,154,0.45); }
  .hero { color: #4A1F7A; font-weight: 700; font-size: 1.15em; background: linear-gradient(90deg, rgba(170,77,230,0.08), transparent); padding: 8px 12px; border-left: 4px solid #692D9A; border-radius: 4px; display: block; margin: 12px 0; }
  .accent { color: #0B5FC0; font-weight: 600; }
  .quote { color: #4A1F7A; font-style: italic; border-left: 3px solid #692D9A; padding: 8px 12px; margin: 12px 0; background: rgba(105,45,154,0.05); }
  table { border-collapse: collapse; width: 100%; }
  th { color: #0B5FC0; border-bottom: 2px solid #0B5FC0; padding: 8px; text-align: left; background: rgba(11,95,192,0.05); }
  td { padding: 8px; border-bottom: 1px solid rgba(11,95,192,0.15); }
  hr { border: none; border-top: 1px solid rgba(11,95,192,0.25); margin: 24px 0; }
  strong { color: #1F1B2E; }
  code { color: #B91C1C; background: rgba(185,28,28,0.08); padding: 1px 6px; border-radius: 4px; font-weight: 600; }
</style>
```

**Color economy (mandatory):**
- **Purple** appears *exactly once* — the `<span class="hero">` in §7. The `<div class="quote">` Research Summary is purple-text by the style rule but is structure, not a second hero.
- **Blue** is everything else (headings, table headers, links, labels).
- **Red** is *only* the backticked numbers (`code`). Body prose is dark.
- **No other colors.** Do not introduce greens/amarants as CSS — severity uses emoji (🟢🟡🔴), not recolored text.

---

## The `.html` anatomy (rendered twin)

Exactly **one standalone HTML file** derived from the `.md`, in this order:

```text
1. Sticky topbar   Brand mark (emoji + ticker) · exchange label · live-price pill · 6 nav anchor links
2. Page head       Kicker pill · H1 (EQUITY RESEARCH REPORT: <TICKER>) · subtitle · 6 meta-grid cards · valuation-status callout
3. KPI strip       4 cards: Revenue (TTM) · Net Profit (TTM) · ROCE/ROE · FCF Yield
4. Section 1-7     Each as <h2 id="..."><span class="num">N.</span> Title</h2> followed by the rendered .md body (callouts, tables, quotes, hero)
5. Verdict box     Strengths + Concerns bullets · Blended DCF + Buy Zone lines (extracted from section 7)
6. Hero takeaway   The single <div class="hero"> from section 7, restyled to the demo.html hero block
7. Footer          Disclaimer + ticker/date line + headline metrics line
```

The file is a full `<!DOCTYPE html>` document — openable directly in any browser, no server needed.

### Design system — demo.html style
The visual system is captured in `assets/demo-report.css` (the verbatim token set from `stock-ui/demo.html`, IRCTC Sep 3 2026). **Copy that file into a `<style>` tag at the top of `<head>` — verbatim. Never edit the tokens. Never invent new colors.**

Tokens (`assets/demo-report.css` is the source of truth):
`--purple #692D9A` · `--purple-text #4A1F7A` · `--blue #0B5FC0` · `--bg #f8f9fb` / `--bg2 #f1f3f8` · `--surface #fff` · `--border #e2e8f0` · `--text #1F1B2E` · `--muted #64748b` · `--gold #92400e` · `--red #dc2626` · `--green #059669` · `--amber #d97706`.

Components used: `.topbar` (sticky, blur) · `.brand-mark` · `.pill` (green/amber/red/blue/purple) · `.kicker` · `.meta-grid` / `.meta-card` · `.valuation-status` · `.kpi-row` / `.kpi` · `.callout` (purple/blue) · `.card` (+ `.highlight`) · `.quote` (+ `.warning`) · `.hero` · `.val-visual` / `.bar-track` / `.bar-fill` / `.bar-marks` · `.dashboard` / `.flag-grid` / `.flag` / `.sev` · `.verdict-box` · `.btn` / `.btn.primary` / `.btn.purple`.

> **Numbers in the HTML:** the source `.md` uses **red** `#B91C1C`. In the rendered HTML, backticked numbers become `code` which the demo.css styles **purple** per the YK light spec. This is intentional and accepted — keep the demo.css `code` rule as-is (it was locked in after user review). Do **not** inject a gold `code.gold` variant unless the user explicitly asks for the dark-gold look.

### The `<style>` block (verbatim)
Always embed `assets/demo-report.css` inside `<style>` at the top of `<head>`. **Strip the `.md`'s own YK light-bg `<style>` block** before rendering — the demo.css supersedes it (avoid duplicate/conflicting `code` rules).

### Data extraction rules (renderer)
The renderer reads the `.md` and extracts two layers:

**Layer 1 — Metadata (topbar / meta-grid / KPI strip):**

| Field | Source | Pattern |
|---|---|---|
| Ticker | Filename | first `_`-token of `<TICKER>_<Mon>_<Day>_<Year>.md` |
| Date | Filename | `Sep_3_2026` → `September 3, 2026` |
| Live price | `.md` body | `(?:At\|Spot\|Live)\s+\`₹([\d,]+(?:\.\d+)?)\`` |
| Market cap | §3 table | `\*\*Market Cap\*\*.*?\`₹([\d,]+)\s*Cr\`` |
| Sector | `.md` body | `Sector[:\s]+([^\n\|]+)` or first sentence of §1 |
| Valuation status | `.md` body | first match of `(🟡\|🟢\|🔴)?\s*(Fairly Valued\|Undervalued\|Overvalued\|Modestly (Under\|Over)valued\|Cheap\|Expensive)` |
| Revenue TTM | §3 table | `\*\*Revenue\*\*.*?\`₹([\d,]+)\s*Cr\`` |
| Net Profit TTM | §3 table | `\*\*Net Profit\*\*.*?\`₹([\d,]+)\s*Cr\`` |
| ROCE / ROE | Whole `.md` | `(\d+(?:\.\d+)?)%\s*\/\s*(\d+(?:\.\d+)?)%` |
| FCF yield | §3 table | `\*\*Free Cash Flow\*\*.*?\`₹([\d,]+)\s*Cr\`.*?\`([\d.]+)%\`` |

If a field can't be extracted, fill `—` rather than failing.

**Layer 2 — Section bodies (sections 1-7):** Split the `.md` by `/^## (\d+)\.\s+(.+)$/m`. For each section, render the body markdown, then post-process:
1. **Blockquotes** → `<div class="quote">` (default) or `<div class="quote warning">` if content contains `WARNING` or `BALANCE-SHEET`.
2. **§6 (Red Flags) table** → wrap `🔴 High` / `🟡 Medium` cells in `<span class="pill red">` / `<span class="pill amber">`. After the table, append a `<div class="dashboard">` with a `<div class="flag-grid">` of flag tiles (one per row; 5 or 6 rows supported).
3. **§5 (DCF) table** → wrap the "Blended Intrinsic" row's last cell in a green pill. Wrap the ASCII valuation bar (fenced code block) in `<div class="val-visual">` with a real `.bar-track` (width = `(IV − WS Low) / (DCF − WS Low) × 100%` rounded) and `.bar-marks` (WS Low · Live · Buy Zone · IV · DCF).
4. **§7 (Verdict)** → wrap the Research Summary block in `<div class="card highlight">`. Wrap the strengths/concerns blockquote in `<div class="verdict-box">`. Extract the hero text and re-render as the demo.html `<div class="hero">` with a "🎯 The Verdict" label.
5. **`<span class="hero">` from the `.md`** → keep (demo.css has `.hero`); add the "🎯 The Verdict — hero takeaway" label as a `.label` div above it.

The 7 section headings rewrite to `<h2 id="<slug>"><span class="num">N.</span> Title</h2>` with slugs (`overview`, `strengths`, `financials`, `valuation`, `flags`, `verdict`). Section 5 DCF has no anchor — the nav skips it; the section is reachable from the page top.

### HTML post-processing details
- **§1** overview: paragraph · segments table · `> Strategic Position:` blockquote → `<div class="quote">`. Optionally wrap a short first paragraph in `<div class="callout purple">` with 🛡️ icon.
- **§3** financials: table renders; `> ⚠️ BALANCE-SHEET WARNING` → `<div class="quote warning">`.
- **§4** valuation: if the last column has 🟢/🟡/🔴 + phrase, wrap each in `<span class="pill green|amber|red">`.
- **§5** DCF: "Blended Intrinsic" row gets a green pill in its valuation cell. ASCII bar → `.val-visual` with real `.bar-fill`. DCF Parameters bullet list (after the bar) wrapped in `<div class="card">` with `⚙️ DCF Parameters` H3.
- **§6** red flags: numbered table with severity pills + a `<div class="dashboard">`/`<div class="flag-grid">` of flag tiles (label + `.sev high`/`.sev med`; 5 or 6 rows supported).
- **§7** verdict: Research Summary → `<div class="card highlight">` (purple label); strengths/concerns → `<div class="verdict-box">`; blended-DCF/buy-zone blockquote → two `<p>` lines inside the verdict box; `<span class="hero">` → `<div class="hero">` with "🎯 The Verdict" label.
- **Footer:** italic disclaimer + `<span style="color:var(--blue)">TICKER · EXCH · date · Generated by stock skill · demo.html light palette</span>` + muted headline-metrics line.

A small `<script>` at the end intercepts in-page `#anchor` clicks and smooth-scrolls (accounts for the ~56px sticky topbar) — copy the pattern from `examples/` / the existing `Stock/2026-09_html/*.html` footer script.

---

## House-style notes

- **Currency:** Indian names → `₹` + `Cr` / `Lakh` / `T`. US names → `$` + `B` / `T`. Match the listing exchange.
- **Net cash vs net debt:** Net Cash Adjustment uses `+₹XXX Cr` when net cash, `−$X.XXB` when net debt (US). Sign follows economics, not region.
- **Month naming:** full month in the filename (`September`, not `Sep`) is canonical. The HTML twin may use the `Sep` abbreviation to match an existing sibling file; prefer full.
- **Indicative segments:** footnoted `*` on every Indian PSU / thin-disclosure segment table.
- **Yields in the interpretation cell:** always surface the derived multiple (Earnings Yield, FCF Yield, P/S, P/E) inside the snapshot/multiples tables — that's where the "read" lives.
- **Buy Zone = `0.80 × Blended`** exactly, a single value, stated as 20% safety margin.
- **DCF rows:** 4 is canonical; 5 is allowed when both Forward P/E *and* EV/EBITDA peer cross-checks are material — then Blended = equal weight on DCF + all peer rows.

---

## Procedure when invoked

1. **Resolve the ticker + market.** If a `_guided_demo.md` exists for that ticker in `Stock/<YYYY-MM>/`, treat it as the format source-of-truth. If the user passed financials, use them; otherwise state clearly that live data must be supplied or fetched — never invent numbers.
2. **Create the output folders** `Stock/<YYYY-MM>/` and `Stock/<YYYY-MM>_html/` if missing.
3. **Author the `.md`** with the verbatim `<style>` block + all 7 sections + disclaimer, following the section spec.
4. **Run the quality gate** (below) before saving the `.md`.
5. **Render the `.html` twin:**
   - Read the `.md`, extract metadata (Layer 1) and section bodies (Layer 2).
   - Strip the `.md`'s YK light-bg `<style>` block.
   - Build the template: topbar → page-head → KPI strip → 7 sections → verdict-box → hero → footer. Embed `assets/demo-report.css` verbatim in `<head>`. Apply the post-processing transforms.
   - Save to `Stock/<YYYY-MM>_html/<TICKER>_<Mon>_<Day>_<Year>.html`.
6. **Print a 3-5 line preview:** both file paths, ticker, date, sections produced, and the valuation verdict line.
7. **End** with the standard follow-up question: *"Want changes to the design? (yes / no / different palette)"* — unless the user requested `.md`-only.

**Re-render-only mode (existing `.md`, new HTML):** if the user points at an existing `Stock/<YYYY-MM>/<TICKER>_*.md` and wants HTML, skip steps 1-4 and run 5-6.

---

## Quality gate (run before saving)

```text
HEADER   ☐ 🚀/ticker-emoji title + 6-label blockquote (TICKER / REPORT DATE / LIVE PRICE / MARKET CAP / SECTOR / VALUATION STATUS)
STRUCT  ☐ Exactly 7 ALL-CAPS sections in order ☐ <style> prepended verbatim ☐ One hero + one quote in .md
TABLES  ☐ Every number in backticks ☐ §3 = 5 rows ☐ §4 = 6 rows ☐ §5 = DCF table → 📌 NOTE → 📈 Bar → ⚙️ Params ☐ §6 = Dashboard strip
DATA    ☐ DCF params fully disclosed ☐ Buy Zone = Blended × 0.80 (single value) ☐ ≥1 🔴 High if consensus < spot
CLOSE   ☐ Verdict = one 🎯 question/sentence, not hedge ☐ Disclaimer italicized
HTML    ☐ demo-report.css embedded verbatim (and only that) ☐ .md <style> stripped (not duplicated) ☐ 7 numbered <h2> with .num spans
         ☐ topbar (ticker + price pill + 6 nav) ☐ meta-grid 6 cards ☐ KPI strip 4 cards ☐ .hero exactly once
         ☐ Red Flag severity in .pill.red/.pill.amber ☐ .val-visual with real .bar-fill ☐ .dashboard/.flag-grid present
FILES   ☐ One .md in Stock/<YYYY-MM>/ ☐ One .html in Stock/<YYYY-MM>_html/ (unless .md-only requested)
```

---

## Reference examples

- **`examples/IRCTC_Sep_3_2026.md`** — canonical narrative-heavy report (regulated-tollbooth framing). Note: its §5 has 5 rows (two peer methods) — acceptable; blended = equal weight on DCF + peer rows.
- **`examples/BETA_September_12_2026.md`** + **`examples/BETA_Sep_12_2026.html`** — **Beta Drugs small-cap oncology** (live Sep 12 2026, `₹2,118.50` / `₹2,349 Cr`, `51.5x` P/E, `100-day` CCC, `₹-16 Cr` FCF). Demonstrates: indicative 4-engine segment table, normalized-FCF DCF (`₹30 Cr` base vs reported `₹-16 Cr`), `25%` MOS for small-cap illiquidity, and full demo.html twin with muted purple codes.
- **`examples/ITC_September_10_2026_UI_Blue.html`** and **`..._UI_Purple.html`** — the dark-theme dashboard twins (legacy; this skill emits only the unified demo.html light page). Kept for reference only.
- **`Stock/2026-09/ITC_September_10_2026_styled.md`** and **`Stock/2026-09_html/ITC_September_10_2026_styled.html`** — live in-folder report + its rendered twin conforming to this spec (Meta-style framing, Valuation-Bar, DCF-Parameters, Red-Flag Dashboard, demo.html chrome).
- **`Stock/2026-09_html/AAPL_Sep_3_2026.html`** — the cleanest rendered twin reference (full chrome, nav, meta-grid, KPI strip, hero, footer script).

---

## What this skill is not

- **Not a data fetcher.** It needs financials from the user, filings, or a fetch step — it does not silently invent numbers.
- **Not a chart/visualization generator.** The demo.html style is markup + CSS only (the valuation bar is a CSS-painted `.bar-fill`, not an SVG/Chart.js).
- **Not financial advice.** The disclaimer is mandatory on every `.md` and `.html` file.
- **Not multi-name / screen.** Single-name, long-only, bottom-up only.

---

*Last updated: 2026-09-10 · unified author+render `stock` skill · 7-section ALL-CAPS narrative `.md` (YK light-bg, red numbers) + rich demo.html-style `.html` twin (light palette, purple hero, blue workhorse) · reports in `Stock/<YYYY-MM>/` and `Stock/<YYYY-MM>_html/` · CSS in `assets/demo-report.css`.*
