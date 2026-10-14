#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract.py — one-time extractor for the forecast-overview skill.

Copies the forecast section (06) + forecast data out of full-overview-2-0
into this skill's own folders, so forecast-overview is self-contained:

  full-overview-2-0/assets/forecast-model.md
      -> forecast-overview/assets/forecast-model.md (verbatim)
  full-overview-2-0/data/ujjivan.json [forecast]
      -> forecast-overview/data/ujjivan-forecast.json
  full-overview-2-0/data/maxhealth.json [forecast]
      -> forecast-overview/data/maxhealth-forecast.json
  forecast-model.md section 06 numbers (TDPS)
      -> forecast-overview/data/tdps-forecast.json
  Company_Overview/Final/Ujjivan_Gemini-forecast-2026-09-25.html
  <h2 id="s06"> ... <!-- TAKEAWAY -->
      -> forecast-overview/references/forecast-section.html
      (s06 card + twin-chart JS + header-toggle JS — working reference)

Run:  python .opencode/skill/forecast-overview/scripts/extract.py
Safe to re-run (overwrites).
"""
import json
import pathlib
import re

ROOT = pathlib.Path(r"C:\Users\Yogesh Kumar\Downloads\Open_Code")
SRC = ROOT / ".opencode" / "skill" / "full-overview-2-0"
DST = pathlib.Path(__file__).resolve().parents[1]

( DST / "assets" ).mkdir(parents=True, exist_ok=True)
( DST / "data" ).mkdir(parents=True, exist_ok=True)
( DST / "references" ).mkdir(parents=True, exist_ok=True)

# 1. forecast-model.md verbatim
fm = ( SRC / "assets" / "forecast-model.md" ).read_text(encoding="utf-8")
( DST / "assets" / "forecast-model.md" ).write_text(fm, encoding="utf-8")
print(f"OK assets/forecast-model.md ({len(fm):,} chars)")

# 2/3. forecast blocks from company data files
for stem, out in [("ujjivan", "ujjivan-forecast.json"),
                  ("maxhealth", "maxhealth-forecast.json")]:
    d = json.loads(( SRC / "data" / f"{stem}.json" ).read_text(encoding="utf-8"))
    slim = {
        "company": d["meta"]["company"],
        "short": d["meta"].get("short", d["meta"]["company"]),
        "nse": d["meta"]["nse"],
        "render_date": d["meta"].get("render_date", ""),
        "anchor_price": d["forecast"]["anchor"]["price"],
        "shares_cr": d["forecast"]["anchor"].get("shares_cr"),
        "forecast": d["forecast"],
    }
    p = DST / "data" / out
    p.write_text(json.dumps(slim, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"OK data/{out}")

# 4. TDPS forecast (from forecast-model.md section 06 numbers)
tdps = {
    "company": "TD Power Systems",
    "short": "TDPS",
    "nse": "TDPOWERSYS",
    "render_date": "2026-09-20",
    "anchor_price": 764,
    "shares_cr": 31.24,
    "forecast": {
        "anchor": {"price": 764, "mcap_cr": 23864, "shares_cr": 31.24,
                   "sales_ttm_cr": 2124, "eps_ttm": 8.8, "pe": 86.8},
        "scenarios": {
            "bear": {"price_fy31": 444, "mcap_fy31_cr": 13854, "cagr": -10.3,
                     "sales_cagr": 10, "sales_fy31_cr": 3421,
                     "pat_margin_fy31": 9.0, "exit_pe": 45,
                     "eps_fy31": 9.9},
            "base": {"price_fy31": 1315, "mcap_fy31_cr": 41060, "cagr": 11.5,
                     "sales_cagr": 18, "sales_fy31_cr": 4859,
                     "pat_margin_fy31": 13.0, "exit_pe": 65,
                     "eps_fy31": 20.2},
            "bull": {"price_fy31": 2407, "mcap_fy31_cr": 75190, "cagr": 25.8,
                     "sales_cagr": 25, "sales_fy31_cr": 6482,
                     "pat_margin_fy31": 14.5, "exit_pe": 80,
                     "eps_fy31": 30.1},
        },
        "year_path": {
            "price": {
                "bear": [764, 602, 518, 471, 454, 444],
                "base": [764, 834, 923, 1017, 1165, 1315],
                "bull": [764, 975, 1249, 1546, 1936, 2407],
            },
            "mcap": {
                "bear": [23864, 18808, 16191, 14701, 14180, 13854],
                "base": [23864, 26066, 28835, 31757, 36403, 41060],
                "bull": [23864, 30466, 39029, 48304, 60484, 75190],
            },
        },
        "note": "Shares flat at ~31.24 Cr — almost debt-free, no dilution assumed. Bear = export deferral + OPM slip + derate to 45x. Bull = data-centre gas surge + UK design-centre localisation, P/E held at 80x.",
    },
}
( DST / "data" / "tdps-forecast.json" ).write_text(
    json.dumps(tdps, indent=2, ensure_ascii=False), encoding="utf-8")
print("OK data/tdps-forecast.json")

# 5. s06 section reference from the built Ujjivan Gemini file
built = ROOT / "Company_Overview" / "Final" / "Ujjivan_Gemini-forecast-2026-09-25.html"
html = built.read_text(encoding="utf-8")
start = html.find('<h2 id="s06">')
end = html.find("<!-- TAKEAWAY -->")
assert start > 0 and end > start, "s06 block not found in built file"
section = html[start:end].rstrip() + "\n"
header = ("<!-- Forecast section 06 reference — extracted from\n"
          "     Company_Overview/Final/Ujjivan_Gemini-forecast-2026-09-25.html\n"
          "     Contains: s06 card (outcomes + assumptions + year path + insight)\n"
          "     + twin-chart JS ([data-fc=price|mcap]) + header-toggle JS (#hdrFcToggle).\n"
          "     Company data changes per request; structure/IDs/JS stay verbatim. -->\n")
( DST / "references" / "forecast-section.html" ).write_text(header + section, encoding="utf-8")
print(f"OK references/forecast-section.html ({len(section):,} chars)")
print("DONE — forecast-overview is self-contained.")
