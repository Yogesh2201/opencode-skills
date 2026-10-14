#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_maxhealth_full.py — Full Max Healthcare Gemini report with AlphaSpread valuation
Generates Company_Overview/Final/MaxHealthcare_Gemini-forecast-2026-09-25.html
"""
import pathlib, json, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
TPL = ROOT / "templates" / "gemini.template.html"
DATA = ROOT / "data" / "maxhealth.json"
OUT = pathlib.Path.cwd() / "Company_Overview" / "Final" / "MaxHealthcare_Gemini-forecast-2026-09-25.html"

tpl = TPL.read_text(encoding="utf-8")
data = json.loads(DATA.read_text(encoding="utf-8"))

text = tpl
meta = data["meta"]
price = data["price"]
kpis = data["company_kpis"]
peers = data["peers_hospitals"]
products = data["products"]
vision = data["vision"]
valuation = data["valuation"]
trends = data["trends"]
forecast = data["forecast"]

# --- Header ---
text = text.replace("TD Power Systems", meta["company"])
text = text.replace("TDPOWERSYS", meta["nse"])
text = text.replace("533553", meta["bse"])
text = text.replace("Dabaspet, Bengaluru", meta["hq"])
text = re.sub(r'<div class="kicker">.*?</div>', f'<div class="kicker">{meta["kicker"]}</div>', text, count=1, flags=re.S)
text = re.sub(r'<h1>.*?</h1>', f'<h1>{meta["company"]}</h1>', text, count=1, flags=re.S)
text = re.sub(r'<div class="subtitle">.*?</div>', f'<div class="subtitle">India\'s leading quinary care hospital chain — <strong>{kpis["beds"]:,} beds, {kpis["hospitals"]} hospitals</strong>, <strong>ARPOB ₹{kpis["arpob_fy25"]:,}</strong>, <strong>Occupancy {kpis["occupancy_fy25"]}%</strong>, <strong>EBITDA {kpis["ebitda_margin_ttm"]}%</strong>. From single hospital (2001) to 22-hospital network — brownfield ramp + diagnostics + @Home, asset-light growth.</div>', text, count=1, flags=re.S)
text = text.replace("TD Power Systems ·", f"{meta['short']} ·")

# --- KPI row ---
kpi_html = f"""
<div class="kpi-row">
  <div class="tile-hero-ring"><div class="tile" data-tip="Screener TTM: Sales ₹{kpis['sales_ttm_cr']:,} Cr (+16% YoY), OPM {kpis['opm_ttm']}% on ₹{kpis['op_profit_ttm_cr']:,} Cr EBITDA. ARPOB ₹{kpis['arpob_fy25']:,}, occupancy {kpis['occupancy_fy25']}% (+300 bps)." tabindex="0">
    <div class="label">Revenue TTM</div>
    <div class="value">₹{kpis['sales_ttm_cr']:,} Cr</div>
    <div class="context">FY25 ₹{kpis['sales_fy25_cr']:,} Cr · +16% TTM · {kpis['opm_ttm']}% OPM</div>
  </div></div>
  <div class="tile" data-tip="Beds {kpis['beds']:,} across {kpis['hospitals']} hospitals, occupancy {kpis['occupancy_fy25']}% (+300 bps YoY), ARPOB ₹{kpis['arpob_fy25']:,} flat YoY (existing units +7%)." tabindex="0">
    <div class="label">Beds & occupancy</div>
    <div class="value">{kpis['beds']:,}</div>
    <div class="context">{kpis['hospitals']} hospitals · {kpis['occupancy_fy25']}% occ · ARPOB ₹77k</div>
  </div>
  <div class="tile" data-tip="Screener TTM: PAT ₹{kpis['pat_ttm_cr']:,} Cr (+25% YoY), net margin {kpis['net_margin_ttm']}%, ROCE {kpis['roce']}% ROE {kpis['roe']}% D/E {kpis['debt_to_equity']}." tabindex="0">
    <div class="label">PAT TTM</div>
    <div class="value">₹{kpis['pat_ttm_cr']:,} Cr</div>
    <div class="context">FY25 ₹{kpis['pat_fy25_cr']:,} Cr · {kpis['net_margin_ttm']}% margin</div>
  </div>
  <div class="tile" data-tip="Bajaj Broking 18 Sep 2026: Price ₹{price['current']:,} (High {price['high_52w']} / Low {price['low_52w']}), MCap ~₹{price['mcap_cr']:,} Cr, P/E {price['pe_ttm']}x, P/B {price['pb']}x (BV ₹{price['bv']}), 52W." tabindex="0">
    <div class="label">Market cap</div>
    <div class="value">₹{price['mcap_cr']:,} Cr</div>
    <div class="delta">₹{price['current']:,} · P/E {price['pe_ttm']}×</div>
  </div>
  <div class="tile" data-tip="ET Money: ROCE {kpis['roce']}% ROE {kpis['roe']}% D/E {kpis['debt_to_equity']}, EBITDA margin {kpis['ebitda_margin_ttm']}% — capital discipline at premium multiple." tabindex="0">
    <div class="label">Returns</div>
    <div class="value">{kpis['roce']}% / {kpis['roe']}%</div>
    <div class="context">ROCE / ROE · D/E {kpis['debt_to_equity']}</div>
  </div>
