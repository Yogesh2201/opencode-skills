#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Ujjivan SFB Gemini report from template + ujjivan.json (filings-only)."""
import pathlib, json, re

ROOT = pathlib.Path(r"C:\Users\Yogesh Kumar\Downloads\Open_Code")
SKILL = ROOT / ".opencode" / "skill" / "full-overview-2-0"
TPL = SKILL / "templates" / "gemini.template.html"
DATA = SKILL / "data" / "ujjivan.json"
OUT = ROOT / "Company_Overview" / "Final" / "Ujjivan_Gemini-forecast-2026-09-25.html"
DATE = "2026-09-25"

data = json.loads(DATA.read_text(encoding="utf-8"))
t = TPL.read_text(encoding="utf-8")

def between_replace(start_marker, end_marker, new_content):
    global t
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.S)
    replacement = start_marker + "\n" + new_content.strip() + "\n\n" + end_marker
    new_t, n = pattern.subn(replacement, t, count=1)
    if n == 0:
        print(f"WARN not found: {start_marker} -> {end_marker}")
    else:
        t = new_t
        print(f"OK {start_marker} ({len(new_content)} chars)")

meta = data["meta"]; price = data["price"]; k = data["bank_kpis"]
peers = data["peers_sfb"]; prod = data["products"]; vis = data["vision"]
val = data["valuation"]; trends = data["trends"]; bigm = data["big_messages"]
red = data["red_flags"]; bot = data["bottom_line"]; fc = data["forecast"]

# ---- Header ----
t = t.replace("TD Power Systems \u2014 Company Profile \u00b7 Gemini v2 (polished)", "Ujjivan Small Finance Bank \u2014 Company Profile \u00b7 Gemini v2 (bank)")
t = t.replace("TD Power Systems", meta["company"])
t = t.replace("TDPOWERSYS", meta["nse"])
t = t.replace("533553", meta["bse"])
t = t.replace("Dabaspet, Bengaluru", meta["hq"])
t = t.replace("Dabaspet", meta["hq"])
t = re.sub(r'<div class="kicker">.*?</div>', '<div class="kicker">Filings-only \u00b7 NSE: UJJIVANSFB \u00b7 BSE: 542904 \u00b7 Bengaluru</div>', t, count=1, flags=re.S)
t = re.sub(r'<div class="subtitle">.*?</div>', '<div class="subtitle">Mass-market inclusion bank \u2014 <strong>loan book \u20b932,122 Cr \u00b7 deposits \u20b937,630 Cr \u00b7 CASA 25.5%</strong>, <strong>secured 43.5%</strong>, <strong>CRAR 23.1%</strong>. Not a corporate lender. A phygital JLG-to-housing franchise that underwrites aspiration at \u20b951k ticket, then graduates borrowers to secured credit.</div>', t, count=1, flags=re.S)
t = t.replace("20 Sep 2026", "25 Sep 2026")
t = t.replace("2026-09-20", DATE)
t = re.sub(r'<title>.*?</title>', '<title>Ujjivan Small Finance Bank \u2014 Company Profile \u00b7 Gemini v2</title>', t, count=1)
t = t.replace("TD Power Systems \u00b7", "Ujjivan SFB \u00b7")

# ---- KPI ROW ----
kpi_new = """
<div class="kpi-row">
  <div class="tile-hero-ring"><div class="tile" data-tip="Loan book Rs.32,122 Cr (+8% YoY). Secured 43.5% vs 30.2% a year ago (+13.3 ppt) - housing + MSME + vehicle + gold driving the pivot." tabindex="0">
    <div class="label">Loan book</div>
    <div class="value">\u20b932,122 Cr</div>
    <div class="context">+8% YoY \u00b7 secured 43.5% (was 30.2%)</div>
  </div></div>
  <div class="tile" data-tip="Deposits Rs.37,630 Cr (+20% YoY). CASA 25.5% (Rs.9,595 Cr) + retail TD - granular funding with LCR 120%." tabindex="0">
    <div class="label">Deposits & CASA</div>
    <div class="value">\u20b937,630 Cr</div>
    <div class="context">+20% YoY \u00b7 CASA 25.5% \u00b7 LCR 120%</div>
  </div>
  <div class="tile" data-tip="Total income FY25 Rs.7,201 Cr, TTM Rs.8,453 Cr. PPOP Rs.1,690 Cr, PAT FY25 Rs.726 Cr / TTM Rs.906 Cr. NIM 8.8%, RoA 1.6%, RoE 12.4%." tabindex="0">
    <div class="label">Total income TTM</div>
    <div class="value">\u20b98,453 Cr</div>
    <div class="context">PAT TTM \u20b9906 Cr \u00b7 NIM 8.8% \u00b7 RoE 12.4%</div>
  </div>
  <div class="tile" data-tip="Market cap Rs.12,215 Cr at Rs.62.7 (Screener 24 Sep 2026 close). P/E 13.5x, P/B 1.79x, BV Rs.35.1, 52W 43.8-73.9." tabindex="0">
    <div class="label">Market cap</div>
    <div class="value">\u20b912,215 Cr</div>
    <div class="delta">\u20b962.7 \u00b7 P/E 13.5x \u00b7 P/B 1.79x</div>
  </div>
  <div class="tile" data-tip="Resilience: GNPA 2.18%, NNPA 0.49%, PCR 78% + floating provision Rs.181 Cr. CRAR 23.1%. 753 branches, 326 districts, 27 states/UTs." tabindex="0">
    <div class="label">Resilience</div>
    <div class="value">23.1%</div>
    <div class="context">CRAR \u00b7 GNPA 2.18% \u00b7 753 branches</div>
  </div>
</div>
"""
between_replace("<!-- KPI ROW -->", "<!-- 01 WHAT THEY DO -->", kpi_new)

