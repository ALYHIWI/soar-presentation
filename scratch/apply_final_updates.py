# -*- coding: utf-8 -*-
import re

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Initial HTML length: {len(html)}")

# ============================================================
# 1. SLIDE 2: Add Student IDs to Team Cards
# ============================================================
team_updates = [
    (
        '<div class="nm">Hizam Mohammed Ali Al-Shajara</div>',
        '<div class="nm">Hizam Mohammed Ali Al-Shajara</div>\n        <div class="std-id" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202210102478</div>'
    ),
    (
        '<div class="nm">Hamoud Abdullah Saleh Abu Amrah</div>',
        '<div class="nm">Hamoud Abdullah Saleh Abu Amrah</div>\n        <div class="std-id" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310101609</div>'
    ),
    (
        '<div class="nm">Mohammed Hameed Qasim Mohammed</div>',
        '<div class="nm">Mohammed Hameed Qasim Mohammed</div>\n        <div class="std-id" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100174</div>'
    ),
    (
        '<div class="nm">Mohammed Taha Qasim Al-Warafi</div>',
        '<div class="nm">Mohammed Taha Qasim Al-Warafi</div>\n        <div class="std-id" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100461</div>'
    ),
    (
        '<div class="nm">Marwan Mohammed Saeed Al-Ameer</div>',
        '<div class="nm">Marwan Mohammed Saeed Al-Ameer</div>\n        <div class="std-id" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100177</div>'
    ),
    (
        '<div class="nm">Noah Ahmed Mohammed Maraq</div>',
        '<div class="nm">Noah Ahmed Mohammed Maraq</div>\n        <div class="std-id" style="font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;color:var(--s);margin-bottom:2px">ID: 202310100452</div>'
    ),
]

for old, new in team_updates:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"✓ Team ID added: {old[:30]}...")
    else:
        print(f"✗ Team ID NOT found: {old[:30]}...")

# ============================================================
# 2. SLIDE 12: Table 2-1 from §2.4.4 of Project Report
# ============================================================
old_s12_table = '''    <div class="tbl-wrap">
      <table class="ctbl">
        <thead>
          <tr>
            <th><span class="en">ML Approach</span><span class="ar" style="display:none">الخوارزمية / النموذج</span></th>
            <th><span class="en">Primary Strength</span><span class="ar" style="display:none">أبرز المزايا ونقاط القوة</span></th>
            <th><span class="en">Operational Limitation</span><span class="ar" style="display:none">القيود في بيئة SOC</span></th>
            <th><span class="en">Project Role</span><span class="ar" style="display:none">الدور في مشروعنا المقترح</span></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Random Forest (RF)</strong></td>
            <td><span class="en">High interpretability, fast training, feature importance scoring</span><span class="ar" style="display:none">قابلية تفسير عالية، سرعة فائقة في التدريب</span></td>
            <td><span class="en">Struggles with temporal sequence shifts</span><span class="ar" style="display:none">أداء أقل مع السلاسل الزمنية المتغيرة</span></td>
            <td><span class="pill pg">Baseline Supervised Classifier</span></td>
          </tr>
          <tr>
            <td><strong>Deep Neural Nets (DNN)</strong></td>
            <td><span class="en">Models complex non-linear alert interactions</span><span class="ar" style="display:none">تمثيل العلاقات غير الخطية المعقدة</span></td>
            <td><span class="en">High compute latency, black-box opacity</span><span class="ar" style="display:none">صعوبة التفسير (صندوق أسود) وتكلفة حوسبة</span></td>
            <td><span class="pill pc">High-Dimensional Feature Mining</span></td>
          </tr>
          <tr>
            <td><strong>Reinforcement Learning (RL)</strong></td>
            <td><span class="en">Dynamic queue optimization, adaptive priority policy</span><span class="ar" style="display:none">تحسين ديناميكي مستمر لترتيب قوائم الانتظار</span></td>
            <td><span class="en">Requires extensive simulation reward tuning</span><span class="ar" style="display:none">حساسية عالية لدوال المكافأة وبيئة المحاكاة</span></td>
            <td><span class="pill py">Queue Scheduling Policy</span></td>
          </tr>
          <tr>
            <td><strong>LLMs &amp; AI Agents</strong></td>
            <td><span class="en">Semantic synthesis, threat narrative generation</span><span class="ar" style="display:none">توليد ملخصات سياقية ذكية وتفسير التقارير</span></td>
            <td><span class="en">Hallucination risks, high token inference cost</span><span class="ar" style="display:none">احتمالية التشتت (الهلوسة) والتكلفة المرتفعة</span></td>
            <td><span class="pill pp">Analyst Briefing Assistant</span></td>
          </tr>
        </tbody>
      </table>
    </div>'''

