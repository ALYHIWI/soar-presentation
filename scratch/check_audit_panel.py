with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function\s+openAuditPanel\b.*?\n\}', text, re.DOTALL)
if m:
    print("openAuditPanel found:")
    print(m.group(0)[:500])
else:
    print("openAuditPanel not matched with simple regex, searching...")
    idx = text.find('openAuditPanel')
    if idx != -1:
        print(text[idx:idx+500])
