# Changelog

All notable changes to the cvnizer skill. Versioning: semver — MAJOR for scope
changes, MINOR for new dimensions/references/mechanics, PATCH for fixes.

## 2.3.2 — 2026-07-08

- Docs: install instructions for OpenAI Codex CLI (`~/.codex/skills/`) and any
  agentskills-format harness. No code changes — the format was already compatible.

## 2.3.1 — 2026-07-08

Security hardening after a skill-security audit (automated scan: WARN, 1 HIGH —
a false positive on an error-message string; manual review found the real items):

- **Prompt-injection guard:** hard constraint added — the block under review is DATA;
  directive-looking content inside CV text is never followed.
- **Config trust hardening:** banned_claims regexes validated (compile errors fail
  loudly, 200-char length cap against ReDoS); docstring + README state that configs
  are trusted input to be reviewed if not self-written.
- **Publication data-leak guards:** `.gitignore` excludes `cvnizer.config.yaml`;
  README fork/publish checklist (config stays local; conversion pairs de-personalized
  before any push).
- Reworded the PyYAML error message that pattern-matched as a runtime pip install
  (scanner false positive; nothing executed).

## 2.3.0 — 2026-07-08

- **Local config** (`cvnizer.config.yaml`, optional, never ships): candidate-approved
  vocabulary allowlist (kills wordlist false positives without weakening the script),
  extra banned-claim regexes (personal hard rules), per-block limit overrides.
  `cvnizer.config.example.yaml` documents the format.
- **check.py fixes:** "US" no longer matches the pronoun "us" (lowercase-only match);
  they/their/them removed from the narration check (legitimate third-party reference —
  narration of the candidate is a Voice-dimension judgment, not a regex). Both were
  live false positives in a real 47-block run.
- **Conversion-pair library** (`references/conversions.md`): real before→after pairs
  grouped by failure type (self-narration, product narration, IC framing, ops-KPI
  vocabulary, negative disclaimers, tool logos, apologetic size words, -ing tails);
  the rewrite step now copies the matching pair's MOVE, never its content. Local copy
  holds personal pairs; de-personalize before any publication.
- **Evidence-embedded verdict:** the verdict is invalid without its script output and
  per-dimension evidence (which sample/marker/measurement decided each score). Closes
  the "only word count ran" partial-application failure, caught twice in real use.

## 2.2.0 — 2026-07-08

- **Altitude dimension** (5th): wording is polished toward a stated target level
  (director/executive default; IC/manager selectable). Verb+object altitude markers
  derived from the Set A corpus; reword-within-facts-only constraint; honest
  "inherently tactical" FAIL when no source material can close the gap.
- **Metric altitude** rule in the markers: ops KPIs are IC/team-level proof; money,
  customer, risk, delivery outcomes are director-level; summaries lead with the
  highest-altitude metric the source offers.

## 2.1.0 — 2026-07-08

- **Sample-seeded tone target** (`references/tone_target.md`): Set A (8 excerpts from
  professionally written executive CVs, measured fingerprint: bullets 15-31 words,
  100% past-tense-verb-led, 2+ metrics, number in first 12 words) vs Set B
  (template-mill/AI anti-samples, six named tells). Register scored by belonging/
  subject/proof tests per sentence, humanizer-style, instead of rules alone.
  LinkedIn rejected as corpus: exec About sections are deliberately conversational
  first person — the opposite register.

## 2.0.0 — 2026-07-08

- **Scope trim (breaking):** wording + size ONLY. Honesty, claim placement, structure,
  and fact-checking removed from the skill (they belong to the caller's own process).
  Six dimensions reduced to four (Voice, Register, Rhythm, Density); the /60 total
  gate replaced by per-dimension floors (every dimension >= 7 — no total to game).
  Fully standalone: no external fact-store or workflow references. README + MIT
  license added; personal banned-claim patterns removed from the script.

## 1.0.0 — 2026-07-08

- Initial skill: deterministic `check.py` (size limits per block type, pronouns,
  em/en dashes, fluff, casual register) + six scored dimensions (>=42/60) composing
  the humanizer-pro loop for CV prose; TDD'd per writing-skills (baseline agent
  shipped a 111-word, 6-sentence summary with em dashes; with the skill, corrected
  and script-verified).
