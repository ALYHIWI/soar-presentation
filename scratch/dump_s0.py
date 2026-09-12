import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'(<section\s+class="slide[^"]*"\s+id="s0"[^>]*>.*?</section>)', html, re.DOTALL)
if m:
    with open('scratch/slide_s0.html', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
    print('Saved scratch/slide_s0.html')
else:
    print('s0 NOT FOUND!')
