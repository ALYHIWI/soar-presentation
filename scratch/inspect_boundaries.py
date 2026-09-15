with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

print("\n--- Checking lines 2020-2030 ---")
for i in range(2020, 2032):
    print(f"{i+1}: {lines[i].rstrip()[:100]}")

print("\n--- Checking lines 2938-2955 ---")
for i in range(2938, 2955):
    print(f"{i+1}: {lines[i].rstrip()[:100]}")

s24_line = None
old_slides_end_line = None
script_line = None

for i in range(2950, len(lines)):
    if 'id="s24"' in lines[i]:
        s24_line = i + 1
    if s24_line and i > (s24_line - 1) and '</section>' in lines[i]:
        old_slides_end_line = i + 1
    if i > 4300 and '<script' in lines[i]:
        script_line = i + 1
        break

print(f"\ns24 starts at line: {s24_line}")
print(f"Old slides last </section> at line: {old_slides_end_line}")
print(f"First <script> after slides at line: {script_line}")

if old_slides_end_line and script_line:
    print("\n--- Between old slides end and script ---")
    for i in range(old_slides_end_line - 2, min(script_line + 5, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()[:100]}")
