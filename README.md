<div align="center">

<img src="assets/banner.svg" alt="Un-AI-ify banner" width="100%" />

# Un-AI-ify

**Transform AI-generated social content into authentic, platform-native posts.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-d97757)](https://github.com/anthropics/skills)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Platforms](https://img.shields.io/badge/platforms-TikTok%20%7C%20Reels%20%7C%20Shorts%20%7C%20X%20%7C%20LinkedIn-blueviolet)]()

</div>

## The problem

Most AI-generated social content sounds the same: uniform sentence length,
hedging language, "unlock"/"revolutionize"/"testament to," a hook that
doesn't hook, and zero specificity. It reads like it was written for no one
in particular — because it usually was.

Un-AI-ify is a [Claude Skill](https://github.com/anthropics/skills) that
takes that draft, diagnoses exactly which patterns are making it generic, and
rebuilds it around a real hook-hold-payoff structure — tuned to the actual
retention mechanics of the platform it's going to, not just "sound more
human."

## What makes this different

This is **not** an AI-detector-evasion tool. Detectors change constantly and
have high false-positive rates on non-native English and technical writing —
building around beating them is a losing, dishonest game.

Un-AI-ify is psychology-first: it applies research on curiosity gaps
(Loewenstein), the Zeigarnik effect, emotional arousal and sharing (STEPPS),
and platform-specific retention data (TikTok's 3-second gate, LinkedIn's 85%
muted-viewing rate, etc.) to make content that's genuinely more compelling —
and it refuses to fabricate stats, credentials, or experiences to get there.
See [`GUARDRAILS`](./SKILL.md#guardrails).

## Install

**Claude Code (recommended)**
```bash
git clone https://github.com/nishchay-bhudia/un-ai-ify.git
mkdir -p ~/.claude/skills
cp -r un-ai-ify/. ~/.claude/skills/un-ai-ify/
```
Restart Claude Code (or start a new session). The skill auto-triggers when
you paste content that sounds AI-generated, or when you say things like
"humanize this" or "un-AI-ify this."

**Project-level (this repo's skill applies only inside one project)**
```bash
mkdir -p .claude/skills
cp -r un-ai-ify/. .claude/skills/un-ai-ify/
```

**Claude.ai**
1. Download this repo as a ZIP (Code → Download ZIP), or `git clone` then zip
   the `un-ai-ify/` folder.
2. Go to **Settings → Customize → Skills → Upload skill**.
3. Upload the ZIP.

## Quick start

1. Paste a script, caption, or post into Claude — anything that sounds
   robotic, vague, or "written by ChatGPT."
2. Say which platform it's for (TikTok, Reels, Shorts, X, or LinkedIn) — or
   just ask, and Claude will ask you if it's ambiguous.
3. Get back: a diagnosis of what was making it sound generic, the
   transformed post, exactly what changed and why, and a self-rated quality
   score.

```
> Un-AI-ify this for TikTok:
> "Today I want to discuss the transformative impact of consistency in
> content creation. Many creators struggle with this..."
```

See [`examples/`](./examples) for five full before/after transformations,
one per platform.

## Features

- 🎯 **6-stage transformation pipeline** — diagnose, extract, reconstruct,
  humanize, platform-adapt, quality-control (full detail in
  [`SKILL.md`](./SKILL.md)).
- 🪝 **38 hook formulas**, organized by audience awareness and psychological
  lever, each with a real example — [`references/hook-formulas.md`](./references/hook-formulas.md).
- 🧠 **Psychology-backed, not detection-based** — curiosity gap theory, the
  Zeigarnik effect, STEPPS — [`references/psychology.md`](./references/psychology.md).
- 🔍 **25-point AI-tell checklist** with before/after fixes for each pattern —
  [`references/ai-patterns.md`](./references/ai-patterns.md).
- 📱 **Platform-native pacing** for TikTok, Reels, Shorts, X, and LinkedIn —
  [`references/platform-rules.md`](./references/platform-rules.md).
- 🛡️ **Guardrails against fabrication** — never invents stats, credentials,
  or personal experience to sound more convincing.
- 🧪 **20-case test suite** for regression-checking any change to the skill —
  [`test-suite/test-cases.md`](./test-suite/test-cases.md).
- 📦 **Fully open-source, MIT-licensed**, zero paywalls, zero usage limits.

## How it works

<img src="assets/hook-formula-diagram.svg" alt="Hook, hold, payoff diagram" width="100%" />

| Stage | What happens |
|---|---|
| 1. Diagnose | Scans for AI tells: uniform rhythm, hedging, filler transitions, generic vocabulary. |
| 2. Extract | Isolates the real core message, strongest claim, and audience — before touching any wording. |
| 3. Reconstruct | Picks a hook formula by audience awareness, builds a hook → hold → payoff arc. |
| 4. Humanize | Varies rhythm, replaces inflated vocabulary, adds specificity, cuts hedging. |
| 5. Platform adapt | Reformats for the target platform's actual pacing, caption, and CTA rules. |
| 6. Quality control | Re-checks against the Stage 1 diagnosis before returning anything. |

## Platform rules at a glance

| Platform | Hook window | Length | Must-have |
|---|---|---|---|
| TikTok | 3 seconds | ≤ 60s | text overlay synced to spoken hook |
| Instagram Reels | ~2 seconds | 15-90s (15-30s optimal) | save/share-focused CTA |
| YouTube Shorts | ~5 seconds | 30-60s | SEO-keyword title, not a hook |
| X / Twitter | first 10 words | 15-30s or thread | each thread tweet stands alone |
| LinkedIn | first sentence | 45-90s | mandatory on-screen captions (85% watch muted) |

Full detail and rationale: [`references/platform-rules.md`](./references/platform-rules.md).

## Example: TikTok before/after

**Before (AI-generated):**
> "Today I want to talk about the transformative impact of building in
> public. In summary, sharing your progress is important because it can
> unlock valuable feedback."

**After:**
> **Hook:** "I posted my failed side project publicly for 90 days straight.
> Here's what actually happened."
> **Hold:** "Not the highlight reel — the actual screenshots, including the
> week I got zero engagement."
> **Payoff preview:** "One post at day 61 changed everything, and it wasn't
> the one I expected."

Four more full transformations (Reels, Shorts, X, LinkedIn) in
[`examples/`](./examples).

## Documentation

- [`SKILL.md`](./SKILL.md) — the full, executable skill definition.
- [`references/hook-formulas.md`](./references/hook-formulas.md) — all 38 hook formulas.
- [`references/platform-rules.md`](./references/platform-rules.md) — platform pacing and caption rules.
- [`references/ai-patterns.md`](./references/ai-patterns.md) — the 25-point AI-tell checklist.
- [`references/psychology.md`](./references/psychology.md) — the research this skill is built on.
- [`examples/`](./examples) — five full before/after transformations.
- [`test-suite/test-cases.md`](./test-suite/test-cases.md) — 20 regression test cases.

## FAQ

**Will this help me beat AI detectors?**
No, and it's not trying to. Detector behavior changes constantly and has high false-positive rates on non-native English and technical writing. This skill optimizes for a human reader's attention, not a classifier.

**Does it make up stats or personal stories to sound convincing?**
No. The [Guardrails section of SKILL.md](./SKILL.md#guardrails) explicitly forbids fabricating claims, credentials, or experiences. If your draft needs a number to land, the skill asks you for the real one.

**Can I use it for multiple platforms from one draft?**
Yes — ask for a multi-platform pass (see Advanced Options in [`SKILL.md`](./SKILL.md#advanced-options)) and it adapts the same core message to each platform's actual pacing rules, not just a reformat.

**Is this free?**
Yes, MIT-licensed, no paywalls, no usage limits, forever.

**How do I add a new hook formula or platform rule?**
See [`CONTRIBUTING.md`](./CONTRIBUTING.md) — PRs adding real, non-fabricated examples are welcome.
