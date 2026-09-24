# MEMORY — `stock-analysis` skill

> Last audited: **2026-09-03 07:27 IST** · **Updated 2026-09-03 07:35 IST for HTML gold numbers** — audited against `SKILL.md` (313 lines, light-bg YK + red #B91C1C) and the sole example `examples/IRCTC_Sep_3_2026.md`.

> **2026-09-03 07:35 — HTML color fix:** dark `.html` numbers switched from red `#FF6B6B` → warm gold `#FFD166` (`--num` / `--num-bg` `rgba(255,209,102,0.12)`) — user confirmed "much better". `SKILL.md:77-90` updated: table now has Gold row + rule notes light=red / dark=gold, optional follow-up notes gold. `Stock/` folder created at repo root.

---

## 1. What this skill is (one line)

Produces a **single-name equity research report** — 7 numbered ALL-CAPS sections, Adobe header (`🚀` + bold-label blockquote), YK light-bg palette with **red `#B91C1C` backticked numbers**, 4-row DCF table + ASCII valuation bar + hero verdict — saved as one styled `.md` in `Stock/` (with optional `as html` dark-theme follow-up).

---

## 2. Audit result — spec vs. example (IRCTC 2026-09-03)

### ✅ Compliant (keep)

| Area | Evidence |
| :--- | :--- |
| **7-section ALL-CAPS shape** | IRCTC has exactly 1→7 in order, correct `## 1. COMPANY OVERVIEW` casing |
| **Style block** | Prepended verbatim, `code { color:#B91C1C }` override intentional vs global YK `#692D9A` |
| **Header blockquote** | 6 bold labels present (TICKER / REPORT DATE / LIVE PRICE / MARKET CAP / SECTOR / VALUATION STATUS) |
| **Guided bullets** | 3 bullets each in §1, §2, §3, §4, §6 — all *before* tables, never inside — earns-place framing |
| **Purple economy** | Exactly one `<span class="hero">` (§7 closer) + one `<div class="quote">` (§7 Research Summary) — no other purple |
| **Valuation bar** | 5-col fenced ASCII (`WS LOW | CURRENT | BUY ZN | IV | DCF`) + 4 bullet metadata lines — Persistent Systems style correct |
| **DCF params** | All inputs disclosed (WACC/Rf/ERP/Beta/Cost of Equity/FCF base/growth fade/terminal g/net cash/shares) |
| **Red flags** | 5 flags, Severity 🟢🟡🔴, Evidence cells backticked + Dashboard fenced strip under `### Red Flag Dashboard` |
| **Disclaimer** | Present, italicized, educational-only + source caveats |

### ⚠️ Drift — fix or document

| # | Drift | Spec says | Example does | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **D-1** | **DCF 4-row vs 5-row** | §5 table = *exactly 4 rows*: `DCF Base | Relative Peer Multiples (Nx EV/EBITDA) | Blended IV | Buy Zone (=0.80×)` | IRCTC has **5 rows**: `DCF ₹487 | Forward P/E 30× ₹585 | EV/EBITDA 22× ₹510 | Blended ₹527 | Buy Zone ₹422` — splits peer multiples into two rows | **Most-likely-to-drift section, and it did.** Decide: either (a) collapse to one `Relative Peer Multiples` row (pick one method) to stay 4-row, or (b) update spec to allow `4–5 rows` when both P/E and EV/EBITDA cross-checks are material. Until then, IRCTC is *non-canonical* despite being the only example. |
| **D-2** | **File naming** | `<TICKER>_<Month_Day_Year>.md` with *full month* e.g. `Meta_September_3_2026.md` | `IRCTC_Sep_3_2026.md` (abbrev `Sep`) | Standardize. Recommend keeping `September` convention; add a lint that rejects `Sep/Sep.` abbrev. |
| **D-3** | **Output folder** | Every report lands in `Stock/` at project root | Repo has *no* `Stock/` folder; example lives in `skill/stock-analysis/examples/` | Create `Stock/` or change spec to `skill/examples` as canonical. Next invocation should `mkdir Stock` before write. |
| **D-4** | **Header emoji** | `# 🚀 EQUITY RESEARCH REPORT:` — rocket non-negotiable | `# 🚂 EQUITY RESEARCH REPORT: IRCTC` — train emoji (contextual) | Allow *one* ticker-relevant emoji substitution and document it; otherwise enforce 🚀. |
| **D-5** | **INR/Cr handling** | Spec examples use `$` / `B` / `T` | IRCTC uses `₹`, `Cr` (₹37,808 Cr, ₹1,227 Cr FCF) — correct for NSE but undocumented | Add an **India note** to spec: use `₹` + `Cr`/`Lakh`, keep `code` red, keep `% of Market Cap` column. |

### 🔍 Not a bug, but worth noting

- **Indian PSU segment splits** are indicative (IRCTC doesn't publish audited segment revenue) — footnote present in §1, good practice to keep.
- **Historical/sector benchmarks** marked `*` as approximate with blockquote footnote — IRCTC does this correctly in §4.
- **Net debt adjustment** as `+₹3,419 Cr` (net cash) — sign correct for zero-debt PSU, but spec phrasing "Net Debt Adjustment: `-$X.XXB`" assumes US net-debt; add sign convention note for net-cash cases.

---

## 3. Quality gate — run before every save

```
HEADER  ☐ 🚀 title + 6-label blockquote (TICKER/REPORT DATE/LIVE PRICE/MARKET CAP/SECTOR/VALUATION STATUS)
STRUCT  ☐ Exactly 7 ALL-CAPS sections in order ☐ <style> prepended verbatim ☐ One hero + one quote only
TABLES  ☐ Every number in backticks = red (#B91C1C) in .md / gold (#FFD166) in .html ☐ §5 = 4 rows (or 5 if spec updated) + 📌 NOTE → 📈 Bar → ⚙️ Params ☐ §6 = Dashboard strip ☐ No bullets inside tables
DATA    ☐ DCF params fully disclosed ☐ Buy Zone = Blended ×0.80 (single value) ☐ ≥1 🔴 High if consensus < spot
CLOSE   ☐ Verdict = one 🎯 question/sentence, not hedge ☐ Disclaimer italicized ☐ File = Stock/<TICKER>_<Month_Day_Year>.md, one file only + html copy uses gold numbers
```

---

## 4. What to update next (priority order)

1. **Resolve D-1** — either re-write IRCTC §5 to 4 rows (merge Forward P/E + EV/EBITDA into one `Relative Peer Multiples (Blended P/E+EV/EBITDA)` row at `₹548` midpoint) or amend `SKILL.md:169-207` to `4–5 rows` with rule: *if two peer methods, show both but Blended = avg(DCF + all peer rows)*.
2. **Create `Stock/` folder** at repo root and move/lint IRCTC copy there as `IRCTC_September_3_2026.md` (keep example copy in skill/examples for reference).
3. **Add `INR/Cr` convention** to `SKILL.md § House style notes` — 1 line.
4. **Add automated checker** (optional): small script that counts `## [1-7].` headings, counts `§5` table rows, rejects abbreviated months, checks `<span class="hero">` count ==1.

---

## 5. Memory for next invocation

- **IRCTC snapshot (Sep 2 close):** spot `₹473`, DCF base `₹487` (+3.0%), blended `₹527` (+11.4%), buy zone `₹422` (spot +12% above entry → *wait*). `TTM Revenue ₹5,425 Cr / PAT ₹1,393 Cr / FCF ₹1,227 Cr / OPM 31% (was 36% FY23) / ROCE 46.1% / ROE 34.6% / P/E 27.4× / P/B 8.78× / 52W high ₹739 / Govt 62.40%`.
- **Thesis:** De-rating `-34% 1Y` from `P/E 50×→27×` is *mostly done*; remaining debate is whether `OPM 31%` is floor or slips another `3-5pp`. Bull = catering re-price + Rail Neer utilisation → `33-34%`; bear = fee cap + input inflation persists.
- **Example quality:** IRCTC is strong on narratives (regulated tollbooth, two-speed engine) but is the *reference for what to fix* on the DCF table shape.

---

*Memory updated 2026-09-03 07:35 — HTML gold #FFD166 locked in as canonical for all future dark HTML (replaces red). Stock/ folder exists. Re-audit after any `SKILL.md` edit or new report.*
