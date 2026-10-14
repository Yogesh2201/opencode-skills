#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_placeholders.py — one-time conversion of verbatim templates to placeholder templates.

Run once after copying examples/ to templates/:
  python scripts/make_placeholders.py

It replaces known TDPS hardcoded values with {{placeholders}} so build.py can do
simple string replacement instead of regex.

Example:
  ₹764  -> {{price.current}}
  ₹23,864 Cr -> {{price.mcap_cr}} Cr
  111 countries -> {{kpi.countries}} countries
  43.5% secured -> {{kpi.secured_pct}}% secured

After this, build.py becomes trivial:
  template.replace("{{price.current}}", str(data["price"]["current"]))

This file is NOT used per-build — only once during prototype setup (0 recurring tokens).
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[1]
GEMINI = ROOT / "templates" / "gemini.template.html"

REPLACEMENTS = [
    ("TD Power Systems", "{{meta.company}}"),
    ("TDPOWERSYS", "{{meta.nse}}"),
    ("533553", "{{meta.bse}}"),
    ("Dabaspet, Bengaluru", "{{meta.hq}}"),
    ("₹764", "₹{{price.current}}"),
    ("₹23,864 Cr", "₹{{price.mcap_cr}} Cr"),
    ("~31.24 Cr shares", "~{{price.shares_cr}} Cr shares"),
    ("₹2,124 Cr", "₹{{kpi.revenue_ttm_cr}} Cr"),
    ("111 countries", "{{kpi.countries}} countries"),
    ("7,200+ installations", "{{kpi.installations}} installations"),
    ("₹2,208 Cr", "₹{{kpi.order_book_cr}} Cr"),
]

def convert():
    text = GEMINI.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    GEMINI.write_text(text, encoding="utf-8")
    print(f"Converted {len(REPLACEMENTS)} placeholders in {GEMINI}")

if __name__ == "__main__":
    convert()
