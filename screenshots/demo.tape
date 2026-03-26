Output demo.gif

Require copier
Require tree
Require hatch

Set Shell "zsh"
Set FontSize 13
Set Width 1200
Set Height 750
Set Theme "Dracula"
Set TypingSpeed 75ms
Set Padding 20
Set WindowBar Colorful

# ── Preparation: clean up any previous demo run ────────────────────────────
Hide
Type "cd /tmp && rm -rf demo-music-app"
Enter
Sleep 1s
Show

# ── Welcome ─────────────────────────────────────────────────────────────────
Type "echo '  django-app-starter — A Copier template for Django reusable apps'"
Enter
Type "echo ''"
Enter
Sleep 2s

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  STEP 1 — Generate a new Django app using copier                        ║
# ╚══════════════════════════════════════════════════════════════════════════╝

Type "echo '  ── Step 1: Generate a new Django app with copier ──────────────────'"
Enter
Type "echo '  copier will ask a few questions and scaffold the full project for us'"
Enter
Sleep 2s

Type "copier copy gh:matagus/django-app-starter /tmp/demo-music-app"
Enter
Sleep 3s

# Project name
Type@150ms "django-music"
Enter
Sleep 1s

# Module name
Type@100ms "music"
Enter
Sleep 1s

# Description
Type@100ms "A Django app for managing music collections"
Enter
Sleep 1s

Sleep 6s

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  STEP 2 — Explore the generated project structure                       ║
# ╚══════════════════════════════════════════════════════════════════════════╝

Type "echo ''"
Enter
Type "echo '  ── Step 2: Explore the generated project structure ────────────────'"
Enter
Type "echo '  The template created everything you need: app, tests, docs, CI & more'"
Enter
Sleep 2s

Type "cd /tmp/demo-music-app && tree -L 2 ."
Enter
Sleep 3s

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  STEP 3 — Run the test suite with hatch                                 ║
# ╚══════════════════════════════════════════════════════════════════════════╝

Type "echo ''"
Enter
Type "echo '  ── Step 3: Run tests with hatch ────────────────────────────────────'"
Enter
Type "echo '  hatch manages virtualenvs automatically across Python & Django versions'"
Enter
Sleep 2s

# Run a single matrix combo to keep the demo fast (Python 3.13 + Django 5.2)
Type "hatch run test:test"
Enter
Sleep 30s

# ── Clean up ────────────────────────────────────────────────────────────────
Hide
Type "cd /tmp && rm -rf demo-music-app"
Enter
Sleep 1s
Show

Type "echo ''"
Enter
Type "echo '  Ready to build your Django app? → https://github.com/matagus/django-app-starter'"
Enter
Sleep 10s