# ---- 01 WHAT THEY DO ----
s01_new = """
<h2 id="s01"><span class="num">01</span> What the company does</h2>
<p class="section-note">Mass-market inclusion, not corporate credit. Ujjivan underwrites <em>aspiration at small ticket</em> (JLG \u20b951k), graduates borrowers to secured credit (housing + MSME), and funds it with granular deposits.</p>

<div class="card">
  <h3>The idea in one line</h3>
  <div class="sub">The business is <strong style="color:var(--ink)">small-ticket credit + phygital collections + granular deposits</strong> sold through 753 branches to borrowers formal credit missed.</div>
  <p style="font-weight:300; line-height:1.65">Ujjivan Small Finance Bank <strong style="font-weight:500">takes deposits in 27 states/UTs and lends to the un-served and under-served \u2014 group JLG micro-loans, individual Vikas loans, affordable housing, MSME, vehicle, gold, agri</strong> \u2014 at tickets from <strong style="font-weight:500">\u20b951k (JLG) to \u20b920L (housing)</strong>. Customers are micro-entrepreneurs, small traders, first-time homeowners, two-wheeler buyers. Revenue is NIM (8.8% FY25) on \u20b932,122 Cr book plus fees (third-party, FIG, treasury). When a vegetable vendor outgrows her \u20b960k JLG loan, Ujjivan graduates her to a \u20b92L Vikas loan, then a housing micro-LAP \u2014 under one balance sheet with CRAR 23.1% that absorbs the MFI cycle.</p>
  <div class="grid-3">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">groups</span> Inclusion engine</div>
      <div style="font-size:.86rem; color:var(--ink-2); font-weight:300; margin-top:6px">JLG + Vikas at <strong style="color:var(--chart-blue-deep)">\u20b951k\u2013\u20b92L</strong> \u2014 joint liability, 12\u201336M tenor, CGFMU covered (~49% of micro).</div>
      <div style="margin-top:10px"><span style="font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px;">Disbursements \u20b923,464 Cr FY25</span></div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">shield</span> Secured pivot</div>
      <div style="font-size:.86rem; color:var(--ink-2); font-weight:300; margin-top:6px"><strong style="color:var(--chart-blue-deep)">30.2% \u2192 43.5% secured in one year</strong> \u2014 housing + MSME + vehicle + gold de-risk the cycle.</div>
      <div style="margin-top:10px"><span style="font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px;">Target 50%+ secured</span></div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">savings</span> Granular funding</div>
      <div style="font-size:.86rem; color:var(--ink-2); font-weight:300; margin-top:6px">Deposits <strong>\u20b937,630 Cr (+20%)</strong> \u2014 CASA 25.5%, retail + CASA \u20b926,676 Cr, LCR 120%.</div>
      <div style="margin-top:10px"><span style="font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px;">700+ outlets \u00b7 Hello Ujjivan app</span></div>
    </div>
  </div>

  <div style="margin-top:20px; background:var(--surface-2); border-radius:var(--r-md); padding:16px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">How value flows \u2014 from saver to borrower</div>
    <div class="flow-3" style="display:grid; grid-template-columns:1fr 1.2fr 1fr; gap:10px; text-align:center; align-items:center;">
      <div style="background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:12px;">
        <div class="msr" style="color:var(--ink-3)">savings</div>
        <div style="font-size:.86rem; font-weight:500; margin-top:4px">Savers</div>
        <div style="font-size:.76rem; color:var(--ink-3); font-weight:300">CASA + retail TD<br>TASC \u00b7 NRI \u00b7 LCR 120%</div>
      </div>
      <div style="background:linear-gradient(135deg, rgba(66,133,244,.08), rgba(155,114,203,.08)); border:1px solid rgba(66,133,244,.14); border-radius:12px; padding:12px;">
        <div class="msr" style="color:var(--chart-blue-deep)">account_balance</div>
        <div style="font-size:.86rem; font-weight:500; color:var(--chart-blue-deep)">Ujjivan SFB</div>
        <div style="font-size:.76rem; color:var(--ink-3); font-weight:300">NIM 8.8% \u00d7 book<br>JLG \u2192 Vikas \u2192 secured</div>
        <div style="margin-top:6px"><span style="font-size:.7rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:3px 8px; color:var(--ink-2)">UNDERWRITING HERE</span></div>
      </div>
      <div style="background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:12px;">
        <div class="msr" style="color:var(--ink-3)">storefront</div>
        <div style="font-size:.86rem; font-weight:500; margin-top:4px">Borrowers</div>
        <div style="font-size:.76rem; color:var(--ink-3); font-weight:300">JLG \u00b7 housing \u00b7 MSME<br>Vehicle \u00b7 gold \u00b7 agri</div>
      </div>
    </div>
    <div style="text-align:center; margin-top:8px; font-size:.72rem; color:var(--ink-3); font-weight:300">Examples: \u20b951k JLG (12\u201324M) \u00b7 Vikas \u20b965k\u2013\u20b92L (24\u201336M) \u00b7 housing \u20b92\u2013\u20b920L (to 180M) \u00b7 2W from 18% p.a. (to 48M)</div>
  </div>

  <div class="money-panel">
    <div class="money-title">Where money comes from \u2014 tap to switch proxy <span class="derived-flag">Segmented view</span></div>
    <div class="money-sub">Book and deposit splits from AR FY25 + BSE Apr-25. These are balance-sheet proxies (not P&amp;L). Inter-segment overlaps mean components are directional.</div>
    <div class="seg" id="seg" role="group" aria-label="Switch money proxy"></div>
    <div class="donutwrap"><div class="donut" id="donut"></div><div class="legend" id="leg"></div></div>
    <div class="money-note" id="donutnote"></div>
    <div class="money-grid">
      <div class="money-mini"><div class="mp-title">Secured pivot in one year</div><div class="mp-sub">Secured 30.2% \u2192 43.5% (+13.3 ppt) \u2014 housing + MSME lead</div><div class="pivot-track" style="margin-top:10px;"><div style="width:30%; background:var(--chart-blue)"></div><div style="width:70%; background:var(--chart-context)"></div></div><div class="pivot-track"><div style="width:44%; background:var(--chart-blue)"></div><div style="width:56%; background:var(--chart-context)"></div></div><div class="mp-sub" style="margin-top:6px;">Top bar FY24 secured \u00b7 bottom bar FY25 secured (blue)</div></div>
      <div class="money-mini"><div class="mp-title">Deposits fund the pivot</div><div class="mp-sub">\u20b937,630 Cr (+20% YoY) \u00b7 CASA 25.5% \u00b7 retail + CASA \u20b926,676 Cr</div><div id="groupedMini" style="margin-top:8px"></div></div>
    </div>
  </div>

  <div class="quote">Business model in one sentence: Ujjivan converts <em>phygital distribution + small-ticket underwriting + granular deposits</em> into <em>resilient, secured-led, inclusion-scale</em> earnings \u2014 the opposite of corporate wholesale banking. Secured mix and CASA carry the margin; collections carry the cycle.<span class="who">\u2014 MD &amp; CEO letter, AR FY25: \u201cSeizing Tomorrow \u2014 building a mass-market bank that earns trust consistently.\u201d</span></div>
</div>
"""
between_replace("<!-- 01 WHAT THEY DO -->", "<!-- 02 COMPETITORS -->", s01_new)

# ---- 02 COMPETITORS ----
bars = ""
for p in peers["peers"]:
    subj = p.get("is_subject", False)
    cls = "purple" if subj else ("emph" if p["share_pct"] > 20 else "dim")
    st = 'style="color:var(--chart-blue-deep); font-weight:500;"' if subj else ""
    vs = 'style="color:var(--chart-blue-deep)"' if subj else 'style="color:var(--ink-3); font-size:.76rem"'
    nm = p["name"] + (" (subject)" if subj else "")
    bars += f'  <div class="bar-row"><span class="cat" {st} data-tip="{p["name"]} \u2014 loan book \u20b9{p["loan_book_cr"]:,} Cr; {p["overlap"]}" tabindex="0">{nm}</span><span class="track"><span class="hairline-grid"></span><span class="fill {cls}" style="width:{p["share_pct"]:.1f}%"></span></span><span class="val"><b>\u20b9{p["loan_book_cr"]:,} Cr</b><br><span {vs}>{p["share_pct"]:.1f}%</span></span></div>\n'

