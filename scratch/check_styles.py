import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check fonts in head
fonts = re.findall(r'<link[^>]*fonts\.googleapis\.com[^>]*>', text)
print("Fonts loaded:", fonts)

# Check CSS variables
vars_block = re.findall(r':root\s*\{([^}]+)\}', text)
if vars_block:
    print("\nCSS Root Variables:")
    for l in vars_block[0].splitlines()[:25]:
        print("  " + l.strip())

# Check slide style rules
print("\nSlide styling rules:")
for r in ['.slide {', '.card {', '.st {', '.hero {', '.sn {']:
    pos = text.find(r)
    if pos != -1:
        print(f"--- Rule {r} ---")
        print(text[pos:pos+200].strip())
