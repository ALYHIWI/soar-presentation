import io
import sys
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Starting complete taste overhaul. File size: {len(content)}")

# =========================================================================
# STEP 1: CLEAN ALL REMAINING EMOJIS IN STUDIO TOOLBAR & CONTROL PANEL
# =========================================================================

# Clean studio toolbar
content = content.replace('✏️ <span class="en">Slide Studio</span>', '<span class="en">Slide Studio</span>')
content = content.replace('➕ <span class="en">Add Card</span>', '<span class="en">+ Add Card</span>')
content = content.replace('🗑️ <span class="en">Remove Card</span>', '<span class="en">Remove Card</span>')
content = content.replace('💾 <span class="en">Save Changes</span>', '<span class="en">Save Changes</span>')
content = content.replace('✕ <span class="en">Done</span>', '<span class="en">Done</span>')

# Add slide modal
content = content.replace('<span>➕</span> <span class="en">Add Custom Slide', '<span class="en">+ Add Custom Slide')
content = content.replace('<div class="tpl-icon">🗂️</div>', '<div class="tpl-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M4 10h16M10 4v16"/></svg></div>')
content = content.replace('<div class="tpl-icon">📊</div>', '<div class="tpl-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></div>')
content = content.replace('<div class="tpl-icon">📈</div>', '<div class="tpl-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div>')
content = content.replace('<div class="tpl-icon">🔄</div>', '<div class="tpl-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg></div>')
content = content.replace('<span class="en">✨ Insert Slide</span>', '<span class="en">Insert Slide</span>')
content = content.replace('<span class="ar" style="display:none">✨ إدراج الشريحة في العرض</span>', '<span class="ar" style="display:none">إدراج الشريحة في العرض</span>')

# Control panel headers and buttons
content = content.replace('📖 <span class="en">Active Slide Source &amp; PDF Mapping</span>', '<span class="en">Active Slide Source &amp; PDF Mapping</span>')
content = content.replace('<div class="cpst">📑 <span class="en">Slide Studio & Lifecycle Controls', '<div class="cpst"><span class="en">Slide Studio & Lifecycle Controls')
content = content.replace('<span>➕</span> <span class="en">Add Slide</span>', '<span class="en">+ Add Slide</span>')
content = content.replace('<span>📋</span> <span class="en">Duplicate</span>', '<span class="en">Duplicate</span>')
content = content.replace('<span>🗑️</span> <span class="en">Delete Slide</span>', '<span class="en">Delete Slide</span>')
content = content.replace('<span>✏️</span> <span class="en">Edit Mode</span>', '<span class="en">Edit Mode</span>')
content = content.replace('💾 <span class="en">Save All Changes</span>', '<span class="en">Save All Changes</span>')
content = content.replace('🔄 <span class="en">Reset</span>', '<span class="en">Reset</span>')

# Animation styles in control panel
content = content.replace('<div class="cpst">🎬 <span class="en">Slide Animation Style', '<div class="cpst"><span class="en">Slide Animation Style')
content = content.replace('<span>💫</span> <span class="en">Cascade Wave</span>', '<span class="en">Cascade Wave</span>')
content = content.replace('<span>🧊</span> <span class="en">3D Flip Cube</span>', '<span class="en">3D Flip Cube</span>')
content = content.replace('<span>⚡</span> <span class="en">Cyber Zoom</span>', '<span class="en">Cyber Zoom</span>')
content = content.replace('<span>🌫️</span> <span class="en">Soft Dissolve</span>', '<span class="en">Soft Dissolve</span>')
content = content.replace('<span>🪜</span> <span class="en">Editorial Lift</span>', '<span class="en">Editorial Lift</span>')
content = content.replace('<span>🪟</span> <span class="en">Glass Flip X</span>', '<span class="en">Glass Flip X</span>')
content = content.replace('<span>🌀</span> <span class="en">Vortex Swirl</span>', '<span class="en">Vortex Swirl</span>')
content = content.replace('<span>🎯</span> <span class="en">Focus Snap</span>', '<span class="en">Focus Snap</span>')
content = content.replace('<div class="cpst">🎯 <span class="en">Element Focus & Hover Effects', '<div class="cpst"><span class="en">Element Focus & Hover Effects')