rows = ""
for p in peers["peers"]:
    subj = p.get("is_subject", False)
    nm = f'<strong style="color:var(--chart-blue-deep)">{p["name"]}</strong>' if subj else f'<strong>{p["name"]}</strong>'
    rows += f'        <tr><td>{nm}</td><td>{p["hq"]}</td><td style="text-align:right">\u20b9{p["loan_book_cr"]:,} Cr</td><td style="font-size:.78rem; color:var(--ink-2)">{p["overlap"]}</td></tr>\n'

s02_new = f"""
<h2 id="s02"><span class="num">02</span> Geographical competitors \u2014 loan-book share</h2>
<p class="section-note">One SFB peer-group pot (~\u20b92.75 lakh Cr FY25 gross loan book). Share = loan book \u00f7 sum of this table. All books from filings. Ujjivan is the mass-market inclusion pivot \u2014 not the biggest, but the fastest de-risking.</p>

<div class="card">
  <h3>Peer-group loan-book share \u2014 who lends how much, geographically</h3>
  <div class="sub">Listed SFBs only. Pot = AU + Equitas + Ujjivan + Jana + Utkarsh + ESAF + Suryoday FY25 books. Ujjivan = 11.7% \u2014 #3 by book, #1 by secured-pivot pace.</div>

{bars}  <div class="axis-note">Bars share one linear axis (0 \u2192 ~\u20b91.16 lakh Cr). At true scale AU SFB is 3.6\u00d7 Ujjivan \u2014 but Ujjivan leads on secured-mix velocity (+13.3 ppt in one year) and deposit growth (+20%). <strong style="color:var(--ink); font-weight:500">That\u2019s the point:</strong> book share \u2260 resilience share. Ujjivan\u2019s relevance is <em>secured % \u00d7 CASA \u00d7 PCR</em> through the MFI cycle, not book size.</div>

  <div class="grid-2" style="margin-top:22px;">
    <div style="background:var(--surface-2); border-radius:var(--r-md); padding:14px;">
      <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Detailed table \u2014 geography &amp; overlap</div>
      <table class="dt">
        <tr><th>Peer</th><th>HQ</th><th style="text-align:right">Loan book</th><th>Overlap</th></tr>
{rows}      </table>
    </div>
    <div style="background:var(--surface); border:1px solid var(--line); border-radius:var(--r-md); padding:14px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
      <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; margin-bottom:12px;">
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">Jaipur 42.0%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">Chennai 15.5%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem; color:var(--chart-blue-deep); font-weight:500;">Bengaluru 22.6%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">Varanasi 7.8%</span>
      </div>
      <div style="font-size:.82rem; color:var(--ink-2); font-weight:300; max-width:280px;">Ujjivan shares Bengaluru with Jana \u2014 but competes <strong style="color:var(--ink)">pan-India in micro + housing</strong> (326 districts, 27 states/UTs). HQ is origin, not market.</div>
      <div style="margin-top:10px; font-size:.72rem; color:var(--ink-3);">Map: HQ geography. Peer-group pot geography is what the bar above measures.</div>
    </div>
  </div>
</div>
"""
between_replace("<!-- 02 COMPETITORS -->", "<!-- 03 KEY PRODUCTS -->", s02_new)

# ---- 03 KEY PRODUCTS ----
fam_html = ""
for f in prod["families"]:
    fam_html += f"""    <div class="pcard">
      <div class="picon"><span class="msr">{f["icon"]}</span></div>
      <h4>{f["name"]}</h4>
      <p><strong>{f["ticket"]}</strong> \u2014 {f["desc"]}</p>
      <span class="pill">{f["pill"]}</span>
    </div>
"""
ext_html = ""
for e in prod["extras"]:
    ext_html += f"""    <div class="pcard" style="background:var(--surface-2); box-shadow:none;">
      <div class="picon"><span class="msr">{e["icon"]}</span></div>
      <h4>{e["name"]}</h4>
      <p>{e["desc"]}</p>
    </div>
"""
sp = prod["spectrum"]
fsn = data["financial_snapshot"]
s03_new = f"""
<h2 id="s03"><span class="num">03</span> Key products</h2>
<p class="section-note">Six credit families + three funding/fee verticals. One operating system: small-ticket underwriting + phygital collections + granular deposits. Every product is a relationship \u2014 JLG today, housing tomorrow.</p>

<div class="card">
  <div class="product-grid">
{fam_html}  </div>
  <div style="margin-top:14px" class="product-grid">
{ext_html}  </div>

  <div style="margin-top:18px; background:var(--surface-2); border-radius:var(--r-md); padding:14px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500;">Ticket spectrum \u2014 where each family lives</div>
    <div class="spectrum">
      <div class="sp-1"><b>{sp["min"]}</b><span style="font-size:.68rem; color:var(--ink-3)">inclusion min</span></div>
      <div class="sp-2">{sp["mid1"]}</div>
      <div class="sp-3">{sp["mid2"]}</div>
      <div class="sp-4">{sp["max"]}</div>
    </div>
    <div style="text-align:center; margin-top:6px; font-size:.72rem; color:var(--ink-3); font-weight:300">Graduation path: JLG \u20b951k \u2192 Vikas \u20b92L \u2192 housing/MSME \u20b920L \u2014 ticket rises as credit history seasons.</div>
  </div>

  <div style="margin-top:18px;">
    <h3>Financial snapshot &amp; quality read</h3>
    <div class="sub">TTM to 24 Sep 2026 \u2014 inclusion growth vs cycle: Total Income ~\u20b98,453 Cr TTM on 8.8% NIM. CRAR 23.1% funds the pivot.</div>
    <table class="dt">
      <tr><th>Metric</th><th style="text-align:right">TTM / FY25</th><th style="text-align:right">% MCap</th><th>Read</th></tr>
      <tr><td><strong>Market Cap</strong></td><td style="text-align:right">\u20b912,215 Cr</td><td style="text-align:right">100%</td><td style="color:var(--ink-2)">\u20b962.7 \u00b7 13.5\u00d7 P/E \u00b7 1.79\u00d7 P/B (BV \u20b935.1) \u00b7 52W 43.8\u201373.9</td></tr>
      <tr><td><strong>Total income</strong></td><td style="text-align:right">\u20b98,453 Cr TTM</td><td style="text-align:right">69.2%</td><td style="color:var(--ink-2)">1.44\u00d7 P/S \u2014 FY25 \u20b97,201 Cr \u00b7 NIM 8.8% \u00b7 PPOP \u20b91,690 Cr</td></tr>
      <tr><td><strong>PAT</strong></td><td style="text-align:right">\u20b9906 Cr TTM</td><td style="text-align:right">7.4%</td><td style="color:var(--ink-2)">7.4% earnings yield \u00b7 EPS \u20b94.67 (194.8 Cr shares) \u00b7 FY25 \u20b9726 Cr</td></tr>
      <tr><td><strong>PPOP / Provisions</strong></td><td style="text-align:right">\u20b91,690 Cr / \u20b91,017 Cr</td><td style="text-align:right">\u2014</td><td style="color:var(--ink-2)">Credit cost 2.45% FY25 (incl. \u20b946 Cr accel.) \u00b7 PCR 78%</td></tr>
      <tr><td><strong style="color:var(--chart-blue-deep)">Net worth / CRAR</strong></td><td style="text-align:right; color:var(--chart-blue-deep)">\u20b96,838 Cr / 23.1%</td><td style="text-align:right">56.0%</td><td style="color:var(--chart-blue-deep)">BV \u20b935.1 \u00b7 floating \u20b9181 Cr buffer \u00b7 LCR 120%</td></tr>
    </table>
    <div class="quote warning">\u26a0\ufe0f CYCLE &amp; MARGIN WATCH: GNPA 2.18% / NNPA 0.49% with 56% unsecured \u2014 credit cost 2.45% must normalise as secured crosses 50%; NIM 8.8% compresses toward ~7% on mix shift; C/I 62% must not drift.<span class="who">\u2014 PCR 78% + floating \u20b9181 Cr + CRAR 23.1%. Watch secured % \u00d7 credit cost, not just disbursements.</span></div>
  </div>
</div>
"""
between_replace("<!-- 03 KEY PRODUCTS -->", "<!-- 04 VISION -->", s03_new)

