import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Global Typography Enhancements
print("Applying global typography scale improvements...")

# Increase max-width of content-box for better presence
content = content.replace(
    ".content-box {\n  width: 100%;\n  max-width: 1160px;",
    ".content-box {\n  width: 100%;\n  max-width: 1280px;"
)

# Increase card text and heading sizes
content = content.replace(
    ".card p, .card ul {\n  font-size: 0.8rem;\n  color: var(--t2);\n  line-height: 1.6;\n}",
    ".card p, .card ul {\n  font-size: 0.94rem;\n  color: var(--t2);\n  line-height: 1.62;\n}"
)

content = content.replace(
    ".card-h {\n  display: flex;\n  align-items: center;\n  gap: 10px;\n  font-size: 0.96rem;",
    ".card-h {\n  display: flex;\n  align-items: center;\n  gap: 10px;\n  font-size: 1.12rem;"
)

content = content.replace(
    "table.ctbl {\n  width: 100%;\n  border-collapse: collapse;\n  font-size: 0.8rem;",
    "table.ctbl {\n  width: 100%;\n  border-collapse: collapse;\n  font-size: 0.92rem;"
)

content = content.replace(
    "table.ctbl th {\n  padding: 10px 14px;\n  font-size: 0.72rem;",
    "table.ctbl th {\n  padding: 12px 14px;\n  font-size: 0.86rem;"
)

content = content.replace(
    "table.ctbl td {\n  padding: 8px 14px;",
    "table.ctbl td {\n  padding: 10px 14px;"
)

content = content.replace(
    ".pill {\n  padding: 4px 12px;\n  border-radius: 100px;\n  font-size: 0.72rem;",
    ".pill {\n  padding: 5px 14px;\n  border-radius: 100px;\n  font-size: 0.82rem; white-space: nowrap;"
)

content = content.replace(
    ".snum {\n  font-size: 1.9rem;\n  font-weight: 800;",
    ".snum {\n  font-size: 2.35rem;\n  font-weight: 900;"
)

content = content.replace(
    ".slbl {\n  font-size: 0.68rem;\n  color: var(--t3);",
    ".slbl {\n  font-size: 0.82rem;\n  color: var(--t3);"
)

content = content.replace(
    ".hl p {\n  font-size: 0.84rem;",
    ".hl p {\n  font-size: 0.95rem;"
)

# 2. Replace Slide 19 markup with the visual rich layout
old_s18_match = re.search(r'<section\b[^>]*id=["\']s18["\'][^>]*>.*?</section>', content, re.DOTALL)
if not old_s18_match:
    print("Error: Could not locate s18 section in content!")
    sys.exit(1)

