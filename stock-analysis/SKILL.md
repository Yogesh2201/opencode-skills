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

# Stock Analysis — Skill Specification (`stock-analysis`)

> **Source of truth:** `C:\Users\Yogesh Kumar\Downloads\CLAUDE-CODE\Stock` — audited 2026-09-10. This skill codifies exactly what that folder does so any agent can reproduce it without guessing.
>
> **Scope:** Every report in `Stock/2026-09` (14 `.md`, 13 complete) follows one styled template. The output of this skill is **one** styled `.md` in the YK light-bg palette (red `#B91C1C` backticked numbers) plus an optional styled `.html` twin in the parallel `Stock/<YYYY-MM>_html/` folder. Same 7 sections, same `<style>` block, same hero verdict.
>
> **Invocation:** `/stock-analysis` or natural language — *"write a stock report on TCS"* / *"DCF on AAPL"* / *"should I buy RELIANCE"*.

---

## What `Stock/` actually contains (audit 2026-09-10)

| Path | Count | Status |
|---|---|---|
| `Stock/2026-09/*.md` | 14 | 13 complete 7-section reports (175–201 lines each) + 1 stub (`INFY_Sep_10_2026.md`, 16 lines, style-only) |
| `Stock/2026-09_html/*.html` | 13 | 1:1 HTML twins for every complete `.md` (42–50 KB each, YK light-bg `demo-report.css`) |

**Period covered:** Sep 3, 5, 10 — 2026. Tickers observed: `AAPL, IEX, IRCTC, ITC (×3), MSFT, PLTR, RELIANCE, SPCX, TCS, TRENT, TSLA` + stub `INFY`. Exchanges: `NSE` (India), `NASDAQ` (US), `BSE`. Currencies: `₹`/`Cr`/`Lakh Cr` for NSE, `$`/`B`/`T` for US.

**Uniform `<style>` block:** All 14 `.md` files prepend the identical 13-line YK light-bg block verbatim (code color `#B91C1C`, `font-weight: 600`). No file invents new tokens. The block is the design contract — omit it and the file reads as off-template.

**Naming observed vs spec:** Spec says `<TICKER>_<Month_Day_Year>.md` with full month. On-disk reality is `<TICKER>_Sep_<D>_<YYYY>.md` (abbrev `Sep`) for 12/13 complete files; one file uses `ITC_September_10_2026_styled.md` (full month + `_styled` suffix). This skill accepts both but **writes** the abbrev form `Sep` to stay bug-compatible with the 12-file majority.

**HTML twin location observed:** Twins live in the parallel `Stock/<YYYY-MM>_html/` folder, same basename with `.html` extension (e.g., `2026-09/TCS_Sep_3_2026.md` → `2026-09_html/TCS_Sep_3_2026.html`). The `stock-ui/server.js` in `CLAUDE-CODE/stock-ui` also enforces this layout via `htmlPathFor()`. This skill preserves it.

---

## When to use / when not to

**Use for:**
- Single-name equity research on a publicly listed company (NSE/BSE/NASDAQ).
- User asks "stock report", "equity research", "DCF analysis", "valuation breakdown", "should I buy X", or pastes raw financials and wants a structured write-up.
- Durable artifact the user will refer back to (saved to `Stock/`).

**Not for:**
- Watchlist updates, ETF/portfolio reviews, earnings-call summaries, or anything that doesn't fit the 7-section shape.
- Short notes — those don't need 7 sections and a DCF.

---

## The output shape — 7 sections, ALL CAPS, in order

Exactly seven numbered sections. **Headers are ALL CAPS** (Adobe convention). No section may be skipped except when source genuinely has no data for it.

```text
1. COMPANY OVERVIEW          Bold intro + 3-5 framing bullets + segment vertical table + Strategic Position blockquote
2. KEY COMPETITIVE STRENGTHS  3 framing bullets + 3-5 row moat table (every cell carries a number, emoji in strength column)
3. FINANCIAL SNAPSHOT & QUALITY READ  3 bullets + 4-col table (Metric/TTM Value/%MC/Interpretation) + ⚠️ BALANCE-SHEET WARNING blockquote (3 paragraphs)
4. VALUATION MULTIPLES        3 bullets + 4-col table (Metric/Value/Benchmark/Read with 🟢🟡🔴) + * footnote blockquote
5. DCF & INTRINSIC VALUATION  Valuation table + 📌 METHODOLOGY NOTE + 📈 Valuation Bar (fenced ASCII) + ⚙️ DCF Parameters
6. RED FLAGS                  3 bullets + numbered table (#/Flag/Severity/Evidence) + Red Flag Dashboard (fenced ASCII strip)
7. BOTTOM LINE & VERDICT      <div class="quote"> Research Summary + > ✅❌ + fair value + Buy Zone + <span class="hero"> 🎯 closing question + italic disclaimer
```