# ---- 04 VISION ----
pil = ""
for p in vis["pillars"]:
    pil += f"""    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">{p["icon"]}</span> {p["label"]}</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">{p["text"]}</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">{p["tag"]}</div>
    </div>
"""
s04_new = f"""
<h2 id="s04"><span class="num">04</span> Company vision</h2>
<p class="section-note">Verbatim from filings, then the funded pillars that make it real.</p>

<div class="card">
  <div class="quote">\u201c{vis["quote"]}\u201d
    <span class="who">\u2014 {vis["quote_source"]}</span>
  </div>

  <div class="grid-4">
{pil}  </div>

  <div style="margin-top:16px; background:linear-gradient(135deg, rgba(66,133,244,.06), rgba(155,114,203,.06)); border:1px solid rgba(66,133,244,.12); border-radius:var(--r-md); padding:14px; text-align:center; font-size:.92rem; font-weight:300; color:var(--ink-2);">
    <span class="msr" style="color:var(--chart-blue-deep)">lightbulb</span> Vision in one line: {vis["oneline"]}
  </div>
</div>
"""
between_replace("<!-- 04 VISION -->", "<!-- 04b VALUATION + DCF -->", s04_new)

# ---- 04b VALUATION ----
tiles = val["tiles"]; _da = val["dcf_assumptions"]; _lc = val["local_crosscheck"]
s04v_new = f"""
<h2 id="s04v"><span class="num">04</span> Valuation + DCF</h2>
<p class="section-note">Read as a system \u2014 AlphaSpread DCF is primary, Multiples is cross-check. Market prices the MFI cycle + secured pivot, not steady-state earnings. Needs secured 50%+ + credit-cost normalisation as CASA deepens.</p>

<div class="card">
  <div class="quote">\u201cOwn the inclusion, but let the cycle give you the price.\u201d \u2014 AlphaSpread intrinsic \u20b9120.48 (+92.1%) vs Multiples \u20b964.69 (fair)
    <span class="who">\u2014 Thesis: 13.5\u00d7 P/E prices the secured pivot + Universal Bank optionality. Bull = secured 50%+ + CGFMU cushion + margin holds near 20%; bear = credit cost stays high + NIM compresses. *Approximate benchmarks. Source: <a href="{val["url"]}" target="_blank">AlphaSpread DCF</a> (7yr Bank template, Rev 14.3%, Margin 21.8\u219219.9%, Discount 10%, Exit 1.8x P/S).</span>
  </div>

  <h3>Valuation multiples \u2014 4 rows only</h3>
  <div class="sub">P/S 1.44\u00d7 (\u20b912,215 / \u20b98,453) lives in Financial snapshot only. Trailing P/E = \u20b912,215 / ~\u20b9906 \u2248 13.5\u00d7. BV \u20b935.1 \u2192 P/B 1.79\u00d7. AlphaSpread DCF is filings + model.</div>
  <table class="dt">
    <tr><th>Metric</th><th style="text-align:right">Value</th><th>Benchmark*</th><th>Read</th></tr>
    <tr><td><strong>Trailing P/E</strong></td><td style="text-align:right">13.5\u00d7</td><td style="color:var(--ink-2)">SFB median ~12\u201318\u00d7* \u00b7 AU ~25\u00d7*</td><td style="color:var(--ok); font-weight:500;">\U0001f7e2 Fair vs cycle</td></tr>
    <tr><td><strong>Forward P/E (FY26E)</strong></td><td style="text-align:right">~12\u00d7</td><td style="color:var(--ink-2)">AlphaSpread exit 1.8x P/S* \u00b7 FY27E EPS \u20b94.85</td><td style="color:var(--warn); font-weight:500;">\U0001f7e1 Watch credit cost</td></tr>
    <tr><td><strong>P/B (BV \u20b935.1)</strong></td><td style="text-align:right">1.79\u00d7</td><td style="color:var(--ink-2)">SFB median ~1.5\u20132.5\u00d7* \u00b7 AU ~3\u00d7*</td><td style="color:var(--ok); font-weight:500;">\U0001f7e2 Backed by 23.1% CRAR</td></tr>
    <tr><td><strong>RoA / RoE</strong></td><td style="text-align:right">1.6% / 12.4%</td><td style="color:var(--ink-2)">SFB median ~1.2% / 12%* \u00b7 FY25</td><td style="color:var(--ok); font-weight:500;">\U0001f7e2 At plan \u2014 must hold</td></tr>
  </table>

  <div class="grid-4">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">\U0001f3af DCF Value</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--chart-blue-deep)">\u20b9{tiles["dcf"]["value"]:.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">7yr Bank \u00b7 10% \u00b7 1.8x P/S \u00b7 +92.1%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">\U0001f4ca Multiples</div>
      <div style="font-size:1.3rem; font-weight:500;">\u20b9{tiles["multiples"]["value"]:.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">P/S,P/E,P/B,Price/Dep \u00b7 +3.2%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">\U0001f48e Intrinsic</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--chart-blue-deep)">\u20b9{tiles["intrinsic"]["value"]:.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">AlphaSpread (DCF) \u00b7 47% undervalued</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">\u2696\ufe0f Buy Zone \u2192</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--ok)">\u20b9{val["buy_zone_20pct"]:.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">20% MOS \u00b7 53.7% above price</div>
    </div>
  </div>

  <div style="margin-top:14px; overflow-x:auto;">
    <table class="dt">
      <tr><th>Approach</th><th style="text-align:right">Value / Share</th><th>vs \u20b962.7</th></tr>
      <tr><td><strong>DCF Value (7yr, 10%, 1.8x P/S) \u2014 AlphaSpread</strong></td><td style="text-align:right">\u20b9{val["dcf_value"]:.2f}</td><td>\U0001f7e2 +92.1%</td></tr>
      <tr><td><strong>Multiples-Based Value \u2014 AlphaSpread</strong></td><td style="text-align:right">\u20b9{val["multiples_value"]:.2f}</td><td>\U0001f7e2 +3.2% (fair)</td></tr>
      <tr><td><strong>Intrinsic Value (Base) \u2014 AlphaSpread</strong></td><td style="text-align:right; color:var(--chart-blue-deep); font-weight:500;">\u20b9{val["intrinsic_value"]:.2f}</td><td>\U0001f7e2 +92.1% (47% undervalued)</td></tr>
      <tr><td><strong>Buy Zone (20% MOS)</strong></td><td style="text-align:right">\u20b9{val["buy_zone_20pct"]:.2f}</td><td>\U0001f3af 53.7% above current</td></tr>
    </table>
  </div>

  <div class="quote">\U0001f4cc METHODOLOGY \u2014 AlphaSpread: 7-year forecast via Bank template, Revenue Growth {_da["revenue_growth"]}% (vs 5Y hist {_da["revenue_growth_5y_hist"]}%, Wall St 3Y {_da["revenue_growth_wallst_3y"]}%), Net Margin {_da["net_margin_start"]}%\u2192{_da["net_margin"]}% (vs 5Y {_da["net_margin_5y_hist"]}%, Wall St 3Y {_da["net_margin_wallst_3y"]}%), Discount Rate {_da["discount_rate"]}%, Exit Multiple {_da["exit_multiple"]}x {_da["exit_multiple_type"]}. Multiples-Based from P/S, P/E, P/B, Price/Deposits etc. vs peers/history. Intrinsic = AlphaSpread selected method (DCF for Ujjivan SFB). History: 41\u201359% undervaluation over 5Y vs 47% today \u2014 in line. <span class="who">\u2014 Source: <a href="{val["url"]}" target="_blank">alphaspread.com/security/nse/ujjivansfb/dcf-valuation</a> + <a href="{val["relative_url"]}" target="_blank">relative-valuation</a>. Price \u20b9{val["price_current"]} (AlphaSpread). Local cross-check: residual \u20b9{_lc["residual_income"]} / Fwd P/E \u20b9{_lc["forward_pe"]} / Fwd P/B \u20b9{_lc["forward_pb"]} \u2192 blended \u20b9{_lc["blended_local"]} \u2014 more conservative on NIM + credit cost.</span></div>

  <div class="val-visual">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500;">\U0001f4c8 Valuation bar \u2014 intrinsic \u20b9120.48 (+92.1%) \u00b7 DCF \u20b9120.48 \u00b7 Multiples \u20b964.69 \u00b7 buy \u20b996.38</div>
    <div style="display:flex; justify-content:space-between; font-size:.72rem; color:var(--ink-3); margin-top:8px; flex-wrap:wrap; gap:6px;"><span>LOW \u20b936</span><span>CURRENT \u20b962.7</span><span>BUY \u20b996.38</span><span>IV \u20b9120.48</span><span>DCF \u20b9120.48</span><span>MULT \u20b964.69</span></div>
    <div class="bar-track"><div class="bar-fill" style="width:68%"></div></div>
    <div class="bar-marks"><span>\u20b936</span><span>IV \u20b9120.48</span><span>\u20b9130</span></div>
    <div style="font-size:.78rem; color:var(--ink-2); margin-top:8px; font-weight:300;">Intrinsic <strong style="color:var(--ink)">\u20b9120.48</strong> \u2014 47% undervalued \u2014 price <strong style="color:var(--ink)">\u20b962.7</strong> sits below buy <strong style="color:var(--ink)">\u20b996.38</strong> (already in buy zone per AlphaSpread). DCF \u20b9120.48 = margin holds near 20% on Bank template; Multiples \u20b964.69 = fairly valued vs history \u2014 watch NIM \u00d7 credit cost.</div>
    <div style="font-size:.72rem; color:var(--ink-3); margin-top:6px;">Bear FY31 36.4 \u00b7 Base 107.9 \u00b7 Bull 197.6 \u00b7 Shares 194.8 Cr (FV \u20b910) \u00b7 Valuation via AlphaSpread \u00b7 Price Sep 24 close \u20b962.7 (AlphaSpread \u20b964.21)</div>
  </div>
</div>
"""
between_replace("<!-- 04b VALUATION + DCF -->", "<!-- 05 TRENDS -->", s04v_new)