new_s12_table = '''    <div class="tbl-wrap" style="overflow-x:auto">
      <table class="ctbl" style="font-size:0.76rem">
        <thead>
          <tr>
            <th><span class="en">Study</span><span class="ar" style="display:none">الدراسة المرجعية</span></th>
            <th><span class="en">Data / Environment</span><span class="ar" style="display:none">بيئة البيانات</span></th>
            <th><span class="en">AI/ML Approach</span><span class="ar" style="display:none">نموذج الذكاء الاصطناعي</span></th>
            <th><span class="en">Context / Feedback</span><span class="ar" style="display:none">السياق والتغذية الراجعة</span></th>
            <th><span class="en">Prioritization Output</span><span class="ar" style="display:none">مخرجات تحديد الأولوية</span></th>
            <th style="color:var(--acc)"><span class="en">SOAR / Response</span><span class="ar" style="display:none">الربط مع SOAR</span></th>
            <th><span class="en">Main Limitation</span><span class="ar" style="display:none">القصور الرئيسي</span></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Gupta et al. (2019)</strong></td>
            <td><span class="en">Real SOC-labeled SOD events</span><span class="ar" style="display:none">سجلات حقيقية مصنفة من SOC</span></td>
            <td><span class="en">DNN supervised classification</span><span class="ar" style="display:none">شبكات عصبية عميقة (DNN)</span></td>
            <td><span class="en">Engineered event features; no online feedback</span><span class="ar" style="display:none">خصائص مهندسة دون تغذية مباشرة</span></td>
            <td><span class="en">Notified / non-notified classification</span><span class="ar" style="display:none">تصنيف ثنائي: إشعار / عدم إشعار</span></td>
            <td><span class="pill pr">No</span></td>
            <td><span class="en">Binary output; low minority-class precision (0.39)</span><span class="ar" style="display:none">مخرج ثنائي، دقة منخفضة لفئة الأقلية</span></td>
          </tr>
          <tr>
            <td><strong>Gelman et al. (2023)</strong></td>
            <td><span class="en">Real MDR data; deployment simulation</span><span class="ar" style="display:none">بيانات MDR حقيقية؛ محاكاة نشر</span></td>
            <td><span class="en">RF + NN actionability scoring (TEQ)</span><span class="ar" style="display:none">غابة عشوائية وشبكات عصبية</span></td>
            <td><span class="en">Content/context features; historical labels</span><span class="ar" style="display:none">خصائص المحتوى والسياق وسجلات سابقة</span></td>
            <td><span class="en">Incident and alert scores, suppression</span><span class="ar" style="display:none">نقاط الحادث والتنبيه، قمع الضجيج</span></td>
            <td><span class="pill pr">No</span></td>
            <td><span class="en">Preprint; operational effects simulated</span><span class="ar" style="display:none">دراسة أولية؛ آثار تشغيلية بالمحاكاة</span></td>
          </tr>
          <tr>
            <td><strong>Liu et al. (2022)</strong></td>
            <td><span class="en">Enterprise-scale heterogeneous event data</span><span class="ar" style="display:none">بيانات متباينة على مستوى المؤسسة</span></td>
            <td><span class="en">Context representation + deviation (Context2Vector)</span><span class="ar" style="display:none">تمثيل السياق واكتشاف الانحراف</span></td>
            <td><span class="en">Behavioral context; expert annotation</span><span class="ar" style="display:none">سياق سلوكي وترميز خبراء</span></td>
            <td><span class="en">Contextual risk ranking</span><span class="ar" style="display:none">ترتيب المخاطر وفق السياق</span></td>
            <td><span class="pill pr">No</span></td>
            <td><span class="en">No downstream response execution</span><span class="ar" style="display:none">غياب التنفيذ الآلي للاستجابة اللاحقة</span></td>
          </tr>
          <tr>
            <td><strong>Wang et al. (2024)</strong></td>
            <td><span class="en">Five multi-step attack datasets</span><span class="ar" style="display:none">5 مجموعات بيانات لهجمات متسلسلة</span></td>
            <td><span class="en">Isolation Forest + RL active learning (AlertPro)</span><span class="ar" style="display:none">غابة العزل مع تعلم نشط معزز</span></td>
            <td><span class="en">Context/history + iterative analyst feedback</span><span class="ar" style="display:none">سياق وتاريخ وتغذية راجعة تكرارية</span></td>
            <td><span class="en">Dynamic alert re-ranking</span><span class="ar" style="display:none">إعادة ترتيب ديناميكي للتنبيهات</span></td>
            <td><span class="pill pr">No</span></td>
            <td><span class="en">Stops at triage/investigation</span><span class="ar" style="display:none">يتوقف عند الفرز والتحقيق فقط</span></td>
          </tr>
          <tr>
            <td><strong>Chavali et al. (2024)</strong></td>
            <td><span class="en">Three public IDS datasets</span><span class="ar" style="display:none">3 مجموعات بيانات IDS عامة</span></td>
            <td><span class="en">TD3-AP / SAC-AP DRL</span><span class="ar" style="display:none">تعلم تعزيزي عميق (TD3/SAC)</span></td>
            <td><span class="en">Resource/state info; no analyst feedback</span><span class="ar" style="display:none">معلومات الموارد وحالة النظام دون محلل</span></td>
            <td><span class="en">Resource-aware investigation priority</span><span class="ar" style="display:none">أولوية التحقيق الواعية بالموارد</span></td>
            <td><span class="pill pr">No</span></td>
            <td><span class="en">No real-world SOC validation or SOAR execution</span><span class="ar" style="display:none">دون تحقق واقعي في SOC أو تنفيذ SOAR</span></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="hl" style="margin-top:10px">
      <p class="en"><strong>Synthesis of Literature Table 2-1:</strong> None of the reviewed academic or preprint systems execute automated downstream SOAR response workflows. This empirically establishes the <strong>core research gap</strong> addressed by our project.</p>
      <p class="ar" style="display:none"><strong>خلاصة المقارنة المعيارية من جدول 2-1:</strong> جميع الأنظمة الأكاديمية السابقة تتوقف عند الفرز أو إعادة الترتيب دون أي تنفيذ آلي للاستجابة عبر SOAR، وهو ما يثبت علمياً الفجوة البحثية الجوهرية لمشروعنا.</p>
    </div>'''

