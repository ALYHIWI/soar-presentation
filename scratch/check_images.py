# -*- coding: utf-8 -*-
"""
Verification and preparation script for SOAR presentation upgrades.
"""
import os

images_dir = 'c:/Users/Mo AL-Yahawy/SOAR/presentation/images'
required_images = [
    'soc_command_center.jpg',
    'alert_fatigue_chaos.jpg',
    'soc_tech_evolution.jpg',
    'blast_radius_hazard.jpg',
    'research_gap_bridge.jpg',
    'system_arch_master.jpg',
    'context_enrichment.jpg',
    'queue_prioritization.jpg',
    'continuous_feedback_loop.jpg',
    'dsr_6phases_methodology.jpg',
    'prior_work_benchmark.jpg',
    'human_ai_teaming.jpg',
    'hero_soar_core.jpg'
]

print("Checking required images in presentation/images:")
all_found = True
for img in required_images:
    p = os.path.join(images_dir, img)
    if os.path.exists(p):
        sz = os.path.getsize(p)
        print(f"  [OK] {img} ({sz} bytes)")
    else:
        print(f"  [MISSING] {img}")
        all_found = False

print(f"\nAll images available: {all_found}")
