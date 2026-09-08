import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

slides = re.findall(r'<section class="slide[^"]*" id="(s\d+)">', content)
print(f'Total slides found: {len(slides)}')
print(f'Slide IDs: {slides[0]} to {slides[-1]}')

sn_matches = re.findall(r'<div class="sn">(\d+ / \d+)</div>', content)
print(f'Total badges: {len(sn_matches)}, First: {sn_matches[0]}, Last: {sn_matches[-1]}')

en_count = len(re.findall(r'class="[^"]*\ben\b', content))
ar_count = len(re.findall(r'class="[^"]*\bar\b', content))
print(f'English elements: {en_count}, Arabic elements: {ar_count}')

svg_count = content.count('<svg')
print(f'Total SVG icons embedded: {svg_count}')

assert len(slides) == 25, f'Expected 25 slides, got {len(slides)}'
assert len(sn_matches) == 25, f'Expected 25 badges, got {len(sn_matches)}'
assert 'const N = 25;' in content
print('ALL VERIFICATION CHECKS PASSED!')
