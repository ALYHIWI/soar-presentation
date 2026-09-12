# -*- coding: utf-8 -*-
import re

s2_new = '''<section class="slide" id="s2">
  <div class="orb o2" style="opacity:0.35"></div>
  <div class="content-box">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
      <span class="en">Chapter 1 &ndash; Operational Context (§1.1-1.2)</span><span class="ar" style="display:none">الفصل الأول &ndash; السياق التشغيلي (§1.1-1.2)</span>
    </div>
    <h2 class="st en">The Modern SOC Operational Landscape</h2>
    <h2 class="st ar" style="display:none">المشهد التشغيلي لمراكز العمليات الأمنية الحديثة (SOC)</h2>
    <div class="gl"></div>
    <p class="lead en">A Security Operations Center (SOC) centralizes cyber threat monitoring, detection, and incident response, but faces acute operational strain from massive log volumes and heterogeneous data schemas (§1.1).</p>
    <p class="lead ar" style="display:none">مركز العمليات الأمنية (SOC) هو الوحدة المركزية لرصد التهديدات والاستجابة لها، لكنه يواجه تعقيداً تشغيلياً كبيراً بسبب طوفان البيانات وتشتت السجلات الأمنية (§1.1).</p>
    <div class="grid g3">
      <div class="card">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg></div>
        <h3 class="ct en">Data Influx &amp; SIEM Role</h3><h3 class="ct ar" style="display:none">طوفان البيانات ودور SIEM</h3>
        <p class="en">Organizations implement SIEM platforms for centralized log management, security-event collection, and basic correlation. Accumulating up to 100 gigabytes of log and alert data daily, a substantial portion may consist of false positives and non-actionable noise (§1.1, §1.2).</p>
        <p class="ar" style="display:none">تجميع غيغابايتات من السجلات يومياً من حساسات الشبكة والأنظمة الطرفية؛ تقوم منصات SIEM بمركزة السجلات وإجراء المطابقات الأولية لكنها تواجه طوفاناً من الإنذارات غير الإجرائية (§1.1, §1.2).</p>
      </div>
      <div class="card">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h3 class="ct en">Heterogeneous Tool Stacks</h3><h3 class="ct ar" style="display:none">تشتت الأدوات الأمنية</h3>
        <p class="en">Security monitoring relies on diverse outputs from multi-vendor security stacks. Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous and complex to analyze (§1.1).</p>
        <p class="ar" style="display:none">بيانات أمنية بصيغ متباينة وغير موحدة صادرة من أدوات متعددة الموردين، مما يخلق عزلة بين الأنظمة ويعيق الرؤية الأمنية الموحدة للمحللين (§1.1).</p>
      </div>
      <div class="card">
        <div class="c-icon ye"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <h3 class="ct en">Tiered Analyst Hierarchy</h3><h3 class="ct ar" style="display:none">هرمية المحللين المرهقة</h3>
        <p class="en">Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, following standard operating procedures to evaluate whether an alert is a legitimate threat or benign activity, manually gathering contextual evidence across disparate sources (§1.1).</p>
        <p class="ar" style="display:none">هيكلية تشغيلية هرمية يجري فيها المحللون المبتدئون فرزاً أولياً لآلاف التنبيهات باتباع إجراءات قياسية، مما يتطلب جمعاً يدوياً للأدلة من شاشات متباينة ويرهق الكوادر البشرية (§1.1).</p>
      </div>
    </div>
    <div class="srow" style="margin-top:14px">
      <div class="sb">
        <div class="snum">100 GB</div>
        <div class="slbl en">Daily Log &amp; Alert Influx</div>
        <div class="slbl ar" style="display:none">تراكم السجلات والتنبيهات يومياً</div>
        <div class="sref en">Document Source: §1.2</div>
        <div class="sref ar" style="display:none">المصدر: توثيق المشروع §1.2</div>
      </div>
      <div class="sb">
        <div class="snum">22.9%</div>
        <div class="slbl en">Queue Dwell Time Reduction</div>
        <div class="slbl ar" style="display:none">تقليص زمن انتظار الحوادث الحرجة</div>
        <div class="sref en">Ref: Gelman et al. (2023) / §1.2</div>
        <div class="sref ar" style="display:none">المرجع: جيلمان وآخرون (2023) / §1.2</div>
      </div>
      <div class="sb">
        <div class="snum">54%</div>
        <div class="slbl en">FP Suppression (95.1% Capture)</div>
        <div class="slbl ar" style="display:none">قمع الإنذارات الكاذبة (مع التقاط 95.1%)</div>
        <div class="sref en">Ref: Gelman et al. (2023) / §2.4.1</div>
        <div class="sref ar" style="display:none">المرجع: جيلمان وآخرون (2023) / §2.4.1</div>
      </div>
    </div>
  </div>
  <div class="sn">03 / 25</div>
</section>'''