new_s18_html = """<section class="slide" id="s18">
  <div class="orb o2" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1260px">
    <div class="tag a1" style="border-color:rgba(255,180,0,0.4);background:rgba(255,180,0,0.08);margin-bottom:10px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#ffd166" stroke-width="2.2"><path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      <span class="en" style="color:#ffd166;font-weight:800;letter-spacing:1px">OPERATIONAL RISK CONTROLS &amp; SAFEGUARDS</span>
      <span class="ar" style="display:none;color:#ffd166;font-weight:800">ضوابط المخاطر التشغيلية وإجراءات الحماية</span>
    </div>
    <h2 class="st en" style="margin-bottom:4px">Challenges, Risks &amp; Technical Mitigations</h2>
    <h2 class="st ar" style="display:none;margin-bottom:4px">التحديات والمخاطر والإجراءات التقنية الوقائية</h2>
    <div class="gl" style="margin:4px auto 14px"></div>
    <p class="lead en" style="margin-bottom:18px;font-size:0.98rem;max-width:920px">
      Key operational risks identified across SOC deployments and the engineering safeguards implemented to guarantee precision, model resilience, and zero business disruption.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:18px;font-size:0.98rem;max-width:920px">
      أهم التحديات والمخاطر التشغيلية في مراكز العمليات والحلول الهندسية المعتمدة لضمان دقة النماذج واستقرارها وحماية استمرارية الأعمال.
    </p>

    <!-- 3 Visual Risk & Mitigation Cards with Interactive Architecture Diagrams -->
    <div class="g3" style="gap:16px;width:100%">
      
      <!-- Card 1: Data Heterogeneity & Schema Drift -->
      <div class="card" style="padding:20px;border:1px solid rgba(255,180,0,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(38,14,28,0.8));display:flex;flex-direction:column;justify-content:space-between">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:38px;height:38px;border-radius:10px;background:rgba(255,180,0,0.15);border:1px solid rgba(255,180,0,0.45);display:flex;align-items:center;justify-content:center;color:#ffd166;flex-shrink:0">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
              </div>
              <div>
                <h3 class="en" style="font-size:1.06rem;font-weight:800;color:#fff;margin:0">Data Heterogeneity</h3>
                <h3 class="ar" style="display:none;font-size:1.06rem;font-weight:800;color:#fff;margin:0">تعدد الصيغ وتباين البيانات</h3>
                <div style="font-size:0.72rem;color:var(--t3);font-family:'JetBrains Mono',monospace">CHALLENGE #1 &middot; INGESTION</div>
              </div>
            </div>
            <span style="padding:4px 10px;border-radius:6px;background:rgba(255,180,0,0.2);border:1px solid rgba(255,180,0,0.5);color:#ffd166;font-size:0.75rem;font-weight:700;white-space:nowrap">Moderate Risk</span>
          </div>

          <!-- Risk Box -->
          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06);margin-bottom:12px">
            <div style="font-size:0.78rem;font-weight:700;color:#ffd166;margin-bottom:3px;display:flex;align-items:center;gap:6px">
              <span>⚠️</span>
              <span class="en">Operational Threat:</span>
              <span class="ar" style="display:none">المخاطرة التشغيلية والأثر:</span>
            </div>
            <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.45;margin:0">
              Multi-vendor logs (Syslog, CEF, Windows Events) arrive with missing fields and divergent syntax, risking parser crashes and ML feature corruption.
            </p>
            <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.45;margin:0">
              تباين صيغ السجلات من أجهزة متعددة ونقص بعض الحقول يهدد بانهيار برامج التحليل وتشويه الخصائص المغذية لنماذج الذكاء الاصطناعي.
            </p>
          </div>

          <!-- Visual Flow Diagram -->
          <div style="background:rgba(0,212,255,0.04);border:1px solid rgba(0,212,255,0.25);border-radius:8px;padding:10px 8px;margin-bottom:12px">
            <div style="font-size:0.72rem;font-weight:800;color:var(--s);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;text-align:center">
              <span class="en">Engineering Pipeline Safeguard</span>
              <span class="ar" style="display:none">معمارية المعالجة الوقائية المعتمدة</span>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;gap:4px;font-size:0.73rem">
              <div style="flex:1;background:rgba(255,255,255,0.05);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid rgba(255,255,255,0.1)">
                <div style="font-weight:700;color:#fff">Raw Logs</div>
                <div style="font-size:0.65rem;color:var(--t3)">Multi-Vendor</div>
              </div>
              <div style="color:var(--s);font-weight:900">&rarr;</div>
              <div style="flex:1.2;background:rgba(0,212,255,0.15);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid var(--s)">
                <div style="font-weight:700;color:#fff">Normalizer</div>
                <div style="font-size:0.65rem;color:var(--s)">Pydantic / ECS</div>
              </div>
              <div style="color:var(--s);font-weight:900">&rarr;</div>
              <div style="flex:1;background:rgba(16,185,129,0.15);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid var(--ok)">
                <div style="font-weight:700;color:#fff">Unified</div>
                <div style="font-size:0.65rem;color:var(--ok)">100% Validated</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Safeguard Status Footer -->
        <div style="display:flex;align-items:center;justify-content:space-between;padding-top:8px;border-top:1px solid rgba(255,255,255,0.08)">
          <span style="font-size:0.78rem;color:var(--t3)" class="en">Implemented Defense:</span>
          <span style="font-size:0.78rem;color:var(--t3);display:none" class="ar">إجراء الحماية المنفذ:</span>
          <span style="display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:100px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:var(--ok);font-size:0.76rem;font-weight:700">
            ✓ <span class="en">Layer 1 Pipeline</span><span class="ar" style="display:none">طبقة الاستيعاب 1</span>
          </span>
        </div>
      </div>

      <!-- Card 2: Operational Disruption Risk -->
      <div class="card" style="padding:20px;border:1px solid rgba(239,68,68,0.4);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(45,12,20,0.8));display:flex;flex-direction:column;justify-content:space-between">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:38px;height:38px;border-radius:10px;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.45);display:flex;align-items:center;justify-content:center;color:#ff6b6b;flex-shrink:0">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <div>
                <h3 class="en" style="font-size:1.06rem;font-weight:800;color:#fff;margin:0">Operational Disruption</h3>
                <h3 class="ar" style="display:none;font-size:1.06rem;font-weight:800;color:#fff;margin:0">مخاطر انقطاع الأعمال</h3>
                <div style="font-size:0.72rem;color:var(--t3);font-family:'JetBrains Mono',monospace">CHALLENGE #2 &middot; CONTAINMENT</div>
              </div>
            </div>
            <span style="padding:4px 10px;border-radius:6px;background:rgba(239,68,68,0.22);border:1px solid rgba(239,68,68,0.55);color:#ff6b6b;font-size:0.75rem;font-weight:700;white-space:nowrap">Critical Risk</span>
          </div>

          <!-- Risk Box -->
          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06);margin-bottom:12px">
            <div style="font-size:0.78rem;font-weight:700;color:#ff6b6b;margin-bottom:3px;display:flex;align-items:center;gap:6px">
              <span>🚫</span>
              <span class="en">Operational Threat:</span>
              <span class="ar" style="display:none">المخاطرة التشغيلية والأثر:</span>
            </div>
            <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.45;margin:0">
              Unrestricted autonomous containment (isolating servers, revoking credentials) triggered by false positives can take down critical business systems.
            </p>
            <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.45;margin:0">
              الأتمتة الكاملة دون رقابة قد تعزل خوادم إنتاجية حساسة أو توقف حسابات حيوية نتيجة إنذار خاطئ، مسببة خسائر فادحة للشركة.
            </p>
          </div>

          <!-- Visual Flow Diagram -->
          <div style="background:rgba(239,68,68,0.04);border:1px solid rgba(239,68,68,0.25);border-radius:8px;padding:10px 8px;margin-bottom:12px">
            <div style="font-size:0.72rem;font-weight:800;color:#ff8585;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;text-align:center">
              <span class="en">Controlled Autonomy Decision Gate</span>
              <span class="ar" style="display:none">بوابات القرار المنضبط للأتمتة</span>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;gap:4px;font-size:0.73rem">
              <div style="flex:1;background:rgba(255,255,255,0.05);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid rgba(255,255,255,0.1)">
                <div style="font-weight:700;color:#fff">Critical Alert</div>
                <div style="font-size:0.65rem;color:var(--t3)">Asset C &ge; 4</div>
              </div>
              <div style="color:#ff6b6b;font-weight:900">&rarr;</div>
              <div style="flex:1.2;background:rgba(255,180,0,0.18);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid #ffd166">
                <div style="font-weight:700;color:#fff">🛡️ Human Gate</div>
                <div style="font-size:0.65rem;color:#ffd166">1-Click Approve</div>
              </div>
              <div style="color:var(--ok);font-weight:900">&rarr;</div>
              <div style="flex:1;background:rgba(16,185,129,0.15);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid var(--ok)">
                <div style="font-weight:700;color:#fff">Safe Action</div>
                <div style="font-size:0.65rem;color:var(--ok)">Instant Rollback</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Safeguard Status Footer -->
        <div style="display:flex;align-items:center;justify-content:space-between;padding-top:8px;border-top:1px solid rgba(255,255,255,0.08)">
          <span style="font-size:0.78rem;color:var(--t3)" class="en">Implemented Defense:</span>
          <span style="font-size:0.78rem;color:var(--t3);display:none" class="ar">إجراء الحماية المنفذ:</span>
          <span style="display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:100px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:var(--ok);font-size:0.76rem;font-weight:700">
            ✓ <span class="en">Policy Gate &sect;3.7</span><span class="ar" style="display:none">بوابة السياسة 3.7§</span>
          </span>
        </div>
      </div>

      <!-- Card 3: Concept Drift & Model Degradation -->
      <div class="card" style="padding:20px;border:1px solid rgba(168,85,247,0.4);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(30,15,45,0.8));display:flex;flex-direction:column;justify-content:space-between">
        <div>
          <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px">
            <div style="display:flex;align-items:center;gap:10px">
              <div style="width:38px;height:38px;border-radius:10px;background:rgba(168,85,247,0.15);border:1px solid rgba(168,85,247,0.45);display:flex;align-items:center;justify-content:center;color:#c084fc;flex-shrink:0">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
              </div>
              <div>
                <h3 class="en" style="font-size:1.06rem;font-weight:800;color:#fff;margin:0">Concept Drift</h3>
                <h3 class="ar" style="display:none;font-size:1.06rem;font-weight:800;color:#fff;margin:0">انجراف النماذج وتغير الهجمات</h3>
                <div style="font-size:0.72rem;color:var(--t3);font-family:'JetBrains Mono',monospace">CHALLENGE #3 &middot; ML ADAPTATION</div>
              </div>
            </div>
            <span style="padding:4px 10px;border-radius:6px;background:rgba(168,85,247,0.22);border:1px solid rgba(168,85,247,0.5);color:#c084fc;font-size:0.75rem;font-weight:700;white-space:nowrap">High Risk</span>
          </div>

          <!-- Risk Box -->
          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06);margin-bottom:12px">
            <div style="font-size:0.78rem;font-weight:700;color:#c084fc;margin-bottom:3px;display:flex;align-items:center;gap:6px">
              <span>🔄</span>
              <span class="en">Operational Threat:</span>
              <span class="ar" style="display:none">المخاطرة التشغيلية والأثر:</span>
            </div>
            <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.45;margin:0">
              Adversaries constantly alter evasion techniques and payload signatures; static machine learning models degrade in classification accuracy over time.
            </p>
            <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.45;margin:0">
              تطور أساليب المهاجمين وتغيير بصمات الهجوم يؤدي بمرور الوقت إلى تقادم نماذج التعلم الآلي وتراجع قدرتها على اكتشاف التهديدات المستحدثة.
            </p>
          </div>

          <!-- Visual Flow Diagram -->
          <div style="background:rgba(168,85,247,0.04);border:1px solid rgba(168,85,247,0.25);border-radius:8px;padding:10px 8px;margin-bottom:12px">
            <div style="font-size:0.72rem;font-weight:800;color:#d8b4fe;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;text-align:center">
              <span class="en">Continuous Active Retraining Loop</span>
              <span class="ar" style="display:none">حلقة التغذية الراجعة التكيفية المستمرة</span>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;gap:4px;font-size:0.73rem">
              <div style="flex:1;background:rgba(255,255,255,0.05);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid rgba(255,255,255,0.1)">
                <div style="font-weight:700;color:#fff">Analyst Verdict</div>
                <div style="font-size:0.65rem;color:var(--t3)">Corrections</div>
              </div>
              <div style="color:#c084fc;font-weight:900">&rarr;</div>
              <div style="flex:1.2;background:rgba(168,85,247,0.18);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid #c084fc">
                <div style="font-weight:700;color:#fff">Feedback Loop</div>
                <div style="font-size:0.65rem;color:#c084fc">Active Retrain</div>
              </div>
              <div style="color:var(--ok);font-weight:900">&rarr;</div>
              <div style="flex:1;background:rgba(16,185,129,0.15);border-radius:6px;padding:6px 2px;text-align:center;border:1px solid var(--ok)">
                <div style="font-weight:700;color:#fff">Adapted ML</div>
                <div style="font-size:0.65rem;color:var(--ok)">Zero Drift</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Safeguard Status Footer -->
        <div style="display:flex;align-items:center;justify-content:space-between;padding-top:8px;border-top:1px solid rgba(255,255,255,0.08)">
          <span style="font-size:0.78rem;color:var(--t3)" class="en">Implemented Defense:</span>
          <span style="font-size:0.78rem;color:var(--t3);display:none" class="ar">إجراء الحماية المنفذ:</span>
          <span style="display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:100px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);color:var(--ok);font-size:0.76rem;font-weight:700">
            ✓ <span class="en">Feedback Loop &sect;3.8</span><span class="ar" style="display:none">حلقة التعلم 3.8§</span>
          </span>
        </div>
      </div>

    </div>
  </div>
  <div class="sn">19 / 20</div>
</section>"""

# Replace old s18 with new s18
content = content[:old_s18_match.start()] + new_s18_html + content[old_s18_match.end():]
print("Replaced Slide 19 markup successfully.")

# Write back to index.html
with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated presentation/index.html successfully!")
