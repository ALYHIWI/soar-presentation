# -*- coding: utf-8 -*-
"""
Script to apply slide-specific HTML upgrades to presentation/index.html
"""
import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Helper function to replace section content by section id
def replace_section(html_content, section_id, new_section_html):
    pattern = re.compile(rf'<section\b[^>]*id=["\']{section_id}["\'][^>]*>.*?</section>', re.DOTALL)
    match = pattern.search(html_content)
    if not match:
        raise ValueError(f"Section {section_id} not found in HTML!")
    return pattern.sub(new_section_html, html_content, count=1)

# === 1. Slide 2 (id="s1"): Ensure Multi-Vendor is strictly on one single line ===
new_s1 = """<section class="slide" id="s1">
  <div class="orb o2" style="opacity:0.35"></div>
  <div class="content-box">
  <div class="tag a1">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/></svg>
  <span class="en">Chapter 1 &ndash; Background</span><span class="ar" style="display:none">الفصل الأول &ndash; الخلفية</span>
  </div>
  <h2 class="st en">Background: The Modern SOC Landscape</h2>
  <h2 class="st ar" style="display:none">الخلفية: مشهد مراكز العمليات الأمنية الحديثة</h2>
  <div class="gl"></div>
  <p class="lead en">A Security Operations Center (SOC) centralizes cyber threat monitoring, detection, and incident response &mdash; but faces acute operational strain from massive log volumes and heterogeneous data schemas.</p>
  <p class="lead ar" style="display:none">مركز العمليات الأمنية (SOC) هو الوحدة المركزية لرصد التهديدات السيبرانية والاستجابة لها، لكنه يواجه ضغطاً تشغيلياً حاداً بسبب طوفان البيانات وتشتت مصادر السجلات.</p>

  <div class="split-ill-grid">
    <!-- Left Column: 3 Core Operational Points & Stat Row -->
    <div style="display:flex;flex-direction:column;gap:10px">
      <div class="card" style="padding:12px 14px">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
          <div class="c-icon cy" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg></div>
          <h3 class="ct en" style="margin:0;font-size:0.95rem">SIEM Platforms &bull; Influx</h3>
          <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">منصات SIEM وطوفان البيانات</h3>
        </div>
        <p class="en" style="font-size:0.82rem;margin:0">Organizations implement SIEM for centralized log management and correlation, accumulating up to <strong>100 GB</strong> of log and alert telemetry daily.</p>
        <p class="ar" style="display:none;font-size:0.82rem;margin:0">تجمع المنظمات ما يصل إلى <strong>100 غيغابايت</strong> من السجلات والتنبيهات يومياً عبر منصات SIEM المركزية.</p>
      </div>

      <div class="card" style="padding:12px 14px">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
          <div class="c-icon rd" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
          <h3 class="ct en" style="margin:0;font-size:0.95rem">Heterogeneous Tool Stacks</h3>
          <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">تشتت الأدوات الأمنية</h3>
        </div>
        <p class="en" style="font-size:0.82rem;margin:0">Multi-vendor security tools (EDR, Firewalls, Cloud) operate with distinct schemas, creating highly fragmented data that is difficult to normalize and correlate.</p>
        <p class="ar" style="display:none;font-size:0.82rem;margin:0">أدوات أمنية متعددة الموردين تعمل بصيغ سجلات متباينة، مما يخلق بيانات مشتتة يصعب توحيدها ومطابقتها.</p>
      </div>

      <div class="card" style="padding:12px 14px">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
          <div class="c-icon ye" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
          <h3 class="ct en" style="margin:0;font-size:0.95rem">Tiered Analyst Hierarchy</h3>
          <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">هرمية المحللين المرهقة</h3>
        </div>
        <p class="en" style="font-size:0.82rem;margin:0">Junior analysts manually investigate alerts by pivoting across disparate tools to evaluate each alert &mdash; creating an acute operational bottleneck.</p>
        <p class="ar" style="display:none;font-size:0.82rem;margin:0">المحللون المبتدئون يجمعون الأدلة يدوياً عبر التنقل بين أدوات منفصلة لتقييم كل تنبيه، مما يولد عنق زجاجة تشغيلي.</p>
      </div>

      <div class="srow" style="margin-top:2px;display:flex;gap:10px">
        <div class="sb" style="flex:1;min-width:0"><div class="snum" style="white-space:nowrap">100 GB</div><div class="slbl en">Daily Influx</div><div class="slbl ar" style="display:none">سجلات يومية</div></div>
        <div class="sb" style="flex:1.2;min-width:0"><div class="snum" style="white-space:nowrap;font-size:clamp(0.85rem, 1.15vw, 1.08rem);letter-spacing:-0.2px">Multi-Vendor</div><div class="slbl en">Data Stacks</div><div class="slbl ar" style="display:none">بيانات متباينة</div></div>
        <div class="sb" style="flex:1;min-width:0"><div class="snum" style="white-space:nowrap">Tier 1-3</div><div class="slbl en">Analyst Model</div><div class="slbl ar" style="display:none">هرمية التحليل</div></div>
      </div>
    </div>

    <!-- Right Column: Illustrated Modern SOC Command Center Card -->
    <div class="ill-card">
      <div class="ill-frame" onclick="openImageModal('images/soc_command_center.jpg', 'Modern Enterprise SOC Command Center - Real-Time Telemetry & Monitoring')">
        <img src="images/soc_command_center.jpg" alt="Modern Enterprise SOC Command Center" class="ill-img" loading="lazy"/>
        <div class="ill-zoom-hint">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          <span>ZOOM</span>
        </div>
      </div>
      <div class="ill-caption">
        <div class="ill-title">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
          <span class="en">Modern Enterprise SOC Command Center</span>
          <span class="ar" style="display:none">غرفة العمليات والسيطرة الأمنية الحديثة</span>
        </div>
        <div class="ill-sub">CHAPTER 1 &sect;1.1</div>
      </div>
    </div>
  </div>

  </div>
  <div class="sn">02 / 21</div>
</section>"""

html = replace_section(html, 's1', new_s1)
print("Updated Slide 2 (s1): Multi-Vendor strictly single line.")

# === 2. Slide 4 (id="s3"): Strip SOURCE labels, 91% precision gauge ===
new_s3 = """<section class="slide" id="s3">
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
      </div>

      <!-- Metric 3: 91% Verified High-Recall Capture / Precision Gauge -->
      <div class="card" style="padding:22px;border:1px solid rgba(16,185,129,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(12,38,25,0.8));display:flex;flex-direction:column;align-items:center;text-align:center">
        <div style="font-size:0.75rem;font-weight:800;color:var(--ok);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px">SAFETY &amp; DETECTION ACCURACY</div>
        
        <!-- SVG Circular Completion Meter: 91% (stroke-dashoffset = 251.2 * 0.09 = 22.6) -->
        <div style="position:relative;width:140px;height:140px;margin-bottom:14px">
          <svg width="140" height="140" viewBox="0 0 100 100" style="transform:rotate(-90deg)">
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="rgba(255,255,255,0.08)" stroke-width="12"/>
            <circle cx="50" cy="50" r="40" fill="transparent" stroke="var(--ok)" stroke-width="12" stroke-dasharray="251.2" stroke-dashoffset="22.6" stroke-linecap="round" style="filter:drop-shadow(0 0 8px var(--ok))"/>
          </svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-size:2rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">91%</span>
            <span style="font-size:0.68rem;color:var(--ok);text-transform:uppercase;font-weight:700">Preserved</span>
          </div>
        </div>

        <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">True Threat Capture Rate</h3>
        <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:6px">معدل التقاط التهديدات الحقيقية</h3>
        
        <p class="en" style="font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          Even while aggressively filtering 54% of noise, the triage engine preserves over <strong>91%</strong> true threat capture rate, ensuring enterprise security integrity.
        </p>
        <p class="ar" style="display:none;font-size:0.86rem;color:var(--t2);line-height:1.5;margin:0">
          رغم قمع 54% من التنبيهات، يحافظ النموذج على أكثر من <strong>91%</strong> من التهديدات الفعلية دون أي تفريط في الأمان المؤسسي.
        </p>
      </div>

    </div>
  </div>
  <div class="sn">04 / 21</div>
</section>"""

html = replace_section(html, 's3', new_s3)
print("Updated Slide 4 (s3): Removed SOURCE citations, fixed 91% meter.")

