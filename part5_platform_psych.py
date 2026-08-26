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

def append(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "a") as f:
        f.write(content)

def do(path, content, msg):
    append(path, content)
    commit(msg)

# ---------------- platform-rules.md ----------------
F = "references/platform-rules.md"

do(F, textwrap.dedent("""\
# Platform Rules

Retention math and formatting requirements differ enough by platform that the
same transformed content can't just be reposted five times. This file backs
Stage 5 of `SKILL.md`.
"""), "docs(platform): add file intro")

do(F, textwrap.dedent("""\

## TikTok

- **Retention gate:** ~65-70% of viewers must still be watching at 3 seconds
  or the algorithm stalls distribution. 70-85% retention at 3s roughly
  doubles views versus baseline; 85%+ is candidate for a bigger push.
- **Hook placement:** must land in the first 3 seconds — no slow fade-in, no
  logo intro, no "hey guys."
- **Format:** spoken hook (first 10-14 words) + text overlay (5-8 words, top
  third, high contrast) reinforcing the same idea — dual signal measurably
  improves 3-second hold.
- **Audio:** most viral TikToks have music or sound cued within the first 3
  seconds — silence at the open reads as low-effort.
- **Hashtags:** 3-5, one broad/viral, the rest niche and specific to the
  content.
- **Content tone:** happiness and humor outperform neutral tone; mild
  negative/contrarian content slightly outperforms neutral, flat content.
"""), "docs(platform): add TikTok rules")

do(F, textwrap.dedent("""\

## Instagram Reels

- **Length:** 15-90 seconds; 15-30 seconds performs best for reach.
- **Primary metric:** saves and shares outrank likes — optimize the ending
  for "save this" or "send to a friend," not just watch time.
- **Captions:** short, conversational, 2-3 lines. On-screen text carries the
  actual message more than the caption does.
- **Tone:** behind-the-scenes, relatable, personality-forward beats polished
  corporate framing.
- **CTA:** ask for a save or share explicitly — it performs better than a
  generic "let me know what you think."
"""), "docs(platform): add Instagram Reels rules")

do(F, textwrap.dedent("""\

## YouTube Shorts

- **Length:** 30-60 seconds is the sweet spot.
- **Discovery model:** Shorts compound through search, not feed velocity —
  this is the one platform where the title matters more than the hook.
- **Title:** write it as an SEO keyword phrase people would actually search,
  not a curiosity hook.
- **Content:** educational, how-to, and myth-busting content outperforms
  trend-chasing because it stays searchable after the trend dies.
- **Tradeoff:** lowest immediate engagement rate of the major short-form
  platforms, but the best passive, long-tail discovery.
"""), "docs(platform): add YouTube Shorts rules")

do(F, textwrap.dedent("""\

## X / Twitter

- **Hook window:** the first ~10 words are the entire hook — most of the
  audience is scanning a timeline, not settling in to watch.
- **Video format:** 15-30 seconds, 16:9 or 9:16.
- **Lifespan:** short — most engagement happens in the first 24-48 hours, so
  replying to early comments matters more here than on other platforms.
- **Structure:** a thread of 5-7 tweets, each able to stand alone,
  consistently outperforms a single long post for retention through the
  whole idea.
"""), "docs(platform): add X/Twitter rules")

do(F, textwrap.dedent("""\

## LinkedIn

- **Length:** 45-90 seconds, 4:5 or 1:1 aspect ratio.
- **Captions are mandatory, not optional** — roughly 85% of viewers watch
  muted. If there's no on-screen text, most of the audience gets nothing.
- **Upload:** native video only — posts with external links get
  algorithmically suppressed in favor of native content.
- **Tone:** a specific professional insight or founder story outperforms
  generic "LinkedIn voice" — avoid inspirational platitudes and corporate
  buzzwords entirely.
- **Format performance:** carousels currently get the highest engagement of
  any LinkedIn format, with native video next; both beat plain text posts by
  a wide margin.
- **CTA:** end with a specific, answerable question — "thoughts?" gets
  ignored; "what's the last tool you switched off because of this?" gets
  replies.
"""), "docs(platform): add LinkedIn rules")

# ---------------- psychology.md ----------------
F = "references/psychology.md"