s19_new = '''<section class="slide" id="s19">
  <div class="orb o2" style="opacity:0.4"></div>
  <div class="content-box">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/></svg>
      <span class="en">Chapter 3 &ndash; Controlled Autonomy (§3.7)</span><span class="ar" style="display:none">الفصل الثالث &ndash; بوابات التحكم والرقابة (§3.7)</span>
    </div>
    <h2 class="st en">Human-AI Teaming: Policy States &amp; Controlled Decision Gates</h2>
    <h2 class="st ar" style="display:none">تكامل الإنسان والذكاء: حالات السياسة وبوابات القرار المنضبطة</h2>
    <div class="gl"></div>
    <div class="grid g4" style="gap:12px">
      <div class="card" style="border-color:rgba(0,230,118,0.3)">
        <div class="c-icon gr"><span style="font-weight:900;font-size:0.9rem">S1</span></div>
        <h3 class="ct en" style="color:var(--ok);font-size:0.85rem">Automated Response</h3><h3 class="ct ar" style="display:none;color:var(--ok);font-size:0.85rem">المستوى 1: استجابة مؤتمتة</h3>
        <p class="en" style="font-size:0.75rem"><strong>High Confidence + Low Blast Radius:</strong> Executes approved low-risk or well-defined response workflows when policy conditions are satisfied (enrichment queries, internal correlation, noise suppression) without requiring human intervention (§3.7).</p>
        <p class="ar" style="display:none;font-size:0.75rem"><strong>ثقة عالية ومخاطر تشغيلية منخفضة:</strong> تنفيذ دفاتر عمل معتمدة ومنخفضة الخطورة عند تحقق شروط السياسة (استعلامات الإثراء، قمع الضجيج المعياري، وإرسال الإشعارات) دون إبطاء (§3.7).</p>
      </div>
      <div class="card" style="border-color:rgba(255,179,0,0.3)">
        <div class="c-icon ye"><span style="font-weight:900;font-size:0.9rem">S2</span></div>
        <h3 class="ct en" style="color:var(--wa);font-size:0.85rem">Human Approval Required</h3><h3 class="ct ar" style="display:none;color:var(--wa);font-size:0.85rem">المستوى 2: اشتراط الموافقة</h3>
        <p class="en" style="font-size:0.75rem"><strong>Operational Consequences:</strong> Generates a recommended response action but requires explicit analyst authorization before execution. Applied to containment actions such as endpoint isolation or credential suspension (§3.7).</p>
        <p class="ar" style="display:none;font-size:0.75rem"><strong>إجراءات ذات أثر تشغيلي:</strong> توليد توصية استجابة محددة مع اشتراط مصادقة المحلل البشري قبل التنفيذ؛ مثل عزل جهاز طرفي أو تعليق حسابات تجنباً لتعطيل الأعمال (§3.7).</p>
      </div>
      <div class="card" style="border-color:rgba(255,107,107,0.3)">
        <div class="c-icon rd"><span style="font-weight:900;font-size:0.9rem">S3</span></div>
        <h3 class="ct en" style="color:var(--acc);font-size:0.85rem">Analyst Investigation</h3><h3 class="ct ar" style="display:none;color:var(--acc);font-size:0.85rem">المستوى 3: تحقيق المحلل</h3>
        <p class="en" style="font-size:0.75rem"><strong>Low Confidence or Critical Assets:</strong> Forwards the alert to the active analyst queue for comprehensive manual validation. Triggered when model confidence is low, risk is ambiguous, or high-criticality assets are affected (§3.7).</p>
        <p class="ar" style="display:none;font-size:0.75rem"><strong>ثقة منخفضة أو أصول حرجة:</strong> توجيه التنبيه لطابور المحلل للتحقيق الشامل عند تدني ثقة النموذج أو ارتباط التنبيه بخوادم الإنتاج الرئيسية أو هويات سيادية (§3.7).</p>
      </div>
      <div class="card" style="border-color:rgba(0,212,255,0.3)">
        <div class="c-icon cy"><span style="font-weight:900;font-size:0.9rem">S4</span></div>
        <h3 class="ct en" style="color:var(--s);font-size:0.85rem">Monitor / Record</h3><h3 class="ct ar" style="display:none;color:var(--s);font-size:0.85rem">المستوى 4: المراقبة والتوثيق</h3>
        <p class="en" style="font-size:0.75rem"><strong>Audit &amp; Baseline Telemetry:</strong> Retains the alert and all associated contextual evidence in the security dossier without initiating containment actions, preserving full retrospective auditability (§3.7).</p>
        <p class="ar" style="display:none;font-size:0.75rem"><strong>الأرشفة والمراقبة المستمرة:</strong> الاحتفاظ بالتنبيه وكافة الأدلة السياقية المرتبطة به في السجل الأمني لأغراض التدقيق والتحليل التاريخي دون إطلاق إجراءات احتواء (§3.7).</p>
      </div>
    </div>
    <div class="hl" style="margin-top:12px">
      <p class="en"><strong>Controlled Autonomy Principle (§3.7):</strong> The decision to automate an action considers not only the estimated security risk but also the potential operational impact of the response itself (Chhetri et al., 2024). Strict policy safeguards prevent automatic suppression of critical assets or privileged identities regardless of model score.</p>
      <p class="ar" style="display:none"><strong>مبدأ الأتمتة المنضبطة (§3.7):</strong> قرار الأتمتة لا يكتفي بحساب درجة الخطر الأمني بل يوازن الأثر التشغيلي للاستجابة ذاتها (Chhetri et al., 2024)، مع حظر قمع أي تنبيه يرتبط بأصول بالغة الأهمية أو حسابات حساسة مهما كانت تنبؤات النموذج.</p>
    </div>
  </div>
  <div class="sn">20 / 25</div>
</section>'''