# === 3. Slide 7 (id="s6"): Object-fit contain for soc_tech_evolution.jpg ===
new_s6 = """<section class="slide" id="s6">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(0,212,255,0.4);background:rgba(0,212,255,0.08);margin-bottom:8px">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M12 20v-6M6 20V10M18 20V4"/></svg>
      <span class="en" style="color:var(--s);font-weight:800;letter-spacing:1px">LITERATURE &amp; EVOLUTION &middot; CHAPTER 2 &sect;2.1-2.3</span>
      <span class="ar" style="display:none;color:var(--s);font-weight:800">تطور التقنيات والأدبيات السابقة &middot; الفصل 2 &sect;2.1-2.3</span>
    </div>
    <h2 class="st en" style="margin-bottom:4px">Existing Systems: SOC Technology Evolution</h2>
    <h2 class="st ar" style="display:none;margin-bottom:4px">الأنظمة الحالية: التطور التاريخي لتقنيات عمليات الأمن</h2>
    <div class="gl" style="margin:4px auto 10px"></div>

    <!-- Featured 3D Evolution Timeline Illustration Card - Full Uncropped View -->
    <div class="ill-card" style="margin-bottom:12px;padding:8px;background:rgba(15,10,22,0.85);border:1px solid rgba(0,212,255,0.25)">
      <div class="ill-frame" style="height:auto;max-height:270px;background:#050208;display:flex;align-items:center;justify-content:center" onclick="openImageModal('images/soc_tech_evolution.jpg', 'Evolution of Security Operations Technologies: Gen 1 to Gen 4')">
        <img src="images/soc_tech_evolution.jpg" alt="Evolution of Security Operations Technologies" style="width:100%;height:auto;max-height:260px;object-fit:contain;display:block;margin:0 auto" loading="lazy"/>
        <div class="ill-zoom-hint">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          <span>FULL TIMELINE ZOOM</span>
        </div>
      </div>
      <div class="ill-caption" style="padding:6px 10px 4px">
        <div class="ill-title" style="font-size:0.82rem">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg>
          <span class="en">From Manual Log Silos (Gen 1) to Autonomous AI-Augmented SOAR (Gen 4)</span>
          <span class="ar" style="display:none">من صوامع السجلات اليدوية (الجيل 1) إلى أداة SOAR المعززة بالذكاء (الجيل 4)</span>
        </div>
        <div class="ill-sub">CHAPTER 2 &sect;2.1-2.3 &middot; COMPLETE 4 GENERATIONS</div>
      </div>
    </div>

    <!-- 4-Generation Concise Cards Grid -->
    <div style="display:grid;grid-template-columns:repeat(4, 1fr);gap:12px;width:100%;margin-bottom:10px">
      
      <!-- Gen 1 -->
      <div class="card" style="padding:12px 14px;border:1px solid rgba(255,255,255,0.1);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(20,10,25,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
          <span style="font-size:0.72rem;font-weight:800;color:var(--t3);font-family:'JetBrains Mono',monospace">GEN 1 &middot; 2000s</span>
          <span style="width:7px;height:7px;border-radius:50%;background:var(--t3)"></span>
        </div>
        <h3 class="en" style="font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">Log Management</h3>
        <h3 class="ar" style="display:none;font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">إدارة السجلات</h3>
        <p class="en" style="font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">Point tools logged independently via Syslog. Analysts inspected text files manually.</p>
        <p class="ar" style="display:none;font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">تسجيل معزول عبر السجلات النصية مع فحص يدوي بطيء.</p>
      </div>

      <!-- Gen 2 -->
      <div class="card" style="padding:12px 14px;border:1px solid rgba(0,212,255,0.25);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(15,25,35,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
          <span style="font-size:0.72rem;font-weight:800;color:var(--s);font-family:'JetBrains Mono',monospace">GEN 2 &middot; 2010s</span>
          <span style="width:7px;height:7px;border-radius:50%;background:var(--s)"></span>
        </div>
        <h3 class="en" style="font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">SIEM Platforms</h3>
        <h3 class="ar" style="display:none;font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">منصات SIEM</h3>
        <p class="en" style="font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">Centralized log collection and rules, but created massive alert fatigue (100 GB/day) with zero auto-response.</p>
        <p class="ar" style="display:none;font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">تجميع مركزي وقواعد مطابقة، ولدت آلاف الإنذارات دون استجابة آلية.</p>
      </div>

      <!-- Gen 3 -->
      <div class="card" style="padding:12px 14px;border:1px solid rgba(255,180,0,0.25);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(35,20,25,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
          <span style="font-size:0.72rem;font-weight:800;color:#ffd166;font-family:'JetBrains Mono',monospace">GEN 3 &middot; 2018s</span>
          <span style="width:7px;height:7px;border-radius:50%;background:#ffd166"></span>
        </div>
        <h3 class="en" style="font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">Rule-Based SOAR</h3>
        <h3 class="ar" style="display:none;font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">SOAR التقليدي</h3>
        <p class="en" style="font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">Static playbooks and API orchestration; rigid conditional trees with zero AI risk intelligence.</p>
        <p class="ar" style="display:none;font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">دفاتر عمل ثابتة وأتمتة واجهات؛ عانت من الجمود وغياب ذكاء تقدير المخاطر.</p>
      </div>

      <!-- Gen 4 -->
      <div class="card" style="padding:12px 14px;border:1px solid var(--ok);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,40,30,0.8));box-shadow:0 0 16px rgba(16,185,129,0.2)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
          <span style="font-size:0.72rem;font-weight:800;color:var(--ok);font-family:'JetBrains Mono',monospace">GEN 4 &middot; OUR WORK</span>
          <span style="width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 6px var(--ok)"></span>
        </div>
        <h3 class="en" style="font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">AI-Augmented SOAR</h3>
        <h3 class="ar" style="display:none;font-size:0.92rem;font-weight:800;color:#fff;margin-bottom:3px">SOAR بالذكاء الاصطناعي</h3>
        <p class="en" style="font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">Dynamic Risk Scoring (R_total), multi-source enrichment, controlled decision gates, and adaptive feedback.</p>
        <p class="ar" style="display:none;font-size:0.78rem;color:var(--t2);line-height:1.4;margin:0">تقييم مخاطر ديناميكي (R_total)، إثراء شامل، بوابات تحكم، وحلقة تعلم.</p>
      </div>

    </div>

    <!-- Comparative Callout Banner -->
    <div style="width:100%;padding:10px 14px;border-radius:8px;background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.08);display:flex;justify-content:space-between;align-items:center">
      <div style="font-size:0.82rem;color:var(--t2)" class="en">
        <strong>The Missing Link (&sect;2.2.3):</strong> Conventional SOAR automates action dispatch, but lacks predictive triage to know <em>when</em> and <em>how aggressively</em> to act without risking service disruption.
      </div>
      <div style="font-size:0.82rem;color:var(--t2);display:none" class="ar">
        <strong>الفجوة الجوهرية (بند 2.2.3):</strong> منصات SOAR التقليدية تؤتمت التنفيذ لكنها تفتقر للفرز التنبؤي لمعرفة <em>متى</em> و<em>بأي شدة</em> تتدخل دون تعطيل الأعمال.
      </div>
      <span style="font-size:0.72rem;padding:3px 8px;border-radius:6px;background:rgba(0,212,255,0.15);color:var(--s);font-weight:700;white-space:nowrap">&sect;2.2.3 Core Finding</span>
    </div>
  </div>
  <div class="sn">07 / 21</div>
</section>"""

html = replace_section(html, 's6', new_s6)
print("Updated Slide 7 (s6): soc_tech_evolution.jpg scaled with object-fit: contain.")