# Template strings in JS
content = content.replace('<div class="ci">⚡</div>', '<div class="ci"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>')
content = content.replace('<div class="ci">🛡️</div>', '<div class="ci"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>')
content = content.replace('<div class="ci">🧠</div>', '<div class="ci"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-2.04z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-2.04z"/></svg></div>')
content = content.replace('<div class="ci">✨</div>', '<div class="ci"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3L12 3z"/></svg></div>')
content = content.replace('<div class="fi">📡</div>', '<div class="fi"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9m14.2 0c3.9 3.9 3.9 10.3 0 14.2M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5m8.4 0c2.3 2.3 2.3 6.1 0 8.5M12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/></svg></div>')
content = content.replace('<div class="fi">🔍</div>', '<div class="fi"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>')
content = content.replace('<div class="fi">🧠</div>', '<div class="fi"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 4.44-2.04z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-4.44-2.04z"/></svg></div>')
content = content.replace('<div class="fi">⚙️</div>', '<div class="fi"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg></div>')
content = content.replace('<div class="farr">➔</div>', '<div class="farr">&rarr;</div>')

print("Cleaned all emojis in control panels and modals.")

# =========================================================================
# STEP 2: ENHANCE SLIDES WITH SVG CHARTS AND DIAGRAMS
# =========================================================================

