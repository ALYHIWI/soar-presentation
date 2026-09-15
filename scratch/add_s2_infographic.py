import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate section s2
s2_pattern = re.compile(r'(<section\b[^>]*id=["\']s2["\'][^>]*>.*?</section>)', re.DOTALL)
m = s2_pattern.search(content)
if not m:
    print("Error: section s2 not found!")
    sys.exit(1)

old_s2 = m.group(1)

# Check if the visual infographic is already present
if 'Alert Triage Bottleneck &amp; Fatigue Flow' in old_s2:
    print("Infographic already present in s2.")
    sys.exit(0)

# The infographic markup to append right after the 22.9% card and before </section>
infographic_markup = """
    <!-- Custom Visual Infographic: Alert Triage Bottleneck & Fatigue Flow -->
    <div class="card" style="margin-top:12px;padding:12px 18px;border:1px solid rgba(0,212,255,0.24);background:linear-gradient(145deg, rgba(20,8,25,0.85), rgba(10,22,35,0.78));display:flex;flex-direction:column;gap:8px">
      <div style="display:flex;justify-content:space-between;align-items:center">
        <div style="font-size:0.75rem;font-weight:800;letter-spacing:1.2px;color:var(--s);text-transform:uppercase;display:flex;align-items:center;gap:6px">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
          <span class="en">Alert Triage Bottleneck &amp; Fatigue Flow</span>
          <span class="ar" style="display:none">مسار عنق زجاجة الفرز وإرهاق التنبيهات</span>
        </div>
        <div style="font-size:0.68rem;color:var(--t3);font-family:'JetBrains Mono',monospace">OPERATIONAL BOTTLENECK PIPELINE</div>
      </div>

      <!-- 5-Stage Data-Flow Pipeline -->
      <div style="display:flex;align-items:center;justify-content:space-between;gap:6px;width:100%;padding:2px 0">
        
        <!-- Stage 1: Alerts -->
        <div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:8px 6px;display:flex;flex-direction:column;align-items:center;text-align:center">
          <div style="width:28px;height:28px;border-radius:6px;background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.3);display:flex;align-items:center;justify-content:center;color:var(--s);margin-bottom:4px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <div style="font-size:0.82rem;font-weight:800;color:#fff"><span class="en">Alerts</span><span class="ar" style="display:none">التنبيهات</span></div>
          <div style="font-size:0.68rem;color:var(--t3);margin-top:1px"><span class="en">Massive Volume</span><span class="ar" style="display:none">طوفان السجلات</span></div>
        </div>

        <!-- Connector 1 -->
        <div style="color:var(--s);font-weight:900;font-size:0.85rem;display:flex;align-items:center">&rarr;</div>

        <!-- Stage 2: Noise -->
        <div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,180,0,0.25);border-radius:8px;padding:8px 6px;display:flex;flex-direction:column;align-items:center;text-align:center">
          <div style="width:28px;height:28px;border-radius:6px;background:rgba(255,180,0,0.15);border:1px solid rgba(255,180,0,0.4);display:flex;align-items:center;justify-content:center;color:#ffd166;margin-bottom:4px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          </div>
          <div style="font-size:0.82rem;font-weight:800;color:#fff"><span class="en">Noise</span><span class="ar" style="display:none">الضجيج</span></div>
          <div style="font-size:0.68rem;color:#ffd166;margin-top:1px"><span class="en">False Positives</span><span class="ar" style="display:none">إنذارات كاذبة</span></div>
        </div>

        <!-- Connector 2 -->
        <div style="color:var(--s);font-weight:900;font-size:0.85rem;display:flex;align-items:center">&rarr;</div>

        <!-- Stage 3: Context Switching -->
        <div style="flex:1.15;background:rgba(255,255,255,0.04);border:1px solid rgba(255,77,109,0.25);border-radius:8px;padding:8px 6px;display:flex;flex-direction:column;align-items:center;text-align:center">
          <div style="width:28px;height:28px;border-radius:6px;background:rgba(255,77,109,0.15);border:1px solid rgba(255,77,109,0.4);display:flex;align-items:center;justify-content:center;color:var(--acc);margin-bottom:4px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
          </div>
          <div style="font-size:0.82rem;font-weight:800;color:#fff"><span class="en">Context Switching</span><span class="ar" style="display:none">تبديل السياق</span></div>
          <div style="font-size:0.68rem;color:var(--acc);margin-top:1px"><span class="en">Analyst Overload</span><span class="ar" style="display:none">إجهاد المحلل</span></div>
        </div>

        <!-- Connector 3 -->
        <div style="color:var(--s);font-weight:900;font-size:0.85rem;display:flex;align-items:center">&rarr;</div>

        <!-- Stage 4: Static Rules -->
        <div style="flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(0,212,255,0.25);border-radius:8px;padding:8px 6px;display:flex;flex-direction:column;align-items:center;text-align:center">
          <div style="width:28px;height:28px;border-radius:6px;background:rgba(0,212,255,0.15);border:1px solid rgba(0,212,255,0.4);display:flex;align-items:center;justify-content:center;color:var(--s);margin-bottom:4px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/><path d="m14 9 3 3-3 3"/></svg>
          </div>
          <div style="font-size:0.82rem;font-weight:800;color:#fff"><span class="en">Static Rules</span><span class="ar" style="display:none">قواعد ثابتة</span></div>
          <div style="font-size:0.68rem;color:var(--s);margin-top:1px"><span class="en">FIFO Queuing</span><span class="ar" style="display:none">طوابير غير مرتبة</span></div>
        </div>

        <!-- Connector 4 -->
        <div style="color:#ef4444;font-weight:900;font-size:0.85rem;display:flex;align-items:center">&rarr;</div>

        <!-- Stage 5: Critical Incidents -->
        <div style="flex:1.15;background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.45);border-radius:8px;padding:8px 6px;display:flex;flex-direction:column;align-items:center;text-align:center;box-shadow:0 0 14px rgba(239,68,68,0.2)">
          <div style="width:28px;height:28px;border-radius:6px;background:rgba(239,68,68,0.25);border:1px solid rgba(239,68,68,0.6);display:flex;align-items:center;justify-content:center;color:#ff6b6b;margin-bottom:4px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          </div>
          <div style="font-size:0.82rem;font-weight:800;color:#fff"><span class="en">Critical Incidents</span><span class="ar" style="display:none">الحوادث الحرجة</span></div>
          <div style="font-size:0.68rem;color:#ff6b6b;font-weight:700;margin-top:1px"><span class="en">Buried in Noise</span><span class="ar" style="display:none">مدفونة بالضجيج</span></div>
        </div>

      </div>
    </div>
"""

# Insert right after the 22.9% card (which ends with </div>\n </div>\n </div> before <div class="sn">03 / 20</div>)
# Let's find the closing of the 22.9% card
target_marker = '</div>\n </div>\n <div class="sn">03 / 20</div>'
if target_marker in old_s2:
    new_s2 = old_s2.replace(target_marker, '</div>\n' + infographic_markup + '  </div>\n <div class="sn">03 / 20</div>')
else:
    # Alternative match
    alt_marker = '<div class="sn">03 / 20</div>'
    idx = old_s2.rfind(alt_marker)
    # find the </div> right before it that closes content-box
    div_idx = old_s2.rfind('</div>', 0, idx)
    new_s2 = old_s2[:div_idx] + infographic_markup + old_s2[div_idx:]

content = content.replace(old_s2, new_s2)

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added custom cybersecurity infographic to Slide 3 (s2) with 100% preservation of all existing content!")