if old_s12_table in html:
    html = html.replace(old_s12_table, new_s12_table, 1)
    print("✓ Slide 12 updated with Table 2-1 from §2.4.4")
else:
    print("✗ Slide 12 table NOT found for exact replacement")

# Also update Slide 12 tag and title to match Table 2-1
old_s12_header = '''    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
      <span class="en">Chapter 2 &ndash; Machine Learning Benchmarks</span><span class="ar" style="display:none">الفصل الثاني &ndash; مقارنة خوارزميات التعلم</span>
    </div>
    <h2 class="st en">Comparative Analysis of ML Triage Approaches</h2>
    <h2 class="st ar" style="display:none">المقارنة المعيارية لتقنيات تعلم الآلة في الفرز الأمني</h2>'''

new_s12_header = '''    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>
      <span class="en">Chapter 2 &ndash; Table 2-1 (§2.4.4)</span><span class="ar" style="display:none">الفصل الثاني &ndash; جدول 2-1 (§2.4.4)</span>
    </div>
    <h2 class="st en">Comparative Analysis of Existing ML-Based SOC Triage Approaches</h2>
    <h2 class="st ar" style="display:none">المقارنة المعيارية لأنظمة الفرز الأمني القائمة على تعلم الآلة (جدول 2-1)</h2>'''

if old_s12_header in html:
    html = html.replace(old_s12_header, new_s12_header, 1)
    print("✓ Slide 12 header updated to Table 2-1 title")
else:
    print("✗ Slide 12 header NOT found")

# ============================================================
# 3. SLIDE 16: Multi-Dimensional Context Enrichment Pipeline (§3.4)
# ============================================================
old_s16_cards = '''    <div class="grid g3">
      <div class="card">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/></svg></div>
        <h3 class="ct en">Asset Posture &amp; Value</h3><h3 class="ct ar" style="display:none">حساسية الأصل وقيمته</h3>
        <p class="en">Queries CMDB for host business criticality tier (Tier 1: Core Banking DB vs Tier 4: Guest Wi-Fi kiosk), existing vulnerabilities (CVEs), and OS patch level.</p>
        <p class="ar" style="display:none">استعلام قاعدة بيانات الأصول لمعرفة أهمية الخادم (خادم إنتاج مالي أم جهاز اختبار) ومستوى الثغرات المسجلة عليه.</p>
      </div>
      <div class="card">
        <div class="c-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <h3 class="ct en">User Identity &amp; Privileges</h3><h3 class="ct ar" style="display:none">هوية المستخدم وصلاحياته</h3>
        <p class="en">Extracts user directory roles (Domain Admin vs contractor), normal working hours, geolocation baseline, and recent privilege escalation attempts.</p>
        <p class="ar" style="display:none">استخراج صلاحيات الحساب (مدير نطاق أم موظف مؤقت)، مواعيد العمل المعتادة، والموقع الجغرافي المسجل له.</p>
      </div>
      <div class="card">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h3 class="ct en">External Threat Intel</h3><h3 class="ct ar" style="display:none">استخبارات التهديدات الخارجية</h3>
        <p class="en">Asynchronous reputation lookups against threat feeds (VirusTotal, AbuseIPDB, AlienVault OTX) for IP, domain, and file hash reputation scores.</p>
        <p class="ar" style="display:none">فحص متزامن لعناوين IP وبصمات الملفات في قواعد التهديدات الدولية لتحديد درجة خطورتها السابقة.</p>
      </div>
    </div>
    <div class="hl" style="margin-top:14px">
      <p class="en"><strong>Enrichment Output:</strong> A densely populated feature vector transforming a naked alert into a situation-aware analytical packet ready for the ML Triage Model.</p>
      <p class="ar" style="display:none"><strong>مخرجات الإثراء:</strong> تحويل التنبيه المجرد إلى متجهة خصائص غنية بالسياق تمكّن نموذج تعلم الآلة من تقدير الموقف بدقة متناهية.</p>
    </div>'''

