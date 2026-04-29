#!/usr/bin/env bash
# =============================================================
# Noctis — Nano Banana 2 image generation script
# Generates all 37 photos for the site in one run.
#
# Prerequisites:
#   1. Bun installed (curl -fsSL https://bun.sh/install | bash)
#   2. Nano Banana 2 skill installed (see setup.sh)
#   3. Gemini API key saved to ~/.nano-banana/.env
#
# Run from the site root:
#   bash scripts/generate-images.sh
#
# Total cost estimate: ~$4 (Flash @ 2K) + $0.30 (Pro 4K Sydney hero) ≈ $4.30
# Total time: ~15–20 min depending on Gemini response latency
# =============================================================
set -e

# Move to the site root regardless of where script was launched from
cd "$(dirname "$0")/.."
mkdir -p images
cd images

# Check nano-banana is on PATH
if ! command -v nano-banana >/dev/null 2>&1; then
  echo "❌ nano-banana command not found."
  echo "   Run scripts/setup.sh first, or ensure \$HOME/.bun/bin is on PATH."
  exit 1
fi

# Visual style header — prepended to every car prompt so the set feels cohesive
VS="Editorial cinematic automotive photography. Muted, premium palette. \
Single dramatic directional light from upper-left. Shallow-to-medium depth of field. \
No visible people, no text, no signage, no badges. Generous negative space. \
Cohesive editorial monochrome aesthetic with one tonal accent per subject."

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Noctis — generating 37 images via Nano Banana 2"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ----- 1. Homepage hero (Sydney) — Pro quality -----
echo "→ [1/37] Sydney harbour hero (Pro 4K)..."
nano-banana "$VS Sydney Harbour at dawn from an elevated vantage in Walsh Bay. \
Sydney Harbour Bridge silhouetted on the left, Opera House shells visible on the right, \
pre-dawn light on the water, cool blue and warm grey palette, generous sky for text overlay." \
  --model pro -s 4K -a 16:9 -o sydney-hero

# ----- 2. ROLLS-ROYCE SPECTRE (Arctic White, silver/chrome accent) -----
echo ""
echo "→ [2/37] Spectre hero..."
nano-banana "$VS 2025 Rolls-Royce Spectre coupe, Arctic White paintwork, \
three-quarter front view, parked on polished concrete in a minimalist dark gallery. \
Single overhead softbox, deep shadows, crisp reflection on paintwork." \
  -s 2K -a 16:9 -o spectre-hero

echo "→ [3/37] Spectre gallery 1..."
nano-banana "$VS White Rolls-Royce Spectre from directly behind, low-angle, \
tail lights illuminated, dark warehouse backdrop, negative space above." \
  -s 2K -a 4:3 -o spectre-1

echo "→ [4/37] Spectre gallery 2..."
nano-banana "$VS Detail shot of a white Rolls-Royce Spectre's Pantheon grille \
and unbadged hood, shallow focus, raking light, black background, macro feel." \
  -s 2K -a 4:3 -o spectre-2

echo "→ [5/37] Spectre gallery 3..."
nano-banana "$VS Rolls-Royce Spectre interior: starlight headliner with thousands of \
fibre-optic points, crisp white leather seats, open-pore wood, warm soft key light." \
  -s 2K -a 4:3 -o spectre-3

echo "→ [6/37] Spectre gallery 4..."
nano-banana "$VS Arctic White Rolls-Royce Spectre on a narrow coastal road at blue hour, \
still car with slight cloud motion in sky, editorial restraint, no other vehicles." \
  -s 2K -a 4:3 -o spectre-4

echo "→ [7/37] Spectre fleet card..."
nano-banana "$VS Arctic White Rolls-Royce Spectre, vertical portrait composition, \
three-quarter front view, dark Walsh Bay warehouse backdrop, single dramatic overhead light." \
  -s 2K -a 4:5 -o spectre-card

# ----- 3. ASTON MARTIN DB12 (Magnetic Silver, warm bronze accent) -----
echo ""
echo "→ [8/37] DB12 hero..."
nano-banana "$VS Magnetic Silver 2024 Aston Martin DB12 Volante with roof down, \
three-quarter profile, parked on a coastal road NSW at golden hour. \
Cliff and ocean softly defocused behind. Warm cream and bronze palette." \
  -s 2K -a 16:9 -o db12-hero

