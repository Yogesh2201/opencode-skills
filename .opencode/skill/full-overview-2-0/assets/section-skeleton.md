# Section skeleton (identical in all three versions)

Copy this order exactly. Only company data changes.

## Page order

1. **Header** — meta chips (Filings-only · NSE · BSE · HQ · date · surface) → kicker → H1 → subtitle → lede
   - Top nav (sticky): `01 What they do` → `02 Competitors` → `03 Products` → `04 Vision` → `04 Valuation` → `05 Trends` → `06 Forecast` → `Takeaway`
   - Far right: **06 FC toggle** — pill `06 FC | Bear · Base · Bull` (`#hdrFcToggle` + 3 `button.hfc-chip` with `data-hfc="bear|base|bull"`). Global filter for both forecast charts (`[data-fc="price"]` + `[data-fc="mcap"]`) via `panel.setAttribute('data-off', ...)`. Syncs bidirectionally with per-panel `.fc-chip` toggles.
2. **KPI row** — 5 tiles, first is hero: Revenue TTM · Operating quality · Global footprint · Market cap · Order book
3. **01 What the company does** — idea line → 3 pillars → money-flow (prime mover → TDPS generator → end use) → money proxies (donut/views: `#seg/#donut/#leg/#donutnote/#groupedMini`) → business-model quote
4. **02 Geographical competitors** — peer share bars (`.bar-row` + `.hairline-grid`) → accessibility peer table → HQ-geography mini-panel
5. **03 Key products** — 6 product families → 3 extras → MVA spectrum (`.spectrum`) → **Financial snapshot & quality read** (5-row table: MCap 100% / Revenue 8.9% / NP 1.15% / Op Profit+FCF / Net Cash 2.6% + `quote warning` on 68%→93% export + 18% OPM floor)
6. **04 Company vision** — verbatim quote → 4 funded pillars (`.vision-grid` / 4 `tile`) → one-line vision callout
7. **04 Valuation + DCF** (`#s04v`, `num 04` duplicate) — quote thesis → 4-row multiples table (Trailing 86.8× / Forward ~78× / EV/EBITDA ~60.7× / OPM 18%) → 4-tile grid (DCF ₹812 / Fwd ₹637 / EV ₹694 → Blended ₹714 → Buy ₹571, 20% MOS) → blended approach table → methodology quote (FCF ₹192, WACC 10.5% g6%, net cash +₹612, equal-weight) → `val-visual` bar (`bar-track` + `bar-fill` 58% + `bar-marks`)
8. **05 Key trends & big messages** — 5 trends (tabbed: `#trendTabs/#tpKicker/#tpTitle/#tpBody/#tpCta` + `#tpPrev/#tpNext`) → 3 management messages (`.msg-grid`) → **Red flags — 2 HIGH · 3 MEDIUM** (5-row table + `.flag-grid` 5× `flag` with `sev.high/med` → `2 HIGH · 3 MEDIUM · 0 LOW`) → **Bottom line — six lenses** (`.msg-grid` 6×: Core idea / What changed / Hidden insight / What breaks / Open question / Takeaway)
9. **06 5-year forecast** (`#s06`) — outcomes (Bear/Base/Bull KPI row) → `fc-note` (export flow + PAT margin + P/E) → twin interactive charts (`[data-fc="price"]` / `[data-fc="mcap"]` with `fc-legend` `.fc-chip[data-s]` toggles, `fc-plot` SVG with `fc-line/fc-dot/fc-end/fc-guide/fc-tip`, header global toggle sync) → assumptions table → year path (price + MCap 6-col) → key insight quote (EPS spread vs price spread) → monitor axis-note
10. **One-line takeaway** (`#s09`) — hero block (dark / `var(--orange)` rule in Plain, orb gradient in Gemini)
11. **Footer** — method · palette · disclaimer (SEBI, illustrative) · render line

## IDs / anchors (HTML versions)

| id | Section |
|---|---|
| `s01` | What the company does |
| `s02` | Geographical competitors |
| `s03` | Key products (+ Financial snapshot) |
| `s04` | Company vision |
| `s04v` | Valuation + DCF (duplicate num 04) |
| `s05` | Key trends & big messages (+ Red flags + Bottom line) |
| `s06` | 5-year forecast (with header FC toggle) |
| `s09` | One-line takeaway |
| `hdrFcToggle` | Header 06 FC toggle pill (contains 3 `hfc-chip`) |
| `seg, donut, leg, donutnote, groupedMini` | Money proxies donut |
| `trendTabs, tpKicker, tpTitle, tpBody, tpCta, tpCount, tpPrev, tpNext` | Trend tabs |
| `progress, totop` | Chrome (Plain) / `gpFab, gpPanel` (Gemini) |

Nav labels: `01 What they do · 02 Competitors · 03 Products · 04 Vision · 04 Valuation · 05 Trends · 06 Forecast · Takeaway` + header `06 FC` toggle pill

## Heading style

- MD: `## 01 🏢 What the company does` … `## 04 🎯 Company vision` → `## 04 💰 Valuation + DCF` → `## 05 📈 Key trends & big messages` (with `### Red flags` + `### Bottom line`) → `## 06 🔮 5-year forecast` → `## 🎯 One-line takeaway`
- HTML: `<h2 id="s0N"><span class="num">0N</span> 🔘 Title <span class="rule/h2-rule"></span></h2>` + `.section-note` paragraph

## Fixed copy blocks (do not paraphrase)

- **Idea line:** *the business is **engineering hours + precision metal** sold through long-cycle OEM partnerships.*
- **Vision quote:** *"We power every possibility. We power the world."* (AR FY25, Corporate Overview pp. 2–5)
- **Financial snapshot sub:** *TTM to Sep 18, 2026 — growth vs premium: Revenue +54% TTM on 18% OPM. ROCE 34.0% fuels the multiple.* + warning *68% → 93% export inflow (+41% YoY to ₹14,783M FY25) — concentration + lumpiness is the real FY26-27 risk; 18% OPM must hold as third plant ramps Q4 FY26*
- **Valuation thesis:** *"Own the engineering, but let a scare give you the price." — 86.8× P/E prices the 40–45 MW US data-centre supercycle.*
- **Takeaway:** *TD Power Systems doesn't sell generators — it sells **certainty of power where failure is not an option**, and the filings say the next chapter is **US data-centre gas power at 40–45 MW + hydro stability + export OEM depth** — engineered in Bengaluru, designed in the UK, installed in 111 countries.*
- **Disclaimer:** *Educational only, not investment advice. Section 04 Valuation is independently modelled (WACC 10.5%, g 6% — disclosed); Section 06 is an illustrative Bear/Base/Bull walk — no price target. Consult a SEBI-registered advisor. Peer % is illustrative share of one pot, not a TAM.*
