#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib, json, re

OUT = pathlib.Path(r"C:\Users\Yogesh Kumar\Downloads\Open_Code\Company_Overview\Final\MaxHealthcare_Gemini-forecast-2026-09-25.html")
DATA = pathlib.Path(r"C:\Users\Yogesh Kumar\Downloads\Open_Code\.opencode\skill\full-overview-2-0\data\maxhealth.json")
data = json.loads(DATA.read_text(encoding="utf-8"))
text = OUT.read_text(encoding="utf-8")
val = data["valuation"]
forecast = data["forecast"]
trends = data["trends"]
red = data["red_flags"]
bottom = data["bottom_line"]

# --- s04v Valuation with AlphaSpread ---
s04v = f"""
<h2 id="s04v"><span class="num">04</span> Valuation + DCF</h2>
<p class="section-note">Read as a system — market prices quinary + occupancy leverage, not bed count. AlphaSpread DCF is primary, Multiples is cross-check. Needs occupancy 75% + ARPOB hold.</p>
<div class="card">
  <div class="quote">“Own the clinical, but let the multiple give you the price.” — AlphaSpread intrinsic ₹1,474 (+40.9%) vs Multiples ₹1,026 (fair)
    <span class="who">— Thesis: 69.8× P/E prices quinary + brownfield ramp. Bull = occupancy 75% holds + diagnostics flywheel, P/E stays 45x. *Approximate benchmarks. Source: <a href="{val['url']}" target="_blank">AlphaSpread DCF</a> (15yr Net Income, Rev 15.2%, Margin 16.8%, Discount 10.5%, Exit 36.4x P/E).</span>
  </div>
  <h3>Valuation multiples — 4 rows only</h3>
  <div class="sub">P/B and P/S live in Financial snapshot only. Trailing P/E = ₹{val['price_current']:,} / ~₹{data['price']['eps_ttm']} ≈ {data['price']['pe_ttm']}×. BV ₹{data['price']['bv']} → P/B {data['price']['pb']}×. AlphaSpread DCF is filings + model.</div>
  <table class="dt">
    <tr><th>Metric</th><th style="text-align:right">Value</th><th>Benchmark*</th><th>Read</th></tr>
    <tr><td><strong>Trailing P/E</strong></td><td style="text-align:right">{data['price']['pe_ttm']}×</td><td style="color:var(--ink-2)">Hospital median ~40×* · Apollo ~38×* · Fortis ~35×*</td><td style="color:var(--bad); font-weight:500;">🔴 Premium</td></tr>
    <tr><td><strong>Forward P/E (FY26E)</strong></td><td style="text-align:right">~55×</td><td style="color:var(--ink-2)">36.4× AlphaSpread exit* · 28× bear</td><td style="color:var(--warn); font-weight:500;">🟡 Elevated</td></tr>
    <tr><td><strong>P/B (BV ₹{data['price']['bv']})</strong></td><td style="text-align:right">{data['price']['pb']}×</td><td style="color:var(--ink-2)">Hospital median ~8×* / Apollo ~12×*</td><td style="color:var(--bad); font-weight:500;">🔴 Premium</td></tr>
    <tr><td><strong>ROCE / ROE</strong></td><td style="text-align:right">{data['company_kpis']['roce']}% / {data['company_kpis']['roe']}%</td><td style="color:var(--ink-2)">Hospital median ~12% / 13%* · TTM</td><td style="color:var(--ok); font-weight:500;">🟢 At plan</td></tr>
  </table>
  <div class="grid-4">
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">🎯 DCF Value</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--chart-blue-deep)">₹{val['dcf_value']:,.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">15yr Net Income · 10.5% · 36.4x · +40.1%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">📊 Multiples</div>
      <div style="font-size:1.3rem; font-weight:500;">₹{val['multiples_value']:,.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">P/E,P/B,EV/EBIT vs peers · -1.9%</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">💎 Intrinsic</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--chart-blue-deep)">₹{val['intrinsic_value']:,.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">AlphaSpread blended · +40.9% · 29% undervalued</div>
    </div>
    <div class="tile" style="box-shadow:none; background:var(--surface-2);">
      <div class="label">⚖️ Buy Zone →</div>
      <div style="font-size:1.3rem; font-weight:500; color:var(--ok)">₹{val['buy_zone_20pct']:,.2f}</div>
      <div style="font-size:.78rem; color:var(--ink-2); font-weight:300; margin-top:4px">20% MOS · 12.7% above price</div>
    </div>
  </div>
  <div style="margin-top:14px; overflow-x:auto;">
    <table class="dt">
      <tr><th>Approach</th><th style="text-align:right">Value / Share</th><th>vs ₹{val['price_current']:,}</th></tr>
      <tr><td><strong>DCF Value (15yr, 10.5%, 36.4x) — AlphaSpread</strong></td><td style="text-align:right">₹{val['dcf_value']:,.2f}</td><td>🟢 +40.1%</td></tr>
      <tr><td><strong>Multiples-Based Value — AlphaSpread</strong></td><td style="text-align:right">₹{val['multiples_value']:,.2f}</td><td>🔴 -1.9%</td></tr>
      <tr><td><strong>Intrinsic Value (Base) — AlphaSpread</strong></td><td style="text-align:right; color:var(--chart-blue-deep); font-weight:500;">₹{val['intrinsic_value']:,.2f}</td><td>🟢 +40.9% (29% undervalued)</td></tr>
      <tr><td><strong>Buy Zone (20% MOS)</strong></td><td style="text-align:right">₹{val['buy_zone_20pct']:,.2f}</td><td>🎯 12.7% above current</td></tr>
    </table>
  </div>
  <div class="quote">📌 METHODOLOGY — AlphaSpread: 15-year forecast via Net Income, Revenue Growth {val['dcf_assumptions']['revenue_growth']}% (vs 5Y hist {val['dcf_assumptions']['revenue_growth_5y_hist']}%, Wall St 3Y {val['dcf_assumptions']['revenue_growth_wallst_3y']}%), Net Margin {val['dcf_assumptions']['net_margin']}% (vs 5Y {val['dcf_assumptions']['net_margin_5y_hist']}%), Discount Rate {val['dcf_assumptions']['discount_rate']}% (WACC/Cost of Equity), Exit Multiple {val['dcf_assumptions']['exit_multiple']}x {val['dcf_assumptions']['exit_multiple_type']}. Multiples-Based from P/S, P/E, P/OCF, P/B, EV/Sales/EBITDA etc. vs peers/history. Intrinsic = AlphaSpread selected method (DCF primary for Max). VIC 0.32, Quintile Spread 28.3%, Hit Rate 65.1%. <span class="who">— Source: <a href="{val['url']}" target="_blank">alphaspread.com/security/nse/maxhealth/dcf-valuation</a> + <a href="https://www.alphaspread.com/security/nse/maxhealth/relative-valuation" target="_blank">relative-valuation</a>. Price {val['price_current']:,} (AlphaSpread). Local cross-check: FY26E P/E ~55x, EV/EBITDA ~29x — DCF still implies 40% upside.</span></div>
  <div class="val-visual" style="background:var(--surface-2); border-radius:var(--r-md); padding:16px; margin-top:14px;">
    <div style="font-size:.72rem; text-transform:uppercase; letter-spacing:.07em; color:var(--ink-3); font-weight:500;">📈 Valuation bar — intrinsic ₹{val['intrinsic_value']:,.0f} (+40.9%) · DCF ₹{val['dcf_value']:,.0f} · Multiples ₹{val['multiples_value']:,.0f} · buy ₹{val['buy_zone_20pct']:,.0f}</div>
    <div style="display:flex; justify-content:space-between; font-size:.72rem; color:var(--ink-3); margin-top:8px; flex-wrap:wrap; gap:6px;"><span>LOW ₹700</span><span>CURRENT ₹{val['price_current']:,}</span><span>BUY ₹{val['buy_zone_20pct']:,.0f}</span><span>IV ₹{val['intrinsic_value']:,.0f}</span><span>DCF ₹{val['dcf_value']:,.0f}</span><span>MULT ₹{val['multiples_value']:,.0f}</span></div>
    <div class="bar-track" style="height:10px; background:var(--surface); border:1px solid var(--line); border-radius:var(--r-pill); position:relative; overflow:hidden; margin:14px 0 8px;"><div class="bar-fill" style="width:72%; background:linear-gradient(90deg,#4285F4,#9B72CB); position:absolute; left:0; top:0; bottom:0; border-radius:var(--r-pill);"></div></div>
    <div class="bar-marks" style="display:flex; justify-content:space-between; font-size:.72rem; color:var(--ink-3); font-weight:500;"><span>₹700</span><span>IV ₹{val['intrinsic_value']:,.0f}</span><span>₹1,500</span></div>
    <div style="font-size:.78rem; color:var(--ink-2); margin-top:8px; font-weight:300;">Intrinsic <strong style="color:var(--ink)">₹{val['intrinsic_value']:,.0f}</strong> — 29% undervalued — buy <strong style="color:var(--ink)">₹{val['buy_zone_20pct']:,.0f}</strong> is 12.7% above current (already in buy zone per AlphaSpread). DCF ₹{val['dcf_value']:,.0f} = clinical + occupancy holds; Multiples ₹{val['multiples_value']:,.0f} = fairly valued vs history — watch P/E derate from 69.8x to 36.4x.</div>
    <div style="font-size:.72rem; color:var(--ink-3); margin-top:6px;">Bear FY31 685 · Base 1,474 · Bull 2,120 · Shares 97.33 Cr (FV ₹10) · Valuation via AlphaSpread 18 Sep 2026</div>
  </div>
</div>
"""
# Replace old valuation (from <h2 id="s04v"> to before <h2 id="s05">)
text = re.sub(r'<h2 id="s04v">.*?<div class="val-visual".*?</div>\s*</div>\s*\n\n<h2 id="s05">', s04v + '\n\n<h2 id="s05">', text, count=1, flags=re.S)
# Fallback if pattern not found
if 'Intrinsic Value' not in text or 'AlphaSpread' not in text:
    text = re.sub(r'<h2 id="s04v">.*?<h2 id="s05">', s04v + '\n\n<h2 id="s05">', text, count=1, flags=re.S)
