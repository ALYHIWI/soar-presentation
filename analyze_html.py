# -*- coding: utf-8 -*-
with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the wrap div in body (not in CSS)
body_content = content[39195:]  # after body start
wrap_in_body = body_content.find('id="wrap"')
if wrap_in_body == -1:
    wrap_in_body = body_content.find("id='wrap'")
print("wrap in body at:", wrap_in_body + 39195)

# Print the content starting from the wrap div
wrap_abs = 39195 + wrap_in_body
print("Content around wrap in body:")
print(content[wrap_abs:wrap_abs+1000])