# ---- 05 TRENDS ----
tabs_html = ""
for i, tr in enumerate(trends):
    sel = "true" if i == 0 else "false"
    tabs_html += f'    <button class="trend-tab" role="tab" id="tt{i+1}" aria-selected="{sel}" aria-controls="tp" data-t="{i}"><span class="msr">{tr["icon"]}</span>{i+1} \u00b7 {tr["kick"].split(chr(183))[-1].strip() if chr(183) in tr["kick"] else tr["kick"]}</button>\n'

msg_html = ""
for m in bigm:
    msg_html += f"""      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">{m["icon"]}</span> {m["label"]}</div>
        <div style="font-size:.86rem; margin-top:4px; font-weight:300;">{m["text"]}</div>
        <div style="margin-top:6px; font-size:.72rem; color:var(--ink-3);">{m["source"]}</div>
      </div>
"""
flag_rows = ""
for j, f in enumerate(red["flags"]):
    sev = "\U0001f534 High" if f["severity"] == "HIGH" else "\U0001f7e1 Med"
    flag_rows += f'      <tr><td><strong>{j+1}</strong></td><td><strong>{f["id"].title()}</strong></td><td>{sev}</td><td style="color:var(--ink-2)">{f["evidence"]}</td></tr>\n'
flag_tiles = ""
for f in red["flags"]:
    sev_cls = "high" if f["severity"] == "HIGH" else "med"
    sev_tx = "\U0001f534 HIGH" if f["severity"] == "HIGH" else "\U0001f7e1 MEDIUM"
    lab = f["id"].replace(" ", "<br>")
    flag_tiles += f'      <div class="flag"><b>{lab}</b><span class="sev {sev_cls}">{sev_tx}</span></div>\n'