# --- 2.1 SLIDE 04 (s3) MOTIVATION & SIGNIFICANCE: ADD 3 SVG METRIC GAUGES ---
# Replace s3 markup with visual gauge cards
old_s3 = re.search(r'<section\b[^>]*id=["\']s3["\'][^>]*>.*?</section>', content, re.DOTALL)
if old_s3:
    new_s3_html = """<section class="slide" id="s3">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(0,212,255,0.4);background:rgba(0,212,255,0.08);margin-bottom:10px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      <span class="en" style="color:var(--s);font-weight:800;letter-spacing:1px">EMPIRICAL BENCHMARKS &middot; CHAPTER 1 &sect;1.3 &amp; CHAPTER 2</span>
      <span class="ar" style="display:none;color:var(--s);font-weight:800">المؤشرات المعيارية المعتمدة &middot; الفصل 1 &sect;1.3 والفصل 2</span>
    </div>
    <h2 class="st en" style="margin-bottom:4px">Motivation &amp; Empirical SOC Significance</h2>
    <h2 class="st ar" style="display:none;margin-bottom:4px">الأهمية والدافع البحثي والمؤشرات المعيارية المعتمدة</h2>
    <div class="gl" style="margin:4px auto 14px"></div>
    <p class="lead en" style="margin-bottom:18px;font-size:0.98rem;max-width:940px">
      Real-world SOC studies quantify human analyst bottlenecks and prove how machine learning triage fundamentally protects analyst cognition.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:18px;font-size:0.98rem;max-width:940px">
      دراسات مراكز العمليات المعتمدة توثق بالأرقام عنق زجاجة الفحص البشري وتثبت كيف يضاعف الفرز الذكي قدرة المركز ويحمي كوادره.
    </p>

    <!-- 3 High-End Visual Metric Cards with SVG Donut / Completion Gauges -->
    <div class="g3" style="gap:16px;width:100%">
      
      <!-- Metric 1: 22.9% Handled Alerts Gauge -->
      <div class="card" style="padding:22px;border:1px solid rgba(239,68,68,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(42,12,20,0.8));display:flex;flex-direction:column;align-items:center;text-align:center">
        <div style="font-size:0.75rem;font-weight:800;color:#ff6b6b;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px">HUMAN TRIAGE GAP (GELMAN 2023)</div>
        
        <!-- SVG Donut Gauge (22.9% vs 77.1%) -->
        <div style="position:relative;width:140px;height:140px;margin-bottom:14px">
          <svg width="140" height="140" viewBox="0 0 100 100" style="transform:rotate(-90deg)">
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="rgba(255,255,255,0.08)" stroke-width="12"/>
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="rgba(239,68,68,0.4)" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="0"/>
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="var(--s)" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="193.6" stroke-linecap="round" style="filter:drop-shadow(0 0 6px var(--s))"/>
          </svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-size:2rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">22.9%</span>
            <span style="font-size:0.68rem;color:var(--t3);text-transform:uppercase">Inspected</span>
          </div>
        </div>

        <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">Critical Alerts Handled</h3>
        <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">التنبيهات الحرجة المفحوصة فعلياً</h3>
        
        <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          Under peak volume, human analysts only investigate <strong>22.9%</strong> of critical alerts, leaving <strong>77.1%</strong> uninspected due to alert fatigue.
        </p>
        <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          أثناء ذروة العمليات، يفحص المحللون <strong>22.9%</strong> فقط من التنبيهات، ويبقى <strong>77.1%</strong> دون فحص بسبب الإجهاد وتراكم السجلات.
        </p>
        <div style="margin-top:auto;padding-top:10px;font-size:0.72rem;color:var(--t3);font-family:'JetBrains Mono',monospace">SOURCE: REPORT &sect;1.2, PAGE 13</div>
      </div>

      <!-- Metric 2: 54% False Positive Suppression -->
      <div class="card" style="padding:22px;border:1px solid rgba(0,212,255,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8));display:flex;flex-direction:column;align-items:center;text-align:center">
        <div style="font-size:0.75rem;font-weight:800;color:var(--s);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px">NOISE REDUCTION BENCHMARK</div>
        
        <!-- SVG Comparison Bar Gauge -->
        <div style="position:relative;width:140px;height:140px;margin-bottom:14px;display:flex;flex-direction:column;justify-content:center;gap:12px;width:100%;max-width:180px">
          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.75rem;font-weight:700;margin-bottom:4px">
              <span style="color:var(--t3)">Legacy Noise</span>
              <span style="color:#ff6b6b">100% Volume</span>
            </div>
            <div style="height:10px;border-radius:6px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:100%;height:100%;background:linear-gradient(90deg, #c31432, #ff6b6b);border-radius:6px"></div>
            </div>
          </div>
          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.75rem;font-weight:700;margin-bottom:4px">
              <span style="color:var(--s)">AI-Filtered</span>
              <span style="color:var(--ok)">-54% Suppressed</span>
            </div>
            <div style="height:10px;border-radius:6px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:46%;height:100%;background:linear-gradient(90deg, var(--s), var(--ok));border-radius:6px;box-shadow:0 0 8px var(--ok)"></div>
            </div>
          </div>
          <div style="font-size:1.85rem;font-weight:900;color:var(--s);font-family:'JetBrains Mono',monospace;margin-top:2px">
            54% <span style="font-size:0.9rem;color:var(--ok);font-weight:700">Suppressed</span>
          </div>
        </div>

        <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">False Positive Reduction</h3>
        <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">قمع الإيجابيات الكاذبة</h3>
        
        <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          Machine learning triage autonomously suppresses <strong>54%</strong> of benign noise, slashing analyst queue dwell time and eliminating alert fatigue.
        </p>
        <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          الفرز الذكي يقمع <strong>54%</strong> من الإنذارات الكاذبة آلياً، مما يقلص زمن انتظار التنبيهات وينهي ظاهرة الإنهاك الذهني.
        </p>
        <div style="margin-top:auto;padding-top:10px;font-size:0.72rem;color:var(--t3);font-family:'JetBrains Mono',monospace">SOURCE: REPORT &sect;2.4.1, PAGE 29</div>
      </div>

      <!-- Metric 3: 95.1% True Threat Capture -->
      <div class="card" style="padding:22px;border:1px solid rgba(16,185,129,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(12,38,25,0.8));display:flex;flex-direction:column;align-items:center;text-align:center">
        <div style="font-size:0.75rem;font-weight:800;color:var(--ok);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px">SAFETY &amp; DETECTION ACCURACY</div>
        
        <!-- SVG Circular Completion Meter (95.1%) -->
        <div style="position:relative;width:140px;height:140px;margin-bottom:14px">
          <svg width="140" height="140" viewBox="0 0 100 100" style="transform:rotate(-90deg)">
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="rgba(255,255,255,0.08)" stroke-width="12"/>
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="var(--ok)" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="12.3" stroke-linecap="round" style="filter:drop-shadow(0 0 8px var(--ok))"/>
          </svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-size:2rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">95.1%</span>
            <span style="font-size:0.68rem;color:var(--ok);text-transform:uppercase;font-weight:700">Preserved</span>
          </div>
        </div>

        <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">True Threat Capture Rate</h3>
        <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">معدل التقاط التهديدات الحقيقية</h3>
        
        <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          Even while aggressively filtering 54% of noise, the triage engine preserves a <strong>95.1%</strong> true threat capture rate, ensuring security integrity.
        </p>
        <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          رغم قمع 54% من التنبيهات، يحافظ النموذج على <strong>95.1%</strong> من التهديدات الفعلية دون أي تفريط في الأمان المؤسسي.
        </p>
        <div style="margin-top:auto;padding-top:10px;font-size:0.72rem;color:var(--t3);font-family:'JetBrains Mono',monospace">SOURCE: REPORT &sect;2.4.1, PAGE 29</div>
      </div>

    </div>
  </div>
  <div class="sn">04 / 20</div>
</section>"""
    content = content[:old_s3.start()] + new_s3_html + content[old_s3.end():]
    print("Upgraded Slide 04 with 3 rich SVG metric gauges.")

