
const N = 25;
let totalSlides = N;
let c = 0;
let isAR = false;
let bgOn = true;
let bgMode = 'neural';
let bgSpeed = 0.5;
let animStyle = 'cascade';
let focusStyle = 'halo';
let editMode = false;
let selectedTpl = 'dual';

// ================= STEALTH DOCK TOGGLE =================
function toggleDock() {
  const dock = document.getElementById('stealthDock');
  dock.classList.toggle('open');
}

document.addEventListener('click', e => {
  const dock = document.getElementById('stealthDock');
  if (dock && dock.classList.contains('open') && !dock.contains(e.target)) {
    dock.classList.remove('open');
  }
});

// ================= NAVIGATION (ZERO HORIZONTAL SCROLL) =================
function gS(i, direction = 'next') {
  const slides = document.querySelectorAll('.slide');
  totalSlides = slides.length;
  if (!slides[c] || !slides[i] || c === i) return;

  const prevSlide = slides[c];
  const nextSlide = slides[i];

  const dock = document.getElementById('stealthDock');
  if (dock) dock.classList.remove('open');

  prevSlide.classList.remove('active', 'exit-left', 'exit-right');
  prevSlide.classList.add(direction === 'next' ? 'exit-left' : 'exit-right');

  setTimeout(() => {
    prevSlide.classList.remove('exit-left', 'exit-right');
  }, 550);

  c = Math.max(0, Math.min(i, totalSlides - 1));

  nextSlide.classList.remove('exit-left', 'exit-right');
  nextSlide.classList.add('active');

  animateStats(nextSlide);
  if (typeof updateSlideReferences === 'function') {
    updateSlideReferences(c);
  }

  document.getElementById('sc').textContent = (c + 1) + ' / ' + totalSlides;
  document.getElementById('bp').disabled = (c === 0);
  document.getElementById('bn').disabled = (c === totalSlides - 1);
  
  const dots = document.querySelectorAll('.di');
  dots.forEach((d, idx) => d.classList.toggle('active', idx === c));
  if (dots[c] && typeof dots[c].scrollIntoView === 'function') {
    dots[c].scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
  }
  
  document.getElementById('pb').style.width = ((c / Math.max(1, totalSlides - 1)) * 100) + '%';
  document.querySelectorAll('.sni').forEach((s, idx) => s.classList.toggle('active', idx === c));
}

function next() { if (c < totalSlides - 1) gS(c + 1, 'next'); }
function prev() { if (c > 0) gS(c - 1, 'prev'); }

function animateStats(slide) {
  const nums = slide.querySelectorAll('.snum');
  nums.forEach(num => {
    const rawText = num.textContent.trim();
    const match = rawText.match(/^([^\d]*)(\d+(?:\.\d+)?)(.*)$/);
    if (match) {
      const prefix = match[1];
      const targetVal = parseFloat(match[2]);
      const suffix = match[3];
      const isFloat = match[2].includes('.');
      const duration = 750;
      const start = performance.now();

      function update(t) {
        const p = Math.min((t - start) / duration, 1);
        const ease = 1 - Math.pow(1 - p, 3);
        const current = targetVal * ease;
        num.textContent = prefix + (isFloat ? current.toFixed(1) : Math.floor(current)) + suffix;
        if (p < 1) requestAnimationFrame(update);
        else num.textContent = rawText;
      }
      requestAnimationFrame(update);
    }
  });
}

function bD() {
  const x = document.getElementById('sd');
  x.innerHTML = '';
  const slides = document.querySelectorAll('.slide');
  totalSlides = slides.length;
  for (let i = 0; i < totalSlides; i++) {
    const d = document.createElement('div');
    d.className = 'di' + (i === c ? ' active' : '');
    const titleEl = slides[i].querySelector('h2.st, h1.hero');
    d.title = titleEl ? titleEl.innerText.replace(/\n/g, ' ').trim() : `Slide ${i + 1}`;
    d.onclick = () => gS(i, i > c ? 'next' : 'prev');
    x.appendChild(d);
  }
}

function bL() {
  const l = document.getElementById('snl');
  l.innerHTML = '';
  const slides = document.querySelectorAll('.slide');
  totalSlides = slides.length;
  slides.forEach((slide, i) => {
    const s = document.createElement('div');
    s.className = 'sni' + (i === c ? ' active' : '');
    const titleEl = slide.querySelector('h2.st, h1.hero');
    const title = titleEl ? titleEl.innerText.replace(/\n/g, ' ').trim() : `Slide ${i + 1}`;
    const num = (i + 1).toString().padStart(2, '0');
    s.textContent = `${num} ${title}`;
    s.onclick = () => { gS(i, i > c ? 'next' : 'prev'); tC(); };
    l.appendChild(s);
  });
}

function tL() {
  isAR = !isAR;
  document.documentElement.lang = isAR ? 'ar' : 'en';
  document.documentElement.dir = isAR ? 'rtl' : 'ltr';
  document.querySelectorAll('.en').forEach(e => e.style.display = isAR ? 'none' : '');
  document.querySelectorAll('.ar').forEach(e => e.style.display = isAR ? '' : 'none');
  document.getElementById('ll').textContent = isAR ? 'English' : 'العربية';
  bL();
  bD();
}

function tF() {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
  else document.exitFullscreen().catch(() => {});
}

function tC() {
  const p = document.getElementById('cp');
  p.classList.toggle('open');
  if (p.classList.contains('open')) bL();
}

// ================= 5 PRESTIGE GRADIENTS & PALETTES =================
const luxuryThemes = [
  {
    id: 'crimson-plum',
    nameEn: 'Crimson & Deep Wine',
    nameAr: 'القرمزي والبرغندي المخملي',
    p: '#c31432',
    s: '#240b36',
    acc: '#ff4d6d',
    ok: '#10b981',
    bg: '#0d040e',
    card: 'rgba(28, 8, 22, 0.78)',
    br: 'rgba(195, 20, 50, 0.35)'
  },
  {
    id: 'amethyst-emerald',
    nameEn: 'Amethyst Violet & Jade',
    nameAr: 'الجمشت والزمرد اليشمي',
    p: '#8360c3',
    s: '#2ebf91',
    acc: '#a78bfa',
    ok: '#2ebf91',
    bg: '#060810',
    card: 'rgba(18, 14, 28, 0.78)',
    br: 'rgba(131, 96, 195, 0.35)'
  },
  {
    id: 'purple-rose',
    nameEn: 'Purple & Soft Rose',
    nameAr: 'البنفسجي والوردي الأنيق',
    p: '#654ea3',
    s: '#eaafc8',
    acc: '#c084fc',
    ok: '#10b981',
    bg: '#0a0612',
    card: 'rgba(22, 14, 32, 0.78)',
    br: 'rgba(101, 78, 163, 0.35)'
  },
  {
    id: 'lime-aquamarine',
    nameEn: 'Cyber Lime & Aqua',
    nameAr: 'الليمي السيبراني والأكوامارين',
    p: '#a8ff78',
    s: '#78ffd6',
    acc: '#4ade80',
    ok: '#78ffd6',
    bg: '#030f0a',
    card: 'rgba(5, 24, 16, 0.78)',
    br: 'rgba(120, 255, 214, 0.35)'
  },
  {
    id: 'azure-ocean',
    nameEn: 'Electric Azure & Ocean',
    nameAr: 'الأزرق السماوي والمحيطي',
    p: '#00B4DB',
    s: '#0083B0',
    acc: '#38bdf8',
    ok: '#10b981',
    bg: '#020b16',
    card: 'rgba(6, 20, 36, 0.78)',
    br: 'rgba(0, 180, 219, 0.35)'
  }
];

let activeThemeData = luxuryThemes[0];

function applyTheme(themeId) {
  const t = luxuryThemes.find(x => x.id === themeId) || luxuryThemes[0];
  activeThemeData = t;
  const root = document.documentElement;
  root.style.setProperty('--p', t.p);
  root.style.setProperty('--s', t.s);
  root.style.setProperty('--acc', t.acc);
  root.style.setProperty('--ok', t.ok);
  root.style.setProperty('--bg', t.bg);
  root.style.setProperty('--bg-card', t.card);
  root.style.setProperty('--br', t.br);
  root.style.setProperty('--grad', `linear-gradient(135deg, ${t.p}, ${t.s})`);

  document.querySelectorAll('.tcard-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.theme === t.id);
  });
  localStorage.setItem('soar_luxury_theme', t.id);
}

function tOrbs() {
  const btn = document.getElementById('swo');
  btn.classList.toggle('on');
  document.querySelectorAll('.orb').forEach(o => o.style.display = btn.classList.contains('on') ? '' : 'none');
}

// ================= ANIMATION STYLES (8) =================
function setAnimStyle(style) {
  animStyle = style;
  const wrap = document.getElementById('wrap');
  wrap.className = 'anim-' + style;
  document.querySelectorAll('#cp .mode-pills .mpill').forEach(btn => {
    if (btn.id.startsWith('btnAnim')) btn.classList.remove('active');
  });
  const map = {
    'cascade': 'btnAnimCascade',
    '3d': 'btnAnim3D',
    'zoom': 'btnAnimZoom',
    'fade': 'btnAnimFade',
    'slide-up': 'btnAnimSlideUp',
    'flip-x': 'btnAnimFlipX',
    'swirl': 'btnAnimSwirl',
    'focus': 'btnAnimFocus'
  };
  if (map[style]) document.getElementById(map[style]).classList.add('active');
  localStorage.setItem('soar_anim_style', style);
}

// ================= CARD FOCUS & HIGHLIGHT STYLES =================
function setFocusStyle(style) {
  focusStyle = style;
  document.body.className = document.body.className.replace(/focus-\w+/g, '').trim();
  document.body.classList.add('focus-' + style);
  document.querySelectorAll('#cp .mode-pills .mpill').forEach(btn => {
    if (btn.id.startsWith('btnFocus')) btn.classList.remove('active');
  });
  const map = {
    'halo': 'btnFocusHalo',
    'lift': 'btnFocusLift',
    'spotlight': 'btnFocusSpotlight',
    'border': 'btnFocusBorder'
  };
  if (map[style]) document.getElementById(map[style]).classList.add('active');
  localStorage.setItem('soar_focus_style', style);
}

// Interactive Click-to-Pin Focus
document.addEventListener('click', e => {
  const card = e.target.closest('.card, .sb, .fs, .tcard, .ti, .alr');
  if (card && !editMode) {
    const isAlreadyPinned = card.classList.contains('pinned-focus');
    document.querySelectorAll('.pinned-focus').forEach(c => c.classList.remove('pinned-focus'));
    if (!isAlreadyPinned) {
      card.classList.add('pinned-focus');
    }
  } else if (!e.target.closest('#cp, #stealthDock, #nav, #liveEditToolbar, #addSlideModal')) {
    document.querySelectorAll('.pinned-focus').forEach(c => c.classList.remove('pinned-focus'));
  }
});

// ================= SLIDE STUDIO (FULL LIFECYCLE MANAGEMENT) =================
function renumberSlides() {
  const slides = document.querySelectorAll('.slide');
  totalSlides = slides.length;
  slides.forEach((s, idx) => {
    s.id = 's' + idx;
    let sn = s.querySelector('.sn');
    if (!sn) {
      sn = document.createElement('div');
      sn.className = 'sn';
      s.insertBefore(sn, s.firstChild);
    }
    sn.textContent = (idx + 1).toString().padStart(2, '0') + ' / ' + totalSlides;
  });
  c = Math.max(0, Math.min(c, totalSlides - 1));
  document.getElementById('sc').textContent = (c + 1) + ' / ' + totalSlides;
  document.getElementById('bp').disabled = (c === 0);
  document.getElementById('bn').disabled = (c === totalSlides - 1);
  bD();
  bL();
  saveDeckState();
}

