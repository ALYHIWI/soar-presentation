import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check script tags
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Total inline scripts: {len(scripts)}")
for i, s in enumerate(scripts):
    print(f"Script {i+1} length: {len(s)}")

# Check localStorage usage
for line in html.splitlines():
    if 'localStorage' in line:
        print("localStorage usage:", line.strip())

# Check currentSlide / init
for line in html.splitlines():
    if 'currentSlide' in line or 'showSlide' in line or 'active' in line and 'class' in line:
        if len(line.strip()) < 120:
            print("Slide logic:", line.strip())
