#!/usr/bin/env python3
"""
Fix index.html fleet card images: replace the shifted pollinations.ai URLs
and the wrong spectre-card/db12-card/etc filenames with the correct hero
images that were downloaded per car (spectre-hero.jpg, db12-hero.jpg, etc).
Also downloads the missing 911-card.jpg with correct Porsche prompt.
"""
import re
import time
import urllib.request
import urllib.error
from pathlib import Path

SITE_ROOT = Path(__file__).parent.parent
INDEX = SITE_ROOT / "index.html"
IMAGES = SITE_ROOT / "images"

# Correct local-path replacements for each fleet card (uses hero images for now)
CARD_FIXES = {
    # find this substring in the car-photo div for each card
    "fleet/rolls-royce-spectre.html": "images/spectre-hero.jpg",
    "fleet/aston-martin-db12.html":   "images/db12-hero.jpg",
    "fleet/mclaren-750s.html":        "images/750s-hero.jpg",
    # ferrari-purosangue is already patched correctly, skip
    "fleet/mercedes-g63.html":        "images/g63-hero.jpg",
    "fleet/porsche-911-gt3.html":     "images/911-hero.jpg",
}

CARD_DIV_RE = re.compile(
    r'(<a href="(fleet/[^"]+)"[^>]*>)\s*'
    r'(<div class="car-photo" style="background-image:url\(\'[^\']+\'\))'
)

def fix_index():
    text = INDEX.read_text(encoding="utf-8")
    original = text

    # For each fleet URL link, find the car-photo div on the next line and update its src
    # We do a simple replacement by finding the exact pollinations.ai URL or wrong local path
    # for each card based on which car it links to.

    # Pattern: the car-photo div immediately follows the <a href="fleet/..."> tag
    # We'll find each block and replace the background-image URL

    for href, local_img in CARD_FIXES.items():
        # Find the car-photo div that comes right after the <a href="<href>"...> anchor
        # The car-photo div may currently have a pollinations.ai URL or a wrong local path
        pattern = re.compile(
            r'(href="' + re.escape(href) + r'"[^>]*>)\s*'
            r'(<div class="car-photo" style="background-image:url\(\')(https://[^\']+|images/[^\']+)(\'\)'
            r'[^>]*>)',
            re.DOTALL
        )

        def replacer(m):
            return m.group(1) + '\n        <div class="car-photo" style="background-image:url(\'' + local_img + '\')' + m.group(4)[m.group(4).find("'"):]

        new_text = pattern.sub(replacer, text)
        if new_text != text:
            print(f"  ✓ Fixed {href} → {local_img}")
            text = new_text
        else:
            # Try simpler approach: just replace the URL inside the car-photo for this anchor
            # Find the anchor block
            anchor_re = re.compile(
                r'(href="' + re.escape(href) + r'"[^>]*>[\s\S]{1,50}?'
                r'<div class="car-photo" style="background-image:url\(\')(https://[^\']+|images/[^\']+)(\'\))',
            )
            new_text2 = anchor_re.sub(lambda m: m.group(1) + local_img + m.group(3), text)
            if new_text2 != text:
                print(f"  ✓ Fixed (v2) {href} → {local_img}")
                text = new_text2
            else:
                print(f"  ✗ Could not fix {href} (pattern not matched)")

    if text != original:
        INDEX.write_text(text, encoding="utf-8")
        print(f"\n  ✎ Saved index.html")
    else:
        print(f"\n  ⚠ index.html unchanged — patterns may not have matched")


def download_missing(url, path, retries=4):
    if path.exists():
        print(f"  ✓ skip {path.name} (exists)")
        return True
    print(f"  ↓ {path.name} …", flush=True)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
            path.write_bytes(data)
            print(f"  ✓ {path.name} ({len(data)//1024} KB)")
            return True
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 8 * (attempt + 1)
                print(f"  ⏳ rate-limited, waiting {wait}s …")
                time.sleep(wait)
            else:
                print(f"  ✗ {path.name}: HTTP {e.code}")
                return False
    return False


if __name__ == "__main__":
    # Download 911-card.jpg with correct Porsche prompt
    print("Downloading missing 911-card.jpg …")
    porsche_url = (
        "https://image.pollinations.ai/prompt/"
        "Python%20Green%20Porsche%20911%20GT3%20Touring%2C%20vertical%20portrait%20composition%2C%20"
        "moody%20concrete-floored%20warehouse%20backdrop%2C%20low%20dramatic%20light%2C%20"
        "editorial%20cinematic%20automotive%20photography%2C%20muted%20premium%20palette%2C%20"
        "single%20dramatic%20overhead%20light%2C%20shallow%20depth%20of%20field%2C%20no%20people%2C%20"
        "no%20text%2C%20no%20badges%2C%20generous%20negative%20space%2C%20luxury%20brand%20aesthetic"
        "?width=1200&height=1500&model=flux&nologo=true&enhance=true"
    )
    download_missing(porsche_url, IMAGES / "911-card.jpg")

    print("\nFixing index.html fleet card images …\n")
    fix_index()

    print("\nDone.")
