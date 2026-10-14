---
name: full-overview-2-0
description: Build a full company overview in one of three versions — MD, Gemini HTML, or Plain HTML — using only its bundled references (examples/example-gemini.html, examples/example-plain.html, examples/example.md — byte copies of the Company_Overview/Final TDPS trio — plus assets/ for section skeleton, tokens, forecast model and verify checklist). Use when the user asks for a "full overview", "company overview", "full-overview-2.0" (skill id full-overview-2-0 — opencode skill names cannot contain dots), a v4/forecast style report, or names one of the three versions (md, gemini, plain). Always asks which version first, generates that file, then offers a follow-up: new stock analysis + the two versions not chosen.
---

# Full Overview 2.0 — three-version company report

Builds a complete company/stock overview in **one** of three versions, then loops
into the next question. Reference files live in **this skill's own folders**:

| Folder | File | Purpose |
|---|---|---|
| `examples/` | `example-gemini.html` | Gemini source - structure, tokens, icons, JS |
| `examples/` | `example-plain.html` | Plain interactive render - donut, tabs, charts |
| `examples/` | `example.md` | Portable Markdown - tables, ASCII bars |
| `assets/` | `section-skeleton.md` | Fixed section order, ids, nav labels, verbatim copy blocks |
| `assets/` | `tokens.md` | Plain + Gemini token blocks, palette rules, SVG rule |
| `assets/` | `forecast-model.md` | Section 06 numbers (anchor, outcomes, assumptions, year path) |
| `assets/` | `verify-checklist.md` | Build + headless verification steps, reply format |
| `templates/` | `gemini.template.html` | **Reusable** — verbatim copy of `examples/` for script rendering (0 LLM tokens) |
| `templates/` | `plain.template.html` | same |
| `templates/` | `markdown.template.md` | same |
| `data/` | `schema.json` | JSON Schema for `data/<company>.json` (LLM generates only this, ~600 tokens) |
| `data/` | `ujjivan.json` / `maxhealth.json` / `tdps.json` | Example data files — filings-traced, peer pot, forecast; `ujjivan.json` (SFB, AlphaSpread **Bank** template) + `maxhealth.json` (hospital, AlphaSpread **Net Income** template) are the two AlphaSpread references |
| `scripts/` | `build.py` | Renderer: `templates/` + `data/<company>.json` → `Company_Overview/Final/` (0 LLM HTML tokens) |
| `scripts/` | `verify.py` | Checklist as script (div balance, s04v, hdrFcToggle, val-visual, flag-grid) |
| `scripts/` | `make_placeholders.py` | One-time: hardcoded values → `{{placeholders}}` for cleaner injection |

`examples/` files are byte copies of the canonical trio in `Company_Overview/Final/`
(`TDPS_Gemini-v4-forecast.html` -> `TDPS_Plain-v4-forecast.html` ->
`TDPS_Plain-v4-forecast.md`). If the user refreshes the Final originals, re-copy them here.

Do **not** use `Full-overview/`, `IRCTC_*`, or any other HTML/MD as a template.
The examples supply structure, tokens and section copy; company data changes per request.

---

## Step 1 — Ask the version (always first, before any reading or writing)

Ask via the question tool with exactly these three options:

1. **Markdown** — portable `.md` (tables, ASCII bars, one-line takeaway)
2. **Gemini** — the rich source HTML (Outfit + Material Symbols, sweep gradient, orb field)
3. **Plain** — the neutral light HTML with live donut, trend tabs and forecast charts

Never assume a version. Only after the user picks, continue to Step 2.

## Step 2 — Two paths (token-optimized preferred)

### Path A — Token-optimized (preferred, ~91% saving)

