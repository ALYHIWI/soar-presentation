import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sections = list(re.finditer(r'<section\b[^>]*>', content, re.IGNORECASE))
print(f"Total <section> tags: {len(sections)}")

slide_sections = []
for i, m in enumerate(sections):
    tag = m.group(0)
    # extract id and class
    id_m = re.search(r'id=["\']([^"\']+)["\']', tag)
    cls_m = re.search(r'class=["\']([^"\']+)["\']', tag)
    slide_id = id_m.group(1) if id_m else "no-id"
    slide_cls = cls_m.group(1) if cls_m else "no-class"
    slide_sections.append((slide_id, slide_cls, m.start()))

print("\nAll sections found:")
for idx, (s_id, s_cls, pos) in enumerate(slide_sections):
    line_no = content[:pos].count('\n') + 1
    print(f"{idx+1:2d}. Line {line_no:4d}: id='{s_id}', class='{s_cls}'")

# Check const N in JS
n_matches = re.findall(r'const\s+N\s*=\s*(\d+)', content)
print(f"\nconst N in JS: {n_matches}")