Drop a section only if the source genuinely has nothing for it. Do not add sections.

---

## Header format (mandatory, byte-for-byte)

Every report opens with this exact two-block header:

```markdown
# 🚀 EQUITY RESEARCH REPORT: <COMPANY NAME>

> **TICKER:** `<EXCHANGE: TICKER>`  (e.g., `NSE: TCS` or `NASDAQ: AAPL`; dual listing `NSE: RELIANCE | BSE: 500325` allowed)
> **REPORT DATE:** `<Month D, YYYY>`  (e.g., `September 3, 2026`)
> **LIVE PRICE:** `₹3,032` or `$235.40` (<date> close — last trading session)
> **MARKET CAP:** `₹10,97,000 Cr` or `$3.51T`  (use ₹/Cr for NSE, $/B/T for US)
> **SECTOR:** <one-line sector description>
> **VALUATION STATUS:** 🟢/🟡/🔴 <CAPS status> — ⚠️ <one-line caveat>
```

The 🚀 emoji in the H1 and the six bold-label lines in the blockquote are non-negotiable. They are the visual signature — drop them and the file reads as off-template.

---

## Color hierarchy — YK light-bg (verbatim)

| Color | Hex | Use | Max |
|---|---|---|---|
| **Purple (deep)** | `#692D9A` | H1 only | 1 |
| **Purple (hero)** | `#4A1F7A` | Closing verdict `<span class="hero">` | 1 |
| **Purple (lavender)** | `#4A1F7A` on `rgba(105,45,154,0.05)` | Research Summary `<div class="quote">` | 1 |
| **Blue (workhorse)** | `#0B5FC0` | H2/H3, table `th`, accents, dividers | many |
| **Dark body** | `#1F1B2E` | Paragraphs, lists, disclaimer | bulk |
| **Red (data)** | `#B91C1C` | **All inline numbers in backticks** (`₹3,032`, `$248`, `+5%`, `27.4x`) — light `.md` only, `font-weight: 600` | many |
| **Gold (dark HTML)** | `#FFD166` | Numbers in dark Neon HTML variant (not used in `2026-09_html` which is light-bg) | — |
| **Blue (HTML blue theme)** | `#0B5FC0` | Numbers in `as html blue` variant | — |
| **Purple (HTML purple theme)** | `#692D9A` | Numbers in `as html purple` variant | — |

**Rule:** Purple earns its place once — on the closing verdict. Red earns its place everywhere numbers appear in the light `.md`. Blue holds the structure. Dark is the floor. No other purple anywhere.

---

## File format and naming

**Primary artifact:** One styled `.md` with `<style>` prepended.

```text
Stock/<YYYY-MM>/<TICKER>_<Mon>_<D>_<YYYY>.md
Stock/<YYYY-MM>_html/<TICKER>_<Mon>_<D>_<YYYY>.html   ← optional twin
```

