import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function updateSlideReferences')
end = text.find('</script>', idx)
print(text[idx:end])
