import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m10 = re.search(r'<section\b[^>]*id=["\']s10["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if m10:
    with open('scratch/s10_current.html', 'w', encoding='utf-8') as out:
        out.write(m10.group(1))
    print("Exported current s10")
else:
    print("s10 not found")