Examples from the audited folder (canonical):
- `Stock/2026-09/TCS_Sep_3_2026.md` + `Stock/2026-09_html/TCS_Sep_3_2026.html`
- `Stock/2026-09/AAPL_Sep_3_2026.md` + `Stock/2026-09_html/AAPL_Sep_3_2026.html`
- `Stock/2026-09/ITC_Sep_5_2026.md` + `Stock/2026-09_html/ITC_Sep_5_2026.html`
- `Stock/2026-09/ITC_September_10_2026_styled.md` ← variant with full month + `_styled` (accept, don't generate)

**Observed majority writes `Sep` (abbrev), not `September`.** The skill writes `Sep` to stay compatible with 12/13 files.

**INFY stub rule:** `INFY_Sep_10_2026.md` is 16 lines (style-only, no sections). This is a failed generation — the agent must validate `lines > 100` and `sections == 7` before declaring success; otherwise retry or surface the error.

---

## The standard `<style>` block (prepend verbatim — do not modify)

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

> **Note on weight:** The audited `Stock/2026-09` files use `font-weight: 600` for `code`. The `Open_Code/.agents/skills/stock-analysis` spec uses `700`. Both render red; `600` is the on-disk truth for `Stock/`.

---

## Section-by-section rules (codified from 13 complete files)

### 1. Company Overview
- **Bold intro** naming the company and its standard-setting position (1–2 sentences, include scale: revenue, employees, devices, market cap).
- 3–5 framing bullets **between** intro and table — crystallize the thesis ("one-company-wearing-X-costume", mental model, why framing matters here).
- **Segment/vertical table:** one row per business vertical, emoji in bold cell (`📱 🍱 🏭 💰` etc.), columns: Vertical | Nature | TTM Revenue | Share of Mix.
- Closing `>` blockquote **Strategic Position:** one line, no preamble.

### 2. Key Competitive Strengths
- 3 framing bullets **before** table — what question the moat answers, threats tested against, durability ranking.
- Table 3–5 rows. Each row = one strength. Every cell carries at least one number in backticks. Emoji in bold cell (`🛡️ 📈 💰 🏦`).
- Typical strengths observed: Regulatory Monopoly, Capital Efficiency (ROCE/ROE), Cash Conversion (FCF/PAT), Dividend, Vertical Stack.

### 3. Financial Snapshot & Quality Read
- 3–5 bullets **before** table — point to the one row that drives the valuation debate.
- 4-col table: Metric | TTM Value | % of Market Cap | Analyst Interpretation. Rows always: Market Cap, Revenue (TTM) with P/S, Net Profit with earnings yield, FCF with FCF yield, Debt-to-Equity.
- Follow with `> ⚠️ **BALANCE-SHEET WARNING**` — exactly 3 paragraphs, bold-led, covering bull case + bear case + what to watch.

### 4. Valuation Multiples
- 3 bullets **before** table — read multiples as a system, what outcome is priced, what is not priced.
- 4-col table: Metric | Value | Benchmark | Valuation Read. Use 🟢🟡🔴. Benchmarks are approximate with `*`.
- Footnote `> \* Historical and sector reference multiples are **approximate**...` is mandatory.

### 5. DCF & Intrinsic Valuation
- **Observed default is 5 rows** (not 4): `DCF Base | Forward P/E | EV/EBITDA | Blended Intrinsic | Buy Zone`. 11/13 complete files follow this 5-row shape.
- **Allowed variants** (documented, don't invent new ones):
  - `ITC Sep 5`: 6 rows — adds **Dividend Discount (Gordon)** as 4th method.
  - `ITC Sep 10 styled`: 7 rows — **DCF Bull + DCF Bear + DDM** bracketing.
  - `RELIANCE`: 10 rows — **SOTP** (Jio + Retail + O2C + New Energy + Net Debt) before the 5-row core.
  - `SPCX`: 6 rows — **DCF Base (g 0%) + Risk-Adjusted DCF + SoTP + Peer EV/Pipeline + Blended + Buy Zone** (micro-cap exception).
  - `TSLA`: 6 rows — adds **Bull-Case DCF (Robotaxi/Optimus)**.
  - Spec's "4-row" (`DCF Base | Relative Peer Multiples | Blended | Buy Zone`) is valid as a collapsed form — use when only one peer method is material.
- Followed by exactly: `> 📌 **METHODOLOGY NOTE:**` → `---` → `## 📈 Valuation Bar (Persistent Systems Style)` (5-col fenced ASCII: WS LOW | CURRENT | BUY ZN | IV | DCF) with 4 bullet metadata lines → `---` → `### ⚙️ DCF Parameters` (WACC, Rf, ERP, Beta, Cost of Equity, Base FCF, growth fade, terminal g, net debt/cash, shares).

### 6. Red Flags
- 3 bullets **before** table — severity convention (🔴 High breaks thesis, 🟡 Medium pressures it, 🟢 Low watches it).
- Numbered table: `#` | Red Flag | Severity | Evidence. 5 flags typical, 6 allowed (SPCX has 6). Each Evidence cell must cite numbers in backticks.
- Close with `### Red Flag Dashboard` fenced ASCII strip — one line per flag, emoji + label.

### 7. Bottom Line & Verdict
- `<div class="quote">` **RESEARCH SUMMARY** — 2–3 paragraphs, bold-led, frame as "mirror image of <prior peer>" when relevant.
- `>` blockquote with `✅ **Strengths:**` and `❌ **Concerns:**` as bulleted sub-items + `**The blended DCF model calculates fair value at ...**` + `**Disciplined Margin-of-Safety Buy Zone: ...**`.
- **Closing `<span class="hero">🎯 The verdict hinges on one question: ...</span>`** — single hero moment, 🎯 emoji, one question the reader must answer.
- *Disclaimer:* italicized, educational-only, sources named (Screener.in / NSE / SEC filings / Yahoo Finance), "not financial advice", consult registered advisor.

---

## Guided-bullet convention

- 3–5 bullets max per section (sections 1,2,3,4,6). Format `- **Bold lead-in:** rest of thought`.
- Bullets go **around** tables — before, never inside.
- Interpretation/framework, not data repetition — they teach what to look at.
- Drop bullets for sections 5 and 7 — those have their own visual structure.

---

## Procedure when invoked

1. **Confirm ticker + date + exchange + currency.** If user gives ticker without date, ask — do not guess. Map `NSE/BSE → ₹/Cr`, `NASDAQ/NYSE → $/B/T`.
2. **Gather financials.** Live price, market cap, TTM revenue/NP/FCF, debt, OPM/ROCE/ROE, segment data, consensus target, 52W range, recent performance. Sources: exchange filings, Screener.in, Yahoo Finance, sell-side consensus. Note missing/vendor-blocked data explicitly.
3. **Run DCF independently** if no vendor DCF. Disclose all parameters in the DCF Parameters block. State "independently modelled, not vendor-quoted".
4. **Write 7 sections in order** following Adobe ALL-CAPS convention. Numbers in backticks. Headings in ALL CAPS. One hero + one quote. Guided bullets where they earn place, never inside tables.
5. **Write one `.md` + optionally one `.html`.** Path: `Stock/<YYYY-MM>/<TICKER>_Sep_<D>_<YYYY>.md` and `Stock/<YYYY-MM>_html/<TICKER>_Sep_<D>_<YYYY>.html`. Prepend `<style>` verbatim.
6. **Validate before success:** `headers == 7` in order, `lines > 100`, `<style>` present, `hero == 1`, `quote == 1`, `DCF rows >= 5` (or 4 if collapsed). If `INFY`-style stub (< 100 lines), retry.
7. **Print 3–5 line preview + file path.** Offer HTML follow-up: *"Want the HTML version? Choose: **blue**, **purple**, or **dark** — say `as html blue` / `as html purple` / `as html dark`."*

---

## Quality gate (run before saving)

> **If 80% of prose were removed, would the tables and red numbers still carry the argument?** If not, restructure.

```text
HEADER  ☐ # 🚀 EQUITY RESEARCH REPORT: <NAME> + 6-label blockquote (TICKER/REPORT DATE/LIVE PRICE/MARKET CAP/SECTOR/VALUATION STATUS)
STRUCT  ☐ Exactly 7 ALL-CAPS sections in order ☐ <style> prepended verbatim ☐ One hero + one quote only ☐ Lines > 100
TABLES  ☐ Every number in backticks = red #B91C1C ☐ §5 = 5 rows default (DCF Base | Forward P/E | EV/EBITDA | Blended | Buy Zone) or valid variant (SOTP/risk-adj/DDM/bull-case) ☐ §5 → 📌 NOTE → 📈 Bar → ⚙️ Params ☐ §6 → Dashboard strip ☐ No bullets inside tables
CONTENT ☐ DCF params fully disclosed ☐ Buy Zone = Blended × 0.80 (or 0.85 if stated) single value ☐ ≥1 🔴 High if near 52W high or stretched multiple ☐ Verdict = one 🎯 question ☐ Disclaimer italicized
DELIVERY ☐ File in Stock/<YYYY-MM>/ with <TICKER>_Sep_<D>_<YYYY>.md naming ☐ HTML twin in _html if requested ☐ Only ONE .md + ONE .html per ticker-date (no duplicate)
```

---

## What this skill is not

- **Not `text-summary`.** That compresses a long source into a 6-section narrative brief. This builds a financial artifact from raw inputs.
- **Not financial advice.** The disclaimer at the bottom of every report is mandatory.
- **Not a watchlist updater.** One ticker = one report.

---

## House style notes

- **Two decimals of precision** where source provides them. Don't round `$248.30` to `$248`.
- **Backticks for every number a reader might quote** — percentages, multiples, ratios, dollar/rupee amounts, share counts. Don't backtick years.
- **One emoji per row max.** 🟢 🔴 🟡 🎯 📌 ⚠️ ✅ ❌ only. 🚀 only in title.
- **Blockquotes for meta-commentary** (warnings, methodology, strategic position) — they render with a left bar.
- **India note:** For NSE/BSE, use `₹` + `Cr`/`Lakh Cr`, keep code red, keep `% of Market Cap` column. Segment splits for PSUs may be indicative — footnote it.

---

*Last audited: 2026-09-10 against `C:\Users\Yogesh Kumar\Downloads\CLAUDE-CODE\Stock` — 14 md + 13 html, 13 complete, 1 stub (INFY). YK light-bg verbatim, 7-section ALL-CAPS, 5-row DCF default, SOTP/risk-adj/bull-case variants documented, `<style>` font-weight 600 on disk, twin in `_html` parallel folder. Spec version: v4-stock-audit.*