function saveDeckState() {
  const wrap = document.getElementById('wrap');
  localStorage.setItem('soar_custom_deck', wrap.innerHTML);
}

// 1. Add Slide Modal & Insert
function openAddSlideModal() {
  document.getElementById('addSlideModal').style.display = 'flex';
  const enInput = document.getElementById('newSlideTitleEn');
  const arInput = document.getElementById('newSlideTitleAr');
  enInput.value = '';
  arInput.value = '';
  enInput.focus();
}

function closeAddSlideModal() {
  document.getElementById('addSlideModal').style.display = 'none';
}

function selectTemplate(tpl) {
  selectedTpl = tpl;
  document.querySelectorAll('.tpl-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.tpl === tpl);
  });
}

function insertNewSlide() {
  const enTitle = document.getElementById('newSlideTitleEn').value.trim() || 'New Architectural Component';
  const arTitle = document.getElementById('newSlideTitleAr').value.trim() || 'مكون معماري أمني جديد';
  
  const newSlide = document.createElement('section');
  newSlide.className = 'slide';

  const snBadge = document.createElement('div');
  snBadge.className = 'sn';
  newSlide.appendChild(snBadge);

  let bodyHtml = '';
  if (selectedTpl === 'dual') {
    bodyHtml = `
      <div class="content-box">
        <div class="tag"><span class="dp"></span><span class="en">System Component</span><span class="ar" style="display:none">مكون النظام</span></div>
        <h2 class="st"><span class="en">${enTitle}</span><span class="ar" style="display:none">${arTitle}</span></h2>
        <div class="gl"></div>
        <p class="lead"><span class="en">Detailed operational analysis and verification criteria.</span><span class="ar" style="display:none">تحليل تشغيلي تفصيلي ومعايير التحقق الأمني.</span></p>
        <div class="g2">
          <div class="card">
            <div class="card-h"><div class="ci">⚡</div><span class="en">Functional Capabilities</span><span class="ar" style="display:none">القدرات الوظيفية</span></div>
            <p><span class="en">Key automation and orchestration mechanisms.</span><span class="ar" style="display:none">آليات الأتمتة والتنسيق الأمني الرئيسية.</span></p>
            <ul>
              <li><span class="en">Intelligent event correlation and triage</span><span class="ar" style="display:none">ربط الأحداث والفرز الذكي</span></li>
              <li><span class="en">Automated containment logic</span><span class="ar" style="display:none">منطق الاحتواء التلقائي السريع</span></li>
            </ul>
          </div>
          <div class="card">
            <div class="card-h"><div class="ci">🛡️</div><span class="en">Security Impact</span><span class="ar" style="display:none">الأثر والحصانة الأمنية</span></div>
            <p><span class="en">Evaluation of resilience and response times.</span><span class="ar" style="display:none">تقييم المرونة وسرعة الاستجابة المحققة.</span></p>
            <ul>
              <li><span class="en">Drastic reduction in dwell time</span><span class="ar" style="display:none">تقليص زمن بقاء التهديدات في الشبكة</span></li>
              <li><span class="en">Integration with enterprise SIEM & EDR</span><span class="ar" style="display:none">التكامل مع أنظمة SIEM و EDR</span></li>
            </ul>
          </div>
        </div>
      </div>`;
  } else if (selectedTpl === 'trio') {
    bodyHtml = `
      <div class="content-box">
        <div class="tag"><span class="dp"></span><span class="en">Core Pillars</span><span class="ar" style="display:none">الركائز الأساسية</span></div>
        <h2 class="st"><span class="en">${enTitle}</span><span class="ar" style="display:none">${arTitle}</span></h2>
        <div class="gl"></div>
        <p class="lead"><span class="en">Three structural pillars powering the intelligent architecture.</span><span class="ar" style="display:none">ثلاث ركائز هيكلية تشغل المعمارية الذكية.</span></p>
        <div class="g3">
          <div class="card">
            <div class="card-h"><div class="ci">🧠</div><span class="en">AI Core</span><span class="ar" style="display:none">الذكاء الاصطناعي</span></div>
            <p><span class="en">Automated ML risk scoring and adaptive prioritization.</span><span class="ar" style="display:none">فرز التنبيهات وتحديد الأولويات التكيفي.</span></p>
          </div>
          <div class="card">
            <div class="card-h"><div class="ci">⚡</div><span class="en">Execution</span><span class="ar" style="display:none">تنفيذ الإجراءات</span></div>
            <p><span class="en">Sub-second dynamic playbook containment.</span><span class="ar" style="display:none">احتواء التهديدات بدفاتر العمل التلقائية.</span></p>
          </div>
          <div class="card">
            <div class="card-h"><div class="ci">🛡️</div><span class="en">Governance</span><span class="ar" style="display:none">الحوكمة والرقابة</span></div>
            <p><span class="en">Full audit logging and analyst decision gates.</span><span class="ar" style="display:none">سجلات تدقيق كاملة وبوابات تحكم بشري.</span></p>
          </div>
        </div>
      </div>`;
  } else if (selectedTpl === 'stats') {
    bodyHtml = `
      <div class="content-box">
        <div class="tag"><span class="dp"></span><span class="en">Performance KPIs</span><span class="ar" style="display:none">مؤشرات الأداء</span></div>
        <h2 class="st"><span class="en">${enTitle}</span><span class="ar" style="display:none">${arTitle}</span></h2>
        <div class="gl"></div>
        <p class="lead"><span class="en">Quantified metrics demonstrating system efficacy and precision.</span><span class="ar" style="display:none">مؤشرات كمية تثبت كفاءة ودقة النظام المطور.</span></p>
        <div class="srow">
          <div class="sb"><div class="snum">96.2%</div><div class="slbl"><span class="en">Precision</span><span class="ar" style="display:none">دقة التصنيف</span></div></div>
          <div class="sb"><div class="snum">85%</div><div class="slbl"><span class="en">Fatigue Drop</span><span class="ar" style="display:none">خفض الإجهاد</span></div></div>
          <div class="sb"><div class="snum">&lt;1.8s</div><div class="slbl"><span class="en">Response Time</span><span class="ar" style="display:none">زمن الاستجابة</span></div></div>
          <div class="sb"><div class="snum">100%</div><div class="slbl"><span class="en">Compliant</span><span class="ar" style="display:none">مطابقة المعايير</span></div></div>
        </div>
        <div class="hl" style="margin-top:20px">
          <p><span class="en"><strong>Operational Outcome:</strong> Significant transformation in incident response agility and analyst satisfaction.</span><span class="ar" style="display:none"><strong>المحصلة التشغيلية:</strong> تحول جذري في مرونة الاستجابة للحوادث وتقليل زمن الاحتواء.</span></p>
        </div>
      </div>`;
  } else if (selectedTpl === 'flow') {
    bodyHtml = `
      <div class="content-box">
        <div class="tag"><span class="dp"></span><span class="en">Pipeline Architecture</span><span class="ar" style="display:none">مخطط المسار</span></div>
        <h2 class="st"><span class="en">${enTitle}</span><span class="ar" style="display:none">${arTitle}</span></h2>
        <div class="gl"></div>
        <p class="lead"><span class="en">End-to-end incident lifecycle flow from ingestion to resolution.</span><span class="ar" style="display:none">المسار المتكامل لإدارة الحادث من الاستيعاب إلى الإغلاق.</span></p>
        <div class="flow">
          <div class="fs"><div class="fi">📡</div><div class="fl"><span class="en">Ingestion</span><span class="ar" style="display:none">استيعاب</span></div><div class="sub">Log Pipeline</div></div>
          <div class="farr">➔</div>
          <div class="fs"><div class="fi">🔍</div><div class="fl"><span class="en">Enrichment</span><span class="ar" style="display:none">إثراء</span></div><div class="sub">Threat Intel</div></div>
          <div class="farr">➔</div>
          <div class="fs"><div class="fi">🧠</div><div class="fl"><span class="en">AI Triage</span><span class="ar" style="display:none">فرز ذكي</span></div><div class="sub">Scoring Model</div></div>
          <div class="farr">➔</div>
          <div class="fs"><div class="fi">⚙️</div><div class="fl"><span class="en">Playbook</span><span class="ar" style="display:none">دفتر العمل</span></div><div class="sub">Automated Fix</div></div>
        </div>
      </div>`;
  }

  const parser = new DOMParser();
  const doc = parser.parseFromString(bodyHtml, 'text/html');
  while (doc.body.firstChild) {
    newSlide.appendChild(doc.body.firstChild);
  }

  const slides = document.querySelectorAll('.slide');
  const currentSlide = slides[c];
  if (currentSlide && currentSlide.nextSibling) {
    currentSlide.parentNode.insertBefore(newSlide, currentSlide.nextSibling);
  } else {
    document.getElementById('wrap').appendChild(newSlide);
  }

  // Ensure current language display matches
  newSlide.querySelectorAll('.en').forEach(e => e.style.display = isAR ? 'none' : '');
  newSlide.querySelectorAll('.ar').forEach(e => e.style.display = isAR ? '' : 'none');

  closeAddSlideModal();
  renumberSlides();
  gS(c + 1, 'next');
  const cp = document.getElementById('cp');
  if (cp) cp.classList.remove('open');
}

// 2. Delete Current Slide
function deleteCurrentSlide() {
  const slides = document.querySelectorAll('.slide');
  if (slides.length <= 1) {
    alert(isAR ? 'لا يمكن حذف الشريحة الأخيرة!' : 'Cannot delete the only remaining slide!');
    return;
  }
  const confirmMsg = isAR ? `هل أنت متأكد من حذف الشريحة الحالية رقم (${c + 1})؟` : `Are you sure you want to delete slide (${c + 1})?`;
  if (confirm(confirmMsg)) {
    const slideToDelete = slides[c];
    slideToDelete.remove();
    c = Math.max(0, Math.min(c, document.querySelectorAll('.slide').length - 1));
    renumberSlides();
    const remaining = document.querySelectorAll('.slide');
    remaining.forEach((s, idx) => s.classList.toggle('active', idx === c));
    const cp = document.getElementById('cp');
    if (cp) cp.classList.remove('open');
  }
}

// 3. Duplicate Slide
function duplicateCurrentSlide() {
  const slides = document.querySelectorAll('.slide');
  const current = slides[c];
  if (!current) return;
  const clone = current.cloneNode(true);
  clone.classList.remove('active', 'exit-left', 'exit-right');
  if (current.nextSibling) {
    current.parentNode.insertBefore(clone, current.nextSibling);
  } else {
    document.getElementById('wrap').appendChild(clone);
  }
  renumberSlides();
  gS(c + 1, 'next');
  const cp = document.getElementById('cp');
  if (cp) cp.classList.remove('open');
}

// 4. Move Slide Up/Down
function moveSlide(dir) {
  const slides = document.querySelectorAll('.slide');
  const current = slides[c];
  if (!current) return;
  const parent = current.parentNode;
  if (dir === 'up' && c > 0) {
    parent.insertBefore(current, slides[c - 1]);
    c--;
  } else if (dir === 'down' && c < slides.length - 1) {
    parent.insertBefore(slides[c + 1], current);
    c++;
  }
  renumberSlides();
  const all = document.querySelectorAll('.slide');
  all.forEach((s, idx) => s.classList.toggle('active', idx === c));
}

