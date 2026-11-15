# -*- coding: utf-8 -*-
import json
import os
import base64

base_dir = os.path.dirname(os.path.abspath(__file__))
brain_dir = r"C:\Users\HP\.gemini\antigravity\brain\6a96b10b-5c7c-47d2-9932-1bae9c1a0a9f"

with open(os.path.join(base_dir, "images.json"), "r", encoding="utf-8") as f:
    images = json.load(f)

envelope_b64 = images.get("envelope", "")
seal_b64 = images.get("seal", "")
leaf_glow_b64 = images.get("leaf_glow", "")
butterfly_full_b64 = images.get("butterfly_full", "")
butterfly_wing_left_b64 = images.get("butterfly_wing_left", "")
butterfly_wing_right_b64 = images.get("butterfly_wing_right", "")
butterfly_body_b64 = images.get("butterfly_body", "")

with open(os.path.join(base_dir, "spin_frame_1.jpg"), "rb") as f:
    spin_f1_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
with open(os.path.join(base_dir, "spin_frame_2.jpg"), "rb") as f:
    spin_f2_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
with open(os.path.join(base_dir, "spin_frame_3.jpg"), "rb") as f:
    spin_f3_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
with open(os.path.join(base_dir, "spin_frame_4.jpg"), "rb") as f:
    spin_f4_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
scene3_card_b64 = spin_f1_b64
new_couple_artwork_b64 = spin_f1_b64

with open(os.path.join(base_dir, "bismillah_clean.png"), "rb") as f:
    bismillah_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

with open(os.path.join(base_dir, "olive_tl.png"), "rb") as f:
    olive_tl_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

with open(os.path.join(base_dir, "olive_br.png"), "rb") as f:
    olive_br_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
with open(os.path.join(base_dir, "scene4_full_card.jpg"), "rb") as f:
    scene4_card_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