new_s16_cards = '''    <div class="grid g3">
      <div class="card">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/></svg></div>
        <h3 class="ct en">Asset &amp; Identity Context</h3><h3 class="ct ar" style="display:none">سياق الأصل وهوية المستخدم</h3>
        <p class="en">Provides organizational context: asset type, business criticality, network location, and exposure level. Enriches account privilege level, authentication history, and sensitive resource access to distinguish routine events from high-impact exposure (§3.4).</p>
        <p class="ar" style="display:none">يوفر السياق المؤسسي: نوع الأصل وحساسيته التشغيلية وموقعه في الشبكة، مع تدقيق صلاحيات الحساب وتاريخ المصادقة للتمييز بين الأنشطة العادية والحسابات الحرجة.</p>
      </div>
      <div class="card">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h3 class="ct en">Threat Intelligence Context</h3><h3 class="ct ar" style="display:none">سياق استخبارات التهديدات</h3>
        <p class="en">Enriches observable indicators (IPs, domains, URLs, file hashes) with reputation status, indicator type, and known malicious associations from threat feeds, supporting situational awareness before risk assessment (Bridges et al., 2023).</p>
        <p class="ar" style="display:none">إثراء المؤشرات الظاهرة (عناوين IP، النطاقات، بصمات الملفات) بحالة السمعة والارتباط بالهجمات الخبيثة من قواعد استخبارات التهديدات المتاحة.</p>
      </div>
      <div class="card">
        <div class="c-icon gr"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 8v4l3 3"/><circle cx="12" cy="12" r="9"/></svg></div>
        <h3 class="ct en">Historical &amp; Behavioral Context</h3><h3 class="ct ar" style="display:none">السياق التاريخي والسلوكي</h3>
        <p class="en">Determines whether similar alerts, indicators, or assets appeared previously within a temporal window. Context2Vector demonstrates that events carry different operational meanings depending on surrounding behavioral context (Liu et al., 2022).</p>
        <p class="ar" style="display:none">تتبع ظهور التنبيهات أو الحسابات المشابهة ضمن نافذة زمنية معينة؛ فالأحداث الأمنية تختلف دلالتها التشغيلية باختلاف السياق السلوكي المحيط بها.</p>
      </div>
    </div>
    <div class="hl" style="margin-top:14px">
      <p class="en"><strong>Enrichment Modular Resilience &amp; Scope (§3.4):</strong> The layer degrades gracefully when particular enrichment sources are temporarily unavailable. It creates an enriched alert representation without assigning final priority or executing response actions directly.</p>
      <p class="ar" style="display:none"><strong>المرونة المعيارية وحدود الإثراء (§3.4):</strong> يتكيف النظام بسلاسة عند تعذر أحد مصادر الإثراء. وتقتصر وظيفته على تجهيز كائن التنبيه المثرى دون اتخاذ قرارات الأولوية أو الاستجابة بشكل مباشر.</p>
    </div>'''

if old_s16_cards in html:
    html = html.replace(old_s16_cards, new_s16_cards, 1)
    print("✓ Slide 16 updated with verbatim §3.4 text")
else:
    print("✗ Slide 16 cards NOT found")

# ============================================================
# 4. SLIDE 17: ML Triage & Analytical Outputs Formulation (§3.5)
# ============================================================
old_s17_content = '''    <div class="grid g2" style="gap:20px">
      <div class="card">
        <h3 class="ct en" style="color:var(--s)">The Risk Scoring Formula</h3>
        <h3 class="ct ar" style="display:none;color:var(--s)">معادلة حساب المخاطر الرياضية</h3>
        <div style="background:rgba(0,0,0,0.5);border:1px solid var(--br);padding:12px;border-radius:8px;font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;color:var(--s);margin:10px 0">
          Risk = (w<sub>1</sub> &middot; S<sub>base</sub>) + (w<sub>2</sub> &middot; C<sub>asset</sub>) + (w<sub>3</sub> &middot; TI<sub>rep</sub>) + (w<sub>4</sub> &middot; A<sub>user</sub>)
        </div>
        <p class="en">Weights <code>w<sub>1</sub>...w<sub>4</sub></code> are calibrated dynamically using Random Forest feature importance and Soft Actor-Critic (SAC) reinforcement reward.</p>
        <p class="ar" style="display:none">تُوزن المعاملات وفق أهمية الخصائص المستخلصة من نموذج الغابة العشوائية وبمكافآت التعلّم المعزز التكيفي.</p>
      </div>
      <div class="card">
        <h3 class="ct en" style="color:var(--ok)">Dual Output: Classification &amp; Confidence</h3>
        <h3 class="ct ar" style="display:none;color:var(--ok)">المخرج المزدوج: التصنيف ودرجة الثقة</h3>
        <ul style="gap:8px;margin-top:6px">
          <li class="en"><strong>Triage Class:</strong> True Positive (Attack), Benign Noise, or Reconnaissance.</li>
          <li class="ar" style="display:none"><strong>فئة التنبيه:</strong> هجوم مؤكد، نشاط حميد كاذب، أو محاولة استكشافية.</li>
          <li class="en"><strong>Confidence Score &Phi;:</strong> Probability distribution [0.0 - 1.0] indicating model certainty.</li>
          <li class="ar" style="display:none"><strong>مؤشر الثقة:</strong> قيمة احتمالية تقيس يقين النموذج بالقرار قبل تشغيل الاستجابة.</li>
          <li class="en"><strong>Mitigation Trigger:</strong> Alerts with Risk &gt; 80 and &Phi; &gt; 0.90 qualify for automatic isolation.</li>
          <li class="ar" style="display:none"><strong>عتبة الاستجابة:</strong> الحوادث ذات الخطورة العالية والثقة المرتفعة تؤهل للعزل الآلي الفوري.</li>
        </ul>
      </div>
    </div>
    <div class="srow" style="margin-top:14px">
      <div class="sb"><div class="snum">0–100</div><div class="slbl en">Contextual Risk Score Range</div><div class="slbl ar" style="display:none">مدى تقييم الخطر</div></div>
      <div class="sb"><div class="snum">AUC</div><div class="slbl en">Primary Evaluation Metric</div><div class="slbl ar" style="display:none">مقياس التقييم الأساسي</div></div>
      <div class="sb"><div class="snum">22.9%</div><div class="slbl en">Wait-Time Reduction (Literature)</div><div class="slbl ar" style="display:none">تحسين وقت الانتظار (الأدبيات)</div></div>
    </div>'''

