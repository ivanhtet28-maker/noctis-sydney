#!/usr/bin/env python3
"""
Generate Noctis site images using Google Imagen 4 via AI Studio.

Usage:
  pip install google-genai
  GOOGLE_API_KEY=your_key_here python3 scripts/generate-images-imagen.py

Images are saved to images/ and overwrite the existing pollinations.ai versions.
Each car gets: hero, 1, 2, 3, 4 (5 images × 6 cars + 1 Sydney hero = 31 total).

Imagen 4 produces photorealistic CGI-quality renders — far superior to pollinations.
"""

import os, sys, time
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    sys.exit("Run: pip install google-genai")

API_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not API_KEY:
    sys.exit("Set GOOGLE_API_KEY environment variable first.\n"
             "Get one at: https://aistudio.google.com/apikey")

client = genai.Client(api_key=API_KEY)
IMAGES = Path(__file__).parent.parent / "images"
IMAGES.mkdir(exist_ok=True)

# ── Base style suffix appended to every prompt ──────────────────────────────
STYLE = (
    "photorealistic automotive CGI render, dramatic studio lighting, "
    "deep black background, reflective dark floor, volumetric rim light, "
    "ultra-sharp detail, no people, no text, no watermarks, "
    "luxury car brand aesthetic, editorial quality"
)

# ── Per-car prompt sets ──────────────────────────────────────────────────────
CARS = {
    "spectre": {
        "color": "Silver Enigma metallic",
        "hero":  "Rolls-Royce Spectre electric coupe, Silver Enigma paint, front three-quarter view, stately and imposing, Pantheon grille gleaming, low camera angle",
        "shots": [
            "Rolls-Royce Spectre, rear three-quarter view, sweeping fastback roofline, taillights illuminated",
            "Rolls-Royce Spectre interior, starlight headliner glowing, champagne leather, Spirit of Ecstasy on dash",
            "Rolls-Royce Spectre wheel detail, 22-inch forged alloy, brake caliper, tyre sidewall",
            "Rolls-Royce Spectre, side profile, full length, silver paint with subtle pinstripe reflection",
        ],
    },
    "db12": {
        "color": "Satin Iridescent Emerald",
        "hero":  "Aston Martin DB12 grand tourer, Iridescent Emerald green, front three-quarter view, bonnet vents prominent, predatory stance",
        "shots": [
            "Aston Martin DB12, rear view, quad exhaust tips, LED taillights, perfect symmetry",
            "Aston Martin DB12 interior, Bridge of Weir leather, carbon fibre console, analogue clock",
            "Aston Martin DB12 side strake detail, chrome vane, green paint depth",
            "Aston Martin DB12, side profile, long bonnet, fastback roofline, emerald green",
        ],
    },
    "750s": {
        "color": "McLaren Orange",
        "hero":  "McLaren 750S Spider, Papaya Orange, front three-quarter view, dihedral doors closed, aggressive aerodynamics",
        "shots": [
            "McLaren 750S Spider, rear view, active rear wing deployed, central exhaust, orange",
            "McLaren 750S cockpit, Alcantara steering wheel, race-inspired seat, portrait display",
            "McLaren 750S engine bay, twin-turbo V8 detail, carbon fibre covers",
            "McLaren 750S, side profile, ultra-low stance, Papaya Orange",
        ],
    },
    "purosangue": {
        "color": "Rosso Portofino",
        "hero":  "Ferrari Purosangue SUV, Rosso Portofino red, front three-quarter view, four-door, muscular haunches, Prancing Horse badge",
        "shots": [
            "Ferrari Purosangue, rear three-quarter view, active spoiler, dual exhaust, red",
            "Ferrari Purosangue interior, Frau leather, Cavallino stitching, dual-screen cockpit",
            "Ferrari Purosangue wheel detail, 22-inch forged wheel, yellow brake caliper, red paint",
            "Ferrari Purosangue, side profile, fastback roofline, long bonnet, Rosso Portofino",
        ],
    },
    "g63": {
        "color": "Obsidian Black",
        "hero":  "Mercedes-AMG G 63, Obsidian Black, front three-quarter view, boxy iconic silhouette, spare wheel on rear, round headlights",
        "shots": [
            "Mercedes-AMG G 63, rear view, spare wheel cover, AMG badge, black",
            "Mercedes-AMG G 63 interior, Nappa leather, AMG Performance steering wheel, digital dashboard",
            "Mercedes-AMG G 63 door hinge detail, external hinges, Obsidian Black paint",
            "Mercedes-AMG G 63, side profile, full length, boxy upright greenhouse, G-Wagon silhouette",
        ],
    },
    "911": {
        "color": "Python Green",
        "hero":  "Porsche 911 GT3 Touring, Python Green, front three-quarter view, naturally aspirated flat-six, rear wing delete touring spec",
        "shots": [
            "Porsche 911 GT3 Touring, rear view, center-exit exhaust, Python Green, round taillights",
            "Porsche 911 GT3 interior, bucket seats, roll cage hints, GT3 steering wheel, Touring spec",
            "Porsche 911 GT3 flat-six engine, 4.0L naturally aspirated, carbon fibre engine cover",
            "Porsche 911 GT3 Touring, side profile, classic 911 silhouette, Python Green",
        ],
    },
}

