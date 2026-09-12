with open('presentation/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find keydown event listener
idx = text.find("keydown")
while idx != -1:
    print("Found keydown at:", idx)
    print(text[idx:idx+600])
    print("="*50)
    idx = text.find("keydown", idx+1)