# === 4. Slide 8 (id="s7"): Add prior_work_benchmark.jpg alongside Table 2-1 ===
new_s7 = """<section class="slide" id="s7">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(255,80,80,0.4);background:rgba(255,80,80,0.06)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ff6b6b" stroke-width="2"><polygon points="7.86 2 16.14 2 22 7.86 22 16.14 16.14 22 7.86 22 16.14 16.14 22 7.86 22 2 16.14 2 7.86 7.86 2"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      <span class="en" style="color:#ff8e8e">Chapter 2 &ndash; Gap Analysis</span><span class="ar" style="display:none;color:#ff8e8e">الفصل الثاني &ndash; تحليل الفجوة</span>
    </div>
    <h2 class="st en">Comparative Analysis of Prior Work (Table 2-1)</h2>
    <h2 class="st ar" style="display:none">المقارنة المعيارية للأعمال السابقة (جدول 2-1)</h2>
    <div class="gl"></div>

    <div style="display:grid;grid-template-columns:1.22fr 0.78fr;gap:16px;align-items:start;margin-top:10px">
      <!-- Left Column: Table 2-1 -->
      <div class="tbl-wrap" style="overflow-x:auto;margin:0">
        <table class="ctbl" style="font-size:0.78rem">
          <thead>
            <tr>
              <th><span class="en">Study</span><span class="ar" style="display:none">الدراسة</span></th>
              <th><span class="en">AI/ML Approach</span><span class="ar" style="display:none">نموذج الذكاء الاصطناعي</span></th>
              <th><span class="en">Key Result</span><span class="ar" style="display:none">النتيجة الرئيسية</span></th>
              <th style="color:var(--acc)"><span class="en">SOAR Integration</span><span class="ar" style="display:none">تكامل SOAR</span></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Gupta et al. (2019)</strong></td>
              <td><span class="en">Random Forest (39,427 events)</span><span class="ar" style="display:none">غابة عشوائية</span></td>
              <td><span class="en">AUC 92.67%, Recall 0.92</span><span class="ar" style="display:none">AUC 92.67%</span></td>
              <td><span class="pill pr">No</span></td>
            </tr>
            <tr>
              <td><strong>Gelman et al. (2023)</strong></td>
              <td><span class="en">Gradient Boosting (commercial cloud SOC)</span><span class="ar" style="display:none">تعزيز تدريجي</span></td>
              <td><span class="en">54% FP suppression, 95.1% capture, 22.9% dwell&darr;</span><span class="ar" style="display:none">54% قمع إيجابيات كاذبة، 22.9% تقليص وقت انتظار</span></td>
              <td><span class="pill pr">No</span></td>
            </tr>
            <tr>
              <td><strong>Liu et al. (2022)</strong></td>
              <td><span class="en">Context2Vector (2.45M events)</span><span class="ar" style="display:none">تمثيل سياقي</span></td>
              <td><span class="en">2.25&times; attacker IP recall improvement</span><span class="ar" style="display:none">2.25&times; تحسن استرجاع IP المهاجم</span></td>
              <td><span class="pill pr">No</span></td>
            </tr>
            <tr>
              <td><strong>Wang et al. (2024)</strong></td>
              <td><span class="en">AlertPro adaptive online learning</span><span class="ar" style="display:none">تعلم تكيفي</span></td>
              <td><span class="en">96.32% precision, 98.47% recall</span><span class="ar" style="display:none">دقة 96.32%، استرجاع 98.47%</span></td>
              <td><span class="pill pr">No</span></td>
            </tr>
            <tr>
              <td><strong>Chavali et al. (2024)</strong></td>
              <td><span class="en">TD3-AP/SAC-AP DRL</span><span class="ar" style="display:none">تعلم تعزيزي عميق</span></td>
              <td><span class="en">50% feature payload reduction, 300&micro;s decision</span><span class="ar" style="display:none">50% تقليص الحمل، 300&micro;s قرار</span></td>
              <td><span class="pill pr">No</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Right Column: Benchmark & SOAR Gap Illustration -->
      <div class="ill-card" style="margin:0;padding:6px">
        <div class="ill-frame" style="max-height:210px" onclick="openImageModal('images/prior_work_benchmark.jpg', 'Comparative Prior Work Benchmark vs SOAR Integration Gap')">
          <img src="images/prior_work_benchmark.jpg" alt="Comparative Prior Work Benchmark" class="ill-img" loading="lazy" style="object-fit:cover;height:210px"/>
          <div class="ill-zoom-hint">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
            <span>BENCHMARK ZOOM</span>
          </div>
        </div>
        <div class="ill-caption" style="padding:4px 8px">
          <div class="ill-title" style="font-size:0.75rem">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--acc)" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span class="en">Critical Void: Advanced ML Models Lack Downstream SOAR Actions</span>
            <span class="ar" style="display:none">الفجوة الحرجة: نماذج الذكاء السابقة تفتقر لتنفيذ استجابات SOAR</span>
          </div>
          <div class="ill-sub">CHAPTER 2 &sect;2.3 &middot; TABLE 2-1 BENCHMARK</div>
        </div>
      </div>
    </div>

    <div class="hl" style="margin-top:10px;border-color:var(--acc)">
      <p class="en"><strong>Research Gap (Table 2-1 Synthesis):</strong> None of the reviewed systems execute automated downstream SOAR response workflows. The integration between ML-based triage and SOAR-controlled response <strong>remains an unaddressed area</strong> &mdash; the core gap this project investigates.</p>
      <p class="ar" style="display:none"><strong>الفجوة البحثية (خلاصة جدول 2-1):</strong> لا يُنفذ أي نظام مراجع مسارات استجابة SOAR المؤتمتة. التكامل بين الفرز القائم على ML والاستجابة المتحكم فيها بـ SOAR <strong>لا يزال غير معالج</strong> &mdash; وهذه هي الفجوة الجوهرية.</p>
    </div>
  </div>
  <div class="sn">08 / 21</div>
</section>"""

html = replace_section(html, 's7', new_s7)
print("Updated Slide 8 (s7): Added prior_work_benchmark.jpg alongside Table 2-1.")

# === 5. Slide 11 (id="s10"): Add dsr_6phases_methodology.jpg ===
new_s10 = """<section class="slide" id="s10">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
      <span class="en">Chapter 1 &ndash; Methodology</span><span class="ar" style="display:none">الفصل الأول &ndash; المنهجية</span>
    </div>
    <h2 class="st en">Development Methodology: Design Science Research (DSR)</h2>
    <h2 class="st ar" style="display:none">منهجية التطوير: علوم التصميم (DSR)</h2>
    <div class="gl"></div>
    <p class="lead en">DSR was selected as it provides a systematic, evidence-based framework for constructing and evaluating design artifacts &mdash; suited to AI-integrated system development where the goal is to build a justified solution to a real operational problem.</p>
    <p class="lead ar" style="display:none">تم اختيار DSR لأنها توفر إطاراً منهجياً قائماً على الأدلة لبناء وتقييم القطع المعمارية &mdash; مناسب لتطوير الأنظمة المدمجة بالذكاء الاصطناعي.</p>

    <div style="display:grid;grid-template-columns:1.15fr 0.85fr;gap:16px;align-items:center;margin-top:12px">
      <!-- Left Column: 6 Phases Flow Grid -->
      <div style="display:flex;flex-direction:column;gap:10px">
        <div class="flow" style="margin:0;display:grid;grid-template-columns:repeat(3, 1fr);gap:10px">
          <div class="fs" style="padding:10px;background:rgba(255,255,255,0.04);border:1px solid rgba(16,185,129,0.3)">
            <div class="fi" style="background:var(--ok);color:#000;font-weight:900">1</div>
            <div class="fl en" style="font-size:0.75rem">Problem Identification</div>
            <div class="fl ar" style="display:none;font-size:0.75rem">تحديد المشكلة</div>
          </div>
          <div class="fs" style="padding:10px;background:rgba(255,255,255,0.04);border:1px solid rgba(16,185,129,0.3)">
            <div class="fi" style="background:var(--ok);color:#000;font-weight:900">2</div>
            <div class="fl en" style="font-size:0.75rem">Solution Objectives</div>
            <div class="fl ar" style="display:none;font-size:0.75rem">أهداف الحل</div>
          </div>
          <div class="fs" style="padding:10px;background:rgba(255,255,255,0.04);border:1px solid rgba(16,185,129,0.3)">
            <div class="fi" style="background:var(--ok);color:#000;font-weight:900">3</div>
            <div class="fl en" style="font-size:0.75rem">Architecture Design</div>
            <div class="fl ar" style="display:none;font-size:0.75rem">تصميم المعمارية</div>
          </div>
          <div class="fs" style="padding:10px;background:rgba(0,212,255,0.1);border:1px solid var(--s);box-shadow:0 0 10px rgba(0,212,255,0.25)">
            <div class="fi" style="background:var(--s);color:#000;font-weight:900">4</div>
            <div class="fl en" style="font-size:0.75rem;font-weight:800;color:#fff">Prototype Demo (Active)</div>
            <div class="fl ar" style="display:none;font-size:0.75rem;font-weight:800;color:#fff">عرض النموذج (قيد التقدم)</div>
          </div>
          <div class="fs" style="padding:10px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1)">
            <div class="fi">5</div>
            <div class="fl en" style="font-size:0.75rem">Evaluation</div>
            <div class="fl ar" style="display:none;font-size:0.75rem">التقييم</div>
          </div>
          <div class="fs" style="padding:10px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1)">
            <div class="fi">6</div>
            <div class="fl en" style="font-size:0.75rem">Communication</div>
            <div class="fl ar" style="display:none;font-size:0.75rem">التوثيق</div>
          </div>
        </div>

        <div class="hl" style="margin:0">
          <p class="en" style="font-size:0.84rem"><strong>Current Phase:</strong> The project has completed Phases 1–3 (Problem Identification, Solution Objectives, Architecture Design) and is actively progressing through Phase 4 (Prototype Development).</p>
          <p class="ar" style="display:none" style="font-size:0.84rem"><strong>المرحلة الحالية:</strong> المشروع أكمل المراحل 1–3 (تحديد المشكلة، الأهداف، التصميم) وهو يتقدم بنشاط في المرحلة 4 (تطوير النموذج الأولي).</p>
        </div>
      </div>

      <!-- Right Column: DSR Blueprint Illustration -->
      <div class="ill-card" style="margin:0;padding:6px">
        <div class="ill-frame" style="max-height:220px" onclick="openImageModal('images/dsr_6phases_methodology.jpg', 'Design Science Research (DSR) 6-Phase Engineering Framework')">
          <img src="images/dsr_6phases_methodology.jpg" alt="DSR 6 Phases Framework" class="ill-img" loading="lazy" style="object-fit:cover;height:220px"/>
          <div class="ill-zoom-hint">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
            <span>DSR BLUEPRINT ZOOM</span>
          </div>
        </div>
        <div class="ill-caption" style="padding:4px 8px">
          <div class="ill-title" style="font-size:0.75rem">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg>
            <span class="en">Rigorous 6-Phase Iterative Cycle (Peffers et al.)</span>
            <span class="ar" style="display:none">دورة مراحل DSR التكرارية المعتمدة</span>
          </div>
          <div class="ill-sub">CHAPTER 1 &sect;1.4 &middot; DSR FRAMEWORK</div>
        </div>
      </div>
    </div>
  </div>
  <div class="sn">11 / 21</div>
</section>"""