SYDNEY_HERO = (
    "Cinematic aerial night view of Sydney Harbour, Opera House shells glowing, "
    "Harbour Bridge illuminated, dark water reflections, city lights, "
    "dramatic moody luxury editorial photography, no people, no text"
)


FORCE = "--force" in sys.argv or "-f" in sys.argv


def generate(prompt: str, dest: Path, aspect: str = "16:9") -> bool:
    if dest.exists() and not FORCE:
        print(f"    skip {dest.name} (exists — use --force to regenerate)")
        return True
    full_prompt = f"{prompt}, {STYLE}"
    print(f"    generating {dest.name} ...", flush=True)
    for attempt in range(4):
        try:
            resp = client.models.generate_images(
                model="imagen-4.0-generate-001",
                prompt=full_prompt,
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio=aspect,
                    safety_filter_level="block_low_and_above",
                    person_generation="dont_allow",
                ),
            )
            img_data = resp.generated_images[0].image.image_bytes
            dest.write_bytes(img_data)
            print(f"    ✓ {dest.name} ({len(img_data)//1024} KB)")
            return True
        except Exception as e:
            msg = str(e)
            if "429" in msg or "quota" in msg.lower() or "rate" in msg.lower():
                wait = 15 * (attempt + 1)
                print(f"    rate-limited, waiting {wait}s ...")
                time.sleep(wait)
            else:
                print(f"    ✗ {dest.name}: {e}")
                return False
    print(f"    ✗ gave up after 4 attempts")
    return False


def main():
    total = 0
    failed = []

    print("\n── Sydney hero ─────────────────────────────")
    ok = generate(SYDNEY_HERO, IMAGES / "sydney-hero.jpg", aspect="16:9")
    if not ok: failed.append("sydney-hero.jpg")
    total += 1
    time.sleep(3)

    for slug, car in CARS.items():
        print(f"\n── {slug} ────────────────────────────────────")

        ok = generate(car["hero"], IMAGES / f"{slug}-hero.jpg", aspect="16:9")
        if not ok: failed.append(f"{slug}-hero.jpg")
        total += 1
        time.sleep(3)

        for i, shot in enumerate(car["shots"], 1):
            ok = generate(shot, IMAGES / f"{slug}-{i}.jpg", aspect="4:3")
            if not ok: failed.append(f"{slug}-{i}.jpg")
            total += 1
            time.sleep(3)

    print(f"\n── Done: {total - len(failed)}/{total} generated ──")
    if failed:
        print(f"Failed: {', '.join(failed)}")
    else:
        print("All images generated successfully.")
        print("\nTip: the card images (spectre-card.jpg etc.) on the homepage")
        print("still use the old files. Re-run with --cards to regenerate those,")
        print("or they'll auto-use the hero images which already look great.")


if __name__ == "__main__":
    main()