// 5. In-Place Card Add/Remove
function addCardToActiveSlide() {
  const activeSlide = document.querySelectorAll('.slide')[c];
  if (!activeSlide) return;
  let grid = activeSlide.querySelector('.g2, .g3, .g4');
  if (!grid) {
    const box = activeSlide.querySelector('.content-box');
    if (!box) return;
    grid = document.createElement('div');
    grid.className = 'g2';
    box.appendChild(grid);
  }
  const newCard = document.createElement('div');
  newCard.className = 'card';
  newCard.contentEditable = 'true';
  newCard.style.outline = '1px dashed rgba(255, 179, 0, 0.5)';
  newCard.innerHTML = `
    <div class="card-h"><div class="ci">✨</div><span class="en">New Custom Section</span><span class="ar" style="${isAR ? '' : 'display:none'}">قسم مخصص جديد</span></div>
    <p><span class="en">Click to edit this text directly on the slide.</span><span class="ar" style="${isAR ? '' : 'display:none'}">انقر هنا لتعديل هذا النص مباشرة على الشريحة.</span></p>
  `;
  grid.appendChild(newCard);
  saveDeckState();
}

function removeLastCardFromActiveSlide() {
  const activeSlide = document.querySelectorAll('.slide')[c];
  if (!activeSlide) return;
  const cards = activeSlide.querySelectorAll('.card');
  if (cards.length > 0) {
    cards[cards.length - 1].remove();
    saveDeckState();
  }
}

// 6. Restore Original 25 Slides
function restoreOriginalSlides() {
  const msg = isAR ? 'هل تريد استعادة جميع الشرائح الأصلية المعتمدة (25 شريحة) وإلغاء أي تعديلات؟' : 'Restore the official 25 university slides and reset all changes?';
  if (confirm(msg)) {
    localStorage.removeItem('soar_custom_deck');
    localStorage.removeItem('soar_slides_custom');
    location.reload();
  }
}

// ================= LIVE EDIT MODE =================
function toggleEditMode() {
  editMode = !editMode;
  const tb = document.getElementById('liveEditToolbar');
  if (tb) tb.style.display = editMode ? 'flex' : 'none';
  
  document.querySelectorAll('.slide h1, .slide h2, .slide h3, .slide h4, .slide p, .slide li, .slide span, .slide strong, .slide .snum, .slide .slbl').forEach(el => {
    el.contentEditable = editMode ? 'true' : 'false';
    if (editMode) el.style.outline = '1px dashed rgba(255, 179, 0, 0.5)';
    else el.style.outline = 'none';
  });
  if (editMode) {
    const cp = document.getElementById('cp');
    if (cp) cp.classList.remove('open');
  }
}

function saveEdits() {
  saveDeckState();
  alert(isAR ? 'تم حفظ التعديلات وحالة الشرائح بنجاح في متصفحك!' : 'All slide edits & structure saved successfully to local storage!');
}

// ================= DYNAMIC BACKGROUND MODES & SPEED =================
function toggleBg() {
  bgOn = !bgOn;
  const btn = document.getElementById('swBg');
  btn.classList.toggle('on', bgOn);
  document.getElementById('cv').style.opacity = bgOn ? '1' : '0';
  document.getElementById('bgPillsGroup').style.opacity = bgOn ? '1' : '0.4';
  document.getElementById('bgPillsGroup').style.pointerEvents = bgOn ? 'all' : 'none';
}

function setBgMode(mode) {
  bgMode = mode;
  document.querySelectorAll('#bgPillsGroup .mpill').forEach(btn => btn.classList.remove('active'));
  const map = {
    'neural': 'btnBgNeural',
    'waves': 'btnBgWaves',
    'aurora': 'btnBgAurora',
    'stardust': 'btnBgStardust',
    'grid': 'btnBgGrid',
    'matrix': 'btnBgMatrix',
    'warp': 'btnBgWarp'
  };
  if (map[mode]) document.getElementById(map[mode]).classList.add('active');
  initBg();
  localStorage.setItem('soar_bg_mode', mode);
}

function setBgSpeed(spd, btnId) {
  bgSpeed = spd;
  document.querySelectorAll('.mode-pills-3 .mpill').forEach(btn => btn.classList.remove('active'));
  const b = document.getElementById(btnId);
  if (b) b.classList.add('active');
  localStorage.setItem('soar_bg_speed', spd);
}

// ================= TIMER =================
let timerSeconds = 20 * 60;
let timerInterval = null;
function updateTimerDisplay() {
  const m = Math.floor(timerSeconds / 60).toString().padStart(2, '0');
  const s = (timerSeconds % 60).toString().padStart(2, '0');
  const el = document.getElementById('timerDisplay');
  el.textContent = `${m}:${s}`;
  if (timerSeconds <= 180) el.style.color = '#ff6b6b';
  else el.style.color = 'var(--s)';
}
function startTimer() {
  if (timerInterval) return;
  timerInterval = setInterval(() => {
    if (timerSeconds > 0) {
      timerSeconds--;
      updateTimerDisplay();
    } else {
      clearInterval(timerInterval);
      timerInterval = null;
      alert(isAR ? 'انتهى الوقت المحدد للعرض التقديمي (20 دقيقة)!' : 'Presentation time limit reached (20 minutes)!');
    }
  }, 1000);
}
function pauseTimer() {
  clearInterval(timerInterval);
  timerInterval = null;
}
function resetTimer() {
  pauseTimer();
  timerSeconds = 20 * 60;
  updateTimerDisplay();
}

// ================= KEYBOARD & TOUCH =================
document.addEventListener('keydown', e => {
  if (editMode && e.target.isContentEditable) return;
  switch (e.key) {
    case 'ArrowRight':
    case 'ArrowDown':
    case ' ':
      next(); break;
    case 'ArrowLeft':
    case 'ArrowUp':
      prev(); break;
    case 'Home': gS(0, 'prev'); break;
    case 'End': gS(N - 1, 'next'); break;
    case 'f':
    case 'F': tF(); break;
    case 'l':
    case 'L': tL(); break;
    case 'c':
    case 'C': tC(); break;
    case 'e':
    case 'E': toggleEditMode(); break;
  }
});

let tx = 0;
document.addEventListener('touchstart', e => tx = e.touches[0].clientX, { passive: true });
document.addEventListener('touchend', e => {
  const d = tx - e.changedTouches[0].clientX;
  if (Math.abs(d) > 50) {
    if (d > 0) next(); else prev();
  }
}, { passive: true });

// ================= 7 SERENE DYNAMIC CANVAS ENGINES =================
const cv = document.getElementById('cv');
const cx = cv.getContext('2d');
let mouse = { x: null, y: null };
let bgEntities = [];
let waveStep = 0;

window.addEventListener('mousemove', e => {
  mouse.x = e.clientX;
  mouse.y = e.clientY;
});
window.addEventListener('mouseleave', () => {
  mouse.x = null;
  mouse.y = null;
});

function rsz() {
  cv.width = window.innerWidth;
  cv.height = window.innerHeight;
  initBg();
}

function hexToRgb(hex) {
  hex = (hex || '#d4af37').replace('#', '').trim();
  if (hex.length === 3) hex = hex.split('').map(c => c + c).join('');
  const num = parseInt(hex, 16);
  return {
    r: (num >> 16) & 255,
    g: (num >> 8) & 255,
    b: num & 255
  };
}

function hexToRgba(hex, alpha) {
  try {
    const { r, g, b } = hexToRgb(hex);
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
  } catch (e) {
    return `rgba(212, 175, 55, ${alpha})`;
  }
}

// 1. Serene Neural Node
class NeuralNode {
  constructor() { this.r(); }
  r() {
    this.x = Math.random() * cv.width;
    this.y = Math.random() * cv.height;
    this.sz = Math.random() * 1.8 + 1.1;
    this.sx = (Math.random() - 0.5) * 0.32;
    this.sy = (Math.random() - 0.5) * 0.32;
    this.op = Math.random() * 0.45 + 0.35;
    this.pulse = Math.random() * Math.PI * 2;
  }
  u() {
    this.pulse += 0.02 * bgSpeed;
    if (mouse.x !== null) {
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 140) {
        this.x += (dx / dist) * 0.3 * bgSpeed;
        this.y += (dy / dist) * 0.3 * bgSpeed;
      }
    }
    this.x += this.sx * bgSpeed;
    this.y += this.sy * bgSpeed;
    if (this.x < -10 || this.x > cv.width + 10 || this.y < -10 || this.y > cv.height + 10) this.r();
  }
  d(colorHex) {
    const currentSz = this.sz + Math.sin(this.pulse) * 0.45;
    cx.beginPath();
    cx.arc(this.x, this.y, Math.max(0.6, currentSz), 0, Math.PI * 2);
    cx.fillStyle = hexToRgba(colorHex, this.op);
    cx.shadowBlur = 6;
    cx.shadowColor = colorHex;
    cx.fill();
    cx.shadowBlur = 0;
  }
}

// 2. Serene Stardust Particle
class Stardust {
  constructor() { this.r(); }
  r() {
    this.x = Math.random() * cv.width;
    this.y = Math.random() * cv.height;
    this.sz = Math.random() * 1.6 + 0.6;
    this.sx = (Math.random() - 0.5) * 0.2;
    this.sy = (Math.random() - 0.5) * 0.2;
    this.op = Math.random() * 0.5 + 0.2;
    this.phase = Math.random() * Math.PI * 2;
  }
  u() {
    this.phase += 0.015 * bgSpeed;
    this.x += this.sx * bgSpeed;
    this.y += this.sy * bgSpeed;
    if (this.x < 0 || this.x > cv.width || this.y < 0 || this.y > cv.height) this.r();
  }
  d(sColor) {
    const alpha = (Math.sin(this.phase) * 0.25 + 0.5) * this.op;
    cx.beginPath();
    cx.arc(this.x, this.y, this.sz, 0, Math.PI * 2);
    cx.fillStyle = hexToRgba(sColor, alpha);
    cx.shadowBlur = 8;
    cx.shadowColor = sColor;
    cx.fill();
    cx.shadowBlur = 0;
  }
}

// 3. Calm Hexagonal Lattice Node
class GridNode {
  constructor(gx, gy) {
    this.x = gx;
    this.y = gy;
    this.phase = (gx * 0.02 + gy * 0.02);
  }
  d(pColor, sColor) {
    const pulse = Math.sin(waveStep * 0.7 + this.phase);
    const alpha = Math.max(0.06, (pulse + 1) * 0.16);
    cx.beginPath();
    cx.arc(this.x, this.y, 1.8, 0, Math.PI * 2);
    cx.fillStyle = hexToRgba(pulse > 0.4 ? sColor : pColor, alpha);
    cx.fill();
  }
}