1. Read `data/schema.json` (structure, ~1.5 KB) + `assets/` for section order/tokens — **do NOT read `examples/` or `templates/` fully**.
2. Generate **only** `data/<company>.json` per `schema.json` — filings-traced fields: `meta` (company, NSE/BSE, HQ, kicker), `price` (current, mcap, shares, BV, P/E, P/B), `bank_kpis` / `company_kpis` (revenue, OPM, etc.), `peers` (pot + peers with share), `products` (6 families + 3 extras + spectrum), `financial_snapshot` (5 rows), `vision` (quote + 4 pillars), **`valuation` (AlphaSpread live from https://www.alphaspread.com — DCF Value, Multiples-Based Value, Intrinsic Value, Buy Zone 20% MOS, 4-row multiples + 4 tiles + methodology; DCF params are template-dependent — banks/SFBs use Bank template e.g. Ujjivan 7yr, Discount 10%, Exit 1.8x P/S; hospitals/industrials use Net Income template e.g. Max 15yr, Discount 10.5%, Exit 36.4x P/E)**, `trends` (5 tabs) + `big_messages` + `red_flags` + `bottom_line`, `forecast` (anchor, 3 scenarios, year_path), `takeaway`. See `data/ujjivan.json` (AlphaSpread Bank-template) and `data/maxhealth.json` (AlphaSpread Net Income-template) as references. **~800 tokens, not 20K.**
3. Render via script (0 LLM HTML tokens):
   ```bash
   python .opencode/skill/full-overview-2-0/scripts/build.py --company <slug> --version <gemini|plain|markdown|all> --date <YYYY-MM-DD>
   ```
   Script reads `templates/<version>.template.html` (static, never LLM) + `data/<slug>.json` and writes `Company_Overview/Final/<folder>/<Company>-<YYYY-MM-DD>.<ext>` — folders `MD-YYYY-MM/` · `Gemini-YYYY-MM/` · `Plain-YYYY-MM/` (folder carries the version; no `forecast` infix, no version tag).
4. Verify via script:
   ```bash
   python .opencode/skill/full-overview-2-0/scripts/verify.py Company_Overview/Final/Gemini-<YYYY-MM>/<Company>-<YYYY-MM-DD>.html
   ```
   Checks: no PART_, div balanced, exactly one </body></html>, s01/s02/s03/s04/s04v/s05/s06/s09 + seg/donut/leg/hdrFcToggle/val-visual/flag-grid present, SVG style="fill:var(--)".

### Path B — Heavy (fallback, legacy)

Paths are relative to this skill folder:

- **Markdown** -> read `examples/example.md` fully.
- **Gemini** -> read `examples/example-gemini.html` fully (head/tokens, section markup, JS).
- **Plain** -> read `examples/example-plain.html` fully.

Also open the matching `assets/` files before writing:
`section-skeleton.md` (order + ids + verbatim copy), `tokens.md` (palette),
`forecast-model.md` (section 06 numbers), and run `verify-checklist.md` at the end.

For HTML versions, read in chunks (head/CSS first, then body, then scripts) and
rebuild the file in parts using a `<!--PART_B-->`-style marker if a single write
would exceed ~50 KB. Never leave a build marker in the delivered file.

Use Path B only if the data schema is insufficient for a custom company. Path A covers all standard SFB/industrial cases (Ujjivan + TDPS examples prove it).

## Step 3 — Structure shared by all three versions

Section order and anchors are fixed (identical across the trio — Sep 26 2026 update adds Financial snapshot, Valuation, Red flags, header FC toggle):

```
header meta-chips → kicker → H1 → subtitle → lede → 5-tile KPI row
  └─ top nav: 01 What they do → 02 Competitors → 03 Products → 04 Vision → 04 Valuation → 05 Trends → 06 Forecast → Takeaway + far-right 06 FC toggle pill (Bear/Base/Bull, #hdrFcToggle)
01 What the company does   (idea line, 3 pillars, flow, money proxies [#seg/#donut/#leg], quote)
02 Geographical competitors (peer share bars + HQ geography + accessibility table)
03 Key products             (6 generator families + 3 extras + MVA spectrum + Financial snapshot & quality read — 5-row MCap/Revenue/NP/Op Profit+FCF/Net Cash + warning)
04 Company vision           (verbatim quote + 4 funded pillars)
04 Valuation + DCF  (#s04v) — **AlphaSpread** (4-row multiples + 4 tiles DCF/Multiples/Intrinsic/Buy + blended table + methodology + val-visual bar; params are template-dependent — hospital e.g. DCF 1,465.53 / Multiples 1,026.34 → Intrinsic 1,474.24 → Buy 1,179.39 with 15yr Net Income template, Rev 15.2%, Net Margin 16.8%, Discount 10.5%, Exit 36.4x P/E; SFB e.g. DCF 120.48 / Multiples 64.69 → Intrinsic 120.48 → Buy 96.38 with 7yr Bank template, Rev 14.3%, Net Margin 21.8→19.9%, Discount 10%, Exit 1.8x P/S)
05 Key trends & big messages (5 trends tabbed + 3 management messages + Red flags 2H·3M + flag-grid + Bottom line six lenses)
06 5-year forecast  (#s06)  (Bear/Base/Bull outcomes + assumptions + year path + insight; twin interactive charts [data-fc=price|mcap] with per-panel .fc-chip + global header hfc-chip sync)
one-line takeaway  (#s09)   (dark/orange hero block)
footer                      (method, palette, disclaimer, render date)
```

### Markdown build rules

- Title + `>` meta block (symbol, HQ, price, cap, shares, TTM, OPM, ROCE, P/E, date, HTML twins).
- Tables for the KPI row, money proxies, peers (Peer / HQ / Revenue / Share / Overlap), products, vision pillars, forecast outcomes, assumptions, 6-year year-path.
- ASCII bars for peer share (`█` ≈ 1%) and forecast CAGR; fenced ` ``` ` blocks.
- Section headings `## 01 🏢 What the company does` … `## 06 🔮 5-year forecast`, then `## 🎯 One-line takeaway`, then `### Method / Palette` and the disclaimer.
- Emoji preserved as written in the reference; ₹ / × / → as literal UTF-8.

### Gemini build rules

- Tokens verbatim from the reference `:root`: `--bg #fbfbfd, --surface #ffffff, --surface-2 #f0f4f9, --surface-3 #e9eef6, --ink #1f1f1f, --ink-2 #444746, --ink-3 #8f909c, --ok #1e8e3e, --warn #b06000, --bad #d93025`, `--chart-blue #4285F4, --chart-blue-deep #1967d2, --chart-then #a8c7fa, --chart-context #b3b5be`.
- `--gemini-sweep: linear-gradient(90deg,#4285F4 0%,#5961F0 25%,#9B72CB 50%,#D96570 75%,#FFA756 100%)`. Sweep budget max 3: sparkle mark, gradient H1, hero-tile ring.
- Fonts: **Outfit** + **Material Symbols Rounded** via Google Fonts (`--font: "Google Sans","Outfit","Segoe UI Variable",system-ui,sans-serif`). Use `.material-symbols-rounded` for icons — no emoji as icons.
- Animated orb field with `--drift-period 36s` / `--cycle-period 48s`, themes via `:root[data-t="green-white|green|sunrise|dusk|none"]`, control-panel FAB; honor `prefers-reduced-motion`.
- Radii `--r-sm 12px, --r-md 16px, --r-lg 24px, --r-pill 999px`; shadows `--sh-1..3`; ease `cubic-bezier(.2,0,0,1)`.

### Plain build rules

- Tokens verbatim: `--page #f9f9f7, --surface #fcfcfb, --surface-2 #f1efe9, --ink #1a1a1a, --ink-2 #3d3d3d, --muted #898781, --accent #2a78d6, --accent-deep #1c5cab, --orange #eb6834, --crit #d03b3b, --good #008300, --hairline rgba(11,11,11,.10), --grid #e1e0d9`.
- Two-hue rule: blue carries TDPS, warm gray carries context, **orange is the one hinge** (TDPS subject bar + takeaway closing rule only). System font stack, no icon fonts, no gradients.
- Forecast encoding everywhere: bear `#d03b3b` · base `#2a78d6` · bull `#008300`.
- Chrome: scroll progress bar, sticky scrollspy nav (`01–06 + Takeaway`), back-to-top, reveal-on-scroll.
- Interactive JS modules (all vanilla, IDs unique per file): segmented money donut (`#seg/#donut/#leg/#donutnote` + `#groupedMini`), 5-pill trend tabs (`#trendTabs/#tp*`), twin hover forecast charts (`[data-fc="price"|"mcap"]` with `.fc-chip` toggles, guide + tooltip), peer `.bar-row` fills with `.hairline-grid`.

## Content rules (all versions)

- **Filings-only + AlphaSpread**: every figure traced (AR FY25, BSE filings, `screener.in`, peer 10-K/AR/NOR) **and valuation pulled live from AlphaSpread** (https://www.alphaspread.com/security/nse/<ticker>/dcf-valuation/base-case + /relative-valuation + /summary — DCF Value, Multiples-Based Value, Intrinsic Value, Buy Zone 20% MOS; DCF params follow AlphaSpread's template for that company — Bank template for SFBs/banks e.g. Ujjivan 7yr, 10%, 1.8x P/S; Net Income template for hospitals/industrials e.g. Max 15yr, 10.5%, 36.4x P/E). Peer % = share of one listed peer-group pot, never a TAM claim.
- Forecast discipline is **Revenue → PAT margin → EPS → P/E → Price → MCap** (bank path does not apply). Anchor ₹764 / ₹23,864 Cr / ~31.24 Cr shares; outcomes Bear ₹444 (−10.3%) · Base ₹1,315 (+11.5%) · Bull ₹2,407 (+25.8%) — keep identical unless the user supplies new data. **Valuation section uses live AlphaSpread DCF + Multiples → Intrinsic as primary, with local model as cross-check** (hospital e.g. DCF Rev 15.2%, Net Margin 16.8%, 15yr, 10.5%, 36.4x → 1,465.53 / Multiples 1,026.34 → Intrinsic 1,474.24; SFB e.g. DCF Rev 14.3%, Net Margin 21.8→19.9%, 7yr Bank, 10%, 1.8x P/S → 120.48 / Multiples 64.69 → Intrinsic 120.48).
- Always mark section 06 **illustrative, not a price target**, and keep the SEBI disclaimer.
- If the user names a different company, keep the structure/tokens and replace only the data (ask for the source figures if they are missing).
- Responsive: KPI/vision/message grids collapse at 900/640px; seg pills scroll; print hides nav/totop.
- SVG correctness: use `style="fill:var(--…)"` / `style="stroke:var(--…)"`, never presentation attributes with `var()`.
- Verify before delivering: zero build markers, `<div>` open/close balanced, exactly one `</body></html>`, headless-Chrome render + no horizontal overflow at 420px.

## Output

Save the new file in `Company_Overview/Final/` **grouped by type + month**
(via script or direct write):

| Chosen version | Folder | File name |
|---|---|---|
| Markdown | `MD-<YYYY-MM>/` | `<Company>-<YYYY-MM-DD>.md` |
| Gemini | `Gemini-<YYYY-MM>/` | `<Company>-<YYYY-MM-DD>.html` |
| Plain | `Plain-<YYYY-MM>/` | `<Company>-<YYYY-MM-DD>.html` |

Every file is `Stock-date` — the folder carries the version. No `forecast` infix anywhere. Reply with the path + one line on what
was built, then **always** go to Step 4.

**Token budget:**
- Path A (preferred): LLM ~1.8K input (schema + filings excerpt) + ~0.8K output (JSON) = **~2.6K** for all 3 versions (2nd/3rd = 0). Was **~35K** per version (113 KB example + 20K HTML generation) → **~91% saving**.
- Path B (legacy): ~28K input (example) + ~20K output per version.

## Step 4 — Follow-up question (always last)

After delivering, ask via the question tool with exactly these three options:

1. **New stock analysis** — start a fresh full overview for a different company (back to Step 1)
2. **<first unchosen version>** — same company, the first version not chosen
3. **<second unchosen version>** — same company, the second version not chosen

Labels are the *remaining two* of MD / Gemini / Plain, in Step-1 order.
Example: picked **Plain** → options are `New stock analysis` / `Markdown` / `Gemini`.
Picked **Markdown** → `New stock analysis` / `Gemini` / `Plain`.

If they pick another version → rebuild the same content in it (re-read that
reference per Step 2) and return to Step 4 with a *fresh* pair of unchosen options.
If they pick new analysis → restart at Step 1.
