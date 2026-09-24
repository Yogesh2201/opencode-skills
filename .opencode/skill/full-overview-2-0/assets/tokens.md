# Tokens & palette (per version)

## Plain (interactive render)

```css
--page:#f9f9f7; --surface:#fcfcfb; --surface-2:#f1efe9;
--ink:#1a1a1a; --ink-2:#3d3d3d; --muted:#898781;
--accent:#2a78d6; --accent-deep:#1c5cab;
--orange:#eb6834; --crit:#d03b3b; --good:#008300;
--hairline:rgba(11,11,11,.10); --grid:#e1e0d9;
--radius:14px;
```

- **Two-hue rule:** blue `#2a78d6` = TDPS · warm gray `#898781` = context.
- **Orange `#eb6834` = the one hinge** — TDPS subject bar + takeaway closing rule only. Never decorate with it.
- Forecast encoding: bear `#d03b3b` · base `#2a78d6` · bull `#008300`.
- System font stack. No icon fonts, no gradients, no orb fields.
- Chrome: 3px progress bar, sticky scrollspy nav, back-to-top, reveal-on-scroll.

## Gemini (source)

```css
--bg:#fbfbfd; --surface:#ffffff; --surface-2:#f0f4f9; --surface-3:#e9eef6;
--ink:#1f1f1f; --ink-2:#444746; --ink-3:#8f909c; --ink-inv:#ffffff;
--line:#e3e3e3; --line-strong:#c5c7c9;
--ok:#1e8e3e; --warn:#b06000; --bad:#d93025;
--gemini-sweep: linear-gradient(90deg,#4285F4 0%,#5961F0 25%,#9B72CB 50%,#D96570 75%,#FFA756 100%);
--chart-blue:#4285F4; --chart-blue-deep:#1967d2; --chart-then:#a8c7fa; --chart-context:#b3b5be;
--r-sm:12px; --r-md:16px; --r-lg:24px; --r-pill:999px;
--font:"Google Sans","Outfit","Segoe UI Variable",system-ui,sans-serif;
--ease:cubic-bezier(.2,0,0,1); --drift-period:36s; --cycle-period:48s; --blur:40px;
```

- Fonts: **Outfit** + **Material Symbols Rounded** via Google Fonts; icons are `<span class="material-symbols-rounded">`, never emoji.
- Sweep budget **max 3**: sparkle mark · gradient H1 · hero-tile ring.
- Orb field: 48s cycle, `data-aurora="flat"` and `prefers-reduced-motion` disable it.
- Themes: `:root[data-t="green-white"|"green"|"sunrise"|"dusk"|"none"]`.

## Markdown

No tokens — hierarchy comes from `#`/`##`/`###`, tables, `>` blockquotes, fenced ASCII bars.
Palette only appears in the footer's **Palette** paragraph (hexes listed as inline `code`).

## SVG rule (both HTML versions)

Use `style="fill:var(--…)"` / `style="stroke:var(--…)"`. Never `fill="var(--…)"` as a
presentation attribute — it does not resolve and renders black/none.
