# Build + verify checklist — global-head

## Before writing

- [ ] Variant chosen via the Step 1 question (blue-black default; black/blue/orange optional) — never assumed.
- [ ] Coverage window decided (start/end UTC + equities status note).
- [ ] The matching `examples/` reference read (blue-black or orange).
- [ ] Story count decided (default 10); every fact sourced from ≥2 wires where possible.
- [ ] Output path decided: `Global-Headlines/<YYYY-MM>/Global-Briefing-<YYYY-MM-DD>[-blueblack].md`.

## While writing

- [ ] The chosen variant's `<style>` block (from `assets/style-block-*.md`) embedded verbatim at the top.
- [ ] H1 includes date + UTC time; metadata line names the window + equities status + story count.
- [ ] Ranking blockquote + confidence legend present immediately after the style block.
- [ ] Stories `## 01` … `## N` each with all five subsections in order.
- [ ] Market impact bullets always include Oil · Equities · Bonds · Currency · Sector winners/losers.
- [ ] "What to watch next" numbered 1–5.
- [ ] Notable section present (bold tag + em dash + 1–2 sentences).
- [ ] Top 3 section present (1–3 with bold headline + em dash + why).
- [ ] Italic caution line present.
- [ ] Macro dashboard table present with all six fixed rows in order.
- [ ] One-chart view present (title + *Why this one.* + numbered bullets + secondary reference).
- [ ] 30-second executive brief present (8 bullets, bolded leads).
- [ ] No fills/backgrounds invented; blue-black variant never uses orange.
- [ ] No `<span class="pill …">` invented outside the two variant taxonomies.

## After writing (run these)

```powershell
$f = "Global-Headlines\<YYYY-MM>\Global-Briefing-<YYYY-MM-DD>[-blueblack].md"
$raw = Get-Content -LiteralPath $f -Raw -Encoding UTF8
[regex]::Matches($raw, 'PART_|JS_[A-Z]').Count        # 0
[regex]::Matches($raw, '<style>').Count                # 1
[regex]::Matches($raw, '## Macro dashboard').Count     # 1
[regex]::Matches($raw, '## 30-second executive brief').Count  # 1
```

- [ ] All five subsection names appear exactly once per story (counts match N × 5).
- [ ] Macro dashboard has exactly the six fixed indicator rows.
- [ ] 30-second brief has exactly 8 bullets.
- [ ] Read-through: numbers cited with sources/dates; no invented quotes.
- [ ] Pills reflect verification status; nothing tagged `pass`/`high` without 2+ wires.

## Reply format

1. File path (one line)
2. What was built (one line — window, story count, variant)
3. **Always** end with the follow-up question: **New briefing** / **Done** — no HTML handoff.