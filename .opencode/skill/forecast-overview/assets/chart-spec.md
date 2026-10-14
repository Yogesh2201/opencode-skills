# Chart spec — twin forecast charts + scenario encoding

Reference for rendering the `fc-stack` block (see `references/forecast-section.html`).
Keep IDs/classes/JS verbatim; replace only data listed in Step 3 of `SKILL.md`.

## Panels

Two panels, same shape, different series:

```html
<div class="fc-panel" data-fc="price"> … </div>
<div class="fc-panel" data-fc="mcap">  … </div>
```

Each panel: `.fc-head` (`.fc-title` + `.fc-sub`) → `.fc-legend` (3×
`button.fc-chip[data-s="bear|base|bull"]` with `.dot`) → `.fc-plot` (contains
`.fc-tip`) → `.fc-foot` (left: units note · right: dashed-today note).

## JS series format (vanilla SVG, no deps)

```js
var YEARS = ["TTM", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"];
var CF = {
  price: {
    ymax: 220, ticks: [0, 50, 100, 150, 200], unit: "₹ / share",
    series: { bear: [...6], base: [...6], bull: [...6] }
  },
  mcap: {
    ymax: 40000, ticks: [0, 10000, 20000, 30000, 40000], unit: "₹ Cr",
    series: { bear: [...6], base: [...6], bull: [...6] }
  }
};
```

- `series` = `year_path.price` / `year_path.mcap` from the data JSON, TTM first.
- `ymax` = first round number above Bull FY31E (≈ +10% headroom).
  Ujjivan price → 220 · Ujjivan MCap → 40000 · TDPS price → 2600 · TDPS MCap → 80000.
- `ticks` = 5–6 evenly spaced values ending at/under `ymax`.
- Hover readout, guide line, end labels and draw-in animation come free from the
  reference JS — do not rewrite it.

## Scenario colours (both versions)

| Scenario | Gemini (`var CF COLORS`) | Plain |
|---|---|---|
| bear | `#d93025` (`var(--bad)`) | `#d03b3b` (`--crit`) |
| base | `#4285F4` (`var(--chart-blue)`) | `#2a78d6` (`--accent`) |
| bull | `#1e8e3e` (`var(--ok)`) | `#008300` (`--good`) |

## Header toggle sync (`#hdrFcToggle`)

Sticky-nav pill `06 FC | Bear · Base · Bull` (`#hdrFcToggle` + 3×
`button.hfc-chip[data-hfc]`) is a **global filter** for both panels via
`panel.setAttribute('data-off', …)`. Syncs bidirectionally with per-panel
`.fc-chip` toggles; clicking a header chip scrolls to `#s06` if out of view.
Reference JS block `/* Header 06 Forecast toggle … */` is included at the end of
`references/forecast-section.html` — keep it with the charts.

## IDs that must survive (unique per file)

`s06`, `data-fc="price"`, `data-fc="mcap"`, `.fc-chip[data-s]`, `.fc-plot`,
`.fc-tip`, `hdrFcToggle`, `.hfc-chip[data-hfc]`.

## SVG rule

Generated SVG uses `style="stroke:…"` / `style="fill:…"` — never presentation
attributes with `var()`.
