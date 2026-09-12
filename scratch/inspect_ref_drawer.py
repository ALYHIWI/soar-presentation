import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Inspect #refDrawer HTML
m = re.search(r'(<!-- FLOATING SLIDE SOURCE REFERENCES DRAWER -->.*?</div>\s*</div>)', text, re.DOTALL)
if m:
    print("=== #refDrawer HTML ===")
    print(m.group(1)[:1500])

# 2. Inspect #refDrawer CSS
m_css = re.search(r'(/\* Reference Inspector Modal / Drawer \*/.*?)(?=/\*|$)', text, re.DOTALL)
if m_css:
    print("\n=== #refDrawer CSS ===")
    print(m_css.group(1)[:1500])
