---
name: company-overview
description: Build a TD Power Systems-style company overview in MD, Plain HTML, or Gemini HTML. Use when the user asks for a company overview, company profile, or one of the three versions (MD, Plain, Gemini). Always asks which version first, then generates that file.
---

# Company Overview Report Builder

Builds a company profile in one of three versions.
Reference outputs live in `Company_Overview/` (project root):

- `Plain.html` — the Plain HTML reference (Layout02)
- `TDPS_Gemini-v2-better.html` — the Gemini HTML reference

Example copies of all three versions live in this skill's `examples/` folder —
`example.md`, `example-plain.html`, `example-gemini.html`. Match them exactly
in structure, tokens, and sections; only the company data changes.

## Step 1 — Ask the version (always first)

Ask via the question tool with exactly these options before doing anything else:

1. **MD** — Generate the content in an MD file (KPIs, all 5 sections, figures, takeaway, sources)
2. **Plain** — Generate the Plain HTML version file layout output (same as Plain.html)
3. **Gemini** — Generate the Gemini HTML version (same as the Gemini file)

Only after the user picks, continue. Never assume a version.

## Step 2 — Read the reference

- MD → no reference file needed; use the Content rules + MD structure below.
- Plain → read `Company_Overview/Plain.html` fully (structure, tokens, all 5 sections, JS).
- Gemini → read `Company_Overview/TDPS_Gemini-v2-better.html` fully.

## Step 3 — Build rules per version

### MD (content in an MD file)

- Structure: title + meta (tickers, plant, sources) → Core idea → KPI table → 01 What they do (+ money proxies) → 02 Competitors table → 03 Key products → 04 Vision (verbatim quote + pillars) → 05 Trends & big messages (+ guidance ratchet + roadmap figures) → One-line takeaway → Figure sources.
- Tables for KPIs, money proxies, peers (Peer/HQ/Revenue/Share/Overlap).
- Save to `Company_Overview/<Company>-Company-Overview-<YYYY-MM-DD>.md`.

### Plain (reproduce Plain.html)

- Tokens: `--page #f9f9f7, --surface #fcfcfb, --accent #2a78d6, --accent-deep #1c5cab, --context #898781, --orange #eb6834` (hinge, max 2 uses: export gauge + closing rule), `--grid #e1e0d9`, hairline `rgba(11,11,11,0.10)`.
- System font stack. No icon fonts, no emojis, no gradients.
- Chrome: scroll progress bar, sticky scrollspy nav (`01–05 + Takeaway`), back-to-top, reveal-on-scroll.
- Sections: lede → KPI row (5 tiles, first is hero) → 01 What they do (3 mini-cards, quote, value-flow, money panel) → 02 Competitors (bars + details table + 2 mini-panels) → 03 Products (6 + 3 cards, MVA spectrum, mix bar) → 04 Vision (quote + 4 pillars) → 05 Trends (4 risk cards + trend-5 panel + guidance chart + roadmap + big-picture chain + watch grid + 3 messages + conviction meter) → accessibility table → takeaway → footer.
- JS modules: segmented money donut (`seg/donut/leg/donutnote` + `groupedMini` + pivot bars), guidance ratchet (`guidMini`), roadmap (`roadmapMini`), progress/scrollspy/reveal/totop.

### Gemini (reproduce TDPS_Gemini-v2-better.html)

- Tokens: `--bg #fbfbfd, --surface #ffffff, --surface-2 #f0f4f9, --surface-3 #e9eef6, --chart-blue #4285F4, --chart-blue-deep #1967d2, --chart-context #b3b5be, --sweep-3 #9B72CB, --warn #b06000`. Blue = subject, gray = context.
- Outfit + Material Symbols Rounded via Google Fonts. Gradient appears exactly 3×: sparkle mark, H1, hero-tile ring. Animated orb field (48s cycle, honors `prefers-reduced-motion`, `data-aurora="flat"` kills it).
- Same 5 sections + money panel + tabbed Key Trends (5 pills, 1 panel, Prev/Next, `n/5` counter, arrow-key nav) + takeaway + gradient control panel (FAB).
- KPI row includes the 5th Order-book tile. Money + trend JS as in reference.

## Content rules (all versions)

- Filings-only: every figure traced to its source; peer % = share of one listed peer-group pot, never a TAM claim.
- Keep all figures, quotes, and the takeaway identical to the reference unless the user supplies new data.
- Responsive: KPI/product/vision/message/watch grids collapse (4→2→1, 3→2→1); seg pills scroll horizontally on mobile; print hides nav/FAB/tabs.
- SVG correctness: never use `fill="var(--…)"` / `stroke="var(--…)"` presentation attributes — always `style="fill:var(--…)"` / `style="stroke:var(--…)"`.
- IDs (`seg, donut, leg, donutnote, groupedMini, guidMini, roadmapMini, tp*`) must be unique per file.

## Output

- MD → `Company_Overview/<Company>-Company-Overview-<YYYY-MM-DD>.md`.
- Plain / Gemini → `Company_Overview/<Company>-<Plain|Gemini>-<YYYY-MM-DD>.html` (single file, CSS/JS inlined).
- Reply with the file path + what was built, then go to Step 4.

## Step 4 — Follow-up question (always last)

After delivering the file, ask via the question tool with exactly these options:

1. **New stock analysis** — Start a fresh company overview for a different company (back to Step 1)
2. **<First unchosen format>** — Regenerate the same company in the first format not chosen (MD / Plain / Gemini)
3. **<Second unchosen format>** — Regenerate the same company in the second format not chosen

Example: if the user picked Plain, the options are New stock analysis / MD / Gemini.
If they pick another format, rebuild the same content in that format (re-read its
reference per Step 2) and return to Step 4. If they pick new analysis, restart at Step 1.