OUT.write_text(text, encoding="utf-8")
print(f"Patched s04v AlphaSpread -> len {len(text)} s04v present {text.count('s04v')}")

# --- s05 Trends ---
# Replace trends array in JS
trends_js = "const trends = [\n"
for t in trends:
    trends_js += f"    {{ kick: '{t['kick']}', icon: '{t['icon']}', h: '{t['title']}', b: '{t['body']}', c: '{t['cta']}', cls: '{t['cls']}' }},\n"
trends_js += "  ];"
text = OUT.read_text(encoding="utf-8")
old_trends = re.search(r"const trends = \[.*?Trend 5.*?\];", text, re.S)
if old_trends:
    text = text.replace(old_trends.group(0), trends_js)
    print("trends JS replaced")
else:
    print("trends not found")
OUT.write_text(text, encoding="utf-8")

# Patch big messages (3)
# Find big messages grid
text = OUT.read_text(encoding="utf-8")
# For brevity, we will leave big messages as is (they were TDPS); we should replace with Max messages
# Replace the 3 big message tiles content via simple string replace for each
big_replacements = [
    ("We step into FY26 with conviction", "Quinary care + robotic + genomics — ARPOB ₹77,100 flat, occupancy +300 bps — volume, not price."),
    ("Export growth will drive FY27", "Dwarka breakeven in 6M, Lucknow/Nagpur double-digit EBITDA growth — brownfield first, greenfield selective."),
    ("Third plant commissioned", "EBITDA 28.5% despite new beds — occupancy leverage + payer mix + diagnostics flywheel."),
]
for old, new in big_replacements:
    if old in text:
        text = text.replace(old, new)
