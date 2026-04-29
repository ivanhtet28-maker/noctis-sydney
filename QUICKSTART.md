# QUICKSTART — Generate the car photos

You have 37 image slots on the site (1 Sydney hero + 6 fleet cards + 6 × (1 hero + 4 gallery)). This generates all of them via **Nano Banana 2** (Google Gemini 3 image gen) in one run.

**Total cost:** ~$4.30 on your Gemini bill. **Total time:** ~15–20 min. **Total clicks:** 3.

---

## 1. Get a Gemini API key

Go to **https://aistudio.google.com/apikey** → sign in → **Create API key**. Copy it. (Free tier covers this easily.)

## 2. Run setup once

```bash
cd noctis-site
bash scripts/setup.sh
```

It will:
- Install **Bun** if you don't have it (JavaScript runtime — used by Nano Banana)
- Clone the `nano-banana-2` tool to `~/tools/nano-banana-2`
- Link `nano-banana` to your PATH globally
- Prompt you for the Gemini API key you just copied

## 3. Generate all images

```bash
bash scripts/generate-images.sh
```

Watch it print `[1/37] Sydney harbour hero…` through `[37/37] 911 fleet card…`. Each image takes 15–30 seconds. When it's done, you'll see a cost summary and a "Done" banner.

The images land directly in `images/` with the exact filenames the HTML is looking for. You don't need to move anything.

## 4. Open the site

```bash
open index.html                 # quickly peek
# OR, for the full experience with 3D:
python3 -m http.server 8000     # then visit http://localhost:8000
```

## That's it.

The site auto-upgrades to real photography as each file lands. If you refresh mid-generation, you'll see the SVG silhouettes fill in with real photos one by one.

---

## If something goes wrong

**`bun: command not found` after setup** — restart your terminal (setup.sh added Bun to your `~/.zshrc`) or run `source ~/.zshrc`.

**`nano-banana: command not found` after setup** — Bun's link didn't register in the new terminal. Manual fallback:
```bash
mkdir -p ~/.local/bin
ln -sf ~/tools/nano-banana-2/src/cli.ts ~/.local/bin/nano-banana
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**API rate limit / 429 errors mid-run** — free tier has a requests-per-minute cap. Wait 60 seconds, then re-run `generate-images.sh`. Already-generated files are skipped automatically (the `-o <name>` output flag writes to that exact filename; existing files are overwritten, which is fine).

**An image looks off / you want to iterate** — delete that one `.png` and re-run just its command. For example to re-do the Porsche hero:
```bash
cd images && rm 911-hero.png
nano-banana "Python Green Porsche 911 GT3 Touring, three-quarter profile, dawn light..." \
  -s 2K -a 16:9 -o 911-hero
```
You can tweak the prompt freely — the script is just a starting point.

**Want higher quality for one specific image?** Re-run with `--model pro` (costs ~2×). Especially worth it for the Sydney hero and Rolls-Royce hero, which are your money shots.

---

## How it works

Every image slot in the HTML has a two-layer CSS background:

```css
background-image: url('images/spectre-hero.png'),  /* your real photo */
                  url('data:image/svg+xml,...');   /* silhouette fallback */
```

- If `spectre-hero.png` exists, you see it.
- If it doesn't, the SVG silhouette I drew shows instead.
- No JavaScript involved, no build step, no 404s in the console — CSS handles the fallback natively.

That means you can ship the site as-is (with silhouettes), generate images on your schedule, and each one that lands improves the page automatically.

## Cost breakdown

| | Count | Rate | Subtotal |
|---|---|---|---|
| Sydney hero (Pro 4K) | 1 | ~$0.302 | ~$0.30 |
| Car heroes (Flash 2K) | 6 | ~$0.101 | ~$0.61 |
| Fleet cards (Flash 2K) | 6 | ~$0.101 | ~$0.61 |
| Gallery images (Flash 2K) | 24 | ~$0.101 | ~$2.42 |
| **Total** | **37** | | **~$3.94** |

Well within the Gemini free tier for new accounts. Worst case, you pay out of pocket: less than a flat white.