new_s17_content = '''    <div class="grid g2" style="gap:20px">
      <div class="card">
        <h3 class="ct en" style="color:var(--s)">Mandatory Analytical Output (§3.5)</h3>
        <h3 class="ct ar" style="display:none;color:var(--s)">المخرج التحليلي الأساسي (§3.5)</h3>
        <p class="en" style="margin-bottom:10px">The primary output of the engine is a <strong>Contextual Risk Score</strong> representing the estimated operational significance of the alert, normalized to a consistent range [0, 1] where higher values indicate greater estimated risk.</p>
        <p class="ar" style="display:none;margin-bottom:10px">المخرج الإلزامي الأساسي للمحرك هو <strong>درجة المخاطر السياقية</strong> المعيارية [0, 1] والتي تعبر عن الأهمية التشغيلية المقدرة للحدث بدلاً من الاعتماد على الشدة الثابتة لأداة الحماية.</p>
        <p class="en"><strong>Principle of Separation:</strong> The engine is deliberately separated from both prioritization and response execution. It produces analytical outputs consumed by subsequent policy checks, preventing a raw model prediction from directly triggering high-impact actions.</p>
        <p class="ar" style="display:none"><strong>مبدأ الفصل المعماري:</strong> يفصل المحرك بصرامة عن إدارة الأولويات وتنفيذ الاستجابة، منعاً لترجمة التنبؤ الخام إلى إجراءات استجابة عالية الخطورة دون مراجعة السياسات.</p>
      </div>
      <div class="card">
        <h3 class="ct en" style="color:var(--ok)">Supporting Outputs: Confidence &amp; Actionability</h3>
        <h3 class="ct ar" style="display:none;color:var(--ok)">المخرجات المساندة: مؤشر الثقة وقابلية التنفيذ</h3>
        <ul style="gap:8px;margin-top:6px">
          <li class="en"><strong>Confidence Indicator:</strong> Conceptually distinct from risk score (Risk = security significance, Confidence = model certainty). A high-risk prediction with low confidence routes to analyst validation; high confidence enables policy-governed automation.</li>
          <li class="ar" style="display:none"><strong>مؤشر الثقة:</strong> منفصل مفهومياً عن درجة الخطر (الخطر يمثل الأهمية الأمنية، بينما الثقة تمثل يقين النموذج). الخطر العالي مع الثقة المنخفضة يتطلب تدقيق المحلل، بينما الثقة العالية تدعم الأتمتة المعتمدة.</li>
          <li class="en"><strong>Predicted Class / Actionability Label:</strong> Distinguishes alerts estimated to require further investigation from lower-priority events (Gupta et al., 2019).</li>
          <li class="ar" style="display:none"><strong>تصنيف قابلية التنفيذ:</strong> يميز التنبيهات التي تتطلب تحقيقاً عن التنبيهات الروتينية منخفضة الأولوية.</li>
          <li class="en"><strong>Explanatory Features:</strong> Exposes the attributes that contributed most strongly to the resulting score to support analyst interpretation and validation.</li>
          <li class="ar" style="display:none"><strong>تفسير القرار:</strong> إظهار الخصائص الأكثر تأثيراً في النتيجة لدعم تفسير المحلل وقراره.</li>
        </ul>
      </div>
    </div>
    <div class="srow" style="margin-top:14px">
      <div class="sb"><div class="snum">[0, 1]</div><div class="slbl en">Normalized Risk Range</div><div class="slbl ar" style="display:none">مدى تقييم الخطر المعياري</div></div>
      <div class="sb"><div class="snum">Distinct</div><div class="slbl en">Risk vs. Confidence Outputs</div><div class="slbl ar" style="display:none">فصل الخطر عن مؤشر الثقة</div></div>
      <div class="sb"><div class="snum">Separated</div><div class="slbl en">Engine vs. Action Execution</div><div class="slbl ar" style="display:none">فصل التحليل عن التنفيذ</div></div>
    </div>'''

if old_s17_content in html:
    html = html.replace(old_s17_content, new_s17_content, 1)
    print("✓ Slide 17 updated with verbatim §3.5 analytical outputs")
else:
    print("✗ Slide 17 content NOT found")

# ============================================================
# 5. SLIDE 18: Prioritization, Suppression, and Policy Overrides (§3.5)
# ============================================================
old_s18_cards = '''    <div class="grid g3">
      <div class="card">
        <div class="c-icon gr"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
        <h3 class="ct en">Automated Noise Suppression</h3><h3 class="ct ar" style="display:none">قمع الضجيج المؤكد آلياً</h3>
        <p class="en">Alerts with Risk &lt; 25 and high benign confidence (&Phi; &gt; 0.95) are auto-resolved and tagged with reasoning, bypassing analyst screens entirely.</p>
        <p class="ar" style="display:none">إغلاق التنبيهات منخفضة الخطورة وعالية اليقين بأنها حميدة تلقائياً مع توثيق السبب لتفريغ شاشات المحللين.</p>
      </div>
      <div class="card">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
        <h3 class="ct en">Dynamic Queue Promotion</h3><h3 class="ct ar" style="display:none">الترقية اللحظية لقائمة الانتظار</h3>
        <p class="en">Incidents are ordered dynamically by composite Risk score rather than arrival timestamp. Critical ransomware indicators leapfrog ahead of 500 routine logs.</p>
        <p class="ar" style="display:none">إعادة فرز قائمة الانتظار بناءً على الخطر اللحظي الفعلي؛ يقفز حادث الفدية المشبوه فوراً إلى أعلى القائمة أمام مئات السجلات الروتينية.</p>
      </div>
      <div class="card">
        <div class="c-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <h3 class="ct en">Anti-Starvation Aging</h3><h3 class="ct ar" style="display:none">خوارزمية منع الركود الزمني</h3>
        <p class="en">An aging factor ensures low-priority alerts do not remain permanently neglected in queues by gradually incrementing priority after SLA thresholds.</p>
        <p class="ar" style="display:none">خوارزمية تصعيد زمني تضمن عدم إهمال التنبيهات المتوسطة إلى الأبد عبر رفع أولويتها تدريجياً عند اقتراب انتهاء مهلة SLA.</p>
      </div>
    </div>'''

