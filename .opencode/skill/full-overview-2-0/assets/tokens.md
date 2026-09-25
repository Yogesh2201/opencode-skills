# Tokens & palette (per version)

## Plain (interactive render)

```css
--page:#f9f9f7; --surface:#fcfcfb; --surface-2:#f1efe9;
--ink:#1a1a1a; --ink-2:#3d3d3d; --muted:#898781;
--accent:#2a78d6; --accent-deep:#1c5cab;
--orange:#eb6834; --crit:#d03b3b; --good:#008300;
--hairline:rgba(11,11,11,.10); --grid:#e1e0d9;
--radius:14px;
```

- **Two-hue rule:** blue `#2a78d6` = TDPS · warm gray `#898781` = context.
- **Orange `#eb6834` = the one hinge** — TDPS subject bar + takeaway closing rule only. Never decorate with it.
- Forecast encoding: bear `#d03b3b` · base `#2a78d6` · bull `#008300`.
- System font stack. No icon fonts, no gradients, no orb fields.
- Chrome: 3px progress bar, sticky scrollspy nav, back-to-top, reveal-on-scroll.

## Gemini (source)

```css
--bg:#fbfbfd; --surface:#ffffff; --surface-2:#f0f4f9; --surface-3:#e9eef6;
--ink:#1f1f1f; --ink-2:#444746; --ink-3:#8f909c; --ink-inv:#ffffff;
--line:#e3e3e3; --line-strong:#c5c7c9;
--ok:#1e8e3e; --warn:#b06000; --bad:#d93025;
--gemini-sweep: linear-gradient(90deg,#4285F4 0%,#5961F0 25%,#9B72CB 50%,#D96570 75%,#FFA756 100%);
--chart-blue:#4285F4; --chart-blue-deep:#1967d2; --chart-then:#a8c7fa; --chart-context:#b3b5be;
--r-sm:12px; --r-md:16px; --r-lg:24px; --r-pill:999px;
--font:"Google Sans","Outfit","Segoe UI Variable",system-ui,sans-serif;
--ease:cubic-bezier(.2,0,0,1); --drift-period:36s; --cycle-period:48s; --blur:40px;
```

- Fonts: **Outfit** + **Material Symbols Rounded** via Google Fonts; icons are `<span class="material-symbols-rounded">`, never emoji.
- Sweep budget **max 3**: sparkle mark · gradient H1 · hero-tile ring.
- Orb field: 48s cycle, `data-aurora="flat"` and `prefers-reduced-motion` disable it.
- Themes: `:root[data-t="green-white"|"green"|"sunrise"|"dusk"|"none"]`.

## Markdown

No tokens — hierarchy comes from `#`/`##`/`###`, tables, `>` blockquotes, fenced ASCII bars.
Palette only appears in the footer's **Palette** paragraph (hexes listed as inline `code`).

## New components (added Sep 26, 2026 — same in both HTML versions)

### 03 Financial snapshot (inside Key products card)

```html
<h3>Financial snapshot & quality read</h3>
<div class="sub">TTM to Sep 18, 2026 — growth vs premium: Revenue +54% TTM on 18% OPM.</div>
<table><!-- 5 rows: MCap 100% · Revenue 8.9% (11.24× P/S) · NP 1.15% (EPS ~8.8) · Op Profit ₹383 / FCF ~₹192 · Net Cash +₹612 (D/E 0.02) --></table>
<div class="quote warning/q[style*=warn]">68% → 93% export, 18% OPM must hold — project FCF choppy</div>
```

### 04 Valuation + DCF (`#s04v`)

```html
<h2 id="s04v"><span class="num">04</span> Valuation + DCF</h2>
<!-- multiples 4 rows: Trailing 86.8× / Forward ~78× / EV/EBITDA 60.7× / OPM 18% -->
<!-- 4 tiles: DCF ₹812 (WACC 10.5% g6%) / Fwd ₹637 (65× PPS) / EV ₹694 (55× EBITDA) → Blended ₹714 → Buy ₹571 (20% MOS) -->
<!-- blended approach table + methodology quote -->
<!-- val-visual: bar-track (58%) + bar-marks LOW 350 / IV 714 / DCF 812 -->
```

Plain: `val-visual { background:var(--page); border:1px solid var(--hairline); border-radius:12px; padding:16px; } .bar-track { height:10px; background:var(--surface); border:1px solid var(--hairline); border-radius:999px; } .bar-fill { background:linear-gradient(90deg,var(--accent),var(--orange)); }`
Gemini: `val-visual { background:var(--surface-2); } .bar-fill { background:linear-gradient(90deg,#4285F4,#9B72CB); }`

### 05 Red flags + Bottom line (inside Trends card)

```html
<h3>Red flags — 2 HIGH · 3 MEDIUM</h3>
<table><!-- 5 rows: Export concentration HIGH / Valuation premium HIGH / Order lumpiness MED / Margin execution MED / Working capital MED --></table>
<div class="flag-grid"><!-- 5× flag: EXPORT CONCEN / VALUAT PREMIUM / ORDER LUMPY / MARGIN EXECUTN / WORK CAP — sev.high/med --></div>
<div>2 HIGH · 3 MEDIUM · 0 LOW</div>
<!-- Bottom line — six lenses: msg-grid 6× Core idea / What changed / Hidden insight / What breaks / Open question / Takeaway -->
```

Flags: Plain `flag { background:var(--page); border:1px solid var(--hairline); } .sev.high { background:rgba(208,59,59,.10); border:1px solid rgba(208,59,59,.35); }`
Gemini `flag { background:var(--surface-2); } .sev.high { background:#fef2f2; border:1px solid #fecaca; }`

### Header 06 FC toggle (`#hdrFcToggle`)

Sticky top nav far right: pill `06 FC | Bear · Base · Bull` (`#hdrFcToggle` containing 3 `button.hfc-chip[data-hfc]`).
Plain: `background:var(--page); border:1px solid var(--hairline); border-radius:999px;`
Gemini: `background:var(--surface-2); border:1px solid var(--line);`

```css
.hfc-chip[aria-pressed="false"] { background:var(--surface) !important; color:var(--muted)/var(--ink-3) !important; }
```
JS: header `hfc-chip` ↔ `[data-fc] .fc-chip` bidirectionally syncs `panel[data-off]` (global filter). Click scrolls to `#s06` if out of view.

## SVG rule (both HTML versions)

Use `style="fill:var(--…)"` / `style="stroke:var(--…)"`. Never `fill="var(--…)"` as a
presentation attribute — it does not resolve and renders black/none.
