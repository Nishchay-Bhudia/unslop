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

F = "test-suite/test-cases.md"

do(F, textwrap.dedent("""\
# Test Cases

20 inputs spanning platform, content type, and AI-pattern density, used to
sanity-check changes to `SKILL.md`. For each: run the skill, then score the
output 1-5 on authenticity, specificity, hook quality, platform fit,
conversational tone, and payoff delivery (see `references/ai-patterns.md`
and `SKILL.md` Stage 6 for the rubric). A score of 3 or below on any axis
means the transformation needs another pass, not a ship.
"""), "docs(tests): add test suite intro and scoring rubric")

CASES = [
    ("SaaS launch", "Generic AI product-announcement paragraph, no numbers.", "TikTok", "Contrarian or how-to-promise hook; forces the user to supply one real number."),
    ("Founder story", "Vague 'exciting journey' personal post.", "LinkedIn", "Professional insight frame, mandatory captions, one honest tradeoff surfaced."),
    ("3-step process", "Listicle with no audience framing.", "YouTube Shorts", "SEO-keyword title; list reframed around a named audience."),
    ("Contrarian take", "Flat opinion statement, no stakes.", "X/Twitter", "Thread structure, first-10-words hook, one tweet per beat."),
    ("Behind-the-scenes", "Raw description with no visual cue.", "Instagram Reels", "Conversational caption, visual-pattern-interrupt hook, save-focused CTA."),
    ("7-item listicle", "'7 things everyone misses,' generic.", "TikTok", "Compressed into a 60s narrative arc, not a read-off list."),
    ("Case study", "Vague 'significant results' claim, no numbers.", "LinkedIn", "Skill should ask for the real number rather than inventing one."),
    ("User complaint", "Frustrated but unfocused paragraph.", "TikTok", "Empathy hook + specific stakes, not generic outrage."),
    ("Feature announcement", "Corporate tone, buzzword-heavy.", "LinkedIn", "Buzzwords stripped, one concrete before/after detail added."),
    ("Wellness content", "Extremely generic, could be about anything.", "All platforms", "Full pipeline run per platform; checks the skill doesn't just reformat, it re-hooks."),
    ("Already-human draft", "A genuinely well-written, specific post.", "TikTok", "Skill should recognize this and make minimal or no changes — tests against over-editing."),
    ("Missing platform", "Solid content, platform unspecified.", "Unspecified", "Skill should ask which platform rather than guessing wrong."),
    ("Fabrication bait", "Draft implies stats the user never gave.", "LinkedIn", "Skill must flag the missing number, not invent one — core guardrail test."),
    ("Thread-worthy idea", "Dense single paragraph, too much for one post.", "X/Twitter", "Skill should recommend and build a thread, not force it into one tweet."),
    ("Cold audience pitch", "Assumes the reader already knows the product.", "TikTok", "Skill should reframe for a cold, unaware audience (contrarian/curiosity hook)."),
    ("Warm audience update", "Written as if for strangers.", "Instagram Reels", "Skill should shift to BAB framing since the real audience already follows the creator."),
    ("Overly emotional draft", "All-caps outrage, no narrative.", "TikTok", "Skill should embed the anger in a real story arc, not just amplify volume."),
    ("Text-heavy LinkedIn post", "No caption/visual plan at all.", "LinkedIn", "Skill must add the mandatory on-screen caption plan, not just rewrite prose."),
    ("Trend-chasing Shorts script", "Built around a fading trend, no evergreen value.", "YouTube Shorts", "Skill should reframe around search-durable value per platform rules."),
    ("Multi-platform brief", "One paragraph, user wants 3 platform versions.", "TikTok + Reels + LinkedIn", "Skill should run the Advanced Options multi-platform pass, not repeat one output three times."),
]

for i, (name, inp, platform, expect) in enumerate(CASES, start=1):
    block = f"""
### Test {i}: {name}
- **Input:** {inp}
- **Platform:** {platform}
- **Expected transformation behavior:** {expect}
"""
    do(F, block, f"docs(tests): add test case {i} — {name}")

print("test-cases.md build done")
