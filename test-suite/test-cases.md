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