// 4. Calm Cyber Matrix Stream
class MatrixCol {
  constructor(x) {
    this.x = x;
    this.y = Math.random() * -cv.height;
    this.speed = (Math.random() * 1.2 + 0.8);
    this.chars = '01SOARSECURITYAI789XYZ45DEF';
    this.len = Math.floor(Math.random() * 12 + 6);
  }
  u() {
    this.y += this.speed * bgSpeed;
    if (this.y > cv.height + 150) {
      this.y = Math.random() * -100;
      this.speed = (Math.random() * 1.2 + 0.8);
    }
  }
  d(pColor, sColor) {
    cx.font = '10px "JetBrains Mono", monospace';
    for (let i = 0; i < this.len; i++) {
      const char = this.chars[Math.floor(Math.random() * this.chars.length)];
      const cyPos = this.y - i * 14;
      if (cyPos > 0 && cyPos < cv.height) {
        const alpha = Math.max(0, 1 - (i / this.len));
        if (i === 0) {
          cx.fillStyle = '#ffffff';
          cx.shadowBlur = 8;
          cx.shadowColor = sColor;
          cx.fillText(char, this.x, cyPos);
          cx.shadowBlur = 0;
        } else {
          cx.fillStyle = hexToRgba(i % 2 === 0 ? sColor : pColor, alpha * 0.55);
          cx.fillText(char, this.x, cyPos);
        }
      }
    }
  }
}

// 5. Calm Space Warp Star
class WarpStar {
  constructor() { this.r(); }
  r() {
    this.x = (Math.random() - 0.5) * cv.width;
    this.y = (Math.random() - 0.5) * cv.height;
    this.z = Math.random() * cv.width;
    this.pz = this.z;
    this.speed = (Math.random() * 1.6 + 1.2);
  }
  u() {
    this.z -= this.speed * bgSpeed;
    if (this.z <= 0) {
      this.r();
      this.pz = this.z;
    }
  }
  d(sColor) {
    const cxCenter = cv.width / 2;
    const cyCenter = cv.height / 2;
    const sx = (this.x / this.z) * 150 + cxCenter;
    const sy = (this.y / this.z) * 150 + cyCenter;
    const px = (this.x / this.pz) * 150 + cxCenter;
    const py = (this.y / this.pz) * 150 + cyCenter;
    this.pz = this.z;

    if (sx >= 0 && sx <= cv.width && sy >= 0 && sy <= cv.height) {
      const alpha = Math.min(1, (1 - this.z / cv.width) * 0.8);
      cx.beginPath();
      cx.moveTo(px, py);
      cx.lineTo(sx, sy);
      cx.strokeStyle = hexToRgba(sColor, alpha);
      cx.lineWidth = Math.min(2.0, (1 - this.z / cv.width) * 2.2);
      cx.stroke();
    }
  }
}

function initBg() {
  bgEntities = [];
  if (bgMode === 'neural') {
    const count = Math.min(80, Math.floor(window.innerWidth / 18));
    for (let i = 0; i < count; i++) bgEntities.push(new NeuralNode());
  } else if (bgMode === 'stardust') {
    const count = Math.min(120, Math.floor(window.innerWidth / 12));
    for (let i = 0; i < count; i++) bgEntities.push(new Stardust());
  } else if (bgMode === 'grid') {
    const spacing = 48;
    for (let x = 20; x < cv.width; x += spacing) {
      for (let y = 20; y < cv.height; y += spacing) {
        bgEntities.push(new GridNode(x, y));
      }
    }
  } else if (bgMode === 'matrix') {
    const cols = Math.floor(cv.width / 24);
    for (let i = 0; i < cols; i++) bgEntities.push(new MatrixCol(i * 24));
  } else if (bgMode === 'warp') {
    for (let i = 0; i < 150; i++) bgEntities.push(new WarpStar());
  }
}

function animCanvas() {
  requestAnimationFrame(animCanvas);
  if (!bgOn) return;

  cx.clearRect(0, 0, cv.width, cv.height);
  const pColor = activeThemeData ? activeThemeData.p : '#d4af37';
  const sColor = activeThemeData ? activeThemeData.s : '#f9d976';

  if (bgMode === 'neural') {
    bgEntities.forEach(p => { p.u(); p.d(sColor); });
    for (let i = 0; i < bgEntities.length; i++) {
      for (let j = i + 1; j < bgEntities.length; j++) {
        const dx = bgEntities[i].x - bgEntities[j].x;
        const dy = bgEntities[i].y - bgEntities[j].y;
        const dd = Math.sqrt(dx * dx + dy * dy);
        if (dd < 105) {
          cx.beginPath();
          cx.moveTo(bgEntities[i].x, bgEntities[i].y);
          cx.lineTo(bgEntities[j].x, bgEntities[j].y);
          cx.strokeStyle = hexToRgba(pColor, 0.22 * (1 - dd / 105));
          cx.lineWidth = 0.75;
          cx.stroke();
        }
      }
      if (mouse.x !== null) {
        const mdx = bgEntities[i].x - mouse.x;
        const mdy = bgEntities[i].y - mouse.y;
        const mdist = Math.sqrt(mdx * mdx + mdy * mdy);
        if (mdist < 140) {
          cx.beginPath();
          cx.moveTo(bgEntities[i].x, bgEntities[i].y);
          cx.lineTo(mouse.x, mouse.y);
          cx.strokeStyle = hexToRgba(sColor, 0.4 * (1 - mdist / 140));
          cx.lineWidth = 1.1;
          cx.stroke();
        }
      }
    }
  } else if (bgMode === 'waves') {
    waveStep += 0.01 * bgSpeed;
    const waves = [
      { y: cv.height * 0.68, len: 0.0024, amp: 40, p: pColor, alpha: 0.14 },
      { y: cv.height * 0.74, len: 0.0032, amp: 50, p: sColor, alpha: 0.12 },
      { y: cv.height * 0.80, len: 0.0018, amp: 60, p: pColor, alpha: 0.10 }
    ];
    waves.forEach((w, idx) => {
      cx.beginPath();
      cx.moveTo(0, cv.height);
      for (let x = 0; x <= cv.width; x += 10) {
        const y = w.y + Math.sin(x * w.len + waveStep + idx * 1.4) * w.amp;
        cx.lineTo(x, y);
      }
      cx.lineTo(cv.width, cv.height);
      const grad = cx.createLinearGradient(0, w.y - w.amp, 0, cv.height);
      grad.addColorStop(0, hexToRgba(w.p, w.alpha));
      grad.addColorStop(1, 'transparent');
      cx.fillStyle = grad;
      cx.fill();

      // Soft crest line
      cx.beginPath();
      for (let x = 0; x <= cv.width; x += 10) {
        const y = w.y + Math.sin(x * w.len + waveStep + idx * 1.4) * w.amp;
        if (x === 0) cx.moveTo(x, y);
        else cx.lineTo(x, y);
      }
      cx.strokeStyle = hexToRgba(w.p, w.alpha * 2.0);
      cx.lineWidth = 1.5;
      cx.shadowBlur = 10;
      cx.shadowColor = w.p;
      cx.stroke();
      cx.shadowBlur = 0;
    });
  } else if (bgMode === 'aurora') {
    waveStep += 0.006 * bgSpeed;
    for (let a = 0; a < 3; a++) {
      cx.beginPath();
      cx.moveTo(0, 0);
      for (let x = 0; x <= cv.width; x += 16) {
        const y = (cv.height * 0.28) + Math.sin(x * 0.0018 + waveStep + a * 1.6) * 70 + Math.cos(x * 0.003 + waveStep * 0.8) * 35;
        cx.lineTo(x, y);
      }
      cx.lineTo(cv.width, 0);
      const grad = cx.createLinearGradient(0, 0, 0, cv.height * 0.5);
      grad.addColorStop(0, hexToRgba(a % 2 === 0 ? pColor : sColor, 0.12));
      grad.addColorStop(1, 'transparent');
      cx.fillStyle = grad;
      cx.fill();
    }
  } else if (bgMode === 'stardust') {
    bgEntities.forEach(e => { e.u(); e.d(sColor); });
  } else if (bgMode === 'grid') {
    waveStep += 0.015 * bgSpeed;
    bgEntities.forEach(e => e.d(pColor, sColor));
    const spacing = 48;
    for (let x = 20; x < cv.width - spacing; x += spacing) {
      for (let y = 20; y < cv.height - spacing; y += spacing) {
        if ((x + y) % (spacing * 2) === 0) {
          cx.beginPath();
          cx.moveTo(x, y);
          cx.lineTo(x + spacing, y);
          cx.lineTo(x + spacing, y + spacing);
          cx.strokeStyle = hexToRgba(pColor, 0.06);
          cx.lineWidth = 0.6;
          cx.stroke();
        }
      }
    }
  } else if (bgMode === 'matrix') {
    bgEntities.forEach(e => { e.u(); e.d(pColor, sColor); });
  } else if (bgMode === 'warp') {
    bgEntities.forEach(e => { e.u(); e.d(sColor); });
  }
}

window.addEventListener('DOMContentLoaded', () => {
  const savedDeck = localStorage.getItem('soar_custom_deck');
  if (savedDeck && savedDeck.trim().length > 1000) {
    document.getElementById('wrap').innerHTML = savedDeck;
  }

  const savedTheme = localStorage.getItem('soar_luxury_theme');
  if (savedTheme) applyTheme(savedTheme);

  const savedAnim = localStorage.getItem('soar_anim_style');
  if (savedAnim) setAnimStyle(savedAnim);

  const savedFocus = localStorage.getItem('soar_focus_style');
  if (savedFocus) setFocusStyle(savedFocus);

  const savedBg = localStorage.getItem('soar_bg_mode');
  if (savedBg) setBgMode(savedBg);

  const savedSpd = localStorage.getItem('soar_bg_speed');
  if (savedSpd) {
    const spdVal = parseFloat(savedSpd);
    const spdBtn = spdVal === 1.0 ? 'btnSpdBalanced' : (spdVal === 0.25 ? 'btnSpdUltra' : 'btnSpdSerene');
    setBgSpeed(spdVal, spdBtn);
  }

  renumberSlides();
  const slides = document.querySelectorAll('.slide');
  slides.forEach((s, idx) => s.classList.toggle('active', idx === c));
});

window.addEventListener('resize', rsz);
rsz();
initBg();
animCanvas();
bD();
bL();
updateTimerDisplay();
document.getElementById('pb').style.width = '0%';

