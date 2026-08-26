#!/usr/bin/env python3
import os, subprocess, textwrap
ROOT = os.path.dirname(os.path.abspath(__file__)); os.chdir(ROOT)

def commit(msg):
    subprocess.run("git add -A", shell=True, cwd=ROOT, check=True)
    r = subprocess.run("git diff --cached --quiet", shell=True, cwd=ROOT)
    if r.returncode == 0:
        print("SKIP:", msg); return
    subprocess.run(["git", "commit", "-q", "-m", msg], cwd=ROOT, check=True)
    print("COMMIT:", msg)

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)

def append(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "a") as f:
        f.write(content)

def do_write(path, content, msg):
    write(path, content)
    commit(msg)

def do_append(path, content, msg):
    append(path, content)
    commit(msg)

EXAMPLES = [
("tiktok-before-after.md", "TikTok", textwrap.dedent("""\
# TikTok: Before / After

## Before (AI-generated)

> "Today I want to talk about the transformative impact of building in
> public. In summary, sharing your progress is important because it can
> unlock valuable feedback. Many creators struggle with consistency, and it's
> worth noting that overcoming this can lead to significant growth over
> time."

Diagnosed patterns: uniform sentence length, "in summary" and "it's worth
noting" as filler transitions, "unlock" and "transformative" as inflated
vocabulary, zero specificity, no hook at all — this doesn't survive 3
seconds.
"""), textwrap.dedent("""\

## After

**Hook (0-3s, spoken + on-screen text):** "I posted my failed side project
publicly for 90 days straight. Here's what actually happened."

**Hold (3-8s):** "Not the highlight reel version — the actual screenshots,
including the week I got zero engagement."

**Payoff preview (8-12s):** "One post at day 61 changed everything, and it
wasn't the one I expected."

**Body:** walks through 2-3 concrete moments with real numbers (view counts,
what changed) instead of general encouragement.

**CTA:** "Follow if you want the day-by-day breakdown."

## What changed

| Before | After |
|---|---|
| "transformative impact of building in public" | "posted my failed side project publicly for 90 days" |
| "it's worth noting that overcoming this can lead to growth" | "one post at day 61 changed everything" |
| No hook | Hook lands in first sentence, spoken + on-screen |

**Hashtags:** #buildinpublic #indiehacker #sidehustle
""")),

("reels-before-after.md", "Instagram Reels", textwrap.dedent("""\
# Instagram Reels: Before / After

## Before (AI-generated)

> "Consistency is key when it comes to content creation. It is important to
> stay authentic while also being strategic. Many creators find that a
> balance between planning and spontaneity leads to the best results."

Diagnosed patterns: generic advice with no specific referent, hedging
("it is important"), no visual or narrative hook, reads like a caption
written for any creator about any topic.
"""), textwrap.dedent("""\

## After

**Hook (0-2s, visual pattern interrupt + caption):** "POV: you finally admit
your 'strategy' was just posting whenever you remembered to."

**Caption (2-3 lines, conversational):**
"I planned content for 3 months. Engagement dropped. I stopped planning and
just posted what I was actually excited about. Saves went up 4x. Plan less,
post more of what you'd actually stop scrolling for."

**CTA:** "Save this for the next time you're overthinking a caption."

## What changed

| Before | After |
|---|---|
| "consistency is key" | specific personal result: "saves went up 4x" |
| No hook | POV-style visual pattern interrupt in frame one |
| Generic CTA-less ending | explicit save prompt (Reels' primary metric) |
""")),

("shorts-before-after.md", "YouTube Shorts", textwrap.dedent("""\
# YouTube Shorts: Before / After

## Before (AI-generated)

> Title: "My Content Creation Journey"
> Script: "In this video, I will discuss my experience with content creation
> and share some tips that may be helpful for beginners."

Diagnosed patterns: title has zero search value, hedging ("tips that may be
helpful"), no specific promise, sounds like a table of contents rather than
content.
"""), textwrap.dedent("""\

## After

**Title (SEO keyword phrase, not a hook):** "How to Post Consistently on
YouTube Shorts (What Actually Worked)"

**Hook (0-5s):** "I missed my posting schedule for 6 weeks straight — here's
the one change that fixed it."

**Body:** a specific, evergreen 3-step system, framed so it's still useful
and searchable a year from now, not tied to a trend.

**End screen:** "Subscribe if you want part 2 — the scheduling tool I
actually use."

## What changed

| Before | After |
|---|---|
| "My Content Creation Journey" (no search value) | "How to Post Consistently on YouTube Shorts" (matches real search queries) |
| "tips that may be helpful" | a named 3-step system |
| No CTA | specific subscribe reason tied to a real part 2 |
""")),

("x-before-after.md", "X/Twitter", textwrap.dedent("""\
# X / Twitter: Before / After

## Before (AI-generated)

> "Building a side project can be a rewarding but challenging experience.
> There are many factors that contribute to success, including consistency,
> feedback, and a clear vision for the product."

Diagnosed patterns: no hook in the first 10 words, generic list with no
specificity, reads like it could be about any product ever built.
"""), textwrap.dedent("""\

## After (thread, 5 tweets)

**Tweet 1 (hook, first 10 words do the work):** "Shipped a Claude Skill
Saturday. 40 stars by Tuesday. Here's exactly what happened —"

**Tweet 2:** the specific first move that got initial traction (a real post,
a real comment thread) — not "posted on social media."

**Tweet 3:** the one thing that didn't work, stated plainly.

**Tweet 4:** the moment it turned — a real number, a real timestamp.

**Tweet 5 (payoff + CTA):** the actual takeaway in one sentence, plus a link.

## What changed

| Before | After |
|---|---|
| "can be a rewarding but challenging experience" | "40 stars by Tuesday" (concrete, checkable) |
| Single dense paragraph | 5-tweet thread, each tweet standing alone |
| No hook | first 10 words carry the entire hook |
""")),

("linkedin-before-after.md", "LinkedIn", textwrap.dedent("""\
# LinkedIn: Before / After

## Before (AI-generated)

> "I'm excited to share that our team has been working hard on an innovative
> new approach to content strategy. This journey has taught us valuable
> lessons about the importance of authenticity in the digital age."

Diagnosed patterns: "excited to share," "innovative," "journey," and
"authenticity in the digital age" are all high-frequency AI/corporate
vocabulary; zero specific detail; no captions plan even though ~85% of
LinkedIn video is watched muted.
"""), textwrap.dedent("""\

## After

**Hook (professional insight, first sentence):** "We killed our content
calendar three months ago. Output went up."

**Body (on-screen captions mandatory, native video):** names the specific
change (e.g., moving from a monthly plan to a same-week publish cycle), one
real metric, and one real tradeoff it caused — full honesty about the
downside, not just the win.

**CTA (specific, answerable question, not "thoughts?"):** "What's the last
process your team cut that turned out to not matter?"

## What changed

| Before | After |
|---|---|
| "innovative new approach to content strategy" | "we killed our content calendar three months ago" |
| "authenticity in the digital age" | one specific, honest tradeoff named |
| "thoughts?" | a specific, answerable question |
| No caption plan | on-screen captions specified (mandatory for muted viewers) |
""")),
]

for fname, platform, before, after in EXAMPLES:
    path = f"examples/{fname}"
    do_write(path, before, f"docs(examples): add {platform} before example")
    do_append(path, after, f"docs(examples): add {platform} after + breakdown")

print("examples build done")
