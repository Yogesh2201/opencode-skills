# Build + verify checklist

## Before writing

- [ ] Version chosen via the Step 1 question (never assumed)
- [ ] The matching `examples/` reference read (Gemini / Plain / Markdown)
- [ ] Output path decided: `Company_Overview/Final/<Company>[_Gemini|_Plain]-forecast-<YYYY-MM-DD>.<ext>`
- [ ] New company? user-supplied figures gathered — else use the reference data verbatim

## While writing

- [ ] HTML files above ~50 KB are built in parts with a `<!--PART_B-->` marker (write → edit chain)
- [ ] Single file: CSS and JS inlined, no external assets except Google Fonts (Gemini only)
- [ ] IDs unique per file: `seg, donut, leg, donutnote, groupedMini, tp*, progress, totop, s01–s06, s04v, s09, hdrFcToggle, hfc-chip` — nav now `01–04 + 04 Valuation (s04v) + 05 + 06 + Takeaway` + header `06 FC` toggle pill
- [ ] Section 03 contains **Financial snapshot & quality read** table (MCap/Revenue/NP/Op Profit+FCF/Net Cash + warning) after MVA spectrum
- [ ] Section 04b **Valuation + DCF** (`h2#s04v`) exists: 4-row multiples + 4 tiles (DCF 812 / Fwd 637 / EV 694 → Blended 714 → Buy 571) + blended table + `val-visual` bar
- [ ] Section 05 contains **Red flags — 2 HIGH · 3 MEDIUM** (5-row table + `.flag-grid` + `2 HIGH · 3 MEDIUM · 0 LOW`) + **Bottom line — six lenses** (`msg-grid` 6×) after Big messages
- [ ] SVG uses `style="fill:var(--…)"`, never presentation-attribute `var()`
- [ ] Emoji/flags: Windows does not render flag emoji — use styled `<span class="cc">US</span>` country codes instead

## After writing (run these)

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
3. **Always** end with the Step 4 question: New stock analysis + the two unchosen versions
