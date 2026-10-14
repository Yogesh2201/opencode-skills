<style>
  /* â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
     BLACK / BLUE / ORANGE
     Text-colour only â€” no fills, no backgrounds anywhere, so the document
     inherits whatever canvas the host renders it on.
     Weight ladder: 400 body â†’ 600 emphasis â†’ 650 value. No 700/800.

     Blue   = settled and structural: headings, rules, verified confidence.
     Orange = unresolved: needs a human decision, or carries known risk.
     Orange is never decorative here. If nothing on the page is genuinely
     uncertain, it should not appear.
     â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• */
  :root {
    --bo-black:       #111418;  /* body, H3, emphasis     18.4:1  AAA */
    --bo-blue:        #0B5FC0;  /* headings, rules, values  5.9:1  AAA */
    --bo-blue-deep:   #0A4DA0;  /* hover, deep emphasis     6.9:1  AAA */
    --bo-orange:      #B45309;  /* unresolved, caution      5.0:1  AA  */
    --bo-orange-deep: #8A3D07;  /* weakest confidence       7.4:1  AAA */
    --bo-muted:       #5B6470;  /* asides, secondary        6.4:1  AAA */
    --bo-line:        #D7DDE5;  /* hairline rules, non-text          */
  }

  body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
         color: var(--bo-black); background: transparent; line-height: 1.6; }

  h1 { color: var(--bo-blue); border-bottom: 3px solid var(--bo-blue);
       padding-bottom: 6px; letter-spacing: -.01em; }
  h2 { color: var(--bo-blue); border-bottom: 1px solid var(--bo-line);
       padding-bottom: 4px; margin-top: 30px; }
  h3 { color: var(--bo-black); font-weight: 600; margin-top: 22px; }
  h4 { color: var(--bo-blue); font-weight: 600; }

  hr { border: 0; border-top: 1px solid var(--bo-line); margin: 28px 0; }

  strong { font-weight: 600; color: var(--bo-black); letter-spacing: -.005em; }
  em     { color: var(--bo-black); }

  a { color: var(--bo-blue); text-decoration: none; border-bottom: 1px solid var(--bo-blue); }
  a:hover { color: var(--bo-blue-deep); border-bottom-color: var(--bo-blue-deep); }

  code { background: transparent; color: var(--bo-blue); padding: 1px 5px; font-size: .88em;
         font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", monospace; }
  pre  { background: transparent; border: 1px solid var(--bo-line);
         border-left: 4px solid var(--bo-blue); border-radius: 6px;
         padding: 14px 16px; overflow-x: auto; line-height: 1.55; }
  pre code { color: var(--bo-black); padding: 0; }

  ul, ol { line-height: 1.65; }
  li::marker { color: var(--bo-muted); }

  table { border-collapse: collapse; width: 100%; margin: 14px 0; background: transparent; }
  th { background: transparent; color: var(--bo-blue); text-transform: uppercase;
       font-size: .78em; letter-spacing: .05em; font-weight: 600; padding: 8px 10px;
       border-bottom: 2px solid var(--bo-blue); text-align: left; }
  td { padding: 8px 10px; border-bottom: 1px solid var(--bo-line);
       font-size: .92em; vertical-align: top; }

  blockquote { border-left: 4px solid var(--bo-blue); background: transparent;
               margin: 12px 0; padding: 10px 14px; color: var(--bo-black); }

  /* Inline value / aside hooks */
  .v   { font-weight: 650; color: var(--bo-blue); letter-spacing: -.005em; }
  .mut { color: var(--bo-muted); }

  /* Confidence ratings â€” the one place orange is earned.
     Verified facts stay blue; anything unresolved or single-sourced goes
     orange, with the weakest tier darkened. */
  .pill { display: inline-block; font-size: .75em; font-weight: 600; letter-spacing: .02em;
          padding: 2px 9px; border-radius: 99px; background: transparent;
          border: 1px solid currentColor; vertical-align: baseline; }
  .pill.high { color: var(--bo-blue); }
  .pill.med  { color: var(--bo-orange); }
  .pill.low  { color: var(--bo-orange-deep); }
  .pill.na   { color: var(--bo-muted); }
</style>
