# Build + verify checklist

## Before writing

- [ ] Version chosen via the Step 1 question (never assumed)
- [ ] The matching `examples/` reference read (Gemini / Plain / Markdown)
- [ ] Output path decided: `Company_Overview/Final/<Company>[_Gemini|_Plain]-forecast-<YYYY-MM-DD>.<ext>`
- [ ] New company? user-supplied figures gathered — else use the reference data verbatim

## While writing

- [ ] HTML files above ~50 KB are built in parts with a `<!--PART_B-->` marker (write → edit chain)
- [ ] Single file: CSS and JS inlined, no external assets except Google Fonts (Gemini only)
- [ ] IDs unique per file: `seg, donut, leg, donutnote, groupedMini, tp*, progress, totop, s01–s06, s09`
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

- [ ] `dump-dom` shows the JS actually ran (donut SVG / trend title / `fc-line` paths present)
- [ ] Screenshot at 1280px: nav not clipped, KPI values on one line, tables aligned
- [ ] No horizontal overflow at 420px (`document.documentElement.scrollWidth <= window.innerWidth`)
- [ ] Print + `prefers-reduced-motion` rules present

## Reply format

1. File path (one line)
2. What was built (one line)
3. **Always** end with the Step 4 question: New stock analysis + the two unchosen versions
