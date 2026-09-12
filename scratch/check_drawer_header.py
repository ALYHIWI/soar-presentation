import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the exact HTML of #refDrawer header
m = re.search(r'<div id="refDrawer">.*?<div class="rd-header">(.*?)</div>', html, re.DOTALL)
if m:
    print("Current rd-header:")
    print(m.group(1))