# --- 2.2 SLIDE 07 (s6) SOC TECHNOLOGY EVOLUTION: ADD 4-GENERATION VISUAL TIMELINE ---
old_s6 = re.search(r'<section\b[^>]*id=["\']s6["\'][^>]*>.*?</section>', content, re.DOTALL)
if old_s6:
    new_s6_html = """<section class="slide" id="s6">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(0,212,255,0.4);background:rgba(0,212,255,0.08);margin-bottom:10px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M12 20v-6M6 20V10M18 20V4"/></svg>
      <span class="en" style="color:var(--s);font-weight:800;letter-spacing:1px">LITERATURE &amp; EVOLUTION &middot; CHAPTER 2 &sect;2.1-2.3</span>
      <span class="ar" style="display:none;color:var(--s);font-weight:800">تطور التقنيات والأدبيات السابقة &middot; الفصل 2 &sect;2.1-2.3</span>
    </div>
    <h2 class="st en" style="margin-bottom:4px">Existing Systems: SOC Technology Evolution</h2>
    <h2 class="st ar" style="display:none;margin-bottom:4px">الأنظمة الحالية: التطور التاريخي لتقنيات عمليات الأمن</h2>
    <div class="gl" style="margin:4px auto 14px"></div>
    <p class="lead en" style="margin-bottom:18px;font-size:0.98rem;max-width:940px">
      Tracing how security architectures evolved from raw perimeter logs to SIEM centralizers, conventional SOAR playbooks, and now AI-driven orchestration.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:18px;font-size:0.98rem;max-width:940px">
      تتبع مسار تطور المعماريات الأمنية من السجلات المعزولة إلى منصات SIEM وSOAR التقليدية وصولاً إلى الأتمتة الذكية المقترحة.
    </p>

    <!-- 4-Generation Visual Interactive Timeline -->
    <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:14px;width:100%;margin-bottom:16px">
      
      <!-- Gen 1: Syslog & Perimeter -->
      <div class="card" style="padding:18px;border:1px solid rgba(255,255,255,0.1);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(20,10,25,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:0.75rem;font-weight:800;color:var(--t3);font-family:'JetBrains Mono',monospace">GEN 1 &middot; 2000s</span>
          <span style="width:8px;height:8px;border-radius:50%;background:var(--t3)"></span>
        </div>
        <h3 class="en" style="font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">Perimeter Firewalls</h3>
        <h3 class="ar" style="display:none;font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">الجدران النارية والـ Syslog</h3>
        <p class="en" style="font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          Point tools logged events independently via Syslog. Analysts inspected text files manually without central correlation.
        </p>
        <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          تسجيل معزول للبيانات عبر السجلات النصية دون ربط مركزي مع فحص يدوي بطيء.
        </p>
      </div>

      <!-- Gen 2: SIEM -->
      <div class="card" style="padding:18px;border:1px solid rgba(0,212,255,0.25);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(15,25,35,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:0.75rem;font-weight:800;color:var(--s);font-family:'JetBrains Mono',monospace">GEN 2 &middot; 2010s</span>
          <span style="width:8px;height:8px;border-radius:50%;background:var(--s)"></span>
        </div>
        <h3 class="en" style="font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">SIEM Centralization</h3>
        <h3 class="ar" style="display:none;font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">منصات SIEM المركزية</h3>
        <p class="en" style="font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          Centralized log ingestion and rule correlation, but triggered massive alert fatigue (100GB/day) with zero automated response.
        </p>
        <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          تجميع مركزي وقواعد مطابقة، لكنها ولدت آلاف الإنذارات دون أي استجابة مؤتمتة.
        </p>
      </div>

      <!-- Gen 3: Conventional SOAR -->
      <div class="card" style="padding:18px;border:1px solid rgba(255,180,0,0.25);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(35,20,25,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:0.75rem;font-weight:800;color:#ffd166;font-family:'JetBrains Mono',monospace">GEN 3 &middot; 2018s</span>
          <span style="width:8px;height:8px;border-radius:50%;background:#ffd166"></span>
        </div>
        <h3 class="en" style="font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">Rule-Based SOAR</h3>
        <h3 class="ar" style="display:none;font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">SOAR التقليدي بالقواعد</h3>
        <p class="en" style="font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          Static playbooks and API orchestration; suffered from high maintenance, rigid boolean trees, and lack of AI triage intelligence.
        </p>
        <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          دفاتر عمل ثابتة وأتمتة واجهات؛ عانت من الهشاشة وصعوبة الصيانة وانعدام الذكاء.
        </p>
      </div>

      <!-- Gen 4: Our AI-SOAR -->
      <div class="card" style="padding:18px;border:1px solid var(--ok);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,40,30,0.8));box-shadow:0 0 20px rgba(16,185,129,0.2)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:0.75rem;font-weight:800;color:var(--ok);font-family:'JetBrains Mono',monospace">GEN 4 &middot; OUR WORK</span>
          <span style="width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 6px var(--ok)"></span>
        </div>
        <h3 class="en" style="font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">AI-Augmented SOAR</h3>
        <h3 class="ar" style="display:none;font-size:1.02rem;font-weight:800;color:#fff;margin-bottom:4px">أداة SOAR بالذكاء الاصطناعي</h3>
        <p class="en" style="font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          Dynamic Risk Scoring (R_total), multi-source enrichment, controlled decision gates, and continuous feedback loop adaptation.
        </p>
        <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);line-height:1.45;margin:0">
          فرز ذكي بمعادلة المخاطر (R_total)، إثراء شامل، بوابات تحكم، وحلقة تعلم مستمرة.
        </p>
      </div>

    </div>

    <!-- Comparative Callout Banner -->
    <div style="width:100%;padding:12px 16px;border-radius:10px;background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.08);display:flex;justify-content:space-between;align-items:center">
      <div style="font-size:0.86rem;color:var(--t2)" class="en">
        <strong>The Missing Link Identified in &sect;2.2.3:</strong> Conventional SOAR automates action dispatch, but lacks predictive triage to know <em>when</em> and <em>how aggressively</em> to act.
      </div>
      <div style="font-size:0.86rem;color:var(--t2);display:none" class="ar">
        <strong>الفجوة المحددة في بند 2.2.3:</strong> منصات SOAR التقليدية تؤتمت التنفيذ لكنها تفتقر للذكاء التنبؤي لمعرفة <em>متى</em> و<em>بأي درجة</em> يجب التدخل.
      </div>
      <span style="font-size:0.75rem;padding:4px 10px;border-radius:6px;background:rgba(0,212,255,0.15);color:var(--s);font-weight:700;white-space:nowrap">&sect;2.2.3 Core Finding</span>
    </div>
  </div>
  <div class="sn">07 / 20</div>
</section>"""
    content = content[:old_s6.start()] + new_s6_html + content[old_s6.end():]
    print("Upgraded Slide 07 with 4-generation visual timeline.")

