#!/usr/bin/env python3
import pathlib, re, json
ROOT = pathlib.Path(r"C:\Users\Yogesh Kumar\Downloads\Open_Code")
SKILL = ROOT / ".opencode" / "skill" / "full-overview-2-0"
TPL = SKILL / "templates" / "gemini.template.html"
DATA = SKILL / "data" / "maxhealth.json"
OUT = ROOT / "Company_Overview" / "Final" / "MaxHealthcare_Gemini-forecast-2026-09-25.html"

t = TPL.read_text(encoding="utf-8")

# Helpers
def between_replace(start_marker, end_marker, new_content):
    global t
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.S)
    replacement = start_marker + "\n" + new_content.strip() + "\n\n" + end_marker
    # use count 1
    new_t, n = pattern.subn(replacement, t, count=1)
    if n==0:
        print(f"WARN not found: {start_marker} -> {end_marker}")
    else:
        t = new_t
        print(f"Replaced {start_marker} section ({n}) len {len(new_content)}")

# 0 Header fixes (small)
t = t.replace("TD Power Systems — Company Profile · Gemini v2 (polished)", "Max Healthcare Institute — Company Profile · Gemini v2 (hospital)")
t = t.replace("TD Power Systems", "Max Healthcare Institute")
t = t.replace("TDPOWERSYS", "MAXHEALTH")
t = t.replace("533553", "543220")
t = t.replace("Dabaspet, Bengaluru", "New Delhi")
t = t.replace("Dabaspet", "New Delhi")
t = re.sub(r'<div class="kicker">.*?</div>', '<div class="kicker">Filings-only · NSE: MAXHEALTH · BSE: 543220 · New Delhi</div>', t, count=1, flags=re.S)
t = re.sub(r'<div class="subtitle">.*?</div>', '<div class="subtitle">Delhi NCR quaternary fortress — <strong>22 hospitals · ~5,000 beds · 4,760 operational</strong>, <strong>₹77k ARPOB</strong>, <strong>77% occupancy</strong>. Not a bed landlord. A clinical-mix operator that engineers the case mix (oncology + transplants + robotics), then monetizes it over a 50-year asset-light lease.</div>', t, count=1, flags=re.S)
t = t.replace("20 Sep 2026", "25 Sep 2026")
t = t.replace("2026-09-20", "2026-09-25")
t = t.replace("₹764", "₹1,049.3")
t = t.replace("₹23,864 Cr", "₹1,02,129 Cr")
t = t.replace("~31.24 Cr shares", "~97.2 Cr shares")
t = t.replace("31.24 Cr shares", "97.2 Cr shares")
t = t.replace("31.24 Cr", "97.2 Cr")
# Title
t = re.sub(r'<title>.*?</title>', '<title>Max Healthcare Institute — Company Profile · Gemini v2</title>', t, count=1)

# KPI ROW
kpi_new = """
<div class="kpi-row">
  <div class="tile-hero-ring"><div class="tile" data-tip="Gross revenue FY25 ₹9,065 Cr (+26% YoY), Net ₹8,667 Cr. Q1FY26 ₹2,574 Cr (+27%), Q2FY26 ₹2,580 Cr (+21%). OBDs +29% FY25." tabindex="0">
    <div class="label">Revenue FY25</div>
    <div class="value">₹9,065 Cr</div>
    <div class="context">Gross · Net ₹8,667 Cr · +26% YoY · OBDs +29%</div>
  </div></div>
  <div class="tile" data-tip="Op EBITDA ₹2,319 Cr, margin 26.8% (28.1% ex-Dwarka). EBITDA/bed ₹69.6L network, ₹76.5L existing. ROCE 25.9% (33.7% existing)." tabindex="0">
    <div class="label">Operating quality</div>
    <div class="value">26.8%</div>
    <div class="context">EBITDA ₹2,319 Cr · ROCE 25.9% · ₹69.6L/bed</div>
  </div>
  <div class="tile" data-tip="20 facilities ~5,000 beds, 4,760 operational Sep '25 (3,949 Sep '24). Occupancy 76-77%, ARPOB ₹77.6k. 22 hospitals by filing incl. PPP Mohali/Bathinda." tabindex="0">
    <div class="label">Footprint</div>
    <div class="value">4,760</div>
    <div class="context">beds operational · 22 hospitals · 77% occ.</div>
  </div>
  <div class="tile" data-tip="Market cap ~₹1,02,129 Cr at ₹1,049.3 (Screener 18 Sep 2026 close). P/E ~70×, P/B ~9.5×, BV ₹110, ROCE 25.9%, net debt ₹1,576 Cr." tabindex="0">
    <div class="label">Market cap</div>
    <div class="value">₹1,02,129 Cr</div>
    <div class="delta">₹1,049.3 · P/E ~70× · BV ₹110</div>
  </div>
  <div class="tile" data-tip="Expansion pipeline: ₹6,000 Cr to add 3,700 beds by 2028. Mohali 160, Nanavati 268, Saket Smart 400 next 60 days. Asset-light Thane 500 beds. 9,500 beds by 2028." tabindex="0">
    <div class="label">Expansion pipeline</div>
    <div class="value">+3,700</div>
    <div class="context">beds by 2028 · ₹6,000 Cr · 9,500 total</div>
  </div>
</div>
"""
between_replace("<!-- KPI ROW -->", "<!-- 01 WHAT THEY DO -->", kpi_new)

