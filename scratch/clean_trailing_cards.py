import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Line 2127: {lines[2126].strip()}")
print(f"Line 2128: {lines[2127].strip()}")
print(f"Line 2145: {lines[2144].strip()}")
print(f"Line 2146: {lines[2145].strip()}")
print(f"Line 2147: {lines[2146].strip()}")

# Keep lines up to 2127 (index 2127) and from 2147 (index 2146)
clean_lines = lines[:2127] + ['\n'] + lines[2146:]

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)

print("Cleaned duplicate cards outside team-title-grid successfully!")
