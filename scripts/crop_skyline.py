#!/usr/bin/env python3
"""Crop the top portion off each Forza image to remove Miami skyline."""
from PIL import Image
from pathlib import Path

ROOT = Path(__file__).parent.parent
IMAGES = ROOT / "images"

# Per-slug crop strategy. Values are fraction of original height to remove from TOP.
# More aggressive crop hides more skyline; too aggressive cuts the car's roof.
CROP_TOP = {
    "spectre":    0.42,  # Cullinan — tall SUV, skyline behind, can crop hard
    "db12":       0.38,  # Bentley GTC — convertible, skyline behind
    "750s":       0.38,  # McLaren GT — low car, lots of skyline
    "purosangue": 0.38,  # F8 Spider — low car
    "g63":        0.30,  # G-Wagon — tall vehicle, less aggressive
    "911":        0.40,  # 911 GT3 — low car
}


def crop_image(path: Path, top_frac: float) -> tuple[int, int]:
    img = Image.open(path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    crop_pixels = int(h * top_frac)
    cropped = img.crop((0, crop_pixels, w, h))
    cropped.save(path, "JPEG", quality=88, optimize=True)
    return cropped.size


def main():
    suffixes = ["card", "hero", "1", "2", "3", "4"]
    total = 0
    for slug, top_frac in CROP_TOP.items():
        for suf in suffixes:
            path = IMAGES / f"{slug}-{suf}.jpg"
            if not path.exists():
                print(f"  - skip {path.name} (missing)")
                continue
            try:
                size = crop_image(path, top_frac)
                print(f"  ✓ {path.name} → {size[0]}x{size[1]}")
                total += 1
            except Exception as e:
                print(f"  ✗ {path.name}: {e}")
    print(f"\nCropped {total} images.")


if __name__ == "__main__":
    main()