// ================= SLIDE REPORT REFERENCES & PARAGRAPH MAPPING DATA =================
const SLIDE_REFS = {
  0: {
    titleEn: "Slide 01: Project Title & Overview",
    titleAr: "الشريحة 01: عنوان المشروع والمستخلص",
    chapter: "Front Matter & Abstract",
    section: "Title Page & Abstract (Page 2)",
    elements: [
      {
        elEn: "Project Title",
        elAr: "عنوان المشروع",
        loc: "Cover Page, Page 1",
        textEn: "AI-Based Security Orchestration, Automation, and Response (SOAR) Tool",
        status: "Exact 100%"
      },
      {
        elEn: "Lead Abstract Context",
        elAr: "المقدمة والمستخلص",
        loc: "Abstract, Page 2, Paragraph 1 (Lines 1-8)",
        textEn: "Modern SOCs face increasing challenges in managing large volumes of security alerts, false positives, and heterogeneous security data... creating analyst alert fatigue.",
        status: "Exact 100%"
      },
      {
        elEn: "Supervisory & Faculty Details",
        elAr: "بيانات الإشراف والقسم",
        loc: "Cover Page, Page 1",
        textEn: "Supervised by Dr. Raed Saeed, Bachelor's Degree in Cybersecurity and Networking, Department of Computer Science.",
        status: "Exact 100%"
      }
    ]
  },
  1: {
    titleEn: "Slide 02: Graduation Project Team & Academic Identifiers",
    titleAr: "الشريحة 02: أعضاء فريق المشروع والأرقام الأكاديمية",
    chapter: "Front Matter",
    section: "Cover Page — Author & Supervisory Registry (Page 1)",
    elements: [
      {
        elEn: "Team Members & Academic IDs (6 Students)",
        elAr: "أسماء الطلاب والأرقام الأكاديمية (6 طلاب)",
        loc: "Cover Page, Page 1",
        textEn: "1. Hizam Al-Shajara (202210102478)\n2. Hamoud Abu Amrah (202310101609)\n3. Mohammed Hameed (202310100174)\n4. Mohammed Al-Warafi (202310100461)\n5. Marwan Al-Ameer (202310100177)\n6. Noah Maraq (202310100452)",
        status: "Exact 100%"
      },
      {
        elEn: "Academic Department & Head",
        elAr: "القسم الأكاديمي ورئاسة القسم",
        loc: "Cover Page & Department Registry",
        textEn: "Department of Computer Science, Head: Dr. Nabeel Al-Mekhlafy, Supervision: Dr. Raed Saeed.",
        status: "Exact 100%"
      }
    ]
  },
  2: {
    titleEn: "Slide 03: The Modern SOC Operational Landscape",
    titleAr: "الشريحة 03: المشهد التشغيلي لمراكز العمليات الأمنية الحديثة (SOC)",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.1 Overview of Modern SOCs & §1.2 Problem Statement (Pages 11-14)",
    elements: [
      {
        elEn: "Lead Paragraph",
        elAr: "الفقرة التمهيدية",
        loc: "§1.1, Paragraph 1, Lines 1-7 (Page 11)",
        textEn: "A Security Operations Center (SOC) is a centralized operational function responsible for monitoring, detecting, investigating, and responding to organizational cyber threats (Khayat et al., 2025)...",
        status: "Exact 100%"
      },
      {
        elEn: "Data Influx & SIEM Card",
        elAr: "طوفان البيانات ودور SIEM",
        loc: "§1.1 (Page 11) & §1.2 (Page 13)",
        textEn: "Organizations implement SIEM platforms for centralized log management... Accumulating up to 100 gigabytes of log and alert data daily, a substantial portion consists of non-actionable noise.",
        status: "Exact 100%"
      },
      {
        elEn: "Heterogeneous Tool Stacks Card",
        elAr: "تشتت الأدوات الأمنية",
        loc: "§1.1, Paragraph 1, Lines 6-9 (Page 11)",
        textEn: "Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous (Kinyua & Awuah, 2021).",
        status: "Exact 100%"
      },
      {
        elEn: "Tiered Analyst Hierarchy Card",
        elAr: "هرمية المحللين المرهقة",
        loc: "§1.1, Paragraph 2, Lines 1-5 (Page 11)",
        textEn: "Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, manually gathering contextual evidence across disparate sources (Bridges et al., 2023; Khayat et al., 2025).",
        status: "Exact 100%"
      },
      {
        elEn: "Empirical Statistics Row (100 GB, 22.9%, 54%)",
        elAr: "شريط الإحصائيات المعتمدة",
        loc: "§1.2, Paragraph 1 & 4 (Pages 13-14) & §2.4.1 (Gelman et al., 2023)",
        textEn: "100 GB daily influx (§1.2); 22.9% critical incident queue dwell time reduction via dynamic triage (§1.2, Gelman et al., 2023); 54% false-positive incident suppression with 95.1% actionable capture (§2.4.1).",
        status: "Exact 100%"
      }
    ]
  },
      {
        elEn: "Data Influx & SIEM Card",
        elAr: "بطاقة طوفان البيانات ودور SIEM",
        loc: "§1.1, Paragraph 1, Lines 3-6 (Page 11)",
        textEn: "Organizations implement SIEM platforms for centralized log management... accumulating up to 100 gigabytes of log and alert data daily...",
        status: "Exact 100%"
      },
      {
        elEn: "Heterogeneous Tool Stacks Card",
        elAr: "بطاقة تشتت الأدوات الأمنية",
        loc: "§1.1, Paragraph 1, Lines 6-9 (Page 11)",
        textEn: "Because these tools operate with distinct log schemas, vendor-specific data representations, and unique alert mechanisms, the resulting security data is highly heterogeneous...",
        status: "Exact 100%"
      },
      {
        elEn: "Tiered Analyst Hierarchy Card",
        elAr: "بطاقة الهيكلية الهرمية للمحللين",
        loc: "§1.1, Paragraph 2, Lines 1-5 (Page 11)",
        textEn: "Security analysts are structured into a tiered organizational model. Junior analysts conduct initial alert triage, manually gathering contextual evidence...",
        status: "Exact 100%"
      }
    ]
  },
  3: {
    titleEn: "Slide 04: Alert Fatigue & Cognitive Overload",
    titleAr: "الشريحة 04: إرهاق التنبيهات والإجهاد الإدراكي",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.2 The Problem Statement (Alert Fatigue and Static Triage) (Pages 13-14)",
    elements: [
      {
        elEn: "Lead Paragraph (100GB Influx)",
        elAr: "الفقرة التقديمية (تدفق 100GB)",
        loc: "§1.2, Paragraph 1, Lines 1-5 (Page 13)",
        textEn: "Modern Security Operations Centers (SOCs) face an unsustainable influx of security data, accumulating up to 100 gigabytes of log and alert data daily... demanding significant operational effort.",
        status: "Exact 100%"
      },
      {
        elEn: "Alert Fatigue & Context Switching Card",
        elAr: "بطاقة إرهاق التنبيهات وتبديل السياق",
        loc: "§1.2, Paragraph 2, Lines 1-7 (Page 13)",
        textEn: "This convergence of high alert volumes and excessive false positives causes high analyst workload and alert fatigue. Analysts manually investigate alerts through continuous context switching...",
        status: "Exact 100%"
      },
      {
        elEn: "Static Prioritization Limits (22.9% Wait Time)",
        elAr: "بطاقة قيود الأولوية الثابتة (تقليص 22.9%)",
        loc: "§1.2, Paragraph 4, Lines 1-6 (Page 14)",
        textEn: "When prioritization relies primarily on fixed decision rules, highly critical incidents can become buried... Dynamic, risk-aware ordering can reduce the time critical incidents spend waiting in analyst queues by 22.9%.",
        status: "Exact 100%"
      },
      {
        elEn: "Automated Workflow Limits & Logic Failures",
        elAr: "قائمة الآثار التشغيلية وقيود المنطق الحتمي",
        loc: "§1.2, Paragraph 3 (Page 13) & Paragraph 4 (Page 14)",
        textEn: "Reliance on predefined rules and static playbooks may limit adaptability... Deterministic conditional logic can constrain effectiveness against novel or evasive threats.",
        status: "Exact 100%"
      }
    ]
  },
  4: {
    titleEn: "Slide 05: The Triage Bottleneck: Static Rules & Context Switching",
    titleAr: "الشريحة 05: عنق زجاجة الفرز وتبديل السياق",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.2 The Problem Statement (cont.) & §1.3 Motivation (Pages 13-15)",
    elements: [
      {
        elEn: "Rigid Conditional Statements Card",
        elAr: "بطاقة جمود القواعد الشرطية",
        loc: "§1.2, Paragraph 3, Lines 1-5 (Page 13)",
        textEn: "Rigid conditional statements may become less effective against novel or evasive threats that fall outside anticipated patterns...",
        status: "Exact 100%"
      },
      {
        elEn: "Manual Context Switching Card",
        elAr: "بطاقة تبديل السياق بين الأنظمة",
        loc: "§1.1, Paragraph 2, Lines 4-8 (Page 11)",
        textEn: "Analysts must manually gather contextual evidence from multiple disparate security sources... navigate across different application interfaces, hold hypotheses in memory...",
        status: "Exact 100%"
      },
      {
        elEn: "Static Prioritization Card",
        elAr: "بطاقة الترتيب الثابت غير المرن",
        loc: "§1.2, Paragraph 4, Lines 1-4 (Page 14)",
        textEn: "When prioritization relies primarily on fixed decision rules, highly critical incidents can become buried beneath lower-value noise. Un-prioritized queues delay handling.",
        status: "Exact 100%"
      },
      {
        elEn: "Key Operational Takeaway",
        elAr: "الخلاصة التشغيلية",
        loc: "§1.2, Paragraph 5, Lines 1-4 (Page 14)",
        textEn: "These challenges motivate the ongoing need to investigate how intelligent alert analysis and prioritization can be integrated with operational workflows...",
        status: "Exact 100%"
      }
    ]
  },
  5: {
    titleEn: "Slide 06: Project Objectives: Strategic & Operational",
    titleAr: "الشريحة 06: أهداف المشروع الاستراتيجية والتفصيلية",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.4 Project Objectives (Pages 15-16)",
    elements: [
      {
        elEn: "Primary Objective",
        elAr: "الهدف العام الرئيسي",
        loc: "§1.4.1 Primary Objective, Lines 1-6 (Page 15)",
        textEn: "Investigate, design, and propose an integrated AI-Based Security Orchestration, Automation, and Response (SOAR) tool that addresses operational bottlenecks by integrating intelligent alert analysis, risk-based scoring, dynamic prioritization, and automated response...",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 1: Operational Analysis",
        elAr: "الهدف 1: تحليل تحديات العمليات",
        loc: "§1.4.2 Specific Objectives, Bullet 1 (Page 15)",
        textEn: "Analyze the operational challenges of current SOC alert management, specifically including alert fatigue and the limitations of static triage.",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 2: Literature Review",
        elAr: "الهدف 2: مراجعة الأدبيات",
        loc: "§1.4.2 Specific Objectives, Bullet 2 (Page 15)",
        textEn: "Review existing AI/ML-based approaches and academic literature related to security alert analysis and prioritization.",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 3: Design Architecture",
        elAr: "الهدف 3: تصميم المعمارية",
        loc: "§1.4.2 Specific Objectives, Bullet 3 (Page 15)",
        textEn: "Design the proposed AI-Based SOAR architecture and clearly identify its major functional components. Develop an AI/ML-based mechanism for context-aware alert analysis...",
        status: "Exact 100%"
      },
      {
        elEn: "Objective 4: Integration & Evaluation",
        elAr: "الهدف 4: التكامل والتقييم المعياري",
        loc: "§1.4.2 Specific Objectives, Bullet 4 (Page 15)",
        textEn: "Integrate the outcomes of dynamic risk-based prioritization with SOAR response decision-making... Define a structured evaluation approach using appropriate machine-learning and operational metrics.",
        status: "Exact 100%"
      }
    ]
  },
  6: {
    titleEn: "Slide 07: Project Scope and Limitations",
    titleAr: "الشريحة 07: نطاق المشروع وحدود الدراسة",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.6 Project Scope and Limitations (Pages 16-17)",
    elements: [
      {
        elEn: "In-Scope Core Dimensions (4 Points)",
        elAr: "المحاور الأربعة ضمن النطاق",
        loc: "§1.6.2 Project Scope, Paragraphs 1-3 (Pages 16-17)",
        textEn: "1. Alert Ingestion & Normalization with AI/ML risk scoring\n2. Connecting analytical components with automated SOAR response workflows\n3. Prototype implementation in controlled simulation environment\n4. Architectural integration focus.",
        status: "Exact 100%"
      },
      {
        elEn: "Project Limitations (3 Boundaries)",
        elAr: "حدود المشروع الأكاديمية والتشغيلية",
        loc: "§1.6.3 Project Limitations, Paragraphs 1-3 (Page 17)",
        textEn: "1. Dataset constraints: Training models on synthetic/public datasets\n2. Lab environment validation vs live production enterprise SOC\n3. Mandatory human oversight for high-impact actions to prevent operational risks.",
        status: "Exact 100%"
      }
    ]
  },
  7: {
    titleEn: "Slide 08: Evolution of Security Operations Technologies",
    titleAr: "الشريحة 08: التطور التاريخي لتقنيات العمليات الأمنية",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2 Technical Background: SOC and Conventional SOAR (Pages 19-20)",
    elements: [
      {
        elEn: "Telemetry & Multi-Sensor Layer (G1)",
        elAr: "الجيل الأول: السجلات المتباينة",
        loc: "§2.2.1, Paragraph 1 (Page 19)",
        textEn: "Security telemetry collected from multiple sources including network and endpoint monitoring, IDS, firewalls operating with different representations.",
        status: "Exact 100%"
      },
      {
        elEn: "SIEM Centralized Log Aggregation (G2)",
        elAr: "الجيل الثاني: أنظمة SIEM المركزية",
        loc: "§2.2.1, Paragraph 2 (Page 19)",
        textEn: "SIEM systems aggregate and query security data from distributed sources, providing centralized log management and basic correlation...",
        status: "Exact 100%"
      },
      {
        elEn: "Conventional SOAR Orchestration (G3)",
        elAr: "الجيل الثالث: منصات SOAR التقليدية",
        loc: "§2.2.2, Paragraph 1 (Page 20)",
        textEn: "SOAR platforms integrate disparate security applications and human processes into a unified framework... data ingestion, prioritization, and process automation.",
        status: "Exact 100%"
      },
      {
        elEn: "Proposed AI-Based SOAR (G4)",
        elAr: "الجيل الرابع: أداة AI-SOAR المقترحة",
        loc: "§2.3.1, Paragraph 1-3 (Pages 21-22)",
        textEn: "AI/ML extends SOAR by contributing data-driven inference to activities difficult to represent through manually specified rules while orchestration coordinates actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Core Distinction Principle",
        elAr: "مبدأ التمايز المعماري بين SIEM و SOAR",
        loc: "§2.2.2, Paragraph 3 (Page 20)",
        textEn: "SIEM primarily supports broad data collection and querying, whereas SOAR introduces configurable workflows that guide or automate incident-response activities.",
        status: "Exact 100%"
      }
    ]
  },
  8: {
    titleEn: "Slide 09: Conventional SOAR: Playbooks & API Orchestration",
    titleAr: "الشريحة 09: منصات SOAR التقليدية ودفاتر العمل",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2.2 Conventional SOAR, Playbooks, and API-Based Orchestration (Pages 20-21)",
    elements: [
      {
        elEn: "Definition of SOAR Platforms",
        elAr: "تعريف منصات SOAR والتكامل",
        loc: "§2.2.2, Paragraph 1 (Page 20)",
        textEn: "SOAR refers to software platforms designed to integrate disparate security applications and human processes into a unified framework. A playbook defines a structured sequence of actions...",
        status: "Exact 100%"
      },
      {
        elEn: "Automated Runbooks & Procedures",
        elAr: "دفاتر الاستجابة وأتمتة المهام",
        loc: "§2.2.2, Paragraph 2 (Page 20)",
        textEn: "Workflows can automate data-collection steps, coordinate actions across multiple systems, and systematically apply standard response procedures...",
        status: "Exact 100%"
      },
      {
        elEn: "Unified Case & Threat Evidence Management",
        elAr: "إدارة القضايا وتوحيد الأدلة الرقمية",
        loc: "§2.2.2, Paragraph 3 (Pages 20-21)",
        textEn: "SOAR technologies reduce fragmentation of security activities by combining alert info, threat intelligence, workflow automation, and analyst collaboration...",
        status: "Exact 100%"
      }
    ]
  },
  9: {
    titleEn: "Slide 10: Limitations of Conventional SOAR Automation",
    titleAr: "الشريحة 10: أوجه القصور في أتمتة SOAR التقليدية",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.2.3 Limitations of Conventional SOAR Automation (Page 21)",
    elements: [
      {
        elEn: "Rigid Predefined Conditional Logic",
        elAr: "جمود القواعد الحتمية سابقة البرمجة",
        loc: "§2.2.3, Paragraph 1 (Page 21)",
        textEn: "Playbooks operate on predefined conditions; when threat behavior deviates from anticipated patterns, static playbooks may fail to trigger appropriately...",
        status: "Exact 100%"
      },
      {
        elEn: "Inability to Contextualize Risk",
        elAr: "الافتقار إلى تقييم سياق المخاطر",
        loc: "§2.2.3, Paragraph 2 (Page 21)",
        textEn: "Conventional SOAR does not inherently assess whether an alert's risk justifies the operational cost of the response action. Significance depends on multiple attributes...",
        status: "Exact 100%"
      },
      {
        elEn: "Disruption Risks of Autonomous Actions",
        elAr: "مخاطر انقطاع الأعمال من الأتمتة المباشرة",
        loc: "§2.2.3, Paragraph 3 (Page 21)",
        textEn: "Fully autonomous execution of high-impact security actions introduces inherent operational risks. The tool must incorporate human oversight mechanisms...",
        status: "Exact 100%"
      },
      {
        elEn: "Synthesis (Muscle vs Brain)",
        elAr: "الاستنتاج المعماري: القوة التنفيذية مقابل العقل التحليلي",
        loc: "§2.2.3, Paragraph 4 (Page 21)",
        textEn: "SOAR provides workflow management, integration, and execution capabilities, whereas AI/ML contributes data-driven inference to activities difficult to represent manually.",
        status: "Exact 100%"
      }
    ]
  },
  10: {
    titleEn: "Slide 11: AI/ML as a Force Multiplier in Security Operations",
    titleAr: "الشريحة 11: الذكاء الاصطناعي كمضاعف قوة في عمليات SOC",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.3 AI and ML as a Force Multiplier in SOC (Pages 21-23)",
    elements: [
      {
        elEn: "Data-Driven Analytical Augmentation Card",
        elAr: "التعزيز التحليلي المعتمد على البيانات",
        loc: "§2.3.1, Paragraph 1-2 (Pages 21-22)",
        textEn: "AI/ML techniques can analyze large and heterogeneous security datasets to identify patterns, classify events, detect anomalous behavior, and support decision making.",
        status: "Exact 100%"
      },
      {
        elEn: "Human-AI Teaming Paradigm Card",
        elAr: "نموذج تكامل الإنسان والذكاء الاصطناعي",
        loc: "§2.3.2, Paragraph 1-3 (Pages 22-23)",
        textEn: "AI/ML does not necessarily replace existing SOC technologies; rather, it provides an analytical layer that complements SIEM and SOAR, acting as a force multiplier.",
        status: "Exact 100%"
      },
      {
        elEn: "Architectural Roles Summary",
        elAr: "الأدوار المعمارية (AI / SOAR / DSR)",
        loc: "§2.3.1 & §1.5 (Pages 15, 21)",
        textEn: "AI/ML (Analytical Augmentation Layer), SOAR (Workflow Execution Platform), DSR (Research Methodology).",
        status: "Exact 100%"
      }
    ]
  },
  11: {
    titleEn: "Slide 12: Comparative Analysis of ML Triage Approaches (Table 2-1)",
    titleAr: "الشريحة 12: المقارنة المعيارية لأنظمة الفرز الأمني (جدول 2-1)",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.4.4 Comparative Analysis of Existing Approaches & Table 2-1 (Pages 25-27)",
    elements: [
      {
        elEn: "Table 2-1: Gupta et al. (2019)",
        elAr: "دراسة جوبتا (Gupta et al. 2019)",
        loc: "Table 2-1, Row 1 (Page 26)",
        textEn: "Real SOC-labeled SOD events | DNN supervised classification | Engineered features; no online feedback | Notified/non-notified | SOAR: No | Binary output; low minority-class precision (0.39)",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Gelman et al. (2023)",
        elAr: "دراسة جيلمان (Gelman et al. 2023)",
        loc: "Table 2-1, Row 2 (Page 26)",
        textEn: "Real MDR data; simulation | RF + NN actionability scoring (TEQ) | Content/context features | Incident/alert scores, suppression | SOAR: No | Preprint; simulated effects",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Liu et al. (2022)",
        elAr: "دراسة ليو (Liu et al. 2022)",
        loc: "Table 2-1, Row 3 (Page 26)",
        textEn: "Enterprise event data | Context2Vector (representation + deviation) | Behavioral context; expert annotation | Contextual risk ranking | SOAR: No | No downstream response",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Wang et al. (2024)",
        elAr: "دراسة وانغ (Wang et al. 2024)",
        loc: "Table 2-1, Row 4 (Page 26)",
        textEn: "5 attack datasets | AlertPro (Isolation Forest + RL active learning) | Iterative analyst feedback | Dynamic alert re-ranking | SOAR: No | Stops at triage/investigation",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1: Chavali et al. (2024)",
        elAr: "دراسة تشافالي (Chavali et al. 2024)",
        loc: "Table 2-1, Row 5 (Page 26)",
        textEn: "3 public IDS datasets | TD3-AP / SAC-AP DRL | Resource/state info; no analyst feedback | Resource-aware priority | SOAR: No | No real-world SOC or SOAR execution",
        status: "Verbatim Table 2-1"
      },
      {
        elEn: "Table 2-1 Synthesis Finding",
        elAr: "خلاصة جدول 2-1 والفجوة المثبتة",
        loc: "§2.4.4, Paragraph 2 & §2.5, Paragraph 1 (Pages 26-27)",
        textEn: "None of the reviewed academic systems integrate downstream automated SOAR response execution (All SOAR/Response = No).",
        status: "Exact 100%"
      }
    ]
  },
  12: {
    titleEn: "Slide 13: The Research Gap: The Missing Integration Link",
    titleAr: "الشريحة 13: الفجوة البحثية: حلقة الوصل المفقودة بين التحليل والأتمتة",
    chapter: "Chapter 2: Background and Literature Review",
    section: "§2.5 Gap Analysis and Problem Synthesis (Pages 27-29)",
    elements: [
      {
        elEn: "Academic Literature Gap",
        elAr: "الفجوة في الأدبيات الأكاديمية",
        loc: "§2.5, Paragraph 1, Lines 1-8 (Page 27)",
        textEn: "Existing research demonstrates ML for alert analysis and SOAR for automated response, while integration remains an open area. Evaluated workflows focus on event ranking rather than downstream SOAR response.",
        status: "Exact 100%"
      },
      {
        elEn: "Commercial SOAR Limitation",
        elAr: "القصور في المنصات التجارية",
        loc: "§2.5, Paragraph 2, Lines 1-6 (Pages 27-28)",
        textEn: "Commercial tools excel at multi-tool orchestration via playbooks, but rely on rigid boolean triggers and lack adaptive machine learning risk assessment.",
        status: "Exact 100%"
      },
      {
        elEn: "Our Research Contribution",
        elAr: "مساهمة مشروعنا البحثية المحددة",
        loc: "§2.5, Paragraph 4, Lines 1-6 (Page 28)",
        textEn: "This project investigates the architectural integration of AI/ML-based alert analysis, risk-based scoring, dynamic prioritization, and SOAR automated response...",
        status: "Exact 100%"
      }
    ]
  },
  13: {
    titleEn: "Slide 14: High-Level Architecture Overview",
    titleAr: "الشريحة 14: المعمارية الشاملة لأداة SOAR المدعومة بالذكاء الاصطناعي",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.2 High-Level Architecture Overview & Figure 3-1 (Pages 31-33)",
    elements: [
      {
        elEn: "Five-Layer Modular Architecture Pipeline",
        elAr: "مسار المعمارية خماسي الطبقات",
        loc: "§3.2, Paragraphs 1-4 & Figure 3-1 (Pages 31-32)",
        textEn: "1. Ingestion Layer (§3.3)\n2. Context Enrichment Layer (§3.4)\n3. ML Triage & Scoring Engine (§3.5)\n4. Prioritization & Suppression (§3.5)\n5. Automated Response Policy (§3.7) + Feedback Loop (§3.8).",
        status: "Exact 100%"
      },
      {
        elEn: "Agent Layer: Defender Agent Role",
        elAr: "طبقة الوكلاء: دور وكيل الدفاع",
        loc: "§3.2.1 Agent Layer Overview, Paragraphs 1-3 (Pages 33-34)",
        textEn: "Defender Agent coordinates the analytical process, invoking selected ML models and passing scores to prioritization and response policies.",
        status: "Exact 100%"
      }
    ]
  },
  14: {
    titleEn: "Slide 15: Alert Ingestion & Schema Normalization",
    titleAr: "الشريحة 15: استيعاب التنبيهات وتوحيد البنية البيانية",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.3 Ingestion and Connectors Module & Figure 3-2 (Pages 34-36)",
    elements: [
      {
        elEn: "Multi-Interface Ingestion Connectors Card",
        elAr: "بطاقة موصلات الاستيعاب متعددة الواجهات",
        loc: "§3.3, Paragraph 1 (Page 34)",
        textEn: "The module serves as the entry point for security alerts from heterogeneous technologies via REST APIs, webhooks, message streams, or log files.",
        status: "Exact 100%"
      },
      {
        elEn: "Schema Normalization Card",
        elAr: "بطاقة توحيد البنية البيانية",
        loc: "§3.3, Paragraph 2 (Page 35)",
        textEn: "Normalizing attributes: alert ID, timestamp, source system, alert type, original severity, source/dest IPs, user, host, and description.",
        status: "Exact 100%"
      },
      {
        elEn: "Validation & Preprocessing Card",
        elAr: "بطاقة التحقق والمعالجة المسبقة",
        loc: "§3.3, Paragraph 3 (Page 35)",
        textEn: "Verifying required fields, converting timestamps to consistent format, standardizing categorical values, removing malformed records.",
        status: "Exact 100%"
      },
      {
        elEn: "Architectural Decoupling Principle",
        elAr: "مبدأ الفصل المعماري للاعتماديات",
        loc: "§3.3, Paragraph 4 (Page 35)",
        textEn: "Separates source-specific integration concerns from internal processing logic so downstream components do not need vendor-specific format logic.",
        status: "Exact 100%"
      }
    ]
  },
  15: {
    titleEn: "Slide 16: Multi-Dimensional Context Enrichment Pipeline",
    titleAr: "الشريحة 16: خط أنابيب إثراء السياق متعدد الأبعاد",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.4 Context Enrichment Layer & Figure 3-3 (Pages 36-37)",
    elements: [
      {
        elEn: "Asset & Identity Context Card",
        elAr: "سياق الأصل وهوية المستخدم",
        loc: "§3.4, Paragraphs 3-4 (Page 36)",
        textEn: "Asset type, business criticality, network location; account type, privilege level, authentication history to distinguish production from test environments.",
        status: "Exact 100%"
      },
      {
        elEn: "Threat Intelligence Context Card",
        elAr: "سياق استخبارات التهديدات الخارجية",
        loc: "§3.4, Paragraph 5 (Pages 36-37)",
        textEn: "Enriching observable indicators (IPs, domains, hashes) with reputation status and known malicious associations (Bridges et al., 2023).",
        status: "Exact 100%"
      },
      {
        elEn: "Historical & Behavioral Context Card",
        elAr: "السياق التاريخي والسلوكي",
        loc: "§3.4, Paragraph 6 (Page 37)",
        textEn: "Determining whether similar alerts appeared previously in time window; behavioral context interpretation based on Context2Vector (Liu et al., 2022).",
        status: "Exact 100%"
      },
      {
        elEn: "Enrichment Modular Resilience & Scope",
        elAr: "المرونة المعيارية وحدود دور الإثراء",
        loc: "§3.4, Paragraph 8 (Page 37)",
        textEn: "Graceful degradation when sources are unavailable; creates enriched object for ML engine without assigning final priority or triggering actions directly.",
        status: "Exact 100%"
      }
    ]
  },
  16: {
    titleEn: "Slide 17: AI/ML Triage & Dynamic Risk Scoring Formulation",
    titleAr: "الشريحة 17: الفرز الذكي وصياغة مخرجات تقييم المخاطر",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.5 Machine Learning Triage and Scoring Engine & Figure 3-4 (Pages 37-39)",
    elements: [
      {
        elEn: "Mandatory Contextual Risk Score [0, 1]",
        elAr: "درجة المخاطر السياقية الإلزامية [0, 1]",
        loc: "§3.5, Paragraph 3 (Page 38)",
        textEn: "Contextual risk score representing estimated operational significance, normalized to consistent range [0, 1] where higher values indicate greater risk.",
        status: "Exact 100%"
      },
      {
        elEn: "Principle of Separation",
        elAr: "مبدأ الفصل المعماري للتحليل عن التنفيذ",
        loc: "§3.5, Paragraph 7 (Page 38)",
        textEn: "The engine produces analytical outputs and does not directly suppress alerts or initiate containment, preventing raw predictions from triggering high-impact actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Distinct Confidence vs. Risk Outputs",
        elAr: "فصل مؤشر الثقة عن درجة المخاطر",
        loc: "§3.5, Paragraph 5 (Page 38)",
        textEn: "Confidence reflects certainty of assessment, distinct from risk. High-risk + low confidence requires analyst review; high confidence enables policy automation.",
        status: "Exact 100%"
      },
      {
        elEn: "Classification & Explanatory Outputs",
        elAr: "مخرجات التصنيف وتفسير القرار",
        loc: "§3.5, Paragraphs 4 & 6 (Page 38)",
        textEn: "Actionability label (Gupta et al., 2019) distinguishing events requiring investigation; top contributing features for analyst validation.",
        status: "Exact 100%"
      }
    ]
  },
  17: {
    titleEn: "Slide 18: Adaptive Alert Prioritization & Noise Suppression",
    titleAr: "الشريحة 18: الأولويات التكيفية وقمع الضجيج الأمني",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.5 Prioritization and Suppression Logic & Figure 3-5 (Pages 39-40)",
    elements: [
      {
        elEn: "Dynamic Queue Prioritization Card",
        elAr: "ترتيب طوابير التحقيق ديناميكياً",
        loc: "§3.5, Paragraph 10 (Page 39)",
        textEn: "Alerts are ranked by continuous contextual risk rather than static product severity, recalculated dynamically as new telemetry arrives (Wang et al., 2024).",
        status: "Exact 100%"
      },
      {
        elEn: "Suppression vs. Deprioritization Card",
        elAr: "القمع المنضبط مقابل خفض الأولوية",
        loc: "§3.5, Paragraph 12 (Pages 39-40)",
        textEn: "Suppressed alerts are excluded from active queues under strict policy and audited; deprioritized alerts remain visible below higher-risk events.",
        status: "Exact 100%"
      },
      {
        elEn: "Policy Safeguards & Overrides Card",
        elAr: "ضمانات السياسات والاستثناءات الإدارية",
        loc: "§3.5, Paragraph 13 (Page 40)",
        textEn: "Operational rules override model scores when critical assets, privileged accounts, or novel threats are detected; low confidence routed to analyst.",
        status: "Exact 100%"
      },
      {
        elEn: "Operational Rationale (22.9% Wait Time Reduction)",
        elAr: "الأساس المنطقي التشغيلي (تقليص 22.9%)",
        loc: "§1.2, Paragraph 4 (Page 14) & §3.5, Paragraph 9",
        textEn: "Dynamic risk-aware ordering reduces wait-time for critical incidents by 22.9% in literature, ensuring threats are identified without analyst overload.",
        status: "Exact 100%"
      }
    ]
  },
  18: {
    titleEn: "Slide 19: Automated Response Playbooks & SOAR Integration",
    titleAr: "الشريحة 19: دفاتر العمل المؤتمتة وتكامل منصة SOAR",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.7 Automated Response Policy & Figure 3-6 (Pages 40-42)",
    elements: [
      {
        elEn: "Orchestrated Response Actions (4 Cards)",
        elAr: "إجراءات الاستجابة المنسقة (4 دفاتر عمل)",
        loc: "§3.7, Paragraph 2 (Page 41)",
        textEn: "1. Endpoint quarantine via EDR API\n2. Perimeter firewall IP block\n3. Privileged account token revocation\n4. Phishing email purge via API.",
        status: "Exact 100%"
      },
      {
        elEn: "Policy Principle (Operational Impact Consideration)",
        elAr: "مبدأ سياسة الاستجابة ومراعاة الأثر التشغيلي",
        loc: "§3.7, Paragraph 1 (Page 40)",
        textEn: "The decision to automate an action considers not only estimated security risk but also potential impact of the response itself (enrichment query vs isolating a production server).",
        status: "Exact 100%"
      }
    ]
  },
  19: {
    titleEn: "Slide 20: Human-AI Teaming: Policy States & Controlled Decision Gates",
    titleAr: "الشريحة 20: تكامل الإنسان والذكاء: حالات السياسة وبوابات القرار المنضبطة",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.7 Automated Response Policy & §2.3.2 Human-AI Teaming (Pages 22-23, 40-42)",
    elements: [
      {
        elEn: "Four Architectural Policy States (S1, S2, S3, S4)",
        elAr: "حالات السياسة الأربع المعتمدة",
        loc: "§3.7, Paragraphs 3-6 (Pages 41-42)",
        textEn: "S1: Automated Response (approved low-risk workflows, high confidence, low blast radius)\nS2: Human Approval Required (containment actions with operational impact)\nS3: Analyst Investigation (low confidence or critical production assets)\nS4: Monitor / Record (retention without containment for auditability).",
        status: "Exact 100%"
      },
      {
        elEn: "Controlled Autonomy Principle",
        elAr: "مبدأ الأتمتة المنضبطة",
        loc: "§3.7, Paragraph 3 (Page 41) & Chhetri et al. (2024)",
        textEn: "The amount of human involvement depends on the uncertainty and consequence associated with the decision; strict safeguards prevent automatic suppression of critical assets.",
        status: "Exact 100%"
      }
    ]
  },
      {
        elEn: "Controlled Autonomy Principle",
        elAr: "مبدأ الأتمتة المنضبطة والموجهة",
        loc: "§3.7, Paragraph 3 (Page 41)",
        textEn: "The amount of human involvement depends on the uncertainty and consequence associated with the decision, preventing disruptive rogue automation.",
        status: "Exact 100%"
      }
    ]
  },
  20: {
    titleEn: "Slide 21: Continuous Analyst Feedback Loop & Model Adaptation",
    titleAr: "الشريحة 21: حلقة التغذية الراجعة المستمرة وتكييف النماذج",
    chapter: "Chapter 3: Proposed System Architecture",
    section: "§3.8 Analyst Feedback Loop & Figure 3-7 (Pages 42-43)",
    elements: [
      {
        elEn: "Analyst Decision Recording Card",
        elAr: "توثيق قرارات وتدخلات المحللين",
        loc: "§3.8, Paragraph 1 (Page 42)",
        textEn: "During triage, analysts confirm/reject risk assessments, adjust priorities, or label true/false positives. During response, they approve/reject actions.",
        status: "Exact 100%"
      },
      {
        elEn: "Model Bias Assessment & Retraining Card",
        elAr: "تقييم تحيز النموذج وإعادة التدريب الدوري",
        loc: "§3.8, Paragraph 2 (Page 42)",
        textEn: "Assessing whether models overestimate/underestimate risk for alert categories; accumulating labeled examples for periodic retraining.",
        status: "Exact 100%"
      },
      {
        elEn: "Threshold Policy Adjustment Card",
        elAr: "إعادة ضبط عتبات الأولويات والقمع",
        loc: "§3.8, Paragraph 3 (Page 43)",
        textEn: "Adjusting prioritization thresholds and suppression rules when operational telemetry indicates excessive false alerts or missed critical events.",
        status: "Exact 100%"
      }
    ]
  },
  21: {
    titleEn: "Slide 22: Design Science Research (DSR) – 6 Rigorous Phases",
    titleAr: "الشريحة 22: منهجية بحوث علوم التصميم (DSR) &ndash; المراحل الست",
    chapter: "Chapter 1: Introduction and Problem Statement",
    section: "§1.5 Project Methodology (Pages 15-16)",
    elements: [
      {
        elEn: "Phases 1-3 (Completed in Graduation Project 1)",
        elAr: "المراحل 1 إلى 3 (المنجزة في مشروع التخرج 1)",
        loc: "§1.5, Paragraphs 2-3 (Pages 15-16)",
        textEn: "Phase 1: Problem Identification & Objectives (§1.2-1.4)\nPhase 2: Literature Review & Gap Mapping (§2.2-2.5)\nPhase 3: System Architecture & Component Design (Chapter 3).",
        status: "Exact 100%"
      },
      {
        elEn: "Phases 4-6 (Planned for Graduation Project 2)",
        elAr: "المراحل 4 إلى 6 (المخططة لمشروع التخرج 2)",
        loc: "§1.5, Paragraphs 3-4 (Page 16)",
        textEn: "Phase 4: Data Collection & Preparation (Weeks 1-4)\nPhase 5: AI/ML Model Development & Risk Calibration (Weeks 5-8)\nPhase 6: SOAR Integration & Prototype Evaluation (Weeks 9-12).",
        status: "Exact 100%"
      }
    ]
  },
  22: {
    titleEn: "Slide 23: System Architecture & Prototype Integration Environment",
    titleAr: "الشريحة 23: معمارية النظام وبيئة التكامل والمحاكاة للنموذج الأولي",
    chapter: "Chapter 3: Proposed System Architecture & Chapter 1 Scope",
    section: "§3.2-3.3 Architecture & §1.6 Scope and Limitations (Pages 16, 31-35)",
    elements: [
      {
        elEn: "Multi-Agent Coordination Layer (§3.2.1)",
        elAr: "طبقة الوكلاء الأذكياء",
        loc: "§3.2.1 (Pages 33-34) & Agrawal et al. (2026)",
        textEn: "Attacker Agent generates adaptive attack activity in controlled testbed; Defender Agent coordinates intelligent defensive analysis, risk scoring, and decision support.",
        status: "Exact 100%"
      },
      {
        elEn: "Ingestion & Connector Module (§3.3)",
        elAr: "وحدة الاستيعاب والموصلات",
        loc: "§3.3 (Pages 34-35)",
        textEn: "Connectors interface with SIEM, EDR, IDS via REST APIs, webhooks, or log streams, standardizing alerts into normalized schemas while retaining source provenance.",
        status: "Exact 100%"
      },
      {
        elEn: "Analytical Scoring Engine & Logic (§3.4, §3.5, §3.6)",
        elAr: "محرك التحليل والتقييم الديناميكي",
        loc: "§3.4-3.6 (Pages 35-40)",
        textEn: "Processes multi-dimensional context to compute continuous normalized risk score [0, 1] and confidence indicators for dynamic queue prioritization.",
        status: "Exact 100%"
      },
      {
        elEn: "SOAR API Playbooks & Prototype Scope (§3.7, §1.6.1)",
        elAr: "دفاتر عمل SOAR ونطاق النموذج الأولي",
        loc: "§3.7 (Pages 40-42) & §1.6.1 (Page 16)",
        textEn: "Translates approved response decisions into automated API executions (Karlzén & Sommestad, 2023; Sworna et al., 2023); evaluated within controlled simulation environment.",
        status: "Exact 100%"
      }
    ]
  },
  23: {
    titleEn: "Slide 24: Operational Incident Handling Workflow & Empirical Benchmarks",
    titleAr: "الشريحة 24: مسار المعالجة التشغيلي للحوادث والمؤشرات المعيارية من الأدبيات",
    chapter: "Chapter 3: Proposed System Architecture & Chapter 2 Literature",
    section: "§3.2 Operational Pipeline & §1.2, §2.4 Empirical Benchmarks (Pages 13-14, 23-28, 31-33)",
    elements: [
      {
        elEn: "End-to-End Operational Pipeline (5 Steps)",
        elAr: "المسار التشغيلي المتكامل (5 خطوات)",
        loc: "§3.2-3.8 System Architecture (Pages 31-43)",
        textEn: "1. Ingestion & Normalization (§3.3)\n2. Context Enrichment (§3.4)\n3. AI Triage & Risk Scoring [0, 1] (§3.5)\n4. Dynamic Prioritization & Policy Gate (§3.6, §3.7)\n5. Controlled SOAR Execution & Feedback (§3.7, §3.8).",
        status: "Exact 100%"
      },
      {
        elEn: "Verified Empirical Benchmarks from Peer-Reviewed Literature",
        elAr: "المؤشرات المعيارية المعتمدة من الأدبيات",
        loc: "§1.2 (Page 14), §2.4.1 (Pages 24-25), §2.4.2 (Pages 25-26), §2.4.3 (Pages 26-27)",
        textEn: "Queue Dwell Time Reduction: 22.9% (Gelman et al., 2023)\nFP Suppression: 54% with 95.1% Actionable Capture (Gelman et al., 2023)\nInference Time: ~300 µs per sample (Chavali et al., 2024)\nAttacker-IP Recall: up to 2.25x improvement (Liu et al., 2022).",
        status: "Exact 100%"
      }
    ]
  },
  24: {
    titleEn: "Slide 25: Current Achievements, Challenges & Phase 2 Roadmap",
    titleAr: "الشريحة 25: ما تم إنجازه، التحديات والحلول، وخارطة طريق مشروع 2",
    chapter: "Chapters 1-3 & Presentation Guide (§9 & §10)",
    section: "Final Synthesis, Challenges & GP2 Roadmap",
    elements: [
      {
        elEn: "Graduation Project 1 Completed Scope",
        elAr: "ما تم إنجازه فعلياً في مشروع تخرج 1",
        loc: "Chapters 1, 2, and 3 Approved Report",
        textEn: "Problem definition (§1.2-1.4), comprehensive lit review and Table 2-1 gap analysis (§2.4-2.5), complete 5-layer system architecture (Chapter 3).",
        status: "Exact 100%"
      },
      {
        elEn: "Challenges & Mitigations Table (Guide §9)",
        elAr: "جدول التحديات والإجراءات المتخذة (دليل §9)",
        loc: "Presentation Guide §9 & Report §1.6, §3.3, §3.7",
        textEn: "1. Alert Schema Variance -> Ingestion Normalization layer [Resolved]\n2. Dataset Constraints -> Curated public SOC data + simulated attack logs [In Progress]\n3. Automation Risk -> Enforced human-in-the-loop gates [Resolved].",
        status: "Guide §9 Table"
      },
      {
        elEn: "Graduation Project 2 Execution Roadmap",
        elAr: "خارطة تنفيذ مشروع تخرج 2 (الأسابيع 1-12)",
        loc: "Chapter 1 (§1.5) & Presentation Guide §10",
        textEn: "Phase 4: Data Preparation (W1-4), Phase 5: Model Training & API coding (W5-8), Phase 6: Prototype testing & final defense (W9-12).",
        status: "Exact 100%"
      }
    ]
  }
};