</div>"""
text = re.sub(r'<div class="kpi-row">.*?</div>\s*</div>\s*</div>\s*<!-- 01', kpi_html + '\n\n<!-- 01', text, count=1, flags=re.S)
if 'Revenue TTM' not in text:
    text = re.sub(r'<div class="kpi-row">.*?<h2 id="s01">', kpi_html + '\n\n<h2 id="s01">', text, count=1, flags=re.S)

# Fix nav
if 'id="hdrFcToggle"' not in text:
    text = text.replace('<a class="chip-jump" href="#s04">04 Vision</a>\n    <a class="chip-jump" href="#s05">05 Trends</a>', '<a class="chip-jump" href="#s04">04 Vision</a>\n    <a class="chip-jump" href="#s04v">04 Valuation</a>\n    <a class="chip-jump" href="#s05">05 Trends</a>\n    <span style="width:1px; height:18px; background:var(--line); margin:0 2px 0 6px; flex:none; display:inline-block;"></span>\n    <div id="hdrFcToggle" style="display:inline-flex; align-items:center; gap:5px; background:var(--surface-2); border:1px solid var(--line); border-radius:var(--r-pill); padding:3px 4px 3px 10px; white-space:nowrap; flex:none;">\n      <span style="font-size:.68rem; font-weight:600; letter-spacing:.07em; color:var(--ink-3);">06 FC</span>\n      <button type="button" class="hfc-chip" data-hfc="bear" aria-pressed="true" title="Toggle Bear scenario" style="font:inherit; font-size:.70rem; font-weight:600; border:1px solid var(--line); background:var(--bad); color:#fff; padding:4px 9px; border-radius:var(--r-pill); cursor:pointer; line-height:1;">Bear</button>\n      <button type="button" class="hfc-chip" data-hfc="base" aria-pressed="true" title="Toggle Base scenario" style="font:inherit; font-size:.70rem; font-weight:600; border:1px solid var(--chart-blue); background:var(--chart-blue); color:#fff; padding:4px 9px; border-radius:var(--r-pill); cursor:pointer; line-height:1;">Base</button>\n      <button type="button" class="hfc-chip" data-hfc="bull" aria-pressed="true" title="Toggle Bull scenario" style="font:inherit; font-size:.70rem; font-weight:600; border:1px solid var(--ok); background:var(--ok); color:#fff; padding:4px 9px; border-radius:var(--r-pill); cursor:pointer; line-height:1;">Bull</button>\n    </div>')

# Write minimal for now, then do full replacements for remaining sections via file write
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(text, encoding="utf-8")
print(f"Wrote KPI + header -> {OUT} len {len(text)}")

# For remaining sections, we will do a second pass that replaces each major section with hospital-specific HTML
# To keep token low, we will now patch the file in place for 02,03,04,04v,05,06
# 02 Peers
peers_html_bars = ""
for p in peers["peers"]:
    is_subject = p.get("is_subject", False)
    cls = "purple" if is_subject else ("emph" if p["share_pct"] > 20 else "dim")
    style = f'color:var(--chart-blue-deep); font-weight:500;' if is_subject else ""
    val_style = f'color:var(--chart-blue-deep)' if is_subject else "color:var(--ink-3); font-size:.76rem"
    peers_html_bars += f'  <div class="bar-row"><span class="cat" {"style=\"" + style + "\"" if is_subject else ""} data-tip="{p["name"]} — MCap ₹{p["mcap_cr"]:,} Cr; {p["overlap"]}" tabindex="0">{p["name"]} · {p["hq"]}</span><span class="track"><span class="hairline-grid"></span><span class="fill {cls}" style="width:{p["share_pct"]:.1f}%"></span></span><span class="val"><b{" style=\"" + val_style + "\"" if is_subject else ""}>₹{p["mcap_cr"]:,} Cr</b><br><span style="{val_style}">{p["share_pct"]:.1f}%</span></span></div>\n'

peers_table_rows = ""
for p in peers["peers"][:5]:
    peers_table_rows += f'        <tr><td><strong{" style=\"color:var(--chart-blue-deep)\"" if p.get("is_subject") else ""}>{p["name"]}</strong></td><td>{p["hq"]}</td><td style="text-align:right">₹{p["mcap_cr"]:,} Cr</td><td style="font-size:.78rem; color:var(--ink-2)">{p["overlap"]}</td></tr>\n'

s02_html = f"""
<h2 id="s02"><span class="num">02</span> Hospital peers — market-cap share</h2>
<p class="section-note">One listed hospital pot (~₹2.85 lakh Cr market cap, Sep 2026). Share = MCap ÷ sum of this table. All figures from filings / screener. Revenue TTM shown for context.</p>
<div class="card">
  <h3>Peer-group market-cap share — who is how big</h3>
  <div class="sub">Listed hospitals only. Pot ~₹2.85 lakh Cr. Max is North-heavy, high ARPOB; Apollo is pan-India + pharmacy.</div>
{peers_html_bars}
  <div class="axis-note">Bars share one linear axis (0 → ~₹1.1 lakh Cr). <strong style="color:var(--ink); font-weight:500">That’s the point:</strong> MCap ≠ bed count. Max’s relevance is <em>quinary + brownfield ramp</em>, not share of pot.</div>
  <div class="grid-2" style="margin-top:22px;">
    <div style="background:var(--surface-2); border-radius:var(--r-md); padding:14px;">
      <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Detailed table — hospital peers</div>
      <table class="dt">
        <tr><th>Peer</th><th>HQ</th><th style="text-align:right">MCap</th><th>Overlap</th></tr>
{peers_table_rows}
      </table>
    </div>
    <div style="background:var(--surface); border:1px solid var(--line); border-radius:var(--r-md); padding:14px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
      <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; margin-bottom:12px;">
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">Apollo 29.8%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem; color:var(--chart-blue-deep); font-weight:500;">Max 35.7%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">Fortis 11.2%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">Narayana 9.8%</span>
      </div>
      <div style="font-size:.82rem; color:var(--ink-2); font-weight:300; max-width:280px;">All hospitals headquartered in India but serve <strong style="color:var(--ink)">pan-India quinary</strong> — Max 22 hospitals, Apollo pan-India. HQ is legacy, not market.</div>
    </div>
  </div>
