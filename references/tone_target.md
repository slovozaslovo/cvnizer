# Tone target — what executive CV text sounds like

This is cvnizer's sample-seeded tone reference, the analog of a humanizer's voice
sample: score Register and Voice by asking **"which sample set does this sentence
belong to — A or B?"**, not by abstract rules alone. Samples are short excerpts from
published executive CV examples (sources at bottom).

## Set A — the target (professionally written executive CVs)

### Summaries: noun-phrase opener, short declarative sentences, proof over adjectives

- "Operations leader with 12+ years in multi-site delivery across manufacturing and
  logistics. Trusted to stabilise underperformance, improve margin, and strengthen
  service levels." (Brendan Hope)
- "Finance Director with experience in PE-backed and listed environments, combining
  robust controls with commercial partnership." (Brendan Hope)
- "Mission-driven COO with a track record of scaling organizations focused on
  educational equity. At Teach for America, launched 10 new sites in underserved rural
  communities, impacting 5,000+ students." (Resume Worded)

### Bullets: past-tense verb first, number early, outcome carries the sentence

- "Led a 9-site operating model redesign, improving OTIF from 82% to 96% in 6 months
  while reducing agency dependency by £420k p.a." (Brendan Hope)
- "Implemented a rolling 13-week cashflow model and working-capital governance,
  improving cash conversion by 11 days." (Brendan Hope)
- "Optimized the organization's $5M operating budget, identifying opportunities to
  reduce costs by 15% while ensuring successful program delivery." (Resume Worded)
- "Built and led a 20-person cross-functional team to successfully execute a major
  program expansion to 3 new cities; mentored and coached 5 director-level direct
  reports, resulting in 2 promotions to VP-level." (Resume Worded)
- "Boosted net revenue 9%, decreased operating expenses 8%, and increased EBITDA 14%
  by merging strategic and financial management with attentive staff leadership."
  (Great Resumes Fast)

### Measured fingerprint of Set A (computed on the samples, not estimated)

- Bullets: **15-31 words** (mean 22), **100% open with a past-tense verb**,
  **2+ metrics per bullet** (mean 3.1), **a number inside the first 12 words in 8/8**.
- Summary sentences: **10-15 words**, noun-phrase openers ("[Function] leader with
  N years in X..."), zero pronouns, at most one adjective and it is load-bearing
  ("multi-site", "PE-backed" — facts, not praise).
- The subject of nearly every sentence is the candidate acting (implied), never the
  product narrating itself and never an abstraction ("the data shows...").

## Set B — the anti-target (template-mill and AI-generated CV prose)

- "With over 15 years of experience in operations management, I bring a proven track
  record in scaling operations... Skilled in leadership, successfully fostering
  multi-team alignment and innovation in complex environments... underscoring a
  commitment to operational excellence." (enhancv sample)
- "Strategic and results-driven Director with six years of experience... Adept at
  stakeholder engagement, risk management, and long-term business planning. Committed
  to delivering sustainable growth and operational excellence." (StandOut CV sample)
- "Visionary Executive with over 15 years of experience leading global organisations,
  specialising in strategic planning, business transformation, and stakeholder
  management." (StandOut CV sample)

### Named tells of Set B

1. **Adjective-stacked openers** — "Strategic and results-driven / Visionary /
   Dynamic [Title]": praise before proof.
2. **Claims catalogs** — "Skilled in... Adept at... Committed to...": three abilities
   listed, zero outcomes shown.
3. **First person + throat-clearing** — "With over N years of experience, I bring...".
4. **Zero numbers** — a whole paragraph of capability words without one metric.
5. **Self-referential gravitas** — "underscoring a commitment to operational
   excellence": the sentence admires itself instead of reporting a result.
6. **Product/feature narration** (junior variant) — describing what the product does
   for its users ("gave drivers their routes on the mobile screen") instead of what
   the leader delivered and what changed commercially.

## Altitude markers — what level the WORDS sit at

The same fact can be worded at three levels. Score Altitude against the target level
(director/executive by default) by looking at the **verbs** and the **objects**:

| Level | Typical verbs | Typical objects | Sample |
|---|---|---|---|
| IC | built, coded, configured, created, wrote, automated | a tool, an agent, a script, a test suite, an app, a dashboard | "Wrote a data-cleanup script and a reporting dashboard for the ops team" |
| Manager | ran, delivered, coordinated, managed | a project, a release, a team's backlog, a rollout | "Delivered the ERP rollout across 3 sites on schedule" |
| Director/exec | redesigned, established, directed, owned, introduced, scaled | an operating model, a function, a portfolio, a P&L, a hiring system, direction | "Led a 9-site operating model redesign, improving OTIF from 82% to 96%" |

Rules:
- Every Set A sample sits at director level: the object is a system, org, model, or
  portfolio — not an artifact. Use that as the comparison, same as tone.
- **Reword within the facts only.** "Built an alerting bot" CAN become
  "Introduced automated alerting into the incident process" only if the
  introduction/process is in the source; ownership and scope are never added.
- If the sentence is inherently an artifact claim with no scope or outcome material
  to reword with, say so — that is a content gap wording cannot close.
- IC-level wording is not "wrong English"; it is wrong ALTITUDE for a director target
  and right for an IC target. Score against the stated level.
- **Metrics have altitude too.** Craft/ops KPIs (test creation speed, code coverage,
  tickets closed) are IC/team-level proof; money, customer, risk, and delivery
  outcomes (EBITDA, CSAT, production incidents, time-to-market, time-to-hire) are
  director-level proof. In a summary, lead with the highest-altitude metric the
  source offers; ops KPIs stay in role bullets.

For each sentence of the block under review:
1. **Belonging test:** read it against Set A and Set B. If it would sit unnoticed in
   Set B, rewrite it toward Set A patterns using the fingerprint numbers.
2. **Subject test:** who acts in this sentence? Target: the candidate (implied).
   Anti-pattern: the product, the team as narrator, or an abstraction.
3. **Proof test:** does the sentence spend its words on a claim or an outcome? Each
   capability word ("strategic", "skilled") is a smell unless a number or named
   outcome sits in the same sentence.

Rewrite toward the fingerprint, re-run `check.py`, re-score. Do not import Set A's
*facts* — only its shape. Facts always come from the source text unchanged.

## Sources

- Brendan Hope, [Executive CV Examples (UK) & 2-Page Template](https://brendanhope.com/blog/executive-cv-writing-guide/)
- Resume Worded, [C-Level and Executive CV Examples](https://resumeworded.com/c-level-cv-examples) and related pages
- Great Resumes Fast, [Health Care Executive President and CEO sample resume](https://greatresumesfast.com/wp-content/uploads/2021/03/Health-Care-Executive-President-and-CEO-Resume.pdf)
- Kelly Donovan, [Introduction to resume speak](https://kellydonovan.com/introduction-resume-speak/) (pronoun-drop conversion pairs)
- Anti-target samples: [enhancv executive resume examples](https://enhancv.com/resume-examples/executive-resumes/), [StandOut CV director](https://standout-cv.com/cv-examples/management-and-leadership/director-cv) and [executive](https://standout-cv.com/cv-examples/management-and-leadership/executive-cv-template) example profiles (quoted as contrast, not as recommendations)
