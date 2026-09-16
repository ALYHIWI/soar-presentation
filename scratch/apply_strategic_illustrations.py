# -*- coding: utf-8 -*-
import re

with open('presentation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS to inject before </style>
custom_css = """
/* ================= LUXURY ILLUSTRATIVE CARDS & LIGHTBOX (DOUBLE-BEZEL) ================= */
.split-ill-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 18px;
  width: 100%;
  align-items: stretch;
  margin-top: 6px;
}

[dir="rtl"] .split-ill-grid {
  direction: rtl;
}

.ill-card {
  position: relative;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 8px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(16px);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  height: 100%;
  min-height: 280px;
}

.ill-card:hover {
  border-color: rgba(0, 212, 255, 0.45);
  box-shadow: 0 12px 36px rgba(0, 212, 255, 0.2);
  transform: translateY(-2px);
}

.ill-frame {
  position: relative;
  width: 100%;
  flex: 1;
  min-height: 200px;
  max-height: 380px;
  border-radius: 12px;
  overflow: hidden;
  background: #080309;
  cursor: zoom-in;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.ill-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
}

.ill-frame:hover .ill-img {
  transform: scale(1.035);
}

.ill-zoom-hint {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 8px;
  padding: 4px 9px;
  color: #fff;
  font-size: 0.7rem;
  font-family: 'JetBrains Mono', monospace;
  display: flex;
  align-items: center;
  gap: 5px;
  pointer-events: none;
  opacity: 0.85;
  transition: all 0.2s;
  z-index: 2;
}

[dir="rtl"] .ill-zoom-hint {
  right: auto;
  left: 10px;
}

.ill-frame:hover .ill-zoom-hint {
  opacity: 1;
  background: rgba(0, 212, 255, 0.35);
  border-color: var(--s);
  color: #fff;
}

.ill-caption {
  padding: 8px 8px 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
}

.ill-title {
  font-size: 0.82rem;
  font-weight: 800;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 6px;
}

.ill-sub {
  font-size: 0.72rem;
  color: var(--s);
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  white-space: nowrap;
}

/* Modal Lightbox */
#imgModal {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 10000;
  background: rgba(0, 0, 0, 0.88);
  backdrop-filter: blur(20px);
  padding: 24px;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

#imgModal.active {
  display: flex;
  animation: modalFadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes modalFadeIn {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}

.modal-content-wrap {
  position: relative;
  max-width: 92vw;
  max-height: 88vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.modal-img {
  max-width: 92vw;
  max-height: 80vh;
  border-radius: 14px;
  border: 1px solid rgba(0, 212, 255, 0.4);
  box-shadow: 0 0 50px rgba(0, 0, 0, 0.95), 0 0 30px rgba(0, 212, 255, 0.3);
  object-fit: contain;
}

.modal-caption {
  margin-top: 12px;
  font-size: 0.95rem;
  font-weight: 700;
  color: #fff;
  text-align: center;
  background: rgba(20, 8, 25, 0.85);
  padding: 6px 24px;
  border-radius: 100px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  letter-spacing: 0.5px;
}

.modal-close-btn {
  position: absolute;
  top: -14px;
  right: -14px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(239, 68, 68, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.5);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(0,0,0,0.6);
  transition: transform 0.2s, background 0.2s;
  z-index: 10;
}
.modal-close-btn:hover {
  transform: scale(1.12);
  background: #ef4444;
}
"""

if '/* ================= LUXURY ILLUSTRATIVE CARDS & LIGHTBOX' not in html:
    html = html.replace('</style>', f'{custom_css}\n</style>')

# ==============================================================================
# SLIDE 02 (s1): BACKGROUND - THE MODERN SOC LANDSCAPE
# ==============================================================================
s1_new = """<!-- ================= S02: BACKGROUND / CONTEXT ================= -->
<section class="slide" id="s1">
 <div class="orb o2" style="opacity:0.35"></div>
 <div class="content-box">
 <div class="tag a1">
 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/></svg>
 <span class="en">Chapter 1 &ndash; Background</span><span class="ar" style="display:none">الفصل الأول &ndash; الخلفية</span>
 </div>
 <h2 class="st en">Background: The Modern SOC Landscape</h2>
 <h2 class="st ar" style="display:none">الخلفية: مشهد مراكز العمليات الأمنية الحديثة</h2>
 <div class="gl"></div>
 <p class="lead en">A Security Operations Center (SOC) centralizes cyber threat monitoring, detection, and incident response — but faces acute operational strain from massive log volumes and heterogeneous data schemas.</p>
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
       <p class="en" style="font-size:0.82rem;margin:0">Junior analysts manually investigate alerts by pivoting across disparate tools to evaluate each alert — creating an acute operational bottleneck.</p>
       <p class="ar" style="display:none;font-size:0.82rem;margin:0">المحللون المبتدئون يجمعون الأدلة يدوياً عبر التنقل بين أدوات منفصلة لتقييم كل تنبيه، مما يولد عنق زجاجة تشغيلي.</p>
     </div>

     <div class="srow" style="margin-top:2px">
       <div class="sb"><div class="snum">100 GB</div><div class="slbl en">Daily Influx</div><div class="slbl ar" style="display:none">سجلات يومية</div></div>
       <div class="sb"><div class="snum">Multi-Vendor</div><div class="slbl en">Data Stacks</div><div class="slbl ar" style="display:none">بيانات متباينة</div></div>
       <div class="sb"><div class="snum">Tier 1-3</div><div class="slbl en">Analyst Model</div><div class="slbl ar" style="display:none">هرمية التحليل</div></div>
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
 <div class="sn">02 / 20</div>
</section>"""

# ==============================================================================
# SLIDE 03 (s2): CORE PROBLEM - ALERT FATIGUE & STATIC TRIAGE
# ==============================================================================
s2_new = """<!-- ================= S03: PROBLEM STATEMENT ================= -->
<section class="slide" id="s2">
 <div class="orb o1" style="opacity:0.4"></div>
 <div class="content-box">
 <div class="tag a1" style="border-color:rgba(255,80,80,0.4);background:rgba(255,80,80,0.06)">
 <div class="dp" style="background:var(--acc);box-shadow:0 0 10px var(--acc)"></div>
 <span class="en" style="color:#ff9b9b">Chapter 1 &ndash; Problem Statement</span>
 <span class="ar" style="display:none;color:#ff9b9b">الفصل الأول &ndash; تعريف المشكلة</span>
 </div>
 <h2 class="st en">The Core Problem: Alert Fatigue &amp; Static Triage</h2>
 <h2 class="st ar" style="display:none">المشكلة الجوهرية: إرهاق التنبيهات والفرز الثابت</h2>
 <div class="gl"></div>

 <div class="split-ill-grid">
   <!-- Left Column: Problem Cards & Benchmark Finding -->
   <div style="display:flex;flex-direction:column;gap:10px">
     <div class="card" style="padding:12px 14px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
         <div class="c-icon rd" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.95rem;color:#ff9b9b">Alert Influx &amp; Noise Flooding</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem;color:#ff9b9b">فيضان التنبيهات والضجيج</h3>
       </div>
       <p class="en" style="font-size:0.82rem;margin:0">Modern SOCs accumulate up to 100 GB daily. Up to 54% consists of false positives and benign noise, severely exhausting cognitive capacity.</p>
       <p class="ar" style="display:none;font-size:0.82rem;margin:0">تستقبل مراكز العمليات ما يصل إلى 100 غيغابايت يومياً؛ أكثر من 54% منها إيجابيات كاذبة وضجيج يستنزف طاقة المحللين.</p>
     </div>

     <div class="card" style="padding:12px 14px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
         <div class="c-icon ye" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.95rem;color:#ffd166">Context Switching Friction</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem;color:#ffd166">إجهاد تبديل السياق بين الأنظمة</h3>
       </div>
       <p class="en" style="font-size:0.82rem;margin:0">Analysts manually pivot across 5 to 10 separate security tools to assemble evidence, causing severe mental friction, slow response, and human error.</p>
       <p class="ar" style="display:none;font-size:0.82rem;margin:0">يتنقل المحللون يدوياً بين 5 إلى 10 أنظمة منفصلة لجمع الأدلة، مما يولد تشتتاً ذهنياً وبطئاً حاداً في الاستجابة.</p>
     </div>

     <div class="card" style="padding:12px 14px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
         <div class="c-icon cy" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/><path d="m14 9 3 3-3 3"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.95rem;color:var(--s)">Static Rules &amp; FIFO Queues</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem;color:var(--s)">القواعد الثابتة وطوابير FIFO</h3>
       </div>
       <p class="en" style="font-size:0.82rem;margin:0">Deterministic rules cannot adapt to novel attacks. Unordered FIFO queues bury critical ransomware threats beneath low-priority noise.</p>
       <p class="ar" style="display:none;font-size:0.82rem;margin:0">قواعد الفرز الثابتة عاجزة عن التكيف مع الهجمات المتطورة؛ طوابير FIFO غير المرتبة تدفن التهديدات الحرجة تحت الضجيج.</p>
     </div>

     <div class="card" style="padding:10px 14px;display:flex;align-items:center;gap:14px;border:1px solid rgba(0,212,255,0.3);background:rgba(0,212,255,0.06)">
       <div style="font-family:'JetBrains Mono',monospace;font-size:1.3rem;font-weight:800;color:var(--s);white-space:nowrap;padding:4px 10px;background:rgba(0,212,255,0.12);border-radius:6px">22.9%</div>
       <div style="font-size:0.82rem;color:var(--t1);line-height:1.35">
         <span class="en"><strong>Key Finding (Gelman 2023):</strong> Dynamic risk-aware ordering reduces critical queue dwell time by <strong>22.9%</strong>.</span>
         <span class="ar" style="display:none"><strong>النتيجة المحورية (Gelman 2023):</strong> الترتيب الديناميكي الواعي بالمخاطر يقلل زمن انتظار الحوادث بنسبة <strong>22.9%</strong>.</span>
       </div>
     </div>
   </div>

   <!-- Right Column: Illustrated Alert Fatigue & Cognitive Storm Card -->
   <div class="ill-card">
     <div class="ill-frame" onclick="openImageModal('images/alert_fatigue_chaos.jpg', 'Alert Fatigue Crisis & Cognitive Overload - Visual Storm')">
       <img src="images/alert_fatigue_chaos.jpg" alt="Alert Fatigue Crisis & Cognitive Overload" class="ill-img" loading="lazy"/>
       <div class="ill-zoom-hint">
         <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
         <span>ZOOM</span>
       </div>
     </div>
     <div class="ill-caption">
       <div class="ill-title">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ff6b6b" stroke-width="2.2"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
         <span class="en">Alert Fatigue &amp; Cognitive Overload Crisis</span>
         <span class="ar" style="display:none">أزمة إرهاق التنبيهات والإنهاك الإدراكي</span>
       </div>
       <div class="ill-sub">CHAPTER 1 &sect;1.2</div>
     </div>
   </div>
 </div>

 </div>
 <div class="sn">03 / 20</div>
</section>"""

# ==============================================================================
# SLIDE 07 (s6): EXISTING SYSTEMS - SOC TECHNOLOGY EVOLUTION
# ==============================================================================
s6_new = """<!-- ================= S07: EXISTING WORK / RELATED WORK ================= -->
<section class="slide" id="s6">
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

    <!-- Featured 3D Evolution Timeline Illustration Card -->
    <div class="ill-card" style="margin-bottom:12px;min-height:220px;max-height:260px;padding:6px">
      <div class="ill-frame" style="max-height:215px" onclick="openImageModal('images/soc_tech_evolution.jpg', 'Evolution of Security Operations Technologies: Gen 1 to Gen 4')">
        <img src="images/soc_tech_evolution.jpg" alt="Evolution of Security Operations Technologies" class="ill-img" loading="lazy"/>
        <div class="ill-zoom-hint">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          <span>FULL TIMELINE ZOOM</span>
        </div>
      </div>
      <div class="ill-caption" style="padding:4px 8px 2px">
        <div class="ill-title" style="font-size:0.78rem">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg>
          <span class="en">From Manual Log Silos (Gen 1) to Autonomous AI-Augmented SOAR (Gen 4)</span>
          <span class="ar" style="display:none">من صوامع السجلات اليدوية (الجيل 1) إلى أداة SOAR المعززة بالذكاء (الجيل 4)</span>
        </div>
        <div class="ill-sub">CHAPTER 2 &sect;2.1-2.3</div>
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
  <div class="sn">07 / 20</div>
</section>"""

# ==============================================================================
# SLIDE 09 (s8): PROPOSED SOLUTION - AI AUGMENTS SOAR (RESEARCH GAP BRIDGE)
# ==============================================================================
s8_new = """<!-- ================= S09: PROPOSED SOLUTION ================= -->
<section class="slide" id="s8">
 <div class="orb o2" style="opacity:0.45"></div>
 <div class="content-box">
 <div class="tag a1">
 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15"/></svg>
 <span class="en">Chapter 2 &ndash; Proposed Solution</span><span class="ar" style="display:none">الفصل الثاني &ndash; الحل المقترح</span>
 </div>
 <h2 class="st en">Proposed Solution: AI Augments SOAR</h2>
 <h2 class="st ar" style="display:none">الحل المقترح: الذكاء الاصطناعي يعزز SOAR</h2>
 <div class="gl"></div>

 <div class="split-ill-grid">
   <!-- Left Column: Solution Cards & Stat Row -->
   <div style="display:flex;flex-direction:column;gap:12px">
     <div class="card" style="padding:14px 16px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
         <div class="c-icon gr" style="width:30px;height:30px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.98rem">AI/ML as Analytical Augmentation</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.98rem">الذكاء الاصطناعي كطبقة تحليلية</h3>
       </div>
       <p class="en" style="font-size:0.84rem;margin:0">AI/ML techniques analyze large heterogeneous security datasets to identify threat patterns, classify events, and calculate continuous risk scores. This provides a <strong>force-multiplier effect</strong> for human analysts.</p>
       <p class="ar" style="display:none;font-size:0.84rem;margin:0">تحلل تقنيات الذكاء الاصطناعي مجموعات البيانات الضخمة لتصنيف الأحداث وتقدير المخاطر ديناميكياً، مما يحقق أثر <strong>مضاعف القوة</strong> للمحللين.</p>
     </div>

     <div class="card" style="padding:14px 16px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px">
         <div class="c-icon cy" style="width:30px;height:30px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.98rem">Human-AI Teaming Paradigm</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.98rem">تكامل الإنسان والذكاء الاصطناعي</h3>
       </div>
       <p class="en" style="font-size:0.84rem;margin:0">AI/ML does not replace the analyst; it provides data-driven intelligence to triage while SOAR handles workflow execution — under strict human analyst oversight for uncertain actions.</p>
       <p class="ar" style="display:none;font-size:0.84rem;margin:0">الذكاء الاصطناعي لا يستبدل المحلل؛ بل يوفر استدلالاً ذكياً للفرز بينما يتولى SOAR التنفيذ — تحت إشراف بشري كامل للإجراءات الحساسة.</p>
     </div>

     <div class="srow" style="margin-top:2px">
       <div class="sb"><div class="snum">AI/ML</div><div class="slbl en">Analytical Layer</div><div class="slbl ar" style="display:none">الطبقة التحليلية</div></div>
       <div class="sb"><div class="snum">SOAR</div><div class="slbl en">Workflow Engine</div><div class="slbl ar" style="display:none">محرك سير العمل</div></div>
       <div class="sb"><div class="snum">DSR</div><div class="slbl en">Methodology</div><div class="slbl ar" style="display:none">منهجية البحث</div></div>
     </div>
   </div>

   <!-- Right Column: Illustrated Research Gap Bridge Card -->
   <div class="ill-card">
     <div class="ill-frame" onclick="openImageModal('images/research_gap_bridge.jpg', 'Bridging the Research Gap: Uniting ML Threat Scoring with SOAR Playbook Execution')">
       <img src="images/research_gap_bridge.jpg" alt="Research Gap Bridge: ML to SOAR Integration" class="ill-img" loading="lazy"/>
       <div class="ill-zoom-hint">
         <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
         <span>ZOOM</span>
       </div>
     </div>
     <div class="ill-caption">
       <div class="ill-title">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
         <span class="en">Bridging the Gap: ML Prediction to SOAR Execution</span>
         <span class="ar" style="display:none">سد الفجوة: ربط تنبؤات ML بتنفيذ أتمتة SOAR</span>
       </div>
       <div class="ill-sub">GAP CLOSED &sect;2.4</div>
     </div>
   </div>
 </div>

 </div>
 <div class="sn">09 / 20</div>
</section>"""

# ==============================================================================
# SLIDE 10 (s9): SYSTEM ARCHITECTURE OVERVIEW (MASTER 3D BLUEPRINT)
# ==============================================================================
s9_new = """<!-- ================= S10: SYSTEM ARCHITECTURE OVERVIEW ================= -->
<section class="slide" id="s9">
 <div class="orb o3" style="opacity:0.4"></div>
 <div class="content-box">
 <div class="tag a1">
 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
 <span class="en">Chapter 3 &ndash; Architecture</span><span class="ar" style="display:none">الفصل الثالث &ndash; المعمارية</span>
 </div>
 <h2 class="st en">System Architecture Overview</h2>
 <h2 class="st ar" style="display:none">نظرة عامة على معمارية النظام</h2>
 <div class="gl"></div>

 <div class="split-ill-grid">
   <!-- Left Column: 5 Architectural Layers Detailed -->
   <div style="display:flex;flex-direction:column;gap:8px">
     <div class="alr" style="padding:8px 12px">
       <div class="all en" style="font-size:0.85rem"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/></svg> Tier 1: Ingestion &amp; Connectors</div>
       <div class="all ar" style="display:none;font-size:0.85rem">الطبقة 1: الاستيعاب والموصلات</div>
       <div class="ali"><span class="ai">SIEM Events</span><span class="ai">EDR Telemetry</span><span class="ai">Syslog / CEF</span></div>
     </div>

     <div class="alr" style="padding:8px 12px">
       <div class="all en" style="color:var(--s);font-size:0.85rem"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/></svg> Tier 2: Multi-Source Enrichment</div>
       <div class="all ar" style="display:none;color:var(--s);font-size:0.85rem">الطبقة 2: الإثراء متعدد المصادر</div>
       <div class="ali"><span class="ai cy">Asset DB</span><span class="ai cy">Identity Sensitivity</span><span class="ai cy">Threat Intel Feeds</span></div>
     </div>

     <div class="alr" style="padding:8px 12px">
       <div class="all en" style="color:var(--ok);font-size:0.85rem"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15"/></svg> Tier 3: AI/ML Risk Scoring Engine</div>
       <div class="all ar" style="display:none;color:var(--ok);font-size:0.85rem">الطبقة 3: محرك تقييم المخاطر بالذكاء</div>
       <div class="ali"><span class="ai gr">Feature Vectorizer</span><span class="ai gr">R_total [0,1]</span><span class="ai gr">Confidence Gate</span></div>
     </div>

     <div class="alr" style="padding:8px 12px">
       <div class="all en" style="color:var(--wa);font-size:0.85rem"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> Tier 4: Response Orchestration</div>
       <div class="all ar" style="display:none;color:var(--wa);font-size:0.85rem">الطبقة 4: تنسيق الاستجابة المؤتمتة</div>
       <div class="ali"><span class="ai ye">Playbook Engine</span><span class="ai ye">Human Approval</span><span class="ai ye">API Dispatch</span></div>
     </div>

     <div class="alr" style="padding:8px 12px">
       <div class="all en" style="color:var(--acc);font-size:0.85rem"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16"/></svg> Tier 5: Dashboard &amp; Feedback Loop</div>
       <div class="all ar" style="display:none;color:var(--acc);font-size:0.85rem">الطبقة 5: لوحة التحكم وحلقة التعلم</div>
       <div class="ali"><span class="ai rd">Analyst Triage HUD</span><span class="ai rd">Active Retraining</span><span class="ai rd">Audit Trails</span></div>
     </div>
   </div>

   <!-- Right Column: Illustrated Master 3D Architecture Blueprint Card -->
   <div class="ill-card">
     <div class="ill-frame" onclick="openImageModal('images/system_arch_master.jpg', 'Master 5-Tier AI-Based SOAR Architecture Blueprint')">
       <img src="images/system_arch_master.jpg" alt="Master 5-Tier AI-Based SOAR Architecture Blueprint" class="ill-img" loading="lazy"/>
       <div class="ill-zoom-hint">
         <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
         <span>INSPECT TIERS</span>
       </div>
     </div>
     <div class="ill-caption">
       <div class="ill-title">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/></svg>
         <span class="en">Full 5-Tier AI-SOAR System Architecture</span>
         <span class="ar" style="display:none">المخطط المعماري خماسي الطبقات لمنظومة SOAR الذكية</span>
       </div>
       <div class="ill-sub">CHAPTER 3 &sect;3.2-3.3</div>
     </div>
   </div>
 </div>

 </div>
 <div class="sn">10 / 20</div>
</section>"""

# ==============================================================================
# SLIDE 14 (s13): DESIGN PROGRESS - ADAPTIVE PRIORITIZATION & NOISE SUPPRESSION
# ==============================================================================
s13_new = """<!-- ================= S14: DESIGN PROGRESS (Prioritization) ================= -->
<section class="slide" id="s13">
 <div class="orb o2" style="opacity:0.35"></div>
 <div class="content-box">
 <div class="tag a1">
 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>
 <span class="en">Chapter 3 &ndash; Design Progress</span><span class="ar" style="display:none">الفصل الثالث &ndash; تقدم التصميم</span>
 </div>
 <h2 class="st en">Design Progress: Adaptive Prioritization &amp; Noise Suppression</h2>
 <h2 class="st ar" style="display:none">تقدم التصميم: الأولويات التكيفية وقمع الضجيج</h2>
 <div class="gl"></div>

 <div class="split-ill-grid">
   <!-- Left Column: Priority Rules & Operational Rationale -->
   <div style="display:flex;flex-direction:column;gap:10px">
     <div class="card" style="padding:12px 14px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
         <div class="c-icon cy" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.95rem">Dynamic Queue Ordering</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">ترتيب طوابير ديناميكي</h3>
       </div>
       <p class="en" style="font-size:0.82rem;margin:0">Alerts are ranked by <strong>continuous contextual risk</strong> rather than static severity tags. Critical incidents surface immediately to the top priority lane.</p>
       <p class="ar" style="display:none;font-size:0.82rem;margin:0">تُرتب التنبيهات حسب <strong>الخطر السياقي المستمر</strong> لا الشدة الثابتة، مما يدفع الحوادث الحرجة فوراً إلى أعلى الطابور.</p>
     </div>

     <div class="card" style="padding:12px 14px">
       <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
         <div class="c-icon gr" style="width:28px;height:28px"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
         <h3 class="ct en" style="margin:0;font-size:0.95rem">Suppression vs. Deprioritization</h3>
         <h3 class="ct ar" style="display:none;margin:0;font-size:0.95rem">القمع المنضبط مقابل خفض الأولوية</h3>
       </div>
       <p class="en" style="font-size:0.82rem;margin:0">Benign alerts (low risk, high confidence) are excluded from primary queues but <strong>retained for audit</strong>. Medium threats remain visible in secondary queues.</p>
       <p class="ar" style="display:none;font-size:0.82rem;margin:0">التنبيهات الحميدة منخفضة الخطر تُستثنى من الطوابير الأولية مع <strong>حفظها للتدقيق</strong>، مما يحفظ وقت المحللين.</p>
     </div>

     <div class="card" style="padding:10px 14px;border:1px solid rgba(16,185,129,0.3);background:rgba(16,185,129,0.06)">
       <div style="display:flex;align-items:center;gap:12px">
         <div style="font-family:'JetBrains Mono',monospace;font-size:1.35rem;font-weight:900;color:var(--ok);white-space:nowrap;padding:4px 10px;background:rgba(16,185,129,0.15);border-radius:6px">-22.9%</div>
         <div style="font-size:0.82rem;color:var(--t1);line-height:1.35">
           <span class="en"><strong>Empirical Benchmark (Gelman et al., 2023):</strong> Dynamic ordering cuts critical incident queue dwell time by <strong>22.9%</strong>.</span>
           <span class="ar" style="display:none"><strong>المؤشر المعياري (Gelman et al., 2023):</strong> الترتيب الديناميكي يقلل زمن انتظار الحوادث الحرجة بنسبة <strong>22.9%</strong>.</span>
         </div>
       </div>
     </div>
   </div>

   <!-- Right Column: Illustrated FIFO vs. Dynamic Risk Queue Card -->
   <div class="ill-card">
     <div class="ill-frame" onclick="openImageModal('images/queue_prioritization.jpg', 'Conventional FIFO Queue vs. Dynamic Risk Queue - 22.9% Dwell Time Reduction')">
       <img src="images/queue_prioritization.jpg" alt="Conventional FIFO Queue vs Dynamic Risk Queue" class="ill-img" loading="lazy"/>
       <div class="ill-zoom-hint">
         <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
         <span>COMPARE QUEUES</span>
       </div>
     </div>
     <div class="ill-caption">
       <div class="ill-title">
         <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="var(--s)" stroke-width="2.2"><path d="M12 20v-6M6 20V10M18 20V4"/></svg>
         <span class="en">FIFO Congestion vs. Dynamic Express Priority</span>
         <span class="ar" style="display:none">طوابير FIFO الراكدة مقابل أولوية المسار السريع الذكية</span>
       </div>
       <div class="ill-sub">BENCHMARK &sect;3.6</div>
     </div>
   </div>
 </div>

 </div>
 <div class="sn">14 / 20</div>
</section>"""

# Apply section replacements
patterns = [
    (r'<section\s+class="slide[^"]*"\s+id="s1"[^>]*>.*?</section>', s1_new),
    (r'<section\s+class="slide[^"]*"\s+id="s2"[^>]*>.*?</section>', s2_new),
    (r'<section\s+class="slide[^"]*"\s+id="s6"[^>]*>.*?</section>', s6_new),
    (r'<section\s+class="slide[^"]*"\s+id="s8"[^>]*>.*?</section>', s8_new),
    (r'<section\s+class="slide[^"]*"\s+id="s9"[^>]*>.*?</section>', s9_new),
    (r'<section\s+class="slide[^"]*"\s+id="s13"[^>]*>.*?</section>', s13_new),
]

for pat, rep in patterns:
    if re.search(pat, html, re.DOTALL):
        html = re.sub(pat, rep, html, count=1, flags=re.DOTALL)
        print(f"Replaced pattern successfully")
    else:
        print(f"FAILED TO MATCH pattern: {pat[:40]}")

# 3. Inject Lightbox Modal and JS right before </body>
modal_html = """
<!-- ================= INTERACTIVE LIGHTBOX MODAL FOR DEFENSE COMMITTEE ================= -->
<div id="imgModal" onclick="closeImageModal(event)">
  <div class="modal-content-wrap" onclick="event.stopPropagation()">
    <button class="modal-close-btn" onclick="closeImageModal(event)" title="Close (Esc)">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
    <img id="modalImg" class="modal-img" src="" alt="Expanded View"/>
    <div id="modalCaption" class="modal-caption"></div>
  </div>
</div>

<script>
function openImageModal(src, caption) {
  const modal = document.getElementById('imgModal');
  const img = document.getElementById('modalImg');
  const cap = document.getElementById('modalCaption');
  if (modal && img && cap) {
    img.src = src;
    cap.textContent = caption || '';
    modal.classList.add('active');
  }
}

function closeImageModal(e) {
  if (e) e.stopPropagation();
  const modal = document.getElementById('imgModal');
  if (modal) {
    modal.classList.remove('active');
  }
}

// Close on Escape key
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    closeImageModal();
  }
});
</script>
"""

if 'id="imgModal"' not in html:
    html = html.replace('</body>', f'{modal_html}\n</body>')

with open('presentation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Applied strategic illustrations, CSS, and Lightbox modal to presentation/index.html")