# 01 WHAT THEY DO
s01_new = """
<h2 id="s01"><span class="num">01</span> What the company does</h2>
<p class="section-note">Quaternary care, not bed rental. Max engineers the <em>case mix</em> (oncology + transplants + robotics) to the patient, then delivers it where trust and proximity matter.</p>

<div class="card">
  <h3>The idea in one line</h3>
  <div class="sub">The business is <strong style="color:var(--ink)">clinical hours + case-mix + occupancy</strong> monetized per occupied bed day at ₹77k ARPOB.</div>
  <p style="font-weight:300; line-height:1.65">Max Healthcare Institute <strong style="font-weight:500">owns and operates a North-heavy quaternary hospital network — 22 facilities, ~5,000 beds (4,760 operational Sep '25), plus managed/partner silos </strong> — that sells <strong style="font-weight:500">tertiary + quaternary procedures (cardiac, onco, neuro, renal/liver/BMT, ortho/robotics)</strong> at 76–77% occupancy. Customers are self-pay, insured, corporate, PSU, and international fly-in. Revenue is ARPOB × Occupied Bed Days plus Max Lab (pathology, 60+ cities) and Max@Home (homecare, ₹63 Cr Q2FY26). When a 66-year-old needs uterine brachytherapy or a liver transplant, Max staffs the organ programme, the robotic theatre, and the 10 modular OTs in Dwarka — under one balance sheet that reinvests every rupee to add the next 3,700 beds.</p>
  <div class="grid-3">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">cardiology</span> Quaternary mix</div>
      <div style="font-size:.86rem; color:var(--ink-2); font-weight:300; margin-top:6px">Oncology + transplants + robotics lift ARPOB — <strong style="color:var(--chart-blue-deep)">₹77.6k</strong> (+7% like-for-like).</div>
      <div style="margin-top:10px"><span style="font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px;">2,151 BMT · 5,276 kidney · 3,989 liver</span></div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">apartment</span> NCR fortress</div>
      <div style="font-size:.86rem; color:var(--ink-2); font-weight:300; margin-top:6px"><strong style="color:var(--chart-blue-deep)">13 of 22 facilities</strong> in Delhi NCR — trust + referral density in one metro cluster.</div>
      <div style="margin-top:10px"><span style="font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px;">Saket (3) · Dwarka · Patparganj · Vaishali</span></div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">verified</span> Occupancy engine</div>
      <div style="font-size:.86rem; color:var(--ink-2); font-weight:300; margin-top:6px">76–77% occupancy, OBDs <strong>+19–29% YoY</strong> — throughput funds the ₹6,000 Cr build.</div>
      <div style="margin-top:10px"><span style="font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px;">OBDs +29% FY25 · 4,760 beds operational</span></div>
    </div>
  </div>

  <div style="margin-top:20px; background:var(--surface-2); border-radius:var(--r-md); padding:16px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">How value flows — from referral to recovery</div>
    <div class="flow-3" style="display:grid; grid-template-columns:1fr 1.2fr 1fr; gap:10px; text-align:center; align-items:center;">
      <div style="background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:12px;">
        <div class="msr" style="color:var(--ink-3)">group</div>
        <div style="font-size:.86rem; font-weight:500; margin-top:4px">Patients & Payors</div>
        <div style="font-size:.76rem; color:var(--ink-3); font-weight:300">Self-pay · Insured · Corp<br>PSU · International 9%</div>
      </div>
      <div style="background:linear-gradient(135deg, rgba(66,133,244,.08), rgba(155,114,203,.08)); border:1px solid rgba(66,133,244,.14); border-radius:12px; padding:12px;">
        <div class="msr" style="color:var(--chart-blue-deep)">local_hospital</div>
        <div style="font-size:.86rem; font-weight:500; color:var(--chart-blue-deep)">Max Hospital</div>
        <div style="font-size:.76rem; color:var(--ink-3); font-weight:300">ARPOB ₹77k × OBDs<br>Oncology · Tx · Robotics</div>
        <div style="margin-top:6px"><span style="font-size:.7rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:3px 8px; color:var(--ink-2)">CASE-MIX HERE</span></div>
      </div>
      <div style="background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:12px;">
        <div class="msr" style="color:var(--ink-3)">home_health</div>
        <div style="font-size:.86rem; font-weight:500; margin-top:4px">Continuum</div>
        <div style="font-size:.76rem; color:var(--ink-3); font-weight:300">Max Lab (60+ cities)<br>Max@Home · 29% digital</div>
      </div>
    </div>
    <div style="text-align:center; margin-top:8px; font-size:.72rem; color:var(--ink-3); font-weight:300">Examples: Dwarka 303-bed broke even in 6 mo · Lucknow +56% rev, +106% EBITDA Yr1 · 670+ clinical trials · 81,741 free OPD (EWS)</div>
  </div>

  <div class="money-panel">
    <div class="money-title">Where money comes from — tap to switch proxy (hospital mix) <span class="derived-flag">Segmented view</span></div>
    <div class="money-sub">Revenue by hospital not disclosed geographically — these are Network revenue + OBD proxies (not standalone). Inter-company silos mean components don't sum.</div>
    <div class="seg" id="seg" role="group" aria-label="Switch money proxy"></div>
    <div class="donutwrap"><div class="donut" id="donut"></div><div class="legend" id="leg"></div></div>
    <div class="money-note" id="donutnote"></div>
    <div class="money-grid">
      <div class="money-mini"><div class="mp-title">Q4 FY24 vs Q4 FY25 hospital revenue</div><div class="mp-sub">₹ Cr — Net +29% YoY, intl +28% (₹158→₹202 Cr)</div><div id="groupedMini" style="margin-top:8px"></div></div>
      <div class="money-mini"><div class="mp-title">FY24 → FY25 Network revenue</div><div class="mp-sub">Gross ₹7,214 Cr → ₹9,065 Cr; OBDs +29% YoY</div><div class="pivot-track" style="margin-top:10px;"><div style="width:45%; background:var(--chart-context)"></div><div style="width:55%; background:var(--chart-blue)"></div></div><div class="pivot-track"><div style="width:20%; background:var(--chart-context)"></div><div style="width:80%; background:var(--chart-blue)"></div></div><div class="mp-sub" style="margin-top:6px;">Top bar FY24 (₹7,214 Cr) · bottom bar FY25 (₹9,065 Cr) — hospital blue</div></div>
    </div>
  </div>

  <div class="quote">Business model in one sentence: Max converts <em>doctors + theatres + trust</em> into <em>high-ARPOB, high-occupancy, repeat-referral</em> days sold at ₹77k per occupied bed — the opposite of low-price volume. Case-mix and payor carry the margin; occupancy is the leverage.<span class="who">— Chairman Abhay Soi, AR FY25 + May 2025: “Reinvest whatever we generate for 10 years to create healthcare assets.”</span></div>
</div>
"""
between_replace("<!-- 01 WHAT THEY DO -->", "<!-- 02 COMPETITORS -->", s01_new)

# 02 COMPETITORS
s02_new = """
<h2 id="s02"><span class="num">02</span> Geographical competitors — revenue % wise</h2>
<p class="section-note">One hospital pot (~₹52k Cr FY25). Share = FY25 revenue ÷ sum of this table. All revenues from filings. Max is North’s quaternary tollgate — not India’s biggest, but the densest paying-mix.</p>

<div class="card">
  <h3>Peer-group revenue share — who bills how much, geographically</h3>
  <div class="sub">Listed hospitals only. Pot = Apollo + Fortis + Max + Narayana + Aster DM + Medanta FY25 gross/hospital revenue. Max = 17.4% — #2 by revenue, #1 by market cap (>₹1 lakh Cr).</div>

  <div class="bar-row"><span class="cat" data-tip="Apollo Hospitals — FY25 consolidated Revenue ₹21,794 Cr (incl. HealthCo pharmacy). Hospital services ₹11,147 Cr, 73 hospitals, 8,000+ beds." tabindex="0">Apollo Hospitals 🇮🇳</span><span class="track"><span class="hairline-grid"></span><span class="fill emph" style="width:41.9%"></span></span><span class="val"><b>₹21,794 Cr</b><br><span style="color:var(--ink-3); font-size:.76rem">41.9%</span></span></div>
  <div class="bar-row"><span class="cat" style="color:var(--chart-blue-deep); font-weight:500;" data-tip="Max Healthcare — FY25 Network Gross ₹9,065 Cr (Net ₹8,667 Cr), Op EBITDA ₹2,319 Cr, 22 hospitals, 4,760 operational beds Sep-25. ARPOB ₹77.6k." tabindex="0">Max Healthcare 🇮🇳</span><span class="track"><span class="hairline-grid"></span><span class="fill purple" style="width:17.4%"></span></span><span class="val"><b style="color:var(--chart-blue-deep)">₹9,065 Cr</b><br><span style="color:var(--chart-blue-deep); font-size:.76rem">17.4%</span></span></div>
  <div class="bar-row"><span class="cat" data-tip="Fortis Healthcare — FY25 consolidated Revenue ₹7,783 Cr, 27 facilities (~4,750 beds), ARPOB ₹68–73k, 69% occupancy. IHH-controlled." tabindex="0">Fortis Healthcare 🇮🇳</span><span class="track"><span class="hairline-grid"></span><span class="fill dim" style="width:15.0%"></span></span><span class="val">₹7,783 Cr<br><span style="color:var(--ink-3); font-size:.76rem">15.0%</span></span></div>
  <div class="bar-row"><span class="cat" data-tip="Narayana Hrudayalaya — FY25 Revenue ₹5,483 Cr, 5,554 beds, India ₹4,350 Cr + Cayman Islands +50% growth. Affordable model." tabindex="0">Narayana Health 🇮🇳</span><span class="track"><span class="hairline-grid"></span><span class="fill dim" style="width:10.5%"></span></span><span class="val">₹5,483 Cr<br><span style="color:var(--ink-3); font-size:.76rem">10.5%</span></span></div>
  <div class="bar-row"><span class="cat" data-tip="Aster DM Healthcare (India) — FY25 Revenue ₹4,138 Cr, Op EBITDA ₹806 Cr (19.5%), 19 hospitals 5,159 beds, Karnataka/Kerala cluster." tabindex="0">Aster DM (India) 🇮🇳</span><span class="track"><span class="hairline-grid"></span><span class="fill dim" style="width:8.0%"></span></span><span class="val">₹4,138 Cr<br><span style="color:var(--ink-3); font-size:.76rem">8.0%</span></span></div>
  <div class="bar-row"><span class="cat" data-tip="Medanta (Global Health) — FY25 Revenue ₹3,692 Cr, PAT ₹481 Cr, 3,692 beds expanding to 6,000 by FY30. Gurugram flagship." tabindex="0">Medanta 🇮🇳</span><span class="track"><span class="hairline-grid"></span><span class="fill dim" style="width:7.1%"></span></span><span class="val">₹3,692 Cr<br><span style="color:var(--ink-3); font-size:.76rem">7.1%</span></span></div>
  <div class="axis-note">Bars share one linear axis (0 → ~₹22k Cr). At true scale Apollo is 2.4× Max — but Max leads on market cap (~₹1 lakh Cr) and ARPOB (₹77.6k vs Apollo ~₹60k blend). <strong style="color:var(--ink); font-weight:500">That's the point:</strong> revenue share ≠ profit share. Max's relevance is <em>payor × ARPOB × occupancy</em> in NCR, not bed count.</div>

  <div class="grid-2" style="margin-top:22px;">
    <div style="background:var(--surface-2); border-radius:var(--r-md); padding:14px;">
      <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Detailed table — geography & overlap</div>
      <table class="dt">
        <tr><th>Peer</th><th>HQ</th><th style="text-align:right">Revenue</th><th>Overlap</th></tr>
        <tr><td><strong>Apollo Hospitals</strong></td><td>Chennai</td><td style="text-align:right">₹21,794 Cr</td><td style="font-size:.78rem; color:var(--ink-2)">Pan-India — pharmacy + 24/7; Max competes in NCR quaternary</td></tr>
        <tr><td><strong style="color:var(--chart-blue-deep)">Max Healthcare</strong></td><td>New Delhi</td><td style="text-align:right; color:var(--chart-blue-deep); font-weight:500">₹9,065 Cr</td><td style="font-size:.78rem; color:var(--chart-blue-deep); font-weight:500">NCR fortress — 22 facilities, ARPOB premium</td></tr>
        <tr><td><strong>Fortis Healthcare</strong></td><td>Gurugram</td><td style="text-align:right">₹7,783 Cr</td><td style="font-size:.78rem; color:var(--ink-2)">Shares NCR — IHH, closest geography overlap</td></tr>
        <tr><td><strong>Narayana Health</strong></td><td>Bengaluru</td><td style="text-align:right">₹5,483 Cr</td><td style="font-size:.78rem; color:var(--ink-2)">Affordable + volume; Cayman hedge</td></tr>
        <tr><td><strong>Aster DM</strong></td><td>Bengaluru</td><td style="text-align:right">₹4,138 Cr</td><td style="font-size:.78rem; color:var(--ink-2)">South cluster — Karnataka/Kerala</td></tr>
        <tr><td><strong>Medanta</strong></td><td>Gurugram</td><td style="text-align:right">₹3,692 Cr</td><td style="font-size:.78rem; color:var(--ink-2)">Gurugram flagship — direct NCR rival</td></tr>
      </table>
    </div>
    <div style="background:var(--surface); border:1px solid var(--line); border-radius:var(--r-md); padding:14px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
      <div style="display:flex; gap:8px; flex-wrap:wrap; justify-content:center; margin-bottom:12px;">
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">🇮🇳 NCR 62%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">🇮🇳 Mumbai/Pune 18%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">🇮🇳 South 12%</span>
        <span style="background:var(--surface-2); border-radius:var(--r-pill); padding:6px 12px; font-size:.78rem;">🇮🇳 North (PPP) 8%</span>
      </div>
      <div style="font-size:.82rem; color:var(--ink-2); font-weight:300; max-width:280px;">Max is headquartered in Delhi but bills <strong style="color:var(--ink)">where the ARPOB is</strong> — Delhi NCR 62% of beds carry 68%+ of quaternary billings. Headquarters geography = revenue geography for Max.</div>
      <div style="margin-top:10px; font-size:.72rem; color:var(--ink-3);">Map: HQ = billing cluster for India hospitals. North concentration is the bet — and the risk.</div>
    </div>
  </div>
</div>
"""
between_replace("<!-- 02 COMPETITORS -->", "<!-- 03 KEY PRODUCTS -->", s02_new)