s22_new = '''<section class="slide" id="s22">
  <div class="orb o1" style="opacity:0.35"></div>
  <div class="content-box">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
      <span class="en">Chapter 3 &ndash; System Architecture &sect;3.2-3.3, &sect;1.6</span><span class="ar" style="display:none">الفصل الثالث &ndash; المعمارية وبيئة المحاكاة &sect;3.2-3.3, &sect;1.6</span>
    </div>
    <h2 class="st en">System Architecture &amp; Prototype Integration Environment</h2>
    <h2 class="st ar" style="display:none">معمارية النظام وبيئة التكامل والمحاكاة للنموذج الأولي</h2>
    <div class="gl"></div>
    <div class="grid g4">
      <div class="card">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/></svg></div>
        <h3 class="ct en">Multi-Agent Layer</h3><h3 class="ct ar" style="display:none">طبقة الوكلاء الأذكياء</h3>
        <p class="en">Informed by Agrawal et al. (2026): Attacker Agent simulates adaptive multi-stage cyber attacks in a controlled testbed; Defender Agent coordinates intelligent alert analysis, risk scoring, and decision support (§3.2.1).</p>
        <p class="ar" style="display:none">بناءً على Agrawal et al. (2026): عميل المهاجم يحاكي سيناريوهات هجومية متعددة المراحل في بيئة محاكاة منضبطة؛ وعميل المدافع ينسق تحليل التنبيهات وتقييم المخاطر ودعم القرار (§3.2.1).</p>
      </div>
      <div class="card">
        <div class="c-icon gr"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/></svg></div>
        <h3 class="ct en">Ingestion &amp; Connectors</h3><h3 class="ct ar" style="display:none">الاستيعاب وموصلات المصادر</h3>
        <p class="en">Connectors interface with SIEM, EDR, IDS, and network telemetry via REST APIs, webhooks, or log streams, standardizing heterogeneous alerts into normalized schemas while retaining source provenance (§3.3).</p>
        <p class="ar" style="display:none">موصلات مخصصة للتكامل مع منصات SIEM و EDR وحساسات الشبكة عبر واجهات REST أو تدفق السجلات، مع توحيد الحقول والحفاظ على تتبع المصدر الأصلي للحدث (§3.3).</p>
      </div>
      <div class="card">
        <div class="c-icon ye"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/></svg></div>
        <h3 class="ct en">Analytical Scoring Engine</h3><h3 class="ct ar" style="display:none">محرك التحليل والتقييم</h3>
        <p class="en">Processes multi-dimensional context (asset criticality, identity sensitivity, threat intelligence) to compute continuous risk scores [0, 1] and confidence indicators for dynamic queue prioritization (§3.4, §3.5).</p>
        <p class="ar" style="display:none">معالجة السياق متعدد الأبعاد (حساسية الأصول، صلاحيات الهوية، واستخبارات التهديدات) لاحتساب درجة خطر معيارية [0, 1] ومؤشر ثقة لإدارة الطوابير ديناميكياً (§3.4, §3.5).</p>
      </div>
      <div class="card">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/></svg></div>
        <h3 class="ct en">SOAR API Playbooks</h3><h3 class="ct ar" style="display:none">دفاتر عمل SOAR والواجهات</h3>
        <p class="en">Translates approved response decisions into automated API executions across target security controls (host isolation, indicator blocking) governed by policy safeguards (Karlzén &amp; Sommestad, 2023; Sworna et al., 2023; §3.7).</p>
        <p class="ar" style="display:none">ترجمة قرارات الاستجابة المعتمدة إلى إجراءات منفذة عبر واجهات البرمجة API (عزل الأجهزة، حظر العناوين) محكومة بضمانات السياسات وإشراف المحلل البشري (§3.7).</p>
      </div>
    </div>
    <div class="hl" style="margin-top:14px">
      <p class="en"><strong>Graduation Project Scope &amp; Simulation Testbed (§1.6.1):</strong> The project focuses on architectural integration and prototype evaluation within a controlled laboratory and simulation environment appropriate for academic research, using benchmark datasets rather than live proprietary enterprise SOCs (§1.6.2).</p>
      <p class="ar" style="display:none"><strong>نطاق المشروع وبيئة المحاكاة (§1.6.1):</strong> يركز المشروع على التكامل المعماري والتقييم التجريبي ضمن بيئة محاكاة واختبار معملية منضبطة تناسب المشروعات الأكاديمية، معتمدة على مجموعات بيانات معيارية بدلاً من بيئات الشركات التجارية المغلقة (§1.6.2).</p>
    </div>
  </div>
  <div class="sn">23 / 25</div>
</section>'''

