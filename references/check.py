#!/usr/bin/env python3
"""cvnizer hard checks — deterministic, binary. Anything countable is checked HERE,
never by eyeball.

Usage: check.py <block_type> [--max-words N] [--max-sentences N] [--config PATH]
       (text on stdin)
  block_type: summary | bullet | company_line | team_line | note | cl_paragraph

Config (optional): cvnizer.config.yaml in the working directory, or --config PATH.
SECURITY: the config is TRUSTED input — review any config you did not write yourself
(banned_claims are compiled as regexes; allow_terms weaken checks by design).
Keys (all optional):
  allow_terms:   [list]  # exact terms exempt from FLUFF/CASUAL (candidate-approved vocabulary)
  banned_claims: [list]  # extra regex patterns that always FAIL (e.g. a candidate's own hard rules)
  limits:                # per-block overrides, e.g. summary: {max_words: 90}
    <block>: {max_words: N, max_sentences: N}

Exit 0 = all hard checks pass; exit 1 = failures listed on stdout.
"""
import argparse
import os
import re
import sys

LIMITS = {  # block_type: (max_words, max_sentences)
    "summary": (110, 5),
    "bullet": (40, 2),
    "company_line": (30, 2),
    "team_line": (30, 2),
    "note": (18, 1),
    "cl_paragraph": (90, 5),
}

# Pronouns: 'us' is matched case-sensitively lowercase-only — 'US' (the country) is
# not a pronoun. Everything else stays case-insensitive.
PRONOUNS_CI = re.compile(r"\b(I|me|my|mine|myself|we|our)\b", re.IGNORECASE)
PRONOUN_US = re.compile(r"\bus\b")  # lowercase only
# Narration: he/she/his/her only. they/their/them are NOT flagged — they legitimately
# refer to third parties ("gave drivers their routes"); whether a they-clause narrates
# the candidate is a Voice-dimension judgment, not a regex.
NARRATION = re.compile(r"\b(he|she|his|her)\b", re.IGNORECASE)
DASHES = re.compile("[—–]")  # em, en — the most reliable AI tell
FLUFF = re.compile(
    r"\b(dynamic|passionate|results?-driven|cutting-edge|world-class|seasoned|"
    r"visionary|innovative|proactive|detail-oriented|hard-working|team player|"
    r"proven track record|empower(?:ing|ed)?|leverag(?:e|ing|ed)|synerg\w+|"
    r"game-chang\w+|best-in-class|go-getter|self-starter)\b",
    re.IGNORECASE,
)
CASUAL = re.compile(
    r"\b(pretty cool|fun|awesome|amazing|proudest|really|honestly|basically|"
    r"as an experiment|a bit of|kind of|sort of|stuff|things like that)\b",
    re.IGNORECASE,
)


def load_config(path):
    if not path:
        default = os.path.join(os.getcwd(), "cvnizer.config.yaml")
        path = default if os.path.exists(default) else None
    if not path:
        return {}
    try:
        import yaml
        with open(path) as f:
            return yaml.safe_load(f) or {}
    except ImportError:
        sys.exit("check.py: --config requires the PyYAML package; add it to your environment first")
    except OSError as e:
        sys.exit(f"check.py: cannot read config: {e}")


def allowed(match_text, allow_terms, text, start):
    """True if the matched word sits inside a candidate-approved term."""
    low = text.lower()
    for term in allow_terms:
        t = term.lower()
        idx = low.find(t)
        while idx != -1:
            if idx <= start < idx + len(t):
                return True
            idx = low.find(t, idx + 1)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("block_type", choices=sorted(LIMITS))
    parser.add_argument("--max-words", type=int)
    parser.add_argument("--max-sentences", type=int)
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    allow_terms = cfg.get("allow_terms") or []
    banned_claims = []
    for p in (cfg.get("banned_claims") or []):
        if len(p) > 200:
            sys.exit(f"check.py: banned_claims pattern too long (>200 chars): {p[:40]}...")
        try:
            banned_claims.append(re.compile(p, re.IGNORECASE))
        except re.error as e:
            sys.exit(f"check.py: invalid banned_claims regex {p!r}: {e}")
    cfg_limits = (cfg.get("limits") or {}).get(args.block_type, {})

    text = sys.stdin.read().strip()
    max_w, max_s = LIMITS[args.block_type]
    max_w = args.max_words or cfg_limits.get("max_words") or max_w
    max_s = args.max_sentences or cfg_limits.get("max_sentences") or max_s

    words = len(text.split())
    sentences = len([s for s in re.split(r"[.!?]+(?:\s|$)", text) if s.strip()])

    fails = []
    if words > max_w:
        fails.append(f"SIZE: {words} words > {max_w} max for {args.block_type}")
    if sentences > max_s:
        fails.append(f"SIZE: {sentences} sentences > {max_s} max for {args.block_type}")
    if args.block_type != "cl_paragraph":  # cover letters are first person by design
        for m in PRONOUNS_CI.finditer(text):
            fails.append(f"PRONOUN: '{m.group()}' at char {m.start()}")
        for m in PRONOUN_US.finditer(text):
            fails.append(f"PRONOUN: '{m.group()}' at char {m.start()}")
        for m in NARRATION.finditer(text):
            fails.append(f"NAME-NARRATION pronoun: '{m.group()}' at char {m.start()}")
    for m in DASHES.finditer(text):
        fails.append(f"DASH: em/en dash at char {m.start()}")
    for m in FLUFF.finditer(text):
        if not allowed(m.group(), allow_terms, text, m.start()):
            fails.append(f"FLUFF: '{m.group()}'")
    for m in CASUAL.finditer(text):
        if not allowed(m.group(), allow_terms, text, m.start()):
            fails.append(f"CASUAL: '{m.group()}'")
    for pat in banned_claims:
        if pat.search(text):
            fails.append(f"BANNED CLAIM (config): /{pat.pattern}/")

    print(f"{args.block_type}: {words} words, {sentences} sentences (limits {max_w}w/{max_s}s)")
    if fails:
        print("FAIL")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