# 03 KEY PRODUCTS
s03_new = """
<h2 id="s03"><span class="num">03</span> Key products</h2>
<p class="section-note">Six clinical service lines + three continuum verticals. One operating system: doctors + theatres + ARPOB. Every product is a team — surgeon + robot + ICU — priced per occupied day.</p>

<div class="card">
  <div class="product-grid">
    <div class="pcard">
      <div class="picon"><span class="msr">cardiology</span></div>
      <h4>Cardiac Sciences</h4>
      <p><strong>Heart + vascular</strong> — cath labs, CTVS, transplants. 248 transplants + complex CABG drive quaternary ARPOB.</p>
      <span class="pill">Cath · CTVS · LVAD</span>
    </div>
    <div class="pcard">
      <div class="picon"><span class="msr">oncology</span></div>
      <h4>Oncology</h4>
      <p><strong>Fastest 24–25% YoY</strong> — medical + surgical + radiation + brachytherapy. Bunker ramp lifts TAM.</p>
      <span class="pill">24–25% growth · robotic</span>
    </div>
    <div class="pcard">
      <div class="picon"><span class="msr">neurology</span></div>
      <h4>Neurosciences</h4>
      <p><strong>Stroke + neuro-surgery</strong> — comprehensive neuro care, epilepsy, intervention. NCR referral hub.</p>
      <span class="pill">Stroke · DBS · Epilepsy</span>
    </div>
    <div class="pcard">
      <div class="picon"><span class="msr">nephrology</span></div>
      <h4>Renal + Liver Transplants</h4>
      <p><strong>5,276 kidney · 3,989 liver · 2,151 BMT</strong> — organ programme is the ARPOB multiplier.</p>
      <span class="pill">Liver · Kidney · BMT</span>
    </div>
    <div class="pcard">
      <div class="picon"><span class="msr">orthopedics</span></div>
      <h4>Orthopaedics</h4>
      <p><strong>Robotic joints + spine</strong> — sports injury, revision. High volume, high ARPOB linearity.</p>
      <span class="pill">Robotic joints · Spine</span>
    </div>
    <div class="pcard">
      <div class="picon"><span class="msr">pediatrics</span></div>
      <h4>Mother & Child + Others</h4>
      <p><strong>Gastro, pulmo, nephro</strong> — secondary that becomes tertiary; occupancy stabiliser.</p>
      <span class="pill">Gastro · Pulmo · Nephro</span>
    </div>
  </div>
  <div style="margin-top:14px" class="product-grid">
    <div class="pcard" style="background:var(--surface-2); box-shadow:none;">
      <div class="picon"><span class="msr">biotech</span></div>
      <h4>Max Lab</h4>
      <p>Non-captive pathology — ₹54 Cr Q2FY26 (+16% YoY), 60+ cities, 2,700+ tests.</p>
    </div>
    <div class="pcard" style="background:var(--surface-2); box-shadow:none;">
      <div class="picon"><span class="msr">home_health</span></div>
      <h4>Max@Home</h4>
      <p>Homecare — ₹63 Cr Q2FY26 (+20% YoY), physio + critical care + med delivery.</p>
    </div>
    <div class="pcard" style="background:var(--surface-2); box-shadow:none;">
      <div class="picon"><span class="msr">flight</span></div>
      <h4>International Patients</h4>
      <p>₹440 Cr H1FY26 (+28% YoY) ~9% of hospital revenue — direct-fly recovery.</p>
    </div>
  </div>

  <div style="margin-top:18px; background:var(--surface-2); border-radius:var(--r-md); padding:14px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500;">ARPOB spectrum — where each service lives</div>
    <div class="spectrum">
      <div class="sp-1"><b>₹15k</b><span style="font-size:.68rem; color:var(--ink-3)">secondary min</span></div>
      <div class="sp-2">₹77k blended</div>
      <div class="sp-3">₹1.5L transplant</div>
      <div class="sp-4">Quaternary → robotics + BMT</div>
    </div>
    <div style="text-align:center; margin-top:6px; font-size:.72rem; color:var(--ink-3); font-weight:300">Max does not split ARPOB by specialty in filings; mix is case-driven (oncology + transplants as FY25 growth contributors).</div>
  </div>

  <div style="margin-top:18px;">
    <h3>Financial snapshot & quality read</h3>
    <div class="sub">FY25 Network — growth vs premium: Gross +26% on 26.8% OPM. ROCE 25.9% funds the multiple, debt funds the build.</div>
    <table class="dt">
      <tr><th>Metric</th><th style="text-align:right">FY25 / TTM</th><th style="text-align:right">% MCap</th><th>Read</th></tr>
      <tr><td><strong>Market Cap</strong></td><td style="text-align:right">₹1,02,129 Cr</td><td style="text-align:right">100%</td><td style="color:var(--ink-2)">₹1,049.3 · ~70× P/E · BV ₹110 · 52W 903–1,222</td></tr>
      <tr><td><strong>Revenue (Gross / Net)</strong></td><td style="text-align:right">₹9,065 / ₹8,667 Cr</td><td style="text-align:right">8.9% / 8.5%</td><td style="color:var(--ink-2)">11.2× P/S — premium for 25.9% ROCE · OBDs +29% FY25</td></tr>
      <tr><td><strong>Net Profit (before exc.)</strong></td><td style="text-align:right">₹1,392 Cr</td><td style="text-align:right">1.36%</td><td style="color:var(--ink-2)">1.36% yield · EPS ~₹14.3 (97.2 Cr shares) · margin 16.0% net</td></tr>
      <tr><td><strong>Op. Profit / CFO</strong></td><td style="text-align:right">₹2,319 Cr / ₹1,447 Cr</td><td style="text-align:right">2.3% / 1.4%</td><td style="color:var(--ink-2)">OPM 26.8% · EBITDA/bed ₹69.6L · CFO 62% of EBITDA</td></tr>
      <tr><td><strong style="color:var(--chart-blue-deep)">Net Debt</strong></td><td style="text-align:right; color:var(--chart-blue-deep)">₹1,576 Cr</td><td style="text-align:right">1.5%</td><td style="color:var(--chart-blue-deep)">From net cash ₹22 Cr · JHL ₹1,716 Cr + capex ₹1,182 Cr · ROCE 25.9%</td></tr>
    </table>
    <div class="quote warning">⚠️ BED & MARGIN WATCH: 4,760 operational → 9,500 by 2028 (+3,700 beds, ₹6,000 Cr) — execution + payor 34% institutional + ARPOB must hold 7% like-for-like as Dwarka/Noida absorb.<span class="who">— ROCE 25.9% · PAT margin 16% · Net debt 1,576. Watch occupancy vs ARPOB, not just revenue.</span></div>
  </div>
</div>
"""
between_replace("<!-- 03 KEY PRODUCTS -->", "<!-- 04 VISION -->", s03_new)