echo "→ [9/37] DB12 gallery 1..."
nano-banana "$VS Aston Martin DB12 Volante detail of front grille and iconic side strake vent, \
dramatic raking light, shallow focus." \
  -s 2K -a 4:3 -o db12-1

echo "→ [10/37] DB12 gallery 2..."
nano-banana "$VS Aston Martin DB12 roof-down cabin shot, obsidian black leather seats, \
brogue stitching, chestnut accents, soft natural light from camera right." \
  -s 2K -a 4:3 -o db12-2

echo "→ [11/37] DB12 gallery 3..."
nano-banana "$VS Aston Martin DB12 Volante three-quarter rear view, roof down, \
parked in the Southern Highlands at late afternoon, rolling hills behind." \
  -s 2K -a 4:3 -o db12-3

echo "→ [12/37] DB12 gallery 4..."
nano-banana "$VS Aston Martin DB12 wheel and tyre detail, machined face, \
dark brake caliper, low-angle raking light." \
  -s 2K -a 4:3 -o db12-4

echo "→ [13/37] DB12 fleet card..."
nano-banana "$VS Aston Martin DB12 Volante, roof down, portrait-orientation hero \
composition for a fleet card, moody dark Sydney Walsh Bay warehouse backdrop." \
  -s 2K -a 4:5 -o db12-card

# ----- 4. McLAREN 750S SPIDER (Volcano Orange) -----
echo ""
echo "→ [14/37] 750S hero..."
nano-banana "$VS Volcano Orange McLaren 750S Spider, roof retracted, low three-quarter \
front view, parked in a modern industrial space with polished concrete floor. \
Single overhead light, deep shadows. Orange accent pops against cool grey surroundings." \
  -s 2K -a 16:9 -o 750s-hero

echo "→ [15/37] 750S gallery 1..."
nano-banana "$VS McLaren 750S dihedral door open, three-quarter front view, \
carbon fibre sill visible, single orange accent in monochrome scene." \
  -s 2K -a 4:3 -o 750s-1

echo "→ [16/37] 750S gallery 2..."
nano-banana "$VS McLaren 750S cockpit detail: small steering wheel, carbon-shell \
Super-Light seats in black Alcantara with orange stitching, cool key light." \
  -s 2K -a 4:3 -o 750s-2

echo "→ [17/37] 750S gallery 3..."
nano-banana "$VS McLaren 750S Spider rear three-quarter, low angle, \
showing rear buttresses and central-exit exhaust, pure matte black backdrop." \
  -s 2K -a 4:3 -o 750s-3

echo "→ [18/37] 750S gallery 4..."
nano-banana "$VS Close-up of McLaren 750S side air intake and carbon ceramic brake disc, \
raking light, editorial still-life feel." \
  -s 2K -a 4:3 -o 750s-4

echo "→ [19/37] 750S fleet card..."
nano-banana "$VS Volcano Orange McLaren 750S Spider roof retracted, \
portrait-orientation fleet card composition, dark Walsh Bay warehouse backdrop, \
dramatic overhead light." \
  -s 2K -a 4:5 -o 750s-card

# ----- 5. FERRARI PUROSANGUE (Rosso Imola) -----
echo ""
echo "→ [20/37] Purosangue hero..."
nano-banana "$VS Rosso Imola Ferrari Purosangue four-door GT, three-quarter front view, \
parked in a modern gallery space. Deep red paintwork catches single overhead light. \
Cinematic composition with upper-third negative space." \
  -s 2K -a 16:9 -o purosangue-hero

echo "→ [21/37] Purosangue gallery 1..."
nano-banana "$VS Ferrari Purosangue rear-hinged welcome door open at 79 degrees, \
interior visible — Iroko wood and cream leather." \
  -s 2K -a 4:3 -o purosangue-1

echo "→ [22/37] Purosangue gallery 2..."
nano-banana "$VS Close-up of Ferrari Purosangue engine bay — V12 mounted mid-front, \
red crackle paint cover, polished manifolds, dramatic warehouse lighting." \
  -s 2K -a 4:3 -o purosangue-2

echo "→ [23/37] Purosangue gallery 3..."
nano-banana "$VS Ferrari Purosangue rear three-quarter on a winding country road \
at blue hour, Southern Highlands Australia, subtle motion blur around car." \
  -s 2K -a 4:3 -o purosangue-3

