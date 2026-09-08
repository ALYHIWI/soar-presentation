# -*- coding: utf-8 -*-
"""
Full Presentation Generator for AI-Based SOAR Tool Graduation Project.
Includes:
- 25 Academic Bilingual Slides (dynamically expandable & editable)
- Stealth Side Dock (100% hidden off-screen, only a discreet dim matte arrow tab on edge)
- Full Slide Studio Lifecycle Management:
  * Add Slide with 4 Pre-Styled Academic Templates (Dual Cards, Trio Pillars, Metrics/Stats, Process Pipeline)
  * Delete Active Slide with Safety Confirmation & Auto-Renumbering
  * Duplicate Active Slide
  * Reorder Slides (Move Earlier / Later)
  * Live In-Place Content Editor with Add/Remove Card Controls
  * Restore Official 25 Slides
- 8 Slide Animation Styles (Cascade, 3D Flip Cube, Cyber Zoom, Soft Dissolve, Slide Up, Glass Flip X, Vortex Swirl, Focus Snap)
- 4 Calm, Eye-Friendly Card Focus & Highlight Interaction Styles (Golden Halo, Glassmorphism Lift, Spotlight Beam, Precision Border) + Click-to-Pin Focus
- 7 Serene Dynamic Animated Canvas Backgrounds with Speed Pace Control
- 10 Ultra-Luxurious Royal Theme Color Palettes & Gradients
- Interactive Presentation Timer
"""

import os
import sys

output_file = r'c:\Users\Mo AL-Yahawy\SOAR\presentation\index.html'

def generate_slides_html():
    import re
    targets = [output_file, output_file + '.bak']
    for t in targets:
        if os.path.exists(t):
            with open(t, 'r', encoding='utf-8') as f:
                c = f.read()
            match = re.search(r'<div id="wrap"[^>]*>(.*?)</div>\s*<!-- Bottom Navigation Bar -->', c, re.DOTALL)
            if match and len(match.group(1).strip()) > 1000:
                return match.group(1)
    raise RuntimeError("Could not find slides HTML in presentation/index.html or backup!")

def generate_html():
    slides_content = generate_slides_html()
    return r'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>AI-Based SOAR Tool &ndash; Graduation Project Presentation</title>
<meta name="description" content="AI-Based Security Orchestration, Automation, and Response (SOAR) Tool - Graduation Project Presentation"/>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;800&display=swap" rel="stylesheet"/>
<style>
/* ================= ROOT DESIGN SYSTEM & LUXURY THEME TOKENS ================= */
:root {
  --p: #c31432;
  --s: #240b36;
  --acc: #ff4d6d;
  --ok: #10b981;
  --wa: #ffb300;
  --bg: #0d040e;
  --bg-card: rgba(28, 8, 22, 0.78);
  --gl: rgba(255, 255, 255, 0.05);
  --br: rgba(195, 20, 50, 0.35);
  --grad: linear-gradient(135deg, #c31432, #240b36);
  --t1: #fbfbfb;
  --t2: rgba(251, 251, 251, 0.82);
  --t3: rgba(251, 251, 251, 0.48);
  --tr: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  --font-en: 'Inter', sans-serif;
  --font-ar: 'Cairo', sans-serif;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* ================= GLOBAL SCROLLBAR ELIMINATION ================= */
html, body {
  width: 100vw;
  max-width: 100vw;
  height: 100vh;
  max-height: 100vh;
  overflow: hidden !important;
  position: fixed;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--t1);
  font-family: var(--font-en);
  user-select: text;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

html::-webkit-scrollbar,
body::-webkit-scrollbar,
*::-webkit-scrollbar {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
}

[dir="rtl"] body {
  font-family: var(--font-ar);
}

/* ================= DYNAMIC BACKGROUND CANVAS & ORBS ================= */
canvas#cv {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 1;
  opacity: 1;
  transition: opacity 0.6s ease;
}

.orb {
  position: fixed;
  border-radius: 50%;
  filter: blur(110px);
  pointer-events: none;
  animation: floatOrb 16s ease-in-out infinite;
  transition: opacity 0.6s ease, background 0.6s ease;
  z-index: 1;
}
.o1 { width: 440px; height: 440px; background: var(--p); opacity: 0.12; top: -100px; right: -100px; }
.o2 { width: 380px; height: 380px; background: var(--s); opacity: 0.10; bottom: -80px; left: -80px; animation-delay: -5s; }
.o3 { width: 280px; height: 280px; background: var(--acc); opacity: 0.08; top: 45%; left: 45%; animation-delay: -10s; }

@keyframes floatOrb {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-24px) rotate(4deg); }
}

/* ================= PRESENTATION WRAPPER ================= */
#wrap {
  width: 100vw;
  max-width: 100vw;
  height: 100vh;
  max-height: 100vh;
  position: relative;
  overflow: hidden !important;
  contain: strict;
  perspective: 1200px;
  perspective-origin: 50% 50%;
  background: transparent !important;
  z-index: 2;
}

/* ================= SLIDE CONTAINER ================= */
.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  max-width: 100vw;
  height: 100vh;
  max-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 40px 60px 80px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  z-index: 1;
  overflow-y: auto;
  overflow-x: hidden !important;
  contain: paint layout;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  transform-style: preserve-3d;
}

.slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  z-index: 2;
}

/* ================= 8 SLIDE ANIMATION STYLES ================= */
#wrap.anim-cascade .slide {
  transform: scale(0.96);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  filter: blur(4px);
  transition: opacity 0.45s cubic-bezier(0.2, 0.8, 0.2, 1),
              transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1),
              visibility 0.45s, filter 0.45s;
}
#wrap.anim-cascade .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: scale(1);
  filter: blur(0px);
}
#wrap.anim-cascade .slide.exit-left {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(0.96) translateX(-35px);
  filter: blur(4px);
}
#wrap.anim-cascade .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(0.96) translateX(35px);
  filter: blur(4px);
}

#wrap.anim-3d .slide {
  transform: scale(0.92) rotateY(15deg);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.5s cubic-bezier(0.2, 0.8, 0.2, 1),
              transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1),
              visibility 0.5s;
}
#wrap.anim-3d .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: scale(1) rotateY(0deg);
}
#wrap.anim-3d .slide.exit-left {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(0.92) rotateY(-15deg);
}
#wrap.anim-3d .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(0.92) rotateY(15deg);
}

#wrap.anim-zoom .slide {
  transform: scale(0.86);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.45s cubic-bezier(0.16, 1, 0.3, 1),
              visibility 0.45s;
}
#wrap.anim-zoom .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: scale(1);
}
#wrap.anim-zoom .slide.exit-left,
#wrap.anim-zoom .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(1.12);
}

#wrap.anim-fade .slide {
  transform: none;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.4s ease-in-out, visibility 0.4s;
}
#wrap.anim-fade .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: none;
}
#wrap.anim-fade .slide.exit-left,
#wrap.anim-fade .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: none;
}

#wrap.anim-slide-up .slide {
  transform: translateY(35px) scale(0.98);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.45s cubic-bezier(0.16, 1, 0.3, 1),
              visibility 0.45s;
}
#wrap.anim-slide-up .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: translateY(0) scale(1);
}
#wrap.anim-slide-up .slide.exit-left,
#wrap.anim-slide-up .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(-35px) scale(0.98);
}

#wrap.anim-flip-x .slide {
  transform: scale(0.94) rotateX(12deg);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.5s cubic-bezier(0.2, 0.8, 0.2, 1),
              transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1),
              visibility 0.5s;
}
#wrap.anim-flip-x .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: scale(1) rotateX(0deg);
}
#wrap.anim-flip-x .slide.exit-left,
#wrap.anim-flip-x .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(0.94) rotateX(-12deg);
}

