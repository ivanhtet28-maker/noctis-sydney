#!/usr/bin/env python3
"""
Re-crop the already-skyline-cropped Forza images so the car sits in the
center vertically. This lets us use `background-position: center` everywhere
(desktop + mobile) without losing the car.

Strategy: crop the bottom 12-22% off (mostly empty asphalt) AND another
3-12% off the top (any residual building peaks). Per-car tuned because
SUVs and coupes have different visual weight.
"""
from PIL import Image
from pathlib import Path

ROOT = Path(__file__).parent.parent
IMAGES = ROOT / "images"

# (top_extra, bottom) — fractions of CURRENT (already-cropped) image height
# to crop further. Tuned by eyeballing each car's composition.
PLAN = {
    "spectre":    {"top": 0.04, "bottom": 0.18},  # Cullinan SUV — tall
    "db12":       {"top": 0.06, "bottom": 0.16},  # GTC convertible — low cabin
    "750s":       {"top": 0.05, "bottom": 0.16},  # McLaren GT
    "purosangue": {"top": 0.04, "bottom": 0.17},  # Ferrari F8 Spider
    "g63":        {"top": 0.02, "bottom": 0.20},  # G63 — tallest, plenty of asphalt
    "911":        {"top": 0.05, "bottom": 0.16},  # 911 GT3
}

SUFFIXES = ["card", "hero", "1", "2", "3", "4"]


def main():
    cropped = 0
    for slug, p in PLAN.items():
        for suf in SUFFIXES:
            path = IMAGES / f"{slug}-{suf}.jpg"
            if not path.exists():
                print(f"  - skip {path.name} (missing)")
                continue
            try:
                img = Image.open(path)
                if img.mode != "RGB":
                    img = img.convert("RGB")
                w, h = img.size
                top = int(h * p["top"])
                bot = int(h * (1 - p["bottom"]))
                if bot - top < h * 0.4:
                    print(f"  ⚠ {path.name}: skipping (would crop too much)")
                    continue
                cropped_img = img.crop((0, top, w, bot))
                cropped_img.save(path, "JPEG", quality=88, optimize=True)
                print(f"  ✓ {path.name}  {w}x{h} → {cropped_img.size[0]}x{cropped_img.size[1]}")
                cropped += 1
            except Exception as e:
                print(f"  ✗ {path.name}: {e}")
    print(f"\nRe-cropped {cropped} images.")


if __name__ == "__main__":
    main()
