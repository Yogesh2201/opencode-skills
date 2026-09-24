---
name: text-summary
description: Compress a long-form text source — article, profile, interview, report, essay, transcript — into a six-section intelligence brief written to a Markdown file. Use when the user pastes a long text and wants it condensed into the *core idea + what changed + the numbers + hidden insight + open question + one-line takeaway* shape. Default output is a `.md` file in the user's `Text-Explanations/` folder at the project root, with a reference copy kept in this skill's `examples/` folder; offer a dark-themed HTML follow-up if the user wants a shareable visual. Do not use for short notes, headlines, code, or anything that already fits on a screen.
---

# Text Summary

> Explain so you understand — don't show off how much you can compress.

A long source becomes a six-section brief that a busy reader can absorb in **under five minutes** and walk away with the actual point, the numbers, the non-obvious insight, and the one line worth remembering.

This is **not** a `simplify-research` job (no evidence tagging, no falsifiers) and **not** a `decode` job (no layered reading speeds, no dashboard). It is a single document, written once, with one shape.

---

## When to use

- A long article, profile, interview, feature, or essay (1,500+ words).
- The user pastes the source and says "summarize this", "break this down", "explain this to me", "what's the point of this", or simply drops a URL/text.
- The output should be **durable** — a file the user can refer back to, not a one-shot chat reply.

When **not** to use: short notes, tweets, press releases under 500 words, code, logs, transcripts of meetings (use `user-research` for that). If the source can be read in 60 seconds, it doesn't need this skill.

---

## The output shape

Exactly **six sections**, in this order. Same emoji + label every time so readers learn the pattern after one file.

```text
🧠 Core idea       One paragraph, plain language. The point of the piece.
🔄 What changed    Before / after, in motion. What shifted, and when.
💰 Why it works    The numbers + mechanism. A table only when comparison earns it.
👀 Hidden insight  1–3 stacked insights — the parts most readers will miss.
⚠️ Open question   What's genuinely unresolved.
🎯 One-line        The line you carry away. Hero treatment.
```

Drop a section only if the source genuinely has nothing for it. **Do not add sections** — the shape is the product.

---

## Voice and style

Conversational, direct, plain words when plain words work; precise words when precision matters.

- *"Here's what's actually going on…"* / *"Watch this part…"* / *"Now here's the twist…"*
- Senior analyst briefing a smart friend. Confident, warm, zero lecturing.
- Walk in order: what happened → why → what people miss → what's next.
- **Show, don't compress-at.** A summary that lists every fact and uses big words isn't a good summary.

### Tools I reach for (when they help)

| Tool | When it earns its place |
|---|---|
| The one-sentence idea | Always — opens every explanation |
| Before / After flow | When something changed (almost always) |
| The numbers | When figures prove the point |
| Small comparison table | When 2+ things differ in a way easier to see than read |
| Hidden insight | When the source has a non-obvious lesson (almost always) |
| Deeper thesis | When the surface story is really about something else |
| Open question | When something is unresolved and the reader should know |
| One-line takeaway | Always — closes every brief |

### I avoid by default

- Dashboards before explanations. A 9-section brief on a 1,500-word article = wrong.
- Jargon as shorthand. "Strategic moat", "synergistic value" — use when the source uses them.
- Hedging into uselessness. "It could be argued that perhaps…" — no.
- Padding to look thorough. Short sources get short briefs.
- Evidence tagging `(fact)/(inference)` everywhere. That's `simplify-research`.
- Layered reading speeds. That's `decode`.

---

## The six sections, in detail

### 🧠 Core idea
- **One paragraph**, 3–5 sentences, plain language.
- Answer: what is this really about?
- The "story isn't really about X — it's about Y" move is welcome here when the surface topic is misleading.

### 🔄 What changed
- **Before** (one short paragraph or bullets) → **After** (one short paragraph or bullets).
- "In motion" means: name the trigger, the timing, the structural shift.
- End with a one-line "**The structural shift:**" sentence that names the deeper movement.

### 💰 Why it works
- The numbers that matter most, presented as a small **comparison table** when 2+ sides differ.
- Pick **one big number** and **one small number** that together explain the story.
- No tables for fewer than 3 comparable numbers — bullets are fine.
- Always end with a sentence that says which number is the load-bearing one.

### 👀 Hidden insight
- **1–3 stacked insights.** Each is something a careful reader would notice but the source writer didn't underline.
- Not in the source explicitly. If it's in the source, it's not hidden.
- Each insight gets its own short paragraph. Quote the source once per insight if a quote carries it.
- This is where the brief earns its keep. Do not phone it in.