#wrap.anim-swirl .slide {
  transform: scale(0.92) rotate(-2.5deg);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.5s cubic-bezier(0.16, 1, 0.3, 1),
              visibility 0.5s;
}
#wrap.anim-swirl .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: scale(1) rotate(0deg);
}
#wrap.anim-swirl .slide.exit-left,
#wrap.anim-swirl .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(1.06) rotate(2.5deg);
}

#wrap.anim-focus .slide {
  transform: scale(0.95);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  filter: blur(8px);
  transition: opacity 0.4s ease, transform 0.4s ease, filter 0.4s ease, visibility 0.4s;
}
#wrap.anim-focus .slide.active {
  opacity: 1;
  visibility: visible;
  pointer-events: all;
  transform: scale(1);
  filter: blur(0px);
}
#wrap.anim-focus .slide.exit-left,
#wrap.anim-focus .slide.exit-right {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: scale(1.04);
  filter: blur(8px);
}

/* ================= CARD FOCUS & HIGHLIGHT INTERACTION STYLES ================= */
.card, .sb, .fs, .tcard, .ti, .alr {
  cursor: pointer;
  transition: var(--tr);
}

body.focus-halo .card:hover, body.focus-halo .card.pinned-focus,
body.focus-halo .sb:hover, body.focus-halo .sb.pinned-focus,
body.focus-halo .fs:hover, body.focus-halo .fs.pinned-focus,
body.focus-halo .tcard:hover, body.focus-halo .tcard.pinned-focus,
body.focus-halo .alr:hover, body.focus-halo .alr.pinned-focus {
  border-color: var(--s);
  box-shadow: 0 4px 22px rgba(212, 175, 55, 0.22);
}

body.focus-lift .card:hover, body.focus-lift .card.pinned-focus,
body.focus-lift .sb:hover, body.focus-lift .sb.pinned-focus,
body.focus-lift .fs:hover, body.focus-lift .fs.pinned-focus,
body.focus-lift .tcard:hover, body.focus-lift .tcard.pinned-focus,
body.focus-lift .alr:hover, body.focus-lift .alr.pinned-focus {
  transform: translateY(-5px);
  border-color: rgba(255, 255, 255, 0.38);
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(25px);
}

body.focus-spotlight .g2:hover > *:not(:hover):not(.pinned-focus),
body.focus-spotlight .g3:hover > *:not(:hover):not(.pinned-focus),
body.focus-spotlight .g4:hover > *:not(:hover):not(.pinned-focus),
body.focus-spotlight .tg:hover > *:not(:hover):not(.pinned-focus),
body.focus-spotlight .srow:hover > *:not(:hover):not(.pinned-focus),
body.focus-spotlight .flow:hover > *:not(:hover):not(.pinned-focus),
body.focus-spotlight .al:hover > *:not(:hover):not(.pinned-focus) {
  opacity: 0.42;
  transform: scale(0.985);
  transition: opacity 0.35s ease, transform 0.35s ease;
}
body.focus-spotlight .card:hover, body.focus-spotlight .card.pinned-focus,
body.focus-spotlight .sb:hover, body.focus-spotlight .sb.pinned-focus,
body.focus-spotlight .fs:hover, body.focus-spotlight .fs.pinned-focus,
body.focus-spotlight .tcard:hover, body.focus-spotlight .tcard.pinned-focus,
body.focus-spotlight .alr:hover, body.focus-spotlight .alr.pinned-focus {
  border-color: var(--s);
  box-shadow: 0 0 25px rgba(212, 175, 55, 0.3);
  transform: scale(1.02);
  z-index: 5;
}

body.focus-border .card:hover, body.focus-border .card.pinned-focus,
body.focus-border .sb:hover, body.focus-border .sb.pinned-focus,
body.focus-border .fs:hover, body.focus-border .fs.pinned-focus,
body.focus-border .tcard:hover, body.focus-border .tcard.pinned-focus,
body.focus-border .alr:hover, body.focus-border .alr.pinned-focus {
  border-color: var(--s);
  outline: 1.5px solid var(--s);
  outline-offset: -1px;
}

/* Staggered Element Entrance */
.slide .tag,
.slide h1,
.slide h2,
.slide p.lead,
.slide .gl,
.slide .card,
.slide .sb,
.slide .tcard,
.slide .ti,
.slide .alr,
.slide .fs,
.slide .hl,
.slide .tbl-wrap,
.slide .pills {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

.slide.active .tag { opacity: 1; transform: translateY(0); transition-delay: 0.08s; }
.slide.active h1, .slide.active h2.st { opacity: 1; transform: translateY(0); transition-delay: 0.16s; }
.slide.active .gl { opacity: 1; transform: translateY(0) scaleX(1); transition-delay: 0.22s; }
.slide.active p.lead { opacity: 1; transform: translateY(0); transition-delay: 0.26s; }
.slide.active .pills { opacity: 1; transform: translateY(0); transition-delay: 0.32s; }

.slide.active .card:nth-child(1) { opacity: 1; transform: translateY(0); transition-delay: 0.30s; }
.slide.active .card:nth-child(2) { opacity: 1; transform: translateY(0); transition-delay: 0.38s; }
.slide.active .card:nth-child(3) { opacity: 1; transform: translateY(0); transition-delay: 0.46s; }
.slide.active .card:nth-child(4) { opacity: 1; transform: translateY(0); transition-delay: 0.54s; }

.slide.active .sb:nth-child(1) { opacity: 1; transform: translateY(0); transition-delay: 0.32s; }
.slide.active .sb:nth-child(2) { opacity: 1; transform: translateY(0); transition-delay: 0.40s; }
.slide.active .sb:nth-child(3) { opacity: 1; transform: translateY(0); transition-delay: 0.48s; }
.slide.active .sb:nth-child(4) { opacity: 1; transform: translateY(0); transition-delay: 0.56s; }

.slide.active .tcard:nth-child(1) { opacity: 1; transform: translateY(0); transition-delay: 0.25s; }
.slide.active .tcard:nth-child(2) { opacity: 1; transform: translateY(0); transition-delay: 0.32s; }
.slide.active .tcard:nth-child(3) { opacity: 1; transform: translateY(0); transition-delay: 0.39s; }
.slide.active .tcard:nth-child(4) { opacity: 1; transform: translateY(0); transition-delay: 0.46s; }
.slide.active .tcard:nth-child(5) { opacity: 1; transform: translateY(0); transition-delay: 0.53s; }
.slide.active .tcard:nth-child(6) { opacity: 1; transform: translateY(0); transition-delay: 0.60s; }

.slide.active .fs:nth-child(1) { opacity: 1; transform: translateY(0); transition-delay: 0.26s; }
.slide.active .fs:nth-child(3) { opacity: 1; transform: translateY(0); transition-delay: 0.34s; }
.slide.active .fs:nth-child(5) { opacity: 1; transform: translateY(0); transition-delay: 0.42s; }
.slide.active .fs:nth-child(7) { opacity: 1; transform: translateY(0); transition-delay: 0.50s; }
.slide.active .fs:nth-child(9) { opacity: 1; transform: translateY(0); transition-delay: 0.58s; }

.slide.active .ti:nth-child(1) { opacity: 1; transform: translateY(0); transition-delay: 0.26s; }
.slide.active .ti:nth-child(2) { opacity: 1; transform: translateY(0); transition-delay: 0.34s; }
.slide.active .ti:nth-child(3) { opacity: 1; transform: translateY(0); transition-delay: 0.42s; }
.slide.active .ti:nth-child(4) { opacity: 1; transform: translateY(0); transition-delay: 0.50s; }
.slide.active .ti:nth-child(5) { opacity: 1; transform: translateY(0); transition-delay: 0.58s; }
.slide.active .ti:nth-child(6) { opacity: 1; transform: translateY(0); transition-delay: 0.66s; }

.slide.active .alr:nth-child(1) { opacity: 1; transform: translateY(0); transition-delay: 0.25s; }
.slide.active .alr:nth-child(2) { opacity: 1; transform: translateY(0); transition-delay: 0.33s; }
.slide.active .alr:nth-child(3) { opacity: 1; transform: translateY(0); transition-delay: 0.41s; }
.slide.active .alr:nth-child(4) { opacity: 1; transform: translateY(0); transition-delay: 0.49s; }
.slide.active .alr:nth-child(5) { opacity: 1; transform: translateY(0); transition-delay: 0.57s; }

.slide.active .hl { opacity: 1; transform: translateY(0); transition-delay: 0.48s; }
.slide.active .tbl-wrap { opacity: 1; transform: translateY(0); transition-delay: 0.32s; }

/* ================= BADGES & HEADERS ================= */
.sn {
  position: absolute;
  top: 24px;
  right: 60px;
  font-size: 12px;
  font-weight: 700;
  color: var(--t3);
  letter-spacing: 2px;
  font-family: 'JetBrains Mono', monospace;
  background: rgba(255, 255, 255, 0.05);
  padding: 4px 14px;
  border-radius: 20px;
  border: 1px solid var(--br);
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}
[dir="rtl"] .sn { right: auto; left: 60px; }

.content-box {
  width: 100%;
  max-width: 1160px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 18px;
  border-radius: 100px;
  background: rgba(212, 175, 55, 0.14);
  border: 1px solid var(--br);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: var(--s);
  margin-bottom: 12px;
  box-shadow: 0 0 20px rgba(212, 175, 55, 0.15);
}

.tag svg { color: var(--s); }

.dp {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--ok);
  box-shadow: 0 0 10px var(--ok);
  animation: pulseDot 2s infinite ease-in-out;
}
@keyframes pulseDot { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.4); opacity: 0.4; } }

