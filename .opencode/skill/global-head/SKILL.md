# Skill: global-head

Build a **Global Briefing** — a ranked, sourced, Markdown-overview of the world's
most consequential developments in a coverage window — and loop into the next
request. Reference files live in **this skill's own folders** (verbatim copies
from `Global-Headlines/`). Markdown-only: one portable `.md` file with an
embedded `<style>` block. No HTML handoff.

| Folder | File | Purpose |
|---|---|---|
| `examples/` | `Global-Briefing-2026-09-30-blueblack.md` | **Canonical reference** — two-hue house style (default variant) |
| `examples/` | `Global-Briefing-2026-09-30.md` | Black/blue/orange variant (confidence-coloured pills) |
| `assets/` | `section-skeleton.md` | Fixed section order, per-story subsections, macro rows |
| `assets/` | `style-block-blueblack.md` | Drop-in `<style>` (blue + ink, text-colour only) |
| `assets/` | `style-block-orange.md` | Drop-in `<style>` (black / blue / orange) |
| `assets/` | `MD-Color-Palette.md` | Palette + weight ladder + usage rules (blue-black) |
| `assets/` | `verify-checklist.md` | Build + verification steps, reply format |
| `data/` | `schema.json` | JSON Schema for `data/<YYYY-MM-DD>.json` (optional) |

Do **not** use any other briefing/report as a template. The two example files
alone supply structure, section order, and per-story subsections; only the
data changes per request.

---

## Step 1 — Choose variant and window (before any research or writing)

Ask via the question tool:

1. **Variant** — two options:
   - `Blue-black (default)` — text-colour only, two hues (blue = heading/value, ink = body). Uses `.pill.pass/.warn/.risk/.na`.
   - `Black/Blue/Orange` — adds orange for unresolved risk. Uses `.pill.high/.med/.low`.
2. **Coverage window** — start/end (UTC) and whether US equities are mid-session (mark intraday figures).
3. **Story count** — default 10; allowed 8–12.
4. **Optional emphasis** — region/topic tilt (e.g. AI, macro, geopolitics), or none.

Record these as `meta` values.

## Step 2 — Research (high-trust only)

Gather facts for each ranked story from **primary/high-trust sources only**:
- Wires: Reuters, AP, Bloomberg, AFP; official statements (Pentagon, White House, central banks, ministries, company filings).
- Every figure must be traceable to a source + date. If a figure is single-sourced or contested, tag its pill accordingly.
- Verify each fact across **≥2 wires** where possible; conflicts must be noted, not averaged.
- Mark intraday prices with `~` and the session date.

Rank by **global importance × market impact × cross-border reach**, not by news
volume. The war/Hormuz complex anchors the top; the Fed path is the second
transmission channel; items 4–N are the highest-consequence discrete events.

For each story capture (per `data/schema.json`):
- `what_happened` — factual bullets, bold lead names.
- `why_matters` — 2–3 paragraphs of analysis (facts ≠ analysis; separate them).
- `market_impact` — five lines: Oil, Equities, Bonds, Currency, Sector winners/losers
  (use "None" where truly absent).
- `watch_next` — exactly 5 numbered forward items.
- `confidence_facts` / `confidence_traj` — high | med | low (+ a one-line note).

Also gather: `notable[]` (below-top items, bold tag + em dash + 1–2 sentences),
`top3[]` (ranked headline + "why"), `caution_line` (italic one-liner that ties
the top items together), `macro_dashboard[]` (the six fixed indicators with a Signal
cell each), `chart` (title, why, numbered bullets, secondary reference), and
`thirty_second_brief[]` (exactly 8 bullets with bolded leads).

**Ask the user for figures if a filing is missing — never invent.**

## Step 3 — Read the reference, then write the file

1. Read `examples/<variant>.md` **fully** — it is the ONLY structural reference.
2. Read `assets/section-skeleton.md`, `assets/verify-checklist.md`, and the chosen
   `assets/style-block-*.md`.
3. Write `Global-Headlines/<YYYY-MM>/Global-Briefing-<YYYY-MM-DD>[-blueblack].md`
   directly. Month folder = render month. Filename includes date only (no `_briefing`
   infix). No build script — hand-rendered from research + reference.

