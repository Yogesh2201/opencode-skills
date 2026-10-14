#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Reusable template renderer for Full Overview 2.0

Goal: LLM generates ONLY data/*.json (~600 tokens). This script renders
all 3 versions (Gemini / Plain / Markdown) with 0 LLM tokens for HTML.

Current heavy path (to replace):
  LLM reads example-gemini.html (113KB, ~28K tokens) + generates 115KB HTML (~20K tokens) = ~35K tokens/build

New light path:
  LLM reads/writes data/ujjivan.json (~2KB, ~800 tokens) + script copies templates via regex = ~3K tokens/build (91% saving)
  2nd/3rd version = 0 LLM tokens (script reuse)

Usage:
  python scripts/build.py --company ujjivan --version gemini --date 2026-09-25
  python scripts/build.py --company ujjivan --version all
  python scripts/build.py --company tdps --version gemini --date 2026-09-25

Template convention:
  templates/*.template.html are verbatim copies of examples/example-*.html (single source).
  No {{mustache}} editing needed for first prototype — script does targeted regex
  replacements for known data points. Later, convert templates to {{placeholders}}
  for cleaner injection (see make_placeholders.py).

Filings-only: data/*.json is the only file LLM touches. Templates are static.
"""
import argparse, json, pathlib, re, datetime, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
DATA = ROOT / "data"
# Output next to the trio — workspace-relative (skill may be invoked from any cwd via bash workdir)
OUT_DIR = pathlib.Path.cwd() / "Company_Overview" / "Final"
if not OUT_DIR.exists():
    # fallback for direct script run from skill folder
    OUT_DIR = pathlib.Path(r"C:\Users\Yogesh Kumar\Downloads\Open_Code\Company_Overview\Final")

# Map version -> template file
TEMPLATE_MAP = {
    "gemini": TEMPLATES / "gemini.template.html",
    "plain": TEMPLATES / "plain.template.html",
    "markdown": TEMPLATES / "markdown.template.md",
}

def load_data(company: str) -> dict:
    p = DATA / f"{company}.json"
    if not p.exists():
        sys.exit(f"Data file not found: {p} — LLM should generate data/{company}.json first (see data/schema.json)")
    return json.loads(p.read_text(encoding="utf-8"))

def render_gemini(template: str, data: dict, date: str) -> str:
    """Two modes:
    - If template contains {{placeholders}} (after make_placeholders.py), do simple replace
    - Else do targeted regex for key fields (fallback, proves 0-LLM-token rendering)
    Full version replaces 40+ via placeholders.
    """
    # Placeholder mode — preferred after one-time conversion
    if "{{" in template:
        out = template
        # Flatten data for placeholder replacement
        def flat(d, prefix=""):
            for k, v in d.items():
                if isinstance(v, dict):
                    yield from flat(v, f"{prefix}{k}.")
                elif isinstance(v, list):
                    # keep lists for JS injection handled separately
                    continue
                else:
                    yield (f"{prefix}{k}", str(v))
        for key, val in flat(data):
            out = out.replace("{{" + key + "}}", val)
        out = out.replace("{{render_date}}", date)
        # Handle forecast year_path JS injection if placeholders present
        if "forecast" in data and "year_path" in data["forecast"]:
            yp = data["forecast"]["year_path"]
            # Replace JS arrays if placeholders like {{forecast.year_path.price.bear}} exist
            # (actual injection done via JSON dump for charts)
            import json as _j
            out = out.replace("{{forecast_json}}", _j.dumps(data["forecast"]))
        out = out.replace("</body>", f"<!-- Rendered via .opencode/skill/full-overview-2-0/scripts/build.py from data/{data.get('meta',{}).get('company','')}.json — {date} — 0 LLM HTML tokens -->\n</body>")
        return out

    out = template
    meta = data.get("meta", {})
    price = data.get("price", {})
    kpis = data.get("bank_kpis", {})
    peers = data.get("peers_sfb", {})
    forecast = data.get("forecast", {})

    # 1. Company name / titles
    # Replace TDPS title + brand (first occurrence)
    out = out.replace("TD Power Systems", meta.get("company", "TD Power Systems"))
    out = out.replace("TDPOWERSYS", meta.get("nse", "TDPOWERSYS"))
    out = out.replace("533553", meta.get("bse", "533553"))
    out = out.replace("Dabaspet, Bengaluru", meta.get("hq", "Bengaluru"))

    # 2. Kicker + subtitle (simple)
    if "kicker" in meta:
        out = re.sub(r'<div class="kicker">.*?</div>', f'<div class="kicker">{meta["kicker"]}</div>', out, count=1, flags=re.S)

    # 3. Price / MCap tiles (regex for hero tile)
    # Example: <div class="value">₹2,124 Cr</div> -> loan book, etc. For demo we do generic price
    # Replace first price occurrence (₹764) with actual price
    if "current" in price:
        out = out.replace("₹764", f"₹{price['current']}")
        out = out.replace("₹23,864 Cr", f"₹{price.get('mcap_cr', 12215):,} Cr".replace(",", ","))
        # shares
        if "shares_cr" in price:
            out = re.sub(r"~31\.24 Cr shares", f"~{price['shares_cr']} Cr shares", out)
            out = re.sub(r"31\.24 Cr shares", f"{price['shares_cr']} Cr shares", out)

    # 3b. Earnings-yield tile (GNG reference values -> data["ey"]; no-op if absent)
    ey = data.get("ey", {})
    if ey:
        R = "&#8377;"
        p = ey.get("price", 669)
        m = ey.get("mcap_cr", 7627)
        pat = ey.get("pat_cr", 142)
        sh = ey.get("shares_cr", 11.40)
        eps = ey.get("eps", 12.46)
        y0 = ey.get("yield_pct", 1.86)
        y1 = ey.get("yield_target_pct", 3.70)
        pe0 = ey.get("pe_current", 53.71)
        pe1 = ey.get("pe_target", 27.027)
        mt = ey.get("mcap_target_cr", 3837.84)
        pt = ey.get("price_target", 336.65)
        lo = ey.get("low_price", 239)
        iv = ey.get("iv", 385)
        swaps = [
            (f"{R}669.00", f"{R}{p:,.2f}"), ("₹669.00", f"₹{p:,.2f}"),
            (f"{R}7,627.00 Cr", f"{R}{m:,.2f} Cr"), ("₹7,627.00 Cr", f"₹{m:,.2f} Cr"),
            (f"{R}3,837.84 Cr", f"{R}{mt:,.2f} Cr"), ("₹3,837.84 Cr", f"₹{mt:,.2f} Cr"),
            (f"{R}336.65", f"{R}{pt:,.2f}"), ("₹336.65", f"₹{pt:,.2f}"),
            ("3.70%", f"{y1:.2f}%"), ("3.7%", f"{y1:.1f}%"),
            ("1.86%", f"{y0:.2f}%"),
            ("53.71&times;", f"{pe0:.2f}&times;"), ("53.71×", f"{pe0:.2f}×"),
            ("53.7&times;", f"{pe0:.1f}&times;"), ("53.7×", f"{pe0:.1f}×"),
            ("27.027&times;", f"{pe1:.3f}&times;"), ("27.027×", f"{pe1:.3f}×"),
            ("27.03&times;", f"{pe1:.2f}&times;"), ("27.03×", f"{pe1:.2f}×"),
            ("27&times;", f"{pe1:.0f}&times;"), ("27×", f"{pe1:.0f}×"),
            (f"{R}669", f"{R}{p:,.0f}"), ("₹669", f"₹{p:,.0f}"),
            (f"{R}7,627 Cr", f"{R}{m:,.0f} Cr"), ("₹7,627 Cr", f"₹{m:,.0f} Cr"),
            (f"{R}142 Cr", f"{R}{pat:,.0f} Cr"), ("₹142 Cr", f"₹{pat:,.0f} Cr"),
            ("+1.84pp", str(ey.get("diff_pp", "+1.84pp"))),
            ("-49.68%", str(ey.get("diff_pe_pct", "-49.68%"))),
            ("-49.7%", str(ey.get("diff_pct", "-49.7%"))),
            (f"LOW {R}239", f"LOW {R}{lo}"), ("LOW ₹239", f"LOW ₹{lo}"),
            (f"IV {R}385", f"IV {R}{iv}"), ("IV ₹385", f"IV ₹{iv}"),
            ("11.40 Cr", f"{sh:.2f} Cr"),
            (f"{R}12.46", f"{R}{eps:.2f}"), ("₹12.46", f"₹{eps:.2f}"),
        ]
        for old, new in swaps:
            out = out.replace(old, new)

    # 4. KPI row: loan book, deposits, total income
    if kpis:
        out = re.sub(r"₹32,122 Cr.*?\n.*?FY25.*?\n", f"₹{kpis.get('loan_book_cr', 32122):,} Cr", out)  # simplified demo
        # More precise replacements would use placeholders; here we just prove mechanism
        # For full build, use: out = re.sub(r"\{\{loan_book_cr\}\}", f"{kpis['loan_book_cr']:,}", out)

    # 5. Forecast anchor line
    if forecast and "anchor" in forecast:
        anc = forecast["anchor"]
        anchor_str = f"Anchor: ₹{anc.get('price', 62.7)} · MCap ₹{anc.get('mcap_cr', 12215):,} Cr · shares ~{anc.get('shares_cr', 194.8)} Cr"
        # Replace anchor line in s06 card
        out = re.sub(r"Anchor:.*?Mcap.*?\n", anchor_str + " · FY25 total income ₹7,201 Cr\n", out, count=1)

    # 6. Render date
    out = out.replace("2026-09-20", date)
    out = out.replace("20 Sep 2026", datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d %b %Y"))

    # 7. Forecast series injection (price/mcap arrays) — critical for charts
    if forecast and "year_path" in forecast:
        yp = forecast["year_path"]
        # Replace JS series arrays (price)
        # Pattern: series: { bear: [62.7, 49.4, ...], base: [...], bull: [...] }
        for kind in ["price", "mcap"]:
            if kind in yp:
                for scen in ["bear", "base", "bull"]:
                    arr = yp[kind].get(scen)
                    if arr:
                        # crude: replace first occurrence of each scenario array
                        # In production, use placeholders: /*{{forecast_price_bear}}*/
                        pass  # placeholder for full impl

    # Traceability
    out = out.replace("</body>", f"<!-- Rendered via .opencode/skill/full-overview-2-0/scripts/build.py from data/{meta.get('company','')}.json — {date} — 0 LLM HTML tokens -->\n</body>")

    return out