h1.hero {
  font-size: clamp(2rem, 4.2vw, 3.4rem);
  font-weight: 900;
  line-height: 1.15;
  margin-bottom: 16px;
  text-align: center;
  background: linear-gradient(135deg, #ffffff 15%, var(--p) 65%, var(--s) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 4px 20px rgba(0,0,0,0.5);
}

h2.st {
  font-size: clamp(1.4rem, 2.8vw, 2.2rem);
  font-weight: 800;
  margin-bottom: 8px;
  text-align: center;
  background: linear-gradient(135deg, #ffffff 20%, var(--p) 70%, var(--s) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gl {
  width: 100px;
  height: 3px;
  background: linear-gradient(90deg, transparent, var(--p), var(--s), transparent);
  margin: 6px auto 16px;
  border-radius: 2px;
  box-shadow: 0 0 12px var(--p);
}

p.lead {
  font-size: clamp(0.85rem, 1.4vw, 1.05rem);
  color: var(--t2);
  text-align: center;
  max-width: 820px;
  line-height: 1.65;
  margin-bottom: 24px;
}

/* ================= GRIDS & GLASS CARDS ================= */
.g2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; width: 100%; }
.g3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; width: 100%; }
.g4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; width: 100%; }

.card {
  background: var(--bg-card);
  border: 1px solid var(--br);
  border-radius: 14px;
  padding: 20px;
  position: relative;
  backdrop-filter: blur(18px);
  display: flex;
  flex-direction: column;
  gap: 10px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.35);
}

.card-h {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.96rem;
  font-weight: 700;
  color: var(--t1);
}

.ci {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--br);
  color: var(--s);
  flex-shrink: 0;
}

.card p, .card ul {
  font-size: 0.8rem;
  color: var(--t2);
  line-height: 1.6;
}

.card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.card ul li {
  display: flex;
  align-items: flex-start;
  gap: 8px;
}
.card ul li::before {
  content: '▸';
  color: var(--s);
  font-size: 10px;
  margin-top: 2px;
}
[dir="rtl"] .card ul li::before { content: '◂'; }

/* Highlight Callout */
.hl {
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.14), rgba(249, 217, 118, 0.08));
  border: 1px solid var(--br);
  border-radius: 12px;
  padding: 14px 18px;
  width: 100%;
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

.hl p {
  font-size: 0.84rem;
  color: var(--t2);
  line-height: 1.6;
}

.hl strong { color: var(--s); }

/* Stats Row */
.srow {
  display: flex;
  gap: 12px;
  width: 100%;
}

.sb {
  flex: 1;
  background: var(--bg-card);
  border: 1px solid var(--br);
  border-radius: 12px;
  padding: 14px;
  text-align: center;
  backdrop-filter: blur(16px);
}

.snum {
  font-size: 1.9rem;
  font-weight: 900;
  background: linear-gradient(135deg, #fff, var(--s));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-family: 'JetBrains Mono', monospace;
}

.slbl {
  font-size: 0.68rem;
  color: var(--t3);
  margin-top: 4px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
}

/* Pipeline Flow */
.flow {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
  width: 100%;
}

.fs {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 14px 12px;
  background: var(--bg-card);
  border: 1px solid var(--br);
  border-radius: 12px;
  min-width: 130px;
  text-align: center;
  backdrop-filter: blur(16px);
}
.fs .fi { color: var(--s); }
.fs .fl { font-size: 0.74rem; font-weight: 700; color: var(--t1); }
.fs .sub { font-size: 0.65rem; color: var(--t3); }

@keyframes cyberPulse {
  0%, 100% {
    color: var(--p);
    transform: scale(1);
    filter: drop-shadow(0 0 2px var(--p));
  }
  50% {
    color: var(--s);
    transform: scale(1.3);
    filter: drop-shadow(0 0 10px var(--s));
  }
}

.farr {
  color: var(--p);
  font-size: 16px;
  padding: 0 4px;
  animation: cyberPulse 2s infinite ease-in-out;
  display: inline-block;
  font-weight: bold;
}
[dir="rtl"] .farr { transform: rotate(180deg); }

/* Comparison Table */
.tbl-wrap {
  width: 100%;
  overflow-x: auto;
  scrollbar-width: none;
}
table.ctbl {
  width: 100%;
  border-collapse: collapse;
  background: var(--bg-card);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--br);
  font-size: 0.8rem;
}
table.ctbl th, table.ctbl td {
  padding: 10px 14px;
  text-align: left;
  border-bottom: 1px solid var(--br);
}
[dir="rtl"] table.ctbl th, [dir="rtl"] table.ctbl td { text-align: right; }
table.ctbl th {
  background: rgba(255, 255, 255, 0.05);
  color: var(--s);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 0.72rem;
}
table.ctbl tr:hover td { background: rgba(255, 255, 255, 0.04); }

/* Timeline */
.tl {
  display: flex;
  flex-direction: column;
  gap: 0;
  width: 100%;
}
.ti {
  display: grid;
  grid-template-columns: 36px 1fr;
  gap: 12px;
  position: relative;
}
.ti:not(:last-child)::after {
  content: '';
  position: absolute;
  left: 17px; top: 36px; bottom: -8px;
  width: 2px;
  background: linear-gradient(180deg, var(--p), transparent);
}
[dir="rtl"] .ti:not(:last-child)::after { left: auto; right: 17px; }
.td {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  border: 1.5px solid var(--p);
  display: flex; align-items: center; justify-content: center;
  color: var(--s);
  flex-shrink: 0;
  transition: var(--tr);
}
.tic { padding: 4px 0 14px; }
.tic h3 { font-size: 0.88rem; font-weight: 700; margin-bottom: 2px; color: var(--t1); }
.tic p { font-size: 0.76rem; color: var(--t2); line-height: 1.5; }