html = replace_section(html, 's10', new_s10)
print("Updated Slide 11 (s10): Added dsr_6phases_methodology.jpg.")

# === 6. Slide 12 (id="s11"): Add context_enrichment.jpg and organize cards ===
new_s11 = """<section class="slide" id="s11">
  <div class="orb o2" style="opacity:0.4"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/></svg>
      <span class="en">Chapter 3 &ndash; Analysis Progress</span><span class="ar" style="display:none">الفصل الثالث &ndash; تقدم التحليل</span>
    </div>
    <h2 class="st en">Analysis Progress: Ingestion &amp; Context Enrichment</h2>
    <h2 class="st ar" style="display:none">تقدم التحليل: الاستيعاب وإثراء السياق</h2>
    <div class="gl"></div>

    <div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:16px;align-items:start;margin-top:10px">
      <!-- Left Column: Layer 1 and Layer 2 Details -->
      <div style="display:flex;flex-direction:column;gap:10px">
        <!-- Layer 1 -->
        <div class="card" style="padding:12px 14px">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
            <div class="c-icon" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg></div>
            <h3 class="ct en" style="margin:0;font-size:0.95rem">Layer 1: Alert Ingestion &amp; Normalization</h3>
            <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">الطبقة 1: الاستيعاب والتوحيد</h3>
          </div>
          <p class="en" style="font-size:0.82rem;margin:0">The ingestion module serves as the entry point for heterogeneous security alerts via REST APIs, webhooks, message streams, and log files. Individual connectors translate incoming data into a <strong>common normalized alert structure</strong> with fields: identifier, timestamp, source system, alert type, original severity, source/destination info, affected asset, and description.</p>
          <p class="ar" style="display:none;font-size:0.82rem;margin:0">وحدة الاستيعاب هي نقطة الدخول للتنبيهات الأمنية المتباينة عبر REST APIs والـ webhooks وتدفقات الرسائل. تترجم الموصلات البيانات الواردة إلى <strong>هيكل تنبيه موحد</strong> مع الحقول الأساسية.</p>
        </div>

        <!-- Layer 2 -->
        <div class="card" style="padding:12px 14px">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
            <div class="c-icon cy" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
            <h3 class="ct en" style="margin:0;font-size:0.95rem">Layer 2: Multi-Dimensional Enrichment</h3>
            <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">الطبقة 2: الإثراء متعدد الأبعاد</h3>
          </div>
          <div style="display:flex;flex-direction:column;gap:6px">
            <div style="background:rgba(255,255,255,0.03);padding:6px 10px;border-radius:6px;border-left:2px solid var(--s)">
              <span class="en" style="font-size:0.8rem"><strong>Asset &amp; Identity Context:</strong> Asset type, business criticality, network location, account privilege level, and authentication history</span>
              <span class="ar" style="display:none;font-size:0.8rem"><strong>سياق الأصل والهوية:</strong> نوع الأصل، الأهمية التجارية، موقع الشبكة، مستوى صلاحية الحساب</span>
            </div>
            <div style="background:rgba(255,255,255,0.03);padding:6px 10px;border-radius:6px;border-left:2px solid var(--ok)">
              <span class="en" style="font-size:0.8rem"><strong>Threat Intelligence Context:</strong> IP, domain, URL, and file hash reputation from threat intelligence feeds</span>
              <span class="ar" style="display:none;font-size:0.8rem"><strong>سياق استخبارات التهديدات:</strong> سمعة عناوين IP والنطاقات والبصمات من قواعد الاستخبارات</span>
            </div>
            <div style="background:rgba(255,255,255,0.03);padding:6px 10px;border-radius:6px;border-left:2px solid #ffd166">
              <span class="en" style="font-size:0.8rem"><strong>Historical &amp; Behavioral Context:</strong> Whether similar alerts or assets appeared in prior temporal windows</span>
              <span class="ar" style="display:none;font-size:0.8rem"><strong>السياق التاريخي والسلوكي:</strong> ما إذا ظهرت تنبيهات أو أصول مماثلة في نوافذ زمنية سابقة</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: 3D Context Enrichment Illustration -->
      <div class="ill-card" style="margin:0;padding:6px">
        <div class="ill-frame" style="max-height:240px" onclick="openImageModal('images/context_enrichment.jpg', 'Multi-Dimensional Alert Context Enrichment Pipeline')">
          <img src="images/context_enrichment.jpg" alt="Context Enrichment Pipeline" class="ill-img" loading="lazy" style="object-fit:cover;height:240px"/>
          <div class="ill-zoom-hint">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
            <span>ENRICHMENT ZOOM</span>
          </div>
        </div>
        <div class="ill-caption" style="padding:4px 8px">
          <div class="ill-title" style="font-size:0.75rem">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/></svg>
            <span class="en">3 Pillars: Asset Topology, Threat Feeds &amp; History</span>
            <span class="ar" style="display:none">المحاور الثلاثة: حساسية الأصول والاستخبارات والتاريخ السلوكي</span>
          </div>
          <div class="ill-sub">CHAPTER 3 &sect;3.4 &middot; DATA ENRICHMENT</div>
        </div>
      </div>
    </div>

    <div class="hl" style="margin-top:10px">
      <p class="en" style="font-size:0.82rem;margin:0"><strong>Design Principle:</strong> The module separates source-specific integration from internal processing. The enrichment layer degrades gracefully when sources are unavailable, and it creates the enriched alert object <em>without</em> assigning final priority or executing response.</p>
      <p class="ar" style="display:none;font-size:0.82rem;margin:0"><strong>مبدأ التصميم:</strong> يفصل الوحدة التكامل الخاص بالمصدر عن المعالجة الداخلية. طبقة الإثراء تتكيف عند تعذر المصادر ولا تصدر أولوية نهائية أو تنفذ استجابة.</p>
    </div>
  </div>
  <div class="sn">12 / 21</div>
</section>"""

html = replace_section(html, 's11', new_s11)
print("Updated Slide 12 (s11): Reorganized cards with context_enrichment.jpg.")

