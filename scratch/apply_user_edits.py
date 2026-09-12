# -*- coding: utf-8 -*-
import re

file_path = r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for .sref and .badge-chip
css_to_find = ".id-badge {"
css_addition = """.sref {
  font-size: 0.63rem;
  color: var(--t3);
  margin-top: 5px;
  font-family: 'JetBrains Mono', monospace;
  background: rgba(255, 255, 255, 0.05);
  padding: 2px 7px;
  border-radius: 4px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: inline-block;
  letter-spacing: 0.2px;
}
.badge-chip {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', monospace;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}
.id-badge {"""

if ".sref {" not in html and css_to_find in html:
    html = html.replace(css_to_find, css_addition, 1)
    print("Added CSS for .sref and .badge-chip")

# 2. Update Slide 3 (id="s2")
s03_old_pattern = r'(<!-- ================= S03: MODERN SOC CONTEXT ================= -->\s*<section class="slide" id="s2">.*?)(<!-- ================= S04: PROBLEM STATEMENT \(ALERT FATIGUE\) ================= -->)'

s03_new = '''<!-- ================= S03: MODERN SOC CONTEXT ================= -->
<section class="slide" id="s2">
  <div class="orb o2" style="opacity:0.35"></div>
  <div class="content-box">
    <div class="tag a1">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
      <span class="en">Chapter 1 &ndash; Operational Context</span><span class="ar" style="display:none">الفصل الأول &ndash; السياق التشغيلي</span>
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
        <p class="en">Organizations implement SIEM platforms for centralized log management, security-event collection, and basic correlation. Accumulating up to 100 gigabytes of log and alert data daily, a substantial portion may consist of false positives and non-actionable noise.</p>
        <p class="ar" style="display:none">تجميع غيغابايتات من السجلات يومياً من حساسات الشبكة والأنظمة الطرفية. تقوم أنظمة SIEM بمركزة السجلات وإجراء مطابقات نمطية.</p>
      </div>
      <div class="card">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        <h3 class="ct en">Heterogeneous Tool Stacks</h3><h3 class="ct ar" style="display:none">تشتت الأدوات الأمنية</h3>
        <p class="en">Security monitoring relies on diverse outputs from multi-vendor security stacks. Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous and complex to analyze.</p>
        <p class="ar" style="display:none">بيانات أمنية بصيغ متباينة وغير موحدة، مما يخلق عزلة بين الأدوات ويعيق الرؤية الشاملة للمحللين الأمنيين.</p>
      </div>
      <div class="card">
        <div class="c-icon ye"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
        <h3 class="ct en">Tiered Analyst Hierarchy</h3><h3 class="ct ar" style="display:none">هرمية المحللين المرهقة</h3>
        <p class="en">Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, following standard operating procedures to evaluate whether an incoming alert represents a legitimate threat or benign activity, manually gathering contextual evidence from multiple disparate security sources.</p>
        <p class="ar" style="display:none">يقضي محللو المستوى الأول ساعات طويلة في الفرز اليدوي لآلاف التنبيهات للتحقق منها قبل تصعيدها، مما يؤخر الاستجابة الفعلية.</p>
      </div>
    </div>
    <div class="srow" style="margin-top:14px">
      <div class="sb">
        <div class="snum">10K+</div>
        <div class="slbl en">Daily Alerts / Enterprise</div>
        <div class="slbl ar" style="display:none">تنبيه يومي لكل مؤسسة</div>
        <div class="sref en">Ref: Gartner &amp; Cisco Benchmark (§1.1)</div>
        <div class="sref ar" style="display:none">المرجع: معايير Cisco &amp; Gartner (§1.1)</div>
      </div>
      <div class="sb">
        <div class="snum">&gt;50%</div>
        <div class="slbl en">False Positive Overhead</div>
        <div class="slbl ar" style="display:none">إنذارات كاذبة غير مجدية</div>
        <div class="sref en">Ref: Ponemon SOC Study / §1.2</div>
        <div class="sref ar" style="display:none">المرجع: دراسات Ponemon و §1.2</div>
      </div>
      <div class="sb">
        <div class="snum">45 min</div>
        <div class="slbl en">Avg Manual Triage Time</div>
        <div class="slbl ar" style="display:none">متوسط زمن الفرز اليدوي</div>
        <div class="sref en">Ref: Bridges et al. (2023) (§1.1)</div>
        <div class="sref ar" style="display:none">المرجع: بريدجز وآخرون (2023) (§1.1)</div>
      </div>
    </div>
  </div>
  <div class="sn">03 / 25</div>
</section>

<!-- ================= S04: PROBLEM STATEMENT (ALERT FATIGUE) ================= -->'''

