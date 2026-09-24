<style>
  /* Color hierarchy — YK palette (light-bg variants) */
  /* Purple = hero (one moment per page). Blue = workhorse structure. Dark = body. */
  h1, h2, h3 { color: #0B5FC0; border-bottom: 1px solid rgba(11,95,192,0.25); padding-bottom: 6px; }
  h1 { color: #692D9A; border-bottom: 2px solid rgba(105,45,154,0.45); }
  .hero { color: #4A1F7A; font-weight: 700; font-size: 1.15em; background: linear-gradient(90deg, rgba(170,77,230,0.08), transparent); padding: 8px 12px; border-left: 4px solid #692D9A; border-radius: 4px; display: block; margin: 12px 0; }
  .accent { color: #0B5FC0; font-weight: 600; }
  .quote { color: #4A1F7A; font-style: italic; border-left: 3px solid #692D9A; padding: 8px 12px; margin: 12px 0; background: rgba(105,45,154,0.05); }
  table { border-collapse: collapse; width: 100%; }
  th { color: #0B5FC0; border-bottom: 2px solid #0B5FC0; padding: 8px; text-align: left; background: rgba(11,95,192,0.05); }
  td { padding: 8px; border-bottom: 1px solid rgba(11,95,192,0.15); }
  hr { border: none; border-top: 1px solid rgba(11,95,192,0.25); margin: 24px 0; }
  strong { color: #1F1B2E; }
  code { color: #692D9A; background: rgba(105,45,154,0.08); padding: 1px 6px; border-radius: 4px; }
</style>

# Beyond the CPI: How Private Data and AI Are Rescuing US Statistics

> The BLS didn't break in 2025 — it started breaking in 2020, and now AI is the only thing that can keep the numbers honest.

---

## 🧠 Core idea

Here's what's actually going on: **America's official economic statistics — the payroll numbers, the CPI, the data the Fed lives by — are cracking, and the fix won't come from Washington alone.**

The author's packed-room topic — "Ensuring the Quality of US Statistics" — would have been a yawn a decade ago. Now, after the BLS commissioner was fired, a third of senior leadership walked out, and the longest-ever shutdown simply erased the October 2025 CPI, it's urgent. The pandemic broke collection for good (in-person surveys stopped, response rates never recovered), e-commerce made the CPI's monthly, brick-and-mortar methods obsolete, and the AI boom is making inflation itself harder to measure. The story isn't really about a troubled statistical agency — it's about **who will measure the economy when the old tools can't keep up, and how the private sector is quietly building that new toolkit with AI.**

## 🔄 What changed

**Before (pre-2020): The calendar economy**

A world where economists and traders lived by the BLS release calendar — payrolls, CPI, retail sales, once a month, on time. In-person price collectors, phone surveys, and a 2,000-person BLS machine built for accuracy over speed. It worked because the economy moved slowly enough to wait.

**The trigger — three forces hitting at once:**

1.  **Timeliness vs. accuracy.** Central banks and traders need answers *now*; statistical agencies need more time to get them *right*. That tension exploded during COVID and never eased.
2.  **Collection collapse.** Lockdowns forced BLS to suspend in-person collection. Nonresponse spiked — and never fully recovered. What was an emergency became a structural hole.
3.  **An economy that outran its ruler.** Prices moved online (changing daily, not monthly), geography stopped mattering for pricing, and quality — especially AI — became unmeasurable. *"Suppose a coding assistant costs the same as six months ago but is twice as capable. Has inflation really remained unchanged?"*

**After (2020-2026): The frontier moves private**

Demand for private data ramped up. The author — a former Fed / White House CEA economist who once scraped cellphone tower traffic and payroll scheduling data when official collection failed — now points to a parallel system: web-scraped prices (Billion Prices Project, Adobe's millions of transactions, Truflation), payroll and payments firehoses, and AI reading thousands of earnings calls. Fed Chair Kevin Warsh has formed a task force on the problem. The market no longer just forecasts the BLS — it hunts for macro signals in higher-frequency, esoteric data that can separate you from the pack.

**The structural shift:** From a single official scorekeeper to a split system — **government sets the standard; the private sector expands the frontier.** Rigor and transparency stay in Washington; flexibility, detail, and speed move to where AI and big data live.

## 💰 Why it works

Watch the numbers — they tell the policy story before the narrative does:

| What broke | The size of the miss |
|---|---|
| **2021 payroll revisions** | Revised **up by 1.9 million** jobs (cumulative). With accurate data, the Fed would have hiked sooner. |
| **2024 & 2025 payroll revisions** | Revised **down by >1 million** each year — the opposite error, delaying rate cuts. |
| **October 2025 CPI** | **Not published at all** — shutdown erased it during peak tariff-cost uncertainty. |
| **Inflation bias (1990s precedent)** | Greenspan testified CPI was biased **upward by 0.5–1.5 pp** annually because it couldn't price computer quality. AI repeats the problem. |
| **Bloomberg Price Project** | Tracks **~140,000 products** and **>321,000 monthly prices** — about **3×** the official CPI sample, built from the ground up on BLS methodology. |
| **BLS staffing** | **~2,000 people** to collect, validate, and review everything. AI agents can now do the first-pass screening they do. |

The **load-bearing number** is that **3× coverage**. It proves private data isn't a small supplement — it's a higher-resolution picture of the same basket, granular enough to catch what headline inflation hides (like the current spike in hard drives, SD cards and memory modules driven by the AI build-out itself). The small number that explains the mechanism: **0.5–1.5 pp** — the quality-adjustment error that already fooled the Fed once in the 1990s and is about to again if we can't price AI correctly.

And the complementary logic the author stresses:

| | **Official data** | **Private / alternative data** |
|---|---|---|
| **Strength** | Rigor, consistency, transparency | Flexibility, detail, freedom to explore |
| **Weakness** | Slow, cautious, budget-constrained (years experimenting with scanner data, never adopted) | Needs methodology discipline; risks without a standard |
| **AI role** | Augment field staff — screening and validation | Scale — LLMs parsing hundreds of earnings transcripts, web-scraping millions of prices |

## 👀 Hidden insight

**1. Revisions *are* monetary policy errors in disguise.**

The source mentions 1.9M up then 1M+ down almost in passing, but that's the whole Fed story. When the labor data was understated in 2021, the Fed stayed loose too long and inflation took off. When it was overstated in 2024-25, the Fed stayed tight too long and delayed cuts. The cost of bad collection isn't abstract credibility — it's the wrong interest rate for millions of people. The BLS nonresponse rate isn't a footnote; it's a policy variable.

**2. The BLS didn't fail to modernize — it *couldn't*.**

> *"The BLS has spent years experimenting with scanner data and other new sources, but it never fully adopted those practices because of its caution and budget constraints."*

That line is easy to miss. It's not that official statistics are behind because they didn't notice e-commerce. They noticed, tested the fix, and couldn't deploy it. Caution (methodology has to be defensible in Congress) and budget (2,000 people, shutdowns) are structural brakes. Private players — Adobe, Truflation, Cavallo and Rigobon at Harvard/MIT — moved faster *because* they don't carry that burden. The gap isn't closing; private data will structurally keep pulling ahead.

**3. AI is both the problem and the patch — at the exact same time.**

This is the twist the author sets up with Greenspan and leaves you to connect. AI breaks measurement: if a coding assistant doubles in capability at the same price, the CPI says zero inflation while productivity has soared — we understate growth the same way we missed computer quality in the late 1990s. But AI also *fixes* measurement: AI agents validate BLS data, LLMs turn the Fed's folksy Beige Book into Bloomberg's Orange Book — AI reading thousands of earnings calls for hiring, pricing, and investment signals. During the Iran war oil spike, that Orange Book prevented a reflexive recession call because executives were still describing healthy demand and accelerating defense/AI orders. The tool that blinds the old ruler is the lens for the new one.

## ⚠️ Open question

Can this split system hold trust?

Official stats survive on legitimacy — everyone agrees the CPI is the CPI. Private data survives on edge — investors pay for a better read than the next person. What happens when the most sophisticated statistical system in the world leans on private filters that are faster but proprietary, and when the politics (a fired commissioner, a missing October CPI, a third of leadership gone) make even the official number feel contestable?

And the harder question underneath: if AI lets companies produce more with fewer employees — as executives are already telling the Orange Book — earnings calls will show it months before payrolls do. Who decides that trade-off matters for policy, and who gets to see the early window first?

---

<span class="hero">🎯 The one-line takeaway:</span>

<span class="hero">*The future of measuring the US economy won't be Washington or Wall Street alone — government will set the standard, but private data and AI will expand the frontier, and the Fed's next mistake will come from whichever side it trusts too much or too little.*</span>