### ⚠️ Open question
- A question that genuinely has no answer yet. Not "what's interesting" — what's unresolved.
- One short paragraph. Often two questions: the obvious one, then the harder one underneath.

### 🎯 One-line takeaway
- **One sentence.** The line the reader carries away.
- Purple hero treatment — this is the only place in the brief where the full color weight lands.
- No emoji clutter. The 🎯 is the marker; the sentence is the work.

---

## File format and naming

**Primary deliverable:** Markdown file in the user's `Text-Explanations/` folder at the project root. A reference copy also stays in `.claude/skills/text-summary/examples/` so future invocations can study the shape — the other two examples (SLB, Ackman) live in both places, and that pair is the convention, not a one-off.

```text
Text-Explanations/<slug>-<YYYY-MM-DD>.md         ← canonical, what the user keeps
.claude/skills/text-summary/examples/<slug>-<YYYY-MM-DD>.md  ← reference copy
```

- **slug** = 2–4 lowercase, hyphenated words pulled from the *idea*, not the topic.
  - ✅ `slb-oilfield-services` (the idea: an invisible giant)
  - ✅ `ackman-brain-institute` (the idea: pivoting from markets to medicine)
  - ❌ `oil-company-profile` (the topic, not the idea)
  - ❌ `bill-ackman-fortune` (the name, not the idea)
- **Date** = the date the brief was written, in the user's timezone. Get it with `date +%Y-%m-%d` — do not guess.
- **Prepend the YK palette `<style>` block** so the .md renders with the color hierarchy in any Markdown previewer. Without it, the hero treatment reads as plain text. Standard block:

  ```html
  <style>
    /* Color hierarchy — YK palette (light-bg variants) */
    /* Purple = hero (one moment per page). Blue = workhorse structure. Dark = body. */
    h1, h2, h3 { color: #0B5FC0; border-bottom: 1px solid rgba(11,95,192,0.25); padding-bottom: 6px; }
    h1 { color: #692D9A; border-bottom: 2px solid rgba(105,45,154,0.45); }
    .hero { color: #4A1F7A; font-weight: 700; font-size: 1.15em; background: linear-gradient(90deg, rgba(170,77,230,0.08), transparent); padding: 8px 12px; border-left: 4px solid #692D9A; border-radius: 4px; display: block; margin: 12px 0; }
    .accent { color: #0B5FC0; font-weight: 600; }
    .quote { color: #4A1F7A; font-style: italic; border-left: 3px solid #692D9A; padding: 8px 12px; margin: 12px 0; background: rgba(105,45,154,0.05); }
    table { border-collapse: collapse; width: 100%; }
    th { color: #0B5FC0; border-bottom: 2px solid #0B5FC0; padding: 8px; text-align: left; background: rgba(11,95,192,0.05); }
    td { padding: 8px; border-bottom: 1px solid rgba(11,95,192,0.15); }
    hr { border: none; border-top: 1px solid rgba(11,95,192,0.25); margin: 24px 0; }
    strong { color: #1F1B2E; }
    code { color: #692D9A; background: rgba(105,45,154,0.08); padding: 1px 6px; border-radius: 4px; }
  </style>
  ```

  For dark-background renderings, swap `#0B5FC0` → `#5BA3FF`, `#692D9A` → `#C58CFF`, `#1F1B2E` → `#E8E6F0`, and adjust the rgba alphas upward (~0.35) so accents stay readable on `#0E1116`.

**Optional follow-up:** If the user asks for it ("as HTML", "make it visual", "with charts", "send me a link"), produce a paired `<slug>-<YYYY-MM-DD>.html` using the YK Neon dark theme. Save it to **both** `Text-Explanations/` and the skill's `examples/` folder — the pair (`.md` + `.html` in both places) is the convention. Never both formats in one turn; the .html is its own turn.

**HTML rules:**
- Full `<!DOCTYPE html>` document — standalone, openable in any browser.
- Use the YK Neon CSS variables from the existing examples (`--purple-glow`, `--blue-electric`, etc.) so all three briefs feel like one system.
- Hero takeaway box uses the pulsing `flare` animation — the **only** place the full purple glow lives.
- Reserve the `.quote` (lavender) treatment for one or two pull-quotes that earn it. Skip it entirely if no source quote carries the insight.
- Wrap load-bearing numbers in `<code>` chips so they pop against the body text.

