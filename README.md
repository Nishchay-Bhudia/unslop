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
