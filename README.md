# Noctis Sydney — static site

A static multi-page site for a fictional luxury car hire brand in Sydney. Editorial monochrome aesthetic, Three.js animated hero on each car page, detailed per-car content.

## Structure

```
noctis-site/
├── index.html                          # Homepage (Sydney)
├── README.md                           # This file
├── assets/
│   ├── noctis.css                      # All shared styles
│   └── noctis-3d.js                    # Three.js setup + per-car scene config
└── fleet/
    ├── rolls-royce-spectre.html        # No. 01 · ultra-luxury EV
    ├── aston-martin-db12.html          # No. 02 · V8 grand tourer
    ├── mclaren-750s.html               # No. 03 · performance
    ├── ferrari-purosangue.html         # No. 04 · V12 estate
    ├── mercedes-g63.html               # No. 05 · character
    └── porsche-911-gt3.html            # No. 06 · driver's
```

## How to run it

**Double-click `index.html` and it works.** All pages use classic scripts (Three.js loaded from a CDN, not as an ES module), so opening via `file://` in any modern browser is fine — no local server required.

If you prefer, you can also serve it locally:

```bash
cd noctis-site
python3 -m http.server 8000
# then open http://localhost:8000
```

Or in VS Code: install the **Live Server** extension → right-click `index.html` → "Open with Live Server."

## Robustness notes

- Page content is visible even if JavaScript fails to load. `.reveal` animations are applied only once JS confirms it's running (by adding `.js-ready` to `<html>`), so a broken CDN or blocked script won't leave you with a blank page.
- Three.js is loaded from jsDelivr's UMD build. If jsDelivr is blocked, the 3D hero is skipped and the static fallback image shows instead — no errors bubble up.
- Mobile (<768px) always shows the static fallback image; no 3D canvas is created.
- `prefers-reduced-motion: reduce` disables all animations and 3D.

## What each car's 3D scene looks like

Each car has a distinctive 3D form, material, and lighting, tuned to its character — defined in `assets/noctis-3d.js`:

| Car | 3D form | Material |
|---|---|---|
| Spectre | Torus knot | Cool chrome/silver, mirror-smooth |
| DB12 | Torus ring | Warm bronze, clearcoat |
| 750S | Faceted icosahedron | Papaya orange, flat-shaded carbon |
| Purosangue | Faceted octahedron | Rosso Imola, glossy |
| G 63 | Rotating cube | Gunmetal, matte |
| 911 GT3 | Slim torus / wheel | Python green, satin |

All scenes:
- Auto-rotate slowly
- Respond to cursor position (subtle parallax tilt)
- Float gently (sine oscillation)
- Include a 240-point particle field drifting in the background
- Gate to a static poster image below 768px viewport width
- Respect `prefers-reduced-motion`

## What's production-ready vs what isn't

**Production-ready:**
- Layout, typography, color system, motion
- Accessibility (semantic HTML, reduced-motion support, mobile gating for 3D)
- Content depth per car
- Responsive across mobile, tablet, desktop

**Not production-ready (swap before client-facing):**
- **Images** — all `picsum.photos` placeholder URLs. Replace with real photography or Nano Banana 2–generated shots.
- **Form handler** — submits to a dummy success state. Wire to Resend/Formspree.
- **SEO** — OG images, sitemap, robots.txt, structured data not wired yet.
- **Domain** — references `.com.au` but no real domain/SSL.

## Next steps (if you want to take this further)

1. Swap all `picsum.photos` seed URLs with real photography (8–15 images per car page × 6 pages = ~80 images total)
2. Build out a shared Reserve modal that deep-links to each car (instead of sending users back to the homepage form)
3. Migrate to Next.js if you need a CMS — per the `premium-website-builder` skill's tech-stack recommendation
4. Deploy to Vercel: `vercel --prod` from the folder

## Credits

- **Fonts:** Fraunces (display), Inter (body) — both via Google Fonts
- **3D:** Three.js r160 via jsDelivr CDN
- **Everything else:** hand-rolled HTML / CSS / vanilla JS

© 2026 Noctis Automotive Pty Ltd (fictional)
