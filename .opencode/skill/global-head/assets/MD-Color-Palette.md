# Markdown Colour System — Blue/Black (Reference)

**A reusable style block and token reference for consistent `.md` briefing documents. Extracted from the `*-blueblack.md` house style. Text colour only — no fills, no backgrounds.**

---

## 01 — Core palette (4 tokens + 1 accent)

| Token | Hex | Role | Contrast on white |
|---|---|---|---|
| `--bb-blue` | <code>#0B5FC0</code> | Primary accent — headings, values, rules, table headers | <span class="v">5.9:1</span> ✓ AAA |
| `--bb-blue-deep` | <code>#0A4DA0</code> | Reserved — hover states, deep emphasis (rarely used) | <span class="v">6.9:1</span> ✓ AAA |
| `--bb-ink` | <code>#111418</code> | Body text, bold emphasis, H3 | <span class="v">18.4:1</span> ✓ AAA |
| `--bb-muted` | <code>#5b6470</code> | Secondary text, asides, `.na` pill | <span class="v">6.4:1</span> ✓ AAA |
| `--bb-line` | <code>#d7dde5</code> | Hairline rules, table row borders | <span class="v">non-text</span> |

> **Why these five.** The palette is deliberately two-hue: a single saturated blue for "this is a number or a heading," and a near-black neutral ramp for everything else. Adding a third hue (green/red for up/down) is the usual move — it is deliberately excluded here so that **emphasis stays typographic rather than chromatic**, and so blue always means the same thing on every page.

### Semantic mapping

| Meaning | Token used | Never use |
|---|---|---|
| Heading, section break | `--bb-blue` | any other colour |
| Key figure / value | `--bb-blue` via `.v` | green, red |
| Body prose | `--bb-ink` | `--bb-blue` (overuse kills the signal) |
| Caveat, source line, asides | `--bb-muted` via `.mut` | full ink |
| Structural rule | `--bb-line` | `--bb-blue` (except H1 underline) |

---

## 02 — Weight ladder

Four steps. No 700 or 800 anywhere — heavy weights read as shouting in a document this dense.

| Level | Weight | Applied to |
|---|---|---|
| Body | `400` | default prose, table cells |
| Emphasis | `600` | `strong`, `.gold`, `.red`, `.pill` |
| Value | `650` | `.v` — one step above emphasis, reinforced by blue colour |
| Headings | `700` (browser default) | H1–H4 only |

```
strong, .gold, .red, .pill  →  600
.v                            →  650
h1–h4                         →  700 (default)
```

Letter-spacing tightening on emphasis: `-.005em`. Pills get `+.02em` (they read as labels, not prose).

---

## 03 — Drop-in style block

Paste at the top of any `.md` file. Self-contained, no external dependencies.

<style>
  :root {
    --bb-blue: #0B5FC0; --bb-blue-deep: #0A4DA0;
    --bb-ink: #111418;  --bb-muted: #5b6470; --bb-line: #d7dde5;
  }
  /* text-color only — no fill / no background anywhere */
  body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; color: var(--bb-ink); background: transparent; }
  h1 { color: var(--bb-blue); border-bottom: 3px solid var(--bb-blue); padding-bottom: 6px; }
  h2 { color: var(--bb-blue); border-bottom: 1px solid var(--bb-line); padding-bottom: 4px; margin-top: 30px; }
  h3 { color: var(--bb-ink); }
  h4 { color: var(--bb-blue); }
  blockquote { border-left: 4px solid var(--bb-blue); background: transparent; margin: 10px 0; padding: 10px 14px; color: var(--bb-ink); }
  blockquote.gold { border-left-color: var(--bb-ink); background: transparent; }
  blockquote.red  { border-left-color: var(--bb-ink); background: transparent; color: var(--bb-ink); }
  blockquote.red .red, blockquote.red strong { color: var(--bb-ink); }
  table { border-collapse: collapse; width: 100%; margin: 12px 0; background: transparent; }
  th { background: transparent; color: var(--bb-blue); text-transform: uppercase; font-size: .78em; letter-spacing: .05em; padding: 8px 10px; border-bottom: 2px solid var(--bb-blue); text-align: left; }
  td { padding: 8px 10px; border-bottom: 1px solid var(--bb-line); font-size: .92em; background: transparent; color: var(--bb-ink); }
  /* weight ladder: 400 body → 600 emphasis → 650 value. No 700/800 anywhere. */
  .v    { font-weight: 650; color: var(--bb-blue); background: transparent; letter-spacing: -.005em; }
  .gold { font-weight: 600; color: var(--bb-ink); background: transparent; }
  .red  { font-weight: 600; color: var(--bb-ink); background: transparent; }
  .mut  { color: var(--bb-muted); background: transparent; }
  strong { font-weight: 600; color: var(--bb-ink); letter-spacing: -.005em; }
  .pill { display: inline-block; font-size: .75em; font-weight: 600; letter-spacing: .02em; padding: 2px 9px; border-radius: 99px; background: transparent; border: 1px solid currentColor; }
  .pill.pass { color: var(--bb-blue); }
  .pill.warn { color: var(--bb-ink); }
  .pill.risk { color: var(--bb-ink); }
  .pill.na   { color: var(--bb-muted); }
  .band { background: transparent; color: var(--bb-ink); padding: 16px 20px; border-radius: 10px; margin-top: 26px; border: 1px solid var(--bb-line); border-left: 4px solid var(--bb-blue); }
  .band b { color: var(--bb-blue); }
  code { background: transparent; color: var(--bb-blue); padding: 1px 5px; font-size: .88em; }
