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

def do(path, content, msg):
    write(path, content)
    commit(msg)

do("assets/banner.svg", textwrap.dedent("""\
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1a1a2e"/>
      <stop offset="55%" stop-color="#4a2a6a"/>
      <stop offset="100%" stop-color="#d97757"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="280" rx="24" fill="url(#bg)"/>
  <text x="60" y="120" font-family="Helvetica, Arial, sans-serif" font-size="64" font-weight="700" fill="#ffffff">Un-AI-ify</text>
  <text x="60" y="168" font-family="Helvetica, Arial, sans-serif" font-size="26" fill="#f0e6e0">A Claude Skill that turns AI-sounding scripts into platform-native, human posts</text>
  <text x="60" y="230" font-family="Helvetica, Arial, sans-serif" font-size="18" fill="#d0c0d0">TikTok &#8226; Reels &#8226; Shorts &#8226; X &#8226; LinkedIn</text>
</svg>
"""), "assets: add README banner svg")

do("assets/hook-formula-diagram.svg", textwrap.dedent("""\
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="220" viewBox="0 0 900 220">
  <style>
    .box { fill: #241d2e; stroke: #d97757; stroke-width: 2; rx: 12; }
    .label { font-family: Helvetica, Arial, sans-serif; font-size: 22px; fill: #ffffff; font-weight: 700; }
    .sub { font-family: Helvetica, Arial, sans-serif; font-size: 14px; fill: #cbb9c9; }
    .arrow { stroke: #d97757; stroke-width: 3; marker-end: url(#arrowhead); }
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#d97757"/>
    </marker>
  </defs>
  <rect x="20" y="60" width="240" height="100" class="box"/>
  <text x="140" y="105" text-anchor="middle" class="label">HOOK</text>
  <text x="140" y="130" text-anchor="middle" class="sub">0-3s &#8226; stop the scroll</text>

  <line x1="260" y1="110" x2="330" y2="110" class="arrow"/>

  <rect x="330" y="60" width="240" height="100" class="box"/>
  <text x="450" y="105" text-anchor="middle" class="label">HOLD</text>
  <text x="450" y="130" text-anchor="middle" class="sub">deepen the gap, raise stakes</text>

  <line x1="570" y1="110" x2="640" y2="110" class="arrow"/>

  <rect x="640" y="60" width="240" height="100" class="box"/>
  <text x="760" y="105" text-anchor="middle" class="label">PAYOFF</text>
  <text x="760" y="130" text-anchor="middle" class="sub">deliver what the hook promised</text>
</svg>
"""), "assets: add hook-hold-payoff diagram svg")

print("assets build done")