new_s18_cards = '''    <div class="grid g3">
      <div class="card">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg></div>
        <h3 class="ct en">Dynamic Queue Prioritization</h3><h3 class="ct ar" style="display:none">ترتيب قوائم الانتظار ديناميكياً</h3>
        <p class="en">Converts analytical outputs into operational decisions about alert ordering. Alerts are ranked by continuous contextual risk rather than static product severity. Relative positions are recalculated dynamically as new telemetry arrives (Wang et al., 2024).</p>
        <p class="ar" style="display:none">تحويل مخرجات التحليل إلى قرارات تشغيلية لترتيب طوابير التحقيق بناءً على الخطر اللحظي المحدث بدلاً من الشدة الثابتة للمنتج المصدر.</p>
      </div>
      <div class="card">
        <div class="c-icon gr"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
        <h3 class="ct en">Suppression vs. Deprioritization</h3><h3 class="ct ar" style="display:none">القمع المنضبط مقابل خفض الأولوية</h3>
        <p class="en">Suppressed alerts are excluded from primary queues under explicit policy (low risk, adequate confidence, non-critical assets) but retained for audit. Deprioritized alerts remain visible below higher-risk events, preserving complete operational traceability.</p>
        <p class="ar" style="display:none">فصل مفهومي دقيق: التنبيهات المقموعة تُستثنى من الطابور النشط وفق شروط صارمة مع أرشفتها للتدقيق، بينما التنبيهات مخفضة الأولوية تظل متاحة تحت الأحداث الأكثر خطورة.</p>
      </div>
      <div class="card">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h3 class="ct en">Policy Safeguards &amp; Overrides</h3><h3 class="ct ar" style="display:none">ضمانات السياسات والاستثناءات</h3>
        <p class="en">Operational rules override model scores when critical assets, privileged accounts, or novel threats are detected. Low-confidence predictions are automatically routed for analyst review, ensuring ML cannot permanently discard uncertain events (§3.5).</p>
        <p class="ar" style="display:none">قواعد تشغيلية تعلو على تنبؤات النموذج عند ارتباط الحدث بأصول حساسة أو هويات إدارية، مع توجيه الحالات منخفضة الثقة للمحلل البشري حتماً.</p>
      </div>
    </div>'''

if old_s18_cards in html:
    html = html.replace(old_s18_cards, new_s18_cards, 1)
    print("✓ Slide 18 updated with verbatim §3.5 prioritization text")
else:
    print("✗ Slide 18 cards NOT found")

# ============================================================
# 6. SLIDE 19: Arabic translation for Policy Principle
# ============================================================
old_s19_ar = '''<p class="ar" style="display:none"><strong>سجل العمليات غير القابل للتعديل:</strong> يتم توثيق كافة العمليات المؤتمتة مشفرة بأوقاتها وأهدافها لضمان المحاسبية الكاملة.</p>'''
new_s19_ar = '''<p class="ar" style="display:none"><strong>مبدأ سياسة الاستجابة (§3.7):</strong> يراعي قرار أتمتة الإجراء الأثر التشغيلي المحتمل للاستجابة ذاتها إلى جانب تقدير المخاطر؛ فالاستعلام عن سياق التهديد يحمل مخاطر تشغيلية أقل بكثير من عزل خادم إنتاج أو تجميد حساب ذي صلاحيات واسعة أو تعديل سياسات الجدار الناري.</p>'''

if old_s19_ar in html:
    html = html.replace(old_s19_ar, new_s19_ar, 1)
    print("✓ Slide 19 Arabic policy principle updated")
else:
    print("✗ Slide 19 Arabic policy principle NOT found")

# ============================================================
# 7. SLIDE 22: Design Science Research Phases (§1.5)
# ============================================================
old_s22_cards = '''        <p class="en">Dataset curation, feature engineering pipeline, simulated enterprise telemetry, and baseline pre-processing.</p>
        <p class="ar" style="display:none">إعداد بيانات التدريب وهندسة الخصائص وإعداد بيئة الاختبار المعملية لمحاكاة شبكات المؤسسات.</p>'''
new_s22_cards = '''        <p class="en">Preparing security alert datasets, performing feature engineering, simulated enterprise telemetry, and baseline pre-processing. Planned for Graduation Project 2 (§1.5).</p>
        <p class="ar" style="display:none">تجهيز مجموعات بيانات التنبيهات الأمنية، هندسة الخصائص، ومحاكاة القياسات المؤسسية (مخطط للتنفيذ في مشروع التخرج 2).</p>'''

