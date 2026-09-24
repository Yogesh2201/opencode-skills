---
name: full-overview
description: Build a full company overview in Markdown, Plain HTML, or Gemini HTML. Use when the user asks for a full overview, full stock overview, or one of the three versions (Markdown, Plain, Gemini). Always asks which version first, then generates that file.
---

# Full Overview Report Builder

Builds a full company/stock overview in one of three versions.
Reference outputs live in `Full-overview/` (project root):

- `IRCTC_Sep_3_2026_Plain.html` — the Plain HTML reference
- `IRCTC_Sep_3_2026_Gemini.html` — the Gemini HTML reference

Example copies of all three versions live in this skill's `examples/` folder —
`example.md`, `example-plain.html`, `example-gemini.html`. Match them exactly
in structure, tokens, and sections; only the company data changes.

## Step 1 — Ask the version (always first)

Ask via the question tool with exactly these options before doing anything else:

1. **Markdown** — Generate the content in an MD file (KPIs, all 5 sections, figures, takeaway, sources)
2. **Plain** — Generate the Plain HTML version file layout output (same as the Plain reference)
3. **Gemini** — Generate the Gemini HTML version (same as the Gemini reference)

Only after the user picks, continue. Never assume a version.

## Step 2 — Read the reference

- Markdown → no reference file needed; use the Content rules + MD structure below.
- Plain → read `Full-overview/IRCTC_Sep_3_2026_Plain.html` fully (structure, tokens, all 5 sections, JS).
- Gemini → read `Full-overview/IRCTC_Sep_3_2026_Gemini.html` fully.

## Step 3 — Build rules per version

### Markdown (content in an MD file)

- Structure: title + meta (tickers, exchange, sources) → Core idea → KPI table → 01 What they do (+ money proxies) → 02 Peers + moat table → 03 Key verticals → 04 Valuation + DCF (multiples table, DCF build, blended IV, buy zone) → 05 Trends, big messages, red flags, bottom-line lenses → One-line takeaway → Figure sources.
- Tables for KPIs, vertical splits, peers (Peer/Geography/Revenue/Share/Overlap), valuation, DCF, red flags.
- Save to `Full-overview/<Company>-<YYYY-MM-DD>.md`.

### Plain (reproduce the Plain reference)

- Tokens: `--page #f9f9f7, --surface #fcfcfb, --accent #2a78d6, --accent-deep #1c5cab, --context #898781, --orange #eb6834` (hinge: subject row + conviction gauge + closing rule), `--grid #e1e0d9`, hairline `rgba(11,11,11,0.10)`.
- System font stack. No icon fonts, no gradients.
- Chrome: scroll progress bar, sticky scrollspy nav (`01–05 + Takeaway`), back-to-top, reveal-on-scroll.
- Sections: lede → KPI row (5 tiles, first is hero) → 01 What they do (3 mini-cards, quote, value-flow, money panel with donut) → 02 Peers + moat (bars + details table + 2 mini-panels) → 03 Verticals (6 + 3 cards, take-rate spectrum, financial snapshot) → 04 Valuation + DCF (quote, multiples table, 4 DCF tiles, DCF table, methodology quote, valuation-bar meter) → 05 Trends (risk cards + trend panel + big messages + conviction meter + red-flags table + watch grid + six lenses) → accessibility table → takeaway → footer.
- JS modules: segmented money donut (`seg/donut/leg/donutnote` + `groupedMini`), progress/scrollspy/reveal/totop.

### Gemini (reproduce the Gemini reference)

- Tokens: `--bg #fbfbfd, --surface #ffffff, --surface-2 #f0f4f9, --surface-3 #e9eef6, --chart-blue #4285F4, --chart-blue-deep #1967d2, --chart-context #b3b5be, --sweep-3 #9B72CB, --warn #b06000`. Blue = subject, gray = context.
- Outfit + Material Symbols Rounded via Google Fonts. Gradient appears exactly 3×: sparkle mark, H1, hero-tile ring. Animated orb field (48s cycle, honors `prefers-reduced-motion`, `data-aurora="flat"` kills it).
- Same 5 sections + money panel + tabbed Key Trends (5 pills, 1 panel, Prev/Next, `n/5` counter, arrow-key nav) + big messages + red flags + six lenses + takeaway + gradient control panel (FAB).
- Money + trend JS as in reference.

## Content rules (all versions)

- Filings-only: every figure traced to its source; peer % = share of one listed peer-group pot, never a TAM claim.
- Keep all figures, quotes, and the takeaway identical to the reference unless the user supplies new data.
- Responsive: KPI/product/message/watch grids collapse on mobile; seg pills scroll horizontally; print hides nav/FAB/tabs.
- SVG correctness: never use `fill="var(--…)"` / `stroke="var(--…)"` presentation attributes — always `style="fill:var(--…)"` / `style="stroke:var(--…)"`.
- IDs (`seg, donut, leg, donutnote, groupedMini, tp*`) must be unique per file.

## Output

- Markdown → `Full-overview/<Company>-<YYYY-MM-DD>.md`.
- Plain / Gemini → `Full-overview/<Company>-<Plain|Gemini>-<YYYY-MM-DD>.html` (single file, CSS/JS inlined).
- Reply with the file path + what was built, then go to Step 4.

## Step 4 — Follow-up question (always last)

After delivering the file, ask via the question tool with exactly these options:

1. **New stock analysis** — Start a fresh full overview for a different company (back to Step 1)
2. **<First unchosen format>** — Regenerate the same company in the first format not chosen
3. **<Second unchosen format>** — Regenerate the same company in the second format not chosen

Example: if the user picked Plain, the options are New stock analysis / Markdown / Gemini.
If they pick another format, rebuild the same content in that format (re-read its
reference per Step 2) and return to Step 4. If they pick new analysis, restart at Step 1.