# --- 2.3 SLIDE 13 (s12) AI/ML TRIAGE & RISK SCORING ENGINE: ADD DYNAMIC GAUGE & FORMULA VISUALIZER ---
old_s12 = re.search(r'<section\b[^>]*id=["\']s12["\'][^>]*>.*?</section>', content, re.DOTALL)
if old_s12:
    new_s12_html = """<section class="slide" id="s12">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(0,212,255,0.4);background:rgba(0,212,255,0.08);margin-bottom:10px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24M14.83 14.83l4.24 4.24M14.83 9.17l4.24-4.24M4.93 19.07l4.24-4.24"/></svg>
      <span class="en" style="color:var(--s);font-weight:800;letter-spacing:1px">MATHEMATICAL FORMULATION &middot; CHAPTER 3 &sect;3.5</span>
      <span class="ar" style="display:none;color:var(--s);font-weight:800">الصياغة الرياضية ومحرك الفرز &middot; الفصل 3 &sect;3.5</span>
    </div>
    <h2 class="st en" style="margin-bottom:4px">Design Progress: AI/ML Triage &amp; Dynamic Risk Scoring</h2>
    <h2 class="st ar" style="display:none;margin-bottom:4px">تقدم التصميم: محرك الفرز الذكي وتقييم المخاطر الديناميكي</h2>
    <div class="gl" style="margin:4px auto 14px"></div>
    <p class="lead en" style="margin-bottom:16px;font-size:0.98rem;max-width:940px">
      Rigorous formulation of total incident risk by coupling supervised machine learning threat probability with base severity and contextual asset criticality.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:16px;font-size:0.98rem;max-width:940px">
      الصياغة الرياضية المعتمدة لدرجة المخاطر الإجمالية بدمج احتمالية التعلم الآلي مع خطورة التنبيه وحساسية الأصل المستهدف.
    </p>

    <!-- Visual 2-Column Grid: Formula Card + Interactive Dynamic Risk Meter -->
    <div class="g2" style="gap:16px;width:100%">
      
      <!-- Left Column: Mathematical Formulation & Weights -->
      <div class="card" style="padding:20px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8))">
        <h3 class="en" style="font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:10px;display:flex;align-items:center;gap:8px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"/></svg>
          Dynamic Risk Formula (R_total)
        </h3>
        <h3 class="ar" style="display:none;font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:10px;align-items:center;gap:8px">
          معادلة تقييم المخاطر الإجمالية الديناميكية
        </h3>

        <!-- Mathematical Box -->
        <div style="background:rgba(0,0,0,0.4);border-radius:10px;padding:14px;border:1px solid rgba(0,212,255,0.3);text-align:center;margin-bottom:14px">
          <div style="font-size:1.25rem;font-weight:900;color:var(--s);font-family:'JetBrains Mono',monospace;letter-spacing:1px">
            R_total = &alpha; &middot; P(Threat) + &beta; &middot; S_base + &gamma; &middot; C_asset
          </div>
          <div style="font-size:0.75rem;color:var(--t3);margin-top:6px;font-family:'JetBrains Mono',monospace">
            Constraint: &alpha; + &beta; + &gamma; = 1.0 &nbsp;|&nbsp; Recommended: &alpha; = 0.50, &beta; = 0.30, &gamma; = 0.20
          </div>
        </div>

        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px;font-size:0.86rem;color:var(--t2)">
          <li style="display:flex;align-items:flex-start;gap:8px">
            <span style="color:var(--s);font-weight:800">&bull;</span>
            <span class="en"><strong>P(Threat) &isin; [0, 1]:</strong> Probabilistic confidence score output by supervised ensemble (Random Forest / XGBoost).</span>
            <span class="ar" style="display:none"><strong>P(Threat):</strong> احتمالية التهديد المحسوبة بنماذج التعلم الآلي بين 0 و1.</span>
          </li>
          <li style="display:flex;align-items:flex-start;gap:8px">
            <span style="color:var(--s);font-weight:800">&bull;</span>
            <span class="en"><strong>S_base &isin; [0, 1]:</strong> Normalized vendor alert severity (CVSS / vendor baseline severity tag).</span>
            <span class="ar" style="display:none"><strong>S_base:</strong> خطورة التنبيه الأولية القياسية المأخوذة من أنظمة الكشف.</span>
          </li>
          <li style="display:flex;align-items:flex-start;gap:8px">
            <span style="color:var(--s);font-weight:800">&bull;</span>
            <span class="en"><strong>C_asset &isin; [0, 1]:</strong> Normalized business criticality weight of target system from Asset DB.</span>
            <span class="ar" style="display:none"><strong>C_asset:</strong> الأهمية التشغيلية وحساسية النظام المستهدف من قاعدة الأصول.</span>
          </li>
        </ul>
      </div>

      <!-- Right Column: Visual Severity Gauge & Priority Queue Mapping -->
      <div class="card" style="padding:20px;border:1px solid rgba(255,180,0,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(35,20,30,0.8));display:flex;flex-direction:column;justify-content:space-between">
        <div>
          <h3 class="en" style="font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:10px;display:flex;align-items:center;gap:8px">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffd166" stroke-width="2.2"><path d="M12 20v-6M6 20V10M18 20V4"/></svg>
            Dynamic Priority Queue Slots
          </h3>
          <h3 class="ar" style="display:none;font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:10px;align-items:center;gap:8px">
            توزيع مستويات الأولوية وتصنيف الطوابير
          </h3>

          <!-- Visual Multi-Zone Risk Bar -->
          <div style="margin-bottom:14px">
            <div style="height:14px;border-radius:7px;background:linear-gradient(90deg, #10b981 0%, #10b981 25%, #00d4ff 25%, #00d4ff 55%, #ffd166 55%, #ffd166 80%, #ef4444 80%, #ef4444 100%);box-shadow:0 0 10px rgba(0,0,0,0.5)"></div>
            <div style="display:flex;justify-content:space-between;font-size:0.7rem;color:var(--t3);font-family:'JetBrains Mono',monospace;margin-top:4px">
              <span>0.0</span><span>0.25</span><span>0.55</span><span>0.80</span><span>1.0</span>
            </div>
          </div>

          <!-- Queue Levels -->
          <div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:8px;margin-bottom:10px">
            <div style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.4);border-radius:8px;padding:8px 10px">
              <div style="font-size:0.78rem;font-weight:800;color:#ff6b6b">P1 &middot; CRITICAL (R &ge; 0.80)</div>
              <div style="font-size:0.72rem;color:var(--t2)">Immediate automated containment</div>
            </div>
            <div style="background:rgba(255,180,0,0.15);border:1px solid rgba(255,180,0,0.4);border-radius:8px;padding:8px 10px">
              <div style="font-size:0.78rem;font-weight:800;color:#ffd166">P2 &middot; HIGH (0.55 &le; R &lt; 0.80)</div>
              <div style="font-size:0.72rem;color:var(--t2)">Semi-autonomous approval gate</div>
            </div>
            <div style="background:rgba(0,212,255,0.15);border:1px solid rgba(0,212,255,0.4);border-radius:8px;padding:8px 10px">
              <div style="font-size:0.78rem;font-weight:800;color:var(--s)">P3 &middot; MEDIUM (0.25 &le; R &lt; 0.55)</div>
              <div style="font-size:0.72rem;color:var(--t2)">Standard analyst triage queue</div>
            </div>
            <div style="background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.4);border-radius:8px;padding:8px 10px">
              <div style="font-size:0.78rem;font-weight:800;color:var(--ok)">P4 &middot; SUPPRESSED (R &lt; 0.25)</div>
              <div style="font-size:0.72rem;color:var(--t2)">Benign noise suppressed (54%)</div>
            </div>
          </div>
        </div>

        <div style="padding-top:8px;border-top:1px solid rgba(255,255,255,0.08);font-size:0.76rem;color:var(--t3);display:flex;justify-content:space-between">
          <span>&sect;3.5 FORMULA DERIVATION</span>
          <span style="color:var(--ok);font-weight:700">&check; ZERO ARBITRARY GUESSES</span>
        </div>
      </div>

    </div>
  </div>
  <div class="sn">13 / 20</div>
</section>"""
    content = content[:old_s12.start()] + new_s12_html + content[old_s12.end():]
    print("Upgraded Slide 13 with mathematical risk gauge and formula visualizer.")

