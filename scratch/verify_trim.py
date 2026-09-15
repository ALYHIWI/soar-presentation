import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = lines[:2944] + lines[4339:]
text = ''.join(new_lines)

ids = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print(f"Slide IDs count: {len(ids)}, IDs: {ids}")

sns = re.findall(r'<div class=["\']sn["\']>([^<]+)</div>', text)
print(f"Slide numbers (sn) count: {len(sns)}, sn: {sns}")
