# Drop your car photos here

This folder holds the photography for the Noctis site. The HTML references images by filename — drop files with the names below and they appear automatically. **If a filename is missing, the SVG car silhouette I drew for that car shows as a fallback, so the site always renders cleanly.**

## Required files (for the full experience)

| Filename                 | Where it appears            | Target size        |
| ------------------------ | --------------------------- | ------------------ |
| `sydney-hero.jpg`        | Homepage hero               | 2400 × 1400, landscape |
| `spectre-card.jpg`       | Homepage fleet card         | 1200 × 1500, portrait  |
| `db12-card.jpg`          | Homepage fleet card         | 1200 × 1500, portrait  |
| `750s-card.jpg`          | Homepage fleet card         | 1200 × 1500, portrait  |
| `purosangue-card.jpg`    | Homepage fleet card         | 1200 × 1500, portrait  |
| `g63-card.jpg`           | Homepage fleet card         | 1200 × 1500, portrait  |
| `911-card.jpg`           | Homepage fleet card         | 1200 × 1500, portrait  |
| `spectre-hero.jpg`       | Spectre detail page hero    | 2400 × 1400            |
| `spectre-1.jpg`…`-4.jpg` | Spectre gallery (4 images)  | 1600 × 1200            |
| `db12-hero.jpg` + `db12-1…4.jpg` | Aston DB12 page     | same                   |
| `750s-hero.jpg` + `750s-1…4.jpg` | McLaren 750S page   | same                   |
| `purosangue-hero.jpg` + `purosangue-1…4.jpg` | Ferrari | same                   |
| `g63-hero.jpg` + `g63-1…4.jpg`   | Mercedes G 63 page  | same                   |
| `911-hero.jpg` + `911-1…4.jpg`   | Porsche 911 GT3     | same                   |

**Minimum to make the site feel real:** just the homepage hero + 6 card photos + 6 detail-page heroes = 13 images. The galleries can stay on silhouette fallbacks if you're moving fast.

## Three ways to source photos

### Option A — Generate with Nano Banana 2 (recommended, $3 total)

This is the workflow the original `premium-website-builder` skill is built around. You own the output. Zero copyright risk. Costs ~$0.07/image on Gemini 3 Flash Image, ~$0.14 on Pro.

Install once:

```bash
git clone https://github.com/kingbootoshi/nano-banana-2-skill.git ~/tools/nano-banana-2
cd ~/tools/nano-banana-2 && bun install && bun link
mkdir -p ~/.nano-banana
echo "GEMINI_API_KEY=your_key_here" > ~/.nano-banana/.env
```

Get a Gemini key at https://aistudio.google.com/apikey.

Then for each car, run the prompts below. I wrote them to produce a **cohesive editorial set** — same lighting, same palette language, same cinematic register — so the final site feels curated.

#### Prompts (copy-paste)

**Homepage hero — Sydney harbour at dawn:**
```bash
nano-banana "Editorial cinematic photograph of Sydney Harbour at dawn, taken from an elevated viewpoint in Walsh Bay. Sydney Harbour Bridge silhouetted on the left, Opera House shells visible on the right, pre-dawn light on the water, muted blue and warm grey palette. No people, no branding, generous negative space in the upper third for text. Shot on medium format, 35mm equivalent, f/5.6." --model pro -s 4K -a 16:9 -o sydney-hero -d ~/Downloads
```

**Rolls-Royce Spectre (Arctic White):**
```bash
nano-banana "Editorial automotive photograph: a white Rolls-Royce Spectre 2025 coupe, three-quarter front view, parked on polished concrete in a minimalist dark gallery space. Single overhead softbox light, deep shadows beneath, crisp reflection on paintwork. Monochrome cool palette. No people, no signage, no other cars. Shot on medium format, 85mm equivalent, f/4." --model pro -s 2K -a 16:9 -o spectre-hero -d ~/Downloads

nano-banana "Rolls-Royce Spectre from directly behind, composed low and centered, dark moody warehouse backdrop, tail lights illuminated, everything else near-black, editorial calm" --model pro -s 2K -a 4:3 -o spectre-1 -d ~/Downloads

nano-banana "Detail shot of a Rolls-Royce Spectre's Pantheon grille and badge-less hood, shallow focus, dramatic directional light, black background" --model pro -s 2K -a 4:3 -o spectre-2 -d ~/Downloads

nano-banana "Rolls-Royce Spectre interior detail: starlight headliner with 4,796 fibre-optic points, crisp white leather seats, open-pore wood — shot with warm soft key light from camera left" --model pro -s 2K -a 4:3 -o spectre-3 -d ~/Downloads

nano-banana "Arctic White Rolls-Royce Spectre on a narrow coastal road at blue hour, long exposure hinting at a still car with moving clouds, editorial restraint, no other vehicles" --model pro -s 2K -a 4:3 -o spectre-4 -d ~/Downloads

nano-banana "Same Rolls-Royce Spectre, portrait-orientation three-quarter front composition for web fleet card, dark backdrop, vertical framing" --model pro -s 2K -a 4:5 -o spectre-card -d ~/Downloads
```

