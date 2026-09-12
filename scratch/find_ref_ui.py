import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['rdModal', 'refDrawer', 'openRef', 'toggleRef', 'rdSlidePill', 'cpSlideRefContent']:
    matches = [m.start() for m in re.finditer(re.escape(term), text)]
    print(f"Term '{term}': {len(matches)} occurrences")
    for m in matches[:3]:
        print("  " + text[max(0, m-50):min(len(text), m+100)].replace('\n', ' '))
