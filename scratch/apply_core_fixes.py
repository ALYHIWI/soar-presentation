import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Update presentation/index.html
with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix supervisor text in Slide 1
old_sup_ar = """      <p class="ar" style="display:none;font-size:0.84rem;margin:0">
        <strong>إشراف الدكتور:</strong> رائد سعيد &nbsp;|&nbsp;
        <strong>التخصص:</strong> بكالوريوس الأمن السيبراني والشبكات &nbsp;|&nbsp;
        <strong>القسم:</strong> علوم الحاسوب
      </p>"""

new_sup_ar = """      <p class="ar" style="display:none;font-size:0.84rem;margin:0">
        <strong>المشرف العلمي:</strong> د. رائد سعيد &nbsp;|&nbsp;
        <strong>التخصص:</strong> الأمن السيبراني والشبكات &nbsp;|&nbsp;
        <strong>القسم:</strong> علوم الحاسوب
      </p>"""

if old_sup_ar in html:
    html = html.replace(old_sup_ar, new_sup_ar)
    print("✓ Fixed Slide 1 supervisor Arabic text")
else:
    print("! Note: supervisor text already updated or differing whitespace")
    # regex fallback
    html = re.sub(
        r'<p class="ar"[^>]*>\s*<strong>(?:إشراف الدكتور:|المشرف العلمي:).*?علوم الحاسوب\s*</p>',
        new_sup_ar.strip(),
        html,
        flags=re.DOTALL
    )

# Fix script top: add immediate localStorage purge
script_tag = "<script>"
immediate_purge = """<script>
// Aggressive cache purge to guarantee immediate sync with active files
try {
  localStorage.removeItem('soar_custom_deck');
  localStorage.removeItem('soar_slides_custom');
} catch(e) {}
"""
if script_tag in html and immediate_purge not in html:
    html = html.replace(script_tag, immediate_purge, 1)
    print("✓ Added immediate localStorage purge at top of <script>")

# Remove saveDeckState() from renumberSlides()
html = re.sub(r'(\s+)saveDeckState\(\);(\s+document\.getElementById\(\'bn\'\)|}\s*\n\s*function saveDeckState)', r'\1// saveDeckState(); removed to prevent stale caching\2', html)
print("✓ Disabled automatic saveDeckState() in slide flow")

# Remove savedDeck restoration in DOMContentLoaded
old_dom_deck = """  const savedDeck = localStorage.getItem('soar_custom_deck');
  if (savedDeck && savedDeck.trim().length > 1000) {
    document.getElementById('wrap').innerHTML = savedDeck;
  }"""

new_dom_deck = """  // Ensure fresh presentation load without stale localStorage deck overwrite
  try {
    localStorage.removeItem('soar_custom_deck');
    localStorage.removeItem('soar_slides_custom');
  } catch(e) {}"""

if old_dom_deck in html:
    html = html.replace(old_dom_deck, new_dom_deck)
    print("✓ Removed stale savedDeck overwrite in DOMContentLoaded")
else:
    print("! savedDeck block not found verbatim, checking regex...")
    html = re.sub(
        r'const savedDeck = localStorage\.getItem\([\'"]soar_custom_deck[\'"]\);.*?document\.getElementById\([\'"]wrap[\'"]\)\.innerHTML = savedDeck;\s*}',
        new_dom_deck,
        html,
        flags=re.DOTALL
    )

# Add toggleRefModal implementation if missing
if "function toggleRefModal" not in html:
    toggle_ref_func = """
function toggleRefModal() {
  const drawer = document.getElementById('refDrawer');
  if (!drawer) return;
  const isOpen = drawer.classList.toggle('open');
  if (isOpen && typeof updateSlideReferences === 'function') {
    updateSlideReferences(c);
  }
}
"""
    # Insert right before updateSlideReferences
    idx_ref = html.find("function updateSlideReferences")
    if idx_ref != -1:
        html = html[:idx_ref] + toggle_ref_func + "\n" + html[idx_ref:]
        print("✓ Added toggleRefModal() function definition")

# Update keydown to include 'r', 'R', and 'Escape'
old_keydown = """    case 'c':
    case 'C': tC(); break;
    case 'e':
    case 'E': toggleEditMode(); break;
  }"""

new_keydown = """    case 'c':
    case 'C': tC(); break;
    case 'r':
    case 'R': toggleRefModal(); break;
    case 'Escape': {
      const drawer = document.getElementById('refDrawer');
      if (drawer && drawer.classList.contains('open')) {
        drawer.classList.remove('open');
      }
      const cp = document.getElementById('cp');
      if (cp && cp.classList.contains('open')) {
        cp.classList.remove('open');
      }
      break;
    }
    case 'e':
    case 'E': toggleEditMode(); break;
  }"""

if old_keydown in html:
    html = html.replace(old_keydown, new_keydown)
    print("✓ Added 'r', 'R' and 'Escape' to keydown listener")

# Update tL() to refresh references drawer
old_tl_tail = """  document.getElementById('ll').textContent = isAR ? 'English' : 'العربية';
  bL();
  bD();
}"""

new_tl_tail = """  document.getElementById('ll').textContent = isAR ? 'English' : 'العربية';
  bL();
  bD();
  if (typeof updateSlideReferences === 'function') {
    updateSlideReferences(c);
  }
}"""

if old_tl_tail in html:
    html = html.replace(old_tl_tail, new_tl_tail)
    print("✓ Updated tL() to refresh references upon language toggle")

# Write back presentation/index.html
with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✓ Saved presentation/index.html successfully")

# 2. Update dev-server.js
with open('dev-server.js', 'r', encoding='utf-8') as f:
    server_js = f.read()

old_server_url = """    let reqUrl = req.url.split('?')[0];
    if (reqUrl === '/' || reqUrl === '') {
      reqUrl = '/index.html';
    }"""

new_server_url = """    let reqUrl = req.url.split('?')[0];
    if (reqUrl.startsWith('/presentation/')) {
      reqUrl = reqUrl.replace('/presentation/', '/');
    }
    if (reqUrl === '/' || reqUrl === '') {
      reqUrl = '/index.html';
    }"""

if old_server_url in server_js:
    server_js = server_js.replace(old_server_url, new_server_url)
    with open('dev-server.js', 'w', encoding='utf-8') as f:
        f.write(server_js)
    print("✓ Updated dev-server.js to support /presentation/ alias gracefully")
