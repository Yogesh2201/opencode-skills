# Section skeleton (identical in all three versions)

Copy this order exactly. Only company data changes.

## Page order

1. **Header** — meta chips (Filings-only · NSE · BSE · HQ · date · surface) → kicker → H1 → subtitle → lede
2. **KPI row** — 5 tiles, first is hero: Revenue TTM · Operating quality · Global footprint · Market cap · Order book
3. **01 What the company does** — idea line → 3 pillars → money-flow (prime mover → TDPS generator → end use) → money proxies (donut/views) → business-model quote
4. **02 Geographical competitors** — peer share bars → accessibility peer table → HQ-geography mini-panel
5. **03 Key products** — 6 product families → 3 extras → MVA spectrum
6. **04 Company vision** — verbatim quote → 4 funded pillars → one-line vision callout
7. **05 Key trends & big messages** — 5 trends (tabbed in HTML) → 3 management messages
8. **06 5-year forecast** — outcomes (Bear/Base/Bull) → assumptions table → year path → key insight → monitor list
9. **One-line takeaway** — hero block
10. **Footer** — method · palette · disclaimer · render line

## IDs / anchors (HTML versions)

| id | Section |
|---|---|
| `s01` | What the company does |
| `s02` | Geographical competitors |
| `s03` | Key products |
| `s04` | Company vision |
| `s05` | Key trends & big messages |
| `s06` | 5-year forecast |
| `s09` | One-line takeaway |

Nav labels: `01 What they do · 02 Competitors · 03 Products · 04 Vision · 05 Trends · 06 Forecast · Takeaway`

## Heading style

- MD: `## 01 🏢 What the company does` … `## 06 🔮 5-year forecast` → `## 🎯 One-line takeaway`
- HTML: `<h2 id="s0N"><span class="num">0N</span> 🔘 Title <span class="rule"></span></h2>` + `.section-note` paragraph

## Fixed copy blocks (do not paraphrase)

- **Idea line:** *the business is **engineering hours + precision metal** sold through long-cycle OEM partnerships.*
- **Vision quote:** *"We power every possibility. We power the world."* (AR FY25, Corporate Overview pp. 2–5)
- **Takeaway:** *TD Power Systems doesn't sell generators — it sells **certainty of power where failure is not an option**, and the filings say the next chapter is **US data-centre gas power at 40–45 MW + hydro stability + export OEM depth** — engineered in Bengaluru, designed in the UK, installed in 111 countries.*
- **Disclaimer:** *Educational only, not investment advice. Section 06 is an illustrative Bear/Base/Bull walk — no price target. Consult a SEBI-registered advisor. Peer % is illustrative share of one pot, not a TAM.*