# --- 2.4 SLIDE 18 (s17) TESTING & EVALUATION: ADD BENCHMARK DASHBOARD ---
old_s17 = re.search(r'<section\b[^>]*id=["\']s17["\'][^>]*>.*?</section>', content, re.DOTALL)
if old_s17:
    new_s17_html = """<section class="slide" id="s17">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(0,212,255,0.4);background:rgba(0,212,255,0.08);margin-bottom:10px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
      <span class="en" style="color:var(--s);font-weight:800;letter-spacing:1px">EMPIRICAL BENCHMARKS &middot; CHAPTER 2 &sect;2.4 &amp; CHAPTER 3</span>
      <span class="ar" style="display:none;color:var(--s);font-weight:800">المؤشرات المعيارية وخطة التقييم &middot; الفصل 2 &sect;2.4 والفصل 3</span>
    </div>
    <h2 class="st en" style="margin-bottom:4px">Testing &amp; Empirical Evaluation Framework</h2>
    <h2 class="st ar" style="display:none;margin-bottom:4px">إطار الاختبار والتقييم التجريبي المعياري</h2>
    <div class="gl" style="margin:4px auto 14px"></div>
    <p class="lead en" style="margin-bottom:16px;font-size:0.98rem;max-width:940px">
      Quantitative validation criteria using public cybersecurity benchmark datasets and statistical performance metrics.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:16px;font-size:0.98rem;max-width:940px">
      معايير التحقق الكمي المعتمدة باستخدام مجموعات البيانات القياسية ومقاييس الأداء الإحصائي المعيارية.
    </p>

    <!-- 2-Column Evaluation Dashboard -->
    <div class="g2" style="gap:16px;width:100%">
      
      <!-- Benchmark Datasets -->
      <div class="card" style="padding:20px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8))">
        <h3 class="en" style="font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:12px;display:flex;align-items:center;gap:8px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
          Benchmark Testbed Datasets
        </h3>
        <h3 class="ar" style="display:none;font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:12px;align-items:center;gap:8px">
          مجموعات البيانات المعيارية للاختبار
        </h3>

        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06)">
            <div style="display:flex;justify-content:space-between;font-weight:700;color:#fff;font-size:0.88rem">
              <span>CIC-IDS2017 / CSE-CIC-IDS2018</span>
              <span style="color:var(--s);font-size:0.75rem">Canadian Institute for Cybersecurity</span>
            </div>
            <p class="en" style="font-size:0.8rem;color:var(--t2);margin:4px 0 0">
              Realistic multi-vector attack traffic (DDoS, Brute Force, Infiltration, Botnet) with diverse packet and flow telemetry.
            </p>
            <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:4px 0 0">
              حركة مرور تحاكي هجمات سيبرانية حقيقية (حجب الخدمة، الاختراق، البوتنت) مع سجلات تدفق وحزم تفصيلية.
            </p>
          </div>

          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06)">
            <div style="display:flex;justify-content:space-between;font-weight:700;color:#fff;font-size:0.88rem">
              <span>UNSW-NB15 Dataset</span>
              <span style="color:var(--s);font-size:0.75rem">Cyber Range Lab (UNSW)</span>
            </div>
            <p class="en" style="font-size:0.8rem;color:var(--t2);margin:4px 0 0">
              Modern synthetic attack behaviors and contemporary normal background traffic across 49 features.
            </p>
            <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:4px 0 0">
              سلوكيات هجومية حديثة وحركة مرور طبيعية معاصرة تضم 49 خاصية أمنية.
            </p>
          </div>
        </div>
      </div>

      <!-- Performance Metrics Bars -->
      <div class="card" style="padding:20px;border:1px solid rgba(16,185,129,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(12,38,25,0.8))">
        <h3 class="en" style="font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:12px;display:flex;align-items:center;gap:8px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--ok)" stroke-width="2.2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          Quantitative Target Metrics
        </h3>
        <h3 class="ar" style="display:none;font-size:1.08rem;font-weight:800;color:#fff;margin-bottom:12px;align-items:center;gap:8px">
          مقاييس الأداء المستهدفة
        </h3>

        <div style="display:flex;flex-direction:column;gap:12px">
          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.82rem;font-weight:700;margin-bottom:4px">
              <span style="color:#fff">False Positive Suppression Rate</span>
              <span style="color:var(--ok);font-family:'JetBrains Mono',monospace">&ge; 54% Target</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:54%;height:100%;background:var(--ok);border-radius:4px;box-shadow:0 0 6px var(--ok)"></div>
            </div>
          </div>

          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.82rem;font-weight:700;margin-bottom:4px">
              <span style="color:#fff">Precision &amp; Recall (AlertPro Benchmark)</span>
              <span style="color:var(--s);font-family:'JetBrains Mono',monospace">96.3% / 98.5%</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:96%;height:100%;background:var(--s);border-radius:4px;box-shadow:0 0 6px var(--s)"></div>
            </div>
          </div>

          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.82rem;font-weight:700;margin-bottom:4px">
              <span style="color:#fff">Mean Time to Respond (MTTR) Reduction</span>
              <span style="color:#ffd166;font-family:'JetBrains Mono',monospace">&gt; 50% Faster</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:75%;height:100%;background:#ffd166;border-radius:4px;box-shadow:0 0 6px #ffd166"></div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  <div class="sn">18 / 20</div>
</section>"""
    content = content[:old_s17.start()] + new_s17_html + content[old_s17.end():]
    print("Upgraded Slide 18 with quantitative benchmark dashboard.")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully applied complete taste overhaul and saved presentation/index.html!")
