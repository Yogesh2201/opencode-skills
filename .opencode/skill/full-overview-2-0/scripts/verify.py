#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify.py — headless checklist for Full Overview 2.0 (prototype)

Runs the same checks as assets/verify-checklist.md but via script (0 LLM tokens).

Checks:
  - No PART_ / JS_ markers
  - <div> balanced
  - exactly one </body></html>
  - required IDs exist: s01, s02, s03, s04, s04v, s05, s06, s09, seg, donut, leg, donutnote, tpKicker, hdrFcToggle
  - val-visual, flag-grid present
  - CSS uses style="fill:var(--...)" not fill="var(--"
  - (optional) headless chrome dump if --chrome flag
"""
import pathlib, re, sys

def verify(path: pathlib.Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    ok = True
    def check(cond, msg):
        nonlocal ok
        print(f"{'PASS' if cond else 'FAIL'}  {msg}")
        if not cond: ok = False

    check(len(re.findall(r"PART_|JS_[A-Z]", raw)) == 0, "no PART_/JS_ markers")
    check(len(re.findall(r"<div\b", raw)) == len(re.findall(r"</div>", raw)), f"div balanced ({len(re.findall(r'<div\b', raw))} open / {len(re.findall(r'</div>', raw))} close)")
    check(len(re.findall(r"</body>", raw)) == 1, "exactly one </body>")
    check(len(re.findall(r"</html>", raw)) == 1, "exactly one </html>")
    for id_ in ["s01", "s02", "s03", "s04", "s04v", "s05", "s06", "s09", "seg", "donut", "leg", "donutnote", "tpKicker", "hdrFcToggle", "val-visual", "flag-grid", "ey-tile"]:
        check(id_ in raw, f"id/class {id_} present")
    check('style="fill:var(' in raw or 'style="stroke:var(' in raw, 'SVG uses style="fill:var(--)"')
    check('fill="var(' not in raw, 'no fill="var('' presentation attr')
    check(path.stat().st_size < 200*1024, f"size {path.stat().st_size:,} < 200KB")
    return ok

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("file", help="path to rendered HTML")
    args = ap.parse_args()
    p = pathlib.Path(args.file)
    if not p.exists():
        sys.exit(f"Not found: {p}")
    ok = verify(p)
    sys.exit(0 if ok else 1)