**Color hierarchy** — purple earns its place once per file:

| Color | Use | Max per file |
|---|---|---|
| **Purple** (`#692D9A` / `#4A1F7A`) | Hero only — the closing one-liner box. Maybe one pull-quote if it's earned. | 1–2 |
| **Blue** (`#0B5FC0`) | Section headings, table headers, dividers, accents, links. The structural color. | many |
| **Dark / body** (`#1F1B2E`, `#0E1116`) | Body text, paragraphs, lists, backgrounds. The default. | bulk |

Full palette and light/dark CSS block: `COLOR_REFERENCES.md` at the project root.

---

## Procedure when invoked

1. **Read the source fully** before writing anything. If the source is a URL the user pasted, fetch it with WebFetch. If it's a long paste, read it in one Read.
2. **Identify the core idea** in one sentence. If you can't, the brief isn't ready.
3. **Draft the six sections** in order. Skip none of the first four; the last two are the closer.
4. **Name the slug** from the idea, not the topic.
5. **Get today's date** with `date +%Y-%m-%d`. Do not guess.
6. **Write the file** to `Text-Explanations/<slug>-<YYYY-MM-DD>.md` (the canonical home) and a reference copy to `.claude/skills/text-summary/examples/<slug>-<YYYY-MM-DD>.md`.
7. **Print a short preview** in the reply (3–5 lines, not the whole file) plus the canonical file path.
8. **Offer the HTML follow-up** in one line, not as a menu:
   > "Want the dark-themed HTML version? Say `as html`."
9. **Append the file to `examples/INDEX.md`** so the example index stays current. Add a one-line row: file → source type → what it shows.

---

## Quality gate

Before writing the file, run the strongest test in one line:

> **If 80% of the prose were removed, would the visuals and the one-line takeaway still carry the argument?**

If not, restructure before saving.

Then the checklist:

```text
☐ Does the core idea tell the whole story in one paragraph?
☐ Does "What changed" name a trigger, a timing, and a structural shift?
☐ Does "Why it works" carry a table only when comparison earns it?
☐ Are the hidden insights actually hidden — i.e., not stated in the source?
☐ Is the open question unresolved, not restated?
☐ Is the one-line takeaway exactly one sentence, and earned?
☐ Is the slug the idea, not the topic?
☐ Is the YK palette `<style>` block prepended so the .md renders with the color hierarchy?
☐ Does the hero treatment land **only** on the one-liner (and maybe one earned pull-quote)?
☐ Did I update examples/INDEX.md?
```

---

## What this skill is not

- **Not `simplify-research`.** That skill produces evidence-tagged dashboards with falsifiers. This one writes a flowing brief.
- **Not `decode`.** That skill has layered reading speeds (30s / 1min / 10min) and stops after Layer 1 by default. This one writes one full document.
- **Not `summary-prompt`.** That's a 6-section intelligence brief *template* with rigid evidence tags. This one follows the shape but the voice is conversational and the structure earns each section.
- **Not `research`.** That skill goes out to gather primary sources. This one summarizes what's already in front of it.

If the user wants evidence tagging, route them to `simplify-research`. If they want reading-speed layers, route them to `decode`. If they want a 30-second scan, route them to `decode`. If they want research, route them to `research`.

---

## Examples to study before writing

| File | Source type | What it shows |
|---|---|---|
| `examples/slb-oilfield-services-2026-09-03.md` | News feature (~2,500 words) | Long-form source compressed; table for "company vs Big Oil"; 3 stacked hidden insights; hero in deep purple reserved for closing |
| `examples/ackman-brain-institute-2026-09-03.md` | Profile / interview (~2,200 words) | Thematic before/after (markets → medicine); "deeper thesis" surfaces that the article is *really* about an opponent you can't fight |

Read both before producing your first brief. The shape stays consistent across very different sources — that's the point.

---

## Hard rules

- **Six sections, in this order.** No more, no fewer unless the source genuinely has nothing for one.
- **No emoji clutter.** The section emojis (🧠 🔄 💰 👀 ⚠️ 🎯) are the standard. Do not invent new ones.
- **No padding.** A 1,500-word article gets a 600-word brief, not a 2,000-word one.
- **Slug from the idea, not the topic.**
- **Date is real.** Get it. Don't guess it.
- **Hero goes once.** If you put the purple treatment on the one-liner *and* a pull-quote *and* a section header, you've decorated, not communicated.
- **Update `examples/INDEX.md`** every time so the index stays useful.