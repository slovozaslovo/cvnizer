# cvnizer scoring — four wording dimensions

Score only after `check.py` passes. Each dimension 1-10 against `register.md`.
**Gate: every dimension >= 7.** No total to game; the weakest dimension is the verdict.

| # | Dimension | The question | 1-3 (fail) | 8-10 (pass) |
|---|---|---|---|---|
| 1 | **Voice** | Implied first person, verb-led, uniform tense? | Pronouns, narrated verbs ("Sets..."), mixed registers | Every clause opens on a base/past verb or noun phrase; zero pronouns |
| 2 | **Register** | Would it sit unnoticed in tone_target.md Set A? | Belongs in Set B: adjective-stacked, claims catalog, self-admiring, product-narrating, conversational | Belongs in Set A: verb-led, number early, outcome carries the sentence (fingerprint: bullets 15-31w, 2+ metrics) |
| 2a | **Altitude** | Do the verbs and objects sit at the TARGET level (tone_target.md altitude markers)? | IC framing on a director run: artifact objects ("an agent", "a script"), hands-on verbs | Verbs and objects at target level, worded from source material only; or an honest "inherently tactical" flag |
| 3 | **Rhythm** | Varied length, no monotony, no forced triads? | Uniform sentence lengths, triads everywhere | Short. Then a longer sentence that carries the proof. |
| 4 | **Density** | Every word earning its place? | Filler phrases, redundant qualifiers, throat-clearing | Nothing cuttable left; brevity reads senior |

## Scoring rules

- Be honest — inflating scores breaks the loop.
- A skills LIST is not prose; do not score it.
- Do not push CV text toward personal-essay voice: warmth and opinion are humanizer
  targets, not CV targets. A perfect CV block is plain, dense, and slightly cold.
- Rhythm is scored on summary and cover-letter paragraphs; single bullets are too
  short for rhythm — score them 8 by default unless a triad or monotone list appears.

## Size limits (enforced by check.py — reference)

| Block | Max words | Max sentences |
|---|---|---|
| summary | 110 | 5 |
| bullet | 40 | 2 |
| company_line / team_line | 30 | 2 |
| note | 18 | 1 |
| cl_paragraph | 90 | 5 |

Defaults are overridable: `check.py summary --max-words 90`.

## Verdict format — always print

```
cvnizer: PASS · level director · 84w/4s (limit 110w/5s) · checks PASS · Voice 9 · Register 8 · Altitude 8 · Rhythm 7 · Density 8
  script: summary: 84 words, 4 sentences (limits 110w/5s) / PASS
  evidence: Voice verb-led, 0 pronouns · Register Set A (number word 5, outcome closes) · Altitude director (object: operating model) · Rhythm 11/24/26/23 · Density cut 2 filler phrases
```
Every dimension score cites what decided it (the sample compared against, the marker
row, the measured lengths). A verdict without this evidence block is INVALID — a
skipped step must be named, never papered over. FAIL verdicts list what failed and
why, no hedging. An "inherently tactical" Altitude FAIL names the missing material
(scope, outcome, ownership) that wording cannot supply.
