import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Check metadata.xml
try:
    with open('metadata.xml', 'r', encoding='utf-8', errors='ignore') as f:
        print("--- metadata.xml ---")
        print(f.read()[:1500])
except Exception as e:
    print("metadata.xml error:", e)

# Check full_project_doc.txt
try:
    with open('full_project_doc.txt', 'r', encoding='utf-8', errors='ignore') as f:
        print("\n--- full_project_doc.txt first 60 lines ---")
        lines = f.readlines()[:80]
        for l in lines:
            if any(k in l.lower() for k in ['prepared', 'student', 'by', 'yahawy', 'al-', 'al_', 'dr.', 'saeed', 'باحث', 'إعداد', 'طلاب']):
                print(">>", l.strip())
            elif len(l.strip()) > 0 and len(l.strip()) < 80:
                print("  ", l.strip())
except Exception as e:
    print("full_project_doc error:", e)

# Check git log or previous commits for slide 0 team
try:
    with open('scratch/slide_s0.html', 'r', encoding='utf-8', errors='ignore') as f:
        print("\n--- scratch/slide_s0.html ---")
        print(f.read()[:2000])
except Exception as e:
    print("slide_s0 error:", e)