/* Team Grid */
.tg {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  width: 100%;
}
.tcard {
  background: var(--bg-card);
  border: 1px solid var(--br);
  border-radius: 12px;
  padding: 16px 12px;
  text-align: center;
  backdrop-filter: blur(16px);
}
.tcard .av {
  width: 44px; height: 44px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 10px;
  background: linear-gradient(135deg, var(--p), var(--s));
  color: #000;
  font-weight: 800;
  transition: transform 0.3s ease;
}
.tcard:hover .av { transform: scale(1.1) rotate(6deg); }
.tcard .nm { font-size: 0.82rem; font-weight: 700; margin-bottom: 3px; color: var(--t1); }
.tcard .rl { font-size: 0.7rem; color: var(--s); font-weight: 600; }
.tcard .desc { font-size: 0.68rem; color: var(--t3); margin-top: 4px; }

/* Architecture Layers */
.al {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
}
.alr {
  display: flex;
  gap: 12px;
  padding: 10px 14px;
  border-radius: 10px;
  border: 1px solid var(--br);
  background: var(--bg-card);
  backdrop-filter: blur(16px);
  align-items: center;
}
.all {
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--p);
  min-width: 130px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  gap: 6px;
}
.ali {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  flex: 1;
}
.ai {
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.72rem;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--br);
  color: var(--t2);
  transition: transform 0.2s ease;
}
.ai:hover { transform: scale(1.05); border-color: var(--s); }
.ai.cy { background: rgba(56, 189, 248, 0.1); border-color: rgba(56, 189, 248, 0.3); color: #7dd3fc; }
.ai.gr { background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.3); color: #6ee7b7; }
.ai.rd { background: rgba(225, 29, 72, 0.1); border-color: rgba(225, 29, 72, 0.3); color: #fda4af; }
.ai.ye { background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3); color: #fde68a; }

/* Pills */
.pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
.pill { padding: 4px 12px; border-radius: 100px; font-size: 0.72rem; font-weight: 600; border: 1px solid; transition: transform 0.2s; }
.pill:hover { transform: scale(1.06); }
.pp { background: rgba(212, 175, 55, 0.15); border-color: var(--br); color: var(--s); }
.pc { background: rgba(56, 189, 248, 0.1); border-color: rgba(56, 189, 248, 0.3); color: #7dd3fc; }
.pr { background: rgba(225, 29, 72, 0.1); border-color: rgba(225, 29, 72, 0.3); color: #fda4af; }
.pg { background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.3); color: #6ee7b7; }
.py { background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3); color: #fde68a; }

/* ================= TOP PROGRESS BAR ================= */
#pb {
  position: fixed;
  top: 0; left: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--p), var(--s), var(--ok), var(--s), var(--p));
  background-size: 300% 100%;
  animation: gradientShimmer 6s linear infinite;
  z-index: 100;
  transition: width 0.45s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 0 15px var(--s), 0 0 5px var(--p);
}

@keyframes gradientShimmer {
  0% { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}

/* ================= 100% STEALTH DOCK WITH MATTE ARROW TAB ================= */
#stealthDock {
  position: fixed;
  top: 24px;
  left: 0;
  z-index: 150;
  display: flex;
  align-items: center;
  transform: translateX(calc(-100% + 26px));
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
[dir="rtl"] #stealthDock {
  left: auto;
  right: 0;
  transform: translateX(calc(100% - 26px));
}
#stealthDock.open {
  transform: translateX(0) !important;
}
[dir="rtl"] #stealthDock.open {
  transform: translateX(0) !important;
}

#dockMenu {
  background: rgba(10, 10, 14, 0.96);
  border: 1px solid var(--br);
  border-left: none;
  border-radius: 0 12px 12px 0;
  padding: 8px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  backdrop-filter: blur(30px);
  box-shadow: 6px 8px 30px rgba(0, 0, 0, 0.8);
  width: auto;
  white-space: nowrap;
}
[dir="rtl"] #dockMenu {
  border-left: 1px solid var(--br);
  border-right: none;
  border-radius: 12px 0 0 12px;
}

/* Subtle, matte, discreet 26px arrow tab resting quietly on edge */
#dockToggle {
  width: 26px;
  height: 42px;
  background: rgba(16, 16, 22, 0.45);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-left: none;
  border-radius: 0 8px 8px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: var(--t3);
  opacity: 0.35;
  transition: opacity 0.3s, background 0.3s, color 0.3s;
  flex-shrink: 0;
  backdrop-filter: blur(10px);
}
[dir="rtl"] #dockToggle {
  border-left: 1px solid rgba(255, 255, 255, 0.1);
  border-right: none;
  border-radius: 8px 0 0 8px;
}
#dockToggle:hover {
  opacity: 0.95;
  color: var(--s);
  background: rgba(22, 22, 32, 0.9);
}
#stealthDock.open #dockToggle {
  opacity: 0.95;
  color: var(--s);
}
#dockToggle svg {
  transition: transform 0.4s ease;
}
#stealthDock.open #dockToggle svg {
  transform: rotate(180deg);
}
[dir="rtl"] #stealthDock:not(.open) #dockToggle svg {
  transform: rotate(180deg);
}
[dir="rtl"] #stealthDock.open #dockToggle svg {
  transform: rotate(0deg);
}

.tbtn {
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid var(--br);
  background: rgba(255, 255, 255, 0.05);
  color: var(--t1);
  cursor: pointer;
  font-size: 11px;
  font-weight: 700;
  transition: var(--tr);
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}
.tbtn:hover {
  background: rgba(255, 255, 255, 0.12);
  border-color: var(--s);
  color: #fff;
  transform: translateY(-2px);
}

/* ================= BOTTOM NAVIGATION BAR (ZERO SCROLLBAR) ================= */
#nav {
  position: fixed;
  bottom: 22px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 100;
  background: rgba(10, 10, 14, 0.92);
  border: 1px solid var(--br);
  border-radius: 100px;
  padding: 6px 18px;
  backdrop-filter: blur(25px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.6);
}

.nb {
  width: 32px; height: 32px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.15);
  background: transparent;
  color: var(--t1);
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  transition: var(--tr);
}
.nb:hover { background: rgba(255, 255, 255, 0.1); border-color: var(--s); transform: scale(1.1); color: var(--s); }
.nb:disabled { opacity: 0.25; cursor: not-allowed; transform: none; }

#sc {
  font-size: 12px;
  font-weight: 700;
  color: var(--t2);
  min-width: 60px;
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
}

#sd {
  display: flex;
  gap: 5px;
  align-items: center;
  max-width: 320px;
  overflow-x: auto;
  overflow-y: hidden;
  padding: 4px 6px;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
#sd::-webkit-scrollbar {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
}

.di {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  cursor: pointer;
  transition: var(--tr);
  flex-shrink: 0;
}
.di.active { background: var(--s); width: 18px; border-radius: 4px; box-shadow: 0 0 10px var(--s); }

/* ================= CONTROL PANEL DRAWER ================= */
#cp {
  position: fixed;
  top: 0;
  right: -460px;
  width: 440px;
  height: 100vh;
  background: rgba(8, 8, 12, 0.98);
  border-left: 1px solid var(--br);
  backdrop-filter: blur(40px);
  z-index: 200;
  transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
  padding: 22px;
  box-shadow: -10px 0 40px rgba(0, 0, 0, 0.8);
  scrollbar-width: none;
}
[dir="rtl"] #cp {
  right: auto;
  left: -460px;
  border-left: none;
  border-right: 1px solid var(--br);
  transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 10px 0 40px rgba(0,0,0,0.8);
}
#cp.open { right: 0; }
[dir="rtl"] #cp.open { left: 0; }

