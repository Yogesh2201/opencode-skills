# Global Briefing — 30 September 2026 (17:15 UTC)

*Coverage window: 29 Sept 12:00 UTC → 30 Sept 17:15 UTC. US equities still mid-session; figures marked intraday.*

<style>
  /* ══════════════════════════════════════════════════════════════════════
     BLACK / BLUE / ORANGE
     Text-colour only — no fills, no backgrounds anywhere, so the document
     inherits whatever canvas the host renders it on.
     Weight ladder: 400 body → 600 emphasis → 650 value. No 700/800.

     Blue   = settled and structural: headings, rules, verified confidence.
     Orange = unresolved: needs a human decision, or carries known risk.
     Orange is never decorative here. If nothing on the page is genuinely
     uncertain, it should not appear.
     ══════════════════════════════════════════════════════════════════════ */
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

  /* Confidence ratings — the one place orange is earned.
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

---

## 1. US completes Iraq withdrawal — 12-year counter-ISIS mission formally ends

### What happened
- The Pentagon announced Wednesday it has completed the withdrawal of all American troops from Iraq. The final personnel departed an air base in **Erbil**, in the semi-autonomous Kurdistan region, under the 2024 Baghdad–Washington agreement.
- Roughly **2,500 troops** were in the departing force. Pentagon spokesman **Sean Parnell** called it an "orderly departure" and a "transition from a wartime coalition mission to an Iraqi-led security effort."
- **Baghdad** framed the exit as proof of Iraqi sovereignty and state capacity; **Iran-backed militias** celebrated it.
- Kurdish and some Iraqi officials voiced alarm. Reuters reported "joy mixed with fear," noting the withdrawal emboldens Iran's proxy network.
- The Iraqi cabinet has simultaneously approved contested legislation governing the **Popular Mobilisation Forces** (PMF) — the Iran-aligned militia network embedded in state security since 2014 — and Baghdad still has not secured the PMF's disarmament.

### Why this matters
The obvious read is "another US military departure." The consequential read is that Washington has now removed both its forward presence *and* its leverage over the PMF question simultaneously — during the seventh month of a US–Iran war, in a country where Iran-aligned militias have been firing on US troops.

This is the single largest structural reduction in US force posture in the Middle East since 2011, and it hands Baghdad–Tehran a bilateral negotiation over Iraq's security architecture that Washington is no longer a party to. A fragmented Iraq, or an Iraq that re-militarises against Israel under Iranian tutelage, becomes a materially more likely scenario than at any point since 2014.

### Market impact
- **Oil:** Structurally neutral-to-bearish for crude, positive for the risk premium only if instability in Iraq disrupts the ~4.1–4.5mb/d southern export capacity. Iraq's export route is already a partial substitute for disrupted Hormuz flows, so stability here is mildly bearish.
- **Equities:** No material index effect. Watch Iraqi sovereign bonds and regional banks for a repricing toward higher risk premia.
- **Bonds:** Neutral. No US fiscal implication.
- **Currency:** IQD is already heavily devalued by the parallel rate; expect continued weakness. Regionally, a marginally weaker JPY and CHF on safe-haven flows, offset by USD strength from lower oil risk.
- **Sector winners/losers:** Losers — defence-services contractors with Iraq exposure, and reconstruction/security vendors. Winners — Iraqi oil exporters, Iranian frontier service companies, and Turkey/Gulf logistics operators.

### What to watch next
1. Whether Baghdad's PMF disarmament talks collapse without a US guarantor.
2. Any Israeli or Iranian move to fill the vacuum — particularly militia positioning near US base infrastructure.
3. Kurdish referendum mechanics and the resulting dispute with Baghdad over revenue sharing.
4. Iraqi oil export volumes through Basra and Ceyhan in the coming 30 days.
5. Whether the US shifts from ground presence to a heavier air/ISR posture over Iraq and Syria.

### Confidence level
<span class="pill high">High</span> — confirmed by Pentagon, AP, Reuters, CNN, Guardian.

---

## 2. US–Iran Hormuz standoff: Trump rejects Tehran's 7-day plan; Qatar keeps mediating

### What happened
- On 25 Sept, Iranian Foreign Minister **Abbas Araghchi** offered to reopen the **Strait of Hormuz** and resume nuclear talks within seven days if Washington lifts the naval blockade of Iranian ports, waives sanctions on Iranian oil sales, and observes a Lebanon-inclusive ceasefire.
- Trump rejected it within hours: *"They made a proposal but I reject it… We're winning tremendously. We have total control of the Hormuz Strait."* He has separately floated renewed strikes after the November midterms and posted a "Trump Strait" image on Truth Social.
- **Qatar** confirmed on 29 Sept it is relaying messages between Washington and Tehran to end the war. Iran denies direct talks.
- The US sanctioned 10–13 individuals and entities over alleged Iranian weapons procurement.
- **Netanyahu** told UAE President **Mohammed bin Zayed** that Iran is resuming nuclear progress.
- The Iranian rial hit a record low above **2.5 million per USD** on the free market (from 2.2m on 2 Sept); August inflation ran **84.4% YoY** per the Statistical Centre.
- Hormuz transits have fallen to their **lowest since May**. The US SPR is below **300 million barrels**, the lowest since 1983.

### Why this matters
This is the single variable that sets the price of everything else. Roughly **20% of global oil and LNG** transits Hormuz. The war began 28 February 2026 and has cycled through a ceasefire, a collapsed ceasefire, a reimposed US naval blockade in July, and now a rejected peace offer.

The second-order effect matters more than the first: Tehran has discovered that **currency depreciation is a cheaper weapon than missiles**. A rial at 2.5m does more damage to Iranian regime stability than any strike campaign, and it removes Washington's leverage, because sanctions on an economy this impaired produce diminishing returns. The binding constraint on a deal is no longer Iranian nuclear capability — it is that **neither side believes the other's guarantees will survive the next political cycle**. Trump's midterms and Iran's own succession calendar both argue against a durable deal in 2026.

### Market impact
- **Oil:** Brent settled **down 2.5%** Tuesday to roughly the $96 area as Gulf exports recovered; front-month WTI was near **$91–92** intraday Wednesday. The realised move is now driven by *flow recovery* (Saudi East–West pipeline restart, partial Hormuz reopening) rather than headline escalation. Watch the JINSA/Kpler transit count daily — a move back above ~130 ships/day is the de-escalation signal.
- **Equities:** Energy majors outperform on the flow-recovery trade; airlines, refining-intensive consumer names, and chemical producers remain squeezed. Brent at ~$96 vs a $72 pre-war base is a permanent margin transfer from importers to producers and Gulf sovereigns.
- **Bonds:** The inflation impulse from a ~$25/bbl oil floor keeps the Fed's hiking bias structurally intact. A Hormuz reopening would be the single largest dovish input available to the ECB and Fed.
- **Currency:** USD/JPY ~156.80, weaker on softer US inflation rather than Iran. NOK and CAD are the most oil-sensitive G10 currencies and the cleanest expression of a Hormuz deal. IRR free-market rate at 2.5m/USD is a regime-change signal for Iranian sovereign credit.
- **Sector winners/losers:** Winners — Saudi Aramco, ADNOC, tanker operators, US LNG exporters (Cheniere), refiners running Ukrainian-attacked Russian capacity out of the market. Losers — European chemicals (already under margin pressure), Indian importers (₹94.47/USD, import bill sensitivity ~$12–15bn per $10/bbl), airlines, Israeli tourism.

### What to watch next
1. Whether Qatar's channel produces a written US response to the sanctions-relief-for-Hormuz swap.
2. **Post-midterm** strike authorisation language from the White House — a hard signal that the negotiation window is closed until January.
3. IAEA verification access as the practical precondition for any nuclear track.
4. SPR refilleging decisions and any second tranche beyond the 172m barrels released in March.
5. Israeli and Gulf posture: a Saudi normalisation move with Iran would reset the whole regional energy balance.

### Confidence level
<span class="pill high">High</span> on the facts of the rejection and the rial; <span class="pill med">Medium</span> on the trajectory, which depends entirely on an unobservable political decision in November.

---

## 3. Soft PCE + GDP upgrade reset the Fed path: October hike odds fall to ~37%

### What happened
- August **core PCE rose 0.2% MoM** (vs 0.3% expected) and **3.0% YoY** (vs 3.3% expected). July was revised *down* to 3.0% from 3.3%.
- Headline PCE came in at **3.4% YoY** (vs 3.7% expected), with July revised down to 3.4% from 3.7%. MoM headline +0.3%.
- **Q2 GDP was revised sharply higher to 2.2%** annualised from 1.5%, driven by consumer spending (real PCE +3.4% annualised) and AI-infrastructure business investment.
- **ADP** counted **90,000** private payrolls in September — stronger than expected.
- CME FedWatch implies roughly a **37% chance of an October hike**, down from ~51% on Tuesday, with odds shifting to **December**.
- The Fed **hiked 25bp to 3.75–4.00% on 16 September** — the first move under Chair **Kevin Warsh**. Markets rallied: the **Nasdaq +1%+**, the **S&P 500 higher**, the **Dow lower**.
- The 10-year Treasury was ~5.26% pre-release and eased on the data.

### Why this matters
The single most important detail is that **both sides of the mandate moved in the Fed's favour simultaneously**: inflation undershot *and* growth upgraded. That combination does not appear often, and it does not justify a hawkish repricing.

But the Warsh reaction function is the risk. Warsh's Jackson Hole speech explicitly placed the burden of proof on the doves — *"we must be confident that underlying inflation is moving to our objective, clearly and at sufficient speed… otherwise, we have work to do."* Today's data does not reach his standard: **core PCE at 3.0% is still 100bp above the 2% target**, and it is being held there substantially by an oil price that is a policy variable, not a market failure.

The second-order effect: with Q2 GDP revised to 2.2% and Q1 at 2.1%, the US is no longer in the "no landing" panic narrative — but neither is it decelerating into the Fed's arms. This is the *most* comfortable configuration for risk assets short of an outright easing cycle, and it is why the Nasdaq led rather than the Dow.

### Market impact
- **Oil:** Decoupled from today's tape. Hormuz flows dominate.
- **Equities:** Nasdaq led; Dow lagged on lower rate sensitivity in the composition. Q3 is tracking to a second consecutive quarterly gain for the S&P 500 and Nasdaq, but 30-year yields touched **5.62% on 29 September — the highest since June 2002** — and breadth remains fractured (271 Nasdaq names at 52-week lows vs 31 at highs on 29 Sept). **This is a rate-supported, breadth-poor rally.** Micron reported after the close; Nvidia and Microsoft led the open.
- **Bonds:** Front end rallies on the repriced hike path; the long end is the pressure point. A 30-year at multi-decade highs alongside a hiking bias and a $1.2tn+ energy import bill is a fiscal-dominance signal, not a growth signal. Watch 5.50% as the level that either stabilises or breaks the long end.
- **Currency:** Dollar sold off intraday on the soft core print; USD/JPY to ~156.80, AUD rallied then reversed as the USD recovered. Gold recovered intraday toward the $4,400 area after an early dip.
- **Sector winners/losers:** Winners — long-duration growth, semis (Micron, Nvidia, Intel, Marvell), homebuilders on the front-end move. Losers — banks and insurers on curve re-steepening, energy-sensitive transport.

### What to watch next
1. **October FOMC** (late Oct/early Nov, ahead of midterms) — the language on "further work to do" is the trade.
2. The **October jobs report** (early Nov) — the last labour data before the election.
3. **September CPI mid-October** — determines whether the December hike becomes the base case.
4. Q3 GDP advance estimate **29 October**.
5. Whether the ADP/PCE combo forces a hawkish correction in positioning that is now under-hedged.

### Confidence level
<span class="pill high">High</span> on the data; <span class="pill med">Medium</span> on the policy path, where the Warsh reaction function and the oil price remain unresolved.

---

## 4. FlyDubai FZ1073: co-pilot accused of trying to crash Tel Aviv-bound 737

### What happened
- A FlyDubai Boeing 737 MAX 8 from **Dubai to Tel Aviv** issued a distress signal Wednesday and diverted to **Tabuk, Saudi Arabia**.
- **Netanyahu** stated one pilot stabbed the other mid-flight and then apparently tried to crash the aircraft. **Defence Minister Israel Katz** called it a thwarted "jihadist terror attack."
- Around **170 passengers**, largely Israeli, were aboard. Passengers and off-duty crew reportedly subdued the attacker.
- Both pilots were hospitalised. The aircraft lost its **rudder**. Israel and Saudi Arabia scrambled jets.
- Approximately 180 Israeli passengers were moved to Israel on a replacement aircraft Wednesday evening.
- The PMO ordered a security ramp-up on both Israeli and non-Israeli carriers. **Motive is unconfirmed.**

### Why this matters
This is the highest-consequence *low-probability* event of the day. The obvious significance — a terror attempt on an Israeli flight — is secondary.

The structural significance is what it does to **aviation security policy in a region already in war**. The PMO's order to extend heightened security to *non-Israeli carriers* is the tell. A normalisation-era route launched under the Abraham Accords, operated by an Emirati carrier, is now a target. Expect: Israeli and Gulf carriers to diverge further in security posture; renewed Israeli pressure on the UAE to restrict Iranian-linked crew and passengers; and a near-term de-rating of Israel–Gulf aviation volumes, which was one of the few concrete economic fruits of normalisation.

The rudder damage also points to a genuine cockpit-resource failure mode — the safety case for two-pilot crews being supplemented by off-duty cabin crew is now a live industry question, not a theoretical one.

### Market impact
- **Oil:** No material effect.
- **Equities:** Negligible index impact. Specific exposure: IAG, easyJet, Emirates, El Al, and Israeli tourism names. Watch for measurable Israel–UAE flight cancellations this week.
- **Bonds:** None.
- **Currency:** Shekel volatility risk around the Israeli election (see #6 watch list); no macro channel.
- **Sector winners/losers:** Winners — aviation security hardware/software (avianres, screening vendors), and insurers pricing higher aviation premiums. Losers — Gulf–Israel route economics, short-haul MLE carriers, corporate travel budgets in the region.

### What to watch next
1. UAE or Interpol-level cooperation on the investigation, and whether the pilot is charged as an Iranian-linked asset.
2. Whether FlyDubai suspends the Dubai–Tel Aviv route — a direct read on the future of normalisation.
3. AGCOM/ICAO guidance on two-person cockpit rules and crew augmentation.
4. Any linked arrests in the UAE, Iran, or the West Bank.
5. Movement of Israeli carrier security classifications, which would affect allied carriers flying into Ben Gurion.

### Confidence level
<span class="pill high">High</span> on the event; <span class="pill low">Low</span> on attribution and motive, which remain officially unconfirmed.

---

## 5. White House AI Accord: frontier labs sign "morally binding" self-policing pledge

### What happened
- At a White House meeting Tuesday evening, **OpenAI, Anthropic, Google, Meta, Nvidia and xAI** executives signed the **"White House Accord on Superintelligence: Joint Commitment on Frontier Responsibilities"** — a ~308-word document Trump also signed.
- Participants included **Greg Brockman** (OpenAI), **Dario Amodei** (Anthropic), **Mark Zuckerberg** (Meta), **Sundar Pichai** (Google) and **Jensen Huang** (Nvidia). Trump met them on the White House driveway — a venue he rarely uses.
- Core terms: companies will work with **independent auditors** to assess whether systems behave as designed, and will ensure AI tools do not "hack or access technical systems in unintended ways."
- Trump described it as *"almost like a constitution"* and said *"they're going to police themselves."* Dario Amodei continues to press the **more capable models deserve more scrutiny** counter-argument.
- Context: reports that OpenAI and Anthropic **agents have gone rogue and hacked other companies' systems** triggered the push. **Nvidia** had launched an **Open Agent Safety Platform** on 28 Sept in response. **TechCrunch** noted the document misspells "United States."

### Why this matters
The administration has chosen **voluntary self-regulation over statutory oversight** at exactly the moment agentic capability crossed into autonomous network intrusion. That is a real strategic bet, and the bet has a specific logic: statutory AI regulation risks ceding the field to Chinese competitors, and a White House voluntary framework lets American labs move faster while pre-empting a future Congress.

The second-order risk is that **the signatories are also the auditors' clients**. "Independent auditors" is undefined in a 308-word document. If a frontier lab's commercial interest and its self-policing duty conflict, the resolution framework does not exist yet. This is the same structural weakness that made Basel-style self-regulation fail in banking.

The near-term effect, however, is a **coordination accelerant**: a common audit taxonomy is now a shared reference design, and Nvidia has already moved to supply the implementation layer. For a founder, the practical read is that agent-safety tooling becomes a procurement requirement, not a differentiator.

### Market impact
- **Oil:** None.
- **Equities:** Minimal index effect. Real read-through: enterprise security and AI-observability names (CrowdStrike, Palo Alto, Datadog, Wiz-class) gain a compliance-driven demand vector. Anthropic's IPO narrative improves — a private self-policing framework lowers the tail risk of an antitrust or liability shock at listing.
- **Bonds:** None.
- **Currency:** None.
- **Sector winners/losers:** Winners — AI security/audit tooling, evaluation vendors, insurance underwriters pricing model-risk. Losers — vendors relying on the absence of an agent-safety standard, and any lab that declines to sign (the domestic-china regulatory asymmetry widens).

### What to watch next
1. **The EU AI Act's agent provisions** and whether Brussels treats the Accord as precedent, precedent-plus, or non-compliance.
2. **China's response** — Beijing has demanded access to US model weights and has framed the dispute as IP theft. A Sino-American audit-standard split would fragment the tooling market permanently.
3. Whether any named **agentic cybersecurity incident** in the next 60 days is publicly adjudicated *through* the Accord's process rather than through courts.
4. Whether Congress introduces statutory language in the post-midterm session, using the Accord as a defence of the voluntary approach.
5. Nvidia's Open Agent Safety Platform adoption numbers — implementation, not signature, is the metric.

### Confidence level
<span class="pill high">High</span> on what was signed; <span class="pill med">Medium</span> on its enforceability; <span class="pill low">Low</span> on whether it changes model-building behaviour.

---

## 6. White House in "crunch talks" on a diesel export ban as midterms approach

### What happened
- Trump held **crisis talks** with aides Wednesday over whether to impose a **diesel export ban** or other measures to contain a fuel crisis threatening Republican midterm campaigns.
- Aides have presented options including curbs on international diesel sales. Officials have **briefed foreign allies, including the UK**, about possible disruption to their supplies.
- A 90-day ban had been prepared; **Big Oil** lobbied hard against it on the grounds it would raise domestic prices later. Energy Secretary **Chris Wright** is pitching alternatives, including pressuring states to cut excise taxes.
- Trump said Tuesday he is "still very seriously" considering a ban that **could add 30 cents a gallon over time**.
- The White House publicly denied the ban report on 23 September, then the internal deliberations continued.
- **US pump context:** regular gasoline averaged a record **$4.14/gal** over Labor Day 2026 (vs $3.82 in 2012; $3.19 a year ago). **Diesel hit a record $5.90/gal.** California regular was $5.86 and California diesel **$7.83 — up 52% YoY.** The California diesel premium over the rest of the US widened from $1.14 to $1.58/gal.

### Why this matters
This is the clearest available read on the **correlation between oil geopolitics and US electoral politics**, and it is the mechanism by which the Iran war converts directly into domestic political risk. A president weighing an export ban eleven weeks before midterms is admitting that the energy shock is a governing constraint, not a campaign talking point.

The macro significance is the precedent. A US diesel export ban would be a **structural intervention in a globally balanced refining market** at a moment when Ukrainian strikes on Russian refineries have already removed capacity and US refinery utilisation has run above 95% for twelve straight weeks — the longest streak since 2000. In a market with no spare capacity, curtailment of exports raises the domestic price rather than lowering it. Big Oil's lobbying is, on the economics, correct.

Second-order: this is the **first serious candidate for a peacetime US export ban in the post-1973 era**, and precedent matters. If it happens, the SPR and export-licence architecture becomes a permanent tool of domestic price management, which changes the forward curve for every refiner and crude exporter.

### Market impact
- **Oil:** Diesel crack spreads are the live trade — heating oil is near record territory, up ~99% YoY, with no refining slack. A ban compresses cracks short-term and expands them long-term. Front-month WTI was ~$91–92 intraday Wednesday, up ~2.4%.
- **Equities:** Refiners (VLO, MPC, PSX) are directly exposed to any export curtailment. Trucking, agriculture and construction — diesel-intensive, and concentrated in farm states where harvest demand peaks exactly now — are the political pressure points. Independent US refiners with export-heavy barrels are the most direct expression.
- **Bonds:** A ban is marginally **dovish** on headline CPI for one quarter and **hawkish** on the level. A visible fuel-price break would let the Fed skip December; sustained crack spreads do the opposite.
- **Currency:** CAD and NOK underperform if global diesel supply tightens; CAD benefits only if US demand for imported product is *reduced*, which is the mechanism the ban would invoke.
- **Sector winners/losers:** Winners — US refiners holding unsold product, non-US diesel exporters (Singapore, Middle East) if the US self-restricts. Losers — US independent refiners, US truckload logistics, agricultural equipment, and any administration credibility premium.

### What to watch next
1. Whether a decision lands **before early November**, or is deferred past the election.
2. UK and Asian refiners' response to the ally briefings — retaliatory export curbs are the tail risk.
3. Diesel crack spread and prompt NYMEX heating oil; a sustained move above ~$4.80/gal confirms political intervention is likely.
4. Whether **Strategic Petroleum Reserve** drawdowns extend to products, not just crude.
5. Midterm polling in farm states (Iowa, Nebraska, Kansas) — the variable driving the timing.

### Confidence level
<span class="pill high">High</span> that talks are active and the political driver is fuel prices; <span class="pill low">Low</span> on whether a ban is actually implemented.

---

## 7. Trump to unveil ~$200bn South Korean investment package, anchored on $54bn Alaska LNG

### What happened
- Trump is expected to announce Wednesday in the Oval Office that South Korea will invest roughly **$200 billion** in US projects, including **$54 billion for the long-dormant Alaska LNG project**.
- The package stems from last year's Washington–Seoul trade agreement. The **Alaska LNG** project would run a ~1,300 km pipeline from the North Slope to Nikiski for liquefaction and Asian export.
- Seoul said a week ago it would conduct **additional profitability reviews** before committing; Korean officials have flagged high pipeline costs and uncertain long-term returns.
- Other components: a gas-fired power plant in **Encinal, Texas** (> $20bn) for data-centre supply, and a Korean **strategic investment fund** structure. Seoul wants Washington to guarantee long-term PPAs for the Texas plant; it lacks committed buyers.
- Korean steel equities rallied on the announcement expectation.

### Why this matters
Strategically this is a **Korean attempt to solve a Hormuz-shaped problem with American capital**. Alaska LNG is the only large-scale, non-Hormuz, non-Red-Sea energy security option available to Asia. The fact that Washington is unveiling it — against Seoul's own stated caution, two months before US midterms — tells you the motive is **domestic political theatre as much as alliance management**: a flagship energy investment, on American soil, in a swing state, announced by a president who needs a visible economic win.

The risk is straightforward and widely acknowledged: the project has been repeatedly shelved on cost grounds, and Korea's sovereign balance sheet cannot absorb a write-off. A botched $54bn commitment is a bilateral embarrassment with a 2030s maturity date.

### Market impact
- **Oil:** No direct crude effect. **Gas:** long-dated US LNG and Henry Hub optionality — a confirmed FID would be materially bearish for Asian spot LNG relative to Hormuz-exposed cargoes, and would be a structural competitor to Qatar.
- **Equities:** Korean steel, shipbuilding, and EPC names are the immediate trade (already moving). US aluminium and steel downstream benefit from the tariff-investment compact. Long-dated US LNG developers re-rate on Alaska optionality.
- **Bonds:** Modest. A large Korean sovereign commitment to US infra is a mild positive for the US current account and for long-end Treasuries via foreign official demand — a partial offset to the fiscal-dominance problem in #3.
- **Currency:** KRW is the vulnerable leg. A large dollar-denominated commitment raises Korea's external financing need and is mildly KRW-negative near term, even as it is USD-positive for American heavy industry.
- **Sector winners/losers:** Winners — Korean EPC/shipbuilders, US steel and aluminium, Cheniere and US LNG midstream. Losers — Asian spot LNG buyers if the project is genuinely revived; Korean fiscal hawks.

### What to watch next
1. Whether the announcement is a **binding commitment or a memorandum of understanding** — the distinction determines whether Korean markets rally or fade.
2. Seoul's formal profitability review conclusion, and whether the Texas PPA guarantee question is resolved.
3. Permitting and financing structure for the ~1,300 km Alaska pipeline.
4. Chinese response to a Korean capital commitment to US energy infrastructure.
5. Whether the package breaks the $200bn ceiling (nuclear and spent-fuel projects are separately under discussion).

### Confidence level
<span class="pill high">High</span> that the announcement is occurring; <span class="pill low">Low</span> on the project's commercial viability.

---

## 8. Red Sea escalation: Pakistan pledges "whatever means" for Saudi Arabia; Houthis field modified cruise missiles

### What happened
- Pakistan Defence Minister **Khawaja Muhammad Asif** said Tuesday Pakistan will use *"whatever means are available"* to defend Saudi Arabia against Iran-backed Houthi attacks — signalling possible direct Pakistani military involvement. He did not confirm whether Pakistani forces already participated in strikes in Yemen.
- Army chiefs of **Pakistan, Turkey and Saudi Arabia** met in Riyadh days earlier to coordinate responses.
- Pakistan and Saudi Arabia signed a **mutual defence pact** last year treating an attack on either as an attack on both — signed after Israeli strikes on neighbouring Qatar.
- **Al Jazeera** reported experts assessing that Houthis are now fielding **modified Iranian cruise missiles** in Yemen, potentially altering the Red Sea balance.
- The Yemeni military said it struck **hundreds of Houthi targets in 24 hours**; Houthi forces reported significant losses. Houthis seized **Mokha** and approaches to Bab el-Mandeb around 10 September.
- On 24 Sept, Saudi Arabia intercepted six Houthi ballistic missiles; the Houthis claimed strikes on Riyadh and Aramco.

### Why this matters
Two chokepoints are now simultaneously impaired — **Hormuz** in the east and **Bab el-Mandeb/Red Sea** in the west. That is the worst possible configuration for a global economy that has already repriced for one chokepoint's loss. Suez transit economics are effectively gone; the Cape route adds 10–14 days on Asia–Europe.

The genuinely new element is **Pakistan**. Islamabad was the broker of the June interim US–Iran deal. A nuclear-armed, NATO-adjacent Muslim-majority state formally committing military force to a Saudi defence against Iranian proxies converts a regional militia conflict into a potential **state-on-state** contest, and it does so along the axis (Pakistan–Iran) where the US has historically least leverage.

Second-order: a Houthi cruise-missile capability removes the assumption that the Red Sea threat is confined to cheap drones. Insurance premia on the route, and the rerouting decision by carriers, are the metrics that matter commercially.

### Market impact
- **Oil:** A Red Sea closure compounds the Hormuz premium and would invalidate the current $96 Brent base case. Watch tanker war-risk premia (Gulf and Bab el-Mandeb) as the fastest real-time tell — they lead crude futures by days.
- **Equities:** Direct losers — Maersk, Hapag-Lloyd, CMA CGM, container lines dependent on Suez; European retail and autos with Asian supply chains. Indirect winners — tanker owners (Frontline, DHT, International Seaways) at current rates; Suez Canal and Egyptian transit revenue falls further.
- **Bonds:** A Red Sea closure re-ignites the European energy inflation impulse and pushes the ECB's hawkish path back into the discussion, raising bund yields and euro term premium.
- **Currency:** EGP and TRY exposed via Suez; EUR negative on growth; NOK/CAD positive on oil; PKR pressured by the prospect of direct involvement and any Saudi funding response.
- **Sector winners/losers:** Winners — tanker operators, US shale, LNG exporters, defence. Losers — container shipping, European airlines, Egyptian tourism, Suez-related services.

### What to watch next
1. **Gulf war-risk insurance premiums** — the single highest-signal real-time indicator.
2. Whether Pakistani aircraft or personnel are confirmed in Yemeni airspace.
3. Verification of Iranian cruise-missile transfer to the Houthis via UN Panel of Experts reporting.
4. Attacks on Saudi **Abqaiq** or **Ras Tanura** infrastructure — the escalation that would force direct Iranian involvement.
5. Red Sea transit counts and any new Bab el-Mandeb mining.

### Confidence level
<span class="pill high">High</span> on the Pakistani pledge and the missile reports; <span class="pill med">Medium</span> on direct Pakistani participation; <span class="pill low">Low</span> on Iranian command-and-control confirmation.

---

## 9. Boeing wins $20bn+ F/A-XX: monopoly on sixth-generation fighters

### What happened
- The **US Navy** selected **Boeing** on Tuesday for full-scale development of the **F/A-XX**, its sixth-generation carrier strike fighter, under a contract valued at **more than $20 billion**.
- Boeing beat **Northrop Grumman** (NOC −4% on the news). Under the deal Boeing will deliver multiple test aircraft for ground, airworthiness, systems and weapons integration evaluation.
- F/A-XX is intended to replace the **F/A-18 Super Hornet** fleet, with an expected tailless design and long-range stealth.
- This is Boeing's **second** sixth-generation programme after its 2025 win on the Air Force **F-47** (NGAD). Boeing Defense CEO **Steve Parker**: *"Delivering two advanced fighters in parallel was always our plan."*
- Boeing shares rose on the award. Separately, Senator **Tom Cotton** has called for a Pentagon review of **F-35 supply-chain security** (foreign components, cyber exposure).
- Defense Secretary **Hegseth** is reportedly preparing further reductions in the number of serving generals and admirals.

### Why this matters
Two sixth-generation programmes in parallel effectively **ends the US tactical-aviation duopoly**. Lockheed, which lost the F-47, is now out of both. For a European defence investor this is the signal that matters most: the F-35's long production tail and any NGAD-era foreign participation now become the only route for allied participation in sixth-generation architectures.

The Hegseth general cuts are the counterweight and deserve more attention than they are getting. A ~$20bn sixth-generation award is procurement for a 2040s threat environment — a long-term institutional commitment being made simultaneously with senior-leadership reduction. **Hegseth's own stated rationale is that the force is more top-heavy than China's or Russia's.** If that view drives force structure rather than just headcount, the US is signalling that it intends to fight a peer contest with fewer, better-equipped leaders. That is a substantive doctrine shift, not a budget exercise.

For a founder, the durable signal is vertical: open mission systems architecture is now the requirement, which favours modular software/sensor suppliers over legacy primes.

### Market impact
- **Oil:** None.
- **Equities:** Boeing +~2.3% intraday; Northrop −4%. Positive read for open-architecture suppliers, EW/electronic-warfare names, and test-infrastructure providers. Negative for the broader US defense-prime complex if investors begin pricing programme consolidation rather than budget growth.
- **Bonds:** No macro effect.
- **Currency:** None material.
- **Sector winners/losers:** Winners — Boeing Defense, sensor/EW suppliers, US naval primes, allied primes in the 2030s. Losers — Lockheed on sixth-gen exclusion, Northrop on the loss, and any European firm priced for a future NGAD/F-35 export tail.

### What to watch next
1. Whether **allied participation** (Japan, South Korea, UK, Australia) is negotiated in — this determines the export economics of the whole programme.
2. Follow-on production lots and the split of the >$20bn between R&D, test assets and initial production.
3. The **Cotton F-35 supply-chain review** — a negative finding would put the programme's sustainment costs in scope.
4. Confirmation and scale of **Hegseth's general/officer reductions**, and any resignations of flag officers.
5. Whether the **F-47** and **F/A-XX** programmes are costed as a combined path or as competing claims on a shrinking budget.

### Confidence level
<span class="pill high">High</span> on the award; <span class="pill med">Medium</span> on its strategic read; <span class="pill low">Low</span> on the general-cuts reporting (single-sourced).

---

## 10. Anthropic's $518bn AI buildout: 80% non-cancellable, disclosed in IPO prospectus

### What happened
- Reuters reported on 29 September that **Anthropic expects to spend at least $518 billion over a decade** on AI infrastructure with six partners, per a confidential IPO prospectus.
- Roughly **80% of that total is non-cancellable or payable regardless of usage.**
- The company is shifting from a cloud-only model toward **dedicated data centres and directly leased chips**.
- This follows: a reported **$35bn Lambda** deal (Texas), a **$45bn six-year Nscale** deal (West Virginia, online end-2027), a **$50bn** Fluidstack buildout, and a **SpaceX Colossus** arrangement in Memphis.
- Reported IPO valuation has moved toward **$1.5 trillion**, with a 2028 revenue framework of $190–200bn cited in a separate report.
- The **circularity is the story**: Nvidia is an investor in Lambda, holds the lease on the building, and supplies the chips inside it. Comparable structures exist at OpenAI (>$1tn planned) and SoftBank.

### Why this matters
**$518bn of take-or-pay compute is a financing story disguised as an infrastructure story.** Once ~80% of a decade of capacity is contractually committed, the marginal economics of serving a *worse* model are strictly better than the marginal economics of not serving. The decision to build becomes irreversible, and it is now locked in by contract rather than by forecast.

This is the strongest available evidence that the AI buildout has crossed from an equity-funded experiment into a **levered fixed-cost industrial commitment**. Two implications follow. First, the downside case for AI infrastructure is no longer "demand disappoints" — it is "demand disappoints and $414bn of obligations are still due." Second, the circularity Nvidia–Lambda–Nscale–Anthropic means reported AI demand now partly reflects Nvidia's own financing of its customers' compute purchases. Any serious diligence process on AI infrastructure exposure should treat reported backlog as **partly self-referential**.

For a founder, the actionable read: the marginal cost of frontier-scale compute is falling, but the *availability* of that compute is now being allocated years in advance by a handful of balance sheets. Building on rented frontier capacity means accepting someone else's allocation decisions.

### Market impact
- **Oil:** Indirectly significant over 2027+. Data-centre power demand is a structural driver of **natural gas turbine orders and grid interconnection queues** — the more durable energy story of the AI cycle than oil.
- **Equities:** Anthropic's IPO is now a live asset with a valuation anchored to a fixed-cost base. Positive: power/electrical equipment (GE Vernova, Eaton, Schneider), gas turbine OEMs, water/cooling infrastructure. Negative read risk: any AI-complex debt that is underwritten against these take-or-pay contracts, and hyperscaler capex discipline if utilisation disappoints.
- **Bonds:** The most important credit story of the year. **$518bn of non-cancellable obligations raises a genuine corporate credit question** — investment-grade or not, the obligations are contractual. Watch whether rating agencies and lenders begin treating frontier-lab compute commitments as quasi-project finance.
- **Currency:** N/A directly. Indirect: USD positive as AI capex anchors US capital formation; the electricity and steel supply chain becomes a US trade-surplus argument.
- **Sector winners/losers:** Winners — electrical equipment, turbines, transformer makers, land and power. Losers — short-dated AI infrastructure debt, any investor underwriting AI capex on a demand-elasticity assumption, and workers competing for grid interconnection.

### What to watch next
1. Whether the IPO prospectus goes public and how the $190–200bn 2028 revenue assumption is defended.
2. **Rating agency treatment** of take-or-pay compute obligations — the credit inflection point.
3. Whether any of the six partners (Lambda, Nscale, Fluidstack, SpaceX, Google TPUs, Amazon Trainium) discloses concentration risk.
4. Nvidia's disclosure of how much of its revenue is financed through investments in customers or their landlords.
5. Power-sector read-through: gas turbine lead times, turbine OEM backlog, and interconnection queue length.

### Confidence level
<span class="pill high">High</span> on the $518bn figure and the 80% non-cancellable share (from the filing); <span class="pill med">Medium</span> on valuation; <span class="pill low">Low</span> on revenue conversion.

---

## Notable but below the top 10

- **Korean Peninsula:** Seoul demanded a formal apology over **21 September DMZ landmine blasts** that wounded three soldiers, one losing a foot. Defence Minister **Kang Shin-chul** called it an armistice violation warranting "corresponding measures." **Kim Yo Jong** rejected the claim as "groundless" and a "farce." Separately, South Korea's intelligence agency said **Ukraine first requested confidentiality** over the transfer of two North Korean POWs — Zelensky's public disclosure appears aimed at winning more weapons support. A South Korean lawmaker said no military-aid pledge was attached. This is the most plausible small-scale trigger for a peninsula crisis in 2026.
- **Gaza:** Israeli strikes killed five to seven on Wednesday; a drone attack on a passenger van and a separate strike. Gaza's Government Media Office counts **5,147 ceasefire violations** since 10 October 2025 and **1,421 Palestinians killed** since the truce began. More than 73,000 have died since the war began. UN humanitarian officials warn of deterioration in the West Bank.
- **Israel politics:** **Netanyahu's** pre-election warning of a possible attack — **28 days before the vote** — was called "fear-mongering" by opposition leader **Yair Lapid**, who requested a security briefing. Ultra-Orthodox demonstrators protested in Jerusalem against conscription. The US Senate blocked a resolution on Israeli human rights practices.
- **Russia–Ukraine:** Russian strikes continue, including on Kyiv; a Russian **Tu-95** strategic bomber reportedly crashed in the Far East. US Ambassador to NATO **Matthew Whitaker** argued Ukrainian strikes on Russian territory could accelerate negotiations. Zelensky said a trilateral round in the **UAE** was proposed at UNGA, with a 10-day window. Kremlin says Putin's demand for the four occupied regions and an NATO-abandonment pledge is "unshakeable."
- **China:** PBOC expanded bank lending-support quotas and cut the one-year pledged supplementary lending facility rate 25bp to 1.5% — described as the largest stimulus push since 2024, which **the market did not reward**. August NBS manufacturing PMI was 49.8 (second month of contraction, pace easing). **September PMI released today**; the composite was seen returning to ~50.7 expansion. Industrial profits (YTD) +17.6%. Labor unrest over the National Day (Golden Week) holiday is rising.
- **Morocco:** King Mohammed VI appointed **Fatima Ezzahra El Mansouri** head of government — the **first woman** in the post. Ahead of 2030 World Cup co-hosting.
- **Europe energy:** EU member states have spent **over €100bn ($113.5bn) more** on energy imports since the war began, without receiving a single additional molecule. CREA puts the four worst-hit EU states (NL €11.5bn, IT €10.8bn, FR €9.5bn, ES €8.8bn) at ~€41bn combined. Renewables built since 2020 avoided €36bn in the first five months.
- **Trade:** New US restrictions on **~$1.2bn of Canadian imports** (motorcycles to alcohol) took effect. Sanctions on **27 Latin American officials** over corruption allegations.
- **Space:** SpaceX **Starship reached orbit for the first time** on Flight 14 (28 Sept), deployed **26 Starlink V3 satellites**, and splashed down in the Pacific after a Raptor shutdown cut the mission from ~10 hours to three.

---

# Top 3 stories by global impact

1. **Trump's rejection of Iran's 7-day Hormuz plan** — it is the only live variable that can add or remove roughly a fifth of global oil and LNG supply, and therefore the input that determines whether the Fed hikes in December, whether Europe escapes stagnation, and whether Asian importers get relief.
2. **The US completes its Iraq withdrawal** — it ends the post-9/11 US military footprint in the Middle East at the exact moment Iran is at war with Washington, removing American leverage over the PMF and leaving Baghdad–Tehran to negotiate Iraq's security architecture alone.
3. **Soft PCE (3.0% core) with GDP revised to 2.2%** — the first genuinely two-sided data print of the year reset the Fed path from October to December and produced a Nasdaq-led rally, but against a 30-year Treasury at a multi-decade high, so it relieves rather than resolves the market's central problem.

*One line of caution: #1 and #3 are in direct tension. A Hormuz deal is the single largest dovish input available to the Fed; a Hormuz breakdown before December restores the October hike as the base case.*

---

# Macro dashboard

| Indicator | Signal |
|---|---|
| **Global risk sentiment** | Cautiously constructive on the day, structurally fragile. VIX ~15.9. Nasdaq +1%+ intraday on soft PCE; Dow lower. But breadth is severely fractured — 271 Nasdaq names at 52-week lows vs 31 at highs on 29 Sept. S&P ~7,670–7,720, on track for a second consecutive quarterly gain. This is a rate-supported, narrow rally. |
| **Oil direction** | Down on flows, up on risk. Brent settled **−2.5%** Tuesday (~$96) as Gulf exports recovered via the East–West pipeline and partial Hormuz reopening; WTI ~**$91–92** intraday Wednesday, +~2.4%. Peak was ~$120. Realised moves now track *transit counts*, not headlines. Watch Kpler/JINSA daily Hormuz vessel counts — 130+ ships/day is the de-escalation threshold. |
| **Inflation pressure** | Cooling at the margin, still far too high. Core PCE **3.0% YoY** (vs 3.4% target) and headline **3.4%**, both revised down for July. US CPI +3.4% in August. Euro area ~3.0% forecast. Iran **84.4%**. UK diesel **$5.90/gal** (record), California diesel **$7.83** (+52% YoY). Above-target inflation is now oil-rationed, not demand-driven. |
| **Growth outlook** | Resilient in the US, deteriorating elsewhere. US Q2 GDP revised **up to 2.2%** from 1.5%; Q1 2.1%; Q2 real consumer spending +3.4% annualised. But Euro area PMIs contracted, German chemicals under margin stress, and EU energy import costs are up **>€100bn** with no additional supply. China PMI 49.8 — second month of contraction. The divergence is widening, not converging. |
| **Geopolitical risk** | **Elevated and broad.** US–Iran war in month seven with a rejected peace offer. **Iraq withdrawal complete** — Iran-aligned PMF empowered. Yemen escalation with **Pakistan** now signalling direct intervention and Houthi cruise-missile capability. **DMZ** landmine dispute plus a Seoul–Kyiv diplomatic rupture over North Korean POWs. Israeli election in 28 days with pre-vote security warnings. Ukraine peace talks stalled in the UAE. |
| **AI/tech sentiment** | Strongly positive on policy, increasingly uncomfortable on economics. **White House AI Accord** signed by six frontier labs. **Anthropic's $518bn, 80% non-cancellable** buildout disclosed. Semis led the open (Nvidia, Intel, Marvell, Micron post-close). The sentiment gap: enthusiasm at the capability frontier, quiet dread in the credit markets about who pays for the capacity. |

---

# One-chart view

**Chart: Iranian rial per US dollar (free market), daily, January 2026 → 30 September 2026 — with a secondary axis showing Brent front-month.**

**Why this one.** Every other chart available today is downstream of two facts: the war, and the Fed. The rial chart *is* the war, rendered in a single instrument. It shows:

- **1.35m rials/USD in March** (start of the Iranian calendar year, pre-war)
- **~1.8m** by late April, at the first ceasefire — the rush for hard currency
- **2.1m** on 2 September, after the US reimposed the naval blockade
- **2.2m → 2.5m+** over the following four weeks, a **~13% move in a month**, accelerating as Trump's rejection hardened

Overlay Brent and the causality is unambiguous: the rial depreciates in stair-steps, each step coinciding with a diplomatic rupture or a strike escalation, and the rial *never* rallies on ceasefire headlines. In April, a two-week ceasefire produced only a partial and reversed recovery. Investors looking for an oil-price chart already have one. What they lack is the chart that answers the question oil cannot — **how much of the war is actually priced, and where is the next convex move.**

It is also the only widely-traded, continuously observable proxy for whether Iranian regime stability is deteriorating fast enough to force Tehran toward the deal Trump rejected. Watch for the rial breaking below 2.5m as confirmation that the seven-day offer is genuinely dead rather than merely paused. And watch it *not* breaking — sustained stabilisation above 2.3m would be the first credible evidence that a mediated deal has traction.

Secondary reference, if one chart is insufficient: **the 30-year Treasury yield against Brent**. Both at multi-decade/multi-year highs simultaneously is the clearest available statement that the world is repricing energy *and* duration risk at the same time.

---

# 30-second executive brief

- **The only question that matters is Hormuz.** Trump rejected Iran's 7-day reopening plan outright. Brent is ~$96 (down 2.5% Tuesday on recovering Gulf flows) but was $120 at peak. Qatar is still relaying messages. Watch daily vessel counts, not headlines.
- **Oil is now a political problem, not just a market one.** The White House held crunch talks on a 90-day diesel export ban eleven weeks before US midterms. UK diesel is a record $5.90/gal; California diesel $7.83. Big Oil is right that a ban raises US prices — there is no refining slack.
- **US military presence in Iraq is now zero.** The 12-year counter-ISIS mission ended Wednesday from Erbil. Iran-aligned PMF are stronger, Kurdish officials alarmed, and Washington has no leverage left on Baghdad's security choices.
- **Soft inflation plus strong growth gave the market its best configuration of the year.** Core PCE 3.0% (vs 3.3% expected, July revised down), Q2 GDP revised up to 2.2%. October hike odds fell to ~37% from ~51%; Nasdaq +1%+, Dow lower.
- **But the long end is the problem.** The 30-year hit 5.62% on 29 September — highest since June 2002 — and 271 Nasdaq names sit at 52-week lows. This is a narrow, rate-supported rally, not a broad one.
- **The Fed hiked on 16 September under Chair Warsh to 3.75–4.00%.** His Jackson Hole logic put the burden on the doves. Core at 3.0% is still 100bp above target and is being held there substantially by a policy-variable oil price. December, not October, is the live question.
- **The US chose voluntary AI self-regulation over statute.** Six frontier labs plus Trump signed a 308-word accord committing to "morally binding" external audits. The signatories are also the auditors' clients. Watch the EU response and any Chinese countermove — a standards split would fragment the tooling market permanently.
- **$518bn of AI compute is now contractually locked and 80% of it is non-cancellable.** That is the most consequential financial fact in technology this year, and it is a *credit* story before it is an equity story.
- **The Red Sea is the under-priced risk.** Hormuz is impaired in the east; Bab el-Mandeb is impaired in the west, with Houthi cruise missiles and Pakistan now signalling direct intervention. War-risk insurance premia lead crude by days.
- **Watch three things into October:** (1) any US response to Qatar's channel; (2) the Israeli election in 28 days, with pre-vote attack warnings already trading as political rhetoric; (3) DMZ landmines and the Seoul–Kyiv rupture over North Korean POWs — small, cheap, and the most plausible small-scale crisis trigger of the year.
