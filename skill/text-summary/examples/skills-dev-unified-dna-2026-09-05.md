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

# The One Prompt That Became Fifteen: Decoding the Skills_Dev Folder

## 🧠 Core idea

Here's what's actually going on — the `SKILLS_DEV` folder isn't 15 different prompts. It's **one idea iterated 15 times** until it became three shippable skills. The idea: *don't summarize information, decode it into understanding* — visually, at three reading speeds, with falsifiability built in.

Every file is a different weight of the same engine. `summary-prompt` learned to teach itself. `ULTIMATE RESEARCH` added the 18-step analytical sequence. `Visual-First Reasoning` locked the 9 visual formats. `deepseak` and `kimi_code` unified them. `UNIFIED MASTER DECODE PROTOCOL` added the 30-second scan and drill-down menus. The three production skills in `.claude/skills/` are just that DNA packaged for three jobs: user research, source decoding, and text summarization.

## 🔄 What changed

**Before (v1.0):** A single 6-section text summarizer (`summary-prompt.md`) — Big Picture, Challenges, Stakeholders, Quotes, Controversies, What to Watch. Useful, but flat. One template, no depth switching, no visuals as code.

**After (v2.0+ → production):** The engine grew a spine. First the 18-step decode sequence (find thesis → tag evidence → follow mechanism → observe observer → falsify). Then the 9-format visual taxonomy (🌳 Tree, 🔗 Chain, 🧱 Box, 🃏 Cards, 📊 Table, 📈 Chart, 🖼️ Image, 🕸️ Timeline, ⚖️ Comparison) with a hard rule: *if 80% of prose were deleted, visuals must still carry the argument*. Then three depth layers — `20s scan → 2min picture → 10min dive` (refined to `30s / 1min / 10min` in UNIFIED MASTER).

**The structural shift:** From *template that produces essays* to *palette that builds dashboards*. The key invention was the **10-block palette** (Thesis, Evidence, Chart, Chain, Insights, What Could Be Wrong, Scenarios, Why It Matters, What to Watch, Bottom Line) — use 5–10, drop what doesn't earn its place. And the **file-first + HTML-gate** rule: default is a `.md` in the current directory, HTML only on explicit "as html." Thinking became shipping.

## 💰 Why it works

The folder's scale is deceptive. The numbers show convergence, not sprawl:

| What the numbers say | Figure | Why it matters |
|---|---|---|
| **Files at root** | 13 (one empty) + 3 production skills = 15 working files | 2 are confirmed identical duplicates — the *real* unique count is 13 |
| **Shared principles** | 8 (decode, visual-first, 3 speeds, palette, tag numbers, mechanism, observe observer, falsify) | Every file repeats these verbatim — that's convergence, not coincidence |
| **Block palette** | 10 blocks | Same backbone in `simplify-research`, `kimi_code`, `deepseak`, `UNIFIED MASTER` |
| **Visual vocabulary** | 9 formats | Identical table in 5 files — the non-negotiable test travels with it |
| **Reading speeds** | 3 (20s/2m/10m) → refined to 30s/1m/10m | Highest-value first, every layer standalone |
| **Prohibitions** | 8 (no chronology, no paraphrase, no padding, no invented data, no correlation-as-causation, no over-psychologizing, no decoration, no slow intro) | The guardrails that keep decoding from drifting back into summarizing |
| **Evolution lineage** | Idea → text-summary → +18 steps → +visuals → +news mode → 5-part unified form → 3-layer UX → 3 skills | All 15 files map onto one tree — `QUICK-REFERENCE DECISION TREE` routes any source in 3 questions |

The big number is **15 files, 1 DNA**. The small number that explains the whole story is **80%** — the visual compression test. If visuals can't carry the argument without prose, restructure.

## 👀 Hidden insight

**The outlier is the clue.** `Context Compact & Summarize Skill.md` is the only file that decodes *conversations*, not content — objective, decisions, evidence, state compressed into a CURRENT STATE block. It looks adjacent, but the master summary flags it as the *compression engine powering the other 14*. The insight: session management and content decoding share the same problem — signal loss across turns — and the same answer.

**The duplicates are documented, not hidden.** Two pairs are identical: `research-easy-synthesis ≡ research-synthesis` and `kimi_code ≡ Qwen_nfpw531fi`. The folder doesn't pretend it's clean — it *labels* the copies as "probable copy" / "confirmed duplicate." That's evidence discipline applied to itself: tag what you know, flag what you infer.

**Shipping gated HTML is a design decision, not a feature.** Every skill says: long article + "I want a visual" ≠ HTML. Default stays `.md` unless the user says `as html` / `make HTML file`. That gate exists because visuals are powerful — the fastest way to misuse them is to generate them by default. The folder treats visual power as something to *earn*, like purple in the YK palette.

## ⚠️ Open question

Can one unified DNA actually serve three different domains — user research (interviews, NPS, tickets), source decoding (articles, reports), and general text summarization — without one of them drifting back into generic summarizing?

And the harder question underneath: the `UNIFIED MASTER DECODE PROTOCOL` adds a memory rule — learn what depth the user picks most and bias future outputs. No production skill has shipped that yet. When it does, does personalization preserve the three-speed guarantee — or does it quietly collapse the 30-second scan that the whole system is built on?

## 🎯 One-line takeaway

<span class="hero">*Fifteen files iterated one sentence — "decode, don't summarize" — until visuals could carry 80% of the argument and a reader could stop at 30 seconds, 2 minutes, or 10 and still know what matters.*</span>