bl = bot
s05_new = f"""
<h2 id="s05"><span class="num">05</span> Key trends &amp; big messages</h2>
<p class="section-note">What AR FY25 and BSE filings say is moving the book \u2014 and what management repeats in every filing. Filings-only.</p>

<div class="card">
  <h3>Five trends the filings name \u2014 and the management line on each</h3>
  <div class="sub">Each card is one filed trend + the big message underneath. Sources: AR FY25 MD letter + BSE 30-Apr-2025 results.</div>

  <div class="trend-tabs" role="tablist" aria-label="Key trends">
{tabs_html}  </div>

  <div class="trend-panel" id="tp" role="tabpanel" aria-live="polite">
    <div class="tp-kicker" id="tpKicker"></div>
    <h4 id="tpTitle"></h4>
    <p class="tp-body" id="tpBody"></p>
    <div><span class="tp-cta" id="tpCta"></span></div>
    <div class="trend-nav">
      <span class="tp-count" id="tpCount">1 / 5</span>
      <span class="tp-btns">
        <button class="tp-arrow" id="tpPrev" aria-label="Previous trend"><span class="msr">chevron_left</span></button>
        <button class="tp-arrow" id="tpNext" aria-label="Next trend"><span class="msr">chevron_right</span></button>
      </span>
    </div>
  </div>

  <div style="margin-top:18px; background:linear-gradient(135deg, rgba(66,133,244,.06), rgba(155,114,203,.06)); border:1px solid rgba(66,133,244,.12); border-radius:var(--r-md); padding:16px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Big messages \u2014 what management repeats in every filing</div>
    <div class="msg-3">
{msg_html}    </div>
  </div>

  <div style="margin-top:18px;">
    <h3>Red flags \u2014 {red["summary"]}</h3>
    <div class="sub">Severity: HIGH breaks thesis \u00b7 MEDIUM pressures it. At 13.5\u00d7 P/E the cycle is already half-priced \u2014 any GNPA miss compresses quickly.</div>
    <table class="dt">
      <tr><th>#</th><th>Red flag</th><th>Severity</th><th>Evidence</th></tr>
{flag_rows}    </table>
    <div class="flag-grid">
{flag_tiles}    </div>
    <div style="text-align:center; margin-top:8px; font-size:.72rem; color:var(--ink-3); font-weight:500; letter-spacing:.07em;">{red["summary"]}</div>
  </div>

  <div style="margin-top:18px; background:linear-gradient(135deg, rgba(66,133,244,.06), rgba(155,114,203,.06)); border:1px solid rgba(66,133,244,.12); border-radius:var(--r-md); padding:16px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Bottom line \u2014 six lenses</div>
    <div class="msg-3">
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">\U0001f9e0 Core idea</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">{bl["core_idea"]}</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">\U0001f504 What changed</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">{bl["what_changed"]}</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">\U0001f440 Hidden insight</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">{bl["hidden_insight"]}</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">\u26a0\ufe0f What breaks</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">{bl["what_breaks"]}</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">\u2753 Open question</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">{bl["open_question"]}</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">\U0001f3af Takeaway</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">{bl["takeaway"]}</div>
      </div>
    </div>
  </div>
</div>
"""
between_replace("<!-- 05 TRENDS -->", "<!-- 06 FORECAST -->", s05_new)