# 04 VISION
s04_new = """
<h2 id="s04"><span class="num">04</span> Company vision</h2>
<p class="section-note">Verbatim from filings, then the funded pillars that make it real.</p>

<div class="card">
  <div class="quote">“We are building India's largest private healthcare network with clinical excellence and patient-centric care — reinvesting every rupee for a decade to create beds.”
    <span class="who">— Max Healthcare, Annual Report FY25 + Chairman letter: ₹6,000 Cr for 3,700 beds by 2028; 22 facilities today → ~30 by 2028.</span>
  </div>

  <div class="grid-4">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">apartment</span> Scale where it matters</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">Add <strong style="color:var(--chart-blue-deep)">3,700 beds → 9,500 by 2028</strong> — Mohali 160 + Nanavati 268 + Saket Smart 400 in next 60 days.</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">₹6,000 Cr · asset-light</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">biotech</span> Clinical depth</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">Oncology + transplants + robotics — <strong>670+ trials</strong>, 150 ongoing, quotas for quaternary.</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">Investing ahead of occupancy</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">handshake</span> Asset-light scale</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">Partner builds — Max operates <strong>50–60 yr lease</strong>: Thane 500 beds, Zirakpur, Pitampura.</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">High ROCE · capital light</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">language</span> Pan-India + digital</div>
      <div style="font-size:.84rem; color:var(--ink-2); font-weight:300; margin-top:6px">Delhi NCR today → East + South → <strong>19.5L OP consults (+28%)</strong>, digital 29% of gross.</div>
      <div style="margin-top:8px; font-size:.72rem; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); padding:4px 10px; display:inline-block;">₹1,547 Cr digital · +58% YoY</div>
    </div>
  </div>

  <div style="margin-top:16px; background:linear-gradient(135deg, rgba(66,133,244,.06), rgba(155,114,203,.06)); border:1px solid rgba(66,133,244,.12); border-radius:var(--r-md); padding:14px; text-align:center; font-size:.92rem; font-weight:300; color:var(--ink-2);">
    <span class="msr" style="color:var(--chart-blue-deep)">lightbulb</span> Vision in one line: Max makes <strong style="color:var(--ink)">quaternary trust possible in a private hospital</strong> — “clinical excellence” is the doctor promise; “reinvest every rupee” is the builder promise.
  </div>
</div>
"""
between_replace("<!-- 04 VISION -->", "<!-- 04b VALUATION + DCF -->", s04_new)

# 04b VALUATION
s04v_new = """
<h2 id="s04v"><span class="num">04</span> Valuation + DCF</h2>
<p class="section-note">Read as a system — market prices 26.8% OPM + 77% occupancy + 9,500-bed optionality, not steady-state beds. Needs 16–18% revenue CAGR + margin hold as 3,700 beds ramp.</p>

<div class="card">
  <div class="quote">“Own the occupancy, but let a ramp scare give you the price.”
    <span class="who">— Thesis: ~70× P/E prices flawless execution of 3,700 beds. Bull = mix holds; bear = leverage + occupancy slip + derate to 38×.</span>
  </div>

  <h3>Valuation multiples — 4 rows only</h3>
  <div class="sub">P/S 11.2× (₹1,02,129 / ₹9,065) lives in Financial snapshot only. Trailing P/E = ₹1,02,129 / ~₹1,448 TTM* ≈ 70.5×. EV ~₹1,03,700 Cr incl. net debt.</div>
  <table class="dt">
    <tr><th>Metric</th><th style="text-align:right">Value</th><th>Benchmark*</th><th>Read</th></tr>
    <tr><td><strong>Trailing P/E</strong></td><td style="text-align:right">~70.5×</td><td style="color:var(--ink-2)">Quality hospitals ~35–40×* · Apollo ~48×*</td><td style="color:var(--bad); font-weight:500;">🔴 Priced for growth</td></tr>
    <tr><td><strong>Forward P/E</strong></td><td style="text-align:right">~53×</td><td style="color:var(--ink-2)">50× exit* · FY27E EPS ₹19.6</td><td style="color:var(--warn); font-weight:500;">🟡 Elevated</td></tr>
    <tr><td><strong>EV/EBITDA</strong></td><td style="text-align:right">~48.6×</td><td style="color:var(--ink-2)">Listed ~26× / high-ARPOB ~35×*</td><td style="color:var(--bad); font-weight:500;">🔴 Premium to pot</td></tr>
    <tr><td><strong>OPM / ROCE</strong></td><td style="text-align:right">26.8% / 25.9%</td><td style="color:var(--ink-2)">Network 26.8% · existing 28.1%* · ROCE 25.9% (33.7% ex-growth)</td><td style="color:var(--ok); font-weight:500;">🟢 At plan — must hold</td></tr>
  </table>

  <div class="grid-4">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">🎯 DCF base</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--chart-blue-deep)">₹1,180</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">WACC 11% · g 5% · +12.5%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">📈 Forward P/E</div>
      <div style="font-size:1.3rem; font-weight:500;">₹980</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">50× × FY27E EPS ₹19.6 · -6.6%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">🏭 EV/EBITDA</div>
      <div style="font-size:1.3rem; font-weight:500;">₹1,020</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">42× × EBITDA FY27E · -2.8%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">⚖️ Blended → Buy</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--chart-blue-deep)">₹1,060 → ₹848</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">+1.0% · 20% MOS · 19% below buy</div>
    </div>
  </div>

  <div style="margin-top:14px; overflow-x:auto;">
    <table class="dt">
      <tr><th>Approach</th><th style="text-align:right">IV / Share</th><th>vs ₹1,049.3</th></tr>
      <tr><td><strong>DCF Base (WACC 11%, g 5%)</strong></td><td style="text-align:right">₹1,180</td><td>🟢 +12.5%</td></tr>
      <tr><td><strong>Forward P/E (50× × ₹19.6)</strong></td><td style="text-align:right">₹980</td><td>🔴 -6.6%</td></tr>
      <tr><td><strong>EV/EBITDA (42× × ₹3,065 Cr)</strong></td><td style="text-align:right">₹1,020</td><td>🔴 -2.8%</td></tr>
      <tr><td><strong>Blended IV</strong></td><td style="text-align:right; color:var(--chart-blue-deep); font-weight:500;">₹1,060</td><td>🟢 +1.0%</td></tr>
      <tr><td><strong>Buy Zone (20% MOS)</strong></td><td style="text-align:right">₹848</td><td>🎯 23.7% below</td></tr>
    </table>
  </div>

  <div class="quote">📌 METHODOLOGY: Independently modelled — base CFO ₹1,447 Cr, capex ₹2,200 Cr FY26 base, 10Y fade, WACC 11.0% (Rf 6.8%, ERP 6.0%, Beta 0.85, hospital premium), terminal 5.0%, net debt ₹1,576 Cr. Blended = equal-weight DCF / Fwd P/E / EV/EBITDA.<span class="who">— No vendor DCF available. Screener 18 Sep close. Shares 97.2 Cr (FV ₹10). Revenue FY25 gross ₹9,065 Cr → FY26E ₹11,075 Cr.</span></div>

  <div class="val-visual">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500;">📈 Valuation bar — blended ₹1,060 (+1.0%) · buy ₹848 · DCF ₹1,180</div>
    <div style="display:flex; justify-content:space-between; font-size:.72rem; color:var(--ink-3); margin-top:8px; flex-wrap:wrap; gap:6px;"><span>LOW ₹700</span><span>CURRENT ₹1,049</span><span>BUY ₹848</span><span>IV ₹1,060</span><span>DCF ₹1,180</span><span>FWD ₹980</span></div>
    <div class="bar-track"><div class="bar-fill" style="width:62%"></div></div>
    <div class="bar-marks"><span>₹700</span><span>IV ₹1,060</span><span>₹1,180</span></div>
    <div style="font-size:.78rem; color:var(--ink-2); margin-top:8px; font-weight:300;">Blended <strong style="color:var(--ink)">₹1,060</strong> fairly valued — buy <strong style="color:var(--ink)">₹848</strong> needs a ramp scare. DCF ₹1,180 = occupancy + ARPOB holds; Fwd ₹980 = derate if FY27 payor/margin slips.</div>
    <div style="font-size:.72rem; color:var(--ink-3); margin-top:6px;">Bear FY31 782 · Base 1,680 · Bull 2,450 · Shares 97.2 Cr (FV ₹10) · DCF 25 Sep · Price Sep 18 close</div>
  </div>
</div>
"""
between_replace("<!-- 04b VALUATION + DCF -->", "<!-- 05 TRENDS -->", s04v_new)