if old_s22_cards in html:
    html = html.replace(old_s22_cards, new_s22_cards, 1)
    print("✓ Slide 22 Phase 4 updated")

old_s22_p5 = '''        <p class="en">Implementation of AI triage engine, REST API connectors, and execution of automated response playbooks.</p>
        <p class="ar" style="display:none">البرمجة الفعلية لمحرك الفرز وتكامل واجهات الربط مع منصات الاستجابة ودفاتر العمل.</p>'''
new_s22_p5 = '''        <p class="en">Developing the selected AI/ML mechanism, training algorithms, and establishing calibrated risk scoring. Planned for Graduation Project 2 (§1.5).</p>
        <p class="ar" style="display:none">تطوير نموذج الذكاء الاصطناعي/تعلم الآلة المختار، تدريب الخوارزميات، ومعايرة درجات المخاطر (مخطط لمشروع التخرج 2).</p>'''

if old_s22_p5 in html:
    html = html.replace(old_s22_p5, new_s22_p5, 1)
    print("✓ Slide 22 Phase 5 updated")

old_s22_p6 = '''        <p class="en">Assessing classification accuracy, False Positive Reduction rate, and MTTR reduction against baseline SOAR.</p>
        <p class="ar" style="display:none">قياس دقة التنبؤ، معدل خفض الإنذارات الكاذبة، وسرعة احتواء الهجمات مقارنة بالوضع التقليدي.</p>'''
new_s22_p6 = '''        <p class="en">Connecting intelligent analysis with SOAR response workflows; prototype testing and evaluation using ML metrics (AUC, FPR) and operational measures (wait-time, MTTR). Graduation Project 2 (§1.5).</p>
        <p class="ar" style="display:none">ربط التحليل الذكي مع دفاتر عمل SOAR؛ اختبار النموذج الأولي وتقييمه بمقاييس تعلم الآلة والمؤشرات التشغيلية في مشروع 2.</p>'''

if old_s22_p6 in html:
    html = html.replace(old_s22_p6, new_s22_p6, 1)
    print("✓ Slide 22 Phase 6 updated")

# ============================================================
# 8. SLIDE 25: Add Challenges & Mitigations Table (Guide §9 requirement)
# ============================================================
old_s25_grid = '''    <div class="grid g2" style="gap:20px;width:100%">
      <div class="card" style="border-color:rgba(0,212,255,0.4)">
        <h3 class="ct en" style="color:var(--s)">Completed in Project 1 (Chapters 1-3)</h3>
        <h3 class="ct ar" style="display:none;color:var(--s)">ما تم إنجازه في مشروع 1 (الفصول 1 - 3)</h3>
        <ul style="gap:8px;margin-top:8px">
          <li class="en"><strong style="color:var(--ok)">&#10003; Problem Definition:</strong> Analysis of SOC alert fatigue, context switching, static triage limitations, and prioritization gaps.</li>
          <li class="ar" style="display:none"><strong style="color:var(--ok)">&#10003; توصيف المشكلة:</strong> دراسة دقيقة لأزمة إرهاق التنبيهات وتحديد الأهداف.</li>
          <li class="en"><strong style="color:var(--ok)">&#10003; Literature Review &amp; Gap Analysis:</strong> Reviewed AI/ML approaches, SOAR frameworks, and identified the integration gap between intelligent triage and automated response.</li>
          <li class="ar" style="display:none"><strong style="color:var(--ok)">&#10003; مراجعة الأدبيات:</strong> تحديد الفجوة البحثية ومقارنة تقنيات التعلم الآلي.</li>
          <li class="en"><strong style="color:var(--ok)">&#10003; System Architecture (Chapter 3):</strong> Modular pipeline design covering Ingestion, Context Enrichment, AI/ML Engine, Response Policy, and Feedback Loop.</li>
          <li class="ar" style="display:none"><strong style="color:var(--ok)">&#10003; التصميم المعماري:</strong> بناء معمارية الطبقات الخمس ونموذج تقييم المخاطر.</li>
        </ul>
      </div>
      <div class="card" style="border-color:rgba(108,99,255,0.4)">
        <h3 class="ct en" style="color:#a8a0ff">Project 2 Execution Roadmap (Chapters 4-6)</h3>
        <h3 class="ct ar" style="display:none;color:#a8a0ff">خارطة تنفيذ مشروع 2 (الفصول 4 - 6)</h3>
        <ul style="gap:8px;margin-top:8px">
          <li class="en"><strong>Phase 4 (Weeks 1-4):</strong> Dataset curation, feature engineering &amp; pipeline setup.</li>
          <li class="ar" style="display:none"><strong>المرحلة 4 (الأسابيع 1-4):</strong> تجهيز البيانات وهندسة الخصائص وإعداد بيئة العمل.</li>
          <li class="en"><strong>Phase 5 (Weeks 5-8):</strong> Model training (RF/SAC), REST API connector coding.</li>
          <li class="ar" style="display:none"><strong>المرحلة 5 (الأسابيع 5-8):</strong> تدريب النماذج وبرمجة موصلات واجهات API وأدلة العمل.</li>
          <li class="en"><strong>Phase 6 (Weeks 9-12):</strong> Prototype testing, benchmark evaluation &amp; final thesis defense.</li>
          <li class="ar" style="display:none"><strong>المرحلة 6 (الأسابيع 9-12):</strong> الاختبار التجريبي الشامل، قياس الأداء ومناقشة التخرج النهائية.</li>
        </ul>
      </div>
    </div>'''

