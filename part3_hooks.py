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

F = "references/hook-formulas.md"

do(F, textwrap.dedent("""\
# Hook Formulas (38)

Every hook here is organized by the psychological lever it pulls, with a
concrete example — not a template with `[blank]` in it. Pick based on
audience awareness (does the viewer already know the problem exists?) and
platform (TikTok needs the hook in the first 3 seconds; LinkedIn can take a
full sentence). See `SKILL.md` Stage 3a for the selection logic.

Never fill these with numbers or claims the user didn't actually provide —
a hook with a fabricated statistic is worse than a slower, honest one.

## Curiosity-driven
"""), "docs(hooks): add file intro and curiosity section header")

CURIOSITY = [
    ("The Cliffhanger", '"What if I told you the thing you\'re optimizing for is the wrong metric?" — opens a gap without naming the answer yet.'),
    ("The Open Loop", '"The thing nobody tells you about going full-time..." — promises insider information, doesn\'t give it away in the hook.'),
    ("The Specific Number", '"3 mistakes I see every new creator make" — odd, specific numbers read as data, not filler.'),
    ("Counterintuitive Claim", '"Posting less got me more engagement" — violates the obvious assumption, forces a re-read.'),
    ("The Question Hook", '"How many of you have made this exact mistake?" — implicates the viewer directly.'),
    ("Impossibly Specific Number", '"We spent $87,000 to find this out" — a number too precise to be made up reads as credible.'),
    ("The Secret Reveal", '"Nobody\'s talking about what actually moves the needle here" — implies exclusive access.'),
    ("The Countdown Tease", '"In five seconds I\'ll show you the actual number" — creates a short, bridgeable wait.'),
    ("The Mistake Callout", '"I did this wrong for six months before I noticed" — pairs vulnerability with a coming payoff.'),
    ("Expectation Violation", '"This will change how you think about X" — only works if the next line actually delivers something surprising.'),
    ("The Unfinished Sentence", 'Cut the hook mid-thought on screen text while the voiceover keeps going — forces the eye to keep reading.'),
]
for i, (name, ex) in enumerate(CURIOSITY, start=1):
    do(F, f"\n{i}. **{name}** — {ex}\n", f"docs(hooks): add curiosity hook #{i} — {name}")

do(F, "\n## Authority & proof\n", "docs(hooks): add authority section header")
AUTHORITY = [
    ("Credential Lead", '"As someone who\'s shipped 40 Claude Skills..." — only use a credential the user actually has.'),
    ("Case Study Lead", '"I tested this against 500 real creators" — leads with the method, not the adjective.'),
    ("Insider Reveal", '"Working inside the algorithm team taught me this" — implies access; must be true, not aspirational.'),
    ("Social Proof Opener", '"12,000 people are already doing this wrong" — a real, checkable number beats "everyone".'),
    ("Data Hook", 'Lead with the sample size before the finding: "Across 200 tests, the pattern held." Bigger, real numbers carry more weight than vague ones.'),
    ("Before/After Data", 'Quantify the transformation exactly: "3.3% to 11% completion rate" beats "way better retention."'),
]
for i, (name, ex) in enumerate(AUTHORITY, start=1):
    do(F, f"\n{i}. **{name}** — {ex}\n", f"docs(hooks): add authority hook #{i} — {name}")

do(F, "\n## Emotional triggers\n", "docs(hooks): add emotional section header")
EMOTIONAL = [
    ("Fear / FOMO", '"Everyone except you is already doing this" — use sparingly; overused it reads as manipulative.'),
    ("Anger / Outrage", '"The industry benefits from you not knowing this" — needs a real grievance behind it, not manufactured outrage.'),
    ("Empathy / Belonging", '"If you\'ve ever stared at a blank caption box for twenty minutes..." — names a specific, relatable moment.'),
    ("Desire / Aspiration", '"This is what actually sustainable growth looks like" — pairs best with a visual, not just text.'),
    ("Relatable Frustration", '"That exact moment you realize you\'ve been doing this backwards" — self-recognition triggers a comment, not just a watch.'),
    ("Confession", '"I\'m going to admit something most creators won\'t" — works only if what follows is a real admission, not a humblebrag.'),
    ("Mistake Ownership", '"I got this completely wrong for two years" — vulnerability plus a coming correction.'),
]
for i, (name, ex) in enumerate(EMOTIONAL, start=1):
    do(F, f"\n{i}. **{name}** — {ex}\n", f"docs(hooks): add emotional hook #{i} — {name}")