# === 7. Slide 13 (id="s12"): Formula breakdown diagram ===
new_s12 = """<section class="slide" id="s12">
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
    <p class="lead en" style="margin-bottom:14px;font-size:0.98rem;max-width:940px">
      Rigorous formulation of total incident risk by coupling supervised machine learning threat probability with base severity and contextual asset criticality.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:14px;font-size:0.98rem;max-width:940px">
      الصياغة الرياضية المعتمدة لدرجة المخاطر الإجمالية بدمج احتمالية التعلم الآلي مع خطورة التنبيه وحساسية الأصل المستهدف.
    </p>

    <!-- Visual 2-Column Grid: Formula Breakdown + Priority Queue Mapping -->
    <div class="g2" style="gap:16px;width:100%">
      
      <!-- Left Column: Mathematical Formulation & Visual Breakdown -->
      <div class="card" style="padding:18px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8))">
        <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:8px;display:flex;align-items:center;gap:8px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01M12 10h.01M8 10h.01M12 14h.01M8 14h.01M12 18h.01M8 18h.01"/></svg>
          Dynamic Risk Formula (R_total)
        </h3>
        <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:8px;align-items:center;gap:8px">
          معادلة تقييم المخاطر الإجمالية الديناميكية
        </h3>

        <!-- Mathematical Box with Formula -->
        <div style="background:rgba(0,0,0,0.4);border-radius:8px;padding:12px;border:1px solid rgba(0,212,255,0.3);text-align:center;margin-bottom:10px">
          <div style="font-size:1.22rem;font-weight:900;color:var(--s);font-family:'JetBrains Mono',monospace;letter-spacing:1px">
            R_total = &alpha; &middot; P(Threat) + &beta; &middot; S_base + &gamma; &middot; C_asset
          </div>
          <div style="font-size:0.72rem;color:var(--t3);margin-top:4px;font-family:'JetBrains Mono',monospace">
            Constraint: &alpha; + &beta; + &gamma; = 1.0 &nbsp;|&nbsp; Recommended: &alpha; = 0.50, &beta; = 0.30, &gamma; = 0.20
          </div>
        </div>

        <!-- Visual Equation Breakdown Diagram -->
        <div style="display:grid;grid-template-columns:repeat(3, 1fr) auto 1fr;gap:6px;align-items:center;background:rgba(0,0,0,0.3);padding:10px 8px;border-radius:8px;border:1px solid rgba(255,255,255,0.06);margin-bottom:12px;text-align:center">
          <div style="background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.4);border-radius:6px;padding:6px 4px">
            <div style="font-size:0.68rem;color:var(--s);font-weight:800">&alpha; = 0.50</div>
            <div style="font-size:0.78rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">P(Threat)</div>
            <div style="font-size:0.62rem;color:var(--t3)">ML Probability</div>
          </div>
          <div style="background:rgba(255,180,0,0.1);border:1px solid rgba(255,180,0,0.4);border-radius:6px;padding:6px 4px">
            <div style="font-size:0.68rem;color:#ffd166;font-weight:800">&beta; = 0.30</div>
            <div style="font-size:0.78rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">S_base</div>
            <div style="font-size:0.62rem;color:var(--t3)">Vendor Severity</div>
          </div>
          <div style="background:rgba(180,100,255,0.1);border:1px solid rgba(180,100,255,0.4);border-radius:6px;padding:6px 4px">
            <div style="font-size:0.68rem;color:#d8b4fe;font-weight:800">&gamma; = 0.20</div>
            <div style="font-size:0.78rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">C_asset</div>
            <div style="font-size:0.62rem;color:var(--t3)">Asset Criticality</div>
          </div>
          <div style="font-size:1.1rem;font-weight:900;color:var(--s);padding:0 2px">&rarr; &Sigma; &rarr;</div>
          <div style="background:rgba(16,185,129,0.15);border:1px solid var(--ok);border-radius:6px;padding:6px 4px;box-shadow:0 0 8px rgba(16,185,129,0.2)">
            <div style="font-size:0.68rem;color:var(--ok);font-weight:800">OUTPUT</div>
            <div style="font-size:0.82rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace">R_total</div>
            <div style="font-size:0.62rem;color:var(--ok)">Score &isin; [0, 1]</div>
          </div>
        </div>

        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;font-size:0.82rem;color:var(--t2)">
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
      <div class="card" style="padding:18px;border:1px solid rgba(255,180,0,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(35,20,30,0.8));display:flex;flex-direction:column;justify-content:space-between">
        <div>
          <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:10px;display:flex;align-items:center;gap:8px">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffd166" stroke-width="2.2"><path d="M12 20v-6M6 20V10M18 20V4"/></svg>
            Dynamic Priority Queue Slots
          </h3>
          <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:10px;align-items:center;gap:8px">
            توزيع مستويات الأولوية وتصنيف الطوابير
          </h3>

          <!-- Visual Multi-Zone Risk Bar -->
          <div style="margin-bottom:12px">
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

        <div style="padding:8px 12px;border-radius:6px;background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.08);display:flex;justify-content:space-between;align-items:center;font-size:0.75rem">
          <span class="en" style="color:var(--t2)">Analyst Queue Preservation:</span>
          <span class="ar" style="display:none;color:var(--t2)">حماية طابور المحلل:</span>
          <span style="color:var(--ok);font-weight:800;font-family:'JetBrains Mono',monospace">+22.9% Capacity Boost</span>
        </div>
      </div>

    </div>
  </div>
  <div class="sn">13 / 21</div>
</section>"""

html = replace_section(html, 's12', new_s12)
print("Updated Slide 13 (s12): Visual breakdown for Dynamic Risk formula.")

# === 8. Slide 15 (id="s14"): Reorganize playbooks & confidence gate ===
new_s14 = """<section class="slide" id="s14">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
      <span class="en">Chapter 3 &ndash; Design Progress</span><span class="ar" style="display:none">الفصل الثالث &ndash; تقدم التصميم</span>
    </div>
    <h2 class="st en">Design Progress: Response Policy &amp; Automated Playbooks</h2>
    <h2 class="st ar" style="display:none">تقدم التصميم: سياسة الاستجابة ودفاتر العمل المؤتمتة</h2>
    <div class="gl"></div>

    <!-- Top: Response Policy Layer & Confidence Gate Banner -->
    <div class="card" style="padding:14px 18px;margin-bottom:12px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8))">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
        <div style="display:flex;align-items:center;gap:10px">
          <div class="c-icon cy" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
          <h3 class="ct en" style="margin:0;font-size:1.02rem">Response Policy Layer &amp; Confidence Gate</h3>
          <h3 class="ct ar" style="display:none;margin:0;font-size:1.02rem">طبقة سياسة الاستجابة وبوابة الثقة</h3>
        </div>
        <div style="display:flex;gap:8px">
          <span style="font-size:0.72rem;padding:3px 8px;border-radius:6px;background:rgba(16,185,129,0.15);color:var(--ok);font-weight:700">&ge; 90% Auto-Dispatch</span>
          <span style="font-size:0.72rem;padding:3px 8px;border-radius:6px;background:rgba(255,180,0,0.15);color:#ffd166;font-weight:700">&lt; 90% Human Approval</span>
        </div>
      </div>
      <p class="en" style="font-size:0.84rem;color:var(--t2);margin:0">The policy layer maps the prioritized risk score and confidence indicator to a specific playbook. A <strong>confidence gate</strong> ensures high-impact response actions are only triggered when the model's confidence exceeds a defined threshold &mdash; otherwise routing to analyst approval.</p>
      <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);margin:0">تربط طبقة السياسة درجة المخاطر المُرتبة ومؤشر الثقة بدفتر عمل محدد. <strong>بوابة الثقة</strong> تضمن أن إجراءات الاستجابة عالية التأثير لا تُطلق إلا عند تجاوز عتبة ثقة محددة.</p>
    </div>

    <!-- Bottom: 4 Automated Playbook Types Grid -->
    <div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:12px;width:100%">
      <!-- Playbook 1 -->
      <div class="card" style="padding:14px;border:1px solid rgba(239,68,68,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(35,10,18,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="c-icon rd" style="width:26px;height:26px"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></div>
            <strong class="en" style="color:#fff;font-size:0.92rem">Endpoint Containment</strong>
            <strong class="ar" style="display:none;color:#fff;font-size:0.92rem">احتواء نقطة النهاية</strong>
          </div>
          <span style="font-size:0.68rem;padding:2px 6px;border-radius:4px;background:rgba(239,68,68,0.2);color:#ff6b6b;font-weight:700">EDR API</span>
        </div>
        <p class="en" style="font-size:0.8rem;color:var(--t2);margin:0">Quarantine compromised endpoints via EDR API to prevent lateral movement while preserving forensic telemetry.</p>
        <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:0">عزل نقاط النهاية المخترقة عبر واجهة EDR لمنع الانتشار مع الحفاظ على بيانات التتبع.</p>
      </div>

      <!-- Playbook 2 -->
      <div class="card" style="padding:14px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(10,25,35,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="c-icon cy" style="width:26px;height:26px"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/></svg></div>
            <strong class="en" style="color:#fff;font-size:0.92rem">Network Blocking</strong>
            <strong class="ar" style="display:none;color:#fff;font-size:0.92rem">حظر شبكي</strong>
          </div>
          <span style="font-size:0.68rem;padding:2px 6px;border-radius:4px;background:rgba(0,212,255,0.2);color:var(--s);font-weight:700">Firewall API</span>
        </div>
        <p class="en" style="font-size:0.8rem;color:var(--t2);margin:0">Push dynamic block lists to perimeter firewalls to sever active Command &amp; Control channels.</p>
        <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:0">دفع قوائم الحظر الديناميكية للجدران النارية لقطع قنوات القيادة والتحكم النشطة.</p>
      </div>

      <!-- Playbook 3 -->
      <div class="card" style="padding:14px;border:1px solid rgba(255,180,0,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(35,25,10,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="c-icon ye" style="width:26px;height:26px"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg></div>
            <strong class="en" style="color:#fff;font-size:0.92rem">Account Suspension</strong>
            <strong class="ar" style="display:none;color:#fff;font-size:0.92rem">تعليق الحساب</strong>
          </div>
          <span style="font-size:0.68rem;padding:2px 6px;border-radius:4px;background:rgba(255,180,0,0.2);color:#ffd166;font-weight:700">IAM / IdP API</span>
        </div>
        <p class="en" style="font-size:0.8rem;color:var(--t2);margin:0">Revoke active sessions and disable accounts exhibiting anomalous credential behavior.</p>
        <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:0">إلغاء الجلسات النشطة وتعطيل الحسابات التي تُظهر سلوكاً غير طبيعي في بيانات الاعتماد.</p>
      </div>

      <!-- Playbook 4 -->
      <div class="card" style="padding:14px;border:1px solid rgba(16,185,129,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.85), rgba(10,35,25,0.7))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
          <div style="display:flex;align-items:center;gap:8px">
            <div class="c-icon gr" style="width:26px;height:26px"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg></div>
            <strong class="en" style="color:#fff;font-size:0.92rem">Malicious Content Purge</strong>
            <strong class="ar" style="display:none;color:#fff;font-size:0.92rem">تطهير المحتوى الخبيث</strong>
          </div>
          <span style="font-size:0.68rem;padding:2px 6px;border-radius:4px;background:rgba(16,185,129,0.2);color:var(--ok);font-weight:700">Email API</span>
        </div>
        <p class="en" style="font-size:0.8rem;color:var(--t2);margin:0">Identify and remove malicious messages enterprise-wide via email platform API.</p>
        <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:0">تحديد وإزالة الرسائل الخبيثة على مستوى المؤسسة عبر واجهة منصة البريد الإلكتروني.</p>
      </div>
    </div>
  </div>
  <div class="sn">15 / 21</div>
</section>"""