def render_plain(template: str, data: dict, date: str) -> str:
    # Same logic, different template
    return render_gemini(template, data, date)  # reuse for prototype

def render_markdown(template: str, data: dict, date: str) -> str:
    out = template
    meta = data.get("meta", {})
    out = out.replace("TD Power Systems", meta.get("company", "TD Power Systems"))
    out = out.replace("2026-09-20", date)
    return out

def build(company: str, version: str, date: str):
    data = load_data(company)
    company_slug = company.capitalize()  # Ujjivan, Tdps
    # Normalize company file prefix: Ujjivan, TDPS
    prefix_map = {"ujjivan": "Ujjivan", "tdps": "TDPS", "tdp": "TDPS"}
    prefix = prefix_map.get(company.lower(), company_slug)

    versions = ["gemini", "plain", "markdown"] if version == "all" else [version]
    for ver in versions:
        tmpl_path = TEMPLATE_MAP[ver]
        if not tmpl_path.exists():
            print(f"Template missing: {tmpl_path}")
            continue
        tmpl = tmpl_path.read_text(encoding="utf-8")
        if ver == "gemini":
            out = render_gemini(tmpl, data, date)
            out_name = f"{prefix}-{date}.html"
            sub = f"Gemini-{date[:7]}"
        elif ver == "plain":
            out = render_plain(tmpl, data, date)
            out_name = f"{prefix}-{date}.html"
            sub = f"Plain-{date[:7]}"
        else:
            out = render_markdown(tmpl, data, date)
            out_name = f"{prefix}-{date}.md"
            sub = f"MD-{date[:7]}"

        out_path = OUT_DIR / sub / out_name
        # Safety: ensure prototype output goes to Final but marked as prototype
        # For true prototype isolation, uncomment next line to output to prototype_token_opt/out/
        # out_path = ROOT / "out" / out_name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out, encoding="utf-8")
        print(f"Built {ver:8} -> {out_path} ({len(out):,} chars)")

def main():
    ap = argparse.ArgumentParser(description="Build Full Overview 2.0 from data JSON + static templates")
    ap.add_argument("--company", required=True, help="data/<company>.json stem, e.g. ujjivan, tdps")
    ap.add_argument("--version", choices=["gemini", "plain", "markdown", "all"], default="gemini")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD")
    args = ap.parse_args()
    build(args.company, args.version, args.date)

if __name__ == "__main__":
    main()
