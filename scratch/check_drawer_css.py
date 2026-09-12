import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check #refDrawer styling
idx = text.find('#refDrawer {')
end = text.find('/* ================= FLOATING ACTION CONTROLS', idx)
if end == -1:
    end = idx + 2500
print(text[idx:end])
