import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

emoji_pattern = re.compile(
    r'[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\u203c-\u2049]|[\u2190-\u21ff]|[\u2934-\u2935]'
)

# Common emojis
specific_emojis = ['📖', '📍', '🔍', '⚙️', '✓', '✕', '🛡️', '⚡', '🔁', '⚠️', '🚫', '🔄', '📊', '🚀', '⏱️', '🎯', '📄', '🏷️', '👥', '💡', '🎓', '🤖', '🔒', '📈', '🧩', '🛠️', '🔬', '📋', '✅', '❌']

found_emojis = []
for idx, line in enumerate(lines):
    line_emojis = []
    for ch in line:
        code = ord(ch)
        # Check emoji ranges:
        # Miscellaneous Symbols and Pictographs (1F300-1F5FF)
        # Emoticons (1F600-1F64F)
        # Transport and Map Symbols (1F680-1F6FF)
        # Supplemental Symbols and Pictographs (1F900-1F9FF)
        # Symbols and Pictographs Extended-A (1FA70-1FAFF)
        # Dingbats (2700-27BF), Misc Symbols (2600-26FF)
        if (0x1F300 <= code <= 0x1FAFF) or (0x2600 <= code <= 0x27BF) or ch in specific_emojis:
            line_emojis.append(ch)
    if line_emojis:
        found_emojis.append((idx + 1, list(set(line_emojis)), line.strip()[:100]))

print(f"Total lines containing emojis or symbols: {len(found_emojis)}")
for line_no, emojis, text_preview in found_emojis:
    print(f"Line {line_no:4d}: emojis={emojis} | {text_preview}")