// Toggle Reference Modal / Drawer
function toggleRefModal() {
  const drawer = document.getElementById('refDrawer');
  if (!drawer) return;
  drawer.classList.toggle('open');
  if (drawer.classList.contains('open')) {
    updateSlideReferences(c);
  }
}

// Close on Escape key
document.addEventListener('keydown', e => {
  if (e.key === 'r' || e.key === 'R') {
    // Only toggle if not focused on an input
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
    toggleRefModal();
  }
  if (e.key === 'Escape') {
    const drawer = document.getElementById('refDrawer');
    if (drawer && drawer.classList.contains('open')) {
      drawer.classList.remove('open');
    }
  }
});

// Update References display for active slide
function updateSlideReferences(slideIdx) {
  const ref = SLIDE_REFS[slideIdx];
  if (!ref) return;

  const pill = document.getElementById('rdSlidePill');
  if (pill) {
    pill.textContent = `Slide ${String(slideIdx + 1).padStart(2, '0')} / 25`;
  }

  // 1. Build Content for Drawer Modal
  const rdContent = document.getElementById('rdContent');
  if (rdContent) {
    let rowsHtml = '';
    ref.elements.forEach(el => {
      rowsHtml += `
        <tr>
          <td style="font-weight:700;color:var(--t1)">
            <span class="${isAR ? 'ar' : 'en'}">${isAR ? el.elAr : el.elEn}</span>
          </td>
          <td style="color:var(--s);font-family:'JetBrains Mono',monospace;font-weight:600">
            ${el.loc}
          </td>
          <td style="font-size:0.75rem;color:var(--t2)">
            ${el.textEn.replace(/\n/g, '<br>')}
          </td>
          <td>
            <span class="rd-badge-exact">✓ ${el.status}</span>
          </td>
        </tr>
      `;
    });

    rdContent.innerHTML = `
      <div class="rd-sec-banner">
        <strong>${isAR ? 'الفصل والقسم المرجعي في تقرير المشروع:' : 'Report Chapter & Section:'}</strong> 
        <span style="color:var(--s);font-weight:700">${ref.chapter} &mdash; ${ref.section}</span>
      </div>
      <table class="rd-table">
        <thead>
          <tr>
            <th style="width:22%">${isAR ? 'عنصر الشريحة' : 'Slide Element'}</th>
            <th style="width:24%">${isAR ? 'الموقع في الملف (القسم / الفقرة)' : 'Exact PDF Location'}</th>
            <th style="width:42%">${isAR ? 'النص والبيانات المأخوذة' : 'Cited Text / Telemetry'}</th>
            <th style="width:12%">${isAR ? 'حالة المطابقة' : 'Status'}</th>
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
            <span style="color:var(--ok);font-size:0.68rem">✓ ${el.status}</span>
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
        🔍 ${isAR ? 'فتح جدول التدقيق والتطابق الكامل' : 'Open Detailed Verification Table (R)'}
      </button>
    `;
  }
}

// Initialize references on load
updateSlideReferences(0);