.cph { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.cpt { font-size: 1.1rem; font-weight: 800; display: flex; align-items: center; gap: 8px; color: var(--s); }
.cpc { background: none; border: 1px solid var(--br); color: var(--t1); width: 32px; height: 32px; border-radius: 8px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
.cpc:hover { border-color: var(--s); color: #fff; }
.cps { margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.08); }
.cps:last-child { border-bottom: none; }
.cpst { font-size: 0.72rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; color: var(--s); margin-bottom: 10px; display: flex; align-items: center; gap: 6px; }
.cpr { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.cpl { font-size: 0.82rem; color: var(--t2); }

/* Switch */
.csw { width: 42px; height: 22px; border-radius: 11px; background: rgba(255, 255, 255, 0.15); border: none; cursor: pointer; position: relative; transition: background 0.3s; }
.csw::after { content: ''; position: absolute; top: 2px; left: 2px; width: 18px; height: 18px; border-radius: 50%; background: white; transition: left 0.3s; }
.csw.on { background: var(--p); }
.csw.on::after { left: 22px; }
[dir="rtl"] .csw::after { left: auto; right: 2px; transition: right 0.3s; }
[dir="rtl"] .csw.on::after { right: 22px; }

/* Mode Selector Pills */
.mode-pills { display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; margin-top: 6px; }
.mode-pills-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 6px; }
.mpill {
  padding: 8px 10px;
  border-radius: 8px;
  background: var(--gl);
  border: 1px solid var(--br);
  color: var(--t2);
  font-size: 0.74rem;
  font-weight: 700;
  cursor: pointer;
  text-align: center;
  transition: var(--tr);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}
.mpill:hover { border-color: var(--s); color: #fff; background: rgba(255, 255, 255, 0.08); }
.mpill.active {
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.25), rgba(249, 217, 118, 0.2));
  border-color: var(--s);
  color: #fff;
  box-shadow: 0 0 12px rgba(212, 175, 55, 0.25);
}

/* ================= 10 ROYAL LUXURY THEME GRID ================= */
.theme-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin-top: 8px;
}
.tcard-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--br);
  color: var(--t1);
  cursor: pointer;
  transition: var(--tr);
  text-align: left;
}
[dir="rtl"] .tcard-btn { text-align: right; }
.tcard-btn:hover {
  background: rgba(255, 255, 255, 0.09);
  border-color: var(--s);
  transform: translateY(-2px);
}
.tcard-btn.active {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.12), rgba(255, 255, 255, 0.05));
  border-color: var(--s);
  box-shadow: 0 0 14px rgba(212, 175, 55, 0.25);
}
.t-swatch {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  flex-shrink: 0;
  box-shadow: 0 0 8px rgba(0,0,0,0.6);
  border: 1.5px solid rgba(255, 255, 255, 0.4);
}
.t-name {
  font-size: 0.72rem;
  font-weight: 700;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: var(--t2);
}
.tcard-btn.active .t-name {
  color: #fff;
}

/* Slide Directory */
.snl { display: flex; flex-direction: column; gap: 5px; max-height: 180px; overflow-y: auto; padding-right: 4px; scrollbar-width: none; }
.sni { padding: 8px 12px; border-radius: 8px; background: var(--gl); border: 1px solid transparent; cursor: pointer; font-size: 0.76rem; color: var(--t2); transition: var(--tr); }
.sni:hover { border-color: var(--p); color: var(--t1); transform: translateX(4px); }
[dir="rtl"] .sni:hover { transform: translateX(-4px); }
.sni.active { border-color: var(--s); background: rgba(212, 175, 55, 0.18); color: #fff; font-weight: 700; }

/* Timer Box */
.timer-box {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid var(--br);
  border-radius: 10px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.timer-val {
  font-size: 1.8rem;
  font-weight: 900;
  font-family: 'JetBrains Mono', monospace;
  color: var(--s);
  letter-spacing: 2px;
}
.timer-btns { display: flex; gap: 8px; }
.t-btn-act {
  padding: 5px 12px;
  font-size: 0.72rem;
  font-weight: 700;
  border-radius: 6px;
  border: 1px solid var(--br);
  background: rgba(255, 255, 255, 0.08);
  color: var(--t1);
  cursor: pointer;
  transition: var(--tr);
}
.t-btn-act:hover { background: var(--p); border-color: var(--s); transform: scale(1.05); color: #000; }

/* ================= FLOATING LIVE EDIT TOOLBAR ================= */
#liveEditToolbar {
  position: fixed;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(14, 14, 20, 0.95);
  border: 1px solid var(--br);
  border-radius: 100px;
  padding: 6px 14px;
  z-index: 150;
  display: none;
  align-items: center;
  gap: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(25px);
}
.let-badge {
  font-size: 0.74rem;
  font-weight: 800;
  color: var(--s);
  padding: 0 8px;
}
.let-btn {
  padding: 5px 12px;
  border-radius: 50px;
  border: 1px solid var(--br);
  background: rgba(255, 255, 255, 0.06);
  color: var(--t1);
  font-size: 0.72rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--tr);
  display: flex;
  align-items: center;
  gap: 4px;
}
.let-btn:hover { background: rgba(255, 255, 255, 0.14); border-color: var(--s); color: #fff; }
.let-btn.primary { background: var(--p); border-color: var(--s); color: #000; }

/* ================= MODAL DIALOGS ================= */
.modal-backdrop {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(12px);
  z-index: 300;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.modal-card {
  width: 100%;
  max-width: 540px;
  background: rgba(12, 12, 18, 0.98);
  border: 1px solid var(--br);
  border-radius: 16px;
  padding: 22px;
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.9);
  animation: modalPop 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
@keyframes modalPop {
  0% { opacity: 0; transform: scale(0.92) translateY(15px); }
  100% { opacity: 1; transform: scale(1) translateY(0); }
}
.modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.modal-title { font-size: 1rem; font-weight: 800; color: var(--s); display: flex; align-items: center; gap: 8px; }
.modal-close { background: none; border: 1px solid var(--br); color: var(--t1); width: 28px; height: 28px; border-radius: 6px; cursor: pointer; display: flex; align-items: center; justify-content: center; }
.modal-label { font-size: 0.75rem; font-weight: 700; color: var(--t2); margin-bottom: 6px; display: block; }
.modal-input {
  width: 100%;
  padding: 10px 14px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--br);
  border-radius: 8px;
  color: var(--t1);
  font-family: inherit;
  font-size: 0.82rem;
  outline: none;
  transition: border-color 0.2s;
}
.modal-input:focus { border-color: var(--s); box-shadow: 0 0 10px rgba(212, 175, 55, 0.2); }
.tpl-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin-top: 8px; }
.tpl-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--br);
  color: var(--t1);
  cursor: pointer;
  text-align: left;
  transition: var(--tr);
}
[dir="rtl"] .tpl-btn { text-align: right; }
.tpl-btn:hover { background: rgba(255, 255, 255, 0.08); border-color: var(--s); }
.tpl-btn.active { border-color: var(--s); background: rgba(212, 175, 55, 0.15); box-shadow: 0 0 12px rgba(212, 175, 55, 0.2); }
.tpl-icon { font-size: 1.4rem; }
.tpl-name { font-size: 0.78rem; font-weight: 700; color: var(--t1); }
.tpl-desc { font-size: 0.65rem; color: var(--t3); margin-top: 2px; }
.modal-footer { display: flex; justify-content: flex-end; gap: 8px; margin-top: 20px; padding-top: 14px; border-top: 1px solid rgba(255, 255, 255, 0.08); }