do(F, "\n## Story & narrative\n", "docs(hooks): add narrative section header")
NARRATIVE = [
    ("Cold Open (In Media Res)", 'Start mid-action with zero setup: "So the repo hits 40 stars and then it just stops." No preamble.'),
    ("Before/After Contrast", '"This is what my content looked like a year ago. This is what it looks like now." — needs two real, comparable artifacts.'),
    ("Failure-to-Success Arc", '"I failed at this about a dozen times before it clicked" — the number of failures should be real, not rounded up for drama.'),
    ('"They Laughed" Structure', '"Everyone told me this wouldn\'t work — here\'s what happened" — only use if there was genuine, real pushback.'),
]
for i, (name, ex) in enumerate(NARRATIVE, start=1):
    do(F, f"\n{i}. **{name}** — {ex}\n", f"docs(hooks): add narrative hook #{i} — {name}")

do(F, "\n## Direct & tactical\n", "docs(hooks): add tactical section header")
TACTICAL = [
    ("How-To Promise", '"Here\'s the exact 3-step process" — only promise a count you actually deliver.'),
    ("Tool Reveal", '"I built a tool that does X in one step" — lead with what it does, not how proud you are of it.'),
    ("Framework Reveal", '"This is the framework I use for every launch" — name the framework so it\'s memorable and shareable.'),
    ("Instant Payoff", 'Lead with the single most surprising fact instead of building up to it — good for cold, low-attention audiences.'),
]
for i, (name, ex) in enumerate(TACTICAL, start=1):
    do(F, f"\n{i}. **{name}** — {ex}\n", f"docs(hooks): add tactical hook #{i} — {name}")

do(F, "\n## Platform-native\n", "docs(hooks): add platform-native section header")
PLATFORM = [
    ("Scroll-Stop Visual", 'A pattern-interrupt cut or on-screen text that breaks visual rhythm in the first frame — words alone won\'t stop a thumb.'),
    ("Reply / Quote Hook", '"Replying to everyone who asked how I actually did this" — frames the post as answering real demand.'),
    ("Thread / Series Hook", '"Long thread on this, worth the read" — sets expectation up front so people don\'t bounce mid-thread.'),
    ("Subject Line Double-Punch", 'Bold on-screen claim plus a question in the same frame — gives both a skimmer and a reader a reason to stop.'),
    ("Timestamp Hook", '"This is happening right now" — only honest when it\'s actually current; stale "urgent" content reads as manipulative fast.'),
    ("Investment Specificity", '"I put in $4,200 and got back $11,000" — exact numbers, not round ones, read as real.'),
]
for i, (name, ex) in enumerate(PLATFORM, start=1):
    do(F, f"\n{i}. **{name}** — {ex}\n", f"docs(hooks): add platform-native hook #{i} — {name}")

do(F, textwrap.dedent("""\

## Compound hooks

Single-trigger hooks work. Stacking two triggers (e.g. desire + FOMO) works
better. Three (authority + desire + anger) is the strongest — but only when
every element in the stack is true. Example:

> "I spent $50K on courses to learn what I'm about to give you for free —
> and honestly, I'm still annoyed about it."

That's a credential lead (authority) + practical value (desire) + a real,
specific grievance (anger) in one sentence. Don't stack triggers you can't
back up; a compound hook with one fabricated element collapses the whole
thing when a viewer calls it out in the comments.
"""), "docs(hooks): add compound hook stacking guidance")

print("hook-formulas.md build done")
