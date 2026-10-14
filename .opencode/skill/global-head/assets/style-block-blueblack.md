<style>
  :root {
    --bb-blue: #0B5FC0; --bb-blue-deep: #0A4DA0;
    --bb-ink: #111418;  --bb-muted: #5b6470; --bb-line: #d7dde5;
  }
  /* text-color only â€” no fill / no background anywhere */
  body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; color: var(--bb-ink); background: transparent; }
  h1 { color: var(--bb-blue); border-bottom: 3px solid var(--bb-blue); padding-bottom: 6px; }
  h2 { color: var(--bb-blue); border-bottom: 1px solid var(--bb-line); padding-bottom: 4px; margin-top: 30px; }
  h3 { color: var(--bb-ink); }
  h4 { color: var(--bb-blue); }
  blockquote { border-left: 4px solid var(--bb-blue); background: transparent; margin: 10px 0; padding: 10px 14px; color: var(--bb-ink); }
  blockquote.gold { border-left-color: var(--bb-ink); background: transparent; }
  blockquote.red  { border-left-color: var(--bb-ink); background: transparent; color: var(--bb-ink); }
  blockquote.red .red, blockquote.red strong { color: var(--bb-ink); }
  table { border-collapse: collapse; width: 100%; margin: 12px 0; background: transparent; }
  th { background: transparent; color: var(--bb-blue); text-transform: uppercase; font-size: .78em; letter-spacing: .05em; padding: 8px 10px; border-bottom: 2px solid var(--bb-blue); text-align: left; }
  td { padding: 8px 10px; border-bottom: 1px solid var(--bb-line); font-size: .92em; background: transparent; color: var(--bb-ink); }
  /* weight ladder: 400 body â†’ 600 emphasis â†’ 650 value. No 700/800 anywhere. */
  .v    { font-weight: 650; color: var(--bb-blue); background: transparent; letter-spacing: -.005em; }
  .gold { font-weight: 600; color: var(--bb-ink); background: transparent; }
  .red  { font-weight: 600; color: var(--bb-ink); background: transparent; }
  .mut  { color: var(--bb-muted); background: transparent; }
  strong { font-weight: 600; color: var(--bb-ink); letter-spacing: -.005em; }
  .pill { display: inline-block; font-size: .75em; font-weight: 600; letter-spacing: .02em; padding: 2px 9px; border-radius: 99px; background: transparent; border: 1px solid currentColor; }
  .pill.pass { color: var(--bb-blue); }
  .pill.warn { color: var(--bb-ink); }
  .pill.risk { color: var(--bb-ink); }
  .pill.na   { color: var(--bb-muted); }
  .band { background: transparent; color: var(--bb-ink); padding: 16px 20px; border-radius: 10px; margin-top: 26px; border: 1px solid var(--bb-line); border-left: 4px solid var(--bb-blue); }
  .band b { color: var(--bb-blue); }
  code { background: transparent; color: var(--bb-blue); padding: 1px 5px; font-size: .88em; }
</style>