</style>

---

## 04 — Component reference

### Type scale

| Element | Size | Weight | Colour |
|---|---|---|---|
| **H1** | default (2em) | 700 | <code>--bb-blue</code> + 3px blue underline |
| **H2** | 1.5em | 700 | <code>--bb-blue</code> + 1px hairline underline |
| **H3** | 1.25em | 700 | <code>--bb-ink</code> — no rule |
| **H4** | 1em | 700 | <code>--bb-blue</code> — no rule |
| **Body** | 1em | 400 | <code>--bb-ink</code> |
| **Table header** | .78em | 700 | <code>--bb-blue</code>, uppercase, `.05em` tracking |
| **Table cell** | .92em | 400 | <code>--bb-ink</code> |
| **Code inline** | .88em | 400 | <code>--bb-blue</code> |

### Text classes

| Class | Result | Use for |
|---|---|---|
| `<span class="v">` | <span class="v">Key figure in blue, 650 weight</span> | Numbers, tickers, dates, the single most important value in a line |
| `<span class="gold">` | <span class="gold">Emphasis, ink, 600 weight</span> | A judgement or verdict inside a paragraph |
| `<span class="red">` | <span class="red">Caution flag, ink, 600 weight</span> | Risk warnings — **ink, not red**, to hold the two-hue rule |
| `<span class="mut">` | <span class="mut">Secondary text, muted</span> | Source lines, asides, de-emphasised data |
| `**text**` | <strong>Standard emphasis</strong> | Ordinary inline bold |

> **The `.gold` / `.red` naming is legacy.** Both render ink-black by design. Kept for compatibility with existing files; new work should use `.gold` for emphasis and `strong` for routine bold, reserving `.red` strictly for risk flags.

### Pills

| Class | Renders as | Meaning |
|---|---|---|
| `.pill.pass` | <span class="pill pass">✓ PASS</span> | Verified across multiple sources, or positive signal |
| `.pill.warn` | <span class="pill warn">◐ MED</span> | Facts solid, trajectory unresolved |
| `.pill.risk` | <span class="pill risk">● LOW</span> | Single-sourced, contested, or unconfirmed |
| `.pill.na` | <span class="pill na">○ N/A</span> | Not applicable / not disclosed |

### Blocks

| Component | Treatment |
|---|---|
| **Blockquote** | 4px blue left border, transparent, ink text |
| **`.band`** | 1px hairline border + 4px blue left edge, 10px radius, 16/20 padding — the "at a glance" callout |
| **Divider** | `---` → default grey rule |

---

## 05 — Usage rules

1. **Blue is reserved.** If everything is blue, nothing is. Apply `.v` to roughly 5–10 figures per section, not every number.
2. **No fills, ever.** Every element is `background: transparent`. This keeps the file portable across light and dark viewer themes and printable.
3. **Never colour a table cell body.** Only `th` is blue. `td` stays ink.
4. **One accent border per block.** A blockquote gets the blue left edge, a band gets blue left edge *plus* hairline — never both at full strength.
5. **Headings get rules, body does not.** H1 gets 3px, H2 gets 1px, H3/H4 get none. Rules on every heading flatten the hierarchy.
6. **No green/red semantics.** Direction and risk are carried by words (`up`, `down`, `winners`, `losers`) and by `.red`, which is ink.
7. **Weight carries emphasis, not size.** Emphasis is 600; do not reach for larger type in body copy.

---

## 06 — Optional variants

Swap the two token lines to reskin an entire document. Structure and weight ladder stay identical.

| Theme | Blue | Ink | Muted | Line | Best for |
|---|---|---|---|---|---|
| **Blue/Black** *(default)* | `#0B5FC0` | `#111418` | `#5b6470` | `#d7dde5` | Company research, briefings |
| **Slate/Ink** | `#3D5A80` | `#161A1D` | `#5f6a75` | `#dce1e7` | Conservative / legal |
| **Teal/Ink** | `#0F766E` | `#101418` | `#5a6660` | `#d5e0dd` | Energy, climate, ESG |
| **Crimson/Ink** | `#B0233C` | `#141417` | `#6a5a60` | `#e0d5d8` | Risk, credit, compliance |
| **Violet/Ink** | `#5B3FA8` | `#131319` | `#625c72` | `#ddd9e8` | Technology, research |

> All five clear **WCAG AA** (most AA-large) for body-adjacent text and **AA** at minimum on H1/H2 against white. Swap only if you re-verify contrast on the specific render surface.

---

*Reference file. Extract the §03 style block into any new `.md` document to inherit the full system.*