# ---- 06 FORECAST ----
sc = fc["scenarios"]; yp = fc["year_path"]
s06_new = f"""
<h2 id="s06"><span class="num">06</span> 5-year forecast \u2014 illustrative scenarios</h2>
<p class="section-note">Total income \u2192 PAT margin \u2192 EPS \u2192 P/E \u2192 Price \u2192 MCap (bank earnings path; balance-sheet CRAR 23.1% gives buffer, no dilution assumed). Anchor is TTM Sep-26. Hover a chart to read any year. Illustrative \u00b7 not advice / not a price target.</p>

<div class="card">
  <div class="fc-head">
    <div>
      <h3 style="margin-bottom:4px;">FY31E outcomes <span class="derived-flag">Illustrative \u00b7 not advice</span></h3>
      <div class="sub" style="margin-bottom:0;">Anchor: \u20b9{fc["anchor"]["price"]} \u00b7 MCap \u20b9{fc["anchor"]["mcap_cr"]:,} Cr \u00b7 shares ~{fc["anchor"]["shares_cr"]} Cr \u00b7 Total income \u20b9{fc["anchor"]["total_income_ttm_cr"]:,} Cr TTM (FY25 \u20b9{fc["anchor"]["total_income_fy25_cr"]:,} Cr) \u00b7 EPS \u20b9{fc["anchor"]["eps_ttm"]} \u00b7 P/E {fc["anchor"]["pe"]}\u00d7 \u00b7 P/B {fc["anchor"]["pb"]}\u00d7</div>
    </div>
    <span class="fc-badge">5-yr horizon</span>
  </div>

  <div class="fc-kpis">
    <div class="fc-kpi bear">
      <div class="k-label">Bear \u00b7 FY31E price</div>
      <div class="k-price">\u20b9{sc["bear"]["price_fy31"]}</div>
      <div class="k-row"><span>CAGR <b style="color:var(--bad)">{sc["bear"]["cagr"]}%</b></span><span>MCap <b>\u20b9{sc["bear"]["mcap_fy31_cr"]:,} Cr</b></span></div>
    </div>
    <div class="fc-kpi base">
      <div class="k-label">Base \u00b7 FY31E price</div>
      <div class="k-price">\u20b9{sc["base"]["price_fy31"]}</div>
      <div class="k-row"><span>CAGR <b style="color:var(--chart-blue-deep)">+{sc["base"]["cagr"]}%</b></span><span>MCap <b>\u20b9{sc["base"]["mcap_fy31_cr"]:,} Cr</b></span></div>
    </div>
    <div class="fc-kpi bull">
      <div class="k-label">Bull \u00b7 FY31E price</div>
      <div class="k-price">\u20b9{sc["bull"]["price_fy31"]}</div>
      <div class="k-row"><span>CAGR <b style="color:var(--ok)">+{sc["bull"]["cagr"]}%</b></span><span>MCap <b>\u20b9{sc["bull"]["mcap_fy31_cr"]:,} Cr</b></span></div>
    </div>
  </div>

  <div class="fc-note">Bank analogue: <strong style="color:var(--ink)">credit cost + NIM + secured mix + the P/E the market grants</strong>. Total-income CAGR matters less than whether credit cost normalises under 2% as secured crosses 50%. Base 18% tracks deposit +21% Jun-26 then sustains on housing + MSME scale-up, not JLG volume alone.</div>

  <div class="fc-stack" style="margin-top:18px;">
    <div class="fc-panel" data-fc="price">
      <div class="fc-head">
        <div>
          <div class="fc-title">Stock price \u2014 5 years (\u20b9)</div>
          <div class="fc-sub">TTM \u20b962.7 \u2192 FY31E \u00b7 hover for a year readout</div>
        </div>
      </div>
      <div class="fc-legend" role="group" aria-label="Toggle scenarios on the price chart">
        <button class="fc-chip" data-s="bear" aria-pressed="true"><span class="dot" style="background:var(--bad)"></span>Bear {sc["bear"]["cagr"]}%</button>
        <button class="fc-chip" data-s="base" aria-pressed="true"><span class="dot" style="background:var(--chart-blue)"></span>Base +{sc["base"]["cagr"]}%</button>
        <button class="fc-chip" data-s="bull" aria-pressed="true"><span class="dot" style="background:var(--ok)"></span>Bull +{sc["bull"]["cagr"]}%</button>
      </div>
      <div class="fc-plot"><div class="fc-tip" aria-hidden="true"></div></div>
      <div class="fc-foot"><span>\u20b9 per share \u00b7 shares flat ~194.8 Cr (no dilution)</span><span>dashed = today \u20b962.7</span></div>
    </div>

    <div class="fc-panel" data-fc="mcap">
      <div class="fc-head">
        <div>
          <div class="fc-title">Market cap \u2014 5 years (\u20b9 Cr)</div>
          <div class="fc-sub">TTM \u20b912,215 Cr \u2192 FY31E \u00b7 hover for a year readout</div>
        </div>
      </div>
      <div class="fc-legend" role="group" aria-label="Toggle scenarios on the market cap chart">
        <button class="fc-chip" data-s="bear" aria-pressed="true"><span class="dot" style="background:var(--bad)"></span>Bear</button>
        <button class="fc-chip" data-s="base" aria-pressed="true"><span class="dot" style="background:var(--chart-blue)"></span>Base</button>
        <button class="fc-chip" data-s="bull" aria-pressed="true"><span class="dot" style="background:var(--ok)"></span>Bull</button>
      </div>
      <div class="fc-plot"><div class="fc-tip" aria-hidden="true"></div></div>
      <div class="fc-foot"><span>MCap = price \u00d7 ~194.8 Cr shares</span><span>Base 1.7\u00d7 in 5y on earnings + hold ~9.8\u00d7 P/E</span></div>
    </div>
  </div>

  <div style="margin-top:20px; overflow-x:auto;">
  <table class="dt">
    <tr><th>Assumption</th><th>Bear</th><th>Base</th><th>Bull</th></tr>
    <tr><td><strong>Total income CAGR (5y)</strong></td><td>{sc["bear"]["total_income_cagr"]}%</td><td>{sc["base"]["total_income_cagr"]}%</td><td>{sc["bull"]["total_income_cagr"]}%</td></tr>
    <tr><td><strong>FY31 total income</strong></td><td>\u20b9{sc["bear"]["total_income_fy31_cr"]:,} Cr</td><td>\u20b9{sc["base"]["total_income_fy31_cr"]:,} Cr</td><td>\u20b9{sc["bull"]["total_income_fy31_cr"]:,} Cr</td></tr>
    <tr><td><strong>PAT margin FY31</strong></td><td>{sc["bear"]["pat_margin_fy31"]}%</td><td>{sc["base"]["pat_margin_fy31"]}%</td><td>{sc["bull"]["pat_margin_fy31"]}%</td></tr>
    <tr><td><strong>Exit P/E (FY31)</strong></td><td>{sc["bear"]["exit_pe"]}\u00d7</td><td>{sc["base"]["exit_pe"]}\u00d7</td><td>{sc["bull"]["exit_pe"]}\u00d7</td></tr>
    <tr><td><strong>FY31 EPS</strong></td><td>\u20b9{sc["bear"]["eps_fy31"]}</td><td>\u20b9{sc["base"]["eps_fy31"]}</td><td>\u20b9{sc["bull"]["eps_fy31"]}</td></tr>
    <tr><td><strong>FY31 price</strong></td><td style="color:var(--bad); font-weight:500;">\u20b9{sc["bear"]["price_fy31"]}</td><td style="color:var(--chart-blue-deep); font-weight:500;">\u20b9{sc["base"]["price_fy31"]}</td><td style="color:var(--ok); font-weight:500;">\u20b9{sc["bull"]["price_fy31"]}</td></tr>
    <tr><td><strong>FY31 MCap</strong></td><td>\u20b9{sc["bear"]["mcap_fy31_cr"]:,} Cr</td><td>\u20b9{sc["base"]["mcap_fy31_cr"]:,} Cr</td><td>\u20b9{sc["bull"]["mcap_fy31_cr"]:,} Cr</td></tr>
    <tr><td><strong>Price CAGR</strong></td><td>{sc["bear"]["cagr"]}%</td><td>+{sc["base"]["cagr"]}%</td><td>+{sc["bull"]["cagr"]}%</td></tr>
  </table>
  </div>
  <div class="axis-note">Shares flat at ~194.8 Cr (BV \u20b935.1) \u2014 CRAR 23.1% gives buffer, no dilution assumed (Bull at 25% growth could need capital if loan-book CAGR &gt;20%). Bear = MFI credit cost stays high + NIM compresses to ~8% + derate to 6.8\u00d7. Bull = secured 50%+ + CGFMU cushion + Universal Bank licence optionality, P/E held at 12.1\u00d7.</div>

  <div class="quote">Key insight: the EPS spread (\u20b9{sc["bear"]["eps_fy31"]} \u2192 \u20b9{sc["bull"]["eps_fy31"]}, ~3\u00d7) is smaller than the price spread (\u20b9{sc["bear"]["price_fy31"]} \u2192 \u20b9{sc["bull"]["price_fy31"]}, ~5.4\u00d7). <strong>The multiple does the heavy lifting.</strong> A Bear EPS at Base multiple (\u20b9{sc["bear"]["eps_fy31"]} \u00d7 {sc["base"]["exit_pe"]}\u00d7 \u2248 \u20b9{round(sc["bear"]["eps_fy31"]*sc["base"]["exit_pe"],1)}) still trails a Base EPS at Bear multiple (\u20b9{sc["base"]["eps_fy31"]} \u00d7 {sc["bear"]["exit_pe"]}\u00d7 \u2248 \u20b9{round(sc["base"]["eps_fy31"]*sc["bear"]["exit_pe"],1)}) \u2014 collections first, re-rating second.<span class="who">\u2014 Method note: watch credit cost \u00d7 NIM, not just disbursements.</span></div>
  <div class="axis-note">Year path (price \u20b9): Bear {", ".join(map(str, yp["price"]["bear"]))} \u00b7 Base {", ".join(map(str, yp["price"]["base"]))} \u00b7 Bull {", ".join(map(str, yp["price"]["bull"]))}. MCap (\u20b9 Cr): Bear {", ".join(map(str, yp["mcap"]["bear"]))} \u00b7 Base {", ".join(map(str, yp["mcap"]["base"]))} \u00b7 Bull {", ".join(map(str, yp["mcap"]["bull"]))}. Monitor quarterly: secured % \u00b7 GNPA/credit cost \u00b7 NIM vs 8.8% \u00b7 CASA vs 25.5% \u00b7 P/E vs exit \u00b7 Hello Ujjivan adoption \u00b7 Universal Bank licence clock.</div>
</div>
"""
between_replace("<!-- 06 FORECAST -->", "<!-- TAKEAWAY -->", s06_new)

# ---- JS: money views ----
old_views = """    q1: { label: 'Q1 FY27 inflow', mid: ['93%', 'export'], items: [{ name: 'Export & deemed', val: 93.1, c: 'var(--chart-blue)', x: '\u20b9684 Cr' }, { name: 'Domestic', val: 6.9, c: 'var(--chart-context)', x: '\u20b951 Cr' }], note: 'Q1 FY27 \u20b9734 Cr total \u2014 93% export pivot (accelerating vs FY25 68%).' },
    fy26: { label: 'FY26 inflow', mid: ['79%', 'export'], items: [{ name: 'Export & deemed', val: 79, c: 'var(--chart-blue)', x: '\u2248\u20b91,730 Cr' }, { name: 'Domestic', val: 21, c: 'var(--chart-context)', x: '\u2248\u20b9510 Cr' }], note: 'FY26 inflow \u20b92,238 Cr (full year).' },
    book: { label: 'Order book', mid: ['69.5%', 'export'], items: [{ name: 'Exports', val: 69.5, c: 'var(--chart-blue)', x: '\u20b91,533 Cr' }, { name: 'Domestic', val: 17.9, c: 'var(--chart-context)', x: '\u20b9395 Cr' }, { name: 'Railway', val: 9.6, c: 'var(--ink-3)', x: '\u20b9211 Cr' }, { name: 'Remainder', val: 3.0, c: 'var(--surface-3)', x: '' }], note: 'Book \u20b92,208 Cr at 30 Jun 2026. Railway may overlap with reported export/domestic.' },
    base: { label: 'Installed base', mid: ['8,375', 'units'], items: [{ name: 'Asia', val: 5522, c: 'var(--chart-context)', x: '5,522' }, { name: 'Europe', val: 1556, c: 'var(--chart-blue)', x: '1,556' }, { name: 'N. America', val: 674, c: 'var(--ink-3)', x: '674' }, { name: 'Rest', val: 623, c: 'var(--surface-3)', x: '623' }], note: 'Cumulative since inception \u2014 current flow far more US-weighted.' }"""