**Aston Martin DB12 Volante (Magnetic Silver):**
```bash
nano-banana "Editorial photograph of a Magnetic Silver 2024 Aston Martin DB12 Volante with the roof down, three-quarter profile, parked on a coastal road at golden hour in NSW. Cliff face and ocean softly defocused behind. Warm cream and deep bronze palette. No people, no badges visible." --model pro -s 2K -a 16:9 -o db12-hero -d ~/Downloads

nano-banana "Aston Martin DB12 Volante detail of front grille and iconic side strake vent, dramatic raking light, shallow focus" --model pro -s 2K -a 4:3 -o db12-1 -d ~/Downloads

nano-banana "Aston Martin DB12 roof-down cabin shot, obsidian black leather, brogue-stitched seats, chestnut accents, shot in soft natural light from camera right" --model pro -s 2K -a 4:3 -o db12-2 -d ~/Downloads

nano-banana "Aston Martin DB12 Volante three-quarter rear, roof down, parked in the Southern Highlands at late afternoon, restrained editorial photography" --model pro -s 2K -a 4:3 -o db12-3 -d ~/Downloads

nano-banana "Aston Martin DB12 wheel and tyre detail, machined finish, dark brake caliper, shot with low-angle light" --model pro -s 2K -a 4:3 -o db12-4 -d ~/Downloads

nano-banana "Aston Martin DB12 Volante, portrait-orientation hero composition for a fleet card, moody dark Sydney Walsh Bay warehouse backdrop" --model pro -s 2K -a 4:5 -o db12-card -d ~/Downloads
```

**McLaren 750S Spider (Volcano Orange):**
```bash
nano-banana "Editorial photograph of a Volcano Orange McLaren 750S Spider, low, three-quarter front view, roof retracted, parked in a modern industrial space with polished concrete floor. Dramatic single overhead light, shadows deep. Orange pops against cool grey surroundings. No people, no badges." --model pro -s 2K -a 16:9 -o 750s-hero -d ~/Downloads

nano-banana "McLaren 750S dihedral door open, shot from three-quarter front, carbon fibre sill visible, editorial monochrome with single orange accent" --model pro -s 2K -a 4:3 -o 750s-1 -d ~/Downloads

nano-banana "McLaren 750S cockpit detail: steering wheel, carbon-shell Super-Light seats in black Alcantara, orange stitching, shot with cool key light" --model pro -s 2K -a 4:3 -o 750s-2 -d ~/Downloads

nano-banana "McLaren 750S Spider rear three-quarter, low angle, showing rear buttresses and exhaust, pure matte black backdrop" --model pro -s 2K -a 4:3 -o 750s-3 -d ~/Downloads

nano-banana "Close-up detail of McLaren 750S side air intake and carbon ceramic brake disc, raking light, editorial still-life feel" --model pro -s 2K -a 4:3 -o 750s-4 -d ~/Downloads

nano-banana "Volcano Orange McLaren 750S Spider, portrait-orientation fleet card composition, roof retracted, editorial dark backdrop, dramatic overhead light" --model pro -s 2K -a 4:5 -o 750s-card -d ~/Downloads
```

**Ferrari Purosangue (Rosso Imola):**
```bash
nano-banana "Editorial automotive photograph: Rosso Imola Ferrari Purosangue four-door GT, three-quarter front, parked in a modern gallery. Deep red paintwork catches single overhead light. Cinematic composition, no people, no badges visible, generous negative space upper third." --model pro -s 2K -a 16:9 -o purosangue-hero -d ~/Downloads

nano-banana "Ferrari Purosangue rear-hinged 'welcome door' open at 79 degrees, interior visible — Iroko wood and cream leather, editorial still photography" --model pro -s 2K -a 4:3 -o purosangue-1 -d ~/Downloads

nano-banana "Close-up of Ferrari Purosangue engine bay — 6.5L V12 mounted mid-front, red crackle paint cover, polished manifolds, dramatic warehouse lighting" --model pro -s 2K -a 4:3 -o purosangue-2 -d ~/Downloads

nano-banana "Ferrari Purosangue rear three-quarter on a winding road at blue hour, Southern Highlands Australia, subtle motion blur on surrounding landscape, car pin-sharp" --model pro -s 2K -a 4:3 -o purosangue-3 -d ~/Downloads

nano-banana "Detail of Ferrari Purosangue instrument cluster and steering wheel, black Alcantara, yellow Cavallino, dramatic side lighting" --model pro -s 2K -a 4:3 -o purosangue-4 -d ~/Downloads

nano-banana "Rosso Imola Ferrari Purosangue, vertical portrait composition for fleet card, three-quarter front view, dark backdrop, dramatic overhead light, mood of controlled ferocity" --model pro -s 2K -a 4:5 -o purosangue-card -d ~/Downloads
```