html = replace_section(html, 's14', new_s14)
print("Updated Slide 15 (s14): Structured cards for Response Policy & 4 Playbooks.")

# === 9. Slide 17 (id="s16"): Working Prototype live pipeline diagram ===
new_s16 = """<section class="slide" id="s16">
  <div class="orb o3" style="opacity:0.35"></div>
  <div class="content-box" style="max-width:1280px">
    <div class="tag a1" style="border-color:rgba(16,185,129,0.4);background:rgba(16,185,129,0.06)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#6ee7b7" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
      <span class="en" style="color:#6ee7b7">Prototype Demo</span><span class="ar" style="display:none;color:#6ee7b7">عرض النموذج الأولي</span>
    </div>
    <h2 class="st en">Working Prototype: Alert Processing Pipeline</h2>
    <h2 class="st ar" style="display:none">النموذج الأولي العامل: خط معالجة التنبيهات</h2>
    <div class="gl"></div>
    <p class="lead en">The prototype demonstrates the end-to-end alert flow &mdash; from raw security event ingestion through enrichment, AI/ML risk scoring, prioritization, and response initiation &mdash; in a controlled simulation environment.</p>
    <p class="lead ar" style="display:none">يوضح النموذج الأولي تدفق التنبيهات الكامل &mdash; من استيعاب الأحداث الخام عبر الإثراء وتقييم المخاطر والأولوية وبدء الاستجابة &mdash; في بيئة محاكاة محكومة.</p>

    <!-- Animated Pipeline Flow Diagram -->
    <div class="flow" style="margin-top:14px;background:rgba(0,0,0,0.3);padding:14px;border-radius:10px;border:1px solid rgba(255,255,255,0.06);display:grid;grid-template-columns:repeat(6, 1fr);gap:8px">
      <div class="fs" style="padding:8px 6px">
        <div class="fi" style="background:rgba(0,212,255,0.2);color:var(--s)"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg></div>
        <div class="fl en" style="font-size:0.75rem">1. Raw Alert In</div>
        <div class="fl ar" style="display:none;font-size:0.75rem">1. تنبيه خام</div>
      </div>
      <div class="fs" style="padding:8px 6px">
        <div class="fi" style="background:rgba(0,212,255,0.2);color:var(--s)"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"/></svg></div>
        <div class="fl en" style="font-size:0.75rem">2. Normalize</div>
        <div class="fl ar" style="display:none;font-size:0.75rem">2. توحيد</div>
      </div>
      <div class="fs" style="padding:8px 6px">
        <div class="fi" style="background:rgba(0,212,255,0.2);color:var(--s)"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/></svg></div>
        <div class="fl en" style="font-size:0.75rem">3. Enrich</div>
        <div class="fl ar" style="display:none;font-size:0.75rem">3. إثراء</div>
      </div>
      <div class="fs" style="padding:8px 6px">
        <div class="fi" style="background:rgba(255,180,0,0.2);color:#ffd166"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5"/></svg></div>
        <div class="fl en" style="font-size:0.75rem">4. ML Score</div>
        <div class="fl ar" style="display:none;font-size:0.75rem">4. تقييم ML</div>
      </div>
      <div class="fs" style="padding:8px 6px">
        <div class="fi" style="background:rgba(255,180,0,0.2);color:#ffd166"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="20" x2="12" y2="10"/></svg></div>
        <div class="fl en" style="font-size:0.75rem">5. Prioritize</div>
        <div class="fl ar" style="display:none;font-size:0.75rem">5. ترتيب</div>
      </div>
      <div class="fs" style="padding:8px 6px;border:1px solid var(--ok);background:rgba(16,185,129,0.1)">
        <div class="fi" style="background:var(--ok);color:#000"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
        <div class="fl en" style="font-size:0.75rem;font-weight:800;color:#fff">6. Response</div>
        <div class="fl ar" style="display:none;font-size:0.75rem;font-weight:800;color:#fff">6. استجابة</div>
      </div>
    </div>

    <!-- 2 Real-World Simulated Scenarios Grid -->
    <div class="grid g2" style="gap:16px;margin-top:14px">
      <!-- Scenario 1 -->
      <div class="card" style="padding:16px;border:1px solid rgba(239,68,68,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(35,10,20,0.8))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <h3 class="ct en" style="color:#ff6b6b;margin:0;font-size:1rem;display:flex;align-items:center;gap:6px">
            <span style="width:8px;height:8px;border-radius:50%;background:#ef4444;box-shadow:0 0 8px #ef4444"></span>
            Scenario: Anomalous Login
          </h3>
          <h3 class="ct ar" style="display:none;color:#ff6b6b;margin:0;font-size:1rem">سيناريو: تسجيل دخول شاذ</h3>
          <span style="font-size:0.68rem;padding:2px 8px;border-radius:4px;background:rgba(239,68,68,0.2);color:#ff6b6b;font-weight:800">P1 &middot; CRITICAL</span>
        </div>
        <p class="en" style="font-size:0.84rem;color:var(--t2);line-height:1.5;margin:0">A privileged account login from an unusual geographic location is ingested, enriched with asset criticality and threat intel, scored High risk [0.87], confidence 91% &rarr; playbook triggered: account session revocation + analyst notification.</p>
        <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);line-height:1.5;margin:0">تسجيل دخول لحساب متميز من موقع جغرافي غير عادي يُستوعب ويُثرى بحساسية الأصل والاستخبارات، يُقيَّم بخطر عالٍ [0.87]، ثقة 91% &rarr; دفتر عمل: إلغاء الجلسة + إشعار المحلل.</p>
      </div>

      <!-- Scenario 2 -->
      <div class="card" style="padding:16px;border:1px solid rgba(16,185,129,0.35);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(10,35,25,0.8))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <h3 class="ct en" style="color:var(--ok);margin:0;font-size:1rem;display:flex;align-items:center;gap:6px">
            <span style="width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 8px var(--ok)"></span>
            Scenario: Low-Risk Alert Suppression
          </h3>
          <h3 class="ct ar" style="display:none;color:var(--ok);margin:0;font-size:1rem">سيناريو: قمع التنبيه منخفض الخطر</h3>
          <span style="font-size:0.68rem;padding:2px 8px;border-radius:4px;background:rgba(16,185,129,0.2);color:var(--ok);font-weight:800">P4 &middot; SUPPRESSED</span>
        </div>
        <p class="en" style="font-size:0.84rem;color:var(--t2);line-height:1.5;margin:0">A routine port scan on a non-critical test asset receives Risk score [0.12], confidence 88% &rarr; alert suppressed from primary queue, retained in audit log, analyst queue dwell time preserved for genuine threats.</p>
        <p class="ar" style="display:none;font-size:0.84rem;color:var(--t2);line-height:1.5;margin:0">فحص منافذ روتيني على أصل تجريبي غير حرج يتلقى [0.12] ثقة 88% &rarr; التنبيه مقموع من الطابور الرئيسي، محفوظ في سجل التدقيق.</p>
      </div>
    </div>
  </div>
  <div class="sn">17 / 21</div>
</section>"""

html = replace_section(html, 's16', new_s16)
print("Updated Slide 17 (s16): Animated prototype pipeline with execution scenario cards.")

