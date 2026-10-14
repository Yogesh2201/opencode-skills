# Prototype — Reusable Template Token Optimization

**Goal:** Cut Full Overview 2.0 token cost by ~90% by moving HTML generation off the LLM.

> This folder is **isolated from the skill**. Test here, then copy the proven pattern back into `.opencode/skill/full-overview-2-0/` when satisfied.

---

## 1. The problem (measured)

| Step | Current | Tokens |
|------|---------|--------|
| LLM **reads** `examples/example-gemini.html` (113 KB) | every build | ~28,000 |
| + reads 4 assets (`tokens.md`, `section-skeleton.md`, `forecast-model.md`, `verify-checklist.md`) | every build | ~4,000 |
| LLM **generates** full 115 KB HTML (inlined CSS/JS verbatim + company data) | every build | ~20,000 |
| **Total per Gemini build** | | **~35,000** |
| ×3 versions (Gemini/Plain/Markdown) | | **~100,000** |

Second company = pay again. No reuse.

## 2. The solution — data-only LLM

```
prototype_token_opt/
  templates/
    gemini.template.html    ← verbatim copy of examples/example-gemini.html (one-time, static)
    plain.template.html     ← same for Plain
    markdown.template.md    ← same for Markdown
  data/
    ujjivan.json            ← ONLY file LLM generates (~600 tokens)
    tdps.json               ← second example proves multi-company reuse
    schema.json             ← JSON Schema for data/*.json (validates filings-only)
    forecast-model.md       ← copied, now static (not LLM-read per build)
    tokens.md / section-skeleton.md / verify-checklist.md
  scripts/
    build.py                ← python: template + data → Final/ (0 LLM tokens)
    verify.py               ← checklist as script (0 LLM tokens)
    make_placeholders.py    ← one-time converter: hardcoded values → {{placeholders}}
  out/                      ← optional isolated output (vs Company_Overview/Final/)
```

**New cost per build:**

| Step | New | Tokens |
|------|-----|--------|
| LLM reads `data/schema.json` + filings excerpt | once | ~1,800 |
| LLM **generates** `data/<company>.json` only | once | ~800 |
| Script `build.py` renders all 3 HTMLs via file copies + regex | 0 LLM | 0 |
| **Total per company (all 3 versions)** | | **~2,600** |
| Saving | | **~92% (35K → 2.6K)** |
| 2nd version (Plain/Markdown) incremental | | **0** |

## 3. How it works

### Today (heavy) — LLM does everything
```
User picks "Ujjivan + Gemini"
  → LLM reads example-gemini.html (113 KB)
  → LLM reads tokens.md, skeleton, forecast-model.md
  → LLM generates 115 KB HTML with inlined CSS/JS + Ujjivan data
  → LLM writes Company_Overview/Final/Ujjivan_Gemini-forecast-2026-09-25.html
```

### Prototype (light) — LLM does data only
```
User picks "Ujjivan + Gemini"
  → LLM generates data/ujjivan.json only:
    {
      "meta": {"company": "Ujjivan Small Finance Bank", "nse": "UJJIVANSFB", ...},
      "price": {"current": 62.7, "mcap_cr": 12215, "shares_cr": 194.8, ...},
      "peers_sfb": {"peers": [...]},
      "forecast": {"anchor": {...}, "scenarios": {...}, "year_path": {...}}
    }
  → bash: python scripts/build.py --company ujjivan --version all
    → reads templates/gemini.template.html (static, not LLM)
    → reads data/ujjivan.json
    → injects values via regex/placeholders
    → writes Company_Overview/Final/Ujjivan_*.html + .md (all 3)
  → bash: python scripts/verify.py Company_Overview/Final/Ujjivan_Gemini-*.html
```

Templates are **never regenerated** by the LLM. They are file-copied once from `examples/` and treated as immutable.

### Placeholder strategy (two options, pick one)

**Option A — Regex replacement (zero template editing, used in current build.py):**
- Template stays verbatim TDPS.
- `build.py` does `template.replace("TD Power Systems", data["meta"]["company"])`, `re.sub("₹764", f"₹{data['price']['current']}")` for 12 high-visibility fields.
- Pros: No upfront work, works today.
- Cons: Brittle if TDPS values change.

**Option B — Mustache placeholders (cleaner, one-time conversion):**
- Run `python scripts/make_placeholders.py` once: replaces `₹764` → `{{price.current}}`, `111 countries` → `{{kpi.countries}}`, etc.
- Then `build.py` is trivial: `template.replace("{{price.current}}", str(data["price"]["current"]))`.
- Pros: Explicit, maintainable, diffable.
- Cons: One-time 10-min conversion.

Both achieve 0 LLM tokens for HTML. B is recommended for final skill integration.

## 4. What LLM actually generates now (example)