**Mercedes-AMG G 63 (Obsidian Black):**
```bash
nano-banana "Editorial photograph of an Obsidian Black Metallic 2024 Mercedes-AMG G 63, three-quarter front view, parked outside a restored warehouse in Paddington Sydney. Boxy silhouette pin-sharp, reflections from single overhead streetlight. Warm late afternoon, cream palette. No people, no badges." --model pro -s 2K -a 16:9 -o g63-hero -d ~/Downloads

nano-banana "Mercedes-AMG G 63 from directly front on, slat grille face-on, headlights off, moody low-key lighting" --model pro -s 2K -a 4:3 -o g63-1 -d ~/Downloads

nano-banana "Detail of Mercedes G 63 external door hinges and indicator pillar, chrome, macro focus" --model pro -s 2K -a 4:3 -o g63-2 -d ~/Downloads

nano-banana "Mercedes G 63 cabin shot — Macchiato Beige Nappa leather, physical metal switches, sidekick dashboard, shot with soft window light" --model pro -s 2K -a 4:3 -o g63-3 -d ~/Downloads

nano-banana "Mercedes G 63 rear view with spare wheel cover, elegant restraint, dark cool palette" --model pro -s 2K -a 4:3 -o g63-4 -d ~/Downloads

nano-banana "Obsidian Black Mercedes-AMG G 63, portrait-orientation fleet card composition, three-quarter front view, dark Walsh Bay backdrop, single overhead key light" --model pro -s 2K -a 4:5 -o g63-card -d ~/Downloads
```

**Porsche 911 GT3 Touring (Python Green):**
```bash
nano-banana "Editorial automotive photograph: Python Green 2024 Porsche 911 GT3 Touring, three-quarter profile, parked on a quiet mountain road at dawn. Pronounced rear haunches, no rear wing. Soft morning light, cool palette of greens and greys. No people, no badges visible." --model pro -s 2K -a 16:9 -o 911-hero -d ~/Downloads

nano-banana "Porsche 911 GT3 Touring cabin shot emphasising the manual gear lever and GT silver-stitched Alcantara seats, shot with soft natural light from camera left" --model pro -s 2K -a 4:3 -o 911-1 -d ~/Downloads

nano-banana "Porsche 911 GT3 Touring rear view showing center-exit exhaust and subtle rear lip, dramatic low-angle editorial photography" --model pro -s 2K -a 4:3 -o 911-2 -d ~/Downloads

nano-banana "Close-up detail of Porsche 911 GT3 front fender and centre-lock wheel, raking light, focus on the geometry" --model pro -s 2K -a 4:3 -o 911-3 -d ~/Downloads

nano-banana "Python Green Porsche 911 GT3 Touring on the Putty Road at golden hour, Australian bush landscape softly defocused behind, editorial restraint" --model pro -s 2K -a 4:3 -o 911-4 -d ~/Downloads

nano-banana "Python Green Porsche 911 GT3 Touring, vertical portrait composition for fleet card, moody concrete-floored Walsh Bay warehouse backdrop, low dramatic light" --model pro -s 2K -a 4:5 -o 911-card -d ~/Downloads
```

After each batch finishes, the `.png` files land in your Downloads folder. Move them into this `images/` folder (converting to `.jpg` if you want smaller files — use any image tool or Preview's Export).

Total spend: 37 images × ~$0.10 = **~$3.70** on Gemini Pro. Flash (~$0.067/image) would be closer to $2.50.

---

### Option B — Wikimedia Commons (free, legally clean)

Go to https://commons.wikimedia.org and search each car model (e.g. "Rolls-Royce Spectre", "Porsche 911 GT3 Touring"). Filter by license — **CC BY**, **CC BY-SA**, or **public domain** are safe for commercial use with attribution.

1. Click a photo you like
2. Right-click the full-resolution image → "Save As"
3. Rename to match the filenames in the table above
4. Drop in this folder

**Attribution requirement:** CC-licensed photos need credit. Add a small line in the page footer or a dedicated `credits.html` naming each photographer + license. The site already has a footer — easy to add.

---

### Option C — Licensed stock

- **Unsplash / Pexels** (free, but selection on specific luxury cars is thin)
- **Getty / Shutterstock** (paid, pro quality, full legal coverage — budget ~$500 for a 6-car set)
- **Motorpress / magazine archives** (editorial licensing, usually by email request)

Most professional agencies use a mix: one commissioned shoot for the hero, Getty for filler, AI for details. For a $10k client project, factor $500–$1,500 into the budget for photography licensing.

---

## Don't use manufacturer press photos without permission

Porsche, Rolls-Royce, Ferrari, McLaren, Mercedes, and Aston Martin all own their media library and ban reuse outside authorized dealer/editorial contexts. Those images show up beautifully on your portfolio but invite a takedown notice — or worse — the day the site is indexed by search engines. For paying clients, this is not a risk worth carrying.

If a client genuinely wants manufacturer photography, they need to apply for authorized reseller/retailer status with that brand — which unlocks the press library legally. Until then, generate your own or license stock.