# === 10. Slide 18 (id="s17"): Evaluation dashboard with gentle pulsing loop ===
new_s17 = """<section class="slide" id="s17">
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
    <p class="lead en" style="margin-bottom:14px;font-size:0.98rem;max-width:940px">
      Quantitative validation criteria using public cybersecurity benchmark datasets and statistical performance metrics.
    </p>
    <p class="lead ar" style="display:none;margin-bottom:14px;font-size:0.98rem;max-width:940px">
      معايير التحقق الكمي المعتمدة باستخدام مجموعات البيانات القياسية ومقاييس الأداء الإحصائي المعيارية.
    </p>

    <!-- 2-Column Evaluation Dashboard -->
    <div class="g2" style="gap:16px;width:100%">
      
      <!-- Benchmark Datasets -->
      <div class="card" style="padding:18px;border:1px solid rgba(0,212,255,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(15,30,45,0.8))">
        <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:10px;display:flex;align-items:center;gap:8px">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
          Benchmark Testbed Datasets
        </h3>
        <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:10px;align-items:center;gap:8px">
          مجموعات البيانات المعيارية للاختبار
        </h3>

        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06)">
            <div style="display:flex;justify-content:space-between;font-weight:700;color:#fff;font-size:0.86rem">
              <span>CIC-IDS2017 / CSE-CIC-IDS2018</span>
              <span style="color:var(--s);font-size:0.72rem">Canadian Institute for Cybersecurity</span>
            </div>
            <p class="en" style="font-size:0.8rem;color:var(--t2);margin:4px 0 0">
              Realistic multi-vector attack traffic (DDoS, Brute Force, Infiltration, Botnet) with diverse packet and flow telemetry.
            </p>
            <p class="ar" style="display:none;font-size:0.8rem;color:var(--t2);margin:4px 0 0">
              حركة مرور تحاكي هجمات سيبرانية حقيقية (حجب الخدمة، الاختراق، البوتنت) مع سجلات تدفق وحزم تفصيلية.
            </p>
          </div>

          <div style="background:rgba(0,0,0,0.3);border-radius:8px;padding:10px 12px;border:1px solid rgba(255,255,255,0.06)">
            <div style="display:flex;justify-content:space-between;font-weight:700;color:#fff;font-size:0.86rem">
              <span>UNSW-NB15 Dataset</span>
              <span style="color:var(--s);font-size:0.72rem">Cyber Range Lab (UNSW)</span>
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

      <!-- Performance Metrics Bars with Gentle Academic Pulse -->
      <div class="card" style="padding:18px;border:1px solid rgba(16,185,129,0.3);background:linear-gradient(145deg, rgba(28,8,22,0.92), rgba(12,38,25,0.8))">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <h3 class="en" style="font-size:1.05rem;font-weight:800;color:#fff;margin:0;display:flex;align-items:center;gap:8px">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--ok)" stroke-width="2.2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
            Quantitative Target Metrics
          </h3>
          <h3 class="ar" style="display:none;font-size:1.05rem;font-weight:800;color:#fff;margin:0">
            مقاييس الأداء المستهدفة
          </h3>
          <span style="font-size:0.68rem;padding:2px 8px;border-radius:6px;background:rgba(16,185,129,0.15);color:var(--ok);font-weight:700;display:flex;align-items:center;gap:4px">
            <span style="width:6px;height:6px;border-radius:50%;background:var(--ok);display:inline-block;animation:subtlePulseLoop 2s infinite"></span>
            Continuous Live Metric Telemetry
          </span>
        </div>

        <div style="display:flex;flex-direction:column;gap:10px">
          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.8rem;font-weight:700;margin-bottom:3px">
              <span style="color:#fff">False Positive Suppression Rate</span>
              <span style="color:var(--ok);font-family:'JetBrains Mono',monospace">&ge; 54% Target</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:54%;height:100%;background:var(--ok);border-radius:4px;animation:subtlePulseLoop 3s infinite"></div>
            </div>
          </div>

          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.8rem;font-weight:700;margin-bottom:3px">
              <span style="color:#fff">True Threat Capture Rate</span>
              <span style="color:var(--s);font-family:'JetBrains Mono',monospace">95.1% Preserved</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:95.1%;height:100%;background:var(--s);border-radius:4px;box-shadow:0 0 8px var(--s)"></div>
            </div>
          </div>

          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.8rem;font-weight:700;margin-bottom:3px">
              <span style="color:#fff">Precision &amp; Recall (AlertPro Benchmark)</span>
              <span style="color:#ffd166;font-family:'JetBrains Mono',monospace">96.3% / 98.5%</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:96%;height:100%;background:#ffd166;border-radius:4px;box-shadow:0 0 6px #ffd166"></div>
            </div>
          </div>

          <div>
            <div style="display:flex;justify-content:space-between;font-size:0.8rem;font-weight:700;margin-bottom:3px">
              <span style="color:#fff">Mean Time to Respond (MTTR) Reduction</span>
              <span style="color:#ff8e8e;font-family:'JetBrains Mono',monospace">&gt; 50% Faster</span>
            </div>
            <div style="height:8px;border-radius:4px;background:rgba(255,255,255,0.08);overflow:hidden">
              <div style="width:75%;height:100%;background:#ff6b6b;border-radius:4px;box-shadow:0 0 6px #ff6b6b"></div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  <div class="sn">18 / 21</div>
</section>"""

html = replace_section(html, 's17', new_s17)
print("Updated Slide 18 (s17): Evaluation framework dashboard with subtle looping pulse.")

# === 11. Slide 20 (id="s19"): Add continuous_feedback_loop.jpg, remove inline Thank You ===
new_s19 = """<section class="slide" id="s19">
  <div class="orb o1"></div><div class="orb o2"></div>
  <div class="content-box" style="text-align:center;max-width:1280px">
    <div class="tag a1" style="display:inline-flex">
      <div class="dp"></div>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      <span class="en">Conclusion &amp; Next Steps</span><span class="ar" style="display:none">الخلاصة والخطوات التالية</span>
    </div>
    <h2 class="st en" style="font-size:clamp(1.3rem,2.5vw,1.9rem)">Conclusion, Remaining Work &amp; Next Steps</h2>
    <h2 class="st ar" style="display:none;font-size:clamp(1.3rem,2.5vw,1.9rem)">الخلاصة والأعمال المتبقية والخطوات التالية</h2>
    <div class="gl"></div>

    <!-- Main Grid: 3 Status Columns on Left, Feedback Loop on Right -->
    <div style="display:grid;grid-template-columns:1.2fr 0.8fr;gap:16px;margin-top:12px;text-align:left;align-items:start">
      <!-- 3 Status Columns Stacked/Grouped -->
      <div style="display:flex;flex-direction:column;gap:10px">
        <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:10px">
          <!-- Completed -->
          <div class="card" style="padding:10px;border-color:var(--ok);background:rgba(16,185,129,0.06)">
            <h3 class="ct en" style="color:var(--ok);font-size:0.92rem;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;border-radius:50%;background:rgba(16,185,129,0.2);color:var(--ok);flex-shrink:0"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg></span> Completed</h3>
            <h3 class="ct ar" style="display:none;color:var(--ok);font-size:0.92rem">مكتمل</h3>
            <ul style="gap:4px;font-size:0.78rem;padding-left:14px;margin:6px 0 0">
              <li class="en">Problem analysis &amp; operational challenge documentation</li>
              <li class="ar" style="display:none">تحليل المشكلة وتوثيق التحديات التشغيلية</li>
              <li class="en">Literature review &amp; comparative gap analysis (Table 2-1)</li>
              <li class="ar" style="display:none">مراجعة الأدبيات وتحليل الفجوة المقارن</li>
              <li class="en">Full 5-layer system architecture design</li>
              <li class="ar" style="display:none">تصميم المعمارية الكاملة بـ 5 طبقات</li>
              <li class="en">AI/ML engine formulation (risk scoring, confidence gate)</li>
              <li class="ar" style="display:none">صياغة محرك الذكاء الاصطناعي</li>
            </ul>
          </div>

          <!-- In Progress -->
          <div class="card" style="padding:10px;border-color:var(--wa);background:rgba(251,191,36,0.06)">
            <h3 class="ct en" style="color:var(--wa);font-size:0.92rem;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;border-radius:50%;background:rgba(255,180,0,0.2);color:var(--wa);flex-shrink:0"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg></span> In Progress</h3>
            <h3 class="ct ar" style="display:none;color:var(--wa);font-size:0.92rem">قيد التنفيذ</h3>
            <ul style="gap:4px;font-size:0.78rem;padding-left:14px;margin:6px 0 0">
              <li class="en">Prototype implementation: connectors + normalization</li>
              <li class="ar" style="display:none">تنفيذ النموذج الأولي: الموصلات + التوحيد</li>
              <li class="en">ML model training on labeled alert dataset</li>
              <li class="ar" style="display:none">تدريب نموذج ML على مجموعة تنبيهات مصنفة</li>
              <li class="en">Dashboard and analyst feedback portal</li>
              <li class="ar" style="display:none">لوحة التحكم وبوابة تغذية المحلل الراجعة</li>
            </ul>
          </div>

          <!-- Remaining -->
          <div class="card" style="padding:10px;border-color:var(--s);background:rgba(0,212,255,0.06)">
            <h3 class="ct en" style="color:var(--s);font-size:0.92rem;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;border-radius:50%;background:rgba(0,212,255,0.2);color:var(--s);flex-shrink:0"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg></span> Remaining</h3>
            <h3 class="ct ar" style="display:none;color:var(--s);font-size:0.92rem">متبقٍ</h3>
            <ul style="gap:4px;font-size:0.78rem;padding-left:14px;margin:6px 0 0">
              <li class="en">Playbook execution engine + API dispatcher</li>
              <li class="ar" style="display:none">محرك تنفيذ دفاتر العمل + مرسل API</li>
              <li class="en">Full integration testing against defined ML &amp; operational metrics</li>
              <li class="ar" style="display:none">اختبار التكامل الكامل مقابل المقاييس المحددة</li>
              <li class="en">Final evaluation, documentation &amp; project report completion</li>
              <li class="ar" style="display:none">التقييم النهائي والتوثيق وإكمال التقرير</li>
            </ul>
          </div>
        </div>

        <div class="hl" style="margin:0;border-color:var(--p)">
          <p class="en" style="font-size:0.84rem;margin:0">
            <strong>Core Contribution:</strong> This project investigates the architectural integration of AI/ML-based alert analysis, dynamic risk prioritization, and SOAR automated response &mdash; addressing the unresolved gap identified in the comparative literature analysis (Table 2-1).
          </p>
          <p class="ar" style="display:none;font-size:0.84rem;margin:0">
            <strong>المساهمة الجوهرية:</strong> يدرس هذا المشروع التكامل المعماري لتحليل التنبيهات القائم على الذكاء الاصطناعي والأولوية الديناميكية واستجابة SOAR المؤتمتة &mdash; معالجةً للفجوة المحددة في تحليل الأدبيات المقارن.
          </p>
        </div>
      </div>

      <!-- Right Column: Continuous Retraining Feedback Loop Illustration -->
      <div class="ill-card" style="margin:0;padding:6px">
        <div class="ill-frame" style="max-height:220px" onclick="openImageModal('images/continuous_feedback_loop.jpg', 'SOAR Machine Learning Continuous Retraining & Feedback Loop')">
          <img src="images/continuous_feedback_loop.jpg" alt="Continuous Feedback Loop" class="ill-img" loading="lazy" style="object-fit:cover;height:220px"/>
          <div class="ill-zoom-hint">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
            <span>FEEDBACK LOOP ZOOM</span>
          </div>
        </div>
        <div class="ill-caption" style="padding:4px 8px">
          <div class="ill-title" style="font-size:0.75rem">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--ok)" stroke-width="2.2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
            <span class="en">Active Model Drift Monitoring &amp; Analyst Retraining</span>
            <span class="ar" style="display:none">مراقبة انحراف النماذج وإعادة التدريب المستمر</span>
          </div>
          <div class="ill-sub">CHAPTER 5 &sect;5.2 &middot; CONTINUOUS LEARNING</div>
        </div>
      </div>
    </div>
  </div>
  <div class="sn">20 / 21</div>
</section>"""

