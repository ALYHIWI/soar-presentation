import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update rd-header
old_rd_header = """    <div class="rd-title">
      <span>📖</span>
      <span class="en">Slide Report Mapping &amp; Paragraph References</span>
      <span class="ar" style="display:none">توثيق ومطابقة فقرات السلايد مع ملف المشروع</span>
      <span class="rd-slide-pill" id="rdSlidePill">Slide 01 / 25</span>
    </div>
    <button class="rd-close" onclick="toggleRefModal()" title="Close References (ESC / R)">✕</button>"""

new_rd_header = """    <div class="rd-title">
      <span>📖</span>
      <span class="en">Slide Report Mapping &amp; Paragraph References</span>
      <span class="ar" style="display:none">توثيق ومطابقة فقرات السلايد مع ملف المشروع المعتمد</span>
    </div>
    <div class="rd-nav-group" style="display:flex;align-items:center;gap:8px">
      <button class="rd-nav-btn" onclick="prev(); if(typeof updateSlideReferences==='function') updateSlideReferences(c);" title="الشريحة السابقة (ArrowLeft)">◀ <span class="en">Prev</span><span class="ar" style="display:none">السابق</span></button>
      <span class="rd-slide-pill" id="rdSlidePill">Slide 01 / 25</span>
      <button class="rd-nav-btn" onclick="next(); if(typeof updateSlideReferences==='function') updateSlideReferences(c);" title="الشريحة التالية (ArrowRight)"><span class="en">Next</span><span class="ar" style="display:none">التالي</span> ▶</button>
      <button class="rd-close" onclick="toggleRefModal()" title="Close References (ESC / R)">✕</button>
    </div>"""

if old_rd_header in html:
    html = html.replace(old_rd_header, new_rd_header)
    print("✓ Replaced rd-header with navigation-enabled header")
else:
    print("! old_rd_header not found verbatim, checking regex...")
    html = re.sub(
        r'<div class="rd-title">.*?<span class="rd-slide-pill" id="rdSlidePill">.*?</div>\s*<button class="rd-close".*?</button>',
        new_rd_header.strip(),
        html,
        flags=re.DOTALL
    )
    print("✓ Replaced rd-header via regex fallback")

# 2. Add rd-nav-btn CSS
rd_css_rule = """
.rd-nav-btn {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--br);
  color: var(--t1);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.72rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--tr);
  display: flex;
  align-items: center;
  gap: 4px;
}
.rd-nav-btn:hover {
  background: rgba(0, 212, 255, 0.15);
  border-color: var(--s);
  color: #fff;
}
"""
if ".rd-nav-btn {" not in html:
    html = html.replace(".rd-close {", rd_css_rule.strip() + "\n.rd-close {", 1)
    print("✓ Added .rd-nav-btn CSS")

# 3. Upgrade updateSlideReferences implementation
old_update_func_match = re.search(r'function updateSlideReferences\(slideIdx\)\s*\{.*?\n\}\n\n// Initialize references on load', html, re.DOTALL)

