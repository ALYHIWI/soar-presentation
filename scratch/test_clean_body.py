import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's write regex patterns to clean slide bodies without touching .slide-ref-footer or <script>

# Split HTML into slides and footer/script
slides_pattern = r'(<section\s+class="slide[^"]*"\s+id="([^"]+)"[^>]*>)(.*?)(<div class="slide-ref-footer".*?</section>)'

def clean_body_text(body, sid):
    cleaned = body
    
    # Remove (.sref divs) in stats
    cleaned = re.sub(r'<div class="sref[^"]*"[^>]*>.*?</div>\s*', '', cleaned)
    
    # Remove section numbers from tags: e.g. (§1.1-1.2) or (§3.7) or (§3.2, §3.7, §2.4)
    cleaned = re.sub(r'\s*\([§\d\.\s,\-–&;]+\)', '', cleaned)
    
    # Remove specific patterns in headings and paragraphs:
    # e.g. "Key Empirical Finding (§1.2):" -> "Key Empirical Finding:"
    # e.g. "النتيجة التجريبية المحورية (§1.2):" -> "النتيجة التجريبية المحورية:"
    cleaned = re.sub(r'\(§1\.\d+(?:[–\-]\d+\.\d+)?\)', '', cleaned)
    cleaned = re.sub(r'\(§2\.\d+(?:\.\d+)?\)', '', cleaned)
    cleaned = re.sub(r'\(§3\.\d+(?:\.\d+)?\)', '', cleaned)
    cleaned = re.sub(r'\(§9\)', '', cleaned)
    
    # Remove researcher parentheticals from body text except Table 2-1 table cells
    if sid != 's10':
        cleaned = re.sub(r'\s*\([A-Za-z\s&;,]+(?:et al\.)?,?\s*\d{4}[^)]*\)', '', cleaned)
        cleaned = re.sub(r'\s*\(معيار جيلمان[^)]*\)', '', cleaned)
        cleaned = re.sub(r'\s*\(Gelman baseline[^)]*\)', '', cleaned)
        cleaned = re.sub(r'Informed by Agrawal et al\. \(\d{4}\):\s*', '', cleaned)
        cleaned = re.sub(r'بناءً على Agrawal et al\. \(\d{4}\):\s*', '', cleaned)
    
    # Clean up double spaces or dangling punctuation
    cleaned = re.sub(r'\s{2,}', ' ', cleaned)
    cleaned = re.sub(r'\s+\.', '.', cleaned)
    cleaned = re.sub(r'\s+:', ':', cleaned)
    
    return cleaned

matches = list(re.finditer(slides_pattern, html, re.DOTALL))
print(f"Found {len(matches)} slides to test cleaning.")

for m in matches:
    sid = m.group(2)
    orig_body = m.group(3)
    new_body = clean_body_text(orig_body, sid)
    
    # Check if any inline § or et al. remains in new_body
    rem_citations = re.findall(r'(\([^\)]*§[^\)]*\)|§\s*\d+(?:\.\d+)*|\([^\)]*20\d\d[^\)]*\)|et al\.)', new_body)
    if sid != 's10' and rem_citations:
        print(f"Slide {sid} still has remaining citations: {rem_citations}")

print("Clean test complete.")