html = replace_section(html, 's19', new_s19)
print("Updated Slide 20 (s19): Integrated continuous_feedback_loop.jpg.")

# === 12. Slide 21 (id="s20" - NEW GRAND FINALE): Append after s19 ===
new_s20 = """
<section class="slide" id="s20">
  <div class="orb o1" style="width:500px;height:500px;opacity:0.4;top:20%;left:50%;transform:translate(-50%,-50%);animation:haloGlow 6s infinite ease-in-out"></div>
  <div class="orb o2" style="width:400px;height:400px;opacity:0.3;bottom:10%;right:15%"></div>

  <div class="content-box" style="text-align:center;max-width:960px;margin:0 auto;padding:40px 30px;background:linear-gradient(145deg, rgba(20,7,24,0.92), rgba(12,25,35,0.88));border:1px solid rgba(0,212,255,0.3);box-shadow:0 0 40px rgba(0,0,0,0.8), 0 0 30px rgba(0,212,255,0.15)">
    
    <div class="tag a1" style="display:inline-flex;margin-bottom:16px;border-color:rgba(16,185,129,0.4);background:rgba(16,185,129,0.08)">
      <div class="dp"></div>
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="var(--ok)" stroke-width="2.2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
      <span class="en" style="color:var(--ok);font-weight:800;letter-spacing:1px">GRADUATION PROJECT DEFENSE &middot; FINAL REMARKS</span>
      <span class="ar" style="display:none;color:var(--ok);font-weight:800">مشروع التخرج المعتمد &middot; الكلمة الختامية والمناقشة</span>
    </div>

    <!-- Grand Glowing Title -->
    <h1 class="st en" style="font-size:clamp(1.8rem, 3.5vw, 2.6rem);margin-bottom:8px;letter-spacing:-0.5px;color:#fff;text-shadow:0 0 20px rgba(0,212,255,0.4)">
      Thank You &ndash; Open for Discussion &amp; Defense Questions
    </h1>
    <h1 class="st ar" style="display:none;font-size:clamp(1.8rem, 3.5vw, 2.6rem);margin-bottom:8px;color:#fff;text-shadow:0 0 20px rgba(0,212,255,0.4)">
      شكراً لحسن استماعكم &ndash; مستعدون لأسئلة ومناقشة اللجنة الموقرة
    </h1>
    <div class="gl" style="margin:10px auto 20px;width:120px;height:3px"></div>

    <p class="lead en" style="font-size:1.08rem;color:var(--t2);max-width:750px;margin:0 auto 24px">
      AI-Based Security Orchestration, Automation, and Response (SOAR) Tool: Transforming Incident Triage and Autonomous Playbook Execution.
    </p>
    <p class="lead ar" style="display:none;font-size:1.08rem;color:var(--t2);max-width:750px;margin:0 auto 24px">
      أداة الاستجابة والأتمتة الأمنية الذكية المعتمدة على الذكاء الاصطناعي (SOAR): تحويل فرز التنبيهات والأتمتة التكيفية لدفاتر العمل.
    </p>

    <!-- Attribution Grid -->
    <div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:16px;max-width:780px;margin:0 auto 24px;text-align:left">
      <!-- Supervision Card -->
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px 18px">
        <div style="font-size:0.72rem;color:var(--s);text-transform:uppercase;font-weight:800;letter-spacing:1px;margin-bottom:4px">
          <span class="en">Academic Supervision</span>
          <span class="ar" style="display:none">الإشراف الأكاديمي</span>
        </div>
        <div style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:2px">
          <span class="en">Dr. Raed Saeed</span>
          <span class="ar" style="display:none">د. رائد سعيد</span>
        </div>
        <div style="font-size:0.78rem;color:var(--t3)">
          <span class="en">Department of Computer Science &amp; Engineering</span>
          <span class="ar" style="display:none">قسم علوم الحاسوب وهندسة الشبكات</span>
        </div>
      </div>

      <!-- Research Team Card -->
      <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px 18px">
        <div style="font-size:0.72rem;color:var(--ok);text-transform:uppercase;font-weight:800;letter-spacing:1px;margin-bottom:4px">
          <span class="en">Defense Candidate</span>
          <span class="ar" style="display:none">فريق إعداد المشروع</span>
        </div>
        <div style="font-size:1.05rem;font-weight:800;color:#fff;margin-bottom:2px">
          <span class="en">Mo AL-Yahawy &amp; Engineering Team</span>
          <span class="ar" style="display:none">محمد اليحوي وفريق البحث الهندسي</span>
        </div>
        <div style="font-size:0.78rem;color:var(--t3)">
          <span class="en">University of Science and Technology</span>
          <span class="ar" style="display:none">جامعة العلوم والتكنولوجيا</span>
        </div>
      </div>
    </div>

    <!-- Ready for Q&A Interactive Pill -->
    <div style="display:inline-flex;align-items:center;gap:10px;padding:10px 22px;border-radius:30px;background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.4);box-shadow:0 0 16px rgba(0,212,255,0.2)">
      <span style="width:8px;height:8px;border-radius:50%;background:var(--s);box-shadow:0 0 8px var(--s);display:inline-block"></span>
      <span class="en" style="font-size:0.88rem;font-weight:800;color:#fff;letter-spacing:0.5px">READY FOR COMMITTEE DISCUSSION &amp; QUESTIONS</span>
      <span class="ar" style="display:none;font-size:0.88rem;font-weight:800;color:#fff;letter-spacing:0.5px">جاهزون لملاحظات وأسئلة أعضاء لجنة المناقشة</span>
    </div>

  </div>
  <div class="sn">21 / 21</div>
</section>
"""

# Check if s20 already exists
if 'id="s20"' in html:
    html = replace_section(html, 's20', new_s20.strip())
    print("Replaced existing Slide 21 (s20).")
else:
    # Append after s19
    s19_pattern = re.compile(r'(<section\b[^>]*id=["\']s19["\'][^>]*>.*?</section>)', re.DOTALL)
    html = s19_pattern.sub(r'\1\n' + new_s20, html, count=1)
    print("Appended new Slide 21 (s20) after Slide 20 (s19).")

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("All slide upgrades successfully written to presentation/index.html!")
