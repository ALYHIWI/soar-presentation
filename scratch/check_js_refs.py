import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract SLIDE_REFS
idx = text.find('const SLIDE_REFS =')
if idx != -1:
    end_idx = text.find('};', idx) + 2
    refs_code = text[idx:end_idx]
    print(f"SLIDE_REFS found, length: {len(refs_code)}")
    # count how many slide entries like '01': or 's0': or similar
    entries = re.findall(r'[\'"]?(\d+|s\d+)[\'"]?\s*:\s*\{', refs_code)
    print(f"Entries count: {len(entries)}")
    print(f"Entry keys: {entries}")
else:
    print("SLIDE_REFS not found!")
