#!/usr/bin/env python3
"""Final definitive patch for all HTML files after images are downloaded."""
import re
from pathlib import Path

SITE_ROOT = Path(__file__).parent.parent
IMAGES = SITE_ROOT / "images"

def patch_file(html_path, replacements):
    """Apply {old: new} string replacements to an HTML file."""
    text = html_path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    if text != original:
        html_path.write_text(text, encoding="utf-8")
        n = sum(1 for o, n in replacements.items() if o != n and o in original)
        print(f"  ✎ {html_path.name} ({n} replacements)")
        return True
    else:
        print(f"  – {html_path.name} (no changes needed)")
        return False

def fix_index():
    """Ensure index.html hero + all 6 fleet cards use correct local images."""
    html = SITE_ROOT / "index.html"
    text = html.read_text(encoding="utf-8")

    # Fix sydney hero — replace any pollinations or wrong local path with correct one
    # The hero div has a multi-background with gradient, pollinations URL, SVG fallback
    # We need to replace the pollinations URL part
    old_sydney = re.search(r"url\('(https://image\.pollinations\.ai/prompt/cinematic%20Sydney[^']+)'\)", text)
    if old_sydney:
        text = text.replace(f"url('{old_sydney.group(1)}')", "url('images/sydney-hero.jpg')", 1)
        print(f"  ✓ Fixed Sydney hero → images/sydney-hero.jpg")

    # Fix each fleet card: ensure it shows the correct car image
    card_map = {
        'fleet/rolls-royce-spectre.html': 'images/spectre-hero.jpg',
        'fleet/aston-martin-db12.html':   'images/db12-hero.jpg',
        'fleet/mclaren-750s.html':        'images/750s-hero.jpg',
        'fleet/ferrari-purosangue.html':  'images/purosangue-card.jpg',
        'fleet/mercedes-g63.html':        'images/g63-hero.jpg',
        'fleet/porsche-911-gt3.html':     'images/911-hero.jpg',
    }

    for href, local_img in card_map.items():
        # Find the anchor with this href, then the car-photo div immediately after
        # Replace whatever URL is currently in that div (remote or wrong local)
        pattern = re.compile(
            r'(href="' + re.escape(href) + r'"[\s\S]{1,100}?'
            r'<div class="car-photo" style="background-image:url\(\')(.*?)(\'\))',
        )
        def make_replacer(img):
            def replacer(m):
                return m.group(1) + img + m.group(3)
            return replacer
        new_text = pattern.sub(make_replacer(local_img), text, count=1)
        if new_text != text:
            print(f"  ✓ Fleet card {href.split('/')[1].replace('.html','')} → {local_img}")
            text = new_text

    html.write_text(text, encoding="utf-8")
    print(f"  ✎ Saved index.html")


def fix_fleet_page(html_path, hero_local, gallery_locals):
    """Ensure a fleet page hero + gallery use local images."""
    text = html_path.read_text(encoding="utf-8")
    original = text

    # Fix hero: the three-fallback div
    hero_re = re.compile(
        r'(<div class="three-fallback" style="background-image:url\(\')(https://[^\']+)(\'\),)'
    )
    if hero_re.search(text):
        text = hero_re.sub(lambda m: m.group(1) + hero_local + m.group(3), text, count=1)
        print(f"  ✓ Hero → {hero_local}")

    # Fix gallery images (delay-1 through delay-4)
    gallery_re = re.compile(
        r'(<div class="reveal delay-\d+" style="aspect-ratio:4/3; background-image:url\(\')(https://[^\']+)(\'\))'
    )
    i = [0]
    def gallery_replacer(m):
        if i[0] < len(gallery_locals):
            result = m.group(1) + gallery_locals[i[0]] + m.group(3)
            i[0] += 1
            return result
        return m.group(0)
    text = gallery_re.sub(gallery_replacer, text)
    print(f"  ✓ Gallery ({i[0]} images)")

    if text != original:
        html_path.write_text(text, encoding="utf-8")
        print(f"  ✎ Saved {html_path.name}")
    else:
        print(f"  – {html_path.name} already patched")


FLEET_PAGES = [
    ("fleet/rolls-royce-spectre.html",  "spectre"),
    ("fleet/aston-martin-db12.html",    "db12"),
    ("fleet/mclaren-750s.html",         "750s"),
    ("fleet/ferrari-purosangue.html",   "purosangue"),
    ("fleet/mercedes-g63.html",         "g63"),
    ("fleet/porsche-911-gt3.html",      "911"),
]

def main():
    print("=== Fixing index.html ===")
    fix_index()

    print("\n=== Fixing fleet pages ===")
    for rel_path, slug in FLEET_PAGES:
        print(f"\n--- {rel_path} ---")
        html_path = SITE_ROOT / rel_path
        prefix = "../images/"
        hero = f"{prefix}{slug}-hero.jpg"
        gallery = [f"{prefix}{slug}-{n}.jpg" for n in range(1, 5)]
        fix_fleet_page(html_path, hero, gallery)

    print("\n=== Images in images/ ===")
    for f in sorted(IMAGES.glob("*.jpg")):
        print(f"  {f.name} ({f.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    main()