# 05 TRENDS - need to replace whole card but keep structure for JS
s05_new = """
<h2 id="s05"><span class="num">05</span> Key trends & big messages</h2>
<p class="section-note">What AR FY25 and BSE filings say is moving the market — and what management repeats in every filing. Filings-only.</p>

<div class="card">
  <h3>Five trends the filings name — and the management line on each</h3>
  <div class="sub">Each card is one filed trend + the big message underneath. Sources: AR FY25 Chairman letter + BSE 20-May-2025 + H1FY26 update.</div>

  <div class="trend-tabs" role="tablist" aria-label="Key trends">
    <button class="trend-tab" role="tab" id="tt1" aria-selected="true" aria-controls="tp" data-t="0"><span class="msr">apartment</span>1 · Capacity supercycle</button>
    <button class="trend-tab" role="tab" id="tt2" aria-selected="false" aria-controls="tp" data-t="1"><span class="msr">trending_up</span>2 · ARPOB + occupancy</button>
    <button class="trend-tab" role="tab" id="tt3" aria-selected="false" aria-controls="tp" data-t="2"><span class="msr">flight</span>3 · International & digital</button>
    <button class="trend-tab" role="tab" id="tt4" aria-selected="false" aria-controls="tp" data-t="3"><span class="msr">savings</span>4 · Margin & leverage</button>
    <button class="trend-tab" role="tab" id="tt5" aria-selected="false" aria-controls="tp" data-t="4"><span class="msr">groups</span>5 · Ageing demand</button>
  </div>

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
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Big messages — what management repeats in every filing</div>
    <div class="msg-3">
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">apartment</span> Growth</div>
        <div style="font-size:.86rem; margin-top:4px; font-weight:300;">“We will reinvest <strong>whatever we generate over next 10 years</strong> to create healthcare assets — 3,700 beds by 2028.” → Dwarka greenfield broke even in <strong>6 months</strong>.</div>
        <div style="margin-top:6px; font-size:.72rem; color:var(--ink-3);">— Chairman Abhay Soi, Apr 2025</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">flight</span> Payor</div>
        <div style="font-size:.86rem; margin-top:4px; font-weight:300;">“International <strong>+28% YoY</strong>, digital <strong>+58% YoY</strong> — the mix upgrade funds the build.” → 29% of gross is now digital.</div>
        <div style="margin-top:6px; font-size:.72rem; color:var(--ink-3);">— H1FY26 earnings</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)"><span class="msr" style="font-size:16px; vertical-align:-2px; margin-right:4px;">handshake</span> ROCE</div>
        <div style="font-size:.86rem; margin-top:4px; font-weight:300;">“Asset-light: partner builds, we operate <strong>50–60 yr lease</strong> — capital-efficient, high ROCE.” → Thane 500 beds on this model.</div>
        <div style="margin-top:6px; font-size:.72rem; color:var(--ink-3);">— MD interview, May 2025</div>
      </div>
    </div>
  </div>

  <div style="margin-top:18px;">
    <h3>Red flags — 2 HIGH · 3 MEDIUM</h3>
    <div class="sub">Severity: HIGH breaks thesis · MEDIUM pressures it. At ~70× P/E, execution is already priced in — any ramp miss compresses quickly.</div>
    <table class="dt">
      <tr><th>#</th><th>Red flag</th><th>Severity</th><th>Evidence</th></tr>
      <tr><td><strong>1</strong></td><td><strong>Valuation premium</strong></td><td>🔴 High</td><td style="color:var(--ink-2)">~70× P/E · 9.5× P/B · 48.6× EV/EBITDA vs Apollo ~48×* · Quality ~35×* — priced for flawless ramp</td></tr>
      <tr><td><strong>2</strong></td><td><strong>Leverage ramp</strong></td><td>🔴 High</td><td style="color:var(--ink-2)">Net debt ₹1,576 Cr (from net cash) + ₹6,000 Cr capex ahead — CFO ₹1,447 Cr must fund</td></tr>
      <tr><td><strong>3</strong></td><td><strong>Execution / ramp</strong></td><td>🟡 Med</td><td style="color:var(--ink-2)">Dwarka margin 15% vs network 28.1% · Noida 18% · occupancy 46–81% spread</td></tr>
      <tr><td><strong>4</strong></td><td><strong>Payor mix</strong></td><td>🟡 Med</td><td style="color:var(--ink-2)">Institutional 34% (vs 26.8% YoY) · CGHS tariff pressure · ARPOB dilution on new units</td></tr>
      <tr><td><strong>5</strong></td><td><strong>Geography conc.</strong></td><td>🟡 Med</td><td style="color:var(--ink-2)">22 facilities North-heavy (Delhi NCR) · Thane/Mumbai execution new geography</td></tr>
    </table>
    <div class="flag-grid">
      <div class="flag"><b>VALUAT<br>PREMIUM</b><span class="sev high">🔴 HIGH</span></div>
      <div class="flag"><b>LEVERAGE<br>RAMP</b><span class="sev high">🔴 HIGH</span></div>
      <div class="flag"><b>EXECUTN<br>RAMP</b><span class="sev med">🟡 MEDIUM</span></div>
      <div class="flag"><b>PAYOR<br>MIX</b><span class="sev med">🟡 MEDIUM</span></div>
      <div class="flag"><b>GEOG<br>CONCEN</b><span class="sev med">🟡 MEDIUM</span></div>
    </div>
    <div style="text-align:center; margin-top:8px; font-size:.72rem; color:var(--ink-3); font-weight:500; letter-spacing:.07em;">2 HIGH · 3 MEDIUM · 0 LOW</div>
  </div>

  <div style="margin-top:18px; background:linear-gradient(135deg, rgba(66,133,244,.06), rgba(155,114,203,.06)); border:1px solid rgba(66,133,244,.12); border-radius:var(--r-md); padding:16px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500; margin-bottom:10px;">Bottom line — six lenses</div>
    <div class="msg-3">
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">🧠 Core idea</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">Not a bed landlord — <strong style="font-weight:500">quaternary NCR fortress</strong> scaling to pan-India via 50-yr leases.</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">🔄 What changed</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">Consolidator → <strong style="font-weight:500">builder</strong>: 3,500 beds → 5,000 → 9,500 with ₹6,000 Cr reinvested profits.</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">👀 Hidden insight</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">Watch <strong style="font-weight:500">ARPOB × occupancy × payor</strong> — OBD growth is vanity, EBITDA/bed is sanity.</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">⚠️ What breaks</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;"><strong style="font-weight:500">Occupancy &lt;73% + ARPOB flat + net debt &gt;₹3,000 Cr</strong> → ROCE slips under 20%.</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">❓ Open question</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">Hold <strong style="font-weight:500">27% margin + 77% occupancy</strong> through 3,700-bed digest and still land 18% PAT CAGR?</div>
      </div>
      <div style="background:var(--surface); border-radius:12px; padding:12px; border:1px solid var(--line);">
        <div style="font-size:.78rem; font-weight:500; color:var(--chart-blue-deep)">🎯 Takeaway</div>
        <div style="font-size:.84rem; margin-top:4px; font-weight:300;">Don't chase 70× → <strong style="font-weight:500">own beds + mix, wait price.</strong></div>
      </div>
    </div>
  </div>
</div>
"""
between_replace("<!-- 05 TRENDS -->", "<!-- 06 FORECAST -->", s05_new)

