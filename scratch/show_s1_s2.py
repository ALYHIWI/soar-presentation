import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def show_slide_body(sid):
    m = re.search(rf'(<section\s+class="slide[^"]*"\s+id="{sid}"[^>]*>.*?</section>)', html, re.DOTALL)
    if not m:
        print(f"Slide {sid} not found")
        return
    body = m.group(1).split('<div class="slide-ref-footer"')[0]
    print(f"=== SLIDE {sid} BODY ===")
    print(body)

show_slide_body('s1')
show_slide_body('s2')