echo "→ [24/37] Purosangue gallery 4..."
nano-banana "$VS Detail of Ferrari Purosangue instrument cluster and steering wheel, \
black Alcantara, yellow Cavallino emblem, dramatic side lighting." \
  -s 2K -a 4:3 -o purosangue-4

echo "→ [25/37] Purosangue fleet card..."
nano-banana "$VS Rosso Imola Ferrari Purosangue, vertical portrait composition, \
three-quarter front view, moody warehouse backdrop, dramatic overhead light." \
  -s 2K -a 4:5 -o purosangue-card

# ----- 6. MERCEDES-AMG G 63 (Obsidian Black Metallic) -----
echo ""
echo "→ [26/37] G 63 hero..."
nano-banana "$VS Obsidian Black Metallic 2024 Mercedes-AMG G 63, \
three-quarter front view, parked outside a restored warehouse in Paddington Sydney. \
Boxy silhouette pin-sharp, reflections from single overhead streetlight. \
Warm late afternoon, cream palette." \
  -s 2K -a 16:9 -o g63-hero

echo "→ [27/37] G 63 gallery 1..."
nano-banana "$VS Mercedes-AMG G 63 from directly front on, slat grille face-on, \
headlights off, moody low-key lighting." \
  -s 2K -a 4:3 -o g63-1

echo "→ [28/37] G 63 gallery 2..."
nano-banana "$VS Detail of Mercedes G 63 external door hinges and indicator pillar, \
chrome, macro focus." \
  -s 2K -a 4:3 -o g63-2

echo "→ [29/37] G 63 gallery 3..."
nano-banana "$VS Mercedes G 63 cabin interior — Macchiato Beige Nappa leather, \
physical metal switches, sidekick dashboard, soft window light." \
  -s 2K -a 4:3 -o g63-3

echo "→ [30/37] G 63 gallery 4..."
nano-banana "$VS Mercedes G 63 rear view with spare wheel cover, elegant restraint, \
dark cool palette." \
  -s 2K -a 4:3 -o g63-4

echo "→ [31/37] G 63 fleet card..."
nano-banana "$VS Obsidian Black Mercedes-AMG G 63, portrait-orientation fleet card, \
three-quarter front, dark Walsh Bay backdrop, single overhead key light." \
  -s 2K -a 4:5 -o g63-card

# ----- 7. PORSCHE 911 GT3 TOURING (Python Green) -----
echo ""
echo "→ [32/37] 911 hero..."
nano-banana "$VS Python Green 2024 Porsche 911 GT3 Touring, three-quarter profile, \
parked on a quiet mountain road at dawn. Pronounced rear haunches, no rear wing. \
Soft morning light, cool palette of greens and greys." \
  -s 2K -a 16:9 -o 911-hero

echo "→ [33/37] 911 gallery 1..."
nano-banana "$VS Porsche 911 GT3 Touring cabin emphasising the manual gear lever \
and GT silver-stitched Alcantara seats, soft natural light from camera left." \
  -s 2K -a 4:3 -o 911-1

echo "→ [34/37] 911 gallery 2..."
nano-banana "$VS Porsche 911 GT3 Touring rear view showing centre-exit exhaust \
and subtle rear lip, dramatic low-angle editorial photography." \
  -s 2K -a 4:3 -o 911-2

echo "→ [35/37] 911 gallery 3..."
nano-banana "$VS Close-up detail of Porsche 911 GT3 front fender and centre-lock wheel, \
raking light, focus on geometry." \
  -s 2K -a 4:3 -o 911-3

echo "→ [36/37] 911 gallery 4..."
nano-banana "$VS Python Green Porsche 911 GT3 Touring on the Putty Road at golden hour, \
Australian bush landscape softly defocused behind, editorial restraint." \
  -s 2K -a 4:3 -o 911-4

echo "→ [37/37] 911 fleet card..."
nano-banana "$VS Python Green Porsche 911 GT3 Touring, vertical portrait composition, \
moody concrete-floored Walsh Bay warehouse backdrop, low dramatic light." \
  -s 2K -a 4:5 -o 911-card

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✔ Done. Total cost:"
nano-banana --costs || true
echo ""
echo "  Open index.html to see the result."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