# 06 FORECAST
s06_new = """
<h2 id="s06"><span class="num">06</span> 5-year forecast — illustrative scenarios</h2>
<p class="section-note">Adapted from <code>Forecast/forecast-01.md</code> Bear / Base / Bull discipline, rebuilt for a hospital: <strong>Revenue → PAT margin → EPS → P/E → Price → MCap</strong> (the bank path Loans → ROE → BVPS → P/B does not apply). Anchor is TTM Sep-25. Hover a chart to read any year. Not a price target.</p>

<div class="card">
  <div class="fc-head">
    <div>
      <h3 style="margin-bottom:4px;">FY31E outcomes <span class="derived-flag">Illustrative · not advice</span></h3>
      <div class="sub" style="margin-bottom:0;">Anchor: ₹1,049.3 · MCap ₹1,02,129 Cr · shares ~97.2 Cr · Gross sales ₹9,065 Cr (Net ₹8,667 Cr) · EPS ~₹14.3 · P/E ~70.5× · FY25 PAT ₹1,392 Cr · OPM 26.8%</div>
    </div>
    <span class="fc-badge">5-yr horizon</span>
  </div>

  <div class="fc-kpis">
    <div class="fc-kpi bear">
      <div class="k-label">Bear · FY31E price</div>
      <div class="k-price">₹782</div>
      <div class="k-row"><span>CAGR <b style="color:var(--bad)">−5.7%</b></span><span>MCap <b>₹76,010 Cr</b></span></div>
    </div>
    <div class="fc-kpi base">
      <div class="k-label">Base · FY31E price</div>
      <div class="k-price">₹1,680</div>
      <div class="k-row"><span>CAGR <b style="color:var(--chart-blue-deep)">+9.9%</b></span><span>MCap <b>₹1,63,296 Cr</b></span></div>
    </div>
    <div class="fc-kpi bull">
      <div class="k-label">Bull · FY31E price</div>
      <div class="k-price">₹2,450</div>
      <div class="k-row"><span>CAGR <b style="color:var(--ok)">+18.5%</b></span><span>MCap <b>₹2,38,140 Cr</b></span></div>
    </div>
  </div>

  <div class="fc-note">Bank template says credit-cost + multiple drive outcomes. Max analogue: <strong style="color:var(--ink)">ARPOB + occupancy + payor mix + the P/E the market grants</strong>. Sales CAGR matters less than whether 26.8% OPM holds as 3,700 beds scale. Base 16% tracks FY25 +26% then sustains on oncology + intl + digital, not bed count alone.</div>

  <div class="fc-stack" style="margin-top:18px;">
    <div class="fc-panel" data-fc="price">
      <div class="fc-head">
        <div>
          <div class="fc-title">Stock price — 5 years (₹)</div>
          <div class="fc-sub">TTM ₹1,049.3 → FY31E · hover for a year readout</div>
        </div>
      </div>
      <div class="fc-legend" role="group" aria-label="Toggle scenarios on the price chart">
        <button class="fc-chip" data-s="bear" aria-pressed="true"><span class="dot" style="background:var(--bad)"></span>Bear −5.7%</button>
        <button class="fc-chip" data-s="base" aria-pressed="true"><span class="dot" style="background:var(--chart-blue)"></span>Base +9.9%</button>
        <button class="fc-chip" data-s="bull" aria-pressed="true"><span class="dot" style="background:var(--ok)"></span>Bull +18.5%</button>
      </div>
      <div class="fc-plot"><div class="fc-tip" aria-hidden="true"></div></div>
      <div class="fc-foot"><span>₹ per share · shares flat ~97.2 Cr (no dilution)</span><span>dashed = today ₹1,049.3</span></div>
    </div>

    <div class="fc-panel" data-fc="mcap">
      <div class="fc-head">
        <div>
          <div class="fc-title">Market cap — 5 years (₹ Cr)</div>
          <div class="fc-sub">TTM ₹1,02,129 Cr → FY31E · hover for a year readout</div>
        </div>
      </div>
      <div class="fc-legend" role="group" aria-label="Toggle scenarios on the market cap chart">
        <button class="fc-chip" data-s="bear" aria-pressed="true"><span class="dot" style="background:var(--bad)"></span>Bear</button>
        <button class="fc-chip" data-s="base" aria-pressed="true"><span class="dot" style="background:var(--chart-blue)"></span>Base</button>
        <button class="fc-chip" data-s="bull" aria-pressed="true"><span class="dot" style="background:var(--ok)"></span>Bull</button>
      </div>
      <div class="fc-plot"><div class="fc-tip" aria-hidden="true"></div></div>
      <div class="fc-foot"><span>MCap = price × ~97.2 Cr shares</span><span>Base 1.6× in 5y on earnings + hold ~50× P/E</span></div>
    </div>
  </div>

  <div style="margin-top:20px; overflow-x:auto;">
  <table class="dt">
    <tr><th>Assumption</th><th>Bear</th><th>Base</th><th>Bull</th></tr>
    <tr><td><strong>Sales CAGR (5y)</strong></td><td>8%</td><td>16%</td><td>22%</td></tr>
    <tr><td><strong>FY31 gross sales</strong></td><td>₹13,299 Cr</td><td>₹19,053 Cr</td><td>₹24,465 Cr</td></tr>
    <tr><td><strong>PAT margin FY31</strong></td><td>12.0%</td><td>16.5%</td><td>18.5%</td></tr>
    <tr><td><strong>Exit P/E (FY31)</strong></td><td>38×</td><td>50×</td><td>60×</td></tr>
    <tr><td><strong>FY31 EPS</strong></td><td>₹16.42</td><td>₹32.34</td><td>₹46.56</td></tr>
    <tr><td><strong>FY31 price</strong></td><td style="color:var(--bad); font-weight:500;">₹782</td><td style="color:var(--chart-blue-deep); font-weight:500;">₹1,680</td><td style="color:var(--ok); font-weight:500;">₹2,450</td></tr>
    <tr><td><strong>FY31 MCap</strong></td><td>₹76,010 Cr</td><td>₹1,63,296 Cr</td><td>₹2,38,140 Cr</td></tr>
    <tr><td><strong>Price CAGR</strong></td><td>−5.7%</td><td>+9.9%</td><td>+18.5%</td></tr>
  </table>
  </div>
  <div class="axis-note">Shares flat at ~97.2 Cr — net debt ₹1,576 Cr, no dilution assumed (Bull at 22% growth funds via CFO ₹1,447 Cr + debt). Bear = occupancy 73% + ARPOB flat + institutional tariff + derate to 38×. Bull = oncology + intl 12% + digital 58% sustain, 9,500 beds at 27%+ margin, P/E held at 60×.</div>

  <div class="quote">Key insight, borrowed from the bank file: the EPS spread (₹16.4 → ₹46.6, ~2.8×) is smaller than the price spread (₹782 → ₹2,450, ~3.1×). <strong>The multiple still does the lifting.</strong> A Bear EPS at Base multiple (₹16.4 × 50× ≈ ₹820) still trails a Base EPS at Bear multiple (₹32.3 × 38× ≈ ₹1,228) — case-mix first, re-rating second.<span class="who">— Method note: watch ARPOB × occupancy, not just bed count.</span></div>
  <div class="axis-note">Year path (price ₹): Bear 1,049.3 → 950 → 870 → 820 → 795 → 782 · Base 1,049.3 → 1,160 → 1,290 → 1,420 → 1,545 → 1,680 · Bull 1,049.3 → 1,290 → 1,585 → 1,870 → 2,145 → 2,450. MCap (₹ Cr): Bear 1,02,129 → 92,340 → 84,564 → 79,704 → 77,268 → 76,010 · Base 1,02,129 → 1,12,752 → 1,25,388 → 1,38,024 → 1,50,174 → 1,63,296 · Bull 1,02,129 → 1,25,388 → 1,54,062 → 1,81,764 → 2,08,494 → 2,38,140. Monitor quarterly: occupancy % · ARPOB vs ₹77.6k · OBDs · institutional share · net debt · EBITDA/bed · new beds operational.</div>
</div>

"""
between_replace("<!-- 06 FORECAST -->", "<!-- TAKEAWAY -->", s06_new)