with open(os.path.join(base_dir, "scene5_floral_bg.jpg"), "rb") as f:
    scene5_bg_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <meta name="theme-color" content="#FAF7F2">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <title>Wedding Invitation — Najila Ashraf & Afsal</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Cinzel:wght@400;600;700;800&family=Cinzel+Decorative:wght@700&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Great+Vibes&family=Montserrat:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">

  <style>
    :root {{
      --theme-dark: #1C231E;
      --theme-olive: #364238;
      --theme-olive-light: #556658;
      --gold-primary: #D4AF37;
      --gold-light: #F4E29F;
      --gold-dark: #9A7720;
      --gold-gradient: linear-gradient(135deg, #FDF0CD 0%, #D4AF37 50%, #9A7720 100%);
      --gold-glow: rgba(212, 175, 55, 0.45);
      --parchment-bg: #FAF7F2;
      --ink-dark: #2A1C1D;
      --ink-muted: #556658;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      width: 100%;
      height: 100%;
      min-height: 100vh;
      min-height: 100dvh;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
      font-family: 'Cormorant Garamond', serif;
      background: #FAF7F2;
      color: var(--ink-dark);
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* Background Particles Canvas */
    #particlesCanvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    /* Discreet Corner Controls (Audio Toggle) with Safe-Area Clearance */
    .corner-controls {{
      position: absolute;
      top: max(10px, env(safe-area-inset-top, 10px));
      right: max(12px, env(safe-area-inset-right, 12px));
      z-index: 60;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .icon-btn {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(36, 46, 38, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(212, 175, 55, 0.5);
      color: var(--gold-light);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 13px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.3);
      transition: all 0.3s ease;
    }}

    .icon-btn:hover {{
      background: rgba(212, 175, 55, 0.3);
      transform: scale(1.08);
      color: #fff;
    }}

    .icon-btn.music-active {{
      background: rgba(46, 58, 48, 0.9);
      border-color: #D4AF37;
      box-shadow: 0 0 16px rgba(212, 175, 55, 0.7);
      animation: pulseMusic 2.4s ease-in-out infinite;
    }}
    @keyframes pulseMusic {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.08); }}
    }}

    /* Main Stage Container (Full-Page Edge-to-Edge for Mobile) */
    .stage-wrapper {{
      position: relative;
      z-index: 10;
      width: 100vw;
      max-width: 100%;
      height: 100vh;
      height: 100dvh;
      max-height: 100dvh;
      perspective: 1800px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #FAF7F2;
    }}

    /* Card Base Styling (Full Page View, Zero Letterboxing) */
    .invitation-card {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      height: 100dvh;
      background: var(--parchment-bg);
      background-image: 
        radial-gradient(ellipse at center, #FFFFFF 0%, #FAF7F2 100%);
      border: none !important;
      outline: none !important;
      border-radius: 0 !important;
      box-shadow: none !important;
      overflow-y: auto;
      overflow-x: hidden;
      -webkit-overflow-scrolling: touch;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: max(32px, calc(env(safe-area-inset-top, 0px) + 24px));
      padding-bottom: max(20px, calc(env(safe-area-inset-bottom, 0px) + 14px));
      padding-left: max(16px, env(safe-area-inset-left, 0px));
      padding-right: max(16px, env(safe-area-inset-right, 0px));
      opacity: 0;
      pointer-events: none;
      transform: translateY(10px) scale(0.99);
      transition: opacity 1.2s cubic-bezier(0.25, 1, 0.5, 1), transform 1.2s cubic-bezier(0.25, 1, 0.5, 1);
    }}

    .invitation-card.active {{
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0) scale(1);
    }}

    .invitation-card::-webkit-scrollbar {{
      width: 3px;
    }}
    .invitation-card::-webkit-scrollbar-track {{
      background: transparent;
    }}
    .invitation-card::-webkit-scrollbar-thumb {{
      background: rgba(212, 175, 55, 0.4);
      border-radius: 3px;
    }}

    /* Royal Corner Ornaments removed */
    .royal-corner-decor {{ display: none !important; }}

    /* Story Segmented Header Bar with Safe-Area Offset */
    .story-header-bar {{
      position: absolute;
      top: max(10px, env(safe-area-inset-top, 10px));
      left: 0;
      width: 100%;
      padding-left: max(16px, env(safe-area-inset-left, 16px));
      padding-right: max(60px, calc(env(safe-area-inset-right, 16px) + 44px));
      display: flex;
      gap: 5px;
      z-index: 50;
      box-sizing: border-box;
    }}
    .story-dash {{
      flex: 1;
      height: 3.5px;
      background: rgba(212, 175, 55, 0.25);
      border-radius: 2px;
      overflow: hidden;
      cursor: pointer;
      position: relative;
    }}
    .story-dash-fill {{
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      width: 0%;
      background: var(--gold-gradient);
      box-shadow: 0 0 6px rgba(212, 175, 55, 0.8);
      border-radius: 2px;
    }}

    /* Desktop View (Centered Elegant Presentation Frame) */
    @media (min-width: 769px) {{
      body {{
        display: flex;
        align-items: center;
        justify-content: center;
        background: #18201A;
        background-image: 
          radial-gradient(circle at 50% 25%, #2B372E 0%, #121814 100%);
      }}

      .stage-wrapper {{
        width: 440px;
        height: min(94vh, 900px);
        border-radius: 20px;
        box-shadow: 
          0 25px 65px rgba(0, 0, 0, 0.55),
          0 0 0 1px rgba(212, 175, 55, 0.4);
        margin: auto;
      }}

      .invitation-card {{
        border-radius: 20px !important;
        border: 2px solid rgba(212, 175, 55, 0.35) !important;
        box-shadow: none !important;
      }}
    }}

    /* =========================================================
       3D REALISTIC BUTTERFLY (SCENE 1 & SCENE 2)
       ========================================================= */
    .flying-butterfly-container {{
      position: absolute;
      top: 46.7%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.8);
      width: 110px;
      height: 98px;
      pointer-events: none;
      z-index: 48;
      perspective: 900px;
      opacity: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .envelope-flaps-overlay.opened ~ .flying-butterfly-container,
    .active .flying-butterfly-container.fly-active {{
      opacity: 1;
      animation: butterflyFlyUp 5.6s cubic-bezier(0.25, 1, 0.35, 1) forwards;
    }}

    .flying-butterfly-container.landed {{
      animation: none !important;
      top: 112px !important;
      left: 50% !important;
      transform: translate(-50%, -50%) scale(1.05) !important;
      opacity: 1 !important;
    }}

    .butterfly-3d {{
      position: relative;
      width: 100%;
      height: 100%;
      transform-style: preserve-3d;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .wing {{
      position: absolute;
      top: 0;
      width: 48%;
      height: 100%;
      background-size: 100% 100%;
      background-repeat: no-repeat;
      will-change: transform;
    }}

    .wing-left {{
      right: 50%;
      background-image: url("{butterfly_wing_left_b64}");
      background-position: right center;
      transform-origin: right center;
      animation: flapLeftWing 0.26s ease-in-out infinite alternate;
    }}

    .wing-right {{
      left: 50%;
      background-image: url("{butterfly_wing_right_b64}");
      background-position: left center;
      transform-origin: left center;
      animation: flapRightWing 0.26s ease-in-out infinite alternate;
    }}

    .butterfly-body {{
      position: absolute;
      left: 50%;
      top: 0;
      transform: translateX(-50%);
      width: 11%;
      height: 100%;
      background-image: url("{butterfly_body_b64}");
      background-size: contain;
      background-position: center top;
      background-repeat: no-repeat;
      z-index: 5;
    }}

    .butterfly-shadow {{
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, 34px) scale(0.85, 0.35);
      width: 90px;
      height: 44px;
      background: rgba(40, 20, 10, 0.28);
      filter: blur(8px);
      border-radius: 50%;
      pointer-events: none;
      animation: shadowPulse 0.26s ease-in-out infinite alternate;
    }}

    @keyframes flapLeftWing {{
      0% {{ transform: rotateY(12deg); }}
      100% {{ transform: rotateY(78deg); }}
    }}

    @keyframes flapRightWing {{
      0% {{ transform: rotateY(-12deg); }}
      100% {{ transform: rotateY(-78deg); }}
    }}

    @keyframes shadowPulse {{
      0% {{ transform: translate(-50%, 32px) scale(0.9, 0.36); opacity: 0.32; }}
      100% {{ transform: translate(-50%, 38px) scale(0.72, 0.28); opacity: 0.16; }}
    }}

    @keyframes butterflyFlyUp {{
      0% {{
        top: 46.7%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0.7) rotate(0deg);
        opacity: 0;
      }}
      6% {{
        top: 46.7%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0.95) rotate(4deg);
        opacity: 1;
      }}
      28% {{
        top: 38%;
        left: 44%;
        transform: translate(-50%, -50%) scale(1.15) rotate(-14deg);
        opacity: 1;
      }}
      58% {{
        top: 24%;
        left: 55%;
        transform: translate(-50%, -50%) scale(1.18) rotate(11deg);
        opacity: 1;
      }}
      84% {{
        top: 14%;
        left: 48%;
        transform: translate(-50%, -50%) scale(1.10) rotate(-4deg);
        opacity: 1;
      }}
      100% {{
        top: 112px;
        left: 50%;
        transform: translate(-50%, -50%) scale(1.05) rotate(0deg);
        opacity: 1;
      }}
    }}

    /* Scene 2 Perched Butterfly */
    .perched-butterfly-couples {{
      position: absolute;
      top: 112px !important;
      left: 50%;
      transform: translate(-50%, -50%) scale(1.05);
      width: 110px;
      height: 98px;
      z-index: 10;
      pointer-events: none;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .perched-butterfly-couples .perched-butterfly-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 12px 18px rgba(40, 20, 10, 0.28));
    }}

    /* =========================================================
       3D REALISTIC OLIVE ENVELOPE (MATCHING REFERENCE IMAGES)
       ========================================================= */
    .envelope-flaps-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 40;
      pointer-events: auto;
      cursor: pointer;
      perspective: 1400px;
      transition: opacity 1.4s ease 4.2s, visibility 1.4s ease 4.2s;
    }}
    .envelope-flaps-overlay.opened {{
      pointer-events: none;
      visibility: hidden;
      opacity: 0;
    }}

    .flap {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: url("{envelope_b64}");
      background-size: 100% 100%;
      background-position: center;
      background-repeat: no-repeat;
      transform-style: preserve-3d;
      transition: transform 3.8s cubic-bezier(0.25, 1, 0.35, 1), opacity 1.4s ease 2.6s;
      backface-visibility: hidden;
      will-change: transform;
      z-index: 10;
    }}

    .flap-top {{
      clip-path: polygon(11.9% 0, 88.9% 0, 50% 46.7%);
      transform-origin: top center;
      z-index: 12;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
    }}

    .flap-bottom {{
      clip-path: polygon(0 100%, 100% 100%, 50% 46.7%);
      transform-origin: bottom center;
      z-index: 11;
      filter: drop-shadow(0 -2px 4px rgba(0,0,0,0.3));
    }}

    .flap-left {{
      clip-path: polygon(0 0, 11.9% 0, 50% 46.7%, 0 100%);
      transform-origin: left center;
      z-index: 10;
      filter: drop-shadow(2px 0 4px rgba(0,0,0,0.3));
    }}

    .flap-right {{
      clip-path: polygon(88.9% 0, 100% 0, 100% 100%, 50% 46.7%);
      transform-origin: right center;
      z-index: 10;
      filter: drop-shadow(-2px 0 4px rgba(0,0,0,0.3));
    }}

    .envelope-flaps-overlay.opened .flap-top {{
      transform: rotateX(175deg);
    }}
    .envelope-flaps-overlay.opened .flap-bottom {{
      transform: rotateX(-175deg);
    }}
    .envelope-flaps-overlay.opened .flap-left {{
      transform: rotateY(-175deg);
    }}
    .envelope-flaps-overlay.opened .flap-right {{
      transform: rotateY(175deg);
    }}

    /* Subtle Golden Leaf Lighting on Touch/Hover */
    .leaf-glow-layer {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-image: url("{leaf_glow_b64}");
      background-size: 100% 100%;
      background-position: center;
      background-repeat: no-repeat;
      pointer-events: none;
      z-index: 18;
      opacity: 0;
      mix-blend-mode: screen;
      filter: drop-shadow(0 0 3px rgba(255, 230, 130, 0.75)) drop-shadow(0 0 8px rgba(212, 175, 55, 0.5));
      transition: opacity 1.0s cubic-bezier(0.25, 1, 0.35, 1);
    }}
    .envelope-flaps-overlay:hover .leaf-glow-layer,
    .envelope-flaps-overlay:active .leaf-glow-layer,
    .envelope-flaps-overlay.lighting-active .leaf-glow-layer {{
      opacity: 0.88;
    }}
    .envelope-flaps-overlay.opened .leaf-glow-layer {{
      opacity: 0;
      transition: opacity 2.2s ease 1.8s;
    }}

    /* 3D Gold Butterfly Wax Seal */
    .wax-seal {{
      position: absolute;
      top: 46.7%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 102px;
      height: 102px;
      background-image: url("{seal_b64}");
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      z-index: 25;
      filter: drop-shadow(0 8px 18px rgba(0,0,0,0.5));
      transition: transform 0.4s ease, filter 0.4s ease, opacity 0.6s ease;
      cursor: pointer;
    }}
    .wax-seal:hover {{
      transform: translate(-50%, -50%) scale(1.03);
      filter: drop-shadow(0 10px 22px rgba(0,0,0,0.6));
    }}
    .envelope-flaps-overlay.lighting-active .wax-seal {{
      transform: translate(-50%, -50%) scale(1.08);
      filter: drop-shadow(0 0 16px rgba(255, 230, 130, 0.85)) drop-shadow(0 10px 24px rgba(0,0,0,0.6));
    }}
    .envelope-flaps-overlay.opened .wax-seal {{
      transform: translate(-50%, -50%) scale(1.25) !important;
      opacity: 0 !important;
      visibility: hidden !important;
      pointer-events: none !important;
      transition: transform 0.9s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease, visibility 0.6s ease !important;
    }}

    /* =========================================================
       SCENE 1: YOU'RE CORDIALLY INVITED STYLING (IMAGE 3 & 4 MODEL)
       ========================================================= */
    .reveal-container {{
      text-align: center;
      margin-top: 225px !important;
      z-index: 10;
      width: 100%;
      max-width: 340px;
    }}

    .fade-youre {{
      font-family: 'Cinzel', serif;
      font-size: 16px;
      font-weight: 600;
      letter-spacing: 7px;
      color: #8C7873;
      text-transform: uppercase;
      margin-bottom: 6px;
      opacity: 0;
      filter: blur(6px);
      transform: translateY(10px);
      transition: all 1.8s cubic-bezier(0.2, 0.8, 0.2, 1) 3.6s;
    }}

    .fade-cordially {{
      font-family: 'Cinzel Decorative', 'Cinzel', serif;
      font-size: 28px;
      font-weight: 700;
      letter-spacing: 8px;
      color: #384239;
      text-transform: uppercase;
      margin-bottom: 4px;
      opacity: 0;
      filter: blur(8px);
      transform: scale(0.95) translateY(12px);
      transition: all 2.0s cubic-bezier(0.2, 0.8, 0.2, 1) 4.6s;
    }}

    .fade-invited {{
      font-family: 'Cinzel', serif;
      font-size: 20px;
      font-weight: 600;
      letter-spacing: 7px;
      color: #8C7873;
      text-transform: uppercase;
      margin-bottom: 12px;
      opacity: 0;
      filter: blur(6px);
      transform: translateY(10px);
      transition: all 1.8s cubic-bezier(0.2, 0.8, 0.2, 1) 5.6s;
    }}

    .gold-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      margin: 10px 0;
      opacity: 0;
      transition: opacity 1.5s ease 6.4s;
    }}
    .gold-divider svg {{
      width: 18px;
      height: 18px;
      fill: var(--gold-primary);
    }}

    .fade-subtext {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 15px;
      font-style: italic;
      color: #554446;
      line-height: 1.5;
      max-width: 290px;
      margin: 0 auto;
      opacity: 0;
      transform: translateY(8px);
      transition: all 1.8s ease 7.0s;
    }}

    /* Settled or Opened Card Reveal */
    .envelope-flaps-overlay.opened ~ .reveal-container .fade-youre,
    .flying-butterfly-container.landed ~ .reveal-container .fade-youre {{
      opacity: 1 !important;
      filter: blur(0) !important;
      transform: translateY(0) !important;
      transition: opacity 0.8s ease, filter 0.8s ease, transform 0.8s ease !important;
    }}
    .active .flying-butterfly-container.fly-active ~ .reveal-container .fade-youre {{
      opacity: 1;
      filter: blur(0);
      transform: translateY(0);
    }}

    .envelope-flaps-overlay.opened ~ .reveal-container .fade-cordially,
    .flying-butterfly-container.landed ~ .reveal-container .fade-cordially {{
      opacity: 1 !important;
      filter: blur(0) !important;
      transform: scale(1) translateY(0) !important;
      transition: opacity 0.8s ease, filter 0.8s ease, transform 0.8s ease !important;
    }}
    .active .flying-butterfly-container.fly-active ~ .reveal-container .fade-cordially {{
      opacity: 1;
      filter: blur(0);
      transform: scale(1) translateY(0);
    }}

    .envelope-flaps-overlay.opened ~ .reveal-container .fade-invited,
    .flying-butterfly-container.landed ~ .reveal-container .fade-invited {{
      opacity: 1 !important;
      filter: blur(0) !important;
      transform: translateY(0) !important;
      transition: opacity 0.8s ease, filter 0.8s ease, transform 0.8s ease !important;
    }}
    .active .flying-butterfly-container.fly-active ~ .reveal-container .fade-invited {{
      opacity: 1;
      filter: blur(0);
      transform: translateY(0);
    }}

    .envelope-flaps-overlay.opened ~ .reveal-container .gold-divider,
    .flying-butterfly-container.landed ~ .reveal-container .gold-divider {{
      opacity: 1 !important;
      transition: opacity 0.8s ease !important;
    }}
    .active .flying-butterfly-container.fly-active ~ .reveal-container .gold-divider {{
      opacity: 1;
    }}

    .envelope-flaps-overlay.opened ~ .reveal-container .fade-subtext,
    .flying-butterfly-container.landed ~ .reveal-container .fade-subtext {{
      opacity: 1 !important;
      transform: translateY(0) !important;
      transition: opacity 0.8s ease, transform 0.8s ease !important;
    }}
    .active .flying-butterfly-container.fly-active ~ .reveal-container .fade-subtext {{
      opacity: 1;
      transform: translateY(0);
    }}

    /* =========================================================
       SCENE 2: WE'RE GETTING MARRIED & CALLIGRAPHY INK REVEAL
       ========================================================= */
    .married-model-container {{
      text-align: center;
      margin-top: 225px !important;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 10;
    }}

    .married-banner-title {{
      font-family: 'Cinzel', serif;
      font-size: 14px;
      font-weight: 600;
      letter-spacing: 5px;
      color: #7D6B68;
      text-transform: uppercase;
      margin-bottom: 14px;
      text-align: center;
    }}

    .couple-calligraphy-wrap {{
      position: relative;
      width: 100%;
      max-width: 360px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 10px 0;
      text-align: center;
    }}

    .groom-calligraphy {{
      font-family: 'Alex Brush', 'Great Vibes', cursive;
      font-size: 62px;
      color: #4A584C;
      line-height: 1.15;
      letter-spacing: 2px;
      position: relative;
      z-index: 3;
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      text-align: center;
      margin-bottom: 2px;
    }}

    .calligraphy-ampersand {{
      position: absolute;
      top: 50%;
      left: 64%;
      transform: translate(-50%, -50%) scale(0.8);
      font-family: 'Cormorant Garamond', 'Playfair Display', serif;
      font-size: 96px;
      font-weight: 300;
      font-style: italic;
      color: rgba(212, 165, 154, 0.58);
      z-index: 1;
      pointer-events: none;
      line-height: 1;
      user-select: none;
      opacity: 0;
      filter: blur(6px);
      transition: opacity 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) 1.45s, transform 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) 1.45s, filter 0.8s ease 1.45s;
    }}

    .active .calligraphy-ampersand {{
      opacity: 1;
      filter: blur(0);
      transform: translate(-50%, -50%) scale(1);
    }}

    .bride-calligraphy {{
      font-family: 'Alex Brush', 'Great Vibes', cursive;
      font-size: 52px;
      color: #4A584C;
      line-height: 1.15;
      letter-spacing: 1.5px;
      position: relative;
      z-index: 3;
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
      text-align: center;
      margin-top: 2px;
    }}

    /* Letter-by-Letter Flowing Ink Reveal Effect */
    .char-span {{
      display: inline-block;
      opacity: 0;
      transform: translateY(10px) scale(0.9);
      filter: blur(4px);
      transition: opacity 0.45s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.45s ease;
      will-change: opacity, transform, filter;
    }}
    .char-space {{
      display: inline-block;
      width: 10px;
    }}

    /* Afsal letter-by-letter reveal (first) */
    .active .groom-calligraphy .char-span:nth-child(1) {{ transition-delay: 0.50s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .groom-calligraphy .char-span:nth-child(2) {{ transition-delay: 0.68s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .groom-calligraphy .char-span:nth-child(3) {{ transition-delay: 0.86s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .groom-calligraphy .char-span:nth-child(4) {{ transition-delay: 1.04s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .groom-calligraphy .char-span:nth-child(5) {{ transition-delay: 1.22s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}

    /* Najila Ashraf letter-by-letter reveal (after ampersand) */
    .active .bride-calligraphy .char-span:nth-of-type(1)  {{ transition-delay: 1.80s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(2)  {{ transition-delay: 1.95s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(3)  {{ transition-delay: 2.10s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(4)  {{ transition-delay: 2.25s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(5)  {{ transition-delay: 2.40s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(6)  {{ transition-delay: 2.55s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(7)  {{ transition-delay: 2.75s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(8)  {{ transition-delay: 2.90s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(9)  {{ transition-delay: 3.05s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(10) {{ transition-delay: 3.20s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(11) {{ transition-delay: 3.35s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}
    .active .bride-calligraphy .char-span:nth-of-type(12) {{ transition-delay: 3.50s; opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }}

    /* =========================================================
       SCENE 3: WEDDING CELEBRATION PORTRAIT & GRACEFUL CIRCLE SPIN
       ========================================================= */
    #scene-portrait {{
      padding: 0 !important;
      overflow: hidden;
      background: #FAF7F2;
      border: 3px solid #364238;
      outline: 2px solid rgba(212, 175, 55, 0.5);
      outline-offset: -3px;
    }}

    .scene3-artwork-container {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      cursor: pointer;
    }}

    /* 4-Frame Cross-Dissolve Spin Animation */
    .spin-frame {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: calc(100% - 64px);
      object-fit: contain !important;
      object-position: center center;
      background: #FAF7F2;
      display: block;
      opacity: 0;
      transition: opacity 0.18s ease-in-out;
      pointer-events: none;
    }}

    .spin-frame.active-frame {{
      opacity: 1 !important;
    }}

    /* Luxury Slow Reveal of Bride & Groom Artwork */
    #scene-portrait.active .scene3-artwork-container {{
      animation: brideGroomSlowReveal 3.2s cubic-bezier(0.2, 0.8, 0.25, 1) forwards;
    }}

    @keyframes brideGroomSlowReveal {{
      0% {{
        opacity: 0;
        filter: blur(14px);
        transform: scale(0.95);
      }}
      30% {{
        opacity: 0.28;
        filter: blur(8px);
      }}
      65% {{
        opacity: 0.76;
        filter: blur(2.5px);
        transform: scale(0.99);
      }}
      100% {{
        opacity: 1;
        filter: blur(0);
        transform: scale(1);
      }}
    }}

    #scene-portrait.active .spin-action-pill {{
      animation: pillEntrance 1.4s ease 1.2s both;
    }}

    #scene-portrait.active .scene3-nav-overlay {{
      animation: navEntrance 1.4s ease 1.4s both;
    }}

    @keyframes pillEntrance {{
      0% {{ opacity: 0; transform: translateY(-8px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes navEntrance {{
      0% {{ opacity: 0; transform: translateY(8px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Interactive Spin Option Pill */
    .spin-action-pill {{
      position: absolute;
      top: 16px;
      left: 16px;
      z-index: 25;
      background: rgba(255, 255, 255, 0.90);
      border: 1px solid rgba(190, 165, 115, 0.5);
      border-radius: 20px;
      padding: 6px 14px;
      font-family: 'Cinzel', serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 1.2px;
      color: #38453A;
      box-shadow: 0 2px 10px rgba(56, 69, 58, 0.10);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.25s ease;
      backdrop-filter: blur(4px);
    }}

    .spin-action-pill:hover {{
      background: #FFFFFF;
      transform: translateY(-1px);
      box-shadow: 0 4px 14px rgba(56, 69, 58, 0.18);
      border-color: rgba(190, 165, 115, 0.8);
    }}

    .spin-action-pill.spinning {{
      border-color: #38453A;
      background: #FAF7F2;
      box-shadow: 0 0 12px rgba(190, 165, 115, 0.4);
    }}

    .scene3-nav-overlay {{
      position: absolute;
      bottom: max(16px, calc(env(safe-area-inset-bottom, 0px) + 12px));
      left: 0;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 max(16px, env(safe-area-inset-left, 16px));
      box-sizing: border-box;
      z-index: 20;
    }}

    /* =========================================================
       SCENE 4: CEREMONY RECEPTION (EDGE-TO-EDGE FULL PAGE ARTWORK)
       ========================================================= */
    #scene-details {{
      padding: 0 !important;
      overflow: hidden;
      border: 3px solid #364238;
      outline: 2px solid rgba(212, 175, 55, 0.5);
      outline-offset: -3px;
      background: #F5F6F0;
    }}

    .scene4-artwork-container {{
      position: relative;
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      background: #F5F6F0;
    }}

    .scene4-card-img {{
      width: 100%;
      height: 100%;
      object-fit: contain !important;
      object-position: center 40%;
      background: #F5F6F0;
      display: block;
    }}

    .scene4-nav-overlay {{
      position: absolute;
      bottom: max(16px, calc(env(safe-area-inset-bottom, 0px) + 12px));
      left: 0;
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 max(16px, env(safe-area-inset-left, 16px));
      box-sizing: border-box;
      z-index: 20;
    }}

    /* =========================================================
       SCENE 5: CEREMONY SCHEDULE & AUSPICIOUS DAY (AUTHENTIC IMAGE 2 DATA)
       ========================================================= */
    #scene-schedule {{
      background-image: url("{scene5_bg_b64}");
      background-size: 100% 100%;
      background-position: center;
      background-repeat: no-repeat;
    }}

    .scene5-body-content {{
      width: 100%;
      padding-top: 105px;
      display: flex;
      flex-direction: column;
      align-items: center;
      z-index: 10;
    }}

    .insha-allah-header {{
      font-family: 'Amiri', 'Cinzel', serif;
      font-size: 16px;
      color: #38453A;
      letter-spacing: 1px;
      margin-bottom: 2px;
      text-align: center;
    }}

    .insha-allah-sub {{
      font-family: 'Cinzel', serif;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 4px;
      color: #7D6B68;
      text-transform: uppercase;
      margin-bottom: 8px;
      text-align: center;
    }}

    /* Main Wedding Reception Card (Image 2 Model) */
    .schedule-main-card {{
      width: 100%;
      background: rgba(255, 255, 255, 0.90);
      border: 1.5px solid rgba(190, 165, 115, 0.5);
      border-radius: 12px;
      padding: 11px 14px;
      text-align: center;
      box-shadow: 0 4px 14px rgba(56, 66, 57, 0.06);
      margin-bottom: 8px;
    }}

    .schedule-event-badge {{
      font-family: 'Cinzel', serif;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 2px;
      color: #8C7873;
      text-transform: uppercase;
      margin-bottom: 3px;
    }}

    .schedule-date-title {{
      font-family: 'Playfair Display', serif;
      font-size: 17px;
      font-weight: 700;
      color: #38453A;
      line-height: 1.2;
    }}

    .schedule-time-title {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 15px;
      font-style: italic;
      font-weight: 600;
      color: #4A584C;
      margin-top: 2px;
      margin-bottom: 4px;
    }}

    .schedule-gold-rule {{
      width: 45px;
      height: 1px;
      background: rgba(190, 165, 115, 0.5);
      margin: 5px auto;
    }}

    .schedule-venue-name {{
      font-family: 'Cinzel', serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.8px;
      color: #2E3830;
      margin-top: 3px;
    }}

    .venue-sub-tag {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13px;
      font-style: italic;
      font-weight: 500;
      color: #6C5B5D;
    }}

    .schedule-venue-city {{
      font-family: 'Montserrat', sans-serif;
      font-size: 9.5px;
      font-weight: 500;
      letter-spacing: 1px;
      color: #556658;
      text-transform: uppercase;
      margin-top: 2px;
    }}

    /* Nikah Ceremony Box (Image 2 Model) */
    .schedule-nikah-card {{
      width: 100%;
      background: rgba(255, 255, 255, 0.86);
      border: 1px solid rgba(190, 165, 115, 0.45);
      border-radius: 10px;
      padding: 9px 12px;
      text-align: center;
      box-shadow: 0 3px 12px rgba(56, 66, 57, 0.05);
      margin-bottom: 8px;
    }}

    .nikah-tag {{
      font-family: 'Cinzel', serif;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #8C7873;
      text-transform: uppercase;
      margin-bottom: 3px;
    }}

    .nikah-text {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13.5px;
      color: #38453A;
      line-height: 1.35;
      margin: 0;
    }}

    .nikah-text strong {{
      font-family: 'Montserrat', sans-serif;
      font-size: 10.5px;
      font-weight: 600;
      color: #2E3830;
    }}

    .nikah-datetime {{
      display: inline-block;
      margin-top: 2px;
      color: #4A584C;
    }}

    /* Live Countdown Box (Highlighted Royal Card) */
    .countdown-wrap {{
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 251, 242, 0.96) 50%, rgba(250, 244, 230, 0.94) 100%);
      border: 1.5px solid rgba(212, 175, 55, 0.75);
      outline: 2px solid rgba(212, 175, 55, 0.28);
      outline-offset: -4px;
      border-radius: 14px;
      padding: 10px 12px 10px 12px;
      width: 100%;
      text-align: center;
      box-shadow: 0 6px 20px rgba(212, 175, 55, 0.22), 0 2px 8px rgba(56, 66, 57, 0.08);
      margin-bottom: 8px;
      position: relative;
      animation: auspiciousGlow 3.5s ease-in-out infinite;
    }}

    @keyframes auspiciousGlow {{
      0%, 100% {{
        box-shadow: 0 4px 18px rgba(212, 175, 55, 0.20), 0 0 0 1px rgba(212, 175, 55, 0.45);
      }}
      50% {{
        box-shadow: 0 6px 24px rgba(212, 175, 55, 0.35), 0 0 0 1.5px rgba(212, 175, 55, 0.85);
      }}
    }}

    .countdown-label {{
      font-family: 'Cinzel', serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 2.2px;
      color: #8C6D23;
      text-transform: uppercase;
      margin-bottom: 7px;
      text-shadow: 0 1px 2px rgba(212, 175, 55, 0.25);
    }}

    .timer-units {{
      display: flex;
      justify-content: space-around;
      align-items: center;
      gap: 6px;
    }}

    .timer-unit {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.90);
      border: 1px solid rgba(212, 175, 55, 0.40);
      border-radius: 8px;
      padding: 5px 6px 4px 6px;
      box-shadow: 0 2px 6px rgba(180, 150, 100, 0.10);
    }}

    .timer-unit .num {{
      font-family: 'Playfair Display', serif;
      font-size: 22px;
      font-weight: 700;
      color: #2E3830;
      line-height: 1.1;
      text-shadow: 0 1px 2px rgba(212, 175, 55, 0.25);
    }}

    .timer-unit .unit {{
      font-family: 'Montserrat', sans-serif;
      font-size: 8px;
      font-weight: 600;
      letter-spacing: 1.2px;
      color: #7D6B48;
      text-transform: uppercase;
      margin-top: 2px;
    }}

    .compliments-note {{
      font-family: 'Cormorant Garamond', serif;
      font-style: italic;
      font-size: 13px;
      color: #556658;
      line-height: 1.35;
      text-align: center;
      margin-top: 2px;
    }}

    .compliments-note strong {{
      font-family: 'Cinzel', serif;
      font-style: normal;
      font-size: 10.5px;
      letter-spacing: 0.8px;
      color: #38453A;
      display: block;
      margin-top: 2px;
    }}

    /* =========================================================
       SCENE 6: VENUE & ROUTE MAP (DUAL VENUE: WEDDING & NIKAH)
       ========================================================= */
    #scene-map {{
      padding: max(38px, calc(env(safe-area-inset-top, 0px) + 26px)) 16px max(16px, calc(env(safe-area-inset-bottom, 0px) + 12px)) 16px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      align-items: center;
      box-sizing: border-box;
      background: #FAF7F2;
      background-image: radial-gradient(ellipse at 50% 35%, #FFFFFF 0%, #FAF7F2 70%, #F5EFE6 100%);
      border: 3px solid #364238;
      outline: 2px solid rgba(212, 175, 55, 0.5);
      outline-offset: -3px;
      overflow: hidden;
    }}

    .scene6-body-content {{
      width: 100%;
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      text-align: center;
      min-height: 0;
    }}

    .venue-title {{
      font-family: 'Cinzel', serif;
      font-size: 15px;
      letter-spacing: 2.5px;
      color: #2E3830;
      font-weight: 700;
      text-align: center;
      text-transform: uppercase;
      margin-top: 2px;
      margin-bottom: 2px;
    }}

    .venue-sub {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 12px;
      font-style: italic;
      color: #556658;
      text-align: center;
      margin-bottom: 8px;
    }}

    /* Dual Venue Tab Switcher */
    .venue-tab-switcher {{
      display: flex;
      gap: 8px;
      width: 100%;
      margin-bottom: 8px;
      justify-content: center;
    }}

    .venue-tab-btn {{
      flex: 1;
      padding: 7px 6px;
      border-radius: 20px;
      font-family: 'Cinzel', serif;
      font-size: 9.5px;
      font-weight: 600;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      border: 1px solid rgba(190, 165, 115, 0.45);
      background: rgba(255, 255, 255, 0.85);
      color: #4A584C;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      box-shadow: 0 2px 6px rgba(56, 66, 57, 0.04);
    }}

    .venue-tab-btn.active {{
      background: #38453A;
      color: #FAF7F2;
      border-color: rgba(190, 165, 115, 0.6);
      box-shadow: 0 3px 10px rgba(45, 55, 47, 0.20);
    }}

    .address-card {{
      background: rgba(255, 255, 255, 0.90);
      border: 1.5px solid rgba(190, 165, 115, 0.5);
      border-radius: 12px;
      padding: 8px 14px;
      width: 100%;
      box-sizing: border-box;
      text-align: center;
      margin-bottom: 8px;
      box-shadow: 0 4px 14px rgba(56, 66, 57, 0.05);
    }}

    .venue-event-badge {{
      font-family: 'Cinzel', serif;
      font-size: 8.5px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #8C7873;
      text-transform: uppercase;
      margin-bottom: 2px;
    }}

    .residence-name {{
      font-family: 'Cinzel', serif;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.8px;
      color: #2E3830;
      margin-bottom: 2px;
    }}

    .full-address {{
      font-family: 'Cormorant Garamond', serif;
      font-size: 13px;
      color: #4A584C;
      line-height: 1.3;
    }}

    /* Responsive map frame */
    .gmap-frame-box {{
      width: 100%;
      flex: 1;
      min-height: 200px;
      max-height: 380px;
      border-radius: 12px;
      overflow: hidden;
      border: 1.5px solid rgba(190, 165, 115, 0.5);
      margin-bottom: 12px;
      box-shadow: 0 4px 14px rgba(56, 66, 57, 0.08);
      box-sizing: border-box;
      background: #ECE7DE;
    }}

    .gmap-frame-box iframe {{
      width: 100%;
      height: 100%;
      border: none;
      display: block;
    }}

    .directions-btn-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      width: 100%;
      margin-bottom: 8px;
      box-sizing: border-box;
    }}

    .dir-action-btn {{
      padding: 8px 10px;
      border-radius: 20px;
      font-family: 'Cinzel', serif;
      font-size: 9.5px;
      font-weight: 600;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      cursor: pointer;
      border: 1px solid rgba(190, 165, 115, 0.5);
      background: rgba(255, 255, 255, 0.90);
      color: #38453A;
      box-shadow: 0 2px 8px rgba(56, 66, 57, 0.05);
      transition: all 0.25s ease;
    }}

    .dir-action-btn:hover {{
      background: #FFFFFF;
      border-color: rgba(190, 165, 115, 0.8);
      transform: translateY(-1px);
    }}

    .dir-action-btn.primary-directions {{
      background: #38453A;
      color: #FAF7F2;
      border: 1px solid rgba(190, 165, 115, 0.5);
      box-shadow: 0 4px 12px rgba(45, 55, 47, 0.22);
    }}

    .dir-action-btn.primary-directions:hover {{
      background: #2D372F;
    }}

    .scene6-nav-row {{
      display: none;
    }}

    /* =========================================================
       BOTTOM NAVIGATION ROW & BUTTONS
       ========================================================= */
    .card-nav-row {{
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding-top: 12px;
      margin-top: auto;
      z-index: 25;
    }}

    .gold-btn {{
      padding: 10px 22px;
      background: #38453A;
      color: #FAF7F2;
      border: 1px solid rgba(190, 165, 115, 0.5);
      border-radius: 24px;
      font-family: 'Cinzel', serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(45, 55, 47, 0.22);
      transition: all 0.25s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}
    .gold-btn:hover {{
      background: #2B362D;
      border-color: #D4AF37;
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(45, 55, 47, 0.32);
    }}

    .nav-link-btn {{
      padding: 8px 18px;
      background: rgba(56, 69, 58, 0.06);
      color: #38453A;
      border: 1px solid rgba(56, 69, 58, 0.22);
      border-radius: 20px;
      font-family: 'Cinzel', serif;
      font-size: 10.5px;
      font-weight: 600;
      letter-spacing: 1.2px;
      cursor: pointer;
      transition: all 0.25s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}
    .nav-link-btn:hover {{
      background: rgba(56, 69, 58, 0.12);
      border-color: #38453A;
    }}

    .toast {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(60px);
      background: rgba(24, 2, 5, 0.92);
      color: var(--gold-light);
      border: 1px solid var(--gold-primary);
      padding: 10px 22px;
      border-radius: 24px;
      font-family: 'Montserrat', sans-serif;
      font-size: 11.5px;
      font-weight: 500;
      letter-spacing: 1px;
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
      box-shadow: 0 8px 24px rgba(0,0,0,0.6);
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>

  <!-- Floating Particles Canvas -->
  <canvas id="particlesCanvas"></canvas>

  <!-- Discreet Corner Controls -->
  <div class="corner-controls">
    <button id="audioBtn" class="icon-btn music-active" title="Background Music: Kudmayi Reprise (Female) (Playing)">
      <span id="audioIcon">🔊</span>
    </button>
  </div>

  <!-- Background Music: Kudmayi Reprise (Female) -->
  <audio id="bgMusic" autoplay loop preload="auto" playsinline webkit-playsinline>
    <source src="audio/kudmayi_reprise_female.m4a" type="audio/mp4">
    <source src="audio/kudmayi_reprise_female.mp3" type="audio/mpeg">
  </audio>

  <!-- Toast Notification -->
  <div id="toast" class="toast">Address copied to clipboard!</div>

  <!-- Main Presentation Stage -->
  <div class="stage-wrapper">

    <!-- Story Segmented Header Bar -->
    <div class="story-header-bar" id="storyHeaderBar">
      <div class="story-dash" onclick="restartPresentation(event)" title="1. Cordially Invited"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(2)" title="2. We're Getting Married"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(3)" title="3. Wedding Portrait"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(4)" title="4. Ceremony Details"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(5)" title="5. Event Schedule"><div class="story-dash-fill"></div></div>
      <div class="story-dash" onclick="userGoToStep(6)" title="6. Venue & Route Map"><div class="story-dash-fill"></div></div>
    </div>

    <!-- =========================================================
         SCENE 1: ROYAL ENVELOPE OPENING & YOU'RE CORDIALLY INVITED
         ========================================================= -->
    <div id="scene-invited" class="invitation-card active"><!-- The 4 Flaps Unfolding Outward in 3D directly over the card -->
      <div class="envelope-flaps-overlay" id="envelopeBox" title="Click to Open Invitation">
        <div class="flap flap-top"></div>
        <div class="flap flap-bottom"></div>
        <div class="flap flap-left"></div>
        <div class="flap flap-right"></div>
        <div class="leaf-glow-layer" id="leafGlow"></div>
        <div class="wax-seal" id="waxSeal" title="Click to Open Invitation"></div>
      </div>

      <!-- 3D Realistic Flying Butterfly (Emerges from center and perches at top) -->
      <div class="flying-butterfly-container" id="flyingButterfly">
        <div class="butterfly-shadow"></div>
        <div class="butterfly-3d">
          <div class="wing wing-left"></div>
          <div class="butterfly-body"></div>
          <div class="wing wing-right"></div>
        </div>
      </div>

      <div class="reveal-container">
        <div class="fade-youre">YOU'RE</div>
        <div class="fade-cordially">CORDIALLY</div>
        <div class="fade-invited">INVITED</div>
        
        <div class="gold-divider">
          <svg viewBox="0 0 24 24"><path d="M12 2L14.4 9.6L22 12L14.4 14.4L12 22L9.6 14.4L2 12L9.6 9.6L12 2Z"/></svg>
        </div>

        <p class="fade-subtext">
          to celebrate the joyous union and wedding ceremony of our beloved children
        </p>
      </div>

      <div class="card-nav-row">
        <button class="nav-link-btn" onclick="restartPresentation(event)">‹ Replay</button>
        <button class="gold-btn" onclick="userGoToStep(2)">Announcement ➔</button>
      </div>
    </div>

    <!-- =========================================================
         SCENE 2: WE'RE GETTING MARRIED (AFSAL & NAJILA ASHRAF)
         ========================================================= -->
    <div id="scene-couples" class="invitation-card"><!-- Perched Butterfly at top -->
      <div class="perched-butterfly-couples">
        <img class="perched-butterfly-img" src="{butterfly_full_b64}" alt="Golden Perched Butterfly" />
      </div>

      <div class="married-model-container">
        <div class="married-banner-title">WE'RE GETTING MARRIED</div>

        <div class="couple-calligraphy-wrap">
          <!-- Groom Name (Afsal) First, letter-by-letter reveal -->
          <div class="groom-calligraphy" id="groomName">
            <span class="char-span">A</span><span class="char-span">f</span><span class="char-span">s</span><span class="char-span">a</span><span class="char-span">l</span>
          </div>

          <!-- Ampersand & appears gracefully in center -->
          <div class="calligraphy-ampersand">&</div>

          <!-- Bride Name (Najila Ashraf) Second, letter-by-letter reveal -->
          <div class="bride-calligraphy" id="brideName">
            <span class="char-span">N</span><span class="char-span">a</span><span class="char-span">j</span><span class="char-span">i</span><span class="char-span">l</span><span class="char-span">a</span><span class="char-space">&nbsp;</span><span class="char-span">A</span><span class="char-span">s</span><span class="char-span">h</span><span class="char-span">r</span><span class="char-span">a</span><span class="char-span">f</span>
          </div>
        </div>
      </div>

      <div class="card-nav-row" style="margin-top: auto;">
        <button class="nav-link-btn" onclick="userGoToStep(1)">‹ Back</button>
        <button class="gold-btn" onclick="userGoToStep(3)">Wedding Portrait ➔</button>
      </div>
    </div>

    <!-- =========================================================
         SCENE 3: DANCING COUPLE PORTRAIT ARTWORK
         ========================================================= -->
    <div id="scene-portrait" class="invitation-card">
      <div class="scene3-artwork-container" onclick="triggerGracefulSpin(event)" title="Tap to spin the bride">
        <!-- 4-Frame Graceful Spin Animation Layer -->
        <img class="spin-frame spin-f1 active-frame" id="spinFrame1" src="{spin_f1_b64}" alt="Bride Graceful Pose 1 - Front View" />
        <img class="spin-frame spin-f2" id="spinFrame2" src="{spin_f2_b64}" alt="Bride Graceful Pose 2 - Spinning Back View" />
        <img class="spin-frame spin-f3" id="spinFrame3" src="{spin_f3_b64}" alt="Bride Graceful Pose 3 - Profile View Facing Groom" />
        <img class="spin-frame spin-f4" id="spinFrame4" src="{spin_f4_b64}" alt="Bride Graceful Pose 4 - Turning Front View" />

        <!-- Interactive Spin Option Button -->
        <button class="spin-action-pill" id="spinTriggerBtn" onclick="triggerGracefulSpin(event)" title="Gracefully spin the bride in a circle">
          <span>✨ Spin Bride ↺</span>
        </button>

        <!-- Navigation Overlay -->
        <div class="scene3-nav-overlay">
          <button class="nav-link-btn" onclick="userGoToStep(2)">‹ Back</button>
          <button class="gold-btn" onclick="userGoToStep(4)">Ceremony Details ➔</button>
        </div>
      </div>
    </div>

    <div id="scene-details" class="invitation-card"><div class="scene4-artwork-container">
        <!-- Reception Details Artwork Card (Matching User Reference Image) -->
        <img class="scene4-card-img" src="{scene4_card_b64}" alt="Ceremony Reception Details - Razak Hajee Kattil (V K) & Zainaba Razak" />

        <!-- Bottom Navigation Overlay -->
        <div class="scene4-nav-overlay">
          <button class="nav-link-btn" onclick="userGoToStep(3)">‹ Back</button>
          <button class="gold-btn" onclick="userGoToStep(5)">Event Schedule ➔</button>
        </div>
      </div>
    </div>

    <!-- =========================================================
         SCENE 5: CEREMONY SCHEDULE & AUSPICIOUS DAY (FLORAL WATERCOLOR MODEL)
         ========================================================= -->
    <div id="scene-schedule" class="invitation-card">
      <div class="scene5-body-content">
        <!-- Bismillah & Insha Allah -->
        <div class="insha-allah-header">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
        <div class="insha-allah-sub">INSHA ALLAH</div>

        <!-- Main Wedding Reception Card (Image 2 Authentic Model) -->
        <div class="schedule-main-card">
          <div class="schedule-event-badge">WEDDING RECEPTION</div>
          <div class="schedule-date-title">Sunday, January 3, 2027</div>
          <div class="schedule-time-title">12:00 PM Onwards</div>
          <div class="schedule-gold-rule"></div>
          <div class="schedule-venue-name">Zaithoon Villa <span class="venue-sub-tag">(Groom's Residence)</span></div>
          <div class="schedule-venue-city">Payyoli, Kozhikode</div>
        </div>

        <!-- Nikah Ceremony Card (Image 2 Authentic Model) -->
        <div class="schedule-nikah-card">
          <div class="nikah-tag">🕌 NIKAH CEREMONY</div>
          <p class="nikah-text">
            Will take place at <strong>Paloor Moihidheen Juma Masjid</strong> (Thikkodi)<br>
            <span class="nikah-datetime">on <strong>31-12-2026</strong> at <strong>11:00 AM</strong></span>
          </p>
        </div>

        <!-- Live Countdown -->
        <div class="countdown-wrap">
          <div class="countdown-label">✦ Countdown to the Auspicious Day ✦</div>
          <div class="timer-units">
            <div class="timer-unit"><span class="num" id="t-days">00</span><span class="unit">Days</span></div>
            <div class="timer-unit"><span class="num" id="t-hours">00</span><span class="unit">Hours</span></div>
            <div class="timer-unit"><span class="num" id="t-mins">00</span><span class="unit">Mins</span></div>
            <div class="timer-unit"><span class="num" id="t-secs">00</span><span class="unit">Secs</span></div>
          </div>
        </div>

        <!-- Authentic Compliments (Image 2 Authentic Model) -->
        <div class="compliments-note">
          With Best Compliments From:<br>
          <strong>Afeef, Ramshina Afeef, Irshad, Irfan,<br>Fathima Hiba, Family & Friends</strong>
        </div>
      </div>

      <div class="card-nav-row" style="margin-top: auto; z-index: 20;">
        <button class="nav-link-btn" onclick="userGoToStep(4)">‹ Back</button>
        <button class="gold-btn" onclick="userGoToStep(6)">Route Map ➔</button>
      </div>
    </div>

    <div id="scene-map" class="invitation-card">
      <div class="scene6-body-content">
        <div class="venue-title">VENUE & ROUTE MAP</div>
        <div class="venue-sub">Select a ceremony below for directions and location map</div>

        <!-- Venue Selection Tabs (Reception vs Nikah) -->
        <div class="venue-tab-switcher">
          <button class="venue-tab-btn active" id="tabReceptionBtn" onclick="selectVenueTab('reception')">
            🏡 Reception (Payyoli)
          </button>
          <button class="venue-tab-btn" id="tabNikahBtn" onclick="selectVenueTab('nikah')">
            🕌 Nikah (Thikkodi)
          </button>
        </div>

        <!-- Dynamic Venue Info Card -->
        <div class="address-card">
          <div class="venue-event-badge" id="venueEventBadge">WEDDING RECEPTION • SUN, JAN 3, 2027 • 12:00 PM</div>
          <div class="residence-name" id="venueName">Zaithoon Villa (Groom's Residence)</div>
          <div class="full-address" id="venueAddress">
            Payyoli, Kozhikode District, Kerala, India
          </div>
        </div>

        <!-- Reduced & Standardized Google Maps Embed -->
        <div class="gmap-frame-box">
          <iframe 
            id="gmapIframe"
            title="Google Maps Direction to Wedding Ceremony Venue"
            src="https://maps.google.com/maps?q=Payyoli,+Kozhikode,+Kerala&amp;hl=en&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed"
            allowfullscreen="" 
            loading="lazy">
          </iframe>
        </div>

        <!-- Standardized Directions Buttons -->
        <div class="directions-btn-grid">
          <a class="dir-action-btn primary-directions" id="getDirectionsLink" target="_blank" href="https://www.google.com/maps/dir/?api=1&destination=Zaithoon+Villa,+Payyoli,+Kozhikode,+Kerala">
            🗺️ Get Directions
          </a>
          <button class="dir-action-btn" onclick="copyVenueAddress()">
            📋 Copy Address
          </button>
        </div>
      </div>

      <!-- Navigation Row Pinned to Bottom (Matching Scene 5 Exactly) -->
      <div class="card-nav-row" style="margin-top: auto; z-index: 20;">
        <button class="nav-link-btn" onclick="userGoToStep(5)">‹ Back</button>
        <button class="gold-btn" onclick="restartPresentation(event)">✉️ Replay from Beginning</button>
      </div>
    </div>

  </div>

  <!-- Interactive Scripts -->
  <script>
    let currentStep = 1;
    let envelopeOpened = false;
    let autoPlayEnabled = true;
    let autoPlayTimer = null;

    const cards = [
      document.getElementById('scene-invited'),
      document.getElementById('scene-couples'),
      document.getElementById('scene-portrait'),
      document.getElementById('scene-details'),
      document.getElementById('scene-schedule'),
      document.getElementById('scene-map')
    ];

    /* Standard, peaceful pacing for each scene */
    const stepDurations = {{
      1: 13000, // Envelope unfold + butterfly flight + reading "You're Cordially Invited"
      2: 7000,  // We're Getting Married (letter-by-letter flowing ink reveal)
      3: 8500,  // Full Artwork Card
      4: 8500,  // Ceremony Reception Details
      5: 9000   // Ceremony Schedule & Live Countdown
    }};

    const storyDashes = document.querySelectorAll('.story-dash');
    let storyProgressRaf = null;
    let storyStartTime = 0;
    let storyPausedElapsed = 0;

    function updateStoryProgress(step) {{
      if (storyProgressRaf) cancelAnimationFrame(storyProgressRaf);
      storyPausedElapsed = 0;

      storyDashes.forEach((dash, idx) => {{
        const fill = dash.querySelector('.story-dash-fill');
        dash.classList.remove('active', 'completed', 'pending');

        if (idx + 1 < step) {{
          dash.classList.add('completed');
          fill.style.width = '100%';
        }} else if (idx + 1 > step) {{
          dash.classList.add('pending');
          fill.style.width = '0%';
        }} else {{
          dash.classList.add('active');
          fill.style.width = '0%';
          startDashAnimation(dash, fill, step);
        }}
      }});
    }}

    function startDashAnimation(dash, fill, step) {{
      const duration = stepDurations[step] || 8500;
      if (step === 6) {{
        fill.style.width = '100%';
        return;
      }}

      storyStartTime = performance.now() - storyPausedElapsed;

      function frame(now) {{
        if (!autoPlayEnabled) return;
        const elapsed = now - storyStartTime;
        const pct = Math.min(100, (elapsed / duration) * 100);
        fill.style.width = pct + '%';

        if (pct < 100) {{
          storyProgressRaf = requestAnimationFrame(frame);
        }} else {{
          goToStep(step + 1);
        }}
      }}
      storyProgressRaf = requestAnimationFrame(frame);
    }}

    function goToStep(step) {{
      if (step < 1 || step > 6) return;
      currentStep = step;

      cards.forEach((card, idx) => {{
        if (idx + 1 === step) {{
          card.classList.add('active');
        }} else {{
          card.classList.remove('active');
        }}
      }});

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
      updateStoryProgress(step);
      if (step === 3) {{
        showSpinFrame(1);
      }}
    }}

    function userGoToStep(step) {{
      goToStep(step);
    }}

    function nextStep() {{
      if (currentStep < 6) goToStep(currentStep + 1);
    }}

    function prevStep() {{
      if (currentStep > 1) goToStep(currentStep - 1);
    }}

    // ==========================================
    // MAJESTIC SLOW 4-SIDE FLAP OPENING & BUTTERFLY FLIGHT
    // ==========================================
    const envelopeBox = document.getElementById('envelopeBox');
    const waxSeal = document.getElementById('waxSeal');
    const flyingButterfly = document.getElementById('flyingButterfly');

    
    let currentSpinFrame = 1;
    let spinTimer = null;
    let isBrideSpinning = false;

    function showSpinFrame(frameNum) {{
      for (let i = 1; i <= 4; i++) {{
        const frameEl = document.getElementById('spinFrame' + i);
        if (frameEl) {{
          if (i === frameNum) {{
            frameEl.classList.add('active-frame');
          }} else {{
            frameEl.classList.remove('active-frame');
          }}
        }}
      }}
      currentSpinFrame = frameNum;
    }}

    function triggerGracefulSpin(e, numRotations = 2) {{
      if (e) e.stopPropagation();
      if (isBrideSpinning) return;
      isBrideSpinning = true;

      const btn = document.getElementById('spinTriggerBtn');
      if (btn) btn.classList.add('spinning');

      let currentStepIdx = 0;
      const totalSteps = numRotations * 4;
      let frame = 1;

      if (spinTimer) clearInterval(spinTimer);

      spinTimer = setInterval(() => {{
        currentStepIdx++;
        frame = (frame % 4) + 1;
        showSpinFrame(frame);

        if (currentStepIdx >= totalSteps) {{
          clearInterval(spinTimer);
          spinTimer = null;
          // Smoothly settle back on Frame 1
          setTimeout(() => {{
            showSpinFrame(1);
            isBrideSpinning = false;
            if (btn) btn.classList.remove('spinning');
          }}, 500);
        }}
      }}, 500);
    }}

    function triggerCoupleTwirl(e) {{
      triggerGracefulSpin(e, 2);
    }}

    function openInvitation() {{
      if (envelopeOpened) return;
      envelopeOpened = true;

      playBackgroundSong();

      const envBox = document.getElementById('envelopeBox');
      const sealEl = document.getElementById('waxSeal');

      if (envBox) {{
        envBox.classList.add('lighting-active');
        setTimeout(() => {{
          envBox.classList.add('opened');
          if (sealEl) {{
            sealEl.style.opacity = '0';
            sealEl.style.visibility = 'hidden';
            sealEl.style.pointerEvents = 'none';
          }}
        }}, 650);
      }}

      if (flyingButterfly) {{
        flyingButterfly.classList.remove('landed');
        flyingButterfly.classList.add('fly-active');
        setTimeout(() => {{
          flyingButterfly.classList.remove('fly-active');
          flyingButterfly.classList.add('landed');
        }}, 5600);
      }}
    }}
if (waxSeal) waxSeal.addEventListener('click', openInvitation);
    if (envelopeBox) envelopeBox.addEventListener('click', openInvitation);

    function restartPresentation(e) {{
      if (e) {{
        try {{ e.stopPropagation(); }} catch (err) {{}}
      }}
      if (storyProgressRaf) cancelAnimationFrame(storyProgressRaf);
      if (autoPlayTimer) clearTimeout(autoPlayTimer);
      autoPlayEnabled = true;

      // Clean URL params (?step=6) so refreshing stays at beginning
      try {{
        if (window.history && window.history.replaceState) {{
          window.history.replaceState({{}}, document.title, window.location.pathname);
        }}
      }} catch (err) {{}}

      // Grab elements cleanly inside function scope
      const envBox = document.getElementById('envelopeBox');
      const sealEl = document.getElementById('waxSeal');
      const butterflyEl = document.getElementById('flyingButterfly');
      const musicEl = document.getElementById('bgMusic');
      const flaps = document.querySelectorAll('.flap');

      // Temporarily disable transitions during reset
      if (envBox) {{
        envBox.style.transition = 'none';
        envBox.classList.remove('opened', 'lighting-active');
      }}
      if (sealEl) sealEl.style.transition = 'none';
      flaps.forEach(f => f.style.transition = 'none');
      if (butterflyEl) {{
        butterflyEl.style.transition = 'none';
        butterflyEl.style.animation = 'none';
        butterflyEl.classList.remove('fly-active', 'landed');
        butterflyEl.style.opacity = '0';
      }}

      envelopeOpened = false;

      // Force layout reflow so class removals register instantly
      if (envBox) void envBox.offsetHeight;

      // Completely remove all inline styles so stylesheet rules apply naturally
      if (envBox) envBox.removeAttribute('style');
      if (sealEl) sealEl.removeAttribute('style');
      flaps.forEach(f => f.removeAttribute('style'));
      if (butterflyEl) {{
        butterflyEl.removeAttribute('style');
      }}

      // Reset music position if playing
      if (musicEl) {{
        try {{ musicEl.currentTime = 0; }} catch (err) {{}}
      }}

      // Seamlessly navigate to step 1 (The closed envelope page)
      goToStep(1);
      window.scrollTo({{ top: 0, behavior: 'smooth' }});

      // Peaceful preview before gentle auto-open if user doesn't click
      setTimeout(() => {{
        if (!envelopeOpened && currentStep === 1) {{
          openInvitation();
        }}
      }}, 4500);
    }}
    window.addEventListener('DOMContentLoaded', () => {{
      const urlParams = new URLSearchParams(window.location.search);
      const stepParam = parseInt(urlParams.get('step'));
      const openedParam = urlParams.get('opened');

      if (openedParam === '1' || (stepParam && stepParam > 1)) {{
        envelopeOpened = true;
        if (envelopeBox) envelopeBox.classList.add('opened');
        if (waxSeal) {{
          waxSeal.style.opacity = '0';
          waxSeal.style.visibility = 'hidden';
          waxSeal.style.pointerEvents = 'none';
        }}
        if (flyingButterfly) flyingButterfly.classList.add('landed');
      }}

      if (stepParam && stepParam >= 1 && stepParam <= 6) {{
        goToStep(stepParam);
      }} else {{
        updateStoryProgress(1);
        setTimeout(() => {{
          if (!envelopeOpened) {{
            openInvitation();
          }}
        }}, 2800);
      }}
    }});
// ==========================================
    // FLOATING PARTICLES CANVAS
    // ==========================================
    const pCanvas = document.getElementById('particlesCanvas');
    const pCtx = pCanvas.getContext('2d');
    let particles = [];

    function resizeParticlesCanvas() {{
      pCanvas.width = window.innerWidth;
      pCanvas.height = window.innerHeight;
    }}
    window.addEventListener('resize', resizeParticlesCanvas);
    resizeParticlesCanvas();

    class Particle {{
      constructor() {{
        this.reset();
      }}
      reset() {{
        this.x = Math.random() * pCanvas.width;
        this.y = Math.random() * -50;
        this.size = Math.random() * 3.5 + 1.5;
        this.speedY = Math.random() * 0.7 + 0.3;
        this.speedX = Math.sin(Math.random() * Math.PI * 2) * 0.4;
        this.opacity = Math.random() * 0.5 + 0.2;
        this.rotation = Math.random() * 360;
        this.rotSpeed = (Math.random() - 0.5) * 1.2;
        this.isPetal = Math.random() > 0.6;
      }}
      update() {{
        this.y += this.speedY;
        this.x += this.speedX + Math.sin(this.y * 0.02) * 0.4;
        this.rotation += this.rotSpeed;
        if (this.y > pCanvas.height + 20) {{
          this.reset();
        }}
      }}
      draw() {{
        // Clean off-white background: No falling petals or leaves
        pCtx.save();
        pCtx.translate(this.x, this.y);
        pCtx.globalAlpha = this.opacity * 0.4;
        pCtx.fillStyle = '#D4AF37';
        pCtx.beginPath();
        pCtx.arc(0, 0, this.size * 0.35, 0, Math.PI * 2);
        pCtx.fill();
        pCtx.restore();
      }}
    }}

    for (let i = 0; i < 26; i++) {{
      const p = new Particle();
      p.y = Math.random() * pCanvas.height;
      particles.push(p);
    }}

    function animateParticles() {{
      pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);
      particles.forEach(p => {{
        p.update();
        p.draw();
      }});
      requestAnimationFrame(animateParticles);
    }}
    animateParticles();

    // ==========================================
    // DEFAULT BACKGROUND MUSIC SYSTEM: "KUDMAYI REPRISE (FEMALE)"
    // ==========================================
    const bgMusic = document.getElementById('bgMusic');
    const audioBtn = document.getElementById('audioBtn');
    const audioIcon = document.getElementById('audioIcon');
    let isMusicPlaying = true;

    function playBackgroundSong() {{
      if (!bgMusic) return;
      bgMusic.volume = 0.70;
      const playPromise = bgMusic.play();
      if (playPromise !== undefined) {{
        playPromise.then(() => {{
          isMusicPlaying = true;
          if (audioIcon) audioIcon.innerText = '🔊';
          if (audioBtn) audioBtn.classList.add('music-active');
        }}).catch((err) => {{
          console.log('Autoplay waiting for first touch/interaction:', err);
        }});
      }}
    }}

    playBackgroundSong();

    const unlockDefaultAudio = () => {{
      if (bgMusic) {{
        bgMusic.volume = 0.70;
        bgMusic.play().then(() => {{
          isMusicPlaying = true;
          if (audioIcon) audioIcon.innerText = '🔊';
          if (audioBtn) audioBtn.classList.add('music-active');
        }}).catch(() => {{}});
      }}
    }};

    ['click', 'touchstart', 'touchend', 'pointerdown'].forEach((evt) => {{
      document.addEventListener(evt, unlockDefaultAudio, {{ once: true, passive: true }});
      window.addEventListener(evt, unlockDefaultAudio, {{ once: true, passive: true }});
    }});

    function toggleBackgroundSong() {{
      if (!bgMusic) return;
      if (isMusicPlaying) {{
        bgMusic.pause();
        isMusicPlaying = false;
        if (audioIcon) audioIcon.innerText = '🔇';
        if (audioBtn) audioBtn.classList.remove('music-active');
      }} else {{
        bgMusic.volume = 0.70;
        bgMusic.play().then(() => {{
          isMusicPlaying = true;
          if (audioIcon) audioIcon.innerText = '🔊';
          if (audioBtn) audioBtn.classList.add('music-active');
        }}).catch((e) => console.warn('Audio play error:', e));
      }}
    }}

    if (audioBtn) {{
      audioBtn.addEventListener('click', (e) => {{
        e.stopPropagation();
        toggleBackgroundSong();
      }});
    }}

    // ==========================================
    // LIVE WEDDING COUNTDOWN TIMER
    // ==========================================
    const weddingDate = new Date('2027-01-03T12:00:00+05:30').getTime();

    function updateCountdown() {{
      const now = new Date().getTime();
      const diff = weddingDate - now;

      if (diff > 0) {{
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const secs = Math.floor((diff % (1000 * 60)) / 1000);

        document.getElementById('t-days').innerText = String(days).padStart(2, '0');
        document.getElementById('t-hours').innerText = String(hours).padStart(2, '0');
        document.getElementById('t-mins').innerText = String(mins).padStart(2, '0');
        document.getElementById('t-secs').innerText = String(secs).padStart(2, '0');
      }} else {{
        document.getElementById('t-days').innerText = '00';
        document.getElementById('t-hours').innerText = '00';
        document.getElementById('t-mins').innerText = '00';
        document.getElementById('t-secs').innerText = '00';
      }}
    }}
    setInterval(updateCountdown, 1000);
    updateCountdown();

    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{
        t.classList.remove('show');
      }}, 2600);
    }}

    const venueDataMap = {{
      reception: {{
        badge: "WEDDING RECEPTION • SUN, JAN 3, 2027 • 12:00 PM",
        name: "Zaithoon Villa (Groom's Residence)",
        address: "Payyoli, Kozhikode District, Kerala, India",
        fullCopy: "Zaithoon Villa (Groom's Residence), Payyoli, Kozhikode District, Kerala, India",
        mapSrc: "https://maps.google.com/maps?q=Payyoli,+Kozhikode,+Kerala&hl=en&t=&z=15&ie=UTF8&iwloc=&output=embed",
        dirUrl: "https://www.google.com/maps/dir/?api=1&destination=Payyoli,+Kozhikode,+Kerala"
      }},
      nikah: {{
        badge: "🕌 NIKAH CEREMONY • THU, DEC 31, 2026 • 11:00 AM",
        name: "Paloor Moihidheen Juma Masjid",
        address: "Paloor, Thikkodi, Kozhikode District, Kerala, India",
        fullCopy: "Paloor Moihidheen Juma Masjid, Thikkodi, Kozhikode District, Kerala, India",
        mapSrc: "https://maps.google.com/maps?q=Paloor+Muhiyudheen+Juma+Masjid,+Thikkodi,+Kozhikode,+Kerala&hl=en&t=&z=15&ie=UTF8&iwloc=&output=embed",
        dirUrl: "https://www.google.com/maps/dir/?api=1&destination=Paloor+Muhiyudheen+Juma+Masjid,+Thikkodi,+Kozhikode,+Kerala"
      }}
    }};

    let currentSelectedVenue = 'reception';

    function selectVenueTab(venueKey) {{
      currentSelectedVenue = venueKey;
      const data = venueDataMap[venueKey];
      if (!data) return;

      const tabRec = document.getElementById('tabReceptionBtn');
      const tabNik = document.getElementById('tabNikahBtn');
      if (tabRec && tabNik) {{
        if (venueKey === 'reception') {{
          tabRec.classList.add('active');
          tabNik.classList.remove('active');
        }} else {{
          tabRec.classList.remove('active');
          tabNik.classList.add('active');
        }}
      }}

      const badgeEl = document.getElementById('venueEventBadge');
      const nameEl = document.getElementById('venueName');
      const addrEl = document.getElementById('venueAddress');
      const mapEl = document.getElementById('gmapIframe');
      const dirEl = document.getElementById('getDirectionsLink');

      if (badgeEl) badgeEl.innerText = data.badge;
      if (nameEl) nameEl.innerText = data.name;
      if (addrEl) addrEl.innerText = data.address;
      if (mapEl) mapEl.src = data.mapSrc;
      if (dirEl) dirEl.href = data.dirUrl;

      showToast('Switched map to ' + data.name);
    }}

    function copyVenueAddress() {{
      const data = venueDataMap[currentSelectedVenue] || venueDataMap.reception;
      navigator.clipboard.writeText(data.fullCopy).then(() => {{
        showToast('Address copied to clipboard!');
      }}).catch(() => {{
        showToast(data.fullCopy);
      }});
    }}

    function copyAddress() {{
      copyVenueAddress();
    }}

    function copyAddress() {{
      const address = "Zaithoon Villa (Razak Hajee Kattil), Payyoli, Kozhikode District, Kerala, India";
      navigator.clipboard.writeText(address).then(() => {{
        showToast('Address copied to clipboard!');
      }}).catch(() => {{
        showToast('Address: Zaithoon Villa, Payyoli, Kozhikode');
      }});
    }}

    function downloadICal() {{
      const icsData = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//Wedding Reception//EN',
        'CALSCALE:GREGORIAN',
        'METHOD:PUBLISH',
        'BEGIN:VEVENT',
        'SUMMARY:Wedding Reception of Afsal & Najila Ashraf',
        'DESCRIPTION:Cordially invite you and your family to grace the joyous occasion of the wedding reception of their beloved son Afsal with Najila Ashraf. Hosted by Razak Hajee Kattil (V K) & Zainaba Razak.',
        'LOCATION:Zaithoon Villa, Payyoli, Kozhikode, Kerala',
        'DTSTART:20270103T063000Z',
        'DTEND:20270103T103000Z',
        'STATUS:CONFIRMED',
        'END:VEVENT',
        'END:VCALENDAR'
      ].join('\\r\\n');

      const blob = new Blob([icsData], {{ type: 'text/calendar;charset=utf-8' }});
      const link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.setAttribute('download', 'Wedding_Najila_Afsal.ics');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('Calendar event downloaded!');
    }}

    // ==========================================
    // MOBILE TAP & GESTURE NAVIGATION
    // ==========================
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartTime = 0;

    document.addEventListener('touchstart', (e) => {{
      if (e.touches.length > 0) {{
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchStartTime = performance.now();
      }}
    }}, {{ passive: true }});

    document.addEventListener('touchend', (e) => {{
      if (e.changedTouches.length === 0) return;
      const endX = e.changedTouches[0].clientX;
      const endY = e.changedTouches[0].clientY;
      const deltaX = endX - touchStartX;
      const deltaY = endY - touchStartY;
      const elapsedTime = performance.now() - touchStartTime;

      if (Math.abs(deltaX) > 45 && Math.abs(deltaX) > Math.abs(deltaY) * 1.2) {{
        if (deltaX < 0) {{
          nextStep();
        }} else {{
          prevStep();
        }}
        return;
      }}

      if (Math.abs(deltaX) < 18 && Math.abs(deltaY) < 18 && elapsedTime < 380) {{
        const interactiveTarget = e.target.closest('button, a, .icon-btn, .story-dash, iframe, input, select');
        if (interactiveTarget) return;

        if (currentStep === 1 && !envelopeOpened) {{
          openInvitation();
          return;
        }}

        if (endX < window.innerWidth * 0.32) {{
          prevStep();
        }} else {{
          nextStep();
        }}
      }}
    }}, false);

    const stageWrapper = document.querySelector('.stage-wrapper');
    if (stageWrapper) {{
      stageWrapper.addEventListener('click', (e) => {{
        if (e.target.closest('button, a, .icon-btn, .story-dash, iframe, input, select, #waxSeal, .envelope-flaps-overlay')) {{
          return;
        }}
        if (currentStep === 1 && !envelopeOpened) {{
          openInvitation();
          return;
        }}
        const rect = stageWrapper.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        if (clickX < rect.width * 0.32) {{
          prevStep();
        }} else {{
          nextStep();
        }}
      }});
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ') nextStep();
      if (e.key === 'ArrowLeft') prevStep();
    }});

    // Deep linking support for direct scene & venue inspection (?step=X&venue=nikah)
    window.addEventListener('DOMContentLoaded', () => {{
      try {{
        const params = new URLSearchParams(window.location.search);
        const stepParam = parseInt(params.get('step'));
        const venueParam = params.get('venue');

        if (stepParam && stepParam >= 1 && stepParam <= 6) {{
          if (stepParam > 1) {{
            envelopeOpened = true;
            if (envelopeBox) envelopeBox.classList.add('opened');
          }}
          goToStep(stepParam);
          if (stepParam === 6 && venueParam === 'nikah') {{
            setTimeout(() => selectVenueTab('nikah'), 150);
          }}
        }}
      }} catch (err) {{
        console.error('URL param handling error:', err);
      }}
    }});
  </script>
  <!-- SVG Soft Dress Flow Filter (Flowing watercolor gown motion) -->
  <svg style="position: absolute; width: 0; height: 0; pointer-events: none;" aria-hidden="true">
    <defs>
      <filter id="softDressFlow" x="-10%" y="-10%" width="120%" height="120%">
        <feTurbulence type="fractalNoise" baseFrequency="0.012 0.016" numOctaves="2" result="noise">
          <animate attributeName="baseFrequency" dur="7s" values="0.010 0.014; 0.016 0.022; 0.010 0.014" repeatCount="indefinite" />
        </feTurbulence>
        <feDisplacementMap in="SourceGraphic" in2="noise" scale="5" xChannelSelector="R" yChannelSelector="G" />
      </filter>
    </defs>
  </svg>

</body>
</html>
'''

output_scratch = os.path.join(base_dir, "index.html")
with open(output_scratch, "w", encoding="utf-8") as f:
    f.write(html_content)

output_scratch_alias = os.path.join(base_dir, "wedding_invitation.html")
with open(output_scratch_alias, "w", encoding="utf-8") as f:
    f.write(html_content)

output_brain = os.path.join(brain_dir, "wedding_invitation.html")
with open(output_brain, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Wedding invitation generated successfully:")
print("1. Scratch index.html:", os.path.exists(output_scratch), "Size:", os.path.getsize(output_scratch))
print("2. Brain wedding_invitation.html:", os.path.exists(output_brain), "Size:", os.path.getsize(output_brain))
