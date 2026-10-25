# Build + verify checklist

## Before writing

- [ ] No version question — this skill is Markdown-only (never offer Gemini / Plain)
- [ ] `examples/demo-01.md` + `assets/moat-scorecard.md` read before writing
- [ ] Output path decided: `MD-Full-Overview/<YYYY-MM>/<Stock>-<YYYY-MM-DD>.md` (never `Company_Overview/Final/`)
- [ ] New company? user-supplied figures gathered — else use the reference data verbatim

## While writing (MD plain — no color layer)

- [ ] No `<style>` block, no `<span`, no pills, no band markup anywhere in the file
- [ ] Hero figures plain `**bold**` · emoji Read/Severity cells (`🔴`/`🟡`/`🟢`) · plain `>` quality-watch quote in Section 5
- [ ] Headings run `## 1.` … `## 11.` then `## Bottom Line` — moat 7 · valuation 8 · risks 9 · scenarios 10 · watch 11
- [ ] Section 7 **Moat Scorecard**: 10 rows in fixed order, weights sum to 100, one evidence line per row, weighted (never simple) total to one decimal + band + `Up:`/`Down:` + `> **Moat verdict:**`
- [ ] Valuation ASCII bar (BUY/DCF/IV/LOW/CURRENT/HIGH + fill %) in Section 8 · flags summary code block in Section 9
- [ ] One-line takeaway (`> **One line:**`) + Sources + SEBI disclaimer footer; no `### Palette`, no rendered-color line

## HTML checks (legacy — this skill is Markdown-only; ignore unless asked for HTML)

- [ ] HTML files above ~50 KB are built in parts with a `<!--PART_B-->` marker (write → edit chain)
- [ ] Single file: CSS and JS inlined, no external assets except Google Fonts (Gemini only)
- [ ] IDs unique per file: `seg, donut, leg, donutnote, groupedMini, tp*, progress, totop, s01–s06, s04v, s09, hdrFcToggle, hfc-chip` — nav now `01–04 + 04 Valuation (s04v) + 05 + 06 + Takeaway` + header `06 FC` toggle pill
- [ ] Section 03 contains **Financial snapshot & quality read** table (MCap/Revenue/NP/Op Profit+FCF/Net Cash + warning) after MVA spectrum
- [ ] Section 04b **Valuation + DCF** (`h2#s04v`) exists: 4-row multiples + 4 tiles (DCF 812 / Fwd 637 / EV 694 → Blended 714 → Buy 571) + blended table + `val-visual` bar
- [ ] Section 05 contains **Red flags — 2 HIGH · 3 MEDIUM** (5-row table + `.flag-grid` + `2 HIGH · 3 MEDIUM · 0 LOW`) + **Bottom line — six lenses** (`msg-grid` 6×) after Big messages
- [ ] SVG uses `style="fill:var(--…)"`, never presentation-attribute `var()`
- [ ] Emoji/flags: Windows does not render flag emoji — use styled `<span class="cc">US</span>` country codes instead

## After writing — HTML render checks (legacy; MD verification lives in SKILL.md)

```powershell
# 1. no leftover build markers, balanced tags, single close
$raw = Get-Content -LiteralPath $f -Raw -Encoding UTF8
[regex]::Matches($raw,'PART_|JS_[A-Z]').Count      # must be 0
[regex]::Matches($raw,'<div\b').Count == [regex]::Matches($raw,'</div>').Count
[regex]::Matches($raw,'</body>').Count             # 1 (HTML)

# 2. render + boot check (Chrome headless)
chrome --headless=new --disable-gpu --no-sandbox --virtual-time-budget=5000 --dump-dom $url
```

- [ ] `dump-dom` shows the JS actually ran (donut SVG / trend title / `fc-line` paths + `val-visual`/`flag-grid` + `hdrFcToggle hfc-chip` present, `data-off` sync works header ↔ panel)
- [ ] Screenshot at 1280px: nav not clipped, KPI values on one line, tables aligned
- [ ] No horizontal overflow at 420px (`document.documentElement.scrollWidth <= window.innerWidth`)
- [ ] Print + `prefers-reduced-motion` rules present

## Reply format

1. File path (one line)
2. What was built (one line)
3. **Always** end with the Step 3 question (two options only): New stock analysis / Done — no HTML handoff