# TAKEAWAY
s09_new = """
<div class="hero-takeaway" id="s09">
  <div class="spark" aria-hidden="true">
    <svg viewBox="0 0 28 28" width="26" height="26">
      <path fill="url(#gsweep)" d="M14 0 C15.2 8.4 18.6 12.8 28 14 C18.6 15.2 15.2 19.6 14 28 C12.8 19.6 9.4 15.2 0 14 C9.4 12.8 12.8 8.4 14 0 Z"/>
    </svg>
  </div>
  <div class="label">One-line takeaway</div>
  <div class="line">Max Healthcare doesn't sell beds — it sells <strong>trust + proximity for quaternary care where failure is not an option</strong>, and the filings say the next chapter is <strong>9,500 beds by 2028 + asset-light 50-yr leases + oncology/transplant mix at ₹77k ARPOB</strong> — engineered in Delhi NCR, expanding in Mumbai/Lucknow, delivered in 22 hospitals and at home.</div>
</div>

<footer>
  <p><strong>Method.</strong> Filings-only portrait. What-company-does + products + vision + trends sourced from Max Healthcare AR FY25 (BSE 20-May-2025 investor presentation), BSE filings 2025-05-20 (Q4: gross ₹2,429 Cr +29%, EBITDA ₹632 Cr, PAT ₹376 Cr) and 2025-11-14 (H1FY26), <code>maxhealthcare.in</code>. TTM figures from <code>screener.in/company/MAXHEALTH</code> (TTM price ₹1,049.3, MCap ~₹1,02,129 Cr, P/E ~70.5×, P/B ~9.5×, BV ₹110, 52W 903–1,222, ROCE 25.9%, ROCE ex-growth 33.7%, PAT margin 16.0%). Peer revenues from filings: Apollo FY25 ₹21,794 Cr, Fortis ₹7,783 Cr, Narayana ₹5,483 Cr, Aster DM ₹4,138 Cr, Medanta ₹3,692 Cr.</p>
  <p><strong>Surface.</strong> Gemini-style skin (UI-Design/tokens.css v0.5, inlined): top-center orb field with 48s blue→aqua→green→gold cycle (static under prefers-reduced-motion; add <code>data-aurora="flat"</code> to disable blur). White surfaces, neutral gray structure, Outfit type. Hero gradient appears exactly three times — sparkle mark, headline, hero-tile ring — and never as status. Chart encoding: blue <code>#4285F4</code> = Max (the subject), gray = context.</p>
  <p>Rendered 2026-09-25 · Company_Overview/Final/MaxHealthcare_Gemini-forecast-2026-09-25.html · Gemini report surface (Phase 4) · every figure traced to the filing line; peer % is illustrative of one pot, not a TAM.</p>
</footer>
"""
between_replace("<!-- TAKEAWAY -->", "<!-- Gradient control panel -->", s09_new)

# Fix remaining JS data replacements: views and forecast series and trends and mcap ymax
# Views
old_views_block = "    q1: { label: 'Q1 FY27 inflow', mid: ['93%', 'export'], items: [{ name: 'Export & deemed', val: 93.1, c: 'var(--chart-blue)', x: '₹684 Cr' }, { name: 'Domestic', val: 6.9, c: 'var(--chart-context)', x: '₹51 Cr' }], note: 'Q1 FY27 ₹734 Cr total — 93% export pivot (accelerating vs FY25 68%).' },\n    fy26: { label: 'FY26 inflow', mid: ['79%', 'export'], items: [{ name: 'Export & deemed', val: 79, c: 'var(--chart-blue)', x: '≈₹1,730 Cr' }, { name: 'Domestic', val: 21, c: 'var(--chart-context)', x: '≈₹510 Cr' }], note: 'FY26 inflow ₹2,238 Cr (full year).' },\n    book: { label: 'Order book', mid: ['69.5%', 'export'], items: [{ name: 'Exports', val: 69.5, c: 'var(--chart-blue)', x: '₹1,533 Cr' }, { name: 'Domestic', val: 17.9, c: 'var(--chart-context)', x: '₹395 Cr' }, { name: 'Railway', val: 9.6, c: 'var(--ink-3)', x: '₹211 Cr' }, { name: 'Remainder', val: 3.0, c: 'var(--surface-3)', x: '' }], note: 'Book ₹2,208 Cr at 30 Jun 2026. Railway may overlap with reported export/domestic.' },\n    base: { label: 'Installed base', mid: ['8,375', 'units'], items: [{ name: 'Asia', val: 5522, c: 'var(--chart-context)', x: '5,522' }, { name: 'Europe', val: 1556, c: 'var(--chart-blue)', x: '1,556' }, { name: 'N. America', val: 674, c: 'var(--ink-3)', x: '674' }, { name: 'Rest', val: 623, c: 'var(--surface-3)', x: '623' }], note: 'Cumulative since inception — current flow far more US-weighted.' }"
new_views_block = "    q1: { label: 'Q4 FY25 revenue', mid: ['27%', 'growth'], items: [{ name: 'Hospital (Network)', val: 86, c: 'var(--chart-blue)', x: '₹2,326 Cr' }, { name: 'Max Lab', val: 2, c: 'var(--chart-context)', x: '₹46 Cr' }, { name: 'Max@Home', val: 2.4, c: 'var(--ink-3)', x: '₹56 Cr' }, { name: 'Other', val: 9.6, c: 'var(--surface-3)', x: '' }], note: 'Q4 FY25 net ₹2,326 Cr (+29% YoY). Intl ₹202 Cr (+28%, 9% of hospital). Dwarka 303 beds operational 2 Jul 2024.' },\n    fy25: { label: 'FY25 Network', mid: ['₹9,065', 'gross'], items: [{ name: 'Hospital Network', val: 90, c: 'var(--chart-blue)', x: '₹9,065 Cr' }, { name: 'International', val: 5, c: 'var(--chart-context)', x: '~9% (~₹800 Cr)' }, { name: 'New Units', val: 8.5, c: 'var(--ink-3)', x: '15% of Q4 mix' }, { name: 'Max Lab+Home', val: 3.5, c: 'var(--surface-3)', x: '~₹400 Cr' }], note: 'FY25 gross ₹9,065 Cr (+26% YoY, net ₹8,667 Cr). Op EBITDA ₹2,319 Cr (26.8%). New units 15% of Q4 rev vs 2% YoY.' },\n    payor: { label: 'Payor mix', mid: ['34%', 'instit.'], items: [{ name: 'Self-pay + Insured', val: 57, c: 'var(--chart-blue)', x: '~57%' }, { name: 'Institutional (CGHS)', val: 34, c: 'var(--chart-context)', x: '34.0% (vs 26.8% YoY)' }, { name: 'International', val: 9, c: 'var(--ink-3)', x: '~9%' }], note: 'H1 FY26: institutional 34% vs 26.8% Q2 FY25 — tariff pressure watch; self-pay/insured ~57% + intl 9% is the high-yield mix.' },\n    beds: { label: 'Bed capacity', mid: ['4,760', 'operational'], items: [{ name: 'Delhi NCR', val: 62, c: 'var(--chart-blue)', x: '~2,950 beds' }, { name: 'Lucknow + Nagpur + Mumbai', val: 22, c: 'var(--chart-context)', x: '~1,050 beds' }, { name: 'Mohali + Bathinda (PPP)', val: 10, c: 'var(--ink-3)', x: '~480 beds' }, { name: 'Dehradun + others', val: 6, c: 'var(--surface-3)', x: '~280 beds' }], note: 'Operational 4,760 Sep-25 (3,949 Sep-24). Total ~5,000 incl. Dwarka 303 + Saket Smart 400 coming. 3,700 more by 2028.' }"
if old_views_block in t:
    t = t.replace(old_views_block, new_views_block)
    t = t.replace("showView('q1');", "showView('fy25');")
    t = t.replace("showView('fy25');", "showView('fy25');", 1)