Layout to reproduce (verbatim from the reference):

```
# Global Briefing — <D Mon YYYY> (<HH:MM UTC>)
<metadata line: window + equities status + story count>
<style block — chosen variant, verbatim>
> **Ranked by global importance …** … **Confidence pills** …

## 01 — <Headline>
### What happened
### Why this matters
### Market impact
### What to watch next
### Confidence level
---
  … one block per story …

## Notable but below the top 10
## Top 3 stories by global impact
*One line of caution: …*

## Macro dashboard
| Indicator | Signal |

## One-chart view
**Chart: …**
*Why this one.* …

## 30-second executive brief
```

### Markdown build rules (match the reference)

- Variant's `<style>` block embedded verbatim at the top; no fills/backgrounds.
- H1 = title with date + UTC time; metadata line under it.
- Ranking line + confidence legend as a blockquote immediately after `<style>`.
- Stories `## 01` … `## NN`, zero-padded, em dash; each with the five subsections.
- Market impact always the five bullets (Oil · Equities · Bonds · Currency · Sector).
- "What to watch next" numbered 1–5; "Top 3" numbered 1–3.
- Macro dashboard: exactly the six fixed indicators (Global risk sentiment, Oil direction,
  Inflation pressure, Growth outlook, Geopolitical risk, AI/tech sentiment).
- 30-second brief: exactly 8 bullets with bolded leads.
- Use `---` between stories and between major sections.
- Confidence pills: blue-black → `.pass/.warn/.risk/.na`; orange variant →
  `.high/.med/.low`. Never mix taxonomies; never use orange in the blue-black variant.
- Portable UTF-8 figures (`~`, `—`, `·`, `%`); no green/red semantics.
- Optional `### Sources` + the educational-only disclaimer footer.

## Step 4 — Verify before delivering

Run the checks in `assets/verify-checklist.md`:
- Zero build markers (`PART_`, `JS_`).
- Exactly one `<style>` block; correct pill taxonomy for the chosen variant.
- All `##` sections present in reference order; each story has 5 subsections.
- Macro dashboard has 6 rows; 30-second brief has 8 bullets; watch-next 5 per story.
- No claim without a traceable source.

## Step 5 — Follow-up question (always last)

After delivering, ask via the question tool (two options only — Markdown-only,
no HTML handoff):

1. **New briefing** — fresh Global Briefing for a different window (back to Step 1)
2. **Done** — nothing further for now

If they pick new briefing → restart at Step 1.

## Output

Save the file in `Global-Headlines/<YYYY-MM>/`:

| Output | File name |
|---|---|
| Markdown (blue-black) | `Global-Briefing-<YYYY-MM-DD>-blueblack.md` |
| Markdown (black/blue/orange) | `Global-Briefing-<YYYY-MM-DD>.md` |

Reply with the path + one line on the window/story count/variant, then **always**
go to Step 5.

**Token budget:** ~25–40K for a 10-story build on first run; a saved
`data/<YYYY-MM-DD>.json` makes refresh windows cheap.

## Content rules

- **Filings/wires only.** Every figure traced to a published source + date.
  Peer/region claims are relative comparisons, never TAM claims.
- **Confidence discipline:** `.pass`/`.high` only when verified by **≥2 wires**.
  Single-sourced or contested facts must be `.risk`/`.low`, with the note.
- **No invented data.** If a series is unavailable (SPR level, intraday price),
  mark it `~`/best-estimate and name the source; never fabricate a consensus number.
- **Currency convention:** `$` for USD global markets; `₹` for Indian figures;
  `€` for eurozone; use the source's native unit otherwise. Never mix in one table.
- **Illustrative only.** Keep the educational-only disclaimer if any price/target/
  driver language appears; this is synthesis, not investment advice. Consult a
  SEBI-registered / appropriately licensed advisor before acting.
- If the user names a different window/date, keep the structure and replace only
  the data. If they ask for a version without the market-impact block (pure news),
  drop that subsection but keep the rest of the skeleton. ( Markdown skill; no HTML handoff.)
- Verify before delivering: no `PART_` markers, `<style>` present exactly once,
  all six dashboard rows present, 8-bullet 30-second brief, pill taxonomy matches variant.