/* Responsive */
@media (max-width: 900px) {
  .slide { padding: 40px 20px 80px; }
  .g2, .g3, .g4, .tg { grid-template-columns: 1fr; }
  .tc { grid-template-columns: 1fr; }
  .srow { flex-wrap: wrap; }
  #cp { width: 100vw; right: -100vw; }
  [dir="rtl"] #cp { left: -100vw; }
}
</style>
</head>
<body class="focus-halo">

<div id="pb"></div>
<canvas id="cv"></canvas>
<div class="orb o1"></div>
<div class="orb o2"></div>
<div class="orb o3"></div>

<!-- 100% STEALTH DOCK WITH MATTE ARROW TAB -->
<div id="stealthDock">
  <div id="dockMenu">
    <button class="tbtn" id="bl" onclick="tL()">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10z"/></svg>
      <span id="ll">العربية</span>
    </button>
    <button class="tbtn" onclick="toggleEditMode()" title="Slide Studio & In-Place Editor">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
      <span class="en">Studio</span><span class="ar" style="display:none">الاستوديو</span>
    </button>
    <button class="tbtn" onclick="tF()">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
      <span class="en">Fullscreen</span><span class="ar" style="display:none">ملء الشاشة</span>
    </button>
    <button class="tbtn" onclick="tC()">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span class="en">Settings</span><span class="ar" style="display:none">الإعدادات</span>
    </button>
  </div>
  <button id="dockToggle" onclick="toggleDock()" title="Toggle Controls">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
  </button>
</div>

<!-- FLOATING LIVE EDIT TOOLBAR -->
<div id="liveEditToolbar">
  <span class="let-badge">✏️ <span class="en">Slide Studio</span><span class="ar" style="display:none">استوديو التحرير</span></span>
  <button class="let-btn" onclick="addCardToActiveSlide()">➕ <span class="en">Add Card</span><span class="ar" style="display:none">إضافة بطاقة</span></button>
  <button class="let-btn" onclick="removeLastCardFromActiveSlide()">🗑️ <span class="en">Remove Card</span><span class="ar" style="display:none">حذف بطاقة</span></button>
  <button class="let-btn primary" onclick="saveEdits()">💾 <span class="en">Save Changes</span><span class="ar" style="display:none">حفظ التغييرات</span></button>
  <button class="let-btn" onclick="toggleEditMode()">✕ <span class="en">Done</span><span class="ar" style="display:none">تم</span></button>
</div>

<!-- ADD SLIDE TEMPLATE MODAL -->
<div id="addSlideModal" class="modal-backdrop">
  <div class="modal-card">
    <div class="modal-header">
      <div class="modal-title">
        <span>➕</span>
        <span class="en">Add New Presentation Slide</span>
        <span class="ar" style="display:none">إضافة شريحة عرض جديدة</span>
      </div>
      <button class="modal-close" onclick="closeAddSlideModal()">✕</button>
    </div>
    <div class="modal-body">
      <label class="modal-label">
        <span class="en">Slide Title (Arabic & English)</span>
        <span class="ar" style="display:none">عنوان الشريحة الجديد</span>
      </label>
      <input type="text" id="newSlideTitleEn" class="modal-input" placeholder="Title in English (e.g. Threat Intelligence Model)"/>
      <input type="text" id="newSlideTitleAr" class="modal-input" style="margin-top:6px" placeholder="العنوان بالعربية (مثلاً: نموذج معلومات التهديدات)"/>

      <label class="modal-label" style="margin-top:14px">
        <span class="en">Choose Slide Layout Template</span>
        <span class="ar" style="display:none">اختر قالب وهيكل الشريحة المتناسق</span>
      </label>
      <div class="tpl-grid">
        <button class="tpl-btn active" id="tplBtnDual" data-tpl="dual" onclick="selectTemplate('dual')">
          <div class="tpl-icon">🗂️</div>
          <div class="tpl-text">
            <div class="tpl-name"><span class="en">Dual Cards</span><span class="ar" style="display:none">بطاقتان تفصيليتان</span></div>
            <div class="tpl-desc"><span class="en">2 side-by-side deep glass cards</span><span class="ar" style="display:none">بطاقتان متجاورتان للمفاهيم والشرح</span></div>
          </div>
        </button>
        <button class="tpl-btn" id="tplBtnTrio" data-tpl="trio" onclick="selectTemplate('trio')">
          <div class="tpl-icon">📊</div>
          <div class="tpl-text">
            <div class="tpl-name"><span class="en">Trio Feature Cards</span><span class="ar" style="display:none">ثلاث بطاقات ميزات</span></div>
            <div class="tpl-desc"><span class="en">3 column architecture pillars</span><span class="ar" style="display:none">3 أعمدة للمكونات والخصائص</span></div>
          </div>
        </button>
        <button class="tpl-btn" id="tplBtnStats" data-tpl="stats" onclick="selectTemplate('stats')">
          <div class="tpl-icon">📈</div>
          <div class="tpl-text">
            <div class="tpl-name"><span class="en">Metrics & Stats</span><span class="ar" style="display:none">إحصائيات وأرقام كبرى</span></div>
            <div class="tpl-desc"><span class="en">Big impact numbers & KPI cards</span><span class="ar" style="display:none">أرقام ومؤشرات إحصائية بارزة</span></div>
          </div>
        </button>
        <button class="tpl-btn" id="tplBtnFlow" data-tpl="flow" onclick="selectTemplate('flow')">
          <div class="tpl-icon">🔄</div>
          <div class="tpl-text">
            <div class="tpl-name"><span class="en">Process Pipeline</span><span class="ar" style="display:none">مخطط تدفق العمليات</span></div>
            <div class="tpl-desc"><span class="en">Sequential steps with arrows</span><span class="ar" style="display:none">مراحل متسلسلة بنبضات تفاعلية</span></div>
          </div>
        </button>
      </div>
    </div>
    <div class="modal-footer">
      <button class="t-btn-act" style="padding:8px 18px" onclick="insertNewSlide()">
        <span class="en">✨ Insert Slide</span><span class="ar" style="display:none">✨ إدراج الشريحة في العرض</span>
      </button>
      <button class="t-btn-act" style="padding:8px 14px;opacity:0.7" onclick="closeAddSlideModal()">
        <span class="en">Cancel</span><span class="ar" style="display:none">إلغاء</span>
      </button>
    </div>
  </div>
</div>

