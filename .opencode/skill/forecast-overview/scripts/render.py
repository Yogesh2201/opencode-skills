#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render.py — forecast-overview renderer (generic, data-driven).

Reads data/<company>-forecast.json + references/forecast-section.html and
writes a standalone HTML page with the s06 block:

  python .opencode/skill/forecast-overview/scripts/render.py --company pinelabs --date 2026-09-25

Replacements are region-based (regex on stable anchors), never hardcoded to one
company's values, so any data file in the shape of SKILL.md Step 2 works.
Chart scaling (ymax/ticks) comes from data["chart"] — explicit beats clever.

Output: Forecast/<Short>-forecast-<YYYY-MM-DD>.html (standalone page, CSS/JS inlined).
"""
import argparse
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path.cwd()  # workspace root (invoke via bash workdir)
SKILL = pathlib.Path(__file__).resolve().parents[1]
DATA = SKILL / "data"
REF = SKILL / "references" / "forecast-section.html"
OUT_DIR = ROOT / "Forecast"


def fmt_price(v):
    return f"{int(v):,}" if float(v) == int(float(v)) else f"{v:,}"


def fmt_cagr(v, signed=True):
    s = "+" if (signed and float(v) >= 0) else ""
    return f"{s}{v}%"


def rev_of(sc):
    cagr = sc.get("total_income_cagr", sc.get("sales_cagr"))
    fy31 = sc.get("total_income_fy31_cr", sc.get("sales_fy31_cr"))
    return cagr, fy31


CSS = """
:root { --bg:#fbfbfd; --surface:#ffffff; --surface-2:#f0f4f9; --ink:#1f1f1f;
--ink-2:#444746; --ink-3:#8f909c; --line:#e3e3e3; --line-strong:#c5c7c9;
--ok:#1e8e3e; --warn:#b06000; --bad:#d93025; --chart-blue:#4285F4;
--chart-blue-deep:#1967d2; --chart-context:#b3b5be; --r-md:16px; --r-pill:999px; }
body { margin:0; background:var(--bg); color:var(--ink);
font-family:"Outfit","Segoe UI Variable",system-ui,sans-serif; }
.wrap { max-width:880px; margin:0 auto; padding:0 24px 72px; }
.kicker { color:var(--ink-3); font-size:.8rem; letter-spacing:.14em;
text-transform:uppercase; font-weight:500; margin:48px 0 16px; text-align:center; }
h1 { font-size:2.2rem; font-weight:400; text-align:center; margin:0 0 10px; }
.subtitle { color:var(--ink-2); text-align:center; font-weight:300; margin-bottom:8px; }
h2 { font-size:1.32rem; font-weight:500; margin-top:56px; margin-bottom:8px; }
h2 .num { color:var(--ink-3); font-weight:400; margin-right:10px; }
.section-note { color:var(--ink-2); font-weight:300; margin-bottom:22px; }
.card { background:var(--surface); border-radius:var(--r-md); padding:26px 28px;
margin:20px 0; box-shadow:0 1px 2px rgba(0,0,0,.06),0 8px 24px rgba(0,0,0,.05); }
.card h3 { font-size:1.02rem; font-weight:500; margin-bottom:2px; }
.card .sub { color:var(--ink-3); font-size:.84rem; font-weight:300; margin-bottom:18px; }
.derived-flag { display:inline-block; background:var(--surface-2); color:var(--ink-2);
font-size:.66rem; letter-spacing:.05em; text-transform:uppercase;
border-radius:var(--r-pill); padding:2px 10px; margin-left:8px; font-weight:500; }
.fc-head { display:flex; justify-content:space-between; align-items:flex-start; gap:12px; }
.fc-badge { font-size:.72rem; color:var(--ink-3); border:1px solid var(--line);
border-radius:var(--r-pill); padding:4px 12px; white-space:nowrap; }
.fc-kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:14px; }
.fc-kpi { border:1px solid var(--line); border-radius:12px; padding:14px; }
.fc-kpi.bear { border-top:3px solid var(--bad); }
.fc-kpi.base { border-top:3px solid var(--chart-blue); }
.fc-kpi.bull { border-top:3px solid var(--ok); }
.k-label { font-size:.72rem; text-transform:uppercase; letter-spacing:.07em;
color:var(--ink-3); font-weight:500; }
.k-price { font-size:1.7rem; font-weight:500; margin:6px 0; }
.k-row { font-size:.8rem; color:var(--ink-2); display:flex;
justify-content:space-between; gap:8px; }
.fc-note { background:var(--surface-2); border-radius:12px; padding:12px 14px;
font-size:.86rem; font-weight:300; margin-top:14px; }
.fc-stack { display:grid; gap:16px; margin-top:18px; }
.fc-panel { border:1px solid var(--line); border-radius:12px; padding:16px; }
.fc-title { font-weight:500; }
.fc-sub { font-size:.78rem; color:var(--ink-3); }
.fc-legend { display:flex; gap:8px; margin:12px 0; flex-wrap:wrap; }
.fc-chip { font:inherit; font-size:.76rem; font-weight:500; border:1px solid var(--line);
background:var(--surface); border-radius:var(--r-pill); padding:5px 12px; cursor:pointer; }
.fc-chip[aria-pressed="false"] { opacity:.45; }
.fc-chip .dot { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:6px; }
.fc-plot { position:relative; }
.fc-plot svg { width:100%; height:auto; display:block; }
.fc-tip { position:absolute; top:0; background:var(--surface); border:1px solid var(--line);
border-radius:10px; padding:8px 10px; font-size:.76rem; box-shadow:0 8px 24px rgba(0,0,0,.08);
display:none; pointer-events:none; min-width:150px; z-index:5; }
.fc-tip.on { display:block; }
.fc-tip .t-h { font-weight:600; margin-bottom:4px; }
.fc-tip .t-r { display:flex; justify-content:space-between; gap:10px; }
.fc-tip .t-r i { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:5px; }
.fc-foot { display:flex; justify-content:space-between; font-size:.72rem;
color:var(--ink-3); margin-top:8px; flex-wrap:wrap; gap:6px; }
.fc-line { fill:none; stroke-width:2.5; }
.fc-dot { opacity:0; transition:opacity .3s; }
.fc-dot.on { opacity:1; }
.fc-guide { opacity:0; }
.fc-guide.on { opacity:1; }
table.dt { width:100%; border-collapse:collapse; font-size:.84rem; }
table.dt th { text-align:left; color:var(--ink-3); font-weight:500; font-size:.76rem;
border-bottom:2px solid var(--line-strong); padding:8px; }
table.dt td { padding:8px; border-bottom:1px solid var(--line); }
.axis-note { font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:12px; }
.quote { border-left:3px solid var(--chart-blue); background:var(--surface-2);
padding:12px 14px; margin:16px 0 0; font-weight:300; border-radius:0 12px 12px 0; }
.quote .who { display:block; font-size:.74rem; color:var(--ink-3); margin-top:6px; }
footer { margin-top:48px; font-size:.78rem; color:var(--ink-3); font-weight:300; }
footer code { font-size:.74rem; }
@media (max-width:640px) { .fc-kpis { grid-template-columns:1fr; } }
"""


def build_section(ref, d):
    fc = d["forecast"]
    anc = fc["anchor"]
    sc = fc["scenarios"]
    yp = fc["year_path"]
    st = d.get("section_text", {})
    rev_label = d.get("revenue_label", "revenue").capitalize()
    t = ref

    # 1. section-note
    t = re.sub(r'<p class="section-note">.*?</p>',
               f'<p class="section-note">{st["section_note"]}</p>', t, count=1, flags=re.S)
    # 2. anchor sub
    t = re.sub(r'<div class="sub" style="margin-bottom:0;">.*?</div>',
               f'<div class="sub" style="margin-bottom:0;">{st["anchor_sub"]}</div>',
               t, count=1, flags=re.S)
    # 3. KPI tiles
    tiles = []
    for key, cls, col in [("bear", "bear", "var(--bad)"),
                          ("base", "base", "var(--chart-blue-deep)"),
                          ("bull", "bull", "var(--ok)")]:
        s = sc[key]
        tiles.append(f"""    <div class="fc-kpi {cls}">
      <div class="k-label">{key.capitalize()} · FY31E price</div>
      <div class="k-price">₹{fmt_price(s['price_fy31'])}</div>
      <div class="k-row"><span>CAGR <b style="color:{col}">{fmt_cagr(s['cagr'])}</b></span><span>MCap <b>₹{s['mcap_fy31_cr']:,} Cr</b></span></div>
    </div>""")
    t = re.sub(r'<div class="fc-kpis">.*?<div class="fc-note">',
               "<div class=\"fc-kpis\">\n" + "\n".join(tiles) + "\n  </div>\n\n  <div class=\"fc-note\">",
               t, count=1, flags=re.S)
    # 4. fc-note
    t = re.sub(r'<div class="fc-note">.*?</div>',
               f'<div class="fc-note">{st["fc_note"]}</div>', t, count=1, flags=re.S)
    # 5. chart subs (price, mcap in order)
    subs = re.findall(r'<div class="fc-sub">TTM .*? hover for a year readout</div>', t)
    assert len(subs) == 2, f"expected 2 fc-subs, found {len(subs)}"
    t = t.replace(subs[0], f'<div class="fc-sub">{st["price_sub"]}</div>', 1)
    t = t.replace(subs[1], f'<div class="fc-sub">{st["mcap_sub"]}</div>', 1)
    # 6. chart feet (price, mcap in order)
    feet = re.findall(r'<div class="fc-foot"><span>.*?</span><span>.*?</span></div>', t, flags=re.S)
    assert len(feet) == 2, f"expected 2 fc-feet, found {len(feet)}"
    t = t.replace(feet[0],
                  f'<div class="fc-foot"><span>{st["foot_price"][0]}</span><span>{st["foot_price"][1]}</span></div>', 1)
    t = t.replace(feet[1],
                  f'<div class="fc-foot"><span>{st["foot_mcap"][0]}</span><span>{st["foot_mcap"][1]}</span></div>', 1)
    # 7. legend chip labels (price panel carries CAGRs)
    for key, dot in [("bear", "var(--bad)"), ("base", "var(--chart-blue)"), ("bull", "var(--ok)")]:
        pat = re.compile(r'(' + re.escape(f'data-s="{key}" aria-pressed="true"><span class="dot" style="background:{dot}"></span>')
                         + r').*?(</button>)')
        t = pat.sub(rf'\g<1>{key.capitalize()} {fmt_cagr(sc[key]["cagr"])}\g<2>', t, count=1)
    # 8. assumptions table
    rows = []
    rows.append(f'    <tr><td><strong>{rev_label} CAGR (5y)</strong></td><td>{rev_of(sc["bear"])[0]}%</td><td>{rev_of(sc["base"])[0]}%</td><td>{rev_of(sc["bull"])[0]}%</td></tr>')
    rows.append(f'    <tr><td><strong>FY31 {rev_label.lower()}</strong></td><td>₹{rev_of(sc["bear"])[1]:,} Cr</td><td>₹{rev_of(sc["base"])[1]:,} Cr</td><td>₹{rev_of(sc["bull"])[1]:,} Cr</td></tr>')
    rows.append(f'    <tr><td><strong>PAT margin FY31</strong></td><td>{sc["bear"]["pat_margin_fy31"]}%</td><td>{sc["base"]["pat_margin_fy31"]}%</td><td>{sc["bull"]["pat_margin_fy31"]}%</td></tr>')
    rows.append(f'    <tr><td><strong>Exit P/E (FY31)</strong></td><td>{sc["bear"]["exit_pe"]}×</td><td>{sc["base"]["exit_pe"]}×</td><td>{sc["bull"]["exit_pe"]}×</td></tr>')
    rows.append(f'    <tr><td><strong>FY31 EPS</strong></td><td>₹{sc["bear"]["eps_fy31"]}</td><td>₹{sc["base"]["eps_fy31"]}</td><td>₹{sc["bull"]["eps_fy31"]}</td></tr>')
    rows.append(f'    <tr><td><strong>FY31 price</strong></td><td style="color:var(--bad); font-weight:500;">₹{fmt_price(sc["bear"]["price_fy31"])}</td><td style="color:var(--chart-blue-deep); font-weight:500;">₹{fmt_price(sc["base"]["price_fy31"])}</td><td style="color:var(--ok); font-weight:500;">₹{fmt_price(sc["bull"]["price_fy31"])}</td></tr>')
    rows.append(f'    <tr><td><strong>FY31 MCap</strong></td><td>₹{sc["bear"]["mcap_fy31_cr"]:,} Cr</td><td>₹{sc["base"]["mcap_fy31_cr"]:,} Cr</td><td>₹{sc["bull"]["mcap_fy31_cr"]:,} Cr</td></tr>')
    rows.append(f'    <tr><td><strong>Price CAGR</strong></td><td>{fmt_cagr(sc["bear"]["cagr"], signed=False) if float(sc["bear"]["cagr"]) < 0 else fmt_cagr(sc["bear"]["cagr"])}</td><td>{fmt_cagr(sc["base"]["cagr"])}</td><td>{fmt_cagr(sc["bull"]["cagr"])}</td></tr>')
    table = ('  <table class="dt">\n    <tr><th>Assumption</th><th>Bear</th><th>Base</th><th>Bull</th></tr>\n'
             + "\n".join(rows) + '\n  </table>')
    t = re.sub(r'<table class="dt">.*?</table>', table, t, count=1, flags=re.S)
    # 9. shares note
    t = re.sub(r'<div class="axis-note">Shares flat.*?</div>',
               f'<div class="axis-note">{st["shares_note"]}</div>', t, count=1, flags=re.S)
    # 10. insight quote
    t = re.sub(r'<div class="quote">Key insight:.*?</div>',
               f'<div class="quote">{st["insight"]}</div>', t, count=1, flags=re.S)
    # 11. year path + monitor
    yp_line = (f'Year path (price ₹): Bear {", ".join(map(str, yp["price"]["bear"]))} · '
               f'Base {", ".join(map(str, yp["price"]["base"]))} · '
               f'Bull {", ".join(map(str, yp["price"]["bull"]))}. '
               f'MCap (₹ Cr): Bear {", ".join(map(str, yp["mcap"]["bear"]))} · '
               f'Base {", ".join(map(str, yp["mcap"]["base"]))} · '
               f'Bull {", ".join(map(str, yp["mcap"]["bull"]))}. {st["monitor"]}')
    t = re.sub(r'<div class="axis-note">Year path.*?</div>',
               f'<div class="axis-note">{yp_line}</div>', t, count=1, flags=re.S)
    # 12. JS series (price, mcap in order)
    series = re.findall(r'series: \{ bear: \[.*?\], base: \[.*?\], bull: \[.*?\] \}', t)
    assert len(series) == 2, f"expected 2 CF series, found {len(series)}"
    for kind, ser in zip(["price", "mcap"], series):
        new = (f'series: {{ bear: [{", ".join(map(str, yp[kind]["bear"]))}], '
               f'base: [{", ".join(map(str, yp[kind]["base"]))}], '
               f'bull: [{", ".join(map(str, yp[kind]["bull"]))}] }}')
        t = t.replace(ser, new, 1)
    # 13. ymax/ticks (price, mcap in order)
    scales = re.findall(r'ymax: \d+, ticks: \[.*?\]', t)
    assert len(scales) == 2, f"expected 2 ymax scales, found {len(scales)}"
    ch = d["chart"]
    t = t.replace(scales[0],
                  f'ymax: {ch["price_ymax"]}, ticks: [{", ".join(map(str, ch["price_ticks"]))}]', 1)
    t = t.replace(scales[1],
                  f'ymax: {ch["mcap_ymax"]}, ticks: [{", ".join(map(str, ch["mcap_ticks"]))}]', 1)
    return t


def main():
    ap = argparse.ArgumentParser(description="Render a standalone forecast section")
    ap.add_argument("--company", required=True, help="data/<company>-forecast.json stem")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    dp = DATA / f"{args.company}-forecast.json"
    if not dp.exists():
        sys.exit(f"Not found: {dp} — generate it per SKILL.md Step 2 first")
    d = json.loads(dp.read_text(encoding="utf-8"))
    ref = REF.read_text(encoding="utf-8")
    # strip the extractor's leading provenance comment(s) — reference only, never shipped
    ref = re.sub(r'\A(\s*<!--.*?-->\s*)+', '', ref, flags=re.S)
    section = build_section(ref, d)

    # math checks (Step 4)
    fc, sc = d["forecast"], d["forecast"]["scenarios"]
    for key in ["bear", "base", "bull"]:
        s = sc[key]
        assert abs(s["price_fy31"] * fc["anchor"]["shares_cr"] - s["mcap_fy31_cr"]) / s["mcap_fy31_cr"] < 0.02, \
            f"{key}: price × shares != MCap"
        assert fc["year_path"]["price"][key][-1] == s["price_fy31"], f"{key}: year path != outcome"
        assert fc["year_path"]["price"][key][0] == fc["anchor"]["price"], f"{key}: TTM != anchor"
    print("OK outcomes math (price × shares = MCap, paths end at outcomes)")

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['company']} — 5-year forecast</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<div class="kicker">Filings-based · NSE: {d['nse']} · {args.date}</div>
<h1>{d['company']} — 5-year forecast</h1>
<div class="subtitle">Bear / Base / Bull · Illustrative · not a price target</div>
{section}
<footer>
<p><strong>Method.</strong> {d.get('method', 'Filings-based forecast.')}</p>
<p>Educational only, not investment advice. Illustrative Bear/Base/Bull walk — no price target. Consult a SEBI-registered advisor.</p>
<p>Rendered {args.date} · forecast-overview skill · section 06 reference</p>
</footer>
</div>
</body>
</html>
"""
    slug = d['short'].replace(' ', '')
    out = pathlib.Path(args.out) if args.out else OUT_DIR / f"{slug}-forecast-{args.date}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"WROTE {out} ({len(page):,} chars)")


if __name__ == "__main__":
    main()
