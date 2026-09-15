with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Lines around 2935-2955:")
for i in range(2935, 2955):
    print(f"{i+1}: {repr(lines[i])[:100]}")

print("\nLines around 4330-4345:")
for i in range(4330, 4345):
    print(f"{i+1}: {repr(lines[i])[:100]}")
