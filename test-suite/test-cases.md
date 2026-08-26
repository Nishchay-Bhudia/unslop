# Test Cases

20 inputs spanning platform, content type, and AI-pattern density, used to
sanity-check changes to `SKILL.md`. For each: run the skill, then score the
output 1-5 on authenticity, specificity, hook quality, platform fit,
conversational tone, and payoff delivery (see `references/ai-patterns.md`
and `SKILL.md` Stage 6 for the rubric). A score of 3 or below on any axis
means the transformation needs another pass, not a ship.

### Test 1: SaaS launch
- **Input:** Generic AI product-announcement paragraph, no numbers.
- **Platform:** TikTok
- **Expected transformation behavior:** Contrarian or how-to-promise hook; forces the user to supply one real number.

### Test 2: Founder story
- **Input:** Vague 'exciting journey' personal post.
- **Platform:** LinkedIn
- **Expected transformation behavior:** Professional insight frame, mandatory captions, one honest tradeoff surfaced.

### Test 3: 3-step process
- **Input:** Listicle with no audience framing.
- **Platform:** YouTube Shorts
- **Expected transformation behavior:** SEO-keyword title; list reframed around a named audience.

### Test 4: Contrarian take
- **Input:** Flat opinion statement, no stakes.
- **Platform:** X/Twitter
- **Expected transformation behavior:** Thread structure, first-10-words hook, one tweet per beat.

### Test 5: Behind-the-scenes
- **Input:** Raw description with no visual cue.
- **Platform:** Instagram Reels
- **Expected transformation behavior:** Conversational caption, visual-pattern-interrupt hook, save-focused CTA.

### Test 6: 7-item listicle
- **Input:** '7 things everyone misses,' generic.
- **Platform:** TikTok
- **Expected transformation behavior:** Compressed into a 60s narrative arc, not a read-off list.

### Test 7: Case study
- **Input:** Vague 'significant results' claim, no numbers.
- **Platform:** LinkedIn
- **Expected transformation behavior:** Skill should ask for the real number rather than inventing one.

### Test 8: User complaint
- **Input:** Frustrated but unfocused paragraph.
- **Platform:** TikTok
- **Expected transformation behavior:** Empathy hook + specific stakes, not generic outrage.

### Test 9: Feature announcement
- **Input:** Corporate tone, buzzword-heavy.
- **Platform:** LinkedIn
- **Expected transformation behavior:** Buzzwords stripped, one concrete before/after detail added.

### Test 10: Wellness content
- **Input:** Extremely generic, could be about anything.
- **Platform:** All platforms
- **Expected transformation behavior:** Full pipeline run per platform; checks the skill doesn't just reformat, it re-hooks.

### Test 11: Already-human draft
- **Input:** A genuinely well-written, specific post.
- **Platform:** TikTok
- **Expected transformation behavior:** Skill should recognize this and make minimal or no changes — tests against over-editing.

### Test 12: Missing platform
- **Input:** Solid content, platform unspecified.
- **Platform:** Unspecified
- **Expected transformation behavior:** Skill should ask which platform rather than guessing wrong.

### Test 13: Fabrication bait
- **Input:** Draft implies stats the user never gave.
- **Platform:** LinkedIn
- **Expected transformation behavior:** Skill must flag the missing number, not invent one — core guardrail test.

### Test 14: Thread-worthy idea
- **Input:** Dense single paragraph, too much for one post.
- **Platform:** X/Twitter
- **Expected transformation behavior:** Skill should recommend and build a thread, not force it into one tweet.

### Test 15: Cold audience pitch
- **Input:** Assumes the reader already knows the product.
- **Platform:** TikTok
- **Expected transformation behavior:** Skill should reframe for a cold, unaware audience (contrarian/curiosity hook).

### Test 16: Warm audience update
- **Input:** Written as if for strangers.
- **Platform:** Instagram Reels
- **Expected transformation behavior:** Skill should shift to BAB framing since the real audience already follows the creator.

### Test 17: Overly emotional draft
- **Input:** All-caps outrage, no narrative.
- **Platform:** TikTok
- **Expected transformation behavior:** Skill should embed the anger in a real story arc, not just amplify volume.

### Test 18: Text-heavy LinkedIn post
- **Input:** No caption/visual plan at all.
- **Platform:** LinkedIn
- **Expected transformation behavior:** Skill must add the mandatory on-screen caption plan, not just rewrite prose.
