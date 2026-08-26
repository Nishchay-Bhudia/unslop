# Contributing to Un-AI-ify

Un-AI-ify is a Claude Skill: a folder of Markdown instructions, not a codebase.
Contributions that improve accuracy, add platforms, or sharpen the psychology
are welcome.

## Ways to contribute

- **New hook formulas** — add to `references/hook-formulas.md` with a real
  example, not a placeholder.
- **New or updated platform rules** — algorithms change; if TikTok's retention
  gate or LinkedIn's caption requirement shifts, update `references/platform-rules.md`.
- **New AI-tell patterns** — if you spot a stylistic tic models are producing
  in 2026 that isn't in `references/ai-patterns.md`, add it with a before/after.
- **Test cases** — add to `test-suite/test-cases.md` following the existing format.
- **Before/after examples** — real transformations (anonymized) in `examples/`.

## Ground rules

1. **No fabricated proof.** Every example and claim in this repo must be
   plausible and honestly labeled. Do not invent statistics, testimonials, or
   personal stories to make an example look stronger.
2. **Keep SKILL.md under ~500 lines.** Long-form detail belongs in `references/`.
3. **One idea per PR.** Small, reviewable diffs.
4. **Cite your source** when adding a platform rule or psychology claim in the
   PR description, even if it doesn't ship inline in the file.

## Local testing

There's no build step. Load the skill folder into Claude Code
(`.claude/skills/un-ai-ify/`) or zip it for Claude.ai, then run a few cases
from `test-suite/test-cases.md` and compare against `expected-outputs/`.