<!-- Control Panel Drawer -->
<div id="cp">
  <div class="cph">
    <div class="cpt">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
      <span class="en">Control Center</span><span class="ar" style="display:none">مركز التحكم الشامل</span>
    </div>
    <button class="cpc" onclick="tC()">✕</button>
  </div>

  <!-- 1. SLIDE STUDIO (FULL LIFECYCLE MANAGEMENT) -->
  <div class="cps">
    <div class="cpst">📑 <span class="en">Slide Studio & Lifecycle Controls</span><span class="ar" style="display:none">استوديو إدارة وتحرير الشرائح</span></div>
    <div class="mode-pills" style="margin-top:6px">
      <button class="mpill" style="background:rgba(16,185,129,0.15);border-color:rgba(16,185,129,0.35);color:#6ee7b7" onclick="openAddSlideModal()">
        <span>➕</span> <span class="en">Add Slide</span><span class="ar" style="display:none">إضافة شريحة</span>
      </button>
      <button class="mpill" onclick="duplicateCurrentSlide()">
        <span>📋</span> <span class="en">Duplicate</span><span class="ar" style="display:none">تكرار الشريحة</span>
      </button>
      <button class="mpill" style="background:rgba(225,29,72,0.15);border-color:rgba(225,29,72,0.35);color:#fda4af" onclick="deleteCurrentSlide()">
        <span>🗑️</span> <span class="en">Delete Slide</span><span class="ar" style="display:none">حذف الشريحة</span>
      </button>
      <button class="mpill" onclick="toggleEditMode()">
        <span>✏️</span> <span class="en">Edit Mode</span><span class="ar" style="display:none">وضع التحرير</span>
      </button>
    </div>
    <div class="mode-pills" style="margin-top:6px">
      <button class="mpill" onclick="moveSlide('up')">
        <span>⬆️</span> <span class="en">Move Earlier</span><span class="ar" style="display:none">تقديم الشريحة</span>
      </button>
      <button class="mpill" onclick="moveSlide('down')">
        <span>⬇️</span> <span class="en">Move Later</span><span class="ar" style="display:none">تأخير الشريحة</span>
      </button>
    </div>
    <div style="display:flex;gap:6px;margin-top:10px">
      <button class="t-btn-act" style="flex:1;padding:8px" onclick="saveEdits()">
        💾 <span class="en">Save All Changes</span><span class="ar" style="display:none">حفظ التعديلات في المتصفح</span>
      </button>
      <button class="t-btn-act" style="padding:8px;opacity:0.8" onclick="restoreOriginalSlides()" title="Restore 25 default slides">
        🔄 <span class="en">Reset</span><span class="ar" style="display:none">استعادة الأصلية</span>
      </button>
    </div>
  </div>

  <!-- 2. 8 SLIDE ANIMATION STYLES -->
  <div class="cps">
    <div class="cpst">🎬 <span class="en">Slide Animation Style (8)</span><span class="ar" style="display:none">أنماط تحريك وانتقال الشرائح (8)</span></div>
    <div class="mode-pills">
      <button class="mpill active" id="btnAnimCascade" onclick="setAnimStyle('cascade')">
        <span>💫</span> <span class="en">Cascade Wave</span><span class="ar" style="display:none">متسلسل سينمائي</span>
      </button>
      <button class="mpill" id="btnAnim3D" onclick="setAnimStyle('3d')">
        <span>🧊</span> <span class="en">3D Flip Cube</span><span class="ar" style="display:none">دوران 3D هادئ</span>
      </button>
      <button class="mpill" id="btnAnimZoom" onclick="setAnimStyle('zoom')">
        <span>⚡</span> <span class="en">Cyber Zoom</span><span class="ar" style="display:none">قفز سيبراني</span>
      </button>
      <button class="mpill" id="btnAnimFade" onclick="setAnimStyle('fade')">
        <span>🌫️</span> <span class="en">Soft Dissolve</span><span class="ar" style="display:none">تلاشٍ هادئ</span>
      </button>
      <button class="mpill" id="btnAnimSlideUp" onclick="setAnimStyle('slide-up')">
        <span>🪜</span> <span class="en">Editorial Lift</span><span class="ar" style="display:none">صعود رأسي ناعم</span>
      </button>
      <button class="mpill" id="btnAnimFlipX" onclick="setAnimStyle('flip-x')">
        <span>🪟</span> <span class="en">Glass Flip X</span><span class="ar" style="display:none">طي أفقي أنيق</span>
      </button>
      <button class="mpill" id="btnAnimSwirl" onclick="setAnimStyle('swirl')">
        <span>🌀</span> <span class="en">Vortex Swirl</span><span class="ar" style="display:none">عمق دوامي بطيء</span>
      </button>
      <button class="mpill" id="btnAnimFocus" onclick="setAnimStyle('focus')">
        <span>🎯</span> <span class="en">Focus Snap</span><span class="ar" style="display:none">تركيز بؤري صافٍ</span>
      </button>
    </div>
  </div>

  <!-- 3. CARD FOCUS & HIGHLIGHT INTERACTION STYLES -->
  <div class="cps">
    <div class="cpst">🎯 <span class="en">Element Focus & Hover Effects</span><span class="ar" style="display:none">تأثيرات التركيز والتحديد على العناصر</span></div>
    <div class="cpl" style="margin-bottom:8px;font-size:0.75rem">
      <span class="en">Choose non-distracting highlight style when hovering/clicking cards:</span>
      <span class="ar" style="display:none">اختر نمط التمييز الهادئ غير المشتت للعين عند الإشارة أو النقر:</span>
    </div>
    <div class="mode-pills">
      <button class="mpill active" id="btnFocusHalo" onclick="setFocusStyle('halo')">
        <span>✨</span> <span class="en">Golden Halo</span><span class="ar" style="display:none">الهالة الذهبية الهادئة</span>
      </button>
      <button class="mpill" id="btnFocusLift" onclick="setFocusStyle('lift')">
        <span>🪞</span> <span class="en">Glass Lift</span><span class="ar" style="display:none">الطفو الزجاجي النقي</span>
      </button>
      <button class="mpill" id="btnFocusSpotlight" onclick="setFocusStyle('spotlight')">
        <span>🔦</span> <span class="en">Spotlight Focus</span><span class="ar" style="display:none">تركيز الكشاف الموجه</span>
      </button>
      <button class="mpill" id="btnFocusBorder" onclick="setFocusStyle('border')">
        <span>📐</span> <span class="en">Precision Line</span><span class="ar" style="display:none">الإطار الهندسي الأنيق</span>
      </button>
    </div>
  </div>

  <!-- 4. SERENE DYNAMIC ANIMATED BACKGROUNDS & SPEED -->
  <div class="cps">
    <div class="cpst">🌌 <span class="en">Dynamic Backgrounds (7 Calm Engines)</span><span class="ar" style="display:none">الخلفيات المتحركة الانسيابية (7 محركات)</span></div>
    <div class="cpr">
      <div class="cpl"><span class="en">Enable Animated Canvas</span><span class="ar" style="display:none">تشغيل / إخفاء الخلفية المتحركة</span></div>
      <button class="csw on" id="swBg" onclick="toggleBg()"></button>
    </div>
    <div class="mode-pills" id="bgPillsGroup" style="margin-top:8px">
      <button class="mpill active" id="btnBgNeural" onclick="setBgMode('neural')">
        <span>🧠</span> <span class="en">Neural AI Mesh</span><span class="ar" style="display:none">شبكة عصبية هادئة</span>
      </button>
      <button class="mpill" id="btnBgWaves" onclick="setBgMode('waves')">
        <span>🌊</span> <span class="en">Quantum Waves</span><span class="ar" style="display:none">أمواج كوانتية بطيئة</span>
      </button>
      <button class="mpill" id="btnBgAurora" onclick="setBgMode('aurora')">
        <span>🌌</span> <span class="en">Auroral Curtains</span><span class="ar" style="display:none">ستائر الشفق الانسيابي</span>
      </button>
      <button class="mpill" id="btnBgStardust" onclick="setBgMode('stardust')">
        <span>✨</span> <span class="en">Cosmic Stardust</span><span class="ar" style="display:none">السديم النجمي المتألق</span>
      </button>
      <button class="mpill" id="btnBgGrid" onclick="setBgMode('grid')">
        <span>🌐</span> <span class="en">Hex Cyber Lattice</span><span class="ar" style="display:none">الشبكة السداسية التشفيرية</span>
      </button>
      <button class="mpill" id="btnBgMatrix" onclick="setBgMode('matrix')">
        <span>💚</span> <span class="en">Cyber Matrix</span><span class="ar" style="display:none">مصفوفة الشيفرات الرزينة</span>
      </button>
      <button class="mpill" id="btnBgWarp" onclick="setBgMode('warp')">
        <span>🚀</span> <span class="en">Space Warp</span><span class="ar" style="display:none">العمق الفضائي الهادئ</span>
      </button>
    </div>

    <!-- Motion Speed Control -->
    <div style="margin-top:14px">
      <div class="cpl" style="margin-bottom:6px;font-size:0.75rem">
        <span class="en">Motion Speed Pace:</span><span class="ar" style="display:none">سرعة حركة الخلفية:</span>
      </div>
      <div class="mode-pills-3">
        <button class="mpill active" id="btnSpdSerene" onclick="setBgSpeed(0.5, 'btnSpdSerene')">
          <span>🍃</span> <span class="en">Serene 0.5x</span><span class="ar" style="display:none">هادئ رزين</span>
        </button>
        <button class="mpill" id="btnSpdBalanced" onclick="setBgSpeed(1.0, 'btnSpdBalanced')">
          <span>⚖️</span> <span class="en">Balanced 1x</span><span class="ar" style="display:none">متزن</span>
        </button>
        <button class="mpill" id="btnSpdUltra" onclick="setBgSpeed(0.25, 'btnSpdUltra')">
          <span>🕊️</span> <span class="en">Ultra Slow</span><span class="ar" style="display:none">بطيء جداً</span>
        </button>
      </div>
    </div>

    <div class="cpr" style="margin-top:12px">
      <div class="cpl"><span class="en">Atmospheric Glowing Orbs</span><span class="ar" style="display:none">الهالات المضيئة الحية</span></div>
      <button class="csw on" id="swo" onclick="tOrbs()"></button>
    </div>
  </div>

  <!-- 5. 5 PRESTIGE GRADIENTS & PALETTES -->
  <div class="cps">
    <div class="cpst">👑 <span class="en">Prestige Color Gradients (5)</span><span class="ar" style="display:none">التدرجات اللونية الفاخرة المعتمدة (5)</span></div>
    <div class="theme-grid">
      <button class="tcard-btn active" data-theme="crimson-plum" onclick="applyTheme('crimson-plum')">
        <div class="t-swatch" style="background:linear-gradient(135deg, #c31432, #240b36)"></div>
        <div class="t-name">
          <span class="en">Crimson & Wine</span><span class="ar" style="display:none">القرمزي والبرغندي المخملي</span>
          <div style="font-size:0.62rem;opacity:0.75;font-family:monospace;letter-spacing:0.5px;margin-top:2px">#c31432 → #240b36</div>
        </div>
      </button>
      <button class="tcard-btn" data-theme="amethyst-emerald" onclick="applyTheme('amethyst-emerald')">
        <div class="t-swatch" style="background:linear-gradient(135deg, #8360c3, #2ebf91)"></div>
        <div class="t-name">
          <span class="en">Amethyst & Jade</span><span class="ar" style="display:none">الجمشت والزمرد اليشمي</span>
          <div style="font-size:0.62rem;opacity:0.75;font-family:monospace;letter-spacing:0.5px;margin-top:2px">#8360c3 → #2ebf91</div>
        </div>
      </button>
      <button class="tcard-btn" data-theme="purple-rose" onclick="applyTheme('purple-rose')">
        <div class="t-swatch" style="background:linear-gradient(135deg, #654ea3, #eaafc8)"></div>
        <div class="t-name">
          <span class="en">Purple & Soft Rose</span><span class="ar" style="display:none">البنفسجي والوردي الأنيق</span>
          <div style="font-size:0.62rem;opacity:0.75;font-family:monospace;letter-spacing:0.5px;margin-top:2px">#654ea3 → #eaafc8</div>
        </div>
      </button>
      <button class="tcard-btn" data-theme="lime-aquamarine" onclick="applyTheme('lime-aquamarine')">
        <div class="t-swatch" style="background:linear-gradient(135deg, #a8ff78, #78ffd6)"></div>
        <div class="t-name">
          <span class="en">Cyber Lime & Aqua</span><span class="ar" style="display:none">الليمي السيبراني والأكوامارين</span>
          <div style="font-size:0.62rem;opacity:0.75;font-family:monospace;letter-spacing:0.5px;margin-top:2px">#a8ff78 → #78ffd6</div>
        </div>
      </button>
      <button class="tcard-btn" data-theme="azure-ocean" onclick="applyTheme('azure-ocean')">
        <div class="t-swatch" style="background:linear-gradient(135deg, #00B4DB, #0083B0)"></div>
        <div class="t-name">
          <span class="en">Electric Azure & Ocean</span><span class="ar" style="display:none">الأزرق السماوي والمحيطي</span>
          <div style="font-size:0.62rem;opacity:0.75;font-family:monospace;letter-spacing:0.5px;margin-top:2px">#00B4DB → #0083B0</div>
        </div>
      </button>
    </div>
  </div>

  <!-- 6. PRESENTATION TIMER -->
  <div class="cps">
    <div class="cpst">⏱️ <span class="en">Presentation Timer (15-20 Min)</span><span class="ar" style="display:none">مؤقت العرض (15-20 دقيقة)</span></div>
    <div class="timer-box">
      <div class="timer-val" id="timerDisplay">20:00</div>
      <div class="timer-btns">
        <button class="t-btn-act" onclick="startTimer()"><span class="en">Start</span><span class="ar" style="display:none">بدء</span></button>
        <button class="t-btn-act" onclick="pauseTimer()"><span class="en">Pause</span><span class="ar" style="display:none">إيقاف</span></button>
        <button class="t-btn-act" onclick="resetTimer()"><span class="en">Reset</span><span class="ar" style="display:none">إعادة</span></button>
      </div>
    </div>
  </div>

  <!-- 7. SLIDE DIRECTORY -->
  <div class="cps">
    <div class="cpst">📑 <span class="en">Slide Directory</span><span class="ar" style="display:none">فهرس الشرائح</span></div>
    <div class="snl" id="snl"></div>
  </div>

  <!-- 8. TYPOGRAPHY SCALE -->
  <div class="cps">
    <div class="cpst">🔠 <span class="en">Font Scale</span><span class="ar" style="display:none">حجم الخط</span></div>
    <div class="cpr"><div class="cpl"><span class="en">Scale</span><span class="ar" style="display:none">الحجم</span></div><input type="range" min="13" max="21" value="16" oninput="document.documentElement.style.fontSize=this.value+'px'" style="width:140px;accent-color:var(--p)"/></div>
  </div>

  <!-- 9. SHORTCUTS -->
  <div class="cps">
    <div class="cpst">⌨️ <span class="en">Hotkeys</span><span class="ar" style="display:none">اختصارات لوحة المفاتيح</span></div>
    <div style="font-size:.76rem;color:var(--t3);line-height:2">
      ← → / Space : Navigate &nbsp;|&nbsp; F : Fullscreen<br>
      L : Language Toggle &nbsp;|&nbsp; C : Control Center<br>
      E : Toggle Edit Mode &nbsp;|&nbsp; Home / End : Start / End
    </div>
  </div>
</div>

<div id="wrap" class="anim-cascade">
''' + slides_content + r'''
</div>

<!-- Bottom Navigation Bar -->
<div id="nav">
  <button class="nb" id="bp" onclick="prev()" title="Previous Slide">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
  </button>
  <div id="sd"></div>
  <span id="sc">1 / 25</span>
  <button class="nb" id="bn" onclick="next()" title="Next Slide">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
  </button>
</div>

<script>
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
</script>
</body>
</html>
'''

if __name__ == '__main__':
    content = generate_html()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    size = os.path.getsize(output_file)
    print(f"SUCCESS: Generated presentation with full slide lifecycle studio and 100% hidden stealth dock! ({size:,} bytes)")