new_s25_grid = '''    <div class="grid g3" style="gap:14px;width:100%">
      <div class="card" style="border-color:rgba(0,212,255,0.4)">
        <h3 class="ct en" style="color:var(--s);font-size:0.85rem">Completed in GP1 (Chapters 1-3)</h3>
        <h3 class="ct ar" style="display:none;color:var(--s);font-size:0.85rem">ما تم إنجازه في مشروع 1 (الفصول 1 - 3)</h3>
        <ul style="gap:6px;margin-top:6px;font-size:0.75rem">
          <li class="en"><strong style="color:var(--ok)">&#10003; Problem &amp; Objectives (§1.2-1.4):</strong> Empirical analysis of alert fatigue, context switching, and static triage limitations.</li>
          <li class="ar" style="display:none"><strong style="color:var(--ok)">&#10003; توصيف المشكلة:</strong> دراسة دقيقة لأزمة إرهاق التنبيهات وتحديد الأهداف.</li>
          <li class="en"><strong style="color:var(--ok)">&#10003; Literature Synthesis (§2.4-2.5):</strong> Coded Table 2-1 and validated the downstream SOAR integration gap.</li>
          <li class="ar" style="display:none"><strong style="color:var(--ok)">&#10003; مراجعة الأدبيات:</strong> توثيق جدول 2-1 وإثبات فجوة التكامل مع SOAR.</li>
          <li class="en"><strong style="color:var(--ok)">&#10003; System Architecture (Chapter 3):</strong> High-level design: Ingestion, Enrichment, ML Engine, Policy, &amp; Feedback.</li>
          <li class="ar" style="display:none"><strong style="color:var(--ok)">&#10003; التصميم المعماري:</strong> معمارية الطبقات الخمس المكتملة في الفصل الثالث.</li>
        </ul>
      </div>
      <div class="card" style="border-color:rgba(255,179,0,0.4)">
        <h3 class="ct en" style="color:var(--wa);font-size:0.85rem">Challenges &amp; Mitigations (Guide §9)</h3>
        <h3 class="ct ar" style="display:none;color:var(--wa);font-size:0.85rem">التحديات والإجراءات المتخذة (دليل §9)</h3>
        <ul style="gap:6px;margin-top:6px;font-size:0.75rem">
          <li class="en"><strong>Alert Schema Variance:</strong> <em>Mitigation:</em> Implemented schema normalization layer in Ingestion Module (§3.3). [Resolved]</li>
          <li class="ar" style="display:none"><strong>تباين صيغ السجلات:</strong> <em>الإجراء:</em> بناء طبقة توحيد البنية في وحدة الاستيعاب (§3.3). [مكتمل]</li>
          <li class="en"><strong>Dataset Constraints (§1.6):</strong> <em>Mitigation:</em> Utilizing curated public SOC datasets + synthetic attack logs. [In Progress]</li>
          <li class="ar" style="display:none"><strong>محدودية البيانات:</strong> <em>الإجراء:</em> استخدام بيانات SOC العامة وتوليد محاكاة هجمات معيارية. [قيد التنفيذ]</li>
          <li class="en"><strong>Automation Risk (§3.7):</strong> <em>Mitigation:</em> Enforced human-in-the-loop gates for high-impact actions. [Resolved]</li>
          <li class="ar" style="display:none"><strong>مخاطر الأتمتة:</strong> <em>الإجراء:</em> فرض بوابات إشراف بشري للإجراءات عالية التأثير. [مكتمل]</li>
        </ul>
      </div>
      <div class="card" style="border-color:rgba(108,99,255,0.4)">
        <h3 class="ct en" style="color:#a8a0ff;font-size:0.85rem">GP2 Execution Roadmap (Chapters 4-6)</h3>
        <h3 class="ct ar" style="display:none;color:#a8a0ff;font-size:0.85rem">خارطة تنفيذ مشروع 2 (الفصول 4 - 6)</h3>
        <ul style="gap:6px;margin-top:6px;font-size:0.75rem">
          <li class="en"><strong>Phase 4 (Weeks 1-4):</strong> Dataset curation, feature engineering &amp; pipeline setup.</li>
          <li class="ar" style="display:none"><strong>المرحلة 4 (الأسابيع 1-4):</strong> تجهيز البيانات وهندسة الخصائص وإعداد البيئة.</li>
          <li class="en"><strong>Phase 5 (Weeks 5-8):</strong> ML model training (RF/SAC) &amp; SOAR API connector coding.</li>
          <li class="ar" style="display:none"><strong>المرحلة 5 (الأسابيع 5-8):</strong> تدريب النماذج وبرمجة موصلات واجهات API وأدلة العمل.</li>
          <li class="en"><strong>Phase 6 (Weeks 9-12):</strong> Prototype testing, metric benchmarking &amp; final defense.</li>
          <li class="ar" style="display:none"><strong>المرحلة 6 (الأسابيع 9-12):</strong> الاختبار التجريبي، تقييم الأداء والمناقشة النهائية.</li>
        </ul>
      </div>
    </div>'''

if old_s25_grid in html:
    html = html.replace(old_s25_grid, new_s25_grid, 1)
    print("✓ Slide 25 updated with Challenges & Mitigations card (Guide §9 compliant)")
else:
    print("✗ Slide 25 grid NOT found")

with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished updating index.html! New length:", len(html))
