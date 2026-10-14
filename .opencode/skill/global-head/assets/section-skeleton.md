# Section skeleton — global briefing (identical order in both variants)

Copy this order exactly. Only the data (stories, window, figures) changes.

## Page order

1. **Header** — H1 `# Global Briefing — <D Mon YYYY> (<HH:MM UTC>)`  
   → one-line italic/metadata: coverage window + equities status + ranked count  
   → `<style>` block (variant chosen)  
   → `>` blockquote: ranking rule + confidence legend (pills)
2. **Stories 01–N** — each `## 0N — <Headline>` with five `###` subsections:
   - `### What happened` (bullets, bold lead names)
   - `### Why this matters` (2–3 paragraphs, analysis)
   - `### Market impact` (bullets: Oil · Equities · Bonds · Currency · Sector winners/losers)
   - `### What to watch next` (numbered list, 5 items)
   - `### Confidence level` (pill(s) + source note)
   - `---` divider
3. **Notable but below the top N** — `## Notable but below the top 10`  
   (bulleted; bold region/owner tag + em-dash + one or two sentences)
4. **Top 3 stories by global impact** — `## Top 3 stories by global impact`  
   (numbered list; bold headline + em-dash + why it ranks)
5. **Caution line** — italic one-liner (`*One line of caution: …*`)
6. **Macro dashboard** — `## Macro dashboard`  
   (table `| Indicator | Signal |`, six fixed rows — see below)
7. **One-chart view** — `## One-chart view`  
   (bold chart title · *Why this one.* · numbered bullets · secondary reference)
8. **30-second executive brief** — `## 30-second executive brief`  
   (bulleted, 8 items, each leading with a bolded lead)
9. Footer divider + (optional) `### Sources` + SEBI/educational disclaimer line if finance-adjacent.

## Macro dashboard rows (fixed, in this order)

1. Global risk sentiment
2. Oil direction
3. Inflation pressure
4. Growth outlook
5. Geopolitical risk
6. AI/tech sentiment

## Confidence pills

- Blue-black variant uses `.pill.pass` (verified), `.pill.warn` (facts solid, trajectory unresolved), `.pill.risk` (single-sourced/contested), `.pill.na`.
- Black/blue/orange variant uses `.pill.high` / `.pill.med` / `.pill.low`.
- Use **two pills on one line** when facts and trajectory differ (e.g. "High on the facts … Medium on the trajectory …").

## IDs / headers

- Story headers: `## 01 — <Headline>` … `## 10 — <Headline>` (zero-padded, em dash).
- Subsections are `### What happened`, `### Why this matters`, `### Market impact`, `### What to watch next`, `### Confidence level`.
- All section headings use `##` for top-level, `###` for subsections. No `####`.

## Fixed copy blocks (do not paraphrase)

- Ranking line: `> **Ranked by global importance, market impact, and cross-border reach — not by news volume.** Facts are separated from analysis in every entry. Ranking logic: <one short sentence>. **Confidence pills** on every story: <legend>`.
- Confidence legend (blue-black): `<span class=\"pill pass\">✓ HIGH</span> facts verified by multiple wires … <span class=\"pill warn\">◐ MED</span> facts solid, trajectory unresolved … <span class=\"pill risk\">● LOW</span> single-sourced or officially unconfirmed.`
- Disclaimer (optional footer): `*Educational only — a synthesis of public reporting, not investment or policy advice.*`

## MD-only / style rules (from MD-Color-Palette.md)

- No fills, no backgrounds — `background: transparent` everywhere.
- Blue carries "heading/value", ink carries body; never use green/red semantics.
- Weight ladder: 400 body → 600 emphasis (`strong`, `.gold`, `.red`, `.pill`) → 650 value (`.v`) → 700 headings. No 700/800 in body.
- H1: 3px blue underline; H2: 1px hairline underline; H3/H4: no rules.
- Tables: `th` uppercase blue 0.78em, `td` ink 0.92em.
- `.v` for roughly 5–10 figures per section — not every number.
- Pick one variant's `<style>` block and embed it verbatim (drop-in from `assets/`).
- Numbers as reported (≈ for intraday); cite source date where it matters.

## Output path

`Global-Headlines/<YYYY-MM>/Global-Briefing-<YYYY-MM-DD>.md`  
Variants: append `-blueblack` to the filename for the two-hue version (matches existing house convention).

## Markdown build rules

- Exact section order above — never skip Macro dashboard or 30-second brief.
- Each story has all five subsections in order.
- Market impact always has the five bullets (Oil, Equities, Bonds, Currency, Sector).
- Numbered "What to watch next" lists run 1–5.
- Top-3 list runs 1–3 with bolded headline + "—" + why-it-ranks.
- Confidence line at the very end of each story's Confidence subsection.
- Use `---` between stories and between major sections, exactly as in the reference.
- Emoji are avoided; UTF-8 figures (≈, —, ·, %) as literal text.