# Examples — `text-summary` skill

These are real outputs produced by this skill, kept here so future invocations can see what "good" looks like before generating their own.

Each example has both `.md` (the durable artifact) and `.html` (the visual follow-up) so you can compare the two deliveries side by side.

---

## 📁 What's here

| File | Source type | What it shows |
|------|-------------|---------------|
| `slb-oilfield-services-2026-09-03.md` | News feature (Fortune profile, ~2,500 words) | Long-form source compressed into 6 sections; uses table for the numbers; shows "hidden insight" doing the real work (3 stacked insights); closing hero takeaway in deep purple |
| `slb-oilfield-services-2026-09-03.html` | Same | Color hierarchy rendered on dark luxury backdrop; pulsing hero box; quote pull-out treatment |
| `ackman-brain-institute-2026-09-03.md` | Profile / interview (Fortune, ~2,200 words) | Profile source-type treatment; thematic before/after (markets → medicine); "deeper thesis" surfaces that the article is *really* about an opponent you can't fight |
| `ackman-brain-institute-2026-09-03.html` | Same | Same hierarchy; hero box reserved for the one-liner only; two purple quotes in the body earn their place |
| `measles-asterisk-debate-2026-09-05.md` | News feature (WSJ, ~1,500 words) | Disputed measles death in Lancaster — shows asterisk-as-proxy, 70-point immunity gap (25% vs 95%), and MMR-split as quiet policy lever; national map reframes local story |
| `measles-asterisk-debate-2026-09-05.html` | Same | *Pending — .md only until HTML requested* |
| `skills-dev-unified-dna-2026-09-05.md` | Meta / folder synthesis (353 lines) | SKILLS_DEV dev folder decoded — 15 files → 1 DNA, 10-block palette, 9 visuals, 80% test; meta source-type shows skill works on its own documentation |
| `company-overview-2026-09-23.md` | Company profile (BEST Layout02, TD Power Systems) | Company profile compressed into 6 sections; orange hinge (68% export) doing double duty as gauge + closing band; specialization-as-moat hidden insight; export supercycle as primary growth engine |
| `skills-dev-unified-dna-2026-09-05.html` | Same | *Pending — .md only until HTML requested* |

---

## 🎯 What these examples demonstrate

### 1. The shape stays consistent across very different sources

Both pieces — one a company profile, one a person profile — follow the same flow:

```
🧠 Core idea       → one paragraph, plain language
🔄 What changed    → before / after, in motion
💰 Why it works    → numbers + table + mechanism
👀 Hidden insight  → the part most people miss (1–3 stacked)
⚠️ Open question   → what's unresolved
🎯 One-line        → the line you carry away
```

The **emoji + label** is the standard header treatment. Don't invent new section names — readers learn the pattern after one file.

### 2. The hero treatment is earned, not decorative

Both files reserve purple for **exactly one moment** — the closing takeaway box. That's the rule. If you use purple twice in the same explanation, one of those uses is decoration.

The HTML versions extend this: pull quotes get a softer purple treatment (lavender, with a left border), but the **hero-takeaway box** is the only place the full neon glow appears.

### 3. Tables only when comparison earns it

Both files include exactly **one table**. SLB uses it for "company vs. Big Oil" because the numbers are clearer side-by-side than in prose. Ackman uses it for a "world at a glance" data sheet because the figures are scattered in the source. When the source has 3+ comparable numbers, a table earns its place. When it doesn't, drop it.

### 4. The "hidden insight" section is where the real value lives

A weak summary lists facts. A strong summary says the thing the source wouldn't say about itself. Both files put 2–3 insights in this section, and both insights are *not in the source explicitly* — they're what a careful reader would notice but the writer didn't underline.

For SLB: "service companies do the work, Big Oil owns the assets" → "SLB is a victim of its own efficiency gains" → "the founding family's guilt (de Menil Collection)"

For Ackman: "Ackman treats everything as a deal" → "he processes grief like a hostile takeover" → "the American Dream Accounts became law without anyone noticing"

### 5. The open question names what's *unresolved*, not what's interesting

Both files end with a question that genuinely has no answer yet:

- SLB: Can the AI/data center pivot actually break the oil-cycle trap?
- Ackman: What does Lucy actually want?

Bad open questions restate the article. Good ones point to the gap.

---

## 📐 File pair conventions

```
<slug>-<YYYY-MM-DD>.md      ← primary delivery
<slug>-<YYYY-MM-DD>.html    ← only if user accepts the offer
```

The slug should be 2–4 lowercase, hyphenated words pulled from the source's core idea. Not the topic. The *idea*.

- `slb-oilfield-services` ← not `oil-company-profile`
- `ackman-brain-institute` ← not `bill-ackman-fortune`

---

## 🚫 What the examples intentionally do *not* do

- **No 25-section dashboards.** The shape has 6 sections. Period.
- **No evidence tagging** `(fact)/(inference)` everywhere. That's the `simplify-research` skill's job.
- **No layered reading speeds** (20s / 2min / 10min). That's the `decode` skill's job.
- **No falsifier tables.** Those exist; they're not the default here.
- **No jargon as decoration.** "Strategic moat" never appears unless the source uses it.

If you find yourself wanting one of these, the user probably asked for a different skill — check `/simplify-research`, `/decode`, or `/research`.

---

## 🔁 When to update these examples

Replace an example when:
- A new source type comes through that isn't represented (research paper, policy text, long report with multiple ideas)
- The color hierarchy drifts (hero appearing in the wrong place)
- The flow shape changes (a new section is added that wasn't there before)

Keep examples recent. An example from 2025 already feels dated.

— *Last updated: 2026-09-05*