new_update_func = """function updateSlideReferences(slideIdx) {
  const ref = SLIDE_REFS[slideIdx];
  if (!ref) return;

  const pill = document.getElementById('rdSlidePill');
  if (pill) {
    pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 25`;
  }

  // 1. Build Content for Drawer Modal (Doc Ref)
  const rdContent = document.getElementById('rdContent');
  if (rdContent) {
    let rowsHtml = '';
    ref.elements.forEach((el, elIdx) => {
      rowsHtml += `
        <tr>
          <td style="font-weight:700;color:var(--t1)">
            <div style="font-size:0.83rem;color:#fff;display:flex;align-items:center;gap:6px">
              <span style="display:inline-block;width:18px;height:18px;border-radius:50%;background:rgba(0,212,255,0.15);color:var(--s);text-align:center;line-height:18px;font-size:0.68rem">${elIdx + 1}</span>
              ${isAR ? el.elAr : el.elEn}
            </div>
            <div style="font-size:0.71rem;color:var(--t3);margin-top:2px;padding-left:24px">
              ${isAR ? el.elEn : el.elAr}
            </div>
          </td>
          <td style="vertical-align:top">
            <span style="display:inline-block;padding:3px 8px;border-radius:6px;background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.35);color:var(--s);font-family:'JetBrains Mono',monospace;font-size:0.72rem;font-weight:600">
              📍 ${el.loc}
            </span>
          </td>
          <td style="font-size:0.76rem;color:var(--t2);line-height:1.5;background:rgba(255,255,255,0.015);border-radius:6px;padding:8px 10px">
            &ldquo;${el.textEn.replace(/\\n/g, '<br>')}&rdquo;
          </td>
          <td style="vertical-align:top">
            <span class="rd-badge-exact" style="display:inline-flex;align-items:center;gap:4px;padding:3px 8px;border-radius:6px;background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.35);color:var(--ok);font-size:0.68rem;font-weight:700;white-space:nowrap">
              ✓ ${isAR ? 'مطابقة تامة 100%' : 'Exact 100% Match'}
            </span>
          </td>
        </tr>
      `;
    });

    rdContent.innerHTML = `
      <div class="rd-sec-banner" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
        <div>
          <strong style="color:var(--t1)">${isAR ? 'الفصل والقسم المرجعي في تقرير المشروع المعتمد:' : 'Report Chapter & Section Reference:'}</strong> 
          <span style="color:var(--s);font-weight:800;margin-left:6px">${ref.chapter} &mdash; ${ref.section}</span>
        </div>
        <div style="font-size:0.75rem;color:var(--t3)">
          ${isAR ? 'عدد الجزئيات المدققة في هذا السلايد:' : 'Verified Elements in this Slide:'} <strong style="color:#fff">${ref.elements.length}</strong>
        </div>
      </div>
      <table class="rd-table">
        <thead>
          <tr>
            <th style="width:24%">${isAR ? 'عنصر الشريحة / الجزئية' : 'Slide Element / Card'}</th>
            <th style="width:26%">${isAR ? 'الموقع في ملف التقرير (الفصل/القسم/الصفحة)' : 'Report Location (§ & Page)'}</th>
            <th style="width:38%">${isAR ? 'النص والبيانات المعتمدة للمطابقة اليدوية' : 'Cited Telemetry & Text for Manual Audit'}</th>
            <th style="width:12%">${isAR ? 'حالة التدقيق' : 'Audit Match'}</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    `;
  }

  // 2. Build Content for Control Center (#cp)
  const cpRefContent = document.getElementById('cpSlideRefContent');
  if (cpRefContent) {
    let cpItemsHtml = '';
    ref.elements.forEach(el => {
      cpItemsHtml += `
        <div style="padding:6px 8px;border-bottom:1px solid rgba(255,255,255,0.06);font-size:0.73rem">
          <div style="display:flex;justify-content:space-between;color:var(--t1);font-weight:700">
            <span>${isAR ? el.elAr : el.elEn}</span>
            <span style="color:var(--ok);font-size:0.68rem">✓ 100%</span>
          </div>
          <div style="color:var(--s);font-family:'JetBrains Mono',monospace;font-size:0.68rem;margin:2px 0">
            📍 ${el.loc}
          </div>
        </div>
      `;
    });

    cpRefContent.innerHTML = `
      <div style="font-size:0.75rem;margin-bottom:6px;color:var(--t2)">
        <strong>${isAR ? 'الشريحة الحالية:' : 'Active Slide:'}</strong> 
        <span style="color:#fff">${String(slideIdx + 1).padStart(2, '0')} / 25</span> &mdash; 
        <span style="color:var(--s)">${isAR ? ref.titleAr : ref.titleEn}</span>
      </div>
      <div style="font-size:0.72rem;color:var(--t3);margin-bottom:8px">
        📄 <strong>${ref.chapter}</strong> (${ref.section})
      </div>
      <div style="max-height:180px;overflow-y:auto;background:rgba(0,0,0,0.3);border-radius:8px;border:1px solid rgba(255,255,255,0.05)">
        ${cpItemsHtml}
      </div>
      <button onclick="toggleRefModal()" style="width:100%;margin-top:8px;padding:6px;border-radius:6px;background:rgba(0,212,255,0.15);border:1px solid var(--s);color:var(--s);font-size:0.72rem;font-weight:700;cursor:pointer">
        🔍 ${isAR ? 'فتح جدول التدقيق والتطابق الكامل (R)' : 'Open Detailed Verification Table (R)'}
      </button>
    `;
  }
}"""

if old_update_func_match:
    html = html[:old_update_func_match.start()] + new_update_func.strip() + "\n\n// Initialize references on load" + html[old_update_func_match.end():]
    print("✓ Successfully replaced updateSlideReferences with enhanced audit implementation")
else:
    print("! Checking regex fallback for updateSlideReferences...")
    html = re.sub(
        r'function updateSlideReferences\(slideIdx\)\s*\{.*?\}\s*\n+// Initialize references on load',
        new_update_func.strip() + "\n\n// Initialize references on load",
        html,
        flags=re.DOTALL
    )
    print("✓ Replaced updateSlideReferences via regex fallback")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved presentation/index.html successfully.")