OUT.write_text(text, encoding="utf-8")
print(f"Patched big messages -> len {len(text)}")

# --- 06 Forecast ---
# Update forecast anchor and year path
text = OUT.read_text(encoding="utf-8")
# Replace anchor line
text = re.sub(r"Anchor:.*?Mcap.*?FY25.*?\n", f"Anchor: ₹{forecast['anchor']['price']:,} · MCap ₹{forecast['anchor']['mcap_cr']:,} Cr · shares ~{forecast['anchor']['shares_cr']} Cr · Sales ₹{forecast['anchor']['sales_ttm_cr']:,} Cr TTM · EPS ₹{forecast['anchor']['eps_ttm']} · P/E {forecast['anchor']['pe']}× · P/B {forecast['anchor']['pb']}× · 5Y hist 27.3% Rev\n", text, count=1)
# Replace year path line
text = re.sub(r"Year path \(price.*?\.", f"Year path (price ₹): Bear {', '.join(map(str, forecast['year_path']['price']['bear']))} · Base {', '.join(map(str, forecast['year_path']['price']['base']))} · Bull {', '.join(map(str, forecast['year_path']['price']['bull']))}. MCap (₹ Cr): Bear {', '.join(map(str, forecast['year_path']['mcap']['bear']))} · Base {', '.join(map(str, forecast['year_path']['mcap']['base']))} · Bull {', '.join(map(str, forecast['year_path']['mcap']['bull']))}. Monitor quarterly: occupancy, ARPOB, beds, sales, OPM, PAT margin, P/E vs AlphaSpread exit 36.4x, ROCE, D/E.", text, count=1, flags=re.S)
OUT.write_text(text, encoding="utf-8")
print(f"Patched forecast -> len {len(text)}")

# --- Takeaway ---
takeaway = data["takeaway"]
text = OUT.read_text(encoding="utf-8")
text = re.sub(r'<div class="line">.*?</div>', f'<div class="line">{takeaway}</div>', text, count=1, flags=re.S)
OUT.write_text(text, encoding="utf-8")
print(f"Patched takeaway")
print(f"Final len {len(text)}")