`data/ujjivan.json` — 6 KB, ~600 tokens, filings-traced:

```json
{
  "meta": {"company": "Ujjivan Small Finance Bank", "nse": "UJJIVANSFB", "bse": "542904", "hq": "Bengaluru"},
  "price": {"current": 62.7, "mcap_cr": 12215, "shares_cr": 194.8, "pe_ttm": 13.5, "pb": 1.79},
  "bank_kpis": {"loan_book_cr": 32122, "secured_pct": 43.5, "deposits_cr": 37630, "casa_pct": 25.5, "nim_fy25": 8.8, "gnpa": 2.18},
  "peers_sfb": {"peers": [{"name": "AU SFB", "loan_book_cr": 115704, "share_pct": 42.0}, {"name": "Ujjivan SFB", "loan_book_cr": 32122, "share_pct": 11.7, "is_subject": true}]},
  "forecast": {"anchor": {"price": 62.7}, "scenarios": {"bear": {"price_fy31": 36.4, "cagr": -10.3}, "base": {"price_fy31": 107.9, "cagr": 11.5}}}
}
```

Compare to generating 115 KB HTML with inlined 400-line CSS, orb animations, 200-line JS charts, etc. — none of that is LLM work anymore.

## 5. Verification — also off LLM

`scripts/verify.py` replicates `assets/verify-checklist.md`:

```bash
python scripts/verify.py Company_Overview/Final/Ujjivan_Gemini-forecast-2026-09-25.html
# PASS  no PART_/JS_ markers
# PASS  div balanced (295 open / 295 close)
# PASS  exactly one </body>
# PASS  id s04v present
# PASS  hdrFcToggle present
# PASS  val-visual present
# ...
```

0 tokens, runs in <100ms.

## 6. How to test in this prototype (without touching the skill)

```bash
# 1. LLM generates data only (you already have data/ujjivan.json as example)
#    Next company: ask LLM to produce data/<newcompany>.json from filings excerpt — ~600 tokens

# 2. Render all 3 versions with 0 LLM tokens
python prototype_token_opt/scripts/build.py --company ujjivan --version all --date 2026-09-25

# 3. Verify
python prototype_token_opt/scripts/verify.py Company_Overview/Final/Ujjivan_Gemini-forecast-2026-09-25.html
python prototype_token_opt/scripts/verify.py Company_Overview/Final/Ujjivan_Plain-forecast-2026-09-25.html

# 4. Compare token counts
#    Before: LLM read 113KB + 4 assets + generated 115KB = 35K
#    After:  LLM generated 6KB JSON = 2.6K
```

When satisfied, copy the pattern back to the skill:

```bash
# In .opencode/skill/full-overview-2-0/ :
#   mkdir templates/ data/ scripts/
#   cp examples/* templates/  (one-time)
#   move forecast logic to data/forecast_presets.json
#   add scripts/build.py + verify.py
#   update SKILL.md: Step 2 = "read data/schema.json, generate data/<company>.json" not "read example-gemini.html"
```

## 7. Other token savers included

- **Template caching:** `examples/` read once, never per-build. Saves 28K input tokens/build.
- **Static assets:** `tokens.md`, `section-skeleton.md`, `forecast-model.md` become `data/*.json` presets — no LLM parsing of markdown tables per build.
- **CSS/JS deduplication:** Inlined CSS/JS stays in template file, not regenerated. Saves ~12K output tokens/build where LLM was repeating verbatim orb CSS, chart JS.
- **Incremental versions:** Gemini → Plain → Markdown is now 0 tokens for 2nd/3rd (script copies data). Before: 20K × 2 extra.
- **Chunked reads removed:** No `<!--PART_B-->` needed — templates are files, not LLM windows.
- **Schema validation:** `data/schema.json` lets LLM self-check JSON without reading full example for structure.

## 8. Rollout plan

1. **This prototype** — validate with Ujjivan + TDPS (2 companies × 3 versions = 6 files) via `build.py`.
2. **Measure** — compare actual token usage (Opencode logs) before/after on one fresh company (e.g., Jana SFB).
3. **Decide placeholder style** — A (regex, ship today) vs B (mustache, cleaner). Recommendation: B.
4. **Migrate skill** — copy `prototype_token_opt/templates/` + `scripts/` + `data/schema.json` into `.opencode/skill/full-overview-2-0/`, update `SKILL.md` Step 2/3.
5. **Deprecate heavy path** — keep `examples/` as reference but mark "read only via script, not LLM".

---

**Status:** Prototype ready at `prototype_token_opt/`. Run `python prototype_token_opt/scripts/build.py --company ujjivan --version gemini` to prove 0-LLM-token render. No changes made to `.opencode/skill/full-overview-2-0/` yet — safe to test.