s23_new = '''<section class="slide" id="s23">
  <div class="orb o2" style="opacity:0.4"></div>
  <div class="content-box">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
      <span class="en">Chapter 3 &ndash; Operational Workflow &amp; Literature Benchmarks (§3.2, §3.7, §2.4)</span><span class="ar" style="display:none">الفصل الثالث &ndash; مسار المعالجة التشغيلي والمقارنات المعيارية للأدبيات (§3.2, §3.7, §2.4)</span>
    </div>
    <h2 class="st en">Operational Incident Handling Workflow &amp; Empirical Benchmarks</h2>
    <h2 class="st ar" style="display:none">مسار المعالجة التشغيلي للحوادث والمؤشرات المعيارية من الأدبيات</h2>
    <div class="gl"></div>
    <div class="grid g2" style="gap:20px">
      <div class="card" style="padding:14px">
        <h3 class="ct en" style="color:var(--acc)">End-to-End Operational Pipeline (§3.2)</h3>
        <h3 class="ct ar" style="display:none;color:var(--acc)">المسار التشغيلي المتكامل لمعالجة الحادث (§3.2)</h3>
        <div class="tl" style="margin-top:10px">
          <div class="ti">
            <div class="td" style="font-size:0.7rem">1</div>
            <div class="tic">
              <h4 class="en" style="font-size:0.8rem">1. Alert Ingestion &amp; Normalization (§3.3)</h4><h4 class="ar" style="display:none;font-size:0.8rem">1. استيعاب التنبيه وتوحيد الحقول (§3.3)</h4>
              <p class="en">Raw telemetry from detection sensors is validated, normalized into standard schema, and tagged with source provenance.</p>
              <p class="ar" style="display:none">استقبال السجلات غير الموحدة من الحساسات والتحقق من صحتها وتوحيد حقولها مع حفظ مصدر الحدث.</p>
            </div>
          </div>
          <div class="ti">
            <div class="td" style="font-size:0.7rem">2</div>
            <div class="tic">
              <h4 class="en" style="font-size:0.8rem">2. Multi-Dimensional Context Enrichment (§3.4)</h4><h4 class="ar" style="display:none;font-size:0.8rem">2. إثراء السياق متعدد الأبعاد (§3.4)</h4>
              <p class="en">Attaches asset business criticality, user identity sensitivity, and external threat intelligence indicators.</p>
              <p class="ar" style="display:none">ربط التنبيه بحساسية الأصل وهوية المستخدم وصلاحياته واستعلام سمعة المؤشرات الخارجية.</p>
            </div>
          </div>
          <div class="ti">
            <div class="td" style="font-size:0.7rem">3</div>
            <div class="tic">
              <h4 class="en" style="font-size:0.8rem">3. AI Triage &amp; Risk Scoring (§3.5)</h4><h4 class="ar" style="display:none;font-size:0.8rem">3. التقييم الذكي للمخاطر (§3.5)</h4>
              <p class="en">Defender Agent computes continuous contextual risk score R &isin; [0, 1] and calibrated model confidence indicator.</p>
              <p class="ar" style="display:none">عميل المدافع يحتسب درجة الخطر السياقي المعيارية ومؤشر يقين النموذج لفرز الحادث.</p>
            </div>
          </div>
          <div class="ti">
            <div class="td" style="font-size:0.7rem">4</div>
            <div class="tic">
              <h4 class="en" style="font-size:0.8rem">4. Dynamic Prioritization &amp; Policy Gate (§3.6, §3.7)</h4><h4 class="ar" style="display:none;font-size:0.8rem">4. الترتيب الديناميكي وبوابة السياسات (§3.6, §3.7)</h4>
              <p class="en">Queue dynamically reordered; policy gate selects between autonomous action, human approval, or analyst escalation.</p>
              <p class="ar" style="display:none">إعادة ترتيب الطابور ديناميكياً وبوابة السياسات تحدد مستوى الإشراف البشري المطلوب قبل التنفيذ.</p>
            </div>
          </div>
          <div class="ti">
            <div class="td" style="font-size:0.7rem">5</div>
            <div class="tic">
              <h4 class="en" style="font-size:0.8rem">5. Controlled SOAR Execution &amp; Feedback (§3.7, §3.8)</h4><h4 class="ar" style="display:none;font-size:0.8rem">5. التنفيذ عبر SOAR وتسجيل التغذية (§3.7, §3.8)</h4>
              <p class="en">Playbook executes defensive API actions; analyst resolution and execution outcomes logged for offline model refinement.</p>
              <p class="ar" style="display:none">تنفيذ تدابير الاستجابة عبر دفاتر SOAR وتسجيل قرارات المحلل وأثر الإجراء لدعم التحسين المستمر.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="card" style="padding:14px;background:rgba(0,0,0,0.4)">
        <h3 class="ct en" style="color:var(--ok)">Empirical Benchmarks from Literature</h3>
        <h3 class="ct ar" style="display:none;color:var(--ok)">المؤشرات والأرقام المعيارية المثبتة بالأدبيات</h3>
        <div class="srow" style="flex-direction:column;gap:10px;margin-top:10px">
          <div class="sb" style="text-align:left;border-color:rgba(0,212,255,0.4);padding:10px">
            <div style="display:flex;justify-content:space-between;align-items:center">
              <span class="en" style="font-size:0.8rem;font-weight:700;color:var(--s)">Queue Dwell Time Reduction (§1.2)</span>
              <span class="ar" style="display:none;font-size:0.8rem;font-weight:700;color:var(--s)">تقليص زمن انتظار الحوادث الحرجة (§1.2)</span>
              <span style="font-family:'JetBrains Mono',monospace;font-size:1.15rem;color:var(--s);font-weight:900">22.9%</span>
            </div>
            <p class="en" style="font-size:0.72rem;margin-top:3px;color:var(--t2)">Dynamic risk-based prioritization reduces critical incident waiting time in analyst queues (Gelman et al., 2023).</p>
            <p class="ar" style="display:none;font-size:0.72rem;margin-top:3px;color:var(--t2)">الترتيب الديناميكي الواعي بالمخاطر يقلص زمن انتظار الحوادث الحرجة بنسبة 22.9% مقارنة بالطوابير التقليدية.</p>
          </div>
          <div class="sb" style="text-align:left;border-color:rgba(0,230,118,0.4);padding:10px">
            <div style="display:flex;justify-content:space-between;align-items:center">
              <span class="en" style="font-size:0.8rem;font-weight:700;color:var(--ok)">FP Suppression &amp; Capture Rate (§2.4.1)</span>
              <span class="ar" style="display:none;font-size:0.8rem;font-weight:700;color:var(--ok)">قمع الإنذارات الكاذبة والتقاط الحوادث (§2.4.1)</span>
              <span style="font-family:'JetBrains Mono',monospace;font-size:1.15rem;color:var(--ok);font-weight:900">54% / 95.1%</span>
            </div>
            <p class="en" style="font-size:0.72rem;margin-top:3px;color:var(--t2)">High-recall ML decision thresholds suppress 54% of false positives while capturing 95.1% of actionable incidents (Gelman et al., 2023).</p>
            <p class="ar" style="display:none;font-size:0.72rem;margin-top:3px;color:var(--t2)">عتبات التقييم الذكي قمعت 54% من الإيجابيات الكاذبة مع التقاط 95.1% من الحوادث القابلة للتنفيذ.</p>
          </div>
          <div class="sb" style="text-align:left;border-color:rgba(255,179,0,0.4);padding:10px">
            <div style="display:flex;justify-content:space-between;align-items:center">
              <span class="en" style="font-size:0.8rem;font-weight:700;color:var(--wa)">Model Testing / Inference Time (§2.4.3)</span>
              <span class="ar" style="display:none;font-size:0.8rem;font-weight:700;color:var(--wa)">زمن استدلال النموذج لكل عينة (§2.4.3)</span>
              <span style="font-family:'JetBrains Mono',monospace;font-size:1.15rem;color:var(--wa);font-weight:900">~ 300 &mu;s</span>
            </div>
            <p class="en" style="font-size:0.72rem;margin-top:3px;color:var(--t2)">Off-policy actor-critic reinforcement learning triage achieves sub-millisecond inference time per event sample (Chavali et al., 2024).</p>
            <p class="ar" style="display:none;font-size:0.72rem;margin-top:3px;color:var(--t2)">سرعة استدلال متناهية الصغر في تعلم الآلة المعزز بلغت 300 ميكروثانية لكل عينة أمنية.</p>
          </div>
          <div class="sb" style="text-align:left;border-color:rgba(108,99,255,0.4);padding:10px">
            <div style="display:flex;justify-content:space-between;align-items:center">
              <span class="en" style="font-size:0.8rem;font-weight:700;color:#a8a0ff">Attacker-IP Recall Improvement (§2.4.2)</span>
              <span class="ar" style="display:none;font-size:0.8rem;font-weight:700;color:#a8a0ff">تحسين استرجاع عناوين المهاجمين (§2.4.2)</span>
              <span style="font-family:'JetBrains Mono',monospace;font-size:1.15rem;color:#a8a0ff;font-weight:900">2.25&times;</span>
            </div>
            <p class="en" style="font-size:0.72rem;margin-top:3px;color:var(--t2)">Behavioral context representation improves attacker-associated IP identification up to 2.25 times over static triage (Liu et al., 2022).</p>
            <p class="ar" style="display:none;font-size:0.72rem;margin-top:3px;color:var(--t2)">تمثيل السياق السلوكي ضاعف استرجاع عناوين المهاجمين 2.25 مرة مقارنة بالفرز المعتمد على القواعد الثابتة.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="hl" style="margin-top:12px">
      <p class="en"><strong>Theoretical &amp; Empirical Alignment:</strong> Rather than relying on unverified operational claims, the workflow connects the 5-layer architecture directly with verified empirical metrics from peer-reviewed SOC literature (Chavali et al., 2024; Gelman et al., 2023; Liu et al., 2022).</p>
      <p class="ar" style="display:none"><strong>المطابقة العلمية والعملية:</strong> بدلاً من التقديرات غير الموثقة، يربط المسار التشغيلي طبقات المعمارية الخمس مباشرة بمؤشرات الأداء المثبتة علمياً في أبحاث مراكز العمليات (Chavali et al., 2024; Gelman et al., 2023; Liu et al., 2022).</p>
    </div>
  </div>
  <div class="sn">24 / 25</div>
</section>'''

