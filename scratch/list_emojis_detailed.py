import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all unique non-ascii characters that might be emojis or symbols
chars = set()
for ch in text:
    code = ord(ch)
    # Exclude standard arabic (0x0600-0x06FF), arabic supplement (0x0750-0x077F), common punctuation, quotes, dashes
    if code > 127:
        if not (0x0600 <= code <= 0x06FF or 0x0750 <= code <= 0x077F or 0xFB50 <= code <= 0xFDFF or 0xFE70 <= code <= 0xFEFF):
            if ch not in ['’', '‘', '“', '”', '—', '–', '…', '·', '•', '°', '«', '»', '§', '±', '×', '÷', '≥', '≤', '≠', '≈', 'α', 'β', 'γ', 'λ', 'μ', 'π', 'σ', 'τ', 'φ', 'Δ', 'Σ', '→', '←', '↔', '⇒', '⇔', '↑', '↓', '▸', '◂', '▪', '▫']:
                chars.add((ch, hex(code), unicodedata.name(ch, 'UNKNOWN') if 'unicodedata' in sys.modules else ''))

import unicodedata
for ch, hx, _ in sorted(list(chars), key=lambda x: x[1]):
    try:
        nm = unicodedata.name(ch)
    except:
        nm = "UNKNOWN"
    print(f"Char: '{ch}' (Code: {hx}, Name: {nm})")