</div>
"""
# Replace s02 block
text = OUT.read_text(encoding="utf-8")
text = re.sub(r'<h2 id="s02">.*?</div>\s*</div>\s*\n\n<!-- 03', s02_html + '\n\n<!-- 03', text, count=1, flags=re.S)
OUT.write_text(text, encoding="utf-8")
print(f"Patched s02 -> len {len(text)}")

# 03 Products
products_grid = ""
for fam in products["families"]:
    products_grid += f"""    <div class="pcard">
      <div class="picon"><span class="msr">{fam["icon"]}</span></div>
      <h4>{fam["name"]}</h4>
      <p>{fam["desc"]}</p>
      <span class="pill">{fam["pill"]}</span>
    </div>
"""
extras_grid = ""
for extra in products["extras"]:
    extras_grid += f"""    <div class="pcard" style="background:var(--surface-2); box-shadow:none;">
      <div class="picon"><span class="msr">{extra["icon"]}</span></div>
      <h4>{extra["name"]}</h4>
      <p>{extra["desc"]}</p>
    </div>
"""

# Financial snapshot for Max
fs = f"""
  <div style="margin-top:18px;">
    <h3>Financial snapshot & quality read</h3>
    <div class="sub">TTM to 18 Sep 2026 — hospital growth vs premium: Sales ₹{kpis['sales_ttm_cr']:,} Cr TTM on {kpis['opm_ttm']}% OPM. ROCE {kpis['roce']}% at premium multiple.</div>
    <table class="dt">
      <tr><th>Metric</th><th style="text-align:right">TTM / FY25</th><th style="text-align:right">% MCap</th><th>Read</th></tr>
      <tr><td><strong>Market Cap</strong></td><td style="text-align:right">₹{price['mcap_cr']:,} Cr</td><td style="text-align:right">100%</td><td style="color:var(--ink-2)">₹{price['current']:,} · {price['pe_ttm']}× P/E · {price['pb']}× P/B (BV ₹{price['bv']}) · 52W {price['low_52w']}–{price['high_52w']}</td></tr>
      <tr><td><strong>Sales (Revenue)</strong></td><td style="text-align:right">₹{kpis['sales_ttm_cr']:,} Cr</td><td style="text-align:right">8.6%</td><td style="color:var(--ink-2)">11.7× P/S — quinary ARPOB ₹{kpis['arpob_fy25']:,} · {kpis['opm_ttm']}% OPM</td></tr>
      <tr><td><strong>PAT</strong></td><td style="text-align:right">₹{kpis['pat_ttm_cr']:,} Cr</td><td style="text-align:right">1.4%</td><td style="color:var(--ink-2)">1.4% earnings yield · EPS ₹{price['eps_ttm']} (97.33 Cr shares) · PAT FY25 ₹{kpis['pat_fy25_cr']:,} Cr</td></tr>
      <tr><td><strong>EBITDA / OPM</strong></td><td style="text-align:right">₹{kpis['op_profit_ttm_cr']:,} Cr / {kpis['opm_ttm']}%</td><td style="text-align:right">—</td><td style="color:var(--ink-2)">EBITDA margin {kpis['ebitda_margin_ttm']}% · occupancy {kpis['occupancy_fy25']}%</td></tr>
      <tr><td><strong style="color:var(--chart-blue-deep)">Net worth / D/E</strong></td><td style="text-align:right; color:var(--chart-blue-deep)">₹8,936 Cr / {kpis['debt_to_equity']}</td><td style="text-align:right">8.8%</td><td style="color:var(--chart-blue-deep)">ROCE {kpis['roce']}% ROE {kpis['roe']}% — brownfield, not leverage</td></tr>
    </table>
    <div class="quote" style="border-left-color:var(--warn); background:#fffbeb; border:1px solid #fde68a; border-left:3px solid var(--warn);">⚠️ PREMIUM & OCCUPANCY: P/E {price['pe_ttm']}×, P/B {price['pb']}× — premium to hospitals; <strong>occupancy {kpis['occupancy_fy25']}% must hold with new beds</strong> and ARPOB ₹{kpis['arpob_fy25']:,} must not dilute. EBITDA {kpis['ebitda_margin_ttm']}% must hold as Dwarka/Lucknow ramp.<span class="who">— ROCE {kpis['roce']}% · D/E {kpis['debt_to_equity']} — watch occupancy × ARPOB, not just bed adds.</span></div>
  </div>"""

s03_html = f"""
<h2 id="s03"><span class="num">03</span> Key products</h2>
<p class="section-note">Six clinical families + diagnostics/home care/international. One quinary core. Every product is a system — team + technology + post-acute — tailored to case.</p>
<div class="card">
  <div class="product-grid">
{products_grid}
  </div>
  <div style="margin-top:14px" class="product-grid">
{extras_grid}
  </div>
  <div style="margin-top:18px; background:var(--surface-2); border-radius:var(--r-md); padding:14px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500;">Case spectrum — where each family lives</div>
    <div class="spectrum">
      <div class="sp-1"><b>Diagnostics</b><span style="font-size:.68rem; color:var(--ink-3)">Max Lab</span></div>
      <div class="sp-2">Day Care<br><span style="font-size:.68rem; color:var(--ink-3)">@Home</span></div>
      <div class="sp-3">Elective</div>
      <div class="sp-4">Transplants → Cardiac/Onco/Neuro</div>
    </div>
    <div style="text-align:center; margin-top:6px; font-size:.72rem; color:var(--ink-3); font-weight:300">Case mix is payer-driven (self-pay 66% vs institutional); quinary share drives ARPOB.</div>
  </div>
{fs}
</div>
"""
text = OUT.read_text(encoding="utf-8")
text = re.sub(r'<h2 id="s03">.*?<div style="margin-top:18px; background:var\(--surface-2\); border-radius:var\(--r-md\); padding:14px;">.*?MVA spectrum.*?</div>\s*</div>\s*\n\n<h2 id="s04">', s03_html + '\n\n<h2 id="s04">', text, count=1, flags=re.S)
# Fallback broader
if '<h2 id="s03"><span class="num">03</span> Key products</h2>' not in text or 'Cardiac Sciences' not in text:
    text = OUT.read_text(encoding="utf-8")
    text = re.sub(r'<h2 id="s03">.*?</div>\s*\n\n<h2 id="s04"><span class="num">04</span> Company vision', s03_html + '\n\n<h2 id="s04"><span class="num">04</span> Company vision', text, count=1, flags=re.S)
OUT.write_text(text, encoding="utf-8")
print(f"Patched s03 -> len {len(text)}")

# 04 Vision
vision_html = f"""
<h2 id="s04"><span class="num">04</span> Company vision</h2>
<p class="section-note">Verbatim from filings, then the funded pillars that make it real.</p>
<div class="card">
  <div class="quote">“{vision['quote']}”
    <span class="who">— {vision['quote_source']}</span>
  </div>
  <div class="grid-4">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">biotech</span> {vision['pillars'][0]['label']}</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">{vision['pillars'][0]['text']}</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">{vision['pillars'][0]['tag']}</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">apartment</span> {vision['pillars'][1]['label']}</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">{vision['pillars'][1]['text']}</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">{vision['pillars'][1]['tag']}</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">labs</span> {vision['pillars'][2]['label']}</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">{vision['pillars'][2]['text']}</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">{vision['pillars'][2]['tag']}</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">shield</span> {vision['pillars'][3]['label']}</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">{vision['pillars'][3]['text']}</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">{vision['pillars'][3]['tag']}</div>
    </div>
  </div>
  <div style="margin-top:16px; background:linear-gradient(135deg, rgba(66,133,244,.06), rgba(155,114,203,.06)); border:1px solid rgba(66,133,244,.12); border-radius:var(--r-md); padding:14px; text-align:center; font-size:.92rem; font-weight:300; color:var(--ink-2);">
    <span class="msr" style="color:var(--chart-blue-deep)">lightbulb</span> Vision in one line: {vision['oneline']}
  </div>
</div>
"""
text = OUT.read_text(encoding="utf-8")
text = re.sub(r'<h2 id="s04"><span class="num">04</span> Company vision.*?</div>\s*</div>\s*\n\n<!-- 04b', vision_html + '\n\n<!-- 04b', text, count=1, flags=re.S)
if 'Most well regarded' not in text:
    text = OUT.read_text(encoding="utf-8")
    text = re.sub(r'<h2 id="s04">.*?</div>\s*</div>\s*\n\n<h2 id="s04v">', vision_html + '\n\n<h2 id="s04v">', text, count=1, flags=re.S)
OUT.write_text(text, encoding="utf-8")
print(f"Patched s04 vision -> len {len(text)}")

print("s01-s04 patched, next s04v, s05, s06 to be patched in next run")