# Apply replacements
with open(r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_slide(html_text, sid, new_slide_html):
    pattern = r'<section\s+class="slide[^"]*"\s+id="' + sid + r'"[^>]*>.*?</section>'
    assert re.search(pattern, html_text, re.DOTALL), f"Slide {sid} not found in HTML"
    return re.sub(pattern, lambda m: new_slide_html, html_text, count=1, flags=re.DOTALL)

updated_html = replace_slide(html, 's2', s2_new)
updated_html = replace_slide(updated_html, 's19', s19_new)
updated_html = replace_slide(updated_html, 's22', s22_new)
updated_html = replace_slide(updated_html, 's23', s23_new)

# Update s24 Phase 5 bullet
updated_html = updated_html.replace(
    'ML model training (RF/SAC) &amp; SOAR API connector coding.',
    'AI/ML model development, risk scoring calibration (§1.5, §3.5) &amp; SOAR API connector coding.'
)
updated_html = updated_html.replace(
    'تدريب النماذج وبرمجة موصلات واجهات API وأدلة العمل.',
    'تطوير نماذج التعلم ومعايرة درجات المخاطر (§1.5, §3.5) وبرمجة موصلات واجهات البرمجة.'
)

with open('scratch/test_updated_presentation.html', 'w', encoding='utf-8') as f:
    f.write(updated_html)

print("Saved scratch/test_updated_presentation.html successfully!")