html, count_s03 = re.subn(s03_old_pattern, s03_new, html, flags=re.DOTALL)
print(f"Substituted S03: {count_s03} matches")

# 3. Update Slide 4 (id="s3") - Reorganize shapes & symmetrical layout
s04_old_pattern = r'(<!-- ================= S04: PROBLEM STATEMENT \(ALERT FATIGUE\) ================= -->\s*<section class="slide" id="s3">.*?)(<!-- ================= S05: TRIAGE BOTTLENECK & STATIC LIMITS ================= -->)'

s04_new = '''<!-- ================= S04: PROBLEM STATEMENT (ALERT FATIGUE) ================= -->
<section class="slide" id="s3">
  <div class="orb o1" style="background:rgba(255,107,107,0.12)"></div>
  <div class="content-box">
    <div class="tag a1" style="border-color:rgba(255,107,107,0.4);background:rgba(255,107,107,0.15)">
      <div class="dp" style="background:var(--acc);box-shadow:0 0 10px var(--acc)"></div>
      <span class="en" style="color:#ff9b9b">Chapter 1 &ndash; Problem Formulation</span>
      <span class="ar" style="display:none;color:#ff9b9b">الفصل الأول &ndash; صياغة المشكلة الأساسية</span>
    </div>
    <h2 class="st en">The Core Crisis: Alert Fatigue &amp; Cognitive Overload</h2>
    <h2 class="st ar" style="display:none">الأزمة المركزية: إرهاق التنبيهات والإجهاد الذهني</h2>
    <div class="gl"></div>
    
    <p class="lead en">The convergence of massive alert volumes and excessive false positives creates acute analyst workload, cognitive burnout, and critical response delays (§1.2).</p>
    <p class="lead ar" style="display:none">يؤدي التلاقي الحرج بين فيضان التنبيهات والإنذارات الكاذبة إلى إرهاق تحليلي حاد وإجهاد ذهني يؤخر الاستجابة للحوادث الحقيقية (§1.2).</p>
    
    <div class="grid g3" style="gap:14px;margin-top:6px">
      <div class="card" style="border-color:rgba(255,107,107,0.25);background:rgba(255,107,107,0.04)">
        <div class="c-icon rd"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
        <div class="badge-chip en" style="color:var(--acc);background:rgba(255,107,107,0.12);border:1px solid rgba(255,107,107,0.25);font-size:0.68rem;font-weight:700;margin-bottom:8px">100 GB / DAY INFLUX</div>
        <div class="badge-chip ar" style="display:none;color:var(--acc);background:rgba(255,107,107,0.12);border:1px solid rgba(255,107,107,0.25);font-size:0.68rem;font-weight:700;margin-bottom:8px">تدفق 100 غيغابايت يومياً</div>
        <h3 class="ct en" style="color:#ff9b9b">Alert Influx &amp; Noise</h3>
        <h3 class="ct ar" style="display:none;color:#ff9b9b">فيضان التنبيهات والضجيج</h3>
        <p class="en">Modern SOCs accumulate up to 100 GB of log data daily. A substantial portion consists of non-actionable noise and false positives, exhausting operational capacity and diverting analysts from proactive hunting (§1.2).</p>
        <p class="ar" style="display:none">تستقبل مراكز العمليات ما يصل إلى 100 غيغابايت من السجلات يومياً، وتتكون نسبة كبرى منها من ضجيج وإيجابيات كاذبة تستنزف طاقة المحللين (§1.2).</p>
      </div>

      <div class="card" style="border-color:rgba(255,209,102,0.25);background:rgba(255,209,102,0.04)">
        <div class="c-icon ye"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg></div>
        <div class="badge-chip en" style="color:var(--wa);background:rgba(255,209,102,0.12);border:1px solid rgba(255,209,102,0.25);font-size:0.68rem;font-weight:700;margin-bottom:8px">COGNITIVE OVERLOAD</div>
        <div class="badge-chip ar" style="display:none;color:var(--wa);background:rgba(255,209,102,0.12);border:1px solid rgba(255,209,102,0.25);font-size:0.68rem;font-weight:700;margin-bottom:8px">إجهاد ذهني وتبديل سياق</div>
        <h3 class="ct en" style="color:#ffd166">Context Switching</h3>
        <h3 class="ct ar" style="display:none;color:#ffd166">عنق زجاجة تبديل السياق</h3>
        <p class="en">Analysts manually investigate alerts through continuous context switching—repeatedly pivoting across disparate application windows to gather evidence, creating cognitive overload and analyst burnout (§1.1, §1.2).</p>
        <p class="ar" style="display:none">التنقل اليدوي المستمر بين شاشات وتطبيقات معزولة لجمع الأدلة يولد تشتتاً ذهنياً حاداً وإجهاداً إدراكياً يسرع من تسرب الكفاءات (§1.1, §1.2).</p>
      </div>

      <div class="card" style="border-color:rgba(0,212,255,0.25);background:rgba(0,212,255,0.04)">
        <div class="c-icon cy"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/><path d="m14 9 3 3-3 3"/></svg></div>
        <div class="badge-chip en" style="color:var(--s);background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.25);font-size:0.68rem;font-weight:700;margin-bottom:8px">STATIC AUTOMATION LIMITS</div>
        <div class="badge-chip ar" style="display:none;color:var(--s);background:rgba(0,212,255,0.12);border:1px solid rgba(0,212,255,0.25);font-size:0.68rem;font-weight:700;margin-bottom:8px">قصور الأتمتة التقليدية</div>
        <h3 class="ct en" style="color:var(--s)">Static Rules &amp; Queues</h3>
        <h3 class="ct ar" style="display:none;color:var(--s)">القواعد الثابتة وطوابير الانتظار</h3>
        <p class="en">Conventional SOAR relies on deterministic rules and static playbooks that cannot adapt to evolving risk conditions. Critical incidents get buried beneath lower-value noise in un-prioritized FIFO queues (§1.2).</p>
        <p class="ar" style="display:none">اعتماد أدوات SOAR الحالية على قواعد ثابتة حتمية يجعلها عاجزة عن التكيف، مما يؤدي لدفن الهجمات الحرجة تحت طوفان الإنذارات الروتينية (§1.2).</p>
      </div>
    </div>

    <div class="card" style="margin-top:12px;padding:12px 18px;display:flex;align-items:center;gap:18px;background:rgba(0,212,255,0.06);border:1px solid rgba(0,212,255,0.3)">
      <div style="font-family:'JetBrains Mono',monospace;font-size:1.45rem;font-weight:800;color:var(--s);white-space:nowrap;padding:4px 12px;background:rgba(0,212,255,0.12);border-radius:8px;border:1px solid rgba(0,212,255,0.4)">
        22.9%
      </div>
      <div>
        <div class="en" style="font-size:0.82rem;color:var(--t1);line-height:1.4">
          <strong>Key Empirical Finding (§1.2):</strong> In un-prioritized queues, critical incidents wait excessively; dynamic, risk-aware ordering reduces critical incident queue dwell time by <strong>22.9%</strong>.
        </div>
        <div class="ar" style="display:none;font-size:0.82rem;color:var(--t1);line-height:1.4">
          <strong>النتيجة التجريبية المحورية (§1.2):</strong> الطوابير غير المرتبة تؤخر فحص الحوادث؛ الترتيب الديناميكي الذكي يقلل زمن انتظار الحوادث الحرجة في طوابير الفرز بنسبة <strong>22.9%</strong>.
        </div>
      </div>
    </div>
  </div>
  <div class="sn">04 / 25</div>
</section>

<!-- ================= S05: TRIAGE BOTTLENECK & STATIC LIMITS ================= -->'''

html, count_s04 = re.subn(s04_old_pattern, s04_new, html, flags=re.DOTALL)
print(f"Substituted S04: {count_s04} matches")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated index.html successfully!")
