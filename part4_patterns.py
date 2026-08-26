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

F = "references/ai-patterns.md"

do(F, textwrap.dedent("""\
# AI Writing Patterns Checklist (25 points)

These are stylistic tells, not proof of AI authorship — human writers can hit
some of these too. The value isn't detection, it's a checklist: if a draft
trips several of these at once, it reads as generic regardless of who or what
wrote it. Each entry has the pattern, why it reads as generic, and a fix.

## Structural patterns
"""), "docs(patterns): add file intro and structural section header")

STRUCTURAL = [
    ("Uniform sentence length", "Sentences cluster around 12-18 words with little variance.", "Mix a 4-word sentence with a 28-word one in the same paragraph."),
    ("Excessive transitions", '"In summary", "as a result", "overall", "furthermore" used more than ~2x per 300 words.', "Cut them. Ideas can follow each other without a label."),
    ("Hedging language overload", '"may", "might", "could", "suggests", "appears to" stacked defensively.', "State the point directly, or cut it if you're not confident enough to."),
    ("Over-perfect grammar", "Zero contractions, fragments, or false starts across a long piece.", "Let a sentence trail off or start with \"And\" — real writing isn't uniformly polished."),
    ("Symmetrical paragraph structure", "Every paragraph follows topic sentence → explanation → mini-summary.", "Vary paragraph shape; let some be one line."),
]
for i, (name, why, fix) in enumerate(STRUCTURAL, start=1):
    do(F, f"\n{i}. **{name}** — {why} *Fix:* {fix}\n", f"docs(patterns): add structural pattern #{i} — {name}")

do(F, "\n## Vocabulary tells\n", "docs(patterns): add vocabulary section header")
VOCAB = [
    ("Repetitive AI vocabulary", '"delve into", "testament to", "in the realm of", "unlock", "game-changing", "revolutionize".', "Replace with the plain verb: \"look at\", \"shows\", \"in\", \"get\", \"useful\", \"change\"."),
    ("Generic adjectives", '"better", "easier", "powerful" with no referent.', "Attach a number or a mechanism: \"40% faster\", \"one-click setup\"."),
    ("Excessive em dashes", "Em dashes in more than ~30% of sentences.", "Swap half of them for periods or commas."),
    ("Systematic punctuation", "Perfectly consistent Oxford commas, zero regional variance, minimal contractions.", "Let punctuation vary slightly the way a real person's does."),
    ("Proper noun avoidance / generic names", '60-70% of invented example names default to "Emily", "Sarah", "John".', "Use a specific, less-common name, or better, a real one with permission."),
]
for i, (name, why, fix) in enumerate(VOCAB, start=1):
    do(F, f"\n{i}. **{name}** — {why} *Fix:* {fix}\n", f"docs(patterns): add vocabulary pattern #{i} — {name}")

do(F, "\n## Content-level tells\n", "docs(patterns): add content section header")
CONTENT = [
    ("Lack of specific detail", "Broad abstractions instead of a timestamp, a name, a sensory detail.", "Add the exact number, date, or name — even a small one."),
    ("Vague sourcing", '"Studies show", "experts argue" with no author, journal, or date.', "Cite it properly, or replace with \"based on what I've tested\" if that's true."),
    ("Predictable structure", "Definition → explanation → summary, every time.", "Open in the middle of the story instead of with a definition."),
    ("Formulaic constructions", '"It is not just X. It is also Y."', "Say the actual thing plainly instead of using the template."),
    ("Generic lists", '"3 things you need to know" with no audience-specific framing.', "Name who the list is actually for and why these three, not others."),
    ("Fake conversational tone", "Reads as rehearsed casualness rather than actual conversation.", "Write it the way you'd actually text a friend the idea, then tighten."),
    ("Over-explanation", "Explains obvious things as if to a total novice.", "Cut the sentence that restates what the reader already inferred."),
]
for i, (name, why, fix) in enumerate(CONTENT, start=1):
    do(F, f"\n{i}. **{name}** — {why} *Fix:* {fix}\n", f"docs(patterns): add content pattern #{i} — {name}")

do(F, "\n## Detection-adjacent tells (use with caution)\n", "docs(patterns): add detection-adjacent section header")
DETECT = [
    ("Zero regional English variance", "No trace of the writer's actual dialect, region, or idiom.", "Let real idiom through instead of smoothing it into 'standard' English."),
    ("Flat emotional register", "Same emotional intensity from the first line to the last.", "Let intensity rise and fall — real stories have a climax, not a plateau."),
    ("No factual specificity that could be checked", "Every claim is phrased so it can't actually be verified or falsified.", "State something concrete enough that it could be wrong — that's what makes it credible."),
]
for i, (name, why, fix) in enumerate(DETECT, start=1):
    do(F, f"\n{i}. **{name}** — {why} *Fix:* {fix}\n", f"docs(patterns): add detection-adjacent pattern #{i} — {name}")

do(F, textwrap.dedent("""\

## A note on AI detectors

AI detectors have documented false-positive rates as high as 40-80% on
non-native English speakers, technical writing, and structured documents.
This checklist is not a detector-evasion tool and doesn't promise to beat
one. It's a style checklist: content that trips several of these patterns at
once reads as generic to a human reader, independent of whatever a detector
says about it. Optimize for the reader, not the classifier.
"""), "docs(patterns): add note on AI detector unreliability")

print("ai-patterns.md build done")