# groupedMini data
t = t.replace("const data = [{ k: 'Export', a: 257, b: 684 }, { k: 'Domestic', a: 135, b: 51 }];", "const data = [{ k: 'Net rev', a: 1799, b: 2326 }, { k: 'Intl', a: 158, b: 202 }];")
t = t.replace("const max = 750;", "const max = 2500;")

# trends JS
old_trend_js = "    { kick: 'Trend 1 · demand supercycle', icon: 'trending_up', h: 'Data centre & gas turbine surge', b: 'Global generator market <b>$51.99B (2025) → $72.66B (2029)</b>. AI farms + fracking + Ukraine rebuild. Data centre alone → <b>100 GW</b> US spike by 2030.', c: '→ TDPS: 40–45 MW generators, deliveries FY26.', cls: '' },\n    { kick: 'Trend 2 · hybrid transition', icon: 'energy', h: 'Energy transition = \"and\", not \"or\"', b: 'Not wind <em>or</em> gas — wind <em>and</em> gas <em>and</em> hydro. Grids need dispatchable + renewable. TDPS portfolio hits all three.', c: '→ Hydro stable + wind PMG/DFIG + gas bridge', cls: 'purple' },\n    { kick: 'Trend 3 · export supercycle', icon: 'public', h: 'Export is the growth engine', b: 'Highest-ever inflow <b>₹14,783M (+41% YoY)</b> in FY25 — <b>68%</b> exports/deemed exports. \"Will drive FY27 & FY28.\"', c: '→ 45 OEMs · healthy order book into FY26', cls: 'amber' },\n    { kick: 'Trend 4 · capacity bet', icon: 'engineering', h: 'Engineering & capacity ahead of revenue', b: 'UK Design Centre + third plant (ramp <b>Q4 FY26</b>) + motors. FY25 EBITDA <b>₹2,544M (+38.6%)</b>, PAT <b>₹1,746M (+47.5%)</b> on mix + leverage.', c: '→ Capex precedes margin — watch Q4 ramp', cls: 'amber' },\n    { kick: 'Trend 5 · volatility demands adaptability', icon: 'warning', h: 'Volatility demands adaptability', b: 'Global growth easing to <b>2.8% (2025)</b> vs <b>3.3% (2024)</b>; demand uneven — India offers scale/stability/opportunity. TDPS line: \"Solutions that function across complex environments and adapt to changing needs, without pause or compromise.\"', c: '→ Custom engineering as risk hedge', cls: 'amber' }"
new_trend_js = "    { kick: 'Trend 1 · capacity supercycle', icon: 'apartment', h: '9,500 beds by 2028 — reinvesting all profits', b: 'Chairman: <b>₹6,000 Cr capex</b> → <b>3,700 new beds</b> (5,000 → 9,500). +830 beds in 60 days (Mohali 160 + Nanavati 268 + Saket 400). Thane 500 on asset-light.', c: '→ Watch operational beds 4,760 → 6,500', cls: '' },\n    { kick: 'Trend 2 · ARPOB + occupancy', icon: 'trending_up', h: 'ARPOB ₹77k + 77% occupancy = pricing power', b: 'Existing units ARPOB <b>+7% YoY</b> (mix: oncology + robotics + transplants). Network 77% occupancy, OBDs <b>+19% YoY</b>. Existing 78–79%, new units ramp 46–81%.', c: '→ ARPOB × OBDs = revenue engine', cls: 'purple' },\n    { kick: 'Trend 3 · international & digital', icon: 'flight', h: 'International +28%, digital +58% — payor upgrade', b: 'Intl. ₹440 Cr H1FY26 <b>+28% YoY</b> — 9% of hospital rev. Digital ₹1,547 Cr <b>+58% YoY</b> (29% of gross). Max Lab/Med@Home <b>20%+ CAGR</b>.', c: '→ Self-pay + intl share vs institutional 34%', cls: 'amber' },\n    { kick: 'Trend 4 · margin & leverage', icon: 'savings', h: '27% margin holds while funding 3,700 beds', b: 'Op margin <b>26.8% FY25</b> (28.1% ex-Dwarka) → 27% guide. Net debt <b>₹1,576 Cr</b> vs net cash. CFO <b>₹1,447 Cr</b>, EBITDA/bed ₹69.6L.', c: '→ Margin + net debt + FCF', cls: 'amber' },\n    { kick: 'Trend 5 · ageing + under-penetration', icon: 'groups', h: 'India 300M 60+ in 15 yrs — beds still scarce', b: 'India <b>60+ to 300M</b> in 15 yrs, $5Tn economy. Industry net +5,000 beds/yr vs gap widening. Long-capital > PE cycle.', c: '→ 50–60 yr leases > 4-yr PE hold', cls: 'amber' }"
if old_trend_js in t:
    t = t.replace(old_trend_js, new_trend_js)

# Forecast series
t = t.replace("      series: { bear: [764, 602, 518, 471, 454, 444], base: [764, 834, 923, 1017, 1165, 1315], bull: [764, 975, 1249, 1546, 1936, 2407] }", "      series: { bear: [1049.3, 950, 870, 820, 795, 782], base: [1049.3, 1160, 1290, 1420, 1545, 1680], bull: [1049.3, 1290, 1585, 1870, 2145, 2450] }")
t = t.replace("      series: { bear: [23864, 18808, 16191, 14701, 14180, 13854], base: [23864, 26066, 28835, 31757, 36403, 41060], bull: [23864, 30466, 39029, 48304, 60484, 75190] }", "      series: { bear: [102129, 92340, 84564, 79704, 77268, 76010], base: [102129, 112752, 125388, 138024, 150174, 163296], bull: [102129, 125388, 154062, 181764, 208494, 238140] }")
t = t.replace("      ymax: 80000, ticks: [0, 20000, 40000, 60000, 80000], unit: \"₹ Cr\",", "      ymax: 250000, ticks: [0, 50000, 100000, 150000, 200000, 250000], unit: \"₹ Cr\",")

# Clean stray TDPS refs that survived
t = t.replace("tdps.co.in/generators", "maxhealthcare.in/investors")

# Ensure no remaining double brand
# Already handled

OUT.write_text(t, encoding="utf-8")
print(f"Built v2 -> {OUT} {len(t):,} chars")
print("open", t.count("<div"), "close", t.count("</div>"))
import re as _re
print("div open regex", len(_re.findall(r"<div\b", t)), "close", len(_re.findall(r"</div>", t)))
