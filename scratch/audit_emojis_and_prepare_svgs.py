import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where emojis are used in the slides (between line 2028 and 3100)
lines = text.splitlines()

slide_emojis = []
for i, l in enumerate(lines):
    if i >= 2025 and i <= 3150:
        for ch in ['✅', '🔄', '📋', '⚠️', '🚫', '🛡️', '🛡', '⚡', '🧠', '📡', '🔍', '⚙️', '⚙', '✨', '✓', '✕']:
            if ch in l:
                slide_emojis.append((i+1, ch, l.strip()[:100]))

print(f"Slide emoji occurrences: {len(slide_emojis)}")
for l_no, ch, prev in slide_emojis:
    print(f"Line {l_no:4d} [{ch}]: {prev}")
