import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# search for updateSlideReferences or refDrawer
for m in re.finditer(r'updateSlideReferences|refDrawer|toggleRefModal', text):
    pos = m.start()
    line_no = text[:pos].count('\n') + 1
    print(f"Match '{m.group(0)}' at line {line_no}")

# search for objects containing slide data
for m in re.finditer(r'(var|let|const)\s+([a-zA-Z0-9_]+)\s*=\s*\{[^\}]*chapter', text, re.IGNORECASE):
    print(f"Candidate data object: {m.group(2)}")
