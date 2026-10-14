---
name: forecast-overview
description: Build a standalone 5-year Bear/Base/Bull forecast section (the section-06 block) for a company — outcomes, assumptions, year path, twin interactive price/MCap charts, key insight and monitor line. Uses only its bundled references (references/forecast-section.html for structure/JS, assets/forecast-model.md for numbers, data/*-forecast.json as examples). Use when the user asks for a "forecast overview", "5-year forecast", "bear base bull", or a forecast section without the full company report.
---

# Forecast Overview — standalone 5-year forecast section

Builds **only** the forecast block (section 06 of the full-overview trio) for one
company, then stops. Reference files live in **this skill's own folders**:

| Folder | File | Purpose |
|---|---|---|
| `references/` | `forecast-section.html` | Section structure + JS — s06 card, twin charts, header toggle (keep verbatim, replace data only) |
| `assets/` | `forecast-model.md` | Section 06 numbers reference (anchor, outcomes, assumptions, year path, logic lines) |
| `assets/` | `chart-spec.md` | Chart + encoding spec (series format, ymax/ticks, scenario colours, IDs, toggle sync) |
| `data/` | `tdps-forecast.json` | Example data — manufacturer (TDPS: ₹764 → Bear 444 / Base 1,315 / Bull 2,407) |
| `data/` | `ujjivan-forecast.json` | Example data — SFB/bank (Ujjivan: ₹62.7 → Bear 36.4 / Base 107.9 / Bull 197.6) |
| `data/` | `maxhealth-forecast.json` | Example data — hospital (Max: ₹1,046 → Bear 685 / Base 1,474 / Bull 2,120) |
| `scripts/` | `extract.py` | One-time: re-copy section + data out of full-overview-2-0 (safe to re-run) |

Do **not** read or edit `full-overview-2-0/` — this skill is self-contained.
Re-run `scripts/extract.py` only if the source files were refreshed.

---

## Step 1 — Ask the company (always first)

Ask which company the forecast is for and which anchor to use (filings/TTM price,
MCap, shares + revenue/EPS). If the user names a company covered by `data/`,
offer to reuse that file; otherwise gather: price, MCap, shares (flat — no
dilution unless stated), TTM revenue, EPS, and the three scenario CAGRs.

## Step 2 — Generate the data (JSON only)

Write **only** `data/<company>-forecast.json` in the shape of the examples:

```json
{
  "company": "Name", "short": "Short", "nse": "TICKER",
  "anchor_price": 100.0, "shares_cr": 10.0,
  "forecast": {
    "anchor": { "price": 100.0, "mcap_cr": 1000, "shares_cr": 10.0 },
    "scenarios": {
      "bear": { "price_fy31": 60, "mcap_fy31_cr": 600, "cagr": -9.7, "sales_cagr": 10, "pat_margin_fy31": 9.0, "exit_pe": 45, "eps_fy31": 1.3 },
      "base": { "price_fy31": 175, "mcap_fy31_cr": 1750, "cagr": 11.8, "sales_cagr": 18, "pat_margin_fy31": 13.0, "exit_pe": 65, "eps_fy31": 2.7 },
      "bull": { "price_fy31": 320, "mcap_fy31_cr": 3200, "cagr": 26.2, "sales_cagr": 25, "pat_margin_fy31": 14.5, "exit_pe": 80, "eps_fy31": 4.0 }
    },
    "year_path": {
      "price": { "bear": [100, 79, 68, 62, 60, 60], "base": [100, 109, 121, 133, 153, 175], "bull": [100, 128, 164, 203, 254, 320] },
      "mcap": { "bear": [1000, 790, 680, 620, 600, 600], "base": [1000, 1090, 1210, 1330, 1530, 1750], "bull": [1000, 1280, 1640, 2030, 2540, 3200] }
    },
    "note": "One-line scenario logic (bear = …; bull = …)"
  }
}
```

Discipline is **Revenue → PAT margin → EPS → P/E → Price → MCap**
(bank path does not apply — for SFBs use total income as the revenue proxy).
`MCap = price × shares` every year, shares flat.

## Step 3 — Render the section

Copy `references/forecast-section.html`, keep structure/IDs/JS verbatim, replace
only company data: anchor line, 3 KPI tiles, `fc-note`, chart subs/feet,
assumptions table, year-path line, insight numbers, monitor line, and the JS
`series` arrays + `ymax`/`ticks` per `assets/chart-spec.md`.

## Step 4 — Verify + deliver

- [ ] Outcomes math: FY31 price × shares = FY31 MCap (± rounding)
- [ ] Year path ends at FY31 outcomes; TTM column = anchor
- [ ] Exactly one `</body></html>` if delivered as a page; no build markers
- [ ] Section labelled **Illustrative · not advice / not a price target** + SEBI disclaimer kept

Reply with the file path + one line on what was built.

## Block order (fixed)

```
h2#s06 → section-note (path + anchor + hover hint + not-a-target)
fc-head (FY31E outcomes + Illustrative flag + anchor sub + 5-yr badge)
fc-kpis (Bear/Base/Bull tiles: price + CAGR + MCap)
fc-note (what drives outcomes for THIS company)
fc-stack: [data-fc="price"] + [data-fc="mcap"] twin charts (.fc-chip toggles, guide + tooltip)
assumptions table (CAGR / FY31 revenue / PAT margin / exit P/E / EPS / price / MCap)
axis-note (shares flat + bear/bull logic)
quote (key insight: EPS spread vs price spread — the multiple does the lifting)
axis-note (year path TTM→FY31E + monitor quarterly line)
```

## Output

Single section file (HTML block or `.md` with tables + ASCII paths — ask if not
specified). CSS/JS inlined for HTML. Save next to the requester, default
`Forecast/<Company>-forecast-<YYYY-MM-DD>.<ext>`.
