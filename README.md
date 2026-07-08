# cvnizer

**The right words at the right size, for CVs.**

Humanizer skills make AI text sound like a person. cvnizer solves the opposite problem
nobody built a skill for: making CV text sound like a strong senior/executive CV —
which is a *different* register. Pronoun-free. Direct, factual, commercial. Dense.
Deliberately unconversational. And the right length, measured, not eyeballed.

An [agent skill](https://agentskills.io) for Claude Code and compatible harnesses.

## What it catches

```
"Dynamic and passionate operations executive... I basically transformed the
entire company's supply chain — reducing costs by 30% — and I'm really proud
of how my team grew from 12 to 85 people... which was awesome."
```

10 pronouns, 2 em dashes, 10 fluff words, 3 casual-register hits. cvnizer turns it into:

```
"Operations executive with 22 years of experience. Transformed the company-wide
supply chain, cutting costs 30%. Grew the team from 12 to 85 people across
three continents."
```

Same facts, half the words, executive register.

## How it works

1. **Deterministic checks first** (`references/check.py`): word/sentence limits per
   block type, pronouns, em/en dashes, fluff adjectives, casual register — plus your
   optional local config (approved vocabulary, extra banned patterns, limit
   overrides). Counted by script, never by eyeball.
2. **Target level**: wording is polished toward a stated seniority — director/executive
   by default, IC or manager on request. Professionally-polished IC framing on a
   director run is a FAIL, not a pass.
3. **Scored loop** (like a humanizer, different target): five wording dimensions —
   Voice, Register, Altitude, Rhythm, Density — each 1-10, scored by SAMPLE COMPARISON
   against real executive-CV excerpts and template-mill anti-samples
   (`references/tone_target.md`), with rules in `references/register.md`.
   Gate: every dimension ≥ 7, max 3 iterations.
4. **Rewrites follow conversion pairs** (`references/conversions.md`): before→after
   examples grouped by failure type — the loop copies the move, never the content.
   Altitude is reworded within the source's facts, never inflated; an inherently
   tactical claim gets an honest "wording cannot fix this" instead of dressing-up.
5. **Evidence-embedded verdict, always** — invalid without its proof:
   ```
   cvnizer: PASS · level director · 18w/1s (limit 40w/2s) · checks PASS · Voice 9 · Register 9 · Altitude 8 · Rhythm 8 · Density 9
     script: bullet: 18 words, 1 sentences (limits 40w/2s) PASS
     evidence: Voice verb-led, 0 pronouns · Register Set A (number word 4, outcome carries) · Altitude director (object: process at division scope) · Rhythm single bullet · Density nothing cuttable
   ```

## What it deliberately does NOT do

Wording and size only. cvnizer never changes facts, names, dates, or numbers, and it
does not verify them — a false claim leaves cvnizer as a well-worded false claim.
Truthfulness, metric selection, and section structure are content decisions; pair
cvnizer with your own fact-check.

## Install

Copy the `cvnizer/` directory into your agent's skills directory
(e.g. `~/.claude/skills/cvnizer/` for Claude Code). Requires Python 3 for the checker.

## Use

Ask your agent: *"run cvnizer on this summary"*, *"cv-ify this"*, *"does this sound
like a director CV?"* — or let it trigger when finalizing CV sections.

Standalone checker:

```bash
python3 references/check.py summary < my_summary.txt
python3 references/check.py bullet --max-words 30 < bullet.txt
```

Block types: `summary`, `bullet`, `company_line`, `team_line`, `note`, `cl_paragraph`
(cover-letter paragraphs keep first person — their natural form).

## The register, sourced

The wording target distills published industry guidance on executive CV writing:
implied first person / "resume speak" ([The CV & Interview Advisors](https://cvandinterviewadvisors.co.uk/blog/should-a-cv-be-in-third-person),
[Indeed](https://www.indeed.com/career-advice/resumes-cover-letters/resume-first-person),
[Kelly Donovan](https://kellydonovan.com/introduction-resume-speak/)),
direct/factual/commercial register and length discipline
([Brendan Hope](https://brendanhope.com/blog/executive-cv-writing-guide/),
[Page Executive](https://www.pageexecutive.com/advice/topics/leadership/how-to-write-an-executive-cv)).

## Lineage

The scored-convergence-loop idea comes from the humanizer family of skills —
[blader/humanizer](https://github.com/blader/humanizer) and
[Hainrixz/humanizalo](https://github.com/Hainrixz/humanizalo) (both MIT). cvnizer
points the loop at the opposite target: not "sounds human", but "sounds like a
strong CV".

## Local config (never ships)

Personal vocabulary, extra banned-claim rules, and limit overrides live in a local
`cvnizer.config.yaml` (gitignored; see `cvnizer.config.example.yaml`). Treat configs
as trusted input: review any config you did not write. If you fork or publish an
adapted copy: keep the config out of the repo, and replace `references/conversions.md`
pairs with de-personalized equivalents before pushing.

## License

MIT