new_views = """    q1: { label: 'Loan book mix', mid: ['43.5%', 'secured'], items: [{ name: 'Secured (housing+MSME+vehicle+gold)', val: 43.5, c: 'var(--chart-blue)', x: '\u20b913,973 Cr' }, { name: 'Unsecured (JLG+Vikas)', val: 56.5, c: 'var(--chart-context)', x: '\u20b918,149 Cr' }], note: 'Mar-25 \u20b932,122 Cr \u2014 secured 43.5% vs 30.2% a year ago (+13.3 ppt). Target 50%+.' },
    fy26: { label: 'Deposits mix', mid: ['25.5%', 'CASA'], items: [{ name: 'CASA', val: 25.5, c: 'var(--chart-blue)', x: '\u20b99,595 Cr' }, { name: 'Retail TD', val: 45.4, c: 'var(--chart-context)', x: '\u20b917,081 Cr' }, { name: 'Bulk TD', val: 29.1, c: 'var(--ink-3)', x: '\u20b910,954 Cr' }], note: 'Deposits \u20b937,630 Cr (+20% YoY) \u2014 retail + CASA \u20b926,676 Cr, LCR 120%.' },
    book: { label: 'Income mix', mid: ['8,453', 'total Cr'], items: [{ name: 'Net interest (NIM 8.8%)', val: 78, c: 'var(--chart-blue)', x: '~78%' }, { name: 'Fees + treasury + FIG', val: 22, c: 'var(--chart-context)', x: '~22%' }], note: 'Total income TTM \u20b98,453 Cr (FY25 \u20b97,201 Cr) \u2014 NII carries, fees diversify.' },
    base: { label: 'Branch footprint', mid: ['753', 'branches'], items: [{ name: 'Karnataka + TN + WB (core)', val: 45, c: 'var(--chart-blue)', x: '~339' }, { name: 'Rest 24 states/UTs', val: 55, c: 'var(--chart-context)', x: '~414' }], note: '753 branches, 326 districts, 27 states/UTs, 24,903 staff \u2014 phygital (Hello Ujjivan + video KYC).' }"""
if old_views in t:
    t = t.replace(old_views, new_views)
    print("OK money views JS")
else:
    print("WARN money views pattern not found")

old_grouped = "    const data = [{ k: 'Export', a: 257, b: 684 }, { k: 'Domestic', a: 135, b: 51 }];"
new_grouped = "    const data = [{ k: 'Deposits', a: 31374, b: 37630 }, { k: 'CASA', a: 8326, b: 9595 }];"
if old_grouped in t:
    t = t.replace(old_grouped, new_grouped)
    t = t.replace("const max = 750;", "const max = 40000;")
    print("OK groupedMini JS")

# ---- JS: trends ----
trends_js_new = "const trends = [\n"
for tr in trends:
    b = tr["body"].replace("'", "\\'")
    trends_js_new += f"    {{ kick: '{tr['kick']}', icon: '{tr['icon']}', h: '{tr['title']}', b: '{b}', c: '{tr['cta']}', cls: '{tr['cls']}' }},\n"
trends_js_new += "  ];"
t = re.sub(r"const trends = \[.*?Trend 5.*?\];", trends_js_new, t, flags=re.S, count=1)
print("OK trends JS")

# ---- JS: forecast + header-toggle scripts (deleted by s06 replace; restore from template with Ujjivan series) ----
_tpl = TPL.read_text(encoding="utf-8")
_a = _tpl.find("/* 06 Forecast")
_b = _tpl.find("/* Header 06")
_c = _tpl.find("</script>", _b)
if _a > 0 and _b > 0 and _c > 0:
    _s = _tpl.rfind("<script>", 0, _a)
    _scripts = _tpl[_s:_c + len("</script>")]
    _scripts = _scripts.replace("series: { bear: [764, 602, 518, 471, 454, 444], base: [764, 834, 923, 1017, 1165, 1315], bull: [764, 975, 1249, 1546, 1936, 2407] }",
              "series: { bear: [62.7, 49.4, 42.5, 38.6, 37.3, 36.4], base: [62.7, 68.4, 75.7, 83.5, 95.6, 107.9], bull: [62.7, 80.0, 102.5, 126.9, 158.9, 197.6] }")
    _scripts = _scripts.replace("series: { bear: [23864, 18808, 16191, 14701, 14180, 13854], base: [23864, 26066, 28835, 31757, 36403, 41060], bull: [23864, 30466, 39029, 48304, 60484, 75190] }",
              "series: { bear: [12215, 9624, 8279, 7520, 7258, 7094], base: [12215, 13332, 14752, 16260, 18629, 21029], bull: [12215, 15586, 19970, 24723, 30953, 38493] }")
    _scripts = _scripts.replace("ymax: 2600, ticks: [0, 500, 1000, 1500, 2000, 2500]", "ymax: 220, ticks: [0, 50, 100, 150, 200]")
    _scripts = _scripts.replace("ymax: 80000, ticks: [0, 20000, 40000, 60000, 80000]", "ymax: 40000, ticks: [0, 10000, 20000, 30000, 40000]")
    t = t.replace("<!-- TAKEAWAY -->", _scripts + "\n\n<!-- TAKEAWAY -->", 1)
    print("OK forecast+header scripts restored")
else:
    print("WARN forecast script block not found in template")

# ---- Takeaway + footer ----
t = re.sub(r'<div class="line">.*?</div>', f'<div class="line">{data["takeaway"]}</div>', t, count=1, flags=re.S)
t = re.sub(r'<p><strong>Method\.</strong>.*?</p>', f'<p><strong>Method.</strong> {data["method_footer"]}</p>', t, count=1, flags=re.S)
t = t.replace("Rendered 2026-09-20", "Rendered 2026-09-25")
t = t.replace("= TDPS (the subject)", "= Ujjivan (the subject)")
t = t.replace("Company-Briefs/2026-09/TD-Power-Systems_September_20_2026.html", "Company_Overview/Final/Ujjivan_Gemini-forecast-2026-09-25.html")
t = t.replace("every figure traced to the filing line; peer % is illustrative of one pot, not a TAM.", "every figure traced to the filing line; peer % is illustrative share of one SFB pot, not a TAM. Educational only, not investment advice. Section 06 is an illustrative Bear/Base/Bull walk \u2014 no price target. Consult a SEBI-registered advisor.")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(t, encoding="utf-8")
print(f"WROTE {OUT} ({len(t):,} chars)")