do(F, textwrap.dedent("""\
# The Psychology Behind This Skill

This isn't a style guide invented from vibes — it's built on a small set of
well-replicated findings about attention and sharing. Understanding *why*
each rule in `SKILL.md` and `platform-rules.md` exists makes it easier to
apply them correctly to content they don't explicitly cover.

## The 3-second rule

Across TikTok, Reels, and Shorts, the large majority of viewers decide
whether to keep watching within the first three seconds. This isn't a
stylistic preference — it's the mechanism the recommendation algorithm uses
to decide whether to keep showing your content to anyone else. A technically
excellent video with a weak hook never gets the chance to compound, because
distribution is gated before the good part ever plays.
"""), "docs(psych): add file intro and 3-second rule"),

do(F, textwrap.dedent("""\

## Curiosity gaps (Loewenstein's Information Gap Theory)

A curiosity gap isn't intellectual interest — it's a mild state of
discomfort the brain is motivated to resolve. Three conditions make a gap
work:

1. **The viewer already knows enough to sense something's missing.** A
   "revealing a secret" hook with zero context just reads as confusing, not
   intriguing.
2. **The gap is specific**, not vague. "You're doing X wrong" consistently
   outperforms "wait until you see this" — a nameable gap is more compelling
   than a vague tease.
3. **The gap feels solvable within the length of the content.** An
   unresolvable gap produces frustration and drop-off, not engagement.

Headline specificity actually has a curved relationship with clicks: too
vague underperforms, but so does giving away the whole answer. The strongest
hooks name the shape of the answer without handing it over.
"""), "docs(psych): add curiosity gap theory")

do(F, textwrap.dedent("""\

## The Zeigarnik effect

Bluma Zeigarnik's 1927 finding: people remember unfinished tasks roughly
twice as well as completed ones. Applied to short-form content — open a loop
in the hook, maintain tension through the middle, and close the loop
explicitly at the end. The close matters as much as the open: a hook that
promises "3 mistakes" and only delivers two damages trust and depresses
performance on the *next* piece of content too, not just this one.
"""), "docs(psych): add Zeigarnik effect")

do(F, textwrap.dedent("""\

## Emotional arousal and sharing

High-arousal emotions drive sharing far more than low-arousal ones,
regardless of whether the emotion is positive or negative. Awe, anger, and
amusement are high-sharing emotions; sadness, contentment, and fear tend to
be low-sharing, even though all five are recognizable "strong" emotions.
Anger in particular is one of the most reliably viral emotions measured in
large media studies — but only when it's embedded in a story (problem →
discovery → resolution). Pure, un-narrated outrage fatigues an audience fast.

Front-load the emotional peak. Share-worthiness gets decided in roughly the
first 15 seconds — an emotional payoff that lands at 25 seconds has already
missed the window where most viewers who'd share, would.
"""), "docs(psych): add emotional arousal and sharing")

do(F, textwrap.dedent("""\

## The STEPPS framework

From Jonah Berger and Katherine Milkman's research on virality — six levers
that predict whether content gets shared:

- **Social Currency** — does sharing this make the sharer look good?
- **Triggers** — is there something in daily life that reminds people to
  share it?
- **Emotion** — does it produce genuine high-arousal feeling?
- **Public** — is the behavior or idea visible to others?
- **Practical Value** — does it actually help the person who shares it?
- **Stories** — is it carried by a narrative, not just a list of facts?

Not every post needs all six. Picking one or two deliberately (instead of
none) is usually the difference between content that gets watched and
content that gets shared.
"""), "docs(psych): add STEPPS framework")

do(F, textwrap.dedent("""\

## Applying this: the hook decision tree

For any piece of content, work through five questions in order:

1. **Audience** — do they already know the problem exists? What do they want,
   and what are they afraid of?
2. **Desired emotional state** — curiosity, anger, belonging, or aspiration?
   Pick the one lever that fits the real content, not the most dramatic
   option available.
3. **Information gap** — what do they already know, what's specifically
   missing, and can it be resolved within the length of this piece?
4. **Stakes** — what happens if they ignore this, and what do they gain if
   they don't?
5. **Hook selection** — map the above onto 2-3 candidates from
   `hook-formulas.md` and pick the one that doesn't require inventing
   anything to work.

Worked example:

> Content: "How a side project got to 40 GitHub stars in a week."
> Audience: developers with an unshipped side project (aware of the problem).
> Emotion: aspiration + mild frustration at their own inaction.
> Gap: what specifically got it seen, not just "how I grew it."
> Stakes: every week unshipped is a week a competitor could ship first.
> Hook candidates: a mistake-callout ("I sat on this for four months before
> posting it"), or a specific-number hook ("40 stars, one README rewrite").
"""), "docs(psych): add hook decision tree with worked example")

print("platform-rules.md and psychology.md build done")
